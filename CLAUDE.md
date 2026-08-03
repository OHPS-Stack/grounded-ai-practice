# Grounded AI Practice — Claude Code project context

This file is read automatically at the start of every Claude Code session in
this repo. It exists so context built up over many chat sessions doesn't need
re-explaining each time. Keep it updated as the project evolves — treat it as
a living document, not a one-time export.

## What this project is

**Grounded AI Practice** — practical AI capability through responsible,
hands-on learning. Full detail: `project_brief.md`.

**Current stage: research/scoping.** Nothing here is a finished
specification, curriculum, or repo structure. See `research_questions.md` for
the five immediate research priorities driving current work.

## Working approach (from project_brief.md)

- Factual claims must be traceable to sources.

- Evidence, inference, personal observation, and proposal must be clearly
  distinguished — never blur these together.

- Major decisions are made explicitly, not inferred from drafts.

- Structures and rules are introduced only when they solve a demonstrated
  need. **The test is the need, not the timing.** A rule is not suspect
  merely for having been written quickly, and "this was added recently"
  is not by itself evidence that it was premature — judging a rule,
  decision or file by how fast it arrived rather than by what it does is
  not a fair assessment of it. What went wrong in PAWH was governance
  built for problems the project never actually had, carrying more
  machinery than the work required; the defect was fit, not speed. So
  when a rule's value is unclear, ask what would go wrong without it, and
  retire it if the answer is nothing.

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

- **Any bespoke tool built for a task that might need reusing goes in
  `tools/`, not left as a one-off script in a scratch directory.**
  Adopted 2026-07-31. Applies the moment a script does something more
  than a single throwaway check — a real fix, a repeatable transform, a
  self-check with actual logic in it — not only to things explicitly
  planned as reusable in advance; whether it turns out to be reused is
  not knowable ahead of time, and scratch-directory scripts are outside
  the repo entirely and gone once the session's temp files clear.
  Promoting it means: give it a real docstring in the style of the
  existing tools (why it exists, how it works, requirements), a CLI
  rather than only importable functions, and an index entry here in the
  same edit that adds it, per the standing indexing rule below.

- **Every human-run tool gets a GUI as well as a CLI.** Adopted
  2026-08-03 at the creator's direction (see `project_log.md` Entries
  045-047, to follow): the audience the project now aims at — learners and small
  organisations without a terminal habit — is exactly the audience a
  CLI-only tool turns away. The pattern is set by
  `tools/prep_photos.py`: run with no arguments (or `--gui`) the script
  opens a small window; run with any argument it behaves exactly as
  before, so scripts and Claude-driven runs are unaffected. The GUI is
  a thin layer calling the same functions as the CLI — never a second
  implementation — and it exposes only the few decisions a person
  actually makes, leaving the full flag surface on the CLI;
  missing-dependency errors become plain-language dialogs carrying the
  install command. The GUI carries the brand: the GAP palette applied
  through ttk's built-in `clam` theme in the roles `project_brief.md`
  records (Paper ground, Ink text, Stone hints, Ember reserved for the
  primary action), and the wordmark and symbol embedded in the script
  as base64 PNG — the creator's explicit call over runtime asset
  loading, so a copied script keeps its branding; `tools/embed_logo.py`
  generates and refreshes the blobs, and Tk decodes them natively (the
  symbol serves as the window icon, where the 2.7:1 wordmark cannot
  survive). Zero new dependencies: tkinter (standard library)
  for Python tools, WinForms (built into Windows PowerShell) for the
  PowerShell tools. Applies retroactively to the existing tools and to
  every future one — Entry 047 will record the current retrofit status
  (done: `prep_photos`, `trace_reference`, `make_share_folder`; the
  Claude-driven docx/Word pipeline tools pending; `embed_logo`
  proposed as the build-utility exception).

- **Fine visual/spatial refinement gets handed to a real tool, not
  iterated through description.** Early concept exploration (comparing
  directions, testing palettes, rough layouts) works well as an inline
  SVG/widget loop. But once work reaches curve-level refinement, symmetry
  corrections or sub-pixel positioning, proactively suggest handing off to
  a vector editor (Inkscape, Figma, Illustrator) rather than running more
  screenshot-annotate-describe-guess rounds — Claude cannot see a rendered
  result the way someone manipulating the curve directly can. Raise it as
  soon as that level of specificity is needed, not after frustration
  surfaces; this pattern discouraged the creator once during PAWH and
  recurred here. If a hand-edited file comes back, treat it as
  authoritative and re-read it rather than assuming the in-repo copy
  reflects the latest manual edits.

- **Raster concept to editable vector: trace, never redraw.** Adopted
  2026-07-30. Visual concepts are explored in raster tools (Ideogram,
  ChatGPT/DALL-E, Midjourney), where generation is unconstrained by
  Claude's inability to see what it draws, then converted to SVG with
  `tools/trace_reference.py` before hand refinement in Inkscape. The
  script colour-separates the reference, traces each colour through
  Inkscape's potrace engine, applies exact brand palette values, and
  renders the result back to PNG as a self-check.

  This closes a gap the rule above leaves open. That rule says fine
  refinement belongs in a vector editor; it says nothing about how a
  raster concept gets into one. The failure mode it replaces is redrawing
  from visual reference — whether by hand from scratch, or by Claude
  writing SVG blind and iterating on described feedback.

  **A trace is a starting point, never a finished asset.** It reproduces
  its source faithfully, and that includes the irregularities of a
  generated raster: edges that are nearly straight, radii that nearly
  match, symmetry that is nearly exact. Correcting those by hand is a
  required step, not an optional polish pass, before anything is treated
  as final.

- **Final prose in outward-facing documents is the creator's; Claude
  supplies structure and a rough draft.** Adopted 2026-08-01, after
  external review of the UK-climate report found that a fully
  AI-generated register contributed to it reading as abstract and
  over-qualified. The workflow: agree the reasoning and argument
  structure first; Claude produces a rough draft carrying the evidence,
  anchors and citations; the creator writes most of the final prose over
  it. Treat AI-register drafts as raw material, never as candidate
  finals.

- **Infographics are a standing output lane, produced two ways.** Adopted
  2026-08-01 for the publishing funnel (LinkedIn post → profile →
  synopsis document → technical companion → repository). Most viewers
  only ever see the first step, so **every outward graphic carries its
  own source-and-date line on the image** — each element must stand
  alone. Data-driven figures (charts, number comparisons) are produced
  from a script with the data checked into the repo, brand palette
  applied, exported SVG and PNG — reproducible, never hand-drawn numbers;
  the specific charting tool is decided at first build. Bespoke narrative
  graphics go through the existing raster-concept route:
  Ideogram/ChatGPT concept → `tools/trace_reference.py` → Inkscape
  refinement, per the trace rule above. Posting anything externally
  remains a per-item creator decision.

- **Use common PowerShell aliases** (`ls`, `cat`, `cd`) rather than full
  cmdlet names when giving or explaining commands day-to-day. Full
  official names belong in curriculum content that is specifically
  teaching command aliasing — that is the point being taught there, not a
  default for ordinary working sessions.

- **Flag model fit at task boundaries.** When the current model is overkill
  for what is coming (mechanical fetch-and-extract, bulk edits, rendering
  loops), stop and prompt to switch before spending on it. When a task
  would measurably benefit from a stronger model (multi-step reasoning,
  subtle tradeoff analysis, high-stakes prose), say so with the reason.
  Model switching is done by the creator in the app UI, never by Claude.
  One clear flag at the natural boundary — do not nag.

- **Prompt-craft feedback, brief and when earned.** The creator is
  deliberately building prompt-engineering skill, and the pilot unit
  teaches exactly that — so their prompts are legitimate material for
  concrete feedback. When a prompt's construction materially shaped the
  outcome — an ambiguity that forced a guess, a request buried
  mid-paragraph that nearly got missed, an explicit scope/budget
  statement that let the work be planned properly — say so in a sentence
  or two at a natural point in the reply, tied to that specific prompt.
  Not every prompt, no scores, no padded praise, and never withhold a
  real defect to be polite. When a prompt or its failure mode would make
  good teaching material for the prompting curriculum, flag it as
  candidate raw material, redaction needs included.

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
  to the task in front of you, not as a scattershot list. The
  surface-level version of this — Claude Code vs. the claude.ai app's
  other tools — has its own section below.

## Choosing the right Claude surface

Adopted 2026-08-01. This project was built entirely in Claude Code, and
the habit that came with it — treat Claude Code as *the* workspace and
solve everything inside it — is now a limitation rather than a
simplification. Claude Code, and the claude.ai app's Projects, Research,
Cowork and Design, are separate surfaces on one subscription with
genuinely different strengths.

**The standing rule: route the request, don't absorb it.** When a request
would be materially better served on another surface, say so before
starting — which surface, why, and what moving it costs. Same discipline
as the model-fit flag above: one clear flag at the natural boundary, no
nagging. Staying in Claude Code is often the right answer; the point is
that it becomes a decision rather than an assumption.

- **Research** — breadth-first source discovery on a
  `research_questions.md` priority, and the adversarial verification
  passes this project has deferred. It runs many searches over minutes
  and returns a cited report. **Its output is a lead list, not
  evidence.** Every claim still earns its `research_log.md` entry through
  the normal source-scope and interest-type check, exactly as a vendor
  source would.

- **Cowork** — multi-step work over files that does not need the local
  toolchain: reorganising notes, drafting from a folder of sources,
  synthesis across many documents. Same agentic architecture as Claude
  Code, without the terminal.

- **Design** — visual concept exploration, one-pagers, decks. It does
  **not** supersede the raster-concept-to-vector rule above: anything
  becoming a repo asset still goes through `tools/trace_reference.py` and
  Inkscape. Treat Design output exactly as an Ideogram concept — a
  starting point, never a finished asset.

- **Projects** — persistent instructions and repo context for ordinary
  chat, on any device. Best for thinking, reviewing and asking questions
  about the project away from the desk.

- **Claude Code** — anything touching the local toolchain, git, or
  tracked files. Specifically and non-negotiably: the `.docx` pipeline
  (`word_preview.ps1` and `word_roundtrip_test.ps1` drive real local Word
  through COM; `fitshapes.py` measures the locally installed Public Sans
  faces), `trace_reference.py` (local Inkscape), every git operation, and
  every edit to a tracked file. Document work is the trap here — it looks
  like Cowork's territory, but the self-checks that make it trustworthy
  only exist on this machine.

**Continuity: the repo is the source of truth, and syncing is manual.** A
Project's GitHub context is a point-in-time copy of file contents on a
branch — no commit history, no uncommitted work — and it refreshes only
when someone clicks "Sync now". So work done in Claude Code is invisible
to every other surface until it is committed, pushed, *and* re-synced.
Before starting substantial work on another surface, check the repo is
pushed and say so if it is not; after finishing a stretch in Claude Code,
flag that a re-sync is needed. Anything durable produced elsewhere comes
back here and lands in the repo files under the usual rules — the repo
travels with the project, a chat session does not.

**Never grant a remote surface access to the repo root.** `internal/` and
the `.claude-memory` junction both sit inside
`C:\dev\grounded-ai-practice`, and Cowork processes work on Anthropic's
servers rather than locally by default. Pointing it at the project folder
would send exactly the material the public/internal split exists to keep
out of circulation. Grant access to a specific subfolder — `drafts/`,
`exports/` — or to a copy made for the purpose, never the root. Note that
`.gitignore` and the pre-commit hook do nothing here: they guard commits,
not file access, so this rule has no enforcement layer behind it.

## Research discipline

Full detail and current status: `research_log.md` (source key, log entries,
open threads). Key standing rules:

- **Source scope:** prefer official/government sources (gov.uk, ONS,
  Parliament), independent academic sources, and established international
  bodies. Vendor/commercial and advocacy sources are deprioritised, not
  banned — useful for spotting a claim worth checking, not as standalone
  evidence for anything scope-defining. Tag every new source's interest
  type (Independent/Academic, Government/Official, Vendor/Commercial,
  Advocacy/Membership body) in the Source key table.

- **Spoken sources are located by transcript and quoted only after
  verification.** Adopted 2026-08-01. An automatic transcript — YouTube
  ASR, Whisper, a platform's own captions — may be used to *find* a claim
  and its timestamp. It is never the text of a quotation. Any passage
  quoted in a deliverable must be confirmed against the recording itself,
  and cited with speaker, event, date and timestamp. Tag auto-generated
  transcripts as such in the source key, and treat any claim resting on
  one alone as unverified until heard.

  The reason is specific rather than fussy: ASR mis-renders exactly what
  this project cites. The London Tech Week transcript alone produced
  "train 7.5 million workers in a by 2030", "extra1 billion pounds",
  "Kia" for the Prime Minister's name and "Zalinski" for President
  Zelensky. A figure quoted straight out of that would have been wrong in
  print, in a report whose entire argument is that other people's figures
  do not survive checking.

  **Prepared remarks are not the whole event.** Where a department
  publishes a transcript, check what it covers before calling it the
  record — gov.uk's page for that speech carries the ~18-minute prepared
  remarks and not the ~26-minute unscripted conversation that followed
  (`research_log.md` Entry 063). Publishing the prepared portion is
  ordinary practice, not concealment, but the unscripted portion is where
  a speaker departs from the brief, so it is usually the more revealing
  half and it will not be in the official text.

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
  vs-declining conflict between sources. Check `research_log.md`'s Open
  Threads section before assuming something hasn't been investigated yet.

- **Don't chase every open thread every session.** Check in on direction
  before spending significant effort, especially for anything that would
  use a lot of tokens/time.

### Bias self-check (adopted 2026-07-29)

Grounded in `[NIST-1270]` — `research_log.md` Entry 050 holds the evidence
and, importantly, its limits. One finding shaped the design of this list:
NIST states that human biases are largely implicit and that "simply
increasing awareness of bias does not ensure control over it." So this is
deliberately **not** a set of biases to keep in mind. It is five triggers
attached to specific moments, three of which only name practice this
project already had.

1. **Foundational claim → pair it.** Before a claim that would change
   project direction, search for what would disconfirm it, not only what
   supports it. Already the rule above; NIST's name for the pattern is
   *effective challenge*.

2. **AI output that supports the thesis → apply the reversal test.** Ask
   whether it would have survived the same scrutiny had it concluded the
   opposite. NIST's term is *selective adherence* — selectively adopting
   algorithmic advice that matches pre-existing belief. `research_log.md`
   Entry 013 caught the input-side version of this (framing queries to
   find support); this covers the output side, which nothing previously
   did.

3. **A source couldn't be retrieved → record the hole, and say which
   kind of hole it is.** A source that 403s or sits behind a login
   doesn't become absent from the evidence base, it becomes invisible in
   it. Log it as unfetched rather than letting the reachable evidence
   quietly stand in for all of it. NIST: *streetlight effect*, searching
   only where it is easiest to look.

   **Sharpened 2026-07-31:** distinguish *could not be obtained* from
   *nobody has looked yet*. They carry very different weight, and any
   wording that blurs them will be read as the stronger of the two. The
   OSR letter sat in this log and in a drafted report as "has not been
   read directly" — which reads as unavailable — when it was published
   on the regulator's own website the whole time, and its contents did
   not support what had been attributed to it (`research_log.md` Entry
   059). This is a sharpening of an existing trigger, not a sixth item;
   the list stays at five.

4. **Argument rests on numbers → say what isn't counted.** State once, in
   the text, what the figures do not capture. NIST: *McNamara fallacy*,
   the belief that quantitative information is inherently more valuable
   than other information. Directly live for the UK climate report, whose
   argument is built on published figures.

5. **Nothing becomes canonical unchecked.** Every AI-produced output gets
   a human read before it lands as project fact — a rule, a log entry, a
   claim in a deliverable. The human can be the creator; the point is not
   independence but that no unreviewed output is allowed to set itself
   as canonical and then be built on by later work. Unchecked material
   compounds quietly, which is the risk this addresses.

   Independent review is a **second, less frequent thing**: a different
   model or an outside reader, at occasional intervals and on completion
   of any substantial deliverable. That is where NIST's warning applies,
   that those being assessed "may have undue influence on building or
   using the assessment." Valuable, but not the every-output check —
   don't conflate the two, and don't let the rarer one become an excuse
   to skip the routine one.

**Do not grow this list.** NIST also found that surfacing bias information
downstream "does not always result in a directly positive outcome, and can
in fact create the opposite" — so on the evidence a longer checklist here
is a worse one, not merely a heavier one. That is the specific reason to
hold this list at five, rather than a general preference for fewer rules.
Add an item only when a real defect gets through that no existing item
would have caught, and say in the log what that defect was.

**What this list does not claim.** NIST gives no effect sizes for any of
its recommended mitigations, and whether structured practices like these
change behaviour better than awareness alone is genuinely unsettled — see
the Priority 4 open threads. Treat these as reasoned working practice, not
as demonstrated to work.

## File conventions

- **Files intended to directly replace a previous version keep the exact
  same filename — no version suffixes** (no `_v2`, `_final`, `_updated`).
  This project relies on git for version history, not filename suffixes.

- Markdown is the default format for research/reference documents, matching
  the existing project files.

- **Every list item is separated by a blank line.** Adopted 2026-07-29
  and applied across every markdown file in the repo. The older
  convention ran items straight on from one another, which turned any
  list of more than two or three into a single indistinguishable wall of
  text. The rule is unconditional: a blank line before every `- ` and
  every `1.` item, short ones included, at every nesting level.
  Consistency is the point — a rule with a length threshold, or one
  covering bullets but not numbered lists, produces lists that are spaced
  in some places and not others, which reads worse than either style
  applied throughout.

- **Avoid dense blocks generally.** The same instinct applies beyond
  lists: split long unbroken paragraphs, and treat a paragraph that has
  grown past a screenful as a sign the content wants a subheading or a
  list rather than more sentences.

- When editing `research_log.md` or `project_log.md`, preserve the existing
  entry structure (numbered entries, the field shape each uses) rather than
  restructuring it.

- **`research_log.md` is for source-backed research findings only** —
  a dated, numbered entry answering a `research_questions.md` priority,
  with a citable source. **`project_log.md` is for everything else durable
  that isn't research** — scoping/creative decisions, design/production
  work, technical build notes — also as dated, numbered entries, but
  without a research citation. **`project_brief.md` holds the current,
  standing state** of a decision, not its history (that's `project_log.md`'s
  job). Getting this wrong is not hypothetical: `research_log.md` drifted
  into a mixed dump of both for a while, which produced a real numbering
  collision (two unrelated tracks each independently numbering entries
  039-042) before the two were split apart on 2026-07-27 — see
  `project_log.md` Entry 017.

- **Log entries earn their length.** Adopted 2026-07-29. An entry states
  what was found or decided, the evidence or reasoning behind it, and what
  changes as a result — then stops. Detail that belongs in the thing
  produced (a document, a rule in this file, an asset) lives there and is
  referenced, not restated in the log. Length is earned by consequence,
  not by effort spent. This governs **new** entries only: existing ones
  are not condensed retroactively (see "Amending existing content"), and
  where an old stretch of log is hard to navigate the fix is the index or
  the Open Threads section, not the entry.

- **Tracked log entries record decisions and reasoning, never verbatim
  planning/pitch language.** Adopted 2026-08-03. Noting that a framing
  was considered and screened out displays the self-checking and is
  fine; reproducing its wording publishes planning sentiment the record
  does not need. The prompting case: a rejected marketing-register
  claim was drafted into `project_log.md` Entry 044 as a verbatim quote
  and caught at review — the landed entry keeps a quoteless screening
  note instead. State what was considered and why it was kept or
  discarded; quote-level candour lives in `internal/`.

- **Lessons learned become learning content, not only rules.** Adopted
  2026-07-29. When a mistake or hard-won lesson here would be a genuine
  pitfall for someone in a similar position — a solo practitioner
  building real AI capability without an institution behind them — it has
  two destinations rather than one: the working rule that prevents a
  recurrence (this file), and candidate raw material for the project's
  actual teaching output. Flag the second at the moment the first is
  written, while the specifics are still fresh, noting anything that
  would need redacting. Do this alongside the relevant research pass, so
  the lesson arrives with evidence attached rather than as unsupported
  anecdote — the project's own experience is testimony (n=1), and the
  `research_log.md` Entry 049 precedent is how that gets handled honestly.

- **New standalone files beyond these three are the last resort, not the
  default.** Before creating one for durable content, check whether it can
  extend an existing file first. A new file only earns its existence if
  it's a genuinely distinct, closed category that doesn't fit any existing
  file's purpose — not just because an explanation got long.

- **Any new file must be added to this file's "Where to look for what"
  section in the same edit that creates it.** Indexing is not a follow-up
  task — a file left unindexed at the moment it's created is exactly the
  "badly indexed" failure mode this rule exists to prevent (see
  "Relationship to PAWH" in `project_brief.md`).

- **Avoid jargon/buzzwords in naming or reader-facing copy** (unit titles,
  headings, capability names) — plain, concrete wording beats a clever
  abstract phrase. The fix for jargon is plainer language, not a simpler
  underlying idea — the working assumption is a fairly intelligent reader,
  so don't swing into patronising oversimplification either.

- **In published prose, state strong facts flatly and let them imply the
  conclusion.** Present the facts, withhold the adjective, and close with a
  short sentence that points at the gap without naming it. The reader draws
  the conclusion and finds it more convincing for having done so, and there
  is no characterisation to argue with — only facts. Worked example the
  creator singled out, from the UK AI climate report: *"...1,700 skills
  course completions and 126 accreditations, against £74.6 million
  allocated from a £100 million budget. Both sets of numbers are published
  by the government. Neither appears next to the other."* This is not only
  a style preference: understatement matches the project's evidential
  discipline, and overclaiming would undercut the same document's careful
  source-tagging. Only use it where the facts genuinely carry it — if a
  point needs an intensifier to land, the fix is better evidence, not
  louder prose. Avoid the opposite register ("shockingly, the government
  has completely failed to...") which tells the reader what to think and
  invites argument with the characterisation rather than the facts.

- **SVG/vector asset groups (`<g>` elements) should carry clear snake_case
  labels** (`id` and/or `inkscape:label`) so a human can find the right
  group to edit without guessing. Individual leaf `<path>` elements don't
  need their own names — that effort doesn't pay for itself. Never rename
  an *existing* id without first checking nothing references it (gradient
  `url(#...)`, `xlink:href`, `clip-path`) — only add labels to currently
  unlabelled groups unless there's a specific reason to touch a working one.

## Amending existing content

Adopted 2026-07-29. The project is open by design, but openness must not
come at the expense of the integrity of its record. These are not the
same value and they occasionally pull against each other; this section
is how that conflict gets resolved. Three tiers, by what the content is
*for*:

**1. Living / current-state content — amend freely.** `README.md`, this
file, `project_brief.md`, `research_log.md`'s Open Threads section and
source-key status notes. Their job is to state what is true *now*, so
editing them to match current reality is not rewriting history — it is
the whole point. Stale content here is the defect, not the fix.

Corollary, added 2026-07-29 after getting it wrong once: **state the
current position, don't narrate how it changed.** A current-state
document that says "this reverses the earlier decision recorded here"
is doing the log's job badly. Where a change is inconsequential to the
project's integrity — a preference updated, a direction refined — just
smooth it over and let `project_log.md` hold the history. Reserve
visible supersession notes for changes a reader would be misled without
(a retracted claim, a withdrawn recommendation).

**2. Dated log entries — append-only in spirit.** Entries in
`research_log.md` and `project_log.md` record what was known, decided or
believed on a given date. They are only worth citing because they do not
quietly change. So:

- Correct an error with a **new dated entry that supersedes** the old
  one, or a **clearly marked, dated correction note inside** the
  original. The established pattern is `research_log.md` Entries 033
  (retraction) and 046 (deliberate revival with the reasoning shown).

- **Never silently rewrite an entry** to make the record look tidier,
  more consistent, or more flattering than it was. Anyone doing
  diligence can read the git history; a log found to have been quietly
  edited costs more credibility than any awkward entry ever could.

- Historical references to deleted files, retracted framings and
  superseded decisions **stay**. `project_log.md` Entry 024 already
  settled this for file deletions: current-state documents get
  corrected, historical logs do not.

- **Minimal edits for clarity and correctness are allowed** (creator
  decision, 2026-07-29, relaxing the original rule which permitted only
  broken cross-references). An old entry may be edited in place to fix a
  broken cross-reference, a typo, a misspelled name, a mistranscribed
  figure, or a sentence whose wording obscures what it was trying to
  say.

  **The test:** does the edit change what the entry *claimed, decided or
  knew at its date*? If not, edit it and say nothing — the change
  corrects the expression, not the record. If it does — including when
  the original claim was simply wrong — that is a correction of record
  and takes a dated note or a superseding entry, as above. A wrong claim
  is never quietly fixed; an unclear sentence always can be.

  Two things this does **not** license. Condensing an entry because the
  log feels long: length is a navigation problem, so fix the index or
  the going-forward entry format instead (see "Log entries earn their
  length" below). And smoothing wording that reads awkwardly because the
  thinking at the time *was* awkward — that awkwardness is the record,
  and it is often the most useful thing in it.

**3. Compromising content — remove promptly, mark that you did.** If
something in a tracked file should never have been public — a private
individual, a candid assessment, a credential — take it out of the
current file straight away and leave a dated marker saying material was
removed and why, without restating it. Then handle git history under the
"Retroactive rule" in "Public repo vs. internal working files": anything
ever committed is already public in practice, rewriting history is
disruptive and unreliable once a repo has been shared, and it is a
creator decision per item — **never unilateral.**

**The distinction to hold onto:** amending for *privacy* (tier 3) and
amending for *currency* (tier 1) are legitimate and expected. Amending
for *appearance* is not, and a correction-of-record (tier 2) is done in
the open or not at all.

## Word document conventions

Applies to all `.docx` work in this project — currently
`exports/Style_Reference_Example.docx` (the canonical reference) and
`drafts/UK_AI_Skills_Ambition_Report.docx`, plus any future Word
deliverable built the same way. Established 2026-07-27 during the
style-reference review.

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

- **Prose revisions go through `tools/docx_edit.py`, not through pasting
  into Word.** Pasting strips a paragraph's named style and injects
  non-breaking spaces. Found 2026-07-31, when a pasted revision cost §1 of
  the UK-climate report its `Heading1` style — and with it the outline
  level the rule above exists to guarantee, so the section silently
  dropped out of the navigation pane and any TOC — and put 252
  non-breaking spaces into five paragraphs. Word cannot break a line at a
  non-breaking space, so it broke mid-word instead ("throu / ghout"), and
  in one callout the text overflowed its shape and clipped. `fitshapes.py`
  cannot prevent that: it measures assuming normal word wrapping, and its
  height was correct for that assumption. **None of it was visible in the
  document's text.** `docx_text.py` reported the words as correct, because
  they were; only the render disagreed. So this is also the case for
  running `word_preview.ps1` and *looking at the pages* after any hand
  edit, not only after a construction step.

- **Callout cards use small/medium/large size presets**, each fixing the
  icon-well size; a card's width (and therefore its text column) is always
  a free parameter independent of preset, so resizing a card for its
  content never stretches or squeezes the icon. Built as a Word group
  (`wpg:wgp`) of sibling shapes, not nested shapes — see `project_log.md`
  Entry 015 for why (Word rejects a shape nested inside another shape's
  text box) and the rest of the construction.

- **Card and quote height must fit the text inside, not be set once at
  construction time.** A `wpg:wgp` group's height is a static number in
  its XML; nothing in Word recomputes it when the text is edited, so a
  card built for two lines and later filled with eight keeps the two-line
  box and reads as badly over-padded — found 2026-07-31 across every
  callout in a drafted report, and to a lesser extent in two of the six
  groups in the style reference itself. Use `tools/fitshapes.py` after
  writing or editing a card or quote's text, never hand-picked heights.

- **A `.docx` produced by string-substituting into an existing card or
  quote template inherits that template's height regardless of how much
  the new text differs from the original** — this is exactly the failure
  mode the rule above exists for, and it is the ordinary way these get
  built (see `tools/fitshapes.py`'s docstring for how the bug was found).
  Run the fitter as a matter of course whenever a template like this is
  reused, not only when padding looks visibly wrong.

- **`settings.xml` MUST declare `compatibilityMode` 15.** Non-negotiable
  for any document using shapes. Without it Word assumes compatibility
  mode 12 (Word 2007), which predates the DrawingML shape extensions
  (`wps`/`wpg`, Word 2010+) every callout card and pull quote in this
  project depends on. Word will *read* and *render* such a document
  perfectly, then on save silently downgrade the shape groups to legacy
  VML — which fails with "You can't put drawing objects into a text box,
  callout, comment, footnote or endnote" and flattens the cards into
  uneditable blobs. Discovered 2026-07-28 after it had already degraded
  `AI_Skills_Hub_Briefing.docx` in place. The required block:
  `<w:compat><w:compatSetting w:name="compatibilityMode"
  w:uri="http://schemas.microsoft.com/office/word" w:val="15"/></w:compat>`

- **Rendering is not the same check as saving.** `tools/word_preview.ps1`
  proves a document *looks* right; it opens read-only and can never catch
  a save-path defect. `tools/word_roundtrip_test.ps1` opens, saves and
  closes through real Word to prove the document is actually *editable*.
  Run both on any new document construction — the compatibilityMode bug
  above passed every rendering check for three documents running.

- **Content icons have genuinely different aspect ratios** (`outcomes` is
  90×56, `verification` is 90×90) and roughly 30% transparent padding.
  Sizing them to a uniform square box makes the wide ones render short and
  illegible. For icons inline with text, crop to the content bounding box
  and size by **height** so every icon shares a consistent visual height,
  letting width follow the glyph. Inline images sit on the text baseline,
  so also apply a small negative `<w:position>` (about -4 half-points at
  13pt) to centre the icon on the cap height rather than leaving it
  sitting low.

- **Vertical accent/divider bars are pill-shaped** — a narrow `roundRect`
  with `<a:gd name="adj" fmla="val 50000"/>` (50% corner radius relative to
  the shape's short side, which fully rounds a narrow bar into a capsule),
  not a paragraph-border line (`w:pBdr`), which can only draw a straight
  edge. Used for the callout-card divider and the pull-quote rule.

## Public repo vs. internal working files

**This repository is intended to become publicly visible** and to be shown
to prospective employers, collaborators, funders and interviewees as proof
of work. Treat every tracked file as already public. Established
2026-07-28, when the repo moved from local-only toward selective sharing.

### The rule

**Default: public.** Anything tracked by git is public. If content is not
fit for a stranger — or for the person it describes — to read, it does not
go in a tracked file.

**Exception: `internal/`.** Gitignored, hook-blocked, never committed.
This is the only place the following belong:

- Named private individuals, personal connections, and anything about a
  relationship that person has not consented to being published.

- Candid assessments of named organisations or people, especially
  prospective funders, partners or interviewees.

- Political opinions and motive readings about identifiable actors.

- Funding approach strategy and tactical positioning.

- Anything whose disclosure would embarrass the project or its subjects.

**The pointer pattern.** Tracked files may record *that* an internal
position exists, what its evidential status is, and where the evidenced
part sits — without reproducing the wording. This preserves the project's
evidence-vs-opinion discipline without publishing material that damages
its own aims. Worked examples: `research_log.md` Entry 046 and
`project_brief.md`'s "Longer-term direction and positioning".

**Contacts and funding are internal.** The register of people and bodies
worth approaching, and routes to funding or support, lives under
`internal/` — originally written public-safe and tracked, then moved on
2026-07-28, the creator's judgement being that a register of named
people one might approach for money reads differently in public than a
research log does, however carefully worded. Its standing rule travels
with it: **no approach is made without the creator's explicit
per-approach instruction**.

**Internal files are indexed inside `internal/`, not here.** Internal
strategy and planning material that could be compromising is not
indexed, named or described in tracked files unless explicitly required
— a filename plus a one-line description can disclose a relationship on
their own. `internal/README.md` is that directory's own index and
carries the same add-in-the-same-edit discipline this file requires for
tracked files. Where a tracked file genuinely needs to record that an
internal position exists, use the pointer pattern above without naming
the sensitive party. Decided by the creator 2026-07-28.

### Enforcement, and its honest limits

Two layers:

1. `.gitignore` excludes `internal/`.

2. `.githooks/pre-commit` **blocks** commits that stage anything under
   `internal/` or that contain a private marker, and `.githooks/pre-push`
   re-scans the whole tracked tree and the pushed commits at push time.
   Both read the marker list from `internal/private_markers.txt` — never
   tracked, so the public hooks carry no private strings, and a machine
   without that file refuses to commit or push until it exists (an empty
   file is a valid, deliberate choice). Install once per machine:
   `git config core.hooksPath .githooks`

Both are guardrails against accident, **not security controls**:

- `.gitignore` does nothing retroactively and is overridden by `git add -f`.

- The hooks are local-only (cloning does not install them) and are
  bypassed by `--no-verify`.

- **Neither protects git history.** Anything ever committed is public the
  moment the repo is made public, whether or not it was later deleted.

The practical consequence: the audit below matters more than the tooling.

### Repo audit — scheduled, not ad hoc

Run **before any change in who can see the repo** (making it public,
sharing with a new person, attaching it to an application), and otherwise
**monthly** while the repo is shared.

Three passes, in order, because they catch different things:

1. **Claude pass.** Scan tracked files and full git history for: named
   private individuals; candid assessments of named parties; unlabelled
   opinion presented as evidence; personal contact details; credentials or
   tokens; dangling references to files readers cannot see (e.g.
   `[[wiki-links]]` to local memory); stale claims contradicted by later
   entries. Report findings; do not silently rewrite.

2. **ChatGPT pass (or another model).** Same brief, run independently by
   the creator. Different models miss different things, and a second
   opinion on "would this embarrass you" is worth more than a second run
   of the same model. This has already proven its value once — the
   external review of the AI Skills Hub briefing surfaced real defects
   (`project_log.md` Entry 019).

3. **Human verification — required, not optional.** The creator decides on
   every flagged item. Neither model decides what is safe to publish.
   Judgement calls about reputation, relationships and political framing
   are the creator's alone.

Record each audit's date and outcome in `project_log.md`. **Last audit:
2026-07-28** (initial; found the pre-sharing content issues fixed the same
day, history clean across 15 commits).

### Retroactive rule

Because history is permanent, **anything already committed is already
public** for practical purposes. If an audit finds something damaging in
history, rewriting history is possible but disruptive and unreliable once
a repo has been shared — raise it with the creator as a decision, do not
attempt it unilaterally.

## Git conventions

- **Every commit and push gets a review gate.** Adopted 2026-08-03,
  after a pre-commit review found the hook itself carrying in public
  the private name it exists to block. Before preparing any commit,
  review the full set of changes for: private names or markers,
  personal contact details, credentials, candid assessments of named
  parties, dangling cross-references, and claims contradicted by later
  log entries — and report findings for decision rather than silently
  fixing them. The hooks enforce the mechanical part (`internal/`
  staging, the marker list in `internal/private_markers.txt`); this
  review is the judgement part. Neither replaces the scheduled repo
  audit, which also covers history.

- **Draft the commit message and show it to the user before running
  `git commit`**, for any commit with a real message to write (not a
  one-liner the user dictated directly). A go-ahead like "let's commit
  this" means prepare it, not execute it unreviewed — commits are
  semi-permanent and this repo may go public.

- **Match message length to the size of the change.** Routine and
  maintenance commits (renames, cleanups, single fixes, asset
  regeneration) get a one-line title and nothing more, matching the
  existing log — "Removed superseded drafts", "Added document self-check
  tooling". Reserve a multi-paragraph body for genuine milestones: a new
  deliverable, a structural change to the repo, or a decision worth
  reading later. Defaulting to the long form on every commit buries the
  commits that actually matter.

- **Never push to the remote without a separate, explicit go-ahead**, even
  immediately after a local commit the user asked for. The user handles
  pushes themselves.

- **Commit messages (and any other outward-facing prose — docs, summaries)
  must match the user's own voice**: short, direct, no AI-register
  em-dash-chaining, and never third-person references to the user (e.g.
  "the creator") — that framing belongs in `research_log.md`'s internal
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

- `project_brief.md` — problem statement, scope, what's decided vs. open
  (including the "Visual identity" working decisions: palette, logo type,
  tone).

- `research_questions.md` — the ten priority areas and their questions.

- `research_log.md` — source key (with interest-type tags), dated log
  entries, and the Open Threads list showing what's resolved vs. still open.
  Research findings only — see "File conventions" above for the boundary
  with `project_log.md`.

- `project_log.md` — dated log of scoping/creative decisions and design/
  production/technical work (visual identity history, icon/logo production
  notes, Word-document engineering notes, this file's own split from
  `research_log.md`). The chronological history behind what
  `project_brief.md` currently reflects.

- `README.md` — the repository's public front door, written for a reader
  who may be a prospective employer, collaborator or funder. Explains what
  the project is, why the repo is public, the four research rules, and
  where to look. Keep it current when structure changes — it is the first
  and often only thing a visitor reads.

- `internal/` — **gitignored, never committed.** Private contacts,
  candid assessments, funding strategy, political reads, third-party
  reference material. Indexed by its own `internal/README.md`, not
  here — see "Public repo vs. internal working files" above for what
  belongs in it, why, and the indexing rule.

- `.githooks/` — the local guard layer: `pre-commit` blocks commits
  staging `internal/` or containing a private marker; `pre-push`
  re-scans the whole tracked tree and the pushed commits before
  anything leaves the machine. Both read their marker list from
  `internal/private_markers.txt` (never tracked; a missing file blocks,
  an empty one is a deliberate opt-out). Install per machine with
  `git config core.hooksPath .githooks`. Guardrails against accident,
  not security controls.

- `assets/icons/` — the promoted, working content-icon set (36
  icons, current palette). `svg/` for sources, `png/` for 64/128/256px
  exports, `README.md` for the filename→topic manifest.

- `assets/logo/` — the finished logo system. The lead identity is the
  stylised "GAP" wordmark: `logo_wordmark.svg` (Ink letterforms, Ember
  marking the A's two counters), plus `logo_wordmark_mono.svg` (single
  Ink) and `logo_wordmark_reversed.svg` (white letterforms, Ember
  retained, transparent ground). Concepted in Ideogram, traced with
  `tools/trace_reference.py`, refined by hand in Inkscape — production
  history in `project_log.md` Entries 036–037. Two things to know before
  editing it: the master holds a hidden Public Sans reference glyph
  (`a_overlay`, `display:none`) that is **deliberate, not leftover**, and
  minimum usable width is about 160px, below which the A's crossbar
  closes up. Source concepts are `png/gap_reference_1.png` and `_2.png`.
  Wordmark avatars: `profile_picture_square_wordmark` and
  `profile_picture_circular_wordmark` (+ `_inverted`/`_mono` for each),
  built at 84%/80% of a 1024 canvas with an edge-flush border. They hold
  to roughly 64px; below that use the symbol-based avatars instead, since
  a 2.7:1 mark cannot survive a 32px favicon.

  The symbol system below is **supporting rather than primary**, and all
  of it remains valid and in use, nothing deprecated:
  `logo_symbol.svg` (default, shaded), `logo_symbol_flat.svg`,
  `_mono`/`_reversed` symbol variants, and `logo_lockup_horizontal`/
  `logo_lockup_vertical` (+ `_mono`/`_reversed`) icon+wordmark lockups, all
  with wordmark text as real vector paths (Public Sans) and a two-tone
  colour hierarchy, plus `profile_picture_square`/`profile_picture_circular`
  avatar derivatives, plus `png/` exports for all of them. See
  `project_brief.md` "Visual identity" for the full picture.

- `assets/logo/creative_brief.md` — portable creative brief for
  external logo-generation workflows (not a project research/decision
  document itself).

- `drafts/` — work-in-progress files under active iteration. Currently:
  `UK_AI_Skills_Ambition_Report.docx` (+ self-check `.pdf`), an 8-page
  report on the UK's AI skills ambition, delivered results and the gap
  between them — built 2026-07-28 on `research_log.md` Entries 043–048.
  Externally reviewed and reframed 2026-08-01: the draft is demoted to
  evidence companion behind a planned short public-audience report — see
  `project_log.md` Entries 042–043 for the review findings and decisions.
  Nothing here reflects a settled decision; contents may be replaced or
  removed once the format stabilises. Once a document is approved and no
  longer a draft, it moves to `exports/` instead.
  **Removed 2026-07-28** as superseded: `Effective_Prompting_Example.docx`
  (the original Word-template formatting test, superseded by the approved
  style reference) and `AI_Skills_Hub_Briefing.docx` (whose argument and
  research were absorbed into the wider UK-climate report). Their
  construction history remains in `project_log.md` Entries 015 and 019 —
  those entries are historical records and are deliberately **not**
  rewritten to hide that the files once existed.

- `exports/` — finished, current production exports, promoted out of
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
  `project_log.md` Entry 016) — still subject to later refinement, but no
  longer a first draft**; the "Word document conventions" section above is
  the extracted rule set. Its callout cards and pull quote were refitted
  to their text content 2026-07-31 (see `tools/fitshapes.py` and the card/
  quote height rule above) and re-approved on that basis — see
  `project_log.md` Entry 039. Icon set inconsistencies (padding, mismatched
  speech-bubble styles across icons) are the one explicitly open exception
  — separately deferred, creator revisiting the icon set directly in
  Inkscape.

- `tools/word_roundtrip_test.ps1` — the **second** `.docx` self-check:
  opens a document in real Word, saves it, closes it, and reports whether
  the save succeeded. Catches defects `word_preview.ps1` structurally
  cannot, because that one opens read-only. Written 2026-07-28 after a
  document rendered perfectly but could not be saved (see the
  `compatibilityMode` rule above). Always run it against a throwaway copy
   — it saves in place. Same Word-process safety guard as the preview tool.

- `tools/word_preview.ps1` — self-check step for `.docx` work: exports a
  document through real Microsoft Word (COM automation) to PDF so Claude
  can visually verify formatting the way Word actually renders it, instead
  of relying on LibreOffice's approximation. Requires Word and
  poppler-utils (`pdftoppm`) installed locally; see the "Working approach"
  note above on why LibreOffice alone isn't trusted for this.

- `tools/trace_reference.py` — converts a flat raster reference (an
  Ideogram or DALL-E concept, a photographed sketch) into a
  colour-separated, labelled SVG ready for hand refinement in Inkscape.
  Auto-detects the reference's colours and snaps them to the brand
  palette, or takes explicit `--colors` and `--labels`. Traces through
  Inkscape's potrace engine, then renders the result back to PNG as a
  self-check. Requires Python with Pillow (`pip install pillow`) and
  Inkscape 1.x, both discovered automatically. See "Raster concept to
  editable vector" under Working approach for when to reach for it, and
  why its output is never a finished asset. Run with no arguments (or
  `--gui`) for the windowed interface — pick the image, preview the
  colour separation, trace — per the GUI rule under Working approach.

- `tools/fitshapes.py` — fits a `.docx`'s callout-card and pull-quote
  drawing groups to the text they actually contain. These are Word groups
  (`wpg:wgp`) built with a fixed height at construction time; nothing
  recomputes that height when the text is edited, so cards and quotes
  drift out of proportion with their content — found 2026-07-31 across
  every callout in a drafted report. Measures real Public Sans metrics
  (actual glyph widths, real wrapping at the text box's actual width) and
  recentres the icon, divider bar and text box to fit, without touching
  width. Takes a `.docx` in and writes a `.docx` out — `--in-place` to
  overwrite, or a destination path. Requires Python with Pillow and the
  Public Sans TTF faces installed as system fonts. **Does not verify its
  own output** — always run `word_preview.ps1` and
  `word_roundtrip_test.ps1` after, same as any other document construction
  step.

- `tools/docx_text.py` — extracts a `.docx`'s readable text, including the
  text inside callout cards and pull quotes, which are drawing shapes
  rather than body text and so are missed by anything reading only
  paragraphs. For diffing one revision against the last, grepping for a
  phrase, quoting into a log entry, or handing a section out for a wording
  pass. Complements rather than duplicates `word_preview.ps1`: that one
  answers "does it render correctly", this one answers "what does it say",
  and needs no Word process to do it. Marks and numbers shape text boxes
  as it goes, since editing text inside one means `fitshapes.py` has to be
  re-run over the document afterwards. Drops Word's `<mc:Fallback>`
  duplicate of every shape and any `<w:del>` tracked-deletion — without
  that, every card and quote is reported twice and deleted text reads as
  though it were still present. `--styles` labels each paragraph with its
  Word style (useful for checking heading structure), `--no-shapes` gives
  body text only, `-o` writes to a file. Requires Python, standard library
  only — no Pillow, no Word, no Inkscape. Reads `word/document.xml` only:
  headers, footers, footnotes and comments live in separate parts and are
  not extracted.

- `tools/docx_edit.py` — the editing counterpart to `docx_text.py`. Applies
  a JSON list of find/replace operations to a `.docx`, reaching text inside
  callout cards and pull quotes as well as body paragraphs and table cells,
  and matching across split runs so a sentence Word has fragmented into five
  `<w:r>` elements is still found. A `clone` operation copies a paragraph —
  or a whole drawing group — and inserts it elsewhere with its text
  substituted, which is how a new pull quote gets added without hand-writing
  `wpg:wgp` XML. A `set_style` operation restores a named paragraph style
  or clears direct paragraph formatting, which is what repairing a pasted
  revision needs; `"count": "all"` on a replace handles bulk character
  fixes such as stripping non-breaking spaces. **It writes nothing unless
  every edit in the batch matches the number of times declared for it**,
  since an edit that silently does nothing is this project's known failure
  mode (`project_log.md` Entry 039).
  Three structural guards, each added after that exact defect was caught
  here on 2026-07-31: namespace prefixes are preserved, because ElementTree
  renames them to `ns0:` and `fitshapes.py` then sees zero shape groups;
  empty elements are written Word's way (`<tag/>`, not `<tag />`) because
  the other tools match Word's form literally; and the source root element
  is restored, because `mc:Ignorable` names prefixes no element actually
  uses and dropping them makes Word reject the file as corrupt rather than
  report a namespace error. Requires Python, standard library only. Always
  run `fitshapes.py` and then both Word checks afterwards.

- `tools/make_share_folder.ps1` — builds a slimmed copy of the repo for the
  Claude surfaces that take a folder: Cowork and Design. Not for Projects,
  which reads a branch on GitHub rather than a local folder, and whose size
  limit is fixed by deselecting `assets/` and `drafts/` in its own file
  picker. Solves two problems at once: the repo is ~6.7 MB but
  6.3 MB of that is binary output no surface can reason about, and
  `internal/` plus the `.claude-memory` junction sit inside the repo root,
  which must never be handed to a remotely-executing surface (see "Choosing
  the right Claude surface"). `-Mode Docs` (default) copies the root
  markdown, `tools/` and `exports/` — 15 files, 0.88 MB. `-Mode Design`
  copies logo and icon SVGs, the creative brief and `project_brief.md` for
  the palette — 62 files, 0.32 MB, skipping the 3.2 MB of raster logo
  exports. `-Mode All` does both. The destination defaults to
  `C:\dev\gap-share` and **must be outside the repo**; the script refuses
  otherwise. It wipes and rebuilds the destination each run, so it will only
  write to a folder carrying the `.gap-share-folder` marker it drops or to a
  path that does not exist yet — pointing it at a folder of your own files
  aborts rather than deleting them. After copying it re-scans the output for
  `internal/` and `.claude-memory` and deletes everything if either appears.
  Copies the working tree, not a commit, so unlike a Project's GitHub sync
  it does include uncommitted work. The output is disposable: re-run to
  refresh it, and never treat it as a second source of truth. PowerShell
  only — no Word, Python or Inkscape; the window is WinForms, built into
  Windows PowerShell. **Bare invocation opens the window** (before
  2026-08-03 it ran a Docs build) — scripted and Claude-driven runs pass
  `-Mode` explicitly, as the usage examples always showed.

- `tools/prep_photos.py` — prepares phone photos for AI upload: takes what
  any mainstream phone produces (HEIC/HEIF, JPEG, PNG, WebP, TIFF, BMP,
  GIF, AVIF — not RAW/DNG), converts to PNG or JPEG, and renames
  `<YYYY-MM-DD>_<label>_<NN>` (`--label` sets the slug, default `img`;
  numbering runs per date, in capture order; date from EXIF capture time,
  file-modified time as the stated fallback). `--ai` is the compression
  preset for AI use: JPEG quality 85, long edge capped at 1568 px — the
  point past which most Claude models downscale server-side anyway, per
  Anthropic's vision guidance; `--max-edge 2576` reaches the current
  high-resolution models' ceiling at ~3x the image-token cost. Each of
  `--format`/`--max-edge`/`--quality` also works standalone. Bakes EXIF
  orientation into the pixels, carries remaining EXIF across, flattens
  transparency to white for JPEG, never overwrites (a taken name advances
  the sequence), skips its own output when scanning folders so re-runs are
  safe, leaves originals untouched, and re-opens every file it writes as
  an integrity check. `--dry-run` previews, `-o` collects output into one
  folder, `--recurse` descends. Run with no arguments (or `--gui`) for
  the windowed interface over the same code — per the GUI rule under
  Working approach. Default (no `--ai`) output is full-size
  PNG — several times the source size for photographs. Requires Python
  with Pillow; pillow-heif (`pip install pillow-heif`, wheel bundles
  libheif) only when HEIC is among the inputs.

- `tools/embed_logo.py` — embeds the GAP logo into a tool's GUI as
  base64 PNG constants, per the GUI rule's branding requirement: fills
  (or first inserts, or refreshes) the `LOGO_*_PNG` constants in a
  target script from the canonical exports in `assets/logo/png/` —
  wordmark resized for the header (default 180 px, kept above the
  wordmark's ~160 px minimum usable width), symbol at its native 64 and
  32 px for the title bar. Tk decodes base64 PNG natively, so a patched
  tool gains no imports. Python targets get triple-quoted constants,
  inserted above `__main__` if absent; PowerShell targets get
  `@'...'@` here-strings, replace-only — add the three placeholders by
  hand once (see `make_share_folder.ps1` for the shape). Refuses a
  partial constant set, and verifies a patched `.py` still parses
  before writing anything. Re-run over every GUI tool if the brand
  assets change. A build utility run at development time, not a
  learner-facing tool. Requires Python with Pillow.

## Claude's memory: what's in the repo vs. outside it

Two separate systems hold context across sessions — don't confuse them:

- **This repo (`project_brief.md`, `research_log.md`, `research_questions.md`,
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
  `~/.claude/projects/<project-id>/memory/` — the concrete path is
  machine-specific (the project moves between machines; resolve it on
  the machine in use rather than trusting a recorded example).
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
project/user-type entry against this file, `project_brief.md`, and
`research_log.md`: is the durable, process-level rule it describes already
captured in the repo, or only sitting in local memory? Propose anything
missing (for review, not a silent edit, same as any other change here) and
write in what's approved. This exists specifically because local memory
files are machine-specific and don't travel between machines (desktop vs.
laptop) or reliably resurface from old conversation logs — the repo is the
one place guaranteed to travel with the project. Applies in every session
working in this repo, not just the one that first set this up.
**Last run: 2026-07-31.** That pass audited all six memory files and found
five of them correctly machine-local — three are interaction-level
(agent-spawning, tool preferences, how to handle short pasted fragments)
and belong in memory rather than the repo, and the government-recognition
goal is already in `project_brief.md` under "Longer-term direction and
positioning". The one item that needed moving into the repo came from the
session itself rather than from a memory file: the unfetchable-versus-
unfetched distinction, now folded into bias self-check item 3 above.
Previous line, kept for the record: last run 2026-07-28. Update this line
each time the pass completes,
so any session can see how stale it's gotten. That pass audited all 19
memory files: 15 were already properly captured here, and four were
machine-local only — the vector-editing handoff rule, PowerShell alias
preference, model/cost flagging, and the understated-prose register. All
four were approved and written in (Working approach, and File conventions
for the prose one). Deliberate decision the same day: rules that went
straight into the repo without ever passing through local memory (the
public/internal split, `compatibilityMode`, icon sizing) are **not**
mirrored back into memory — the repo is the source of truth and travels
with the project, so duplicating them would only create drift.
