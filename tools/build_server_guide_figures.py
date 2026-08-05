#!/usr/bin/env python3
"""Draw the figures for the home server build documents.

Why this exists
---------------
The build documents explain four things that are genuinely spatial and read
badly as prose: which drive does what and what backs up what, how remote
access works without opening a port, where the display and audio signals
go, and what order the work happens in. It also makes one numeric
comparison — the running cost of leaving this machine on against a mini PC
doing the server half — that is a chart rather than a sentence.

Everything is drawn here rather than hand-produced so the figures can be
regenerated when the guide changes. The numbers behind the cost chart are
in COST_DATA below, in the file, per CLAUDE.md's rule that data-driven
figures come from a script with the data visible rather than from
hand-drawn values.

Why Pillow and not the usual route
----------------------------------
CLAUDE.md's normal path for a repo asset is a raster concept traced to SVG
with tools/trace_reference.py and refined in Inkscape. That rule is about
*concept artwork*, where Claude cannot see what it draws. These are
mechanical diagrams — boxes, arrows and labels on a computed grid, with no
curve work in them — so there is nothing for a vector editor to refine.
Inkscape is also not installed on every machine this repo runs on, and
Pillow already is, because tools/fitshapes.py depends on it.

Figures are drawn at SCALE times their final size and placed at the text
column width, so they stay sharp in print rather than rendering at screen
resolution. Public Sans is loaded from the real installed faces, so the
figures match the document body.

Requirements
------------
Python with Pillow, and the Public Sans TTF faces installed. Writes PNGs
into assets/figures/ by default.

Usage
-----
    python tools/build_server_guide_figures.py
    python tools/build_server_guide_figures.py -o some/other/folder

Command-line only, per project_log.md Entry 049 — a build step runs this,
not a person at a window.
"""

import argparse
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Pillow is required: pip install pillow")

# Palette — project_brief.md, "Visual identity"
INK = "#27221E"
EMBER = "#F15E4B"
SAND = "#F9E8DC"
PAPER = "#FFFFFF"
MIST = "#EFEEED"
SAGE = "#D5E2E1"
STONE = "#6E6E6E"
GRAPHITE = "#404040"

SCALE = 3           # oversample factor
W = 1000            # logical width; final PNG is W * SCALE

# A figure is placed at the text column width, 6.77in. One logical unit is
# therefore about 0.0068in, so a size-13 label would set at roughly 6pt on
# the page — below the point where small print stays comfortable. Type is
# scaled up against the boxes rather than the boxes being redrawn; the
# layouts were built with enough padding to absorb it.
FONT_BOOST = 1.32

# The one piece of data in these figures. Watts at idle, and the UK unit
# price used to turn that into a yearly figure.
COST_DATA = {
    "unit_price_p_per_kwh": 27.0,   # p/kWh, typical UK domestic rate
    "bars": [
        ("This build\n(5600X + GTX 1060)", 60, 80),
        ("Mini PC\n(server roles only)", 6, 10),
    ],
}

FONT_DIRS = [
    os.path.join(os.environ.get("LOCALAPPDATA", ""),
                 r"Microsoft\Windows\Fonts"),
    r"C:\Windows\Fonts",
    "/usr/share/fonts/truetype/public-sans",
    os.path.expanduser("~/.fonts"),
]


def font(weight="Regular", size=16):
    name = "PublicSans-%s.ttf" % weight
    for d in FONT_DIRS:
        p = os.path.join(d, name)
        if d and os.path.exists(p):
            return ImageFont.truetype(p, int(size * FONT_BOOST * SCALE))
    sys.exit("Public Sans not found (looked for %s). Install the family, or "
             "see CLAUDE.md \"Word document conventions\"." % name)


def canvas(height):
    img = Image.new("RGB", (W * SCALE, height * SCALE), PAPER)
    return img, ImageDraw.Draw(img)


def s(v):
    return int(v * SCALE)


def box(d, x, y, w, h, fill, outline=None, radius=8, width=2):
    d.rounded_rectangle([s(x), s(y), s(x + w), s(y + h)], radius=s(radius),
                        fill=fill, outline=outline,
                        width=s(width) if outline else 0)


def text(d, x, y, txt, weight="Regular", size=16, fill=INK, anchor="la",
         spacing=1.35):
    f = font(weight, size)
    d.multiline_text((s(x), s(y)), txt, font=f, fill=fill, anchor=anchor,
                     spacing=int(size * FONT_BOOST * SCALE * (spacing - 1)),
                     align={
                         "la": "left", "ma": "center", "ra": "right",
                         "lm": "left", "mm": "center", "rm": "right"}[anchor])


def arrow(d, x1, y1, x2, y2, colour=EMBER, width=3, head=9, dashed=False):
    if dashed:
        # Manual dashes: Pillow has no dash support.
        import math
        total = math.hypot(x2 - x1, y2 - y1)
        step, on = 14, 8
        n = max(1, int(total // step))
        for i in range(n + 1):
            t0 = min(1.0, (i * step) / total)
            t1 = min(1.0, (i * step + on) / total)
            d.line([s(x1 + (x2 - x1) * t0), s(y1 + (y2 - y1) * t0),
                    s(x1 + (x2 - x1) * t1), s(y1 + (y2 - y1) * t1)],
                   fill=colour, width=s(width))
    else:
        d.line([s(x1), s(y1), s(x2), s(y2)], fill=colour, width=s(width))
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    for sign in (1, -1):
        a = ang + sign * 2.6
        d.line([s(x2), s(y2),
                s(x2 + head * math.cos(a)), s(y2 + head * math.sin(a))],
               fill=colour, width=s(width))


def save(img, out_dir, name):
    path = os.path.join(out_dir, name)
    img.save(path, "PNG")
    print("  %s  (%d x %d)" % (name, img.width, img.height))
    return path


# ---------------------------------------------------------------------------
# Figure 1 — the storage plan
# ---------------------------------------------------------------------------
def fig_storage(out_dir):
    img, d = canvas(370)

    box(d, 30, 55, 640, 285, MIST, SAGE, radius=12)
    text(d, 46, 68, "INSIDE THE MACHINE", "Bold", 11, STONE)

    cards = [
        (52, 95, "500 GB M.2 SSD", "OS, Docker, service\nconfigs, website files",
         INK, PAPER),
        (52, 218, "2 TB HDD", "Media library and\nnetwork shares",
         INK, PAPER),
        (382, 95, "Second HDD", "Nightly backup target",
         INK, PAPER),
    ]
    for x, y, title, body, fg, bg in cards:
        box(d, x, y, 266, 105, bg, SAGE, radius=8)
        text(d, x + 16, y + 16, title, "Bold", 15, fg)
        text(d, x + 16, y + 44, body, "Regular", 13, STONE)

    # Only the SSD is copied nightly. The cron job covers /home and /opt; it
    # does not touch /srv/media, and the figure must not imply otherwise.
    arrow(d, 322, 147, 376, 147)
    text(d, 349, 124, "rsync", "Medium", 11, EMBER, anchor="ma")
    text(d, 382, 218, "Covers /home and /opt,", "Medium", 13, INK)
    text(d, 382, 240, "at 03:00 and 04:00.", "Medium", 13, INK)
    text(d, 382, 268, "The media library is not in\nthe nightly job — it is large,\n"
                      "and mostly re-obtainable.", "Regular", 12, STONE)

    # cold spare, deliberately outside the box
    box(d, 715, 95, 255, 105, SAND, EMBER, radius=8)
    text(d, 731, 111, "Third HDD", "Bold", 15, INK)
    text(d, 731, 139, "Cold spare — stays\nout of the machine", "Regular", 13,
         GRAPHITE)
    text(d, 715, 222, "Not powered, not written to,\nand therefore not exposed\n"
                      "to a PSU failure or a\nmistyped mkfs.", "Regular", 12,
         STONE)

    text(d, 30, 22, "Four drives, three jobs, one of them unplugged",
         "Bold", 18, INK)
    return save(img, out_dir, "fig_storage_plan.png")


# ---------------------------------------------------------------------------
# Figure 2 — remote access without open ports
# ---------------------------------------------------------------------------
def fig_remote(out_dir):
    img, d = canvas(470)
    text(d, 30, 22, "Why nothing needs an open port", "Bold", 18, INK)

    # home
    box(d, 30, 70, 380, 330, MIST, SAGE, radius=12)
    text(d, 46, 84, "YOUR HOME NETWORK", "Bold", 11, STONE)
    box(d, 55, 115, 330, 90, PAPER, SAGE)
    text(d, 71, 131, "The server", "Bold", 15, INK)
    text(d, 71, 158, "Ubuntu · Docker · Jellyfin\nCaddy · Samba", "Regular", 13,
         STONE)
    box(d, 55, 230, 330, 60, PAPER, SAGE)
    text(d, 71, 248, "Router", "Bold", 14, INK)
    text(d, 71, 268, "No port forwarding configured", "Regular", 12, STONE)
    box(d, 55, 315, 330, 65, SAND, EMBER)
    text(d, 71, 331, "ufw", "Bold", 14, INK)
    text(d, 71, 351, "Allows the LAN, blocks the rest", "Regular", 12, GRAPHITE)

    # outbound connections
    arrow(d, 415, 160, 560, 160)
    text(d, 487, 133, "outbound only", "Medium", 11, EMBER, anchor="ma")
    arrow(d, 415, 265, 560, 265)
    text(d, 487, 238, "outbound only", "Medium", 11, EMBER, anchor="ma")

    box(d, 565, 120, 405, 85, INK, radius=8)
    text(d, 585, 138, "Tailscale", "Bold", 15, PAPER)
    text(d, 585, 163, "Encrypted private network. Your laptop\nand phone join it too.",
         "Regular", 12, SAGE)

    box(d, 565, 225, 405, 85, INK, radius=8)
    text(d, 585, 243, "Cloudflare Tunnel", "Bold", 15, PAPER)
    text(d, 585, 268, "Cloudflare serves the website to\nvisitors on the server's behalf.",
         "Regular", 12, SAGE)

    # blocked inbound
    box(d, 565, 330, 405, 105, MIST, STONE, radius=8)
    text(d, 585, 348, "Unsolicited inbound traffic", "Bold", 13, STONE)
    text(d, 585, 375, "Automated SSH login attempts,\nport scans — nothing to arrive at.",
         "Regular", 12, STONE)
    arrow(d, 560, 382, 425, 382, colour=STONE, dashed=True)
    # cross on the blocked path
    cx, cy = 492, 382
    for a, b in (((-9, -9), (9, 9)), ((-9, 9), (9, -9))):
        d.line([s(cx + a[0]), s(cy + a[1]), s(cx + b[0]), s(cy + b[1])],
               fill=EMBER, width=s(4))
    return save(img, out_dir, "fig_remote_access.png")


# ---------------------------------------------------------------------------
# Figure 3 — display and audio chain
# ---------------------------------------------------------------------------
def fig_chain(out_dir):
    img, d = canvas(275)
    text(d, 30, 22, "Where picture and sound actually go", "Bold", 18, INK)

    nodes = [
        (30, 80, 250, "The server", "GTX 1060 HDMI out\n(the only video output)"),
        (375, 80, 250, "AV receiver", "Takes the audio,\npasses video through"),
        (720, 80, 250, "Projector", "Picture only"),
    ]
    for x, y, w, title, body in nodes:
        box(d, x, y, w, 95, PAPER, SAGE)
        text(d, x + 16, y + 16, title, "Bold", 15, INK)
        text(d, x + 16, y + 44, body, "Regular", 12, STONE)

    arrow(d, 285, 127, 370, 127)
    text(d, 327, 100, "HDMI", "Medium", 11, EMBER, anchor="ma")
    arrow(d, 630, 127, 715, 127)
    text(d, 672, 100, "HDMI", "Medium", 11, EMBER, anchor="ma")

    box(d, 375, 205, 250, 55, SAND, EMBER)
    text(d, 391, 221, "Speakers", "Bold", 14, INK)
    arrow(d, 500, 180, 500, 200)

    text(d, 720, 195, "The motherboard's video ports\nare dead — this CPU has no\n"
                      "integrated graphics.", "Regular", 12, STONE)
    return save(img, out_dir, "fig_display_audio_chain.png")


# ---------------------------------------------------------------------------
# Figure 4 — running cost
# ---------------------------------------------------------------------------
def fig_cost(out_dir):
    img, d = canvas(400)
    price = COST_DATA["unit_price_p_per_kwh"]

    def gbp(watts):
        return watts * 24 * 365 / 1000.0 * price / 100.0

    text(d, 30, 22, "What leaving it on costs, per year", "Bold", 18, INK)
    text(d, 30, 48, "Idle draw \u00d7 8,760 hours at %.0fp/kWh. Bars show the "
                    "low\u2013high range." % price, "Regular", 12, STONE)

    base_y, max_h, x0 = 300, 165, 90
    top = max(gbp(hi) for _, _, hi in COST_DATA["bars"])
    axis_right = 600

    # axis
    d.line([s(x0 - 30), s(base_y), s(axis_right), s(base_y)], fill=SAGE,
           width=s(2))
    for frac in (0.25, 0.5, 0.75, 1.0):
        y = base_y - max_h * frac
        d.line([s(x0 - 30), s(y), s(axis_right), s(y)], fill=MIST, width=s(1))
        text(d, x0 - 40, y - 7, "\u00a3%d" % (top * frac), "Regular", 11, STONE,
             anchor="ra")

    for i, (label, lo, hi) in enumerate(COST_DATA["bars"]):
        x = x0 + i * 250
        lo_gbp, hi_gbp = gbp(lo), gbp(hi)
        h_hi = max_h * hi_gbp / top
        h_lo = max_h * lo_gbp / top
        # full range in Sand, the low end solid in Ember
        box(d, x, base_y - h_hi, 160, h_hi, SAND, EMBER, radius=4, width=2)
        box(d, x, base_y - h_lo, 160, h_lo, EMBER, radius=4)
        text(d, x + 80, base_y - h_hi - 32,
             "\u00a3%.0f \u2013 \u00a3%.0f" % (lo_gbp, hi_gbp), "Bold", 15, INK,
             anchor="ma")
        text(d, x + 80, base_y + 14, label, "Medium", 13, INK, anchor="ma")
        text(d, x + 80, base_y + 58, "%d\u2013%d W idle" % (lo, hi),
             "Regular", 12, STONE, anchor="ma")

    text(d, 665, 118, "The difference is roughly\n\u00a3%d a year."
         % (gbp(70) - gbp(8)), "Bold", 15, INK)
    text(d, 665, 170, "What it buys is one machine\ninstead of two, with the GPU\n"
                      "the projector needs already\nin it. Worth knowing, not\n"
                      "necessarily worth acting on.", "Regular", 12, STONE)
    return save(img, out_dir, "fig_running_cost.png")


# ---------------------------------------------------------------------------
# Figure 5 — order of operations
# ---------------------------------------------------------------------------
def fig_order(out_dir):
    img, d = canvas(390)
    text(d, 30, 22, "Two or three evenings, in this order", "Bold", 18, INK)

    cols = [
        ("Evening one", ["Make the Ubuntu USB",
                         "Fit drives, set BIOS",
                         "Install Ubuntu + Nvidia driver",
                         "Start SMART long tests,\nleave overnight"]),
        ("Evening two", ["Read SMART results",
                         "Format and mount",
                         "SSH, keys, Tailscale, ufw",
                         "Cockpit"]),
        ("Evening three", ["Docker and Jellyfin",
                           "Samba shares",
                           "Kodi against the projector",
                           "No-sleep, WoL, backups"]),
    ]
    for i, (title, steps) in enumerate(cols):
        x = 30 + i * 320
        box(d, x, 68, 290, 30, INK, radius=6)
        text(d, x + 145, 76, title, "Bold", 13, PAPER, anchor="ma")
        y = 118
        for stp in steps:
            lines = stp.count("\n") + 1
            h = 32 + (lines - 1) * 18
            box(d, x, y, 290, h, MIST, SAGE, radius=6)
            text(d, x + 14, y + 8, stp, "Regular", 12, INK)
            y += h + 10
        if i < 2:
            arrow(d, x + 297, 190, x + 315, 190)

    text(d, 30, 320, "The SMART tests are the reason this is three evenings "
                     "rather than one — they run for hours,\nand nothing "
                     "downstream should start before they finish.",
         "Regular", 12, STONE)
    return save(img, out_dir, "fig_order_of_operations.png")


def main():
    ap = argparse.ArgumentParser(
        description="Draw the home server guide's figures.")
    ap.add_argument("-o", "--output", default="assets/figures",
                    help="destination folder (default: assets/figures)")
    args = ap.parse_args()
    os.makedirs(args.output, exist_ok=True)
    print("writing figures to %s/" % args.output)
    for fn in (fig_storage, fig_remote, fig_chain, fig_cost, fig_order):
        fn(args.output)


if __name__ == "__main__":
    main()
