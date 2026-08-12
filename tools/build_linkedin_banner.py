"""Compose the profile-banner and social-card exports.

Why this exists: the banner artwork carried no identity until August
2026, and adding identity to a LinkedIn banner is not safe to do
blind — the mobile presentation crops a 1584x396 canvas to roughly its
centre two-thirds, and the desktop presentation lays the profile photo
over the lower left. A wordmark placed by eye can be silently deleted
by exactly the crop the banner exists to survive, so this script
places everything in code, enforces the safe zones, and emits crop
previews for both presentations. The 2026-08-12 redesign (creator
decision, concept B of three) retired the original radar-motif SVG:
the base is now generated here — Ink ground, dot grid, a ghosted
book-and-terminal symbol, an Ember baseline rule — so the design has
no hand-drawn source to drift from. `--svg` remains for composing over
an SVG base instead.

The same brand system also serves link-preview duty, so `--card-out`
composes a 1280x640 social card (GitHub repository social preview,
LinkedIn entry media): same ground, dots, ghost and rule, with the
reversed wordmark, a subtitle and the domain. Card text is
bounds-checked against its own margins and the ghost's column.

The ghost keeps the symbol's interior detail deliberately: the
reversed symbol is composited at low alpha rather than flattened to a
silhouette, so the terminal chevron reads as Ink cut-outs through the
lightened body — flattening it to one colour would erase the very
feature that makes the mark recognisable.

Checks refuse to write when the wordmark or text leaves its safe
window, collides with a reserved zone, or lands below the wordmark's
~160 px minimum usable width. The render still gets a human read
afterwards — the checks bound placement, they do not see the picture.

Requires: Python with Pillow; ``vl-convert-python`` (via the sibling
``gap_chart``) only when ``--svg`` is used; the Public Sans faces
installed (paths via the sibling ``build_server_guide_figures``); the
wordmark and symbol exports in ``assets/logo/png/``.

Command-line by the Entry 049 decision — a build step run by Claude or
the creator at a terminal, not a learner-facing tool.
"""

import argparse
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from build_server_guide_figures import FONT_DIRS  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PNGDIR = os.path.join(REPO, "assets", "logo", "png")

# Native banner geometry (1x), and the zones learned from the crop
# previews: mobile keeps ~[270, 1315] horizontally; the desktop
# avatar circle sits over the lower left.
BANNER_W, BANNER_H = 1584, 396
MOBILE_SAFE = (280, 1310)          # x-range that survives the mobile crop
AVATAR_CENTRE, AVATAR_R = (188, 412), 118   # desktop photo overlap (approx)
WORDMARK_MIN_W = 160               # below this the A's crossbar closes up
MOTIF_X = 1008                     # right column reserved for the motif

CARD_W, CARD_H = 1280, 640
CARD_MARGIN = 90
CARD_TEXT_W = 700                  # subtitle column, clear of the ghost

INK = (39, 34, 30)
EMBER = (241, 94, 75)
SAND = (249, 232, 220, 255)
SAND3 = (249, 232, 220)
DOT = (64, 58, 52)
GHOST_ALPHA = 0.08


def load_font(weight, px):
    # The server-guide script's font() bakes in that script's canvas
    # scale, so this loads the face at an exact pixel size instead,
    # reusing only its knowledge of where the family lives.
    name = "PublicSans-%s.ttf" % weight
    for d in FONT_DIRS:
        p = os.path.join(d, name)
        if d and os.path.exists(p):
            return ImageFont.truetype(p, int(px))
    raise SystemExit("Public Sans not found (looked for %s)" % name)


def _checks(pairs):
    ok = True
    for name, passed in pairs:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
        ok &= passed
    if not ok:
        raise SystemExit("placement check failed; nothing written")


def _ghost(symbol_png, height_px):
    sym = Image.open(symbol_png).convert("RGBA")
    w = round(sym.width * height_px / sym.height)
    sym = sym.resize((w, height_px), Image.LANCZOS)
    sym.putalpha(sym.split()[3].point(lambda v: int(v * GHOST_ALPHA)))
    return sym


def _dots(d, w, h, scale):
    for gx in range(48, w // scale, 44):
        for gy in range(40, h // scale, 44):
            d.ellipse([gx * scale - 2, gy * scale - 2,
                       gx * scale + 2, gy * scale + 2], fill=DOT)


def _save(img, out):
    # Export at composed resolution (2x by default): LinkedIn and
    # GitHub both recompress uploads, and a native-size export goes
    # soft after their pass — found 2026-08-12 on the live banner.
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    img.convert("RGB").save(out)
    print(f"wrote {out} ({img.width}x{img.height})")


def draw_banner_base(scale, symbol_png):
    w, h = BANNER_W * scale, BANNER_H * scale
    img = Image.new("RGBA", (w, h), INK + (255,))
    d = ImageDraw.Draw(img)
    _dots(d, w, h, scale)
    img.alpha_composite(_ghost(symbol_png, 330 * scale),
                        (1040 * scale, 40 * scale))
    d.rectangle([0, 382 * scale, w, 388 * scale], fill=EMBER)
    return img


def compose_split_banner(out, scale=2, previews=False):
    # The abstract Sand-over-Ink split (creator's pick, 2026-08-12,
    # from three abstract concepts): no wordmark, no symbol and —
    # since the same day's live review — no domain line either. The
    # creator found the text sliding behind the avatar at window
    # sizes the zone model doesn't cover, and judged it redundant
    # besides (the Featured cards, contact info and company page all
    # carry the URL). Every element is full-bleed, so the design is
    # crop-immune by construction and needs no placement checks.
    w, h = BANNER_W * scale, BANNER_H * scale
    img = Image.new("RGBA", (w, h), SAND3 + (255,))
    d = ImageDraw.Draw(img)
    for gx in range(48, BANNER_W, 44):
        for gy in range(40, 280, 44):
            d.ellipse([gx * scale - 2, gy * scale - 2,
                       gx * scale + 2, gy * scale + 2],
                      fill=(219, 203, 191))
    d.rectangle([0, 292 * scale, w, 300 * scale], fill=EMBER)
    d.rectangle([0, 300 * scale, w, h], fill=INK + (255,))
    for gx in range(48, BANNER_W, 44):
        for gy in range(322, BANNER_H, 44):
            d.ellipse([gx * scale - 2, gy * scale - 2,
                       gx * scale + 2, gy * scale + 2], fill=DOT)

    print("  PASS  crop-immune: no placed content")
    _save(img, out)

    if previews:
        final = Image.open(out).convert("RGBA")
        s = final.width // BANNER_W
        stem = os.path.dirname(out)
        crop = final.crop((270 * s, 0, 1315 * s, BANNER_H * s))
        p1 = os.path.join(stem, "preview_banner_mobilecrop.png")
        crop.convert("RGB").save(p1)
        print(f"wrote {p1}")


def compose_banner(out, svg, wordmark_png, symbol_png, domain, scale=2,
                   previews=False):
    if svg:
        from gap_chart import to_png
        tmp = out + ".base.png"
        to_png(svg, tmp, scale=float(scale))
        base = Image.open(tmp).convert("RGBA")
        os.remove(tmp)
        if base.size != (BANNER_W * scale, BANNER_H * scale):
            raise SystemExit(f"base render is {base.size}, expected "
                             f"{(BANNER_W * scale, BANNER_H * scale)}")
    else:
        base = draw_banner_base(scale, symbol_png)

    wm = Image.open(wordmark_png).convert("RGBA")
    wm_w = 430 * scale
    wm_h = round(wm.height * wm_w / wm.width)
    wm = wm.resize((wm_w, wm_h), Image.LANCZOS)
    wm_x, wm_y = 350 * scale, 88 * scale

    label = load_font("SemiBold", 26 * scale)
    d = ImageDraw.Draw(base)
    dm_x = wm_x
    dm_y = wm_y + wm_h + 20 * scale
    dm_w = d.textlength(domain, font=label)

    _checks([
        ("wordmark >= min usable width", wm_w / scale >= WORDMARK_MIN_W),
        ("wordmark inside mobile-safe window",
         MOBILE_SAFE[0] * scale <= wm_x
         and wm_x + wm_w <= MOBILE_SAFE[1] * scale),
        ("domain line inside mobile-safe window",
         MOBILE_SAFE[0] * scale <= dm_x
         and dm_x + dm_w <= MOBILE_SAFE[1] * scale),
        ("clear of desktop avatar zone",
         wm_x > (AVATAR_CENTRE[0] + AVATAR_R) * scale),
        ("clear of the motif column", wm_x + wm_w < MOTIF_X * scale),
        ("block clear of the grounding rule",
         dm_y + 30 * scale < 382 * scale),
    ])

    base.alpha_composite(wm, (wm_x, wm_y))
    d.text((dm_x, dm_y), domain, font=label, fill=SAND)
    _save(base, out)

    if previews:
        final = Image.open(out).convert("RGBA")
        s = final.width // BANNER_W
        stem = os.path.dirname(out)
        crop = final.crop((270 * s, 0, 1315 * s, BANNER_H * s))
        p1 = os.path.join(stem, "preview_banner_mobilecrop.png")
        crop.convert("RGB").save(p1)
        ring = Image.new("RGBA", final.size, (0, 0, 0, 0))
        rd = ImageDraw.Draw(ring)
        cx, cy = AVATAR_CENTRE
        rd.ellipse(((cx - AVATAR_R) * s, (cy - AVATAR_R) * s,
                    (cx + AVATAR_R) * s, (cy + AVATAR_R) * s),
                   fill=(255, 255, 255, 90),
                   outline=(255, 255, 255, 220), width=3 * s)
        desk = Image.alpha_composite(final, ring).convert("RGB")
        p2 = os.path.join(stem, "preview_profile_desktop.png")
        desk.save(p2)
        print(f"wrote {p1}\nwrote {p2}")


def _lead_image(path, scale, large=False):
    # A card's lead mark. Wide marks (the GAP wordmark) size by width,
    # square marks (the GitHub Invertocat) by height; the large sizes
    # serve the no-subtitle layout, where the mark carries the card.
    # If the source arrives with a fully opaque canvas — the official
    # GitHub Mark PNG bakes its white box in — alpha is derived from
    # luminance so the black glyph lands cleanly on a light ground;
    # the glyph itself is untouched, per the mark's usage terms.
    img = Image.open(path).convert("RGBA")
    if img.split()[3].getextrema()[0] == 255:
        alpha = img.convert("L").point(lambda v: 255 - v)
        img = Image.new("RGBA", img.size, (0, 0, 0, 255))
        img.putalpha(alpha)
    if img.width / img.height > 1.8:
        w = (560 if large else 380) * scale
        h = round(img.height * w / img.width)
    else:
        # Square marks size taller than the wide wordmark is high: a
        # compact circle needs the extra to read as the same weight.
        h = (380 if large else 160) * scale
        w = round(img.width * h / img.height)
    return img.resize((w, h), Image.LANCZOS)


def _wrap(d, text, f, max_w):
    lines, line = [], ""
    for word in text.split():
        probe = (line + " " + word).strip()
        if d.textlength(probe, font=f) <= max_w:
            line = probe
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def compose_card(out, subtitle, wordmark_png, symbol_png, domain,
                 scale=2, theme="dark", lead_png=None):
    # Light cards exist so two cards can sit side by side (the
    # Featured section) as siblings, not twins. Text on the light
    # ground is Ink throughout: Ember fails the 4.5:1 text threshold
    # on Sand, so there it is a rule colour, never a text colour.
    if theme == "light":
        ground, dot, text_fill, dom_fill = SAND3, (213, 197, 185), \
            INK, INK
    else:
        ground, dot, text_fill, dom_fill = INK, DOT, SAND, EMBER
    w, h = CARD_W * scale, CARD_H * scale
    img = Image.new("RGBA", (w, h), ground + (255,))
    d = ImageDraw.Draw(img)
    for gx in range(48, CARD_W, 44):
        for gy in range(40, CARD_H, 44):
            d.ellipse([gx * scale - 2, gy * scale - 2,
                       gx * scale + 2, gy * scale + 2], fill=dot)
    img.alpha_composite(_ghost(symbol_png, 380 * scale),
                        (860 * scale, 130 * scale))
    d.rectangle([0, 616 * scale, w, 626 * scale], fill=EMBER)

    lead = _lead_image(lead_png or wordmark_png, scale,
                       large=not subtitle)
    m = CARD_MARGIN * scale
    dom_f = load_font("SemiBold", 26 * scale)
    dom_y = 552 * scale

    if subtitle:
        lead_y = 100 * scale
        sub_f = load_font("Regular", 30 * scale)
        lines = _wrap(d, subtitle, sub_f, CARD_TEXT_W * scale)
        sub_y = lead_y + lead.height + 42 * scale
        line_h = 44 * scale
        _checks([
            ("subtitle fits three lines", len(lines) <= 3),
            ("subtitle clear of the ghost column",
             all(d.textlength(t, font=sub_f) <= CARD_TEXT_W * scale
                 for t in lines)),
            ("subtitle clear of the domain line",
             sub_y + len(lines) * line_h < dom_y - 10 * scale),
            ("domain clear of the rule",
             dom_y + 34 * scale < 616 * scale),
        ])
        img.alpha_composite(lead, (m, lead_y))
        for i, t in enumerate(lines):
            d.text((m, sub_y + i * line_h), t, font=sub_f,
                   fill=text_fill)
    else:
        lead_y = (540 * scale - lead.height) // 2
        _checks([
            ("lead clear of the ghost column",
             m + lead.width < 860 * scale),
            ("lead clear of the domain line",
             lead_y + lead.height < dom_y - 10 * scale),
            ("domain clear of the rule",
             dom_y + 34 * scale < 616 * scale),
        ])
        img.alpha_composite(lead, (m, lead_y))

    d.text((m, dom_y), domain, font=dom_f, fill=dom_fill)
    _save(img, out)


def main():
    ap = argparse.ArgumentParser(
        description="Compose the profile banner and/or a 1280x640 "
                    "social card, with placement checks.")
    ap.add_argument("--out", help="banner output PNG path")
    ap.add_argument("--style", choices=["split", "symbol"],
                    default="split",
                    help="banner style: the abstract Sand/Ink split "
                         "(default since 2026-08-12) or the dark "
                         "wordmark-and-symbol design")
    ap.add_argument("--svg", help="with --style symbol: compose over "
                    "this SVG base instead of the generated one")
    ap.add_argument("--card-out", help="social-card output PNG path")
    ap.add_argument("--card-subtitle",
                    help="subtitle line for the social card")
    ap.add_argument("--card-theme", choices=["dark", "light"],
                    default="dark",
                    help="light swaps to the Sand ground with the Ink "
                         "wordmark and flat symbol (unless overridden)")
    ap.add_argument("--card-lead",
                    help="lead mark for the card in place of the "
                         "wordmark (e.g. the official GitHub Mark on "
                         "the repository card)")
    ap.add_argument("--wordmark",
                    default=os.path.join(PNGDIR,
                                         "logo_wordmark_reversed_1024.png"),
                    help="wordmark PNG (reversed variant, dark grounds)")
    ap.add_argument("--symbol",
                    default=os.path.join(PNGDIR,
                                         "logo_symbol_reversed_1024.png"),
                    help="symbol PNG for the ghost motif")
    ap.add_argument("--domain", default="groundedaipractice.co.uk")
    ap.add_argument("--scale", type=int, default=2)
    ap.add_argument("--previews", action="store_true",
                    help="with --out: also write mobile-crop and "
                         "desktop previews beside the banner")
    a = ap.parse_args()

    if not a.out and not a.card_out:
        ap.error("nothing to do: pass --out and/or --card-out")

    if a.out:
        if a.style == "split":
            compose_split_banner(a.out, a.scale, a.previews)
        else:
            compose_banner(a.out, a.svg, a.wordmark, a.symbol,
                           a.domain, a.scale, a.previews)
    if a.card_out:
        wm, sym = a.wordmark, a.symbol
        if a.card_theme == "light":
            if wm == ap.get_default("wordmark"):
                wm = os.path.join(PNGDIR, "logo_wordmark_1024.png")
            if sym == ap.get_default("symbol"):
                sym = os.path.join(PNGDIR, "logo_symbol_flat_1024.png")
        compose_card(a.card_out, a.card_subtitle, wm, sym,
                     a.domain, a.scale, a.card_theme, a.card_lead)


if __name__ == "__main__":
    main()
