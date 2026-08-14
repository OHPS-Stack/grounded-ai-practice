#!/usr/bin/env python3
"""Fit callout-card and pull-quote shapes in a .docx to the text they contain.

Why this exists
----------------
This project's callout cards and pull quotes (see CLAUDE.md, "Word document
conventions") are Word drawing groups (wpg) built with a fixed height at
construction time. Nothing recomputes that height when the text inside is
edited, so a card holding two lines gets the same box as one holding eight,
and the difference shows up as dead vertical padding above and below the
icon and text. This happened across every callout in
UK_AI_Skills_Ambition_Report.docx and in two of the six groups in
Style_Reference_Example.docx (found and fixed 2026-07-31).

This script measures the real text with the real font (Public Sans, as
installed) and rewrites each group's geometry to fit it, recentring the icon,
divider bar and text box as it goes. Widths are never touched — only heights
and vertical offsets — so the existing size-preset rule (icon well fixed,
text column free) still holds.

How it works
------------
1. Unzips the .docx and reads word/document.xml.
2. Finds every <wpg:wgp> callout-card or pull-quote group.
3. Measures each paragraph's real wrapped height at the text box's actual
   width, using the installed Public Sans font faces at their exact size and
   line-spacing multiplier — not an estimate.
4. Sets card height to max(text height, icon-well height) + 2x padding, or
   quote height to text height + 2x padding, and recentres the icon, divider
   bar and text box within the new height.
5. Rewrites the group's <a:off>/<a:ext> pairs and the drawing's own
   <wp:extent>, repacks the .docx.

This does NOT verify the result. Word document self-checks are
tools/word_preview.ps1 (renders through real Word, catches layout defects)
and tools/word_roundtrip_test.ps1 (saves through real Word, catches the
compatibilityMode/VML defect a render can't). Always run both after using
this script — see CLAUDE.md, "Rendering is not the same check as saving".

Requirements
------------
Python 3.9+ with Pillow     pip install pillow
Public Sans TTF faces       installed as system fonts (Regular/Bold/Italic/
                            BoldItalic under the family name "Public Sans")

Font faces are found automatically on standard install paths; pass
--font-dir to override. If they're missing the script says so and stops
rather than guessing at fallback metrics, since a wrong measurement would
silently reintroduce the padding bug in a different amount.

Examples
--------
Fit in place (back up first — this overwrites the source):

    python tools/fitshapes.py report.docx --in-place

Write to a new file, with wider padding on the callout cards:

    python tools/fitshapes.py report.docx report_fitted.docx --pad 12
"""
from __future__ import annotations

import argparse
import glob
import html
import os
import re
import shutil
import sys
import tempfile
import zipfile

try:
    from PIL import ImageFont
except ImportError:
    sys.exit(
        "Pillow is not installed. This script needs it to measure real font "
        "metrics.\n  pip install pillow"
    )

EMU_PT = 12700
SCALE = 64  # render font this many times larger, for measurement precision

FONT_DIR_CANDIDATES = [
    r"C:\Windows\Fonts",
    # Windows per-user font folder. This is where a right-click > Install
    # puts a font, which is the default action, so it is at least as likely
    # as the system folder above. Left unexpanded and skipped off Windows.
    os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Windows\Fonts"),
    "/Library/Fonts",
    "/System/Library/Fonts",
    os.path.expanduser("~/.local/share/fonts"),
    "/usr/share/fonts/truetype/public-sans",
]

FACE_NAMES = {
    (False, False): ["PublicSans-Regular.ttf"],
    (True, False): ["PublicSans-Bold.ttf"],
    (False, True): ["PublicSans-Italic.ttf"],
    (True, True): ["PublicSans-BoldItalic.ttf"],
}

_font_cache: dict = {}
_font_dir: str | None = None


def find_font_dir(override: str | None) -> str:
    if override:
        if not os.path.isdir(override):
            sys.exit(f"--font-dir does not exist: {override}")
        return override
    for path in FONT_DIR_CANDIDATES:
        if os.path.isdir(path) and glob.glob(os.path.join(path, "PublicSans-Regular*")):
            return path
    sys.exit(
        "Public Sans font faces were not found (checked: "
        + ", ".join(FONT_DIR_CANDIDATES)
        + ").\nThis script measures real glyph widths and cannot estimate "
        "safely without the actual font. Install Public Sans, or pass "
        "--font-dir pointing at the folder holding PublicSans-Regular.ttf "
        "and its Bold/Italic/BoldItalic siblings."
    )


_measure_face: str | None = None
_line_scale: float = 1.0


def _resolve_measure_face(bold: bool) -> str:
    """The override face, with a bold sibling when one sits beside it.

    Measuring Korean text with Public Sans is measuring glyphs the font
    does not have: every Hangul syllable comes back as .notdef, the line
    is underestimated, and the card is then fitted too short for its own
    contents. Pointing this at a face that covers the script is the fix.
    Malgun Gothic ships bold as malgunbd.ttf beside malgun.ttf, which is
    the usual Windows convention, so try that before falling back.
    """
    if not bold:
        return _measure_face
    stem, ext = os.path.splitext(_measure_face)
    for cand in (stem + "bd" + ext, stem + "-Bold" + ext, stem + "b" + ext):
        if os.path.exists(cand):
            return cand
    return _measure_face


def _font(bold: bool, italic: bool, pt: float):
    """The width-measuring font: the override face when one is set."""
    key = (bold, italic, round(pt, 2))
    if _measure_face:
        ckey = ("measure",) + key
        if ckey not in _font_cache:
            _font_cache[ckey] = ImageFont.truetype(
                _resolve_measure_face(bold), max(1, round(pt * SCALE)))
        return _font_cache[ckey]
    return _metrics_font(bold, italic, pt)


def _metrics_font(bold: bool, italic: bool, pt: float):
    """Public Sans, always — the document's base font, used for line height."""
    key = (bold, italic, round(pt, 2))
    if key not in _font_cache:
        for name in FACE_NAMES[(bold, italic)]:
            path = os.path.join(_font_dir, name)
            if os.path.exists(path):
                break
        else:
            hits = glob.glob(os.path.join(_font_dir, "PublicSans-Regular*"))
            if not hits:
                sys.exit(f"No Public Sans face found in {_font_dir}")
            path = hits[0]
        _font_cache[key] = ImageFont.truetype(path, max(1, round(pt * SCALE)))
    return _font_cache[key]


def text_width_pt(text: str, bold: bool, italic: bool, pt: float) -> float:
    return _font(bold, italic, pt).getlength(text) / SCALE


def natural_line_pt(bold: bool, italic: bool, pt: float) -> float:
    """Line height from whichever face is actually drawing the text.

    A CJK face carries taller ascent and descent than a Latin one, and Word
    lays the line out with the font it renders in, so the override face is
    the right source when one is set. An earlier version of this function
    forced Public Sans here, on the theory that Malgun metrics were what
    made Korean cards render several times too deep. That theory was wrong:
    the depth came from measuring XML numeric references instead of
    characters (see paragraphs_of). With that fixed, using the real face's
    metrics is both correct and necessary — Public Sans metrics under-size a
    Korean card and clip its last line.
    """
    asc, desc = _font(bold, italic, pt).getmetrics()
    return (asc + desc) / SCALE * _line_scale


def wrap_count(text: str, bold: bool, italic: bool, pt: float, width_pt: float) -> int:
    """Number of lines `text` occupies when wrapped to width_pt."""
    words, lines, cur = text.split(), 0, ""
    for w in words:
        trial = (cur + " " + w).strip()
        if not cur or text_width_pt(trial, bold, italic, pt) <= width_pt:
            cur = trial
        else:
            lines += 1
            cur = w
    return max(1, lines + (1 if cur else 0))


# ---------------------------------------------------------------- parsing
DEFAULT_SZ = 21       # half-points, matches this project's docDefaults
DEFAULT_LINE = 264    # w:line, lineRule auto (percent of natural line height x100)
DEFAULT_AFTER = 200   # twips


def paragraphs_of(txbx_xml: str):
    """Yield (text, bold, italic, size_pt, line_mult, after_pt) per paragraph."""
    out = []
    for pm in re.finditer(r"<w:p\b[^>]*>(.*?)</w:p>", txbx_xml, re.S):
        p = pm.group(1)
        ppr = re.search(r"<w:pPr>(.*?)</w:pPr>", p, re.S)
        line, after = DEFAULT_LINE, DEFAULT_AFTER
        if ppr:
            sp = re.search(r"<w:spacing([^/]*)/>", ppr.group(1))
            if sp:
                m = re.search(r'w:line="(\d+)"', sp.group(1))
                if m:
                    line = int(m.group(1))
                m = re.search(r'w:after="(\d+)"', sp.group(1))
                if m:
                    after = int(m.group(1))
        # Unescape before measuring. The writer emits non-ASCII as XML numeric
        # references, so the raw run text holds "&#8212;" where the document
        # shows one em-dash, and "&#47928;" per Korean syllable. Measuring the
        # reference instead of the character counts seven characters for one
        # and inflates the fitted height — mildly in English, by a factor of
        # about five in Korean, which is how this was finally noticed.
        text = html.unescape(
            "".join(re.findall(r"<w:t(?:\s[^>]*)?>([^<]*)</w:t>", p)))
        rpr = re.search(r"<w:rPr>(.*?)</w:rPr>", p, re.S)
        bold = italic = False
        sz = DEFAULT_SZ
        if rpr:
            r = rpr.group(1)
            bold = "<w:b/>" in r
            italic = "<w:i/>" in r
            m = re.search(r'<w:sz w:val="(\d+)"', r)
            if m:
                sz = int(m.group(1))
        out.append((text, bold, italic, sz / 2.0, line / 240.0, after / 20.0))
    return out


def text_block_height_pt(txbx_xml: str, box_width_pt: float) -> float:
    total = 0.0
    paras = paragraphs_of(txbx_xml)
    for i, (text, b, it, pt, line_mult, after) in enumerate(paras):
        n = wrap_count(text, b, it, pt, box_width_pt) if text else 1
        total += n * natural_line_pt(b, it, pt) * line_mult
        if i < len(paras) - 1:
            total += after
    return total


# ---------------------------------------------------------------- fitting
def _nums(xml: str, tag: str):
    return [(m.start(), m.end(), int(m.group(1)), int(m.group(2)))
            for m in re.finditer(r'<a:%s (?:x|cx)="(-?\d+)" (?:y|cy)="(-?\d+)"/>' % tag, xml)]


def fit_group(group_xml: str, pad_pt: float, quote_pad_pt: float):
    """Return (new_group_xml, new_height_emu). new_height_emu is None if this
    group didn't match a recognised shape (callout card or pull quote) and
    was left untouched."""
    offs = _nums(group_xml, "off")
    exts = _nums(group_xml, "ext")
    shapes = len(re.findall(r"<wps:wsp>", group_xml))
    # <pic:pic> sometimes carries its own inline xmlns:pic declaration
    # (<pic:pic xmlns:pic="...">) and sometimes doesn't, depending on how Word
    # serialised it — an exact "<pic:pic>" substring check misses the former
    # and silently skips every callout card built that way. Found 2026-07-31
    # when this dropped all three callout cards in a real report while
    # leaving its pull quotes (which don't have a picture to detect) fitted.
    has_pic = bool(re.search(r"<pic:pic\b", group_xml))

    txbx = re.search(r"<w:txbxContent>(.*?)</w:txbxContent>", group_xml, re.S)
    if not txbx:
        return group_xml, None

    # the text rectangle is the last wps:wsp; its width sets the wrap
    text_ext = exts[-1]
    box_w_pt = text_ext[2] / EMU_PT
    text_h_pt = text_block_height_pt(txbx.group(1), box_w_pt)

    if shapes >= 4 and has_pic:                     # callout card: bg, icon-well, icon, bar, text
        icon_h = exts[2][3]                          # icon well is square
        content_h = max(text_h_pt * EMU_PT, icon_h)
        new_h = round(content_h + 2 * pad_pt * EMU_PT)
        icon_y = round((new_h - icon_h) / 2)
        pic_h = exts[3][3]
        pic_y = icon_y + round((icon_h - pic_h) / 2)
        bar_h = exts[4][3]
        bar_y = round((new_h - bar_h) / 2)
        text_y = round(pad_pt * EMU_PT)
        text_h = new_h - 2 * text_y
        new_off_y = [0, 0, icon_y, pic_y, bar_y, text_y]
        new_ext_cy = [new_h, new_h, icon_h, pic_h, bar_h, text_h]
    elif shapes == 2:                                # pull quote: bar, text
        new_h = round(text_h_pt * EMU_PT + 2 * quote_pad_pt * EMU_PT)
        new_off_y = [0, 0, 0]
        new_ext_cy = [new_h, new_h, new_h]
    else:
        return group_xml, None

    out, cursor = [], 0
    events = sorted([(s, e, "off", i) for i, (s, e, _, _) in enumerate(offs)] +
                    [(s, e, "ext", i) for i, (s, e, _, _) in enumerate(exts)])
    for s, e, kind, idx in events:
        out.append(group_xml[cursor:s])
        frag = group_xml[s:e]
        if kind == "off" and idx < len(new_off_y):
            frag = re.sub(r'y="-?\d+"', 'y="%d"' % new_off_y[idx], frag)
        elif kind == "ext" and idx < len(new_ext_cy):
            attr = "cy" if "cy=" in frag else "y"
            frag = re.sub(r'%s="-?\d+"' % attr, '%s="%d"' % (attr, new_ext_cy[idx]), frag)
        out.append(frag)
        cursor = e
    out.append(group_xml[cursor:])
    return "".join(out), new_h


CHEXT = re.compile(r'<a:chExt cx="(\d+)" cy="(\d+)"/>')


def fit_document_xml(xml: str, pad_pt: float, quote_pad_pt: float, log=None):
    """Fit every wpg group in a document.xml string; returns the new string."""
    result, cursor, n = [], 0, 0
    for m in re.finditer(r"<wpg:wgp>.*?</wpg:wgp>", xml, re.S):
        new_group, new_h = fit_group(m.group(0), pad_pt, quote_pad_pt)
        if new_h is None:
            continue
        new_group = CHEXT.sub(lambda g: '<a:chExt cx="%s" cy="%d"/>' % (g.group(1), new_h),
                              new_group)
        head = xml[cursor:m.start()]
        old_h = int(re.search(r'<a:ext cx="\d+" cy="(\d+)"/>', m.group(0)).group(1))
        head = re.sub(r'(<wp:extent cx="\d+" cy=")%d(")' % old_h,
                      r"\g<1>%d\g<2>" % new_h, head)
        result.append(head)
        result.append(new_group)
        cursor = m.end()
        if log is not None:
            log.append((n, old_h, new_h))
        n += 1
    result.append(xml[cursor:])
    return "".join(result)


# ------------------------------------------------------------------- I/O
def fit_docx(src_path: str, dest_path: str, pad_pt: float, quote_pad_pt: float):
    with tempfile.TemporaryDirectory() as work:
        with zipfile.ZipFile(src_path) as z:
            order = z.namelist()
            z.extractall(work)

        doc_path = os.path.join(work, "word", "document.xml")
        xml = open(doc_path, encoding="utf8").read()
        changes: list = []
        new_xml = fit_document_xml(xml, pad_pt, quote_pad_pt, log=changes)
        open(doc_path, "w", encoding="utf8").write(new_xml)

        if not changes:
            print("No callout-card or pull-quote groups found — nothing to fit.")
        for n, old_h, new_h in changes:
            print(f"  group {n}: {old_h:>7} -> {new_h:>7} EMU  "
                 f"({old_h / EMU_PT:5.1f}pt -> {new_h / EMU_PT:5.1f}pt)")

        if os.path.exists(dest_path):
            os.remove(dest_path)
        with zipfile.ZipFile(dest_path, "w", zipfile.ZIP_DEFLATED) as z:
            for name in order:
                full = os.path.join(work, name)
                if os.path.exists(full):
                    z.write(full, name)
    return len(changes)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fit callout-card and pull-quote shapes to their text content.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("source", help="input .docx")
    parser.add_argument("dest", nargs="?", help="output .docx (omit with --in-place)")
    parser.add_argument("--in-place", action="store_true",
                        help="overwrite the source file — back it up first")
    parser.add_argument("--pad", type=float, default=10.0,
                        help="callout-card vertical padding in points, each side (default: 10)")
    parser.add_argument("--quote-pad", type=float, default=4.0,
                        help="pull-quote vertical padding in points, each side (default: 4)")
    parser.add_argument("--font-dir", help="folder containing the Public Sans TTF faces")
    parser.add_argument("--measure-face", metavar="TTF",
                        help="measure with this font file instead of Public "
                             "Sans, for documents whose script Public Sans "
                             r"cannot draw (e.g. C:\Windows\Fonts\malgun.ttf "
                             "for Korean)")
    parser.add_argument("--line-scale", type=float, default=1.0, metavar="N",
                        help="multiply computed line height by N. Word lays "
                             "CJK lines out taller than the font's own "
                             "ascent+descent, and the shortfall grows with "
                             "the number of lines, so padding cannot absorb "
                             "it. Measured at about 1.15 for Korean in Malgun "
                             "Gothic; leave at 1.0 for Latin documents.")
    args = parser.parse_args()

    if args.in_place == bool(args.dest):
        sys.exit("Pass either a destination path or --in-place, not both or neither.")

    global _font_dir, _measure_face, _line_scale
    _font_dir = find_font_dir(args.font_dir)
    if args.measure_face:
        if not os.path.exists(args.measure_face):
            sys.exit(f"--measure-face does not exist: {args.measure_face}")
        _measure_face = args.measure_face
    if args.line_scale <= 0:
        sys.exit("--line-scale must be positive")
    _line_scale = args.line_scale

    dest = args.source if args.in_place else args.dest
    n = fit_docx(args.source, dest, args.pad, args.quote_pad)
    print(f"\nwrote {dest} ({n} group(s) fitted)")
    print("Run tools/word_preview.ps1 and tools/word_roundtrip_test.ps1 before "
         "treating this as final — a repacked .docx has not been opened by Word yet.")


if __name__ == "__main__":
    main()
