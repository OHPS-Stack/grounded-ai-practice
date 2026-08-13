#!/usr/bin/env python3
"""Draw the UK AI events figure: what it costs to get in the room.

Why this exists
---------------
The project's outward work now depends on being in rooms that contain
policymakers, SME leaders and practitioners — the audiences the research
argues are underserved. Which rooms are reachable is a cost question with
a structure worth seeing: the entry price of a UK AI event in 2026 spans
two orders of magnitude for broadly the same subject, and the cheapest
doors are opened by an application rather than a payment.

That is a two-variable claim — date against route, with cost as a direct
label — so it goes through `gap_chart.py` rather than the hand-composed
SVG route, for the same reason the VRAM figures do: it needs real scales.

What is deliberately NOT on the figure
--------------------------------------
Travel and accommodation. They dominate the real cost for anyone
attending from outside the host city, and for the two-night events they
exceed every entry price here except the London ones. But the project's
data-driven-figures rule forbids hand-estimated numbers on a published
chart, and a defensible hotel figure would need its own dated pricing
pass. So the absence is stated on the figure in words instead, per the
bias checklist's "say what isn't counted" trigger, and left unplotted.

Sources and holes
-----------------
Every row was read from the organiser's own site on 2026-08-13, not from
a search summary or an aggregator. Two holes are recorded rather than
filled, and they are different kinds:

  - Birmingham Tech Week publishes no pricing on its public pages and
    names no volunteer route. That is *not published where I could reach
    it*, which is not the same as *does not exist* — the figure says
    "not published" and the notes say to ask.

  - AI UK 2027 (the Alan Turing Institute's national showcase) has no
    announced date, and its registration page returned HTTP 403. It is
    therefore absent from the figure entirely rather than drawn at a
    guessed date, and carried in the notes instead.

Two events were checked and dropped as past: the BridgeAI Annual
Showcase (09 March 2026) and AI Summit London 2026 (10-11 June 2026).
CogX was dropped because the festival was wound down in 2025.

Requirements: Python with `vl-convert-python`.

Usage
-----
    python tools/build_events_figure.py
    python tools/build_events_figure.py --out DIR --png
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gap_chart as gc                                      # noqa: E402

# ------------------------------------------------------------------ data
#
# Read from each organiser's own site, 2026-08-13. `cost` is the cheapest
# published route, which is what the figure encodes; the fuller pricing
# for each event lives in the notes rather than on the chart, because a
# figure that lists every pass tier stops being readable at a glance.
#
# `side` places the cost label. The June 2027 row sits at the right edge
# of the time axis, so its label is drawn to the left — a right-side
# label there runs off the canvas, which `check_labels` now catches but
# which is cheaper to avoid than to discover.

APPLY = "Free, but you must apply"
CHEAP = "Pay, under £100"
FULL = "Pay, full price only"
UNKNOWN = "Price not published"

# London Tech Week is drawn as unpriced rather than free, and the
# distinction matters. Its complimentary early-career pass and its
# £99.50 campus pass are both *2026* prices; the 2027 edition has
# confirmed dates and no published pricing at all. Carrying a 2026 price
# forward to a 2027 date would be exactly the conflation this project's
# rules exist to catch, so the row states what is actually known.
EVENTS = [
    # name,                          start date,   route,   cost label,    side
    ("UK AI Conference, Nottingham", "2026-09-29", CHEAP,   "£35",         "right"),
    ("OxGen AI Summit, Oxford",      "2026-10-15", APPLY,   "£0",          "right"),
    ("Birmingham Tech Week",         "2026-10-19", UNKNOWN, "not priced",  "right"),
    ("AI World Congress, London",    "2026-11-25", FULL,    "£2,295",      "right"),
    ("BCS SGAI, Cambridge",          "2026-12-14", CHEAP,   "£35",         "right"),
    ("London Tech Week",             "2027-06-07", UNKNOWN, "2027 TBC",    "left"),
]

TITLE = "Getting into a UK AI event costs £35 in Nottingham, £2,295 in London."

SUBTITLE = ("Cheapest published route into six UK AI events, September 2026 "
            "to June 2027. Entry price only,\nexcluding VAT. Travel and "
            "accommodation are not counted here, and are the larger cost "
            "for\nanything needing an overnight stay.")

SOURCE = ("Sources: organiser websites, read 13 August 2026 — uk-ai.org, "
          "oxgensummit.org, birminghamtechweek.com,\n"
          "aiconference.london, bcs-sgai.org, londontechweek.com. "
          "\"Not published\" means not published, not free:\n"
          "Birmingham Tech Week lists no prices, and London Tech Week has "
          "2027 dates but no 2027 pricing.\n"
          "AI UK 2027 is absent because no date is announced. "
          "Grounded AI Practice.")

ORDER = [name for name, *_ in EVENTS]


def spec(dark=False):
    rows = [{"event": n, "date": d, "route": r, "cost": c, "side": s}
            for n, d, r, c, s in EVENTS]
    palette = gc.TIER["category_dark" if dark else "category_light"]
    # Domain fixed explicitly so a route's colour does not change when the
    # event list is edited — a legend that reshuffles between builds makes
    # two versions of the same figure impossible to compare.
    domain = [APPLY, CHEAP, FULL, UNKNOWN]

    base = {"data": {"values": rows}}
    enc = {
        "y": {"field": "event", "type": "nominal", "sort": ORDER,
              "axis": {"title": None, "labelFontSize": 13,
                       "labelLimit": 220, "domain": False, "ticks": False}},
        "x": {"field": "date", "type": "temporal",
              # Monthly ticks collide across a ten-month span at this
              # width — the label check caught eight overlapping pairs
              # before this was stepped to every second month.
              "axis": {"title": None, "format": "%b %Y",
                       "tickCount": {"interval": "month", "step": 2},
                       "grid": True},
              "scale": {"padding": 26}},
    }
    return {
        **base,
        "title": {"text": TITLE, "subtitle": SUBTITLE.split("\n")},
        "layer": [
            {"mark": {"type": "point", "filled": True, "size": 200,
                      "opacity": 1},
             "encoding": {**enc,
                          "color": {"field": "route", "type": "nominal",
                                    "scale": {"domain": domain,
                                              "range": palette[:len(domain)]},
                                    "legend": {"title": None,
                                               "columns": 2,
                                               "symbolLimit": 4}}}},
            # Cost is direct-labelled rather than left to the legend
            # because no categorical palette in this project's system
            # survives greyscale — `palette_check.py` measures that, and
            # the honest response is a figure that reads without colour.
            #
            # Two filtered layers rather than one layer with `align` and
            # `dx` driven by a field: those are mark properties, and
            # Vega-Lite silently ignored the scales put on them, which
            # centred every label on top of its own marker. No check
            # catches that — the labels neither overlap each other nor
            # leave the canvas — so it was found by looking at the
            # render, which is what the geometry rule is for.
            *[{"transform": [{"filter": f"datum.side === '{side}'"}],
               "mark": {"type": "text", "fontSize": 13, "fontWeight": 600,
                        "baseline": "middle",
                        "align": "left" if side == "right" else "right",
                        "dx": 15 if side == "right" else -15},
               "encoding": {
                   **enc,
                   "text": {"field": "cost"},
                   "color": {"value": gc.PALETTE["paper"] if dark
                             else gc.PALETTE["ink"]}}}
              for side in ("right", "left")],
        ],
        "resolve": {"scale": {"color": "independent"}},
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default=os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "assets", "figures"))
    ap.add_argument("--png", action="store_true",
                    help="also rasterise each SVG at 2x")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    # No check_coverage call by design. That check refuses a comparison
    # the data cannot support by counting categories at each level of the
    # x variable — but every event here sits at its own date, so each
    # level holds exactly one category by construction and the count
    # would refuse every honest version of this figure. The comparison
    # the chart actually invites is across routes, which is guarded by
    # the fixed colour domain above.
    print("building UK AI events figure")
    stem = os.path.join(a.out, "uk_ai_events")
    written = []
    for variant in ("light", "dark"):
        written += gc.render(spec(dark=(variant == "dark")), stem,
                             width=770, height=250, source=SOURCE,
                             variants=(variant,))
    for path in written:
        gc.check_labels(path)
        if gc.check_glyphs(path):
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
