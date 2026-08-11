#!/usr/bin/env python3
"""GAP's Vega-Lite chart layer: brand theme, render pipeline, title discipline.

Why this exists
---------------
`build_site_figures.py` composes SVG by hand — every coordinate a literal,
text wrapping a width estimate. That is fine for the stat strips it was
written for and it cannot draw a chart: no scales, no axes, no marks, so
anything past three bars means writing fresh arithmetic. This module is
the other half. Vega-Lite declares a chart as data plus encodings; this
file supplies the GAP theme, renders it without a browser, and adds the
brand furniture Vega-Lite has no opinion about.

The division of labour is deliberate. **Vega-Lite draws the plot; this
module draws everything around it.** Vega-Lite is very good at scales,
axes, marks and legends, and poor at editorial layout — the source line,
the caveat block, the dashed "not published" box. Fighting it for those
would be worse than the hand-composed route, so it is not asked to.

Palette comes from `palette_check.py`, which is the single source of
truth: tier 1 for highlight-against-context, tier 2 for up to five
nominal categories, tier 3 for ordered data. Importing rather than
copying means a palette correction reaches every chart.

Titles
------
A chart title states the finding, not the contents. "AI adoption by firm
size" is a label: it names the axes and leaves the reader to work out why
they are looking. "Small firms adopt AI at a third the rate of large
ones" is a title: read alone, it carries the point. `check_title()`
enforces the distinction as far as a machine can — it catches the common
label shapes and warns — but the judgement is the writer's, and the
warning is advisory for that reason.

Rendering
---------
`vl-convert` embeds a JavaScript runtime and the Vega-Lite compiler, so
there is no Node, no browser and no network in the path. It measures text
against fonts installed on this machine, which is why Public Sans comes
out correct rather than estimated. It also rasterises plain SVG, which
gives the repo an SVG-to-PNG converter it otherwise lacks.

Requirements: Python with `vl-convert-python`. Pillow is not needed.

Usage
-----
    from gap_chart import render, theme, TIER
    render(spec, "docs/assets/figures/name")   # writes light + dark SVG
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from palette_check import PALETTE, SETTLED           # noqa: E402

FONT = "Public Sans"

# UK number formatting. d3-format takes the currency symbol from a locale
# rather than from the format string, so "£,d" is not a valid spec —
# "$,d" plus this locale is what puts a pound sign on an axis. It is a
# render-time argument to vl-convert, *not* spec config: setting
# `numberFormatLocale` inside the config is silently ignored and the axis
# comes out in dollars, which is how this was found.
UK_LOCALE = {"decimal": ".", "thousands": ",", "grouping": [3],
             "currency": ["£", ""]}

# The palette tiers, named for what they encode rather than for their
# index, so a spec reads as a decision: TIER["ordered"], not TIER[3].
TIER = {
    "highlight_light": [h for _, h in SETTLED["tier1_light"]],
    "highlight_dark":  [h for _, h in SETTLED["tier1_dark"]],
    "category_light":  [h for _, h in SETTLED["tier2_light"]],
    "category_dark":   [h for _, h in SETTLED["tier2_dark"]],
    "ordered_light":   [h for _, h in SETTLED["tier3_light"]],
    "ordered_dark":    [h for _, h in SETTLED["tier3_dark"]],
}


# ------------------------------------------------------------------ theme

def theme(dark=False):
    """Vega-Lite config carrying the brand. Applied once here rather than
    per-chart, the same role styles.xml plays for the .docx pipeline."""
    ink, paper = PALETTE["ink"], PALETTE["paper"]
    fg     = paper if dark else ink
    bg     = ink if dark else paper
    muted  = PALETTE["mist"] if dark else PALETTE["graphite"]
    faint  = PALETTE["stone"]
    return {
        "background": bg,
        "font": FONT,
        "title": {
            "font": FONT, "fontSize": 25, "fontWeight": 700, "color": fg,
            "anchor": "start", "offset": 18, "dx": 6,
            "subtitleFont": FONT, "subtitleFontSize": 15,
            "subtitleColor": muted, "subtitleLineHeight": 21,
            "subtitlePadding": 10,
        },
        "axis": {
            "labelFont": FONT, "labelFontSize": 13, "labelColor": muted,
            "titleFont": FONT, "titleFontSize": 13, "titleFontWeight": 600,
            "titleColor": muted, "titlePadding": 10,
            "domainColor": faint, "tickColor": faint,
            "gridColor": faint, "gridOpacity": 0.22, "gridDash": [2, 3],
            "labelPadding": 6,
        },
        "legend": {
            "labelFont": FONT, "labelFontSize": 13, "labelColor": fg,
            "titleFont": FONT, "titleFontSize": 13, "titleColor": muted,
            "titleFontWeight": 600, "symbolType": "circle", "symbolSize": 130,
            "orient": "top", "direction": "horizontal", "offset": 8,
            "titleLimit": 0,
            # Legend symbols default to partial opacity, so the key came
            # out a paler colour than the marks it was labelling — which
            # is exactly the kind of mismatch that makes a reader doubt
            # the mapping.
            "symbolOpacity": 1, "symbolStrokeWidth": 0,
        },
        "text": {"font": FONT, "fontSize": 13, "color": fg},
        "view": {"stroke": None},
        "range": {"category": TIER["category_dark" if dark else "category_light"],
                  "ordinal":  TIER["ordered_dark" if dark else "ordered_light"]},
    }


def footer(text, dark=False):
    """The source-and-date line, as a Vega-Lite layer. Every outward
    graphic carries its own attribution because in the publishing funnel
    most viewers only ever see the image."""
    return {
        "mark": {"type": "text", "align": "left", "baseline": "top",
                 "font": FONT, "fontSize": 11.5, "dy": 22,
                 "color": PALETTE["stone"], "lineHeight": 15},
        "encoding": {"text": {"value": text.split("\n")}},
    }


# ------------------------------------------------------------------ title

LABEL_STARTS = (
    "chart of", "graph of", "breakdown of", "overview of", "summary of",
    "comparison of", "distribution of", "analysis of", "figures for",
)


def check_title(title):
    """Advisory check against the label/title rule. Returns a list of
    warnings; never raises. A machine can spot the shapes a label usually
    takes — no verb, an ' by ' axis-naming construction, an opening
    'Overview of' — but it cannot tell whether a sentence carries an
    insight, so this warns and leaves the call to the writer."""
    warn = []
    t = title.strip()
    low = t.lower()
    if low.startswith(LABEL_STARTS):
        warn.append("opens like a label ('%s...')" % t.split()[0])
    if " by " in low and len(t.split()) <= 7:
        warn.append("' by ' with a short title usually names axes "
                    "rather than stating a finding")
    # A finding is a claim, and a claim needs a verb. Crude, but the
    # noun-phrase title is the single most common label shape.
    verbish = ("is", "are", "was", "were", "has", "have", "runs", "run",
               "falls", "fall", "rises", "rise", "costs", "cost", "adopts",
               "adopt", "stops", "stop", "grew", "grows", "beats", "leaves",
               "buys", "gets", "goes", "makes", "takes", "counts", "promised",
               "reported", "published", "spent", "trains", "trained")
    if not any(w.strip(",.;:").lower() in verbish for w in t.split()):
        warn.append("no verb — reads as a noun phrase, which is a label")
    if len(t.split()) < 4:
        warn.append("very short; unlikely to carry a finding")
    return warn


# ----------------------------------------------------------------- render

def render(spec, out_stem, width=760, height=400, source=None,
           variants=("light", "dark"), verbose=True):
    """Render one spec into brand light and dark SVGs.

    `out_stem` is a path without extension; `_dark` is appended for the
    dark variant, matching what the site's <picture> elements expect.
    """
    import vl_convert as vlc

    title = spec.get("title", {})
    if isinstance(title, dict) and title.get("text"):
        for w in check_title(title["text"]):
            print(f"  title warning: {w}", file=sys.stderr)

    written = []
    for variant in variants:
        dark = variant == "dark"
        s = json.loads(json.dumps(spec))          # deep copy per variant
        s["config"] = theme(dark)
        s.setdefault("width", width)
        s.setdefault("height", height)
        if source:
            layers = s.pop("layer", None)
            if layers is None:
                inner = {k: s.pop(k) for k in ("mark", "encoding")
                         if k in s}
                layers = [inner]
            s["layer"] = layers
            s["resolve"] = s.get("resolve", {})
        svg = vlc.vegalite_to_svg(s, format_locale=UK_LOCALE)
        _verify(svg, s, variant)
        if source:
            svg = _append_source(svg, source, dark)
        path = f"{out_stem}{'_dark' if dark else ''}.svg"
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(svg)
        written.append(path)
        if verbose:
            print(f"  wrote {path}")
    return written


def _verify(svg, spec, variant):
    """Refuse to write a chart that did not fully render.

    Vega reports errors from its embedded JavaScript runtime by printing
    to stderr and carrying on, so a bad axis format or a missing field
    produces a *plausible* SVG with pieces silently absent — the exact
    shape of failure this project's self-checks exist to catch. An
    invalid d3 format string, for instance, drops every tick label while
    leaving the axis line in place. Cheap structural checks catch that
    class without needing to see the picture.
    """
    n_text = svg.count("<text")
    title = spec.get("title", {})
    want = title.get("text") if isinstance(title, dict) else None
    problems = []
    if want:
        # Vega splits long titles across tspans, so match on first words.
        head = " ".join(want.split()[:3])
        if head not in svg:
            problems.append(f"title {head!r} missing from output")
    n_layers = len(spec.get("layer", [])) or 1
    if n_text < 2 * n_layers:
        problems.append(f"only {n_text} text elements for {n_layers} "
                        f"layer(s) — axis labels or marks likely dropped")
    if len(svg) < 800:
        problems.append(f"output only {len(svg)} bytes")
    if problems:
        raise SystemExit(
            f"chart render failed ({variant}): " + "; ".join(problems) +
            "\n  Check the Vega ERROR lines above — the SVG was not written."
        )


def _append_source(svg, source, dark):
    """Add the source-and-date line beneath the plot. Done to the rendered
    SVG rather than as a Vega-Lite mark because a text mark lives inside
    the data rectangle, gets clipped by the view, and moves when the
    scales change — the furniture must not depend on the data."""
    import re
    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    if not m:
        return svg
    w, h = float(m.group(1)), float(m.group(2))
    lines = source.split("\n")
    extra = 16 + 15 * len(lines)
    nh = h + extra
    svg = svg.replace(f'viewBox="0 0 {m.group(1)} {m.group(2)}"',
                      f'viewBox="0 0 {m.group(1)} {nh:g}"', 1)
    svg = re.sub(r'(<svg[^>]*?)height="[\d.]+"', rf'\1height="{nh:g}"', svg, 1)
    bg = PALETTE["ink"] if dark else PALETTE["paper"]
    out = [f'<rect x="0" y="{h:g}" width="{w:g}" height="{extra:g}" fill="{bg}"/>']
    y = h + 14
    for ln in lines:
        out.append(f'<text x="6" y="{y:g}" font-family="{FONT}, Arial, sans-serif" '
                   f'font-size="11.5" fill="{PALETTE["stone"]}">'
                   f'{_esc(ln)}</text>')
        y += 15
    return svg.replace("</svg>", "\n".join(out) + "\n</svg>")


def _esc(s):
    import html
    return html.escape(s, quote=True)


# ------------------------------------------------------- coverage check

def check_coverage(rows, x_field, cat_field, verbose=True):
    """Refuse a comparison the data cannot actually support.

    A chart that colours by category invites the reader to compare
    categories. Where some level of the x variable carries only one
    category, no comparison exists there — but the eye reads the whole
    plot as one comparison and fills the gap in with the pattern it can
    see. The chart is then making a claim its data does not contain.

    Found on the first figure built with this module. The VRAM scatter
    was meant to show Intel undercutting its competitors on price per
    gigabyte; at 12 GB and at 32 GB it plotted Intel cards with nothing
    beside them, so exactly the comparison the figure existed to make was
    the one missing. The chart was structurally sound and the underlying
    research was a rough draft that said so on its first line.

    This catches the mechanical half — an incomplete comparison grid. The
    other half is judgement and belongs to the standing rule: finish and
    re-read the research before drawing anything from it.
    """
    levels = {}
    for r in rows:
        levels.setdefault(r[x_field], set()).add(r[cat_field])
    all_cats = set()
    for cats in levels.values():
        all_cats |= cats

    thin, partial = [], []
    for level in sorted(levels, key=lambda v: (isinstance(v, str), v)):
        cats = levels[level]
        if len(cats) < 2:
            thin.append((level, next(iter(cats))))
        elif cats != all_cats:
            partial.append((level, sorted(all_cats - cats)))

    if verbose:
        if not thin and not partial:
            print(f"  coverage check: all {len(levels)} {x_field} levels "
                  f"carry every category")
        for level, only in thin:
            print(f"  COVERAGE: {x_field}={level} has only '{only}' — "
                  f"no comparison is possible at this level")
        for level, missing in partial:
            print(f"  coverage: {x_field}={level} missing "
                  f"{', '.join(repr(m) for m in missing)}")
    return thin, partial


# ------------------------------------------------------- geometry check

def check_labels(svg_path, gap=1.0, verbose=True):
    """Find overlapping text in a rendered chart.

    The project's standing rule is that a generated visual asset gets a
    geometry self-check, because a script cannot see its own output. For
    the hand-composed figures that meant measuring in a browser. Here it
    means walking the rendered SVG: Vega positions text with nested
    translate() transforms and a text-anchor, so absolute position is the
    accumulated translation plus an anchor correction.

    Written after the first chart built on this module put all six data
    labels directly on top of their own points — a conditional offset
    that Vega silently ignored, invisible in the spec and obvious in the
    picture.

    Width is estimated from character count, so this is **advisory**: it
    prints and returns findings rather than raising. A fuzzy measure that
    blocked a build would teach the next person to skip it, which is the
    same reasoning behind the pre-commit hook's advisory tier.
    """
    import re
    import xml.etree.ElementTree as ET

    SVG = "{http://www.w3.org/2000/svg}"
    tree = ET.parse(svg_path)
    items = []

    def walk(node, ox, oy):
        t = node.get("transform", "")
        for dx, dy in re.findall(r"translate\(([-\d.]+)[, ]+([-\d.]+)\)", t):
            ox, oy = ox + float(dx), oy + float(dy)
        if node.tag == f"{SVG}text" and (node.text or "").strip():
            # Rotated text (Vega sets the y-axis title this way) would need
            # its box transposed; measuring it as horizontal reports a
            # collision with every tick label it passes. Skipped rather
            # than mismeasured.
            if "rotate" in t:
                for child in node:
                    walk(child, ox, oy)
                return
            # Text may be placed by x/y attributes instead of a transform —
            # the source line added by _append_source is. Missing this made
            # the checker stack every such line at the origin and report
            # them as overlapping each other.
            ox += float(node.get("x", 0) or 0)
            oy += float(node.get("y", 0) or 0)
            txt = node.text.strip()
            size = float(re.sub(r"[^\d.]", "",
                                node.get("font-size", "13") or "13") or 13)
            # Public Sans averages a little over half the em across mixed
            # case; generous rather than tight, so near-misses surface.
            w = len(txt) * size * 0.55
            anchor = node.get("text-anchor", "start")
            x = ox - w / 2 if anchor == "middle" else (
                ox - w if anchor == "end" else ox)
            items.append((txt, x, oy - size * 0.78, w, size))
        for child in node:
            walk(child, ox, oy)

    walk(tree.getroot(), 0.0, 0.0)

    hits = []
    for i in range(len(items)):
        ta, xa, ya, wa, sa = items[i]
        for j in range(i + 1, len(items)):
            tb, xb, yb, wb, sb = items[j]
            if (xa < xb + wb + gap and xb < xa + wa + gap and
                    ya < yb + sb + gap and yb < ya + sa + gap):
                hits.append((ta, tb))
    if verbose:
        if hits:
            print(f"  label check: {len(hits)} overlapping pair(s) in "
                  f"{os.path.basename(svg_path)}")
            for a, b in hits[:8]:
                print(f"    {a!r} overlaps {b!r}")
        else:
            print(f"  label check: {len(items)} labels, no overlaps "
                  f"({os.path.basename(svg_path)})")
    return hits


def to_png(svg_path, png_path, scale=2.0):
    """Rasterise for Word documents and LinkedIn, which take no SVG."""
    import vl_convert as vlc
    with open(svg_path, encoding="utf-8") as fh:
        png = vlc.svg_to_png(fh.read(), scale=scale)
    with open(png_path, "wb") as fh:
        fh.write(png)
    print(f"  wrote {png_path}")


if __name__ == "__main__":
    print(__doc__.splitlines()[0])
    print("\nA library, not a command. Import it from a figure script.")
    print(f"\nTiers available: {', '.join(TIER)}")
    for t in ("AI adoption by firm size",
              "Small firms adopt AI at a third the rate of large ones"):
        w = check_title(t)
        print(f"\n  {t!r}\n    {'; '.join(w) if w else 'reads as a finding'}")
