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
    "Prices are single-day UK listings checked 11 Aug 2026 and will move. "
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
    if a.png:
        for path in written:
            gc.to_png(path, path[:-4] + ".png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
