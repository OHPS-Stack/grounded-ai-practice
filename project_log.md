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
     committed in b03d76d.

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

  2. **The audit gap.** The hook entered history in commit `c6734cb`,
     2026-07-28, titled "Prepare for public release". The audit recorded
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
