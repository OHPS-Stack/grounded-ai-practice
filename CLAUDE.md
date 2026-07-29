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
  to the task in front of you, not as a scattershot list.

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

3. **A source couldn't be retrieved → record the hole.** A source that
   403s or sits behind a login doesn't become absent from the evidence
   base, it becomes invisible in it. Log it as unfetched rather than
   letting the reachable evidence quietly stand in for all of it. NIST:
   *streetlight effect*, searching only where it is easiest to look.

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
`documents/Style_Reference_Example.docx` (the canonical reference) and
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

- **Callout cards use small/medium/large size presets**, each fixing the
  icon-well size; a card's width (and therefore its text column) is always
  a free parameter independent of preset, so resizing a card for its
  content never stretches or squeezes the icon. Built as a Word group
  (`wpg:wgp`) of sibling shapes, not nested shapes — see `project_log.md`
  Entry 015 for why (Word rejects a shape nested inside another shape's
  text box) and the rest of the construction.

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
   `internal/`, or that contain known private markers in tracked files.
   Install once per machine: `git config core.hooksPath .githooks`

Both are guardrails against accident, **not security controls**:

- `.gitignore` does nothing retroactively and is overridden by `git add -f`.

- The hook is local-only (cloning does not install it) and is bypassed by
  `git commit --no-verify`.

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

- `.githooks/pre-commit` — blocks commits staging `internal/` or
  containing known private markers. Install per machine with
  `git config core.hooksPath .githooks`. A guardrail against accident,
  not a security control.

- `assets/brand/icons/` — the promoted, working content-icon set (36
  icons, current palette). `svg/` for sources, `png/` for 64/128/256px
  exports, `README.md` for the filename→topic manifest.

- `assets/brand/logo/` — the finished logo system, and **supporting rather
  than primary**: the lead identity is a stylised "GAP" wordmark, decided
  but not yet designed (`project_log.md` Entry 027). Everything here
  remains valid and in use, nothing is deprecated.
  `logo_symbol.svg` (default, shaded), `logo_symbol_flat.svg`,
  `_mono`/`_reversed` symbol variants, and `logo_lockup_horizontal`/
  `logo_lockup_vertical` (+ `_mono`/`_reversed`) icon+wordmark lockups, all
  with wordmark text as real vector paths (Public Sans) and a two-tone
  colour hierarchy, plus `profile_picture_square`/`profile_picture_circular`
  avatar derivatives, plus `png/` exports for all of them. See
  `project_brief.md` "Visual identity" for the full picture.

- `assets/brand/logo/creative_brief.md` — portable creative brief for
  external logo-generation workflows (not a project research/decision
  document itself).

- `drafts/` — work-in-progress files under active iteration. Currently:
  `UK_AI_Skills_Ambition_Report.docx` (+ self-check `.pdf`), an 8-page
  report on the UK's AI skills ambition, delivered results and the gap
  between them — built 2026-07-28 on `research_log.md` Entries 043–048,
  **not yet reviewed by the creator** (see `project_log.md` Entry 022).
  Nothing here reflects a settled decision; contents may be replaced or
  removed once the format stabilises. Once a document is approved and no
  longer a draft, it moves to `documents/` instead.
  **Removed 2026-07-28** as superseded: `Effective_Prompting_Example.docx`
  (the original Word-template formatting test, superseded by the approved
  style reference) and `AI_Skills_Hub_Briefing.docx` (whose argument and
  research were absorbed into the wider UK-climate report). Their
  construction history remains in `project_log.md` Entries 015 and 019 —
  those entries are historical records and are deliberately **not**
  rewritten to hide that the files once existed.

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
  `project_log.md` Entry 016) — still subject to later refinement, but no
  longer a first draft**; the "Word document conventions" section above is
  the extracted rule set. Icon set inconsistencies (padding, mismatched
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
**Last run: 2026-07-28.** Update this line each time the pass completes,
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
