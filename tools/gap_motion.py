#!/usr/bin/env python3
"""GAP's motion layer: turn the figure helpers into frames, and check them.

Why this exists
---------------
`build_server_guide_figures.py` and its siblings draw brand-correct
diagrams — Public Sans from the installed faces, the palette from
`project_brief.md`, boxes and arrows on a computed grid. They draw one
picture. A great deal of what this project explains is a *process*: what
the model does with the fraction of context a prompt carries, how a claim
moves from source to log entry to figure, why a price per gigabyte ranks
cards differently from a price. Those read badly as a single frame and
well as ten seconds of movement.

This module is the thinnest possible layer that gets there. It does not
draw anything. It takes a `draw(d, t)` function written against the
existing helpers, calls it once per frame with the clock moved on, and
encodes the result.

Why not Remotion, Motion Canvas or After Effects
------------------------------------------------
The obvious answer was Remotion, and it was rejected on fit rather than
quality. It is React, TypeScript and a Chrome Headless Shell downloaded
into `node_modules`, against a repo that has no JavaScript build step and
treats that as a feature. Its licence is free for an individual and for a
non-profit of any size, so the threshold is not the objection; the
toolchain is. Motion Canvas was the closer call — MIT, no threshold, and
built for exactly this kind of explanatory animation — but headless
rendering is still an open request upstream, and its model is a human
driving an interactive editor. Claude cannot see an editor.

What is left is the route that was already here. Every frame is drawn by
the same code that draws the static figures, so brand fidelity is not a
thing to get right; it is inherited. And every frame is a PNG, which
matters more than it sounds: it means the geometry self-check rule
extends to motion for nothing, because the contact sheet below is
readable by the same eyes that read a rendered document.

The checks, and what each one caught
------------------------------------
Per CLAUDE.md, a generated visual asset gets a self-check before it is
accepted, and a script that draws cannot see its own output.

`check_motion` blocks a render whose frames are all identical. That is
what a `t` parameter accepted and never used looks like, and it produces
a perfectly valid video of a still image — no error, no warning, nothing
to notice until someone watches it.

`check_dimensions` blocks odd pixel dimensions. H.264 at `yuv420p`
chroma-subsamples by two in each direction and cannot represent an odd
edge; `imageio-ffmpeg` hides this by silently resizing to a multiple of
16 unless `macro_block_size=1` is set, which trades a hard failure for a
quietly rescaled, slightly soft video.

`check_persistence` is the source-line check. CLAUDE.md requires every
outward graphic to carry its own source-and-date line, and motion breaks
that rule quietly: a line drawn for six frames of a six-second clip
satisfies any static check and attributes nothing. This asserts that a
named region has ink in *every* frame. **Its honest limit: it verifies
that something is drawn there, not that the something is correct.** It
cannot read text. It catches absence, late arrival and early exit, which
are the three ways the rule actually gets broken.

`check_tail` is advisory rather than blocking, and warns when the clip
runs on after the motion has stopped. A held final frame is sometimes
deliberate; usually it is dead air, and in a feed it is the stretch
during which the viewer scrolls on. It was written after this module's
own first render, a 4-second demo whose motion finished at 2.5 seconds.

`contact_sheet` is not a check but the thing that makes checking
possible — sampled frames tiled into one labelled PNG, so a whole clip
can be read in a single image. Same move as `--sheet` in `gap_icon.py`,
and for the same reason: the numbers confirm a render completed and
cannot say whether it looks right. The demo above was read this way and
the dead tail was visible in it before any check existed.

The four blocking checks were verified by deliberately breaking a good
clip four ways — a `draw` ignoring `t`, a source line stopping at 0.5s,
an odd width, a duration under the profile floor — and confirming each
is refused while an unbroken control still writes. That pass found a
real defect in this module rather than in the clips: the persistence
check had been wired to fire only when `render` drew the source line
itself, so a caller drawing its own attribution got no check and no
warning that none had run. Drawing and checking are separate arguments
now.

Frames go to disk rather than a list. A 6-second 1080x1080 clip at 30fps
is 180 frames of about 3.5 MB each in memory, and holding them all is
half a gigabyte for no gain. Writing them out bounds memory to one frame
and leaves the frames inspectable afterwards, which is the render →
inspect → fix loop rather than an obstacle to it.

Requirements
------------
Python with Pillow, the Public Sans TTF faces installed, and
`build_server_guide_figures.py` beside this file. GIF and WebP need
nothing further. MP4 needs `imageio-ffmpeg`, whose pip wheel carries a
static ffmpeg binary, so no system ffmpeg install is required:

    pip install imageio-ffmpeg

Usage
-----
    from gap_motion import render, PROFILES, seg, ease_out_cubic

    def draw(d, t):
        sg.text(d, 40, 40, "hello", "Bold", 28)

    render(draw, "assets/motion/demo", PROFILES["square"],
           duration=6.0, source="Source: ... Retrieved 2026-08-29.")

    python tools/gap_motion.py --demo -o assets/motion
    python tools/gap_motion.py --selftest

Command-line only, per project_log.md Entry 049 — a build step runs this,
not a person at a window.
"""

import argparse
import contextlib
import hashlib
import os
import shutil
import sys
import tempfile

try:
    from PIL import Image, ImageChops
except ImportError:
    sys.exit("Pillow is required: pip install pillow")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_server_guide_figures as sg                      # noqa: E402


# ---------------------------------------------------------------------------
# Output profiles
# ---------------------------------------------------------------------------
# Sizes and the duration floor are platform facts, kept in one place with
# their provenance rather than scattered through call sites.
#
# PROVENANCE, and its weakness: the LinkedIn figures below were taken from
# secondary summaries of LinkedIn's specs on 2026-08-29, not from
# LinkedIn's own help pages. They agreed with one another, which is weaker
# evidence than it looks — they may share a source. Under this project's
# source-scope rule that is vendor/commercial tier. Verify against
# LinkedIn's own documentation before treating a render as publishable.
#
# `min_duration` is the one that bites: LinkedIn rejects a clip under 3
# seconds outright, so a 2-second loop is not a stylistic choice there.
PROFILES = {
    # Square. Safe everywhere, and the most legible in a phone feed.
    "square": {"size": (1080, 1080), "fps": 30, "min_duration": 3.0,
               "logical": (360, 360)},
    # 4:5 portrait. Takes the most vertical space a feed will give.
    "portrait": {"size": (1080, 1350), "fps": 30, "min_duration": 3.0,
                 "logical": (360, 450)},
    # 9:16. For the vertical feed.
    "vertical": {"size": (1080, 1920), "fps": 30, "min_duration": 3.0,
                 "logical": (360, 640)},
    # 16:9 landscape, for a document or a site rather than a feed.
    "wide": {"size": (1600, 900), "fps": 30, "min_duration": 0.0,
             "logical": (400, 225)},
    # A short loop inside a learning unit. No platform floor applies.
    "loop": {"size": (900, 600), "fps": 25, "min_duration": 0.0,
             "logical": (360, 240)},
}

# Render above the output size and downsample. Genuine supersampling:
# Pillow draws hard-edged polygons and text, and a LANCZOS reduction is
# what turns a stepped diagonal into a clean one. 2 is the point of
# diminishing returns; 3 costs 2.25x the draw time for very little.
OVERSAMPLE = 2


# ---------------------------------------------------------------------------
# Easing
# ---------------------------------------------------------------------------
# The code we own instead of importing a timeline framework. All take and
# return 0..1. Motion craft, in the order it matters: things arrive with
# deceleration, leave faster than they arrived, and never all at once.

def clamp(v, lo=0.0, hi=1.0):
    return lo if v < lo else hi if v > hi else v


def seg(t, start, end):
    """Normalise absolute time `t` into 0..1 across a segment, clamped.

    The single most useful primitive here. A timeline is a set of
    overlapping segments, and this is what turns "between 1.2s and 2.0s"
    into a progress value the easings can take.
    """
    if end <= start:
        return 1.0 if t >= end else 0.0
    return clamp((t - start) / (end - start))


def linear(p):
    return p


def ease_out_cubic(p):
    """Fast start, gentle settle. The default for anything arriving."""
    return 1.0 - (1.0 - p) ** 3


def ease_in_cubic(p):
    """Gentle start, fast finish. For anything leaving."""
    return p ** 3


def ease_in_out_cubic(p):
    if p < 0.5:
        return 4.0 * p * p * p
    return 1.0 - ((-2.0 * p + 2.0) ** 3) / 2.0


def ease_out_back(p, overshoot=1.70158):
    """Overshoot and settle — the spring feel, without a spring solver.

    Reaches past 1.0 near the end and comes back. Use it on scale and
    position, never on opacity or colour, where exceeding 1.0 clips
    instead of overshooting and the effect is simply wrong.
    """
    c3 = overshoot + 1.0
    return 1.0 + c3 * ((p - 1.0) ** 3) + overshoot * ((p - 1.0) ** 2)


def stagger(i, n, t, start, end, overlap=0.6):
    """Progress for element `i` of `n`, offset so they do not arrive together.

    `overlap` is how much of each element's animation runs while the next
    has already begun: 0 is strictly sequential, 1 is simultaneous. The
    whole set still finishes at `end`.
    """
    if n <= 1:
        return seg(t, start, end)
    span = end - start
    each = span / (1.0 + (n - 1) * (1.0 - overlap))
    offset = start + i * each * (1.0 - overlap)
    return seg(t, offset, offset + each)


def mix(a, b, p):
    """Interpolate a number, or a tuple of numbers, by p."""
    if isinstance(a, (tuple, list)):
        return tuple(x + (y - x) * p for x, y in zip(a, b))
    return a + (b - a) * p


def fade(colour, p, ground="#FFFFFF"):
    """Blend a hex colour towards `ground` — Pillow has no alpha on draws.

    p=1 is the full colour, p=0 is the ground. This is what an opacity
    ramp has to be when drawing onto an RGB canvas.
    """
    c = _hex(colour)
    g = _hex(ground)
    return tuple(int(round(gg + (cc - gg) * clamp(p))) for cc, gg in zip(c, g))


def _hex(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


# ---------------------------------------------------------------------------
# The drawing context
# ---------------------------------------------------------------------------
@contextlib.contextmanager
def _figure_grid(logical_w, scale, font_boost=1.0):
    """Point the sibling module's globals at this clip, then put them back.

    `build_server_guide_figures` keeps W, SCALE and FONT_BOOST as module
    globals, which is right for a script that draws one set of figures at
    one size. Borrowing its helpers means moving them. Restoring them
    matters because a caller may build static figures later in the same
    process, and leaving SCALE at a video value would silently change
    their size.

    FONT_BOOST resets to 1.0 by default. Its 1.32 exists to correct type
    for a figure placed at a 6.77in text column in Word, which is a print
    correction with no meaning on a video frame.
    """
    old = (sg.W, sg.SCALE, sg.FONT_BOOST)
    sg.W, sg.SCALE, sg.FONT_BOOST = logical_w, scale, font_boost
    try:
        yield
    finally:
        sg.W, sg.SCALE, sg.FONT_BOOST = old


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------
def check_dimensions(size, verbose=True):
    """Block odd pixel dimensions. Returns True if acceptable.

    H.264 at yuv420p subsamples chroma by two in each direction, so an
    odd edge cannot be represented. imageio-ffmpeg's default
    macro_block_size=16 papers over this by resizing, which is worse than
    a refusal: the output is a slightly soft video at dimensions nobody
    asked for.
    """
    w, h = size
    bad = [n for n, v in (("width", w), ("height", h)) if v % 2]
    if bad:
        if verbose:
            print("  FAIL  odd %s (%dx%d) - H.264 yuv420p needs even "
                  "dimensions" % (" and ".join(bad), w, h))
        return False
    return True


def check_duration(duration, profile, verbose=True):
    """Block a clip shorter than the target platform accepts."""
    floor = profile.get("min_duration", 0.0)
    if duration < floor:
        if verbose:
            print("  FAIL  %.2fs is below this profile's %.1fs floor"
                  % (duration, floor))
        return False
    return True


def check_motion(hashes, verbose=True):
    """Block a render in which nothing moved.

    A `draw` that ignores `t` produces a valid video of a still image.
    Nothing errors, nothing warns, and the defect survives every other
    check here.
    """
    distinct = len(set(hashes))
    if distinct <= 1:
        if verbose:
            print("  FAIL  all %d frames identical - is `t` wired up?"
                  % len(hashes))
        return False
    if distinct < max(2, len(hashes) // 10) and verbose:
        print("  note  only %d distinct frames out of %d - heavily "
              "stepped, or mostly static" % (distinct, len(hashes)))
    return True


def check_tail(hashes, fps, limit=0.15, floor=0.4, verbose=True):
    """Warn when the clip keeps running after the motion has stopped.

    Advisory, not blocking: a held final frame is sometimes deliberate,
    giving a reader time to finish the last label. What it is usually is
    dead air, and in a feed the dead tail is the part during which the
    viewer scrolls on.

    Found on this module's own first render — a 4.0s demo whose motion
    finished at 2.5s. `check_motion` cannot see it, because that only
    fires when *every* frame matches.
    """
    if len(hashes) < 2:
        return True
    last, n = hashes[-1], 0
    for h in reversed(hashes):
        if h != last:
            break
        n += 1
    secs = n / float(fps)
    if n > len(hashes) * limit and secs >= floor:
        if verbose:
            print("  note  last %.2fs (%d frames, %.0f%%) is motionless - "
                  "trim, or hold deliberately"
                  % (secs, n, 100.0 * n / len(hashes)))
        return False
    return True


def check_persistence(frame_paths, region, ground="#FFFFFF", verbose=True):
    """Assert a region has ink in *every* frame. The source-line check.

    `region` is (x0, y0, x1, y1) in output pixels. CLAUDE.md requires
    every outward graphic to carry its own source-and-date line, and a
    moving image breaks that quietly — a line present for six frames of a
    six-second clip passes any single-frame check and attributes nothing.

    Honest limit, stated because it matters: this verifies that something
    is drawn in that box, not that it is the right something. It cannot
    read. What it catches is absence, late arrival and early exit, which
    is how the rule actually gets broken.
    """
    flat = Image.new("RGB", (region[2] - region[0], region[3] - region[1]),
                     _hex(ground))
    empty = []
    for i, p in enumerate(frame_paths):
        with Image.open(p) as im:
            crop = im.convert("RGB").crop(region)
            # "Has ink" = at least one pixel meaningfully off the ground.
            # Done as a difference-and-threshold rather than a pixel loop:
            # the region is tens of thousands of pixels per frame, and
            # Image.getdata() is both slow here and deprecated in Pillow 12.
            diff = ImageChops.difference(crop, flat).convert("L")
            if diff.point(lambda v: 255 if v > 8 else 0).getbbox() is None:
                empty.append(i)
    if empty:
        if verbose:
            rng = ("frames %d-%d" % (empty[0], empty[-1])
                   if len(empty) > 1 else "frame %d" % empty[0])
            print("  FAIL  source region is blank in %d of %d frames (%s)"
                  % (len(empty), len(frame_paths), rng))
        return False
    return True


def contact_sheet(frame_paths, out_path, fps, cols=5, rows=3, thumb=320):
    """Tile sampled frames into one labelled PNG, evenly across the clip.

    Not a check — the thing that makes checking possible. A clip cannot
    be read by a process that reads images one at a time; a sheet can.
    """
    n = min(cols * rows, len(frame_paths))
    if n == 0:
        return None
    idx = [round(i * (len(frame_paths) - 1) / max(1, n - 1))
           for i in range(n)]

    with Image.open(frame_paths[0]) as probe:
        aspect = probe.height / probe.width
    tw, th = thumb, int(round(thumb * aspect))
    pad, label_h = 12, 26
    used_rows = (n + cols - 1) // cols
    sheet = Image.new("RGB",
                      (cols * (tw + pad) + pad,
                       used_rows * (th + label_h + pad) + pad),
                      _hex(sg.MIST))

    from PIL import ImageDraw
    d = ImageDraw.Draw(sheet)
    with _figure_grid(logical_w=100, scale=1, font_boost=1.0):
        f = sg.font("SemiBold", 13)
        for k, fi in enumerate(idx):
            cx = pad + (k % cols) * (tw + pad)
            cy = pad + (k // cols) * (th + label_h + pad)
            with Image.open(frame_paths[fi]) as im:
                sheet.paste(im.convert("RGB").resize((tw, th),
                                                     Image.LANCZOS), (cx, cy))
            d.text((cx, cy + th + 5),
                   "frame %d   %.2fs" % (fi, fi / float(fps)),
                   font=f, fill=_hex(sg.GRAPHITE))
    sheet.save(out_path, "PNG")
    return out_path


# ---------------------------------------------------------------------------
# Encoders
# ---------------------------------------------------------------------------
def _encode_mp4(frame_paths, out_path, size, fps, crf=18):
    try:
        import imageio_ffmpeg
    except ImportError:
        sys.exit(
            "MP4 output needs imageio-ffmpeg, which is not installed.\n"
            "Its pip wheel carries a static ffmpeg binary, so this does "
            "not install anything system-wide:\n\n"
            "    pip install imageio-ffmpeg\n\n"
            "GIF and WebP need nothing extra — try --format gif.")

    writer = imageio_ffmpeg.write_frames(
        out_path, size, fps=fps,
        codec="libx264", pix_fmt_in="rgb24", pix_fmt_out="yuv420p",
        # 1, not the default 16: keep the exact dimensions we checked
        # rather than being silently resized to a multiple.
        macro_block_size=1,
        output_params=["-crf", str(crf), "-preset", "medium",
                       "-movflags", "+faststart"])
    writer.send(None)
    try:
        for p in frame_paths:
            with Image.open(p) as im:
                writer.send(im.convert("RGB").tobytes())
    finally:
        writer.close()
    return out_path


def _encode_pillow(frame_paths, out_path, fps, fmt, max_edge=None):
    """GIF or animated WebP, Pillow only. No new dependency.

    GIF is 256 colours and one byte per pixel per frame, so it is capped
    to a sane edge by default; a full-size GIF of a 1080 clip is tens of
    megabytes and worse-looking than the MP4 it replaces.
    """
    frames = []
    for p in frame_paths:
        with Image.open(p) as im:
            im = im.convert("RGB")
            if max_edge and max(im.size) > max_edge:
                r = max_edge / float(max(im.size))
                im = im.resize((int(im.width * r), int(im.height * r)),
                               Image.LANCZOS)
            frames.append(im.convert("P", palette=Image.ADAPTIVE, colors=256)
                          if fmt == "gif" else im.copy())
    ms = int(round(1000.0 / fps))
    frames[0].save(out_path, format=fmt.upper(), save_all=True,
                   append_images=frames[1:], duration=ms, loop=0,
                   **({"disposal": 2, "optimize": True} if fmt == "gif"
                      else {"quality": 88, "method": 4}))
    return out_path


# ---------------------------------------------------------------------------
# The render
# ---------------------------------------------------------------------------
def render(draw, out_stem, profile, duration=6.0, source=None,
           source_region=None, formats=("mp4",), fps=None, ground=None,
           keep_frames=None, sheet=True, oversample=OVERSAMPLE, verbose=True):
    """Draw `duration` seconds of `draw(d, t)` and encode it.

    `draw` receives a Pillow ImageDraw and the time in seconds, and works
    in the logical units of `profile["logical"]` — the same units the
    static figure helpers use, so sg.box/sg.text/sg.arrow work unchanged.

    `source` is drawn bottom-left in every frame and is not optional for
    anything outward-facing. Drawing and checking are separate, so there
    are three positions and each has to be chosen:

      source="Source: ..."        draw the line here, and check it
      source=None, source_region= caller draws its own line; still checked
      neither                     no line and no check, decided deliberately

    Nothing is written until every blocking check passes.
    """
    fps = fps or profile["fps"]
    out_w, out_h = profile["size"]
    log_w, log_h = profile["logical"]
    ground = ground or sg.PAPER
    n_frames = max(1, int(round(duration * fps)))

    if verbose:
        print("rendering %s  %dx%d  %.2fs  %dfps  (%d frames)"
              % (os.path.basename(out_stem), out_w, out_h, duration, fps,
                 n_frames))

    ok = check_dimensions((out_w, out_h), verbose)
    ok = check_duration(duration, profile, verbose) and ok
    if not ok:
        sys.exit("refusing to render: failed a blocking check")

    # Draw at oversample x output, then reduce. SCALE must be a whole
    # number: sg.canvas multiplies it into Image.new, which takes ints
    # only, and sg.s() truncates with it. Rounding up rather than to
    # nearest keeps the draw at or above the supersampling target, and
    # the closing resize lands the exact output size either way.
    scale = max(1, -(-out_w * oversample // log_w))
    if out_w % log_w and verbose:
        print("  note  logical width %d does not divide output width %d - "
              "one logical unit is %.3f px" % (log_w, out_w,
                                               out_w / float(log_w)))

    tmp = keep_frames or tempfile.mkdtemp(prefix="gap_motion_")
    os.makedirs(tmp, exist_ok=True)
    frame_paths, hashes = [], []

    # The source line sits inside the bottom margin, in logical units.
    src_y = log_h - 14
    if source_region is None and source:
        source_region = (0, int(out_h * (src_y - 3) / float(log_h)),
                         out_w, out_h)

    try:
        with _figure_grid(logical_w=log_w, scale=scale, font_boost=1.0):
            for i in range(n_frames):
                t = i / float(fps)
                img, d = sg.canvas(log_h)
                if ground != sg.PAPER:
                    d.rectangle([0, 0, img.width, img.height], fill=ground)
                draw(d, t)
                if source:
                    sg.text(d, 16, src_y, source, "Regular", 9, sg.STONE)
                img = img.resize((out_w, out_h), Image.LANCZOS)
                p = os.path.join(tmp, "f%05d.png" % i)
                img.save(p, "PNG")
                img.close()
                frame_paths.append(p)
                with open(p, "rb") as fh:
                    hashes.append(hashlib.blake2b(fh.read(),
                                                  digest_size=16).digest())

        ok = check_motion(hashes, verbose)
        check_tail(hashes, fps, verbose=verbose)   # advisory, never blocks
        # Checked whenever a region is known, whether this module drew the
        # line or the caller did. Coupling the check to `source` meant a
        # caller who drew their own attribution got no check and no word
        # about it, which is the failure this module exists to prevent.
        if source_region:
            ok = check_persistence(frame_paths, source_region, ground,
                                   verbose) and ok
        if not ok:
            sys.exit("refusing to write: failed a blocking check "
                     "(frames left in %s)" % tmp)

        os.makedirs(os.path.dirname(os.path.abspath(out_stem)), exist_ok=True)
        written = []
        for fmt in formats:
            out = "%s.%s" % (out_stem, fmt)
            if fmt == "mp4":
                _encode_mp4(frame_paths, out, (out_w, out_h), fps)
            elif fmt in ("gif", "webp"):
                _encode_pillow(frame_paths, out, fps, fmt,
                               max_edge=640 if fmt == "gif" else None)
            else:
                sys.exit("unknown format %r (mp4, gif, webp)" % fmt)
            written.append(out)
            if verbose:
                print("  wrote %s  (%.1f MB)"
                      % (os.path.basename(out),
                         os.path.getsize(out) / 1e6))

        if sheet:
            sp = contact_sheet(frame_paths, out_stem + "_sheet.png", fps)
            written.append(sp)
            if verbose:
                print("  wrote %s  <- read this before accepting the clip"
                      % os.path.basename(sp))
        return written
    finally:
        if not keep_frames:
            shutil.rmtree(tmp, ignore_errors=True)


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------
def demo_draw(d, t):
    """Exercise every path: stagger, easing, a fade, a persistent line.

    The values are deliberately labelled as placeholders and assert
    nothing. A demo that renders plausible-looking figures is a figure
    with no source, and this repo's rules exist to stop those existing.
    """
    sg.text(d, 16, 22, "How a bar chart arrives", "ExtraBold", 22, sg.INK)
    sg.text(d, 16, 50, "demo output — the numbers are placeholders",
            "Regular", 11, sg.STONE)

    bars = [("first", 0.55), ("second", 0.80), ("third", 0.35)]
    base_y, bar_h, gap = 90, 34, 46
    for i, (label, value) in enumerate(bars):
        p = ease_out_cubic(stagger(i, len(bars), t, 0.3, 2.4, overlap=0.55))
        y = base_y + i * gap
        sg.box(d, 100, y, 220, bar_h, _hex(sg.MIST), radius=4)
        if p > 0:
            sg.box(d, 100, y, max(1, 220 * value * p), bar_h,
                   sg.EMBER if i == 1 else sg.INK, radius=4)
        sg.text(d, 92, y + bar_h / 2, label, "SemiBold", 13,
                fade(sg.INK, p, sg.PAPER), anchor="rm")

    # A late note, arriving after the bars have settled and fading in.
    q = ease_out_cubic(seg(t, 2.4, 3.2))
    if q > 0:
        sg.text(d, 16, 250, "the middle one is the point",
                "Bold", 15, fade(sg.EMBER, q, sg.PAPER))


def _selftest():
    """Assert the timing maths. A wrong easing is invisible in a render."""
    checks = []

    def eq(name, got, want, tol=1e-9):
        checks.append((name, abs(got - want) <= tol, got, want))

    eq("seg before", seg(0.5, 1.0, 2.0), 0.0)
    eq("seg start", seg(1.0, 1.0, 2.0), 0.0)
    eq("seg mid", seg(1.5, 1.0, 2.0), 0.5)
    eq("seg end", seg(2.0, 1.0, 2.0), 1.0)
    eq("seg after", seg(9.0, 1.0, 2.0), 1.0)
    eq("seg zero-width", seg(2.0, 2.0, 2.0), 1.0)

    for f in (linear, ease_out_cubic, ease_in_cubic, ease_in_out_cubic):
        eq("%s(0)" % f.__name__, f(0.0), 0.0)
        eq("%s(1)" % f.__name__, f(1.0), 1.0)
    eq("ease_out_back(0)", ease_out_back(0.0), 0.0)
    eq("ease_out_back(1)", ease_out_back(1.0), 1.0)
    checks.append(("ease_out_back overshoots",
                   max(ease_out_back(p / 100.0) for p in range(101)) > 1.0,
                   "peak>1", "peak>1"))

    # Staggered elements must all start apart and all finish together.
    n = 4
    starts = []
    for i in range(n):
        s_ = next((k / 1000.0 for k in range(0, 4001)
                   if stagger(i, n, k / 1000.0, 0.0, 4.0) > 0), None)
        starts.append(s_)
        eq("stagger %d ends at end" % i, stagger(i, n, 4.0, 0.0, 4.0), 1.0)
    checks.append(("stagger offsets ascend",
                   all(starts[i] < starts[i + 1] for i in range(n - 1)),
                   starts, "ascending"))
    eq("stagger n=1", stagger(0, 1, 2.0, 0.0, 4.0), 0.5)

    eq("mix", mix(10.0, 20.0, 0.25), 12.5)
    checks.append(("mix tuple", mix((0, 10), (10, 20), 0.5) == (5.0, 15.0),
                   mix((0, 10), (10, 20), 0.5), (5.0, 15.0)))
    checks.append(("fade to ground", fade("#000000", 0.0) == (255, 255, 255),
                   fade("#000000", 0.0), (255, 255, 255)))
    checks.append(("fade full", fade("#000000", 1.0) == (0, 0, 0),
                   fade("#000000", 1.0), (0, 0, 0)))

    # The checks themselves must actually refuse bad input.
    checks.append(("check_dimensions rejects odd",
                   not check_dimensions((1081, 1080), verbose=False),
                   "refused", "refused"))
    checks.append(("check_dimensions accepts even",
                   check_dimensions((1080, 1080), verbose=False),
                   "accepted", "accepted"))
    checks.append(("check_motion rejects identical",
                   not check_motion([b"a"] * 30, verbose=False),
                   "refused", "refused"))
    checks.append(("check_motion accepts varied",
                   check_motion([bytes([i]) for i in range(30)],
                                verbose=False),
                   "accepted", "accepted"))
    checks.append(("check_duration rejects short",
                   not check_duration(2.0, PROFILES["square"], verbose=False),
                   "refused", "refused"))
    # A tail of 30 identical frames at 30fps is 1.0s of 3.0s — flagged.
    checks.append(("check_tail flags dead tail",
                   not check_tail([bytes([i]) for i in range(60)] + [b"z"] * 30,
                                  30, verbose=False),
                   "flagged", "flagged"))
    checks.append(("check_tail passes live tail",
                   check_tail([bytes([i]) for i in range(90)], 30,
                              verbose=False),
                   "passed", "passed"))
    # Two held frames is 0.07s — under the floor, not worth a note.
    checks.append(("check_tail ignores brief hold",
                   check_tail([bytes([i]) for i in range(20)] + [b"z"] * 2,
                              30, verbose=False),
                   "passed", "passed"))

    # sg's globals must come back exactly as they were.
    before = (sg.W, sg.SCALE, sg.FONT_BOOST)
    with _figure_grid(1, 99, 9.9):
        pass
    checks.append(("figure grid restored", (sg.W, sg.SCALE,
                                            sg.FONT_BOOST) == before,
                   (sg.W, sg.SCALE, sg.FONT_BOOST), before))

    bad = [c for c in checks if not c[1]]
    for name, okc, got, want in checks:
        print("  %s  %s" % ("ok  " if okc else "FAIL", name))
        if not okc:
            print("        got %r, wanted %r" % (got, want))
    print("\n%d checks, %d failed" % (len(checks), len(bad)))
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(
        description="Render brand-correct motion from the figure helpers.")
    ap.add_argument("--demo", action="store_true",
                    help="render the built-in demo clip")
    ap.add_argument("--selftest", action="store_true",
                    help="assert the easing and check logic, render nothing")
    ap.add_argument("-o", "--output", default="assets/motion",
                    help="destination folder (default: assets/motion)")
    ap.add_argument("--profile", default="square", choices=sorted(PROFILES),
                    help="output profile (default: square)")
    ap.add_argument("--format", default="gif",
                    help="comma-separated: mp4, gif, webp (default: gif)")
    ap.add_argument("--duration", type=float, default=3.5,
                    help="seconds (default: 3.5)")
    ap.add_argument("--keep-frames", metavar="DIR",
                    help="write frames here and keep them, for inspection")
    args = ap.parse_args()

    if args.selftest:
        return _selftest()
    if not args.demo:
        ap.error("nothing to do — pass --demo, --selftest, or import "
                 "this module and call render()")

    os.makedirs(args.output, exist_ok=True)
    render(demo_draw, os.path.join(args.output, "demo"),
           PROFILES[args.profile], duration=args.duration,
           source="Demo output. No data claim. Built 2026-08-29.",
           formats=tuple(f.strip() for f in args.format.split(",")),
           keep_frames=args.keep_frames)
    return 0


if __name__ == "__main__":
    sys.exit(main())
