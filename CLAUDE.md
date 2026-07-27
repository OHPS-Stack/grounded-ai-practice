# Grounded AI Practice — Claude Code project context

This file is read automatically at the start of every Claude Code session in
this repo. It exists so context built up over many chat sessions doesn't need
re-explaining each time. Keep it updated as the project evolves — treat it as
a living document, not a one-time export.

## What this project is

**Grounded AI Practice** — practical AI capability through responsible,
hands-on learning. Full detail: `PROJECT_BRIEF.md`.

**Current stage: research/scoping.** Nothing here is a finished
specification, curriculum, or repo structure. See `RESEARCH_QUESTIONS.md` for
the five immediate research priorities driving current work.

## Working approach (from PROJECT_BRIEF.md)

- Factual claims must be traceable to sources.
- Evidence, inference, personal observation, and proposal must be clearly
  distinguished — never blur these together.
- Major decisions are made explicitly, not inferred from drafts.
- Structures and rules are introduced only when they solve a demonstrated
  need — avoid premature governance (this is explicitly what PAWH, the
  project's predecessor, got wrong).
- The project should remain understandable without depending on an AI
  assistant. AI tools support research and production; human review remains
  necessary.
- Commands should never be blind copy-paste — whether Claude runs one or
  hands one to the user. When suggesting a command for the user to run
  themselves, explain what it does and why, especially anything security or
  system-relevant. This is part of the project's own subject matter
  (responsible AI use, verification, human oversight), not just a courtesy.
  For setup/install/configuration commands specifically, default to
  explaining and handing off for the user to run themselves rather than
  Claude executing directly — even when permission would likely be
  granted. Reserve direct execution for read-only/diagnostic actions or
  when the user explicitly asks Claude to run something.
- Word documents (`.docx`) get a self-check before being treated as
  finished: `tools/word_preview.ps1` exports the file through actual
  Microsoft Word via COM automation to PDF, which Claude then reads
  directly — not a LibreOffice-rendered approximation. LibreOffice's layout
  engine has diverged from Word's real rendering on grouped/shape-based
  content in this project before, so treat a LibreOffice preview as
  provisional, not confirmation that formatting is correct.
- More generally: prefer workflows where output can be self-verified
  against ground truth (a real renderer, the actual target application, a
  test suite) over iterative guess-and-describe loops. If no such path
  exists yet but one could plausibly be built, say so explicitly rather
  than defaulting to repeated manual review rounds.
- Ask the user directly for cheap-to-state facts about their own
  environment or preferences (e.g. "is X installed?") rather than running
  exploratory commands to find out — reserve diagnostic commands for
  things faster to check than to ask about.
- If a task's best approach depends on a tool or runtime that turns out to
  be missing, say so explicitly — what's missing, what it would unlock,
  brief install instructions — before falling back to a weaker workaround.
  Never install anything yourself; surface the command for the user to run
  (see "Commands should never be blind copy-paste" below).
- When a stated pain point matches a known tool or product (including
  Anthropic's own — Claude for Word/Excel/PowerPoint, Claude in Chrome,
  connectors), name it unprompted. Time it to when it's actually relevant
  to the task in front of you, not as a scattershot list.

## Research discipline

Full detail and current status: `RESEARCH_LOG.md` (source key, log entries,
open threads). Key standing rules:

- **Source scope:** prefer official/government sources (gov.uk, ONS,
  Parliament), independent academic sources, and established international
  bodies. Vendor/commercial and advocacy sources are deprioritised, not
  banned — useful for spotting a claim worth checking, not as standalone
  evidence for anything scope-defining. Tag every new source's interest
  type (Independent/Academic, Government/Official, Vendor/Commercial,
  Advocacy/Membership body) in the Source key table.
- **Confirm/disconfirm pairing applies to foundational claims** — the ones
  that would actually change project direction — not to every statistic.
  Don't default to only searching for evidence that supports an existing
  hypothesis; this project has already caught itself doing this once (see
  Entry 013 in the log) and corrected for it.
- **Exhaustive adversarial verification of every claim is deferred** to
  dedicated deep-research passes later, once scope is firmer. Right now,
  general research to inform direction is the priority, not a citation-perfect
  final product.
- **Known unresolved tensions are parked, not endlessly re-litigated:** e.g.
  the technical-vs-literacy capability framing question, the gap-widening-
  vs-declining conflict between sources. Check `RESEARCH_LOG.md`'s Open
  Threads section before assuming something hasn't been investigated yet.
- **Don't chase every open thread every session.** Check in on direction
  before spending significant effort, especially for anything that would
  use a lot of tokens/time.

## File conventions

- **Files intended to directly replace a previous version keep the exact
  same filename — no version suffixes** (no `_v2`, `_final`, `_updated`).
  This project relies on git for version history, not filename suffixes.
- Markdown is the default format for research/reference documents, matching
  the existing project files.
- When editing `RESEARCH_LOG.md` or `PROJECT_LOG.md`, preserve the existing
  entry structure (numbered entries, the field shape each uses) rather than
  restructuring it.
- **`RESEARCH_LOG.md` is for source-backed research findings only** —
  a dated, numbered entry answering a `RESEARCH_QUESTIONS.md` priority,
  with a citable source. **`PROJECT_LOG.md` is for everything else durable
  that isn't research** — scoping/creative decisions, design/production
  work, technical build notes — also as dated, numbered entries, but
  without a research citation. **`PROJECT_BRIEF.md` holds the current,
  standing state** of a decision, not its history (that's `PROJECT_LOG.md`'s
  job). Getting this wrong is not hypothetical: `RESEARCH_LOG.md` drifted
  into a mixed dump of both for a while, which produced a real numbering
  collision (two unrelated tracks each independently numbering entries
  039-042) before the two were split apart on 2026-07-27 — see
  `PROJECT_LOG.md` Entry 017.
- **New standalone files beyond these three are the last resort, not the
  default.** Before creating one for durable content, check whether it can
  extend an existing file first. A new file only earns its existence if
  it's a genuinely distinct, closed category that doesn't fit any existing
  file's purpose — not just because an explanation got long.
- **Any new file must be added to this file's "Where to look for what"
  section in the same edit that creates it.** Indexing is not a follow-up
  task — a file left unindexed at the moment it's created is exactly the
  "badly indexed" failure mode this rule exists to prevent (see
  "Relationship to PAWH" in `PROJECT_BRIEF.md`).
- **Avoid jargon/buzzwords in naming or reader-facing copy** (unit titles,
  headings, capability names) — plain, concrete wording beats a clever
  abstract phrase. The fix for jargon is plainer language, not a simpler
  underlying idea — the working assumption is a fairly intelligent reader,
  so don't swing into patronising oversimplification either.
- **SVG/vector asset groups (`<g>` elements) should carry clear snake_case
  labels** (`id` and/or `inkscape:label`) so a human can find the right
  group to edit without guessing. Individual leaf `<path>` elements don't
  need their own names — that effort doesn't pay for itself. Never rename
  an *existing* id without first checking nothing references it (gradient
  `url(#...)`, `xlink:href`, `clip-path`) — only add labels to currently
  unlabelled groups unless there's a specific reason to touch a working one.

## Word document conventions

Applies to `.docx` work in this project (currently
`Effective_Prompting_Example.docx`, `Style_Reference_Example.docx` in
`drafts/`, and any future Word deliverable built the same way). Established
2026-07-27 during the style-reference review.

- **Body font is Public Sans, not Calibri.** Installed locally as its own
  family (`Public Sans`, with regular/bold/italic faces under that one
  family name), plus separate weight-named families (Black/ExtraBold/
  ExtraLight/Light/Medium/SemiBold/Thin) if finer control is ever needed.
  Reference via `w:rFonts w:ascii="Public Sans"` and toggle `<w:b/>`/`<w:i/>`
  for bold/italic — no separate family string needed for those two faces.
- **Structural text uses real named Word paragraph styles, not per-run
  direct formatting.** Title, Subtitle, Heading1/2/3, Normal/body, Caption
  and Quote each get their own font/size/weight/colour defined once in
  `styles.xml`'s `<w:rPr>` for that style, so a run using it needs no direct
  formatting at all. Headings carry a real `<w:outlineLvl>` so Word's native
  Table of Contents and Navigation pane work without extra setup, and so a
  section added later can just pick "Heading 1" from the Styles pane and
  match what's already there. Reserve direct run/cell formatting for
  content that's genuinely data-driven per instance — callout-card label
  colour (varies by semantic type), table cell shading, palette swatch
  text — not for faking a structural role with bold-and-a-bigger-size.
- **Callout cards use small/medium/large size presets**, each fixing the
  icon-well size; a card's width (and therefore its text column) is always
  a free parameter independent of preset, so resizing a card for its
  content never stretches or squeezes the icon. Built as a Word group
  (`wpg:wgp`) of sibling shapes, not nested shapes — see `PROJECT_LOG.md`
  Entry 015 for why (Word rejects a shape nested inside another shape's
  text box) and the rest of the construction.
- **Vertical accent/divider bars are pill-shaped** — a narrow `roundRect`
  with `<a:gd name="adj" fmla="val 50000"/>` (50% corner radius relative to
  the shape's short side, which fully rounds a narrow bar into a capsule),
  not a paragraph-border line (`w:pBdr`), which can only draw a straight
  edge. Used for the callout-card divider and the pull-quote rule.

## Git conventions

- **Draft the commit message and show it to the user before running
  `git commit`**, for any commit with a real message to write (not a
  one-liner the user dictated directly). A go-ahead like "let's commit
  this" means prepare it, not execute it unreviewed — commits are
  semi-permanent and this repo may go public.
- **Never push to the remote without a separate, explicit go-ahead**, even
  immediately after a local commit the user asked for. The user handles
  pushes themselves.
- **Commit messages (and any other outward-facing prose — docs, summaries)
  must match the user's own voice**: short, direct, no AI-register
  em-dash-chaining, and never third-person references to the user (e.g.
  "the creator") — that framing belongs in `RESEARCH_LOG.md`'s internal
  entries, not in text written in the user's own voice.

## Known mistakes to not repeat

- Earlier in this project (before the Claude Code migration), several log
  edits accidentally deleted an entry's header when inserting new content
  before it, because old_str/new_str boundaries didn't fully cover the
  edited region. When inserting new content immediately before existing
  content, anchor edits narrowly and verify the target file afterward rather
  than assuming the edit landed cleanly.
- Confirmation bias in research query framing was caught once already (only
  searching for evidence *for* the assumed problem, never against it) — stay
  alert to this pattern recurring, especially when sources have a
  commercial/institutional interest in a particular answer.

## Where to look for what

- `PROJECT_BRIEF.md` — problem statement, scope, what's decided vs. open
  (including the "Visual identity" working decisions: palette, logo type,
  tone).
- `RESEARCH_QUESTIONS.md` — the ten priority areas and their questions.
- `RESEARCH_LOG.md` — source key (with interest-type tags), dated log
  entries, and the Open Threads list showing what's resolved vs. still open.
  Research findings only — see "File conventions" above for the boundary
  with `PROJECT_LOG.md`.
- `PROJECT_LOG.md` — dated log of scoping/creative decisions and design/
  production/technical work (visual identity history, icon/logo production
  notes, Word-document engineering notes, this file's own split from
  `RESEARCH_LOG.md`). The chronological history behind what
  `PROJECT_BRIEF.md` currently reflects.
- `assets/brand/icons/` — the promoted, working content-icon set (36
  icons, current palette). `svg/` for sources, `png/` for 64/128/256px
  exports, `README.md` for the filename→topic manifest.
- `assets/brand/logo/` — the finished logo system, status FINAL:
  `logo_symbol.svg` (default, shaded), `logo_symbol_flat.svg`,
  `_mono`/`_reversed` symbol variants, and `logo_lockup_horizontal`/
  `logo_lockup_vertical` (+ `_mono`/`_reversed`) icon+wordmark lockups, all
  with wordmark text as real vector paths (Public Sans) and a two-tone
  colour hierarchy, plus `profile_picture_square`/`profile_picture_circular`
  avatar derivatives, plus `png/` exports for all of them. See
  `PROJECT_BRIEF.md` "Visual identity" for the full picture.
- `assets/brand/logo/creative_brief.md` — portable creative brief for
  external logo-generation workflows (not a project research/decision
  document itself).
- `drafts/` — work-in-progress files under active iteration. Currently:
  `Effective_Prompting_Example.docx`, a formatting test for the pilot
  unit's Word-document template — see `PROJECT_LOG.md` Entry 015 and the
  PAWH semantic-callout construction it's adapting — still genuinely a
  draft, nothing settled; and `AI_Skills_Hub_Briefing.docx`, not yet
  logged. Nothing here reflects a settled decision; contents may be
  replaced or removed once the format stabilises. Once a document is
  approved and no longer a draft, it moves to `documents/` instead.
- `documents/` — finished, current production exports, promoted out of
  `drafts/` once approved (not work-in-progress). Currently:
  `Style_Reference_Example.docx` (+ its self-check `.pdf`), a 6-page
  catalogue of the Word visual patterns in use, built on a real named-style
  system (Title/Subtitle/Heading1-3/Normal/Caption/Quote, all Public Sans,
  all with real outline levels so Word's native TOC and Navigation pane
  work against them) rather than per-run direct formatting — plus title
  block, pull quote (pill-bar Word group), callout cards (four semantic
  types, small/medium/large size presets with a fixed icon well independent
  of text-column width), three table types, dash/native-bullet/
  native-number lists, a figure-with-caption, and the palette as swatches.
  **Approved as canonical for current purposes (2026-07-27, see
  `PROJECT_LOG.md` Entry 016) — still subject to later refinement, but no
  longer a first draft**; the "Word document conventions" section above is
  the extracted rule set. Icon set inconsistencies (padding, mismatched
  speech-bubble styles across icons) are the one explicitly open exception
  — separately deferred, creator revisiting the icon set directly in
  Inkscape.
- `tools/word_preview.ps1` — self-check step for `.docx` work: exports a
  document through real Microsoft Word (COM automation) to PDF so Claude
  can visually verify formatting the way Word actually renders it, instead
  of relying on LibreOffice's approximation. Requires Word and
  poppler-utils (`pdftoppm`) installed locally; see the "Working approach"
  note above on why LibreOffice alone isn't trusted for this.

## Claude's memory: what's in the repo vs. outside it

Two separate systems hold context across sessions — don't confuse them:

- **This repo (`PROJECT_BRIEF.md`, `RESEARCH_LOG.md`, `RESEARCH_QUESTIONS.md`,
  this file)** is the source of truth for project content: decisions,
  findings, working rules. Git-tracked, versioned, fully visible and
  editable by anyone with the repo, survives independently of any chat
  session. This file (`CLAUDE.md`) is specifically where durable,
  project-relevant working rules belong — Claude should propose additions
  here (for review, not silent edits) when something durable and
  process-level emerges, rather than leaving it stranded in chat history.
- **Claude Code's own cross-session memory** (auto-generated notes about the
  user's preferences, working style, and project context) lives outside
  this repo, at a fixed path tied to the project directory:
  `~/.claude/projects/<project-id>/memory/` (on this machine:
  `C:\Users\ThinkPad\.claude\projects\C--Users-ThinkPad-Documents-grounded-ai-practice\memory\`).
  These are real, plain-text `.md` files — not sandboxed, not hidden —
  readable and editable with any text editor at any time. They are *not*
  git-tracked and are not part of this repo. This is where Claude's
  behavioural/interaction notes about the user live (e.g. "prefers terse
  responses"); it is deliberately kept separate from project documentation
  rather than mirrored into the repo, per the user's decision on
  2026-07-24.

The context window shown in the Claude Code UI for a given session is
dominated by that session's own message history (tool calls, search
results, file reads) — not by these memory/rule files, which are small.
Long research sessions will naturally accumulate a large context window;
this is expected, not a sign that something is being hidden. Starting a
fresh session is reasonable once a research thread's findings have been
written into the repo files above, since nothing durable is lost by doing
so.

**Standing task — periodic rule-extraction pass.** Roughly every ~2 hours
of active work in a session (self-paced, no hard timer — use judgement on
when enough has accumulated), read through the local memory files
(`~/.claude/projects/<project-id>/memory/`) and check each feedback/
project/user-type entry against this file, `PROJECT_BRIEF.md`, and
`RESEARCH_LOG.md`: is the durable, process-level rule it describes already
captured in the repo, or only sitting in local memory? Propose anything
missing (for review, not a silent edit, same as any other change here) and
write in what's approved. This exists specifically because local memory
files are machine-specific and don't travel between machines (desktop vs.
laptop) or reliably resurface from old conversation logs — the repo is the
one place guaranteed to travel with the project. Applies in every session
working in this repo, not just the one that first set this up.
**Last run: 2026-07-27.** Update this line each time the pass completes,
so any session can see how stale it's gotten.
