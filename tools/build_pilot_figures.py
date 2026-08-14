#!/usr/bin/env python3
"""Draw the two figures for the pilot AI workstation unit.

Why this exists
---------------
The pilot unit's argument turned structural on 2026-08-14: one machine
hosts two card eras in one PCIe slot, and the operating-system decision
falls out of where each card's stack is actually documented. Both of
those are relationships, and the project's rule is that a mechanism or
relationship gets a diagram rather than another paragraph. Two figures:

    fig_pilot_stacks     one machine, two card eras — the AMD-era stack
                         (Windows 11: Ollama native; WSL2: Docker ->
                         vLLM) and the Arc-era stack (native Ubuntu:
                         Xe KMD -> OMIX -> PyTorch XPU / vLLM container
                         / Ollama Vulkan) over the single shared slot.

    fig_pilot_os_matrix  where each card's stack is documented, per the
                         vendors' own pages — the evidence grid behind
                         the unit's OS conclusion, with the WSL2 hole
                         and the Ubuntu convergence visible at a glance.

Drawn with Pillow on the helpers, palette and Public Sans faces of
`build_server_guide_figures.py`, from which this imports — one set of
drawing conventions, not two copies drifting apart.

Brand marks
-----------
The stacks figure identifies real vendors' software, and at the
creator's 2026-08-14 direction it uses their real marks — monochrome,
because the house palette should not compete with eight brand colour
schemes. The SVGs live in `assets/figures/brand_icons/` (see its
README for source, licence and the takedown note); this script tints
them ink or paper at render time and rasterises through vl-convert,
the repo's standing SVG rasteriser. Identification, not endorsement,
and never redrawn by hand.

Requirements
------------
Python with Pillow, `vl-convert-python`, the Public Sans TTF faces
installed, `tools/build_server_guide_figures.py` beside this file, and
the brand-icon SVGs in `assets/figures/brand_icons/`. Writes PNGs into
assets/figures/ by default.

Usage
-----
    python tools/build_pilot_figures.py
    python tools/build_pilot_figures.py -o some/other/folder

Command-line only, per project_log.md Entry 049 — a build step runs
this, not a person at a window.
"""

import argparse
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_server_guide_figures as sg                     # noqa: E402

INK, EMBER, SAND = sg.INK, sg.EMBER, sg.SAND
PAPER, MIST, SAGE = sg.PAPER, sg.MIST, sg.SAGE
STONE, GRAPHITE = sg.STONE, sg.GRAPHITE

ICON_DIR = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "assets", "figures", "brand_icons")


def _find_inkscape():
    import shutil
    exe = shutil.which("inkscape")
    if exe:
        return exe
    for cand in (r"C:\Program Files\Inkscape\bin\inkscape.exe",
                 r"C:\Program Files (x86)\Inkscape\bin\inkscape.exe"):
        if os.path.exists(cand):
            return cand
    return None


def _rasterise(svg_text, px_device):
    """SVG text -> PNG bytes at px_device square.

    vl-convert first (the chart layer's rasteriser, no processes spawned);
    Inkscape second, discovered the way trace_reference.py does — the two
    machines this repo runs on each have one of them, not both.
    """
    try:
        import vl_convert as vlc
        return vlc.svg_to_png(svg_text, scale=px_device / 24.0)
    except ImportError:
        pass
    exe = _find_inkscape()
    if not exe:
        sys.exit("no SVG rasteriser: install vl-convert-python "
                 "(pip install vl-convert-python) or Inkscape 1.x")
    import subprocess
    import tempfile
    fd, svg_path = tempfile.mkstemp(suffix=".svg")
    png_path = svg_path[:-4] + ".png"
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(svg_text)
        subprocess.run([exe, svg_path, "--export-type=png",
                        "--export-filename=" + png_path,
                        "-w", str(px_device), "-h", str(px_device)],
                       check=True, capture_output=True)
        with open(png_path, "rb") as fh:
            return fh.read()
    finally:
        for p in (svg_path, png_path):
            if os.path.exists(p):
                os.unlink(p)


_ICON_CACHE = {}


def _icon(slug, px, colour=INK):
    """Rasterise one brand SVG at px logical pixels, tinted flat."""
    from PIL import Image
    key = (slug, px, colour)
    if key in _ICON_CACHE:
        return _ICON_CACHE[key]
    path = os.path.join(ICON_DIR, slug + ".svg")
    if not os.path.exists(path):
        sys.exit("brand icon missing: %s (see brand_icons/README.md)" % path)
    with open(path, encoding="utf-8") as fh:
        svg = fh.read()
    # simple-icons ship a single unfilled path; one fill on the root tints
    # the whole mark without touching the file on disk.
    svg = svg.replace("<svg ", '<svg fill="%s" ' % colour, 1)
    png = _rasterise(svg, px * sg.SCALE)
    _ICON_CACHE[key] = Image.open(io.BytesIO(png)).convert("RGBA")
    return _ICON_CACHE[key]


def _paste(img, slug, x, y, px, colour=INK):
    ic = _icon(slug, px, colour)
    img.paste(ic, (sg.s(x), sg.s(y)), ic)


# ---------------------------------------------------------------------------
# Figure 1 — one machine, two card eras
# ---------------------------------------------------------------------------
def fig_pilot_stacks(out_dir):
    img, d = sg.canvas(424)
    sg.text(d, 30, 20, "One machine, two card eras", "Bold", 18, INK)
    sg.text(d, 30, 46, "The pilot's software stacks as their vendors "
            "document them; one graphics slot means the cards take turns.",
            "Regular", 12.5, GRAPHITE)

    # --- era headers ---
    sg.box(d, 30, 76, 455, 42, SAND, radius=10)
    _paste(img, "amd", 44, 85, 24)
    sg.text(d, 76, 83, "Radeon RX 7900 XT", "Bold", 14, INK)
    sg.text(d, 76, 102, "20 GB — phases 1–2, in the machine now",
            "Regular", 10, STONE)

    sg.box(d, 515, 76, 455, 42, SAND, radius=10)
    _paste(img, "intel", 529, 85, 24)
    sg.text(d, 561, 83, "Arc Pro B70", "Bold", 14, INK)
    sg.text(d, 561, 102, "32 GB ECC — the Arc phase, after the swap",
            "Regular", 10, STONE)

    # --- AMD era: Windows 11 band ---
    sg.box(d, 30, 126, 455, 190, MIST, SAGE, radius=10)
    _paste(img, "windows", 46, 137, 16)
    sg.text(d, 70, 139, "WINDOWS 11", "Bold", 11, STONE)

    sg.box(d, 46, 166, 200, 58, PAPER, SAGE, radius=8)
    _paste(img, "ollama", 58, 176, 20)
    sg.text(d, 86, 173, "Ollama", "Bold", 12.5, INK)
    sg.text(d, 86, 191, "native Windows app", "Regular", 9.5, STONE)
    sg.text(d, 58, 207, "PHASE 1", "Medium", 9.5, EMBER)

    sg.box(d, 46, 232, 423, 72, PAPER, SAGE, radius=8)
    sg.text(d, 60, 240, "WSL2 — UBUNTU 24.04", "Bold", 10.5, STONE)
    sg.text(d, 455, 240, "PHASE 2", "Medium", 9.5, EMBER, anchor="ra")
    sg.box(d, 60, 260, 150, 34, MIST, SAGE, radius=6)
    _paste(img, "docker", 70, 268, 18)
    sg.text(d, 96, 264, "Docker", "Bold", 11.5, INK)
    sg.text(d, 96, 280, "Engine", "Regular", 9, STONE)
    sg.arrow(d, 214, 277, 240, 277, EMBER, 2, 7)
    sg.box(d, 244, 260, 211, 34, MIST, SAGE, radius=6)
    _paste(img, "vllm", 254, 269, 16)
    sg.text(d, 276, 264, "vLLM  (ROCm)", "Bold", 11.5, INK)
    sg.text(d, 276, 280, "OpenAI-compatible endpoint", "Regular", 9, STONE)

    # --- Arc era: native Ubuntu band ---
    sg.box(d, 515, 126, 455, 190, MIST, SAGE, radius=10)
    _paste(img, "ubuntu", 531, 137, 16)
    sg.text(d, 555, 139, "UBUNTU 26.04 LTS — NATIVE", "Bold", 11, STONE)
    sg.text(d, 955, 139, "dual-boot or outright: open", "Regular", 9.5,
            STONE, anchor="ra")

    sg.box(d, 531, 166, 423, 32, PAPER, SAGE, radius=8)
    sg.text(d, 545, 174, "Xe kernel driver — kernel 6.17 class, device E223",
            "Regular", 11.5, INK)
    sg.box(d, 531, 204, 423, 32, PAPER, SAGE, radius=8)
    # One point smaller than its sibling row: the full component list is
    # worth keeping and at 11.5 it touched the box border.
    sg.text(d, 545, 213, "OMIX — Intel's validated stack: Level Zero / "
            "OpenCL / SYCL", "Regular", 10.5, INK)

    sg.box(d, 531, 242, 131, 62, PAPER, SAGE, radius=8)
    _paste(img, "pytorch", 587, 250, 18)
    sg.text(d, 596, 272, "PyTorch", "Bold", 11, INK, anchor="ma")
    sg.text(d, 596, 288, "XPU", "Regular", 9, STONE, anchor="ma")

    sg.box(d, 677, 242, 131, 62, PAPER, SAGE, radius=8)
    _paste(img, "vllm", 733, 250, 18)
    sg.text(d, 742, 272, "vLLM", "Bold", 11, INK, anchor="ma")
    sg.text(d, 742, 288, "Intel container", "Regular", 9, STONE, anchor="ma")

    sg.box(d, 823, 242, 131, 62, PAPER, SAGE, radius=8)
    _paste(img, "ollama", 879, 250, 18)
    sg.text(d, 888, 272, "Ollama", "Bold", 11, INK, anchor="ma")
    sg.text(d, 888, 288, "Vulkan backend", "Regular", 9, STONE, anchor="ma")

    # --- the shared slot ---
    sg.box(d, 30, 330, 940, 52, INK, radius=10)
    sg.box(d, 46, 338, 140, 36, SAND, radius=8)
    sg.text(d, 116, 350, "RX 7900 XT", "Bold", 11, INK, anchor="ma")
    sg.box(d, 814, 338, 140, 36, SAND, radius=8)
    sg.text(d, 884, 350, "Arc Pro B70", "Bold", 11, INK, anchor="ma")
    sg.text(d, 500, 340, "MSI B650 GAMING PLUS WIFI — one PCIe 4.0 x16 "
            "slot, CPU-fed", "Medium", 12, PAPER, anchor="ma")
    sg.text(d, 500, 360, "one card installed at a time — the swap happens "
            "after Phase 2", "Regular", 10.5, SAGE, anchor="ma")

    sg.text(d, 30, 398, "Vendor documentation read 2026-08-13/14 — "
            "research_log.md Entries 080, 086–087. Monochrome marks via "
            "Simple Icons; trademarks belong to their owners.",
            "Regular", 9.5, STONE)
    return sg.save(img, out_dir, "fig_pilot_stacks.png")


# ---------------------------------------------------------------------------
# Figure 2 — where each card's stack is documented
# ---------------------------------------------------------------------------
def _cell(d, x, y, w, verdict, lines, v_colour=INK, fill=PAPER,
          outline=SAGE, owidth=2):
    sg.box(d, x, y, w, 88, fill, outline, radius=8, width=owidth)
    sg.text(d, x + 16, y + 10, verdict, "Bold", 12, v_colour)
    for i, ln in enumerate(lines):
        sg.text(d, x + 16, y + 30 + i * 15, ln, "Regular", 10, GRAPHITE)


def fig_pilot_os_matrix(out_dir):
    img, d = sg.canvas(470)
    sg.text(d, 30, 20, "Where each card's stack is documented", "Bold", 18,
            INK)
    sg.text(d, 30, 46, "Per the vendors' own pages: every Intel-validated "
            "route to the B70 runs on native Linux.", "Regular", 12.5,
            GRAPHITE)

    sg.box(d, 180, 80, 385, 40, INK, radius=8)
    _paste(img, "amd", 196, 90, 20, PAPER)
    sg.text(d, 226, 87, "Radeon RX 7900 XT", "Bold", 12.5, PAPER)
    sg.text(d, 226, 104, "20 GB — in the machine now", "Regular", 9, SAGE)

    sg.box(d, 595, 80, 375, 40, INK, radius=8)
    _paste(img, "intel", 611, 90, 20, PAPER)
    sg.text(d, 641, 87, "Arc Pro B70", "Bold", 12.5, PAPER)
    sg.text(d, 641, 104, "32 GB ECC — incoming", "Regular", 9, SAGE)

    rows = [("Windows 11", None), ("WSL2", None), ("Ubuntu", "(native)")]
    for i, (label, sub) in enumerate(rows):
        y = 128 + i * 98
        sg.box(d, 30, y, 140, 88, MIST, radius=8)
        if sub:
            sg.text(d, 100, y + 30, label, "Bold", 12, INK, anchor="ma")
            sg.text(d, 100, y + 48, sub, "Regular", 10, STONE, anchor="ma")
        else:
            sg.text(d, 100, y + 38, label, "Bold", 12, INK, anchor="ma")

    _cell(d, 180, 128, 385, "Documented",
          ["Ollama on Windows — ROCm v7 / HIP7-capable",
           "driver route; a Vulkan backend beside it."])
    _cell(d, 595, 128, 375, "Partial",
          ["PyTorch XPU validated on Windows 11; Ollama's",
           "Vulkan path. No OMIX, no Intel containers —",
           "no Phase 2 deployment shape."])

    _cell(d, 180, 226, 385, "Documented",
          ["AMD's ROCm 7.2.1 WSL matrix — RX 7900 XT on",
           "Ubuntu 24.04/22.04; PyTorch, ONNX and",
           "TensorFlow at production support."])
    _cell(d, 595, 226, 375, "Not documented",
          ["Absent from PyTorch's validated list, and",
           "Intel's IPEX documentation excluded B-series",
           "here. No vendor page places the card in WSL2."],
          v_colour=EMBER, fill=SAND, outline=EMBER)

    _cell(d, 180, 324, 385, "Not exercised here",
          ["The pilot's AMD phases run on Windows and",
           "WSL2 by design."], v_colour=STONE)
    _cell(d, 595, 324, 375, "Fully validated",
          ["OMIX packages; PyTorch XPU; Intel's PyTorch",
           "and vLLM containers. Ubuntu 26.04 is the host",
           "OS on Intel's own support matrix."],
          outline=EMBER, owidth=3)

    sg.text(d, 30, 428, "Sources, read directly 2026-08-13/14: Ollama GPU "
            "and Docker documentation; AMD ROCm compatibility matrices "
            "(Windows 6.4.4, WSL 7.2.1);", "Regular", 9.5, STONE)
    sg.text(d, 30, 442, "PyTorch Intel-GPU documentation; Intel dgpu-docs "
            "and the IPEX end-of-life page — research_log.md Entries 080, "
            "086–087.", "Regular", 9.5, STONE)
    return sg.save(img, out_dir, "fig_pilot_os_matrix.png")


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("-o", "--out", default=os.path.join("assets", "figures"))
    a = p.parse_args()
    os.makedirs(a.out, exist_ok=True)
    print("building pilot-unit figures")
    fig_pilot_stacks(a.out)
    fig_pilot_os_matrix(a.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
