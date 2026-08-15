# Icon library — Lucide icons converted to the GAP set

Icons here come from [Lucide](https://lucide.dev/), pinned at release
**1.31.0**, and are converted into this project's own icon geometry and
palette by `tools/gap_icon.py`. They sit beside the 36 bespoke icons in
`assets/icons/svg/` and are meant to be usable in the same places — the
landing site's icon wells, figures, and document callouts.

## Why these are converted rather than copied

Lucide draws the way this project's icons draw: stroke outline, no fill,
round caps and joins. The proportions differ sharply, though. Lucide works
on a 24 grid at stroke-width 2; the GAP icons work on a 512 canvas at
stroke-width 14. Scaled naively to 512 a Lucide icon arrives at
stroke-width 42.7 — roughly three times heavier than the set it is joining
— and fills 83% of its canvas where the GAP icons fill 70%. Beside a
bespoke icon it would read as a second, louder system.

So each icon is refitted. Its longest axis, stroke included, is measured by
rendering and placed on 358.4 units, 70.0% of the canvas, centred — the
convention the bespoke set already follows, measured off `verification`,
`storage` and `terminal_and_cli`, which agree on it to within 0.4%. The
stroke is set to 14 canvas units. Path data is never rewritten: the
original elements are wrapped in a transformed `icon_canvas` group, exactly
as the bespoke icons are.

Every icon is single-colour Ink `#27221E` unless an Ember `#F15E4B` accent
was chosen for it by hand. Which element earns the accent is a judgement,
not something the tool guesses — the manifest below records where one was
applied.

## Licence and attribution

Lucide is published under the **ISC License** (Copyright © 2026 Lucide
Icons and Contributors), with icons derived from Feather under the **MIT
License** (Copyright © 2013-present Cole Bemis). Both permit modification
and redistribution provided the copyright notice and permission notice
travel with the files.

The full licence text is in `LICENSE` beside this file, fetched from the
pinned release. It must stay here for as long as any icon in this folder
does — that is the entire condition both licences impose, and the
converted files are derivative works, so it applies to them too.

The conversion changes geometry and colour only. No icon is redrawn, and
no icon is presented as this project's own design.

## Adding one

Browse names at [lucide.dev/icons](https://lucide.dev/icons/), then:

```bash
python tools/gap_icon.py shield-check
```

Run it once with no `--accent` to see the icon's elements and their
indices, then again naming the one that should be Ember:

```bash
python tools/gap_icon.py shield-check --accent 1 --refresh
```

Notes worth knowing before you use it:

- The pinned version is deliberate. `main` and `@latest` would make a
  rebuild months from now produce a different file, and the `brand_icons/`
  folder already carries that weakness.

- Nothing is written unless the output passes a geometry self-check —
  rendered again and verified for span, centring and canvas containment.

- The site serves its own copies from `docs/assets/icons/`. Adding an icon
  to a page means copying the SVG across as well, the same as for the
  bespoke set.

- PNGs are opt-in (`--png`, at 64/128/256px) rather than automatic, so the
  repo carries raster exports only where something needs them.

## Manifest

<!-- manifest:start -->
| File | Lucide source | Ember accent | Added |
|---|---|---|---|
| `banknote.svg` | `banknote` | yes | 2026-08-15 |
| `calendar_days.svg` | `calendar-days` | yes | 2026-08-15 |
| `landmark.svg` | `landmark` | no | 2026-08-15 |
| `shield_check.svg` | `shield-check` | yes | 2026-08-15 |
| `users.svg` | `users` | no | 2026-08-15 |
<!-- manifest:end -->

## If an icon is withdrawn upstream

Lucide removing or renaming an icon does not affect the copies here — they
are already converted and committed, and the pin means a rebuild fetches
the same release. If the project ever needs to stop using one, delete the
file, remove its manifest row, and replace its uses with a bespoke icon
from `assets/icons/svg/`. Same fallback as `assets/figures/brand_icons/`.
