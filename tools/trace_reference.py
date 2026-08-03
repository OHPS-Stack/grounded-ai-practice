#!/usr/bin/env python3
"""Turn a flat raster reference into an editable, colour-separated SVG.

Why this exists
---------------
Concept work happens in raster tools (Ideogram, ChatGPT/DALL-E, Midjourney).
Refinement happens by hand in Inkscape. This script is the bridge between them:
it converts a flat, limited-colour reference PNG into a labelled SVG with
brand-exact fills, so hand refinement starts from real traced geometry instead
of a redraw from visual reference.

It does NOT produce a finished asset. A trace faithfully reproduces its source,
including the irregularities of an AI-generated raster: "straight" edges that
wobble, corner radii that vary, near-but-not-quite symmetry. Correcting those is
the hand-editing step that follows. See CLAUDE.md, "Raster concept to editable
vector", for where this sits in the workflow.

The window
----------
Run with no arguments (or --gui) and a small window opens instead of the
command line: pick the reference image, check where the SVG will go, choose
how many colours to find and whether to snap them to the GAP palette, then
"Detect colours" to preview the separation and "Trace" to run it. The window
drives exactly the same functions as the command line; the finer controls
(explicit colours and labels, corner smoothing, speckle threshold) stay
command-line on purpose.

How it works
------------
1. Reads the reference and identifies its background colour.
2. Determines target colours, either auto-detected by median-cut quantisation
   or supplied explicitly with --colors.
3. Assigns every pixel to its nearest target colour and emits one 1-bit mask per
   colour. Nearest-colour assignment means anti-aliased edge pixels fall to
   whichever side they are closer to rather than being dropped, which is what
   keeps traced edges clean.
4. Traces each mask through Inkscape's object-trace action (potrace underneath),
   which emits smooth beziers rather than polygon approximations.
5. Assembles the paths into one SVG with snake_case group ids and
   inkscape:label attributes, per this project's SVG naming convention.
6. Renders the result back to PNG as a self-check, so the output can be compared
   against the reference by eye rather than assumed correct.

Requirements
------------
Python 3.9+ with Pillow     pip install pillow
Inkscape 1.x                https://inkscape.org

Both are found automatically on standard install paths; pass --inkscape to
override. If either is missing the script says so and stops rather than falling
back to a lower-quality method. The window needs tkinter, which ships with
Python on Windows.

Examples
--------
Auto-detect two colours and snap them to the brand palette:

    python tools/trace_reference.py ref.png out.svg --snap

Specify colours and group names explicitly:

    python tools/trace_reference.py ref.png out.svg \\
        --colors "#27221E,#F15E4B" --labels "letterforms_ink,crossbar_ember"
"""

from __future__ import annotations

import argparse
import os
import queue
import re
import shutil
import subprocess
import sys
import tempfile
import threading

try:
    from PIL import Image
except ImportError:
    sys.exit(
        "Pillow is not installed. This script needs it for colour separation.\n"
        "  pip install pillow"
    )

try:
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk
    TK_OK = True
except ImportError:  # rare stripped-down Python; the CLI still works
    TK_OK = False

# Grounded AI Practice palette. See project_brief.md, "Visual identity".
BRAND = {
    "ink": "#27221E",
    "ember": "#F15E4B",
    "sand": "#F9E8DC",
    "paper": "#F9F9F9",
    "mist": "#EFEEED",
    "sage": "#D5E2E1",
    "stone": "#6E6E6E",
    "graphite": "#404040",
}

# The window uses the same palette in the roles project_brief.md records;
# only EMBER_DEEP is derived (Ember darkened for hover/pressed states).
INK, EMBER, PAPER = BRAND["ink"], BRAND["ember"], BRAND["paper"]
MIST, SAND, STONE = BRAND["mist"], BRAND["sand"], BRAND["stone"]
EMBER_DEEP = "#D94C3B"

DITHER_NONE = getattr(getattr(Image, "Dither", Image), "NONE")

INKSCAPE_CANDIDATES = [
    r"C:\Program Files\Inkscape\bin\inkscape.exe",
    r"C:\Program Files (x86)\Inkscape\bin\inkscape.exe",
    "/Applications/Inkscape.app/Contents/MacOS/inkscape",
    "/usr/bin/inkscape",
    "/usr/local/bin/inkscape",
]


class TraceError(Exception):
    """A pipeline failure with a plain-language message."""


def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.strip().lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def rgb_to_hex(c) -> str:
    return "#{:02X}{:02X}{:02X}".format(*c)


def distance(a, b) -> int:
    """Squared RGB distance. Adequate for flat art with well-separated colours."""
    return sum((x - y) ** 2 for x, y in zip(a, b))


def find_inkscape(override: str | None) -> str:
    if override:
        if not os.path.exists(override) and not shutil.which(override):
            sys.exit(f"Inkscape not found at: {override}")
        return override
    found = shutil.which("inkscape")
    if found:
        return found
    for path in INKSCAPE_CANDIDATES:
        if os.path.exists(path):
            return path
    sys.exit(
        "Inkscape was not found. It does the actual tracing, so there is no\n"
        "sensible fallback. Install it from https://inkscape.org, or pass the\n"
        "executable path with --inkscape."
    )


SEPARATION = 3000   # squared RGB, roughly 55 per channel
MIN_SHARE = 0.002   # ignore anything under 0.2% of the image
BLEND_TOLERANCE = 26  # plain RGB distance from an anti-aliasing ramp


def blend_distance(colour, start, end) -> float:
    """Distance from `colour` to the straight line between two other colours.

    Anti-aliased edges produce a continuous ramp of intermediate colours between
    the background and each real colour. Those intermediates can be numerous
    enough to look like colours in their own right, so they are identified
    geometrically -- by sitting on the line between two colours already known --
    rather than by any pixel-count threshold, which they can pass.
    """
    ax, ay, az = start
    dx, dy, dz = (end[0] - ax, end[1] - ay, end[2] - az)
    denominator = dx * dx + dy * dy + dz * dz
    if denominator == 0:
        return distance(colour, start) ** 0.5
    t = ((colour[0] - ax) * dx + (colour[1] - ay) * dy + (colour[2] - az) * dz) / denominator
    t = max(0.0, min(1.0, t))
    nearest = (ax + t * dx, ay + t * dy, az + t * dz)
    return sum((c - n) ** 2 for c, n in zip(colour, nearest)) ** 0.5


def detect_colours(im: Image.Image, count: int, background):
    """Find the `count` most significant colours that are not the background.

    Quantises generously rather than to `count` colours: a reference that is
    mostly background will otherwise spend its whole palette on background
    variations and miss small accent elements entirely.
    """
    quantised = im.quantize(colors=64, method=Image.Quantize.MEDIANCUT)
    palette = quantised.getpalette() or []
    total = im.size[0] * im.size[1]
    tally = sorted(quantised.getcolors(maxcolors=256) or [], reverse=True)

    picked = []
    for pixels, index in tally:
        if pixels / total < MIN_SHARE:
            continue
        rgb = tuple(palette[index * 3:index * 3 + 3])
        if distance(rgb, background) < SEPARATION:
            continue
        if any(distance(rgb, chosen) < SEPARATION for chosen in picked):
            continue
        # Reject ramps between the background and anything already accepted.
        if any(blend_distance(rgb, background, chosen) < BLEND_TOLERANCE
               for chosen in picked):
            continue
        picked.append(rgb)
        if len(picked) == count:
            break
    return picked


def resolve_palette(image: Image.Image, colors=None, count=2, snap=False,
                    background=None, log=print):
    """Settle the background and target colours for one reference image."""
    if background:
        bg = hex_to_rgb(background)
    else:
        bg = max(image.getcolors(image.size[0] * image.size[1]) or [],
                 key=lambda t: t[0])[1]
    log(f"background: {rgb_to_hex(bg)}")

    if colors:
        targets = [hex_to_rgb(c) for c in colors.split(",")]
    else:
        targets = detect_colours(image, count, bg)
        if not targets:
            raise TraceError("No colours found distinct from the background.")
        if snap:
            snapped = []
            for colour in targets:
                name = min(BRAND, key=lambda k: distance(colour, hex_to_rgb(BRAND[k])))
                log(f"  snap {rgb_to_hex(colour)} -> {BRAND[name]} ({name})")
                snapped.append(hex_to_rgb(BRAND[name]))
            targets = snapped
    log("colours   : " + ", ".join(rgb_to_hex(c) for c in targets))
    return bg, targets


def build_masks(im: Image.Image, targets, background, folder: str):
    """Emit one black-shape-on-white mask per target colour."""
    palette_image = Image.new("P", (1, 1))
    flat: list[int] = []
    for colour in [background, *targets]:
        flat.extend(colour)
    flat.extend([0, 0, 0] * (256 - len(targets) - 1))
    palette_image.putpalette(flat)

    assigned = im.quantize(palette=palette_image, dither=DITHER_NONE)

    masks = []
    for position, _ in enumerate(targets, start=1):
        lut = [0 if i == position else 255 for i in range(256)]  # shape black
        mask = assigned.point(lut, mode="L").convert("1")
        path = os.path.join(folder, f"mask_{position}.png")
        mask.save(path)
        masks.append((path, mask.histogram()[0]))  # index 0 == the black shape
    return masks


def trace(inkscape: str, mask_path: str, size, speckles: int,
          smooth_corners: float, optimize: float) -> str | None:
    """Trace one mask and return its path data, or None if nothing was found."""
    folder = os.path.dirname(mask_path)
    stem = os.path.splitext(os.path.basename(mask_path))[0]
    wrapper = os.path.join(folder, f"wrap_{stem}.svg")
    traced = os.path.join(folder, f"traced_{stem}.svg")
    width, height = size

    with open(wrapper, "w", encoding="utf8") as handle:
        handle.write(
            '<svg xmlns="http://www.w3.org/2000/svg" '
            'xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
            f'<image xlink:href="{os.path.basename(mask_path)}" x="0" y="0" '
            f'width="{width}" height="{height}"/></svg>'
        )

    # scans=2 with remove_background=true isolates the shape and discards the
    # background rectangle. Single-scan mode traces the background instead.
    actions = (
        f"select-all;object-trace:2,true,false,true,"
        f"{speckles},{smooth_corners},{optimize};"
        f"export-filename:{traced};export-plain-svg;export-do"
    )
    subprocess.run([inkscape, wrapper, f"--actions={actions}"],
                   capture_output=True, text=True, check=False)

    if not os.path.exists(traced):
        return None
    found = re.findall(r'<path[^>]*?\sd="([^"]*)"',
                       open(traced, encoding="utf8").read(), re.S)
    return found[0] if found else None


def assemble(paths, colours, labels, size, out_path: str, root_label: str):
    width, height = size
    body = []
    for path_data, colour, label in zip(paths, colours, labels):
        body.append(
            f'    <g id="{label}" inkscape:label="{label}">\n'
            f'      <path fill="{colour}" fill-rule="evenodd" d="{path_data}"/>\n'
            f'    </g>'
        )
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg"\n'
        '     xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"\n'
        f'     viewBox="0 0 {width} {height}" width="{width}" height="{height}">\n'
        f'  <g id="{root_label}" inkscape:label="{root_label}">\n'
        + "\n".join(body)
        + f'\n  </g>\n</svg>\n'
    )
    with open(out_path, "w", encoding="utf8") as handle:
        handle.write(svg)


def tighten(inkscape: str, svg_path: str) -> None:
    """Crop the viewBox to the drawing, then restore the labels plain-SVG strips."""
    original = open(svg_path, encoding="utf8").read()
    labels = re.findall(r'inkscape:label="([^"]*)"', original)
    subprocess.run(
        [inkscape, svg_path, "--export-type=svg", "--export-plain-svg",
         "--export-area-drawing", f"--export-filename={svg_path}"],
        capture_output=True, text=True, check=False,
    )
    updated = open(svg_path, encoding="utf8", errors="replace").read()
    if "inkscape:label" not in updated:
        updated = updated.replace(
            'xmlns="http://www.w3.org/2000/svg"',
            'xmlns="http://www.w3.org/2000/svg"\n'
            '   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"', 1)
        for label in labels:
            updated = updated.replace(
                f'id="{label}"', f'id="{label}" inkscape:label="{label}"')
        with open(svg_path, "w", encoding="utf8") as handle:
            handle.write(updated)


def run_trace(reference: str, output: str, colors=None, labels=None,
              root_label="artwork", count=2, snap=False, background=None,
              speckles=2, smooth_corners=1.0, optimize=0.2, inkscape=None,
              no_check=False, log=print):
    """The whole pipeline, shared by the CLI and the window.

    Returns (output_path, check_png_path_or_None). Raises TraceError with a
    plain-language message on pipeline failures; find_inkscape still exits
    the process when Inkscape is missing, so window code checks that first.
    """
    inkscape = find_inkscape(inkscape)
    image = Image.open(reference).convert("RGB")
    size = image.size
    log(f"reference : {reference} ({size[0]}x{size[1]})")

    background_rgb, targets = resolve_palette(
        image, colors=colors, count=count, snap=snap, background=background,
        log=log)

    if labels:
        label_list = [s.strip() for s in labels.split(",")]
        if len(label_list) != len(targets):
            raise TraceError(
                f"Got {len(label_list)} labels for {len(targets)} colours.")
    else:
        label_list = [f"layer_{i}_{rgb_to_hex(c).lstrip('#').lower()}"
                      for i, c in enumerate(targets, start=1)]

    with tempfile.TemporaryDirectory() as work:
        masks = build_masks(image, targets, background_rgb, work)
        traced, kept_colours, kept_labels = [], [], []
        for (mask_path, pixels), colour, label in zip(masks, targets, label_list):
            data = trace(inkscape, mask_path, size, speckles,
                         smooth_corners, optimize)
            if not data:
                log(f"  ! {label}: nothing traced ({pixels} px) - skipped")
                continue
            nodes = len(re.findall(r"[MmCcLlSsQqTtAaHhVv]", data))
            subpaths = len(re.findall(r"[Mm]", data))
            log(f"  {label}: {pixels} px -> {subpaths} subpath(s), {nodes} nodes")
            traced.append(data)
            kept_colours.append(rgb_to_hex(colour))
            kept_labels.append(label)

        if not traced:
            raise TraceError("Nothing was traced. Check --colors against the reference.")

        os.makedirs(os.path.dirname(os.path.abspath(output)), exist_ok=True)
        assemble(traced, kept_colours, kept_labels, size, output, root_label)

    tighten(inkscape, output)
    log(f"wrote     : {output}")

    check = None
    if not no_check:
        check = os.path.splitext(output)[0] + "_check.png"
        subprocess.run(
            [inkscape, output, "--export-type=png", "--export-width=1200",
             f"--export-filename={check}"], capture_output=True, text=True, check=False)
        if os.path.exists(check):
            log(f"self-check: {check}")
            log("Compare it against the reference before treating the SVG as usable.")
        else:
            check = None
    return output, check


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Trace a flat raster reference into a colour-separated SVG.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Run with no arguments (or "--gui") to open the window instead.',
    )
    parser.add_argument("reference", help="input PNG/JPG reference image")
    parser.add_argument("output", help="output SVG path")
    parser.add_argument("--colors", help="comma-separated hex colours to separate")
    parser.add_argument("--labels", help="comma-separated snake_case group names")
    parser.add_argument("--root-label", default="artwork",
                        help="name of the outer group (default: artwork)")
    parser.add_argument("--count", type=int, default=2,
                        help="how many colours to auto-detect (default: 2)")
    parser.add_argument("--snap", action="store_true",
                        help="snap detected colours to the nearest brand palette colour")
    parser.add_argument("--background", help="background hex; default is the most common colour")
    parser.add_argument("--speckles", type=int, default=2, help="suppress specks below N px")
    parser.add_argument("--smooth-corners", type=float, default=1.0,
                        help="0 keeps every corner sharp, 1.33 rounds everything")
    parser.add_argument("--optimize", type=float, default=0.2,
                        help="curve tolerance; lower means more nodes and more fidelity")
    parser.add_argument("--inkscape", help="path to the Inkscape executable")
    parser.add_argument("--no-check", action="store_true",
                        help="skip rendering the self-check PNG")
    args = parser.parse_args()

    try:
        run_trace(args.reference, args.output, colors=args.colors,
                  labels=args.labels, root_label=args.root_label,
                  count=args.count, snap=args.snap, background=args.background,
                  speckles=args.speckles, smooth_corners=args.smooth_corners,
                  optimize=args.optimize, inkscape=args.inkscape,
                  no_check=args.no_check)
    except TraceError as error:
        sys.exit(str(error))


class GuiApp:
    """The window: a thin layer over the same functions the CLI uses."""

    def __init__(self):
        self.reference = None
        self.output_override = None
        self.running = False
        self.open_when_done = True  # scripted tests switch this off
        self.q = queue.Queue()

        self.root = tk.Tk()
        self.root.title("Trace a reference")
        self.root.minsize(640, 600)
        self._apply_brand()
        frame = ttk.Frame(self.root, padding=12)
        frame.grid(row=0, column=0, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(9, weight=1)

        if self._load_logo():
            ttk.Label(frame, image=self._logo).grid(
                row=0, column=0, sticky="w", pady=(0, 12))
        else:  # script travelling without the blobs: text header, same layout
            ttk.Label(frame, text="Grounded AI Practice",
                      font=("Segoe UI", 13, "bold")).grid(
                row=0, column=0, sticky="w", pady=(0, 12))

        ttk.Label(frame, text="1.  Choose the reference image",
                  style="Header.TLabel").grid(row=1, column=0, sticky="w")
        row = ttk.Frame(frame)
        row.grid(row=2, column=0, sticky="w", pady=(4, 10))
        ttk.Button(row, text="Choose an image...",
                   command=self.pick_reference).pack(side="left")
        self.ref_label = ttk.Label(
            row, text="a flat, limited-colour concept (PNG or JPG)",
            style="Hint.TLabel")
        self.ref_label.pack(side="left", padx=8)

        ttk.Label(frame, text="2.  Where the SVG will be written",
                  style="Header.TLabel").grid(row=3, column=0, sticky="w")
        row = ttk.Frame(frame)
        row.grid(row=4, column=0, sticky="w", pady=(4, 10))
        ttk.Button(row, text="Change...", command=self.pick_output).pack(side="left")
        self.out_label = ttk.Label(row, text="(next to the image, as <name>.svg)",
                                   style="Hint.TLabel")
        self.out_label.pack(side="left", padx=8)

        ttk.Label(frame, text="3.  Colours", style="Header.TLabel").grid(
            row=5, column=0, sticky="w")
        row = ttk.Frame(frame)
        row.grid(row=6, column=0, sticky="w", pady=(4, 2))
        ttk.Label(row, text="Find").pack(side="left")
        self.count_var = tk.StringVar(value="2")
        ttk.Spinbox(row, from_=1, to=6, width=3,
                    textvariable=self.count_var).pack(side="left", padx=6)
        ttk.Label(row, text="colours automatically, and").pack(side="left")
        self.snap_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(frame, variable=self.snap_var,
                        text="snap them to the GAP palette "
                             "(right for brand assets; untick for other artwork)"
                        ).grid(row=7, column=0, sticky="w", pady=(0, 10))

        row = ttk.Frame(frame)
        row.grid(row=8, column=0, sticky="w", pady=(0, 10))
        self.detect_btn = ttk.Button(row, text="Detect colours",
                                     command=self.detect)
        self.detect_btn.pack(side="left")
        self.trace_btn = ttk.Button(row, text="Trace", command=self.trace,
                                    style="Accent.TButton")
        self.trace_btn.pack(side="left", padx=8)

        self.text = tk.Text(frame, height=14, state="disabled", wrap="none",
                            font=("Consolas", 9), relief="flat",
                            highlightthickness=1, highlightbackground=MIST,
                            highlightcolor=EMBER, background="#FFFFFF",
                            foreground=INK)
        self.text.grid(row=9, column=0, sticky="nsew")

    def _apply_brand(self):
        """GAP palette over ttk's built-in clam theme — clam, unlike the
        native Windows theme, honours colour configuration on every widget."""
        self.root.configure(background=PAPER)
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure(".", background=PAPER, foreground=INK,
                        font=("Segoe UI", 9))
        style.configure("TButton", background=MIST, foreground=INK,
                        padding=(10, 4))
        style.map("TButton", background=[("pressed", SAND), ("active", SAND)])
        style.configure("Accent.TButton", background=EMBER,
                        foreground="#FFFFFF")
        style.map("Accent.TButton",
                  background=[("disabled", MIST), ("pressed", EMBER_DEEP),
                              ("active", EMBER_DEEP)],
                  foreground=[("disabled", STONE)])
        style.map("TCheckbutton", background=[("active", PAPER)])
        style.configure("Header.TLabel", font=("Segoe UI", 10, "bold"))
        style.configure("Hint.TLabel", foreground=STONE)
        style.configure("TEntry", fieldbackground="#FFFFFF")
        style.configure("TSpinbox", fieldbackground="#FFFFFF")

    def _load_logo(self):
        """Header wordmark + title-bar symbol, embedded at the bottom of
        this file as base64 PNG so a copy of the script keeps its branding
        without the repo alongside. Tk decodes base64 PNG natively."""
        try:
            self._logo = tk.PhotoImage(data=LOGO_WORDMARK_PNG)
            # title bar gets the symbol: the 2.7:1 wordmark dies at icon size
            self._icons = [tk.PhotoImage(data=d)
                           for d in (LOGO_SYMBOL_64_PNG, LOGO_SYMBOL_32_PNG)]
            self.root.iconphoto(True, *self._icons)
            return True
        except Exception:  # blobs absent or corrupted: text header instead
            return False

    def _append(self, line):
        self.text.configure(state="normal")
        self.text.insert("end", line + "\n")
        self.text.see("end")
        self.text.configure(state="disabled")

    def _clear_text(self):
        self.text.configure(state="normal")
        self.text.delete("1.0", "end")
        self.text.configure(state="disabled")

    def _output_path(self):
        if self.output_override:
            return self.output_override
        return os.path.splitext(self.reference)[0] + ".svg"

    def pick_reference(self):
        picked = filedialog.askopenfilename(
            title="Choose the reference image",
            filetypes=[("Images", "*.png *.jpg *.jpeg *.webp *.bmp"),
                       ("All files", "*.*")])
        if picked:
            self.reference = picked
            self.ref_label.config(text=os.path.basename(picked))
            if not self.output_override:
                self.out_label.config(text=self._output_path())

    def pick_output(self):
        start = os.path.splitext(self.reference)[0] + ".svg" \
            if self.reference else ""
        picked = filedialog.asksaveasfilename(
            title="Choose where to write the SVG",
            defaultextension=".svg", initialfile=os.path.basename(start),
            filetypes=[("SVG", "*.svg")])
        if picked:
            self.output_override = picked
            self.out_label.config(text=picked)

    def _settings(self):
        if not self.reference:
            messagebox.showinfo("No image chosen yet",
                                "Choose the reference image first (step 1).")
            return None
        try:
            count = max(1, min(6, int(self.count_var.get())))
        except ValueError:
            count = 2
        return count, self.snap_var.get()

    def detect(self):
        """Preview the colour separation without tracing anything."""
        if self.running:
            return
        settings = self._settings()
        if not settings:
            return
        count, snap = settings
        self._clear_text()
        try:
            image = Image.open(self.reference).convert("RGB")
            resolve_palette(image, count=count, snap=snap, log=self._append)
            self._append("\npreview only - nothing traced yet. These are the "
                         "colours Trace will separate.")
        except TraceError as error:
            self._append(str(error))
        except Exception as error:
            self._append(f"FAILED  {error}")

    def trace(self):
        if self.running:
            return
        settings = self._settings()
        if not settings:
            return
        count, snap = settings
        try:  # check Inkscape up front so the failure is a dialog, not a crash
            find_inkscape(None)
        except SystemExit as error:
            messagebox.showerror("Inkscape is needed for tracing", str(error))
            return
        self._clear_text()
        self.running = True
        self.detect_btn.state(["disabled"])
        self.trace_btn.state(["disabled"])
        threading.Thread(target=self._work,
                         args=(self.reference, self._output_path(), count, snap),
                         daemon=True).start()
        self.root.after(100, self._poll)

    def _work(self, reference, output, count, snap):
        try:
            out, check = run_trace(reference, output, count=count, snap=snap,
                                   log=self.q.put)
            self.q.put(("done", out, check))
        except (TraceError, Exception) as error:
            self.q.put(f"FAILED  {error}")
            self.q.put(("done", None, None))

    def _poll(self):
        while True:
            try:
                item = self.q.get_nowait()
            except queue.Empty:
                self.root.after(100, self._poll)
                return
            if isinstance(item, tuple):
                _, out, check = item
                self.running = False
                self.detect_btn.state(["!disabled"])
                self.trace_btn.state(["!disabled"])
                if out:
                    self._append("\nDone. The SVG is a starting point for hand "
                                 "refinement in Inkscape, never a finished "
                                 "asset - and compare the self-check PNG "
                                 "against the reference first.")
                    if self.open_when_done:
                        os.startfile(os.path.dirname(os.path.abspath(out)))
                return
            self._append(item)


def run_gui():
    if not TK_OK:
        sys.exit("tkinter is missing from this Python, so the window cannot "
                 "open. The command line still works - run with -h for usage.")
    try:  # crisp text on scaled Windows displays
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass
    GuiApp().root.mainloop()


# Embedded GAP logo (base64 PNG; Tk decodes it natively). Generated by
# tools/embed_logo.py from assets/logo/png - regenerate there if the
# brand assets change; never hand-edit.
LOGO_WORDMARK_PNG = """
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
uBUYOi4zX/8fsVsipdQVSM0AAAAASUVORK5CYII=
"""

LOGO_SYMBOL_64_PNG = """
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
SUVORK5CYII=
"""

LOGO_SYMBOL_32_PNG = """
iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAEPElEQVR42sVXXWhcRRT+zszdZN24
mt0N3ULRQGqapEkT8TFWfWrtQ9EK0ofG/vjzJEKLFdI00eqjRYSC1YjQgoINBQVLGwIWJFqE0L5o
V+2LGrCVQtIYKW524905PuydOzN77zZNTPQ+3Mt+d+5833znzDmzxMz4Py8PAFpbWzMJ8t8mou1S
yKwQlJZCgISAFAQiCj8welnf/wJj0UzJ1TfOuiKYz8CRq9d+PuUBgMTix0rRTikIDAZz9UlgILjX
zmD9bAK4qUaXTRuPAbsAVAUoxY8QqqRgBiig1z/Naq3J4rB4B8KRNkZWCFjhfhLGYmZYQtiMvnuL
DRoRoklsAQCF8SUzuCoEgZBlWryUA8FTGEOMpf2PbsW2bTuC6dgIYVgYhxhrtC7GFgYzLhTA1mrB
2Pn0Lpw4OYqh4WOQQjqkZtxSBDWYJmF2IuUFTzIkhGPDQ1CVCgb2HUBXdw9eO/gKZmdnVmSx3rdu
ynCIi2hoGeXFMkaGBvHm60expbcPY599gZ7e3mVabFbLVlJxgCk7B0wSWrMAODv2KV7aPwApJU5/
Mob+rY/dtcWGWGO1icxODpATVyuhbty4jrm5W0gkErg3nXYsdQg4DqvngBHjmT1QjX/4BQEdXV0Y
/egUmjNZDB4+hInxC7X1OLKqmvJQBzOXAABSiuzcYjC2P7kDZ85+DiEl9u3ZjfEL55ZncQxmVs+u
AKVLTeDjnoG9OHFyFNPT09j9zFMofP/dyixml9je8oqVtQ3ZNB0GkF+/HhPj5zFyZBALpWK1GwYz
JpNJbOl7GNLzIo1gfn4ePxYKiBjPke7h1gF2CzDefec4BAkIISDIDd3hwaMY2Lu/bn9/8cBzuPT1
JNzS4IphmJIfFiK2e46u/8xgIiehJsbPI5vNOWcETVAsLuCnwg8BSQypLUa5Akz3CUgDDZHSeXlq
Cpenppa2uA7GNZtB5wBV2WqIg3MBhR9H+m19i+sQG4ydHHC3yp2IGbFJdmdSA3DcmRDh0SMwwhEC
UJAcy7HYeRs599ZUwvBjfRTT6w8zdiUWR8U4QvQuICLKt2TARBoDgYoE+KBqPpJpFQCxFRoKJ6PQ
4jgsmFVvKFZoSDSWtQNCV6C2to147/0P0dvXl/oP/hKktRHeulzz31JKfDV5CR0tGfDFc8Dt+bWl
z7T8Qs8+v9Hr7oaYuQmkUk3Fjs7OVOmD4/CvfLvmyxdtHfelAHjl8kMEzKJcKjX4vg+/tR1/Tl6M
S91VvRpKJaSCENC6XPMCETUePPQqhoZH4P9xC/7c7NpaQOKbZFv748TMyLdkrxKhRxChfdOm3zo3
b/79nsakkp5QnvBU2JFWMwPT6cLIG2+9TMyMDflcf6XCZ0jQg4IIQhAIwZNEsH14taNy+tfrN18g
/feciOSGfO4JKDwACEiPKoKoQkSV6EHq312KVCVZUl9em5m5/Q8rDQfdDkx5PQAAAABJRU5ErkJg
gg==
"""


if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1:] == ["--gui"]:
        run_gui()
    else:
        main()
