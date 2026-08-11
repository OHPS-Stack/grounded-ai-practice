#!/usr/bin/env python3
"""Audit a chart colour set for contrast, colour-vision safety and greyscale survival.

Why this exists
---------------
The brand palette in `project_brief.md` is settled, but it was designed for
a *page*: one accent (Ember), two neutrals and four near-white grounds. A
chart needs something the page never did — several colours that stay
distinguishable *from each other* while sitting on the same background.
Picking those by eye is exactly the failure mode this project avoids
elsewhere: nobody can see a red/green confusion by looking at it with
normal colour vision, and a set that reads clearly on screen can collapse
to four identical greys in a printed Word document.

All three failures are arithmetic, so all three are checkable. This tool
does the checking, and `build_site_figures.py` should call it before
drawing anything, the same way it already refuses to build on a WCAG
contrast failure.

How it works
------------
Four independent checks per candidate set:

* **Contrast** — WCAG 2.1 ratio of every series colour against both
  grounds (Paper for light figures, Ink for dark). Marks carrying meaning
  are graphical objects under SC 1.4.11, so the threshold is 3:1, not the
  4.5:1 used for body text.

* **Separation** — pairwise perceptual distance in OKLab, which is
  near-uniform, so one threshold holds across the whole space (CIELAB's
  does not).

* **Colour-vision deficiency** — the same pairwise distances recomputed
  through Machado, Oliveira & Fernandes (2009) severity-1.0 matrices for
  protanopia, deuteranopia and tritanopia, applied in linear RGB as that
  paper specifies.

* **Greyscale** — lightness separation alone, which is what survives
  achromatopsia, a monochrome printer, and a photocopied handout.

The separation threshold is **calibrated, not invented**: it is derived
from the Okabe-Ito colour-universal set, which is long-established as
CVD-safe. Run `--calibrate` to print the weakest pair in that set under
every simulation. A candidate is judged against what a known-good set
actually achieves rather than against a number chosen to be passed.

A build utility in the `build_site_figures.py` / `embed_logo.py` category:
Claude or a build step runs it, not a learner, so it stays command-line by
the Entry 049 decision.

Requirements: Python, standard library only.

Usage
-----
    python tools/palette_check.py --calibrate        # derive thresholds
    python tools/palette_check.py --audit SET        # audit one named set
    python tools/palette_check.py --audit all        # audit every set
    python tools/palette_check.py --oklch SET        # print OKLCH values
    python tools/palette_check.py --proof out.svg    # render the proof sheet
"""

import argparse
import sys

# ----------------------------------------------------------------- palette

PALETTE = {
    "ink":      "#27221E",
    "ember":    "#F15E4B",
    "sand":     "#F9E8DC",
    "paper":    "#F9F9F9",
    "mist":     "#EFEEED",
    "sage":     "#D5E2E1",
    "stone":    "#6E6E6E",
    "graphite": "#404040",
}

# The reference set every threshold here is calibrated against. Okabe &
# Ito, "Color Universal Design" (2008) — the eight-colour qualitative set
# designed for colour-universal design, minus its white/black anchors.
OKABE_ITO = {
    "orange":         "#E69F00",
    "sky blue":       "#56B4E9",
    "bluish green":   "#009E73",
    "yellow":         "#F0E442",
    "blue":           "#0072B2",
    "vermillion":     "#D55E00",
    "reddish purple": "#CC79A7",
}

# --------------------------------------------------------- colour science

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#" + "".join(f"{max(0, min(255, round(c * 255))):02X}" for c in rgb)


def srgb_to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def linear_to_srgb(c):
    c = max(0.0, min(1.0, c))
    return c * 12.92 if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055


def luminance(hexcolor):
    r, g, b = (srgb_to_linear(c) for c in hex_to_rgb(hexcolor))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    l1, l2 = sorted((luminance(a), luminance(b)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


# Ottosson's OKLab. Perceptually near-uniform, so a single distance
# threshold is meaningful everywhere in the space.

def hex_to_oklab(hexcolor):
    r, g, b = (srgb_to_linear(c) for c in hex_to_rgb(hexcolor))
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = (v ** (1 / 3) if v > 0 else -((-v) ** (1 / 3))
                  for v in (l, m, s))
    return (
        0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
        1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
        0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_,
    )


def oklab_to_hex(lab):
    L, a, b = lab
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = (v ** 3 for v in (l_, m_, s_))
    lin = (
        +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    )
    return rgb_to_hex(tuple(linear_to_srgb(c) for c in lin))


def oklch(hexcolor):
    """(lightness 0-1, chroma, hue degrees) — the readable form."""
    import math
    L, a, b = hex_to_oklab(hexcolor)
    return L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360


def delta_e(a, b):
    """Euclidean distance in OKLab. Not CIEDE2000, and deliberately so:
    OKLab's uniformity is what makes a plain distance defensible here."""
    la, aa, ba = hex_to_oklab(a)
    lb, ab, bb = hex_to_oklab(b)
    return ((la - lb) ** 2 + (aa - ab) ** 2 + (ba - bb) ** 2) ** 0.5


# ------------------------------------------------------- the shared band
#
# A mark that must clear 3:1 against BOTH grounds is boxed in from two
# sides, and the box is narrow. Solving the WCAG ratio for the two grounds
# gives the only luminance range where a single colour can serve a light
# and a dark figure alike. This is the single most consequential number in
# the file: it is why the Okabe-Ito set cannot be adopted unaltered, its
# orange and purple both sitting outside it.

def shared_band():
    lp, li = luminance(PALETTE["paper"]), luminance(PALETTE["ink"])
    return (MARK_CONTRAST * (li + 0.05) - 0.05,
            (lp + 0.05) / MARK_CONTRAST - 0.05)


def _in_gamut(lab, eps=1e-3):
    """True if this OKLab value survives to sRGB without being clamped.
    oklab_to_hex clamps silently, so without this check the solver would
    happily return a colour that is not the one it solved for."""
    L, a, b = lab
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = (v ** 3 for v in (l_, m_, s_))
    lin = (
        +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    )
    return all(-eps <= c <= 1 + eps for c in lin)


def solve_hue(hue_deg, target_lum):
    """Most saturated in-gamut sRGB colour at this OKLab hue whose WCAG
    luminance is target_lum. Chroma descends until the colour both fits
    the gamut and actually hits the luminance target."""
    import math
    hr = math.radians(hue_deg)
    c = 0.40
    while c > 0.002:
        lo, hi = 0.0, 1.0
        for _ in range(48):
            mid = (lo + hi) / 2
            lab = (mid, c * math.cos(hr), c * math.sin(hr))
            if luminance(oklab_to_hex(lab)) < target_lum:
                lo = mid
            else:
                hi = mid
        lab = ((lo + hi) / 2, c * math.cos(hr), c * math.sin(hr))
        hx = oklab_to_hex(lab)
        if _in_gamut(lab) and abs(luminance(hx) - target_lum) < 0.002:
            return hx
        c -= 0.004
    return None


# Machado, Oliveira & Fernandes (2009), severity 1.0. Applied in LINEAR
# RGB as the paper specifies — applying these to gamma-encoded values is a
# common implementation error and shifts every result.
CVD_MATRICES = {
    "protanopia": (
        (0.152286, 1.052583, -0.204868),
        (0.114503, 0.786281, 0.099216),
        (-0.003882, -0.048116, 1.051998),
    ),
    "deuteranopia": (
        (0.367322, 0.860646, -0.227968),
        (0.280085, 0.672501, 0.047413),
        (-0.011820, 0.042940, 0.968881),
    ),
    "tritanopia": (
        (1.255528, -0.076749, -0.178779),
        (-0.078411, 0.930809, 0.147602),
        (0.004733, 0.691367, 0.303900),
    ),
}


def simulate(hexcolor, kind):
    if kind == "normal":
        return hexcolor
    if kind == "greyscale":
        # Relative luminance back out to a neutral — what a monochrome
        # printer does, and what achromatopsia leaves.
        y = luminance(hexcolor)
        return rgb_to_hex((linear_to_srgb(y),) * 3)
    m = CVD_MATRICES[kind]
    r, g, b = (srgb_to_linear(c) for c in hex_to_rgb(hexcolor))
    out = tuple(row[0] * r + row[1] * g + row[2] * b for row in m)
    return rgb_to_hex(tuple(linear_to_srgb(c) for c in out))


VISIONS = ["normal", "protanopia", "deuteranopia", "tritanopia", "greyscale"]


# ------------------------------------------------------------- candidates
#
# Every set leads with Ember, because a GAP figure's highlighted series is
# Ember by brand rule; the question each set answers is only what stands
# beside it.

def ramp(a, b, n):
    """Even steps between two colours through OKLab. Used for ordered data.
    Interpolating toward a brand neutral is what keeps a ramp on-brand:
    darkening at constant hue while maximising chroma — the obvious
    approach — walks Ember into saturated magenta, which is both off-brand
    and not what 'more of the same thing' should look like."""
    la, lb = hex_to_oklab(a), hex_to_oklab(b)
    return [oklab_to_hex(tuple(la[i] + (lb[i] - la[i]) * (k / (n - 1))
                               for i in range(3))) for k in range(n)]


# The settled system, in three tiers. Tier sizes are capped by measurement,
# not preference: `--solve` demonstrates that no five-colour categorical
# set clears the CVD floor inside GAP's contrast constraints, on either
# ground, so the cap at three is a finding rather than a style choice.

SETTLED = {
    # Tier 1 — highlight against context. The default, and already the
    # project's de facto practice: adoption_gap.svg greys two bars and
    # Embers the third. Ground-dependent by nature, so it is a role map
    # with a light and a dark reading, matching build_site_figures.theme().
    "tier1_light": [("Highlight", "#F15E4B"), ("Context", "#27221E"),
                    ("De-emphasis", "#6E6E6E")],
    # De-emphasis is Stone, not Mist. Mist reads as a de-emphasised Paper
    # on a page, which is its job there, but as two chart marks the pair
    # is dE 0.033 — less than half the separation floor, and visibly one
    # colour. Caught by looking at the proof sheet, not by the audit,
    # which had not been pointed at this set.
    "tier1_dark":  [("Highlight", "#F15E4B"), ("Context", "#F9F9F9"),
                    ("De-emphasis", "#6E6E6E")],

    # Tier 2 — nominal categories, five colours, one set per ground.
    #
    # The hues are designed, not optimised: Ember (30) is the brand's warm
    # pole and Sage (191) its cool one, so Gold sits between them and Slate
    # and Plum extend past Sage. Only the *lightness* of each was searched,
    # which is what carries the set through colour-vision deficiency —
    # under red-green CVD hue collapses and lightness is what survives.
    #
    # Optimising separation directly instead produced #0003D4, #EEE900 and
    # #3CFBF6: maximally distinguishable and nothing to do with this brand.
    # Separation is the constraint here, brand coherence the objective.
    "tier2_light": [("Ember", "#F15E4B"), ("Gold", "#774D04"),
                    ("Sage deep", "#0CA1A2"), ("Slate", "#00579F"),
                    ("Plum", "#5F014E")],
    # Plum is a dusty rose, not the #FDC3EB the search first returned. That
    # one cleared every threshold and read as candy pink: chroma 0.083
    # against 0.000-0.025 for every non-Ember colour in the brand. Picked
    # by listing all 986 valid options for the slot and sorting by chroma
    # rather than by separation — the same reversal that fixed tier 2 as a
    # whole. This one is chroma 0.028 and improves the margin as well.
    "tier2_dark":  [("Ember", "#F15E4B"), ("Gold", "#FBA929"),
                    ("Sage deep", "#2DA9AB"), ("Slate", "#006EC5"),
                    ("Plum", "#E6CFD8")],
}

# Tier 3 — ordered data. Not audited as a categorical set: adjacent steps
# in a ramp are meant to be close, and judging them against the CVD
# separation floor asks the wrong question. What a ramp must do is stay
# monotonic in lightness, which is also why it is the only part of this
# system that survives greyscale.
SETTLED["tier3_light"] = [(f"S{i+1}", h) for i, h in
                          enumerate(ramp(PALETTE["ember"], PALETTE["ink"], 3))]
SETTLED["tier3_dark"] = [(f"S{i+1}", h) for i, h in
                         enumerate(ramp(PALETTE["ember"], PALETTE["sand"], 3))]


CANDIDATES = {
    # The project's current de facto practice, formalised. adoption_gap.svg
    # already does exactly this: Ember for the series being argued about,
    # neutrals for the context. Storytelling-with-data's grey-everything-
    # except-the-point, arrived at independently.
    "editorial": [
        ("Ember",    "#F15E4B"),
        ("Ink",      "#27221E"),
        ("Stone",    "#6E6E6E"),
        ("Mist",     "#EFEEED"),
    ],

    # Okabe-Ito with Ember substituted for its vermillion slot. Maximally
    # safe if the substitution survives; the blues and greens are the
    # least GAP-like thing in this file.
    "universal": [
        ("Ember",    "#F15E4B"),
        ("Blue",     "#0072B2"),
        ("Green",    "#009E73"),
        ("Orange",   "#E69F00"),
        ("Purple",   "#CC79A7"),
    ],

    # The middle option: Okabe-Ito's hue *positions* held, but chroma and
    # lightness pulled toward the GAP palette's warmer, quieter character.
    # Deliberately less saturated than `universal`.
    "warmed": [
        ("Ember",    "#F15E4B"),
        ("Deep sage", "#3E6B66"),
        ("Slate",    "#2F5D7C"),
        ("Ochre",    "#C68A3E"),
        ("Plum",     "#8C5A72"),
    ],

    # Ordered data — firm size, budget tranches, time buckets — is not
    # categorical and should not use a categorical scale. Ember-anchored
    # sequential ramp for those cases.
    "sequential": [
        ("Ember",    "#F15E4B"),
        ("Step 2",   "#D46A55"),
        ("Step 3",   "#A9705F"),
        ("Step 4",   "#7A6B5C"),
        ("Step 5",   "#4A5B54"),
    ],
}


# ------------------------------------------------------------------ audit

# WCAG 2.1 SC 1.4.11: graphical objects conveying meaning need 3:1
# against adjacent colour. Chart marks are graphical objects.
MARK_CONTRAST = 3.0

GROUNDS = [("paper", PALETTE["paper"]), ("ink", PALETTE["ink"])]


def calibrate():
    """Derive separation thresholds from the Okabe-Ito set rather than
    inventing them. Prints the weakest pair under each simulation."""
    names = list(OKABE_ITO)
    print("Calibration — Okabe-Ito colour-universal set (7 colours, 21 pairs)")
    print("The weakest pair under each simulation is the bar a candidate")
    print("set has to clear, since this set is established as CVD-safe.\n")
    worst = {}
    for vision in VISIONS:
        lo, pair = 99.0, None
        for i, a in enumerate(names):
            for b in names[i + 1:]:
                d = delta_e(simulate(OKABE_ITO[a], vision),
                            simulate(OKABE_ITO[b], vision))
                if d < lo:
                    lo, pair = d, (a, b)
        worst[vision] = lo
        print(f"  {vision:<13} weakest dE {lo:5.3f}   ({pair[0]} / {pair[1]})")
    floor = min(worst[v] for v in VISIONS if v != "greyscale")
    print(f"\n  colour floor  {floor:5.3f}   (worst across the three CVD types)")
    print(f"  grey floor    {worst['greyscale']:5.3f}")
    return floor, worst["greyscale"]


def audit(name, colours, floor, grey_floor, verbose=True):
    """Check one candidate set. Returns a list of failure strings."""
    fails = []
    if verbose:
        print(f"\n{'=' * 66}\n{name}  ({len(colours)} colours)\n{'=' * 66}")

    # 1. contrast, against the ground(s) this set is actually for. A set
    # named _light is for light figures; checking its Ink-coloured context
    # mark against an Ink ground asks a question the set never claimed to
    # answer, and a tool that reports failures nobody should act on is a
    # tool people learn to skip.
    if name.endswith("_light"):
        grounds = [("paper", PALETTE["paper"])]
    elif name.endswith("_dark"):
        grounds = [("ink", PALETTE["ink"])]
    else:
        grounds = GROUNDS
    if verbose:
        print("\n  contrast against grounds (need 3.0:1, SC 1.4.11)")
    for label, hexv in colours:
        for gname, ghex in grounds:
            ratio = contrast(hexv, ghex)
            ok = ratio >= MARK_CONTRAST
            if verbose:
                print(f"    {label:<10} on {gname:<6} {ratio:5.2f}:1  "
                      f"{'ok' if ok else 'FAIL'}")
            if not ok:
                fails.append(f"{name}: {label} on {gname} = {ratio:.2f}:1")

    # 2/3/4. pairwise separation, normal + CVD + greyscale
    if verbose:
        print("\n  weakest pair under each simulation")
    for vision in VISIONS:
        lo, pair = 99.0, None
        for i, (la, ha) in enumerate(colours):
            for lb, hb in colours[i + 1:]:
                d = delta_e(simulate(ha, vision), simulate(hb, vision))
                if d < lo:
                    lo, pair = d, (la, lb)
        # Greyscale is reported, never enforced, on a categorical set. The
        # Okabe-Ito reference itself manages only dE 0.006 in greyscale, so
        # there is no honest threshold to hold a candidate to — the correct
        # response to a low number here is not a different palette but a
        # figure that does not make colour carry the meaning.
        if vision == "greyscale":
            if verbose:
                print(f"    {vision:<13} dE {lo:5.3f}  (informational; "
                      f"Okabe-Ito manages {grey_floor:.3f})   "
                      f"({pair[0]} / {pair[1]})")
            continue
        ok = lo >= floor
        if verbose:
            print(f"    {vision:<13} dE {lo:5.3f}  need {floor:5.3f}  "
                  f"{'ok' if ok else 'FAIL'}   ({pair[0]} / {pair[1]})")
        if not ok:
            fails.append(f"{name}: {vision} {pair[0]}/{pair[1]} "
                         f"dE {lo:.3f} < {floor:.3f}")
    return fails


def solve_set(spread, floor, grey_floor, keep_ember=True):
    """Build a candidate set on the Okabe-Ito hue angles, placed inside the
    shared band. `spread` staircases luminance across the band instead of
    holding it constant: constant luminance is the textbook advice for
    categorical scales, because varying it implies an order that nominal
    data does not have — but it also guarantees the set vanishes in
    greyscale. Both are computed so the trade is visible rather than
    assumed."""
    lo, hi = shared_band()
    lo, hi = lo + 0.010, hi - 0.010          # headroom off the 3:1 edges
    hues = [(n, oklch(h)[2]) for n, h in OKABE_ITO.items()
            if n in ("blue", "bluish green", "reddish purple", "orange")]
    ember_l = luminance(PALETTE["ember"])
    out = [("Ember", PALETTE["ember"])] if keep_ember else []
    n = len(hues)
    for i, (name, hue) in enumerate(hues):
        target = (lo + (hi - lo) * i / max(1, n - 1)) if spread else (lo + hi) / 2
        if keep_ember and abs(target - ember_l) < 0.012:
            target = lo + (hi - lo) * 0.5
        hx = solve_hue(hue, target)
        out.append((name.title(), hx if hx else "#808080"))
    return out


def audit_ordered(name, colours):
    """Ordered ramps get different questions. Adjacent steps in a ramp are
    supposed to be close, so the categorical separation floor would fail a
    correct ramp; what matters instead is that lightness moves one way
    only, that neighbours are still separable, and that the ends are far
    apart. Monotonic lightness is also why a ramp is the only part of this
    system that survives greyscale."""
    fails = []
    print(f"\n{'=' * 66}\n{name}  ({len(colours)} steps, ordered)\n{'=' * 66}")
    ground = PALETTE["ink"] if name.endswith("_dark") else PALETTE["paper"]
    gname = "ink" if name.endswith("_dark") else "paper"

    print(f"\n  contrast against {gname} (need 3.0:1)")
    for label, hexv in colours:
        r = contrast(hexv, ground)
        print(f"    {label:<10} {hexv}  {r:5.2f}:1  {'ok' if r >= MARK_CONTRAST else 'FAIL'}")
        if r < MARK_CONTRAST:
            fails.append(f"{name}: {label} on {gname} = {r:.2f}:1")

    lums = [luminance(h) for _, h in colours]
    mono = (all(lums[i] > lums[i + 1] for i in range(len(lums) - 1)) or
            all(lums[i] < lums[i + 1] for i in range(len(lums) - 1)))
    adj = min(delta_e(colours[i][1], colours[i + 1][1])
              for i in range(len(colours) - 1))
    ends = delta_e(colours[0][1], colours[-1][1])
    grey = delta_e(simulate(colours[0][1], "greyscale"),
                   simulate(colours[-1][1], "greyscale"))
    print(f"\n  monotonic lightness   {mono}")
    print(f"  weakest adjacent      dE {adj:.3f}")
    print(f"  endpoint separation   dE {ends:.3f}")
    print(f"  greyscale span        dE {grey:.3f}")
    if not mono:
        fails.append(f"{name}: lightness not monotonic")
    return fails


def show_oklch(name, colours):
    print(f"\n{name} — OKLCH")
    print(f"  {'':<10} {'hex':<9} {'L':>6} {'C':>6} {'H':>7}")
    for label, hexv in colours:
        L, C, H = oklch(hexv)
        print(f"  {label:<10} {hexv:<9} {L:6.3f} {C:6.3f} {H:7.1f}")


# ------------------------------------------------------------ proof sheet

def proof_sheet(path, which=None):
    """Render each tier as swatches, as bars and as thin lines, under all
    five simulations, on the ground it is actually for. A palette cannot be
    judged as swatches alone — the same set that reads clearly in a 60px
    block can be indistinguishable as a 3px line, which is what a line
    chart uses. Nor can it be judged from numbers, which is the reason this
    exists at all: the audit says a set passes, this says what it looks
    like."""
    src = which if which is not None else SETTLED
    sets = list(src.items())
    dark_bg = {n: n.endswith("_dark") for n, _ in sets}
    row_h = 132
    block_h = 34
    head = 92
    width = 1180
    height = head + sum(row_h * (len(c) > 0) for _, c in sets) * len(VISIONS) // 1
    # one band per (set, vision)
    bands = [(n, c, v) for n, c in sets for v in VISIONS]
    height = head + len(bands) * block_h + len(sets) * 46 + 60

    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
         f'width="{width}" height="{height}" role="img">']
    o.append(f'<rect width="{width}" height="{height}" fill="{PALETTE["paper"]}"/>')
    f = ("font-family=\"'Public Sans','Segoe UI',Arial,sans-serif\"")
    o.append(f'<text x="40" y="52" {f} font-size="26" font-weight="700" '
             f'fill="{PALETTE["ink"]}">Categorical palette candidates</text>')
    o.append(f'<text x="40" y="76" {f} font-size="14" '
             f'fill="{PALETTE["graphite"]}">Each set shown as swatches, as bars '
             f'and as 3px lines, under normal vision, three colour-vision '
             f'deficiencies and greyscale.</text>')

    y = head
    for sname, colours in sets:
        band_top = y
        band_h = 34 + block_h * len(VISIONS)
        if dark_bg.get(sname):
            o.append(f'<rect x="24" y="{band_top - 6}" width="{width - 48}" '
                     f'height="{band_h + 6}" fill="{PALETTE["ink"]}"/>')
        tcol = PALETTE["paper"] if dark_bg.get(sname) else PALETTE["ink"]
        scol = PALETTE["mist"] if dark_bg.get(sname) else PALETTE["stone"]
        o.append(f'<text x="40" y="{y + 18}" {f} font-size="17" '
                 f'font-weight="700" fill="{tcol}">{sname}</text>')
        y += 34
        for vision in VISIONS:
            o.append(f'<text x="40" y="{y + 21}" {f} font-size="12" '
                     f'fill="{scol}">{vision}</text>')
            x = 150
            for _, hexv in colours:
                c = simulate(hexv, vision)
                o.append(f'<rect x="{x}" y="{y + 4}" width="64" height="26" '
                         f'rx="4" fill="{c}"/>')
                x += 70
            # bars, varying height so they read as a chart not a legend
            x = 150 + 70 * len(colours) + 40
            for i, (_, hexv) in enumerate(colours):
                c = simulate(hexv, vision)
                bh = 26 - i * 3
                o.append(f'<rect x="{x}" y="{y + 4 + (26 - bh)}" width="26" '
                         f'height="{bh}" fill="{c}"/>')
                x += 32
            # thin lines — the hardest test
            x = x + 40
            for i, (_, hexv) in enumerate(colours):
                c = simulate(hexv, vision)
                yy = y + 8 + i * 4
                o.append(f'<line x1="{x}" y1="{yy}" x2="{x + 150}" y2="{yy}" '
                         f'stroke="{c}" stroke-width="3"/>')
            y += block_h
        y += 12

    o.append("</svg>")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(o))
    print(f"wrote {path}")


def proof_png(path, which=None):
    """The proof sheet as PNG. Same content as the SVG version, drawn with
    Pillow so it needs no SVG renderer — this project has no Inkscape on
    every machine, and a proof nobody can open is not a proof."""
    from PIL import Image, ImageDraw

    src = which if which is not None else SETTLED
    sets = list(src.items())
    sw, gap, row = 78, 8, 40
    head, pad = 96, 40
    height = head + sum(40 + row * len(VISIONS) + 16 for _ in sets) + 40
    width = 1240
    img = Image.new("RGB", (width, height), PALETTE["paper"])
    d = ImageDraw.Draw(img)
    d.text((pad, 34), "Categorical palette — settled system, proof sheet",
           fill=PALETTE["ink"])
    d.text((pad, 56), "swatches | bars | 3px lines, under normal vision, "
                      "three CVD types and greyscale", fill=PALETTE["graphite"])

    y = head
    for sname, colours in sets:
        dark = sname.endswith("_dark")
        bh = 40 + row * len(VISIONS) + 8
        if dark:
            d.rectangle([24, y - 8, width - 24, y + bh], fill=PALETTE["ink"])
        tcol = PALETTE["paper"] if dark else PALETTE["ink"]
        scol = PALETTE["mist"] if dark else PALETTE["stone"]
        d.text((pad, y), f"{sname}   ({len(colours)} colours)", fill=tcol)
        y += 26
        for vision in VISIONS:
            d.text((pad, y + 12), vision, fill=scol)
            x = 170
            for _, hexv in colours:
                d.rectangle([x, y + 4, x + sw, y + row - 10],
                            fill=simulate(hexv, vision))
                x += sw + gap
            x += 40
            for i, (_, hexv) in enumerate(colours):
                h = (row - 14) - i * 4
                d.rectangle([x, y + 4 + ((row - 14) - h), x + 30, y + row - 10],
                            fill=simulate(hexv, vision))
                x += 36
            x += 40
            for i, (_, hexv) in enumerate(colours):
                yy = y + 8 + i * 6
                d.rectangle([x, yy, x + 190, yy + 3],
                            fill=simulate(hexv, vision))
            y += row
        y += 24
    img.save(path)
    print(f"wrote {path}  ({width}x{height})")


# ------------------------------------------------------------------- main

def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--calibrate", action="store_true",
                   help="derive thresholds from the Okabe-Ito set")
    p.add_argument("--audit", metavar="SET",
                   help="audit a named candidate set, or 'all'")
    p.add_argument("--oklch", metavar="SET", help="print OKLCH values")
    p.add_argument("--proof", metavar="PATH", help="render the proof sheet")
    p.add_argument("--solve", action="store_true",
                   help="solve candidate sets inside the shared band")
    a = p.parse_args()

    if a.solve:
        lo, hi = shared_band()
        print(f"shared band (3:1 on Paper and Ink): {lo:.4f} - {hi:.4f}\n")
        floor, grey_floor = calibrate()
        for spread in (False, True):
            label = "solved-spread" if spread else "solved-flat"
            s = solve_set(spread, floor, grey_floor)
            CANDIDATES[label] = s
            show_oklch(label, s)
            audit(label, s, floor, grey_floor)
        return 0

    if not any((a.calibrate, a.audit, a.oklch, a.proof)):
        p.print_help()
        return 0

    floor = grey_floor = None
    if a.calibrate or a.audit:
        floor, grey_floor = calibrate()

    if a.audit:
        # SETTLED first: a name in both resolves to the settled reading.
        pool = {**CANDIDATES, **SETTLED}
        if a.audit == "all":
            names = list(pool)
        elif a.audit == "settled":
            names = list(SETTLED)
        else:
            names = [a.audit]
        allfails = []
        for n in names:
            if n not in pool:
                print(f"unknown set: {n}\navailable: "
                      f"{', '.join(pool)}, settled, all", file=sys.stderr)
                return 2
            if n.startswith("tier3"):
                allfails += audit_ordered(n, pool[n])
            else:
                allfails += audit(n, pool[n], floor, grey_floor)
        print(f"\n{'=' * 66}")
        if allfails:
            print(f"{len(allfails)} failure(s):")
            for x in allfails:
                print(f"  {x}")
        else:
            print("all audited sets pass")

    if a.oklch:
        names = list(CANDIDATES) if a.oklch == "all" else [a.oklch]
        for n in names:
            show_oklch(n, CANDIDATES[n])

    if a.proof:
        if a.proof.lower().endswith(".png"):
            proof_png(a.proof)
        else:
            proof_sheet(a.proof)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
