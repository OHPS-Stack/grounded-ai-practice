# Grounded AI Practice — Project Log

## Document status

Working document, maintained alongside `research_log.md`. Split out from it
on 2026-07-27 (see Entry 017 below) once that file's research-only purpose
had drifted into a general dump for every kind of durable record.

## Purpose

Records scoping/creative decisions and design/production/technical work —
everything durable that is **not** source-backed research evidence (that
belongs in `research_log.md`) and is **not** a standing current-state
summary (that belongs in `project_brief.md`). Think of it as the
chronological "what happened and why" history behind the decisions
`project_brief.md` currently reflects.

This log is intended to be maintained by Claude, not edited by hand. New
entries are appended as decisions are made or work is completed; existing
entries are not silently altered — corrections or supersessions are added
as new entries that reference the one they update, so history stays
traceable, consistent with `research_log.md`'s own non-alteration
convention.

## How to read this log

Same entry shape as `research_log.md`, adapted for content that usually has
no external citation:

| Field | Meaning |
|---|---|
| ID | Sequential entry number (this file's own sequence, separate from `research_log.md`'s) |
| Date logged | When the entry was added |
| Priority / Question | Which `research_questions.md` priority this touches, if any — some entries (like this file's own creation) aren't tied to one |
| Source | Who decided or built something (the creator directly, or Claude Code on the creator's instruction) rather than an external citation |
| What happened | What changed, decided, or was built |
| Inference drawn | Any conclusion drawn beyond the plain fact, clearly marked as inference |
| Limitations / conflicting evidence | Usually "Not applicable" here — kept for structural consistency with `research_log.md`, since this is a production record, not a claim needing corroboration |
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
  format — both remain open (see `project_brief.md`). As previously flagged,
  `RS-AILIT25`'s pilot-first recommendation is drawn from a children's-
  education evidence base, and `GRR-EBIP`'s sequencing model is K-12-
  originated (Entry 027) — applying both to adult, self-directed learning is
  this project's own extension, not something either source tested directly.
- **Effect on project direction:** Recorded as a working decision in
  `project_brief.md` ("First public output"). Converts four sessions of
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
  was recorded in `project_brief.md` ("Inherited workstation architecture")
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
  explicitly distinct in `project_brief.md` so they aren't accidentally
  conflated in future sessions.

### Entry 003 — Visual identity: palette and logo-type decision (Priority 7/10)

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 7 (delivery format) touches on visual
  presentation; Priority 10 (sustainability/public presentation) — "visual
  identity beyond the approved project name" (`project_brief.md`, "Not yet
  decided").
- **Source:** Direct creative decision by the project's creator, 2026-07-24
  — a design choice, not an evidence-based research finding, so this entry
  intentionally has no source-key citation.
- **What changed:** The creator finalised a six-colour palette (Ink, Ember,
  Sand, Paper, Mist, Sage — see `project_brief.md`, "Visual identity"),
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
  `project_brief.md`'s "Visual identity" section to point at the current
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
  - `project_brief.md` ("Visual identity") and `CLAUDE.md` ("Where to look
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
  palette table in `project_brief.md`, explicitly scoped as sparing-use
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
  **Graphite**. Added to the palette table in `project_brief.md`, same
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
  **FINAL** — `project_brief.md`'s "Visual identity" section and "Not yet
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
  open question flagged after `research_log.md` Entries 039-040: which single core capability
  the pilot unit (Entry 001, this file) should teach.
- **Source:** Direct decision by the project's creator, 2026-07-26, made
  against the four candidates and disconfirm check set out in
  `research_log.md` Entries 039-040. Not new external evidence — a scoping choice informed by
  already-logged sources.
- **What the source directly supports:** The creator chose **Candidate B
  (effective prompting)**, with a specific rationale not captured verbatim
  in `research_log.md` Entry 039's tradeoff summary: prompting is well suited to illustrating
  the gap between what a learner sees (their own typed input) and what the
  model actually does with it, giving the unit a concrete way to touch on
  backend model behaviour while still teaching an immediately usable skill
  applicable to whatever AI tools the learner already has.
- **Inference drawn:** This framing directly addresses the design constraint
  `research_log.md` Entry 040 raised — that a production-skill candidate (B) or evaluative
  candidate (A) risks being taught as a checklist unless it folds in some
  version of Candidate C's capability/limitation mental model as scaffolding.
  By building the "why" (what the model does with input) into the prompting
  lesson itself, rather than treating C as a separate prerequisite unit, this
  choice resolves that tension for the pilot rather than deferring it. This
  reading is this entry's own synthesis, not something the creator stated in
  those terms.
- **Limitations / conflicting evidence:** `research_log.md` Entry 039 flagged Candidate B as
  the weakest fit to the project's stated "responsible/verification" framing
  (`project_brief.md`'s problem statement) and the most likely to read as
  generic tool-training. That risk is not eliminated by this decision — the
  unit is still a production-skill unit first. It is a scoping choice for
  *this* pilot, not a claim that responsible-use content is unimportant;
  Candidate D (responsible/safe use) remains a plausible second unit if the
  project later stacks further pilots.
- **Effect on project direction:** Unblocks drafting the pilot unit itself.
  Working title recorded in `project_brief.md`: "Effective prompting — what's
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

### Entry 017 — research_log.md split: this file created to separate decisions/production notes from research findings

- **Date logged:** 2026-07-27
- **Priority / Question:** Not tied to a single research priority — a
  documentation-structure fix the creator asked for directly.
- **Source:** Direct creator request, 2026-07-27: "RESEARCH_LOG is not just
  being used to collate sources and research sessions but now as a general
  dump for all rule files. Can we fix this?"
- **What happened:** Audited all 52 entries then in `research_log.md`
  against its own stated Purpose ("records what was actually found" against
  a `research_questions.md` priority, with a citable source). ~36 were
  genuine research; the other 16 were scoping decisions, design/production
  work, and technical build notes (visual identity, icon/logo production,
  Word-document engineering notes) that had been logged the same way purely
  because `CLAUDE.md`'s file-conventions rule pointed all durable content at
  `research_log.md`. Concretely, this also produced a real numbering
  collision: two unrelated tracks (research and visual-identity/production)
  had each independently numbered entries 039-042, so every one of those
  four numbers pointed at two different entries depending on which track
  was meant. The 16 non-research entries (former Entries 035-050 in this
  file) were moved to this file and renumbered 001-016 in their original
  chronological order; internal cross-references between them were updated
  to the new numbers, and the one entry (former Entry 047) that cited the
  *staying* research Entries 039/040 was updated to say so explicitly
  rather than being remapped. `research_log.md`'s own Open Threads section
  citations pointing at moved entries were updated the same way. The
  039-042 collision resolved itself once the production-track copies left
  — `research_log.md`'s own 039-042 are unique again without renumbering.
- **Inference drawn:** None — this is a direct restructuring in response to
  an explicit instruction, not a research finding.
- **Limitations / conflicting evidence:** Not applicable — production/
  technical record.
- **Effect on project direction:** `CLAUDE.md`'s "File conventions" section
  updated so future durable content is routed correctly: `research_log.md`
  for source-backed research only, this file for everything else durable
  that isn't a `project_brief.md`-level current-state summary. This entry
  exists in the file it's documenting the creation of, which is intentional
  — it is itself exactly the kind of entry `project_log.md` is for.

### Entry 018 — Profile pictures: standard/inverted roles swapped, spine-shadow deepened, square standard rebuilt

- **Date logged:** 2026-07-27
- **Priority / Question:** Continues Entries 012/014 (Priority 7/10,
  visual identity derivative assets) — a styling/naming correction, not a
  reopening of the FINAL core brand system (Entry 011).
- **Source:** Direct creator request and iterative feedback, 2026-07-27,
  working live against rendered screenshots.
- **What happened:** The creator asked for a white-background/dark-book
  circular profile picture (opposite of Entry 014's Ink-background/
  white-book redesign), initially built and reviewed as
  `profile_picture_circular_inverted.svg`. The book's existing spine-shadow
  gradient (a black overlay, originally tuned at 0.42 opacity against a
  *white* book in Entry 014) proved nearly invisible against this dark Ink
  book — black-on-near-black has far less inherent contrast than
  black-on-white — so the creator had it raised in two rounds, 0.42→0.75→
  0.92, confirmed correct at that final value. The creator then reversed
  the naming: the white-background/dark-book version is the standard/
  default going forward, and the original Ink-background/white-book
  version (Entry 014) is now the `_inverted` variant — opposite of how
  Entry 012/014 originally set the two up. Both circular files were
  rewritten under swapped filenames accordingly
  (`profile_picture_circular.svg` = new standard,
  `profile_picture_circular_inverted.svg` = former default, spine opacity
  left at 0.42 since it already read correctly there). The creator also
  asked for the deepened 0.92 spine-shadow peak applied everywhere else the
  standard dark book symbol appears with that shading: `logo_symbol.svg`,
  `logo_lockup_horizontal.svg`, `logo_lockup_vertical.svg` (checked by
  grep across `assets/brand/logo/` for every `spineGrad`/
  `stop-opacity="0.42"` occurrence; `logo_symbol_flat.svg` and all `_mono`
  variants have no spine-shadow element at all, so were correctly out of
  scope). Finally, the creator asked for a square profile picture built in
  the circular standard's style — `profile_picture_square.svg` was rebuilt
  the same way (white background, Ink ring, dark book, 0.92 spine peak,
  white chevron/cursor) reusing the existing square file's icon
  position/scale convention (icon sized slightly larger than the circular
  version, per Entry 012), and the prior Ink-background/white-book square
  file was renamed to `profile_picture_square_inverted.svg` to match the
  circular pair.
- **Inference drawn:** The 0.42→0.92 opacity gap is a direct, derivable
  consequence of the underlying book colour, not an arbitrary re-tune — a
  fixed-opacity black overlay reads very differently depending on how dark
  the base colour already is. This is this entry's own read of why the
  original value failed here, not something the creator stated in those
  terms.
- **Limitations / conflicting evidence:** Not applicable — production
  record. PNG derivatives for all four profile-picture files (256/512/
  1024px, per Entry 012's convention) have not yet been regenerated as of
  this entry — flagged as outstanding.
- **Effect on project direction:** None on core brand-system direction
  (still FINAL per Entry 011). Updates `project_brief.md`'s "Visual
  identity" section to the new standard/inverted naming and the deepened
  spine-shadow value. Outstanding: PNG regeneration for all four profile
  pictures, and confirming whether an export tool/process should be set up
  for this rather than repeating ad hoc Inkscape CLI calls each time (see
  `CLAUDE.md`'s self-check-tooling preference).

### Entry 019 — AI Skills Hub briefing rebuilt on the GAP style system; production paused

- **Date logged:** 2026-07-28
- **Priority / Question:** Priority 7 (delivery format) and Priority 10
  (public presentation) — the second real document built on the approved
  style system (Entry 016), and the first with substantive external-facing
  content.
- **Source:** Production work by Claude Code across 2026-07-27/28, three
  review rounds by the creator, plus one external review (the creator fed
  the document to ChatGPT and returned its critique for evaluation).
- **What happened:** `drafts/AI_Skills_Hub_Briefing.docx` was rebuilt from
  scratch on the GAP Word style system — named styles, title block, pull
  quote, callout card, three table types, real header/footer, corrected
  page margins — replacing its original ad-hoc navy/grey styling. Content
  was deepened with three research findings logged after the original
  24 July draft (`research_log.md` Entries 026–028: PRIMES' full criteria,
  the GRR sequencing model, the overconfidence confirm/disconfirm pair),
  and the closing section was rewritten to reflect the project's decided
  audience/pilot direction instead of the stale "not yet finalised"
  framing. The external ChatGPT review's points were evaluated
  individually rather than applied wholesale: evidential-framing fixes,
  claim moderation, an evidential-role table column, a limitations list,
  and two renderer-verified defects (WCAG-failing Ember text at small
  size; a table row splitting across pages) were accepted; its
  Caption-style contrast complaint was rejected after computing the actual
  ratio (4.84:1, passes AA), and its endnote/DOI citation overhaul was
  deferred as out of scope. The creator then hand-rewrote the opening into
  a deliberately more opinionated "Overview/Editorial" section and
  flagged that the earlier draft's sentence complexity had over-imitated
  their casual prompting style — a prose-tightening pass followed
  (vocabulary/tone matching yes, complexity matching no; see the
  voice-matching rule refinement in local memory).
- **Inference drawn:** None — production record.
- **Limitations / conflicting evidence:** Not applicable.
- **Effect on project direction:** Production on this document is
  **paused as of 2026-07-28** at the creator's direction, in favour of a
  wider research pass (Entry 020). Noted for resumption: §2 and §3 could
  merge; the document's scope should widen beyond the AI Skills Hub
  toward the broader UK AI climate as stronger concepts and figures land
  in research. The document remains in `drafts/`, not approved, not
  promoted.

### Entry 020 — Longer-term direction: roadmap.sh reference model, official-channel positioning aim, Hub account as research asset

- **Date logged:** 2026-07-28
- **Priority / Question:** Priority 7 (delivery format, long-term),
  Priority 10 (sustainability/public presentation), Priority 5
  (comparables — extends the roadmap.sh design-pattern analysis in
  `research_log.md` Entry 020).
- **Source:** Direct statement of carefully-considered direction by the
  project's creator, 2026-07-28, recorded into `project_brief.md`
  ("Longer-term direction and positioning") the same day.
- **What happened:** Four connected considerations were recorded, each
  labelled by evidential status: (1) roadmap.sh as a concrete reference
  model for the eventual deliverable's *kind* — accessible, customisable,
  interactive resource hub, with AI leveraged alongside explicit learner
  input for tailoring; explicitly not competing with or copying it.
  (2) An official-channel positioning aim — the project pitched to and
  approved by the correct governing body as the credible fix to the
  documented AI Skills Hub problems — firming up the previously
  loosely-held government-recognition aim. (3) A political-timing
  observation, explicitly the creator's own read and not evidence, on how
  current political conditions might affect receptiveness — held in
  internal working notes rather than a tracked file, and unverified. (4) The
  creator's active AI Skills Hub account recorded as a research asset for
  first-hand evidence collection (guidance-vs-content contradictions,
  platform comparisons) that unauthenticated tooling cannot reach. One
  further claim — that policymakers understand AI's value conceptually
  but lack practical understanding — was recorded *with the creator's own
  "unfounded" flag attached*, requiring direct quotes/evidence before any
  external use.
- **Inference drawn:** None — a direction record. The creator's own
  labelling of one claim as unfounded is preserved rather than laundered
  into an assertion.
- **Limitations / conflicting evidence:** The positioning aim depends on
  research not yet done (the UK-climate report, Entry 019's successor
  deliverable) and on the flagged claim being either supported or
  dropped. Nothing here commits the project to a platform build.
- **Effect on project direction:** Defines the next research deliverable:
  a comprehensive Word report on the UK AI climate, government postures,
  and actually delivered results — framing where GAP fits. Initial source
  set (non-exhaustive, competing sources still to be identified): the
  Innovate UK BridgeAI report (March 2026), the Innovate UK "Unlocking UK
  Economic Growth through AI" white paper (February 2026), the Innovate
  UK Business Connect knowledge centre, and the AI Skills Hub platform
  itself.

### Entry 021 — Repo prepared for public sharing: public/internal split, enforcement, audit process, README

- **Date logged:** 2026-07-28
- **Priority / Question:** Priority 10 (sustainability and public
  presentation) — the first substantive work on this priority, which had
  been essentially untouched.
- **Source:** Direct instruction from the project's creator, 2026-07-28,
  triggered by moving from a local-only repository toward selective
  sharing with trusted contacts and, later, wider public access as proof
  of work.
- **What happened:**
  1. **Audit run first.** All 15 existing commits checked: history is
     clean, no damaging content. Critically, every politically candid
     passage was found to be **uncommitted** — working tree only — so the
     split could be made before anything entered permanent history.
  2. **Public/internal rule established** (`CLAUDE.md`, "Public repo vs.
     internal working files"): default public, with a gitignored
     `internal/` directory as the sole exception for private contacts,
     candid assessments of named parties, political reads and funding
     strategy. Tracked files may record *that* a position exists and its
     evidential status, via a pointer, without reproducing wording — the
     discipline is preserved without publishing material that damages the
     project's own aims.
  3. **Enforcement built and tested.** `.gitignore` excludes `internal/`;
     `.githooks/pre-commit` blocks any commit staging `internal/` or
     containing known private markers. Both paths were tested with real
     staged commits (including the `git add -f` bypass) and confirmed to
     block. Documented honestly as guardrails against accident, not
     security controls: local-only, `--no-verify`-bypassable, and useless
     retroactively.
  4. **Content moved.** Candid political assessments relocated to
     `internal/editorial_positions.md`; private named contacts to
     `internal/contacts_private.md`. Tracked files rewritten to pointers.
     Verified zero remaining occurrences across all tracked files.
  5. **Audit process defined** (`CLAUDE.md`): three passes — Claude scan,
     independent second-model pass, then **required human verification**,
     with the creator deciding every flagged item. Triggered before any
     change in repo visibility, otherwise monthly. Outcomes logged here.
  6. **`README.md` written** as a public front door, assuming a reader who
     may be a prospective employer, collaborator or funder. Presents the
     research discipline itself as the project's current output, and
     points at the retraction (Entry 033) and self-bias-check (Entry 013)
     as evidence of that discipline rather than hiding them.
  7. **Housekeeping surfaced by the audit:** three dangling
     `[[wiki-link]]` references to a local memory file that public readers
     cannot see were replaced with real `project_brief.md` references;
     Word lock files (`~$*`) and OS cruft added to `.gitignore`.
  8. **Instro AI competing interest declared.** The creator has a personal
     connection to Instro AI, which this project's research cites
     positively (`research_log.md` Entry 031). Decision: disclose in any
     published document citing Instro, mandatory and relationship-typed if
     Instro provides funding or backing. The Entry 031 findings stay —
     they are independently sourced, and quiet removal would be worse than
     disclosure. Recorded in `contacts_and_funding.md` under "Declared
     interests".
- **Inference drawn:** None — a structural/production record.
- **Limitations / conflicting evidence:** The enforcement layer protects
  against accident only. Anything committed in future is permanent for
  practical purposes once the repo is public, so the audit discipline
  matters more than the tooling. The `internal/` directory living inside
  the repo working tree is a deliberate convenience trade-off made by the
  creator, accepting that a single `--no-verify` would defeat it.
- **Effect on project direction:** Unblocks selective sharing of the repo.
  Opens Priority 10 properly for the first time. Establishes that
  reputational and relationship judgements are the creator's alone — no
  model decides what is safe to publish. **This entry doubles as the
  record of the first audit (2026-07-28).**

### Entry 022 — UK AI climate report drafted; lockup PNG aspect-ratio bug fixed

- **Date logged:** 2026-07-28
- **Priority / Question:** Priority 1 and Priority 10 — the deliverable
  defined in Entry 020, built while the creator conducted a manual review
  of the repository.
- **Source:** Production work by Claude Code, 2026-07-28, on the research
  logged as `research_log.md` Entries 043–048.
- **What happened:**
  1. **Logo asset bug found and fixed.** The README logo rendered wrongly.
     Root cause was not the README: all twelve non-reversed lockup PNGs
     (horizontal and vertical, standard and mono) had been exported onto
     forced square canvases, ignoring the SVG sources' real aspect ratios
     (horizontal 420×150, vertical 220×260). Only the reversed variants
     were correct. All twelve re-exported from source via the Inkscape CLI
     and verified against expected ratios. The README now also swaps to the
     reversed lockup under `prefers-color-scheme: dark`, since the standard
     lockup's Ink wordmark is close to invisible on a dark GitHub theme.
  2. **Evidence gaps closed before writing**, on the view that better
     sources produce a measurably better document than better prose does.
     Two significant finds: the Public Accounts Committee's *Use of AI in
     Government* (Entry 047), the project's first genuinely independent
     scrutiny source; and the provenance of the £400bn figure (Entry 048),
     traced to vendor-commissioned consultancy research.
  3. **Report built** as `drafts/UK_AI_Skills_Ambition_Report.docx`, eight
     pages, on the GAP style system. Structure: an opinionated
     Overview/Editorial, then the ambition, the delivered results, the
     guidance-versus-product contradiction, institutional capability,
     supplier concentration, what the evidence supports, where the project
     fits, and method/limitations/declared interests. Lessons from the AI
     Skills Hub briefing applied: related critique sections merged rather
     than split, scope widened beyond the Hub, and sentence complexity kept
     down.
  4. **Two defects caught by rendering, not by reading.** An orphaned
     media file failed schema validation and was removed. More
     significantly, hard page breaks collided with natural flow and
     produced a near-blank page five. Fixed properly rather than
     cosmetically: `keepNext` added to the Heading1/2/3 styles so headings
     can never orphan, and the manual page breaks removed in favour of
     natural flow. Document went from ten pages with a blank to eight
     clean ones.
  5. **Declared interests section included** — the report states plainly
     that it is published by a project proposing an alternative to what it
     criticises, and that the author benefits if the critique persuades.
     No Instro citation appears in this report, so the Instro declaration
     recorded in `contacts_and_funding.md` was not required here; it still
     applies to any future document citing Instro.
- **Inference drawn:** None — production record. The report's own
  inferences are labelled inside it.
- **Limitations / conflicting evidence:** The report is a first draft and
  has had no creator review. Its largest stated weakness is its own: no
  response has been sought from any criticised party, which the document
  admits in §8. The `keepNext` change to `styles.xml` affects the shared
  style system and should be carried into the canonical
  `documents/Style_Reference_Example.docx` if it is regenerated — it is a
  genuine improvement, not a document-specific hack.
- **Effect on project direction:** Delivers the Entry 020 deliverable in
  draft. Confirms the value of closing evidence gaps before writing rather
  than after. Establishes `keepNext` on headings as a style-system
  improvement worth propagating.

### Entry 023 — Documents rendered but could not be saved: missing compatibilityMode downgraded every shape group

- **Date logged:** 2026-07-28
- **Priority / Question:** Priority 7 (delivery format) — a defect
  affecting every Word document the project has produced.
- **Source:** Creator bug report (Word refused to save
  `UK_AI_Skills_Ambition_Report.docx`, reporting "You can't put drawing
  objects into a text box, callout, comment, footnote or endnote", after
  which the callout cards became flat uneditable shapes), then direct
  diagnosis against the on-disk XML.
- **What happened:** The first hypothesis — that the callout construction
  was at fault, as in Entry 015 — was **wrong**, and checking rather than
  assuming is what found the real cause. Comparing the file Claude
  generated against the file on disk after Word touched it showed Word had
  rewritten all five `wpg:wgp` DrawingML groups into legacy `v:group` VML,
  and had written `compatibilityMode` **12** into `settings.xml`.
  Root cause: the project's `settings.xml` declared no compatibility mode
  at all, so Word defaulted the document to Word 2007 behaviour. Mode 12
  predates the `wps`/`wpg` shape extensions (Word 2010+) that every
  callout card and pull quote uses, so Word downgraded them to VML on
  save — and a VML group holding both a picture and a text box is exactly
  the construction that error describes.
- **Why every rendering check missed it:** `tools/word_preview.ps1` opens
  documents **read-only**. Word reads `wpg` groups perfectly well; it only
  breaks on the save path. Three documents passed every visual check while
  carrying the defect.
- **Fixes applied:**
  1. `compatibilityMode` 15 declared in the report's `settings.xml`, and
     retrofitted into `drafts/Effective_Prompting_Example.docx` and
     `drafts/AI_Skills_Hub_Briefing.docx` by surgical settings-only
     rewrite (no content touched).
  2. **New tool** `tools/word_roundtrip_test.ps1` — opens, saves and
     closes through real Word and reports success or the actual error.
     All three fixed documents verified `SAVE OK`, with the report
     additionally confirmed to retain all five `wpg:wgp` groups and zero
     VML after a real Word save, and to hold `compatibilityMode` 15
     across a second round-trip.
  3. Heading icons corrected in the same pass: icons have real aspect
     variation (`outcomes` 90x56 vs `verification` 90x90) plus ~30%
     transparent padding, so a uniform square box rendered the wide ones
     short and illegible. Now cropped to content bbox and sized by
     height, with a negative `w:position` to centre them on the cap
     height instead of sitting on the baseline.
  4. Both rules written into `CLAUDE.md`'s Word document conventions.
- **Inference drawn:** None beyond the diagnosis, which is directly
  evidenced by the before/after XML.
- **Limitations / conflicting evidence:** `AI_Skills_Hub_Briefing.docx`
  **was already degraded before the fix** — Word converted its groups to
  VML during the creator's own edit, and the on-disk copy now has one
  fewer shape group than was generated. The compatibilityMode fix stops
  further degradation but does not restore the original DrawingML; that
  document would need rebuilding to recover it. `documents/Style_Reference_Example.docx`
  has the same defect and was **left untouched pending the creator's
  decision**, since it is the approved canonical reference.
- **Effect on project direction:** Establishes that rendering checks and
  save checks are different verifications, and that this project needs
  both. Adds a hard requirement to the Word conventions. The general
  lesson is broader than Word: a document that displays correctly can
  still be structurally wrong in ways only a different operation reveals.

### Entry 024 — Naming convention standardised; file/reference integrity self-check

- **Date logged:** 2026-07-28
- **Priority / Question:** Not tied to a research priority — repository
  hygiene, prompted by the creator noticing inconsistent naming and having
  removed several files.
- **Source:** Direct creator instruction, 2026-07-28.
- **What happened:**
  1. **Integrity check run first**, before any renaming. It found four
     dangling references: `contacts_and_funding.md` (including a
     **clickable link in `README.md`**, the public front page),
     `Effective_Prompting_Example.docx`, and `AI_Skills_Hub_Briefing.docx`.
     It also found `Style_Reference_Example.docx` duplicated into
     `drafts/` alongside the tracked copy in `documents/`.
  2. **Naming standardised to lower snake_case** for the repository's
     markdown documents: `PROJECT_BRIEF.md`, `PROJECT_LOG.md`,
     `RESEARCH_LOG.md` and `RESEARCH_QUESTIONS.md` became
     `project_brief.md`, `project_log.md`, `research_log.md`,
     `research_questions.md`. `internal/CONTACTS_AND_FUNDING.md` was
     renamed to match its siblings. 153 cross-references were rewritten
     across tracked and internal files.
  3. **Two deliberate exemptions**, agreed with the creator rather than
     assumed. `CLAUDE.md` stays uppercase because Claude Code looks for
     that exact filename. `README.md` stays uppercase because it is a
     near-universal convention that every developer and GitHub itself
     recognise on sight — lowercase would read as unfamiliar rather than
     consistent. The `.docx` deliverables keep `Title_Case_With_Underscores`
     because they leave the repository as email attachments, where the
     filename is read by the recipient.
     **The resulting rule: snake_case for repository files, Title_Case for
     documents that leave the repository, with README and CLAUDE exempt.**
  4. **Windows case-rename trap handled.** `core.ignorecase` is true on
     this machine, so a direct `git mv` of a case-only rename would not
     have registered. Each file was moved via a temporary name; git
     recorded all four as true renames, preserving history.
  5. **`contacts_and_funding.md` moved to `internal/`** by the creator —
     recorded here as a deliberate reclassification, not a deletion. A
     register of named people one might approach for funding reads
     differently in public than a research log does, however carefully
     worded. `README.md` and `CLAUDE.md` updated accordingly.
  6. **`MIGRATION_CHECKPOINT.md` deleted** outright as spent; it recorded
     a one-off validation of the original Claude Project setup and had no
     inbound references.
- **Inference drawn:** None — hygiene work.
- **Limitations / conflicting evidence:** Historical references to the
  deleted drafts in `project_log.md` Entries 015 and 019, and in
  `research_log.md`, were **deliberately left intact**. Those entries are
  records of what was true when written, and this project's own
  non-alteration convention forbids silently rewriting them to hide that
  the files once existed. Only current-state documents (`README.md`,
  `CLAUDE.md`) were corrected. Two items flagged as outstanding during
  this pass were then resolved in the same session on the creator's
  instruction: the byte-identical duplicate of
  `Style_Reference_Example.docx` (and its `.pdf`) was deleted from
  `drafts/`, leaving the tracked copy in `documents/` as the single
  source; and `documents/Style_Reference_Example.docx` had
  `compatibilityMode` 15 applied, closing the last instance of the
  save-corruption bug diagnosed in Entry 023. Verified by round-trip
  through real Word — all six shape groups survive the save with no VML
  downgrade. **Every `.docx` in the project now carries the
  declaration.** The document's self-check `.pdf` was not regenerated:
  the change is confined to `settings.xml` and does not affect rendering.
- **Effect on project direction:** Repository naming is now internally
  consistent with a stated rule rather than an accident of history. The
  distinction between current-state documents (which must be corrected
  when files move) and historical logs (which must not) is now recorded
  explicitly, since it will recur every time files are removed.

### Entry 025 — PAWH's technical history recorded: the failure catalogue behind the project's method

- **Date logged:** 2026-07-29
- **Priority / Question:** Not tied to a research priority — project
  history, recorded from the creator's own account (2026-07-29). The
  research-evidence half of the same account (the AI Skills Hub user
  journey that prompted PAWH) is `research_log.md` Entry 049; the full
  primary text is held in the internal working notes.
- **Source:** Direct creator account, 2026-07-29.
- **What happened:** PAWH — the predecessor project `project_brief.md`
  describes as historical source material — now has its technical
  history on record, in the creator's own analysis:
  1. **Where it ran:** a ChatGPT project on a Pro subscription,
     building "conceptually legitimate but badly implemented"
     agent-like tools.
  2. **The core mechanism:** periodic "Source of Truth" updates —
     markdown files holding agent guidance, assets and workflows,
     maintained to reduce and optimise context windows and usage —
     delivered by repeatedly uploading a bloated, unorganised zip
     (~400MB at its worst) into the ChatGPT Project Source area.
  3. **Around it:** ChatGPT-generated PowerShell scripts modifying
     project files automatically, and rudimentary git integration via
     the GitHub plugin.
  4. **The failure mode, in the creator's own attribution:** the
     project folder became too large and complex to manually navigate
     and review; over-reliance on AI with insufficient output checking;
     regression, long waits and unnecessarily high usage *despite*
     rules being repeatedly iterated and refined in the project files —
     "an artifact of my poor implementation, not the capability of the
     model used". The attempted cure — meticulously crafted workflows
     per agential task — did not work either.
  5. **The resolution:** stepping back, reviewing alternatives, and
     finding that essentially everything being hand-rolled already
     existed as established convention and tooling (the Claude Code
     workflow now in use). PAWH was closed out as a learning
     experience; selected assets and ideas were retained; the project
     restarted fresh.
- **Inference drawn:** The failure catalogue maps, item by item, onto
  existing conventions the project's future curriculum could teach —
  which makes it distinctive raw material: a genuinely documented
  record of a motivated newcomer independently reinventing standard
  practice badly, before discovering it existed.
  - Source-of-Truth markdown guidance → the `CLAUDE.md` /
    project-instructions convention.
  - Bulk zip re-uploads as state management → version control.
  - Ever-longer rule files fighting regression → context/tooling
    structure (subagents, skills), not rule volume — connecting to the
    Entry 034 illustration already logged in the research log.
  - Unchecked outputs degrading quietly → the verify-against-ground-
    truth discipline this project now applies (`tools/word_preview.ps1`
    et al.).
  Positioning inference, for the creator's later decision rather than
  action now: the founder's journey — earnest official-pathway user,
  failed by it (Entry 049), self-taught through documented failure to
  working practice — is itself the project's strongest single
  credibility narrative, and the repo is its evidence.
- **Limitations / conflicting evidence:** A single retrospective
  self-account; timings and the 400MB figure are the creator's
  recollection. PAWH's artefacts survive and could corroborate details
  if that ever matters. How much of the personal framing becomes public
  is an open decision recorded with the primary text in the internal
  notes — this entry deliberately carries the technical history only.
- **Effect on project direction:** Candidate content for the pilot unit
  ("you will reinvent this badly; here is the existing convention" is a
  teachable pattern with a true story behind it). Confirms the
  project's existing bias toward tooling-verified workflows over
  rule-accumulation as learned, not assumed. No new commitments made.

### Entry 026 — Housekeeping pass: internal-indexing rule applied to CLAUDE.md, prompt-craft feedback rule added, log-amendment policy proposed

- **Date logged:** 2026-07-29
- **Priority / Question:** Not tied to a research priority — repository
  hygiene and working-rule changes, on the creator's instruction to
  transfer the session's conclusions into the repo, verify
  structure/naming, and address historical-log integrity without
  sacrificing openness.
- **Source:** Direct creator instruction, 2026-07-29.
- **What happened:**
  1. **The internal-indexing rule (decided 2026-07-28) is now applied
     in `CLAUDE.md`**, which previously contradicted it: internal files
     are indexed by `internal/README.md`, not by CLAUDE.md's "Where to
     look for what"; the ten-line public description of the
     contacts/funding register was folded into a category-level
     `internal/` bullet, and the "Public repo vs. internal working
     files" section now states the rule and its rationale (a filename
     plus a one-line description can disclose a relationship on its
     own).
  2. **Prompt-craft feedback rule added to `CLAUDE.md`** (creator
     request): brief, concrete, occasional feedback where a prompt's
     construction materially shaped the outcome, plus flagging of
     prompts that would make good teaching material for the prompting
     pilot unit. Chosen framing is explicit-but-brief feedback rather
     than covert steering.
  3. **Stale-content fixes:** the research log's leftover entry-template
     comment (self-marked for removal "once first real entry is added";
     49 entries existed) deleted; CLAUDE.md's recorded memory path
     de-machined (it embedded a previous machine's absolute path — the
     replacement says resolve per machine instead of trusting a
     recorded example).
  4. **Naming/structure check:** this session's new internal files
     conform to the Entry 024 rule (snake_case; README exemption). One
     new explicit rule added to `internal/README.md`: third-party files
     under `reference_material/` keep their original filenames as
     received (provenance); directories the project creates follow
     lowercase snake_case (one directory renamed to comply).
  5. **Log-amendment policy adopted** (creator's explicit approval,
     2026-07-29) and written into `CLAUDE.md` as a new "Amending
     existing content" section. Three tiers, reconciling "open by
     design" with record integrity: *living/current-state content*
     (Open Threads, README, CLAUDE.md, project_brief, source-key status
     notes) freely amendable, since reflecting current truth is its
     function; *dated log entries* append-only in spirit — errors
     corrected by a superseding dated entry or a clearly marked, dated
     correction note inside the old entry (the Entry 033 / Entry 046
     pattern), never silently rewritten, because the logs' evidential
     value depends on being trustworthy records, and a log found to
     have been quietly edited would cost more credibility than any
     awkward entry; *compromising content* removed from current files
     promptly with a dated removal marker, and git history handled per
     the existing retroactive rule (already-committed is
     already-public; rewriting history is a creator decision per item,
     never unilateral). The governing distinction, now stated in
     `CLAUDE.md`: amending for privacy or for currency is legitimate;
     amending for appearance is not, and a correction of record happens
     in the open or not at all.
  6. **Scan result under the adopted policy:** no compromising content
     found in tracked files beyond what is already handled. The
     Instro-related public record (`research_log.md` Entries 031/033
     and the Entry 021 declaration here) was assessed and
     **deliberately left unchanged** under tier 2 — they are honest
     records as written, the standing competing-interests declaration
     covers future publications, and a visibility-change trigger is
     recorded in the internal notes. Rewriting them now is the one move
     that could make an innocent record look managed.
  7. **Open Threads consolidated** (creator's approval, 2026-07-29).
     The section had reached 602 lines of chronological
     resolved/still-open passes interleaved, no longer serving the
     at-a-glance purpose its own header claimed — the clearest
     "confusing" finding of the scan, and a tier-1 living-content edit
     rather than a history change. Every item was traced through its
     supersessions first: 63 catalogued, of which the genuinely open
     ones were regrouped under the ten `research_questions.md`
     priorities plus an external-engagement group and a short,
     explicitly-labelled tail for production items that are not
     research questions. Resolved threads were deleted outright, since
     the dated entry that closed each one is already its record —
     which is now the section's stated rule going forward. Result: 602
     lines to 275, no open item lost. Deliberate scope decisions worth
     recording: the visual-identity thread was dropped entirely (closed
     out at `project_log.md` Entry 011); the local-AI workstation
     items were kept but grouped under a standing "parked" note rather
     than deleted, since parked is not resolved; and Priority 3 now
     carries an explicit pointer showing it is blocked behind the
     technical-vs-literacy reconciliation rather than genuinely empty.
  7. **Model-prompt candidate parked:** the creator's 2026-07-29
     strategy prompt as annotated teaching material for the prompting
     pilot unit — pending the creator's own quality judgement against
     the in-session critique, and requiring redaction (named private
     parties, the commercial relationship, personal history, internal
     file references) before any public form exists. The annotated
     form — a genuinely effective prompt plus its honest improvement
     list — was judged more teachable than an idealised specimen.
- **Inference drawn:** None — hygiene and process work.
- **Limitations / conflicting evidence:** The scan covered tracked
  files as they currently stand; git history was last audited
  2026-07-28 (clean across 15 commits) and was not re-audited here.
  The amendment policy in item 5 is a proposal on record, not a rule in
  force — nothing in this pass touched a dated entry's content.
- **Effect on project direction:** `CLAUDE.md` now agrees with the
  internal-indexing decision instead of contradicting it. The
  "open by design, but not at the expense of integrity" instruction has
  a concrete mechanism awaiting approval rather than an ad-hoc
  practice, and the distinction it rests on — amendment-for-privacy
  vs. amendment-for-clarity vs. correction-of-record — is now written
  down.

### Entry 027 — Primary logo superseded: "GAP" wordmark decided, production parked

- **Date logged:** 2026-07-29
- **Priority / Question:** Not tied to a research priority — visual
  identity, reversing a working decision of 24 July 2026.
- **Source:** Direct creator decision, 2026-07-29.
- **What happened:** The primary mark changes from the existing
  icon+wordmark to a **stylised vector wordmark of "GAP"**. The creator's
  assessment: the current symbol is PAWH-derived in character, somewhat
  generic, and not professional enough to lead. Three reasons recorded:
  clarity at small sizes; producible directly in Inkscape by the creator,
  where the earlier symbol needed AI-mediated curve iteration that the
  project's own vector-handoff rule now steers away from; and "GAP"
  carrying the project's subject matter, the skills gap, so the mark says
  something rather than only identifying. Existing symbol, variants and
  both lockups are **retained as supporting assets — nothing deleted**.
  `project_brief.md` "Visual identity" updated from status FINAL to
  "palette and icon set FINAL; primary mark REOPENED", including the
  explicit note that this reverses its own recorded "not a wordmark-only
  mark" decision.
- **Inference drawn:** None — a stated creator preference, not a research
  finding.
- **Limitations / conflicting evidence:** **No design work has been done
  and none is scheduled** — only the direction is decided. Three questions
  are left open for when production resumes: whether the wordmark stands
  alone or pairs with a reduced device; how it sits against the existing
  lockups; and a deliberate similarity check against the well-known
  clothing retailer of the same name. Different sector, likely fine, but
  better looked at than discovered late.
- **Effect on project direction:** Visual identity is no longer fully
  closed. The change is narrow: which mark leads, not the palette, icon
  set or any existing file's validity.

### Entry 028 — Bias self-check adopted, and reshaped by the source before it was built

- **Date logged:** 2026-07-29
- **Priority / Question:** Priority 4 and Priority 6, via the creator's
  proposal to research human and AI biases and add mitigations as a
  lightweight self-check in the project's working rules.
- **Source:** Creator instruction, 2026-07-29, plus `research_log.md`
  Entry 050 (`[NIST-1270]`, read directly) — that entry holds the
  evidence; this one holds the decision.
- **What happened:** The research contradicted the proposal's original
  shape. NIST states that human biases are largely implicit and that
  awareness of them does not confer control, and warns that surfacing
  bias information to users can produce the opposite of the intended
  effect. An awareness checklist was therefore the one design the
  evidence specifically argued against. What was adopted into `CLAUDE.md`
  instead is **five procedural triggers attached to specific moments** —
  pair foundational claims; apply a reversal test to AI output that
  supports the thesis; record sources that couldn't be retrieved; say
  what the numbers don't count; keep the periodic check independent of
  the author. Three of the five only name practice the project already
  had. The rule carries an explicit **do-not-grow clause** and a
  statement of what it does not claim.
- **Inference drawn:** That the project had independently arrived at
  three of NIST's recommended structural practices (confirm/disconfirm
  pairing, second-model audit, scheduled cadence) is convergence worth
  noting, not validation of them. The one genuine gap it exposed —
  *selective adherence*, accepting supporting AI output with less
  scrutiny than contradicting output — is now covered; `research_log.md`
  Entry 013 had only caught the input-side version of the same problem.
- **Limitations / conflicting evidence:** `[NIST-1270]` is US, voluntary,
  and **published March 2022** — it predates general use of
  conversational AI assistants and addresses algorithmic decision
  systems, which is not this project's usage pattern. It gives **no
  effect sizes** for any recommended mitigation, so the alternatives are
  reasoned, not demonstrated. It was read because it was named as an
  approved source, not found through a balanced search, and has no
  disconfirming pair yet — logged as an open thread, since a working rule
  now rests on it. Whether structured practice beats awareness remains
  genuinely unsettled across Entries 028 (research log), 050 and this.
- **Effect on project direction:** A working rule exists where none did.
  The material is also candidate teaching content, but that is a separate
  track and is not decided here.

### Entry 029 — Log-amendment policy relaxed; entry-length and lessons-to-content rules added

- **Date logged:** 2026-07-29
- **Priority / Question:** Not tied to a research priority — working
  rules, arising from the creator's aim to make the logs more readable
  and to convert lessons already learned into teaching material.
- **Source:** Direct creator decision, 2026-07-29.
- **What happened:** Three changes to `CLAUDE.md`.
  1. **The amendment policy proposed in Entry 026 is now in force, and
     relaxed on adoption.** Its original tier 2 allowed exactly one
     retroactive fix to a dated entry: a broken cross-reference. The
     creator's compromise widens this to any edit that is minimal and
     serves clarity or correctness. The operative test written in: does
     the edit change *what the entry claimed, decided or knew at its
     date*? If not, edit it and say nothing. If it does — including when
     the original claim was wrong — it is a correction of record and
     takes a dated note or superseding entry. Explicitly not licensed:
     condensing entries because the log feels long, and smoothing wording
     that is awkward because the thinking was.
  2. **"Log entries earn their length"** — a going-forward format rule.
     Detail belonging in the thing produced lives there and is
     referenced, not restated. Applies to new entries only.
  3. **"Lessons learned become learning content, not only rules"** — when
     a lesson here would be a genuine pitfall for a solo practitioner
     building AI capability without an institution behind them, it goes
     to two places: the rule that prevents recurrence, and candidate raw
     material for teaching output, flagged at the moment the rule is
     written and paired with a research pass so it arrives with evidence
     rather than as anecdote.
- **Inference drawn:** Readability of the logs was diagnosed as a
  navigation problem rather than a length problem, which is why the fix
  is a forward format rule plus the existing index/Open Threads
  structure, rather than retroactive condensing.
- **Limitations / conflicting evidence:** The relaxation creates real
  room for judgement, and the honest risk is that "clarity" quietly
  absorbs edits that are really about appearance. The test above is the
  only guard, and it depends on being applied in good faith; git history
  remains the backstop. No existing entry was edited under the new rule
  in this pass.
- **Effect on project direction:** The record can now be tidied where
  tidying costs nothing, without opening the door the original rule was
  written to keep shut. The lessons-to-content rule turns the project's
  own accumulated mistakes into an input for the teaching output rather
  than only into internal governance.

### Entry 030 — "Premature governance" reframed: the test is demonstrated need, not timing

- **Date logged:** 2026-07-29
- **Priority / Question:** Not tied to a research priority — working rules.
- **Source:** Direct creator decision, 2026-07-29.
- **What happened:** The standing caution against premature governance was
  softened in `CLAUDE.md` ("Working approach") and `project_brief.md`
  ("Relationship to PAWH"). The concern remains valid and the rule still
  requires a demonstrated need, but the criterion is now stated
  explicitly as **the need, not the speed at which a rule arrived**.
  Recency is not evidence of prematurity, and judging a rule, decision or
  file by how quickly it was added rather than by what it does is not a
  fair assessment of it. PAWH's defect is restated as one of *fit* —
  machinery exceeding what the work required — rather than of timing.
  The bias self-check's do-not-grow clause was also rebased onto its own
  evidence (`[NIST-1270]` on flagging backfiring) instead of leaning on
  the general failure-mode framing.
- **Inference drawn:** None — a stated creator position.
- **Limitations / conflicting evidence:** `project_log.md` Entry 025
  records the PAWH failure mode in the creator's own attribution at that
  date and is **deliberately left unedited**, per the tier-2 rule: this
  is a change of current stance, not a correction of what was believed
  then.
- **Effect on project direction:** Removes a standing bias toward
  treating new rules as suspect by default, while keeping the
  requirement that each one earn its place.

### Entry 031 — Review feedback applied: canonical-check rule, formatting convention, current-state smoothing

- **Date logged:** 2026-07-29

- **Priority / Question:** Not tied to a research priority — working rules,
  arising from the creator's review of commit `c1eaa3e`.

- **Source:** Direct creator decision, 2026-07-29.

- **What happened:** Four changes.

  1. **Bias self-check trigger 5 rewritten.** It previously read "let
     someone who isn't the author check", making independence the point.
     It now reads **"nothing becomes canonical unchecked"**: every
     AI-produced output gets a human read before it lands as project
     fact, and that human can be the creator. The risk being addressed
     is unreviewed material quietly compounding into canon, not a lack
     of independence. Independent review — a different model, an outside
     reader — is kept as a separate and less frequent practice, for
     occasional intervals and on completion of substantial deliverables,
     explicitly not a substitute for the routine check.

  2. **The `[NIST-1270]` disconfirming-pair debt is closed** rather than
     carried. Existing precedent for the practices it supports was
     judged strong enough, and the confirm/disconfirm rule is reserved
     for claims that would change project direction. The separate gap —
     no post-2023 source on human–LLM interaction — stays open at low
     priority.

  3. **Current-state documents smooth over inconsequential changes.**
     Added as a corollary to amendment tier 1, after `project_brief.md`
     was written to narrate its own logo reversal. State the position;
     let `project_log.md` hold the history. Visible supersession notes
     are reserved for changes a reader would be misled without.

  4. **Markdown formatting convention adopted:** a blank line between
     list items whenever an item runs to more than one line, plus a
     general instruction to break up dense blocks. The previous
     run-straight-on style turned multi-line lists into walls of text.

- **Inference drawn:** None — creator decisions on review.

- **Limitations / conflicting evidence:** The formatting convention is
  applied to new and substantially edited content only, so the repo will
  hold both styles until files are touched for other reasons. A full
  reformatting sweep has not been done and is not scheduled.

- **Effect on project direction:** The self-check's most-used trigger now
  describes a routine habit rather than an occasional audit, which is
  what makes it usable day to day. Three of the four changes came out of
  a review pass, which is itself the trigger-5 practice working.
