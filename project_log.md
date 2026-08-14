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
  arising from the creator's review of the commit that added the bias
  self-check, 2026-07-29.

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

### Entry 032 — List spacing applied repo-wide; the rule made unconditional

- **Date logged:** 2026-07-29

- **Priority / Question:** Not tied to a research priority — formatting,
  superseding Entry 031's statement that no sweep was scheduled.

- **Source:** Direct creator instruction, 2026-07-29, on review of the
  partial application.

- **What happened:** Entry 031 adopted list spacing only for items running
  to more than one line, and only for new or edited content. Both limits
  were wrong in practice: the result was lists spaced in some places and
  not others, which reads worse than either style applied throughout. The
  rule is now **unconditional** — a blank line before every `- ` item,
  short ones included, at every nesting level — and has been applied to
  all 17 markdown files in the working tree, tracked and internal. 823
  blank lines inserted, nothing else changed. Verified three ways: every
  added line is blank, no blank line falls between two table rows, and
  internal word counts are identical before and after.

- **Inference drawn:** None — mechanical formatting.

- **Limitations / conflicting evidence:** Numbered (`1.`) lists were not
  included, the instruction being specific to dashed items. Those already
  written with spacing keep it, so numbered lists remain inconsistent
  across the repo. Worth settling if it becomes visible.

- **Effect on project direction:** The logs are materially easier to scan,
  which was the underlying aim behind the readability work in Entries 029
  and 031 rather than an end in itself.

### Entry 033 — Numbered lists folded into the spacing rule, superseding Entry 032's stated limitation

- **Date logged:** 2026-07-29

- **Priority / Question:** Not tied to a research priority — formatting.
  Supersedes the limitation recorded in Entry 032.

- **Source:** Direct creator instruction, 2026-07-29.

- **What happened:** Entry 032 recorded that numbered (`1.`) lists were
  left out of the spacing sweep, on a literal reading of an instruction
  that specified dashed items. The same inconsistency argument applies to
  them, so the rule is now **all list items, dashed and numbered alike**.
  A further 116 blank lines were inserted across five tracked files and
  four internal ones, bringing the total to 939. The rule text in
  `CLAUDE.md` was updated to match. Nothing else in the repo uses list
  syntax, so coverage is complete.

- **Inference drawn:** None — mechanical formatting.

- **Limitations / conflicting evidence:** None outstanding. Entry 032's
  figure of 823 and its statement that numbered lists were excluded were
  both accurate at the time it was written and are left unedited; this
  entry supersedes them rather than rewriting the original, per the
  amendment rule.

- **Effect on project direction:** Closes the formatting work. Also a
  worked example of the tier-2 rule in practice: Entry 032 had already
  been committed, so the correction took a new entry rather than an
  in-place edit.

### Entry 034 — Domain and project email acquired; website direction noted, architecture not yet decided

- **Date logged:** 2026-07-29

- **Priority / Question:** Not tied to a research priority — project
  infrastructure and a working consideration on deliverable shape.

- **Source:** Direct creator decision, 2026-07-29.

- **What happened:** `groundedaipractice.co.uk` registered via GoDaddy,
  with a one-year Microsoft 365 mailbox alongside it. Three intended uses
  named, none yet decided:

  1. host the pilot learner trial;

  2. host an accompanying chatbot, provisionally OpenWebUI with agents
     built per learner profile — which connects to the deferred "local AI
     workstation" second track in `project_brief.md`;

  3. serve as a linkable proof of work from GitHub and LinkedIn.

  No site exists, no hosting is chosen, and the creator has stated no
  prior website-building experience, so this is direction only.

- **Inference drawn (this entry's own):** The static site and the chatbot
  have **incompatible hosting requirements** and should not be treated as
  one decision. A proof-of-work site is static and hosts free on GitHub
  Pages or similar, which also reinforces the repo-as-evidence angle.
  OpenWebUI is a stateful containerised application needing a persistent
  server. The standard resolution is a subdomain split — static site at
  the apex, chatbot at something like `chat.` — which keeps the two
  decisions independent rather than letting the harder one dictate both.

- **Limitations / conflicting evidence:** Two risks are flagged but
  unresearched. **Email deliverability:** a newly registered domain has no
  sending reputation, and Microsoft 365 configures SPF and DKIM but
  typically not DMARC, so outreach sent early from this address could be
  filtered — university mail systems especially. **Data protection:** a
  learner trial that builds per-learner agent profiles is personal-data
  processing and profiling under UK GDPR, which affects trial design and
  may require ICO registration. Neither has been checked against a source.

- **Effect on project direction:** Adds a concrete hosting question to the
  deliverable-shape thread. The data-protection point is not merely
  compliance overhead here — a project about responsible AI practice
  handling learner data carelessly would undercut its own argument, so
  getting it right is a credibility asset. Outreach-channel implications
  are held internally.

### Entry 035 — Existing PC identified as the server host; deferred, but it revives the second track

- **Date logged:** 2026-07-29

- **Priority / Question:** Not tied to a research priority — infrastructure
  availability. Bears on the deferred "local AI workstation" second track
  in `project_brief.md`.

- **Source:** Direct creator statement, 2026-07-29, with full component
  list supplied.

- **What happened:** There are **two machines, with distinct roles.**

  - **Main desktop** — Ryzen 7 7800X3D, Radeon RX 7900 XT (20 GB VRAM),
    32 GB. Also used for gaming. This is the machine the inherited PAWH
    workstation architecture was scoped around, already recorded under
    "Inherited workstation architecture" in `project_brief.md`.

  - **Secondary machine, earmarked as a dedicated server** — Ryzen 5
    5600X (6c/12t), 32 GB DDR4-3600, GTX 1060 6 GB, 500 GB M.2 SATA SSD
    plus a 500 GB HDD, 450 W PSU, Mini ITX. Originally intended as a
    Linux media player. A UPS is planned for it.

  The secondary machine can host the chatbot server rather than renting a
  VPS, removing the monthly hosting cost noted in Entry 034.
  **Explicitly deferred — not a current priority.**

- **Inference drawn (this entry's own):**

  1. The secondary machine is comfortably adequate for server duty,
     because **OpenWebUI is a web front end and does not itself need a
     GPU** — it talks to a backend, which can be a hosted API. CPU and
     RAM are the binding constraints for that use and both are generous.

  2. The GPU only matters if inference runs locally, and the two machines
     differ sharply there. The secondary machine's GTX 1060 (6 GB, Pascal,
     no tensor cores) realistically fits a 7–8B model at 4-bit
     quantisation with limited context — adequate for demonstrating local
     inference, not for serving it. The main desktop's 7900 XT has 20 GB
     and handles substantially larger models. So the natural split is
     **serving and always-on duty on the secondary machine, local
     inference experiments on the main desktop** — which also matches the
     PAWH architecture's own assumption that services stop cleanly so
     gaming performance isn't compromised.

  3. The build-out is genuine teaching material of exactly the kind the
     lessons-to-content rule anticipates — Linux, containers, reverse
     proxy, TLS, firewalling, backups, monitoring — with the advantage
     that it would be written from having done it rather than researched.

- **Limitations / conflicting evidence:** Three risks unresearched, all of
  them specific to the secondary machine in continuous-duty use. Its
  **PSU dates from the 2015 CX450M line** and is the component most likely
  to fail under 24/7 operation. **Single-drive storage with no redundancy
  or backup** matters more than usual because a learner trial would hold
  personal data, which UK GDPR requires be protected against loss, not
  only against disclosure. And **home hosting has connectivity
  constraints** — dynamic IP, possible CGNAT, and residential ISP terms
  that often disallow inbound services.

- **Effect on project direction:** Removes the recurring VPS cost from the
  chatbot plan. It does **not** revive the deferred second track — that
  was deferred as a matter of focus rather than for want of hardware, and
  remains closed until the creator reopens it. What this changes is that
  the second track, whenever it resumes, now has two machines with a
  natural division of labour rather than one shared with gaming. Nothing
  is scheduled; this records availability, not a decision to proceed.

### Entry 036 — Raster-to-vector tracing pipeline established; GAP wordmark traced

- **Date logged:** 2026-07-30

- **Priority / Question:** Not tied to a research priority — tooling and
  design production. Prompted by the creator selecting a wordmark concept
  and needing it as an editable vector rather than a redraw from visual
  reference.

- **Source:** Direct creator instruction, 2026-07-30.

- **What happened:**

  1. **Concept chosen.** Five stylised "GAP" wordmark directions were
     written as image-generation prompts. The creator generated them in
     Ideogram (Pro subscription — free generation had been withdrawn since
     the third-party pricing summaries consulted were written) and selected
     the concept in which the A is negative space, bridged by an Ember
     crossbar. Kept as `gap_reference_1.png`, with a baseline-bar variant
     kept as `gap_reference_2.png`.

  2. **Traced, not redrawn.** The reference was colour-separated with
     Pillow, each mask traced through Inkscape 1.4.4's `object-trace`
     action (potrace), and reassembled with exact palette values into
     `assets/logo/logo_wordmark.svg`. Verified by rendering the
     result back to PNG and comparing it against the reference.

  3. **Generalised into `tools/trace_reference.py`**, the one-off pipeline
     having worked. Testing auto-detection against both references exposed
     two defects, since fixed. The quantiser was starved at too few
     colours and spent its palette on background variations, missing the
     artwork. And anti-aliasing ramps between background and artwork passed
     both the distance and pixel-share filters, crowding out the genuine
     accent colour. The second is fixed geometrically — a candidate lying
     on the line between the background and an already-accepted colour is
     rejected as a blend artifact — rather than by threshold tuning, which
     had already failed once.

  4. **Rule recorded** in `CLAUDE.md` under Working approach, "Raster
     concept to editable vector", with the tool indexed in the same edit.

- **Inference drawn:** None beyond the creator's own assessment that this
  removes a recurring pain point in AI asset creation.

- **Limitations / conflicting evidence:** The traced wordmark is **not a
  finished asset.** It reproduces the source raster's irregularities: the
  two angled cuts facing the gap do not share an exact angle, corner radii
  vary between the G and the P, baseline and cap height are not level, and
  long edges wobble by a pixel or two. These are hand-corrections in
  Inkscape, and the file should not be exported to PNG, built into lockups,
  or used in any document until they are made. **These were made on
  2026-07-31 — see Entry 037.** Separately,
  `object-trace`'s parameter format is absent from `--help` and was
  recovered by reading the action's own error output — a future Inkscape
  release could change it without notice.

- **Effect on project direction:** Unblocks the visual-identity work that
  the report redraft and README rewrite are waiting on. More generally, it
  establishes a repeatable capability: a flat concept from any raster
  generator can now reach Inkscape as real geometry, removing the blind-SVG
  iteration loop that discouraged the creator during PAWH and recurred
  here.

### Entry 037 — GAP wordmark refined and finished; variant set produced

- **Date logged:** 2026-07-31

- **Priority / Question:** Not tied to a research priority — design
  production, completing what Entry 036 deliberately left unfinished.

- **Source:** Creator's hand refinement in Inkscape, 30–31 July 2026, plus
  direct instruction.

- **What happened:**

  1. **The concept was fixed, not merely tidied.** The traced reference read
     as "G — P": a floating dash, not a letter. The prompt that generated it
     had specified the A as pure negative space "bridged by one small
     floating horizontal crossbar", and Ideogram executed exactly that. The
     refinement inverts which part carries colour. Ember now marks the A's
     two counters — the triangle at its apex, and the opening below its
     crossbar — so the white band between them reads as the crossbar itself.
     The A is still undrawn negative space; what changed is that its
     internal structure became visible.

  2. **Letterforms regularised against Public Sans Bold**, the typeface used
     elsewhere in the identity. The master keeps a hidden copy of that
     reference type (`a_overlay`, `display:none`), now documented in an XML
     comment as deliberate rather than leftover, on the creator's
     instruction to retain it.

  3. **A non-uniform vertical stretch was found and removed.** The outer
     group carried sx=1.0592, sy=1.1701 — roughly 10% of vertical stretch,
     applied by dragging rather than redrawing, which thickens horizontal
     strokes relative to verticals. Corrected by bringing sy down to match
     sx, restoring the aspect ratio from 2.512 to 2.778 against the traced
     2.790, and the canvas was refitted to the artwork. Done as a direct XML
     edit rather than a round-trip through Inkscape's plain-SVG exporter,
     which would have stripped the live path effects.

  4. **Variant set produced**, following the conventions the symbol variants
     already set: `logo_wordmark_mono.svg` (Ember recoloured to Ink, single
     colour) and `logo_wordmark_reversed.svg` (letterforms white, Ember
     retained, transparent background). Nine PNG exports at 256/512/1024
     across the three files.

- **Inference drawn:** The mono variant works because the A is defined by
  the white space around its counters rather than by their colour, so
  recolouring them to Ink leaves the letter legible. Checked by rendering,
  not assumed.

- **Correction, 2026-07-31 (same day).** The claim immediately above — that
  the mono variant was "checked by rendering, not assumed" — overstates what
  happened, and the check it describes was worthless. That render was produced
  by Inkscape, which recomputes a path's geometry from `inkscape:original-d`
  wherever a live path effect is attached, and therefore displays a corrected
  shape even when the stored `d` attribute, the only thing any other renderer
  reads, is wrong. The variants were in fact broken at the time; the creator
  found this by opening them in a browser. Verifying Inkscape's output with
  Inkscape is circular and proves nothing, in the same way a LibreOffice
  preview cannot confirm a Word document. The variants recorded above were
  subsequently rebuilt and checked in a browser (Entry 038).

- **Limitations / conflicting evidence:** Minimum usable width is around
  160px; by 110px the white crossbar between the two Ember shapes begins to
  close and the A degrades. The lower Ember trapezoid still carries its own
  non-uniform transform (sx/sy 0.787, about 1.1 degrees of skew), so its
  corner radii do not match the triangle's — left alone deliberately, since
  changing it would alter the design rather than correct an accident. The
  similarity check against the well-known clothing retailer's "GAP"
  wordmark remains outstanding and is recorded in `project_brief.md` as
  still open.

- **Effect on project direction:** The primary mark is finished, which
  unblocks the README rewrite, the report redraft, and the LinkedIn
  profile. No lockup pairing the GAP wordmark with a reduced device has
  been produced; whether one is wanted is undecided.

### Entry 038 — Wordmark finished; profile-picture set built

- **Date logged:** 2026-07-31

- **Priority / Question:** Not tied to a research priority — design
  production, closing out the visual identity.

- **Source:** Creator's Inkscape work and direct instruction, 31 July 2026.

- **What happened:**

  1. **Further hand refinement** of `logo_wordmark.svg` beyond Entry 037,
     including path labels corrected to snake_case (`g_p`, `top_void`,
     `bottom_void`).

  2. **The remaining vertical stretch is deliberate and stays.** The outer
     group carries sx=1.0592, sy=1.0920 — roughly 3% of non-uniform vertical
     scale, applied because the creator could not achieve the intended
     proportions by moving nodes directly. Recorded explicitly so a later
     pass does not "correct" it. This must not be confused with the 10%
     stretch removed in Entry 037, which was accidental. Resulting aspect
     ratio is 2.693.

  3. **Variants regenerated** from the finished master — `logo_wordmark_mono`
     and `logo_wordmark_reversed`, plus nine PNG exports.

  4. **Profile-picture set built**: square and circular, each in standard,
     inverted and monochrome treatments, at 84% and 80% of a 1024 canvas with
     an edge-flush border, following the construction of the existing
     symbol-based avatars. Eighteen PNG exports. The wordmark is scaled
     uniformly in all six, so the deliberate stretch carries through
     unchanged, and live path effects are stripped so the exports are plain,
     self-contained SVG rather than files whose `d` could drift from their
     `inkscape:original-d`.

  5. **The clothing-retailer similarity question is closed** — the creator's
     decision, having looked at it deliberately, that the two marks are
     visually unrelated and the sectors differ, so the shared word needs no
     design response. Recorded in `project_brief.md`.

  6. **A browser-based self-check was added to `tools/trace_reference.py`,
     then reverted** on the creator's instruction. The tool stands as
     committed, without it.

- **Inference drawn:** None.

- **Limitations / conflicting evidence:** The wordmark avatars hold to about
  64px. Below that the A's crossbar closes, and the symbol-based avatars
  remain the correct choice — a 2.7:1 mark cannot survive a 32px favicon, so
  the two sets are complementary rather than one superseding the other. No
  lockup pairing the wordmark with a reduced device has been produced;
  whether one is wanted remains undecided.

- **Effect on project direction:** The visual identity is complete for current
  purposes. The README rewrite, the report redraft and the LinkedIn profile
  are unblocked.

### Entry 039 — Callout-card and pull-quote padding bug found and fixed; fitshapes.py built and promoted to tools/

- **Date logged:** 2026-07-31

- **Priority / Question:** Not tied to a research priority — document
  construction defect and tooling.

- **Source:** Creator's visual review of the redrafted report, with an
  annotated screenshot marking the intended vertical extent against the
  actual rendered extent.

- **What happened:**

  1. **The defect.** Callout cards and pull quotes are built as `wpg:wgp`
     drawing groups with a height set once at construction time. Nothing
     in Word recomputes that height when the text inside changes, so a
     card built by copying an existing card's XML and substituting new
     text keeps the old card's height regardless of how much text now
     fills it. Present in all three callout cards in the redrafted report
     (up to 136.1pt for a two-line label plus body against a 65pt icon
     well) and, to a smaller extent, in two of the six groups in
     `exports/Style_Reference_Example.docx` itself — the other four had
     already been built correctly, height matching the icon well almost
     exactly.

  2. **`tools/fitshapes.py` built** to fix it properly rather than by
     hand. Measures each paragraph's real wrapped height using the
     installed Public Sans font faces at their actual weight, style, size
     and line-spacing multiplier — not an estimated line height — then
     sets card height to `max(text height, icon-well height) + 2x padding`
     (quote height to `text height + 2x padding`), recentring the icon,
     divider bar and text box. Widths are never touched, preserving the
     existing size-preset rule that the icon well is fixed and only the
     text column resizes.

  3. **A real bug found and fixed during testing, not before shipping.**
     The tool's first version detected a callout card by checking for the
     literal substring `<pic:pic>` inside its group. This missed every
     callout in the report, because Word had serialised those particular
     picture elements as `<pic:pic xmlns:pic="...">` — the same element,
     carrying its own inline namespace declaration, which is valid and
     ordinary OOXML but broke an exact-substring check. The bug was
     silent: the tool ran without error and reported success, having
     quietly skipped all three callout cards and fitted only the report's
     three pull quotes (which don't need picture detection). Found by
     noticing the report's callout heights were unmoved after a run that
     claimed to have fitted 3 groups, when 6 were expected. Fixed by
     matching `<pic:pic\b` instead of the exact tag. Re-run against the
     style reference confirmed the fix produced byte-identical output
     there, since that document's picture elements happened to serialise
     without the inline namespace.

  4. **Both fixed documents verified through real Word**, not rendering
     alone — `word_roundtrip_test.ps1` (save survives) and
     `word_preview.ps1` (renders correctly), per this project's own rule
     that a render is not a save check. The style reference dropped from
     72.4–124.7pt group heights to 54.3–104.5pt range; six of its groups
     were already close to correct and moved by under 1pt.

  5. **Style reference promoted** to `exports/Style_Reference_Example.docx`
     as the corrected version, re-approved as canonical on this basis. The
     redrafted report was re-fitted with the same tool and both files
     placed back in `drafts/`.

- **Inference drawn:** A template-substitution build process (write once,
  copy the XML, swap the text) is the ordinary way these documents get
  built in this project, and it is also the ordinary way this specific bug
  gets introduced — the geometry is never wrong by design, only stale
  relative to text that has since changed. This is now a standing
  construction rule (see CLAUDE.md, "Word document conventions") rather
  than a one-off fix, since it will recur every time a card or quote
  template is reused with different content.

- **Limitations / conflicting evidence:** The tool does not verify its own
  output — it explicitly says so, both in its docstring and in its own
  final line of console output — because Word verification already has
  dedicated tooling that handles the safety-critical parts (confirming a
  genuinely new WINWORD.exe process before automating it) and duplicating
  that here would be redundant and riskier. The `has_pic` bug is the kind
  of defect that would have shipped silently if the report's callout
  heights hadn't been checked against the expected group count — worth
  remembering when trusting this tool's console output alone in future
  runs, rather than the actual rendered result.

- **Effect on project direction:** Removes a defect that would otherwise
  have recurred in every future document built from these templates.
  Unblocks treating the redrafted report as visually finished, subject to
  the creator's own outstanding wording and formatting edits noted
  separately. `tools/fitshapes.py` is now indexed in `CLAUDE.md` alongside
  the other Word tooling, per the newly adopted rule that any bespoke tool
  which might be reused is promoted to `tools/` rather than left in a
  scratch directory.

### Entry 040 — Report revision tooling built; §4 rebuilt on a corrected attribution

- **Date logged:** 2026-07-31

- **Priority / Question:** Not tied to a research priority — document
  production and tooling, arising from the creator's review pass over
  `drafts/UK_AI_Skills_Ambition_Report.docx`.

- **Source:** Production work, 2026-07-31, on the research in
  `research_log.md` Entry 059.

- **What happened:**

  1. **`tools/docx_text.py` built** to read a `.docx` as plain text
     including shape content, because reviewing prose that lives inside
     callout cards and pull quotes previously meant rendering the whole
     document to PDF. It drops Word's `<mc:Fallback>` duplicate of every
     shape; without that, every card and quote is reported twice.

  2. **`tools/docx_edit.py` built** as its editing counterpart, after
     manual copy-paste of revisions into Word introduced three defects in
     one pass — an orphaned paragraph where a replacement removed its own
     lead-in sentence, a stray quote mark and a `?` in a table cell, and a
     doubled dash in a §8 bullet. It applies a declared list of edits and
     writes nothing unless every one matches the expected number of times.

  3. **Three structural defects found in that tool by the project's own
     checks, not by inspection**, each now a permanent guard in it:
     ElementTree renamed every namespace prefix to `ns0:`-style on
     serialisation, which left `fitshapes.py` reporting zero shape groups
     in a document that had six; it wrote empty elements as `<tag />`
     where Word writes `<tag/>`, which crashed the fitter's regexes; and
     it dropped root-element namespace declarations that no element uses
     but `mc:Ignorable` names, which Word rejects as a corrupt file rather
     than as a namespace error. Only the last was caught by Word itself —
     the first would have passed every check except a shape count.

  4. **Report revised** across §1, §4, §5, §6, §8 and the source list.
     The substantive change is §4, rebuilt after Entry 059 established
     that findings the section credited to the statistics regulator were
     FE Week's journalism and the department's own admissions. The OSR
     letter's undertaking on methodological detail was added as a seventh
     drawing group, cloned from an existing pull quote.

- **Inference drawn:** None beyond the above — production record. The
  attribution correction and its reasoning are Entry 059.

- **Limitations / conflicting evidence:** The XSD validator in the bundled
  docx skill could not run (`defusedxml` missing); Word's own save and
  render checks stood in for it, which is the stronger test anyway.

- **Visual check completed later the same day, and it found two defects
  nothing else had.** poppler-utils was installed and all eight rendered
  pages were read. Both defects were **pre-existing** — present in the
  pre-edit file, confirmed by running the same diagnostic against it —
  and both came from prose being pasted into Word by hand:

  1. **252 non-breaking spaces** across five pasted paragraphs. Word
     cannot break a line at a non-breaking space, so it broke mid-word
     instead: "it p / ublished", "throu / ghout", "Forty- / eight". In the
     §1 NOTE callout this also overflowed the shape, clipping the last
     line — and `fitshapes.py` could not have prevented it, because it
     measures assuming normal word wrapping and its height was correct
     for that assumption.

  2. **§1's heading had lost its `Heading1` style**, leaving only a stray
     `spacing after=60`. It rendered at body size, and silently dropped
     out of the outline level that Word's navigation pane and any table
     of contents depend on — the exact thing the named-style system in
     "Word document conventions" exists to guarantee.

  A third, smaller version of the same thing: three Overview paragraphs
  carried a direct `spacing after=60` the surrounding paragraphs do not,
  so they sat visibly tighter than the rest of the page.

  All three were fixed with two new `docx_edit.py` operations — a bulk
  character replacement, and `set_style`, which restores a named style or
  clears direct paragraph formatting. Re-verified: SAVE OK, 8 pages, all
  read.

  **The general lesson is that none of this was visible in the text.**
  `docx_text.py` reported the document as correct throughout, because the
  words were correct. Only the render showed it. Pasting prose into Word
  by hand is the mechanism that introduced every one of these, which is
  the argument for routing revisions through `docx_edit.py` instead.

- **Effect on project direction:** Gives the project a read/edit pair for
  `.docx` prose revision, which is the loop the report is now in. Both are
  indexed in `CLAUDE.md`. The guards in `docx_edit.py` are the reusable
  part: they encode what Word and `fitshapes.py` each silently tolerate.

### Entry 041 — Report review completed: 29 edits, three research corrections, and what a human read caught that no check could

- **Date logged:** 2026-07-31

- **Priority / Question:** Not tied to a research priority — the record of
  the creator's full review pass over
  `drafts/UK_AI_Skills_Ambition_Report.docx`.

- **Source:** Review session, 2026-07-31. Research findings are
  `research_log.md` Entries 059–061.

- **What happened:**

  1. **Twenty-nine edits across three passes**, each proposed with its
     defect named, approved individually, then applied through
     `docx_edit.py` with a dry run first. Sections 1 and 4 were rebuilt,
     §6 went from three paragraphs to six, and the report grew from eight
     pages to nine.

  2. **Three research corrections came out of the review, not out of
     planned research.** The creator asked whether the OSR letter was
     actually available; it was, and reading it showed the report had
     credited the statistics regulator with findings that were FE Week's
     journalism and the department's own admissions (Entry 059). The
     creator then spotted the government's delivery tracker, which marks
     Recommendation 14 delivered and names five publications, and shows
     the only recommendation addressing the general workforce sitting
     among the two skills items *not* met (Entry 060). Following the
     numbers on that tracker produced the largest correction of all: the
     June 2025 target was 7.5 million, not 10 million, and three
     government sources disagree about it (Entry 061). That last one sat
     in the report's opening sentence.

  3. **The bias self-check fired, and the existing list caught it.**
     Item 2, the reversal test, applied to §6: the report was scrutinising
     a 119-organisation government survey while presenting the PRIMES
     framework's own evidence base without caveat — a 536-response survey
     run through Amazon Mechanical Turk that its authors say skews
     London-based and AI-engaged. The caveat is now in §6. No new item was
     added to the list, because an existing item covered it. Per the rule
     in `CLAUDE.md`, that is the outcome that keeps the list at five.

  4. **A seventh drawing group** was added — the OSR letter's undertaking
     as a pull quote, cloned from an existing quote rather than
     hand-written, then refitted.

- **Inference drawn:** The review caught a class of defect that none of
  this project's checks can reach. `word_roundtrip_test.ps1` proves a file
  saves, `word_preview.ps1` proves it renders, `docx_text.py` proves what
  it says — and every one of those passed on a document that credited the
  wrong party with a regulator's findings, introduced four public bodies
  without explaining any of them, and opened on a target that did not
  exist when the figure beneath it was counted. Those needed a reader.
  The relevant rule already exists as bias self-check item 5, that nothing
  becomes canonical unchecked; this is the clearest evidence so far of
  what it is for.

- **Limitations / conflicting evidence:** The June 2025 announcement now
  carrying the report's opening paragraph was read through a fetch
  extraction rather than raw, and the Prime Minister's 9 June Tech Week
  speech is unread — so the target correction rests on a source that
  itself needs a direct read. The three 2021 FE Week articles remain
  unread in full, leaving §4's geographic-filter claim without a
  direct-read source. Both are logged as open threads. File placement had
  to be handed to the creator throughout, because the shell in this
  session could not write into the repository.

- **Effect on project direction:** The report is materially more accurate
  than it was this morning, and its weakest remaining claims are now
  named rather than buried. The working loop — propose with the defect
  stated, approve individually, accumulate, dry-run, apply, refit, verify
  through real Word, hand back — is the method for any future document
  revision, and is what the two new tools exist to serve.

### Entry 042 — External review returns; report reframed around a public-audience accountability argument

- **Date logged:** 2026-08-01

- **Priority / Question:** Priority 1/10 — the direction of the project's
  primary deliverable. Follows Entry 041's revision record.

- **Source:** External review arranged and relayed by the creator:
  professionals in the field, plus non-technical readers matching the
  project's stated target audience. Reviewers deliberately not named in
  this tracked file.

- **What happened:**

  1. **The findings.** The report's arguments read as abstract and vague
     to a lay reader; qualifiers and technical detail smother structurally
     sound points; the document lacks a single comprehensible conclusion;
     and the fully AI-generated prose register contributes to all three.

  2. **The decision.** The report is reframed for the project's actual
     target audience, the general reader. Its argument is no longer
     organised toward "where GAP fits". The new spine, per the creator's
     sketch: government prices AI's promise in the hundreds of billions
     and promises ten million upskilled workers; its published progress
     cannot be checked by anyone outside government; the delivery and the
     evidence base are concentrated in companies with a stake in the
     answer; the population the ambition implies — the general public and
     small organisations, increasingly exposed to AI whether they know it
     or not — is the one the structure underserves; and government
     already owns the tools to fix the measurement. GAP appears as a
     declared interest, not as the solution.

  3. **Claim triage against the evidence base.** Most of the sketch is
     already carried by logged findings: the target/figure sequence and
     unit mismatch (Entries 053/061), self-assessment throughout the
     delivery chain (Entries 044/053/060), the Skills Toolkit precedent
     and the OSR letter (Entries 055/059), interest concentration in the
     evidence base (Entries 046/048/052), the professional-supply policy
     focus and the Recommendation 19 gap (Entries 051/058/060), public
     exposure and recognition figures (Entry 058), and the benchmark's
     partial application (Entry 053).

  4. **Three elements ruled unpublishable as worded, substitutes
     adopted:**

     - Any suggestion a party "could be intentionally misrepresenting"
       figures. Substitute: the published definition itself includes the
       partners' internal training, the breakdown is withheld, and the
       figure is therefore unverifiable — the report's existing
       construction, which carries the point without alleging intent.

     - "Government does not understand AI well enough to make informed
       policy." This claim has sat in `project_brief.md` as
       flagged-unsupported since July. Substitute: state what the record
       shows — estimates the Action Plan itself called imprecise and
       outdated, a government-commissioned review calling the evidence
       base limited, productivity claims footnoted to unpublished
       business interviews — and let the reader conclude.

     - "The initiative will fail its target" as prediction. Substitute:
       on the published numbers, progress toward a workers target cannot
       be known at all, because the count is in courses; the one number
       that would settle it — distinct workers — is unpublished, which is
       what the planned FOI asks for.

  5. **Five research threads opened** (recorded in `research_log.md`
     Open Threads): direct evidence of policymaker comprehension;
     verification of partner-claimed totals; a citable source for AI
     embedding in everyday products; an official SME-population cite; and
     a decision on whether regulator capability enters scope.

  6. **Pending creator decisions:** final thesis wording; confirmation of
     the two-document shape (short public report plus the existing draft
     as technical companion); the drafting process for the public
     document's voice; and whether the FOI is now sent (standing
     constraint: no external approach without explicit per-approach
     instruction).

- **Inference drawn:** The independent-review tier of the bias self-check
  (item 5's rarer second tier) has now earned its place twice — Entry 019
  and this. A lay reader catches a register problem that expert review
  and every in-repo check structurally cannot.

- **Limitations / conflicting evidence:** Feedback arrived via the
  creator's summary rather than reviewers' verbatim notes. The triage
  classifications are Claude's, reviewed by the creator in session but
  not yet tested against a redraft.

- **Effect on project direction:** The nine-page draft is demoted to
  evidence companion. The primary deliverable becomes a short
  public-audience report built on the reframed argument. No document
  edits made yet; the redraft begins once the pending decisions are
  taken.

### Entry 043 — Reframe decisions taken: blended thesis, creator-voiced prose, infographics convention

- **Date logged:** 2026-08-01

- **Priority / Question:** Priority 10 / deliverable direction — answers
  most of the pending decisions recorded in Entry 042.

- **Source:** Creator decisions, 2026-08-01.

- **What happened:**

  1. **Thesis.** The public report's spine blends all three candidate
     framings — accountability (the counting handed to the companies
     selling the training), steering blind (progress reported in numbers
     government cannot verify, against a workforce it has not measured),
     and reach (AI arriving in everyone's life while the training reaches
     the people who already had it) — presented as one cohesive argument
     rather than a choice among them.

  2. **Prose process.** For outward-facing documents, Claude supplies the
     agreed structure, the arguments and a rough draft; the creator
     writes most of the final prose over it. Written into `CLAUDE.md`
     Working approach the same day. This answers the external-review
     finding that a fully AI-generated register contributed to the
     draft's problems.

  3. **The comprehension claim is reinstated in evidential form.** The
     creator pushed back on Entry 042's route-around, holding that the
     claim was flagged pending research rather than judged wrong, and
     pointed at the Prime Minister's London Tech Week speech. The speech
     was read the same day and the pushback was borne out — see
     `research_log.md` Entry 062 for the confirmed misstatement, the
     closed attribution question, and the four-claim verification
     catalogue still open. The published form states the checkable record
     and lets the reader conclude.

  4. **Infographics adopted as a standing convention**, serving the
     publishing funnel: LinkedIn post → profile → synopsis document →
     technical companion → repository, with each element standing alone.
     Two production lanes are defined in `CLAUDE.md`: data-driven figures
     scripted and reproducible from the repo, and bespoke narrative
     graphics through the existing raster-concept-to-trace pipeline.
     Every outward graphic carries its own source-and-date line. First
     candidate figures, from logged findings: courses-versus-people; the
     2021/2026 precedent parallel; the 7.5m-to-10m target move set
     against the course count; the met/unmet recommendation split.

- **Inference drawn:** None — decision record.

- **Limitations / conflicting evidence:** The FOI decision (Entry 042
  item 6) remains open. Substitutions 1 and 3 from Entry 042 were not
  contested and stand.

- **Effect on project direction:** Unblocks the redraft. Next concrete
  step: Claude produces the structure-and-arguments rough draft of the
  synopsis document for the creator's prose pass, per the new process.

### Entry 044 — Reframing: the practice system is the project's primary artifact; product direction adopted

- **Date logged:** 2026-08-03

- **Priority / Question:** Priority 10 / project direction, eventual
  format and commercial potential; touches Priority 7 (delivery format)
  and Priority 2 (audience).

- **Source:** Creator realisation and decisions, 2026-08-03. Evidence
  citations below are to `research_log.md`.

- **What happened:**

  1. **The realisation.** The project's most distinctive artifact is not
     any single research report but the system that produces them: the
     file structure, working rules, verification tooling, logs and memory
     architecture, deliberately built so any LLM can parse and act on
     them. In effect the repo is a custom research-and-learning agent
     with built-in tools and workflows — a working demonstration of the
     practical AI capability the project exists to teach. The AI Skills
     Hub research is not displaced by this framing; it becomes the case
     study the system produced, proof the method finds things official
     channels miss.

  2. **Working direction adopted (creator decision, 2026-08-03).** GAP's
     product direction is to package this practice as a learning and
     research capability for SMEs and individuals: educating users in
     proper use of the AI tools now available to them, optimising the
     context they give a model in each case, and building custom —
     sometimes fully local — tools and workflows where those reduce
     usage cost, increase privacy and decrease reliance on cloud
     services. Platform vendors productising the context-and-workflow
     layer (persistent project context, skills, memory, agent tooling)
     is treated as infrastructure to leverage and teach, not as
     competition: GAP's role is helping people choose and use that layer
     well. The aim is to let small organisations adapt and integrate AI
     in the custom ways large organisations already can — helping the
     smaller actor keep up. Evidential status: the large/small adoption
     gap is evidenced (Entry 029, complications logged in Entry 041;
     `[OECD-SMEAI25]`: 40% large-firm vs 11.9% small-firm adoption,
     OECD-wide), and the claims-separation below governs the rest. The
     decision is a direction, not a validation — the demand side remains
     unresearched (see effect section). Marketing-register framings were
     screened out under the evidence discipline before recording.

  3. **What the research log supports in this positioning, cited
     precisely.** Government-led AI skills delivery and its counting run
     through eleven large commercial partners (Entries 046, 053); the
     delivery design assumes an employer rolling training out to staff,
     a layer SMEs and individuals lack (Entry 026 and the primary-
     audience decision, `project_brief.md`); the one Action Plan
     recommendation about ordinary workers is not met (Entry 060);
     government's own evidence review concedes policy has focused on AI
     professionals and evidence on AI skills for life is "necessarily
     limited" (Entry 058); and no published breakdown of completions by
     employer size exists (Entry 064), so who is actually being trained
     cannot be verified from outside. One delivery partner holds
     builder, evidence-supplier and delivery-partner roles
     simultaneously (Entry 046) — recorded as documented role
     concentration. The claim "almost all training happens at large
     firms" is deliberately not made: the checkable version — the
     structure tilts toward large-firm delivery and the published
     figures cannot show who is trained — is stronger and survives
     scrutiny.

  4. **Inference recorded as inference.** As large-employer training
     pools saturate, meeting the workforce ambition — 7.5 million
     workers by 2030 as originally stated, with government sources
     disagreeing on the later 10-million framing (Entry 061) — would
     require reaching smaller organisations and individuals: the
     population GAP targets. In that context a completed GAP unit, or a
     custom tool or workflow built with GAP guidance, is a candidate
     countable "upskilled" outcome, connecting this direction to the
     official-channel positioning aim already in `project_brief.md`.
     This saturation argument is unverified inference, not evidence.

  5. **Motive attribution excluded.** Why this market is underserved is
     a motive question about identifiable actors; per the public/
     internal rule it is not recorded in tracked files. The fact of
     underservice stands on the entries cited above.

- **Inference drawn:** The repo can generate the missing cost/quality
  evidence itself: a controlled before/after comparison (a defined task
  run cold versus with the full context system, measuring tokens,
  iteration rounds and output quality) would convert the creator's n=1
  experience into checkable data. Logged as a research question, not yet
  scheduled.

- **Limitations / conflicting evidence:** The demand side (whether SMEs
  will pay, what they would pay for) is untested against any evidence.
  The adoption-gap evidence carries logged complications (Entry 041).
  The cost/quality mechanism rests on the creator's own experience
  (n=1) until the comparison above is run. The distance from a bespoke
  personal system — one person, one machine, one toolchain — to a
  generalisable product is the actual hard work and is not addressed by
  the reframing.

- **Effect on project direction:** `project_brief.md` gains this as a
  working direction under "Longer-term direction and positioning";
  `research_questions.md` Priority 10 gains validation questions
  covering the demand side and the before/after measurement. The pilot
  unit remains the first output and the public report the primary
  research deliverable — this reframes how existing work is presented,
  it does not reorder the queue. Flagged as candidate teaching material
  for the prompting/context curriculum: the chatbot-level-usage pattern
  and its cost consequences are exactly the pitfall the pilot audience
  faces (no redaction needs identified).

### Entry 045 — Every human-run tool gets a GUI; pattern set in prep_photos.py

- **Date logged:** 2026-08-03

- **Decision (creator):** Every GAP tool a human drives gets a simple
  graphical interface alongside its CLI — retroactively for the
  existing tools and as standard for future ones. The reasoning
  connects to Entry 044's audience framing: the learners and small
  organisations the project now aims at are exactly the users a
  terminal-only tool turns away, and the creator includes themselves in
  that assessment for day-to-day use.

- **Pattern (established and verified in `tools/prep_photos.py`):**
  running the script with no arguments (or `--gui`) opens a small
  tkinter window; any argument gives the exact CLI behaviour, so
  scripts and Claude-driven runs are unaffected. The window is a thin
  layer calling the same functions as the CLI — never a second
  implementation — and exposes only the decisions a person actually
  makes (which photos, the naming word, AI-size vs full quality,
  destination), with a preview step mirroring `--dry-run` before
  anything is written. Missing-dependency errors become plain-language
  dialogs carrying the install command. Zero new dependencies: tkinter
  ships with Python on Windows; the PowerShell tools will use WinForms,
  built into Windows PowerShell. Verified by CLI regression (identical
  behaviour after refactoring shared functions out of `main()`) and a
  scripted GUI run — populated programmatically, previewed, screenshot
  inspected, then a real conversion through the window's threaded path.

- **Effect:** Standing rule added to `CLAUDE.md` Working approach the
  same day. Retrofits pending for the seven other tools: `docx_text`,
  `docx_edit`, `fitshapes`, `trace_reference`, `word_preview`,
  `word_roundtrip_test`, `make_share_folder` — queued for creator
  review of the pattern before rollout.

### Entry 046 — GUI pattern refinement: GAP branding, embedded in the script

- **Date logged:** 2026-08-03

- **Decision (creator):** the tool GUIs carry GAP branding — the
  palette and a small logo — kept lightweight and compatible. On the
  logo's delivery the creator overrode the first implementation:
  runtime loading from `assets/logo/png/` (with a text fallback) was
  replaced by embedding the images in the script as base64, since
  users of a copied script won't have the repo structure alongside,
  and a few kilobytes of image data is not meaningfully "bulk".

- **How:** palette applied through ttk's built-in `clam` theme in the
  roles `project_brief.md` records — Paper ground, Ink text, Stone
  hints, Mist/Sand neutral buttons, Ember reserved for the primary
  action (Convert). Wordmark at 180 px in the header, above its
  ~160 px minimum usable width; symbol as the 64/32 px window icon,
  where the 2.7:1 wordmark cannot survive. Blobs generated by the new
  `tools/embed_logo.py` (re-runnable whenever brand assets change;
  inserts or refreshes the constants, refuses partial sets, verifies
  the patched file still parses before writing). Net cost ~10 KB of
  PNG (~13 KB as base64) in a 41 KB tool; Tk decodes base64 PNG
  natively, so the patched tool gains no imports.

- **Verification:** scripted run of the branded window (preview,
  screenshot inspected, real conversion including HEIC through the
  threaded path); CLI dry-run regression unchanged.

- **Effect:** `CLAUDE.md` GUI rule amended with the branding
  requirement and `embed_logo.py` indexed, same day. Applies to all
  retrofits. One open point for the creator: `embed_logo.py` is a
  development-time build utility rather than a learner-facing tool —
  proposed as the recognised exception to the GUI rule, rather than
  getting a window of its own.

### Entry 047 — GUI retrofit: trace_reference.py and make_share_folder.ps1

- **Date logged:** 2026-08-03

- **Decision (creator):** retrofit the GUI pattern to the remaining
  user-facing tools — identified as `trace_reference.py` (a person
  picks a concept image and traces it) and `make_share_folder.ps1`
  (run by hand before a Cowork/Design session) — then commit the GUI
  body of work. The docx/Word pipeline tools are Claude-driven
  self-check steps rather than user-facing, so their retrofits stay
  pending without blocking the commit.

- **What was built:**

  1. `trace_reference.py`: pipeline extracted from `main()` into
     `run_trace()` and `resolve_palette()` (shared by CLI and window;
     `TraceError` replaces mid-pipeline `sys.exit` so the window can
     catch failures), plus a branded tkinter window — reference
     picker, derived output path, colour count, snap-to-palette
     toggle, a "Detect colours" preview that runs the real detection
     without tracing, and the trace itself threaded with the same log
     lines as the CLI.

  2. `make_share_folder.ps1`: build wrapped in `Invoke-ShareFolder`
     (CLI and window share it), plus the first WinForms window — mode
     radios, destination with browse, Ember build button, log pane.
     **Bare invocation now opens the window rather than running a
     Docs build**; scripted runs pass `-Mode`, as the usage lines
     always showed. A `-GuiSelfTest` switch renders the window,
     screenshots it and builds into a test folder — the scripted
     verification hook for a language where driving a window from
     outside is harder than in tkinter.

  3. `embed_logo.py` extended to PowerShell targets: `$NAME = @'...'@`
     here-strings, replace-only (a `.ps1` has no `__main__` anchor to
     insert above), decoded in WinForms via `Convert.FromBase64String`.

- **Verification:** make_share_folder — the CLI Docs build and the
  window's build produce the identical 17-file set; window screenshot
  inspected (wordmark, symbol title-bar icon, palette correct).
  trace_reference — window screenshot inspected; the detect/preview
  path verified end to end (near-brand test colours snapped correctly
  to Ember and Ink); the missing-Inkscape refusal behaves exactly as
  before. **The actual trace run is unverified on this machine, which
  has no Inkscape install** — first use on the Inkscape machine should
  confirm it, though the pipeline is the same lines relocated, not
  rewritten.

- **Effect:** GUI retrofit status — done: `prep_photos.py`,
  `trace_reference.py`, `make_share_folder.ps1`. Pending
  (Claude-driven pipeline tools, deprioritised by the creator's
  user-facing narrowing): `docx_text.py`, `docx_edit.py`,
  `fitshapes.py`, `word_preview.ps1`, `word_roundtrip_test.ps1`.
  Proposed exception: `embed_logo.py` (build utility). `CLAUDE.md`
  rule and index updated to match.

### Entry 048 — The guard carried the name it guarded against; history rewritten; repo audit

- **Date logged:** 2026-08-03

- **Priority / Question:** Priority 10 (public presentation); repo
  privacy discipline. Also the audit record required by `CLAUDE.md`,
  "Repo audit — scheduled, not ad hoc".

- **Source:** Pre-commit review and creator decisions, 2026-08-03. Work
  done in session.

- **What happened:**

  1. **The defect.** `.githooks/pre-commit` — a tracked, public file —
     carried the private marker name in plain text, beside a comment
     pointing at the private contacts file under `internal/`. The hook
     skipped scanning itself, so it could never have caught it. The
     disclosure was not only the name: the name plus its context
     identified that person as one held in the project's private
     contacts file.

  2. **The audit gap.** The hook entered history in the commit titled
     "Prepare for public release", 2026-07-28. The audit recorded
     that day covered 15 commits — the state *before* that commit. The
     guard written during the pre-publication audit is what carried the
     name past it. Exposure: a public repo, six days, 17 of 33 commits,
     with no forks or stars at the time of the rewrite.

  3. **Go-forward fix.** The marker list moved to
     `internal/private_markers.txt`, never tracked. `pre-commit` was
     rebuilt to read it and to refuse to run if it is missing, and a new
     `pre-push` re-scans the whole tracked tree and the pushed commits
     before anything leaves the machine. Both tested: a poisoned staged
     file blocks, clean states pass.

  4. **History rewritten.** The creator's decision was that the privacy
     concern supersedes both the disruption of rewriting shared history
     and the project's preference for showing its record openly. A
     mirror backup was taken first
     (`C:\dev\gap-history-backup-2026-08-03.git`, 33 commits);
     `git filter-repo` replaced the name across all commits;
     verification scanned every revision individually and found zero
     hits; both `.docx` deliverables were integrity-checked after the
     blob rewrite. All hashes from 2026-07-28 onward changed. The
     force-push landed the same day; a GitHub Support request to purge
     the overwritten commits follows it.

  5. **New rule.** Every commit and push now gets a review gate
     (`CLAUDE.md`, Git conventions) — the judgement layer above what the
     hooks enforce mechanically.

  6. **Audit record.** The creator's decision is that this counts as the
     scheduled repo audit. Passes run: the Claude scan of tracked files
     and full history, and creator verification of every flagged item.
     Findings beyond the marker: two current-state documents carrying
     stale claims, both corrected (the `drafts/` index still calling the
     report unreviewed, and a brief bullet still calling a flagged claim
     unsupported after `research_log.md` Entries 062–063 evidenced its
     core). No emails, credentials, dangling cross-references or private
     content found in tracked files, the new tools, or any historical
     `.docx` blob.

- **Inference drawn:** The defect was structural rather than careless.
  The hook was the one tracked file the marker check exempted, so no
  amount of care in writing it would have been caught by the tooling.
  That is why the fix is a review gate rather than a resolution to be
  more careful.

- **Limitations / conflicting evidence:** A rewrite cannot retract what
  was already public. Anyone who cloned during the six-day window holds
  a copy; GitHub keeps overwritten commits reachable by their hash until
  garbage collection or a Support purge; third-party mirrors and
  crawlers are outside anyone's control. Whether the repo was public for
  the whole window is not verifiable from local data. The independent
  second-model pass was not run this time, so this audit rests on one
  model plus creator verification.

- **Effect on project direction:** Hooks, marker file and review gate
  are in place; `CLAUDE.md`'s audit line updated to 2026-08-03. Flagged
  as candidate teaching material, and a strong one: a guard that
  published the thing it existed to block, and the fact that deleting a
  file never removes it from git history. Redaction need: the name
  itself, which must not appear in any teaching version.

### Entry 049 — Claude-driven tools stay command-line

- **Date logged:** 2026-08-03

- **Priority / Question:** Priority 7 (delivery format).

- **Source:** Creator decision, 2026-08-03. Settles the pending list and
  the proposed exception in Entry 047.

- **What happened:** The docx/Word pipeline tools — `docx_text.py`,
  `docx_edit.py`, `fitshapes.py`, `word_preview.ps1` and
  `word_roundtrip_test.ps1` — need only a command line for now, and
  `embed_logo.py`'s proposed build-utility exception is confirmed on the
  same basis. Claude or a build step runs all six; a person does not, so
  Entry 045's justification does not reach them.

- **Inference drawn:** The rule's operative test is therefore *would a
  person without a terminal habit ever run this*, not *is it a tool*. If
  any of the six later becomes something a learner runs directly, this
  decision reopens with it.

- **Limitations / conflicting evidence:** Not applicable.

- **Effect on project direction:** Clears Entry 047's pending list.
  `CLAUDE.md`'s GUI rule states the decision rather than a pending
  retrofit.

### Entry 050 — Second track reopened for the server build; home server project adopted

- **Date logged:** 2026-08-04

- **Priority / Question:** Priority 6 (technical and conceptual scope) for
  the build itself; bears on the deferred second track in
  `project_brief.md`.

- **Source:** Creator decision, 2026-08-04, with a full hardware
  inventory, settled-decision list and step-by-step build guide supplied
  from prior work in a separate conversation.

- **What happened:** An established home server project — Linux install,
  storage, remote access, self-hosted services, a small NAS and a small
  website — was brought into the repo. It runs on the secondary machine
  recorded in Entry 035, and the creator has **reopened the deferred
  second track** for the server half specifically. Local inference, RAG,
  voice, model routing and automation stay deferred.

  Three scoping decisions were taken at adoption:

  1. **The build is project work, not merely infrastructure.** Entry 035
     recorded the machine's availability while explicitly declining to
     revive the track. That is now reversed by decision rather than by
     drift.

  2. **The AV workstream stays outside the repo.** The wider project also
     covers a home cinema. None of it is tracked. What survives in the
     build documents is only the part that constrains the server: the GPU
     is the sole display output, audio leaves the machine over HDMI to a
     receiver, the projector is the display (so Ubuntu Desktop rather
     than Server), and the machine sits in a living space rather than a
     garage, which makes noise a design constraint.

  3. **Room photographs are internal only.** Several frames carry a named
     private individual, personal likenesses and a third-party business
     name with a phone number. They go to `internal/build_photos/` under
     the same treatment as the LinkedIn headshot. Noted at the time: the
     pre-commit marker scan reads text, so it offers no protection
     against a name inside an image.

  **Correction to Entry 035's hardware record.** That entry listed the
  secondary machine as holding "a 500 GB M.2 SATA SSD plus a 500 GB HDD".
  The current state is the SSD alone, with three spare HDDs — one known to
  be 2 TB, the other two of unknown capacity, age and health — none yet
  fitted. Whether the 500 GB HDD is among those three is unresolved and
  sits as an open question in the build document. Entry 035 is left
  unedited; this entry supersedes its inventory.

- **Inference drawn:** Two of the three risks Entry 035 flagged are
  answered by decisions the incoming project had already taken
  independently — storage redundancy by the no-RAID plan with a dedicated
  rsync target and an out-of-machine cold spare, and home-hosting
  connectivity by Tailscale and Cloudflare Tunnel, both of which avoid
  inbound ports and sidestep dynamic IP and CGNAT entirely. **PSU age is
  not addressed by anything in the incoming project**, and on a 450 W unit
  from the 2015 CX450M line facing continuous duty it is the least
  mitigated risk in the build. It is carried into
  `drafts/home_server_build.md` as an open item rather than left to lapse
  with Entry 035.

- **Limitations / conflicting evidence:** The build guide is
  AI-generated and has not been verified against the hardware. It
  self-flags at least one assumption — that populating the M.2 slot with a
  SATA drive disables a SATA port through lane sharing — as needing
  confirmation against the ASRock AB350 Gaming-ITX/ac manual. Under bias
  self-check item 5 it lands as a draft carrying marked unverified claims,
  not as canonical procedure. Its instructions are followed and corrected
  as the build proceeds; corrections are the point of keeping it in
  `drafts/`.

- **Effect on project direction:** `project_brief.md`'s second-track
  section moves from deferred to active for the server half. Two new
  files in `drafts/`: `home_server_build.md` (standing state) and
  `home_server_build_guide.md` (procedure), both indexed in `CLAUDE.md`.
  Nothing in the current research or pilot-unit work is reordered — the
  public report and the prompting unit remain ahead of this. Entry 035's
  third inference stands: the build-out is teaching material of the kind
  the lessons-to-content rule anticipates, now written from having done it
  rather than researched, and that connection should be revisited when the
  build completes rather than mined for content while it is in progress.

### Entry 051 — Markdown-to-Word conversion tooling; the build guide as first output

- **Date logged:** 2026-08-04

- **Priority / Question:** Priority 7 (delivery format) and Priority 8
  (information architecture — how Word, web and repository outputs relate
  without becoming duplicate authorities).

- **Source:** Creator request, 2026-08-04, following Entry 050: the build
  guide is easier to follow as a formatted document than as Markdown in a
  code editor.

- **What happened:** Two command-line tools were built and the guide's
  Word version produced from them.

  `tools/md_to_docx.py` converts Markdown to a house-style `.docx`. The
  design decision worth recording is that it **contributes no formatting
  of its own** — `styles.xml`, `numbering.xml` and `settings.xml` are
  taken from a template document, by default
  `exports/Style_Reference_Example.docx`. Every earlier Word deliverable
  here was built by hand-writing `word/document.xml`, which is
  proportionate for a six-page catalogue built once and not for a
  document regenerated whenever its source changes. A converter holding
  its own copy of the house style would drift from the reference the
  moment either changed, and the drift would stay invisible until two
  documents were compared side by side.

  `tools/build_server_guide_figures.py` draws the guide's five figures.

  Both are command-line only, consistent with Entry 049 — a build step
  runs them, not a person, so Entry 045's GUI rule does not reach them.

  **Two findings from building it.** The machine in use has no Inkscape
  installed and no `cairosvg` or `matplotlib`, so the figures are drawn
  with Pillow, which is present because `fitshapes.py` depends on it.
  This is not a departure from the raster-to-vector rule: that rule
  governs concept artwork, where Claude cannot see what it draws, and
  these are boxes and arrows on a computed grid with no curve work in
  them. Separately, the first figure drafted showed the media drive being
  backed up, which the guide's own cron job does not do — it copies
  `/home` and `/opt` only. The figure was corrected and a NOTE callout
  added making the gap explicit in the text.

- **Inference drawn:** A generated document introduces a duplicate-
  authority risk that the repo's existing conventions do not cover, since
  every previous `.docx` here was itself the source. The rule adopted is
  that the Markdown is authoritative and the `.docx` is an artefact:
  editing the document directly loses the edit at the next rebuild.
  Recorded in `CLAUDE.md` against the file rather than as a general rule,
  because it is currently true of exactly one document.

- **Limitations / conflicting evidence:** The converter handles the
  constructs this guide uses and no more — no nested lists, no inline
  links, no footnotes. It has been exercised on one document. Callout
  heights are emitted as a guess and depend on `fitshapes.py` to be
  right, so the existing post-construction sequence is not optional.

- **Effect on project direction:** Markdown-sourced Word output is now a
  route this project has. Whether the UK-climate report or the pilot unit
  should use it is not decided here — both have hand-built construction
  histories and neither is a straightforward Markdown source.

### Entry 052 — Build guide split public/internal; synopsis published; three findings corrected

- **Date logged:** 2026-08-05

- **Priority / Question:** Priority 7 (delivery format) and Priority 10
  (public presentation). The guide is also the structural prototype for
  the planned learning units, which reaches Priority 4.

- **Source:** Creator decision, 2026-08-05, plus four checks recorded
  below.

- **What happened:** The home server guide moved to `internal/` and a
  shorter public account, `drafts/home_server_synopsis.md`, was written to
  stand in the repository. The standing-state document moved with it. The
  split is by **what the content is about**, not by sensitivity grading:
  the guide is about one machine on one home network and includes
  recovering personal data from an old drive, none of which generalises;
  the synopsis is the decisions and their reasoning, which is the part a
  stranger can use.

  The guide was substantially rewritten rather than relocated. Extended
  Linux orientation section, a graphical route given alongside every
  command-line one, the PAWH command-unit teaching pattern applied
  throughout (instruction, command, replica, check), and terminal replicas
  in place of bare code blocks — see Entry 053 for that tooling.

  **Four things were checked and three of them changed what the document
  says.**

  1. **Neither UK sports service supports Linux.** NOW's platform list
     excludes it and the check is on the operating system, not the
     browser, so user-agent spoofing does not defeat it; discovery+/HBO
     Max omits Linux browsers likewise. Compounding it, Widevine on Linux
     is L3 (software) only, which caps most premium services at 720p and
     rules out 4K. The guide previously implied this was configurable. It
     is not, by any route or provider, and the recommendation is now a
     separate streaming device on the receiver's second HDMI input.

  2. **Docker publishes past UFW.** UFW manages the `INPUT` chain; Docker
     writes its published ports into `FORWARD` via NAT. A container port
     is therefore reachable across the network while `ufw status` reports
     it closed, with no warning. The build now binds containers to
     `127.0.0.1` and verifies with `ss -tlnp` rather than trusting the
     firewall's own summary. This is the single most consequential
     correction in the rewrite.

  3. **`unattended-upgrades` covers less than assumed.** It ships
     configured for the Ubuntu `-security` pocket only, so Tailscale,
     Docker and Caddy — all installed from their own repositories — never
     update automatically. A monthly manual update is now part of the
     documented routine.

  4. **Windows 7 Professional had no BitLocker** (Ultimate and Enterprise
     only), which confirmed the old 2 TB drive's data is recoverable
     despite three forgotten account passwords. A Windows password
     controls login, not encryption. This one confirmed rather than
     overturned the working assumption.

  Storage paths also changed from `/mnt/media` to `/srv/media`. The FHS
  defines `/srv` as data served by this system, which is what a media
  library and a Samba share are; `/mnt` is for temporary mounts. The
  original followed the common home-server convention, which is simply
  wrong on this point.

- **Inference drawn:** The public/internal boundary here is not about
  embarrassment, which is what `CLAUDE.md`'s existing framing mostly
  anticipates. It is about **generality** — the guide is not unfit to
  publish, it is uninteresting to anyone who does not own this machine,
  and it names a home network. That is a third reason for the split and
  worth naming as one.

- **Limitations / conflicting evidence:** None of the four findings has
  been confirmed against the hardware, because the build has not reached
  those steps. They rest on vendor documentation and, for the Docker
  behaviour, on Docker's own networking documentation plus consistent
  independent reporting. The SATA lane-sharing question was **retired
  rather than answered**: published sources contradict each other and
  mostly describe a different board, so the guide now instructs reading
  the BIOS storage screen, which is ground truth.

- **Effect on project direction:** The repository gains a public artifact
  about the build and loses the operational detail. `CLAUDE.md`'s index
  and `internal/README.md` are updated. The guide's structure —
  orientation before action, one idea per step, a stated check per step,
  replicas of what the learner should see — is now the working prototype
  for the learning units, and is the first thing to review when those
  start rather than being redesigned from nothing.

### Entry 053 — PAWH replica system adapted; terminal replicas replace bare code blocks

- **Date logged:** 2026-08-05

- **Priority / Question:** Priority 4 (learning design) and Priority 7
  (delivery format).

- **Source:** `GAP_Replica_System_Transfer_Pack_2026-08-05`, supplied by
  the creator — the PAWH replica framework packaged for migration, with
  its own rules extract, source audit and honest limitations list.

- **What happened:** `tools/replica.py` now renders terminal replicas from
  a JSON description: a picture of a shell session showing the window, the
  prompt colouring and the returned output, generated rather than
  screenshotted.

  The reason is a teaching one. A fenced code block shows what to type and
  not what happens, and a learner who has never opened a terminal cannot
  tell from one whether they have succeeded. Real screenshots were not an
  option: they would have to be taken on the machine being built, before
  it is built, and would carry its real hostname and network.

  **What was carried over:** the template-generation strategy over one-off
  images, generic names only, application chrome kept faithful to the real
  application rather than restyled into GAP's palette, nothing inside the
  window but prompt, command and output, and the five-step command-unit
  teaching sequence.

  **What was deliberately changed, each with a reason:**

  1. **The primary renderer is Ubuntu's GNOME Terminal, not PowerShell.**
     PAWH taught Windows; this build is Ubuntu. PowerShell is retained
     because parts of the build genuinely happen on Windows — writing the
     install USB, and connecting over SSH.

  2. **JSON input, not YAML.** PyYAML is not a dependency of this repo and
     every tool here that can be standard-library-only is. The pack's
     schema was already JSON Schema.

  3. **No File Explorer renderer.** The pack's audit records that the
     manifest and schema describe one the generator never implemented.
     Claiming it would reproduce exactly the defect that audit exists to
     flag.

  4. **Validation refuses a real user path.** The pack states the
     generic-names rule; enforcing it in code means it cannot be forgotten
     under time pressure.

  One implementation detail worth recording because it was not obvious:
  the renderer draws on a **fixed character grid**, placing each character
  at its own cell rather than letting the font advance. Box-drawing
  characters in `lsblk` and `systemctl` output do not occupy exactly one
  cell in Consolas, so drawing whole strings left every column after one
  of them slightly askew — subtle enough to look like carelessness rather
  than a bug, which is worse. A terminal is a grid; the renderer is now
  one too.

- **Inference drawn:** Generating the illustration from the same data that
  describes the command removes a class of drift the project would
  otherwise have to police by hand — a corrected command cannot leave a
  stale screenshot behind, because there is no screenshot to go stale.
  That property is the reason to prefer this over screenshots even once
  the machine exists.

- **Limitations / conflicting evidence:** The font is a substitution —
  Ubuntu ships Ubuntu Mono, absent on Windows, so Consolas stands in and
  metrics differ slightly from a real terminal. Everything carrying
  meaning is accurate. Coverage is two renderers and the tests are smoke
  tests, not visual regression; a rendering change would be caught by a
  person looking, not by the suite.

- **Effect on project direction:** The transfer pack stays unchanged as a
  reference snapshot; `tools/replica.py` is the active GAP implementation.
  Replica specs and renders live in `assets/replicas/`, JSON as the source
  of truth. Available to the learning units when they start, which was the
  point of migrating it rather than rebuilding it later.

### Entry 054 — Server-track technical findings: Windows disk recovery, BIOS revision, SATA question retired, Linux DRM ceiling

- **Date logged:** 2026-08-05

- **Priority / Question:** Not tied to a research priority — technical
  findings on the server track. Finding 4 bears on Priority 6 (technical
  scope) and on any future claim the project makes about Linux as a
  platform to recommend.

- **Source:** Web sources cited below, all checked 2026-08-05. Build
  execution detail is held internally, per Entry 052.

- **What happened:** Four findings.

  **1. A Windows account password does not encrypt a disk.** It controls
  login. Mounted from another operating system, the files are readable
  whoever has forgotten what. The only barrier would be full-disk
  encryption, and **Windows 7 Professional did not include BitLocker for
  fixed drives** — Ultimate and Enterprise only, per Microsoft's edition
  documentation and contemporaneous reviews. Absent a deliberate EFS
  choice, such a disk is plain NTFS and fully readable. Consequence for
  the build: a recovery pass now precedes any formatting step, because
  "the password is lost" is not a reason to treat data as gone.

  **2. BIOS instructions rewritten for the actual board and revision.**
  ASRock Fatal1ty AB350 Gaming-ITX/ac on UEFI P7.40, with real menu paths
  rather than generic setting names. Two additions the original lacked:
  **CSM disabled**, to force a clean UEFI install rather than a legacy one
  that is harder to repair later; and an explicit instruction **not to
  flash the BIOS**, since P7.40 already carries the AGESA that permits a
  Zen 3 chip on B350 — which is why the machine posts at all — and a
  failed flash on this board has no easy recovery.

  **3. The SATA lane-sharing question was retired rather than answered.**
  Published sources contradict each other on which port an M.2 SATA module
  disables, and most describe the AB350 Pro4, a different board with two
  M.2 slots. ASRock's own specification page for the ITX board carries no
  footnote on it. Rather than pick a source, the guide now directs reading
  `Advanced > Storage Configuration`, which lists what the board actually
  sees. With two drives in a board having at least three usable ports, the
  answer changes no decision.

  **4. Live UK sport cannot run on this machine.** NOW does not support
  Linux — an operating-system check rather than a browser one, since
  user-agent spoofing does not defeat it — and discovery+/TNT Sports does
  not list Linux browsers among its supported platforms. Independently,
  Widevine on Linux is L3 (software) only, which most premium services cap
  at 720p and which cannot serve 4K. The decision is therefore
  architectural rather than a matter of provider choice: a dedicated
  streaming device on a second RX-V677 HDMI input.

- **Inference drawn:** The DRM finding generalises past this build. Any
  future project claim about Linux as a media or workstation platform has
  to account for commercial streaming being partly closed to it — not by
  technical incapability but by platform policy and a DRM tier Linux
  cannot reach. That is a concrete, citable instance of a constraint this
  project should understand before recommending Linux to a learner
  audience, and it belongs in any teaching material that comes out of this
  build.

- **Limitations / conflicting evidence:** The BIOS menu paths are written
  from ASRock's AM4 UEFI conventions and are **not verified against P7.40
  on the machine** — the guide flags where labels vary and instructs
  proceeding without any setting that cannot be found. The board manual
  PDF could not be parsed when fetched (binary content), so it is logged
  as unfetched rather than as absent, per bias self-check item 3. The
  streaming-platform support pages are vendor sources and were not
  cross-checked against a second independent source; they are, however,
  the operators' own statements about their own products, which is the
  appropriate authority for what a service supports.

- **Effect on project direction:** Finding 4 is the one that reaches past
  this build, and is carried into the project's own claims rather than
  only into the guide. The build documents absorb the rest; they are
  internal, per Entry 052, and their revision detail belongs with them.

- **Sources (all checked 2026-08-05):**

  - ASRock, product specification page, Fatal1ty AB350 Gaming-ITX/ac.
    Vendor/Commercial. Confirms four SATA3 ports and one Ultra M.2 socket
    supporting M.2 SATA and PCIe modules; carries no lane-sharing
    footnote.

  - NOW, help centre, "Watch NOW on your laptop or computer".
    Vendor/Commercial. Supported browsers are Windows and macOS only.

  - discovery+, help centre, "Browsers and devices supported by
    discovery+". Vendor/Commercial. Device list excludes Linux browsers.

  - Widevine security-level documentation and secondary technical
    coverage of L1/L2/L3. Mixed Vendor/Commercial and
    Independent/Academic. Linux desktop is L3-only; L3 is
    software-based and publicly broken, hence common 720p caps.

  - Microsoft edition documentation and contemporaneous technical
    reviews of Windows 7 BitLocker. Vendor/Commercial and
    Independent. BitLocker for fixed drives is Ultimate and Enterprise
    only; Professional excluded.

  - ASRock AM4 UEFI conventions, from the vendor's published manuals for
    the AM4 board family. Vendor/Commercial. Used for the menu paths;
    not verified against P7.40 on the machine, per the limitation above.

### Entry 055 — Public landing site built: docs/ serves GitHub Pages and the domain

- **Date logged:** 2026-08-05

- **Priority / Question:** Not tied to a research priority — project
  infrastructure. Delivers the third intended use of the domain recorded
  in Entry 034 (a linkable proof of work), and gives the Entry 044
  product direction its outward face.

- **Source:** Creator request, 2026-08-05. Security claims verified
  against GitHub's Pages documentation, a GitHub community statement on
  response headers, and MDN's CSP reference — the links sit next to the
  claims they support in `docs/README.md`.

- **What happened:** A single-page static site in `docs/` — no
  framework, no build step, no JavaScript, nothing loaded from a third
  party — ready for GitHub Pages to serve from `/docs` on `main`, and
  portable unchanged to `groundedaipractice.co.uk` or any host. Content
  drawn from the current direction: the courses-versus-people evidence
  (`research_log.md` Entries 044/053/061/062), the four research rules,
  the practice-system framing and SME direction (Entry 044, this log),
  and current work. Four figures are scripted in
  `tools/build_site_figures.py` per the data-driven figures rule — data
  transcribed with entry citations beside the constants, light and dark
  variants, source-and-date line on every image, and a WCAG 2.1 AA
  contrast audit that refuses to build on a failing pair. Security
  posture: attack surface reduced to nearly nothing (no scripts, no
  cookies, no third-party loads), CSP via `<meta>` with
  `default-src 'none'`, and the limits stated rather than papered over
  — GitHub Pages cannot set response headers, so `frame-ancestors` and
  HSTS are unavailable there; the header set to apply on any
  header-capable host is recorded in `docs/README.md`, as is the safe
  custom-domain order (verify the TXT record before touching DNS, per
  GitHub's domain-takeover guidance). Rendering verified against the
  real engine: text-geometry probes over every figure (no overflow, no
  collisions), both themes, mobile width, all assets loading, console
  clean. Same-day addition: Public Sans ships self-hosted —
  `tools/build_site_fonts.py` subsets the installed faces to five WOFF2
  files (~200 KB total, OFL licence text alongside), with `local()`
  sources preferred so an installed copy downloads nothing; font
  loading re-verified in the preview afterwards.

- **Inference drawn:** None — build record. One verification note: the
  OECD adoption figures (40% / 20.4% / 11.9% by firm size, 2024) were
  re-corroborated by search on 2026-08-05 before being charted; the PDF
  itself remains unread and `[OECD-SMEAI25]` keeps its UNVERIFIED-
  beyond-synthesis status in the research log's source key.

- **Limitations / conflicting evidence:** The site's prose is Claude's
  rough draft and falls under the outward-facing prose rule — the
  creator writes the final copy before Pages is enabled. Figure text renders in the
  viewer's installed fonts — browsers fetch no external fonts for
  `<img>`-embedded SVGs — so the brand face is guaranteed on the pages,
  not inside the figures. Geometry was verified by
  in-browser measurement, not yet by a human eye on a composited
  screen.

- **Effect on project direction:** The repo gains `docs/` and
  `tools/build_site_figures.py`, both indexed in `CLAUDE.md` in the
  same change. Enabling Pages, pointing the domain, updating the
  canonical URLs to it, and posting the link anywhere each remain
  per-item creator decisions. Also recorded openly: this session found
  two entries in this file numbered 052 and renumbered the second
  (“Drives fitted”, dated 2026-08-05, uncommitted) to 054 — a
  numbering-collision fix in the Entry 017 category; CLAUDE.md,
  project_brief.md and internal/README.md were checked first and
  nothing referenced the old number.

### Entry 056 — Outward-prose rule refined: shared drafting, creator review as the gate

- **Date logged:** 2026-08-05

- **Priority / Question:** Process — refines the Entry 043 prose rule,
  during the landing-site prose pass.

- **Source:** Creator decision, 2026-08-05.

- **What happened:** The creator relaxed the requirement that final
  outward prose be written by them alone. Claude may now draft
  candidate final prose in the creator's register and plain language;
  every passage still passes the creator's review before publication,
  and the creator rewrites at will. Recorded in `CLAUDE.md` alongside
  the original rule, worded around what the rule protects (ownership,
  review, and open disclosure of the AI-assisted method) so the public
  rule cannot be misread as the work being AI-generated without
  oversight. First applied to the landing-site hero, Block 1 of the
  prose pass.

- **Inference drawn:** None — decision record.

- **Limitations / conflicting evidence:** None noted.

- **Effect on project direction:** The site prose pass proceeds as
  draft, review, apply per block, rather than creator rewrites of
  every block. The review gate, and item 5 of the bias self-check,
  are unchanged.

### Entry 057 — Landing site rebuilt on the asset system; prose sweep completed; unit hosting opened

- **Date logged:** 2026-08-05

- **Priority / Question:** Project infrastructure — continues Entries
  055 and 056. Creator direction: review the whole site, finish the
  prose in the established register, use the existing icons, replicas
  and callout patterns, and fix the custom diagrams that read poorly.

- **Source:** Creator direction and review, 2026-08-05.

- **What happened:**

  1. The two abstract SVG diagrams (claim-verification flow,
     practice-system) are retired. Both are now native HTML in the
     page, built from the brand icon set with white icon wells matching
     the Word callout construction. Real text scales, wraps and reads
     to screen readers; the data figures stay scripted per the
     data-driven rule, and only content that is genuinely a chart is
     drawn. The four method cards moved to a fixed two-by-two grid.

  2. First use of the replica system outside the build guide: the
     system section now shows `tools/replica.py` output of the site's
     own figure build, contrast audit included. The spec is
     `assets/replicas/site_figures_build.json`; its output lines are
     verbatim from a real run, after the figure script switched to
     printing repo-relative paths so the replica cannot drift from
     real behaviour.

  3. The Word callout pattern translated to CSS (icon well, Ember
     divider, warm ground) and applied to the "what this is not" note.

  4. Register sweep over everything not yet reviewed block by block:
     figure-internal strings, alt text, the share-card sub-line, the
     brand link's screen-reader label, and `docs/README.md` in full.
     Visible page text now carries zero em dashes; the em dash in the
     page title stays as a deliberate exception, a conventional
     separator in a browser tab rather than prose.

  5. Hosting the pilot unit on the site is opened as a working
     consideration: a `learn/` folder using the same stylesheet, whose
     callout, flow and card styles are already the unit's visual
     language. A static unit page collects nothing from a learner,
     keeping the trial's data-protection questions (Entry 034) with
     the trial rather than the site. Publishing remains per-item.

- **Inference drawn:** None — build record.

- **Limitations / conflicting evidence:** Blocks 1 to 6 were reviewed
  individually by the creator; this pass's changes are applied but
  await the same review on the rendered page before any commit.

- **Effect on project direction:** `CLAUDE.md` updated in the same
  change (figures tool entry, `docs/` entry, `assets/replicas/`
  entry). The site prose pass is complete pending the creator's read;
  the domain steps in `docs/README.md` are the next action after
  commit and push.

### Entry 058 — Autonomous refinement pass: projection chart, BridgeAI reframed, the how-gap made concrete

- **Date logged:** 2026-08-05

- **Priority / Question:** Project infrastructure — the landing site,
  continuing Entries 055-057. Executed autonomously at the creator's
  direction while they were away, against their written notes.

- **Source:** Creator notes, 2026-08-05: five prose corrections; the
  courses figure redesigned as a line graph with projections; BridgeAI
  explained before its numbers are used; the large-versus-small
  infrastructure difference made concrete.

- **What happened:**

  1. **The evidence figure is now a projection chart.** Course
     completions from June 2025 (the counting start [AISKILLSBOOST26]
     states) to the January 2026 figure, then a straight line at that
     pace to 2030, reaching about 9.4 million against the dashed
     targets: 7.5 million workers (June 2025) and 10 million (drawn
     from January 2026, where that framing appeared). The legend's
     third entry is a line that cannot be drawn: workers trained, no
     data published. This respects the Entry 042 decision against
     failure predictions: the chart does not say the target will be
     missed; it shows the count is on course only in a unit that is
     not people. The projection is computed in the script from the
     logged dates and count, with the assumption stated on the image.

  2. **BridgeAI corrected and explained.** The previous strip said
     "over the same period", which was wrong: BridgeAI's figures run
     from its 2023 launch to end 2025, the partnership's from June
     2025. The page now explains what BridgeAI is before using its
     numbers, and a separate at-a-glance strip carries them (including
     820+ projects funded, so the programme is not misread as
     training-only). Entry 053's cherry-pick warning is respected:
     1,700 is never set against the 10-million target.

  3. **The how-gap paragraph and comparison diagram.** The system
     section now states the practical difference in how large and
     small organisations deploy AI, anchored to the OECD paper's
     depth-of-use finding (among SMEs using generative AI, only 29%
     use it in core activities — added to Entry 065 in the research
     log the same day). An icon-based two-column comparison makes it
     visual. The direction paragraph now closes on the point the
     creator asked for: the same pattern large firms deploy, scaled
     down.

  4. **Creator's five prose corrections applied** (hero lead, bracket
     subclause, groundwork sentence, evidence intro, infrastructure
     paragraph), and the replica regenerated against the new build
     output — during which the self-check caught a shell-mangled
     backslash that had put a control character into the pictured
     command, exactly the drift the verbatim rule exists to stop.

- **Inference drawn:** None — build record.

- **Limitations / conflicting evidence:** The projection assumes the
  first seven months' pace continues; the image says so. All changes
  await the creator's review of the rendered page.

- **Effect on project direction:** `CLAUDE.md` figure-tool entry and
  `docs/README.md` updated. The chart, strip and comparison are the
  templates for future figure work: charts scripted, diagrams native.
### Entry 059 — Site figures settled as stat strips; interest-concentration facts added to the page

- **Date logged:** 2026-08-05

- **Priority / Question:** Project infrastructure, closing the landing
  site's figure and prose work. Continues Entries 055-058.

- **Source:** Creator review and rulings, 2026-08-05. Claims cited to
  `research_log.md` Entries 046, 048, 052 and 066.

- **What happened:**

  1. **Three figure concepts were tried and the simplest won.** A
     projection line chart, then a two-lane timeline, were both
     rejected by the creator as convoluted and conceptually flawed:
     plotting courses against worker targets on any shared axis
     performs the conflation the page criticises, and no amount of
     legend text undoes that. The settled figure is a stat strip in
     the same grammar as the BridgeAI one: two labelled groups in
     different units and different colours either side of a divider,
     with the missing number below in a dashed outline, kept
     deliberately quieter than the two figures so it reads as the gap
     between them rather than a third statistic. The reasoning is
     written into the script's docstring, because a later reader may
     otherwise assume a strip should "obviously" be a chart.

  2. **The terminal replica was removed from the page** at the
     creator's direction: a contrast-audit window in the system
     section asked the reader to do technical work in the middle of an
     argument about small firms, weakening the large-versus-small
     comparison that follows it. The spec, image and sync tool stay in
     the repository for a learning-unit page, and the CSS stays with a
     comment; `tools/build_site_replica.py` no longer copies into
     `docs/`.

  3. **Three interest-concentration facts added**, each stated flatly
     with no characterisation, under a new heading in the evidence
     section: PwC's three roles around the AI Skills Hub (Entry 046);
     the £400bn figure's footnote citing Google-commissioned research
     by Public First, and the same consultancy's £550bn figure for
     Microsoft, both companies being among the eleven partners
     (Entries 048/052); and the promise outlasting the Prime Minister
     who made it (Entry 066). The block closes by conceding what the
     facts do not show — that the figures are wrong — and stating only
     what they do.

  4. **A drafting error caught by checking rather than by review.**
     The vendor-attribution sentence was first drafted from memory
     with the £400bn credited to Microsoft. Entry 052 exists precisely
     to correct that attribution, and reading it before writing
     produced the accurate version. Recorded because the failure mode
     is the one the project's own method exists to catch, and it
     nearly reached a public page.

  5. A fourth candidate, the vendor's claims from the London Tech Week
     stage, was proposed and rejected: Entry 063 limits that material
     to context rather than evidence, and using it would spend
     credibility the other three facts earn. The investment-emphasis
     angle stays off the page until the relevant timestamps are heard
     under the spoken-source protocol.

- **Inference drawn:** None — build and decision record.

- **Limitations / conflicting evidence:** Public First's Google report
  is still unread (Entry 052's limitation), so the page states its
  commissioning and citation, never its method. The creator's final
  visual review of the settled figure is outstanding.

- **Effect on project direction:** The figure grammar is now settled
  for the site: charts only where the content is genuinely a chart,
  stat strips where two numbers must not be compared, native HTML for
  diagrams. `CLAUDE.md` and `docs/README.md` updated in the same
  change.
### Entry 060 — Rule extraction pass; commit-message format fixed and history normalised

- **Date logged:** 2026-08-06

- **Priority / Question:** Working rules and repository record. Runs the
  standing extraction pass and settles a defect in how commits are
  written.

- **Source:** Creator direction and rulings, 2026-08-06.

- **What happened:**

  1. **Extraction pass.** The five pre-move memory files are all
     already captured in the repo and none needed migrating; they stay
     orphaned under the old project path and load in no session. The
     one file under the current path concerns wording public guidance
     and stays machine-local by its own logic. Four rules were promoted
     out of this session instead: feedback on a draft produces a
     revised draft rather than an edit; a claim going into a
     deliverable is re-read from its log entry rather than recalled;
     generated visual assets get a geometry self-check; both logs are
     CRLF on append.

  2. **Three orphaned commit references found and fixed.** The
     2026-08-03 history rewrite silently invalidated every commit SHA
     cited in this file, including the one inside Entry 048's own
     account of that rewrite. All three now reference commits by title
     and date, which survive a rewrite. Corrected in place as broken
     cross-references, per the amendment policy.

  3. **A commit-message format was adopted** after an audit of all 37
     messages found five subject-line styles (imperative, past tense,
     third-person present, bare noun phrase, and GitHub's default
     "Update README.md"), inconsistent trailing full stops, bodies both
     hard-wrapped and not, and one message repeating its own subject as
     its first body line. The format is in `CLAUDE.md` under Git
     conventions. The substantive change is that bodies are no longer
     hard-wrapped at 72 columns: that convention serves terminal
     `git log`, while these commits are read on GitHub, where every
     hard break becomes a mid-sentence tear.

  4. **History was normalised to the format.** Permitted under the
     amendment policy's own test, which asks whether an edit changes
     what the record claimed at its date: reformatting tense, wrapping
     and structure corrects expression, not record. Two constraints
     held throughout. **No claim was altered**, including claims later
     found wrong — the commit stating the £400bn figure was
     Microsoft-commissioned keeps that wording, because
     `research_log.md` Entry 052 correcting it to Google is part of the
     record the repository exists to show. **No body was invented** for
     a commit that never had one; bare messages had their subject line
     normalised and nothing more.

- **Inference drawn:** None — decision and maintenance record.

- **Limitations / conflicting evidence:** A rewrite changes every
  commit SHA, so any clone must be re-cloned rather than pulled, and
  any SHA recorded outside this repository is now stale. This is the
  second rewrite; the first is what orphaned the references fixed in
  item 2, which is the reason commits are now cited by title and date.

- **Effect on project direction:** `CLAUDE.md` gains the four rules and
  the commit format, and its extraction-pass line moves to today. Future
  commits follow the format; future references to commits use titles,
  not hashes.

### Entry 061 — External peer review: the site redrafted in first person around the origin story

- **Date logged:** 2026-08-07

- **Priority / Question:** The landing site and the project's outward
  register. Second external review of the project's written work, and
  the first of the site.

- **Source:** Trusted-peer feedback relayed by the creator, 2026-08-07
  (peer unnamed by design); creator rulings the same day.

- **What happened:**

  1. The peer judged the site professional, well reasoned and
     genuinely valuable primary research; found the personal origin
     story missing and said it should be central, given that the
     project's present value is substantially as a portfolio piece, a
     framing the creator endorsed; and flagged prose reading as
     AI-generated, naming two passages in the system section.

  2. The diagnosis the creator set out and Claude accepted: the
     register rules were being applied at constant density. Exact
     mimicry of the creator's own tics, applied uniformly, reads as
     more AI-generated rather than less. Entry 042's external review
     had caught the opposite failure, abstract and over-qualified, and
     the rules written in response overcorrected into this one.

  3. A second defect in the flagged passages, found on inspection:
     both were conclusions about concepts the page had never
     introduced. For a project whose output is teaching, prose that
     performs conclusions instead of explaining them contradicts its
     own purpose.

  4. Creator rulings: redraft the whole site's prose; first person
     throughout; the origin story leads the home page and gets its own
     about page; the mechanic-to-researcher arc is published,
     exercising the option Entry 049's limitations deliberately left
     open on 2026-07-29; structure and tooling unchanged.

  5. A framing rule was set for the trade narrative and recorded with
     the primary account internally: nothing published may imply the
     previous employer lacked diagnostic rigour. The supported framing,
     that diagnosis is gated by manufacturer tools, software and access
     agreements, was then evidenced at `research_log.md` Entry 067,
     which also confirmed the motive version stays unpublished.

- **Inference drawn:** A style rule has now failed in both directions,
  hedged in Entry 042 and uniform here. The durable lesson is that any
  register applied at constant density reads synthetic, including the
  author's own; the `CLAUDE.md` refinement written from this pass
  carries it.

- **Limitations / conflicting evidence:** One reviewer, and register
  judgement is partly taste. The control is that the creator reviewed
  every redrafted block, correcting the workshop passage twice before
  approving it.

- **Effect on project direction:** The site speaks as its author on
  every page. Candidate teaching material flagged for the prompting
  unit: two external reviews producing opposite failures of the same
  rule is a better lesson about instructions than either alone.

### Entry 062 — The site becomes multi-page: assembler tool, page split, about page

- **Date logged:** 2026-08-07

- **Priority / Question:** Landing-site infrastructure, following the
  creator's decision that the site is the project's primary output
  rather than a landing page, and will later host the gated pilot on
  its own subdomain.

- **Source:** Creator decisions, 2026-08-07.

- **What happened:**

  1. `tools/build_site_pages.py` assembles `docs/` from `site/`
     sources: one shared shell, one fragment per page, plain HTML out,
     and nothing written unless every page passes every check. Jekyll
     was considered and declined on the project's own grounds. GitHub
     Pages runs it free, but it can only be verified after publishing,
     and this project verifies before. The rebuilt single page was
     proved identical to the reviewed original before any splitting,
     which is what made the split safe.

  2. Split into home, evidence, method, system and about, each with
     its own `h1`, restoring the heading order the one-page structure
     had left broken. About joined the nav; a hidden portfolio page
     would defeat its purpose.

  3. The about page was drafted from the internal primary account and
     Entries 049 and 025, through creator review. Constraints held: no
     dates, since the experience is not precisely dated; the unpinned
     "1 million delivered" figure omitted; the employer and the IT
     consultant unnamed. The page states plainly that it describes the
     platform as found then, that testimony is not data, and that the
     checkable claims live elsewhere and do not rest on it.

  4. Hosting was settled: one site, plain portable static files, on
     Pages for now, with the gated pilot to sit on its own subdomain
     when it exists. Portability comes from how the site is built
     rather than where it is hosted, so nothing is trapped.

  5. The approved state was committed as a checkpoint before an
     autonomous overnight pass, so that everything produced unattended
     stayed individually reviewable and reversible.

- **Inference drawn:** None — build and decision record.

- **Limitations / conflicting evidence:** GitHub Pages serves
  `404.html` for nested missing paths, where that page's relative
  asset links resolve wrongly. The fix belongs with the custom-domain
  work and is parked until then.

- **Effect on project direction:** `docs/README.md` and `CLAUDE.md`
  updated to match. The description of the site as one page is retired
  everywhere it appeared.

### Entry 063 — Autonomous overnight pass: remaining pages redrafted, theme toggle, preview-cache fix

- **Date logged:** 2026-08-07

- **Priority / Question:** Completing the site, executed autonomously
  while the creator rested, under rails agreed first: nothing committed
  beyond the approved checkpoint, nothing pushed or published, no edits
  to the logs or `CLAUDE.md`, and research staged rather than appended.

- **Source:** Creator direction, 2026-08-07.

- **What happened:**

  1. System, evidence and method redrafted in first person, including
     both peer-flagged passages. The OECD claims were re-read from
     Entry 065 at drafting time, per the re-read rule, and the 29%
     sentence now tracks that entry's generative-AI scope exactly. The
     evidence page was deliberately the lightest touch, since its
     factual sentences had already been reviewed.

  2. The theme toggle the creator asked for at the start of the day:
     one external script, `script-src 'self'` added to the policy,
     dark values duplicated behind a `data-theme` override, and the
     `<picture>` dark sources switched by script because they follow
     the system query rather than the override. That is the same
     mismatch found earlier in the day, when a browser's pinned theme
     made half the site unreachable. The button is hidden entirely
     without JavaScript. The footer privacy line and `docs/README.md`
     were rewritten in the same pass, so that no published claim
     outlived the change it described.

  3. Two defects found beyond the agreed scope and fixed. The 404 page
     still told visitors the site was a single page. And the preview
     server allowed browser caching, so a rebuilt page rendered
     against a stale stylesheet and the new toggle appeared broken
     when it was not; `tools/serve_site.py` now serves `docs/` with
     caching disabled, and `.claude/launch.json` runs it.

  4. Verification: every page at three widths in both themes, no
     horizontal overflow, correct breakpoint behaviour, and the toggle
     checked end to end including persistence across reload.
     Screenshots were unavailable, since the browser pane does not
     composite unattended, so the evidence is measurement, the same
     method as the figure geometry checks.

- **Inference drawn:** None — production record.

- **Limitations / conflicting evidence:** The pass produced one
  deliberate rule exception: `tools/serve_site.py` was written without
  its `CLAUDE.md` index entry, because `CLAUDE.md` was off-limits
  overnight. The entry landed with this one, closing the gap in the
  same commit rather than the same edit.

- **Effect on project direction:** The site is redrafted in one voice
  across every page, and the rendered review that gates enabling Pages
  is the only step left before publication decisions resume.

### Entry 064 — The landing site goes live on groundedaipractice.co.uk

- **Date logged:** 2026-08-08

- **Priority / Question:** Publication decisions, resumed after the
  rendered review gate that closed Entry 063.

- **Source:** Creator decision and session work, 2026-08-08.

- **What happened:** The domain was attached and the site published.
  Pages was already serving from `/docs`, so the work was DNS and the
  repo-side switch.

  At the registrar: four `A` records on the apex to GitHub's Pages
  addresses, the `www` `CNAME` retargeted from the apex to
  `ohps-stack.github.io`, and GitHub's verification `TXT` added. The
  domain also carries a Microsoft 365 mailbox, so eleven email records
  were identified and left alone, and `MX` was re-checked after every
  change.

  Repo side: `docs/CNAME` added and `base_url` in `site/pages.json`
  switched from the github.io project URL to the domain. Nav and asset
  links were already relative, so nothing else needed touching — the
  `{{root}}` design in `tools/build_site_pages.py` paid for itself
  here. A latent defect surfaced in the same pass: the line-ending rule
  in `.gitattributes` matched only `docs/*.html`, so the four pages in
  subdirectories were checked out CRLF, rewritten LF by the builder,
  and reported as modified when their content was identical.

  Verified over the live domain rather than assumed: apex 200 with a
  valid certificate, `http` and `www` both 301 to it, all four subpages
  200, the custom 404 returning a real 404 status, stylesheet and
  subset web fonts loading, no broken images, and the `og` card
  reachable. Enforce HTTPS ticked.

  One documented step was found to be in the wrong order.
  `docs/README.md` said to verify the domain with GitHub before
  pointing DNS. That is correct from a clean start, but once the `A`
  records are live and the domain is not yet attached to a repository,
  the site sits in precisely the window where another repository can
  claim it — so attaching is the way out of that window, not something
  to hold back pending verification. The README now says so.

- **Inference drawn:** None — production record.

- **Limitations / conflicting evidence:** A defect was found in the
  zone that belongs to the mailbox rather than the site: the `SPF`
  record authorises GoDaddy's mail servers while `MX` delivers to
  Microsoft 365, so mail sent from Microsoft 365 fails `SPF` against a
  hard fail. `DKIM` is configured for Microsoft and should carry
  `DMARC`, so delivery is probably unaffected — but the margin is one
  broken signature wide. Left unchanged and recorded as a separate
  task. A live mailbox is not something to edit in passing.

- **Effect on project direction:** The site is public at its own
  domain. Posting the link anywhere remains a per-item decision.

### Entry 065 — Ubuntu installed on the server; hardware record corrected in four places

- **Date logged:** 2026-08-08

- **Priority / Question:** Priority 6 — the server build reaching a
  working base for the first time.

- **Source:** Session work at the machine, 2026-08-08.

- **What happened:** Ubuntu 26.04 LTS was installed to the NVMe in UEFI
  mode. The machine now boots to its own desktop with no boot menu, and
  drives the projector through the receiver with wireless input from
  across the room.

  The session opened on a false premise. The build was believed to have
  Ubuntu installed and merely a boot-order problem, since it needed
  `F11` at every power-on. The boot menu showed no `ubuntu` firmware
  entry at all, and booting the NVMe reached an abandoned Windows 10/11
  setup. Ubuntu had never been installed — every prior session had been
  running the live USB, which leaves nothing behind, and that is why
  the setup never appeared to finish.

  Four corrections to the hardware record follow, each observed rather
  than inferred:

  1. **The system drive is a Crucial P1 500 GB NVMe (`CT500P1SSD8`),
     not the WD Blue 500 GB M.2 SATA** recorded throughout the build
     documents. It uses PCIe lanes, so the standing open question about
     which SATA port the M.2 module disables is void, and all four SATA
     ports are available.

  2. **Windows sits on the 500 GB Seagate, not the 2 TB** — the
     firmware entry reads `Windows Boot Manager (ST500DM002-1BD142)`.
     Both drives carry GPT layouts with Microsoft reserved partitions,
     so neither is the legacy MBR Windows 7 install the recovery plan
     assumed.

  3. **There are four spare drives, not three.** The two unknown
     capacities are now known: 320 GB `ST3320418AS` (2010) and 160 GB
     Hitachi `HDS721016CLA382` (2010), alongside the 2 TB
     `ST2000DM001` (2012) and 500 GB `ST500DM002` (2014).

  4. **Noise is a consideration, not the dominant constraint**, at the
     creator's direction. This softens what the build document recorded
     and changes fan-curve and siting advice.

  Two decisions were taken during the install. **No disk encryption:**
  it defends only against physical theft, does nothing while an
  always-on machine is running, and its passphrase prompt would cancel
  the settled "Restore on AC/Power Loss → Power On" requirement, since
  nothing can unlock the disk remotely before networking exists. The
  hardware-backed alternative needs Secure Boot, which this build
  disables so the Nvidia kernel modules load without signing problems.
  **Plain ext4, no LVM:** data lives on separate drives, and one less
  abstraction between the creator and a recoverable system is worth
  more than a feature that might be wanted in a year.

- **Inference drawn:** The transferable finding is about handover
  documents. A brief supplied mid-session carried a four-day-old state
  that contradicted the repo in six places, and its hardware inventory
  was wrong in ways the repo had never caught either. Both were
  corrected only because the machine itself was read — the boot menu
  and the drive labels — rather than the documents describing it. The
  same instinct as the re-read rule in `CLAUDE.md`, applied to hardware
  instead of citations.

- **Limitations / conflicting evidence:** SMART health of every drive
  remains untested, and the 2 TB is a fourteen-year-old Barracuda
  7200.14, the generation whose 3 TB member is the best-documented
  consumer drive failure case there is. Nothing should be trusted with
  data until the long tests pass. The install was also completed with
  both hard drives connected, against the advice to unplug them; the
  confirmation screen was read instead and showed every `sd` partition
  unchanged. A forced power-off during the session risked the package
  database, which was checked afterwards with `dpkg --audit` and found
  clean.

- **Effect on project direction:** The server has a working base for
  the first time. SMART long tests, the recovery pass on both Windows
  drives, storage mounts, Stremio, Tailscale and the firewall all
  remain.

### Entry 066 — A chart layer, a categorical palette, and a figure refused for incomplete research

- **Date logged:** 2026-08-11

- **Priority / Question:** Priority 7 — how research findings reach a
  public audience, and Priority 10 — the repository demonstrating
  credible practice.

- **Source:** Session work, 2026-08-11.

- **What was decided:** The project's data figures gain a second
  production route. `build_site_figures.py` composes SVG by hand and
  cannot draw a chart, having no scales, axes or marks; `gap_chart.py`
  adds a Vega-Lite layer for figures that need them, with the division
  that Vega-Lite draws the plot and the module draws the editorial
  furniture around it. Rendering is through `vl-convert`, which embeds
  its own JavaScript runtime, so nothing reaches a browser, a Node
  install or the network.

  A categorical palette was settled first, since every figure depends on
  it. `palette_check.py` audits contrast, colour-vision deficiency and
  greyscale against a pass mark calibrated from the Okabe-Ito
  colour-universal set rather than invented. Three tiers:
  highlight-against-context, five nominal categories per ground, and
  ordered Ember ramps. The constraint that decided the shape is that a
  mark clearing 3:1 on both Paper and Ink sits in a luminance band only
  0.132 wide.

  Two figure titles were rewritten under a rule adopted this session:
  a title states the finding, and one that describes the chart is a
  label. The OECD firm-size figure moved from a highlight to an ordered
  ramp, firm size being an ordinal variable and the gradient being the
  finding.

- **How it was checked:** Every claim above is a number the tools print.
  The palette audit reports its ratios and distances on each run; the
  contrast audit refuses to build on a failure. Beyond that, each of the
  chart layer's self-checks was written after the defect it catches got
  through: a render that failed and wrote the file anyway, six data
  labels placed on top of their own points, a dollar sign on a UK price
  axis, and two colours in the dark palette that were one colour to the
  eye. The last was found only by rendering a proof sheet and looking at
  it, having passed an audit that had not been pointed at that set.

- **What went wrong:** The first chart built on the new layer was drawn
  from `drafts/budget_vram_for_local_ai.md`, whose first line records it
  as a rough draft and which separately notes one comparator "not priced
  this pass" and one supporting source unread. The figure was
  conceptually and structurally sound and made no comparison at 12 GB or
  32 GB, where only Intel cards had been priced — the single comparison
  it existed to make. The four generated files were deleted.

  The mechanical half is now blocked by `check_coverage()`, which counts
  categories at each level of the x variable and refuses a build where a
  level carries only one. The general half is judgement and became a
  standing rule: a chart is a published claim and takes the
  finished-research bar rather than its source document's, because a
  figure travels further than the document it came from.

- **Effect on project direction:** Figures with real axes are now
  possible, which was previously a hard limit on what the research could
  show. The VRAM figure stays unbuilt until a non-Intel comparator is
  priced at 12 GB and at 32 GB. Nothing in `project_brief.md` has been
  amended; the palette recorded there as final now has a charting
  extension awaiting a decision on whether to fold it in.

### Entry 067 — The VRAM research completed and the figure built; site outputs re-verified

- **Date logged:** 2026-08-11

- **Priority / Question:** Priority 6 (research completion) and
  Priority 7 (outputs), executed autonomously at the creator's
  direction to finalise the open research and regenerate
  public-facing outputs.

- **Source:** Session work, 2026-08-11.

- **What happened:**

  1. The research that blocked the VRAM figure was closed as
     `research_log.md` Entries 070–072: non-Intel comparators priced
     at every capacity tier, the surfaced-but-unread benchmark
     sources read directly (two source rows upgraded from leads, two
     added), and vendor prompting guidance read for the pilot unit.
     The draft document was updated throughout from the new entries,
     and now embeds the figure.

  2. `tools/build_vram_figures.py` builds clean: coverage passes on
     real data at 12/16/24/32 GB, and the title changed with the
     finding — the CUDA options do not run out above 24 GB, they
     triple in price. The 48 GB tier stays off the chart (its CUDA
     comparator was priced only in the US used market) and lives in
     the draft's table instead.

  3. A defect the tool checks cannot catch was found by looking at
     the render, per the geometry rule: labels were given their own
     y-field so clustered columns could spread, and that second field
     on the y channel silently deleted the visible price axis — on a
     price chart — while the render, coverage and label checks all
     passed. Fixed by feeding labels a separate dataset that reuses
     the same field name; the lesson is recorded in the tool's
     comments and its `CLAUDE.md` index entry.

  4. Site outputs re-verified: figures rebuilt with the palette audit
     passing, `build_site_pages.py --check` reporting no drift, and
     the terminal replica resynced after this session's figure-script
     changes.

- **Inference drawn:** None — production record.

- **Limitations / conflicting evidence:** Everything is uncommitted
  working-tree state for the creator's review; nothing was committed
  or pushed. The R9700 price in the figure is a search-snippet
  figure, marked as such on the image's own source line.

- **Effect on project direction:** The budget-VRAM thread's desk
  research is done and its figure is publishable-quality pending the
  creator's review; what remains on the thread is empirical
  (Open Threads, Priority 6).

### Entry 068 — Pilot unit first draft: effective prompting

- **Date logged:** 2026-08-11

- **Priority / Question:** Immediate priority Q5 / Priorities 3–4 —
  drafting the pilot unit that Entry 013's capability decision
  unblocked, at the creator's direction in the same autonomous
  session.

- **Source:** Session work, 2026-08-11. Design basis re-read at
  drafting time per the re-read rule: `research_log.md` Entries
  039–040 (candidate evidence and sequencing check), 026–027 (PRIMES
  criteria, GRR model), `project_log.md` Entry 013 (decision and
  rationale); techniques verified against `[ANTHROPIC-PROMPTDOCS26]`
  (`research_log.md` Entry 072).

- **What was decided (production decisions, all open to review):**

  1. The Entry 013 rationale is executed structurally: the unit opens
     with a "what happens when you hit send" mechanism section — the
     compressed Candidate C scaffolding Entry 040's sequencing
     evidence called for — built around one idea (the model fills
     every gap you leave with the most ordinary assumption) and one
     Mermaid diagram of the gap between what the learner knows and
     what they typed.

  2. The technique content is five named moves: task and reader,
     background, shape, example, exclusions. The Entry 039 risk that
     a prompting unit reads as generic tool-training is countered by
     centring diagnosis: a symptom→fix table mapping what an answer
     looks like to which move was missing, so the unit teaches
     reading output, not reciting recipes.

  3. GRR mapping: worked example (a price-increase email, invented
     but SME-shaped) → three guided exercises, the first two
     deliberately tool-free since the skill practised is diagnosis →
     independent practice on the learner's own real task via a
     five-line template → a one-week spaced return, scaling GRR's
     spaced-practice recommendation and PRIMES' revisit instinct to
     unit size.

  4. PRIMES alignment: 45–60 minutes, one sitting or two; builds on
     informal use rather than assuming none; an explicit
     when-prompting-is-not-the-fix section covering the
     when-not-to-use requirement; tool-neutral throughout for the
     Expandable criterion. The invented-specifics warning keeps the
     project's verification framing present and names checking AI
     output as the planned second unit, so Candidates A and D are
     deferred visibly rather than dropped.

  5. Illustrative outputs are framed as illustrative — the unit
     describes the shape of what comes back and has the learner
     generate the real comparison in Exercise 3, rather than
     presenting fabricated tool output as a real transcript.

- **Limitations / conflicting evidence:** Untested with learners —
  the unit says so in its own closing section, and Priority 9
  (evaluation) now becomes load-bearing, as Open Threads already
  notes. Prose is draft register for the creator to rewrite. The
  worked example is invented rather than drawn from real logged
  usage; real learner material would strengthen a revision.

- **Effect on project direction:** The project's first output exists
  as a reviewable draft at `drafts/effective_prompting.md`, indexed
  in `CLAUDE.md` the same day. Next steps in order: creator review
  and prose pass, then the learner trial, then promotion through the
  docx pipeline if distribution needs it.

### Entry 069 — Both drafts promoted through the Word pipeline; a path quirk fixed in the preview tool

- **Date logged:** 2026-08-11

- **Priority / Question:** Priority 7 (delivery format) — the creator's
  direction to produce polished Word/PDF versions of the budget-VRAM
  research document and the pilot unit; the markdown-first rule's
  promotion step, run for its second and third documents.

- **Source:** Session work, 2026-08-11.

- **What happened:**

  1. The remaining research was closed first, so neither document
     ships an unread-source caveat: `research_log.md` Entry 073 read
     the vLLM project's Arc post (Intel-authored, it turns out), the
     bentech operational follow-up (named frictions, and measured
     B60/B70 load power), and the Phoronix B50 review
     (sensor-measured 59 W average). The budget document's software,
     power and sources sections were updated from it.

  2. The unit's Mermaid sketch became a drawn figure
     (`tools/build_prompting_figures.py`, importing the server-guide
     script's helpers rather than copying them), because the
     diagram's point is proportion — the tall column of what you know
     against the small box of what you typed — and auto-layout gives
     every node equal weight. Three geometry defects were caught by
     looking at renders across two rebuild rounds: an arrow striking
     through its own label, quote text sitting on a box border, and
     body text flush against box edges.

  3. Both documents then went through the full pipeline:
     `md_to_docx.py` with a strapline marking each as a draft;
     `fitshapes.py` (four callout cards fitted in each);
     `word_preview.ps1`; a page-by-page read of both PDFs (8 and 6
     pages — no blocking defects, tables banded with repeated
     headers, quotes and code blocks mapping as intended); and
     `word_roundtrip_test.ps1` against throwaway copies — SAVE OK for
     both. Outputs: `drafts/Budget_VRAM_for_Local_AI.docx` and
     `drafts/Effective_Prompting.docx`, each with its self-check
     `.pdf` beside it.

  4. One tool defect found and fixed in passing: `word_preview.ps1`
     resolved its input path but handed a relative `-OutPath`
     straight to Word COM, which resolves against its own working
     directory and fails with "directory name isn't valid". The
     parameter is now made absolute before use.

  5. On review, two register defects flagged at handover were fixed at
     the creator's direction — the tiers table's 12 GB cell claimed a
     "measured example" that was a description, and now carries the
     same em-dash the 16 GB row does; the WARNING card's aside was
     reworded — and both documents were rebuilt through the same
     pipeline, the unit's rebuild also carrying the creator's own
     prose edits to the markdown.

- **Inference drawn:** None — production record.

- **Limitations / conflicting evidence:** Both documents remain drafts
  in register, and each strapline says so; the unit remains untested
  with learners. The docx files are generated outputs — the markdown
  stays the source of truth, and publication of either document
  remains a per-item creator decision.

- **Effect on project direction:** Both deliverables exist in
  distributable form pending the creator's prose pass. `CLAUDE.md`
  indexed the new figure tool and the generated documents in the same
  session.

### Entry 070 — Profile surfaces overhauled: LinkedIn copy pack, GitHub identity, README refresh

- **Date logged:** 2026-08-12

- **Priority / Question:** The publishing funnel's profile step (the
  infographics lane's LinkedIn post → profile → repository chain) — the
  creator's request to bring the outward profiles, LinkedIn foremost
  and GitHub beside it, up to the project's current state.

- **Source:** Session work, 2026-08-12.

- **What happened:**

  1. A full LinkedIn candidate copy pack was drafted into
     `internal/linkedin_assets/` — headline options, About, experience
     and education entries, skills, featured items and a settings
     checklist. Per "Tracked logs record the project, not the person",
     the content stays internal. The creator set the direction
     in-session: employers first with the project as flagship proof of
     capability; the approved real headshot on LinkedIn and the brand
     mark on GitHub (the symbol-based avatar, since a 2.7:1 wordmark
     cannot survive the platform's smallest renders). Drafted without
     sight of the live profile — the browser extension was not
     connected — so reconciliation against what is actually published
     is the pack's first open item.

  2. The GitHub account was found essentially unconfigured: no display
     name, bio, website field or profile README. The July
     profile-README draft was rewritten around the live site as the
     lead link, with the wordmark and three current work items; an
     identity checklist was prepared alongside. A username rename is
     under consideration, with implications mapped from GitHub's own
     documentation and `docs/README.md`'s DNS record rather than
     memory: the `www` CNAME and the Pages verification TXT both embed
     the username, local remotes need re-pointing, repository URLs
     redirect until the old name is reclaimed, and old profile-page
     links 404 permanently.

  3. `README.md` was refreshed to current state: the live site linked
     in the header, Current focus updated (the public report, the
     now-drafted pilot unit, the budget-VRAM thread), `docs/` and
     `tools/` added to the contents table, and Tooling expanded to
     state the self-verification approach.

  4. The banner was rebuilt through a new tool,
     `tools/build_linkedin_banner.py`, which rasterises the SVG source
     via `gap_chart.to_png`, overlays the reversed wordmark and domain
     in Public Sans, and enforces the mobile-crop safe window, the
     desktop avatar clearance and the wordmark's minimum usable width
     in code, refusing to write otherwise. The first run failed its own
     domain-line check — the imported font helper bakes in its home
     script's canvas scale, so the text drew at roughly double size —
     fixed by loading the face at exact pixel size. Renders were then
     verified by reading them, per the geometry rule. `CLAUDE.md`
     indexed the tool in the same edit session, and a stale note in
     `project_brief.md` (avatar PNGs "pending regeneration" that have
     existed since July) was corrected in passing.

- **Inference drawn:** None — production record.

- **Limitations / conflicting evidence:** The copy pack is a rough
  draft under the outward-facing prose rule — final wording is the
  creator's, several facts are bracketed for them to fill, and the pack
  was written blind to the live profile. Nothing in this entry
  publishes anything: applying profile changes, creating the profile
  repository, any rename, and any DNS edit are each per-item creator
  actions.

- **Effect on project direction:** None — distribution-surface
  maintenance ahead of the funnel's first use.

### Entry 071 — Profile copy finalised interactively and applied live; banner redesigned; social cards added

- **Date logged:** 2026-08-12

- **Priority / Question:** Continuation of Entry 070 — interactive finalisation of the profile copy with the creator, its application to the live profile, and the visual-cohesion pass.

- **Source:** Session work, 2026-08-12; live profile read back through the browser extension before and after application.

- **What happened:**

  1. Every copy block was finalised through creator review rounds rather than wholesale acceptance. The pattern worth recording: the creator repeatedly caught and corrected AI-register defects — compound jargon, repeated tics across blocks on one page, a causal overreach between paragraphs, and workflow transcription standing where skill statements belonged — and twice redirected emphasis on evidence-weight grounds, so that pinned skills lead with 3 yrs 9 mos of professional diagnosis ahead of weeks-old tool skills, and the skills-to-entry mapping was rebalanced the same way. One factual correction of note: a line on the live profile itself was flagged by the creator as overclaiming and replaced with the accurate mechanism. Flagged as candidate raw material for the prompting/verification curriculum (redactions needed: employer specifics).

  2. Applied live by the creator and verified by read-back: headline (creator's final variant), both experience entries verbatim, a third entry with its real dates, and the skills mapping. Still to apply: About, Featured, education and certification entries, images, and the settings pass.

  3. The banner was redesigned by concept selection — three directions rendered and shown, the creator choosing the Ink-dark symbol motif — and `tools/build_linkedin_banner.py` was rewritten around a code-generated base, retiring the radar-motif SVG. The same tool now composes 1280×640 social cards; two are built and tracked in `assets/social/` (repository social preview, general project card), indexed in `CLAUDE.md` in the same session. Placement remains code-enforced and every render got a human read.

- **Inference drawn:** None — production record. One observation kept: the creator's corrections ran consistently in the direction of the project's own published register rules, applied unprompted to surfaces those rules were never written for.

- **Limitations / conflicting evidence:** The profile is a personal surface; per the person/project rule the copy lives in `internal/` and this entry records process only. Uploading the banner, the repo social image and the remaining sections are per-item creator actions.

- **Effect on project direction:** None — the publishing funnel's profile step is materially ready for first use.

### Entry 072 — Visual pass, second round: abstract split banner, light repo card, resolution fix, avatar and icon routes

- **Date logged:** 2026-08-12

- **Priority / Question:** Continuation of Entries 070–071 — the creator's review of the applied profile against the live page.

- **Source:** Session work, 2026-08-12; the creator's screenshots of the live profile.

- **What happened:**

  1. The creator reviewed the applied profile live and raised four defects: the banner rendered soft, the banner and headshot read as stylistically disconnected, several company entries carry placeholder icons, and the two Featured link cards were near-identical. All four confirmed on inspection — the last one being the site's Open Graph card and the repository card sharing one design language too closely.

  2. Exports now leave `build_linkedin_banner.py` at composed resolution (3168×792 banner, 2560×1280 cards): both platforms recompress uploads, and a native-size export goes soft after their pass.

  3. The banner moved to an abstract design at the creator's direction — three concepts carrying the aesthetic without the wordmark or symbol were rendered, and the Sand-over-Ink split chosen. It is now the tool's default style, the symbol design retained as an option. This supersedes Entry 071's banner choice the same day it was made: seeing the design live changed the decision, which is the review loop working as intended.

  4. The repository social card was rebuilt as a light Sand theme so the Featured pair reads as siblings rather than twins. The card composer gained a theme option; text on the light ground is Ink throughout, because Ember fails the text-contrast threshold on Sand — the palette discipline reaching a new surface.

  5. Routes chosen for the remaining defects: the headshot background is to be recomposed over a brand ground using a locally-run segmentation model (rembg — install and every upload remain the creator's actions; the photo never leaves the machine), and a LinkedIn Company Page will be created by the creator, which is the only mechanism that puts a real icon on the project's own entry; its fields are drafted in the internal pack, with the symbol avatar over the wordmark avatar because entry thumbnails render below the wordmark's minimum usable size. The other employers' icons depend on those companies' own pages existing, which is outside anyone's control here and recorded as such.

- **Inference drawn:** None — production record.

- **Limitations / conflicting evidence:** Uploads, the rembg install, and page creation are per-item creator actions; the headshot compositor is unbuilt until the install lands.

- **Effect on project direction:** None.

### Entry 073 — Profile review round: banner made fully abstract, GitHub-marked repo card, headshot recompose rejected

- **Date logged:** 2026-08-12

- **Priority / Question:** Continuation of Entries 070–072 — the creator's completeness review of the applied profile, and the outcomes of the remaining visual work.

- **Source:** Session work, 2026-08-12; live profile read back through the browser extension.

- **What happened:**

  1. Live read-back confirmed the creator had applied the custom URL and the recruiters-only open-to-work configuration; the education and certification entries remain absent (blocked on certificate facts only the creator holds), and the About section could not be verified either way — the page extractor does not reliably surface mid-page sections, and the limit was reported as an instrument limit rather than a finding, per the streetlight discipline.

  2. The banner's domain line was removed at the creator's direction, making the split design fully abstract: the creator found the text sliding behind the avatar at window sizes the placement model does not cover, and judged it redundant besides, since the URL lives on the Featured cards, in contact info and on the planned company page. Every element is now full-bleed, so the design is crop-immune by construction and the placement checks reduce to nothing — the strongest possible fix for a placement bug being to have nothing placed.

  3. The repository social card was rebuilt with the official GitHub Mark leading in place of the GAP wordmark, at the creator's direction, so the Featured pair reads as siblings with distinct faces. The mark was downloaded from GitHub's own brand assets with the creator's explicit permission and is used unmodified per GitHub's logo terms; its PNG bakes an opaque white canvas, so the card composer derives transparency from luminance, leaving the glyph untouched. The mark is tracked beside the cards with its provenance noted in the index.

  4. The headshot recompose (Entry 072's pending route) was built and rejected: rembg's model ran locally and produced four variants, and the creator declined all of them — the removal is not clean enough on the 400 px source. The original photo stays; the pipeline (`tools/build_profile_photo.py`) remains for a retry if a higher-resolution original surfaces.

- **Inference drawn:** None — production record.

- **Limitations / conflicting evidence:** Still outstanding on the profile: the education and certification entries (certificate facts pending), About confirmation, the company page creation, and the re-uploads of the abstract banner and GitHub-marked card — each a creator action.

- **Effect on project direction:** None.

### Entry 074 — Two FOI requests drafted and routed: the counting rules behind the headline figures

- **Date logged:** 2026-08-12

- **Priority / Question:** Research Priority 1's delivered-results thread — turning the log's documented unverifiability findings (`research_log.md` Entries 044, 051, 053, 056, 060, 061) into formal requests for the recorded information the published figures omit.

- **Source:** Session work, 2026-08-12; precedent survey on WhatDoTheyKnow the same day.

- **What happened:**

  1. Two requests were drafted to `drafts/foi_requests.md`, each item mapped to the log entry it rests on, every entry re-read directly at drafting. DSIT, eight items on the 1,001,147 course-completion figure: the operational definition of "completed", the external/internal learner split, One Big Thing's contribution, UK filtering, unique individuals if held, the benchmark-checked proportion, the governing methodology documents with partner identities severable, and the recorded basis for measuring a workers target in course completions. UKRI/Innovate UK, six items on BridgeAI: the completion and accreditation definitions, unique individuals, the £74.6m breakdown, Hub reporting subsequent to UKRI's own disclosure FOI2026/00204, and any evaluation of the programme or its timetable — the last answering Entry 044's "no independent evaluation located".

  2. The precedent survey found six adjacent requests, none covering these questions, and three facts that shaped the drafts: DSIT answered "not held" on Hub costs, placing the Hub's operational records with UKRI; UKRI has already disclosed quarterly Hub reports once, so the new request cites that reference and asks for subsequent editions; and a 2025 request on BridgeAI KPIs was partially successful. The disclosure-log PDFs behind FOI2026/00204 were located, not read — the Hub item is worded to be satisfied by newer editions of whatever they contain.

  3. Two refusal triggers were designed out rather than argued with: per-partner figures are not a primary ask, since DSIT's explainer pre-flags commercial sensitivity and a league table invites section 43 against the whole request; and no policy advice is requested, avoiding section 35 — the counting rules and measurement methodology are asked for instead. Both requests carry the section 16 severability line so one expensive item cannot sink the rest.

  4. The creator chose the WhatDoTheyKnow route — request, requester name and every response published permanently, creating a citable public thread — over direct email. Dispatch is the creator's own action; the statutory twenty working days run from receipt.

- **Inference drawn:** None yet — findings arrive with the responses and land in `research_log.md` when they do.

- **Limitations / conflicting evidence:** Either request can be refused in part or in full; the severable wording is mitigation, not a guarantee. Nothing in the requests should be described as evidence until a response is in hand — and a refusal, if it comes, is itself a documented fact about the figures' checkability.

- **Effect on project direction:** The report's unverifiability findings acquire a formal test with a statutory clock. Responses feed the public-audience report; the request threads become citable the moment they are live.

### Entry 075 — The budget-VRAM findings drawn for the publishing funnel: the price-ladder figure

- **Date logged:** 2026-08-12

- **Priority / Question:** The Entry 067 thread — turning the completed budget-VRAM research into a graphic for the publishing funnel's first step, at the creator's direction to make the document's point clearer and feed-readable.

- **Source:** Session work, 2026-08-12. Data unchanged from `research_log.md` Entries 068–073, re-read at build per the chart rule.

- **What happened:**

  1. A second figure joined `tools/build_vram_figures.py`: `vram_price_ladder`, the document's comparison table drawn as a ladder — one row per card, grouped by VRAM tier with the draft's what-fits descriptors as tier headers, every bar carrying its own name and price, and the per-tier finding annotated where the eye lands: 2.4x at 12 GB, +£120 at 16, used-meets-new at 24, 3.3x at 32. The title states the document's reading ("Nvidia's premium is for the software, not the silicon"); gently portrait output (1544x1678 at 2x) because the feed gives tall images more room.

  2. The scatter stays as the in-document figure; the ladder exists because a feed viewer gives a graphic no axes-and-legend reading time. Same data, same date, and the honesty furniture kept: the 3090 as a two-tracker range marked used against the B60's new, the 48 GB board's exclusion stated with its reason, the software caveat in the subtitle, source-and-date line on the image.

  3. Checks: coverage passes at all four tiers on real data; the label check reports no overlaps in either variant; and both renders were read by eye per the geometry rule — which caught what the code checks could not, a source line running off the canvas edge and the 32 GB annotation block sitting against the 5090's full-width bar. Both fixed and rebuilt.

- **Inference drawn:** None — presentation work over settled findings; no claim appears on the figure that the document's table does not contain.

- **Limitations / conflicting evidence:** The figure inherits its research's limits — single-day UK listing prices in a fast-moving market, stated on the image. It will date quickly; the build regenerates from corrected constants.

- **Effect on project direction:** The post graphic exists as a candidate. The post text and any posting remain per-item creator decisions, and the figure itself awaits the creator's review.

### Entry 076 — The post figure redrawn as launch-to-street; a missing-glyph self-check added

- **Date logged:** 2026-08-12

- **Priority / Question:** Supersedes the figure described in Entry 075, same day, at the creator's direction: show each card's original retail price alongside its UK street price, because the strategic story — where Intel's GPU division is now pointed — was being crowded out by current UK availability.

- **Source:** Session work, 2026-08-12; launch prices from `research_log.md` Entry 078, gathered for this figure.

- **What happened:**

  1. `vram_price_ladder` was rebuilt from grouped bars to a dumbbell per card: hollow marker at the launch price, solid at today's UK street price, the line between them the move. The per-tier annotations now state the launch-price comparison, and the title uses three real UK sterling prices (B70 £1,290, RTX 5090 £1,919 launch and £4,199 today) so the headline claim needs none of the converted figures the rows carry.

  2. The two price bases are not the same kind of number and the figure says so: vendor UK MSRPs exist for consumer cards, while every workstation card is a US list converted at a stated rate with VAT added, marked with an asterisk on each affected label. Mixing an unconverted dollar list with sterling on one axis would have been the larger error; converting and labelling it is the smaller one.

  3. The launch layer is one card thinner than the street layer, because the CUDA card at 24 GB is a 2020 part on the used market. Rather than let that pass, `check_coverage` now runs on both layers and a thin launch level must be declared in `LAUNCH_GAP_NOTED` with the note the figure actually shows; an undeclared gap refuses the build.

  4. **A new class of defect, and a new check for it.** Every label containing an arrow rendered in a serif face: Public Sans has no U+2192, and a single missing glyph drops the whole text run to a fallback font. The spec was valid, the render completed, and `_verify`, `check_labels` and `check_coverage` all passed on a chart with a dozen labels in the wrong typeface — it was visible only by looking. `gap_chart.check_glyphs()` now reads the rendered SVG's text against the font's character map and blocks on any character the brand face cannot draw. The arrow became a guillemet, which Public Sans carries.

  5. Reading the render also caught a false claim written into the 24 GB annotation — "the widest gap on this chart", when the RTX 5090's 2.2x move is wider than the B60's 1.6x. Corrected to what the number actually supports.

- **Inference drawn:** The creator's premise held in one direction and reversed in the other, which is recorded as a finding in `research_log.md` Entry 078 rather than resolved silently in the drawing.

- **Limitations / conflicting evidence:** The figure now carries four lines of source and method, which is dense for a feed graphic; the alternative was dropping caveats the two price bases genuinely need. Launch dates span fifteen months of a moving memory market, so the hollow markers are not contemporaneous with each other.

- **Effect on project direction:** `check_glyphs` applies to every future chart, not only this one. Entry 075's description of the figure is superseded from this date; the bar version is not kept.

### Entry 077 — The post figure stripped back; a canvas-overflow check finds a clipped source line on a second figure

- **Date logged:** 2026-08-12

- **Priority / Question:** Creator review of the Entry 076 figure: the presentation was not right and the image carried too much text for a social post, most of which belongs in the post body.

- **Source:** Session work, 2026-08-12.

- **What happened:**

  1. `vram_price_ladder` was cut to the comparison and nothing else — the four-line subtitle became two short lines, the three-line annotation block beside every tier went entirely, the tier descriptors dropped to three words, the footer went from four lines to three, and type sizes rose throughout. Rendered text elements fell from 39 to 24. The dumbbell form and the underlying data are unchanged.

  2. **The design rule this establishes:** a figure for the publishing funnel's first step carries the comparison; the post body carries the argument. The earlier build failed that test by treating the image as a self-contained document, which is the right instinct for a report figure and the wrong one for a feed.

  3. `check_labels` gained a canvas-overflow test. Pairwise overlap structurally cannot catch a label running off the edge, because it collides with nothing — so the check measured every label against the SVG's own viewBox width instead. It immediately found the defect twice: once on this figure's rewritten footer, and once, unprompted, on `vram_price_capacity`, whose source line has been clipped by about 57 px since it was built on 2026-08-11 and had passed every check since. Both fixed by splitting the line.

- **Inference drawn:** None — presentation work over unchanged findings.

- **Limitations / conflicting evidence:** The width estimate behind the overflow test is the same approximate character-count measure `check_labels` already used, so it will miss a marginal clip and can in principle cry wolf on one; it stays advisory for that reason. Stripping the annotations also removed the figure's statement of the launch-versus-street reversal recorded in `research_log.md` Entry 078, which now survives only in the draft document and the post text — a deliberate trade, but it means the image no longer carries that finding on its own.

- **Effect on project direction:** The overflow test applies to every chart built on `gap_chart`. The spare-figure rule is recorded in the `build_vram_figures.py` index entry as the reasoning for its shape.

### Entry 078 — The capability ladder: era anchors instead of an index number

- **Date logged:** 2026-08-12

- **Priority / Question:** Creator direction, extending the budget-VRAM publishing set: show what a 32 GB card's models are *capable of* against the frontier, with previously-frontier products (GPT-4, the free-ChatGPT models) as anchors a non-specialist recognises — explicitly not an "arbitrary intelligence number" presentation.

- **Source:** Session work, 2026-08-12; research basis `research_log.md` Entry 079.

- **What happened:**

  1. Third figure added to `tools/build_vram_figures.py`: `vram_capability_ladder`, a two-column vertical ladder — the closed frontier's dated anchors on the left, the models that fit one card on the right, a dashed guide at the single-card best marking where the frontier stood in late 2024. Whiskers are drawn where the comparison is close (the two local models and o1) and omitted where a ±5 interval changes nothing; the log entry carries the full intervals.

  2. **Scale choice was a source-discipline decision, not a convenience.** Artificial Analysis surfaced the models first, but its index is rescaled between versions, its reproduction terms are unclear, and it is a commercial benchmarking product. Epoch AI's Capabilities Index is independent, CC-BY, publishes per-model confidence intervals, and its raw CSVs were retrieved directly — so Epoch is the published axis and AA the cross-check, per the source-scope rule.

  3. **The era-anchor labels are sourced product history, not colour.** GPT-4 is labelled as the paid ChatGPT of 2023 because it was never the free model — the free tier ran GPT-3.5 until GPT-4o mini replaced it in July 2024, confirmed against OpenAI's own announcement before the label was written. The creator's initial framing had GPT-4 as the free-app model; the correction is the kind the figure exists to get right.

  4. `check_coverage` is deliberately not run on this figure: it guards categorical comparisons within levels of an x variable, and this chart has no such structure — both columns sit on one shared capability scale, which is the comparison. Noted in the script beside the call sites that do run it.

- **Inference drawn:** The translation device that works for a feed audience is time, not points — "where the frontier stood in late 2024", "what free ChatGPT ran in 2024" — with the index shown but de-emphasised. Same lesson as Entry 077's spare-figure rule, applied to a scale nobody outside the field knows.

- **Limitations / conflicting evidence:** The figure leans on one composite index; the cross-check agrees on ordering but not units. The "late 2024" placement rests on CI-overlapping equality with o1, stated as "level with", and o3's December announcement sits above the guide — the log entry records both rather than the figure arguing them.

- **Effect on project direction:** The budget-VRAM publishing set is now three figures: price-against-capacity (report), price ladder (feed), capability ladder (either). Two candidate teaching artefacts flagged for the source-evaluation lane: the llm-explorer trap (a capability question answered from a popularity-sorted, FP16-assuming directory) and the three-tier confusion ("open models are 4 months behind" read as if it described single-card models).

### Entry 079 — Prose register: the AI tells named, and a paired-rewrite session agreed

- **Date logged:** 2026-08-13

- **Priority / Question:** Creator feedback on generated prose across the project: despite the existing prose rules it still reads as AI-written, it can make a complicated field harder to follow than it needs to be, and on public surfaces that reading alone discredits the work.

- **Source:** Session work, 2026-08-13; trusted-peer review of the project and site, reported by the creator in distilled form.

- **What happened:**

  1. The peer feedback, distilled: the project looks professional; parts are confusing or unclear; the prose sounds unnatural; and no product, conclusion or value proposition is stated. The same material persuaded when the creator explained it in person — which reads as a communication gap, not an evidence gap.

  2. A LinkedIn reply drafted this session was rejected once on register. The redraft that passed differed in nameable ways, recorded because they generalise: balanced antithesis constructions in every sentence, epigram closers, things described instead of named, abstract nouns as agents, and project-internal shorthand in outward text. The first draft carried all five at once.

  3. Agreed: a paired-rewrite register session — Claude drafts passages, the creator rewrites them in their own words — seeded with samples the creator wrote without AI involved, run over real project passages rather than invented exercises, and distilled afterwards into a voice reference and exemplar bank presented for review. Where the output lives (tracked or `internal/`) is undecided.

- **Inference drawn:** Descriptions of a register underperform exemplars of it; the fix is paired examples available at drafting time, not more adjectives in the rules. The review gate stays regardless — this narrows the draft-to-final gap, it does not close it.

- **Limitations / conflicting evidence:** The tells list is one session's observation against one reader's judgement. The Entry 061 lesson still binds: purging tells at uniform density would only manufacture a new uniform style.

- **Effect on project direction:** Register session queued behind the pilot workstation work. Candidate teaching material flagged: making AI prose carry your own voice is precisely the audience's problem, and the session's method and before/after pairs are raw material for a unit on it (redaction pass needed on any pair the creator marks personal).

### Entry 080 — The product hypothesis, and the desktop designated pilot testbed

- **Date logged:** 2026-08-13

- **Priority / Question:** Creator direction: define what the project could actually offer, and start proving it on hardware already owned.

- **Source:** Session work, 2026-08-13; stack facts verified against vendor documentation (sources listed in the unit).

- **What happened:**

  1. Working hypothesis recorded — hypothesis, not commitment: an AI workstation installed on a small organisation's own premises, local or local-plus-API hybrid, carrying bespoke workflows and onboard guidance that teaches its own proper use. Positioned on data locality, cost predictability and learning value rather than raw capability, which is the positioning the budget-VRAM document's break-even and capability findings will actually support.

  2. The project's desktop PC (8-core Ryzen X3D, 32 GB RAM, RDNA3 GPU with 20 GB VRAM) designated the phase-1 testbed. `drafts/pilot_ai_workstation.md` created: three phases — native Windows inference, the containerised deployment shape under WSL2, the SME task set and tutor layer — with a fixed three-prompt measurement protocol so the project's first own-hardware numbers stay comparable across runs and future cards.

  3. This session ran on the laptop, so nothing was installed. The load-bearing stack facts were verified against official documentation: Ollama lists the RX 7900 XT on Windows with a driver-level requirement (no ROCm SDK install); AMD's WSL compatibility matrix (ROCm 7.2.1) lists the card under WSL2 on Ubuntu 24.04/22.04; vLLM carries gfx1100 support upstream. The SEO-blog tier that dominates these search terms was used as leads only, per the source-scope rule.

  4. An Arc card purchase (B580 / B60 / B70) remains open and is the creator's decision; the pilot de-risks the product shape first at no new spend, and the Intel software question stays unanswerable without Intel hardware.

  5. One claim offered alongside the hypothesis is parked as an unverified lead: that enterprise-tier LLM services can leak sensitive or proprietary information under repeated or adversarial prompting, resting on a video source not yet identified or verified — the "nobody has looked yet" kind of hole, per bias trigger 3. The claim is foundational to the fully-local positioning, so it takes a confirm/disconfirm pass before any outward use; the adjacent, already-citable framings (data governance and retention terms, prompt-injection exfiltration in tool-connected deployments) are the honest interim ground.

- **Inference drawn:** The peer-review pattern and the product hypothesis point the same way: the evidence base is ahead of the communication of it, and the missing "so what" on the site is the offer this hypothesis, once tested, would supply.

- **Limitations / conflicting evidence:** The hypothesis is untested end to end. Capability adequacy is task-specific and unmeasured — the pilot's own question. The workstation-as-product economics must survive the project's own break-even finding that below a high usage threshold the API route stays cheaper.

- **Effect on project direction:** The pilot phases become the active workstream, alongside the queued register session. The hands-on unit thread in `research_log.md`'s Open Threads now has a concrete first machine and a written protocol.

### Entry 081 — The Arc card decision: Arc Pro B70, 32 GB

- **Date logged:** 2026-08-13

- **Priority / Question:** Creator decision, closing the purchase question the budget-VRAM document and the pilot unit both recorded as open.

- **Source:** Creator decision, 2026-08-13. Card selection reasoned from `research_log.md` Entries 068–073 and 078–079, re-read rather than recalled.

- **What happened:**

  1. **Decided: the Arc Pro B70**, 32 GB, ~£1,290 UK street at the 2026-08-11 price snapshot.

  2. **Why the B70 rather than the cheaper cards the documents named.** The B580 at ~£245 tests the floor and the B60 at ~£830 tests the price claim, but neither reaches 32 GB — and 32 GB is where the project's own findings converge. Entry 078 found the Intel/Nvidia gap widest there at street prices, 3.3x against 2.3x at launch. Entry 079's capability ladder put the useful single-card open models, Qwen3.6 35B-A3B and Gemma 4 31B, at 24–32 GB. A cheaper card would have measured a tier the argument does not rest on.

  3. **What it unblocks.** The three-prompt protocol in `drafts/pilot_ai_workstation.md` runs on it unchanged, which is what the protocol was built for. The VRAM document's "What would settle it" section becomes actionable. The idle-power hole, open since Entry 071 and unmeasurable in software because the Linux driver does not expose GPU power, becomes measurable with a wall meter.

  4. Buying the card settles nothing by itself. Every claim in the VRAM document still stands or falls on measurement, and nothing is published from it until it has been run.

- **Inference drawn:** Desk research on this question is finished. Seven primary benchmark sources, every surfaced lead read, and what remains is the kind of uncertainty only a card on a bench resolves.

- **Limitations / conflicting evidence:** The purchase is made into a rising market, so the price paid is a snapshot and not a recommendation to a later reader. The break-even finding is unchanged and unflattering — below a high usage threshold the API route stays cheaper, and this card does not move that arithmetic. Two findings surfaced this session, ECC on the Arc Pro line and the memory-bandwidth cost of unified-memory machines, are not yet in `research_log.md` and nothing above rests on them.

- **Effect on project direction:** Phase-1 AMD work and the Arc work now run in sequence on one protocol. Three tracked documents carry current-state claims the decision makes stale; corrected in the same edit.

### Entry 082 — The technical exchange produces a common-environment agreement and two baseline documents; both verified and converted through the pipeline

- **Date logged:** 2026-08-14

- **Priority / Question:** The external practitioner exchange (running since 2026-08-13; private record in the internal working notes, per the pointer pattern) reaching its first joint work products, on the thread the B70 purchase opened (Entry 081).

- **Source:** Session work, 2026-08-14: the correspondence transcript supplied by the creator, two received documents, vendor verification (`research_log.md` Entry 086), and the repo's own hardware records.

- **What happened:**

  1. **A common working environment was proposed by the correspondent and accepted in principle: Ubuntu 26.04 LTS Desktop, x86-64** — chosen to match what the project's always-on server already runs. Staging: the correspondent builds and validates the shared stack on his own 16 GB Arc card first, then evaluates how much transfers to the project's incoming B70; exact versions recorded at every verified stage, toward a shared "reference environment manifest". His stated principle — stability and reproducibility before newest versions — matches the pilot unit's protocol design, arrived at independently.

  2. **Two source-checked baseline documents were received**: a 24-page A770 AI/RAG installation-and-verification guide (the shared-stack half, staged INSTALL → VERIFY → RECORD → NEXT with explicit PASS gates), and a B70-specific checkpoint supplement keyed to the project's card. The author's own caveat is carried on both: cross-checked against Intel's current documentation, **not yet validated on hardware** — his phrase, "source-checked first, hardware-validated next".

  3. **The load-bearing citations were verified at the vendor the same day** — `research_log.md` Entry 086. Every checked claim resolved, including the OMIX stack the B70 document is built around, which had entered the exchange as an unverified AI-search result and turns out to be real and current. One label could not be re-pinned (Ollama's Vulkan path described as "Experimental" — not found on the two pages fetched), and Intel's OMIX matrix already lists a release beyond the one the documents cite — which confirms the documents' own freeze-at-install advice rather than faulting them.

  4. **Both documents were converted through the project's pipeline** (`tools/md_to_docx.py` → `tools/fitshapes.py` → both Word self-checks) as the demonstration promised to the correspondent — faithfully: prose unaltered, code blocks re-indented only where PDF text extraction had flattened them, and discrepancy findings reported in chat rather than edited into another author's documents. Outputs delivered in-session and deliberately not tracked: third-party-authored content, with the internal reference-material folder as the archive location if wanted.

  5. **The reconciliation surfaced a hardware decision the repo has not recorded: which machine hosts the B70.** *(Answered by the creator the same day — Entry 083. Left as written because the surfacing is what this entry records.)* The server is the Ubuntu 26.04 machine the environment agreement anchors on, but it is a one-slot Mini-ITX B350 build — a PCIe 3.0 link two generations below the card's Gen5 interface, a 2015-line 450 W PSU already logged as the build's open unmitigated risk (Entry 035) set against a 230 W-TBP card, an incumbent GPU doing display duty to the projector, and Resizable BAR support unverified under the build's standing do-not-update-BIOS note. The desktop is the stronger platform but runs Windows for the pilot's phases 1–2, and its board slot layout and PSU rating are unrecorded. Neither machine matches the documents' assumed environment without a decision, and the decision is cheaper made before the card arrives than after.

- **Inference drawn:** The exchange has moved from findings about the project's documents (`research_log.md` Entries 082–083) to joint infrastructure. The verification outcome is worth stating plainly: the correspondent's documents passed a hostile citation check — every URL real, every quoted support level as stated — and the one thing the check could not do, validate against hardware, is the thing the documents themselves name as next.

- **Limitations / conflicting evidence:** The environment agreement is in-principle, not installed fact; nothing has been stood up on either side. The reconciliation also caught one currency gap on the project's own side: the creator described the desktop's WSL2/Ollama/Docker layer to the correspondent as running, while the pilot unit still records phases 1–2 as planned — to be reconciled whichever way is true before the pilot doc's status notes are next relied on.

- **Effect on project direction:** The B70 host-machine decision joins the queue ahead of the card's arrival, with the PSU question attached to it. The pilot's Arc phase gains a peer-review loop — the A770 end of the shared stack gets validated by someone who owns the card. `research_log.md` Entry 086 carries the software-stack corrections queued for the VRAM draft.

### Entry 083 — The B70 goes in the desktop; the real question turns out to be the operating system, not the platform

- **Date logged:** 2026-08-14

- **Priority / Question:** Creator decision, closing the host-machine question Entry 082 surfaced the same day.

- **Source:** Creator decision, 2026-08-14. Requirements checked against vendor documentation and against the machine itself before writing — `research_log.md` Entry 087.

- **What happened:**

  1. **Decided: the B70 goes in the existing desktop**, the Ryzen 7 7800X3D machine already designated the pilot testbed (Entry 080), reusing that build's foundations rather than the always-on server. Native Linux, WSL2 and a possible new motherboard and CPU were all raised by the creator as things the route might need; each was checked rather than assumed.

  2. **The desktop is the better host on every axis that was in doubt.** It carries the faster CPU, a modern AM5 platform with Resizable BAR, and a graphics slot at PCIe 4.0 x16 from the CPU. The server would have offered a 2015-line 450 W PSU already logged as an unmitigated risk, a PCIe 3.0 link, and its only slot occupied by the card driving the projector. The decision removes the whole cluster of constraints Entry 082 item 5 listed.

  3. **A new Intel motherboard and CPU are not required by the card.** Resizable BAR is the actual platform requirement, an AM5 Ryzen 7000 system satisfies it, and Intel's documentation allows for non-Intel platforms with ReBAR or Smart Access Memory enabled. What a board change would buy is slot topology rather than compatibility — see below — so it is a later question and not on the path to first tokens.

  4. **Two real constraints replaced the imagined one.** The board publishes one graphics-usable slot (PCI_E1 Gen4 x16 from the CPU; PCI_E2 is Gen3 x1 from the chipset), so the 7900 XT and the B70 take turns rather than coexisting — which sequences the pilot rather than changing it, AMD phases first, then swap. And **WSL2 is not a documented path for a B-series Arc card**: PyTorch's validated client-GPU list names Windows 11 and Ubuntu only, and Intel's IPEX documentation explicitly excludes B-series from WSL2. Phase 2's containerised deployment shape therefore means native Linux for the Arc half.

  5. **So the open question is now the operating system, not the machine.** Three routes, priced in `drafts/pilot_ai_workstation.md`: native Windows (validated for PyTorch XPU and Ollama, but no OMIX, no Intel containers, and none of the shared stack agreed with the external correspondent); dual-boot Ubuntu 26.04 (everything, at the cost of rebooting between the AMD and Intel halves); or Ubuntu outright (everything, at the cost of the desktop's current use). Nothing is decided here.

  6. **Three checks queued before the card arrives:** MSI's own slot specification read by hand, since their site blocks automated fetching and the second and third slots are search-level; the PSU rating read off the unit, unrecorded and unreadable in software; and ReBAR with Above 4G Decoding confirmed in BIOS.

- **Inference drawn:** The decision converges with the collaboration rather than diverging from it. The shared environment agreement assumes Ubuntu 26.04, and the WSL2 finding independently forces native Linux for the containerised phase — so the route that satisfies the project's own Phase 2 is the same route that keeps the two environments comparable.

- **Limitations / conflicting evidence:** Both load-bearing negatives are the weakest-sourced claims in the entry — the WSL2 exclusion comes from an EOL-dated product's documentation at search level, and PyTorch's silence is absence of validation rather than a statement of impossibility. Cheap to test once the card is here, and worth testing rather than inheriting. The board's slot layout is likewise search-level. The PSU is the check with actual physical risk behind it and it is still open.

- **Effect on project direction:** `drafts/pilot_ai_workstation.md` revised in the same session — machine table, Phase 2 scope, and the Arc section rebuilt around host and OS. The Entry 082 note that neither candidate host could negotiate Gen5 is superseded: this board does Gen4 x16 from the CPU, which is a different and better answer than the server's Gen3, and enough for single-card inference either way.

### Entry 084 — Every numbered list after the first was wrong, in every document the converter has made

- **Date logged:** 2026-08-14

- **Priority / Question:** Promoting `drafts/pilot_ai_workstation.md` through the docx pipeline at the creator's direction, the foundations now being settled.

- **Source:** Session work, 2026-08-14. Defects found by reading rendered pages; fixes in `tools/md_to_docx.py`.

- **What happened:**

  1. **The unit was promoted.** `drafts/Pilot_AI_Workstation.docx` and its self-check `.pdf` now exist, which the file's own index entry had deferred until the unit stabilised. The markdown remains the source of truth.

  2. **Reading the render found four defects, none of which any automated check caught.** The fitter, the Word render check and the save round-trip all passed on a document that was visibly wrong.

     - **Numbered lists never restarted.** Every ordered list in a document pointed at the template's single numbering instance, so Word continued one sequence file-wide: the pilot unit's first procedure began at step 4 and its prompt set at 13. Fixed by emitting one numbering instance per list, each carrying a `startOverride`. The template's abstract definition — the house numbering format — is untouched, so the tool still contributes no formatting of its own.

     - **A fenced block indented under a list item was swallowed as prose.** The continuation branch appended it to the item's text, which collapsed the pilot's fixed extraction test input from five lines into one. Fixed by emitting the block properly, with the list resuming afterwards on the same numbering.

     - **A table column could be narrower than a word in it**, so Word broke "Motherboard" mid-word across three lines. Columns now carry a floor sized to their longest unbreakable word, estimated generously rather than measured — the tool takes no font dependency by design.

     - **Two-digit list markers collided with their text** ("11.STEP 11"), the hanging indent having been sized for a single digit. This one only exists in lists of ten or more items, which is why nothing had hit it before.

  3. **The already-converted documents were rebuilt.** The two received from the external correspondent (`project_log.md` Entry 082) carried the numbering defect — the B70 document's "Proceed" sequence rendered as 7, 8, 9 and its fourteen-step bring-up sequence would have followed on from an earlier list. Both regenerated and re-verified before being sent anywhere.

  4. **The rest of the repo's generated documents were checked rather than assumed.** Counting ordered lists in each source found only one other affected file, the internal build guide with five; the other units carry one list or none, where the defect cannot show. That one was regenerated too, its original footer recovered from the existing file rather than guessed.

- **Inference drawn:** The self-check tooling verifies what it was built to verify and stays silent on everything else. `fitshapes.py` measures card heights, `word_preview.ps1` proves a document renders, `word_roundtrip_test.ps1` proves it saves — and a document can pass all three while numbering its steps wrongly from beginning to end. The geometry rule already says generated visual assets get looked at; this extends the same reasoning to generated documents, where the failure is not a clipped label but a wrong instruction.

- **Limitations / conflicting evidence:** The column-width floor is an estimate, not a measurement, so a table with an unusually wide heading may still be tighter or looser than a person would set it. The numbering fix has been verified on four documents, not proven in general — a document mixing nested ordered lists, which the converter flattens anyway, has not been tested.

- **Effect on project direction:** `tools/md_to_docx.py` gains the four fixes and the docstring notes to match. Anything previously converted and sent outside the project should be assumed to carry the numbering defect and regenerated before it is relied on.

### Entry 085 — The creator's revision reconciled, the PSU recorded, and the pilot unit gets its two figures

- **Date logged:** 2026-08-14

- **Priority / Question:** The pilot unit's revision pass, at the creator's direction: check the validity of its points, propose structural strengthening, record the PSU, and build one or two figures where the information genuinely benefits.

- **Source:** Session work, 2026-08-14: the creator's hand-edited `.docx` (backed up before anything regenerated over it), the machine's own reports, and the vendor documentation already logged in `research_log.md` Entries 080 and 086–087.

- **What happened:**

  1. **The creator edited the generated Word file directly, and the edits were ported back into the markdown source rather than lost.** The revision was extracted and checked first: no non-breaking spaces, styles intact — the paste defects of Entries 039–041 did not recur. Ported: the title split to Title + Subtitle, shorter declarative sentences through the Phase 1 evidence bullets, the cooling spec, a softened 24 GB-class claim, and a Phase 3 expansion — a medical-RAG task-set bullet marked undecided, and the tutor layer's learning vision. Two mechanical slips were fixed in the port and reported; two register questions (an "ineffective training" characterisation and an unhedged market-uniqueness claim) were raised in chat for decision rather than edited, per the revised-draft rule.

  2. **The PSU is recorded: Corsair RM1000x (2021), 1000 W, 80+ Gold, fully modular** — stated by the creator from the unit. That closes the third pre-arrival check and the swap-risk concern; the hardware table and `[GAP-DESKTOP26]` carry it.

  3. **Two figures built, and a new tool to build them.** `fig_pilot_stacks` — one machine, two card eras over the single shared slot, carrying real vendor marks at the creator's direction, monochrome so eight brand colour schemes do not compete with the document (sources and licence: `assets/figures/brand_icons/README.md`). `fig_pilot_os_matrix` — where each card's stack is documented per the vendors' own pages, which is the unit's OS argument as a grid. `tools/build_pilot_figures.py` draws both on the server-guide helpers and rasterises the marks through vl-convert or Inkscape, whichever the machine has: this desktop has Inkscape and not `vl-convert-python`, the reverse of the laptop, so the chart layer's own figures cannot rebuild here until that package is installed.

  4. **The converter learned the Title/Subtitle split as a rule:** an italic-only line directly under the `#` title now takes the template's real Subtitle style, so the creator's hand pattern is reproducible from markdown.

  5. **One correction owned.** Entry 084's column-width floor was still ~150 twips short for "Motherboard", and the mid-word break survived — the render check that "confirmed" the fix had been read too quickly. The constant is corrected and the fix verified on the actual page this time. Both figures' first renders also each carried one defect (text touching a box border; a source line clipped at the canvas edge — the same overflow class `gap_chart` checks for in code), caught by reading the renders.

- **Inference drawn:** Item 5's, again and sharper: a check that exists but is skim-read is a check that does not exist. The Pillow figure family has no coded equivalent of `check_labels`, so its geometry rule is only as good as the reading.

- **Limitations / conflicting evidence:** The figure family's overlap checking is manual; worth code if the family grows past these three scripts. The validity findings on the two Phase 3 claims are proposals awaiting the creator's decision, not applied changes.

- **Effect on project direction:** The pilot unit carries its figures, the recorded PSU, and the creator's own register through the Phase 1 prose. `tools/build_pilot_figures.py` and `assets/figures/brand_icons/` are indexed in `CLAUDE.md` in the same edit. The two register questions stand open in chat.

- **Follow-up, same day — the register questions decided and the argument restructured.** The creator took both wording proposals and three of the five structural ones. The two claims that outran the evidence are now inside it: "otherwise ineffective training for SMEs in the UK" became "training that is currently measured only in course completions" — which is what Entries 044 and 074–076 actually support — and the market-uniqueness claim is hedged to "nothing else found so far", pending a Priority 5 comparables scan that has never been run. Structurally: the tutor-layer vision moved from page six into "What this pilot is for", where it now states the product's purpose before the hardware detail rather than after it; Phase 3 keeps only what Phase 3 can test, with the two task sets folded into one concept carrying two candidates; and the OS-routes section states its convergence before the table so the table reads as evidence, ending on "Not decided." One flattening defect was caught in the render and fixed: the converter renders nested list items at their parent's level, so the two task-set candidates arrived as siblings of the bullet that introduced them — the opposite of the change requested. Italic "Candidate one/two" labels restore the hierarchy in both markdown and Word without teaching the converter to nest, which is a larger change than this earned.

- **Closing pass, same day — the Word file taken as canonical, and two rules adopted from it.** The creator made a final editing pass in Word before sending the document out, so that file rather than the markdown was the current version. Reconciled by porting every change back into the markdown, regenerating, and diffing the two text extractions against each other — which caught a deletion no reading would have found, the closing "Not decided." having been cut from a section it had been added to earlier the same day. It also caught an over-correction of mine: a doubled "confirmed" that had been tidied on the assumption it was a slip, restored to the creator's wording because a canonical file's register is theirs to set. One spelling was normalised to match the rest of the document and reported. Two rules came out of this and are written into `CLAUDE.md` with their evidence: **the em-dash apposition** as the project's most persistent AI tell, promoted after two consecutive revision passes showed breaking those asides into short sentences was the creator's dominant edit; and **the canonical hand-edit loop** above, as a working procedure rather than an improvisation. The same day's rule-extraction pass found sixteen of eighteen memory files already captured in the repo, two correctly machine-local, and exactly one gap — which was the first of those two rules.

### Entry 086 — A Korean edition for the correspondent, and the measuring bug it exposed

- **Date logged:** 2026-08-14

- **Priority / Question:** Creator direction: produce a plain-text copy of the pilot unit for sending over LinkedIn, which does not accept `.md`, and a Korean translation so the correspondent can read it in an ordinary PDF viewer rather than through a machine translator.

- **Source:** Session work, 2026-08-14. Translation done in-project rather than by the recipient's tooling, at the creator's reasoning that the full project context is here and mistranslation of the technical argument is the risk worth spending on.

- **What happened:**

  1. **`drafts/pilot_ai_workstation.txt`** — the English markdown with image lines rewritten as readable figure references, since a relative path to a file the recipient does not have is noise. Sent as the machine-readable copy.

  2. **A Korean edition, markdown-first like every other unit.** `drafts/pilot_ai_workstation_ko.md` is the source; `Pilot_AI_Workstation_KO.docx` and its self-check `.pdf` are generated from it. Held in formal register throughout. **Product names, commands, file paths, citation keys and the three fixed measurement prompts are deliberately left in English** — the prompts because they are the measurement's input, and translating them would end comparability between runs. A translator's note callout states this at the top. The two figures stay English with translated captions.

  3. **Two capabilities added, both reusable.** `md_to_docx.py --east-asia` names a font on `w:eastAsia`, which is the attribute Word resolves CJK characters through, so Latin text keeps Public Sans and Hangul renders in Malgun Gothic. Applied as one sweep over the assembled XML rather than at each of the five places a run is built, because a single missed site is a paragraph of tofu. `fitshapes.py --measure-face` measures widths with a font that has the script's glyphs, and `--line-scale` compensates for Word laying CJK lines out taller than the font's own metrics — measured at about 1.28 here, and a multiplier rather than padding because the shortfall grows with the number of lines.

  4. **The real find: `fitshapes.py` has been measuring escaped XML, not text.** The writer emits non-ASCII as numeric character references, so the fitter was measuring the literal string `&#8212;` — seven characters — wherever a document shows one em-dash. In English that inflated card heights mildly and invisibly. In Korean, where every syllable becomes `&#47928;`, a 430-character paragraph measured as 2,037 and produced a callout card 476pt deep against a correct 147pt, which is what finally made it visible. Fixed by unescaping before measuring. **Every callout card this project has ever fitted was slightly too tall**, which is why the defect survived: it erred toward padding, never toward clipping.

- **Inference drawn:** The same lesson as Entry 084, from the opposite direction. That defect hid because no check could see it; this one hid because it failed safely. A bug that only ever adds whitespace produces no symptom anyone will chase, and it took a script the font could not draw to surface a defect that had been in every English document all along. Translation worked here as a stress test, not just a deliverable.

- **Limitations / conflicting evidence:** `--line-scale` is an empirical constant, not a derivation — it was fitted by rendering and reading, and 1.28 is calibrated for Malgun Gothic at this document's sizes rather than established for CJK generally. Two intermediate explanations were wrong before the real cause was found: first that CJK line metrics were to blame, then that Malgun carried a line gap PIL was not reporting. Both were tested and discarded, the second by measurement. The translation is unreviewed by a native speaker; the creator's own check is the gate before it is sent.

- **Effect on project direction:** The document pipeline can now produce non-Latin editions, which it could not this morning. Anything previously fitted carries slightly generous callout padding and will tighten on the next rebuild — cosmetic, and not worth regenerating documents for on its own.
