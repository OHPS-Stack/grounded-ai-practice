#!/usr/bin/env python3
"""Render terminal replicas — realistic screenshots of a shell, drawn from data.

Why this exists
---------------
A guide that teaches command-line work has to show the learner what they
will actually see. A fenced code block shows what to *type*; it does not
show the window, the prompt, the colours, or what comes back. Someone who
has never opened a terminal cannot tell from a code block whether they
have succeeded.

Real screenshots would solve that and cannot be used: they would have to
be taken on the machine being built, before it is built, and they would
carry the real hostname, the real username and the real network.

So replicas are generated from structured data instead. The same input
that describes a command produces the picture of running it, which means
the picture cannot drift from the text, and a correction to the command
is a one-line change rather than a re-shoot.

Adapted from the PAWH replica system (transfer pack dated 2026-08-05).
That prototype rendered Windows PowerShell and CMD; this project's build
is Ubuntu, so the primary renderer here is GNOME Terminal. PowerShell is
kept because parts of the build genuinely happen on Windows — writing the
install USB, and connecting over SSH from the desktop.

Deliberate departures from the transfer pack, each with a reason
----------------------------------------------------------------
- **JSON input, not YAML.** The pack's example used YAML; PyYAML is not
  a dependency of this repo and every tool here that can be
  standard-library-only is. The pack's schema was already JSON Schema.

- **No File Explorer renderer.** The pack's own audit records that the
  manifest and schema describe one but the generator never implemented
  it. Claiming it here would repeat the defect the audit exists to flag.

- **Validation is hand-rolled**, not `jsonschema`, for the same
  dependency reason. It is strict about what it does check and says so
  when it rejects something.

Rules carried over unchanged, from the pack's rules extract
-----------------------------------------------------------
Generic paths and names only, never personal ones. Application chrome
stays faithful to the real application and is never restyled into GAP's
brand colours — the learner is being shown Ubuntu, not a GAP-themed
illustration of Ubuntu. No welcome banners, copyright text or scrollbars
unless the lesson genuinely needs them. Nothing inside the window except
prompt, command and output; explanation belongs in the prose around it.

Fidelity notes
--------------
Colours are Ubuntu's defaults: the aubergine terminal background, the
Tango palette, and bash's stock `PS1`, which renders `user@host` bright
green and the path bright blue, both bold. Window chrome is Yaru dark.

The font is a substitution and worth knowing about: Ubuntu ships Ubuntu
Mono, which is not present on a Windows machine, so Consolas is used.
Metrics differ slightly from a real Ubuntu terminal. Everything that
carries meaning — layout, colour, wrapping, alignment — is accurate.

Requirements
------------
Python with Pillow. No other dependencies.

Usage
-----
    python tools/replica.py shot.json -o assets/replicas/shot.png
    python tools/replica.py shot.json                 # infers output name
    python tools/replica.py --demo -o out/            # renders both demos
    python tools/replica.py --selftest                # smoke tests

Input format (JSON)
-------------------
    {
      "type": "ubuntu_terminal",
      "user": "yourname",
      "host": "gap-server",
      "cwd": "~",
      "cols": 84,
      "blocks": [
        {"command": "lsblk", "output": ["NAME   SIZE TYPE", "sda   1.8T disk"]},
        {"command": "sudo mount -a", "output": [], "password": true}
      ]
    }

`type` is `ubuntu_terminal` or `powershell`. For `powershell`, use `cwd`
as the full path and omit `user`/`host`. A block may set `"password":
true` to show the one-off sudo password prompt above its output, and
`"error": true` to render its output in the palette's red.

Command-line only, per project_log.md Entry 049.
"""

import argparse
import json
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Pillow is required: pip install pillow")

SCALE = 2

# ---------------------------------------------------------------------------
# Ubuntu / GNOME Terminal, Yaru dark. Tango palette, as Ubuntu ships it.
# ---------------------------------------------------------------------------
UBUNTU = {
    "bg": "#300A24",            # the aubergine
    "header": "#303030",
    "header_line": "#1F1F1F",
    "title": "#DEDEDE",
    "btn": "#3D3D3D",
    "btn_glyph": "#DEDEDE",
    "text": "#EEEEEC",          # Tango white
    "muted": "#B4B0AB",
    "green": "#8AE234",         # bold green — user@host
    "blue": "#729FCF",          # bold blue — path
    "red": "#EF2929",
    "yellow": "#FCE94F",
    "cursor": "#EEEEEC",
}

# ---------------------------------------------------------------------------
# Windows Terminal / PowerShell, dark. Kept faithful to Windows 11 chrome.
# ---------------------------------------------------------------------------
PWSH = {
    "bg": "#0C0C0C",
    "header": "#2B2B2B",
    "header_line": "#1A1A1A",
    "title": "#E6E6E6",
    "btn": "#2B2B2B",
    "btn_glyph": "#E6E6E6",
    "text": "#E6E6E6",
    "muted": "#B9B9B9",
    "green": "#16C60C",
    "blue": "#3B78FF",
    "red": "#E74856",
    "yellow": "#F5E66D",        # command text, as the prototype had it
    "cursor": "#E6E6E6",
}

MONO_CANDIDATES = [
    "C:/Windows/Fonts/consola.ttf",
    "/usr/share/fonts/truetype/ubuntu/UbuntuMono-R.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
]
MONO_BOLD_CANDIDATES = [
    "C:/Windows/Fonts/consolab.ttf",
    "/usr/share/fonts/truetype/ubuntu/UbuntuMono-B.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
]
UI_CANDIDATES = [
    "C:/Windows/Fonts/segoeui.ttf",
    "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]

FONT_PX = 15          # logical
LINE_H = 21           # logical
PAD_X = 14
PAD_TOP = 12
HEADER_H = 40


def _load(candidates, size):
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def fonts():
    return (_load(MONO_CANDIDATES, FONT_PX * SCALE),
            _load(MONO_BOLD_CANDIDATES, FONT_PX * SCALE),
            _load(UI_CANDIDATES, int(13.5 * SCALE)))


def s(v):
    return int(v * SCALE)


# ---------------------------------------------------------------------------
# Validation — strict about what it checks, explicit when it refuses
# ---------------------------------------------------------------------------
VALID_TYPES = ("ubuntu_terminal", "powershell")


def validate(spec, where="input"):
    """Raise ValueError with a usable message, or return the spec."""
    if not isinstance(spec, dict):
        raise ValueError("%s: top level must be a JSON object" % where)

    t = spec.get("type")
    if t not in VALID_TYPES:
        raise ValueError(
            "%s: \"type\" must be one of %s (got %r). File Explorer is not "
            "implemented — see this tool's docstring." % (
                where, ", ".join(VALID_TYPES), t))

    blocks = spec.get("blocks")
    if not isinstance(blocks, list) or not blocks:
        raise ValueError("%s: \"blocks\" must be a non-empty array" % where)

    for i, b in enumerate(blocks):
        at = "%s: blocks[%d]" % (where, i)
        if not isinstance(b, dict):
            raise ValueError("%s must be an object" % at)
        if "command" not in b:
            raise ValueError("%s has no \"command\"" % at)
        if not isinstance(b["command"], str):
            raise ValueError("%s: \"command\" must be a string" % at)
        out = b.get("output", [])
        if not isinstance(out, list) or any(not isinstance(x, str)
                                            for x in out):
            raise ValueError("%s: \"output\" must be an array of strings" % at)

    cols = spec.get("cols", 84)
    if not isinstance(cols, int) or not (20 <= cols <= 200):
        raise ValueError("%s: \"cols\" must be an integer 20-200" % where)

    # Privacy guard. The pack's rules require generic names; this catches the
    # obvious slip of pasting a real home directory in.
    blob = json.dumps(spec).lower()
    for marker in ("c:\\users\\thinkpad", "/home/thinkpad"):
        if marker in blob:
            raise ValueError(
                "%s: looks like a real user path (%r). Replicas use generic "
                "names — see the rules in this tool's docstring." %
                (where, marker))
    return spec


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
def wrap(line, cols):
    """Wrap the way a terminal does — hard at the column count, no words."""
    if len(line) <= cols:
        return [line]
    return [line[i:i + cols] for i in range(0, len(line), cols)] or [""]


def build_lines(spec):
    """Flatten the spec into (segments, ...) rows ready to draw.

    A row is a list of (text, colour_key, bold) segments.
    """
    kind = spec["type"]
    cols = spec.get("cols", 84)
    rows = []

    if kind == "ubuntu_terminal":
        user = spec.get("user", "yourname")
        host = spec.get("host", "gap-server")
        cwd = spec.get("cwd", "~")

        def prompt_segments():
            return [("%s@%s" % (user, host), "green", True),
                    (":", "text", False),
                    (cwd, "blue", True),
                    ("$ ", "text", False)]
        prompt_len = len("%s@%s:%s$ " % (user, host, cwd))
    else:
        cwd = spec.get("cwd", "C:\\Users\\YourName")

        def prompt_segments():
            return [("PS %s> " % cwd, "text", False)]
        prompt_len = len("PS %s> " % cwd)

    for b in spec["blocks"]:
        cmd_colour = "text" if kind == "ubuntu_terminal" else "yellow"
        # The command shares the prompt's row; wrap it against what is left.
        avail = max(10, cols - prompt_len)
        parts = wrap(b["command"], avail)
        rows.append(prompt_segments() + [(parts[0], cmd_colour, False)])
        for extra in parts[1:]:
            rows.append([(" " * prompt_len, "text", False),
                         (extra, cmd_colour, False)])

        if b.get("password"):
            rows.append([("[sudo] password for %s: " %
                          spec.get("user", "yourname"), "text", False)])

        colour = "red" if b.get("error") else "text"
        for line in b.get("output", []):
            for piece in wrap(line, cols):
                rows.append([(piece, colour, False)])
        rows.append([])  # blank line between blocks

    if rows and not rows[-1]:
        rows.pop()

    # A returned prompt means the command finished and you are back where you
    # started. That is wrong for anything that hands the session somewhere
    # else \u2014 `ssh` being the obvious case, where showing the local prompt
    # again would teach the opposite of what happened. Set
    # "trailing_prompt": false for those.
    if spec.get("trailing_prompt", True):
        rows.append([])
        rows.append(prompt_segments() + [("\u2588", "cursor", False)])
    return rows


def render(spec, out_path):
    validate(spec)
    palette = UBUNTU if spec["type"] == "ubuntu_terminal" else PWSH
    mono, mono_b, ui = fonts()
    rows = build_lines(spec)
    cols = spec.get("cols", 84)

    char_w = mono.getlength("M")
    width = int(char_w * cols) + s(PAD_X) * 2
    height = s(HEADER_H) + s(PAD_TOP) + int(len(rows) * s(LINE_H)) + s(PAD_TOP)

    img = Image.new("RGB", (width, height), palette["bg"])
    d = ImageDraw.Draw(img)

    # header
    d.rectangle([0, 0, width, s(HEADER_H)], fill=palette["header"])
    d.line([0, s(HEADER_H), width, s(HEADER_H)], fill=palette["header_line"],
           width=max(1, SCALE // 2))

    if spec["type"] == "ubuntu_terminal":
        title = spec.get("title", "%s@%s: %s" % (spec.get("user", "yourname"),
                                                 spec.get("host", "gap-server"),
                                                 spec.get("cwd", "~")))
    else:
        title = spec.get("title", "Windows PowerShell")
    d.text((width // 2, s(HEADER_H) // 2), title, font=ui,
           fill=palette["title"], anchor="mm")

    # window controls, right-aligned
    if spec["type"] == "ubuntu_terminal":
        r = s(11)
        cx = width - s(24)
        for glyph in ("\u00d7", "\u25a1", "\u2212"):
            d.ellipse([cx - r, s(HEADER_H) // 2 - r,
                       cx + r, s(HEADER_H) // 2 + r], fill=palette["btn"])
            d.text((cx, s(HEADER_H) // 2), glyph, font=ui,
                   fill=palette["btn_glyph"], anchor="mm")
            cx -= s(30)
    else:
        # Segoe UI has no U+2715; it renders as tofu. U+00D7 is present and
        # is what the real title bar looks like at this size anyway.
        cx = width - s(26)
        for glyph in ("\u00d7", "\u25a1", "\u2212"):
            d.text((cx, s(HEADER_H) // 2), glyph, font=ui,
                   fill=palette["btn_glyph"], anchor="mm")
            cx -= s(34)

    # Body, drawn on a fixed character grid.
    #
    # Drawing whole strings and letting the font advance would be simpler and
    # is wrong: box-drawing characters (lsblk's tree, systemctl's status) do
    # not advance exactly one cell in Consolas, so any column after one of
    # them lands slightly off and the output stops looking like real terminal
    # output. A terminal is a grid; placing every character at its own cell
    # reproduces that exactly, whatever the font does.
    y = s(HEADER_H) + s(PAD_TOP)
    for row in rows:
        col = 0
        for text, key, bold in row:
            f = mono_b if bold else mono
            for ch in text:
                if ch != " ":
                    d.text((s(PAD_X) + col * char_w, y), ch, font=f,
                           fill=palette[key])
                col += 1
        y += s(LINE_H)

    os.makedirs(os.path.dirname(os.path.abspath(out_path)) or ".",
                exist_ok=True)
    img.save(out_path, "PNG")
    return img.size


# ---------------------------------------------------------------------------
# Demos and self-test
# ---------------------------------------------------------------------------
DEMO_UBUNTU = {
    "type": "ubuntu_terminal", "user": "yourname", "host": "gap-server",
    "cwd": "~", "cols": 78,
    "blocks": [
        {"command": "lsblk -o NAME,SIZE,TYPE,MOUNTPOINTS", "output": [
            "NAME        SIZE TYPE MOUNTPOINTS",
            "sda       465.8G disk ",
            "\u2514\u2500sda1    465.8G part /mnt/backup",
            "sdb         1.8T disk ",
            "\u2514\u2500sdb1      1.8T part /mnt/media",
            "nvme0n1   465.8G disk ",
            "\u251c\u2500nvme0n1p1   1G part /boot/efi",
            "\u2514\u2500nvme0n1p2 464.8G part /",
        ]},
    ],
}

DEMO_PWSH = {
    "type": "powershell", "cwd": "C:\\Users\\YourName", "cols": 74,
    "blocks": [
        {"command": "ssh yourname@gap-server", "output": [
            "Welcome to Ubuntu 24.04.3 LTS (GNU/Linux 6.8.0-51-generic x86_64)",
        ]},
    ],
}


def selftest():
    """Smoke tests. Exercises validation, wrapping and both renderers."""
    import tempfile
    failures = []
    ran = [0]

    def check(name, fn):
        ran[0] += 1
        try:
            fn()
        except AssertionError as e:
            failures.append("%s: %s" % (name, e))
        except Exception as e:
            failures.append("%s: unexpected %s: %s" % (name, type(e).__name__, e))

    def bad(spec, fragment):
        try:
            validate(spec)
        except ValueError as e:
            assert fragment in str(e), "expected %r in %r" % (fragment, str(e))
            return
        raise AssertionError("should have been rejected: %r" % spec)

    check("rejects unknown type",
          lambda: bad({"type": "file_explorer_full", "blocks": [{"command": "x"}]},
                      "not implemented"))
    check("rejects empty blocks",
          lambda: bad({"type": "ubuntu_terminal", "blocks": []}, "non-empty"))
    check("rejects missing command",
          lambda: bad({"type": "ubuntu_terminal", "blocks": [{"output": []}]},
                      "no \"command\""))
    check("rejects non-string output",
          lambda: bad({"type": "ubuntu_terminal",
                       "blocks": [{"command": "x", "output": [1]}]},
                      "array of strings"))
    check("rejects a real user path",
          lambda: bad({"type": "ubuntu_terminal", "cwd": "/home/thinkpad",
                       "blocks": [{"command": "x"}]}, "generic names"))
    check("rejects out-of-range cols",
          lambda: bad({"type": "ubuntu_terminal", "cols": 500,
                       "blocks": [{"command": "x"}]}, "20-200"))

    def wrapping():
        assert wrap("x" * 25, 10) == ["x" * 10, "x" * 10, "x" * 5]
        assert wrap("short", 10) == ["short"]
        assert wrap("", 10) == [""]

    check("wraps hard at the column count", wrapping)

    def render_both():
        with tempfile.TemporaryDirectory() as td:
            a = render(DEMO_UBUNTU, os.path.join(td, "u.png"))
            b = render(DEMO_PWSH, os.path.join(td, "p.png"))
            assert a[0] > 200 and a[1] > 200, "ubuntu render too small: %s" % (a,)
            assert b[0] > 200 and b[1] > 200, "pwsh render too small: %s" % (b,)

    check("renders both types", render_both)

    def deterministic():
        with tempfile.TemporaryDirectory() as td:
            p1 = os.path.join(td, "1.png")
            p2 = os.path.join(td, "2.png")
            render(DEMO_UBUNTU, p1)
            render(DEMO_UBUNTU, p2)
            assert open(p1, "rb").read() == open(p2, "rb").read(), \
                "same input produced different bytes"

    check("is deterministic", deterministic)

    for f in failures:
        print("FAIL  %s" % f)
    print("%d passed, %d failed" % (ran[0] - len(failures), len(failures)))
    return 1 if failures else 0


def main():
    ap = argparse.ArgumentParser(
        description="Render a terminal replica from a JSON description.")
    ap.add_argument("input", nargs="?", help="JSON spec file")
    ap.add_argument("-o", "--output", help="destination .png, or a folder")
    ap.add_argument("--demo", action="store_true",
                    help="render the built-in demos instead of an input file")
    ap.add_argument("--selftest", action="store_true", help="run smoke tests")
    args = ap.parse_args()

    if args.selftest:
        sys.exit(selftest())

    if args.demo:
        dest = args.output or "."
        os.makedirs(dest, exist_ok=True)
        for name, spec in (("demo_ubuntu_terminal", DEMO_UBUNTU),
                           ("demo_powershell", DEMO_PWSH)):
            p = os.path.join(dest, name + ".png")
            size = render(spec, p)
            print("wrote %s  (%d x %d)" % (p, *size))
        return

    if not args.input:
        ap.error("give an input .json, or --demo, or --selftest")

    with open(args.input, encoding="utf-8") as fh:
        try:
            spec = json.load(fh)
        except json.JSONDecodeError as e:
            sys.exit("%s is not valid JSON: %s" % (args.input, e))

    out = args.output
    if not out:
        out = os.path.splitext(args.input)[0] + ".png"
    elif os.path.isdir(out):
        out = os.path.join(
            out, os.path.splitext(os.path.basename(args.input))[0] + ".png")

    try:
        size = render(spec, out)
    except ValueError as e:
        sys.exit(str(e))
    print("wrote %s  (%d x %d)" % (out, *size))


if __name__ == "__main__":
    main()
