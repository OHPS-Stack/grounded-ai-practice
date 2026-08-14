#!/usr/bin/env python3
r"""Stage part of one file's uncommitted additions, so two unrelated sets of
changes to the same file can be committed separately.

Why this exists
---------------
A file-sync layer sits over this repo (`CLAUDE.md`, Git conventions):
`internal/` is gitignored and can only travel between machines by sync, and
tracked files can arrive the same way. Sync copies whichever version of a
file it saw last. It does not merge. On 2026-08-14 a sync landed one
machine's uncommitted work mid-session, and `research_log.md` ended up
holding two independent sets of additions — a research thread written here
and an unrelated one written on the other machine — which belonged in two
different commits rather than one bundle.

`git add -p` is the normal answer to that and is not available to Claude:
the harness cannot drive interactive git. This is the non-interactive
equivalent for the additions-only case, which is what a numbered log or an
appended table always is.

How it works
------------
The subset is described by what to leave out rather than what to keep,
because the lines to exclude are the identifiable ones — a source-key tag,
an entry heading. Given a file and at least one `--drop`:

1. **Refuse unless the file is HEAD plus additions only.** Deletions make
   "drop these added lines" ambiguous, and guessing there is how a real edit
   gets silently reverted.
2. Build the subset in memory: drop every line starting with a `--drop`
   prefix, and with `--drop-from`, drop from the first line starting with
   that marker to the end of the file.
3. **Check before writing anything:** every pattern matched at least once,
   the result still differs from HEAD, it still differs from the working
   tree, and no line ending changed.
4. Stage it with `git hash-object -w --path` and `git update-index
   --cacheinfo`. **The `--path` argument is not optional** — it applies the
   repo's own CRLF clean filter, and hashing a working-tree file without it
   stages a blob that differs from HEAD in every line.
5. Reconcile the split and refuse if it does not add up: staged additions
   plus the additions left unstaged must equal the original count.

The working tree is never modified and nothing is committed — reviewing the
staged diff and committing stay separate, deliberate steps.

Requirements
------------
Python, standard library only, run inside a git working tree. Command-line
only by the `project_log.md` Entry 049 decision: this is git surgery run by
Claude or by someone already in a terminal, not one of the learner-facing
tools the GUI rule covers.

Usage
-----
    # preview the split, write nothing
    python tools/stage_subset.py research_log.md \
        --drop "| \`[INTEL-" --drop-from "### Entry 086" --dry-run

    # stage the subset, then review and commit yourself
    python tools/stage_subset.py research_log.md \
        --drop "| \`[INTEL-" --drop-from "### Entry 086"
    git diff --cached
"""

import argparse
import subprocess
import sys


def git(*args, binary=False):
    """Run a git command, returning stdout. Raises on a non-zero exit."""
    result = subprocess.run(
        ("git",) + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False
    )
    if result.returncode != 0:
        raise SystemExit(
            f"git {' '.join(args)} failed:\n{result.stderr.decode('utf-8', 'replace')}"
        )
    return result.stdout if binary else result.stdout.decode("utf-8")


def numstat(*args):
    """Return (insertions, deletions) for a single-file numstat, or (0, 0)."""
    out = git(*args).strip()
    if not out:
        return 0, 0
    added, removed = out.split("\t")[:2]
    if added == "-" or removed == "-":
        raise SystemExit("Refusing: git reports this path as binary.")
    return int(added), int(removed)


def endings(text):
    """Return (crlf count, lone-LF count)."""
    crlf = text.count("\r\n")
    return crlf, text.count("\n") - crlf


def main():
    parser = argparse.ArgumentParser(
        description="Stage a subset of one file's uncommitted additions.",
        epilog="Patterns match the start of a line. Nothing is committed.",
    )
    parser.add_argument("path", help="repo-relative path of the tracked file")
    parser.add_argument(
        "--drop",
        action="append",
        default=[],
        metavar="PREFIX",
        help="drop lines starting with PREFIX; repeatable",
    )
    parser.add_argument(
        "--drop-from",
        metavar="PREFIX",
        help="drop from the first line starting with PREFIX to end of file",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="report the split without staging"
    )
    args = parser.parse_args()

    if not args.drop and not args.drop_from:
        parser.error("give at least one --drop or --drop-from")

    path = args.path.replace("\\", "/")

    if path not in git("ls-files", "--", path).split():
        raise SystemExit(f"Refusing: {path} is not tracked at this exact path.")

    staged_add, staged_del = numstat("diff", "--cached", "--numstat", "--", path)
    if staged_add or staged_del:
        raise SystemExit(
            f"Refusing: {path} already has staged changes, which this would "
            "overwrite. Unstage them first (git restore --staged)."
        )

    total_add, total_del = numstat("diff", "--numstat", "HEAD", "--", path)
    if total_del:
        raise SystemExit(
            f"Refusing: {path} has {total_del} deleted line(s) against HEAD. "
            "This tool only handles files changed by addition."
        )
    if not total_add:
        raise SystemExit(f"Nothing to do: {path} matches HEAD.")

    with open(path, "r", encoding="utf-8", newline="") as handle:
        original = handle.read()

    kept, hits, cut_from = [], {p: 0 for p in args.drop}, None
    for index, line in enumerate(original.splitlines(keepends=True)):
        if args.drop_from and line.startswith(args.drop_from):
            cut_from = index
            break
        matched = next((p for p in args.drop if line.startswith(p)), None)
        if matched is not None:
            hits[matched] += 1
            continue
        kept.append(line)

    unmatched = [p for p, count in hits.items() if count == 0]
    if unmatched:
        raise SystemExit(
            "Refusing: these --drop patterns matched nothing, so the split is "
            "not what was asked for:\n  " + "\n  ".join(unmatched)
        )
    if args.drop_from and cut_from is None:
        raise SystemExit(
            f"Refusing: --drop-from {args.drop_from!r} matched no line."
        )

    while kept and not kept[-1].strip():
        kept.pop()
    subset = "".join(kept)

    if subset == original:
        raise SystemExit("Refusing: the subset is the whole file; nothing dropped.")

    before, after = endings(original), endings(subset)
    if before[1] == 0 and after[1] != 0:
        raise SystemExit(
            f"Refusing: the subset introduced {after[1]} bare LF(s) into a "
            "CRLF file."
        )

    head_blob = git("rev-parse", f"HEAD:{path}").strip()
    subset_probe = subprocess.run(
        ("git", "hash-object", "--path", path, "--stdin"),
        input=subset.encode("utf-8"),
        stdout=subprocess.PIPE,
        check=True,
    ).stdout.decode().strip()
    if subset_probe == head_blob:
        raise SystemExit(
            "Refusing: the subset is identical to HEAD, so it would stage "
            "nothing. Check the patterns."
        )

    print(f"{path}: {total_add} added line(s) against HEAD")
    for pattern, count in hits.items():
        print(f"  dropped {count:>3} line(s) starting {pattern!r}")
    if cut_from is not None:
        cut_count = len(original.splitlines()) - cut_from
        print(f"  dropped {cut_count:>3} line(s) from {args.drop_from!r} onward")

    if args.dry_run:
        print("\nDry run: nothing staged.")
        return

    blob = subprocess.run(
        ("git", "hash-object", "-w", "--path", path, "--stdin"),
        input=subset.encode("utf-8"),
        stdout=subprocess.PIPE,
        check=True,
    ).stdout.decode().strip()
    git("update-index", "--cacheinfo", f"100644,{blob},{path}")

    now_staged, staged_removed = numstat("diff", "--cached", "--numstat", "--", path)
    now_unstaged, unstaged_removed = numstat("diff", "--numstat", "--", path)

    print(f"\nstaged:   {now_staged} added line(s)")
    print(f"unstaged: {now_unstaged} added line(s) still in the working tree")

    if staged_removed or unstaged_removed:
        raise SystemExit(
            "FAILED: the split reports deletions, which it must never "
            "produce. Run `git restore --staged` on the path and investigate."
        )
    if now_staged + now_unstaged != total_add:
        raise SystemExit(
            f"FAILED: {now_staged} + {now_unstaged} does not equal the "
            f"original {total_add}. Run `git restore --staged` on the path "
            "and investigate."
        )

    print(f"reconciled: {now_staged} + {now_unstaged} = {total_add}")
    print("\nReview `git diff --cached` before committing. Nothing was committed.")


if __name__ == "__main__":
    sys.exit(main())
