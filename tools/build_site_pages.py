#!/usr/bin/env python3
"""Assemble the landing site's HTML pages from one shared layout.

WHY THIS EXISTS
---------------
The site began as a single page, so its header, nav and footer lived in
one file and there was nothing to share. As a multi-page site that shell
would be copied into every page, and a nav change would mean editing
every file and hoping none was missed.

Jekyll would solve that, and GitHub Pages runs it for free, but it puts a
build step between what the preview server shows and what visitors get:
checking the finished page locally then needs Ruby and a setup matching
GitHub's. This project's whole method is verifying output against ground
truth rather than guessing at it, so a pipeline that can only be checked
after publishing is the wrong trade. This script keeps the single source
for the shell and still emits plain, portable HTML that any host can
serve and the local preview renders identically.

HOW IT WORKS
------------
Sources live in ``site/`` and output lands in ``docs/``. That separation
is not cosmetic: GitHub Pages publishes everything under ``docs/``, so a
fragment left in there would be served to the public as a half-page.

    site/pages.json      site config and the ordered page list
    site/layout.html     the shell, with {{token}} placeholders
    site/pages/*.html    one content fragment per page (inner <main>)

Each page in the manifest names its fragment, its output path, its title
and description, and whether it appears in the nav. The script fills the
layout's tokens per page, generates the nav with ``aria-current="page"``
on the page being rendered, and resolves ``{{root}}`` to the relative
prefix that page needs ("" at the top level, "../" one level down) so
every asset reference stays relative and the site works unchanged at a
project URL, at a domain root, or opened from disk.

NOTHING IS WRITTEN UNTIL EVERY PAGE PASSES EVERY CHECK
------------------------------------------------------
All pages are assembled in memory and verified as a set, because a build
that writes three good pages and then fails leaves the site in a state
nobody chose. The checks:

  * no ``{{token}}`` survives into the output, which would otherwise ship
    a literal placeholder to a reader;
  * fragments are fragments, carrying no <html>, <head> or <body>;
  * tags balance, so a dropped </div> is caught here rather than by a
    browser silently repairing it into a different layout;
  * every local href/src/srcset resolves to a file that will exist in
    ``docs/`` after the build;
  * every ``#anchor`` resolves to an id that exists on the page it points
    at, across pages as well as within them.

That last check is the one that earns its keep during a page split: the
single-page site linked to ``#evidence`` and ``#method``, and those
become cross-page links the moment the sections move to their own files.
A browser gives no warning when such a link silently goes nowhere.

The script only ever writes the output files named in the manifest. It
never deletes and never cleans, because ``docs/`` also holds the
stylesheet, fonts, icons, generated figures and ``.nojekyll``, none of
which it owns.

USAGE
-----
    python tools/build_site_pages.py            build and report changes
    python tools/build_site_pages.py --check    verify only, write nothing
    python tools/build_site_pages.py --list     show the page table

``--check`` verifies and additionally reports whether the files on disk
are already up to date, for use before a commit that touches the site.

Command-line only, by the project_log.md Entry 049 decision: a build step
runs this, not a person, so the every-tool-gets-a-GUI rule does not reach
it.

Requires Python, standard library only. No Ruby, no Node, no network.
"""

from __future__ import annotations

import argparse
import html.parser
import json
import posixpath
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site"
DOCS = REPO / "docs"

MANIFEST = SITE / "pages.json"
LAYOUT = SITE / "layout.html"
FRAGMENTS = SITE / "pages"

TOKEN = re.compile(r"\{\{\s*([a-z_]+)\s*\}\}")

# Elements that never carry a closing tag, so the balance check must not
# expect one. Matches the HTML spec's void element list.
VOID = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}

# Attributes whose values point at something that must exist.
URL_ATTRS = ("href", "src", "srcset")


class Problem(Exception):
    """A build-stopping defect. Message is written for a human."""


# --------------------------------------------------------------------------
# parsing helpers
# --------------------------------------------------------------------------

class _Collector(html.parser.HTMLParser):
    """Collects ids, link targets and tag balance from assembled HTML."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[tuple[str, int]] = []   # (url, line)
        self.stack: list[tuple[str, int]] = []
        self.imbalance: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        got = dict(attrs)
        if got.get("id"):
            self.ids.add(got["id"])
        for attr in URL_ATTRS:
            value = got.get(attr)
            if not value:
                continue
            if attr == "srcset":
                # "a.svg 1x, b.svg 2x" -> the URL is the first token of each part
                for part in value.split(","):
                    candidate = part.strip().split()
                    if candidate:
                        self.links.append((candidate[0], self.getpos()[0]))
            else:
                self.links.append((value, self.getpos()[0]))
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_startendtag(self, tag, attrs) -> None:      # <foo />
        self.handle_starttag(tag, attrs)
        if tag not in VOID and self.stack and self.stack[-1][0] == tag:
            self.stack.pop()

    def handle_endtag(self, tag: str) -> None:
        if tag in VOID:
            return
        if not self.stack:
            if self.imbalance is None:
                self.imbalance = (
                    f"line {self.getpos()[0]}: </{tag}> with nothing open"
                )
            return
        open_tag, open_line = self.stack[-1]
        if open_tag != tag:
            if self.imbalance is None:
                self.imbalance = (
                    f"line {self.getpos()[0]}: </{tag}> closes <{open_tag}> "
                    f"opened on line {open_line}"
                )
            return
        self.stack.pop()


def _collect(markup: str) -> _Collector:
    parser = _Collector()
    parser.feed(markup)
    parser.close()
    return parser


# --------------------------------------------------------------------------
# assembly
# --------------------------------------------------------------------------

def _read(path: Path, what: str) -> str:
    if not path.exists():
        raise Problem(f"{what} is missing: {path.relative_to(REPO)}")
    return path.read_text(encoding="utf-8")


def _depth_prefix(output: str) -> str:
    """Relative prefix from a page's own directory back to docs/."""
    depth = output.count("/")
    return "../" * depth


def _build_nav(nav_items: list[dict], current: str, root: str) -> str:
    """The nav list items, with the current page marked for assistive tech."""
    lines = []
    for item in nav_items:
        classes = f' class="{item["class"]}"' if item.get("class") else ""
        if "url" in item:
            href, current_attr = item["url"], ""
        else:
            target = item["page"]
            href = root + item["href"]
            current_attr = ' aria-current="page"' if target == current else ""
        lines.append(
            f'        <li><a{classes} href="{href}"{current_attr}>'
            f'{item["label"]}</a></li>'
        )
    return "\n".join(lines)


def assemble(manifest: dict, layout: str) -> dict[str, str]:
    """Render every page to a string. Raises Problem on any defect."""
    site = manifest["site"]
    base = site["base_url"].rstrip("/") + "/"
    nav_items = manifest["nav"]

    by_slug = {page["slug"]: page for page in manifest["pages"]}
    for item in nav_items:
        if "page" in item and item["page"] not in by_slug:
            raise Problem(
                f'nav points at "{item["page"]}", which is not a page in '
                f"pages.json"
            )

    built: dict[str, str] = {}
    for page in manifest["pages"]:
        fragment_path = FRAGMENTS / page["fragment"]
        fragment = _read(fragment_path, f'fragment for "{page["slug"]}"')

        lowered = fragment.lower()
        for banned in ("<html", "<head", "<body"):
            if banned in lowered:
                raise Problem(
                    f'{fragment_path.relative_to(REPO)} contains "{banned}". '
                    f"Fragments hold page content only; the shell lives in "
                    f"site/layout.html."
                )

        root = _depth_prefix(page["output"])
        url_path = page["url"]
        values = {
            "root": root,
            "home": root if root else "./",
            "title": page["title"],
            "description": page["description"],
            "canonical": base + url_path,
            "og_title": page.get("og_title", page["title"]),
            "og_description": page.get("og_description", page["description"]),
            "og_url": base + url_path,
            "og_image": base + site["og_image"],
            "site_name": site["name"],
            "nav": _build_nav(nav_items, page["slug"], root),
        }

        def substitute(match: re.Match) -> str:
            key = match.group(1)
            if key not in values:
                raise Problem(
                    f'{{{{{key}}}}} is used but not defined by this script. '
                    f"Known tokens: {', '.join(sorted(values))}."
                )
            return str(values[key])

        # Fragments are substituted before insertion, not after, so a page
        # one level down can write {{root}}assets/... and get ../assets/... .
        # Doing it in the other order would leave the token untouched, since
        # re.sub does not rescan what it has just inserted.
        values["content"] = TOKEN.sub(substitute, fragment).strip("\n")
        rendered = TOKEN.sub(substitute, layout)

        leftover = TOKEN.search(rendered)
        if leftover:
            raise Problem(
                f'page "{page["slug"]}" still contains {leftover.group(0)} '
                f"after substitution"
            )

        built[page["output"]] = rendered

    return built


# --------------------------------------------------------------------------
# verification
# --------------------------------------------------------------------------

def verify(built: dict[str, str], manifest: dict) -> list[str]:
    """Every check that must pass before anything is written."""
    problems: list[str] = []
    collected = {}

    for output, markup in built.items():
        parsed = _collect(markup)
        collected[output] = parsed
        if parsed.imbalance:
            problems.append(f"{output}: unbalanced tags, {parsed.imbalance}")
        elif parsed.stack:
            tag, line = parsed.stack[-1]
            problems.append(
                f"{output}: <{tag}> opened on line {line} is never closed"
            )

    # Files that will exist in docs/ after this build: everything already
    # there, plus everything this build is about to write.
    on_disk = {
        p.relative_to(DOCS).as_posix()
        for p in DOCS.rglob("*")
        if p.is_file()
    }
    after_build = on_disk | set(built)

    for output, markup in built.items():
        page_dir = posixpath.dirname(output)
        for url, line in collected[output].links:
            url = url.strip()
            if not url or url.startswith(("http://", "https://", "mailto:", "data:", "//")):
                continue

            target, _, fragment = url.partition("#")

            if not target:                       # same-page anchor
                if fragment and fragment not in collected[output].ids:
                    problems.append(
                        f'{output}:{line}: "#{fragment}" matches no id on '
                        f"this page"
                    )
                continue

            if target.startswith("/"):
                problems.append(
                    f'{output}:{line}: "{url}" is root-relative, which '
                    f"breaks when the site is served from a project URL. "
                    f"Use {{{{root}}}} instead."
                )
                continue

            resolved = posixpath.normpath(posixpath.join(page_dir, target))
            candidates = [resolved]
            if target.endswith("/") or resolved in {"", "."}:
                candidates = [posixpath.join(resolved, "index.html").lstrip("./")]
                candidates[0] = candidates[0] or "index.html"

            if not any(c in after_build for c in candidates):
                problems.append(
                    f'{output}:{line}: "{url}" points at '
                    f"{candidates[0]}, which does not exist"
                )
                continue

            if fragment:
                hit = candidates[0]
                if hit in collected and fragment not in collected[hit].ids:
                    problems.append(
                        f'{output}:{line}: "{url}" points at an id that does '
                        f"not exist on {hit}"
                    )

    return problems


# --------------------------------------------------------------------------
# entry point
# --------------------------------------------------------------------------

def load() -> tuple[dict, str]:
    manifest = json.loads(_read(MANIFEST, "site/pages.json"))
    layout = _read(LAYOUT, "site/layout.html")
    return manifest, layout


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Assemble docs/ pages from site/ sources.",
    )
    parser.add_argument(
        "--check", action="store_true",
        help="verify and report drift without writing anything",
    )
    parser.add_argument(
        "--list", action="store_true",
        help="print the page table and exit",
    )
    args = parser.parse_args(argv)

    try:
        manifest, layout = load()

        if args.list:
            print(f"{'slug':<12} {'output':<28} {'in nav':<7} title")
            in_nav = {i.get("page") for i in manifest["nav"]}
            for page in manifest["pages"]:
                mark = "yes" if page["slug"] in in_nav else "-"
                print(
                    f"{page['slug']:<12} {page['output']:<28} {mark:<7} "
                    f"{page['title'][:44]}"
                )
            return 0

        built = assemble(manifest, layout)
        problems = verify(built, manifest)

    except Problem as exc:
        print(f"build refused: {exc}", file=sys.stderr)
        return 2

    if problems:
        print(
            f"build refused: {len(problems)} problem(s), nothing written",
            file=sys.stderr,
        )
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1

    # read_text translates CRLF to \n, so this compares content rather than
    # bytes. That is deliberate: pages are written LF (see .gitattributes) and
    # a file differing only in line endings is not a change worth reporting.
    changed, same = [], []
    for output, markup in sorted(built.items()):
        destination = DOCS / output
        current = (
            destination.read_text(encoding="utf-8") if destination.exists() else None
        )
        (changed if current != markup else same).append(output)

    if args.check:
        print(f"{len(built)} page(s) verified, nothing written")
        if changed:
            print(f"out of date on disk: {', '.join(changed)}")
            return 1
        print("docs/ is up to date")
        return 0

    for output, markup in sorted(built.items()):
        destination = DOCS / output
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(markup, encoding="utf-8", newline="\n")

    print(f"{len(built)} page(s) written to docs/")
    for output in changed:
        print(f"  changed   {output}")
    for output in same:
        print(f"  unchanged {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
