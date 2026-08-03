#!/usr/bin/env python3
r"""Prepare phone photos for AI upload: convert, rename, optionally shrink.

Why this exists
---------------
Phone photos reach the desktop as IMG_4232.HEIC or PXL_20260801_093015.jpg —
names that say nothing, in formats desktop tools handle unevenly (HEIC in
particular needs codec packs Windows does not ship). This is the step
between transfer and use: however the photos left the phone (cloud folder,
AirDrop, cable), this turns the pile into files ready to hand to Claude or
any other tool — converted to PNG or JPEG, named <date>_<label>_<NN>.<ext>
so a batch reads chronologically, and optionally shrunk to the size an AI
model actually consumes. Originals are never modified, moved or deleted.

Input formats: HEIC/HEIF (iPhone; needs pillow-heif), JPEG (the Android
default), PNG (screenshots), WebP, TIFF, BMP, GIF, AVIF. RAW/DNG (iPhone
ProRAW, Samsung Expert RAW) is out of scope — that needs a raw developer,
not a format conversion. Live Photo .mov companions and video are ignored.

The window
----------
Run with no arguments (or --gui) and a small window opens instead of the
command line: pick photos or a folder, type the naming word, choose
"smaller for AI" or "full quality", preview the new names, convert. It
drives exactly the same functions as the command line — the window exists
so the tool is reachable without a terminal, not as a different tool —
and it exposes only the decisions a person actually makes; every finer
control below stays command-line on purpose.

The --ai preset
---------------
--ai resizes so the long edge is at most 1568 px and saves JPEG at quality
85. The number comes from Anthropic's vision guidance rather than folklore:
most Claude models scale any image beyond 1568 px on its long edge down
before the model sees it, so pixels past that limit are upload weight with
no fidelity gain. Current high-resolution Claude models accept up to
2576 px at roughly three times the image-token cost — pass --max-edge 2576
when that detail matters more than size. Typical result: a 3 MB HEIC
becomes a 15-25 MB PNG untouched, or a JPEG of a few hundred KB under
--ai. Each of --format, --max-edge and --quality can also be set
individually; an explicit value overrides the preset.

How it works
------------
1. Dates each file from EXIF DateTimeOriginal (the capture time), falling
   back to EXIF DateTime, then to the file's modified time — and marks
   which files used the weakest fallback, since a copied file's modified
   time can be long after the photo was taken.

2. Numbers files per date in capture order, and never overwrites: a name
   already on disk advances the sequence, so re-running over a folder
   after a fresh import is safe. Files already named by this tool are
   skipped when a folder is scanned, so its own output is never
   re-converted — pass such a file explicitly to reprocess it.

3. Bakes EXIF orientation into the pixels, because viewers do not reliably
   honour rotation metadata in PNG/JPEG, and carries the remaining EXIF
   (capture time included) into the output. For JPEG output, transparency
   is flattened onto white.

4. Re-opens every file it writes as an integrity self-check.

Requires Python with Pillow. pillow-heif (pip install pillow-heif) is
needed only when HEIC/HEIF files are among the inputs; every other format
works with Pillow alone. The window needs tkinter, which ships with
Python on Windows.

Usage
-----
    python tools/prep_photos.py                    # no arguments: the window
    python tools/prep_photos.py C:\imports --label whiteboard --ai
    python tools/prep_photos.py C:\imports --dry-run
    python tools/prep_photos.py IMG_4232.HEIC shot.webp -o C:\out
"""

import argparse
import os
import queue
import re
import sys
import threading
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageOps, features

try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
    HEIF_OK = True
except ImportError:
    HEIF_OK = False

try:
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk
    TK_OK = True
except ImportError:  # rare stripped-down Python; the CLI still works
    TK_OK = False

HEIF_EXTS = {".heic", ".heif"}
PIL_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".bmp", ".gif",
            ".avif"}
INPUT_EXTS = HEIF_EXTS | PIL_EXTS
AI_MAX_EDGE = 1568   # long edge beyond which most Claude models downscale anyway
AI_QUALITY = 85
OWN_OUTPUT = re.compile(r"\d{4}-\d{2}-\d{2}_[a-z0-9_]+_\d{2,}\.(png|jpg)",
                        re.IGNORECASE)
EXIF_IFD = 0x8769          # pointer to the EXIF sub-IFD, where capture time lives
DATETIME_ORIGINAL = 36867  # capture time (sub-IFD)
DATETIME = 306             # file-level timestamp (IFD0)
HEIF_INSTALL_MSG = (
    "HEIC/HEIF files are present but pillow-heif is not installed.\n"
    "Install it with:  pip install pillow-heif\n"
    "(plain pip install; the wheel bundles libheif, no Windows codec packs)")

# GAP palette (project_brief.md, "Visual identity") — used per the roles
# recorded there; only EMBER_DEEP is derived (Ember darkened for hover)
INK = "#27221E"         # primary text
EMBER = "#F15E4B"       # primary accent: the one action that matters
EMBER_DEEP = "#D94C3B"
PAPER = "#F9F9F9"       # main background
MIST = "#EFEEED"        # secondary background: neutral buttons, borders
SAND = "#F9E8DC"        # warm tint: hover and selections
STONE = "#6E6E6E"       # neutral grey: hints and secondary text


def snake_case(text):
    text = re.sub(r"[\s\-]+", "_", text.strip().lower())
    text = re.sub(r"[^a-z0-9_]", "", text)
    return re.sub(r"_{2,}", "_", text).strip("_") or "img"


def resolve_settings(ai, fmt=None, max_edge=None, quality=None):
    """Fill unset options from the --ai preset or the plain defaults."""
    fmt = fmt or ("jpg" if ai else "png")
    if max_edge is None:
        max_edge = AI_MAX_EDGE if ai else None
    if quality is None:
        quality = AI_QUALITY
    return fmt, max_edge, quality, (".jpg" if fmt == "jpg" else ".png")


def capture_time(src):
    """Return (datetime, "exif" | "mtime") for one image."""
    with Image.open(src) as im:
        exif = im.getexif()
        stamp = exif.get_ifd(EXIF_IFD).get(DATETIME_ORIGINAL) or exif.get(DATETIME)
    if stamp:
        try:
            return datetime.strptime(str(stamp).strip(), "%Y:%m:%d %H:%M:%S"), "exif"
        except ValueError:
            pass  # malformed stamp: fall through to mtime
    return datetime.fromtimestamp(src.stat().st_mtime), "mtime"


def collect(sources, recurse):
    """Gather input files; folder scans skip this tool's own output."""
    files, skipped = [], 0
    for name in sources:
        path = Path(name)
        if path.is_dir():
            walk = path.rglob("*") if recurse else path.iterdir()
            for p in walk:
                if not p.is_file() or p.suffix.lower() not in INPUT_EXTS:
                    continue
                if OWN_OUTPUT.fullmatch(p.name):
                    skipped += 1
                    continue
                files.append(p)
        elif path.is_file() and path.suffix.lower() in INPUT_EXTS:
            files.append(path)  # explicit args bypass the own-output skip
        elif path.is_file():
            print(f"ignoring {path.name}: not a supported image format",
                  file=sys.stderr)
        else:
            sys.exit(f"not found: {path}")
    unique, seen = [], set()
    for p in files:
        key = str(p.resolve()).lower()
        if key not in seen:
            seen.add(key)
            unique.append(p)
    return unique, skipped


def analyse(files):
    """Read each file's capture time; returns (records, failures)."""
    records, failures = [], []
    for src in files:
        try:
            when, origin = capture_time(src)
        except Exception as exc:
            failures.append((src, f"unreadable: {exc}"))
            continue
        records.append({"src": src, "when": when, "origin": origin})
    return records, failures


def plan_names(records, label, ext, outdir):
    """Assign each record a destination, never claiming a taken name."""
    by_date = defaultdict(list)
    for rec in records:
        by_date[rec["when"].strftime("%Y-%m-%d")].append(rec)
    claimed = set()  # lowercased: NTFS will not distinguish two casings
    for date_str in sorted(by_date):
        batch = sorted(by_date[date_str],
                       key=lambda r: (r["when"], r["src"].name.lower()))
        width = max(2, len(str(len(batch))))
        seq = 1
        for rec in batch:
            folder = outdir or rec["src"].parent
            while True:
                dest = folder / f"{date_str}_{label}_{seq:0{width}d}{ext}"
                seq += 1
                key = str(dest).lower()
                if key not in claimed and not dest.exists():
                    break
            claimed.add(key)
            rec["dest"] = dest


def convert(src, dest, fmt, max_edge, quality):
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im)
        exif = im.getexif()  # orientation already applied and removed
        if max_edge and max(im.size) > max_edge:
            im.thumbnail((max_edge, max_edge), Image.Resampling.LANCZOS)
        has_alpha = im.mode in ("RGBA", "LA") or (
            im.mode == "P" and "transparency" in im.info)
        if fmt == "jpg":
            if has_alpha:
                im = im.convert("RGBA")
                flat = Image.new("RGB", im.size, (255, 255, 255))
                flat.paste(im, mask=im.getchannel("A"))
                im = flat
            elif im.mode != "RGB":
                im = im.convert("RGB")
        elif im.mode not in ("RGB", "RGBA", "L", "LA"):
            im = im.convert("RGBA" if has_alpha else "RGB")
        params = {"optimize": True}
        if exif:
            params["exif"] = exif.tobytes()
        if fmt == "jpg":
            params["quality"] = quality
        im.save(dest, format="JPEG" if fmt == "jpg" else "PNG", **params)
    with Image.open(dest) as check:
        check.verify()


def main():
    ap = argparse.ArgumentParser(
        description="Convert phone photos to PNG/JPEG named "
                    "<date>_<label>_<NN>, optionally shrunk for AI upload.",
        epilog='Run with no arguments (or "--gui") to open the window instead.')
    ap.add_argument("sources", nargs="+",
                    help="image files and/or folders containing them")
    ap.add_argument("--label", default="img",
                    help="subject slug for the new names, snake_cased for you "
                         "(default: img)")
    ap.add_argument("--ai", action="store_true",
                    help=f"preset for AI upload: JPEG, long edge <= "
                         f"{AI_MAX_EDGE} px, quality {AI_QUALITY} "
                         "(each part overridable below)")
    ap.add_argument("--format", choices=("png", "jpg"), default=None,
                    help="output format (default: png, or jpg under --ai)")
    ap.add_argument("--max-edge", type=int, default=None, metavar="PX",
                    help="shrink so the longest edge is at most PX; never "
                         "upscales (default: no resize, or "
                         f"{AI_MAX_EDGE} under --ai)")
    ap.add_argument("--quality", type=int, default=None, metavar="N",
                    help=f"JPEG quality 1-95 (default {AI_QUALITY}; "
                         "ignored for png)")
    ap.add_argument("-o", "--outdir", type=Path,
                    help="write every output into this folder instead of "
                         "beside its source")
    ap.add_argument("--recurse", action="store_true",
                    help="scan folders recursively")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the rename map and write nothing")
    args = ap.parse_args()

    fmt, max_edge, quality, ext = resolve_settings(
        args.ai, args.format, args.max_edge, args.quality)
    label = snake_case(args.label)

    files, skipped = collect(args.sources, args.recurse)
    if skipped:
        print(f"skipped {skipped} file(s) already named by this tool; "
              "pass one explicitly to reprocess it")
    if not files:
        sys.exit("no supported image files found")

    if not HEIF_OK and any(p.suffix.lower() in HEIF_EXTS for p in files):
        sys.exit(HEIF_INSTALL_MSG)
    if any(p.suffix.lower() == ".avif" for p in files) and not features.check("avif"):
        sys.exit(".avif files are present but this Pillow build lacks AVIF "
                 "support.\nFix with:  pip install --upgrade pillow")

    records, failures = analyse(files)
    plan_names(records, label, ext, args.outdir)

    if args.outdir and not args.dry_run:
        args.outdir.mkdir(parents=True, exist_ok=True)

    converted = 0
    for rec in records:
        note = "" if rec["origin"] == "exif" else "  (file date: no usable EXIF)"
        line = f"{rec['src'].name} -> {rec['dest'].name}{note}"
        if args.dry_run:
            print(line)
            continue
        try:
            convert(rec["src"], rec["dest"], fmt, max_edge, quality)
        except Exception as exc:
            failures.append((rec["src"], str(exc)))
            rec["dest"].unlink(missing_ok=True)  # no half-written files left behind
            continue
        converted += 1
        print(line)

    if args.dry_run:
        print(f"\ndry run: {len(records)} file(s) would be written as "
              f"{fmt.upper()}; nothing touched")
    else:
        print(f"\n{converted} of {len(files)} file(s) converted to "
              f"{fmt.upper()}; originals untouched")
    for src, why in failures:
        print(f"FAILED  {src}: {why}", file=sys.stderr)
    if failures:
        sys.exit(1)


class GuiApp:
    """The window: a thin layer over the same functions the CLI uses."""

    def __init__(self):
        self.sources = []
        self.outdir = None
        self.running = False
        self.open_when_done = True  # scripted tests switch this off
        self.q = queue.Queue()

        self.root = tk.Tk()
        self.root.title("Prep photos for AI")
        self.root.minsize(640, 620)
        self._apply_brand()
        frame = ttk.Frame(self.root, padding=12)
        frame.grid(row=0, column=0, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(12, weight=1)

        if self._load_logo():
            ttk.Label(frame, image=self._logo).grid(
                row=0, column=0, sticky="w", pady=(0, 12))
        else:  # script travelling without the repo: text header, same layout
            ttk.Label(frame, text="Grounded AI Practice",
                      font=("Segoe UI", 13, "bold")).grid(
                row=0, column=0, sticky="w", pady=(0, 12))

        ttk.Label(frame, text="1.  Choose the photos",
                  style="Header.TLabel").grid(row=1, column=0, sticky="w")
        row = ttk.Frame(frame)
        row.grid(row=2, column=0, sticky="w", pady=(4, 2))
        ttk.Button(row, text="Add photos...", command=self.add_photos).pack(
            side="left")
        ttk.Button(row, text="Add a folder...", command=self.add_folder).pack(
            side="left", padx=6)
        ttk.Button(row, text="Clear", command=self.clear_sources).pack(side="left")
        self.source_list = tk.Listbox(
            frame, height=5, relief="flat", highlightthickness=1,
            highlightbackground=MIST, highlightcolor=EMBER,
            background="#FFFFFF", foreground=INK,
            selectbackground=SAND, selectforeground=INK)
        self.source_list.grid(row=3, column=0, sticky="ew", pady=(0, 10))

        ttk.Label(frame, text="2.  Pick a word for the new names",
                  style="Header.TLabel").grid(row=4, column=0, sticky="w")
        row = ttk.Frame(frame)
        row.grid(row=5, column=0, sticky="w", pady=(4, 10))
        self.label_var = tk.StringVar(value="img")
        ttk.Entry(row, textvariable=self.label_var, width=22).pack(side="left")
        self.example = ttk.Label(row, text="", style="Hint.TLabel")
        self.example.pack(side="left", padx=8)
        self.label_var.trace_add("write", lambda *_: self._update_example())

        ttk.Label(frame, text="3.  Choose the output",
                  style="Header.TLabel").grid(row=6, column=0, sticky="w")
        self.mode_var = tk.StringVar(value="ai")
        ttk.Radiobutton(frame, variable=self.mode_var, value="ai",
                        command=self._update_example,
                        text="Smaller files for AI chats - JPEG, sized to what "
                             "the AI actually uses (recommended)").grid(
            row=7, column=0, sticky="w", pady=(4, 0))
        ttk.Radiobutton(frame, variable=self.mode_var, value="full",
                        command=self._update_example,
                        text="Full quality - PNG, much larger files").grid(
            row=8, column=0, sticky="w")
        self.dest_var = tk.StringVar(value="beside")
        ttk.Radiobutton(frame, variable=self.dest_var, value="beside",
                        command=self._reset_outdir,
                        text="Save next to the originals").grid(
            row=9, column=0, sticky="w", pady=(6, 0))
        row = ttk.Frame(frame)
        row.grid(row=10, column=0, sticky="w")
        ttk.Radiobutton(row, variable=self.dest_var, value="chosen",
                        command=self._pick_outdir,
                        text="Save into one folder:").pack(side="left")
        self.outdir_label = ttk.Label(row, text="(none chosen)",
                                      style="Hint.TLabel")
        self.outdir_label.pack(side="left", padx=6)

        row = ttk.Frame(frame)
        row.grid(row=11, column=0, sticky="w", pady=10)
        self.preview_btn = ttk.Button(row, text="Preview the new names",
                                      command=self.preview)
        self.preview_btn.pack(side="left")
        self.convert_btn = ttk.Button(row, text="Convert", command=self.convert,
                                      style="Accent.TButton")
        self.convert_btn.pack(side="left", padx=8)

        self.text = tk.Text(frame, height=12, state="disabled", wrap="none",
                            font=("Consolas", 9), relief="flat",
                            highlightthickness=1, highlightbackground=MIST,
                            highlightcolor=EMBER, background="#FFFFFF",
                            foreground=INK)
        self.text.grid(row=12, column=0, sticky="nsew")
        self._update_example()

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
        style.map("TRadiobutton", background=[("active", PAPER)])
        style.configure("Header.TLabel", font=("Segoe UI", 10, "bold"))
        style.configure("Hint.TLabel", foreground=STONE)
        style.configure("TEntry", fieldbackground="#FFFFFF")

    def _load_logo(self):
        """Header wordmark + title-bar symbol, embedded at the bottom of
        this file as base64 PNG so a copy of the script keeps its branding
        without the repo alongside. Tk decodes base64 PNG natively - no
        extra imports and no files to find."""
        try:
            self._logo = tk.PhotoImage(data=LOGO_WORDMARK_PNG)
            # title bar gets the symbol: the 2.7:1 wordmark dies at icon size
            self._icons = [tk.PhotoImage(data=d)
                           for d in (LOGO_SYMBOL_64_PNG, LOGO_SYMBOL_32_PNG)]
            self.root.iconphoto(True, *self._icons)
            return True
        except Exception:  # blobs absent or corrupted: text header instead
            return False

    def _update_example(self):
        ext = ".jpg" if self.mode_var.get() == "ai" else ".png"
        stamp = datetime.now().strftime("%Y-%m-%d")
        self.example.config(text=f"files become  {stamp}_"
                                 f"{snake_case(self.label_var.get())}_01{ext}")

    def add_photos(self):
        picked = filedialog.askopenfilenames(
            title="Choose photos",
            filetypes=[("Photos", "*.heic *.heif *.jpg *.jpeg *.png *.webp "
                                  "*.tif *.tiff *.bmp *.gif *.avif"),
                       ("All files", "*.*")])
        self.sources.extend(p for p in picked if p not in self.sources)
        self._refresh_sources()

    def add_folder(self):
        picked = filedialog.askdirectory(title="Choose a folder of photos")
        if picked and picked not in self.sources:
            self.sources.append(picked)
        self._refresh_sources()

    def clear_sources(self):
        self.sources = []
        self._refresh_sources()

    def _refresh_sources(self):
        self.source_list.delete(0, "end")
        for s in self.sources:
            p = Path(s)
            self.source_list.insert(
                "end", f"[folder]  {p}" if p.is_dir() else p.name)

    def _pick_outdir(self):
        picked = filedialog.askdirectory(title="Choose the output folder")
        if picked:
            self.outdir = Path(picked)
            self.outdir_label.config(text=picked)
        elif self.outdir is None:
            self.dest_var.set("beside")  # dialog cancelled, nothing chosen

    def _reset_outdir(self):
        self.outdir = None
        self.outdir_label.config(text="(none chosen)")

    def _append(self, line):
        self.text.configure(state="normal")
        self.text.insert("end", line + "\n")
        self.text.see("end")
        self.text.configure(state="disabled")

    def _clear_text(self):
        self.text.configure(state="normal")
        self.text.delete("1.0", "end")
        self.text.configure(state="disabled")

    def _prepare(self):
        """The same assembly the CLI does; None if nothing can run."""
        if not self.sources:
            messagebox.showinfo("Nothing chosen yet",
                                "Add photos or a folder first (step 1).")
            return None
        files, skipped = collect(self.sources, recurse=False)
        if skipped:
            self._append(f"skipped {skipped} file(s) already named by this "
                         "tool; add one by itself to reprocess it")
        if not files:
            messagebox.showinfo("Nothing to convert",
                                "No supported photos found in what you chose.")
            return None
        if not HEIF_OK and any(p.suffix.lower() in HEIF_EXTS for p in files):
            messagebox.showerror(
                "One extra install needed for HEIC",
                "iPhone HEIC photos need the pillow-heif package.\n\n"
                "Open a terminal, run\n\n        pip install pillow-heif\n\n"
                "then start this tool again.")
            return None
        if any(p.suffix.lower() == ".avif" for p in files) \
                and not features.check("avif"):
            messagebox.showerror(
                "AVIF needs a newer Pillow",
                "Open a terminal, run\n\n        pip install --upgrade "
                "pillow\n\nthen start this tool again.")
            return None
        records, failures = analyse(files)
        for src, why in failures:
            self._append(f"FAILED  {src.name}: {why}")
        fmt, max_edge, quality, ext = resolve_settings(
            self.mode_var.get() == "ai")
        plan_names(records, snake_case(self.label_var.get()), ext, self.outdir)
        return records, fmt, max_edge, quality

    def preview(self):
        if self.running:
            return
        self._clear_text()
        prepared = self._prepare()
        if not prepared:
            return
        records = prepared[0]
        for rec in records:
            note = "" if rec["origin"] == "exif" \
                else "   (file date: no usable EXIF)"
            self._append(f"{rec['src'].name}  ->  {rec['dest'].name}{note}")
        self._append(f"\npreview only - nothing written yet. Convert will "
                     f"write {len(records)} file(s).")

    def convert(self):
        if self.running:
            return
        self._clear_text()
        prepared = self._prepare()
        if not prepared:
            return
        records, fmt, max_edge, quality = prepared
        if self.outdir:
            self.outdir.mkdir(parents=True, exist_ok=True)
        self.running = True
        self.preview_btn.state(["disabled"])
        self.convert_btn.state(["disabled"])
        threading.Thread(target=self._work,
                         args=(records, fmt, max_edge, quality),
                         daemon=True).start()
        self.root.after(100, self._poll)

    def _work(self, records, fmt, max_edge, quality):
        done, folder = 0, None
        for rec in records:
            note = "" if rec["origin"] == "exif" \
                else "   (file date: no usable EXIF)"
            try:
                convert(rec["src"], rec["dest"], fmt, max_edge, quality)
            except Exception as exc:
                rec["dest"].unlink(missing_ok=True)
                self.q.put(f"FAILED  {rec['src'].name}: {exc}")
                continue
            done += 1
            folder = rec["dest"].parent
            self.q.put(f"{rec['src'].name}  ->  {rec['dest'].name}{note}")
        self.q.put(("done", done, len(records), folder))

    def _poll(self):
        while True:
            try:
                item = self.q.get_nowait()
            except queue.Empty:
                self.root.after(100, self._poll)
                return
            if isinstance(item, tuple):
                _, done, total, folder = item
                self._append(f"\n{done} of {total} file(s) converted; "
                             "originals untouched")
                self.running = False
                self.preview_btn.state(["!disabled"])
                self.convert_btn.state(["!disabled"])
                if folder and done and self.open_when_done:
                    os.startfile(folder)  # show the results in Explorer
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
