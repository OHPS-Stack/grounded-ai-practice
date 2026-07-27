# Grounded AI Practice — Project Log

## Document status

Working document, maintained alongside `RESEARCH_LOG.md`. Split out from it
on 2026-07-27 (see Entry 017 below) once that file's research-only purpose
had drifted into a general dump for every kind of durable record.

## Purpose

Records scoping/creative decisions and design/production/technical work —
everything durable that is **not** source-backed research evidence (that
belongs in `RESEARCH_LOG.md`) and is **not** a standing current-state
summary (that belongs in `PROJECT_BRIEF.md`). Think of it as the
chronological "what happened and why" history behind the decisions
`PROJECT_BRIEF.md` currently reflects.

This log is intended to be maintained by Claude, not edited by hand. New
entries are appended as decisions are made or work is completed; existing
entries are not silently altered — corrections or supersessions are added
as new entries that reference the one they update, so history stays
traceable, consistent with `RESEARCH_LOG.md`'s own non-alteration
convention.

## How to read this log

Same entry shape as `RESEARCH_LOG.md`, adapted for content that usually has
no external citation:

| Field | Meaning |
|---|---|
| ID | Sequential entry number (this file's own sequence, separate from `RESEARCH_LOG.md`'s) |
| Date logged | When the entry was added |
| Priority / Question | Which `RESEARCH_QUESTIONS.md` priority this touches, if any — some entries (like this file's own creation) aren't tied to one |
| Source | Who decided or built something (the creator directly, or Claude Code on the creator's instruction) rather than an external citation |
| What happened | What changed, decided, or was built |
| Inference drawn | Any conclusion drawn beyond the plain fact, clearly marked as inference |
| Limitations / conflicting evidence | Usually "Not applicable" here — kept for structural consistency with `RESEARCH_LOG.md`, since this is a production record, not a claim needing corroboration |
| Effect on project direction | Whether this changes, confirms, or has no current effect on the brief |

---

## Log entries

### Entry 001 — First public output: working decision (Priority 5/7, answers immediate priority Q5)

- **Date logged:** 2026-07-24
- **Priority / Question:** Immediate research priority 5 — "What should the
  project build first to test these assumptions?" — and Priority 7's "What is
  the smallest useful public output that could test the project's core
  assumptions?"
- **Source:** Direct instruction from the project's creator, 2026-07-24,
  choosing between candidate options presented from the existing evidence
  base (no new sources fetched this entry).
- **What changed:** The creator decided the first build should be a **single
  pilot learning unit** — one core capability, PRIMES-sized (30–90 minutes,
  `SE-PRIMES-EMPLOYER26`), GRR-sequenced (`GRR-EBIP`) — tested with a small
  number of real learners before any wider course, roadmap or platform
  structure is built. This was chosen over two alternatives considered: (a)
  drafting a full competency-mapped skeleton pathway without full content, or
  (b) deferring the decision pending deeper research into the rest of
  Priority 7's sub-questions (accessibility, format relationships,
  install-free access).
- **Inference drawn:** None beyond the creator's own stated choice; the
  supporting rationale (pilot-first per `RS-AILIT25`; avoiding the "directory
  not programme" failure mode per `LSE-CARDOSO26`/`TECHOSAURUS26`/`HUMANCO26`;
  unit sizing/sequencing per `SE-PRIMES-EMPLOYER26`/`GRR-EBIP`) draws directly
  on entries already in this log (020–027, 034), not new research.
- **Limitations / conflicting evidence:** This decides the *shape* of the
  first output, not which capability it teaches, nor the project's permanent
  format — both remain open (see `PROJECT_BRIEF.md`). As previously flagged,
  `RS-AILIT25`'s pilot-first recommendation is drawn from a children's-
  education evidence base, and `GRR-EBIP`'s sequencing model is K-12-
  originated (Entry 027) — applying both to adult, self-directed learning is
  this project's own extension, not something either source tested directly.
- **Effect on project direction:** Recorded as a working decision in
  `PROJECT_BRIEF.md` ("First public output"). Converts four sessions of
  Priority 3–5 research into a concrete, testable next build step, consistent
  with the project's stated aim of reducing uncertainty before creating new
  structures. The immediate open question this raises — which single
  capability the pilot unit should teach — is the natural next decision
  point.

### Entry 002 — Second track confirmed: local AI workstation, seeded from inherited PAWH architecture

- **Date logged:** 2026-07-24
- **Priority / Question:** Immediate priority Q5 / Priority 7, continuing
  Entry 001's first-output decision; also touches Priority 6 (technical
  scope) via the inherited architecture's content.
- **Source:** Direct input from the project's creator, 2026-07-24 — a
  stack summary the creator obtained from a separate ChatGPT project that
  holds fuller context on the PAWH predecessor's original workstation
  design. Not an external/independent source; recorded as project
  provenance, not evidence.
- **What changed:** The creator confirmed the local/hybrid AI workstation
  (PowerShell/WSL2 fundamentals as its first module) should be a **second,
  parallel track**, not a replacement for the general-literacy pilot decided
  in Entry 001. The full inherited architecture (Windows 11 + Windows
  Terminal + WSL2 + Docker Compose running Ollama/Open WebUI, with
  SearXNG/Whisper/Qdrant, later Langflow/n8n/MCP integrations, considered)
  was recorded in `PROJECT_BRIEF.md` ("Inherited workstation architecture")
  as historical intent to evaluate, per the existing "Relationship to PAWH"
  convention — not a committed specification.
- **Inference drawn:** Terminal/shell basics is a sensible *first module of
  the workstation track specifically* (Docker, Ollama and everything after
  it in the described architecture depends on it) — this is the project's
  own reasoning, not stated by any external source. It would not be a
  sensible choice for the general-literacy pilot's audience (individuals/SME
  employees without an L&D layer), which the evidence base (Entries 017,
  019, 024, 026) consistently points toward practical/non-technical literacy
  content first, not command-line prerequisites.
- **Limitations / conflicting evidence:** None of this entry's content is
  independently sourced evidence — it's project-provenance context (the
  creator's own prior work) and a scope decision, not a new research finding.
  The two tracks' relationship (shared modules, sequencing, whether the
  workstation track needs its own audience research) is unaddressed.
- **Effect on project direction:** Unblocks work on the workstation track
  without disturbing the general-literacy pilot's status as the project's
  first tested output. Gives the workstation track a concrete architectural
  reference to design lessons against, while keeping the two tracks
  explicitly distinct in `PROJECT_BRIEF.md` so they aren't accidentally
  conflated in future sessions.

### Entry 003 — Visual identity: palette and logo-type decision (Priority 7/10)

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 7 (delivery format) touches on visual
  presentation; Priority 10 (sustainability/public presentation) — "visual
  identity beyond the approved project name" (`PROJECT_BRIEF.md`, "Not yet
  decided").
- **Source:** Direct creative decision by the project's creator, 2026-07-24
  — a design choice, not an evidence-based research finding, so this entry
  intentionally has no source-key citation.
- **What changed:** The creator finalised a six-colour palette (Ink, Ember,
  Sand, Paper, Mist, Sage — see `PROJECT_BRIEF.md`, "Visual identity"),
  confirmed an icon + wordmark logo type, and confirmed a tone positioned
  between "grounded/academic" and "approachable/friendly." The existing
  legacy PAWH icon set (`assets/brand/legacy-pawh-icons/`) was confirmed to
  use a superseded palette and now needs a recolour/overhaul pass — not
  done in this entry, flagged as future work.
- **Inference drawn:** None — a direct decision, not derived from evidence.
- **Limitations / conflicting evidence:** Not applicable — this is a design
  decision, not a factual claim requiring corroboration.
- **Effect on project direction:** Unblocks visual work on the pilot unit
  (Entry 001) once its core capability is chosen. The logo mark itself
  remains undesigned, and the legacy icon overhaul is unscheduled — both
  flagged in Open Threads.

### Entry 004 — Symbol-only candidate locked; wordmark pairing rejected

- **Date logged:** 2026-07-24
- **Priority / Question:** Continues Entry 003 (Priority 7/10, visual
  identity).
- **Source:** Direct creative decision by the project's creator, 2026-07-24
  — no source-key citation, as with Entry 003.
- **What changed:** Of the icon concepts sketched, the creator confirmed
  the recoloured evolution of the approved PAWH "terminal + handbook"
  symbol (geometry unchanged, recoloured flat to Ink/Ember/white) as
  correct and worth locking as a working candidate — saved to
  `assets/brand/logo/candidates/symbol_v01_terminal_handbook_recolour.svg`.
  The creator intends to further refine this candidate by editing its SVG
  paths directly. The wordmark tested alongside it ("Grounded AI Practice"
  in a placeholder bold sans, single-line or stacked) was rejected — it
  didn't match the symbol's style and read as too long and visually
  disconnected from the mark. Other symbol concepts remain to be explored;
  this candidate is not a final decision.
- **Inference drawn:** None — a direct decision, not derived from evidence.
- **Limitations / conflicting evidence:** Not applicable.
- **Effect on project direction:** First concrete logo asset now exists in
  the repo, but as an explicitly provisional candidate. Wordmark design is
  now a separately unresolved problem from the symbol — pairing a
  strong-existing-typeface wordmark with this specific symbol's style is an
  open task, not solved by this entry.

### Entry 005 — Inkscape handoff produced two improved candidates; shaded version preferred

- **Date logged:** 2026-07-24
- **Priority / Question:** Continues Entries 003/004 (Priority 7/10, visual
  identity).
- **Source:** Direct creative work by the project's creator in Inkscape,
  2026-07-24 — no source-key citation, as with prior visual-identity
  entries.
- **What changed:** Following the workflow handoff logged in the previous
  entry, the creator produced two refined symbol candidates directly in
  Inkscape: `GAP_logo_flat.svg` (flat Ink/Ember/Paper, proper corner
  fillets replacing the earlier hand-coded curve approximations) and
  `GAP_logo_shaded.svg` (the same geometry with added gradient shading — a
  book-cover gradient, a spine shadow, subtle page depth, and a rounded
  highlight on the Ember bar). The creator confirmed `GAP_logo_shaded.svg`
  as the current best version. The earlier AI-iteratively-edited file
  (`symbol_v01_terminal_handbook_recolour.svg`) has been removed.
- **Inference drawn:** The shaded version's gradient shading achieves the
  "3D/book effect" that earlier curve-asymmetry attempts (this log's Entry
  004 corner tweak) were only partially addressing — this is the project's
  own read of the outcome, not stated by any external source, but it's a
  reasonably direct visual comparison.
- **Limitations / conflicting evidence:** Not applicable — direct creative
  work, not a research finding.
- **Effect on project direction:** Confirms the workflow correction from
  the previous entry was the right call — the handoff produced a clearly
  better result than continued AI-iterative editing was achieving. Updates
  `PROJECT_BRIEF.md`'s "Visual identity" section to point at the current
  files. The wordmark pairing remains the next open piece, now against a
  meaningfully improved symbol.

### Entry 006 — Legacy PAWH icon set recoloured and structural flags fixed

- **Date logged:** 2026-07-24
- **Priority / Question:** Continues Entries 003–005 (Priority 7/10, visual
  identity) — closes the "legacy icon set needs recolour/overhaul" item
  open since Entry 003.
- **Source:** Direct work by Claude Code (bulk find/replace across all 35
  files, verified by grep) plus the project's creator's manual visual
  review of every icon; four targeted structural fixes reviewed/approved
  by the creator. No source-key citation, as with other visual-identity
  entries.
- **What changed:** All 35 icons in `assets/brand/legacy-pawh-icons/`
  recoloured from the superseded navy/orange palette to the current one.
  Full mapping: `#0F1C2F`→`#27221E` (Ink), `#FF5A1F`→`#F15E4B` (Ember),
  six assorted light-grey variants (`#D1D8E0`, `#AEB7C3`, `#E5E7EB`,
  `#E8EBEF`, `#C5CDD6`, `#8E97A8`)→`#D5E2E1` (Sage), and three one-off
  outlier colours found only in `B04-E`→their nearest palette equivalent.
  White (`#FFFFFF`) left unchanged. Verified via grep that no pre-recolour
  hex values remain anywhere in the set. The creator then manually checked
  every icon and confirmed correct rendering and colour application.
  Separately, four icons were flagged during the recolour pass for
  construction issues unrelated to colour and fixed: `B04-E`'s
  non-standard 1254×1254 viewBox normalised to 512×512 via a wrapping
  transform (no coordinates altered); `B05-L`'s stale
  CairoSVG-specific-rendering claim in its desc corrected (its paths use
  no renderer-specific features); `B04-C`'s intentionally-duplicated
  ink-ring/white-fill paths documented with a comment explaining why
  (needed for correct rendering on non-white backgrounds, not an
  accidental duplication); `B04-D`'s live `<text>` "API" element (the only
  text-based, font-dependent element in the whole set) removed at the
  creator's request, left empty for manual type-setting in Inkscape. Four
  other icons (`B02-E`, `B05-B`, `B05-F`, `B03-A`) were flagged only for
  unusually high prior revision counts (v08–v10 vs. v01–v03 typical), not
  any identified defect — cleared without changes after the creator's
  manual review found no problem.
- **Inference drawn:** None beyond what's stated — this is direct
  production work, not a research finding.
- **Limitations / conflicting evidence:** Not applicable.
- **Effect on project direction:** Closes the legacy-icon-set open item
  from Entry 003. `B04-D` is not fully finished — it needs the creator to
  add "API" type by hand in Inkscape before it's usable. Everything else
  in the set is now current-palette and ready to use.

### Entry 007 — Logo symbol and icon set promoted from candidate/legacy to working assets

- **Date logged:** 2026-07-24
- **Priority / Question:** Continues Entries 003–006 (Priority 7/10, visual
  identity) — closes out the visual-identity work for now, leaving only the
  wordmark unresolved.
- **Source:** Direct restructuring/production work by Claude Code, per the
  creator's explicit instruction to promote both assets and clean up the
  folder structure. No source-key citation, as with other visual-identity
  entries.
- **What changed:** The creator manually finished `B04-D_API_MCP.svg` (hand-set
  the "API" type in Inkscape's text tool) and confirmed both the icon set
  and logo symbol as finished, no longer provisional. Both were promoted:
  - **Icon set:** moved from `assets/brand/legacy-pawh-icons/Batch_0X/B0X-Y_Name.svg`
    (36 files across 5 batch subfolders, an artefact of how the icons were
    originally produced) to flat, snake_case files at
    `assets/brand/icons/svg/{topic}.svg` — e.g. `B01-A_Purpose.svg` →
    `purpose.svg`. Moved via `git mv` to preserve history as renames. PNG
    exports generated at 64/128/256px (transparent background) via the
    Inkscape CLI into `assets/brand/icons/png/`, one file per icon per
    size (108 total). A `README.md` manifest added listing every icon
    filename against its topic, replacing the discoverability the batch
    folders used to provide.
  - **Logo:** `assets/brand/logo/candidates/GAP_logo_shaded.svg` →
    `assets/brand/logo/logo_symbol.svg` (default/primary) and
    `GAP_logo_flat.svg` → `logo_symbol_flat.svg` (explicit flat variant).
    These two were untracked in git (never previously committed), so this
    was a plain move rather than a tracked rename. PNG exports generated
    at 32/64/128/256/512/1024px (transparent background) for both
    variants into `assets/brand/logo/png/` (12 files total).
  - `assets/brand/legacy-pawh-icons/` and `assets/brand/logo/candidates/`
    removed entirely once empty.
  - `PROJECT_BRIEF.md` ("Visual identity") and `CLAUDE.md` ("Where to look
    for what") updated to the new paths and promoted status.
- **Inference drawn:** None — direct production/restructuring work.
- **Limitations / conflicting evidence:** Not applicable. Note: the icon
  count is 36, not the "35" stated in earlier entries (003/004/006) — a
  miscount in this log, not a change in the underlying file set; corrected
  here for the record, earlier entries left as-is per this log's
  non-alteration convention.
- **Effect on project direction:** The icon set and logo symbol are now
  ordinary working assets, referenced directly at their new paths rather
  than treated as candidates pending promotion. Only the wordmark pairing
  remains open in the visual-identity thread.

### Entry 008 — Wordmark finalised; full logo variant set produced

- **Date logged:** 2026-07-24
- **Priority / Question:** Continues Entries 003–007 (Priority 7/10, visual
  identity) — closes the last open item in the visual-identity thread.
- **Source:** Direct production work by Claude Code, per the creator's
  request to finalise the wordmark and produce monochrome/horizontal/
  vertical logo variants. No source-key citation, as with other
  visual-identity entries.
- **What changed:** Tested single-line ("GROUNDED AI PRACTICE") against
  two-line ("GROUNDED AI" / "PRACTICE") wordmark arrangements against the
  *current* refined symbol (the earlier "too long and disconnected"
  verdict was against the pre-Inkscape symbol, not retested until now) —
  two-line read clearly better and matches the symbol's roughly-square
  proportions, so it was used as the basis going forward. Recommended
  **Public Sans** (SIL Open Font License) as the wordmark typeface — a
  GSA-designed typeface built for federal digital services, a strong
  conceptual match for the project's evidence-based/anti-hype positioning;
  noted Manrope as a fallback if it doesn't suit once seen rendered. Eight
  new SVG files created in `assets/brand/logo/`, all derived from
  `logo_symbol_flat.svg`'s existing correct geometry via colour/text
  changes only (no new curve work): `logo_symbol_mono.svg` and
  `logo_symbol_reversed.svg` (single-Ink and white-on-dark versions of the
  symbol alone — reversed uses a transparent page-fill so it works on any
  dark background, not just Ink); `logo_lockup_horizontal.svg` and
  `logo_lockup_vertical.svg` (icon + two-line wordmark, side-by-side and
  stacked) each with matching `_mono`/`_reversed` variants. PNG
  derivatives generated via the Inkscape CLI: 32–1024px for the two square
  symbol variants, 256–1024px width for the four lockup variants (42 PNGs
  total). All verified by rendering — including the reversed lockups
  specifically composited against dark backgrounds to confirm correctness
  (a transparent PNG viewed directly appears blank against a white
  preview, which is expected, not a defect). The lockup SVGs declare
  `font-family="'Public Sans', sans-serif"` but were built using a system
  sans-serif fallback for layout purposes only, since real downloadable
  fonts can't be loaded in this chat's rendering — same constraint and
  same resolution pattern as the logo symbol and the API/MCP icon: the
  creator still needs to install the real font, apply it, check kerning,
  and convert the text to paths in Inkscape.
- **Inference drawn:** None beyond what's stated — direct production work.
- **Limitations / conflicting evidence:** Not applicable.
- **Effect on project direction:** Closes the visual-identity thread's
  last open item at the direction level. What remains is execution
  polish (real typeface, kerning, path-conversion) rather than an
  open design decision — a creator task in Inkscape, not a further Claude
  Code design pass, per the established workflow correction (Entries
  003/006/007).

### Entry 009 — Stone (neutral grey) added to the palette

- **Date logged:** 2026-07-24
- **Priority / Question:** Continues the visual-identity thread (Entries
  003–008, Priority 7/10) — the six-colour palette had no true grey.
- **Source:** Direct creative decision by the project's creator, 2026-07-24
  — no source-key citation, as with other visual-identity entries.
- **What changed:** The creator confirmed they're making manual colour
  edits during the font-to-path conversion pass in Inkscape and wanted a
  grey option for sparing use in the monochrome logo variants. Three
  candidates were proposed with different undertones (warm, matching Ink;
  cool, matching Sage; fully neutral) — the creator picked **Stone**
  (`#6E6E6E`), the fully neutral option, specifically because it has no
  warm/cool lean, unlike every other colour in the palette. Added to the
  palette table in `PROJECT_BRIEF.md`, explicitly scoped as sparing-use
  only (monochrome logo detailing initially), not a general UI/text
  colour.
- **Inference drawn:** None — a direct decision, not derived from evidence.
- **Limitations / conflicting evidence:** Not applicable.
- **Effect on project direction:** The palette is now seven colours. No
  files were changed to use Stone yet — the creator is applying it
  manually themselves as part of the same Inkscape pass covering the
  wordmark font-to-path conversion.

### Entry 010 — Graphite (second neutral grey) added to the palette

- **Date logged:** 2026-07-24
- **Priority / Question:** Continues Entry 009 — the creator wanted a
  second, darker grey alongside Stone.
- **Source:** Direct creative decision by the project's creator, 2026-07-24
  — no source-key citation, as with other visual-identity entries.
- **What changed:** Two candidates were proposed, both matching Stone's
  zero warm/cool lean rather than introducing a third undertone: Graphite
  (`#404040`, a genuine third step between Stone and Ink) and Charcoal
  (`#2B2B2B`, matching Ink's depth but neutral). The creator picked
  **Graphite**. Added to the palette table in `PROJECT_BRIEF.md`, same
  sparing-use scope as Stone (monochrome logo detailing, not general
  UI/text colour).
- **Inference drawn:** None — a direct decision, not derived from evidence.
- **Limitations / conflicting evidence:** Not applicable.
- **Effect on project direction:** The palette is now eight colours. No
  files changed to use Graphite yet — same as Stone, this is for the
  creator to apply manually during their own Inkscape work.

### Entry 011 — Visual identity finalised: wordmark polished, two-tone hierarchy, reversed variants redesigned

- **Date logged:** 2026-07-24
- **Priority / Question:** Closes the visual-identity thread (Entries
  003–010, Priority 7/10) — the creator confirmed final logo revisions are
  complete.
- **Source:** Direct manual work by the project's creator in Inkscape,
  2026-07-24 — no source-key citation, as with other visual-identity
  entries.
- **What changed:** The creator completed the outstanding Inkscape work
  across all ten logo SVGs: installed Public Sans, applied it to every
  wordmark, tightened "GROUNDED"'s letter-spacing, and converted all
  wordmark text to vector paths (no font dependency remains anywhere in
  the brand system now). Beyond the planned polish, the creator introduced
  a consistent **two-tone wordmark hierarchy** across every variant:
  "GROUNDED" always takes the variant's most prominent available tone
  (Ember in full-colour, Graphite in monochrome, white in reversed), while
  "AI"/"PRACTICE" take a quieter tone (Ink in full-colour/mono, Stone in
  reversed) — this is the realised use for Stone and Graphite (Entries
  009/010), not just the "sparing use" originally anticipated when they
  were added. Separately, the creator redesigned the reversed variants'
  page-fill area: originally built transparent so it would work on any
  dark background, all three reversed files (`logo_symbol_reversed.svg`,
  both reversed lockups) now use an explicit Ink fill instead — a
  deliberate, consistent choice across all three files, narrowing the
  reversed variants' intended use to Ink-coloured backgrounds specifically
  rather than arbitrary dark backgrounds. All 42 PNG derivatives were
  regenerated from the final SVGs and spot-checked, including compositing
  the reversed variants against Ink to confirm the two-tone treatment
  reads correctly (a transparent/white element is invisible against this
  chat's white preview background, which is expected, not a defect — the
  same verification step used for earlier reversed-variant checks).
- **Inference drawn:** None beyond what's stated — direct production work,
  described accurately from reading the final files rather than assumed
  from what was originally planned.
- **Limitations / conflicting evidence:** Not applicable.
- **Effect on project direction:** The visual identity is now genuinely
  **FINAL** — `PROJECT_BRIEF.md`'s "Visual identity" section and "Not yet
  decided" list both updated to reflect this; visual identity removed from
  the open-questions list entirely. No further Claude Code or Inkscape
  design work is anticipated on the logo/icon system unless the creator
  reopens it.

### Entry 012 — Square and circular profile pictures added

- **Date logged:** 2026-07-24
- **Priority / Question:** Extends the now-FINAL visual identity (Entries
  003–011, Priority 7/10) with two derivative assets, not a new design
  decision.
- **Source:** Direct request from the project's creator, 2026-07-24, who
  supplied an old PAWH-era circular avatar as a reference for the general
  composition style (icon centred on a solid disc with an inset ring
  border) — explicitly noted as using outdated assets/colours, not as a
  spec to copy literally.
- **What changed:** Built `profile_picture_square.svg` and
  `profile_picture_circular.svg` in `assets/brand/logo/`, both using the
  main shaded `logo_symbol.svg` on a Paper background with a thick Ink
  ring border. Sizing went through several rounds of creator feedback:
  initial concept used the reversed symbol on an Ink background (rejected
  — creator wanted the normal-colour logo on Paper instead), then the
  icon size and border thickness/position were each adjusted twice before
  confirmation. Final state: square version's icon is slightly larger
  than the circular version's, and the border sits close to the image
  edge on both. PNGs generated at 256/512/1024px. The circular file is
  built as a true circle (transparent corners via a circular clip), not
  just a square file — relevant since the creator's specific intended use
  for it is a GitHub profile picture, and GitHub auto-crops square
  uploads to a circle regardless, so this file works correctly whether or
  not further cropping happens.
- **Inference drawn:** None — direct production work.
- **Limitations / conflicting evidence:** Not applicable.
- **Effect on project direction:** None on project direction — these are
  supplementary derivative assets for the creator's personal/social use,
  not a change to the core brand system.

### Entry 013 — Pilot unit core capability decided: effective prompting

- **Date logged:** 2026-07-26
- **Priority / Question:** Immediate priority Q5 / Priority 3 — resolves the
  open question flagged after `RESEARCH_LOG.md` Entries 039-040: which single core capability
  the pilot unit (Entry 001, this file) should teach.
- **Source:** Direct decision by the project's creator, 2026-07-26, made
  against the four candidates and disconfirm check set out in
  `RESEARCH_LOG.md` Entries 039-040. Not new external evidence — a scoping choice informed by
  already-logged sources.
- **What the source directly supports:** The creator chose **Candidate B
  (effective prompting)**, with a specific rationale not captured verbatim
  in `RESEARCH_LOG.md` Entry 039's tradeoff summary: prompting is well suited to illustrating
  the gap between what a learner sees (their own typed input) and what the
  model actually does with it, giving the unit a concrete way to touch on
  backend model behaviour while still teaching an immediately usable skill
  applicable to whatever AI tools the learner already has.
- **Inference drawn:** This framing directly addresses the design constraint
  `RESEARCH_LOG.md` Entry 040 raised — that a production-skill candidate (B) or evaluative
  candidate (A) risks being taught as a checklist unless it folds in some
  version of Candidate C's capability/limitation mental model as scaffolding.
  By building the "why" (what the model does with input) into the prompting
  lesson itself, rather than treating C as a separate prerequisite unit, this
  choice resolves that tension for the pilot rather than deferring it. This
  reading is this entry's own synthesis, not something the creator stated in
  those terms.
- **Limitations / conflicting evidence:** `RESEARCH_LOG.md` Entry 039 flagged Candidate B as
  the weakest fit to the project's stated "responsible/verification" framing
  (`PROJECT_BRIEF.md`'s problem statement) and the most likely to read as
  generic tool-training. That risk is not eliminated by this decision — the
  unit is still a production-skill unit first. It is a scoping choice for
  *this* pilot, not a claim that responsible-use content is unimportant;
  Candidate D (responsible/safe use) remains a plausible second unit if the
  project later stacks further pilots.
- **Effect on project direction:** Unblocks drafting the pilot unit itself.
  Working title recorded in `PROJECT_BRIEF.md`: "Effective prompting — what's
  really happening when you hit send." Naming went through one revision
  round: an initial draft phrase ("effective prompting, taught through the
  user-facing input vs. model-processing lens") was rejected by the creator
  as jargon-heavy and unintuitive, not reflective of substance — plain,
  concrete wording was preferred over an abstract "lens" framing, consistent
  with the project's accessibility goal for its general-public/SME audience.

### Entry 014 — Icon and logo consistency pass: fill-ratio, stroke width, background-blend fills, layer labelling, profile picture redesign

- **Date logged:** 2026-07-27
- **Priority / Question:** Priority 7/10 (visual identity, already status FINAL
  at the direction level per Entries 003–012) — this entry records
  execution-level technical fixes, not a reopening of that direction, same
  category as the four-icon construction fixes in Entry 006/007.
- **Source:** Direct creator review of the icon set and logo assets,
  2026-07-26/27, working from a self-produced audit (Inkscape CLI geometry
  queries measuring actual drawn-content bounding boxes against each
  icon's declared canvas, not just viewBox) plus visual comparison
  artifacts built during the session.
- **What changed:**
  1. **Fill-ratio normalisation.** All 36 icons measured: fill-ratio (content
     bounding box vs. 512×512 canvas) ranged 0.48–0.90, median 0.64 — the
     root cause of icons reading as inconsistent sizes despite identical
     export dimensions. Every icon normalised to a 0.70 target via a
     uniform scale+recentre transform (aspect ratio preserved, no path
     coordinates touched), matching the low-risk technique already used
     for the Vector Database viewBox fix (Entry 006).
  2. **Stroke-width normalisation (partial, creator-approved subset only).**
     Full-set stroke-width audit found values from 3 to 32. Creator
     approved exactly five specific fixes to the 14-weight de facto
     standard: Information (16→14), Architecture (12→14), Troubleshooting
     (10→14), Verification's border (16→14), Tip's speech-bubble outline
     (11→14, explicitly not its lightbulb/filament details). Checked all
     other icons using the same bubble motif (`ai_assistant`,
     `quote_callout`) — already correct. Icons mixing several stroke
     weights deliberately (bold outline + thin inner accent) were reviewed
     via a rendered side-by-side comparison and the creator confirmed
     these are intentionally sized, not touched.
  3. **Background-matching backing fills corrected from Paper to pure
     white.** Creator's finding: Ink/Paper hardcoded into fills meant to
     blend with a surrounding background (rather than used as genuine
     structural/brand colour) don't actually blend with a true-white
     document page or arbitrary dark surface, since Paper (`#F9F9F9`) and
     Ink (`#27221E`) are not literally `#FFFFFF`/`#000000`. Checked across
     the whole icon set and the non-reversed logo files (`logo_symbol.svg`,
     `_flat`, `_mono`, four lockups): Cloud AI's interior fill was already
     correct (pure white from original construction); the "page" strip and
     terminal chevron/cursor across the logo files were on Paper and fixed
     to pure white (22 occurrences across 7 files, plus an unrelated latent
     bug found in the process — `logo_symbol_flat.svg`'s chevron/underscore
     had a `style` attribute silently overriding its own `stroke="#ffffff"`
     to `#f9f9f9`, now consistent). Vector Database and Embedding's
     database-stack fill was already pure white; its circular
     badge-background element was initially changed to white in the same
     pass, then explicitly reverted by the creator, who wants that specific
     element to stay page-tinted — a deliberate exception, not an oversight.
     `logo_symbol_reversed.svg`'s Ink page-fill was separately confirmed
     as intentional and explicitly left alone (see point 5).
  4. **SVG layer/group labelling.** Per creator convention (stated while
     reviewing their own manual edit to `hybrid_ai.svg`): groups/layers
     should carry clear snake_case labels; individual leaf paths should not
     be individually named, since the effort doesn't pay for itself. Applied
     to all 34 icon SVGs that had unlabelled groups (75 groups total across
     the set) via a script that only adds `id` attributes to currently
     unlabelled `<g>` elements — never renames an existing id, to avoid
     breaking any gradient/clip-path reference. `hybrid_ai.svg` skipped (no
     groups; creator was mid-edit). Logo symbol/lockup files already had
     adequate existing labels from earlier work, left alone.
  5. **Reversed-logo judgement call resolved.** Asked whether
     `logo_symbol_reversed.svg`'s Ink page-fill (Entry 011's "no longer
     intended to work on arbitrary dark backgrounds, only Ink specifically")
     should be reconsidered under the new background-fill finding. Creator
     confirmed it should stay exactly as-is — a genuinely intentional
     choice, not an instance of the bug being fixed elsewhere.
  6. **Profile pictures redesigned.** Creator supplied a reference image
     (external source, style only) and asked for its border/background
     treatment adapted with navy substituted for Ink. Both
     `profile_picture_square.svg` and `profile_picture_circular.svg` were
     rebuilt: Ink background (was Paper), a Paper ring now flush with the
     canvas edge (was a thick Ink ring inset from the edge — went through
     an intermediate thin-ring version before the creator asked for it
     thicker), and the reversed logo symbol (not the shaded/normal-colour
     one) centred on top — its Ink page-fill disappears into the new
     background by construction, directly validating the point 5 decision.
     Added a subtle depth treatment reusing `logo_symbol.svg`'s exact
     spine-shadow gradient technique, narrowed on creator instruction so it
     doesn't extend far enough right to visually compete with the terminal
     chevron. Creator approved the final result.
- **Inference drawn:** The background-blend-fill problem (point 3) and the
  reversed-symbol page-fill decision (point 5) are two sides of the same
  underlying question — whether a colour token in a fill is standing in for
  "whatever surface this sits on" or is genuine brand colour — and the
  profile picture redesign (point 6) is a real, working example of the
  "intentional Ink background" case that justifies keeping point 5 as
  Ink rather than reverting it to transparent. This connective reading is
  this entry's own synthesis, not something stated directly by the creator
  in those terms.
- **Limitations / conflicting evidence:** Not applicable — this entry
  records completed, creator-reviewed and rendered-verified production
  work, not a research finding with counter-evidence to weigh.
- **Effect on project direction:** None on direction (palette/logo
  type/tone remain FINAL per Entry 011). All PNG derivatives regenerated
  from the updated SVGs (icons at 64/128/256px; touched logo/lockup files
  at their existing size sets; profile pictures at 256/512/1024px) in one
  batch at the end of the pass, per the creator's own sequencing
  instruction (fix colours → normalise strokes → redesign profile pictures
  → regenerate everything once, not repeatedly).

### Entry 015 — Pilot-unit example doc: PAWH callout review and Word-group construction technique

- **Date logged:** 2026-07-27 (records work done 2026-07-26, ahead of Entry
  014; logged retrospectively after being flagged as a documentation gap).
- **Priority / Question:** Priority 7 (delivery format) — the Word-document
  formatting standard for the pilot unit example at
  `drafts/Effective_Prompting_Example.docx`.
- **Source:** Direct creator review across several rounds, working from one
  file shared out of a larger PAWH reference pack: `PAWH_Semantic_Callout_
  Word_Component_Library_v01.docx` (approved PAWH authority, 2026-07-22:
  rounded shell, white icon well, internal divider, tinted text area;
  approved types Note/Warning/Check/Troubleshooting, Tip/Important/Example
  deferred). Creator explicitly said GAP's callouts aren't limited to
  PAWH's four types — the full 36-icon set can be used to build further
  variants in the same style.
- **What happened:** Rebuilding the callout cards to match that pattern
  went through three constructions. A table-cell-shading version worked
  but had square corners. Nesting a rounded shape inside another shape's
  text box got closer visually but Word refused to open the file outright
  ("You can't put drawing objects into a text box, callout, comment,
  footnote or endnote") — a real, hard OOXML constraint, not a bug to work
  around. The fix: build each card as a Word **group** (`wpg:wgp`) of
  sibling objects — background shape, icon-well shape, icon picture,
  divider shape, separate text-box shape — which is how Word's own "group
  objects" feature works, and matches how the PAWH masters themselves are
  built (their reuse instructions say "select and copy the complete
  **grouped** object"). This construction opens correctly in Word and
  renders with correct text and document-order placement.
- **Inference drawn:** LibreOffice (the only renderer available in this
  environment) proved unreliable specifically for grouped shapes with
  embedded text — it mis-ordered content, produced a duplicated/empty box,
  and rendered text boxes blank, none of which were real defects once
  checked in actual Microsoft Word via `tools/word_preview.ps1`. This is
  this project's own finding, not documented anywhere externally that was
  checked — treat LibreOffice as reliable for ordinary content but not for
  this specific shape category going forward.
- **Limitations / conflicting evidence:** Not applicable — production/
  technical record, not a research claim.
- **Effect on project direction:** None on direction. Practical effect: the
  cosmetic punch list from the creator's real-Word review (icon well size,
  icon resolution, divider/well height match) was resolved once
  `tools/word_preview.ps1` existed to self-verify against (see Entry in
  `CLAUDE.md`'s "Working approach" on self-check tooling). The example doc
  remains a draft, not the finished pilot unit content — the creator's
  wider PAWH reference pack also covers a title-card system and a
  not-yet-reviewed native-table authority, both still open if this thread
  resumes.

### Entry 016 — Style Reference example doc approved as canonical (current scope)

- **Date logged:** 2026-07-27
- **Priority / Question:** Priority 7 (delivery format) — status update to
  the Word-document style system established in Entries 013/015 and
  substantially revised this session.
- **Source:** Direct creator decision, 2026-07-27, after two review rounds
  on `drafts/Style_Reference_Example.docx`: an initial pass (icon padding/
  speech-bubble consistency, font, direct-vs-styled formatting, callout-card
  sizing, pull-quote shape, table variety) and a revised build addressing
  it, which the creator then reviewed and signed off on.
- **What happened:** Creator approved the current style reference — a real
  named-style system (Title/Subtitle/Heading1-3/Normal/Caption/Quote, all
  Public Sans) in place of per-run direct formatting, callout cards with
  small/medium/large size presets, pill-shaped accent bars, and three table
  types — as canonical for current purposes. Extracted into `CLAUDE.md`'s
  new "Word document conventions" section the same session. Explicitly
  scoped as provisional, not frozen: "subject to later changes and
  refinement." The icon set itself (border padding, inconsistent
  speech-bubble styling across icons using that motif) remains a known,
  separately deferred issue — the creator is revisiting it directly in
  Inkscape, not part of what was just approved.
- **Inference drawn:** None — this is a direct decision, not something
  inferred from a draft.
- **Limitations / conflicting evidence:** Not applicable — production/
  technical record, not a research claim. "Canonical for current purposes"
  is explicitly not a permanent lock; treat `CLAUDE.md`'s "Word document
  conventions" as the current approved baseline, not an unchangeable one,
  until the creator says otherwise.
- **Effect on project direction:** Future Word-document work — including
  eventual pilot-unit real content — should follow the approved conventions
  by default rather than re-deriving formatting choices. The icon set is
  the one explicit open exception, pending the creator's own Inkscape pass.

### Entry 017 — RESEARCH_LOG.md split: this file created to separate decisions/production notes from research findings

- **Date logged:** 2026-07-27
- **Priority / Question:** Not tied to a single research priority — a
  documentation-structure fix the creator asked for directly.
- **Source:** Direct creator request, 2026-07-27: "RESEARCH_LOG is not just
  being used to collate sources and research sessions but now as a general
  dump for all rule files. Can we fix this?"
- **What happened:** Audited all 52 entries then in `RESEARCH_LOG.md`
  against its own stated Purpose ("records what was actually found" against
  a `RESEARCH_QUESTIONS.md` priority, with a citable source). ~36 were
  genuine research; the other 16 were scoping decisions, design/production
  work, and technical build notes (visual identity, icon/logo production,
  Word-document engineering notes) that had been logged the same way purely
  because `CLAUDE.md`'s file-conventions rule pointed all durable content at
  `RESEARCH_LOG.md`. Concretely, this also produced a real numbering
  collision: two unrelated tracks (research and visual-identity/production)
  had each independently numbered entries 039-042, so every one of those
  four numbers pointed at two different entries depending on which track
  was meant. The 16 non-research entries (former Entries 035-050 in this
  file) were moved to this file and renumbered 001-016 in their original
  chronological order; internal cross-references between them were updated
  to the new numbers, and the one entry (former Entry 047) that cited the
  *staying* research Entries 039/040 was updated to say so explicitly
  rather than being remapped. `RESEARCH_LOG.md`'s own Open Threads section
  citations pointing at moved entries were updated the same way. The
  039-042 collision resolved itself once the production-track copies left
  — `RESEARCH_LOG.md`'s own 039-042 are unique again without renumbering.
- **Inference drawn:** None — this is a direct restructuring in response to
  an explicit instruction, not a research finding.
- **Limitations / conflicting evidence:** Not applicable — production/
  technical record.
- **Effect on project direction:** `CLAUDE.md`'s "File conventions" section
  updated so future durable content is routed correctly: `RESEARCH_LOG.md`
  for source-backed research only, this file for everything else durable
  that isn't a `PROJECT_BRIEF.md`-level current-state summary. This entry
  exists in the file it's documenting the creation of, which is intentional
  — it is itself exactly the kind of entry `PROJECT_LOG.md` is for.
