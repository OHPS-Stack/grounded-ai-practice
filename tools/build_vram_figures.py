#!/usr/bin/env python3
"""Draw the figures for the budget-VRAM research document.

Why this exists
---------------
`drafts/budget_vram_for_local_ai.md` argues that VRAM is the deciding
purchase number and that the cheap routes to a lot of it carry a software
cost the price does not show. That is a two-variable claim — capacity
against price, split by software stack — and the hand-composed SVG route
in `build_site_figures.py` cannot draw it: it has no scales and no axes,
so every position would be arithmetic written by hand.

This is the first figure built on `gap_chart.py`, the Vega-Lite layer,
and it is here rather than there because figures belong with the document
that argues from them, the same way the server-guide figures do.

Data is transcribed from the pricing table in the draft, dated
2026-08-11, with the research-log entries beside it. Prices are
single-day UK listings and are labelled as such on the figure; the
RTX 3090 is drawn as a range rather than a point because the trackers
disagree and averaging them would hide that.

Requirements: Python with `vl-convert-python`.

Usage
-----
    python tools/build_vram_figures.py
    python tools/build_vram_figures.py --out DIR --png
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gap_chart as gc                                      # noqa: E402

# ------------------------------------------------------------------ data
#
# drafts/budget_vram_for_local_ai.md, "the realistic options" table;
# research_log.md Entries 068-071. UK street prices checked 2026-08-11.
# The R9700 figure is a search-snippet price (both fetch routes blocked,
# Entry 070); the 48 GB B60 Dual is priced in the draft's table but kept
# off this chart, since the CUDA comparator at 48 GB was only priced in
# the US used market.

CUDA = "NVIDIA — CUDA, everything works"
OPEN = "Intel / AMD — llama.cpp, vLLM"

CARDS = [
    # name,                 VRAM, price, laby, stack, label side
    #
    # Labels sit beside their point, not above it: three cards share the
    # 16 GB column, two share 24 GB and three share 32 GB, so vertical
    # placement collided. `laby` is the label's own y where it must
    # differ from the point's: with the axis stretched to £4,400 for the
    # 5090, the 16 GB cluster spans 11px, so its three labels all take
    # the right side, spread ~15px apart by laby. Left-side labels at
    # 16 GB are ruled out entirely — the check caught them reaching
    # back across the narrow 12–16 gap into the 12 GB labels. The
    # offsets are small enough that each label still reads as belonging
    # to its point, and check_labels verifies the result.
    ("Arc B580",              12,  245,  245, OPEN, "right"),
    ("RTX 5070",              12,  599,  599, CUDA, "right"),
    ("RX 9060 XT",            16,  330,  240, OPEN, "right"),
    ("Arc Pro B50",           16,  380,  380, OPEN, "right"),
    ("RTX 5060 Ti",           16,  450,  530, CUDA, "right"),
    ("Arc Pro B60",           24,  830,  830, OPEN, "left"),
    ("Radeon R9700",          32, 1250, 1250, OPEN, "left"),
    ("Arc Pro B70",           32, 1290, 1290, OPEN, "right"),
    ("RTX 5090",              32, 4199, 4199, CUDA, "left"),
]

# Trackers conflict on the used-3090 price, so it is a range, not a point.
RANGE_CARD = {"name": "RTX 3090 (used)", "vram": 24, "lo": 750, "hi": 1129,
              "stack": CUDA}

SOURCE = (
    "Prices are single-day UK listings checked 11 Aug 2026 and will move.\n"
    "RTX 3090 shown as a range because price trackers disagree; "
    "Radeon R9700 from a search snippet.\n"
    "Sources: UK retailer listings and price trackers, 11 Aug 2026; "
    "Phoronix, Apr 2026 · groundedaipractice.co.uk · Aug 2026"
)


def spec():
    """A scatter, because the claim is about two numbers at once. A bar
    chart of price, or of VRAM, would each show one half and neither
    would show the relationship the document argues about."""
    points = [{"name": n, "vram": v, "price": p, "stack": s}
              for n, v, p, _, s, _ in CARDS]
    # The label layers get their own rows, with `price` holding the
    # label's y rather than the card's. Same field name deliberately: a
    # second field on the y channel (even axis-less) merged into the
    # shared scale and silently deleted the visible price axis — found
    # by looking at the render after every check had passed.
    labels = [{"name": n, "vram": v, "price": ly, "stack": s, "place": pl}
              for n, v, _, ly, s, pl in CARDS]
    rng = [{"name": RANGE_CARD["name"], "vram": RANGE_CARD["vram"],
            "lo": RANGE_CARD["lo"], "hi": RANGE_CARD["hi"],
            "mid": (RANGE_CARD["lo"] + RANGE_CARD["hi"]) / 2,
            "stack": RANGE_CARD["stack"]}]

    colour = {
        "field": "stack", "type": "nominal", "title": None,
        # Ember is the accent and goes to the side being argued about —
        # the open stack, which is where the document's tension sits.
        "scale": {"domain": [OPEN, CUDA],
                  "range": [gc.PALETTE["ember"], gc.PALETTE["stone"]]},
        "legend": {"orient": "top", "direction": "horizontal",
                   "labelLimit": 320},
    }
    x = {"field": "vram", "type": "quantitative",
         "title": "VRAM (GB) — the number that decides what will run",
         "scale": {"domain": [8, 38], "nice": False},
         "axis": {"values": [12, 16, 24, 32], "format": "d"}}
    y = {"field": "price", "type": "quantitative",
         "title": "UK street price (£)",
         "scale": {"domain": [0, 4400], "nice": False},
         "axis": {"format": "$,d", "tickCount": 5}}
    return {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "title": {
            "text": "At 32 GB the software premium is 3x: "
                    "£4,199 against £1,250–£1,290",
            "subtitle": [
                "Nvidia's CUDA stack runs everything on day one; the "
                "£245–£1,290 cards run llama.cpp and vLLM with the "
                "frictions the document describes.",
                "The one overlap is the used RTX 3090, where two years "
                "of price inflation meet a new, warrantied Arc Pro B60.",
            ],
        },
        "layer": [
            # the 3090's price range, drawn first so points sit over it
            {"data": {"values": rng},
             "mark": {"type": "rule", "strokeWidth": 7, "opacity": 0.5,
                      "strokeCap": "round"},
             "encoding": {"x": x,
                          "y": {"field": "lo", "type": "quantitative"},
                          "y2": {"field": "hi"},
                          "color": colour}},
            {"data": {"values": rng},
             "mark": {"type": "text", "align": "left", "dx": 14, "dy": -4,
                      "fontSize": 13, "fontWeight": 600},
             "encoding": {"x": x,
                          "y": {"field": "mid", "type": "quantitative"},
                          "text": {"field": "name"},
                          "color": colour}},
            {"data": {"values": rng},
             "mark": {"type": "text", "align": "left", "dx": 14, "dy": 13,
                      "fontSize": 11.5},
             "encoding": {"x": x,
                          "y": {"field": "mid", "type": "quantitative"},
                          "text": {"value": "£750–1,129"},
                          "color": colour}},
            # the fixed-price cards
            {"data": {"values": points},
             "mark": {"type": "point", "filled": True, "size": 190,
                      "opacity": 1},
             "encoding": {"x": x, "y": y, "color": colour}},
            # Two label layers rather than one with a conditional offset:
            # an encoded `dy` condition is silently ignored here, which
            # put every label on top of its own point. The rows come
            # from `labels`, whose price is the label position — see the
            # note where it is built.
            {"data": {"values": labels},
             "transform": [{"filter": "datum.place === 'right'"}],
             "mark": {"type": "text", "align": "left", "dx": 15,
                      "fontSize": 13, "fontWeight": 600},
             "encoding": {"x": x, "y": y, "text": {"field": "name"},
                          "color": colour}},
            {"data": {"values": labels},
             "transform": [{"filter": "datum.place === 'left'"}],
             "mark": {"type": "text", "align": "right", "dx": -15,
                      "fontSize": 13, "fontWeight": 600},
             "encoding": {"x": x, "y": y, "text": {"field": "name"},
                          "color": colour}},
        ],
        "resolve": {"scale": {"color": "shared"}},
    }


# ----------------------------------------------------------- post figure
#
# The second figure exists for the publishing funnel's first step — a
# LinkedIn-format graphic — where the scatter above asks too much of a
# feed reader: axes to orient, a legend to decode, eleven points to
# rank. This one is the comparison table drawn as a ladder: one row per
# card, grouped by capacity tier, every bar carrying its own name and
# price, and the per-tier finding stated where the eye lands. Same
# data, same date, same honesty lines (the 3090 as a range, the used/new
# note at 24 GB); nothing here is drawn that the document's table does
# not contain.
#
# Tier descriptors are the draft's own "what the tiers buy" table.
# Portrait-ish proportions are deliberate: LinkedIn's feed gives tall
# images more room than wide ones.

X_MAX = 4400          # £ domain ceiling; leaves label room past the 5090

# Launch prices, `research_log.md` Entry 078. Two bases, and the figure
# marks which is which, because they are not the same kind of number:
#   "uk"   — the vendor published a UK MSRP in pounds, inc. VAT.
#   "conv" — no UK RRP exists (true of every workstation card), so the
#            US list is converted at $1 = £0.7396 and 20% VAT added.
# Mixing an unconverted dollar list with a sterling street price on one
# axis would be the real error here; converting and labelling it is the
# smaller one, and the asterisk in the label carries it to the reader.
USD_GBP = 0.7396      # GBP/USD 1.3521, 2026-08-12
VAT = 1.20


def _conv(usd):
    return round(usd * USD_GBP * VAT)


# Deliberately spare. An earlier build carried a four-line subtitle, a
# three-line annotation beside every tier and a four-line footer — a blog
# post set in a PNG. In a feed the image has about a second to land and
# the words belong in the post body, so everything that is not the
# comparison itself has been cut: no annotation blocks, a one-line
# subtitle, and tier descriptors trimmed to the few words that tell a
# non-specialist why a capacity matters.
POST_TIERS = [
    # capacity, what it runs, cards
    #
    # card = (name, launch £, basis, street lo, street hi, stack)
    # street hi is None for a point price; the used 3090 is the one range.
    (12, "7–9B models",
     [("Arc B580", 250, "uk", 245, None, OPEN),
      ("RTX 5070", 539, "uk", 599, None, CUDA)]),
    (16, "12–14B models",
     [("Arc Pro B50", _conv(349), "conv", 380, None, OPEN),
      ("RX 9060 XT", 315, "uk", 330, None, OPEN),
      ("RTX 5060 Ti", 399, "uk", 450, None, CUDA)]),
    (24, "27–32B models",
     [("Arc Pro B60", _conv(599), "conv", 830, None, OPEN),
      ("RTX 3090 · used", None, None, 750, 1129, CUDA)]),
    (32, "27–32B with headroom",
     [("Arc Pro B70", _conv(949), "conv", 1290, None, OPEN),
      ("Radeon R9700", _conv(1299), "conv", 1250, None, OPEN),
      ("RTX 5090", 1919, "uk", 4199, None, CUDA)]),
]

# At 24 GB the launch layer carries only Intel, because the CUDA card at
# that capacity is a 2020 part on the used market. That is a real absence
# and the figure states it, so the launch-layer coverage check accepts it
# here and nowhere else — see main().
LAUNCH_GAP_NOTED = {
    24: "RTX 3090 labelled 'used', with no launch marker drawn",
}

POST_SOURCE = (
    "UK listing prices, 11 Aug 2026 — a market the memory shortage is "
    "still moving.\n"
    "*  US list converted at $1 = £0.74 plus VAT; the workstation cards "
    "carry no UK RRP.\n"
    "RTX 3090 shown used, across two trackers that disagree, so it carries "
    "no launch price.  ·  groundedaipractice.co.uk"
)


def post_spec(dark=False):
    """A dumbbell per card: hollow marker at the launch price, solid at
    today's UK street price, joined by a line whose length is the move.

    Drawn on a hidden quantitative row scale rather than a band scale so
    headers, separators and annotation blocks can sit at fractional rows.
    Rows are negated (`yv = -row`) because a quantitative y axis puts low
    values at the bottom and the ladder reads top-down.
    """
    fg = gc.PALETTE["paper"] if dark else gc.PALETTE["ink"]
    muted = gc.PALETTE["mist"] if dark else gc.PALETTE["graphite"]

    conns, ranges, launch_pts, street_pts = [], [], [], []
    lab_r, lab_l, caps_hdr, desc_hdr, seps = [], [], [], [], []
    y = 0.0
    for i, (cap, fits, cards) in enumerate(POST_TIERS):
        if i:
            seps.append({"yv": -(y - 0.52), "p0": 0, "p": X_MAX})
        caps_hdr.append({"yv": -y, "t": f"{cap} GB"})
        desc_hdr.append({"yv": -y, "t": f"·  {fits}"})
        for name, launch, basis, lo, hi, stack in cards:
            y += 1.0
            row = {"yv": -y, "stack": stack}
            if launch is not None:
                star = "*" if basis == "conv" else ""
                # "»" not "→": Public Sans has no U+2192, and a missing
                # glyph drops the whole text run to a serif fallback —
                # invisible to every check, obvious in the render.
                text = f"{name}   £{launch:,}{star} » £{lo:,}"
                conns.append({**row, "p0": launch, "p": lo})
                launch_pts.append({**row, "p": launch})
                street_pts.append({**row, "p": lo})
            else:
                text = f"{name}   £{lo:,}–{hi:,}"
                ranges.append({**row, "p0": lo, "p": hi})
            right = max(launch or 0, hi or lo)
            if right > 0.6 * X_MAX:
                lab_l.append({**row, "p": min(launch or lo, lo), "t": text})
            else:
                lab_r.append({**row, "p": right, "t": text})
        y += 1.15                                   # gap before next header

    x = {"field": "p", "type": "quantitative",
         "scale": {"domain": [0, X_MAX], "nice": False}, "axis": None}
    x0 = {**x, "field": "p0"}

    def yq(field="yv"):
        return {"field": field, "type": "quantitative",
                "scale": {"domain": [-(y - 0.45), 0.62], "nice": False},
                "axis": None}

    colour = {
        "field": "stack", "type": "nominal", "title": None,
        "scale": {"domain": [OPEN, CUDA],
                  "range": [gc.PALETTE["ember"], gc.PALETTE["stone"]]},
        "legend": {"orient": "top", "direction": "horizontal",
                   "labelLimit": 340},
    }
    ground = gc.PALETTE["ink"] if dark else gc.PALETTE["paper"]

    return {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "title": {
            # Two real UK prices, no converted figure — the headline claim
            # should not need the asterisk the labels carry.
            "text": "32 GB of graphics memory: £1,290, or £4,199",
            "subtitle": [
                "Capacity decides which AI models will run at all.",
                "Hollow marker: price at launch.   Solid: UK price "
                "today, 11 August 2026.",
            ],
        },
        "layer": [
            {"data": {"values": seps},
             "mark": {"type": "rule", "strokeWidth": 1, "opacity": 0.35,
                      "color": gc.PALETTE["stone"]},
             "encoding": {"y": yq(), "x": x0, "x2": {"field": "p"}}},
            # launch → street, drawn under the markers
            {"data": {"values": conns},
             "mark": {"type": "rule", "strokeWidth": 3.5, "opacity": 0.45},
             "encoding": {"x": x0, "x2": {"field": "p"}, "y": yq(),
                          "color": colour}},
            # the used 3090's tracker disagreement, as a band
            {"data": {"values": ranges},
             "mark": {"type": "rule", "strokeWidth": 11, "strokeCap": "round",
                      "opacity": 0.55 if dark else 0.38},
             "encoding": {"x": x0, "x2": {"field": "p"}, "y": yq(),
                          "color": colour}},
            # Hollow marker: an explicit background fill rather than
            # filled:false, so the connector line does not show through
            # the middle of it and read as a solid dot.
            {"data": {"values": launch_pts},
             "mark": {"type": "point", "filled": True, "size": 190,
                      "strokeWidth": 3, "fill": ground, "opacity": 1},
             "encoding": {"x": x, "y": yq(),
                          "stroke": colour, "color": colour}},
            {"data": {"values": street_pts},
             "mark": {"type": "point", "filled": True, "size": 210,
                      "opacity": 1},
             "encoding": {"x": x, "y": yq(), "color": colour}},
            {"data": {"values": caps_hdr},
             "mark": {"type": "text", "align": "left", "baseline": "middle",
                      "fontSize": 19, "fontWeight": 700, "color": fg,
                      "x": 2},
             "encoding": {"y": yq(), "text": {"field": "t"}}},
            {"data": {"values": desc_hdr},
             "mark": {"type": "text", "align": "left", "baseline": "middle",
                      "fontSize": 14, "color": muted, "x": 76},
             "encoding": {"y": yq(), "text": {"field": "t"}}},
            {"data": {"values": lab_r},
             "mark": {"type": "text", "align": "left", "baseline": "middle",
                      "dx": 16, "fontSize": 15.5, "fontWeight": 600,
                      "color": fg},
             "encoding": {"x": x, "y": yq(), "text": {"field": "t"}}},
            # The 5090 reaches the right edge, so its label runs leftward
            # from its launch marker into that row's empty space.
            {"data": {"values": lab_l},
             "mark": {"type": "text", "align": "right", "baseline": "middle",
                      "dx": -16, "fontSize": 15.5, "fontWeight": 600,
                      "color": fg},
             "encoding": {"x": x, "y": yq(), "text": {"field": "t"}}},
        ],
        "resolve": {"scale": {"color": "shared"}},
    }


# ----------------------------------------------------- capability figure
#
# The third figure answers the question the price figures leave open:
# what are the models that fit actually capable of? Scale is Epoch AI's
# Capabilities Index (CC-BY, retrieved 2026-08-12), chosen over the
# Artificial Analysis index on independence, licence and scale stability
# — `research_log.md` Entry 079 carries the numbers, the computed lag and
# every caveat; `project_log.md` Entry 078 the design decisions.
#
# The design problem is that an index point means nothing to the
# intended reader, so each closed-model point carries an era anchor — a
# dated product the reader has used ("what free ChatGPT ran") — and the
# dashed guide translates the comparison into time. Era labels are
# sourced product history (`[OPENAI-4OMINI24]`): GPT-4 was the *paid*
# ChatGPT; the free tier ran GPT-3.5 until GPT-4o mini replaced it in
# July 2024.
#
# `check_coverage` is deliberately not run here: it guards categorical
# comparisons within levels of an x variable, and this figure has no
# such structure — both columns sit on one shared capability scale,
# which is itself the comparison.

X_CLOSED = 3.6        # column positions on a hidden [0, 10] x scale
X_LOCAL = 7.2

# rows: (eci, ci_lo, ci_hi, name, role, name_y, role_y[, xv])
# ci None where the interval is omitted from the drawing (Entry 079 has
# them all); label y positions are hand-spread where points cluster,
# same laby pattern as CARDS above. A role of None makes a one-line
# label — used through the 2023–24 cluster, where three two-line labels
# cannot fit beside points 0.9–1.9 index points apart. The two local
# rows carry their own xv, nudged apart so their overlapping whiskers
# read as two intervals rather than one thick bar — both defects were
# invisible to check_labels and found by looking at the render.
ECI_CLOSED = [
    (161.65, None, None, "The frontier today",
     "GPT-5.6 Sol · Claude Opus 5 · Aug 2026", 162.5, 161.4),
    (161.53, None, None, None, None, None, None),
    (161.02, None, None, None, None, None, None),
    (150.00, None, None, "GPT-5 · Aug 2025",
     "ChatGPT's flagship model", 150.55, 149.45),
    (142.45, 140.33, 143.44, "o1 · Dec 2024",
     "ChatGPT's first reasoning model", 142.9, 141.8),
    (128.57, None, None, "GPT-4o — ChatGPT's default · 2024",
     None, 129.35, None),
    (126.64, None, None, "GPT-4o mini — free ChatGPT, 2024–25",
     None, 127.05, None),
    (125.70, None, None, "GPT-4 · Mar 2023",
     "the original paid ChatGPT", 125.2, 124.1),
]

ECI_LOCAL = [
    (143.50, 137.82, 148.13, "Qwen3.6 35B · Apr 2026",
     "Alibaba · open weights", 145.35, 144.30, 7.05),
    (142.28, 134.48, 146.86, "Gemma 4 31B · Apr 2026",
     "Google · open weights", 141.40, 140.35, 7.35),
]

GUIDE_Y = 143.5       # the single-card best; the line the figure is about

CAP_SOURCE = (
    "Scale: Epoch AI Capabilities Index (CC-BY), data retrieved "
    "12 Aug 2026 — a composite of 50+ benchmarks.\n"
    "Whiskers: 95% intervals where the comparison is close · "
    "fits = ≤40B parameters at 4-bit (Epoch's model).\n"
    "Epoch AI, epoch.ai/eci · product history: OpenAI announcements · "
    "groundedaipractice.co.uk · Aug 2026"
)


def capability_spec(dark=False):
    """A two-column ladder on one vertical scale: the closed frontier's
    dated anchors on the left, the models that fit one card on the
    right. One scale because that is the claim; two columns because the
    reader's question is which side of the room each thing lives on."""
    fg = gc.PALETTE["paper"] if dark else gc.PALETTE["ink"]
    muted = gc.PALETTE["mist"] if dark else gc.PALETTE["graphite"]

    def col(rows, default_x, label_x=None):
        # label_x anchors every label in the column at one x, so a
        # right-hand label can never start under a neighbouring row's
        # whisker — found when Gemma's interval line grazed the Qwen
        # label's first letter.
        pts, whisk, names, roles = [], [], [], []
        for row in rows:
            eci, lo, hi, name, role, ny, ry = row[:7]
            xv = row[7] if len(row) > 7 else default_x
            lx = label_x if label_x is not None else xv
            pts.append({"xv": xv, "yv": eci})
            if lo is not None:
                whisk.append({"xv": xv, "lo": lo, "hi": hi})
            if name:
                names.append({"xv": lx, "yv": ny, "t": name})
            if role:
                roles.append({"xv": lx, "yv": ry, "t": role})
        return pts, whisk, names, roles

    c_pts, c_whisk, c_names, c_roles = col(ECI_CLOSED, X_CLOSED)
    l_pts, l_whisk, l_names, l_roles = col(
        ECI_LOCAL, X_LOCAL, label_x=max(r[7] for r in ECI_LOCAL))

    x = {"field": "xv", "type": "quantitative",
         "scale": {"domain": [0, 10], "nice": False}, "axis": None}
    y = {"field": "yv", "type": "quantitative",
         "title": "Epoch AI capability index",
         "scale": {"domain": [123.2, 163.8], "nice": False},
         "axis": {"values": [125, 130, 135, 140, 145, 150, 155, 160],
                  "format": "d"}}

    def text_layer(rows, align, dx, size, weight, colour):
        return {"data": {"values": rows},
                "mark": {"type": "text", "align": align,
                         "baseline": "middle", "dx": dx, "fontSize": size,
                         "fontWeight": weight, "color": colour},
                "encoding": {"x": x, "y": y, "text": {"field": "t"}}}

    return {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "title": {
            "text": "One graphics card now runs late 2024's frontier AI",
            "subtitle": [
                "The best open models that fit a 24–32 GB card, on "
                "Epoch AI's capability scale — clearly above",
                "every ChatGPT model of 2023–24, about a year and a "
                "half behind today's paid frontier.",
            ],
        },
        "layer": [
            {"data": {"values": [{"lo": 0.5, "hi": 9.5, "yv": GUIDE_Y}]},
             "mark": {"type": "rule", "strokeDash": [6, 4],
                      "strokeWidth": 1.5, "opacity": 0.8,
                      "color": gc.PALETTE["stone"]},
             "encoding": {"x": {**x, "field": "lo"},
                          "x2": {"field": "hi"}, "y": y}},
            {"data": {"values": [{"xv": 5.0, "yv": 144.45,
                                  "t": "where the frontier stood, "
                                       "late 2024"}]},
             "mark": {"type": "text", "align": "center",
                      "baseline": "middle", "fontSize": 12.5,
                      "color": muted},
             "encoding": {"x": x, "y": y, "text": {"field": "t"}}},
            {"data": {"values": c_whisk},
             "mark": {"type": "rule", "strokeWidth": 2.5, "opacity": 0.55,
                      "color": gc.PALETTE["stone"]},
             "encoding": {"x": x, "y": {**y, "field": "lo"},
                          "y2": {"field": "hi"}}},
            {"data": {"values": l_whisk},
             "mark": {"type": "rule", "strokeWidth": 2.5, "opacity": 0.55,
                      "color": gc.PALETTE["ember"]},
             "encoding": {"x": x, "y": {**y, "field": "lo"},
                          "y2": {"field": "hi"}}},
            {"data": {"values": c_pts},
             "mark": {"type": "point", "filled": True, "size": 150,
                      "opacity": 1, "color": gc.PALETTE["stone"]},
             "encoding": {"x": x, "y": y}},
            {"data": {"values": l_pts},
             "mark": {"type": "point", "filled": True, "size": 200,
                      "opacity": 1, "color": gc.PALETTE["ember"]},
             "encoding": {"x": x, "y": y}},
            text_layer(c_names, "right", -16, 13.5, 600, fg),
            text_layer(c_roles, "right", -16, 11.5, 400, muted),
            text_layer(l_names, "left", 16, 13.5, 600,
                       gc.PALETTE["ember"]),
            text_layer(l_roles, "left", 16, 11.5, 400, muted),
        ],
    }


# ------------------------------------------------- price-per-gigabyte
#
# The third form, and the simplest: one bar per card, £ per gigabyte of
# VRAM. It buys one thing the tiered views cannot show — a comparison
# *across* capacities on a single axis, which is what makes the fair and
# surprising pairing visible: Intel's 32 GB card costs less per gigabyte
# than Nvidia's 12 GB one.
#
# It also carries a trap the document names, so the figure has to answer
# it. Per gigabyte the small cards win, but capability moves in steps,
# not gradients: a 12 GB card at £20/GB cannot run what a 32 GB card runs
# at any price. So capacity is printed on every bar and the subtitle says
# it outright. Sorted ascending, cheapest first, because the £131/GB
# outlier lands harder arriving last.

PPG_SOURCE = (
    "Bars are UK listing prices, 11 Aug 2026 — a market the memory "
    "shortage is still moving.\n"
    "Launch notches for the Arc Pro and Radeon R9700 cards are US list "
    "converted at $1 = £0.74 plus VAT; those carry no UK RRP.\n"
    "RTX 3090 is a used 2020 card with no launch price; its bar is the "
    "spread between two trackers that disagree.  ·  "
    "groundedaipractice.co.uk"
)


def ppg_spec(dark=False):
    fg = gc.PALETTE["paper"] if dark else gc.PALETTE["ink"]

    rows = []
    for cap, _, cards in POST_TIERS:
        for name, launch, basis, lo, hi, stack in cards:
            street, top = lo / cap, (hi / cap) if hi else None
            rows.append({
                "label": f"{name}  ·  {cap} GB",
                "stack": stack,
                "ppg": street,
                "ppg_hi": top,
                "launch_ppg": (launch / cap) if launch else None,
                "labx": top or street,
                # No asterisk here. It marks a converted US list price,
                # which is the *launch* figure — the street £/GB beside
                # it is a real UK listing, so carrying the symbol on this
                # label would attribute the conversion to the wrong
                # number. The footer names the affected cards instead.
                "text": (f"£{street:.0f}–{top:.0f}" if top
                         else f"£{street:.0f}"),
                # Sorted on the low value, not a range's midpoint: the
                # eye ranks these by where the solid bar ends, so a
                # midpoint sort makes the ordering look broken.
                "sortk": street,
            })
    rows.sort(key=lambda r: r["sortk"])
    order = [r["label"] for r in rows]

    colour = {
        "field": "stack", "type": "nominal", "title": None,
        "scale": {"domain": [OPEN, CUDA],
                  "range": [gc.PALETTE["ember"], gc.PALETTE["stone"]]},
        "legend": {"orient": "top", "direction": "horizontal",
                   "labelLimit": 340},
    }
    x = {"field": "ppg", "type": "quantitative",
         "title": "£ per gigabyte of VRAM",
         "scale": {"domain": [0, 145], "nice": False},
         "axis": {"format": "$,d", "tickCount": 6}}
    y = {"field": "label", "type": "nominal", "sort": order, "title": None,
         "axis": {"labelFontSize": 14.5, "labelPadding": 12,
                  "labelLimit": 260, "domain": False, "ticks": False,
                  "labelColor": fg}}

    return {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "title": {
            "text": "Intel's 32 GB card costs less per gigabyte "
                    "than Nvidia's 12 GB card",
            "subtitle": [
                "UK street prices, 11 August 2026. The notch on each bar "
                "marks what that card cost per gigabyte at launch.",
                "Capacity is printed on every bar: a cheap 12 GB card "
                "still cannot run what 32 GB runs.",
            ],
        },
        "layer": [
            {"data": {"values": rows},
             "mark": {"type": "bar", "height": 26, "cornerRadiusEnd": 3},
             "encoding": {"x": x, "y": y, "color": colour}},
            # the 3090's tracker disagreement, continuing its bar
            {"data": {"values": [r for r in rows if r["ppg_hi"]]},
             "mark": {"type": "bar", "height": 26, "cornerRadiusEnd": 3,
                      "opacity": 0.42},
             "encoding": {"x": x, "x2": {"field": "ppg_hi"}, "y": y,
                          "color": colour}},
            # launch price as a notch: a tick reads in both directions,
            # and the Arc B580 is the one card that got *cheaper*
            {"data": {"values": [r for r in rows if r["launch_ppg"]]},
             "mark": {"type": "tick", "thickness": 3, "size": 30,
                      "color": fg, "opacity": 0.9},
             "encoding": {"x": {**x, "field": "launch_ppg"}, "y": y}},
            {"data": {"values": rows},
             "mark": {"type": "text", "align": "left", "baseline": "middle",
                      "dx": 9, "fontSize": 14.5, "fontWeight": 700,
                      "color": fg},
             "encoding": {"x": {**x, "field": "labx"}, "y": y,
                          "text": {"field": "text"}}},
        ],
        "resolve": {"scale": {"color": "shared"}},
    }


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--out", default=os.path.join("assets", "figures"))
    p.add_argument("--png", action="store_true",
                   help="also rasterise, for Word and social")
    p.add_argument("--allow-gaps", action="store_true",
                   help="build despite an incomplete comparison "
                        "(for review only — not a publishable figure)")
    a = p.parse_args()
    os.makedirs(a.out, exist_ok=True)
    stem = os.path.join(a.out, "vram_price_capacity")
    print("building VRAM figures")

    # Blocking, not advisory. Counting categories per level involves no
    # estimation, so a failure here is a fact about the data rather than a
    # guess about the picture — and what it prevents is a public graphic
    # implying a comparison the research never made.
    rows = [{"vram": v, "stack": s} for _, v, _, _, s, _ in CARDS]
    rows.append({"vram": RANGE_CARD["vram"], "stack": RANGE_CARD["stack"]})
    thin, _ = gc.check_coverage(rows, "vram", "stack")
    if thin and not a.allow_gaps:
        raise SystemExit(
            "refusing to build: the comparison is incomplete at "
            + ", ".join(f"{lvl} GB" for lvl, _ in thin) +
            ".\n  This figure exists to compare vendors at each capacity; "
            "at those levels only one vendor is priced."
            "\n  Finish the pricing research first, or pass --allow-gaps "
            "to build a deliberately partial figure for review."
        )
    written = gc.render(spec(), stem, width=740, height=560, source=SOURCE)
    for path in written:
        gc.check_labels(path)
        if gc.check_glyphs(path) and not a.allow_gaps:
            raise SystemExit(
                "refusing to write: a label uses a character Public Sans "
                "cannot draw, which silently resets that run in a fallback "
                "face. Substitute the character.")
    if a.png:
        for path in written:
            gc.to_png(path, path[:-4] + ".png")

    # The post ladder draws from POST_TIERS, so its coverage is checked
    # from POST_TIERS — passing the scatter's check would prove nothing
    # about a figure built from a different table. Both price layers are
    # checked, because each one invites its own comparison.
    print("building post ladder")
    street_rows = [{"vram": cap, "stack": s}
                   for cap, _, cards in POST_TIERS
                   for _, _, _, _, _, s in cards]
    thin, _ = gc.check_coverage(street_rows, "vram", "stack")
    if thin and not a.allow_gaps:
        raise SystemExit(
            "refusing to build the post ladder: only one stack priced at "
            + ", ".join(f"{lvl} GB" for lvl, _ in thin))

    # The launch layer is thinner than the street layer by one card, and
    # that absence has to be declared and shown rather than tolerated —
    # an undeclared gap here would let the eye read a launch comparison
    # at a capacity where only one vendor has a launch price.
    print("  launch layer:")
    launch_rows = [{"vram": cap, "stack": s}
                   for cap, _, cards in POST_TIERS
                   for _, launch, _, _, _, s in cards if launch is not None]
    thin, _ = gc.check_coverage(launch_rows, "vram", "stack")
    undeclared = [lvl for lvl, _ in thin if lvl not in LAUNCH_GAP_NOTED]
    if undeclared and not a.allow_gaps:
        raise SystemExit(
            "refusing to build: the launch-price layer compares only one "
            "stack at " + ", ".join(f"{lvl} GB" for lvl in undeclared) +
            ",\n  and that gap is not declared in LAUNCH_GAP_NOTED. Either "
            "price the missing comparator or state the absence on the "
            "figure and declare it there.")
    for lvl, _ in thin:
        print(f"  launch gap at {lvl} GB declared: {LAUNCH_GAP_NOTED[lvl]}")
    ladder = os.path.join(a.out, "vram_price_ladder")
    written = []
    for variant in ("light", "dark"):
        written += gc.render(post_spec(dark=(variant == "dark")), ladder,
                             width=760, height=600, source=POST_SOURCE,
                             variants=(variant,))
    for path in written:
        gc.check_labels(path)
        if gc.check_glyphs(path) and not a.allow_gaps:
            raise SystemExit(
                "refusing to write: a label uses a character Public Sans "
                "cannot draw, which silently resets that run in a fallback "
                "face. Substitute the character.")
    if a.png:
        for path in written:
            gc.to_png(path, path[:-4] + ".png")

    # check_coverage is not run on the £/GB figure: it plots every card
    # on one shared axis rather than comparing within capacity levels, so
    # there is no per-level grid to be thin. The trap it does carry —
    # small cards flattering the ranking — is answered on the figure, in
    # the capacity printed on every bar and in the subtitle.
    print("building price-per-gigabyte bars")
    ppg = os.path.join(a.out, "vram_price_per_gb")
    written = []
    for variant in ("light", "dark"):
        written += gc.render(ppg_spec(dark=(variant == "dark")), ppg,
                             width=760, height=470, source=PPG_SOURCE,
                             variants=(variant,))
    for path in written:
        gc.check_labels(path)
        if gc.check_glyphs(path) and not a.allow_gaps:
            raise SystemExit(
                "refusing to write: a label uses a character Public Sans "
                "cannot draw, which silently resets that run in a fallback "
                "face. Substitute the character.")
    if a.png:
        for path in written:
            gc.to_png(path, path[:-4] + ".png")

    # No check_coverage call here by design — see the block comment
    # above ECI_CLOSED for why it has no denominator on this figure.
    print("building capability ladder")
    cap = os.path.join(a.out, "vram_capability_ladder")
    written = []
    for variant in ("light", "dark"):
        written += gc.render(capability_spec(dark=(variant == "dark")),
                             cap, width=760, height=600,
                             source=CAP_SOURCE, variants=(variant,))
    for path in written:
        gc.check_labels(path)
        if gc.check_glyphs(path) and not a.allow_gaps:
            raise SystemExit(
                "refusing to write: a label uses a character Public Sans "
                "cannot draw, which silently resets that run in a fallback "
                "face. Substitute the character.")
    if a.png:
        for path in written:
            gc.to_png(path, path[:-4] + ".png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
