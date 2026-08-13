#!/usr/bin/env python3
"""Draw the APPG on AI's published two-year round-table programme.

Why this exists
---------------
The All-Party Parliamentary Group on Artificial Intelligence publishes a
full forward programme — every round-table evidence session it will hold
through November 2027, dated, with the questions each will ask. All of
them sit in the UK Parliament and are chaired by parliamentarians. It is
public, it is specific, and almost nobody outside the AI policy circuit
knows it exists, which is reason enough to draw it.

The finding on the figure is narrower and checkable. The brochure's own
themes page names **"AI Skills and Workforce Preparedness"** as a key
area under *AI and the UK Economy, Industry and Workforce*. Across all
fourteen sessions in the published programme, none is dedicated to it.

That is stated as a fact and left there, per the project's
understatement rule. It is deliberately **not** dressed as a failure:
the 25 January 2027 session on robotics and manufacturing does ask what
skills gaps need addressing and how to cultivate an AI-literate
manufacturing workforce, and the subtitle says so. The point is the
absence of a session of its own, not an absence of interest, and a
reader who downloads the brochure can check both halves.

A source that contradicts itself
--------------------------------
The brochure gives the environment session two different dates: 10
October 2027 on its detail page, 18 October 2027 in its Overview 2027
summary table. Neither is obviously the erratum. The later date is
plotted because the overview table is the document's own consolidated
schedule, and the discrepancy is printed on the figure rather than
quietly resolved — a chart that silently picks one of two published
dates is making an editorial call its reader cannot see.

Why colour encodes held-versus-scheduled and nothing else
---------------------------------------------------------
The brochure sorts its work into eight themes. Eight exceeds the five
this project's categorical palette can hold apart (`palette_check.py`
measures that), and collapsing them into five would mean inventing a
taxonomy the source does not use in order to fit a colour limit — the
wrong way round. So colour carries the one distinction the data really
supports, and all fourteen sessions are shown so the count in the title
is checkable on the figure itself.

Requires Python with `vl-convert-python`.

Usage
-----
    python tools/build_appg_figure.py --png
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gap_chart as gc                                      # noqa: E402

# ------------------------------------------------------------------ data
#
# APPG AI 2026-2027 programme brochure (Big Innovation Centre), read
# 2026-08-13. Dates and titles are transcribed from the brochure's own
# "Overview 2026" and "Overview 2027" summary tables, which are the
# document's consolidated schedule, cross-checked against each session's
# detail page. The only disagreement between the two is the environment
# session — see the module docstring.
#
# Quarterly Advisory Board meetings are deliberately excluded: they are
# internal governance rather than evidence sessions, so counting them
# would inflate the denominator the title depends on.

HELD = "Held"
SCHEDULED = "Scheduled"

SESSIONS = [
    # date,        title,                              status,    side
    ("2026-01-26", "Horizon Scanning",                  HELD,      "right"),
    ("2026-03-09", "AI Growth Zones",                   HELD,      "right"),
    ("2026-05-11", "AI and Technology Sovereignty",     HELD,      "right"),
    ("2026-06-15", "Youth Perspectives on AI",          HELD,      "right"),
    ("2026-09-07", "AI Without Borders",                SCHEDULED, "right"),
    ("2026-10-19", "Autonomous Vehicles",               SCHEDULED, "right"),
    ("2026-11-16", "AI in Welfare and Citizen Support", SCHEDULED, "right"),
    ("2027-01-25", "AI in Robotics and Manufacturing",  SCHEDULED, "right"),
    ("2027-03-08", "The Hardware of AI",                SCHEDULED, "right"),
    ("2027-05-10", "AI and the Future of Human Autonomy", SCHEDULED, "right"),
    ("2027-06-14", "AI in Education",                   SCHEDULED, "right"),
    ("2027-09-06", "AI and National Security Revisited", SCHEDULED, "left"),
    ("2027-10-18", "AI and the Environment",            SCHEDULED, "left"),
    ("2027-11-22", "AI and Economic Inequalities",      SCHEDULED, "left"),
]

# Short date labels, drawn beside each point because the axis only ticks
# quarterly and the exact sitting date is the useful thing to take away.
MONTH = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr", "05": "May",
         "06": "Jun", "07": "Jul", "08": "Aug", "09": "Sep", "10": "Oct",
         "11": "Nov", "12": "Dec"}

TITLE = "What Parliament's AI group will discuss until November 2027"

SUBTITLE = ("Every round-table evidence session in the APPG on AI's published "
            "programme, all held in the UK Parliament.\nIts themes page names "
            "\"AI Skills and Workforce Preparedness\" as a key area. The "
            "25 January 2027 session on robotics\nand manufacturing does ask "
            "what skills gaps need addressing; none of the fourteen is given "
            "over to the question.")

SOURCE = ("Source: APPG on Artificial Intelligence 2026-2027 programme "
          "brochure, Big Innovation Centre, read 13 August 2026.\n"
          "Quarterly Advisory Board meetings are excluded — internal "
          "governance, not evidence sessions. The brochure dates the "
          "environment\nsession 10 October on its detail page and 18 October "
          "in its overview table; the later date is shown. "
          "Grounded AI Practice.")

ORDER = [t for _, t, *_ in SESSIONS]


def spec(dark=False):
    rows = []
    for date, title, status, side in SESSIONS:
        y, m, d = date.split("-")
        rows.append({"session": title, "date": date, "status": status,
                     "side": side,
                     "when": f"{int(d)} {MONTH[m]} {y[2:]}"})
    # Held sessions take the quiet neutral and scheduled ones the accent,
    # so the eye lands on what has not happened yet.
    fg = gc.PALETTE["paper"] if dark else gc.PALETTE["ink"]
    palette = [gc.PALETTE["stone"], gc.PALETTE["ember"]]

    enc = {
        "y": {"field": "session", "type": "nominal", "sort": ORDER,
              "axis": {"title": None, "labelFontSize": 13,
                       "labelLimit": 250, "domain": False, "ticks": False}},
        "x": {"field": "date", "type": "temporal",
              "axis": {"title": None, "format": "%b %Y",
                       "tickCount": {"interval": "month", "step": 3},
                       "grid": True},
              "scale": {"padding": 26}},
    }
    return {
        "data": {"values": rows},
        "title": {"text": TITLE, "subtitle": SUBTITLE.split("\n")},
        "layer": [
            {"mark": {"type": "point", "filled": True, "size": 200,
                      "opacity": 1},
             "encoding": {**enc,
                          "color": {"field": "status", "type": "nominal",
                                    "scale": {"domain": [HELD, SCHEDULED],
                                              "range": palette},
                                    "legend": {"title": None,
                                               "labelLimit": 0}}}},
            # Two filtered layers rather than field-driven `align`/`dx`:
            # those are mark properties and Vega-Lite silently ignores
            # scales placed on them, which centres every label on its own
            # marker. No check catches it; only the render does.
            *[{"transform": [{"filter": f"datum.side === '{side}'"}],
               "mark": {"type": "text", "fontSize": 12, "fontWeight": 600,
                        "baseline": "middle",
                        "align": "left" if side == "right" else "right",
                        "dx": 15 if side == "right" else -15},
               "encoding": {**enc, "text": {"field": "when"},
                            "color": {"value": fg}}}
              for side in ("right", "left")],
        ],
        "resolve": {"scale": {"color": "independent"}},
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default=os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "assets", "figures"))
    ap.add_argument("--png", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    # check_coverage is not run: every session sits at its own date, so
    # each x level holds exactly one status by construction and the
    # count would refuse every honest version of this figure.
    print("building APPG programme figure")
    stem = os.path.join(a.out, "appg_programme")
    written = []
    for variant in ("light", "dark"):
        written += gc.render(spec(dark=(variant == "dark")), stem,
                             width=560, height=480, source=SOURCE,
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
