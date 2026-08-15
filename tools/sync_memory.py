#!/usr/bin/env python3
"""Mirror Claude Code's machine-local memory into ``internal/``, per machine.

WHY THIS EXISTS
---------------
Claude Code keeps its cross-session memory in a per-project folder under
the user's home directory, outside the repository. That folder is
machine-local by design and nothing carries it between machines, so the
laptop cannot see what the desktop learned and vice versa. This project
has already lost that memory once: a folder move on one machine orphaned
every file under the old project path, and no memory loaded for days
before anyone noticed (`CLAUDE.md`, the 2026-08-03 extraction pass).

``internal/`` is the one directory that already travels between the two
machines, by file sync rather than by git, and it is gitignored and
hook-blocked so nothing here can reach the public repository. That makes
it the right destination: memory files carry behavioural notes about the
creator and their environment, which is material that should never be
committed anyway.

This does not replace the rule-extraction pass. That pass promotes
durable *project* rules into ``CLAUDE.md``, which is where they belong
because the repo travels on its own. This mirror preserves everything
else — the machine-local and behavioural context that never earns a
rule but is still worth having on the other machine.

ONE FOLDER PER MACHINE, AND WHY IT IS NOT NEGOTIABLE
----------------------------------------------------
The sync layer copies whichever version of a file it saw last. It does
not reconcile two machines' edits; that is what git is for, and git is
exactly what cannot be used here. So if both machines mirrored into one
shared folder, the second sync would overwrite the first machine's
memories with its own — silently, and with no history to recover from.
That is a worse failure than the one this tool exists to fix.

Each machine therefore writes only ``internal/claude_memory/<label>/``
and never touches another machine's folder. The mirrors sit side by
side, both readable from either machine. ``--status`` is what makes them
useful: it lists every machine's mirror and names the memories one
machine holds that this one does not.

WHAT IT REFUSES
---------------
Refusals matter more than features here, because the failure mode is
silent data loss:

  * no ``internal/`` — the sync is not set up, or this is the wrong
    checkout, and writing a mirror nobody will see is worse than saying
    so;
  * no memory folder for this project — reported with every path
    searched, rather than creating an empty mirror that reads as "this
    machine has learned nothing";
  * a mirrored file newer than its local counterpart — that means the
    mirror holds something the local folder does not, so overwriting it
    would destroy the newer copy. Reported and skipped unless
    ``--force``;
  * any destination outside ``internal/claude_memory/``.

Deletion is never propagated. A memory removed locally stays in the
mirror until a person removes it, because "gone from this machine" and
"should be gone everywhere" are different statements and this tool
cannot tell them apart.

USAGE
-----
    python tools/sync_memory.py               # mirror, and report
    python tools/sync_memory.py --dry-run     # what would change
    python tools/sync_memory.py --status      # every machine's mirror
    python tools/sync_memory.py --machine X   # override the folder label

Requires Python, standard library only. Command-line by the Entry 049
decision: this is housekeeping run at a session boundary, not a
learner-facing tool.
"""

from __future__ import annotations

import argparse
import filecmp
import json
import os
import platform
import shutil
import socket
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MIRROR_ROOT = REPO / "internal" / "claude_memory"
STAMP = "_machine.json"


class Problem(Exception):
    """A condition the tool refuses to work around."""


# --------------------------------------------------------------- locating


def project_key(repo: Path) -> str:
    """Claude Code's folder name for a project path.

    ``C:\\dev\\grounded-ai-practice`` becomes
    ``C--dev-grounded-ai-practice``: the drive colon and every separator
    become a dash.
    """
    text = str(repo)
    for ch in (":", "\\", "/"):
        text = text.replace(ch, "-")
    return text


def find_memory_dir(repo: Path) -> Path:
    """Locate this machine's memory folder for this project.

    The derived name is tried first, then any sibling whose name matches
    case-insensitively, because the path is machine-specific and a
    recorded example is not to be trusted.
    """
    projects = Path.home() / ".claude" / "projects"
    searched = []

    exact = projects / project_key(repo) / "memory"
    searched.append(exact)
    if exact.is_dir():
        return exact

    if projects.is_dir():
        want = project_key(repo).lower()
        for child in sorted(projects.iterdir()):
            if child.name.lower() == want and (child / "memory").is_dir():
                return child / "memory"
        searched.append(projects / "<no case-insensitive match>")

    raise Problem(
        "no memory folder found for this project. Searched:\n  "
        + "\n  ".join(str(p) for p in searched)
        + "\nIf the repository has moved, the old folder is orphaned and "
        "still holds the memories — copy it across before mirroring."
    )


def machine_label(explicit: str | None) -> str:
    label = explicit or socket.gethostname() or platform.node()
    label = label.strip()
    if not label:
        raise Problem("could not determine a machine name; pass --machine")
    for ch in '<>:"/\\|?*':
        label = label.replace(ch, "-")
    return label


# ----------------------------------------------------------------- mirror


def _stamp(dest: Path, source: Path, label: str, count: int) -> None:
    (dest / STAMP).write_text(
        json.dumps(
            {
                "machine": label,
                "hostname": socket.gethostname(),
                "user": os.environ.get("USERNAME") or os.environ.get("USER", ""),
                "memory_source": str(source),
                "files": count,
                "last_mirrored": datetime.now(timezone.utc)
                .replace(microsecond=0)
                .isoformat(),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def mirror(source: Path, label: str, dry_run: bool, force: bool) -> int:
    dest = MIRROR_ROOT / label
    if MIRROR_ROOT not in dest.parents:
        raise Problem(f"destination escapes the mirror root: {dest}")

    files = sorted(p for p in source.glob("*.md") if p.is_file())
    if not files:
        raise Problem(f"no .md memory files in {source}")

    new, updated, same, blocked = [], [], [], []

    for src in files:
        dst = dest / src.name
        if not dst.exists():
            new.append(src.name)
        elif filecmp.cmp(src, dst, shallow=False):
            same.append(src.name)
            continue
        elif dst.stat().st_mtime > src.stat().st_mtime and not force:
            blocked.append(src.name)
            continue
        else:
            updated.append(src.name)

        if not dry_run:
            dest.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    if not dry_run and (new or updated):
        _stamp(dest, source, label, len(files))

    verb = "would be" if dry_run else ""
    print(f"machine  {label}")
    print(f"source   {source}")
    print(f"mirror   {dest}")
    print(
        f"  {len(new)} new, {len(updated)} updated, {len(same)} unchanged"
        + (f", {len(blocked)} BLOCKED" if blocked else "")
    )
    for name in new:
        print(f"    + {name} {verb}".rstrip())
    for name in updated:
        print(f"    ~ {name} {verb}".rstrip())

    if blocked:
        print(
            "\n  The mirrored copy is NEWER than the local one for these,\n"
            "  so the mirror holds something this machine does not:"
        )
        for name in blocked:
            print(f"    ! {name}")
        print(
            "  Nothing was overwritten. Read the mirrored copy, fold in what\n"
            "  matters, then re-run with --force to accept the local version."
        )
        return 1
    return 0


# ----------------------------------------------------------------- status


def status(current: str) -> int:
    if not MIRROR_ROOT.is_dir():
        print(f"no mirrors yet at {MIRROR_ROOT}")
        return 0

    machines = sorted(p for p in MIRROR_ROOT.iterdir() if p.is_dir())
    if not machines:
        print(f"no machine folders under {MIRROR_ROOT}")
        return 0

    holdings: dict[str, set[str]] = {}
    for folder in machines:
        names = {p.name for p in folder.glob("*.md")}
        holdings[folder.name] = names
        stamp = folder / STAMP
        when = "unknown"
        if stamp.is_file():
            try:
                when = json.loads(stamp.read_text(encoding="utf-8")).get(
                    "last_mirrored", "unknown"
                )
            except (json.JSONDecodeError, OSError):
                pass
        here = "  (this machine)" if folder.name == current else ""
        print(f"{folder.name:<24} {len(names):>3} files   last {when}{here}")

    mine = holdings.get(current, set())
    elsewhere = {
        name: who
        for who, names in holdings.items()
        if who != current
        for name in names - mine
    }
    if elsewhere:
        print(f"\nHeld on another machine but not on {current}:")
        for name in sorted(elsewhere):
            print(f"  {name}   (from {elsewhere[name]})")
        print(
            "\nThese are readable now. Anything durable and project-level\n"
            "belongs in CLAUDE.md via the rule-extraction pass, not only here."
        )
    elif mine:
        print(f"\nNothing on another machine that {current} does not also hold.")
    return 0


# ------------------------------------------------------------------- main


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Mirror Claude Code's local memory into internal/, per machine."
    )
    ap.add_argument("--machine", help="folder label (default: this hostname)")
    ap.add_argument("--dry-run", action="store_true", help="report without writing")
    ap.add_argument("--status", action="store_true", help="show every machine's mirror")
    ap.add_argument(
        "--force",
        action="store_true",
        help="overwrite mirrored files that are newer than the local copy",
    )
    args = ap.parse_args(argv)

    try:
        label = machine_label(args.machine)
        if args.status:
            return status(label)
        if not (REPO / "internal").is_dir():
            raise Problem(
                f"no internal/ directory at {REPO / 'internal'}.\n"
                "That folder is how memory reaches the other machine. Without "
                "it there is nothing to mirror into."
            )
        return mirror(find_memory_dir(REPO), label, args.dry_run, args.force)
    except Problem as exc:
        print(f"sync_memory: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
