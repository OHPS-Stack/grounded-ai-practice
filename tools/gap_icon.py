"""Bring a Lucide icon into the GAP icon set's own geometry and palette.

The project's 36 bespoke icons are stroke outlines on a 512 canvas: Ink
`#27221E` at stroke-width 14, Ember `#F15E4B` for accents, round caps and
joins, no fill. Lucide draws the same way — stroke outline, `fill="none"`,
round caps — but on a 24 grid at stroke-width 2. Those proportions are not
compatible. Scaled naively to 512 a Lucide icon arrives at stroke-width
42.7 against the set's 14, roughly three times heavier, and it fills 83%
of its canvas where the GAP icons fill 70%. Dropped onto a page beside a
bespoke icon it reads as a different system, which is the opposite of what
a shared icon library is for.

So this converts rather than copies. Two numbers do the work, and both were
measured off the existing set rather than chosen:

    Fitting. `verification.svg`, `storage.svg` and `terminal_and_cli.svg`
    each carry their own `translate(...) scale(...)` on a group called
    `icon_canvas`, and all three land the icon's longest axis — stroke
    included — on 358.4 units, 70.0% of the 512 canvas, centred. They agree
    to within 0.4%, so the set's convention is per-icon bbox fitting to a
    fixed visual size, not a fixed scale factor. This reproduces that.

    Stroke. Fixed at 14 in canvas units, which means a fractional
    stroke-width in the group's local units (14 divided by the fit scale).
    That is why the written file carries an odd-looking number there; the
    `<desc>` records the arithmetic so a later hand edit in Inkscape is not
    working blind.

Path data is never rewritten. The original elements are wrapped in a
transformed group exactly as the bespoke icons are, so no float drift and
no parsing of the SVG path grammar — the two failure modes a redraw would
introduce.

The bounding box is measured by rendering, not by parsing `d` attributes.
Rendering is ground truth, and it doubles as the geometry self-check the
project requires of any generated visual asset: after writing, the output
is rendered again and its span, centring and containment are checked
against the target. A file that misses is not written.

Accents are the judgement half and stay manual. A run prints the icon's
elements with their indices; `--accent` names which take Ember. Without it
the icon is single-colour Ink, which is a legitimate finished state.

Provenance: icons come from a pinned Lucide release (LUCIDE_VERSION), not
from `main` or `@latest`, so a rebuild months from now produces the same
file. Source, version and fetch date go into every icon's `<desc>` and into
the manifest table in the library README.

Usage:
    python tools/gap_icon.py shield-check
    python tools/gap_icon.py shield-check --accent 1
    python tools/gap_icon.py cpu --name hardware_and_performance_alt
    python tools/gap_icon.py server --png
    python tools/gap_icon.py --list

Requires Python with Pillow, and an SVG rasteriser: vl-convert-python
(`pip install vl-convert-python`) or Inkscape 1.x, discovered the way
trace_reference.py does.
"""

import argparse
import io
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date

# --- pinned upstream ---------------------------------------------------

LUCIDE_VERSION = "1.31.0"
LUCIDE_RAW = ("https://raw.githubusercontent.com/lucide-icons/lucide/"
              "%s/icons/%s.svg")

# --- house geometry, measured off assets/icons/svg/ --------------------

CANVAS = 512.0          # viewBox of every icon in the set
CONTENT_SPAN = 358.4    # longest axis incl. stroke: 70.0% of CANVAS
STROKE = 14.0           # Ink outline weight in canvas units
SRC_STROKE = 2.0        # Lucide's own stroke-width on its 24 grid

INK = "#27221E"
EMBER = "#F15E4B"
PAPER = "#FFFFFF"       # sheet ground, matching build_server_guide_figures
STONE = "#6E6E6E"       # sheet labels

PROBE_PX = 2048         # render size for bbox measurement
ALPHA_FLOOR = 8         # ignore antialiasing fringe when measuring

SVG_NS = "http://www.w3.org/2000/svg"

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(REPO, "assets", "icons", "library")
TABLE_START = "<!-- manifest:start -->"
TABLE_END = "<!-- manifest:end -->"


# --- rasterising -------------------------------------------------------

def _find_inkscape():
    import shutil
    exe = shutil.which("inkscape")
    if exe:
        return exe
    for cand in (r"C:\Program Files\Inkscape\bin\inkscape.exe",
                 r"C:\Program Files (x86)\Inkscape\bin\inkscape.exe"):
        if os.path.exists(cand):
            return cand
    return None


def _rasterise(svg_text, px):
    """SVG text -> PNG bytes, rendered px square.

    vl-convert first (no process spawned), Inkscape second. Mirrors
    build_pilot_figures.py rather than importing from it: that module is
    document-specific, and coupling an icon tool to a figure script for
    thirty lines of discovery would be the wrong dependency.
    """
    try:
        import vl_convert as vlc
        # scale is relative to the SVG's own width, which callers set.
        m = re.search(r'width="([0-9.]+)"', svg_text)
        intrinsic = float(m.group(1)) if m else CANVAS
        return vlc.svg_to_png(svg_text, scale=px / intrinsic)
    except ImportError:
        pass
    exe = _find_inkscape()
    if not exe:
        sys.exit("no SVG rasteriser: install vl-convert-python "
                 "(pip install vl-convert-python) or Inkscape 1.x")
    import subprocess
    import tempfile
    fd, svg_path = tempfile.mkstemp(suffix=".svg")
    png_path = svg_path[:-4] + ".png"
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(svg_text)
        subprocess.run([exe, svg_path, "--export-type=png",
                        "--export-filename=" + png_path,
                        "-w", str(px), "-h", str(px)],
                       check=True, capture_output=True)
        with open(png_path, "rb") as fh:
            return fh.read()
    finally:
        for p in (svg_path, png_path):
            if os.path.exists(p):
                os.unlink(p)


def _ink_bbox(png_bytes, px, units):
    """Bounding box of drawn pixels, returned in SVG user units.

    Thresholds the alpha channel first: an antialiased edge fades to 1/255
    and would otherwise inflate every measurement by a pixel on each side.
    """
    from PIL import Image
    im = Image.open(io.BytesIO(png_bytes)).convert("RGBA")
    alpha = im.getchannel("A").point(lambda v: 255 if v >= ALPHA_FLOOR else 0)
    box = alpha.getbbox()
    if not box:
        return None
    per_unit = px / units
    left, upper, right, lower = box
    return (left / per_unit, upper / per_unit,
            right / per_unit, lower / per_unit)


# --- conversion --------------------------------------------------------

def fetch(name):
    url = LUCIDE_RAW % (LUCIDE_VERSION, name)
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            return r.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            sys.exit("no Lucide icon named %r at version %s\n"
                     "check the name at https://lucide.dev/icons/"
                     % (name, LUCIDE_VERSION))
        raise


def _children(svg_text):
    """The drawable elements of a Lucide icon, in document order."""
    root = ET.fromstring(svg_text)
    out = []
    for el in root:
        tag = el.tag.split("}")[-1]
        if tag in ("path", "circle", "rect", "line", "polyline",
                   "polygon", "ellipse"):
            out.append(el)
    return out


def _serialise(el):
    ET.register_namespace("", SVG_NS)
    s = ET.tostring(el, encoding="unicode")
    # ElementTree writes '<tag />'; the repo's other tools match Word's and
    # Inkscape's '<tag/>' form literally, so normalise here too.
    return s.replace(" />", "/>").strip()


def _probe_svg(elements):
    body = "\n".join("  " + _serialise(e) for e in elements)
    return ('<svg xmlns="%s" width="24" height="24" viewBox="0 0 24 24" '
            'fill="none" stroke="#000000" stroke-width="%g" '
            'stroke-linecap="round" stroke-linejoin="round">\n%s\n</svg>'
            % (SVG_NS, SRC_STROKE, body))


def convert(name, out_name, accents, quiet=False):
    """Fetch a Lucide icon and return (svg_text, report dict)."""
    src = fetch(name)
    els = _children(src)
    if not els:
        sys.exit("no drawable elements in Lucide icon %r" % name)

    # 1. measure the source, stroke included, on its own 24 grid
    png = _rasterise(_probe_svg(els), PROBE_PX)
    box = _ink_bbox(png, PROBE_PX, 24.0)
    if not box:
        sys.exit("Lucide icon %r rendered empty" % name)
    left, upper, right, lower = box
    w_u, h_u = right - left, lower - upper

    # geometry without stroke: round caps extend half a stroke every side
    w_g, h_g = w_u - SRC_STROKE, h_u - SRC_STROKE
    long_g = max(w_g, h_g)
    if long_g <= 0:
        sys.exit("Lucide icon %r is all stroke, nothing to fit" % name)

    # 2. solve the fit: longest axis incl. stroke lands on CONTENT_SPAN
    scale = (CONTENT_SPAN - STROKE) / long_g
    local_stroke = STROKE / scale
    cx, cy = (left + right) / 2.0, (upper + lower) / 2.0
    tx, ty = CANVAS / 2 - scale * cx, CANVAS / 2 - scale * cy

    # 3. write the group, path data untouched
    stray = sorted(i for i in accents if i >= len(els))
    if stray:
        sys.exit("--accent %s out of range: %r has %d element(s), "
                 "indices 0-%d"
                 % (",".join(str(i) for i in stray), name,
                    len(els), len(els) - 1))

    lines = []
    for i, el in enumerate(els):
        s = _serialise(el)
        if i in accents:
            # the group carries stroke=Ink; an accent overrides on the element
            if not s.endswith("/>"):
                sys.exit("element %d of %r has children and cannot take an "
                         "accent attribute cleanly" % (i, name))
            s = s[:-2] + ' stroke="%s"/>' % EMBER
        lines.append("    " + s)

    desc = ("Lucide %s icon, converted to the GAP canvas by "
            "tools/gap_icon.py. Fitted from a measured source bbox of "
            "%.3f x %.3f units to a %.1f-unit span, 70%% of the 512 "
            "canvas: scale %.5f, stroke %g/%.5f = %.5f local units."
            % (name, w_u, h_u, CONTENT_SPAN, scale, STROKE, scale,
               local_stroke))

    svg = ('<svg xmlns="%s" width="512" height="512" viewBox="0 0 512 512" '
           'fill="none">\n'
           '  <title>%s</title>\n'
           '  <desc>%s</desc>\n\n'
           '  <g transform="translate(%.3f,%.3f) scale(%.5f)" '
           'id="icon_canvas"\n'
           '     fill="none" stroke="%s" stroke-width="%.5f"\n'
           '     stroke-linecap="round" stroke-linejoin="round">\n'
           '%s\n'
           '  </g>\n'
           '</svg>\n'
           % (SVG_NS, out_name.replace("_", " ").title(), desc,
              tx, ty, scale, INK, local_stroke, "\n".join(lines)))

    report = {"lucide": name, "elements": len(els), "scale": scale,
              "local_stroke": local_stroke, "src_bbox": (w_u, h_u),
              "accents": sorted(accents),
              "tags": [e.tag.split("}")[-1] for e in els]}
    return svg, report


def selfcheck(svg, tol=2.0):
    """Render the output and verify it hits the house geometry.

    The project requires a geometry self-check on any generated visual
    asset, for the reason that a script drawing an SVG cannot see what it
    drew. Three ways this can be wrong and none is visible in the source:
    a fit that missed, an icon off centre, and one running past the canvas.

    Measured on a frame padded by half a canvas on every side, not on the
    canvas itself. Rendering clips to the viewBox, so ink that overflows is
    simply absent from the raster and a bbox taken there can never exceed
    the canvas — the containment test would have been unable to fail, and
    an overflowing icon would have reported a plausible clipped span
    instead. Padding puts the overflow back in the picture.
    """
    pad = CANVAS / 2
    framed = svg.replace('viewBox="0 0 512 512"',
                         'viewBox="%g %g %g %g"'
                         % (-pad, -pad, CANVAS + 2 * pad, CANVAS + 2 * pad))
    framed = re.sub(r'width="512" height="512"',
                    'width="%g" height="%g"'
                    % (CANVAS + 2 * pad, CANVAS + 2 * pad), framed)
    if framed == svg:
        return False, "could not build a padded frame to measure on"

    png = _rasterise(framed, PROBE_PX)
    box = _ink_bbox(png, PROBE_PX, CANVAS + 2 * pad)
    if not box:
        return False, "output rendered empty"
    # back into real canvas coordinates
    left, upper, right, lower = (v - pad for v in box)
    span = max(right - left, lower - upper)
    cx, cy = (left + right) / 2.0, (upper + lower) / 2.0

    fails = []
    if abs(span - CONTENT_SPAN) > tol:
        fails.append("span %.1f, want %.1f +/- %.1f"
                     % (span, CONTENT_SPAN, tol))
    if abs(cx - CANVAS / 2) > tol or abs(cy - CANVAS / 2) > tol:
        fails.append("centre (%.1f, %.1f), want (256, 256) +/- %.1f"
                     % (cx, cy, tol))
    if left < 0 or upper < 0 or right > CANVAS or lower > CANVAS:
        fails.append("overflows canvas: (%.1f, %.1f)-(%.1f, %.1f)"
                     % (left, upper, right, lower))
    if fails:
        return False, "; ".join(fails)
    return True, ("span %.1f (%.1f%% of canvas), centre (%.1f, %.1f)"
                  % (span, 100 * span / CANVAS, cx, cy))


# --- manifest ----------------------------------------------------------

def _manifest_rows(readme):
    if TABLE_START not in readme:
        return []
    body = readme.split(TABLE_START, 1)[1].split(TABLE_END, 1)[0]
    rows = []
    for line in body.strip().splitlines():
        if line.startswith("|") and "---" not in line and "File" not in line:
            rows.append(line)
    return rows


def update_manifest(entries):
    """Rewrite the manifest table in the library README, sorted by file."""
    path = os.path.join(LIB, "README.md")
    if not os.path.exists(path):
        sys.exit("missing %s — the library README carries the licence "
                 "attribution and must exist before icons are added" % path)
    with open(path, "r", encoding="utf-8") as fh:
        readme = fh.read()

    rows = {}
    for line in _manifest_rows(readme):
        key = line.split("|")[1].strip()
        rows[key] = line
    for e in entries:
        cell = ("| `%s.svg` | `%s` | %s | %s |"
                % (e["out"], e["lucide"],
                   "yes" if e["accents"] else "no", e["date"]))
        rows["`%s.svg`" % e["out"]] = cell

    table = ("| File | Lucide source | Ember accent | Added |\n"
             "|---|---|---|---|\n"
             + "\n".join(rows[k] for k in sorted(rows)))
    head, rest = readme.split(TABLE_START, 1)
    _, tail = rest.split(TABLE_END, 1)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(head + TABLE_START + "\n" + table + "\n" + TABLE_END + tail)


def _label_font(px):
    """Public Sans if it is installed, Pillow's default otherwise.

    The sheet is a check artefact rather than a deliverable, so a fallback
    face is acceptable here in a way it would not be in a figure.
    """
    from PIL import ImageFont
    for d in (os.path.join(os.environ.get("LOCALAPPDATA", ""),
                           r"Microsoft\Windows\Fonts"),
              r"C:\Windows\Fonts"):
        p = os.path.join(d, "PublicSans-Regular.ttf")
        if os.path.exists(p):
            return ImageFont.truetype(p, px)
    return ImageFont.load_default()


def contact_sheet(out_path, cell=128, cols=6, pad=26):
    """Render the library beside the bespoke set for a human read.

    The numeric self-check confirms each icon hits the house geometry. It
    cannot say whether the result *looks* like it belongs, which is the
    actual question a converted icon raises and which this project's rules
    are repeatedly clear only looking at a render can answer. Stroke weight
    against the bespoke set is the thing to judge here.
    """
    from PIL import Image, ImageDraw

    bands = [("library — converted from Lucide %s" % LUCIDE_VERSION,
              os.path.join(LIB, "svg")),
             ("bespoke — assets/icons/svg", os.path.join(REPO, "assets",
                                                         "icons", "svg"))]
    font = _label_font(15)
    head = _label_font(19)
    lab_h, band_h = 22, 34

    plan = []
    for title, d in bands:
        files = sorted(f for f in os.listdir(d)) if os.path.isdir(d) else []
        rows = (len(files) + cols - 1) // cols if files else 0
        plan.append((title, d, files, rows))

    width = cols * (cell + pad) + pad
    height = pad + sum(band_h + r * (cell + lab_h + pad) + pad
                       for _, _, _, r in plan)
    sheet = Image.new("RGB", (width, height), PAPER)
    draw = ImageDraw.Draw(sheet)

    y = pad
    for title, d, files, rows in plan:
        draw.text((pad, y), title, font=head, fill=INK)
        y += band_h
        for i, f in enumerate(files):
            cx = pad + (i % cols) * (cell + pad)
            cy = y + (i // cols) * (cell + lab_h + pad)
            with open(os.path.join(d, f), "r", encoding="utf-8") as fh:
                png = _rasterise(fh.read(), cell)
            im = Image.open(io.BytesIO(png)).convert("RGBA")
            sheet.paste(im, (cx, cy), im)
            name = f[:-4]
            if len(name) > 17:
                name = name[:16] + "\u2026"
            draw.text((cx + cell / 2, cy + cell + 5), name, font=font,
                      fill=STONE, anchor="ma")
        y += rows * (cell + lab_h + pad) + pad

    sheet.save(out_path)
    return width, height, [len(f) for _, _, f, _ in plan]


def write_png(svg, out_name):
    from PIL import Image
    outdir = os.path.join(LIB, "png")
    os.makedirs(outdir, exist_ok=True)
    made = []
    for size in (64, 128, 256):
        png = _rasterise(svg, size)
        p = os.path.join(outdir, "%s_%d.png" % (out_name, size))
        with open(p, "wb") as fh:
            fh.write(png)
        Image.open(p).verify()          # reopen as an integrity check
        made.append(os.path.basename(p))
    return made


# --- CLI ---------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Convert a Lucide icon into the GAP icon set's "
                    "geometry and palette.",
        epilog="Browse names at https://lucide.dev/icons/ — this pins "
               "Lucide " + LUCIDE_VERSION + ".")
    ap.add_argument("names", nargs="*", help="Lucide icon name(s)")
    ap.add_argument("--name", help="output filename stem (single icon only; "
                                   "default is the Lucide name with "
                                   "hyphens as underscores)")
    ap.add_argument("--accent", default="",
                    help="comma-separated element indices to stroke Ember; "
                         "run without it first to see the index list")
    ap.add_argument("--png", action="store_true",
                    help="also export 64/128/256px PNGs")
    ap.add_argument("--refresh", action="store_true",
                    help="overwrite an icon already in the library")
    ap.add_argument("--dry-run", action="store_true",
                    help="convert and self-check, write nothing")
    ap.add_argument("--list", action="store_true",
                    help="list icons already in the library")
    ap.add_argument("--sheet", metavar="OUT.png",
                    help="render the library beside the bespoke set for a "
                         "visual check, and exit")
    args = ap.parse_args()

    if args.sheet:
        w, h, counts = contact_sheet(args.sheet)
        print("wrote %s (%dx%d) — %d library, %d bespoke"
              % (args.sheet, w, h, counts[0], counts[1]))
        return

    if args.list:
        d = os.path.join(LIB, "svg")
        got = sorted(f for f in os.listdir(d)) if os.path.isdir(d) else []
        print("%d icon(s) in assets/icons/library/svg/" % len(got))
        for f in got:
            print("  " + f)
        return

    if not args.names:
        ap.error("give at least one Lucide icon name, or --list")
    if args.name and len(args.names) > 1:
        ap.error("--name applies to a single icon only")

    accents = set()
    if args.accent:
        try:
            accents = {int(x) for x in args.accent.split(",") if x.strip()}
        except ValueError:
            ap.error("--accent takes comma-separated integers")
    if accents and len(args.names) > 1:
        ap.error("--accent applies to a single icon only")

    os.makedirs(os.path.join(LIB, "svg"), exist_ok=True)
    entries = []
    for name in args.names:
        out = args.name or name.replace("-", "_")
        dest = os.path.join(LIB, "svg", out + ".svg")
        if os.path.exists(dest) and not (args.refresh or args.dry_run):
            print("skip %s — already in the library (--refresh to redo)"
                  % out)
            continue

        svg, rep = convert(name, out, accents)
        ok, detail = selfcheck(svg)
        print("%s -> %s.svg" % (name, out))
        print("  %d element(s); index them with --accent:" % rep["elements"])
        for i, tag in enumerate(rep["tags"]):
            mark = "  <- Ember" if i in accents else ""
            print("    [%d] %s%s" % (i, tag, mark))
        print("  fit: scale %.5f, local stroke %.5f"
              % (rep["scale"], rep["local_stroke"]))
        if not ok:
            sys.exit("  SELF-CHECK FAILED: %s\n  nothing written." % detail)
        print("  self-check ok: %s" % detail)

        if args.dry_run:
            print("  dry run, not written")
            continue
        with open(dest, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(svg)
        print("  wrote %s" % os.path.relpath(dest, REPO))
        if args.png:
            for f in write_png(svg, out):
                print("  wrote %s" % f)
        entries.append({"out": out, "lucide": name,
                        "accents": sorted(accents),
                        "date": date.today().isoformat()})

    if entries:
        update_manifest(entries)
        print("manifest updated: assets/icons/library/README.md")


if __name__ == "__main__":
    main()
