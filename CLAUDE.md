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
  themselves, explain what it does and why, especially anything security- or
  system-relevant. This is part of the project's own subject matter
  (responsible AI use, verification, human oversight), not just a courtesy.
- Word documents (`.docx`) get a self-check before being treated as
  finished: `tools/word_preview.ps1` exports the file through actual
  Microsoft Word via COM automation to PDF, which Claude then reads
  directly — not a LibreOffice-rendered approximation. LibreOffice's layout
  engine has diverged from Word's real rendering on grouped/shape-based
  content in this project before, so treat a LibreOffice preview as
  provisional, not confirmation that formatting is correct.

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
- When editing `RESEARCH_LOG.md`, preserve the existing entry structure
  (numbered entries, the Source key table with tags, the Open Threads
  section) rather than restructuring it.
- **New standalone files are the last resort, not the default.** Before
  creating one for durable content, check whether it can extend an existing
  file first — most durable detail belongs in `RESEARCH_LOG.md` (as a dated,
  numbered entry) or as a new section in `PROJECT_BRIEF.md`. A new file only
  earns its existence if it's a genuinely distinct, closed category that
  doesn't fit any existing file's purpose — not just because an explanation
  got long.
- **Any new file must be added to this file's "Where to look for what"
  section in the same edit that creates it.** Indexing is not a follow-up
  task — a file left unindexed at the moment it's created is exactly the
  "badly indexed" failure mode this rule exists to prevent (see
  "Relationship to PAWH" in `PROJECT_BRIEF.md`).

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
- `drafts/` — work-in-progress, non-authoritative files under active
  iteration (currently: `Effective_Prompting_Example.docx`, a formatting
  test for the pilot unit's Word-document template — see `RESEARCH_LOG.md`
  Entry 047 and the PAWH semantic-callout construction it's adapting).
  Nothing here reflects a settled decision; contents may be replaced or
  removed once the format stabilises.
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
