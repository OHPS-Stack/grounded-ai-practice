#!/usr/bin/env python3
"""Build the landing site's web fonts — subsetted WOFF2 from installed Public Sans.

Why this exists
---------------
The site (`docs/`) declares Public Sans with a system-font fallback.
Without files to serve, only visitors who happen to have the face
installed see the brand type. This script produces self-hosted WOFF2
subsets from the Public Sans TTFs already installed as user fonts, so
the pages ship the brand face at web-appropriate sizes with no CDN, no
third-party request, and nothing new for `font-src 'self'` to allow.

Subsetting keeps Basic Latin, Latin-1 Supplement and General
Punctuation (U+0020–007E, U+00A0–00FF, U+2000–206F) — deliberately a
character-range subset rather than a scrape of today's page text, so
the creator's prose pass cannot silently step outside the glyph set.
Kerning and default OpenType layout features are preserved. Note that
Public Sans carries no U+2011 (non-breaking hyphen); the pages use a
plain hyphen in a `white-space: nowrap` span instead.

The faces built are the weights the stylesheet actually uses (400,
400 italic, 600, 700, 800). Adding a weight to the CSS means adding
its face here and re-running.

Self-check: every output is reopened with fontTools, probed for a set
of characters the site's copy depends on (£, en/em dash, curly quotes,
middle dot), and reported with its size. A missing probe glyph or an
implausible file size fails the run.

Scope note: these files style the HTML pages only. The figures are
SVGs loaded through `<img>`, and browsers do not fetch external fonts
for documents embedded that way — figure text renders in the viewer's
installed fonts by design (see `tools/build_site_figures.py`).

`docs/fonts/LICENSE.md` (SIL OFL, from the upstream Public Sans
repository) must accompany the files; the script refuses to build
without it rather than distribute unlicensed copies.

Requires Python with fontTools and brotli (`pip install fonttools
brotli`), and the Public Sans static TTFs installed as user fonts. A
build-step tool, command-line by the Entry 049 decision.

Usage
-----
    python tools/build_site_fonts.py          # writes docs/fonts/*.woff2
    python tools/build_site_fonts.py --out DIR
"""

import argparse
import os
import sys

from fontTools.subset import Subsetter, Options, parse_unicodes
from fontTools.ttLib import TTFont

FACES = [
    ("PublicSans-Regular.ttf",  "public_sans_400.woff2"),
    ("PublicSans-Italic.ttf",   "public_sans_400_italic.woff2"),
    ("PublicSans-SemiBold.ttf", "public_sans_600.woff2"),
    ("PublicSans-Bold.ttf",     "public_sans_700.woff2"),
    ("PublicSans-ExtraBold.ttf", "public_sans_800.woff2"),
]

UNICODE_RANGES = "0020-007E,00A0-00FF,2000-206F"

# Characters the site's copy depends on; a subset missing any of these
# is a broken build, not a smaller one.
PROBES = {0x00A3: "£", 0x2013: "–", 0x2014: "—", 0x2018: "'",
          0x201C: '"', 0x00B7: "·"}

SIZE_FLOOR_KB, SIZE_CEIL_KB = 8, 80


def find_fonts_dir():
    candidates = [
        os.path.join(os.environ.get("LOCALAPPDATA", ""),
                     "Microsoft", "Windows", "Fonts"),
        r"C:\Windows\Fonts",
    ]
    for d in candidates:
        if os.path.exists(os.path.join(d, FACES[0][0])):
            return d
    sys.exit("Public Sans TTFs not found in user or system fonts. "
             "Install the static faces (see project_brief.md, Word "
             "document conventions) and re-run.")


def build_face(src, dest):
    font = TTFont(src)
    options = Options()
    options.flavor = "woff2"
    subsetter = Subsetter(options)
    subsetter.populate(unicodes=parse_unicodes(UNICODE_RANGES))
    subsetter.subset(font)
    font.save(dest)

    # reopen the artefact itself — verify what was written, not what
    # was intended
    check = TTFont(dest)
    cmap = check.getBestCmap()
    missing = [ch for cp, ch in PROBES.items() if cp not in cmap]
    if missing:
        sys.exit(f"{dest}: probe characters missing after subset: "
                 f"{' '.join(missing)}")
    kb = os.path.getsize(dest) / 1024
    if not SIZE_FLOOR_KB <= kb <= SIZE_CEIL_KB:
        sys.exit(f"{dest}: {kb:.0f} KB is outside the plausible "
                 f"{SIZE_FLOOR_KB}-{SIZE_CEIL_KB} KB range for a subset "
                 "face — inspect before shipping.")
    return check["maxp"].numGlyphs, kb


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", default=os.path.join(
        os.path.dirname(__file__), "..", "docs", "fonts"))
    args = parser.parse_args()

    licence = os.path.join(args.out, "LICENSE.md")
    if not os.path.exists(licence):
        sys.exit(f"{licence} is missing. The OFL licence text must ship "
                 "with the font files — restore it from the upstream "
                 "Public Sans repository before building.")

    src_dir = find_fonts_dir()
    os.makedirs(args.out, exist_ok=True)
    total = 0.0
    for src_name, dest_name in FACES:
        src = os.path.join(src_dir, src_name)
        if not os.path.exists(src):
            sys.exit(f"missing source face: {src}")
        glyphs, kb = build_face(src, os.path.join(args.out, dest_name))
        total += kb
        print(f"wrote {dest_name:32} {glyphs:4} glyphs  {kb:5.1f} KB")
    print(f"total {total:.1f} KB across {len(FACES)} faces")


if __name__ == "__main__":
    main()
