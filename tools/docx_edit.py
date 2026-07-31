#!/usr/bin/env python3
"""Apply verified text edits to a .docx, including inside callout cards and quotes.

Why this exists
---------------
Revising a Word deliverable in this project means changing prose that lives in
three different places: ordinary body paragraphs, table cells, and the text
boxes inside callout-card and pull-quote drawing groups (see CLAUDE.md, "Word
document conventions"). Doing that by hand means unzipping the .docx and
editing word/document.xml, which is where two things go wrong.

The first is that Word splits a sentence across many <w:r> runs — revision
marks, spell-check state, formatting boundaries — so a phrase you can see on
the page frequently does not exist as a contiguous string in the XML. A naive
search-and-replace silently finds nothing.

The second is worse, and this project has already been bitten by it once: an
edit that quietly does nothing still reports success. tools/fitshapes.py
shipped a bug where a namespace-qualified tag broke an exact-substring check,
the run claimed to have fitted three groups, and the three it had skipped went
unnoticed until someone counted (project_log.md Entry 039). So this tool
treats a replacement that does not match, or that matches more times than
declared, as a hard error. It writes nothing unless every edit in the batch
lands exactly as specified.

How it works
------------
1. Reads word/document.xml from the .docx.
2. For each paragraph, flattens its own <w:t> nodes into one string — shape
   text boxes are handled as their own paragraphs, not merged into the
   paragraph that hosts them, so an edit can never straddle that boundary.
3. Finds the target text in the flattened string and writes the replacement
   back across the underlying nodes, so a phrase split over five runs is
   still matched and replaced correctly.
4. Counts every match across the document and compares it to the expected
   count for that edit. Any mismatch aborts the whole batch.

It can also clone a paragraph — including a whole pull-quote or callout
drawing group — and insert the copy elsewhere, substituting text as it goes.
Drawing identifiers (docPr, cNvPr) are renumbered in the clone, since two
shapes sharing an id is invalid and Word repairs it destructively.

What it does not do
-------------------
It does not change formatting, styles, or shape geometry. Editing the text
inside a card or quote changes how much room that text needs, and nothing
here recomputes it — run tools/fitshapes.py afterwards, then the two real-Word
checks (tools/word_preview.ps1 and tools/word_roundtrip_test.ps1). Rendering
is not the same check as saving.

Requirements
------------
Python 3.9+. Standard library only.

The edit file
-------------
A JSON list of operations. "replace" is the default op and may be written as
a bare object:

    [
      {"find": "old sentence.", "replace": "new sentence."},
      {"find": "recurring phrase", "replace": "new", "count": 3},
      {"op": "clone",
       "source": "text identifying the paragraph to copy",
       "after":  "text identifying the paragraph to insert it after",
       "replacements": [["old quote text", "new quote text"]]}
    ]

"count" declares how many matches to expect (default 1). State it explicitly
rather than letting a phrase match somewhere you did not intend.

Examples
--------
    python tools/docx_edit.py report.docx edits.json -o report_new.docx
    python tools/docx_edit.py report.docx edits.json --in-place
    python tools/docx_edit.py report.docx edits.json --dry-run
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import re
import shutil
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
MC = "{http://schemas.openxmlformats.org/markup-compatibility/2006}"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

W_P = W + "p"
W_T = W + "t"
W_PPR = W + "pPr"
W_PSTYLE = W + "pStyle"
W_VAL = W + "val"
W_BODY = W + "body"
W_DRAWING = W + "drawing"
W_PICT = W + "pict"
W_OBJECT = W + "object"
W_TXBXCONTENT = W + "txbxContent"
MC_ALTERNATE = MC + "AlternateContent"
MC_FALLBACK = MC + "Fallback"

SHAPE_HOLDERS = (W_DRAWING, W_PICT, W_OBJECT, MC_ALTERNATE)

def register_source_namespaces(raw: str) -> None:
    """Teach ElementTree the document's own namespace prefixes before writing.

    ElementTree invents ns0, ns1, ns2 ... prefixes on serialisation for every
    namespace it was not told about. The result is still valid XML and Word
    will still open it, but every tool that matches literal tag names breaks:
    tools/fitshapes.py looks for "<wpg:wgp", and a document rewritten as
    "<ns7:wgp" reports zero shape groups and fits nothing. That is how this
    was found — a refit run that claimed success on a document whose six
    callouts and quotes had become invisible to it.

    Declarations are collected from the whole file, not just the root tag.
    Word also declares namespaces inline on nested elements, and those are
    the ones most easily missed: a picture serialised as
    <pic:pic xmlns:pic="..."> is ordinary OOXML, and that exact pattern has
    caused trouble in this repo before (project_log.md Entry 039).
    """
    for prefix, uri in re.findall(r'xmlns:([\w.-]+)="([^"]+)"', raw):
        ET.register_namespace(prefix, uri)


def first_element_tag(xml: str) -> str:
    """The document's root opening tag, skipping the <?xml ...?> declaration."""
    match = re.search(r"<[\w:.-]+(?:\s[^>]*?)?>", xml)
    return match.group(0) if match else ""


def merge_root_tag(original: str, generated: str) -> str:
    """Restore the source root element, keeping any namespaces ET added.

    ElementTree declares only the namespaces it sees used on an element or an
    attribute name. Word's root element additionally declares prefixes that
    appear nowhere else in the file but are named in mc:Ignorable — w15, w16,
    w16se and friends. Dropping those leaves mc:Ignorable pointing at
    undeclared prefixes, and Word does not report that as a namespace problem:
    it refuses the file outright as corrupted.
    """
    declared = dict(re.findall(r'xmlns:([\w.-]+)="([^"]+)"', original))
    extra = [f'xmlns:{p}="{u}"'
             for p, u in re.findall(r'xmlns:([\w.-]+)="([^"]+)"', generated)
             if p not in declared]
    if not extra:
        return original
    return original[:-1].rstrip() + " " + " ".join(extra) + ">"


def undeclared_ignorable(xml: str) -> list[str]:
    """mc:Ignorable prefixes with no matching declaration on the root element."""
    tag = first_element_tag(xml)
    declared = set(re.findall(r"xmlns:([\w.-]+)=", tag))
    match = re.search(r'mc:Ignorable="([^"]*)"', tag)
    if not match:
        return []
    return [p for p in match.group(1).split() if p not in declared]


def structural_census(xml: str) -> dict[str, int]:
    """Counts of the structures an edit must never destroy."""
    return {
        "shape groups (wpg:wgp)": xml.count("<wpg:wgp"),
        "shapes (wps:wsp)": xml.count("<wps:wsp"),
        "alternate content": xml.count("<mc:AlternateContent"),
        "tables": xml.count("<w:tbl>"),
        "drawings": xml.count("<w:drawing>"),
    }


# ------------------------------------------------------------ text handling
def own_text_nodes(p: ET.Element) -> list[ET.Element]:
    """<w:t> nodes belonging to this paragraph's own runs, excluding shape text."""
    out: list[ET.Element] = []

    def rec(el: ET.Element) -> None:
        for child in el:
            if child.tag in SHAPE_HOLDERS:
                continue
            if child.tag == W_T:
                out.append(child)
            else:
                rec(child)

    rec(p)
    return out


def flatten(nodes: list[ET.Element]) -> str:
    return "".join(n.text or "" for n in nodes)


def replace_across(nodes: list[ET.Element], find: str, repl: str) -> int:
    """Replace every occurrence of `find` spanning these nodes. Returns the count."""
    hits = 0
    while True:
        flat = flatten(nodes)
        start = flat.find(find)
        if start < 0:
            return hits
        end = start + len(find)

        spans, pos = [], 0
        for n in nodes:
            length = len(n.text or "")
            spans.append((pos, pos + length, n))
            pos += length

        first = True
        for s, e, n in spans:
            if e <= start or s >= end:
                continue
            text = n.text or ""
            before = text[: max(0, min(len(text), start - s))]
            after = text[max(0, min(len(text), end - s)) :]
            n.text = before + repl + after if first else before + after
            if n.text != (n.text or "").strip():
                n.set(XML_SPACE, "preserve")
            first = False
        hits += 1


def all_paragraphs(root: ET.Element) -> list[ET.Element]:
    return list(root.iter(W_P))


# ---------------------------------------------------------------- cloning
def renumber_drawing_ids(clone: ET.Element, used: set[int]) -> None:
    """Give every docPr/cNvPr in the clone a fresh id. Duplicates are invalid."""
    nxt = (max(used) + 1) if used else 1000
    for el in clone.iter():
        if el.tag.rsplit("}", 1)[-1] in ("docPr", "cNvPr") and "id" in el.attrib:
            while nxt in used:
                nxt += 1
            el.set("id", str(nxt))
            used.add(nxt)
            nxt += 1


def collect_drawing_ids(root: ET.Element) -> set[int]:
    used: set[int] = set()
    for el in root.iter():
        if el.tag.rsplit("}", 1)[-1] in ("docPr", "cNvPr"):
            try:
                used.add(int(el.get("id", "")))
            except ValueError:
                pass
    return used


def body_index(body: ET.Element, target: ET.Element) -> int:
    for i, child in enumerate(body):
        if child is target or target in child.iter():
            return i
    sys.exit("internal: paragraph is not inside the document body")


def find_body_block(root: ET.Element, body: ET.Element, anchor: str, label: str) -> int:
    """Index in the body of the block containing `anchor`.

    Word stores every drawing shape twice — DrawingML under <mc:Choice> and
    legacy VML under <mc:Fallback> — so text inside a callout or quote matches
    two paragraphs that both live inside the same body-level block. That is
    not ambiguity, so resolve to the block and only complain if the anchor
    genuinely spans separate blocks.
    """
    matches = [p for p in all_paragraphs(root) if anchor in flatten(own_text_nodes(p))]
    if not matches:
        sys.exit(f"{label}: no paragraph contains {anchor!r}")
    idxs = {body_index(body, m) for m in matches}
    if len(idxs) > 1:
        sys.exit(f"{label}: {anchor!r} spans {len(idxs)} separate blocks — make it unique")
    return idxs.pop()


# ------------------------------------------------------------------ driver
def apply_edits(root: ET.Element, edits: list[dict]) -> list[str]:
    body = root.find(W_BODY)
    if body is None:
        sys.exit("document.xml has no <w:body>")

    log: list[str] = []
    for i, edit in enumerate(edits, 1):
        op = edit.get("op", "replace")

        if op == "replace":
            find, repl = edit["find"], edit["replace"]
            expected = edit.get("count", 1)
            hits = sum(replace_across(own_text_nodes(p), find, repl)
                       for p in all_paragraphs(root))
            if expected == "all":
                if hits == 0:
                    sys.exit(f"edit {i}: {find[:70]!r} matched nothing. "
                             "Nothing has been written.")
            elif hits != expected:
                sys.exit(
                    f"edit {i}: expected {expected} match(es) for {find[:70]!r}, "
                    f"found {hits}. Nothing has been written."
                )
            log.append(f"  {i}. replaced x{hits}: {find[:60]!r}")

        elif op == "set_style":
            # Pasting prose into Word regularly strips a paragraph's named
            # style, which silently costs the heading its outline level and so
            # its place in the navigation pane and any table of contents.
            anchor, style = edit["anchor"], edit.get("style")
            expected = edit.get("count", 1)
            targets = [p for p in all_paragraphs(root)
                       if anchor in flatten(own_text_nodes(p))]
            if len(targets) != expected:
                sys.exit(
                    f"edit {i}: expected {expected} paragraph(s) matching "
                    f"{anchor[:60]!r}, found {len(targets)}. Nothing written."
                )
            for p in targets:
                pr = p.find(W_PPR)
                if pr is None:
                    pr = ET.Element(W_PPR)
                    p.insert(0, pr)
                if edit.get("clear_direct"):
                    for child in list(pr):
                        pr.remove(child)
                if style:
                    for old in pr.findall(W_PSTYLE):
                        pr.remove(old)
                    ps = ET.Element(W_PSTYLE)
                    ps.set(W_VAL, style)
                    pr.insert(0, ps)  # the schema requires pStyle first in pPr
                # An empty pPr is legal but noise; drop it so the paragraph
                # matches unstyled siblings exactly.
                if len(pr) == 0 and not pr.attrib:
                    p.remove(pr)
            what = f"style -> {style}" if style else "cleared direct formatting"
            log.append(f"  {i}. {what} x{len(targets)}: {anchor[:50]!r}")

        elif op == "clone":
            src_idx = find_body_block(root, body, edit["source"], f"edit {i} source")
            clone = copy.deepcopy(body[src_idx])
            renumber_drawing_ids(clone, collect_drawing_ids(root))
            counts = []
            for find, repl in edit.get("replacements", []):
                hits = sum(replace_across(own_text_nodes(p), find, repl)
                           for p in clone.iter(W_P))
                if hits == 0:
                    sys.exit(
                        f"edit {i}: clone replacement {find[:60]!r} matched nothing "
                        f"inside the copied block. Nothing has been written."
                    )
                counts.append(hits)
            # Resolve the insertion point only after the clone is built, so an
            # anchor added by an earlier edit in this batch is visible.
            after_idx = find_body_block(root, body, edit["after"], f"edit {i} after")
            body.insert(after_idx + 1, clone)
            log.append(f"  {i}. cloned after {edit['after'][:50]!r} "
                       f"(replacements matched {counts})")

        else:
            sys.exit(f"edit {i}: unknown op {op!r}")

    return log


def process(src: str, dest: str, edits: list[dict], dry_run: bool) -> list[str]:
    with tempfile.TemporaryDirectory() as work:
        with zipfile.ZipFile(src) as z:
            order = z.namelist()
            if "word/document.xml" not in order:
                sys.exit(f"{src} has no word/document.xml — is it really a .docx?")
            z.extractall(work)

        doc = os.path.join(work, "word", "document.xml")
        with open(doc, encoding="utf-8") as fh:
            raw = fh.read()

        register_source_namespaces(raw)
        before = structural_census(raw)

        root = ET.fromstring(raw)
        log = apply_edits(root, edits)

        if dry_run:
            return log

        # Keep the original XML prologue byte for byte; Word cares about the
        # standalone="yes" declaration and ET does not emit it.
        split = re.match(r"(.*?)(<[\w:.-]+[\s>])", raw, re.S)
        prologue = split.group(1) if split else ""
        new_raw = prologue + ET.tostring(root, encoding="unicode")
        # ElementTree closes empty elements as "<tag />"; Word writes "<tag/>".
        # Tools in this repo match Word's form literally — fitshapes.py reads
        # <a:ext cx=".." cy=".."/> with a regex — so normalise back rather than
        # leave a document that only some of the toolchain can parse. Text
        # content cannot contain a literal "/>" because > is escaped there.
        new_raw = new_raw.replace(" />", "/>")
        # Put the document's own root element back, with its full set of
        # namespace declarations. See merge_root_tag for why this matters.
        orig_root, new_root = first_element_tag(raw), first_element_tag(new_raw)
        if orig_root and new_root:
            new_raw = new_raw.replace(new_root, merge_root_tag(orig_root, new_root), 1)

        stranded = undeclared_ignorable(new_raw)
        if stranded:
            sys.exit(
                "aborted: mc:Ignorable names prefixes that are not declared on the "
                f"root element ({', '.join(stranded)}). Word rejects this as a "
                "corrupt file. Nothing has been written."
            )

        invented = len(re.findall(r"<ns\d+:", new_raw))
        if invented:
            sys.exit(
                f"aborted: serialisation invented {invented} namespace prefixes "
                "(ns0:, ns1: ...). The document's own prefixes were not preserved, "
                "which silently breaks fitshapes.py. Nothing has been written."
            )
        after = structural_census(new_raw)
        lost = {k: (before[k], after[k]) for k in before if after[k] < before[k]}
        if lost:
            detail = "; ".join(f"{k}: {b} -> {a}" for k, (b, a) in lost.items())
            sys.exit(f"aborted: edits destroyed document structure ({detail}). "
                     "Nothing has been written.")

        with open(doc, "w", encoding="utf-8", newline="") as fh:
            fh.write(new_raw)

        log.append("  structure check: " + ", ".join(
            f"{k.split(' (')[0]} {before[k]}->{after[k]}" for k in before))

        tmp_out = os.path.join(work, "_out.docx")
        with zipfile.ZipFile(tmp_out, "w", zipfile.ZIP_DEFLATED) as z:
            for name in order:
                full = os.path.join(work, name)
                if os.path.exists(full):
                    z.write(full, name)
        shutil.move(tmp_out, dest)
    return log


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Apply verified text edits to a .docx, shape text included.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("source", help="input .docx")
    parser.add_argument("edits", help="JSON file of edit operations")
    parser.add_argument("-o", "--out", help="output .docx")
    parser.add_argument("--in-place", action="store_true",
                        help="overwrite the source file — back it up first")
    parser.add_argument("--dry-run", action="store_true",
                        help="verify every edit matches, then write nothing")
    args = parser.parse_args()

    if not args.dry_run and (args.in_place == bool(args.out)):
        sys.exit("Pass either -o DEST or --in-place, not both or neither.")

    with open(args.edits, encoding="utf-8") as fh:
        edits = json.load(fh)

    dest = args.source if args.in_place else (args.out or args.source)
    log = process(args.source, dest, edits, args.dry_run)

    print("\n".join(log))
    if args.dry_run:
        print(f"\ndry run: all {len(edits)} edit(s) matched. Nothing written.")
    else:
        print(f"\nwrote {dest} ({len(edits)} edit(s) applied)")
        print("Text inside a card or quote has changed size — run tools/fitshapes.py, "
              "then word_preview.ps1 and word_roundtrip_test.ps1.")


if __name__ == "__main__":
    main()
