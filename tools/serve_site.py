#!/usr/bin/env python3
"""Serve docs/ for local preview with browser caching disabled.

Plain ``python -m http.server`` leaves browser heuristic caching in
play: after a stylesheet edit, the page can arrive fresh while
styles.css is served from the browser's cache, and the preview then
renders a mix of new HTML and old CSS. Found 2026-08-06, when a rebuilt
page kept rendering with the previous stylesheet and the theme override
appeared broken when it was not. A preview that can silently show stale
output fails the project's self-verification standard, which is the
reason this wrapper exists.

It is http.server with one change: every response carries
``Cache-Control: no-cache``, so the browser revalidates each file
against the working tree on every load. Binds to 127.0.0.1 only —
nothing on the network can reach it.

Usage:
    python tools/serve_site.py [port]

Port defaults to 8330, matching .claude/launch.json, which runs this
script for the in-app preview. Serves the repository's docs/ folder
regardless of the working directory it is started from. Standard
library only. Command-line by the project_log.md Entry 049 decision — a
dev-server wrapper, not a learner-facing tool.
"""

import functools
import http.server
import sys
from pathlib import Path


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    # Quieter logs: one line per request, no per-header noise.
    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


def main() -> int:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8330
    docs = Path(__file__).resolve().parent.parent / "docs"
    if not docs.is_dir():
        print(f"docs/ not found at {docs}", file=sys.stderr)
        return 2
    handler = functools.partial(NoCacheHandler, directory=str(docs))
    with http.server.ThreadingHTTPServer(("127.0.0.1", port), handler) as srv:
        print(f"serving {docs} at http://localhost:{port} (Cache-Control: no-cache)")
        srv.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
