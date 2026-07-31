#!/usr/bin/env python3
"""Extract the readable text of a .docx, including the text inside its shapes.

Why this exists
---------------
Reviewing or rewording a Word deliverable means reading what it actually
says, and in this project a substantial part of that text is not body text
at all: every callout card and pull quote is a Word drawing group (see
CLAUDE.md, "Word document conventions"). Opening the file in Word is how a
person reads it. This is how to get the same words as plain text — for
diffing a revision against the last one, grepping for a phrase, quoting
into a log entry, or handing a section to an AI assistant for a wording
pass.

tools/word_preview.ps1 already puts a document through real Word, but it
produces a PDF to look at, needs Word installed, and spends a Word process
doing it. This reads the file directly and needs nothing but Python. The
two answer different questions: that one asks "does it render correctly",
this one asks "what does it say".

The specific trap it avoids
---------------------------
Word stores every modern drawing shape twice — once as DrawingML under
<mc:Choice>, and again as legacy VML under <mc:Fallback> for readers too
old to understand the first. Both copies carry the same text. Anything
that strips tags naively therefore reports every callout and pull quote
twice, which is actively misleading in the situation this tool exists for:
the document appears to repeat itself, and a reviewer can waste time
"fixing" a duplication that is not in the document. Fallback subtrees are
discarded before any text is collected.

How it works
------------
1. Reads word/document.xml straight out of the .docx, which is a zip.
2. Parses it as XML and drops <mc:Fallback> and <w:del> subtrees, so shape
   text is not duplicated and deleted tracked-changes text is not reported
   as though it were still present.
3. Walks the body in document order: paragraphs become lines, table rows
   become " | "-separated lines, and shape text boxes are emitted where
   they occur, marked and numbered, so it is obvious which text lives in a
   card or quote rather than in the body.

That last point matters beyond readability. Editing text inside a card or
quote changes how much space it needs, and nothing in Word recomputes the
group's height — so a shape whose text you changed needs
tools/fitshapes.py run over the document afterwards. The [shape N] markers
are there so that is visible while reading. They number the text boxes in
this dump only; they are not an index into fitshapes.py's own group
numbering, which counts something different.

What it does not read
---------------------
Headers, footers, footnotes, endnotes and comments live in their own parts
(word/header1.xml and friends) and are not extracted. Neither is anything
that is not text: images, icon wells, shape geometry, colours, sizes,
styling. This gives you the words, not the document.

Requirements
------------
Python 3.9+. Standard library only — no Pillow, no Word, no Inkscape.

Examples
--------
Read a report to the terminal:

    python tools/docx_text.py drafts/UK_AI_Skills_Ambition_Report.docx

Label each paragraph with its Word style, to check the heading structure:

    python tools/docx_text.py exports/Style_Reference_Example.docx --styles

Body text only, and save it for diffing against a later revision:

    python tools/docx_text.py report.docx --no-shapes -o report_body.txt
"""
from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
import zipfile

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
MC = "{http://schemas.openxmlformats.org/markup-compatibility/2006}"

W_P = W + "p"
W_TBL = W + "tbl"
W_TR = W + "tr"
W_TC = W + "tc"
W_T = W + "t"
W_TAB = W + "tab"
W_BR = W + "br"
W_CR = W + "cr"
W_PPR = W + "pPr"
W_PSTYLE = W + "pStyle"
W_VAL = W + "val"
W_DEL = W + "del"
W_SDT = W + "sdt"
W_SDTCONTENT = W + "sdtContent"
W_BODY = W + "body"
W_DRAWING = W + "drawing"
W_PICT = W + "pict"
W_OBJECT = W + "object"
W_TXBXCONTENT = W + "txbxContent"
MC_FALLBACK = MC + "Fallback"
MC_ALTERNATE = MC + "AlternateContent"

# Anything that carries shape content rather than run content. Skipped when
# collecting a paragraph's own text, because shapes are emitted separately.
SHAPE_HOLDERS = (W_DRAWING, W_PICT, W_OBJECT, MC_ALTERNATE)


# --------------------------------------------------------------- XML prep
def prune(root: ET.Element) -> None:
    """Drop <mc:Fallback> and <w:del> subtrees in place.

    Fallback holds a duplicate VML copy of every DrawingML shape's text;
    w:del holds text a tracked change has removed. Both would otherwise be
    reported as present in the document.
    """
    doomed = [(parent, child)
              for parent in root.iter()
              for child in parent
              if child.tag in (MC_FALLBACK, W_DEL)]
    for parent, child in doomed:
        parent.remove(child)


# ------------------------------------------------------------ collection
def para_text(p: ET.Element) -> str:
    """Text of this paragraph's own runs, excluding any shape text inside it."""
    parts: list[str] = []

    def rec(el: ET.Element) -> None:
        for child in el:
            tag = child.tag
            if tag in SHAPE_HOLDERS:
                continue
            if tag == W_T:
                parts.append(child.text or "")
            elif tag == W_TAB:
                parts.append("\t")
            elif tag in (W_BR, W_CR):
                parts.append("\n")
            else:
                rec(child)

    rec(p)
    return "".join(parts)


def para_style(p: ET.Element) -> str | None:
    pr = p.find(W_PPR)
    if pr is None:
        return None
    style = pr.find(W_PSTYLE)
    return None if style is None else style.get(W_VAL)


def shapes_in(p: ET.Element) -> list[ET.Element]:
    """Top-level shape text boxes under this paragraph, in document order.

    Does not descend into a text box it has already found, so a shape
    nested inside another shape's text box is emitted once, by its parent,
    rather than twice.
    """
    found: list[ET.Element] = []

    def rec(el: ET.Element) -> None:
        for child in el:
            if child.tag == W_TXBXCONTENT:
                found.append(child)
            else:
                rec(child)

    rec(p)
    return found


def blocks(container: ET.Element):
    """Yield ('p' | 'tbl', element) for the block-level children of a container."""
    for child in container:
        if child.tag == W_P:
            yield "p", child
        elif child.tag == W_TBL:
            yield "tbl", child
        elif child.tag == W_SDT:
            content = child.find(W_SDTCONTENT)
            if content is not None:
                yield from blocks(content)


# -------------------------------------------------------------- rendering
class Renderer:
    def __init__(self, show_styles: bool, show_shapes: bool):
        self.show_styles = show_styles
        self.show_shapes = show_shapes
        self.lines: list[str] = []
        self.shape_n = 0

    def render(self, container: ET.Element, indent: str = "") -> None:
        for kind, el in blocks(container):
            if kind == "p":
                self.paragraph(el, indent)
            else:
                self.table(el, indent)

    def paragraph(self, p: ET.Element, indent: str) -> None:
        text = para_text(p).strip()
        if text:
            prefix = ""
            if self.show_styles:
                style = para_style(p)
                prefix = f"[{style}] " if style else ""
            self.lines.append(indent + prefix + text)
        self.emit_shapes(p, indent)

    def table(self, tbl: ET.Element, indent: str) -> None:
        deferred: list[ET.Element] = []
        for tr in tbl.findall(W_TR):
            cells = [self.cell_text(tc, deferred) for tc in tr.findall(W_TC)]
            self.lines.append(indent + " | ".join(cells))
        for p in deferred:
            self.emit_shapes(p, indent)

    def cell_text(self, tc: ET.Element, deferred: list[ET.Element]) -> str:
        """Flatten a cell to one string; queue any shapes for after the table."""
        bits: list[str] = []
        for kind, el in blocks(tc):
            if kind == "p":
                text = para_text(el).strip()
                if text:
                    bits.append(text)
                if shapes_in(el):
                    deferred.append(el)
            else:
                nested = [self.cell_text(c, deferred)
                          for tr in el.findall(W_TR) for c in tr.findall(W_TC)]
                bits.extend(b for b in nested if b)
        return " / ".join(bits)

    def emit_shapes(self, p: ET.Element, indent: str) -> None:
        for box in shapes_in(p):
            self.shape_n += 1
            n = self.shape_n
            if not self.show_shapes:
                continue
            self.lines.append("")
            self.lines.append(f"{indent}[shape {n}]")
            self.render(box, indent)
            self.lines.append(f"{indent}[/shape {n}]")
            self.lines.append("")


def extract(path: str, show_styles: bool, show_shapes: bool) -> str:
    try:
        with zipfile.ZipFile(path) as z:
            try:
                raw = z.read("word/document.xml")
            except KeyError:
                sys.exit(f"{path} is a zip, but has no word/document.xml — "
                         "is it really a .docx?")
    except FileNotFoundError:
        sys.exit(f"No such file: {path}")
    except zipfile.BadZipFile:
        sys.exit(f"{path} is not a .docx. A .docx is a zip archive; this file "
                 "is not one. Legacy .doc files need converting first.")

    root = ET.fromstring(raw)
    prune(root)

    body = root.find(W_BODY)
    if body is None:
        sys.exit("document.xml has no <w:body> — the file looks malformed.")

    renderer = Renderer(show_styles, show_shapes)
    renderer.render(body)

    text = "\n".join(renderer.lines)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract the readable text of a .docx, shape text included.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("source", help="input .docx")
    parser.add_argument("-o", "--out", help="write to this file instead of stdout")
    parser.add_argument("--styles", action="store_true",
                        help="prefix each paragraph with its Word style name")
    parser.add_argument("--no-shapes", action="store_true",
                        help="body text only — skip callout cards and pull quotes")
    args = parser.parse_args()

    text = extract(args.source, args.styles, not args.no_shapes)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"wrote {args.out}")
    else:
        # Word text is full of curly quotes, em-dashes and £; a Windows
        # console defaulting to cp1252 would fail on all three.
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
