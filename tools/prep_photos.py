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
Run with no arguments (or --gui) and a small window opens instead of the
command line: pick photos or a folder, type the naming word, choose a
preset, preview the new names, convert. It drives exactly the same
functions as the command line — the window exists so the tool is reachable
without a terminal, not as a different tool — and it exposes only the
decisions a person actually makes; every finer control below stays
command-line on purpose.

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

So --tier resizes to the largest size the tier actually accepts, computed
with Anthropic's published reference algorithm rather than by capping an
edge. --selftest asserts that maths against the worked examples in their
documentation, because a wrongly sized file looks perfectly fine and fails
silently. Every count the tool prints is the real cost of the file it
wrote: --dry-run prices a batch before anything is written.

Presets and limits
------------------
--ai      JPEG at quality 85, standard tier. The everyday case.
--text    PNG (lossless, so small writing survives), high-resolution tier
          — for documents, whiteboards and screenshots. Anthropic's own
          guidance warns that heavy JPEG compression makes text hard to
          read, which is the whole reason this preset is not just --ai.

Each of --format, --tier, --max-edge and --quality overrides its preset.
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

Limits and figures are from platform.claude.com/docs/en/build-with-claude/
vision and .../vision-coordinates, read 2026-08-29. They move; re-read them
before trusting the numbers, and re-run --selftest after any change.

Usage
-----
    python tools/prep_photos.py                    # no arguments: the window
    python tools/prep_photos.py C:\imports --label whiteboard --ai
    python tools/prep_photos.py C:\scans --label contract --text --manifest
    python tools/prep_photos.py C:\imports --ai --dry-run    # price it first
    python tools/prep_photos.py C:\imports --ai --delete-originals
    python tools/prep_photos.py IMG_4232.HEIC shot.webp -o C:\out
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

OWN_OUTPUT = re.compile(r"\d{4}-\d{2}-\d{2}_[a-z0-9_]+_\d{2,}\.(png|jpg)",
                        re.IGNORECASE)
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


def target_size(width, height, tier, max_edge=None):
    """Final pixel size for one image: the manual cap first, then the tier."""
    if max_edge and max(width, height) > max_edge:
        scale = max_edge / max(width, height)
        width = max(round(width * scale), 1)
        height = max(round(height * scale), 1)
    if tier:
        width, height = fit_to_tier(width, height, *TIERS[tier])
    return width, height


def resolve_settings(ai=False, text=False, fmt=None, max_edge=None,
                     quality=None, tier=..., metadata=None):
    """Fill unset options from a preset or the plain defaults.

    Returns (fmt, max_edge, quality, ext, tier, metadata). --text wins over
    --ai where they disagree; an explicit flag wins over both.
    """
    if fmt is None:
        fmt = "png" if text or not ai else "jpg"
    if tier is ...:
        tier = "high" if text else (DEFAULT_TIER if ai else None)
    if quality is None:
        quality = AI_QUALITY
    if metadata is None:
        metadata = "safe"
    return fmt, max_edge, quality, (".jpg" if fmt == "jpg" else ".png"), \
        tier, metadata


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


def analyse(files, tier=None, max_edge=None):
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
        out = target_size(*size, tier, max_edge)
        records.append({"src": src, "when": when, "origin": origin,
                        "size": size, "located": located, "out_size": out,
                        "tokens": count_tokens(*out)})
    return records, failures


def plan_names(records, label, ext, outdir):
    """Assign each record a destination, never claiming a taken name."""
    by_date = defaultdict(list)
    for rec in records:
        by_date[rec["when"].strftime("%Y-%m-%d")].append(rec)
    claimed = set()  # lowercased: NTFS will not distinguish two casings
    for date_str in sorted(by_date):
        batch = sorted(by_date[date_str],
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


def convert(src, dest, fmt, max_edge, quality, tier=None, metadata="safe"):
    """Write one prepared copy. Returns its (width, height)."""
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im)
        exif = im.getexif()  # orientation already applied and removed
        target = target_size(*im.size, tier, max_edge)
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


def upload_notes(records, tier, fmt):
    """Lines about what this batch will cost and where it hits a limit.

    Kept out of both front ends because the CLI and the window need exactly
    the same warnings, and a limit stated in only one of them is a trap.
    """
    if not records:
        return []
    total = sum(r["tokens"] for r in records)
    count = len(records)
    tier_name = {"standard": "a standard-resolution model",
                 "high": "a high-resolution model (Claude 4.7 and later)"}
    notes = [f"{count} image(s), about {total:,} visual tokens"
             + (f" on {tier_name[tier]}" if tier else "")]
    if not tier:
        billed = {name: sum(count_tokens(*fit_to_tier(*r["out_size"], *limits))
                            for r in records)
                  for name, limits in TIERS.items()}
        notes.append("  no model tier set, so that is what you upload, not "
                     "what you are billed for: Claude downscales these to "
                     f"about {billed['standard']:,} tokens (standard) or "
                     f"{billed['high']:,} (high-resolution)")
    if count > CLAUDE_AI_PER_MESSAGE:
        messages = -(-count // CLAUDE_AI_PER_MESSAGE)
        notes.append(f"  claude.ai takes {CLAUDE_AI_PER_MESSAGE} images per "
                     f"message, so this needs {messages} messages "
                     "(the API takes 100 in one request)")
        over = [r for r in records if max(r["out_size"]) > MANY_IMAGE_EDGE]
        if over:
            notes.append(f"  {len(over)} of them are over {MANY_IMAGE_EDGE} px "
                         "on a side, which a single API request of more than "
                         f"{CLAUDE_AI_PER_MESSAGE} images rejects")
    if fmt == "png":
        notes.append("  PNG keeps text crisp but uploads large; use the AI "
                     "preset for photographs")
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
    for n, rec in enumerate(sorted(records, key=lambda r: r["dest"].name), 1):
        w, h = rec["out_size"]
        when = rec["when"].strftime("%Y-%m-%d %H:%M")
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
    ap.add_argument("--tier", choices=tuple(TIERS) + ("none",), default=None,
                    help="resize to exactly what this model tier accepts, so "
                         "no uploaded pixel is thrown away server-side: "
                         "standard (below Claude 4.7) or high (Claude 4.7 and "
                         "later). Default: standard under --ai, high under "
                         "--text, none otherwise")
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

    fmt, max_edge, quality, ext, tier, metadata = resolve_settings(
        args.ai, args.text, args.format, args.max_edge, args.quality,
        ... if args.tier is None else (None if args.tier == "none"
                                       else args.tier),
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

    records, failures = analyse(files, tier, max_edge)
    plan_names(records, label, ext, args.outdir)

    if args.outdir and not args.dry_run:
        args.outdir.mkdir(parents=True, exist_ok=True)

    converted = 0
    for rec in records:
        note = "" if rec["origin"] == "exif" else "  (file date: no usable EXIF)"
        w, h = rec["out_size"]
        line = (f"{rec['src'].name} -> {rec['dest'].name}"
                f"  [{w}x{h}, {rec['tokens']:,} tokens]{note}")
        if args.dry_run:
            print(line)
            continue
        try:
            rec["written"] = convert(rec["src"], rec["dest"], fmt, max_edge,
                                     quality, tier, metadata)
        except Exception as exc:
            failures.append((rec["src"], str(exc)))
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

    for line in upload_notes(done, tier, fmt):
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


class GuiApp:
    """The window: a thin layer over the same functions the CLI uses."""

    def __init__(self):
        self.sources = []
        self.outdir = None
        self.running = False
        self.open_when_done = True  # scripted tests switch this off
        self.q = queue.Queue()

        self.root = tk.Tk()
        self.root.title("Prep photos for AI")
        self.root.minsize(660, 780)
        self._apply_brand()
        frame = ttk.Frame(self.root, padding=12)
        frame.grid(row=0, column=0, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(17, weight=1)

        if self._load_logo():
            ttk.Label(frame, image=self._logo).grid(
                row=0, column=0, sticky="w", pady=(0, 12))
        else:  # script travelling without the repo: text header, same layout
            ttk.Label(frame, text="Grounded AI Practice",
                      font=("Segoe UI", 13, "bold")).grid(
                row=0, column=0, sticky="w", pady=(0, 12))

        ttk.Label(frame, text="1.  Choose the photos",
                  style="Header.TLabel").grid(row=1, column=0, sticky="w")
        row = ttk.Frame(frame)
        row.grid(row=2, column=0, sticky="w", pady=(4, 2))
        ttk.Button(row, text="Add photos...", command=self.add_photos).pack(
            side="left")
        ttk.Button(row, text="Add a folder...", command=self.add_folder).pack(
            side="left", padx=6)
        ttk.Button(row, text="Clear", command=self.clear_sources).pack(side="left")
        self.source_list = tk.Listbox(
            frame, height=5, relief="flat", highlightthickness=1,
            highlightbackground=MIST, highlightcolor=EMBER,
            background="#FFFFFF", foreground=INK,
            selectbackground=SAND, selectforeground=INK)
        self.source_list.grid(row=3, column=0, sticky="ew", pady=(0, 10))

        ttk.Label(frame, text="2.  Pick a word for the new names",
                  style="Header.TLabel").grid(row=4, column=0, sticky="w")
        row = ttk.Frame(frame)
        row.grid(row=5, column=0, sticky="w", pady=(4, 10))
        self.label_var = tk.StringVar(value="img")
        ttk.Entry(row, textvariable=self.label_var, width=22).pack(side="left")
        self.example = ttk.Label(row, text="", style="Hint.TLabel")
        self.example.pack(side="left", padx=8)
        self.label_var.trace_add("write", lambda *_: self._update_example())

        ttk.Label(frame, text="3.  Choose the output",
                  style="Header.TLabel").grid(row=6, column=0, sticky="w")
        self.mode_var = tk.StringVar(value="ai")
        ttk.Radiobutton(frame, variable=self.mode_var, value="ai",
                        command=self._update_example,
                        text="Photographs for AI chats - JPEG, sized to "
                             "exactly what the AI keeps (recommended)").grid(
            row=7, column=0, sticky="w", pady=(4, 0))
        ttk.Radiobutton(frame, variable=self.mode_var, value="text",
                        command=self._update_example,
                        text="Documents, whiteboards and screenshots - PNG, "
                             "so small writing stays readable").grid(
            row=8, column=0, sticky="w")
        ttk.Radiobutton(frame, variable=self.mode_var, value="full",
                        command=self._update_example,
                        text="Full quality - PNG at original size, much "
                             "larger files").grid(row=9, column=0, sticky="w")
        self.dest_var = tk.StringVar(value="beside")
        ttk.Radiobutton(frame, variable=self.dest_var, value="beside",
                        command=self._reset_outdir,
                        text="Save next to the originals").grid(
            row=10, column=0, sticky="w", pady=(6, 0))
        row = ttk.Frame(frame)
        row.grid(row=11, column=0, sticky="w")
        ttk.Radiobutton(row, variable=self.dest_var, value="chosen",
                        command=self._pick_outdir,
                        text="Save into one folder:").pack(side="left")
        self.outdir_label = ttk.Label(row, text="(none chosen)",
                                      style="Hint.TLabel")
        self.outdir_label.pack(side="left", padx=6)

        ttk.Label(frame, text="4.  Anything else",
                  style="Header.TLabel").grid(row=12, column=0, sticky="w",
                                              pady=(10, 0))
        self.strip_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(frame, variable=self.strip_var,
                        text="Leave out where the photo was taken and who owns "
                             "the camera").grid(row=13, column=0, sticky="w",
                                                pady=(4, 0))
        self.manifest_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(frame, variable=self.manifest_var,
                        text="Write a numbered list to paste with the images"
                        ).grid(row=14, column=0, sticky="w")
        self.delete_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(frame, variable=self.delete_var,
                        text="Send the originals to the Recycle Bin once the "
                             "copies are made").grid(row=15, column=0,
                                                     sticky="w")

        row = ttk.Frame(frame)
        row.grid(row=16, column=0, sticky="w", pady=10)
        self.preview_btn = ttk.Button(row, text="Preview the new names",
                                      command=self.preview)
        self.preview_btn.pack(side="left")
        self.convert_btn = ttk.Button(row, text="Convert", command=self.convert,
                                      style="Accent.TButton")
        self.convert_btn.pack(side="left", padx=8)

        self.text = tk.Text(frame, height=12, state="disabled", wrap="none",
                            font=("Consolas", 9), relief="flat",
                            highlightthickness=1, highlightbackground=MIST,
                            highlightcolor=EMBER, background="#FFFFFF",
                            foreground=INK)
        self.text.grid(row=17, column=0, sticky="nsew")
        self._update_example()

    def _apply_brand(self):
        """GAP palette over ttk's built-in clam theme — clam, unlike the
        native Windows theme, honours colour configuration on every widget."""
        self.root.configure(background=PAPER)
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure(".", background=PAPER, foreground=INK,
                        font=("Segoe UI", 9))
        style.configure("TButton", background=MIST, foreground=INK,
                        padding=(10, 4))
        style.map("TButton", background=[("pressed", SAND), ("active", SAND)])
        style.configure("Accent.TButton", background=EMBER,
                        foreground="#FFFFFF")
        style.map("Accent.TButton",
                  background=[("disabled", MIST), ("pressed", EMBER_DEEP),
                              ("active", EMBER_DEEP)],
                  foreground=[("disabled", STONE)])
        style.map("TRadiobutton", background=[("active", PAPER)])
        style.configure("Header.TLabel", font=("Segoe UI", 10, "bold"))
        style.configure("Hint.TLabel", foreground=STONE)
        style.configure("TEntry", fieldbackground="#FFFFFF")

    def _load_logo(self):
        """Header wordmark + title-bar symbol, embedded at the bottom of
        this file as base64 PNG so a copy of the script keeps its branding
        without the repo alongside. Tk decodes base64 PNG natively - no
        extra imports and no files to find."""
        try:
            self._logo = tk.PhotoImage(data=LOGO_WORDMARK_PNG)
            # title bar gets the symbol: the 2.7:1 wordmark dies at icon size
            self._icons = [tk.PhotoImage(data=d)
                           for d in (LOGO_SYMBOL_64_PNG, LOGO_SYMBOL_32_PNG)]
            self.root.iconphoto(True, *self._icons)
            return True
        except Exception:  # blobs absent or corrupted: text header instead
            return False

    def _settings(self):
        """The window's controls translated into the CLI's own settings."""
        mode = self.mode_var.get()
        return resolve_settings(
            ai=mode == "ai", text=mode == "text",
            metadata="safe" if self.strip_var.get() else "keep")

    def _update_example(self):
        ext = self._settings()[3]
        stamp = datetime.now().strftime("%Y-%m-%d")
        self.example.config(text=f"files become  {stamp}_"
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

    def _refresh_sources(self):
        self.source_list.delete(0, "end")
        for s in self.sources:
            p = Path(s)
            self.source_list.insert(
                "end", f"[folder]  {p}" if p.is_dir() else p.name)

    def _pick_outdir(self):
        picked = filedialog.askdirectory(title="Choose the output folder")
        if picked:
            self.outdir = Path(picked)
            self.outdir_label.config(text=picked)
        elif self.outdir is None:
            self.dest_var.set("beside")  # dialog cancelled, nothing chosen

    def _reset_outdir(self):
        self.outdir = None
        self.outdir_label.config(text="(none chosen)")

    def _append(self, line):
        self.text.configure(state="normal")
        self.text.insert("end", line + "\n")
        self.text.see("end")
        self.text.configure(state="disabled")

    def _clear_text(self):
        self.text.configure(state="normal")
        self.text.delete("1.0", "end")
        self.text.configure(state="disabled")

    def _prepare(self):
        """The same assembly the CLI does; None if nothing can run."""
        if not self.sources:
            messagebox.showinfo("Nothing chosen yet",
                                "Add photos or a folder first (step 1).")
            return None
        files, skipped = collect(self.sources, recurse=False)
        if skipped:
            self._append(f"skipped {skipped} file(s) already named by this "
                         "tool; add one by itself to reprocess it")
        if not files:
            messagebox.showinfo("Nothing to convert",
                                "No supported photos found in what you chose.")
            return None
        if not HEIF_OK and any(p.suffix.lower() in HEIF_EXTS for p in files):
            messagebox.showerror(
                "One extra install needed for HEIC",
                "iPhone HEIC photos need the pillow-heif package.\n\n"
                "Open a terminal, run\n\n        pip install pillow-heif\n\n"
                "then start this tool again.")
            return None
        if any(p.suffix.lower() == ".avif" for p in files) \
                and not features.check("avif"):
            messagebox.showerror(
                "AVIF needs a newer Pillow",
                "Open a terminal, run\n\n        pip install --upgrade "
                "pillow\n\nthen start this tool again.")
            return None
        fmt, max_edge, quality, ext, tier, metadata = self._settings()
        records, failures = analyse(files, tier, max_edge)
        for src, why in failures:
            self._append(f"FAILED  {src.name}: {why}")
        plan_names(records, snake_case(self.label_var.get()), ext, self.outdir)
        return records, (fmt, max_edge, quality, tier, metadata)

    def _report(self, records, tier, fmt, metadata):
        """The batch notes, worded exactly as the command line words them."""
        for line in upload_notes(records, tier, fmt):
            self._append(line)
        located = [r for r in records if r["located"]]
        if located:
            where = ("carried into the copies" if metadata == "keep"
                     else "left out of the copies")
            self._append(f"  {len(located)} original(s) record where the photo "
                         f"was taken; that location is {where}")

    def preview(self):
        if self.running:
            return
        self._clear_text()
        prepared = self._prepare()
        if not prepared:
            return
        records, (fmt, _max_edge, _q, tier, metadata) = prepared
        for rec in records:
            note = "" if rec["origin"] == "exif" \
                else "   (file date: no usable EXIF)"
            w, h = rec["out_size"]
            self._append(f"{rec['src'].name}  ->  {rec['dest'].name}"
                         f"   [{w}x{h}, {rec['tokens']:,} tokens]{note}")
        self._append(f"\npreview only - nothing written yet. Convert will "
                     f"write {len(records)} file(s).")
        self._report(records, tier, fmt, metadata)

    def convert(self):
        if self.running:
            return
        self._clear_text()
        prepared = self._prepare()
        if not prepared:
            return
        records, settings = prepared
        if self.delete_var.get() and not messagebox.askyesno(
                "Send the originals to the Recycle Bin?",
                f"{len(records)} original file(s) will go to the Recycle Bin "
                "once their copies are made and checked.\n\nAny file whose "
                "copy fails is kept. You can restore anything from the "
                "Recycle Bin afterwards.\n\nGo ahead?", default="no"):
            self._append("cancelled - nothing written, nothing deleted")
            return
        if self.outdir:
            self.outdir.mkdir(parents=True, exist_ok=True)
        self.running = True
        self.preview_btn.state(["disabled"])
        self.convert_btn.state(["disabled"])
        # Read every Tk variable here, on the main thread: touching them from
        # the worker is not safe, and the user could change one mid-run.
        chores = (self.manifest_var.get(), self.delete_var.get(),
                  snake_case(self.label_var.get()))
        threading.Thread(target=self._work, args=(records, settings, chores),
                         daemon=True).start()
        self.root.after(100, self._poll)

    def _work(self, records, settings, chores):
        fmt, max_edge, quality, tier, metadata = settings
        want_manifest, want_delete, label = chores
        folder = None
        for rec in records:
            note = "" if rec["origin"] == "exif" \
                else "   (file date: no usable EXIF)"
            try:
                rec["written"] = convert(rec["src"], rec["dest"], fmt,
                                         max_edge, quality, tier, metadata)
            except Exception as exc:
                rec["dest"].unlink(missing_ok=True)
                self.q.put(f"FAILED  {rec['src'].name}: {exc}")
                continue
            folder = rec["dest"].parent
            w, h = rec["out_size"]
            self.q.put(f"{rec['src'].name}  ->  {rec['dest'].name}"
                       f"   [{w}x{h}, {rec['tokens']:,} tokens]{note}")
        done = [r for r in records if r.get("written")]
        self.q.put(f"\n{len(done)} of {len(records)} file(s) converted")
        self.q.put(("report", done, tier, fmt, metadata))
        for line in size_warnings(done):
            self.q.put(line)
        if want_manifest and done:
            try:
                path = write_manifest(done, (folder or done[0]["dest"].parent)
                                      / f"{label}_manifest.txt")
                self.q.put(f"  list written to {path.name}")
            except Exception as exc:
                self.q.put(f"  could not write the list: {exc}")
        if want_delete:
            gone, kept = delete_originals(done)
            self.q.put(f"  {gone} original(s) sent to the Recycle Bin")
            for src, why in kept:
                self.q.put(f"  kept {src.name}: {why}")
        else:
            self.q.put("  originals untouched")
        self.q.put(("done", len(done), len(records), folder))

    def _poll(self):
        while True:
            try:
                item = self.q.get_nowait()
            except queue.Empty:
                self.root.after(100, self._poll)
                return
            if isinstance(item, tuple) and item[0] == "report":
                _, records, tier, fmt, metadata = item
                self._report(records, tier, fmt, metadata)
                continue
            if isinstance(item, tuple):
                _, done, total, folder = item
                self.running = False
                self.preview_btn.state(["!disabled"])
                self.convert_btn.state(["!disabled"])
                if folder and done and self.open_when_done:
                    os.startfile(folder)  # show the results in Explorer
                return
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
    if target_size(4000, 3000, "standard", max_edge=800) != (800, 600):
        print("FAIL --max-edge is not applied before the tier fit")
        bad += 1
    else:
        print("ok   --max-edge 800 caps before the tier fit")
    print(f"\n{'FAILED' if bad else 'passed'}: {len(cases) + 2 - bad} of "
          f"{len(cases) + 2} checks")
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
