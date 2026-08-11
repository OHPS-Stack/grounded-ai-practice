#!/usr/bin/env python3
"""Draw the figure for the effective-prompting pilot unit.

Why this exists
---------------
The unit's one mechanism diagram — what the learner knows, the fraction
of it that becomes the prompt, and the model predicting from exactly
that fraction — started life as a Mermaid sketch in
`drafts/effective_prompting.md`. Promotion to the Word pipeline needs a
real image (`md_to_docx.py` takes `![caption](path)` only), and the
diagram's whole point is proportion: the tall column of what you know
against the small box of what you typed. A hand grid draws that
relationship deliberately; Mermaid's auto-layout gives every node equal
weight, which is the opposite of the message.

Drawn with Pillow on the same helpers, palette and installed Public Sans
faces as `build_server_guide_figures.py`, from which this imports — one
set of drawing conventions, not two copies drifting apart. Boxes and
arrows on a computed grid, no curve work, so the trace-and-Inkscape
route for concept artwork does not apply.

Requirements
------------
Python with Pillow, the Public Sans TTF faces installed, and
`tools/build_server_guide_figures.py` present beside this file. Writes
PNGs into assets/figures/ by default.

Usage
-----
    python tools/build_prompting_figures.py
    python tools/build_prompting_figures.py -o some/other/folder

Command-line only, per project_log.md Entry 049 — a build step runs
this, not a person at a window.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_server_guide_figures as sg                     # noqa: E402

INK, EMBER, SAND = sg.INK, sg.EMBER, sg.SAND
PAPER, MIST, SAGE = sg.PAPER, sg.MIST, sg.SAGE
STONE, GRAPHITE = sg.STONE, sg.GRAPHITE


# ---------------------------------------------------------------------------
# Figure — the gap between what you know and what you typed
# ---------------------------------------------------------------------------
def fig_prompt_gap(out_dir):
    img, d = sg.canvas(350)
    sg.text(d, 30, 22, "What you know stays with you; the model gets the prompt",
            "Bold", 18, INK)

    # Everything the learner knows — deliberately the tallest thing here.
    sg.box(d, 30, 64, 250, 230, MIST, SAGE, radius=12)
    sg.text(d, 46, 78, "WHAT YOU KNOW", "Bold", 11, STONE)
    rows = [
        "The task, and who it's for",
        "The background and history",
        "The shape you want",
        "How you sound",
        "What must not be said",
    ]
    for i, r in enumerate(rows):
        sg.text(d, 46, 104 + i * 26, r, "Regular", 13, INK)
    sg.text(d, 46, 242, "…and everything else\nin your head", "Regular", 11,
            STONE)

    # The label sits under the arrow, clear of both boxes — above it, the
    # first render struck the text through with the arrow and ran it into
    # the prompt box.
    sg.arrow(d, 285, 179, 350, 179)
    sg.text(d, 317, 190, "typing", "Medium", 11, EMBER, anchor="ma")

    # The prompt — small on purpose; the size difference is the message.
    sg.box(d, 355, 137, 192, 84, SAND, EMBER, radius=8)
    sg.text(d, 367, 149, "THE PROMPT", "Bold", 11, GRAPHITE)
    sg.text(d, 367, 171, "“Write an email about\na price increase.”",
            "Regular", 13, INK)
    sg.text(d, 355, 231, "The only thing the model sees.", "Medium", 12, EMBER)
    sg.text(d, 355, 251, "The rest never left your head.", "Regular", 11,
            STONE)

    sg.arrow(d, 552, 179, 585, 179)

    sg.box(d, 590, 128, 182, 104, INK, radius=8)
    sg.text(d, 602, 140, "THE MODEL", "Bold", 11, SAGE)
    sg.text(d, 602, 162, "Predicts the most\nplausible continuation\nof exactly what it got",
            "Regular", 12, PAPER)

    sg.arrow(d, 777, 179, 812, 179)

    sg.box(d, 817, 128, 158, 104, MIST, SAGE, radius=8)
    sg.text(d, 831, 140, "THE ANSWER", "Bold", 11, STONE)
    sg.text(d, 831, 162, "Fluent, confident —\nordinary wherever\nyou left a gap",
            "Regular", 12, INK)

    sg.text(d, 30, 316,
            "Every gap gets filled with the most ordinary assumption — or an "
            "invented specific. Nothing warns you which.",
            "Medium", 13, GRAPHITE)
    return sg.save(img, out_dir, "fig_prompt_gap.png")


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("-o", "--out", default=os.path.join("assets", "figures"))
    a = p.parse_args()
    os.makedirs(a.out, exist_ok=True)
    print("building prompting-unit figures")
    fig_prompt_gap(a.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
