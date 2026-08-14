#!/usr/bin/env python3
"""Convert a Markdown file into a .docx carrying this project's house style.

Why this exists
---------------
The repo's durable content is Markdown, and Markdown read in a code editor
is functional rather than pleasant. Long procedural documents in
particular — a build guide followed step by step, away from the machine
that renders it — are easier to work from as a formatted document with
real headings, tables, shaded code blocks and figures.

The alternative was hand-building each document's word/document.xml, which
is how every earlier Word deliverable here was made. That is fine for a
six-page style catalogue built once; it is not fine for a document that
tracks a Markdown source and gets regenerated every time the source
changes.

Where the style comes from
--------------------------
Nowhere in this file. styles.xml, numbering.xml and settings.xml are
lifted wholesale from a template .docx — by default
exports/Style_Reference_Example.docx, which CLAUDE.md records as canonical.
So the named styles (Title/Subtitle/Heading1-3/Normal/Caption/Quote/
Eyebrow, all Public Sans, all with real outline levels), the bullet and
number definitions, and the compatibilityMode 15 declaration that shape
groups depend on, all arrive already correct and stay correct if the
reference is ever revised. This tool contributes no formatting opinions of
its own beyond the block-level mapping below.

That inheritance is the point. A converter that hard-coded a second copy
of the house style would drift from the reference the moment either
changed, and the drift would be invisible until someone put two documents
side by side.

What it maps
------------
    # / ## / ### / ####    Title / Heading1 / Heading2 / Heading3
    *italic line* directly under the # title    the Subtitle style
    paragraph              Normal, with **bold**, *italic*, `code` runs
    - item / 1. item       bulleted and numbered lists (house numbering).
                           Each numbered list restarts at 1, and a fenced
                           block indented under an item is emitted as a code
                           block with the list resuming after it.
    | a | b |              table with Ink header row and Paper/Mist banding
    ```fenced```           shaded single-cell table, Consolas, no wrapping
    > **NOTE** — text      callout card (NOTE/TIP/WARNING/CHECK)
    > text                 Quote style
    ![caption](path.png)   inline figure sized to the text column, plus a
                           Caption paragraph carrying the alt text
    ---                    a thin Sage rule

Blank lines between list items are the repo's own Markdown convention, so
a list is held open across them; a blank line only ends a list when the
next non-blank line is not itself an item or an indented continuation.

Callout cards are emitted at a fixed height, which is wrong for any card
whose text does not happen to fill it — see the height rule in CLAUDE.md.
Run tools/fitshapes.py over the output afterwards, then both Word checks,
exactly as for any other construction step.

Requirements
------------
Python with Pillow, and only for figures — Pillow is used to read a PNG's
pixel dimensions so the image can be scaled to the text column. A document
with no images needs nothing but the standard library. No Word process is
involved; this writes the file directly.

Usage
-----
    python tools/md_to_docx.py drafts/guide.md -o exports/Guide.docx
    python tools/md_to_docx.py guide.md -o Guide.docx --footer "Build guide"
    python tools/md_to_docx.py guide.md -o Guide.docx --highlight "[UNVERIFIED]"

Command-line only, per project_log.md Entry 049: Claude or a build step
runs this, not a person at a window.
"""

import argparse
import os
import re
import shutil
import sys
import zipfile

# ---------------------------------------------------------------------------
# Palette (project_brief.md, "Visual identity")
# ---------------------------------------------------------------------------
INK = "27221E"
EMBER = "F15E4B"
SAND = "F9E8DC"
PAPER = "F9F9F9"
MIST = "EFEEED"
SAGE = "D5E2E1"
STONE = "6E6E6E"
GRAPHITE = "404040"

# Page geometry, matching the style reference: A4 with 1080-twip margins.
CONTENT_TWIPS = 9746
EMU_PER_TWIP = 635  # 914400 EMU per inch / 1440 twips per inch

# Callout card semantics: label colour, card fill, icon file in the template.
CALLOUTS = {
    "NOTE": (STONE, SAGE, "information_128.png"),
    "TIP": (EMBER, SAND, "tip_128.png"),
    "WARNING": (EMBER, SAND, "warning_128.png"),
    "CHECK": (STONE, MIST, "verification_128.png"),
}

MONO = "Consolas"


def esc(text):
    """Escape text for XML content, and normalise the dashes we care about."""
    out = (text.replace("&", "&amp;")
               .replace("<", "&lt;")
               .replace(">", "&gt;"))
    return "".join(c if ord(c) < 128 else "&#%d;" % ord(c) for c in out)


# ---------------------------------------------------------------------------
# Inline formatting
# ---------------------------------------------------------------------------
INLINE_RE = re.compile(r"(\*\*.+?\*\*|(?<!\*)\*(?!\*).+?(?<!\*)\*(?!\*)|`[^`]+`)")
CODE_RE = re.compile(r"(`[^`]+`)")


def runs(text, base_size=21, colour=INK, highlight=None):
    """Turn a line of Markdown inline markup into a list of <w:r> strings."""
    out = []
    for piece in INLINE_RE.split(text):
        if not piece:
            continue
        bold = italic = False
        if piece.startswith("**") and piece.endswith("**") and len(piece) > 4:
            body, bold = piece[2:-2], True
        elif piece.startswith("`") and piece.endswith("`") and len(piece) > 2:
            _emit(piece[1:-1], False, False, True, colour, base_size,
                  highlight, out)
            continue
        elif piece.startswith("*") and piece.endswith("*") and len(piece) > 2:
            body, italic = piece[1:-1], True
        else:
            body = piece
        # Code spans nest inside bold and italic — "**run `sudo apt` first**"
        # is ordinary Markdown, and splitting only on the outer markup leaves
        # the backticks to render as literal characters.
        for seg in CODE_RE.split(body):
            if not seg:
                continue
            if seg.startswith("`") and seg.endswith("`") and len(seg) > 2:
                _emit(seg[1:-1], bold, italic, True, colour, base_size,
                      highlight, out)
            else:
                _emit(seg, bold, italic, False, colour, base_size,
                      highlight, out)
    return out


def _emit(body, bold, italic, mono, colour, size, highlight, out):
    """Append runs for one already-unwrapped fragment, splitting on the
    highlight token, which is coloured wherever it appears."""
    if highlight and highlight in body:
        for frag in re.split("(" + re.escape(highlight) + ")", body):
            if not frag:
                continue
            is_hl = frag == highlight
            out.append(_run(frag, bold or is_hl, italic, mono,
                            EMBER if is_hl else colour, size))
        return
    out.append(_run(body, bold, italic, mono, colour, size))


def _run(text, bold, italic, mono, colour, size):
    font = MONO if mono else "Public Sans"
    size = size - 2 if mono else size
    rpr = ['<w:rFonts w:ascii="%s" w:hAnsi="%s" w:cs="%s"/>' % (font, font, font)]
    if bold:
        rpr.append("<w:b/><w:bCs/>")
    if italic:
        rpr.append("<w:i/><w:iCs/>")
    if mono:
        rpr.append('<w:shd w:val="clear" w:color="auto" w:fill="%s"/>' % MIST)
    rpr.append('<w:color w:val="%s"/>' % colour)
    rpr.append('<w:sz w:val="%d"/><w:szCs w:val="%d"/>' % (size, size))
    return ('<w:r><w:rPr>%s</w:rPr><w:t xml:space="preserve">%s</w:t></w:r>'
            % ("".join(rpr), esc(text)))


# ---------------------------------------------------------------------------
# Block parser
# ---------------------------------------------------------------------------
def parse(md):
    """Parse Markdown text into a flat list of (kind, payload) blocks."""
    lines = md.replace("\r\n", "\n").split("\n")
    blocks, i, n = [], 0, len(lines)
    # Set when a numbered list is interrupted by a fenced block and resumes
    # after it, so the resumed part keeps counting instead of restarting.
    list_continues = False

    def is_item(s):
        return bool(re.match(r"^\s*(?:[-*]\s+|\d+\.\s+)", s))

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # Fenced code
        if stripped.startswith("```"):
            lang = stripped[3:].strip()
            i += 1
            body = []
            while i < n and not lines[i].strip().startswith("```"):
                body.append(lines[i])
                i += 1
            i += 1
            blocks.append(("code", (lang, body)))
            continue

        # Horizontal rule
        if re.fullmatch(r"-{3,}|\*{3,}|_{3,}", stripped):
            blocks.append(("rule", None))
            i += 1
            continue

        # Heading
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            blocks.append(("h%d" % len(m.group(1)), m.group(2).strip()))
            i += 1
            continue

        # Standalone image
        m = re.fullmatch(r"!\[(.*?)\]\((.+?)\)", stripped)
        if m:
            blocks.append(("image", (m.group(2).strip(), m.group(1).strip())))
            i += 1
            continue

        # Table
        if stripped.startswith("|") and i + 1 < n and \
                re.fullmatch(r"\|[\s:\-|]+\|", lines[i + 1].strip()):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(cells)
                i += 1
            del rows[1]  # the |---|---| separator
            blocks.append(("table", rows))
            continue

        # Blockquote
        if stripped.startswith(">"):
            body = []
            while i < n and lines[i].strip().startswith(">"):
                body.append(lines[i].strip().lstrip(">").strip())
                i += 1
            text = " ".join(x for x in body if x)
            m = re.match(r"^\*\*(NOTE|TIP|WARNING|CHECK)\*\*\s*[—:-]?\s*(.*)$",
                         text)
            if m:
                blocks.append(("callout", (m.group(1), m.group(2))))
            else:
                blocks.append(("quote", text))
            continue

        # List — held open across the blank lines the repo's style mandates
        if is_item(stripped):
            items, ordered = [], bool(re.match(r"^\s*\d+\.\s", stripped))
            continues, split = list_continues, False
            list_continues = False
            while i < n:
                cur = lines[i]
                if cur.strip().startswith("```") and items:
                    # A fenced block indented under a list item. Without this
                    # the indented-continuation branch below swallows it as
                    # prose and the block's line breaks are lost — which turns
                    # a fixed test input into one run-on line. Emit the list so
                    # far, then the block; if items resume after it they carry
                    # on counting rather than restarting at 1.
                    lang = cur.strip()[3:].strip()
                    i += 1
                    fenced = []
                    while i < n and not lines[i].strip().startswith("```"):
                        fenced.append(lines[i])
                        i += 1
                    i += 1
                    pad = min((len(x) - len(x.lstrip())
                               for x in fenced if x.strip()), default=0)
                    fenced = [x[pad:] if x.strip() else "" for x in fenced]
                    j = i
                    while j < n and not lines[j].strip():
                        j += 1
                    resumes = j < n and is_item(lines[j].strip())
                    blocks.append(("list", (ordered, items, continues)))
                    blocks.append(("code", (lang, fenced)))
                    list_continues = ordered and resumes
                    split = True
                    break
                if is_item(cur.strip()):
                    items.append(re.sub(r"^\s*(?:[-*]\s+|\d+\.\s+)", "",
                                        cur.strip()))
                    i += 1
                elif not cur.strip():
                    # Look ahead: only a further item or an indented
                    # continuation keeps the list alive.
                    j = i + 1
                    while j < n and not lines[j].strip():
                        j += 1
                    if j < n and (is_item(lines[j].strip())
                                  or lines[j].startswith(("  ", "\t"))):
                        i = j
                    else:
                        i = j
                        break
                elif cur.startswith(("  ", "\t")) and items:
                    items[-1] += " " + cur.strip()
                    i += 1
                else:
                    break
            if not split:
                blocks.append(("list", (ordered, items, continues)))
            continue

        # Paragraph
        body = []
        while i < n and lines[i].strip() and not is_item(lines[i].strip()) \
                and not lines[i].strip().startswith(("#", ">", "|", "```")) \
                and not re.fullmatch(r"-{3,}", lines[i].strip()):
            body.append(lines[i].strip())
            i += 1
        if body:
            blocks.append(("para", " ".join(body)))
        else:
            i += 1
    return blocks


# ---------------------------------------------------------------------------
# Block renderers
# ---------------------------------------------------------------------------
def p_heading(style, text, page_break, highlight):
    ppr = '<w:pStyle w:val="%s"/>' % style
    if page_break:
        ppr += "<w:pageBreakBefore/>"
    inner = "".join(runs(text, size_for(style), colour_for(style),
                         highlight=highlight))
    # Heading styles carry their own font/size/colour; strip our run props so
    # the named style is what actually decides, per the direct-formatting rule.
    inner = re.sub(r"<w:rPr>.*?</w:rPr>", "", inner) if style != "Normal" \
        else inner
    return "<w:p><w:pPr>%s</w:pPr>%s</w:p>" % (ppr, inner)


def size_for(style):
    return {"Title": 56, "Heading1": 26, "Heading2": 24, "Heading3": 22}.get(
        style, 21)


def colour_for(style):
    return GRAPHITE if style == "Heading3" else INK


def p_para(text, highlight):
    return "<w:p>%s</w:p>" % "".join(runs(text, highlight=highlight))


ORDERED_NUM_BASE = 100


def numbering_with_restarts(xml, num_ids):
    """Give every numbered list its own numbering instance, restarting at 1.

    The template defines numId 2 for numbered lists. Pointing every list in a
    document at that single instance makes Word continue one sequence across
    the whole file, so a document's second numbered list starts at 7 rather
    than 1. That defect passed the fitter, the render check and the
    round-trip check, and was caught only by reading a rendered page — see
    project_log.md Entry 084.

    The abstract definition is untouched, so the house numbering format still
    comes from the template and nowhere else. This adds *instances* of it,
    each carrying a startOverride, which is exactly what Word writes when a
    person restarts a list by hand.
    """
    if not num_ids:
        return xml
    m = re.search(r'<w:num\b[^>]*w:numId="2"[^>]*>\s*'
                  r'<w:abstractNumId\s+w:val="(\d+)"\s*/>', xml)
    if not m:
        sys.exit("template numbering.xml has no numId 2 for numbered lists")
    abstract = m.group(1)
    added = "".join(
        '<w:num w:numId="%d"><w:abstractNumId w:val="%s"/>'
        '<w:lvlOverride w:ilvl="0"><w:startOverride w:val="1"/>'
        "</w:lvlOverride></w:num>" % (nid, abstract)
        for nid in num_ids)
    if "</w:numbering>" not in xml:
        sys.exit("template numbering.xml has no closing element")
    return xml.replace("</w:numbering>", added + "</w:numbering>")


def p_list(ordered, items, highlight, num_id):
    out = []
    for it in items:
        # The hanging indent has to clear the widest marker the list will
        # produce. 240 twips fits "9." and collides with "14.", which only
        # showed up on a rendered page — a list has to reach ten items before
        # the defect exists at all.
        ppr = ('<w:pPr><w:numPr><w:ilvl w:val="0"/>'
               '<w:numId w:val="%d"/></w:numPr>'
               '<w:spacing w:after="120"/><w:ind w:left="480" w:hanging="300"/>'
               "</w:pPr>" % num_id)
        out.append("<w:p>%s%s</w:p>" % (ppr, "".join(runs(it,
                                                          highlight=highlight))))
    return "".join(out)


def p_rule():
    return ('<w:p><w:pPr><w:pBdr><w:bottom w:val="single" w:sz="6" '
            'w:space="4" w:color="%s"/></w:pBdr>'
            '<w:spacing w:before="80" w:after="160"/></w:pPr></w:p>' % SAGE)


def p_quote(text, highlight):
    return ('<w:p><w:pPr><w:pStyle w:val="Quote"/>'
            '<w:ind w:left="360"/></w:pPr>%s</w:p>'
            % "".join(runs(text, 24, INK, highlight=highlight)))


def p_code(lines):
    """A shaded single-cell table. Tables clip rather than reflow, which is
    what code wants — a wrapped command is a wrong command."""
    body = []
    for ln in lines:
        body.append(
            '<w:p><w:pPr><w:spacing w:after="0" w:line="240" '
            'w:lineRule="auto"/></w:pPr>'
            '<w:r><w:rPr><w:rFonts w:ascii="%s" w:hAnsi="%s" w:cs="%s"/>'
            '<w:color w:val="%s"/><w:sz w:val="17"/><w:szCs w:val="17"/>'
            '</w:rPr><w:t xml:space="preserve">%s</w:t></w:r></w:p>'
            % (MONO, MONO, MONO, INK, esc(ln) or ""))
    if not body:
        body.append('<w:p><w:pPr><w:spacing w:after="0"/></w:pPr></w:p>')
    return (
        '<w:tbl><w:tblPr><w:tblW w:w="%d" w:type="dxa"/>'
        '<w:tblLayout w:type="fixed"/>'
        '<w:tblLook w:val="0000" w:firstRow="0" w:lastRow="0" '
        'w:firstColumn="0" w:lastColumn="0" w:noHBand="0" w:noVBand="0"/>'
        '</w:tblPr><w:tblGrid><w:gridCol w:w="%d"/></w:tblGrid>'
        '<w:tr><w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/>'
        '<w:tcBorders><w:top w:val="single" w:sz="4" w:color="%s"/>'
        '<w:left w:val="single" w:sz="18" w:color="%s"/>'
        '<w:bottom w:val="single" w:sz="4" w:color="%s"/>'
        '<w:right w:val="single" w:sz="4" w:color="%s"/></w:tcBorders>'
        '<w:shd w:val="clear" w:color="auto" w:fill="%s"/>'
        '<w:tcMar><w:top w:w="120" w:type="dxa"/><w:left w:w="160" '
        'w:type="dxa"/><w:bottom w:w="120" w:type="dxa"/>'
        '<w:right w:w="120" w:type="dxa"/></w:tcMar></w:tcPr>%s</w:tc></w:tr>'
        '</w:tbl><w:p><w:pPr><w:spacing w:after="80"/></w:pPr></w:p>'
        % (CONTENT_TWIPS, CONTENT_TWIPS, CONTENT_TWIPS,
           SAGE, EMBER, SAGE, SAGE, MIST, "".join(body)))


def p_table(rows, highlight):
    cols = max(len(r) for r in rows)
    widths = column_widths(rows, cols)

    out = ['<w:tbl><w:tblPr><w:tblW w:w="%d" w:type="dxa"/>'
           '<w:tblLayout w:type="fixed"/>'
           '<w:tblLook w:val="0000" w:firstRow="0" w:lastRow="0" '
           'w:firstColumn="0" w:lastColumn="0" w:noHBand="0" w:noVBand="0"/>'
           '</w:tblPr><w:tblGrid>%s</w:tblGrid>'
           % (CONTENT_TWIPS,
              "".join('<w:gridCol w:w="%d"/>' % x for x in widths))]

    for r_i, row in enumerate(rows):
        header = r_i == 0
        fill = INK if header else (PAPER if r_i % 2 else MIST)
        tr = ['<w:tr>']
        if header:
            tr.append('<w:trPr><w:tblHeader/></w:trPr>')
        for c_i in range(cols):
            cell = row[c_i] if c_i < len(row) else ""
            colour = PAPER if header else INK
            content = runs(cell, 20, colour, highlight=highlight)
            if header:
                content = [x.replace("<w:rPr>", "<w:rPr><w:b/><w:bCs/>")
                           for x in content]
            tr.append(
                '<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/>'
                '<w:tcBorders><w:top w:val="single" w:sz="4" w:color="%s"/>'
                '<w:left w:val="single" w:sz="4" w:color="%s"/>'
                '<w:bottom w:val="single" w:sz="4" w:color="%s"/>'
                '<w:right w:val="single" w:sz="4" w:color="%s"/></w:tcBorders>'
                '<w:shd w:val="clear" w:color="auto" w:fill="%s"/>'
                '<w:tcMar><w:top w:w="120" w:type="dxa"/>'
                '<w:left w:w="160" w:type="dxa"/>'
                '<w:bottom w:w="120" w:type="dxa"/>'
                '<w:right w:w="160" w:type="dxa"/></w:tcMar>'
                '<w:vAlign w:val="center"/></w:tcPr>'
                '<w:p><w:pPr><w:spacing w:after="0"/></w:pPr>%s</w:p></w:tc>'
                % (widths[c_i], SAGE, SAGE, SAGE, SAGE, fill,
                   "".join(content) or ""))
        tr.append("</w:tr>")
        out.append("".join(tr))
    out.append('</w:tbl><w:p><w:pPr><w:spacing w:after="80"/></w:pPr></w:p>')
    return "".join(out)


MARKUP_RE = re.compile(r"\*\*|`|(?<!\*)\*(?!\*)")
MIN_COL_TWIPS = 900


def column_widths(rows, cols):
    """Size columns to the content, not evenly.

    An even split is wrong for the tables this project actually writes: a
    column holding "d", "rwx", "r-x" gets the same room as one holding a
    paragraph, which leaves half the table empty and forces the prose into
    a narrow ribbon. Weighting by the longest cell — damped, so one very
    long cell cannot swallow the table — tracks what a person would do by
    hand.
    """
    weights = []
    for c in range(cols):
        longest = 0
        for r_i, row in enumerate(rows):
            cell = row[c] if c < len(row) else ""
            plain = MARKUP_RE.sub("", cell)
            # Headers are short by nature and shouldn't drive the width, but
            # a column must still fit its own heading.
            longest = max(longest, len(plain) if r_i else min(len(plain), 14))
        # Damping: width should grow with content, but sub-linearly, or a
        # 300-character cell would take the whole table.
        weights.append(max(4.5, longest ** 0.62))

    # A column has to fit its longest unbreakable word. Weighting alone gave a
    # narrow first column the word "Motherboard" and Word broke it mid-word
    # ("Moth / erboa / rd"). Estimated rather than measured: this tool takes no
    # font dependency by design, so the estimate must run generous — the first
    # constant tried (100 twips/char + 260) was still ~150 twips short for
    # "Motherboard" at body size and the break survived a render check that
    # was read too quickly. 122/char + 340 clears it with margin to spare;
    # erring wide costs a little space, erring narrow costs legibility.
    floors = []
    for c in range(cols):
        longest_word = 0
        for row in rows:
            cell = row[c] if c < len(row) else ""
            for word in MARKUP_RE.sub("", cell).split():
                longest_word = max(longest_word, len(word))
        floors.append(min(CONTENT_TWIPS // 2,
                          max(MIN_COL_TWIPS, longest_word * 122 + 340)))

    total = sum(weights)
    widths = [max(floors[i], int(CONTENT_TWIPS * w / total))
              for i, w in enumerate(weights)]

    # Re-normalise: the floors may have pushed the total over. Take the excess
    # from whichever column has the most room above its own floor.
    over = sum(widths) - CONTENT_TWIPS
    while over > 0:
        slack = [w - floors[k] for k, w in enumerate(widths)]
        biggest = slack.index(max(slack))
        take = min(over, slack[biggest])
        if take <= 0:
            break
        widths[biggest] -= take
        over -= take
    widths[-1] += CONTENT_TWIPS - sum(widths)
    return widths


def p_image(rid, cx, cy, doc_id, name):
    return (
        '<w:p><w:pPr><w:jc w:val="center"/>'
        '<w:spacing w:before="80" w:after="60"/></w:pPr>'
        '<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
        '<wp:extent cx="%d" cy="%d"/><wp:effectExtent l="0" t="0" r="0" b="0"/>'
        '<wp:docPr id="%d" name="%s"/><wp:cNvGraphicFramePr>'
        '<a:graphicFrameLocks noChangeAspect="1"/></wp:cNvGraphicFramePr>'
        '<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/'
        'drawingml/2006/picture"><pic:pic><pic:nvPicPr>'
        '<pic:cNvPr id="%d" name="%s"/><pic:cNvPicPr/></pic:nvPicPr>'
        '<pic:blipFill><a:blip r:embed="%s"/><a:stretch><a:fillRect/>'
        '</a:stretch></pic:blipFill><pic:spPr><a:xfrm><a:off x="0" y="0"/>'
        '<a:ext cx="%d" cy="%d"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/>'
        '</a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic>'
        '</wp:inline></w:drawing></w:r></w:p>'
        % (cx, cy, doc_id, esc(name), doc_id, esc(name), rid, cx, cy))


def p_caption(text, highlight):
    return ('<w:p><w:pPr><w:pStyle w:val="Caption"/>'
            '<w:jc w:val="center"/></w:pPr>%s</w:p>'
            % "".join(re.sub(r"<w:rPr>.*?</w:rPr>", "", x)
                      for x in runs(text, 17, STONE, highlight=highlight)))


def p_callout(kind, text, rid, doc_id, highlight):
    """A callout card, built as a Word group of sibling shapes.

    Height is fixed here and will be wrong for most text — fitshapes.py is
    what makes it right. See CLAUDE.md, "Card and quote height must fit the
    text inside".
    """
    label_col, fill, _ = CALLOUTS[kind]
    cx = CONTENT_TWIPS * EMU_PER_TWIP
    # Rough starting height: two lines plus padding, then one line per ~95
    # characters of body text. fitshapes.py corrects it.
    lines = max(2, 1 + len(text) // 95)
    cy = 480000 + lines * 190000
    icon_box = min(828000, cy - 254000)
    icon = int(icon_box * 0.78)
    pad = (cy - icon_box) // 2
    text_x = 1281600
    body = "".join(runs(text, 19, INK, highlight=highlight))
    return (
        '<w:p><w:pPr><w:spacing w:before="120" w:after="160"/></w:pPr>'
        '<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
        '<wp:extent cx="%d" cy="%d"/><wp:effectExtent l="0" t="0" r="0" b="0"/>'
        '<wp:docPr id="%d" name="Callout %s"/><wp:cNvGraphicFramePr/>'
        '<a:graphic><a:graphicData uri="http://schemas.microsoft.com/office/'
        'word/2010/wordprocessingGroup"><wpg:wgp><wpg:cNvGrpSpPr/>'
        '<wpg:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="%d" cy="%d"/>'
        '<a:chOff x="0" y="0"/><a:chExt cx="%d" cy="%d"/></a:xfrm>'
        '</wpg:grpSpPr>'
        # card
        '<wps:wsp><wps:cNvSpPr/><wps:spPr><a:xfrm><a:off x="0" y="0"/>'
        '<a:ext cx="%d" cy="%d"/></a:xfrm><a:prstGeom prst="roundRect">'
        '<a:avLst><a:gd name="adj" fmla="val 8000"/></a:avLst></a:prstGeom>'
        '<a:solidFill><a:srgbClr val="%s"/></a:solidFill>'
        '<a:ln w="9525"><a:solidFill><a:srgbClr val="%s"/></a:solidFill>'
        '</a:ln></wps:spPr><wps:bodyPr/></wps:wsp>'
        # icon well
        '<wps:wsp><wps:cNvSpPr/><wps:spPr><a:xfrm><a:off x="108000" y="%d"/>'
        '<a:ext cx="%d" cy="%d"/></a:xfrm><a:prstGeom prst="roundRect">'
        '<a:avLst><a:gd name="adj" fmla="val 20000"/></a:avLst></a:prstGeom>'
        '<a:solidFill><a:srgbClr val="%s"/></a:solidFill><a:ln><a:noFill/>'
        '</a:ln></wps:spPr><wps:bodyPr/></wps:wsp>'
        # icon
        '<pic:pic><pic:nvPicPr><pic:cNvPr id="%d" name="%s icon"/>'
        '<pic:cNvPicPr/></pic:nvPicPr><pic:blipFill><a:blip r:embed="%s"/>'
        '<a:stretch><a:fillRect/></a:stretch></pic:blipFill><pic:spPr>'
        '<a:xfrm><a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"/></a:xfrm>'
        '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
        # divider bar
        '<wps:wsp><wps:cNvSpPr/><wps:spPr><a:xfrm><a:off x="1080000" y="%d"/>'
        '<a:ext cx="57600" cy="%d"/></a:xfrm><a:prstGeom prst="roundRect">'
        '<a:avLst><a:gd name="adj" fmla="val 50000"/></a:avLst></a:prstGeom>'
        '<a:solidFill><a:srgbClr val="%s"/></a:solidFill><a:ln><a:noFill/>'
        '</a:ln></wps:spPr><wps:bodyPr/></wps:wsp>'
        # text box
        '<wps:wsp><wps:cNvSpPr/><wps:spPr><a:xfrm><a:off x="%d" y="%d"/>'
        '<a:ext cx="%d" cy="%d"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/>'
        '</a:prstGeom><a:noFill/><a:ln><a:noFill/></a:ln></wps:spPr>'
        '<wps:txbx><w:txbxContent>'
        '<w:p><w:pPr><w:spacing w:after="40"/></w:pPr><w:r><w:rPr>'
        '<w:rFonts w:ascii="Public Sans" w:hAnsi="Public Sans" '
        'w:cs="Public Sans"/><w:b/><w:bCs/><w:color w:val="%s"/>'
        '<w:sz w:val="19"/><w:szCs w:val="19"/></w:rPr>'
        '<w:t xml:space="preserve">%s</w:t></w:r></w:p>'
        '<w:p><w:pPr><w:spacing w:after="0"/></w:pPr>%s</w:p>'
        '</w:txbxContent></wps:txbx>'
        '<wps:bodyPr rot="0" anchor="t" lIns="0" tIns="0" rIns="0" bIns="0"/>'
        '</wps:wsp></wpg:wgp></a:graphicData></a:graphic></wp:inline>'
        '</w:drawing></w:r></w:p>'
        % (cx, cy, doc_id, kind, cx, cy, cx, cy, cx, cy, fill, STONE,
           pad, icon_box, icon_box, PAPER,
           doc_id + 1, kind, rid,
           108000 + (icon_box - icon) // 2, pad + (icon_box - icon) // 2,
           icon, icon,
           pad, icon_box, label_col,
           text_x, pad, cx - text_x - 108000, icon_box,
           label_col, kind, body))


# ---------------------------------------------------------------------------
# Document assembly
# ---------------------------------------------------------------------------
DOC_OPEN = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/'
    '2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/'
    '2006/relationships" xmlns:wp="http://schemas.openxmlformats.org/'
    'drawingml/2006/wordprocessingDrawing" xmlns:a="http://schemas.'
    'openxmlformats.org/drawingml/2006/main" xmlns:pic="http://schemas.'
    'openxmlformats.org/drawingml/2006/picture" xmlns:wps="http://schemas.'
    'microsoft.com/office/word/2010/wordprocessingShape" xmlns:wpg="http://'
    'schemas.microsoft.com/office/word/2010/wordprocessingGroup"><w:body>')

SECT_PR = ('<w:sectPr><w:footerReference w:type="default" r:id="rIdFooter"/>'
           '<w:pgSz w:w="11906" w:h="16838"/>'
           '<w:pgMar w:top="1080" w:right="1080" w:bottom="1080" w:left="1080" '
           'w:header="708" w:footer="720" w:gutter="0"/></w:sectPr>')


def title_block(rid, eyebrow, strapline):
    return (
        '<w:tbl><w:tblPr><w:tblW w:w="%d" w:type="dxa"/>'
        '<w:tblLayout w:type="fixed"/>'
        '<w:tblLook w:val="0000" w:firstRow="0" w:lastRow="0" '
        'w:firstColumn="0" w:lastColumn="0" w:noHBand="0" w:noVBand="0"/>'
        '</w:tblPr><w:tblGrid><w:gridCol w:w="4200"/><w:gridCol w:w="5546"/>'
        '</w:tblGrid><w:tr>'
        '<w:tc><w:tcPr><w:tcW w:w="4200" w:type="dxa"/><w:tcBorders>'
        '<w:top w:val="nil"/><w:left w:val="nil"/>'
        '<w:bottom w:val="single" w:sz="16" w:color="%s"/>'
        '<w:right w:val="nil"/></w:tcBorders><w:tcMar>'
        '<w:top w:w="60" w:type="dxa"/><w:left w:w="0" w:type="dxa"/>'
        '<w:bottom w:w="160" w:type="dxa"/><w:right w:w="120" w:type="dxa"/>'
        '</w:tcMar><w:vAlign w:val="center"/></w:tcPr>'
        '<w:p><w:pPr><w:jc w:val="left"/></w:pPr><w:r><w:drawing>'
        '<wp:inline distT="0" distB="0" distL="0" distR="0">'
        '<wp:extent cx="2148840" cy="768042"/>'
        '<wp:effectExtent l="0" t="0" r="0" b="0"/>'
        '<wp:docPr id="1001" name="Grounded AI Practice logo"/>'
        '<wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect="1"/>'
        '</wp:cNvGraphicFramePr><a:graphic><a:graphicData uri="http://schemas.'
        'openxmlformats.org/drawingml/2006/picture"><pic:pic><pic:nvPicPr>'
        '<pic:cNvPr id="1001" name="Grounded AI Practice logo"/>'
        '<pic:cNvPicPr/></pic:nvPicPr><pic:blipFill><a:blip r:embed="%s"/>'
        '<a:stretch><a:fillRect/></a:stretch></pic:blipFill><pic:spPr>'
        '<a:xfrm><a:off x="0" y="0"/><a:ext cx="2148840" cy="768042"/></a:xfrm>'
        '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
        '</a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>'
        '</w:tc>'
        '<w:tc><w:tcPr><w:tcW w:w="5546" w:type="dxa"/><w:tcBorders>'
        '<w:top w:val="nil"/><w:left w:val="nil"/>'
        '<w:bottom w:val="single" w:sz="16" w:color="%s"/>'
        '<w:right w:val="nil"/></w:tcBorders><w:tcMar>'
        '<w:top w:w="60" w:type="dxa"/><w:left w:w="120" w:type="dxa"/>'
        '<w:bottom w:w="160" w:type="dxa"/><w:right w:w="0" w:type="dxa"/>'
        '</w:tcMar><w:vAlign w:val="center"/></w:tcPr>'
        '<w:p><w:pPr><w:pStyle w:val="Eyebrow"/><w:jc w:val="right"/></w:pPr>'
        '<w:r><w:t xml:space="preserve">%s</w:t></w:r></w:p>'
        '<w:p><w:pPr><w:spacing w:after="0"/><w:jc w:val="right"/></w:pPr>'
        '<w:r><w:rPr><w:rFonts w:ascii="Public Sans" w:hAnsi="Public Sans" '
        'w:cs="Public Sans"/><w:i/><w:iCs/><w:color w:val="%s"/>'
        '<w:sz w:val="16"/><w:szCs w:val="16"/></w:rPr>'
        '<w:t xml:space="preserve">%s</w:t></w:r></w:p></w:tc></w:tr></w:tbl>'
        '<w:p><w:pPr><w:spacing w:after="120"/></w:pPr></w:p>'
        % (CONTENT_TWIPS, EMBER, rid, EMBER, esc(eyebrow), INK,
           esc(strapline)))


def build(md_path, out_path, template, footer_text, eyebrow, strapline,
          highlight, break_before_h1):
    with open(md_path, encoding="utf-8") as fh:
        blocks = parse(fh.read())

    base = os.path.dirname(os.path.abspath(md_path))
    tpl = zipfile.ZipFile(template)
    tpl_names = set(tpl.namelist())

    media = {}           # archive name -> bytes
    rels = []            # (rId, target)
    next_rid = [10]

    def add_media(src_name, data):
        for rid, target in rels:
            if target == "media/" + src_name:
                return rid
        rid = "rId%d" % next_rid[0]
        next_rid[0] += 1
        media["word/media/" + src_name] = data
        rels.append((rid, "media/" + src_name))
        return rid

    def from_template(name):
        return add_media(name, tpl.read("word/media/" + name))

    body = []
    logo_rid = from_template("logo_lockup_horizontal_512.png")
    body.append(title_block(logo_rid, eyebrow, strapline))

    doc_id = [3000]
    seen_h1 = [False]
    used_callouts = set()
    ordered_nums = []

    prev_kind = [None]
    for kind, payload in blocks:
        if kind == "h1":
            body.append(p_heading("Title", payload, False, highlight))
        elif kind == "h2":
            brk = break_before_h1 and seen_h1[0]
            seen_h1[0] = True
            body.append(p_heading("Heading1", payload, brk, highlight))
        elif kind == "h3":
            body.append(p_heading("Heading2", payload, False, highlight))
        elif kind in ("h4", "h5", "h6"):
            body.append(p_heading("Heading3", payload, False, highlight))
        elif kind == "para":
            # An italic-only paragraph directly under the document title is
            # its subtitle, and takes the template's real Subtitle style
            # rather than an italic Normal — matching the Title/Subtitle
            # split the creator applied by hand on 2026-08-14.
            m_sub = re.fullmatch(r"\*([^*].*?)\*", payload.strip())
            if prev_kind[0] == "h1" and m_sub:
                body.append('<w:p><w:pPr><w:pStyle w:val="Subtitle"/>'
                            "</w:pPr>%s</w:p>"
                            % "".join(runs(m_sub.group(1),
                                           highlight=highlight)))
                prev_kind[0] = "subtitle"
                continue
            body.append(p_para(payload, highlight))
        elif kind == "list":
            ordered, items = payload[0], payload[1]
            continues = payload[2] if len(payload) > 2 else False
            if not ordered:
                num_id = 1
            elif continues and ordered_nums:
                # Resumed after a code block that sat inside an item, so it
                # carries on counting rather than restarting.
                num_id = ordered_nums[-1]
            else:
                num_id = ORDERED_NUM_BASE + len(ordered_nums)
                ordered_nums.append(num_id)
            body.append(p_list(ordered, items, highlight, num_id))
        elif kind == "table":
            body.append(p_table(payload, highlight))
        elif kind == "code":
            body.append(p_code(payload[1]))
        elif kind == "rule":
            body.append(p_rule())
        elif kind == "quote":
            body.append(p_quote(payload, highlight))
        elif kind == "callout":
            knd, text = payload
            icon = CALLOUTS[knd][2]
            if icon not in tpl_names and "word/media/" + icon not in tpl_names:
                sys.exit("template has no icon %s for %s callouts"
                         % (icon, knd))
            rid = from_template(icon)
            used_callouts.add(knd)
            body.append(p_callout(knd, text, rid, doc_id[0], highlight))
            doc_id[0] += 2
        elif kind == "image":
            path, caption = payload
            full = path if os.path.isabs(path) else os.path.join(base, path)
            if not os.path.exists(full):
                sys.exit("image not found: %s" % full)
            try:
                from PIL import Image
            except ImportError:
                sys.exit("Pillow is needed for images: pip install pillow")
            with Image.open(full) as im:
                pw, ph = im.size
            max_cx = CONTENT_TWIPS * EMU_PER_TWIP
            # Figures are rendered oversampled so they stay sharp in print;
            # display them at the text column width, never wider.
            cx = min(max_cx, pw * 9525)
            cy = int(cx * ph / pw)
            rid = add_media(os.path.basename(full), open(full, "rb").read())
            body.append(p_image(rid, cx, cy, doc_id[0],
                                caption or os.path.basename(full)))
            doc_id[0] += 1
            if caption:
                body.append(p_caption(caption, highlight))
        prev_kind[0] = kind

    footer_rid = from_template("logo_symbol_256.png")
    footer = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/'
        '2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/'
        '2006/relationships" xmlns:wp="http://schemas.openxmlformats.org/'
        'drawingml/2006/wordprocessingDrawing" xmlns:a="http://schemas.'
        'openxmlformats.org/drawingml/2006/main" xmlns:pic="http://schemas.'
        'openxmlformats.org/drawingml/2006/picture">'
        '<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:drawing>'
        '<wp:inline distT="0" distB="0" distL="0" distR="0">'
        '<wp:extent cx="164592" cy="164592"/>'
        '<wp:effectExtent l="0" t="0" r="0" b="0"/>'
        '<wp:docPr id="1010" name="Grounded AI Practice symbol"/>'
        '<wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect="1"/>'
        '</wp:cNvGraphicFramePr><a:graphic><a:graphicData uri="http://schemas.'
        'openxmlformats.org/drawingml/2006/picture"><pic:pic><pic:nvPicPr>'
        '<pic:cNvPr id="1010" name="Grounded AI Practice symbol"/>'
        '<pic:cNvPicPr/></pic:nvPicPr><pic:blipFill><a:blip r:embed="rIdFtr"/>'
        '<a:stretch><a:fillRect/></a:stretch></pic:blipFill><pic:spPr>'
        '<a:xfrm><a:off x="0" y="0"/><a:ext cx="164592" cy="164592"/></a:xfrm>'
        '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
        '</a:graphicData></a:graphic></wp:inline></w:drawing></w:r>'
        '<w:r><w:rPr><w:rFonts w:ascii="Public Sans" w:hAnsi="Public Sans" '
        'w:cs="Public Sans"/><w:color w:val="%s"/><w:sz w:val="16"/>'
        '<w:szCs w:val="16"/></w:rPr>'
        '<w:t xml:space="preserve">  %s</w:t></w:r></w:p></w:ftr>'
        % (STONE, esc(footer_text)))

    doc_rels = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
                '<Relationships xmlns="http://schemas.openxmlformats.org/'
                'package/2006/relationships">'
                '<Relationship Id="rIdStyles" Type="http://schemas.'
                'openxmlformats.org/officeDocument/2006/relationships/styles" '
                'Target="styles.xml"/>'
                '<Relationship Id="rIdNum" Type="http://schemas.'
                'openxmlformats.org/officeDocument/2006/relationships/'
                'numbering" Target="numbering.xml"/>'
                '<Relationship Id="rIdSettings" Type="http://schemas.'
                'openxmlformats.org/officeDocument/2006/relationships/'
                'settings" Target="settings.xml"/>'
                '<Relationship Id="rIdFooter" Type="http://schemas.'
                'openxmlformats.org/officeDocument/2006/relationships/footer" '
                'Target="footer1.xml"/>']
    for rid, target in rels:
        doc_rels.append('<Relationship Id="%s" Type="http://schemas.'
                        'openxmlformats.org/officeDocument/2006/relationships/'
                        'image" Target="%s"/>' % (rid, target))
    doc_rels.append("</Relationships>")

    footer_rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
                   '<Relationships xmlns="http://schemas.openxmlformats.org/'
                   'package/2006/relationships">'
                   '<Relationship Id="rIdFtr" Type="http://schemas.'
                   'openxmlformats.org/officeDocument/2006/relationships/image"'
                   ' Target="media/logo_symbol_256.png"/></Relationships>')

    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/'
        'content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-'
        'package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Default Extension="png" ContentType="image/png"/>'
        '<Default Extension="jpeg" ContentType="image/jpeg"/>'
        '<Override PartName="/word/document.xml" ContentType="application/vnd.'
        'openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '<Override PartName="/word/styles.xml" ContentType="application/vnd.'
        'openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
        '<Override PartName="/word/numbering.xml" ContentType="application/vnd.'
        'openxmlformats-officedocument.wordprocessingml.numbering+xml"/>'
        '<Override PartName="/word/settings.xml" ContentType="application/vnd.'
        'openxmlformats-officedocument.wordprocessingml.settings+xml"/>'
        '<Override PartName="/word/footer1.xml" ContentType="application/vnd.'
        'openxmlformats-officedocument.wordprocessingml.footer+xml"/>'
        '</Types>')

    package_rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
                    '<Relationships xmlns="http://schemas.openxmlformats.org/'
                    'package/2006/relationships"><Relationship Id="rId1" '
                    'Type="http://schemas.openxmlformats.org/officeDocument/'
                    '2006/relationships/officeDocument" '
                    'Target="word/document.xml"/></Relationships>')

    document = DOC_OPEN + "".join(body) + SECT_PR + "</w:body></w:document>"

    tmp = out_path + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", package_rels)
        z.writestr("word/document.xml", document)
        z.writestr("word/_rels/document.xml.rels", "".join(doc_rels))
        z.writestr("word/footer1.xml", footer)
        z.writestr("word/_rels/footer1.xml.rels", footer_rels)
        # Styles and settings come from the template unchanged — including the
        # compatibilityMode 15 declaration the shape groups need.
        for part in ("word/styles.xml", "word/settings.xml"):
            z.writestr(part, tpl.read(part))
        # Numbering comes from the template too; the only addition is one
        # restarting instance per numbered list. See numbering_with_restarts.
        z.writestr("word/numbering.xml",
                   numbering_with_restarts(
                       tpl.read("word/numbering.xml").decode("utf-8"),
                       ordered_nums).encode("utf-8"))
        for name, data in media.items():
            z.writestr(name, data)
    tpl.close()
    shutil.move(tmp, out_path)
    return len(blocks), len(media), sorted(used_callouts)


def main():
    ap = argparse.ArgumentParser(
        description="Convert Markdown to a house-style .docx.")
    ap.add_argument("markdown", help="source .md file")
    ap.add_argument("-o", "--output", required=True, help="destination .docx")
    ap.add_argument("--template",
                    default="exports/Style_Reference_Example.docx",
                    help="style donor .docx (default: the style reference)")
    ap.add_argument("--footer", default="Grounded AI Practice",
                    help="footer text beside the symbol")
    ap.add_argument("--eyebrow", default="GROUNDED AI PRACTICE",
                    help="small caps label in the title block")
    ap.add_argument("--strapline", default="",
                    help="italic line under the eyebrow")
    ap.add_argument("--highlight", default=None,
                    help="literal token to colour Ember wherever it appears")
    ap.add_argument("--break-before-h1", action="store_true",
                    help="start each top-level section on a new page")
    args = ap.parse_args()

    if not os.path.exists(args.template):
        sys.exit("template not found: %s" % args.template)

    blocks, media, callouts = build(
        args.markdown, args.output, args.template, args.footer,
        args.eyebrow, args.strapline, args.highlight, args.break_before_h1)

    print("wrote %s" % args.output)
    print("  %d blocks, %d media parts" % (blocks, media))
    if callouts:
        print("  callouts: %s" % ", ".join(callouts))
        print("  NOW RUN: python tools/fitshapes.py %s --in-place"
              % args.output)
    print("  THEN:    tools/word_preview.ps1 and tools/word_roundtrip_test.ps1")


if __name__ == "__main__":
    main()
