#!/usr/bin/env python3
"""Keep the landing site's terminal replica verbatim-true to the tool it pictures.

Why this exists
---------------
The replica pictures `tools/build_site_figures.py` running — the
practice made visible, contrast audit and all. The replica system's rule
is that a picture of a command must not drift from the command, and this
one is especially exposed: every figure change alters the build output
the image displays. Keeping the spec synced by hand failed quickly (a
shell-mangled backslash once put an invisible control character into the
pictured command), so the sync is a tool, not a procedure.

**The landing page does not currently show this replica** — it was
tried in the system section and removed, because a contrast-audit
window asked the reader to do technical work in the middle of an
argument about small firms. The asset is kept for a learning-unit page,
where a picture of a real shell session earns its place, and this tool
keeps it true in the meantime. It writes only into `assets/replicas/`;
restoring the site copy means copying the PNG into `docs/` again.

How it works
------------
Runs the real figure build, captures its stdout verbatim, writes those
lines into `assets/replicas/site_figures_build.json`, renders the PNG
through `tools/replica.py`, and copies it into `docs/assets/replicas/`.
The pictured command stays `python tools\\build_site_figures.py --og`
with the generic `C:\\gap` working directory, per the replica pack's
generic-names rule.

`--check` compares a fresh capture against the stored spec and exits
nonzero on drift without writing anything — run it before a commit that
touches the figure script.

Run after every change to `tools/build_site_figures.py` or its data.
Command-line by the Entry 049 decision (a build step, not a
learner-facing tool). Requires Python with Pillow (for the render step).

Usage
-----
    python tools/build_site_replica.py           # resync spec and render
    python tools/build_site_replica.py --check   # verify only, no writes
"""

import argparse
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC = os.path.join(ROOT, "assets", "replicas", "site_figures_build.json")
PNG = os.path.join(ROOT, "assets", "replicas", "site_figures_build.png")


def capture():
    run = subprocess.run(
        [sys.executable, os.path.join("tools", "build_site_figures.py"),
         "--og"],
        capture_output=True, text=True, cwd=ROOT)
    if run.returncode != 0:
        sys.exit("figure build failed; not touching the replica:\n"
                 + run.stderr)
    return run.stdout.strip().splitlines()


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="verify the stored spec matches a fresh run")
    args = ap.parse_args()

    lines = capture()
    bad = [ln for ln in lines if any(ord(ch) < 32 for ch in ln)]
    if bad:
        sys.exit("control characters in captured output; refusing")

    if args.check:
        with open(SPEC, encoding="utf-8") as fh:
            stored = json.load(fh)["blocks"][0]["output"]
        if stored == lines:
            print("replica spec matches the live build output")
            return
        sys.exit("replica spec has drifted from the live build output — "
                 "run tools/build_site_replica.py to resync")

    spec = {
        "type": "powershell",
        "cwd": "C:\\gap",
        "cols": max(76, max(map(len, lines)) + 2),
        "blocks": [{
            "command": "python tools\\build_site_figures.py --og",
            "output": lines,
        }],
    }
    with open(SPEC, "w", encoding="utf-8") as fh:
        json.dump(spec, fh, indent=2)
        fh.write("\n")

    render = subprocess.run(
        [sys.executable, os.path.join("tools", "replica.py"),
         os.path.relpath(SPEC, ROOT), "-o", os.path.relpath(PNG, ROOT)],
        cwd=ROOT)
    if render.returncode != 0:
        sys.exit("replica render failed")

    from PIL import Image
    size = Image.open(PNG).size
    print(f"replica resynced: {len(lines)} verbatim lines, {size[0]}x{size[1]}")


if __name__ == "__main__":
    main()
