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
back to a lower-quality method.

Examples
--------
Auto-detect two colours and snap them to the brand palette:

    python tools/trace_reference.py ref.png out.svg --snap

Specify colours and group names explicitly:

    python tools/trace_reference.py ref.png out.svg \
        --colors "#27221E,#F15E4B" --labels "letterforms_ink,crossbar_ember"
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile

try:
    from PIL import Image
except ImportError:
    sys.exit(
        "Pillow is not installed. This script needs it for colour separation.\n"
        "  pip install pillow"
    )

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

DITHER_NONE = getattr(getattr(Image, "Dither", Image), "NONE")

INKSCAPE_CANDIDATES = [
    r"C:\Program Files\Inkscape\bin\inkscape.exe",
    r"C:\Program Files (x86)\Inkscape\bin\inkscape.exe",
    "/Applications/Inkscape.app/Contents/MacOS/inkscape",
    "/usr/bin/inkscape",
    "/usr/local/bin/inkscape",
]


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


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Trace a flat raster reference into a colour-separated SVG.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
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

    inkscape = find_inkscape(args.inkscape)
    image = Image.open(args.reference).convert("RGB")
    size = image.size
    print(f"reference : {args.reference} ({size[0]}x{size[1]})")

    if args.background:
        background = hex_to_rgb(args.background)
    else:
        background = max(image.getcolors(size[0] * size[1]) or [], key=lambda t: t[0])[1]
    print(f"background: {rgb_to_hex(background)}")

    if args.colors:
        targets = [hex_to_rgb(c) for c in args.colors.split(",")]
    else:
        targets = detect_colours(image, args.count, background)
        if not targets:
            sys.exit("No colours found distinct from the background.")
        if args.snap:
            snapped = []
            for colour in targets:
                name = min(BRAND, key=lambda k: distance(colour, hex_to_rgb(BRAND[k])))
                print(f"  snap {rgb_to_hex(colour)} -> {BRAND[name]} ({name})")
                snapped.append(hex_to_rgb(BRAND[name]))
            targets = snapped
    print("colours   : " + ", ".join(rgb_to_hex(c) for c in targets))

    if args.labels:
        labels = [s.strip() for s in args.labels.split(",")]
        if len(labels) != len(targets):
            sys.exit(f"Got {len(labels)} labels for {len(targets)} colours.")
    else:
        labels = [f"layer_{i}_{rgb_to_hex(c).lstrip('#').lower()}"
                  for i, c in enumerate(targets, start=1)]

    with tempfile.TemporaryDirectory() as work:
        masks = build_masks(image, targets, background, work)
        traced, kept_colours, kept_labels = [], [], []
        for (mask_path, pixels), colour, label in zip(masks, targets, labels):
            data = trace(inkscape, mask_path, size, args.speckles,
                         args.smooth_corners, args.optimize)
            if not data:
                print(f"  ! {label}: nothing traced ({pixels} px) - skipped")
                continue
            nodes = len(re.findall(r"[MmCcLlSsQqTtAaHhVv]", data))
            subpaths = len(re.findall(r"[Mm]", data))
            print(f"  {label}: {pixels} px -> {subpaths} subpath(s), {nodes} nodes")
            traced.append(data)
            kept_colours.append(rgb_to_hex(colour))
            kept_labels.append(label)

        if not traced:
            sys.exit("Nothing was traced. Check --colors against the reference.")

        os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
        assemble(traced, kept_colours, kept_labels, size, args.output, args.root_label)

    tighten(inkscape, args.output)
    print(f"wrote     : {args.output}")

    if not args.no_check:
        check = os.path.splitext(args.output)[0] + "_check.png"
        subprocess.run(
            [inkscape, args.output, "--export-type=png", "--export-width=1200",
             f"--export-filename={check}"], capture_output=True, text=True, check=False)
        if os.path.exists(check):
            print(f"self-check: {check}")
            print("Compare it against the reference before treating the SVG as usable.")


if __name__ == "__main__":
    main()
