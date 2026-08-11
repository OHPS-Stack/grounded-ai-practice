#!/usr/bin/env python3
"""Draw the landing-site figures — reproducible SVG infographics from logged data.

Why this exists
---------------
The public landing site (`docs/`) carries three data figures — the
promise-versus-count strip, the BridgeAI delivery strip and the OECD
adoption gap by firm size — plus the decorative 404 mark. Under the
data-driven figures rule in `CLAUDE.md`, outward graphics are produced
from a script with their data checked into the repo — never hand-drawn
numbers — and each data figure carries its own source-and-date line on
the image, because in the publishing funnel each element must stand
alone.

The first two are stat strips rather than plotted charts, and that is
a decision rather than a shortcut: earlier drafts plotted courses
against worker targets on a shared axis, which performed the very
conflation the page criticises. Where two figures are in different
units, the honest presentation separates them and names the missing
number between them.

The claim-verification flow and the practice-system diagram were
figures here once and are now native HTML on the page, built from the
brand icon set: real text beats drawn text for accessibility, for
responsive layout, and for staying consistent with the rest of the
page. Only content that is genuinely a chart is drawn here.

Every number here is transcribed from a logged, cited finding in
`research_log.md`; the entry references sit next to the data below. If a
figure's numbers change, the fix is a corrected constant and a re-run,
not an image edit.

How it works
------------
Pure standard library for the SVGs: each figure is composed as SVG text
at a fixed viewBox, in the brand palette, in light and dark variants
(`_dark` suffix) so the site can swap them with `prefers-color-scheme`.
Text wrapping uses a conservative width estimate rather than font
metrics, with generous margins, so fallback fonts on machines without
Public Sans do not overflow.

Self-check: before writing anything, every foreground/background pair
used is audited against WCAG 2.1 contrast thresholds (4.5:1 normal text,
3:1 large text). A failing pair aborts the build. The ratios print on
every run so the check is visible, not silent.

`--og` additionally composites the social-share card
(`og_card.png`, 1200x630) from the existing wordmark PNG export.
Requires Pillow and the Public Sans TTFs installed as user fonts; the
SVG figures need neither.

A build-step tool in the `embed_logo.py`/`build_server_guide_figures.py`
category: Claude or a build step runs it, so it stays command-line by the
Entry 049 decision (no GUI).

Usage
-----
    python tools/build_site_figures.py            # SVGs into docs/assets/figures/
    python tools/build_site_figures.py --og       # also build the share card
    python tools/build_site_figures.py --out DIR  # different destination
"""

import argparse
import html
import os
import sys

# ---------------------------------------------------------------- palette

PALETTE = {
    "ink":      "#27221E",
    "ember":    "#F15E4B",
    "sand":     "#F9E8DC",
    "paper":    "#F9F9F9",
    "mist":     "#EFEEED",
    "sage":     "#D5E2E1",
    "stone":    "#6E6E6E",
    "graphite": "#404040",
    # Midpoints of the ordered ramps. Ember->Ink on light figures,
    # Ember->Sand on dark; only the middle step is a colour the brand did
    # not already have. Both are computed in tools/palette_check.py, which
    # is where the ramps are defined and audited — these are here so the
    # contrast pairs below can name them.
    "ramp_light_mid": "#864235",
    "ramp_dark_mid":  "#FBA794",
}

FONT = "'Public Sans', 'Segoe UI', -apple-system, Arial, sans-serif"

# ------------------------------------------------------------------ data
#
# Transcribed from research_log.md; the entry numbers are the audit trail.

AMBITION_DATA = {
    # [AISKILLSBOOST26] via Entry 053: "1,001,147 AI training courses have
    # been completed according to course completion data shared with DSIT
    # by industry partners in January 2026", covering "all AI skills
    # courses delivered by partners since June 2025". Targets: 7.5m
    # workers announced June 2025, 10m framing from January 2026
    # (Entries 061/062).
    "announce": (2025, 6),
    "figure_at": (2026, 1),
    "courses": 1001147,
    "target_first": 7500000,
    "target_raised": 10000000,
    "horizon": (2030, 12),
    "caveat": (
        "Completions are self-reported by the delivery partners; one "
        "person can complete several courses, and the count includes "
        "the partners' own employees."
    ),
    "source": (
        "Sources: DSIT, AI Skills Boost explainer, 28 Jan 2026; DSIT and "
        "No.10, AI Opportunities delivery tracker, Jan 2026; gov.uk, "
        "Prime Minister's London Tech Week speech, Jun 2025 · "
        "groundedaipractice.co.uk · Aug 2026"
    ),
}

BRIDGEAI_DATA = {
    # Entry 044 (research log), [IUK-BRIDGEAI-YR3]: launched 2023, £100m
    # backed by UKRI's Technologies Mission Fund and Innovate UK; figures
    # to end of 2025.
    # The title now carries "£100 million programme", so the intro no
    # longer repeats it.
    "intro": (
        "The government's own AI programme, launched 2023 and run by "
        "Innovate UK. It funds projects and business support as well as "
        "training. From launch to the end of 2025:"
    ),
    "stats": [
        ("£74.6m", "of £100m allocated"),
        ("820+", "AI projects funded"),
        ("1,700+", "course completions"),
        ("126", "accreditations"),
    ],
    "caveat": "Figures are self-reported by the delivery consortium.",
    "source": (
        "Source: Innovate UK, BridgeAI Year 3 report, 2025 · "
        "groundedaipractice.co.uk · Aug 2026"
    ),
}

ADOPTION_DATA = {
    # [OECD-SMEAI25]: OECD, "AI adoption by small and medium-sized
    # enterprises", discussion paper for the G7, Dec 2025 — read directly
    # 2026-08-05, research_log.md Entry 065. Figures are for enterprises
    # with 10+ employees, 2024 or latest available year per country (the
    # UK's data point is 2020), unweighted average across member
    # countries.
    "bars": [
        ("Large firms (250+ employees)", 40.0),
        ("Medium firms (50–249)", 20.4),
        ("Small firms (10–49)", 11.9),
    ],
    "highlight": "Small firms (10–49)",
    "caveat": (
        "Firms with 10 or more employees, 2024 or latest available year "
        "per country (the UK's is 2020). OECD-wide, not UK-specific; "
        "firms under 10 employees are not counted."
    ),
    "source": (
        "Source: OECD, “AI adoption by small and medium-sized enterprises”, "
        "Dec 2025 · groundedaipractice.co.uk · Aug 2026"
    ),
}

SITE_STAMP = "groundedaipractice.co.uk · Aug 2026"

# ------------------------------------------------------------- contrast

def _lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hexcolor):
    h = hexcolor.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(fg, bg):
    l1, l2 = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


# Every (foreground, background, threshold, where-used) pair the figures
# rely on. 4.5 = normal text, 3.0 = large text (>= ~24px regular / 18.7px
# bold). Adding a colour use to a figure means adding its pair here.
CONTRAST_PAIRS = [
    ("ink", "paper", 4.5, "body text, light"),
    ("graphite", "paper", 4.5, "secondary text, light"),
    ("stone", "paper", 4.5, "source lines, light"),
    ("ember", "paper", 3.0, "large stat numbers, light"),
    ("ink", "sand", 4.5, "gap strip and callouts, light"),
    ("ink", "mist", 4.5, "cards and flow boxes, light"),
    ("ink", "sage", 4.5, "output cards, light"),
    ("paper", "ink", 4.5, "body text, dark"),
    ("mist", "ink", 4.5, "secondary text, dark"),
    ("ember", "ink", 3.0, "large stat numbers, dark"),
    ("paper", "graphite", 4.5, "raised strip text, dark"),
    # Ordered ramp marks. 3.0 is the graphical-object threshold (WCAG 2.1
    # SC 1.4.11), not the 4.5 text takes — a bar is not text.
    ("ramp_light_mid", "paper", 3.0, "adoption ramp, light"),
    ("ink", "paper", 3.0, "adoption ramp, light"),
    ("ramp_dark_mid", "ink", 3.0, "adoption ramp, dark"),
    ("sand", "ink", 3.0, "adoption ramp, dark"),
]


def audit_contrast():
    print("contrast audit (WCAG 2.1):")
    failures = []
    for fg, bg, need, where in CONTRAST_PAIRS:
        ratio = contrast(PALETTE[fg], PALETTE[bg])
        status = "ok" if ratio >= need else "FAIL"
        print(f"  {fg:>8} on {bg:<8} {ratio:5.2f}:1  need {need}  {status}   ({where})")
        if ratio < need:
            failures.append((fg, bg, ratio, need, where))
    if failures:
        raise SystemExit(
            "contrast audit failed: " +
            "; ".join(f"{f} on {b} = {r:.2f} < {n} ({w})" for f, b, r, n, w in failures)
        )


# ------------------------------------------------------------- svg bits

def esc(s):
    return html.escape(s, quote=True)


def wrap(text, size, max_width):
    """Estimate-based word wrap: ~0.56em average advance for Public Sans,
    deliberately pessimistic so fallback fonts stay inside the margin."""
    per_char = 0.56 * size
    limit = max(1, int(max_width / per_char))
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if len(trial) <= limit or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(x, y, lines, size, fill, weight="400", anchor="start",
               leading=1.45, style=""):
    out = []
    for i, line in enumerate(lines):
        out.append(
            f'<text x="{x}" y="{y + i * size * leading:.1f}" '
            f'font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{style}>{esc(line)}</text>'
        )
    return "\n".join(out), y + (len(lines) - 1) * size * leading


def svg_open(width, height, bg, title, desc):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" role="img" '
        f'aria-labelledby="t d">\n'
        f'<title id="t">{esc(title)}</title>\n'
        f'<desc id="d">{esc(desc)}</desc>\n'
        f'<rect width="{width}" height="{height}" fill="{bg}"/>'
    )


def theme(dark):
    """Colour roles for a variant. Dark surfaces use Ink with Graphite
    raised panels, per the reversed-asset conventions."""
    if dark:
        return {
            "bg": PALETTE["ink"], "text": PALETTE["paper"],
            "muted": PALETTE["mist"], "faint": PALETTE["mist"],
            "accent": PALETTE["ember"], "panel": PALETTE["graphite"],
            "panel_text": PALETTE["paper"], "hairline": PALETTE["stone"],
            "box": PALETTE["graphite"], "box_text": PALETTE["paper"],
            "out_box": PALETTE["graphite"], "out_text": PALETTE["paper"],
            "bar": PALETTE["paper"],
            # Ordered ramp, least to most. On a dark ground the brighter
            # end reads as "more", so it runs Ember -> Sand.
            "ramp": [PALETTE["ember"], PALETTE["ramp_dark_mid"],
                     PALETTE["sand"]],
        }
    return {
        "bg": PALETTE["paper"], "text": PALETTE["ink"],
        "muted": PALETTE["graphite"], "faint": PALETTE["stone"],
        "accent": PALETTE["ember"], "panel": PALETTE["sand"],
        "panel_text": PALETTE["ink"], "hairline": PALETTE["stone"],
        "box": PALETTE["mist"], "box_text": PALETTE["ink"],
        "out_box": PALETTE["sage"], "out_text": PALETTE["ink"],
        "bar": PALETTE["ink"],
        "ramp": [PALETTE["ember"], PALETTE["ramp_light_mid"], PALETTE["ink"]],
    }


def footer_lines(parts, width, y, t):
    """Caveat (if any) then source-and-date line, bottom-left."""
    out = []
    for kind, textv in parts:
        size = 14 if kind == "caveat" else 12.5
        fill = t["muted"] if kind == "caveat" else t["faint"]
        style = ' font-style="italic"' if kind == "caveat" else ""
        lines = wrap(textv, size, width - 96)
        block, y = text_block(48, y, lines, size, fill, style=style)
        out.append(block)
        y += size * 1.9
    return "\n".join(out), y


# ------------------------------------------------------------- figure 1

def fig_ambition(dark):
    """The promise and the count as a glanceable strip, in the same
    format as the BridgeAI figure. Two groups in different units and
    different colours, a divider between them, and the number that
    would connect them shown as an absence with the same visual weight
    as the numbers. No shared axis, no timeline: the point is that
    these are different kinds of thing, and the layout says so without
    machinery."""
    t = theme(dark)
    W = 960
    title = "Counted in courses, promised in people"
    desc = (
        "Two figures side by side, in different units. The promise, in "
        "people: 10 million workers promised AI training by 2030, "
        "announced as 7.5 million in June 2025 and raised in January "
        "2026. The count, in courses: 1,001,147 course completions "
        "reported by the eleven partner companies, January 2026, the "
        "latest figure published. Below, in a dashed box: people "
        "actually trained is not published, the number that would "
        "connect the two."
    )
    parts = []
    block, _ = text_block(48, 64, [title], 30, t["text"], weight="700")
    parts.append(block)

    # group labels
    parts.append('<text x="48" y="122" font-family="%s" font-size="13" '
                 'font-weight="700" letter-spacing="0.08em" fill="%s">'
                 'THE PROMISE, IN PEOPLE</text>' % (FONT, t["muted"]))
    parts.append('<text x="508" y="122" font-family="%s" font-size="13" '
                 'font-weight="700" letter-spacing="0.08em" fill="%s">'
                 'THE COUNT, IN COURSES</text>' % (FONT, t["muted"]))

    # divider between the two groups
    parts.append('<line x1="480" y1="104" x2="480" y2="256" stroke="%s" '
                 'stroke-width="1" opacity="0.6"/>' % t["hairline"])

    # the promise
    block, _ = text_block(48, 174, ["10 million"], 44, t["text"],
                          weight="700")
    parts.append(block)
    left_sub = wrap(
        "workers promised AI training by 2030. Announced as 7.5 million "
        "in June 2025; raised in January 2026.", 14, 400)
    block, _ = text_block(48, 204, left_sub, 14, t["muted"])
    parts.append(block)

    # the count
    block, _ = text_block(508, 174, ["1,001,147"], 44, t["accent"],
                          weight="700")
    parts.append(block)
    right_sub = wrap(
        "course completions reported by the eleven partner companies. "
        "January 2026, the latest figure published.", 14, 400)
    block, _ = text_block(508, 204, right_sub, 14, t["muted"])
    parts.append(block)

    # The number that would connect them, shown as an absence. Kept
    # deliberately quieter than the two figures above: it is the gap
    # between them, not a third statistic.
    parts.append('<rect x="48" y="270" width="%d" height="68" rx="10" '
                 'fill="none" stroke="%s" stroke-width="2" '
                 'stroke-dasharray="7 5"/>' % (W - 96, t["faint"]))
    block, _ = text_block(72, 300,
                          ["People actually trained: not published."],
                          19, t["text"], weight="700")
    parts.append(block)
    block, _ = text_block(72, 322,
                          ["the number that would connect the two"],
                          13.5, t["muted"])
    parts.append(block)

    y = 372
    parts.append('<line x1="48" y1="%d" x2="%d" y2="%d" stroke="%s" '
                 'stroke-width="1" opacity="0.5"/>'
                 % (y, W - 48, y, t["hairline"]))
    y += 26
    d = AMBITION_DATA
    block, y = footer_lines(
        [("caveat", d["caveat"]), ("source", d["source"])], W, y, t)
    parts.append(block)
    H = int(y + 8)
    return (svg_open(W, H, t["bg"], title, desc) + "\n" +
            "\n".join(parts) + "\n</svg>\n", "ambition_vs_delivery", W, H)


# ----------------------------------------------------------- figure 1b

def fig_bridgeai(dark):
    t = theme(dark)
    W = 960
    d = BRIDGEAI_DATA
    # A title states the finding; "BridgeAI, at a glance" named the
    # subject and left the reader to do the work. The two facts placed
    # together are the finding, and the conclusion is left withheld, per
    # the understatement rule.
    title = "A £100 million programme, 1,700 course completions"
    desc = (
        "BridgeAI is the government's own 100 million pound AI programme, "
        "launched 2023 and run by Innovate UK; it funds projects and "
        "business support as well as training. From launch to the end of "
        "2025: 74.6 of 100 million pounds allocated, 820 plus AI projects "
        "funded, 1,700 plus course completions, 126 accreditations."
    )
    parts = []
    y = 56
    block, _ = text_block(48, y, [title], 24, t["text"], weight="700")
    parts.append(block)
    y += 34
    intro_lines = wrap(d["intro"], 16, W - 96)
    block, iy = text_block(48, y, intro_lines, 16, t["muted"])
    parts.append(block)
    y = iy + 46

    col_w = (W - 96) / 4
    row_bottom = y
    for i, (num, sub) in enumerate(d["stats"]):
        x = 48 + i * col_w
        block, _ = text_block(x, y, [num], 30, t["text"], weight="700")
        parts.append(block)
        sub_lines = wrap(sub, 13.5, col_w - 24)
        block, sy = text_block(x, y + 26, sub_lines, 13.5, t["muted"])
        parts.append(block)
        row_bottom = max(row_bottom, sy)
    y = row_bottom + 34

    parts.append('<line x1="48" y1="%d" x2="%d" y2="%d" stroke="%s" '
                 'stroke-width="1" opacity="0.5"/>'
                 % (y, W - 48, y, t["hairline"]))
    y += 26
    block, y = footer_lines(
        [("caveat", d["caveat"]), ("source", d["source"])], W, y, t)
    parts.append(block)
    H = int(y + 8)
    return (svg_open(W, H, t["bg"], title, desc) + "\n" +
            "\n".join(parts) + "\n</svg>\n", "bridgeai_glance", W, H)


# ------------------------------------------------------------- figure 2

def fig_adoption(dark):
    t = theme(dark)
    W = 960
    # Was "AI adoption by firm size", which named the axes. The ratio is
    # computed below from the same constants, so the two cannot drift.
    title = "Small firms adopt AI at a third the rate of large ones"
    desc = (
        "Bar chart, shaded from dark to light as firm size falls. Share of "
        "firms using AI across the OECD area, 2024 or latest available "
        "year: large firms with 250 or more employees, 40 percent; medium "
        "firms with 50 to 249 employees, 20.4 percent; small firms with 10 "
        "to 49 employees, 11.9 percent. Adoption falls at every step down "
        "in firm size, with small firms adopting at 30 percent of the "
        "large-firm rate."
    )
    parts = []
    y = 64
    block, _ = text_block(48, y, [title], 30, t["text"], weight="700")
    parts.append(block)
    block, _ = text_block(48, y + 32,
                          ["Share of firms using AI — OECD area, "
                           "2024 or latest available year"],
                          16, t["muted"])
    parts.append(block)
    y += 88

    label_w, bar_x = 300, 360
    bar_max = W - bar_x - 120
    scale = bar_max / 40.0
    bars = ADOPTION_DATA["bars"]
    # Firm size is an ordered variable, so it takes the ordered ramp rather
    # than a highlight: the finding here is the gradient, and a ramp shows
    # a gradient where one Ember bar among two greys shows a single number.
    # Darkest step is the highest rate, which is the convention and also
    # lands Ember on small firms — the lowest rate, and the group this
    # project is about. Colour carries the ordering; the value labels carry
    # the magnitude, so nothing is lost if colour is lost.
    for i, (label, value) in enumerate(bars):
        colour = t["ramp"][len(bars) - 1 - i]
        lab_lines = wrap(label, 16, label_w)
        block, _ = text_block(48, y + 28, lab_lines, 16, t["text"], weight="600")
        parts.append(block)
        bw = max(4, value * scale)
        parts.append(f'<rect x="{bar_x}" y="{y}" width="{bw:.0f}" height="44" '
                     f'rx="6" fill="{colour}"/>')
        block, _ = text_block(bar_x + bw + 14, y + 30, [f"{value:g}%"], 20,
                              t["text"], weight="700")
        parts.append(block)
        y += 76

    # The comparison the bars imply, stated once and computed from the data
    # above rather than typed in, so it cannot drift from the figures.
    hi = max(v for _, v in bars)
    lo = min(v for _, v in bars)
    block, _ = text_block(
        48, y + 12,
        [f"Small firms adopt at {lo / hi:.0%} of the large-firm rate."],
        17, t["text"], weight="600")
    parts.append(block)
    y += 36
    parts.append(f'<line x1="48" y1="{y}" x2="{W - 48}" y2="{y}" '
                 f'stroke="{t["hairline"]}" stroke-width="1" opacity="0.5"/>')
    y += 26
    block, y = footer_lines(
        [("caveat", ADOPTION_DATA["caveat"]), ("source", ADOPTION_DATA["source"])],
        W, y, t)
    parts.append(block)

    H = int(y + 8)
    return (svg_open(W, H, t["bg"], title, desc) + "\n" +
            "\n".join(parts) + "\n</svg>\n", "adoption_gap", W, H)


# ------------------------------------------------------- figure 3 (404)

def fig_notfound(dark):
    """The 404 mark. Carries no data, so it takes no source line — the
    source-and-date rule exists to attribute claims, and a decorative
    mark makes none. Built from a single <text> with three <tspan>s so
    the glyphs flow on their own metrics; nothing here needs hand
    positioning, and no curve work is attempted (see the vector-editor
    rule in CLAUDE.md)."""
    t = theme(dark)
    W, H = 640, 250
    title = "404"
    desc = ("The numerals four, zero, four, with the zero drawn as an "
            "outline rather than filled.")
    parts = [
        f'<text x="{W / 2}" y="178" font-family="{FONT}" font-size="170" '
        f'font-weight="800" text-anchor="middle" letter-spacing="6">'
        f'<tspan fill="{t["text"]}">4</tspan>'
        f'<tspan fill="none" stroke="{t["accent"]}" stroke-width="7">0</tspan>'
        f'<tspan fill="{t["text"]}">4</tspan></text>'
    ]
    return (svg_open(W, H, t["bg"], title, desc) + "\n" +
            "\n".join(parts) + "\n</svg>\n", "not_found", W, H)


# ------------------------------------------------------------- og card

def build_og_card(out_dir):
    from PIL import Image, ImageDraw, ImageFont

    fonts_dir = os.path.join(os.environ.get("LOCALAPPDATA", ""),
                             "Microsoft", "Windows", "Fonts")
    bold = os.path.join(fonts_dir, "PublicSans-Bold.ttf")
    regular = os.path.join(fonts_dir, "PublicSans-Regular.ttf")
    wordmark = os.path.join(os.path.dirname(__file__), "..",
                            "assets", "logo", "png", "logo_wordmark_1024.png")
    for path in (bold, regular, wordmark):
        if not os.path.exists(path):
            print(f"og card skipped: missing {path}")
            return

    W, H = 1200, 630
    img = Image.new("RGB", (W, H), PALETTE["paper"])
    draw = ImageDraw.Draw(img)

    mark = Image.open(wordmark).convert("RGBA")
    mw = 560
    mh = int(mark.height * mw / mark.width)
    mark = mark.resize((mw, mh), Image.LANCZOS)
    img.paste(mark, ((W - mw) // 2, 118), mark)

    f_tag = ImageFont.truetype(bold, 40)
    f_sub = ImageFont.truetype(regular, 26)
    tag = "Practical AI capability through responsible, hands-on learning."
    sub = "Independent research on the UK's AI skills gap"
    for textv, font, yy, fill in ((tag, f_tag, 384, PALETTE["ink"]),
                                  (sub, f_sub, 448, PALETTE["graphite"])):
        tw = draw.textlength(textv, font=font)
        draw.text(((W - tw) / 2, yy), textv, font=font, fill=fill)
    draw.rectangle([((W - 120) / 2, 530), ((W + 120) / 2, 538)],
                   fill=PALETTE["ember"])

    out = os.path.join(out_dir, "og_card.png")
    img.save(out)
    Image.open(out).verify()
    print(f"wrote {os.path.relpath(out)}")


# ----------------------------------------------------------------- main

def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", default=os.path.join(
        os.path.dirname(__file__), "..", "docs", "assets", "figures"))
    parser.add_argument("--og", action="store_true",
                        help="also build og_card.png (needs Pillow + Public Sans)")
    args = parser.parse_args()

    audit_contrast()
    os.makedirs(args.out, exist_ok=True)

    for fig in (fig_ambition, fig_bridgeai, fig_adoption, fig_notfound):
        for dark in (False, True):
            svg, name, w, h = fig(dark)
            suffix = "_dark" if dark else ""
            path = os.path.join(args.out, f"{name}{suffix}.svg")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(svg)
            print(f"wrote {os.path.relpath(path)}  ({w}x{h})")

    if args.og:
        build_og_card(args.out)


if __name__ == "__main__":
    main()
