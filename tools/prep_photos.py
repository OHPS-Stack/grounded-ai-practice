#!/usr/bin/env python3
r"""Prepare phone photos for AI upload: convert, rename, optionally shrink.

Why this exists
---------------
Phone photos reach the desktop as IMG_4232.HEIC or PXL_20260801_093015.jpg —
names that say nothing, in formats desktop tools handle unevenly (HEIC in
particular needs codec packs Windows does not ship). This is the step
between transfer and use: however the photos left the phone (cloud folder,
AirDrop, cable), this turns the pile into files ready to hand to Claude or
any other tool — converted to PNG or JPEG, named <date>_<label>_<NN>.<ext>
so a batch reads chronologically, and optionally shrunk to the size an AI
model actually consumes. Originals are never modified, moved or deleted.

Input formats: HEIC/HEIF (iPhone; needs pillow-heif), JPEG (the Android
default), PNG (screenshots), WebP, TIFF, BMP, GIF, AVIF. RAW/DNG (iPhone
ProRAW, Samsung Expert RAW) is out of scope — that needs a raw developer,
not a format conversion. Live Photo .mov companions and video are ignored.

The window
----------
Run with no arguments (or --gui) and a window opens instead of the command
line: pick photos or a folder, name them, choose which AI they are going
to, preview, convert. It drives exactly the same functions as the command
line — the window exists so the tool is reachable without a terminal, not
as a different tool — and it exposes only the decisions a person actually
makes; every finer control below stays command-line on purpose.

Each of the five sections carries a "?" button explaining what that
section does and why it matters, in plain language rather than flag
names. Those panels are Toplevels rather than messagebox.showinfo, which
plays the system alert sound - wrong for a button that reports nothing
wrong. The saving is drawn as a headline figure with the money beside it,
because the reduction is the reason to use the tool at all, and a drawn
progress bar reports a run in place of a scrolling log.

It opens dark and carries a light/dark toggle in the header, whose band
uses the reversed wordmark - white letterforms on the dark ground. The
Ink wordmark would need a pale plate behind it, and a plate on a dark
band reads as a boxed image dropped onto the header rather than as the
identity. tools/embed_logo.py generates both faces.

Nothing in either panel is positioned by a hard-coded pixel: every item
is placed from the measured extent of the one before it, because
coordinates tuned by eye at one display scale overlap at another - which
happened three times before the rule was applied properly. A 7pt label
renders 19px tall on a DPI-aware Windows process, so guessed pitches of
10px and then 15px both collided; asking Tk is the only reliable answer.
The saving is shown as a stacked before/after pair rather than one track,
because a single bar with a caption sitting in its empty half reads as a
progress bar that has stalled.

Sizing for the model, not for the disk
--------------------------------------
This is what separates the tool from a general image compressor. Claude
sees an image as a grid of 28x28-pixel patches, and each patch costs one
visual token. Every model enforces two limits at once: a longest-edge
limit, and a budget of visual tokens. An image over EITHER is downscaled
server-side before the model ever sees it, so pixels past that point are
upload weight, latency and nothing else.

    Standard tier (below Claude 4.7)   1568 px long edge, 1568 tokens
    High-resolution (Claude 4.7+)      2576 px long edge, 4784 tokens

The token budget is the one that usually binds, and capping the long edge
does not satisfy it. A 4:3 phone photo capped at 1568 px is 1568x1176,
which costs 56 x 42 = 2352 tokens against a budget of 1568, so it is
downscaled again on arrival — to 1270x952. An earlier version of this tool
did exactly that, and shipped a third more pixels than any model kept.

So --model resizes to the largest size that model actually accepts,
computed with Anthropic's published reference algorithm rather than by
capping an edge. --selftest asserts that maths against the worked examples
in their documentation, because a wrongly sized file looks perfectly fine
and fails silently. Every count the tool prints is the real cost of the
file it wrote: --dry-run prices a batch before anything is written.

Other providers
---------------
--model also takes `openai` and `gemini`, because the same argument holds
wherever you send an image, and the numbers differ enough to matter:

    claude-standard  28 px patches, 1568 px / 1568 tokens
    claude-high      28 px patches, 2576 px / 4784 tokens
    openai           32 px patches x1.2, 2500-patch budget at high detail
    gemini           768 px tiles at 258 tokens, or 258 flat under 384 px

**Only the Claude figures are exact.** Anthropic publish their resizing
algorithm and this tool runs a port of it, checked against their own worked
examples. The OpenAI and Gemini numbers are computed from published
formulas and are close estimates — the self-test checks them against the
worked examples those vendors give, which is as far as arithmetic can go
without an API key. Gemini documents no hard dimension cap, so nothing is
resized for it and the tool says so rather than inventing a limit.

With --model none the tool resizes nothing and prints what the batch would
cost on each provider, which is the cheapest way to see the difference.

When it will not write
----------------------
Windows ransomware protection (Controlled Folder Access) guards Documents,
Pictures and Desktop, and blocks programs it does not recognise. It
reports a blocked write as **"[Errno 2] No such file or directory"** — a
message that sends you looking for a missing file when the real problem is
a security setting. The tool checks every destination folder before
converting anything and explains that specific case, because otherwise one
blocked folder produces one identical, misleading failure per photo, which
is exactly what it did. The remedy is to save elsewhere, or to allow
Python through in Windows Security; the tool never changes that setting.
diagnose() covers the other likely failures — a file open in another
program, a full disk, a truncated image, a source that moved since the
scan, a path too long for Windows.

Presets and limits
------------------
--ai      JPEG at quality 85. The everyday case, for photographs.
--text    PNG (lossless, so small writing survives) — for documents,
          whiteboards and screenshots. Anthropic's own guidance warns that
          heavy JPEG compression makes text hard to read, which is the
          whole reason this preset is not just --ai.

Each of --format, --model, --max-edge and --quality overrides its preset.
The tool also warns where a batch meets a published limit: 20 images per
message on claude.ai (100 per API request), the stricter 2000 px per-image
rule that applies to API requests holding more than 20 images, and the
10 MB per-image ceiling.

Metadata, and what it is really for
-----------------------------------
--metadata safe (the default) drops GPS location, camera owner and body
serial from the copies, and keeps the capture time. Note precisely why:
Anthropic documents that Claude is not given an image's metadata at all,
so this is not about what the model reads. It is that the file itself
carries those tags onward — to the service's storage, to whoever the
folder is shared with next, to a different vendor entirely. --metadata
keep restores the old carry-everything behaviour, --metadata strip drops
the lot. Originals are never altered either way, and the tool reports how
many of them record a location.

Deleting the originals
----------------------
--delete-originals sends each original to the Recycle Bin, and only after
its copy has been written, re-opened and verified: a file whose conversion
failed is always kept, and a failed batch cannot cost anyone their photos.
It never runs under --dry-run, and the window asks before doing it. There
is deliberately no permanent-delete option — the whole safety case rests
on the deletion being undoable, so where no Recycle Bin is available the
tool refuses rather than falling back to an unlink.

How it works
------------
1. Dates each file from EXIF DateTimeOriginal (the capture time), falling
   back to EXIF DateTime, then to the file's modified time — and marks
   which files used the weakest fallback, since a copied file's modified
   time can be long after the photo was taken.

2. Numbers files per date in capture order, and never overwrites: a name
   already on disk advances the sequence, so re-running over a folder
   after a fresh import is safe. Files already named by this tool are
   skipped when a folder is scanned, so its own output is never
   re-converted — pass such a file explicitly to reprocess it.

3. Bakes EXIF orientation into the pixels, because viewers do not reliably
   honour rotation metadata in PNG/JPEG, and carries the surviving EXIF
   into the output under the --metadata policy above. For JPEG output,
   transparency is flattened onto white.

4. Re-opens every file it writes as an integrity self-check — which is
   also the precondition for deleting anything.

5. Optionally writes a numbered manifest (--manifest) to paste alongside
   the images. Anthropic's guidance asks for images to be introduced as
   "Image 1:", "Image 2:" so a prompt can refer back to them; without it
   the model has the pictures and no way to tell which is which.

Requires Python with Pillow. pillow-heif (pip install pillow-heif) is
needed only when HEIC/HEIF files are among the inputs; every other format
works with Pillow alone. The window needs tkinter, which ships with
Python on Windows. Note that Claude accepts JPEG, PNG, GIF and WebP only —
HEIC, TIFF, BMP and AVIF have to be converted, which is this tool's job.

Limits and figures are vendor documentation read 2026-08-29:
platform.claude.com/docs/en/build-with-claude/vision and
.../vision-coordinates; developers.openai.com/api/docs/guides/images-vision;
ai.google.dev/gemini-api/docs/image-understanding. They move; re-read them
before trusting the numbers, and re-run --selftest after any change.

Dates, and why the filenames are not what they show
---------------------------------------------------
Dates shown to a person are DD/MM/YYYY. Filenames cannot contain "/", so
--date-format uk (the default) writes 29-08-2026, which reads the way UK
dates are written. **That order does not sort chronologically in a file
browser**, which the year-first form does, so --date-format iso is there
for anyone who wants a folder that sorts itself. The manifest is always
ordered by capture time regardless, since the ordering is its whole job.

What it costs
-------------
--currency turns the token counts into money (GBP by default, also USD
and EUR) using each vendor's published input-token price. Two honesty
notes carried into the output itself: the figure is quoted at one named
model per provider, since a tier holds several at different prices and a
named price can be checked where an average cannot; and the exchange
rates are dated on screen, because they move daily. --fx and --price
replace either number.

Usage
-----
    python tools/prep_photos.py                    # no arguments: the window
    python tools/prep_photos.py C:\imports --label whiteboard --ai
    python tools/prep_photos.py C:\scans --label contract --text --manifest
    python tools/prep_photos.py C:\imports --ai --model openai
    python tools/prep_photos.py C:\imports --model none --dry-run  # compare
    python tools/prep_photos.py C:\imports --ai --delete-originals
    python tools/prep_photos.py IMG_4232.HEIC shot.webp -o C:\out
    python tools/prep_photos.py C:\imports --ai --currency USD
    python tools/prep_photos.py C:\imports --ai --date-format iso
    python tools/prep_photos.py --selftest         # check the sizing maths
"""

import argparse
import os
import queue
import re
import sys
import threading
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageOps, features
from PIL import UnidentifiedImageError

try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
    HEIF_OK = True
except ImportError:
    HEIF_OK = False

try:
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk
    TK_OK = True
except ImportError:  # rare stripped-down Python; the CLI still works
    TK_OK = False

HEIF_EXTS = {".heic", ".heif"}
PIL_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".bmp", ".gif",
            ".avif"}
INPUT_EXTS = HEIF_EXTS | PIL_EXTS
AI_QUALITY = 85

# Claude's vision limits, from platform.claude.com/docs/en/build-with-claude/
# vision and .../vision-coordinates, read 2026-08-29. A tier is
# (max_edge_px, max_visual_tokens); an image over EITHER limit is downscaled
# server-side, and for ordinary photos it is the token budget that binds.
PATCH = 28               # Claude sees the image as 28x28-pixel patches
TIERS = {"standard": (1568, 1568),   # every model below Claude 4.7
         "high": (2576, 4784)}       # Claude 4.7 and later
DEFAULT_TIER = "standard"
CLAUDE_AI_PER_MESSAGE = 20   # images per message on claude.ai
MANY_IMAGE_EDGE = 2000       # per-image edge cap once a request holds >20
MAX_UPLOAD_MB = 10           # per image, claude.ai and the API direct

OPENAI_PATCH = 32        # developers.openai.com/api/docs/guides/images-vision
OPENAI_MULTIPLIER = 1.2  # current GPT-5.x families bill 1.2x the patch count
OPENAI_BUDGET = 2500     # patch budget at "high" detail on budgeted models
GEMINI_TILE_TOKENS = 258     # ai.google.dev/gemini-api/docs/image-understanding
GEMINI_SMALL_EDGE = 384      # both sides at or under this: one flat charge
GEMINI_CROP_DIVISOR = 1.5    # crop unit is the short side over 1.5


def _claude_count(w, h):
    return -(-w // PATCH) * -(-h // PATCH)


def _openai_count(w, h):
    patches = -(-w // OPENAI_PATCH) * -(-h // OPENAI_PATCH)
    return round(patches * OPENAI_MULTIPLIER)


def _ceil(value):
    """Ceiling of a float, without dragging in math for three call sites."""
    whole = int(value)
    return whole if whole == value else whole + 1


def _gemini_count(w, h):
    """Gemini charges 258 tokens a tile, or 258 flat for a small image."""
    if w <= GEMINI_SMALL_EDGE and h <= GEMINI_SMALL_EDGE:
        return GEMINI_TILE_TOKENS
    crop = max(min(w, h) / GEMINI_CROP_DIVISOR, 1)
    return _ceil(w / crop) * _ceil(h / crop) * GEMINI_TILE_TOKENS


def _openai_fit(w, h):
    """Largest aspect-preserving size inside OpenAI's high-detail budget."""
    return _budget_fit(w, h, OPENAI_PATCH, OPENAI_BUDGET)


def _budget_fit(w, h, patch, budget):
    if -(-w // patch) * -(-h // patch) <= budget:
        return w, h
    if h > w:
        tall_h, tall_w = _budget_fit(h, w, patch, budget)
        return tall_w, tall_h
    aspect = w / h
    lo, hi = 1, w
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        short = max(round(mid / aspect), 1)
        if -(-mid // patch) * -(-short // patch) <= budget:
            lo = mid
        else:
            hi = mid
    return lo, max(round(lo / aspect), 1)


# The models the tool can size for. `fit` returns the size the provider will
# actually keep, or None where the provider documents no hard limit and
# resizing is the user's own tradeoff rather than a rule. `exact` marks the
# one provider whose own reference algorithm is published and ported here;
# the others are computed from published formulas and are good estimates.
MODELS = {
    "claude-standard": {
        "label": "Claude - Sonnet 4.5, Haiku 4.5 and earlier",
        "short": "Claude (standard)",
        "count": _claude_count,
        "fit": lambda w, h: fit_to_tier(w, h, *TIERS["standard"]),
        "formats": ("JPEG", "PNG", "GIF", "WebP"),
        "per_message": CLAUDE_AI_PER_MESSAGE,
        "max_mb": MAX_UPLOAD_MB,
        "exact": True,
        "note": "1568 px longest edge, 1568 visual tokens",
    },
    "claude-high": {
        "label": "Claude - Opus 5, Sonnet 5 and 4.7 (high resolution)",
        "short": "Claude (high resolution)",
        "count": _claude_count,
        "fit": lambda w, h: fit_to_tier(w, h, *TIERS["high"]),
        "formats": ("JPEG", "PNG", "GIF", "WebP"),
        "per_message": CLAUDE_AI_PER_MESSAGE,
        "max_mb": MAX_UPLOAD_MB,
        "exact": True,
        "note": "2576 px longest edge, 4784 visual tokens",
    },
    "openai": {
        "label": "ChatGPT / OpenAI - GPT-5 family",
        "short": "ChatGPT",
        "count": _openai_count,
        "fit": _openai_fit,
        "formats": ("JPEG", "PNG", "GIF", "WebP"),
        "per_message": None,
        "max_mb": None,
        "exact": False,
        "note": "32 px patches, 2500-patch budget at high detail",
    },
    "gemini": {
        "label": "Google Gemini",
        "short": "Gemini",
        "count": _gemini_count,
        "fit": None,          # no hard cap documented: resizing is a choice
        "formats": ("JPEG", "PNG", "WebP", "HEIC", "HEIF"),
        "per_message": None,
        "max_mb": None,
        "exact": False,
        "note": "768 px tiles at 258 tokens each",
    },
}
# Input-token prices, USD per million, from each vendor's own pricing page
# read 2026-08-29. A tier holds several models at different prices, so each
# entry names the one model its figure is for: a reader can check a named
# price and cannot check an averaged one. Override with --price.
#   Claude   platform.claude.com/docs/en/about-claude/pricing
#   OpenAI   developers.openai.com/api/docs/pricing
#   Gemini   ai.google.dev/gemini-api/docs/pricing
PRICES = {
    "claude-standard": (3.00, "Sonnet 4.5"),
    "claude-high": (5.00, "Opus 5"),
    "openai": (5.00, "GPT-5.6 Sol"),
    "gemini": (0.75, "Gemini 3.7 Flash"),
}

# Rates recorded 2026-08-28; they move daily, so the tool dates them wherever
# it shows money and --fx replaces the number. USD is the base because every
# vendor publishes in it.
FX_DATE = "28/08/2026"
CURRENCIES = {
    "GBP": ("£", 0.7321),
    "USD": ("$", 1.0),
    "EUR": ("€", 0.8620),
}
DEFAULT_CURRENCY = "GBP"


def money(tokens, model, currency=DEFAULT_CURRENCY, rate=None, price=None):
    """What `tokens` input tokens cost, as a rendered string, or None.

    Deliberately returns a string with its own precision: at these prices a
    batch of photos costs fractions of a penny, and a figure rounded to two
    decimal places would read "£0.00" and teach the reader nothing.
    """
    if not model or model not in PRICES:
        return None
    per_mtok = price if price is not None else PRICES[model][0]
    symbol, default_rate = CURRENCIES.get(currency, ("", 1.0))
    amount = (tokens / 1_000_000) * per_mtok * (default_rate if rate is None
                                                else rate)
    if amount >= 1:
        return f"{symbol}{amount:,.2f}"
    if amount >= 0.01:
        return f"{symbol}{amount:.2f}"
    if amount >= 0.0001:
        return f"{symbol}{amount:.4f}"
    return f"under {symbol}0.0001"


def priced_as(model):
    """The model name a cost figure is quoted at, for showing beside it."""
    return PRICES[model][1] if model in PRICES else ""

DEFAULT_MODEL = "claude-high"
TIER_ALIAS = {"standard": "claude-standard", "high": "claude-high"}

# Either date order counts as this tool's own output, so a folder prepared
# under one setting is still skipped after the setting changes.
OWN_OUTPUT = re.compile(
    r"(\d{4}-\d{2}-\d{2}|\d{2}-\d{2}-\d{4})_[a-z0-9_]+_\d{2,}\.(png|jpg)",
    re.IGNORECASE)
# Filenames cannot contain "/", so the day-first setting uses hyphens. It
# reads the way UK dates are written; the ISO setting sorts chronologically
# in a file browser, which day-first cannot.
DATE_FORMATS = {"uk": "%d-%m-%Y", "iso": "%Y-%m-%d"}
DEFAULT_DATE_FORMAT = "uk"
DISPLAY_DATE = "%d/%m/%Y"        # dates shown to a person, never in a name
EXIF_IFD = 0x8769          # pointer to the EXIF sub-IFD, where capture time lives
DATETIME_ORIGINAL = 36867  # capture time (sub-IFD)
DATETIME = 306             # file-level timestamp (IFD0)
GPS_IFD = 0x8825           # pointer to the GPS IFD: where the photo was taken
# Tags naming a person or a specific camera body, dropped by --metadata safe.
IDENTIFYING_IFD0 = (315, 0x8298)             # Artist, Copyright
IDENTIFYING_SUB = (0xA430, 0xA431, 0xA435)   # owner name, body serial, lens serial
HEIF_INSTALL_MSG = (
    "HEIC/HEIF files are present but pillow-heif is not installed.\n"
    "Install it with:  pip install pillow-heif\n"
    "(plain pip install; the wheel bundles libheif, no Windows codec packs)")

# GAP palette (project_brief.md, "Visual identity") — used per the roles
# recorded there; only EMBER_DEEP is derived (Ember darkened for hover)
INK = "#27221E"         # primary text
EMBER = "#F15E4B"       # primary accent: the one action that matters
EMBER_DEEP = "#D94C3B"
PAPER = "#F9F9F9"       # main background
MIST = "#EFEEED"        # secondary background: neutral buttons, borders
SAND = "#F9E8DC"        # warm tint: hover and selections
STONE = "#6E6E6E"       # neutral grey: hints and secondary text

# Two palettes over the one brand. Dark is the default at the creator's
# direction: the light scheme leaned on Sand for section heads and read as a
# wash of pale peach across the whole window. Sand is now a selection tint
# only, which is the role project_brief.md gives it.
THEMES = {
    "dark": {"ground": "#1B1815", "card": "#262220", "head": "#332D29",
             "text": "#F4F1EE", "muted": "#9E958D", "line": "#3B3430",
             "field": "#151211", "btn": "#3A3430", "btn_active": "#4A423C",
             "track": "#151211", "select": "#4A3A34", "band": "#131110",
             "band_text": "#FFFFFF", "band_muted": "#9E958D"},
    "light": {"ground": PAPER, "card": "#FFFFFF", "head": MIST,
              "text": INK, "muted": STONE, "line": "#E4E1DE",
              "field": "#FFFFFF", "btn": MIST, "btn_active": SAND,
              "track": "#FFFFFF", "select": SAND, "band": INK,
              "band_text": "#FFFFFF", "band_muted": "#B9B2AC"},
}
DEFAULT_THEME = "dark"



def snake_case(text):
    text = re.sub(r"[\s\-]+", "_", text.strip().lower())
    text = re.sub(r"[^a-z0-9_]", "", text)
    return re.sub(r"_{2,}", "_", text).strip("_") or "img"


def count_tokens(width, height):
    """Visual tokens an image costs Claude: one per 28x28 patch."""
    return -(-width // PATCH) * -(-height // PATCH)


def fit_to_tier(width, height, max_edge, max_tokens):
    """The size Claude would downscale this image to, or it unchanged.

    A direct port of Anthropic's published reference implementation (see the
    module docstring). Both limits matter and the token budget is usually the
    binding one, so this cannot be replaced by capping the long edge.
    """
    def fits(w, h):
        return (-(-w // PATCH) * PATCH <= max_edge
                and -(-h // PATCH) * PATCH <= max_edge
                and count_tokens(w, h) <= max_tokens)

    if fits(width, height):
        return width, height
    if height > width:                       # solve landscape, then swap back
        tall_h, tall_w = fit_to_tier(height, width, max_edge, max_tokens)
        return tall_w, tall_h
    aspect = width / height
    lo, hi = 1, width                        # lo always fits; hi never does
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if fits(mid, max(round(mid / aspect), 1)):
            lo = mid
        else:
            hi = mid
    return lo, max(round(lo / aspect), 1)


def target_size(width, height, model, max_edge=None):
    """Final pixel size for one image: the manual cap first, then the model."""
    if max_edge and max(width, height) > max_edge:
        scale = max_edge / max(width, height)
        width = max(round(width * scale), 1)
        height = max(round(height * scale), 1)
    fit = MODELS[model]["fit"] if model else None
    if fit:
        width, height = fit(width, height)
    return width, height


def token_cost(width, height, model):
    """Tokens this size costs on one model, or None if no model is chosen."""
    return MODELS[model]["count"](width, height) if model else None


def diagnose(exc, src=None, dest=None):
    """Turn an exception into a sentence someone can act on.

    Every branch here is a failure mode seen or reproduced on this machine,
    not a guess at what might go wrong. The first is the reason this
    function exists: Windows ransomware protection reports a blocked write
    as "no such file or directory", so the honest error is actively
    misleading and the tool has to translate it.
    """
    folder = Path(dest).parent if dest else None
    if isinstance(exc, FileNotFoundError):
        if folder and folder.is_dir():
            return ("Windows ransomware protection is blocking writes to "
                    "this folder.\n\nSave the copies somewhere else, or "
                    "allow Python through Controlled folder access in "
                    "Windows Security.")
        if src and not Path(src).exists():
            return "the original has moved or been deleted since the scan"
        if folder:
            return f"the folder {folder} does not exist"
    if isinstance(exc, PermissionError):
        return ("the file is open in another program, or is marked "
                "read-only")
    if isinstance(exc, OSError) and getattr(exc, "errno", None) == 28:
        return "the disk is full"
    if isinstance(exc, OSError) and "truncated" in str(exc).lower():
        return "the image is damaged or was only partly copied"
    if isinstance(exc, UnidentifiedImageError):
        return "this is not an image the tool can read, whatever its name says"
    if isinstance(exc, MemoryError):
        return "the image is too large to fit in memory"
    if dest and len(str(Path(dest).resolve())) > 255:
        return ("the full path is too long for Windows; save into a folder "
                "nearer the top of the drive")
    return str(exc)


def writable(folder):
    """None if files can be written to `folder`, else why they cannot.

    Run before converting anything: without it a blocked folder produces
    one identical cryptic failure per photo, which is what it did.
    """
    folder = Path(folder)
    if not folder.exists():
        try:
            folder.mkdir(parents=True, exist_ok=True)
        except Exception as exc:
            return diagnose(exc, dest=folder / "x")
    probe = folder / f".gap_write_probe_{os.getpid()}"
    try:
        probe.write_bytes(b"")
        probe.unlink()
        return None
    except Exception as exc:
        try:
            probe.unlink()
        except OSError:
            pass
        return diagnose(exc, dest=probe)


def resolve_settings(ai=False, text=False, fmt=None, max_edge=None,
                     quality=None, model=..., metadata=None):
    """Fill unset options from a preset or the plain defaults.

    Returns (fmt, max_edge, quality, ext, model, metadata). --text wins over
    --ai where they disagree; an explicit flag wins over both.
    """
    if fmt is None:
        fmt = "png" if text or not ai else "jpg"
    if model is ...:
        model = DEFAULT_MODEL if (ai or text) else None
    if quality is None:
        quality = AI_QUALITY
    if metadata is None:
        metadata = "safe"
    return fmt, max_edge, quality, (".jpg" if fmt == "jpg" else ".png"), \
        model, metadata


def inspect(src):
    """One open per file: capture time, pixel size, and what EXIF discloses.

    Returns (datetime, "exif" | "mtime", (width, height), has_location).
    """
    with Image.open(src) as im:
        exif = im.getexif()
        stamp = exif.get_ifd(EXIF_IFD).get(DATETIME_ORIGINAL) or exif.get(DATETIME)
        size = im.size
        if exif.get(274) in (5, 6, 7, 8):  # orientation: the transpose swaps them
            size = (size[1], size[0])
        located = bool(exif.get_ifd(GPS_IFD))
    when = None
    if stamp:
        try:
            when = datetime.strptime(str(stamp).strip(), "%Y:%m:%d %H:%M:%S")
        except ValueError:
            pass  # malformed stamp: fall through to mtime
    if when:
        return when, "exif", size, located
    return datetime.fromtimestamp(src.stat().st_mtime), "mtime", size, located


def clean_exif(exif, metadata):
    """Apply the --metadata policy, returning EXIF bytes or None.

    "keep" carries everything across; "safe" drops where the photo was taken
    and who owns the camera, keeping the capture time; "strip" carries none.
    """
    if metadata == "strip" or not exif:
        return None
    if metadata == "safe":
        for tag in (GPS_IFD,) + IDENTIFYING_IFD0:
            exif.pop(tag, None)
        sub = exif.get_ifd(EXIF_IFD)
        for tag in IDENTIFYING_SUB:
            sub.pop(tag, None)
    try:
        return exif.tobytes()
    except Exception:
        return None  # malformed source EXIF: better to drop it than to fail


def recycle(path):
    """Send one file to the Recycle Bin. Raises if that cannot be done.

    Deliberately never falls back to unlink(): the whole safety case for
    deleting originals at all is that the deletion is undoable.
    """
    if sys.platform == "win32":
        import ctypes
        from ctypes import wintypes

        class SHFILEOPSTRUCTW(ctypes.Structure):
            _fields_ = [("hwnd", wintypes.HWND),
                        ("wFunc", wintypes.UINT),
                        ("pFrom", wintypes.LPCWSTR),
                        ("pTo", wintypes.LPCWSTR),
                        ("fFlags", ctypes.c_uint16),
                        ("fAnyOperationsAborted", wintypes.BOOL),
                        ("hNameMappings", wintypes.LPVOID),
                        ("lpszProgressTitle", wintypes.LPCWSTR)]

        FO_DELETE, FOF_ALLOWUNDO, FOF_NOCONFIRMATION, FOF_SILENT = 3, 0x40, 0x10, 0x4
        op = SHFILEOPSTRUCTW(
            None, FO_DELETE, str(Path(path).resolve()) + "\0\0", None,
            FOF_ALLOWUNDO | FOF_NOCONFIRMATION | FOF_SILENT, False, None, None)
        result = ctypes.windll.shell32.SHFileOperationW(ctypes.byref(op))
        if result != 0 or op.fAnyOperationsAborted:
            raise OSError(f"the Recycle Bin refused it (code {result})")
        return
    try:
        from send2trash import send2trash
    except ImportError:
        raise OSError("no Recycle Bin available on this platform without "
                      "send2trash (pip install send2trash)")
    send2trash(str(path))


def collect(sources, recurse):
    """Gather input files; folder scans skip this tool's own output."""
    files, skipped = [], 0
    for name in sources:
        path = Path(name)
        if path.is_dir():
            walk = path.rglob("*") if recurse else path.iterdir()
            for p in walk:
                if not p.is_file() or p.suffix.lower() not in INPUT_EXTS:
                    continue
                if OWN_OUTPUT.fullmatch(p.name):
                    skipped += 1
                    continue
                files.append(p)
        elif path.is_file() and path.suffix.lower() in INPUT_EXTS:
            files.append(path)  # explicit args bypass the own-output skip
        elif path.is_file():
            print(f"ignoring {path.name}: not a supported image format",
                  file=sys.stderr)
        else:
            sys.exit(f"not found: {path}")
    unique, seen = [], set()
    for p in files:
        key = str(p.resolve()).lower()
        if key not in seen:
            seen.add(key)
            unique.append(p)
    return unique, skipped


def analyse(files, model=None, max_edge=None, resize=True):
    """Read each file's capture time, size and disclosures.

    Also works out the size and token cost each output will have, so a dry
    run can report the whole bill without writing anything.
    """
    records, failures = [], []
    for src in files:
        try:
            when, origin, size, located = inspect(src)
        except Exception as exc:
            failures.append((src, f"unreadable: {exc}"))
            continue
        out = target_size(*size, model if resize else None, max_edge)
        records.append({"src": src, "when": when, "origin": origin,
                        "size": size, "located": located, "out_size": out,
                        "tokens": token_cost(*out, model) or 0})
    return records, failures


def plan_names(records, label, ext, outdir, date_format=DEFAULT_DATE_FORMAT):
    """Assign each record a destination, never claiming a taken name."""
    by_date = defaultdict(list)
    for rec in records:
        by_date[rec["when"].date()].append(rec)
    claimed = set()  # lowercased: NTFS will not distinguish two casings
    # Grouped and sorted by the real date, never by the formatted string:
    # day-first text does not sort chronologically.
    for day in sorted(by_date):
        date_str = day.strftime(DATE_FORMATS[date_format])
        batch = sorted(by_date[day],
                       key=lambda r: (r["when"], r["src"].name.lower()))
        width = max(2, len(str(len(batch))))
        seq = 1
        for rec in batch:
            folder = outdir or rec["src"].parent
            while True:
                dest = folder / f"{date_str}_{label}_{seq:0{width}d}{ext}"
                seq += 1
                key = str(dest).lower()
                if key not in claimed and not dest.exists():
                    break
            claimed.add(key)
            rec["dest"] = dest


def convert(src, dest, fmt, max_edge, quality, model=None, metadata="safe"):
    """Write one prepared copy. Returns its (width, height)."""
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im)
        exif = im.getexif()  # orientation already applied and removed
        target = target_size(*im.size, model, max_edge)
        if target != im.size:
            im = im.resize(target, Image.Resampling.LANCZOS)
        has_alpha = im.mode in ("RGBA", "LA") or (
            im.mode == "P" and "transparency" in im.info)
        if fmt == "jpg":
            if has_alpha:
                im = im.convert("RGBA")
                flat = Image.new("RGB", im.size, (255, 255, 255))
                flat.paste(im, mask=im.getchannel("A"))
                im = flat
            elif im.mode != "RGB":
                im = im.convert("RGB")
        elif im.mode not in ("RGB", "RGBA", "L", "LA"):
            im = im.convert("RGBA" if has_alpha else "RGB")
        params = {"optimize": True}
        carried = clean_exif(exif, metadata)
        if carried:
            params["exif"] = carried
        if fmt == "jpg":
            params["quality"] = quality
        im.save(dest, format="JPEG" if fmt == "jpg" else "PNG", **params)
        written = im.size
    with Image.open(dest) as check:
        check.verify()
    return written


def savings(records, model):
    """(before, after, percent_saved) in tokens for the chosen model.

    "Before" is what the untouched originals would have cost on the same
    model, so the pair is a like-for-like comparison rather than a
    flattering one against a different yardstick.
    """
    if not records or not model:
        return None
    before = sum(token_cost(*r["size"], model) for r in records)
    after = sum(token_cost(*r["out_size"], model) for r in records)
    if not before:
        return None
    return before, after, round(100 * (before - after) / before)


def upload_notes(records, model, fmt, currency=DEFAULT_CURRENCY):
    """Lines about what this batch will cost and where it hits a limit.

    Kept out of both front ends because the CLI and the window need exactly
    the same warnings, and a limit stated in only one of them is a trap.
    """
    if not records:
        return []
    count = len(records)
    if not model:
        each = {key: sum(token_cost(*spec["fit"](*r["size"]) if spec["fit"]
                                    else r["size"], key) for r in records)
                for key, spec in MODELS.items()}
        notes = [f"{count} image(s), left at original size"]
        notes.append("  no model chosen, so nothing was resized. Sized for "
                     "one, these would cost about: "
                     + ", ".join(f"{MODELS[k]['short']} {v:,}"
                                 for k, v in each.items()))
        if fmt == "png":
            notes.append("  PNG keeps text crisp but uploads large; use the "
                         "photo preset for photographs")
        return notes

    spec = MODELS[model]
    saved = savings(records, model)
    notes = [f"{count} image(s), {saved[1]:,} tokens on {spec['short']}"
             + ("" if spec["exact"] else " (estimated)")]
    if saved and saved[2] > 0:
        line = (f"  down from {saved[0]:,} unprepared - "
                f"{saved[2]}% fewer tokens")
        was, now = money(saved[0], model, currency), money(saved[1], model,
                                                           currency)
        if was and now:
            line += (f", {was} down to {now} per upload at "
                     f"{priced_as(model)} pricing (rates {FX_DATE})")
        notes.append(line)
    if not spec["fit"]:
        notes.append("  this provider documents no hard size limit, so "
                     "nothing was resized for it; the count is what it costs")
    if spec["per_message"] and count > spec["per_message"]:
        messages = -(-count // spec["per_message"])
        notes.append(f"  claude.ai takes {spec['per_message']} images per "
                     f"message, so this needs {messages} messages "
                     "(the API takes 100 in one request)")
        over = [r for r in records if max(r["out_size"]) > MANY_IMAGE_EDGE]
        if over:
            notes.append(f"  {len(over)} of them are over {MANY_IMAGE_EDGE} px "
                         "on a side, which a single API request of more than "
                         f"{spec['per_message']} images rejects")
    if fmt == "png" and "PNG" in spec["formats"]:
        notes.append("  PNG keeps text crisp but uploads large; use the "
                     "photo preset for photographs")
    return notes


def size_warnings(records):
    """Outputs too big to upload. Reads the files, so run it after writing."""
    warnings = []
    for rec in records:
        dest = rec.get("dest")
        if not dest or not dest.exists():
            continue
        mb = dest.stat().st_size / 1_048_576
        if mb > MAX_UPLOAD_MB:
            warnings.append(f"  {dest.name} is {mb:.1f} MB, over the "
                            f"{MAX_UPLOAD_MB} MB per-image upload limit")
    return warnings


def write_manifest(records, path):
    """A paste-alongside list naming each image in the order it is sent.

    Anthropic's vision guidance asks for images to be introduced as
    "Image 1:", "Image 2:" so a prompt can refer back to them; without that
    the model has the pictures and no idea which is which.
    """
    lines = ["Images attached, in order:", ""]
    # Ordered by when the photo was taken, not by filename: day-first names
    # do not sort chronologically, and the order is the point of the list.
    for n, rec in enumerate(sorted(records, key=lambda r: (r["when"],
                                                           r["dest"].name)), 1):
        w, h = rec["out_size"]
        when = rec["when"].strftime(DISPLAY_DATE + " %H:%M")
        dated = when if rec["origin"] == "exif" else when + " (file date)"
        lines.append(f"Image {n}: {rec['dest'].name} - taken {dated} "
                     f"- {w}x{h} px, {rec['tokens']:,} visual tokens")
    lines += ["", f"Total: {len(records)} image(s), "
                  f"{sum(r['tokens'] for r in records):,} visual tokens."]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def delete_originals(records):
    """Recycle the sources whose output is on disk and verified.

    Never deletes a source whose conversion failed or whose output is
    missing or empty, so a failed batch cannot cost anyone their photos.
    """
    gone, kept = 0, []
    for rec in records:
        dest = rec.get("dest")
        if not rec.get("written") or not dest or not dest.exists() \
                or dest.stat().st_size == 0:
            kept.append((rec["src"], "its converted copy is missing"))
            continue
        try:
            recycle(rec["src"])
            gone += 1
        except Exception as exc:
            kept.append((rec["src"], str(exc)))
    return gone, kept


def main():
    ap = argparse.ArgumentParser(
        description="Convert phone photos to PNG/JPEG named "
                    "<date>_<label>_<NN>, optionally shrunk for AI upload.",
        epilog='Run with no arguments (or "--gui") to open the window instead.')
    ap.add_argument("sources", nargs="+",
                    help="image files and/or folders containing them")
    ap.add_argument("--label", default="img",
                    help="subject slug for the new names, snake_cased for you "
                         "(default: img)")
    ap.add_argument("--ai", action="store_true",
                    help="preset for AI upload: JPEG at quality "
                         f"{AI_QUALITY}, sized to the standard model tier "
                         "(each part overridable below)")
    ap.add_argument("--text", action="store_true",
                    help="preset for documents, whiteboards and screenshots: "
                         "PNG (lossless, so small text survives), sized to "
                         "the high-resolution tier")
    ap.add_argument("--model", choices=tuple(MODELS) + ("none",), default=None,
                    help="resize to exactly what this model keeps, so no "
                         "uploaded pixel is thrown away: "
                         + "; ".join(f"{k} ({v['note']})"
                                     for k, v in MODELS.items())
                         + f". Default: {DEFAULT_MODEL} under a preset, none "
                         "otherwise")
    ap.add_argument("--tier", choices=tuple(TIERS) + ("none",), default=None,
                    help=argparse.SUPPRESS)  # kept working; --model replaces it
    ap.add_argument("--metadata", choices=("keep", "safe", "strip"),
                    default=None,
                    help="EXIF carried into the copies: keep all; safe "
                         "(default) drops GPS location and camera "
                         "owner/serial but keeps the capture time; strip "
                         "drops the lot. Originals are never altered")
    ap.add_argument("--delete-originals", action="store_true",
                    help="after a verified conversion, send each original to "
                         "the Recycle Bin; skips any file whose copy is "
                         "missing, and never runs under --dry-run")
    ap.add_argument("--date-format", choices=tuple(DATE_FORMATS),
                    default=DEFAULT_DATE_FORMAT,
                    help="date order in the new filenames: uk (default) is "
                         "day-first and reads the way UK dates are written; "
                         "iso is year-first and is the only one that sorts "
                         "chronologically in a file browser")
    ap.add_argument("--currency", choices=tuple(CURRENCIES),
                    default=DEFAULT_CURRENCY,
                    help=f"currency for the cost estimate (default "
                         f"{DEFAULT_CURRENCY})")
    ap.add_argument("--fx", type=float, default=None, metavar="RATE",
                    help=f"USD-to-currency rate, replacing the one recorded "
                         f"on {FX_DATE}")
    ap.add_argument("--price", type=float, default=None, metavar="USD",
                    help="USD per million input tokens, replacing the "
                         "model's published price")
    ap.add_argument("--manifest", action="store_true",
                    help="also write a numbered list of the outputs to paste "
                         "alongside them in the chat")
    ap.add_argument("--format", choices=("png", "jpg"), default=None,
                    help="output format (default: png, or jpg under --ai)")
    ap.add_argument("--max-edge", type=int, default=None, metavar="PX",
                    help="additionally cap the longest edge at PX, applied "
                         "before the tier fit; never upscales")
    ap.add_argument("--quality", type=int, default=None, metavar="N",
                    help=f"JPEG quality 1-95 (default {AI_QUALITY}; "
                         "ignored for png)")
    ap.add_argument("-o", "--outdir", type=Path,
                    help="write every output into this folder instead of "
                         "beside its source")
    ap.add_argument("--recurse", action="store_true",
                    help="scan folders recursively")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the rename map and write nothing")
    args = ap.parse_args()

    chosen = args.model or (TIER_ALIAS.get(args.tier, args.tier)
                            if args.tier else None)
    fmt, max_edge, quality, ext, model, metadata = resolve_settings(
        args.ai, args.text, args.format, args.max_edge, args.quality,
        ... if chosen is None else (None if chosen == "none" else chosen),
        args.metadata)
    label = snake_case(args.label)

    files, skipped = collect(args.sources, args.recurse)
    if skipped:
        print(f"skipped {skipped} file(s) already named by this tool; "
              "pass one explicitly to reprocess it")
    if not files:
        sys.exit("no supported image files found")

    if not HEIF_OK and any(p.suffix.lower() in HEIF_EXTS for p in files):
        sys.exit(HEIF_INSTALL_MSG)
    if any(p.suffix.lower() == ".avif" for p in files) and not features.check("avif"):
        sys.exit(".avif files are present but this Pillow build lacks AVIF "
                 "support.\nFix with:  pip install --upgrade pillow")

    records, failures = analyse(files, model, max_edge)
    plan_names(records, label, ext, args.outdir, args.date_format)

    # Check every destination folder before writing a single file: without
    # this a blocked folder yields one identical cryptic failure per photo.
    if not args.dry_run:
        for folder in sorted({r["dest"].parent for r in records}):
            why = writable(folder)
            if why:
                sys.exit(f"Cannot write to {folder}.\n\n{why}")

    converted = 0
    for rec in records:
        note = "" if rec["origin"] == "exif" else "  (file date: no usable EXIF)"
        w, h = rec["out_size"]
        cost = f", {rec['tokens']:,} tokens" if model else ""
        line = (f"{rec['src'].name} -> {rec['dest'].name}"
                f"  [{w}x{h}{cost}]{note}")
        if args.dry_run:
            print(line)
            continue
        try:
            rec["written"] = convert(rec["src"], rec["dest"], fmt, max_edge,
                                     quality, model, metadata)
        except Exception as exc:
            failures.append((rec["src"], diagnose(exc, rec["src"], rec["dest"])))
            rec["dest"].unlink(missing_ok=True)  # no half-written files left behind
            continue
        converted += 1
        print(line)

    done = [r for r in records if r.get("written")]
    if args.dry_run:
        print(f"\ndry run: {len(records)} file(s) would be written as "
              f"{fmt.upper()}; nothing touched")
        done = records
    else:
        print(f"\n{converted} of {len(files)} file(s) converted to "
              f"{fmt.upper()}")

    for line in upload_notes(done, model, fmt, args.currency):
        print(line)
    if not args.dry_run:
        for line in size_warnings(done):
            print(line)

    located = [r for r in records if r["located"]]
    if located:
        where = ("carried into the copies" if metadata == "keep"
                 else "left out of the copies")
        print(f"  {len(located)} original(s) record where the photo was "
              f"taken; that location is {where}")

    if args.manifest and done and not args.dry_run:
        folder = args.outdir or done[0]["dest"].parent
        path = write_manifest(done, folder / f"{label}_manifest.txt")
        print(f"  list written to {path.name}")

    if args.delete_originals and not args.dry_run:
        gone, kept = delete_originals(done)
        print(f"\n{gone} original(s) sent to the Recycle Bin")
        for src, why in kept:
            print(f"  kept {src.name}: {why}", file=sys.stderr)
    elif args.delete_originals:
        print("\ndry run: originals would be sent to the Recycle Bin")
    else:
        print("  originals untouched")

    for src, why in failures:
        print(f"FAILED  {src}: {why}", file=sys.stderr)
    if failures:
        sys.exit(1)


# The window's help text. Every control has an entry: a control a person
# cannot explain to themselves is a control they will leave alone. Each entry
# says what the thing does now — never what changed, which belongs in
# project_log.md rather than in front of someone trying to use the tool.
HELP = {
    "photos": (
        "Which photos to prepare",
        "Add single photos, or a whole folder and every image in it is "
        "picked up.\n\n"
        "Reads HEIC (what iPhones produce), JPEG, PNG, WebP, TIFF, BMP, GIF "
        "and AVIF. RAW camera files need a photo editor instead.\n\n"
        "Your originals are never changed, unless you tick the Recycle Bin "
        "option in step 5."),
    "name": (
        "What the copies are called",
        "One plain word describing the batch. The copies come out as\n\n"
        "        2026-08-29_whiteboard_01.jpg\n\n"
        "so they sort into date order.\n\n"
        "The date is when the photo was taken, read from the photo itself. "
        "Where there is none, the file's own date is used and the results "
        "say so."),
    "model": (
        "Which AI you are sending these to",
        "Every AI shrinks your image before it looks at it, and charges you "
        "for the result. Send a 12-megapixel photo and most of it is thrown "
        "away on arrival.\n\n"
        "Pick the one you are actually using and the copies are sized to "
        "exactly what it keeps. Nothing visible is lost, because it would "
        "have been discarded anyway.\n\n"
        "Claude figures are exact. ChatGPT and Gemini are close estimates "
        "from their published formulas.\n\n"
        "Unsure? Claude (high resolution) is a safe default."),
    "use": (
        "What kind of images these are",
        "Photographs - JPEG. Smallest files. Rooms, objects, people, "
        "damage, places.\n\n"
        "Documents and screenshots - PNG, which keeps small lettering "
        "readable where JPEG smudges it. Use this for anything you want the "
        "AI to read.\n\n"
        "Full quality - no resizing. Much larger files, and the AI shrinks "
        "them anyway. For your own records rather than for uploading."),
    "save": (
        "Where the copies go",
        "Next to the originals, or all together in one folder. One folder "
        "is usually easier when you are about to drag them into a chat.\n\n"
        "Windows ransomware protection guards Documents, Pictures and "
        "Desktop. If it blocks a folder, save somewhere else."),
    "options": (
        "The three optional extras",
        "Location and camera details - photos carry hidden tags recording "
        "where they were taken and which camera took them. The AI is never "
        "shown them, but the file carries them wherever it goes next.\n\n"
        "Numbered list - a small text file naming each image in order. "
        "Paste it in with the pictures so the AI knows which is which.\n\n"
        "Recycle Bin - happens only after each copy is written and checked. "
        "Anything that failed is kept, and you can restore from the Recycle "
        "Bin afterwards."),
}


class GuiApp:
    """The window: a thin layer over the same functions the CLI uses."""

    def __init__(self, theme=DEFAULT_THEME):
        self.sources = []
        self.outdir = None
        self.running = False
        self.open_when_done = True     # scripted tests switch this off
        self.q = queue.Queue()
        self.theme = theme
        self._saved = None             # last computed saving, for redraws
        self._saved_model = None
        self._progress_state = (0, 0, "", "idle")
        self._savings_h = 0            # reserved height, measured at startup
        self._last_folder = None       # what "Show the files" opens
        self._open_help = None
        self._log = []                 # replayed when the theme is rebuilt

        self.root = tk.Tk()
        self.root.title("Prep photos for AI")
        self.root.minsize(680, 520)
        self._build_all()
        self._fit_to_screen()

    # ---------- construction, repeated when the theme changes ----------

    def _build_all(self):
        self.c = THEMES[self.theme]
        self._apply_brand()
        self.root.configure(background=self.c["ground"])
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self._build_header()
        body = tk.Frame(self.root, background=self.c["ground"], padx=14,
                        pady=8)
        body.grid(row=1, column=0, sticky="nsew")
        body.columnconfigure(0, weight=1)
        body.columnconfigure(1, weight=1)
        body.rowconfigure(7, weight=1)
        self._build_sources(body)
        self._build_naming(body)
        self._build_destination(body)
        self._build_actions(body)
        self._build_log(body)
        self._update_example()

    def _toggle_theme(self):
        """Rebuild in the other palette, carrying the window's state over.

        Recolouring every widget in place would mean tracking each one; the
        window is cheap to build, so it is built again and the state is
        copied across.
        """
        keep = dict(
            label=self.label_var.get(), mode=self.mode_var.get(),
            model=self.model_var.get(), dest=self.dest_var.get(),
            strip=self.strip_var.get(), manifest=self.manifest_var.get(),
            delete=self.delete_var.get(), currency=self.currency_var.get())
        self.theme = "light" if self.theme == "dark" else "dark"
        for child in self.root.winfo_children():
            child.destroy()
        self._build_all()
        self.label_var.set(keep["label"])
        self.mode_var.set(keep["mode"])
        self.model_var.set(keep["model"])
        self.dest_var.set(keep["dest"])
        self.strip_var.set(keep["strip"])
        self.manifest_var.set(keep["manifest"])
        self.delete_var.set(keep["delete"])
        self.currency_var.set(keep["currency"])
        self._refresh_sources()
        if self.outdir:
            self.outdir_label.config(text=self.outdir.name or str(self.outdir))
        for line, tag in self._log:
            self._write(line, tag)
        self._update_example()
        self._draw_savings(self._saved, self._saved_model)
        self._draw_progress(*self._progress_state)
        if self._last_folder:
            self.show_btn.state(["!disabled"])

    def _fit_to_screen(self):
        """Size the window to what it needs, capped by the screen.

        A hard-coded height put the results pane below the bottom edge on a
        shorter display, so the one thing a run produces was invisible.
        """
        self.root.update_idletasks()
        height = min(self.root.winfo_reqheight(),
                     self.root.winfo_screenheight() - 120)
        width = min(max(self.root.winfo_reqwidth(), 780),
                    self.root.winfo_screenwidth() - 80)
        self.root.geometry(f"{width}x{height}")

    # ---------- chrome ----------

    def _build_header(self):
        """A dark band with the mark on it, so the window opens on something
        other than a grey form. The band uses the reversed wordmark - white
        letterforms, Ember counters kept - so the mark sits on the band
        itself. The Ink wordmark would need a pale plate behind it, and a
        plate on a dark band reads as a boxed image dropped onto the header
        rather than as the identity."""
        c = self.c
        band = tk.Frame(self.root, background=c["band"])
        band.grid(row=0, column=0, sticky="ew")
        band.columnconfigure(1, weight=1)
        if self._load_logo():
            tk.Label(band, image=self._logo, background=c["band"],
                     bd=0).grid(row=0, column=0, padx=(16, 14), pady=11)
        else:  # script travelling without the repo: text mark, same layout
            tk.Label(band, text="GAP", background=c["band"],
                     foreground=c["band_text"], bd=0,
                     font=("Segoe UI", 20, "bold")).grid(
                row=0, column=0, padx=(16, 14), pady=11)
        text = tk.Frame(band, background=c["band"])
        text.grid(row=0, column=1, sticky="w", pady=9)
        tk.Label(text, text="Prepare images for AI", background=c["band"],
                 foreground=c["band_text"],
                 font=("Segoe UI", 14, "bold")).pack(anchor="w")
        tk.Label(text, text="Convert, rename, and size them to what the model "
                            "actually keeps", background=c["band"],
                 foreground=c["band_muted"], font=("Segoe UI", 9)).pack(
            anchor="w")
        moon = "☀  Light" if self.theme == "dark" else "☾  Dark"
        tk.Button(band, text=moon, command=self._toggle_theme, relief="flat",
                  background=c["band"], foreground=c["band_muted"],
                  activebackground=c["band"], activeforeground=EMBER,
                  font=("Segoe UI", 9), cursor="hand2", bd=0,
                  padx=10, pady=4).grid(row=0, column=2, padx=14)
        tk.Frame(self.root, background=EMBER, height=3).grid(
            row=0, column=0, sticky="sew")

    def _card(self, parent, row, column, number, title, help_key,
              columnspan=1):
        """One numbered section, drawn as a bordered card with a ? button."""
        c = self.c
        outer = tk.Frame(parent, background=c["line"], padx=1, pady=1)
        outer.grid(row=row, column=column, columnspan=columnspan,
                   sticky="nsew", pady=(0, 7),
                   padx=(0, 8) if columnspan == 1 and column == 0 else 0)
        outer.columnconfigure(0, weight=1)
        outer.rowconfigure(1, weight=1)
        head = tk.Frame(outer, background=c["head"])
        head.grid(row=0, column=0, sticky="ew")
        head.columnconfigure(1, weight=1)
        tk.Label(head, text=f" {number} ", background=EMBER,
                 foreground="#FFFFFF", font=("Segoe UI", 9, "bold")).grid(
            row=0, column=0, padx=(8, 6), pady=5)
        tk.Label(head, text=title, background=c["head"], foreground=c["text"],
                 font=("Segoe UI", 10, "bold")).grid(row=0, column=1,
                                                     sticky="w")
        tk.Button(head, text="?", width=2, relief="flat",
                  background=c["head"], foreground=c["muted"],
                  activebackground=EMBER, activeforeground="#FFFFFF",
                  font=("Segoe UI", 9, "bold"), cursor="hand2", bd=0,
                  command=lambda: self._help(help_key)).grid(
            row=0, column=2, padx=(4, 6))
        inner = tk.Frame(outer, background=c["card"], padx=10, pady=7)
        inner.grid(row=1, column=0, sticky="nsew")
        inner.columnconfigure(0, weight=1)
        return inner

    def _check(self, parent, var, text):
        c = self.c
        return tk.Checkbutton(
            parent, variable=var, text=text, background=c["card"],
            foreground=c["text"], activebackground=c["card"],
            activeforeground=c["text"], selectcolor=c["field"],
            font=("Segoe UI", 9), bd=0, highlightthickness=0, anchor="w")

    def _radio(self, parent, var, value, text, command):
        c = self.c
        return tk.Radiobutton(
            parent, variable=var, value=value, text=text, command=command,
            background=c["card"], foreground=c["text"],
            activebackground=c["card"], activeforeground=c["text"],
            selectcolor=c["field"], font=("Segoe UI", 9), bd=0,
            highlightthickness=0, anchor="w")

    def _help(self, key):
        """A branded panel rather than messagebox.showinfo, which plays the
        system alert sound - wrong for a help button, which reports nothing
        wrong. A Toplevel is silent and can carry the palette."""
        c = self.c
        title, body = HELP[key]
        win = tk.Toplevel(self.root)
        win.title(title)
        win.configure(background=c["ground"])
        win.transient(self.root)
        win.resizable(False, False)
        head = tk.Frame(win, background=c["band"])
        head.pack(fill="x")
        tk.Label(head, text=title, background=c["band"],
                 foreground=c["band_text"], font=("Segoe UI", 11, "bold"),
                 padx=16, pady=9).pack(anchor="w")
        tk.Frame(win, background=EMBER, height=3).pack(fill="x")
        tk.Message(win, text=body, background=c["ground"],
                   foreground=c["text"], font=("Segoe UI", 9), width=430,
                   justify="left", padx=16, pady=13).pack(fill="both",
                                                          expand=True)
        bar = tk.Frame(win, background=c["ground"])
        bar.pack(fill="x", padx=16, pady=(0, 13))
        ttk.Button(bar, text="Close", command=win.destroy,
                   style="Accent.TButton").pack(side="right")
        win.bind("<Escape>", lambda _e: win.destroy())
        win.bind("<Return>", lambda _e: win.destroy())
        win.update_idletasks()
        x = self.root.winfo_rootx() + (self.root.winfo_width()
                                       - win.winfo_width()) // 2
        win.geometry(f"+{max(x, 0)}+{max(self.root.winfo_rooty() + 90, 0)}")
        win.grab_set()
        win.focus_set()
        self._open_help = win          # scripted tests inspect and close it

    # ---------- sections ----------

    def _build_sources(self, body):
        c = self.c
        card = self._card(body, 0, 0, "1", "Choose the photos", "photos",
                          columnspan=2)
        row = tk.Frame(card, background=c["card"])
        row.grid(row=0, column=0, sticky="w", pady=(0, 6))
        ttk.Button(row, text="Add photos...", command=self.add_photos).pack(
            side="left")
        ttk.Button(row, text="Add a folder...", command=self.add_folder).pack(
            side="left", padx=6)
        ttk.Button(row, text="Clear", command=self.clear_sources).pack(
            side="left")
        self.count_label = tk.Label(row, text="nothing chosen yet",
                                    background=c["card"], foreground=c["muted"],
                                    font=("Segoe UI", 9))
        self.count_label.pack(side="left", padx=10)
        self.source_list = tk.Listbox(
            card, height=2, relief="flat", highlightthickness=1,
            highlightbackground=c["line"], highlightcolor=EMBER,
            background=c["field"], foreground=c["text"],
            font=("Segoe UI", 9), selectbackground=c["select"],
            selectforeground=c["text"])
        self.source_list.grid(row=1, column=0, sticky="ew")

    def _build_naming(self, body):
        c = self.c
        card = self._card(body, 1, 0, "2", "Name the copies", "name",
                          columnspan=2)
        row = tk.Frame(card, background=c["card"])
        row.grid(row=0, column=0, sticky="w")
        self.label_var = tk.StringVar(value="img")
        ttk.Entry(row, textvariable=self.label_var, width=20).pack(side="left")
        self.example = tk.Label(row, text="", background=c["card"],
                                foreground=c["muted"], font=("Consolas", 9))
        self.example.pack(side="left", padx=10)
        self.label_var.trace_add("write", lambda *_: self._update_example())

        card = self._card(body, 2, 0, "3", "Which AI, and what kind of images",
                          "model", columnspan=2)
        row = tk.Frame(card, background=c["card"])
        row.grid(row=0, column=0, sticky="ew", pady=(0, 7))
        tk.Label(row, text="Sending to:", background=c["card"],
                 foreground=c["text"], font=("Segoe UI", 9)).pack(
            side="left", padx=(0, 8))
        self.model_var = tk.StringVar(value=MODELS[DEFAULT_MODEL]["label"])
        self.model_box = ttk.Combobox(
            row, textvariable=self.model_var, state="readonly", width=42,
            values=[m["label"] for m in MODELS.values()])
        self.model_box.pack(side="left")
        self.model_box.bind("<<ComboboxSelected>>",
                            lambda _e: self._on_model_change())
        tk.Label(row, text="Costs in:", background=c["card"],
                 foreground=c["text"], font=("Segoe UI", 9)).pack(
            side="left", padx=(12, 6))
        self.currency_var = tk.StringVar(value=DEFAULT_CURRENCY)
        currency = ttk.Combobox(row, textvariable=self.currency_var,
                                state="readonly", width=5,
                                values=list(CURRENCIES))
        currency.pack(side="left")
        currency.bind("<<ComboboxSelected>>",
                      lambda _e: self._on_model_change())
        self.mode_var = tk.StringVar(value="ai")
        for value, text in (
                ("ai", "Photographs - JPEG, smallest files"),
                ("text", "Documents and screenshots - PNG, keeps small "
                         "writing readable"),
                ("full", "Full quality - no resizing, much larger files")):
            self._radio(card, self.mode_var, value, text,
                        self._update_example).grid(sticky="w", column=0)

    def _build_destination(self, body):
        c = self.c
        card = self._card(body, 3, 0, "4", "Save the copies", "save")
        self.dest_var = tk.StringVar(value="beside")
        self._radio(card, self.dest_var, "beside", "Next to the originals",
                    self._reset_outdir).grid(row=0, column=0, sticky="w")
        row = tk.Frame(card, background=c["card"])
        row.grid(row=1, column=0, sticky="w")
        self._radio(row, self.dest_var, "chosen", "One folder:",
                    self._pick_outdir).pack(side="left")
        self.outdir_label = tk.Label(row, text="(none chosen)",
                                     background=c["card"],
                                     foreground=c["muted"],
                                     font=("Segoe UI", 9))
        self.outdir_label.pack(side="left", padx=4)

        card = self._card(body, 3, 1, "5", "Anything else", "options")
        self.strip_var = tk.BooleanVar(value=True)
        self.manifest_var = tk.BooleanVar(value=False)
        self.delete_var = tk.BooleanVar(value=False)
        for var, text in (
                (self.strip_var, "Leave out location and camera details"),
                (self.manifest_var, "Write a numbered list to paste with them"),
                (self.delete_var, "Send originals to the Recycle Bin")):
            self._check(card, var, text).grid(sticky="w", column=0)

    def _build_actions(self, body):
        c = self.c
        row = tk.Frame(body, background=c["ground"])
        row.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(0, 7))
        self.preview_btn = ttk.Button(row, text="Preview",
                                      command=self.preview)
        self.preview_btn.pack(side="left")
        self.convert_btn = ttk.Button(row, text="Convert", command=self.convert,
                                      style="Accent.TButton")
        self.convert_btn.pack(side="left", padx=8)
        self.show_btn = ttk.Button(row, text="Show the files",
                                   command=self._show_output)
        self.show_btn.pack(side="right")
        self.show_btn.state(["disabled"])

        panel = tk.Frame(body, background=c["line"], padx=1, pady=1)
        panel.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(0, 7))
        panel.columnconfigure(0, weight=1)
        self.savings = tk.Canvas(panel, height=84, background=c["head"],
                                 highlightthickness=0)
        self.savings.grid(row=0, column=0, sticky="ew")
        self.progress = tk.Canvas(panel, height=38, background=c["card"],
                                  highlightthickness=0)
        self.progress.grid(row=1, column=0, sticky="ew")
        # Both canvases size themselves from their width, so they have to be
        # redrawn when the window is resized or they keep the first layout.
        self.savings.bind("<Configure>",
                          lambda _e: self._draw_savings(self._saved,
                                                        self._saved_model))
        self.progress.bind("<Configure>",
                           lambda _e: self._draw_progress(
                               *self._progress_state))
        self._measure_savings()
        self._draw_progress()

    def _build_log(self, body):
        c = self.c
        wrap = tk.Frame(body, background=c["line"], padx=1, pady=1)
        wrap.grid(row=7, column=0, columnspan=2, sticky="nsew")
        wrap.columnconfigure(0, weight=1)
        wrap.rowconfigure(0, weight=1)
        # wrap="word" is deliberate: an earlier window clipped long error
        # messages at the right edge with no way to read the rest of them.
        self.text = tk.Text(wrap, height=4, state="disabled", wrap="word",
                            font=("Consolas", 9), relief="flat", padx=8,
                            pady=6, background=c["field"], foreground=c["text"],
                            highlightthickness=0,
                            insertbackground=c["text"])
        self.text.grid(row=0, column=0, sticky="nsew")
        bar = ttk.Scrollbar(wrap, orient="vertical", command=self.text.yview)
        bar.grid(row=0, column=1, sticky="ns")
        self.text.configure(yscrollcommand=bar.set)
        self.text.tag_configure("error", foreground=EMBER)
        self.text.tag_configure("note", foreground=c["muted"])
        self.text.tag_configure("head", foreground=c["text"],
                                font=("Consolas", 9, "bold"))

    # ---------- the headline figure and the progress bar ----------

    def _draw_savings(self, saved, model=None):
        """The saving, drawn large. It is the reason the tool exists, so it
        gets its own panel rather than a line in a log.

        Nothing here is positioned by a hard-coded pixel. Every item is placed
        from the measured extent of the one before it. Two earlier versions
        overlapped their own text because the numbers were tuned by eye at
        one display scale and the fonts are larger at another.
        """
        self._saved, self._saved_model = saved, model
        c, col = self.savings, self.c
        c.delete("all")
        c.update_idletasks()
        width = max(c.winfo_width(), 420)
        pad = 15

        def below(item, gap, x, **kw):
            bottom = c.bbox(item)[3] if item else pad
            return c.create_text(x, bottom + gap, anchor="nw", **kw)

        if not saved:
            first = c.create_text(pad, pad, anchor="nw", fill=col["muted"],
                                  font=("Segoe UI", 11),
                                  text="Choose photos and press Preview to "
                                       "see what they cost")
            below(first, 6, pad, fill=col["muted"], font=("Segoe UI", 9),
                  text="Nothing is written until you press Convert.")
            return self._fit_savings(c, pad)

        before, after, percent = saved
        name = MODELS[model]["short"] if model else ""
        cur = self.currency_var.get() if hasattr(self, "currency_var") \
            else DEFAULT_CURRENCY
        cost_before = money(before, model, cur)
        cost_after = money(after, model, cur)
        if percent <= 0:
            first = c.create_text(pad, pad, anchor="nw", fill=col["text"],
                                  font=("Segoe UI", 15, "bold"),
                                  text=f"{after:,} tokens"
                                       + (f" on {name}" if name else ""))
            below(first, 8, pad, fill=col["muted"], font=("Segoe UI", 9),
                  text="Already within this model's limits - there is nothing "
                       "to save by resizing.")
            return self._fit_savings(c, pad)

        big = c.create_text(pad, pad, anchor="nw", fill=EMBER,
                            font=("Segoe UI", 27, "bold"), text=f"{percent}%")
        caption = below(big, 0, pad, fill=col["text"],
                        font=("Segoe UI", 9, "bold"), text="fewer tokens")
        # The right column starts clear of the widest thing on the left.
        left = max(c.bbox(big)[2], c.bbox(caption)[2]) + 24
        counts = c.create_text(left, pad, anchor="nw", fill=col["text"],
                               font=("Segoe UI", 14, "bold"),
                               text=f"{before:,}  →  {after:,} tokens")
        last = counts
        if cost_before and cost_after:
            last = below(counts, 2, left, fill=col["text"],
                         font=("Segoe UI", 10, "bold"),
                         text=f"{cost_before}  →  {cost_after} per upload")
            last = below(last, 1, left, fill=col["muted"],
                         font=("Segoe UI", 8),
                         text=f"on {name}, {priced_as(model)} input pricing"
                              f"  ·  rates {FX_DATE}")
        else:
            last = below(counts, 3, left, fill=col["muted"],
                         font=("Segoe UI", 9),
                         text=f"visual tokens" + (f", on {name}" if name
                                                  else ""))
        # Two bars, not one track with a caption inside it: a single bar
        # with a label sitting in its empty half reads as a progress bar
        # that has stalled. Stacked, the pair is a before-and-after and
        # needs no caption at all.
        bar_top = c.bbox(last)[3] + 6
        tag_w = 40                                   # room for the end tags
        bar_w = max(width - left - pad - tag_w, 80)
        bar_h = 8
        c.create_rectangle(left, bar_top, left + bar_w, bar_top + bar_h,
                           fill=col["muted"], width=0)
        first = c.create_text(left + bar_w + 5, bar_top + bar_h / 2,
                              anchor="w", fill=col["muted"],
                              font=("Segoe UI", 7), text="before")
        # The end tags are centred on their bars, so each one reaches half
        # its own height ABOVE the bar. The second row is placed from that
        # measured height rather than a guessed pitch: a 7pt label renders
        # 19px tall here, and pitches of 10 and 15 both overlapped.
        top, bottom = c.bbox(first)[1], c.bbox(first)[3]
        second = bottom + 2 + (bottom - top) / 2 - bar_h / 2
        kept = max(bar_w * (after / before), 2) if before else 0
        c.create_rectangle(left, second, left + bar_w, second + bar_h,
                           fill=col["track"], width=0)
        c.create_rectangle(left, second, left + kept, second + bar_h,
                           fill=EMBER, width=0)
        c.create_text(left + bar_w + 5, second + bar_h / 2, anchor="w",
                      fill=EMBER, font=("Segoe UI", 7, "bold"), text="now")
        return self._fit_savings(c, pad)

    @staticmethod
    def _fit_canvas(canvas, pad):
        """Grow the canvas to whatever was actually drawn on it."""
        box = canvas.bbox("all")
        if box:
            canvas.configure(height=box[3] + pad)

    def _fit_savings(self, canvas, pad):
        """Hold the panel at its reserved height rather than growing it.

        Sizing it to its content made the window reflow on every preview and
        squeezed the results pane off the bottom, so the worst case is
        measured once at startup and the panel keeps that height throughout.
        """
        if self._savings_h:
            canvas.configure(height=self._savings_h)
            return
        self._fit_canvas(canvas, pad)

    def _measure_savings(self):
        """Reserve room for the widest, tallest thing the panel can show.

        The real figures are put back afterwards: measuring writes the dummy
        worst case into _saved, and a later redraw (a theme change, a resize)
        would otherwise put 999,999,999 back on screen.
        """
        keep = (self._saved, self._saved_model)
        self._savings_h = 0
        widest = max(MODELS, key=lambda k: len(MODELS[k]["short"]))
        self._draw_savings((999999999, 111111111, 100), widest)
        self.savings.update_idletasks()
        box = self.savings.bbox("all")
        self._savings_h = (box[3] + 15) if box else 120
        self.savings.configure(height=self._savings_h)
        self._saved, self._saved_model = keep
        self._draw_savings(*keep)

    def _draw_progress(self, done=0, total=0, current="", state="idle"):
        """A drawn bar rather than ttk.Progressbar, which cannot be given the
        palette on Windows and reads as a stray piece of another app."""
        self._progress_state = (done, total, current, state)
        c, col = self.progress, self.c
        c.delete("all")
        c.update_idletasks()
        width = max(c.winfo_width(), 420)
        pad = 12
        track_w = width - 2 * pad
        c.create_rectangle(pad, 6, pad + track_w, 17,
                           fill=col["track"], outline=col["line"])
        if state != "idle":
            fraction = (done / total) if total else 0
            if track_w * fraction >= 1:
                c.create_rectangle(pad, 6, pad + track_w * fraction, 17,
                                   fill=EMBER if state == "running"
                                   else col["muted"], width=0)
        if state == "idle":
            label, right = "Ready", ""
        elif state == "running":
            label = f"Converting {min(done + 1, total)} of {total}"
            if current:
                label += f"   ·   {current}"
            right = f"{round((done / total) * 100) if total else 0}%"
        else:
            label, right = f"Finished - {done} of {total} written", "100%"
        c.create_text(pad, pad + 15, anchor="nw", fill=col["muted"],
                      font=("Segoe UI", 8), text=label)
        if right:
            c.create_text(pad + track_w, pad + 15, anchor="ne",
                          fill=col["muted"], font=("Segoe UI", 8), text=right)
        self._fit_canvas(c, 4)

    def _show_output(self):
        """Opening Explorer automatically threw a window over the results the
        user had just been shown, so it is a button they press instead."""
        if self._last_folder and Path(self._last_folder).is_dir():
            os.startfile(self._last_folder)

    # ---------- behaviour ----------

    def _apply_brand(self):
        """GAP palette over ttk's built-in clam theme - clam, unlike the
        native Windows theme, honours colour configuration on every widget."""
        c = self.c
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure(".", background=c["ground"], foreground=c["text"],
                        font=("Segoe UI", 9))
        style.configure("TButton", background=c["btn"], foreground=c["text"],
                        padding=(12, 5), borderwidth=0)
        style.map("TButton", background=[("pressed", c["btn_active"]),
                                         ("active", c["btn_active"])],
                  foreground=[("disabled", c["muted"])])
        style.configure("Accent.TButton", background=EMBER,
                        foreground="#FFFFFF", padding=(16, 5))
        style.map("Accent.TButton",
                  background=[("disabled", c["btn"]), ("pressed", EMBER_DEEP),
                              ("active", EMBER_DEEP)],
                  foreground=[("disabled", c["muted"])])
        style.configure("TEntry", fieldbackground=c["field"],
                        foreground=c["text"], insertcolor=c["text"],
                        borderwidth=1)
        style.configure("TCombobox", fieldbackground=c["field"],
                        background=c["btn"], foreground=c["text"],
                        arrowcolor=c["text"], borderwidth=1)
        style.map("TCombobox",
                  fieldbackground=[("readonly", c["field"])],
                  foreground=[("readonly", c["text"])],
                  selectbackground=[("readonly", c["field"])],
                  selectforeground=[("readonly", c["text"])])
        style.configure("TScrollbar", background=c["btn"], troughcolor=c["ground"],
                        arrowcolor=c["text"], borderwidth=0)
        self.root.option_add("*TCombobox*Listbox.background", c["field"])
        self.root.option_add("*TCombobox*Listbox.foreground", c["text"])
        self.root.option_add("*TCombobox*Listbox.selectBackground", EMBER)
        self.root.option_add("*TCombobox*Listbox.selectForeground", "#FFFFFF")

    def _load_logo(self):
        """Header wordmark + title-bar symbol, embedded at the bottom of this
        file as base64 PNG so a copy of the script keeps its branding without
        the repo alongside. Tk decodes base64 PNG natively - no extra imports
        and no files to find."""
        try:
            self._logo = tk.PhotoImage(
                data=LOGO_WORDMARK_REVERSED_PNG).subsample(2, 2)
            # title bar gets the symbol: the 2.7:1 wordmark dies at icon size
            self._icons = [tk.PhotoImage(data=d)
                           for d in (LOGO_SYMBOL_64_PNG, LOGO_SYMBOL_32_PNG)]
            self.root.iconphoto(True, *self._icons)
            return True
        except Exception:  # blobs absent or corrupted: text header instead
            return False

    def _model_key(self):
        for key, spec in MODELS.items():
            if spec["label"] == self.model_var.get():
                return key
        return DEFAULT_MODEL

    def _on_model_change(self):
        self._update_example()
        self._draw_savings(self._saved, self._saved_model)

    def _settings(self):
        """The window's controls translated into the CLI's own settings."""
        mode = self.mode_var.get()
        fmt, max_edge, quality, ext, _model, metadata = resolve_settings(
            ai=mode == "ai", text=mode == "text", model=self._model_key(),
            metadata="safe" if self.strip_var.get() else "keep")
        return fmt, max_edge, quality, ext, self._model_key(), metadata, \
            mode != "full"

    def _update_example(self):
        ext = self._settings()[3]
        stamp = datetime.now().strftime(DATE_FORMATS[DEFAULT_DATE_FORMAT])
        self.example.config(text=f"becomes  {stamp}_"
                                 f"{snake_case(self.label_var.get())}_01{ext}")

    def add_photos(self):
        picked = filedialog.askopenfilenames(
            title="Choose photos",
            filetypes=[("Photos", "*.heic *.heif *.jpg *.jpeg *.png *.webp "
                                  "*.tif *.tiff *.bmp *.gif *.avif"),
                       ("All files", "*.*")])
        self.sources.extend(p for p in picked if p not in self.sources)
        self._refresh_sources()

    def add_folder(self):
        picked = filedialog.askdirectory(title="Choose a folder of photos")
        if picked and picked not in self.sources:
            self.sources.append(picked)
        self._refresh_sources()

    def clear_sources(self):
        self.sources = []
        self._refresh_sources()
        self._draw_savings(None)

    def _refresh_sources(self):
        self.source_list.delete(0, "end")
        for s in self.sources:
            p = Path(s)
            self.source_list.insert(
                "end", f"[folder]  {p}" if p.is_dir() else p.name)
        n = len(self.sources)
        self.count_label.config(
            text="nothing chosen yet" if not n else
            f"{n} item{'s' if n != 1 else ''} chosen")

    def _pick_outdir(self):
        picked = filedialog.askdirectory(title="Choose the output folder")
        if picked:
            self.outdir = Path(picked)
            self.outdir_label.config(text=Path(picked).name or picked)
        elif self.outdir is None:
            self.dest_var.set("beside")  # dialog cancelled, nothing chosen

    def _reset_outdir(self):
        self.outdir = None
        self.outdir_label.config(text="(none chosen)")

    def _write(self, line, tag):
        self.text.configure(state="normal")
        self.text.insert("end", line + "\n", tag or ())
        self.text.see("end")
        self.text.configure(state="disabled")

    def _append(self, line, tag=None):
        self._log.append((line, tag))
        self._write(line, tag)

    def _clear_text(self):
        self._log = []
        self.text.configure(state="normal")
        self.text.delete("1.0", "end")
        self.text.configure(state="disabled")

    def _prepare(self):
        """The same assembly the CLI does; None if nothing can run."""
        if not self.sources:
            messagebox.showinfo("Nothing chosen yet",
                                "Add photos or a folder first (step 1).",
                                parent=self.root)
            return None
        missing = [s for s in self.sources if not Path(s).exists()]
        if missing:
            messagebox.showerror(
                "Some of those are gone",
                "These are no longer where they were when you added them:"
                "\n\n" + "\n".join(Path(m).name for m in missing[:10])
                + "\n\nUse Clear and add them again.", parent=self.root)
            return None
        files, skipped = collect(self.sources, recurse=False)
        if skipped:
            self._append(f"skipped {skipped} file(s) already named by this "
                         "tool; add one by itself to reprocess it", "note")
        if not files:
            messagebox.showinfo(
                "Nothing to convert",
                "No supported photos found in what you chose.\n\nThe tool "
                "reads HEIC, JPEG, PNG, WebP, TIFF, BMP, GIF and AVIF. RAW "
                "camera files are not supported.", parent=self.root)
            return None
        if not HEIF_OK and any(p.suffix.lower() in HEIF_EXTS for p in files):
            messagebox.showerror(
                "One extra install needed for HEIC",
                "iPhone HEIC photos need the pillow-heif package.\n\n"
                "Open a terminal, run\n\n        pip install pillow-heif\n\n"
                "then start this tool again.", parent=self.root)
            return None
        if any(p.suffix.lower() == ".avif" for p in files) \
                and not features.check("avif"):
            messagebox.showerror(
                "AVIF needs a newer Pillow",
                "Open a terminal, run\n\n        pip install --upgrade "
                "pillow\n\nthen start this tool again.", parent=self.root)
            return None
        fmt, max_edge, quality, ext, model, metadata, resize = self._settings()
        records, failures = analyse(files, model, max_edge, resize)
        for src, why in failures:
            self._append(f"FAILED  {src.name}: {why}", "error")
        if not records:
            messagebox.showerror(
                "None of those could be read",
                "Every file failed to open. The results panel says why for "
                "each one.", parent=self.root)
            return None
        plan_names(records, snake_case(self.label_var.get()), ext, self.outdir)
        return records, (fmt, max_edge, quality, model, metadata, resize)

    def _check_destinations(self, records):
        """Refuse before writing anything if a target folder is blocked."""
        for folder in sorted({r["dest"].parent for r in records}):
            why = writable(folder)
            if why:
                messagebox.showerror(
                    "Windows will not let the tool write there",
                    f"{folder}\n\n{why}", parent=self.root)
                self._append(f"cannot write to {folder}: {why}", "error")
                return False
        return True

    def _report(self, records, model, fmt, metadata):
        """The batch notes, worded exactly as the command line words them."""
        for line in upload_notes(records, model, fmt,
                                 self.currency_var.get()):
            self._append(line, "note" if line.startswith("  ") else "head")
        located = [r for r in records if r["located"]]
        if located:
            where = ("carried into the copies" if metadata == "keep"
                     else "left out of the copies")
            self._append(f"  {len(located)} original(s) record where the photo "
                         f"was taken; that location is {where}", "note")

    def preview(self):
        if self.running:
            return
        self._clear_text()
        prepared = self._prepare()
        if not prepared:
            return
        records, (fmt, _me, _q, model, metadata, _rs) = prepared
        for rec in records:
            note = "" if rec["origin"] == "exif" \
                else "   (file date: no usable EXIF)"
            w, h = rec["out_size"]
            self._append(f"{rec['src'].name}  ->  {rec['dest'].name}"
                         f"   [{w}x{h}, {rec['tokens']:,} tokens]{note}")
        self._append(f"\npreview only - nothing written yet. Convert will "
                     f"write {len(records)} file(s).", "head")
        self._report(records, model, fmt, metadata)
        self._draw_savings(savings(records, model), model)

    def convert(self):
        if self.running:
            return
        self._clear_text()
        prepared = self._prepare()
        if not prepared:
            return
        records, settings = prepared
        if not self._check_destinations(records):
            return
        if self.delete_var.get() and not messagebox.askyesno(
                "Send the originals to the Recycle Bin?",
                f"{len(records)} original file(s) will go to the Recycle Bin "
                "once their copies are made and checked.\n\nAny file whose "
                "copy fails is kept. You can restore anything from the "
                "Recycle Bin afterwards.\n\nGo ahead?", default="no",
                parent=self.root):
            self._append("cancelled - nothing written, nothing deleted", "note")
            return
        self.running = True
        self.preview_btn.state(["disabled"])
        self.convert_btn.state(["disabled"])
        self.show_btn.state(["disabled"])
        self._draw_progress(0, len(records), "", "running")
        # Read every Tk variable here, on the main thread: touching them from
        # the worker is not safe, and the user could change one mid-run.
        chores = (self.manifest_var.get(), self.delete_var.get(),
                  snake_case(self.label_var.get()))
        threading.Thread(target=self._work, args=(records, settings, chores),
                         daemon=True).start()
        self.root.after(100, self._poll)

    def _work(self, records, settings, chores):
        fmt, max_edge, quality, model, metadata, resize = settings
        want_manifest, want_delete, label = chores
        folder = None
        for index, rec in enumerate(records):
            note = "" if rec["origin"] == "exif" \
                else "   (file date: no usable EXIF)"
            self.q.put(("progress", index, len(records), rec["src"].name))
            try:
                rec["written"] = convert(rec["src"], rec["dest"], fmt,
                                         max_edge, quality,
                                         model if resize else None, metadata)
            except Exception as exc:
                rec["dest"].unlink(missing_ok=True)
                self.q.put(("error", f"FAILED  {rec['src'].name}: "
                                     f"{diagnose(exc, rec['src'], rec['dest'])}"))
                continue
            folder = rec["dest"].parent
            w, h = rec["out_size"]
            self.q.put(f"{rec['src'].name}  ->  {rec['dest'].name}"
                       f"   [{w}x{h}, {rec['tokens']:,} tokens]{note}")
        done = [r for r in records if r.get("written")]
        self.q.put(("head", f"\n{len(done)} of {len(records)} file(s) "
                            "converted"))
        self.q.put(("report", done, model, fmt, metadata))
        for line in size_warnings(done):
            self.q.put(("note", line))
        if want_manifest and done:
            try:
                path = write_manifest(done, (folder or done[0]["dest"].parent)
                                      / f"{label}_manifest.txt")
                self.q.put(("note", f"  list written to {path.name}"))
            except Exception as exc:
                self.q.put(("error", f"  could not write the list: "
                                     f"{diagnose(exc)}"))
        if want_delete:
            gone, kept = delete_originals(done)
            self.q.put(("note", f"  {gone} original(s) sent to the Recycle "
                                "Bin"))
            for src, why in kept:
                self.q.put(("error", f"  kept {src.name}: {why}"))
        else:
            self.q.put(("note", "  originals untouched"))
        self.q.put(("done", len(done), len(records), folder, done, model))

    def _poll(self):
        while True:
            try:
                item = self.q.get_nowait()
            except queue.Empty:
                self.root.after(100, self._poll)
                return
            if isinstance(item, tuple) and item[0] == "report":
                self._report(item[1], item[2], item[3], item[4])
                continue
            if isinstance(item, tuple) and item[0] == "progress":
                self._draw_progress(item[1], item[2], item[3], "running")
                continue
            if isinstance(item, tuple) and item[0] == "done":
                _, done, total, folder, records, model = item
                self._draw_savings(savings(records, model), model)
                self._draw_progress(done, total, "", "finished")
                self.running = False
                self.preview_btn.state(["!disabled"])
                self.convert_btn.state(["!disabled"])
                # Explorer is no longer opened automatically: it threw a
                # window over the results the user had just been shown.
                self._last_folder = folder if (folder and done) else None
                self.show_btn.state(["!disabled"] if self._last_folder
                                    else ["disabled"])
                return
            if isinstance(item, tuple):
                self._append(item[1], item[0])
                continue
            self._append(item)

def selftest():
    """Check the sizing maths against Anthropic's own worked examples.

    The resize rule is the one thing here that cannot be checked by looking
    at the output: a wrongly sized file is a perfectly good image, just one
    that gets silently downscaled again on arrival. So the documented
    examples are asserted in code rather than trusted to a careful reading.
    """
    std, high = TIERS["standard"], TIERS["high"]
    cases = [  # (w, h, tier, expected size, expected tokens) from the docs
        (200, 200, std, (200, 200), 64),
        (1000, 1000, std, (1000, 1000), 1296),
        (1092, 1092, std, (1092, 1092), 1521),
        (1920, 1080, std, (1456, 819), 1560),
        (3840, 2160, std, (1456, 819), 1560),
        (3840, 2160, high, (2576, 1449), 4784),
        (1920, 1080, high, (1920, 1080), 2691),
        (1075, 1520, std, (924, 1307), None),   # the A4-scan example
        (1075, 1520, high, (1075, 1520), 2145),
    ]
    bad = 0
    for w, h, tier, want_size, want_tokens in cases:
        got = fit_to_tier(w, h, *tier)
        tokens = count_tokens(*got)
        ok = got == want_size and (want_tokens is None or tokens == want_tokens)
        # 2000x1500 is excluded above on purpose: the reference implementation
        # returns 1270 where the docs print 1269 beside it, at an identical
        # 1564 tokens. This follows the code, which is what the API runs.
        if not ok:
            bad += 1
        print(f"{'ok  ' if ok else 'FAIL'} {w}x{h} tier {tier} -> {got} "
              f"({tokens} tokens), expected {want_size}"
              + (f" ({want_tokens} tokens)" if want_tokens else ""))
    portrait = fit_to_tier(1500, 2000, *std)
    if portrait != (fit_to_tier(2000, 1500, *std)[1],
                    fit_to_tier(2000, 1500, *std)[0]):
        print("FAIL portrait and landscape disagree")
        bad += 1
    else:
        print(f"ok   portrait 1500x2000 -> {portrait}, mirrors the landscape")
    if target_size(4000, 3000, "claude-standard", max_edge=800) != (800, 600):
        print("FAIL --max-edge is not applied before the model fit")
        bad += 1
    else:
        print("ok   --max-edge 800 caps before the model fit")
    extra = 2
    # The other providers' own worked examples, from their documentation.
    for label, got, want in (
            ("Gemini 960x540 (docs: 6 tiles)", _gemini_count(960, 540),
             6 * GEMINI_TILE_TOKENS),
            ("Gemini 300x300 (docs: flat 258)", _gemini_count(300, 300),
             GEMINI_TILE_TOKENS),
            ("OpenAI 1024x1024 patches x1.2", _openai_count(1024, 1024),
             round(32 * 32 * OPENAI_MULTIPLIER))):
        extra += 1
        if got != want:
            print(f"FAIL {label} -> {got}, expected {want}")
            bad += 1
        else:
            print(f"ok   {label} -> {got}")
    fitted = _openai_fit(4032, 3024)
    patches = -(-fitted[0] // OPENAI_PATCH) * -(-fitted[1] // OPENAI_PATCH)
    extra += 1
    if patches > OPENAI_BUDGET:
        print(f"FAIL OpenAI fit exceeds its budget: {patches}")
        bad += 1
    else:
        print(f"ok   OpenAI fit 4032x3024 -> {fitted}, {patches} patches "
              f"within {OPENAI_BUDGET}")
    print(f"\n{'FAILED' if bad else 'passed'}: {len(cases) + extra - bad} of "
          f"{len(cases) + extra} checks")
    return 1 if bad else 0


def run_gui():
    if not TK_OK:
        sys.exit("tkinter is missing from this Python, so the window cannot "
                 "open. The command line still works - run with -h for usage.")
    try:  # crisp text on scaled Windows displays
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass
    GuiApp().root.mainloop()


# Embedded GAP logo (base64 PNG; Tk decodes it natively). Generated by
# tools/embed_logo.py from assets/logo/png - regenerate there if the
# brand assets change; never hand-edit.
LOGO_WORDMARK_PNG = """
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
uBUYOi4zX/8fsVsipdQVSM0AAAAASUVORK5CYII=
"""

LOGO_WORDMARK_REVERSED_PNG = """
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
AAAASUVORK5CYII=
"""

LOGO_SYMBOL_64_PNG = """
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
SUVORK5CYII=
"""

LOGO_SYMBOL_32_PNG = """
iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAEPElEQVR42sVXXWhcRRT+zszdZN24
mt0N3ULRQGqapEkT8TFWfWrtQ9EK0ofG/vjzJEKLFdI00eqjRYSC1YjQgoINBQVLGwIWJFqE0L5o
V+2LGrCVQtIYKW524905PuydOzN77zZNTPQ+3Mt+d+5833znzDmzxMz4Py8PAFpbWzMJ8t8mou1S
yKwQlJZCgISAFAQiCj8welnf/wJj0UzJ1TfOuiKYz8CRq9d+PuUBgMTix0rRTikIDAZz9UlgILjX
zmD9bAK4qUaXTRuPAbsAVAUoxY8QqqRgBiig1z/Naq3J4rB4B8KRNkZWCFjhfhLGYmZYQtiMvnuL
DRoRoklsAQCF8SUzuCoEgZBlWryUA8FTGEOMpf2PbsW2bTuC6dgIYVgYhxhrtC7GFgYzLhTA1mrB
2Pn0Lpw4OYqh4WOQQjqkZtxSBDWYJmF2IuUFTzIkhGPDQ1CVCgb2HUBXdw9eO/gKZmdnVmSx3rdu
ynCIi2hoGeXFMkaGBvHm60expbcPY599gZ7e3mVabFbLVlJxgCk7B0wSWrMAODv2KV7aPwApJU5/
Mob+rY/dtcWGWGO1icxODpATVyuhbty4jrm5W0gkErg3nXYsdQg4DqvngBHjmT1QjX/4BQEdXV0Y
/egUmjNZDB4+hInxC7X1OLKqmvJQBzOXAABSiuzcYjC2P7kDZ85+DiEl9u3ZjfEL55ZncQxmVs+u
AKVLTeDjnoG9OHFyFNPT09j9zFMofP/dyixml9je8oqVtQ3ZNB0GkF+/HhPj5zFyZBALpWK1GwYz
JpNJbOl7GNLzIo1gfn4ePxYKiBjPke7h1gF2CzDefec4BAkIISDIDd3hwaMY2Lu/bn9/8cBzuPT1
JNzS4IphmJIfFiK2e46u/8xgIiehJsbPI5vNOWcETVAsLuCnwg8BSQypLUa5Akz3CUgDDZHSeXlq
Cpenppa2uA7GNZtB5wBV2WqIg3MBhR9H+m19i+sQG4ydHHC3yp2IGbFJdmdSA3DcmRDh0SMwwhEC
UJAcy7HYeRs599ZUwvBjfRTT6w8zdiUWR8U4QvQuICLKt2TARBoDgYoE+KBqPpJpFQCxFRoKJ6PQ
4jgsmFVvKFZoSDSWtQNCV6C2to147/0P0dvXl/oP/hKktRHeulzz31JKfDV5CR0tGfDFc8Dt+bWl
z7T8Qs8+v9Hr7oaYuQmkUk3Fjs7OVOmD4/CvfLvmyxdtHfelAHjl8kMEzKJcKjX4vg+/tR1/Tl6M
S91VvRpKJaSCENC6XPMCETUePPQqhoZH4P9xC/7c7NpaQOKbZFv748TMyLdkrxKhRxChfdOm3zo3
b/79nsakkp5QnvBU2JFWMwPT6cLIG2+9TMyMDflcf6XCZ0jQg4IIQhAIwZNEsH14taNy+tfrN18g
/feciOSGfO4JKDwACEiPKoKoQkSV6EHq312KVCVZUl9em5m5/Q8rDQfdDkx5PQAAAABJRU5ErkJg
gg==
"""


if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1:] == ["--gui"]:
        run_gui()
    elif sys.argv[1:] == ["--selftest"]:
        sys.exit(selftest())
    else:
        main()
