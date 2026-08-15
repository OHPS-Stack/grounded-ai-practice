"""Draws the two figures in the Proton Drive setup document.

`proton_architecture` — the choice that decides whether a repository
stays intact: syncing the repository root puts `.git` under a service
that copies rather than merges, while syncing only `internal/` leaves
git in sole charge of everything it tracks. The document argues this in
words; the diagram is what makes the boundary obvious at a glance, which
is the whole reason it exists as a picture rather than a callout.

`proton_file_states` — the three states a synced file can occupy, and
what each means for a script that tries to read it. This is the
mechanism people get wrong, because a cloud placeholder looks like a
present file in File Explorer: it has a name, a size and a thumbnail,
and nothing on screen distinguishes it from real contents.

Imports its drawing helpers, palette and font loading from
`build_server_guide_figures.py` rather than copying them, so the
project's figures stay one set of conventions. Outputs land in
`assets/figures/`, which is tracked: both diagrams are generic mechanism
drawings and carry no private paths, even though the document they
illustrate is internal.

Requires Python with Pillow, the Public Sans faces installed as system
fonts, and its sibling script beside it. Command-line by the Entry 049
decision — a build step, not a learner-facing tool.

Usage:
    python tools/build_proton_figures.py
    python tools/build_proton_figures.py --out some/other/dir
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
# Figure 1 — the two arrangements
# ---------------------------------------------------------------------------
def fig_architecture(out_dir):
    img, d = sg.canvas(470)
    sg.text(d, 30, 22, "What you point Proton Drive at decides whether git stays in charge",
            "Bold", 18, INK)

    # --- Left: the wrong arrangement -------------------------------------
    sg.box(d, 30, 66, 440, 372, MIST, STONE, radius=12)
    sg.text(d, 48, 82, "SYNCING THE REPOSITORY ROOT", "Bold", 11, STONE)
    sg.text(d, 48, 100, "Wrong", "Bold", 15, EMBER)

    sg.box(d, 48, 130, 404, 246, PAPER, STONE, radius=8)
    sg.text(d, 64, 142, "grounded-ai-practice/", "Bold", 12, INK)

    rows = [
        (".git/", "history, refs, objects", EMBER),
        ("research_log.md", "tracked", EMBER),
        ("project_log.md", "tracked", EMBER),
        ("internal/", "gitignored", SAGE),
    ]
    y = 168
    for name, note, tint in rows:
        sg.box(d, 64, y, 372, 40, SAND if tint is EMBER else MIST,
               tint, radius=6, width=2)
        sg.text(d, 78, y + 8, name, "Bold", 12, INK)
        sg.text(d, 78, y + 23, note, "Regular", 10, STONE)
        y += 50

    sg.text(d, 48, 390, "Proton copies whichever version it saw last.",
            "Bold", 11, EMBER)
    sg.text(d, 48, 410, "Two machines' git state can overwrite each other.",
            "Regular", 10, STONE)

    # --- Right: the correct arrangement ----------------------------------
    sg.box(d, 530, 66, 440, 372, MIST, SAGE, radius=12)
    sg.text(d, 548, 82, "SYNCING ONLY internal/", "Bold", 11, STONE)
    sg.text(d, 548, 100, "Correct", "Bold", 15, INK)

    sg.box(d, 548, 130, 404, 246, PAPER, STONE, radius=8)
    sg.text(d, 564, 142, "grounded-ai-practice/", "Bold", 12, INK)

    rows2 = [
        (".git/", "git only", None),
        ("research_log.md", "git only", None),
        ("project_log.md", "git only", None),
        ("internal/", "Proton Drive, pinned", SAGE),
    ]
    y = 168
    for name, note, tint in rows2:
        fill = MIST if tint else PAPER
        sg.box(d, 564, y, 372, 40, fill, tint or MIST, radius=6, width=2)
        sg.text(d, 578, y + 8, name, "Bold", 12, INK)
        sg.text(d, 578, y + 23, note, "Regular", 10,
                INK if tint else STONE)
        y += 50

    sg.text(d, 548, 390, "Each mechanism carries only what it is good at.",
            "Bold", 11, INK)
    sg.text(d, 548, 410, "Nothing is in charge of the same file twice.",
            "Regular", 10, STONE)

    return sg.save(img, out_dir, "proton_architecture.png")


# ---------------------------------------------------------------------------
# Figure 2 — the three file states
# ---------------------------------------------------------------------------
def fig_file_states(out_dir):
    img, d = sg.canvas(340)
    sg.text(d, 30, 22, "A placeholder looks exactly like a real file until something opens it",
            "Bold", 18, INK)

    cards = [
        ("Available when online",
         "Metadata and thumbnail only",
         ["Name, size and icon are local", "Contents are not on disk",
          "Reading it triggers a download", "Fails with no connection"],
         SAND, EMBER, "DEFAULT"),
        ("Available on this device",
         "Downloaded, but not protected",
         ["Full contents on disk", "Reads normally", "Can be evicted later",
          "Optimize storage may reclaim it"],
         MIST, STONE, "AFTER OPENING"),
        ("Always keep on this device",
         "Pinned, never evicted",
         ["Full contents on disk", "Reads normally, always",
          "Survives low disk space", "What internal/ is set to"],
         SAGE, INK, "THE TARGET"),
    ]

    x = 30
    for title, sub, bullets, fill, edge, tag in cards:
        sg.box(d, x, 68, 300, 236, fill, edge, radius=12)
        sg.text(d, x + 18, 82, tag, "Bold", 10, STONE)
        sg.text(d, x + 18, 100, title, "Bold", 13, INK)
        sg.text(d, x + 18, 120, sub, "Regular", 11, STONE)
        d.line([sg.s(x + 18), sg.s(142), sg.s(x + 282), sg.s(142)],
               fill=edge, width=sg.s(1))
        by = 154
        for b in bullets:
            sg.text(d, x + 18, by, "•", "Bold", 11, edge)
            sg.text(d, x + 34, by, b, "Regular", 11, INK)
            by += 26
        x += 320

    sg.text(d, 30, 314,
            "The pre-commit hook reads a file inside internal/ on every commit. "
            "Pinning removes the failure mode entirely.",
            "Regular", 11, STONE)

    return sg.save(img, out_dir, "proton_file_states.png")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    default = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "assets", "figures")
    ap.add_argument("--out", default=default, help="output directory")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    print("Building Proton Drive figures into %s" % args.out)
    fig_architecture(args.out)
    fig_file_states(args.out)
    print("Done.")


if __name__ == "__main__":
    main()
