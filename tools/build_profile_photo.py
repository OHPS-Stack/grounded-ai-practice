"""Recompose a headshot over brand grounds, locally.

Why this exists: the profile photo and the banner are the two images
a profile viewer sees together, and a phone-snap background ties the
photo to wherever it was taken rather than to the identity around it.
The fix is background replacement — but a personal likeness does not
go to a web background-remover, so segmentation runs through rembg's
local U²-Net model: the photo never leaves the machine, which is the
entire reason this tool exists instead of a browser tab.

What it does: cuts the subject out once, then composes variants on
the brand grounds — Sand and Mist flats with the Ember rule drawn
behind the subject (echoing the banner's split), the literal
Sand-over-Ink split, and a plain control — plus a circle-crop preview
of each (how the platform actually displays it) and a labelled
contact sheet for choosing from. Output size follows the source; it
never upscales, because invented pixels on a face are exactly the
"AI-generated" look the recompose is meant to avoid.

Self-checks: the cutout's alpha coverage must land in a plausible
range for a head-and-shoulders crop (an empty or near-total mask
means segmentation failed), and a clipped-head warning fires if the
top row carries subject. Edge quality is not machine-checkable —
the contact sheet gets a human read, per the geometry rule.

Requires: Python with Pillow and rembg (``pip install "rembg[cpu]"``;
first run downloads the model to the user folder). Outputs carry a
personal likeness: keep them under ``internal/``, never tracked.

Command-line by the Entry 049 decision — a build step, not a
learner-facing tool.
"""

import argparse
import os
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from build_linkedin_banner import INK, EMBER, SAND3, load_font  # noqa: E402

MIST = (239, 238, 237)

VARIANTS = ["a_sand_rule", "b_mist_rule", "c_split", "d_sand_plain"]


def cutout(photo_path):
    from rembg import remove
    src = Image.open(photo_path).convert("RGB")
    if src.width != src.height:
        side = min(src.size)
        left = (src.width - side) // 2
        src = src.crop((left, 0, left + side, side))
    cut = remove(src)
    hist = cut.split()[3].histogram()
    cover = sum(hist[129:]) / (cut.width * cut.height)
    print(f"  cutout alpha coverage: {cover:.0%}")
    if not 0.15 <= cover <= 0.85:
        raise SystemExit("segmentation looks wrong (coverage outside "
                         "15-85%); not composing")
    top = cut.crop((0, 0, cut.width, 2)).split()[3]
    if top.getextrema()[1] > 128:
        print("  NOTE: subject touches the top edge (head may be "
              "clipped in the source crop)")
    return src.size[0], cut


def ground(side, variant, rule_frac):
    img = Image.new("RGBA", (side, side), SAND3 + (255,))
    d = ImageDraw.Draw(img)
    ry = round(side * rule_frac)
    rh = max(6, side // 44)
    if variant == "b_mist_rule":
        d.rectangle([0, 0, side, side], fill=MIST)
    if variant in ("a_sand_rule", "b_mist_rule"):
        d.rectangle([0, ry, side, ry + rh], fill=EMBER)
    elif variant == "c_split":
        d.rectangle([0, ry, side, ry + rh], fill=EMBER)
        d.rectangle([0, ry + rh, side, side], fill=INK)
    return img


def circle_preview(img):
    side = img.width
    mask = Image.new("L", (side * 4, side * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, side * 4, side * 4), fill=255)
    mask = mask.resize((side, side), Image.LANCZOS)
    out = Image.new("RGB", (side, side), (255, 255, 255))
    out.paste(img.convert("RGB"), (0, 0), mask)
    return out


def build(photo, out_dir, rule_frac):
    os.makedirs(out_dir, exist_ok=True)
    side, cut = cutout(photo)
    previews = []
    for v in VARIANTS:
        img = ground(side, v, rule_frac)
        img.alpha_composite(cut)
        p = os.path.join(out_dir, f"headshot_{v}.png")
        img.convert("RGB").save(p)
        print(f"wrote {p}")
        previews.append((v, circle_preview(img)))

    cell = side + 40
    label_f = load_font("SemiBold", max(16, side // 18))
    sheet = Image.new("RGB", (cell * 2 + 20, cell * 2 + 60),
                      (255, 255, 255))
    d = ImageDraw.Draw(sheet)
    for i, (v, pv) in enumerate(previews):
        x = 20 + (i % 2) * cell
        y = 20 + (i // 2) * cell
        sheet.paste(pv, (x, y))
        d.text((x + side // 2, y + side + 8), v.replace("_", " "),
               font=label_f, fill=INK, anchor="ma")
    sp = os.path.join(out_dir, "headshot_contact_sheet.png")
    sheet.save(sp)
    print(f"wrote {sp}")


def main():
    ap = argparse.ArgumentParser(
        description="Recompose a headshot over brand grounds using "
                    "local segmentation.")
    ap.add_argument("--photo", required=True, help="source headshot")
    ap.add_argument("--out-dir", required=True,
                    help="output folder (keep under internal/)")
    ap.add_argument("--rule-frac", type=float, default=0.68,
                    help="Ember rule height as a fraction of the side")
    a = ap.parse_args()
    build(a.photo, a.out_dir, a.rule_frac)


if __name__ == "__main__":
    main()
