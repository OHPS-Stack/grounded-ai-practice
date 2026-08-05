#!/usr/bin/env python3
"""Draw the landing-site figures — reproducible SVG infographics from logged data.

Why this exists
---------------
The public landing site (`docs/`) carries four figures: the
courses-versus-people comparison, the OECD adoption gap by firm size, the
claim-verification method, and the practice-system diagram. Under the
data-driven figures rule in `CLAUDE.md`, outward graphics are produced
from a script with their data checked into the repo — never hand-drawn
numbers — and every one carries its own source-and-date line on the
image, because in the publishing funnel each element must stand alone.

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
}

FONT = "'Public Sans', 'Segoe UI', -apple-system, Arial, sans-serif"

# ------------------------------------------------------------------ data
#
# Transcribed from research_log.md; the entry numbers are the audit trail.

AMBITION_DATA = {
    # Entry 061/062: 7.5m announced June 2025 (PM speech + DSIT + TechFirst
    # releases, verbatim confirmed); raised to 10m January 2026, the month
    # the first progress figure appeared.
    "workers_target": "7.5 million",
    "workers_target_desc": (
        "workers promised training in AI by 2030 — announced June 2025, "
        "raised to 10 million in January 2026"
    ),
    # Entry 044 (research log) + [AISKILLSBOOST26], DSIT explainer,
    # 28 Jan 2026, read directly: 1,001,147 completions; counts partners'
    # customers, their own employees, and civil-service internal training;
    # no partner- or course-level breakdown published.
    "courses_reported": "1,001,147",
    "courses_reported_desc": (
        "course completions reported as progress, January 2026 — counted "
        "and supplied by the eleven companies delivering the training; "
        "includes their own employees; no breakdown published"
    ),
    "gap_line": (
        "Distinct workers trained — the number that would connect the two "
        "— is not published."
    ),
    # Entry 044 (research log), [IUK-BRIDGEAI-YR3]: BridgeAI year-three
    # figures, end of 2025.
    "bridgeai": [
        ("£100m", "programme budget"),
        ("£74.6m", "allocated by end 2025"),
        ("1,700+", "course completions"),
        ("126", "accreditations"),
    ],
    "bridgeai_label": (
        "BridgeAI, the government's £100 million AI programme, over the "
        "same period:"
    ),
    "caveat": (
        "Figures are self-reported by delivery partners; “course” is "
        "not defined in the source; courses do not equal people. "
        "BridgeAI's £100 million funds projects and business support as "
        "well as training."
    ),
    "source": (
        "Sources: gov.uk — Prime Minister's London Tech Week speech, Jun 2025; "
        "DSIT, AI Skills Boost explainer, 28 Jan 2026; Innovate UK, BridgeAI "
        "Year 3 report, 2025 · groundedaipractice.co.uk · Aug 2026"
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

METHOD_STEPS = [
    "A claim worth using appears",
    "Find the primary source; tag whose interest it serves — "
    "government, academic, vendor, advocacy",
    "Search for what would disconfirm it, not only what supports it",
    "Log what the source directly supports — and what it does not",
    "Cite it in deliverables — or retract it, in the open",
]

SYSTEM_DATA = {
    "inputs": [
        "Working rules and conventions",
        "Research and decision logs",
        "Verification tooling",
        "Persistent project memory",
    ],
    "engine": "Any capable AI assistant",
    "gate": "Human review at every decision point",
    "outputs": [
        "Research reports",
        "Learning units",
        "Custom local tools",
    ],
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
    ("ink", "sand", 4.5, "gap strip text, light"),
    ("ink", "mist", 4.5, "method boxes, light"),
    ("ink", "sage", 4.5, "system output boxes, light"),
    ("paper", "ink", 4.5, "body text, dark"),
    ("mist", "ink", 4.5, "secondary text, dark"),
    ("ember", "ink", 3.0, "large stat numbers, dark"),
    ("paper", "graphite", 4.5, "raised strip text, dark"),
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
        }
    return {
        "bg": PALETTE["paper"], "text": PALETTE["ink"],
        "muted": PALETTE["graphite"], "faint": PALETTE["stone"],
        "accent": PALETTE["ember"], "panel": PALETTE["sand"],
        "panel_text": PALETTE["ink"], "hairline": PALETTE["stone"],
        "box": PALETTE["mist"], "box_text": PALETTE["ink"],
        "out_box": PALETTE["sage"], "out_text": PALETTE["ink"],
        "bar": PALETTE["ink"],
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
    t = theme(dark)
    W = 960
    parts = []
    title = "Counted in courses, promised in people"
    desc = (
        "7.5 million workers were promised AI training by 2030; progress is "
        "published as 1,001,147 course completions supplied by the eleven "
        "delivery partners; the number of distinct workers trained is not "
        "published. BridgeAI, the government's 100 million pound AI "
        "programme, reports 1,700+ completions, 126 accreditations and "
        "74.6 million pounds allocated; the programme funds projects and "
        "business support as well as training."
    )
    y = 64
    block, _ = text_block(48, y, [title], 30, t["text"], weight="700")
    parts.append(block)
    y += 58

    # two big stat rows: number column, description column
    for num, desckey in (
        (AMBITION_DATA["workers_target"], AMBITION_DATA["workers_target_desc"]),
        (AMBITION_DATA["courses_reported"], AMBITION_DATA["courses_reported_desc"]),
    ):
        block, _ = text_block(48, y + 34, [num], 46, t["accent"], weight="700")
        parts.append(block)
        dlines = wrap(desckey, 17, W - 420)
        block, dy = text_block(360, y + 12, dlines, 17, t["text"])
        parts.append(block)
        y = max(y + 70, dy + 40)

    # the gap strip
    strip_lines = wrap(AMBITION_DATA["gap_line"], 18, W - 160)
    strip_h = 34 + len(strip_lines) * 18 * 1.45
    parts.append(
        f'<rect x="48" y="{y}" width="{W - 96}" height="{strip_h:.0f}" '
        f'rx="10" fill="{t["panel"]}"/>'
    )
    block, _ = text_block(72, y + 30, strip_lines, 18, t["panel_text"], weight="600")
    parts.append(block)
    y += strip_h + 44

    # BridgeAI mini-stats
    lbl = wrap(AMBITION_DATA["bridgeai_label"], 15, W - 96)
    block, ly = text_block(48, y, lbl, 15, t["muted"], weight="600")
    parts.append(block)
    y = ly + 34
    col_w = (W - 96) / 4
    for i, (num, sub) in enumerate(AMBITION_DATA["bridgeai"]):
        x = 48 + i * col_w
        block, _ = text_block(x, y, [num], 28, t["text"], weight="700")
        parts.append(block)
        sub_lines = wrap(sub, 13, col_w - 24)
        block, _ = text_block(x, y + 24, sub_lines, 13, t["muted"])
        parts.append(block)
    y += 78

    parts.append(f'<line x1="48" y1="{y}" x2="{W - 48}" y2="{y}" '
                 f'stroke="{t["hairline"]}" stroke-width="1" opacity="0.5"/>')
    y += 26
    block, y = footer_lines(
        [("caveat", AMBITION_DATA["caveat"]), ("source", AMBITION_DATA["source"])],
        W, y, t)
    parts.append(block)

    H = int(y + 8)
    return (svg_open(W, H, t["bg"], title, desc) + "\n" +
            "\n".join(parts) + "\n</svg>\n", "ambition_vs_delivery", W, H)


# ------------------------------------------------------------- figure 2

def fig_adoption(dark):
    t = theme(dark)
    W = 960
    title = "AI adoption by firm size"
    desc = (
        "Share of firms using AI across the OECD area, 2024 or latest "
        "available year: large firms with 250 or more employees, 40 "
        "percent; medium firms with 50 to 249 employees, 20.4 percent; "
        "small firms with 10 to 49 employees, 11.9 percent."
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
    for label, value in ADOPTION_DATA["bars"]:
        colour = t["accent"] if label == ADOPTION_DATA["highlight"] else t["bar"]
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

    y += 8
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


# ------------------------------------------------------------- figure 3

def fig_method(dark):
    t = theme(dark)
    W = 760
    title = "How a claim earns its place"
    desc = ("Five steps: " + "; ".join(s.replace("—", "-") for s in METHOD_STEPS) + ".")
    parts = []
    y = 60
    block, _ = text_block(48, y, [title], 28, t["text"], weight="700")
    parts.append(block)
    y += 48

    box_w = W - 96
    for i, step in enumerate(METHOD_STEPS):
        lines = wrap(step, 17, box_w - 110)
        box_h = 36 + len(lines) * 17 * 1.45
        parts.append(f'<rect x="48" y="{y}" width="{box_w}" height="{box_h:.0f}" '
                     f'rx="10" fill="{t["box"]}"/>')
        # step number in an Ember disc
        cx, cy = 84, y + box_h / 2
        parts.append(f'<circle cx="{cx}" cy="{cy:.0f}" r="17" fill="{t["accent"]}"/>')
        parts.append(f'<text x="{cx}" y="{cy + 6:.0f}" font-family="{FONT}" '
                     f'font-size="17" font-weight="700" fill="{PALETTE["ink"]}" '
                     f'text-anchor="middle">{i + 1}</text>')
        block, _ = text_block(122, y + 30, lines, 17, t["box_text"], weight="500")
        parts.append(block)
        y += box_h
        if i < len(METHOD_STEPS) - 1:
            parts.append(f'<line x1="{W / 2}" y1="{y + 4}" x2="{W / 2}" y2="{y + 24}" '
                         f'stroke="{t["hairline"]}" stroke-width="2"/>')
            parts.append(f'<path d="M {W / 2 - 6} {y + 20} L {W / 2} {y + 30} '
                         f'L {W / 2 + 6} {y + 20}" fill="none" '
                         f'stroke="{t["hairline"]}" stroke-width="2"/>')
            y += 38

    y += 30
    block, y = footer_lines([("source", SITE_STAMP)], W, y, t)
    parts.append(block)
    H = int(y + 8)
    return (svg_open(W, H, t["bg"], title, desc) + "\n" +
            "\n".join(parts) + "\n</svg>\n", "method_steps", W, H)


# ------------------------------------------------------------- figure 4

def fig_system(dark):
    t = theme(dark)
    W = 960
    title = "The repository is the system"
    desc = (
        "Working rules, research and decision logs, verification tooling and "
        "persistent memory are read by any capable AI assistant, which "
        "produces research reports, learning units and custom local tools. "
        "Human review gates every decision."
    )
    parts = []
    y = 60
    block, _ = text_block(48, y, [title], 28, t["text"], weight="700")
    parts.append(block)
    y += 44

    top = y
    in_w, in_h, in_gap = 268, 62, 16
    # input stack
    iy = top
    for label in SYSTEM_DATA["inputs"]:
        lines = wrap(label, 15, in_w - 32)
        parts.append(f'<rect x="48" y="{iy}" width="{in_w}" height="{in_h}" '
                     f'rx="10" fill="{t["box"]}"/>')
        oy = iy + in_h / 2 - (len(lines) - 1) * 15 * 1.45 / 2 + 5
        block, _ = text_block(48 + in_w / 2, oy, lines, 15, t["box_text"],
                              weight="500", anchor="middle")
        parts.append(block)
        iy += in_h + in_gap
    stack_h = iy - in_gap - top

    # engine box, centred against the stack
    en_w, en_h = 240, 96
    ex, ey = 400, top + stack_h / 2 - en_h / 2
    parts.append(f'<rect x="{ex}" y="{ey:.0f}" width="{en_w}" height="{en_h}" '
                 f'rx="12" fill="none" stroke="{t["accent"]}" stroke-width="3"/>')
    en_lines = wrap(SYSTEM_DATA["engine"], 17, en_w - 36)
    oy = ey + en_h / 2 - (len(en_lines) - 1) * 17 * 1.45 / 2 + 6
    block, _ = text_block(ex + en_w / 2, oy, en_lines, 17, t["text"],
                          weight="700", anchor="middle")
    parts.append(block)

    # output stack
    out_w, out_h, out_gap = 240, 70, 22
    ox = 704
    out_total = len(SYSTEM_DATA["outputs"]) * out_h + (len(SYSTEM_DATA["outputs"]) - 1) * out_gap
    oy0 = top + stack_h / 2 - out_total / 2
    yy = oy0
    for label in SYSTEM_DATA["outputs"]:
        lines = wrap(label, 15, out_w - 32)
        parts.append(f'<rect x="{ox}" y="{yy:.0f}" width="{out_w}" height="{out_h}" '
                     f'rx="10" fill="{t["out_box"]}"/>')
        ly = yy + out_h / 2 - (len(lines) - 1) * 15 * 1.45 / 2 + 5
        block, _ = text_block(ox + out_w / 2, ly, lines, 15, t["out_text"],
                              weight="600", anchor="middle")
        parts.append(block)
        yy += out_h + out_gap

    # connectors
    mid = top + stack_h / 2
    parts.append(f'<line x1="{48 + in_w}" y1="{mid:.0f}" x2="{ex - 10}" y2="{mid:.0f}" '
                 f'stroke="{t["hairline"]}" stroke-width="2"/>')
    parts.append(f'<path d="M {ex - 18} {mid - 6:.0f} L {ex - 8} {mid:.0f} '
                 f'L {ex - 18} {mid + 6:.0f}" fill="none" stroke="{t["hairline"]}" '
                 f'stroke-width="2"/>')
    parts.append(f'<line x1="{ex + en_w}" y1="{mid:.0f}" x2="{ox - 10}" y2="{mid:.0f}" '
                 f'stroke="{t["hairline"]}" stroke-width="2"/>')
    parts.append(f'<path d="M {ox - 18} {mid - 6:.0f} L {ox - 8} {mid:.0f} '
                 f'L {ox - 18} {mid + 6:.0f}" fill="none" stroke="{t["hairline"]}" '
                 f'stroke-width="2"/>')

    # human-review gate below the engine
    gy = top + stack_h + 34
    g_w = 400
    gx = (W - g_w) / 2
    g_lines = wrap(SYSTEM_DATA["gate"], 16, g_w - 36)
    g_h = 30 + len(g_lines) * 16 * 1.45
    parts.append(f'<rect x="{gx}" y="{gy}" width="{g_w}" height="{g_h:.0f}" '
                 f'rx="10" fill="{t["panel"]}"/>')
    ly = gy + 26
    block, _ = text_block(W / 2, ly, g_lines, 16, t["panel_text"],
                          weight="600", anchor="middle")
    parts.append(block)
    parts.append(f'<line x1="{W / 2}" y1="{ey + en_h:.0f}" x2="{W / 2}" y2="{gy - 6}" '
                 f'stroke="{t["hairline"]}" stroke-width="2" stroke-dasharray="4 4"/>')

    y = gy + g_h + 40
    block, y = footer_lines([("source", SITE_STAMP)], W, y, t)
    parts.append(block)
    H = int(y + 8)
    return (svg_open(W, H, t["bg"], title, desc) + "\n" +
            "\n".join(parts) + "\n</svg>\n", "practice_system", W, H)


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
    sub = "Independent, evidence-led research on the UK's AI skills gap"
    for textv, font, yy, fill in ((tag, f_tag, 384, PALETTE["ink"]),
                                  (sub, f_sub, 448, PALETTE["graphite"])):
        tw = draw.textlength(textv, font=font)
        draw.text(((W - tw) / 2, yy), textv, font=font, fill=fill)
    draw.rectangle([((W - 120) / 2, 530), ((W + 120) / 2, 538)],
                   fill=PALETTE["ember"])

    out = os.path.join(out_dir, "og_card.png")
    img.save(out)
    Image.open(out).verify()
    print(f"wrote {out}")


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

    for fig in (fig_ambition, fig_adoption, fig_method, fig_system):
        for dark in (False, True):
            svg, name, w, h = fig(dark)
            suffix = "_dark" if dark else ""
            path = os.path.join(args.out, f"{name}{suffix}.svg")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(svg)
            print(f"wrote {path}  ({w}x{h})")

    if args.og:
        build_og_card(args.out)


if __name__ == "__main__":
    main()
