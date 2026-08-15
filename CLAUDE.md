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
  every future one — Entry 047 records the retrofit (done:
  `prep_photos`, `trace_reference`, `make_share_folder`). The
  Claude-driven docx/Word pipeline tools and `embed_logo` stay
  command-line by decision (Entry 049): Claude or a build step runs
  those, not a person, so the rule's test — would someone without a
  terminal habit ever run this — does not reach them.

- **Lessons are markdown-first; the export pipeline is a promotion
  step.** Adopted 2026-08-09 at the creator's direction. The creator is
  the project's first pilot learner; infrastructure sessions double as
  learning-material generation. Long technical instruction is produced
  as a house-conventions markdown unit (callouts, blank-line lists —
  readable as-is in Obsidian and GitHub), with chat carrying only a
  skimmable summary. The docx/PDF pipeline runs when a unit stabilises
  or needs distribution — its Word-render self-check is the main cost,
  so iteration stays in markdown. Where a mechanism or relationship is
  the point, a diagram beats a callout — Mermaid in the markdown for
  sketches (rendered to images at promotion, since `md_to_docx.py`
  takes `![caption](path)` only), the data-driven figures rule for
  anything with numbers in it; callouts are for warnings and tips, not
  the only graphic. Technical specifics are verified against
  documentation or the machine before being presented as instruction —
  the internal build guide's BIOS section, whose menu paths were
  asserted from memory and found wrong on the real board (2026-08-08),
  is the cautionary case. Units teach the reading of output — the
  fields that matter, the values that decide, the traps — rather than
  paste-and-analyse loops. First exemplar:
  `drafts/reading_smart_results.md`.

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

  Refined 2026-08-05: the division of labour is about ownership, not
  keystrokes. Claude may draft candidate final prose when it holds to
  the creator's register and plain language; the creator reviews every
  passage, edits freely, and nothing is published without approval. The
  argument, the voice and the final say stay the creator's, and the
  AI-assisted method is disclosed wherever the work is published. What
  the rule guards is that review and ownership, not who types.

- **Feedback on a draft produces a revised draft, not an edit.**
  Adopted 2026-08-06. When the creator comments on drafted prose or a
  drafted asset, the response is a corrected version shown for review;
  writing it to the file needs an explicit go-ahead. Caught during the
  landing-site prose pass, where a block was revised and applied in one
  step and the creator pointed out they had never seen the revision.
  The review gate is the whole justification for Claude drafting
  candidate final prose at all, so skipping it removes the ground the
  rule above stands on.
- **A generated document edited by hand becomes canonical, and the
  markdown is reconciled to it.** Adopted 2026-08-14 after two rounds
  of it on the pilot unit. The loop: copy the `.docx` aside before
  running anything; extract its text with `tools/docx_text.py
  --styles`; port every change into the markdown source; regenerate;
  extract the rebuild and **diff the two extractions**. The diff is the
  proof, and it catches two things a read does not. Deletions —
  a sentence the creator cut is simply absent from the new file, and
  nothing draws the eye to a gap. And limits of the converter — nested
  list items flatten to their parent's level, so hierarchy has to be
  carried in the wording instead. Mechanical slips (a doubled word, a
  stray article, a spelling inconsistent with the rest of the document)
  get fixed and reported; wording choices are matched exactly, even
  where they read a little oddly, because the file is canonical and the
  register is the creator's.

  A factual claim is a third case, and it follows neither branch: a
  hand edit asserting something primary evidence contradicts gets
  corrected, and the correction reported. Ownership covers the
  register and the argument, not a fact the record disproves.
  Matching such a claim exactly, which is what this rule says to do
  with wording, publishes a falsehood to the very people the document
  was written for. Where the correction is itself worth reading, give
  it room in the document rather than silently swapping the claim.
  Added 2026-08-14; the case that prompted it involves a private
  third party and stays in `internal/`.

- **Nothing outward is sent by Claude. Draft it, show it, stop.**
  Adopted 2026-08-14, stated explicitly by the creator and demonstrated
  the same day: three connection notes and a post comment were drafted
  in chat, and the creator sent the ones they chose. It covers every
  outward communication — email, LinkedIn messages and connection
  notes, comments, form submissions, anything addressed to another
  person — and asking first does not satisfy it. "Draft a message to X"
  is a request for a draft, and approval of one message never carries
  to the next.

  The reason is the one behind never pushing to the remote: an outward
  message carries the creator's name and their relationships, and it
  cannot be recalled. Where a platform imposes a limit, offer two or
  three options with character counts and say which one you would send
  and why. Recording that an approach happened, and what came of it,
  belongs in the internal register once the creator confirms they sent
  it. The contacts register's per-approach rule is the narrow case of
  this; this is the general one.

- **In an ongoing correspondence, read what has already been sent before
  drafting the next message.** Adopted 2026-08-13. Claude does not
  reliably track which points have already gone out, and a follow-up
  that re-introduces the creator's own background, a decision already
  announced, or a courtesy already extended reads as though nobody had
  been listening. Caught during a long technical exchange with an
  external contact, where a drafted reply repeated four things sent
  hours earlier. Re-read the sent messages first, and name what was cut
  as already covered, so the check is visible rather than assumed.

  **Corollary, from the same exchange: while the other party is still
  composing, silence on a question is not information.** Claude twice
  read unanswered questions as evidence the correspondent had no answer;
  he returned to each of them several messages later. Where a reading of
  someone's behaviour would change what gets written, mark it as a
  reading.

- **A change in scope or direction gets propagated the same day, and the
  newer position wins.** Adopted 2026-08-15. A decision that changes what
  the project is or where it is going does not stay in the place it was
  first written. Walk the repo files it touches — `project_brief.md` for
  the standing position, `project_log.md` for the dated decision,
  `CLAUDE.md` for any working rule it changes, `research_questions.md` if
  it opens or closes a question — and then the outward surfaces: the
  landing site sources in `site/`, `README.md`, the GitHub profile, and
  the LinkedIn profile copy. Most of those are current-state documents
  whose whole job is to be true now, so a stale one is the defect rather
  than the record.

  The case that prompted it: the funding route the project is aiming at —
  government grants letting a small organisation buy an AI workstation
  with a tutor layer on it — existed only in local memory and `internal/`
  while `project_brief.md` said nothing about it. Nothing was being held
  back. It simply never got copied out of the conversation it arrived in,
  and local memory does not travel between machines.

  **Where a newer position and an older one directly conflict, prefer the
  newer.** It is usually the better informed of the two, having been
  reached with the older one's evidence already in hand. The test remains
  whether it is actually better informed rather than merely more recent —
  a hasty revision does not beat a considered one on timestamp alone, and
  "the need, not the timing" still governs. But the default is the newer,
  and the superseded position becomes history in `project_log.md` rather
  than a second current answer left standing beside it.

- **Generated visual assets get a geometry self-check before they are
  accepted.** Adopted 2026-08-06. A script that draws an SVG cannot see
  its own output, so every figure on the landing site was verified by
  loading it in a browser and measuring the rendered text: labels
  probed for overflow past the canvas edge, pairwise collision against
  each other, and containment inside the box each belongs to. Same
  instinct as `word_preview.ps1` for documents, and it caught real
  defects repeatedly. Applies to any generated diagram or figure, not
  only the site's. Extended 2026-08-11 to charts built through
  `tools/gap_chart.py`, which carries the same checks in code: a render
  that did not complete, and overlapping labels in the rendered SVG.
  Both were written after the defect they catch — Vega reports errors
  from its embedded JavaScript runtime by printing and carrying on, so a
  bad axis format produced a plausible figure with every tick label
  silently missing, and an offset it ignored put six data labels on top
  of their own points.

- **A chart is a published claim, so it takes the finished-research bar
  rather than its source document's.** Adopted 2026-08-11 at the
  creator's direction. Figures travel further than the documents they
  come from — the infographics rule below already requires each one to
  carry its own source line precisely because most viewers only ever
  see the image — so a chart drawn from a rough draft publishes that
  draft's gaps as findings. Before drawing: read the source document's
  own status note, close the open questions the figure depends on, and
  re-read the relevant `research_log.md` entries directly rather than
  working from a draft's summary of them. The case: the budget-VRAM
  scatter was built from a document whose first line reads "rough
  draft", which also recorded one comparator "not priced this pass" and
  one supporting source "unread". The chart was conceptually and
  structurally sound, and made no comparison at all at 12 GB or 32 GB,
  where only Intel cards had been priced — the single comparison the
  figure existed to make. `check_coverage()` in `tools/gap_chart.py`
  blocks that specific shape, counting categories at each level of the
  x variable and refusing a build where a level carries only one; the
  general case is judgement and lives here.

- **A chart title states the finding; a title that describes the chart
  is a label.** Adopted 2026-08-11 at the creator's direction. The test
  is whether someone who reads only the title walks away with the
  point. "AI adoption by firm size" names the axes and leaves the
  reader to do the work; "Small firms adopt AI at a third the rate of
  large ones" carries it. This is the same instinct as the
  understatement rule under File conventions and subject to the same
  limit — a title still states facts and lets the conclusion land,
  rather than telling the reader what to feel about them.
  `check_title()` in `tools/gap_chart.py` flags the common label shapes
  (no verb, an axis-naming " by " construction, an "Overview of"
  opening) but stays advisory, because it cannot tell whether a
  sentence carries an insight: it flags "A £100 million programme,
  1,700 course completions", which is a noun phrase and also exactly
  the withheld-adjective construction this project's prose rules are
  built on.

  **Refined 2026-08-13 at the creator's direction.** Applied at full
  strength this rule produces titles that are punchlines about a
  subject the reader has not been introduced to, which in a technical
  field costs more comprehension than the insight buys. The title's
  first job is to say what the reader is looking at; stating the
  finding is its second job, and it only gets to do both when both fit
  in one plain sentence. Where they do not, **the subject wins and the
  finding moves to the subtitle** — a title that names its subject is
  not the failure this rule was written against. The failure it was
  written against is a title that names the *axes* ("AI adoption by
  firm size"), which tells the reader nothing they could not get from
  looking. Naming the subject is not the same thing as naming the axes.

  This is the same correction "Explain before concluding" makes to the
  prose rules under File conventions, and it arrived four days earlier
  there — the chart rule was written without inheriting it, which is
  the actual defect rather than the rule being too strict.
  `check_title()` **cannot see this failure mode**: it flags a title
  for having no verb, which is the opposite pressure, so a
  subject-establishing title will always warn. Treat its output as weak
  evidence and ignore it freely when the title's job is to establish
  the subject. Four figures were retitled on this refinement the day it
  was adopted — `uk_ai_events`, `appg_programme` and the two internal
  ones — and only the first kept both jobs in one sentence.

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

- **Report what changes in Claude Code, and what it means here.** Adopted
  2026-08-15 at the creator's direction. On a new release, or when a task
  touches a feature that has moved, say what changed and what it costs or
  unlocks — verified against the changelog
  (`https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md`)
  and `code.claude.com/docs`, **never from recall**, since the model's
  knowledge cutoff sits months behind the installed build and a confidently
  wrong account of the tool's own behaviour is worse than none. Filter to
  this project: Windows, PowerShell, solo (no org or managed settings), a
  public repo with a gitignored `internal/`, the `.docx` and figure
  pipelines, the laptop/desktop split. Skip enterprise, Bedrock/Vertex and
  team features unless asked. One flag at a natural boundary, per the
  model-fit rule above — not a changelog dump. The same applies to new
  skills, plugins and marketplace tools that fit work in hand, which is the
  standing tool-recommendation rule above applied to a moving target.

  The version is not reliably discoverable on this machine: the desktop app
  puts no `claude` on `PATH`, and carries no version in the registry or
  under `%APPDATA%\Claude`. Ask rather than probe.

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

- **Short pasted fragments get a fix, not a question.** Adopted
  2026-08-03. When the user pastes a short clause or single sentence
  with no instruction, that is deliberate: name the defect in a
  sentence, give the rewrite, stop. Longer passages arrive with a
  stated problem and can be treated normally. Asking what is wrong
  with a one-line fragment costs a round trip for something already
  visible.

- If a task's best approach depends on a tool or runtime that turns out to
  be missing, say so explicitly — what's missing, what it would unlock,
  brief install instructions — before falling back to a weaker workaround.
  Never install anything yourself; surface the command for the user to run
  (see "Commands should never be blind copy-paste" below).

- When a stated pain point matches a known tool or product (including
  Anthropic's own — Claude for Word/Excel/PowerPoint, Claude in Chrome,
  connectors), name it unprompted. Time it to when it's actually relevant
  to the task in front of you, not as a scattershot list. This includes
  community-built and open-source tools for Claude Code where they
  genuinely fit the work in hand — verified by a cheap lookup before
  recommending, never from a vaguely remembered name. The
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

- **A claim going into a deliverable is re-read from its log entry,
  never recalled.** Adopted 2026-08-06. Claude's recollection of a
  logged finding is not evidence of it. During the landing-site build a
  sentence was drafted attributing the £400bn figure to
  Microsoft-commissioned research; `research_log.md` Entry 052 exists
  precisely to correct that attribution to Google, and reading the entry
  before writing produced the accurate version. Recall is the mechanism
  by which an already-corrected error gets reintroduced downstream,
  which is worse than the original error because the correction makes it
  look settled.

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
  **Text read from an image is not the text either.** Extended
  2026-08-13. The same failure arrives by a second route — a message
  read from a screenshot rather than from pasted text. One read this way
  produced a clause ambiguous between "that would be efficient" and
  "efficiency would be low", opposite meanings, in the passage a reply
  was about to be built on; the pasted text settled it. Use a screenshot
  to locate a claim, ask for the text before quoting, translating or
  reasoning from it, and say which of the two you are working from.

- **Confirm/disconfirm pairing applies to foundational claims** — the ones
  that would actually change project direction — not to every statistic.
  Don't default to only searching for evidence that supports an existing
  hypothesis; this project has already caught itself doing this once (see
  Entry 013 in the log) and corrected for it.

- **A completed evidence base still needs checking against the operating
  questions.** Adopted 2026-08-13. Research assembled to answer a
  purchase comparison answers that comparison and leaves the operating
  envelope untouched — what the hardware is like to own, what it reports
  about itself, what else can drive it, what breaks. The case:
  `drafts/budget_vram_for_local_ai.md` rested on seven primary benchmark
  sources and recorded that every surfaced lead had been read, and one
  practitioner conversation then found four gaps in it
  (`research_log.md` Entries 082-083) — ECC memory, the bandwidth cost of
  unified-memory machines, OpenCL as a working software path, and a
  vendor telemetry tool that disproved a stated limitation. None was a
  failure of rigour. All four sat outside the question the document had
  been built to answer, which is precisely why its sources never
  surfaced them. So when an evidence base is declared complete, run one
  separate pass asking how the thing is actually operated — and treat a
  practitioner's account as the cheapest route to those questions, while
  logging it at testimony's weight rather than a source's.

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

- **Both logs are CRLF; append accordingly.** Writing to them with a
  tool that emits bare newlines leaves mixed line endings and a diff
  that appears to rewrite the entire file. Convert on write, then
  confirm no stray LFs remain before staging.

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

- **Tracked logs record the project, not the person.** Adopted
  2026-08-05 at the creator's direction, after a log entry reached the
  staging area carrying the creator's forgotten disk passwords, their
  personal media stack, and a request they had made in chat that was
  declined. None of it was project content, none of it had been
  reviewed, and it would have been published on the next commit.

  **The test:** is the fact about the *project's* decisions, findings or
  reasoning, or about the *creator's* circumstances, possessions, habits
  or requests? The first belongs in the log. The second belongs in
  `internal/`, or nowhere.

  A technical finding can nearly always be written in its general form —
  "a Windows account password does not encrypt a disk" rather than "the
  creator has forgotten three passwords on an old drive" — and the
  general form is the better record anyway, because it is the part that
  transfers to anyone else.

  Two things this does **not** prohibit. Ordinary design and scoping
  decisions attributed to the creator ("the creator asked for a square
  profile picture") are the log's job and stay. And recording that a
  request was screened out is fine *in the abstract*, via the pointer
  pattern — what is prohibited is reproducing what was asked for, which
  publishes the request rather than the judgement.

  **This applies at the moment of writing, not at the audit.** Draft
  every log entry as though the repository were already public, because
  by the next commit it may be.

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

  **Understatement is a closing move, not a register.** Refined
  2026-08-07 after a second external review (`project_log.md` Entry
  061). The rules above were written to fix the *opposite* defect — an
  external review of the UK-climate report found AI-drafted prose
  abstract and over-qualified (Entry 042) — and were then applied at
  constant density across the landing site. The second reviewer read
  the result as AI-generated, naming the flat two-beat and the
  rule-of-three list as the tells. **Mimicking the creator's tics at
  full coverage is not their voice; a person varies.** So: reserve the
  signature moves — the withheld adjective, the implication left to the
  reader — for the few places the facts genuinely carry them, roughly
  once a page rather than once a paragraph, and let most passages be
  plainly informative with no rhetorical turn at all. Vary sentence
  length and paragraph shape.

  **Explain before concluding.** Both flagged passages shared a second
  defect worth more than the tics: each was a punchline about a concept
  the page had never introduced. A teaching project whose prose
  performs conclusions instead of explaining them contradicts its own
  purpose, so the fix was to teach the idea first and let the
  conclusion land after.

  **The em-dash apposition is this project's most persistent AI tell.**
  Adopted 2026-08-14, from two consecutive revision passes on the pilot
  unit in which the creator's edits were overwhelmingly one move: an
  aside bracketed by em-dashes, broken out into a colon, a semicolon or
  a new sentence. "...beyond the installer's own prompts — read them
  rather than clicking through" became "...beyond the installer's own
  prompts, so read them rather than clicking through", a dozen times
  over. The construction is not banned; being the *default* is the
  defect. Draft the aside as its own short sentence first and reach for
  paired dashes only where the interruption earns it — about as often
  as the withheld adjective, which is to say rarely. This is the
  sentence-level companion to the understatement rule above: the same
  instinct at a smaller scale, and the same failure mode of applying a
  signature move at constant density.

  **The site speaks in first person** (creator decision, 2026-08-07):
  one narrator on every page, the origin story leading, plain
  first-person procedure on the evidence and method pages. Voice-matching
  means writing as a person with the creator's register would, not
  reproducing their mannerisms at maximum density.

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

**This covers the directory's shape, not only its contents.** Extended
2026-08-15, when `internal/` was reorganised by subject so that it could
be navigated at all. Grouping by subject is exactly what turns folder
names into the disclosure risk filenames already were, so the layout is
recorded in `internal/README.md` alongside the contents. This file says
that the directory is organised; it does not say how.

**Build scripts for an internal document live beside it in `internal/`,
never in `tools/`.** Adopted 2026-08-15. A script is a worse disclosure
than a bare filename, because its docstring explains what the document
is for — so a figure builder sitting in a public directory announces
both that a private document exists and what it argues. Caught the same
day the rule above was written, when a figure script for an internal
setup guide was written into `tools/` and indexed here. Nothing in it
was compromising, which is why the fix was a move rather than a history
rewrite.

The outputs follow the script: an internal script's figures are internal
too, because `assets/figures/` entries all name the tracked script that
builds them, and a tracked image whose builder is private breaks the
source-of-truth convention the whole folder relies on. Where a diagram
is genuinely worth publishing, write a public counterpart rather than
letting one script straddle the line — `tools/build_events_figure.py`
and its internal sibling are the model. The ordinary case needs no such
pairing: the builder simply sits beside the document it builds.

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

   The pre-commit hook carries a **third check**, added 2026-08-05 after
   an unreviewed log entry reached the staging area (see "Tracked logs
   record the project, not the person"). It scans **only added lines**,
   in two tiers: a narrow set of legally-sensitive terms that **blocks**,
   and heuristic phrasing plus machine-specific absolute paths that
   **prints for review without blocking**. The split is deliberate — a
   fuzzy pattern that refuses a commit teaches you to reach for
   `--no-verify`, which switches off checks 1 and 2 as well, so the
   uncertain tier stays advisory to keep the certain ones enforceable.
   `.githooks/` is excluded from its own scan, since the file necessarily
   contains the words it looks for. It cannot catch the general case,
   which is semantic rather than lexical; the review gate is the actual
   guard and this is the backstop.

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
2026-08-03** (`project_log.md` Entry 048; found the private marker inside
the pre-commit hook itself, six days public across 17 of 33 commits —
history rewritten, marker list moved out of tracked content, review gate
adopted; two stale current-state claims corrected; no other findings. The
independent second-model pass was not run.) Previous: 2026-07-28
(initial; pre-sharing content issues fixed the same day, history clean
across 15 commits — the audit that the hook was written immediately
after, and so did not cover).

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
  parties, **the creator's personal circumstances, possessions or chat
  requests** (see "Tracked logs record the project, not the person"),
  machine-specific absolute paths, dangling cross-references, and claims
  contradicted by later log entries — and report findings for decision
  rather than silently fixing them. Read every log entry added since the
  last commit, including ones written in an earlier session: the defect
  this rule exists for arrived that way. The hooks enforce the mechanical part (`internal/`
  staging, the marker list in `internal/private_markers.txt`); this
  review is the judgement part. Neither replaces the scheduled repo
  audit, which also covers history.

- **Draft the commit message and show it to the user before running
  `git commit`**, for any commit with a real message to write (not a
  one-liner the user dictated directly). A go-ahead like "let's commit
  this" means prepare it, not execute it unreviewed — commits are
  semi-permanent and this repo may go public.

- **Commit messages follow one fixed format.** Adopted 2026-08-06 after
  an audit found five subject-line styles across the history (imperative,
  past tense, third-person present, bare noun phrase, and GitHub's
  default "Update README.md"), some with trailing full stops and some
  without.

  **Subject:** imperative mood, capitalised, no trailing full stop, 70
  characters or fewer. A semicolon joins two related changes. "Add the
  landing site" — never "Added…", "Adds…", "Landing site updates", or a
  trailing period.

  **Body:** blank line after the subject, then one paragraph per idea,
  each written as **a single unwrapped line**. Do not hard-wrap at 72
  columns: that convention serves terminal `git log`, while these
  commits are read on GitHub, which soft-wraps and turns every hard
  break into a mid-sentence tear. Bullets are `- ` and are likewise
  unwrapped. Never repeat the subject line as the body's first line.

  **Voice and length:** the user's own — short, direct, no
  em-dash-chaining, no third-person "the creator". Length matches the
  size of the change: routine work (renames, cleanups, single fixes,
  asset regeneration) gets a subject line and nothing else, and a
  multi-paragraph body is reserved for a new deliverable, a structural
  change, or a decision worth reading later. Defaulting to the long form
  buries the commits that matter.

  Refined 2026-08-13 at the creator's direction: even when a body is
  earned, keep it brief and plain — short `- ` bullets rather than
  paragraphs, ordinary words rather than project shorthand, and detail
  left in the logs, which the commit references instead of restating.
  The test: readable at a glance by someone who was not in the session.

  **History was normalised to this format on 2026-08-06** (`project_log.md`
  Entry 060). That pass changed expression only: no claim was altered,
  including claims later found wrong, and no body was invented for a
  commit that never had one.

- **Never push to the remote without a separate, explicit go-ahead**, even
  immediately after a local commit the user asked for. The user handles
  pushes themselves.

- **A file-sync layer sits over this repo, and it does not merge.**
  Adopted 2026-08-14. `internal/` is gitignored, so it can only reach
  another machine by file sync — Proton Drive, currently — and tracked
  files can arrive the same way: during one session a sync landed the
  desktop's uncommitted work on five tracked files mid-conversation.
  Sync copies whichever version of a file it saw last. It does not
  reconcile two machines' edits, which is precisely what git is for. So
  **commit before leaving a machine**, and say when a push is due so the
  user can make it — never push, per the rule above.

  It also changes how a numbered log is appended to. `research_log.md`
  gained six source-key rows and Entries 086-087 between one read and
  the next, while Claude's context still held the file as ending at
  Entry 083. Nothing was lost, and the numbering stayed sequential only
  because the other machine had independently skipped ahead; two tracks
  numbering entries in one file is the collision `project_log.md` Entry
  017 already records. So **re-read the tail of a numbered log
  immediately before writing an entry into it**, rather than trusting a
  read from earlier in the same session, and treat an unexplained change
  in a tracked file as a sync rather than a mystery.

  Where two unrelated sets of additions have already landed in one file,
  they can still be committed apart rather than bundled: build the
  intended content, stage it with `git hash-object -w --path <file>` and
  `git update-index --cacheinfo`, then check `git diff --cached` before
  committing. The `--path` argument matters — it applies the repo's own
  CRLF clean filter, and hashing a working-tree file without it stages a
  blob that differs from HEAD in every line.

- **Commit messages (and any other outward-facing prose — docs, summaries)
  must match the user's own voice**: short, direct, no AI-register
  em-dash-chaining, and never third-person references to the user (e.g.
  "the creator") — that framing belongs in `research_log.md`'s internal
  entries, not in text written in the user's own voice.

- **No AI co-author attribution on commits.** Adopted 2026-08-03 at the
  user's direction. Commit messages carry no `Co-Authored-By: Claude`
  trailer and no equivalent AI-contributor line, so the commit history
  and the GitHub contributor list read as the user's own work — which
  is what they are: every commit is reviewed and decided by the user
  before it is made. Claude Code's default is to append that trailer,
  so this rule has to be applied deliberately in each session rather
  than assumed. The AI-assisted working method is stated openly in
  `README.md` and throughout the logs; it does not also need a
  machine-readable authorship claim on every commit.

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

- `docs/` — the public landing site, served by GitHub Pages from `/docs`
  on `main` and live at **`groundedaipractice.co.uk`**, its canonical
  address (`project_log.md` Entry 064). `docs/CNAME` is what attaches
  the domain, and `base_url` in `site/pages.json` is what feeds the
  `canonical` and `og:` URLs — change it there and rebuild, never in
  the generated HTML. The same DNS zone serves the project's mailbox,
  so the mail records are never touched. A
  static site of eight pages (home, evidence, workstation, learning,
  method, system, about, contact, plus `404.html`), written in the
  creator's first person: no
  framework, nothing loaded from a third party, and exactly one script
  — `theme.js`, the light/dark override, which the CSP admits via
  `script-src 'self'`. **Everything in `docs/` ending `.html` is
  generated output — edit `site/` instead**, since a hand edit here is
  lost at the next build; `404.html` is the one hand-maintained
  exception, because it uses no shared shell. Preview it through
  `tools/serve_site.py`, never a bare `http.server`. Its data figures are generated by
  `tools/build_site_figures.py` — correct the data constants and re-run,
  never edit the SVGs; its diagrams are native HTML built from the icon
  set; and its logo files and icons are copies of the canonical assets
  in `assets/`. `docs/README.md` is the folder's own index:
  deployment, the security posture and its honest limits (GitHub Pages
  cannot set response headers, so CSP rides a `<meta>` tag and
  `frame-ancestors`/HSTS are unavailable there), and the safe order for
  attaching the custom domain — verify the TXT record before touching
  DNS. Site prose falls under the outward-facing prose rule (Claude's
  rough draft, the creator's final copy), and enabling Pages, pointing
  the domain and posting the link anywhere are each per-item creator
  decisions. Built 2026-08-05 — `project_log.md` Entry 055.

- `site/` — the landing site's **sources**, assembled into `docs/` by
  `tools/build_site_pages.py`. `layout.html` is the shell every page
  shares (head, header, nav, footer) with `{{token}}` placeholders;
  `pages.json` is the site's structure — the ordered nav and one record
  per page giving its fragment, output path, title and description;
  `pages/` holds one content fragment per page, each being the inner
  content of `<main>` and nothing else. Deliberately outside `docs/`,
  because GitHub Pages publishes that folder wholesale and a fragment
  left in it would be served to the public as a half-page. Added
  2026-08-06 when the site moved from one page to several.

- `internal/` — **gitignored, never committed.** Private contacts,
  candid assessments, funding strategy, political reads, third-party
  reference material. Organised by subject into a handful of folders
  rather than the flat list it was until 2026-08-15, when it reached
  about 75 files and stopped being navigable. The folder names are
  themselves disclosive, so the structure is indexed alongside the
  contents in its own `internal/README.md`, not here — see "Public
  repo vs. internal working files" above for what belongs in it, why,
  and the indexing rule. One path inside it is fixed rather than free:
  `internal/private_markers.txt`, which both hooks hard-code.

- `.githooks/` — the local guard layer: `pre-commit` blocks commits
  staging `internal/` or containing a private marker, and additionally
  scans **added lines only** for legally-sensitive terms (blocking) and
  for personal-circumstance phrasing and machine-specific paths
  (advisory, printed not blocked); `pre-push` re-scans the whole tracked
  tree and the pushed commits before anything leaves the machine. Both
  read their marker list from `internal/private_markers.txt` (never
  tracked; a missing file blocks, an empty one is a deliberate opt-out).
  **That path is hard-coded in both hooks**, so it is fixed against any
  reorganisation of `internal/` and must never be moved.
  Install per machine with `git config core.hooksPath .githooks`.
  Guardrails against accident, not security controls.

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

- `drafts/reading_smart_results.md` — learning-unit draft: how to read
  a drive's SMART results. The `smartctl` command decomposed and the
  Disks GUI route beside it, the self-test log statuses, the five
  attributes Backblaze's failure data says to read raw, the Seagate
  raw-value trap, and a verdict table for what the outcomes decide.
  Written 2026-08-09 during the server build — the first unit drafted
  directly from the pilot-learner sessions; generic by design, no
  machine specifics. `drafts/Reading_SMART_Results.docx` (+ self-check
  `.pdf`) is generated from it by `tools/md_to_docx.py`; the markdown
  is the source of truth.

- `drafts/budget_vram_for_local_ai.md` — research-document draft: what
  budget GPU hardware (Intel's Arc Pro line foremost) changes about the
  local-AI cost question, and what it doesn't. Why VRAM is the deciding
  purchase number, the 2026 memory-price crisis, dated UK prices for
  the realistic options, measured Arc inference performance, the
  software-stack risk (IPEX-LLM archived; LLM Scaler "beta at best"),
  the break-even against API pricing, and the uncounted costs stated
  per the bias checklist. Built 2026-08-11 on `research_log.md`
  Entries 068–071 at the creator's direction; extends the Entry
  030/042 local-vs-cloud thread. Carries the `vram_price_capacity`
  and `vram_capability_ladder` figures; the comparator prices and
  previously unread benchmark sources that its first pass left open
  were closed the same day (Entries 070–073 — every surfaced lead in
  the thread is now read), and the capability section was rebuilt
  2026-08-12 on Entry 079's era-anchored comparison. `drafts/Budget_VRAM_for_Local_AI.docx` (+ self-check
  `.pdf`) is generated from it by `tools/md_to_docx.py`; the
  markdown is the source of truth. Rough draft — structure and evidence in
  place, final prose the creator's, per the outward-facing prose rule.
  Every price is a dated single-day listing; the closing section holds
  the design sketch for the hands-on follow-up unit (hardware purchase
  is a creator decision).

- `drafts/effective_prompting.md` — the pilot learning unit, first
  full draft: "Effective prompting — what's really happening when
  you hit send." The five moves (task and reader, background, shape,
  example, exclusions), the fill-every-gap mental model folded in as
  scaffolding per the Entry 040 sequencing evidence, a symptom→fix
  table for diagnosing answers from the answer alone, three guided
  exercises (two deliberately tool-free), an independent-practice
  template, the when-prompting-is-not-the-fix cases, and a spaced
  one-week return. GRR-sequenced, PRIMES-sized (45–60 minutes),
  tool-neutral; technique claims verified against vendor guidance
  (`research_log.md` Entry 072). Drafted 2026-08-11 — see
  `project_log.md` Entry 068 for the production decisions. Untested
  with learners; final prose the creator's; the learner trial is the
  unit's own next step. `drafts/Effective_Prompting.docx`
  (+ self-check `.pdf`) is generated from it by
  `tools/md_to_docx.py`; the markdown is the source of truth, and
  its mechanism diagram is the drawn `fig_prompt_gap.png` from
  `tools/build_prompting_figures.py`.

- `drafts/foi_requests.md` — two Freedom of Information requests,
  **sent 2026-08-12 via WhatDoTheyKnow, responses due by 10 September
  2026**: DCMS (the counting rules, splits, UK filtering and
  benchmark coverage behind the 1,001,147 course-completion figure,
  and how a workers target is measured in course completions —
  re-addressed after DSIT's abolition, Entry 077) and UKRI/Innovate
  UK (the BridgeAI completion definition, the £74.6m breakdown, the
  Hub's contractually mandated performance figures, the second white
  paper, and the contract-extension decision). Grounded in
  `research_log.md` Entries 044, 051, 053, 056, 060, 061 and 074–077,
  each read directly; shortened and re-drafted audience-first before
  sending, with five questions deliberately held back for follow-up
  rounds. The live thread URLs and due dates are in the file and in
  `research_log.md`'s Open Threads. `drafts/foi_requests.txt` is the
  paste-ready text as sent. Requester details are never stored in
  either file.

- `drafts/home_server_synopsis.md` — the **public** account of the home
  server build: what it does, the four decisions worth explaining (no
  RAID, Ubuntu Desktop over a server distribution, nothing exposed to the
  internet, and live sport belonging on a separate device), two silent
  failure modes worth knowing, what is unfinished, and why an
  infrastructure build sits in a research repository. Written 2026-08-05
  when the full guide moved to `internal/` (`project_log.md` Entry 052) —
  short, generic, and carrying no machine or network specifics.
  `drafts/Home_Server_Synopsis.docx` (+ self-check `.pdf`) is generated
  from it; the markdown is the source of truth. Shares its figures with
  the internal guide, in `assets/figures/`.

- **The full build guide and its standing state are now in `internal/`**
  and are indexed there, not here — they carry the specific machine, the
  home network and the recovery of personal data from an old drive.
  `drafts/home_server_synopsis.md` above is the public-facing account.
  Moved 2026-08-05 at the creator's direction; `project_log.md` Entry 052
  records the split and the reasoning.

- `drafts/pilot_ai_workstation.md` — the pilot AI workstation unit:
  turning the project's desktop (RDNA3 GPU, 20 GB VRAM) into the
  working proof of the product hypothesis in three phases — native
  Windows inference through Ollama, the containerised deployment
  shape (WSL2, Docker, vLLM over ROCm), then the SME-shaped task set
  and tutor layer. Carries the fixed three-prompt measurement
  protocol that keeps the project's first own-hardware numbers
  comparable across runs and future cards, and keeps the Arc
  purchase question explicitly separate from what the owned card can
  prove. Stack facts verified against vendor documentation
  2026-08-13; every step stays marked planned until it has been run
  on the desktop, per the verify-before-teaching rule. Written
  2026-08-13 (`project_log.md` Entry 080). Revised 2026-08-14 on the
  desktop itself: the hardware table carries what the machine reports,
  and the Arc card's host is decided — it goes in this desktop, which
  makes the operating system rather than the machine the open question
  (`project_log.md` Entry 083, evidence in `research_log.md` Entry
  087). `drafts/Pilot_AI_Workstation.docx` (+ self-check `.pdf`) is
  generated from it by `tools/md_to_docx.py`; the markdown is the
  source of truth, and its two figures come from
  `tools/build_pilot_figures.py`. Three send-copies exist alongside it,
  all generated and all regenerable: `drafts/pilot_ai_workstation.txt`
  (the markdown with figure references made readable, for platforms
  that reject `.md`), and a Korean edition —
  `drafts/pilot_ai_workstation_ko.md` as its source, with
  `Pilot_AI_Workstation_KO.docx` and its self-check `.pdf` built from
  it. The Korean edition leaves product names, commands, citation keys
  and **the three fixed measurement prompts** in English, the prompts
  because they are the measurement's input and translating them would
  end comparability; a translator's note in the document says so.
  Build it with `--east-asia "Malgun Gothic"` and fit it with
  `--measure-face` and `--line-scale`, per `project_log.md` Entry 086.

- `assets/figures/` — the diagrams for the home server documents (drive
  layout and what the nightly job copies, why neither remote-access route
  needs an open port, where picture and sound go, annual running cost,
  order of operations). Generated by
  `tools/build_server_guide_figures.py`; regenerate before rebuilding
  either document. Shared by the public synopsis and the internal guide,
  which is why they live in `assets/` rather than beside either one.
  Since 2026-08-11 the folder also holds the budget-VRAM figures
  (`vram_price_capacity`, the LinkedIn-format `vram_price_ladder` and
  `vram_price_per_gb`, and
  since 2026-08-12 the capability ladder `vram_capability_ladder`,
  each light and dark, SVG and PNG), generated by
  `tools/build_vram_figures.py` for its own draft document, and the
  prompting unit's mechanism figure (`fig_prompt_gap.png`), from
  `tools/build_prompting_figures.py`. Since 2026-08-13 it also holds
  `uk_ai_events` (light and dark, SVG and PNG), the events-and-cost
  timeline from `tools/build_events_figure.py`, and `appg_programme`
  (same four files), the APPG round-table calendar from
  `tools/build_appg_figure.py`. Since 2026-08-14 it holds the pilot
  unit's `fig_pilot_stacks.png` and `fig_pilot_os_matrix.png`, from
  `tools/build_pilot_figures.py`, and the `brand_icons/` subfolder of
  third-party monochrome marks those figures use — see that folder's
  README for source and licence before touching them.

- `assets/replicas/` — terminal replicas for the build guide and the
  landing site: a `.json` spec and its rendered `.png` per screenshot,
  generated by `tools/replica.py` (`site_figures_build` is the landing
  site's one; the rest belong to the guide). **The JSON is the source of
  truth**; edit it and re-render rather than touching the PNG. All of them use generic names
  (`yourname`, `gap-server`) — the renderer refuses a real user path, and
  that guard is the reason these are safe to keep in a public directory
  even though the guide they illustrate is internal.

- `assets/social/` — the project's social/link-preview cards
  (1280×640, exported 2×: a lead mark, optional subtitle, domain and
  ghosted symbol on an Ink or Sand ground; since 2026-08-12 both ship
  subtitle-free with the enlarged lead): `repo_social_preview.png` (light,
  led by the GitHub Mark) for the repository's social-preview setting
  and `gap_card.png` (dark, led by the GAP wordmark) as the general
  project card — themed and marked apart deliberately, so the two
  sitting side by side in a Featured section read as siblings rather
  than twins. `github-mark.png` is the official GitHub Invertocat,
  downloaded from GitHub's own brand assets with the creator's
  permission and used unmodified per GitHub's logo terms (the
  composer derives transparency from its baked white canvas; the
  glyph is untouched). All generated by
  `tools/build_linkedin_banner.py` — regenerate rather than edit.
  Added 2026-08-12.

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
  step. For a non-Latin edition, `--measure-face` measures widths with a
  font that has the script's glyphs and `--line-scale` compensates for
  Word laying CJK lines out taller than the font's own metrics (about
  1.28 for Malgun Gothic; a multiplier rather than padding, because the
  shortfall grows with the line count). Until 2026-08-14 it measured the
  writer's escaped XML rather than the text — seven characters for every
  em-dash, and about five for every Korean syllable — so **every card it
  had ever fitted was slightly too tall**; the defect survived because it
  erred toward padding and never toward clipping (`project_log.md`
  Entry 086).

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

- `tools/md_to_docx.py` — converts a Markdown file into a house-style
  `.docx`. Written 2026-08-04 for the home server guide, which needed to
  be readable away from a code editor. It contributes **no formatting of
  its own**: `styles.xml`, `numbering.xml` and `settings.xml` are lifted
  wholesale from a template `.docx`, by default
  `exports/Style_Reference_Example.docx`, so the named styles, the bullet
  and number definitions and the `compatibilityMode` 15 declaration all
  arrive already correct and stay correct if the reference is revised —
  a converter carrying its own copy of the house style would drift
  invisibly. Maps headings to Title/Heading1-3, tables to the Ink-header
  banded pattern, fenced code to a shaded single-cell table (a table
  because it clips rather than reflows, and a wrapped command is a wrong
  command), `> **NOTE**`/`TIP`/`WARNING`/`CHECK` blockquotes to callout
  cards, and `![caption](path)` to a figure sized to the text column with
  a Caption paragraph; an italic-only line directly under the `#` title
  becomes the template's real Subtitle style (added 2026-08-14, matching
  the creator's hand pattern). `--highlight` colours a literal token
  Ember wherever it appears. `--east-asia FONT` names a face on
  `w:eastAsia`, the attribute Word resolves CJK characters through, so a
  translated edition keeps Public Sans for Latin and renders Hangul or
  Kana in a font that has the glyphs (added 2026-08-14 for the Korean
  edition; applied as one sweep over the assembled XML, because a single
  missed run is a paragraph of tofu). Holds lists open across the blank lines this
  repo's Markdown convention mandates. Each numbered list restarts at 1,
  via its own numbering instance rather than the template's shared one —
  before 2026-08-14 every list after the first continued the previous
  one's count, wrongly, in every document the tool had produced
  (`project_log.md` Entry 084, which also covers the fenced-block,
  column-width and two-digit-marker fixes made the same day).
  **Emits callout cards at a guessed
  height** — always run `fitshapes.py` and then both Word checks after,
  same as any other construction step. None of those checks can see a
  wrong list number, so read the render as well. Requires Python; Pillow only if
  the document has figures.

- `tools/replica.py` — renders **terminal replicas**: realistic pictures
  of a shell session, drawn from a JSON description rather than
  photographed. A fenced code block shows what to type; it does not show
  the window, the prompt colours, or what comes back, and someone who has
  never opened a terminal cannot tell from it whether they succeeded.
  Real screenshots would have to be taken on the machine being built,
  before it is built, and would carry its real hostname and network.
  Renders `ubuntu_terminal` (GNOME Terminal, Yaru dark, the aubergine
  background and Tango palette, bash's stock coloured prompt) and
  `powershell` (Windows 11 chrome). Adapted 2026-08-05 from the PAWH
  replica system — `project_log.md` Entry 053 records what was carried
  over, what was deliberately dropped, and why. Draws on a **fixed
  character grid** rather than letting the font advance, because
  box-drawing characters in `lsblk` and `systemctl` output do not occupy
  exactly one cell in Consolas and every column after one of them would
  land askew. Validation refuses a real user path, keeping the pack's
  generic-names rule enforced rather than merely documented. `--selftest`
  runs the smoke tests; `--demo` renders both types. Requires Python with
  Pillow, standard library otherwise. **No File Explorer renderer** — the
  transfer pack's own audit records that the original never implemented
  one, and claiming it here would repeat the defect that audit exists to
  flag.

- `tools/build_server_guide_figures.py` — draws the five figures in the
  home server documents: the drive layout and what the
  nightly job actually copies, why neither remote-access route needs an
  open port, where picture and sound go, annual running cost against a
  mini PC, and the order of operations. Document-specific rather than
  general tooling, kept here so the figures can be regenerated when the
  guide changes rather than being unreproducible artefacts. The cost
  chart's numbers are in `COST_DATA` in the file, per the data-driven
  figures rule. Drawn with Pillow rather than through
  `trace_reference.py` and Inkscape: that route is for concept artwork
  where Claude cannot see what it draws, whereas these are boxes and
  arrows on a computed grid with no curve work in them — and Inkscape is
  not installed on every machine this repo runs on, while Pillow already
  is. Requires Python with Pillow and the Public Sans faces installed.

- `tools/build_pilot_figures.py` — draws the pilot workstation unit's
  two figures: `fig_pilot_stacks` (one machine, two card eras over the
  single shared PCIe slot — the AMD-era Windows/WSL2 stack beside the
  Arc-era native-Ubuntu stack) and `fig_pilot_os_matrix` (where each
  card's stack is documented per the vendors' own pages, the unit's
  OS argument as a grid). Imports its helpers from
  `build_server_guide_figures.py` like the prompting script does. The
  stacks figure carries real vendor marks at the creator's 2026-08-14
  direction — monochrome, tinted at render time from the SVGs in
  `assets/figures/brand_icons/` (that folder's README records source,
  licence and the takedown fallback); identification, not endorsement,
  and never redrawn by hand. Rasterises the marks through
  `vl-convert-python` where present, else Inkscape, discovered the way
  `trace_reference.py` finds it — the desktop has Inkscape and not
  vl-convert, the laptop the reverse. Requires Python with Pillow, the
  Public Sans faces, its sibling script, and one of the two
  rasterisers. Command-line by the Entry 049 decision.

- `tools/build_prompting_figures.py` — draws the effective-prompting
  unit's mechanism figure (`assets/figures/fig_prompt_gap.png`): what
  the learner knows, the fraction of it the prompt carries, and the
  model predicting from exactly that fraction. Imports its drawing
  helpers, palette and font loading from
  `build_server_guide_figures.py` rather than copying them, so the
  two stay one set of conventions. The unit's markdown sketched this
  as Mermaid first; the drawn version exists because the diagram's
  point is proportion — the tall column of what you know against the
  small box of what you typed — which auto-layout flattens into
  equal-weight nodes. Regenerate before rebuilding the unit's docx.
  Requires Python with Pillow, the Public Sans faces, and its
  sibling script beside it. Command-line by the Entry 049 decision.

- `tools/build_site_pages.py` — assembles the site's HTML pages from
  `site/` into `docs/`, so the header, nav and footer live in one place
  rather than being copied into every page. Jekyll would do this and
  GitHub Pages runs it free, but it can only be checked locally with
  Ruby installed and a setup matching GitHub's, which would mean
  verifying pages after publishing rather than before — the wrong trade
  for this project. The output is plain portable HTML the preview
  renders identically. `{{root}}` resolves per page to the relative
  prefix that page needs, so the site works unchanged at a project URL,
  at a domain root, or opened from disk; root-relative links are
  rejected for breaking the first of those. **Nothing is written until
  every page passes every check**: no surviving `{{token}}`, no
  `<html>`/`<head>`/`<body>` inside a fragment, balanced tags, every
  local `href`/`src`/`srcset` resolving to a file that will exist, and
  every `#anchor` resolving to an id that exists on the page it points
  at — the last of which is what catches a page split silently breaking
  the old in-page links. It only writes the files named in
  `pages.json` and never deletes, since `docs/` also holds the
  stylesheet, fonts, icons and generated figures. `--check` verifies and
  reports drift without writing, for use before a commit; `--list`
  prints the page table. Requires Python, standard library only.
  Command-line by the Entry 049 decision — a build step, not a
  learner-facing tool.

- `tools/serve_site.py` — serves `docs/` for local preview with
  `Cache-Control: no-cache` on every response. Plain
  `python -m http.server` leaves browser heuristic caching in play, so
  the preview can render fresh HTML against a stale stylesheet — found
  2026-08-07, when a rebuilt page kept the previous CSS and the new
  theme toggle appeared broken when it was not. A preview that can
  silently show stale output fails the self-verification standard this
  project runs on, which is the whole reason this wrapper exists. Binds
  to 127.0.0.1 only; `.claude/launch.json` runs it for the in-app
  preview; port defaults to 8330. Requires Python, standard library
  only. Command-line by the Entry 049 decision.

- `tools/build_site_figures.py` — draws the landing site's data figures
  (the promise-versus-count strip, the BridgeAI delivery strip, and the
  OECD adoption gap by firm size) plus the 404 mark, as light and dark
  SVG variants into `docs/assets/figures/`, and the social-share card
  with `--og`. The first two are stat strips by decision, not shortcut:
  earlier drafts plotted courses against worker targets on a shared
  axis, performing the conflation the page criticises. Where two
  figures are in different units, the honest presentation separates
  them and names the missing number between them. The
  claim-verification flow and the practice-system diagram are
  deliberately not here: they carry no data, so they are native HTML in
  the page, built from the icon set — only content that is genuinely a
  chart gets drawn. Data is transcribed from logged findings with the
  entry numbers recorded beside the constants, per the data-driven
  figures rule, and every variant carries its own source-and-date line.
  Before writing anything it audits every palette pair the figures and
  site rely on against WCAG 2.1 AA contrast thresholds and refuses to
  build on a failure — the printed ratios double as the site's
  accessibility record. Standard library only for the SVGs; Pillow and
  the Public Sans faces are needed only for `--og`. Command-line by the
  Entry 049 decision — a build step, not a learner-facing tool.

- `tools/palette_check.py` — decides and verifies the colours charts are
  allowed to use. The brand palette was designed for a *page*: one accent
  and a set of near-white grounds. A chart needs something a page never
  did, several colours that stay apart **from each other** on one
  background, and the ways that fails are invisible to the person
  choosing them — red and green collapse into one colour for roughly one
  reader in twelve, and any categorical set collapses entirely in
  black-and-white print. Both are arithmetic, so both are checked here:
  WCAG contrast against each ground (3:1 for marks, per SC 1.4.11, not
  the 4.5:1 text uses), pairwise distance in OKLab, the same distances
  recomputed through Machado (2009) simulations of the three
  colour-vision deficiencies, and greyscale. **The pass mark is
  calibrated, not invented** — `--calibrate` measures the weakest pair in
  the Okabe-Ito colour-universal set and uses that, so a candidate is
  held to what an established safe palette actually achieves. Greyscale
  is reported but never enforced, because Okabe-Ito itself manages only
  dE 0.006 there; the honest response to a low number is a figure that
  direct-labels rather than a different palette. Holds the settled
  three-tier system (`--audit settled`): highlight-against-context for
  the ordinary case, five nominal categories per ground, and Ember→Ink /
  Ember→Sand ramps for ordered data, which are the only part that
  survives printing. Ordered ramps are audited on different criteria from
  categorical sets — adjacent steps in a ramp are *meant* to be close.
  `--solve` and `--proof` show the working: the constraint that decides
  everything is that a mark clearing 3:1 on both Paper and Ink must sit
  in a luminance band only 0.132 wide. Two defects reached the proof
  sheet past a passing audit — Paper against Mist at less than half the
  floor, and an optimiser returning Ember plus two blues because blue
  survives red-green CVD — so `--proof` is not optional polish; it is the
  step that catches what the numbers were not asked about. Requires
  Python, standard library only; `--proof out.png` additionally needs
  Pillow. Command-line by the Entry 049 decision.

- `tools/gap_chart.py` — the Vega-Lite layer, and the other half of
  `build_site_figures.py`. That one composes SVG by hand, every
  coordinate a literal and text wrapping a width estimate; it is right
  for the editorial stat strips it was written for and it cannot draw a
  chart, having no scales, axes or marks. This module supplies the
  brand theme, renders without a browser, and adds the furniture
  Vega-Lite has no opinion about. **The division is deliberate:
  Vega-Lite draws the plot, this draws everything around it** — the
  source line, the caveat, the editorial layout — because Vega-Lite is
  excellent at scales and poor at editorial furniture, and fighting it
  for the second would be worse than the hand-composed route. Palette
  comes from `palette_check.py` rather than a copy, so a colour
  correction reaches every chart; `TIER` names the sets by what they
  encode. Four self-checks, and each exists because the defect got
  through first: `_verify` refuses to write a chart that did not fully
  render, since Vega reports errors by printing and continuing;
  `check_labels` walks the rendered SVG accumulating transforms to find
  text that overlaps other text **or runs past the canvas edge** — the
  second was added 2026-08-12 after a source line was clipped on two
  different figures, a failure pairwise overlap structurally cannot see
  because a label running off the edge collides with nothing — and is
  advisory because its width estimate is
  approximate; `check_coverage` blocks a comparison the data cannot
  support, and is *not* advisory because counting categories involves
  no estimation; `check_glyphs` reads the rendered text against the
  font's character map and blocks on any character Public Sans cannot
  draw, because one missing glyph silently resets that whole text run
  in a fallback face — an arrow (U+2192) put a dozen labels in serif
  while every other check passed, and only looking at the render found
  it. `check_title` enforces the label/title rule as far as
  a machine can. Note that UK currency formatting is a **render-time**
  argument (`format_locale`) — setting `numberFormatLocale` in spec
  config is silently ignored and the axis comes out in dollars.
  Requires Python with `vl-convert-python`, which embeds its own
  JavaScript runtime: no Node, no browser, no network. It also
  rasterises plain SVG, which gives the repo an SVG-to-PNG converter it
  otherwise lacks on machines without Inkscape. A library, not a
  command.

- `tools/build_vram_figures.py` — the figures for
  `drafts/budget_vram_for_local_ai.md`, and the first built on
  `gap_chart.py`: a scatter of price against capacity, coloured by
  software stack, with the used RTX 3090 drawn as a range because the
  trackers disagree and averaging them would hide that. Kept here
  rather than in the chart module because figures belong with the
  document that argues from them, as the server-guide figures do.
  Builds clean as of 2026-08-11: the comparator research that blocked
  it (`research_log.md` Entries 070–071) priced a non-Intel card at
  every level and `check_coverage()` passes on real data — the
  refusal-first history is `project_log.md` Entry 066. Since
  2026-08-12 it also draws `vram_price_ladder`, the publishing-funnel
  form of the same table, built for the LinkedIn step where the
  scatter's axes-and-legend reading asks too much of a feed viewer:
  one dumbbell per card grouped by capacity tier, hollow marker at the
  launch price and solid at today's UK street price. **It is
  deliberately spare** — the first build carried a four-line subtitle,
  a three-line annotation beside every tier and a four-line footer,
  which is a blog post set in a PNG; the prose belongs in the post body
  and the image gets about a second in a feed, so everything that is
  not the comparison was cut. Launch prices are
  `research_log.md` Entry 078 and come in two bases the figure marks
  apart — vendor UK MSRP for consumer cards, US list converted plus
  VAT (asterisked) for the workstation cards, which have no UK RRP.
  Because the launch layer is one card thinner than the street layer,
  `check_coverage` runs on both and a thin launch level must be
  declared in `LAUNCH_GAP_NOTED` with the note the figure shows; an
  undeclared gap refuses the build. Since 2026-08-12 it also draws
  `vram_capability_ladder`, the capability side of the same argument:
  the two open models that fit a 24–32 GB card placed on Epoch AI's
  CC-BY capability index beside dated era anchors a lay reader has
  used — GPT-4, the free-ChatGPT models, o1 — because a composite
  score means nothing to the intended audience and time does
  (`research_log.md` Entry 079; design decisions `project_log.md`
  Entry 078). Its era labels are sourced product history, not colour
  (GPT-4 was the *paid* ChatGPT; the free tier ran GPT-3.5 until
  GPT-4o mini replaced it in July 2024), and `check_coverage` is
  deliberately not run on it — both columns sit on one shared scale,
  so there is no per-level category comparison to guard. Since
  2026-08-12 it also draws `vram_price_per_gb`, the simplest of the
  three and the one the creator picked for the post: one bar per card,
  £ per gigabyte, sorted cheapest first, with a notch marking what
  that card cost per gigabyte at launch. It is the only view that
  compares *across* capacities on one axis, which is what makes its
  title checkable from the figure — Intel's 32 GB card costs less per
  gigabyte than Nvidia's 12 GB one. Two things it has to answer in its
  own furniture: per gigabyte the small cards flatter the ranking,
  when capability moves in steps, so capacity is printed on every bar
  and the subtitle says a cheap 12 GB card still cannot run what 32 GB
  runs; and the converted-price asterisk belongs to the launch notch,
  not the street bar beside it, so the footer names the affected cards
  rather than marking the wrong number. Ranges sort on their low value,
  not their midpoint, because the eye ranks bars by where they end.
  `check_coverage` is not run on it, for the same reason as the
  capability ladder. Output is
  `assets/figures/vram_price_capacity.{svg,png}`,
  `vram_price_ladder.{svg,png}`, `vram_price_per_gb.{svg,png}` and
  `vram_capability_ladder.{svg,png}` plus dark variants.
  One defect class its checks cannot see: a second field on the y
  encoding channel silently deleted the visible price axis while
  every check passed — caught only by looking at the render, which
  is what the geometry rule is for. `--allow-gaps` remains for
  deliberately partial review builds and says in its own help that
  the result is not publishable.

- `tools/build_events_figure.py` — draws `uk_ai_events`, the timeline
  of UK AI events and what each one costs to enter, built on
  `gap_chart.py`. Written 2026-08-13 when the project started
  considering conferences as a route to the rooms its research argues
  about. Every row was read from the organiser's own site rather than
  from a search summary or an aggregator, and the two holes are
  recorded as different kinds: Birmingham Tech Week publishes no
  pricing where it could be reached, which is **not published rather
  than absent**, and AI UK 2027 has no announced date so it is left off
  the figure entirely rather than drawn at a guess. Three events were
  checked and dropped as past or defunct — the BridgeAI Annual Showcase
  (March 2026), AI Summit London 2026, and CogX, whose festival was
  wound down in 2025. London Tech Week is drawn as unpriced because its
  free early-career pass and £99.50 campus pass are **2026** prices
  against a 2027 date, and carrying one forward would be the quiet
  conflation the chart rules exist to catch. Travel and accommodation
  are deliberately not plotted — they dominate the real cost from
  outside the host city, but a defensible figure would need its own
  dated pricing pass, so the absence is stated in words per the bias
  checklist rather than estimated. `check_coverage` is not run, and the
  reason is in the code: every event sits at its own date, so each
  x level holds exactly one category by construction and the count
  would refuse every honest version of this figure. One defect its
  checks could not see: `align` and `dx` are mark properties, and
  Vega-Lite silently ignored the scales put on them, centring every
  cost label on top of its own marker — no check fires, because the
  labels neither overlap nor leave the canvas, and only looking at the
  render found it. Requires Python with `vl-convert-python`.

- `tools/build_appg_figure.py` — draws `appg_programme`, the APPG on
  AI's published two-year round-table calendar, built on `gap_chart.py`.
  Written 2026-08-13 from the group's own 2026-2027 programme brochure.
  The finding is narrow and checkable: the brochure's themes page names
  "AI Skills and Workforce Preparedness" as a key area, and none of the
  fourteen sessions is dedicated to it — stated flat and left there, with
  the subtitle conceding that the January 2027 robotics session *does*
  ask about skills gaps, so the claim is about a session of its own
  rather than an absence of interest. All fourteen are plotted so the
  count in the title can be checked against the figure. Three decisions
  worth knowing: quarterly Advisory Board meetings are excluded as
  internal governance, since counting them would inflate the denominator
  the title rests on; colour encodes only held-versus-scheduled, because
  the brochure's own eight themes exceed the five the categorical
  palette can hold apart and collapsing them would mean inventing a
  taxonomy the source does not use in order to fit a colour limit; and
  **the brochure contradicts itself** on the environment session, dating
  it 10 October 2027 on the detail page and 18 October in the overview
  table — the later date is plotted and the discrepancy is printed on
  the figure, because silently picking one of two published dates makes
  an editorial call the reader cannot see. Requires Python with
  `vl-convert-python`. Its internal counterpart, the priority calendar
  that ranks these against other events, is indexed in `internal/`.

- `tools/build_site_replica.py` — keeps the landing site's terminal
  replica verbatim-true to the tool it pictures: runs the real figure
  build, captures its output, rewrites the replica spec and renders it
  through `tools/replica.py`. The landing page does not currently show
  the replica (tried in the system section, removed as a distraction
  mid-argument); the asset is kept for a learning-unit page. Exists
  because a hand-synced spec drifted once (a shell-mangled backslash put
  a control character into the pictured command); `--check` compares the
  stored spec against a fresh run without writing, for use before
  commits that touch the figure script. Run after every figure-script
  change. Command-line by the Entry 049 decision.

- `tools/build_site_fonts.py` — builds the landing site's web fonts:
  subsets the locally installed Public Sans faces to the five WOFF2
  files in `docs/fonts/` (400/400-italic/600/700/800, Basic Latin +
  Latin-1 + General Punctuation, ~200 KB total), so the site serves the
  brand face itself with no font CDN and nothing beyond
  `font-src 'self'`. Refuses to build unless the OFL licence text is
  present beside the outputs (`docs/fonts/LICENSE.md`, from the
  upstream Public Sans repository), and reopens every artefact to probe
  the characters the site's copy depends on (£, dashes, curly quotes)
  before accepting it. Adding a weight to the stylesheet means adding
  its face here and re-running. Figure SVGs are excluded by design:
  browsers fetch no external fonts for `<img>`-embedded documents, so
  figure text stays on the viewer's installed fonts. Requires Python
  with fontTools and brotli (`pip install fonttools brotli`) and the
  Public Sans TTFs installed. Command-line by the Entry 049 decision.

- `tools/build_linkedin_banner.py` — composes the profile-banner
  export and the project's 1280×640 social cards (repository social
  preview, LinkedIn entry media) from the brand assets. Two generated
  banner styles — the abstract Sand-over-Ink split (default since
  2026-08-12, the creator's pick from rendered concepts after seeing
  the first design live) and the Ink-dark wordmark-and-symbol design
  (`--style symbol`; `--svg` composes that one over an SVG base
  instead) — and dark/light card themes, with text set in Public Sans
  and bounds-checked. The redesigns retired the original radar-motif
  SVG. Placement is enforced
  in code because the platforms' presentations can silently delete a
  hand-placed identity — LinkedIn's mobile view keeps roughly the
  centre two-thirds of the banner canvas, and the desktop layout lays
  the profile photo over the lower left — and the wordmark's ~160 px
  minimum usable width is checked at output size. Refuses to write on
  any failed check; renders still get a human read afterwards, per
  the geometry rule. Banner outputs live beside the other profile
  assets outside the tracked tree; the social cards are tracked in
  `assets/social/`. Requires Python with Pillow and the Public Sans
  faces; `vl-convert-python` (via `gap_chart`) only for `--svg`.
  Command-line by the Entry 049 decision — a build step, not a
  learner-facing tool.

- `tools/build_profile_photo.py` — recomposes a headshot over brand
  grounds: cuts the subject out with rembg's locally-run U²-Net model
  (a personal likeness never goes to a web background-remover — the
  photo stays on the machine, which is the tool's reason to exist),
  then composes variants on Sand/Mist grounds with the Ember rule
  behind the subject, the Sand-over-Ink split, and a plain control,
  each with a circle-crop preview and a labelled contact sheet to
  choose from. Never upscales — invented pixels on a face are the
  exact "AI-generated" look the recompose avoids. Checks alpha
  coverage for failed segmentation; edge quality is judged by reading
  the sheet, per the geometry rule. Outputs carry a likeness: keep
  them under `internal/`, never tracked. Requires Python with Pillow
  and rembg (`pip install "rembg[cpu]"`). Command-line by the Entry
  049 decision. Added 2026-08-12.

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

- `tools/stage_subset.py` — stages part of one file's uncommitted
  additions, so two unrelated sets of changes to the same file can be
  committed apart rather than bundled. It exists because the file-sync
  layer over this repo does not merge (see Git conventions): a sync can
  leave one tracked file holding this machine's additions alongside
  another machine's, and `git add -p`, the ordinary answer, cannot be
  driven by the harness Claude runs under. The subset is described by
  what to leave out — `--drop` for line prefixes, `--drop-from` to cut
  to end of file — because the lines to exclude are the identifiable
  ones: a source-key tag, an entry heading. **It refuses anything it
  cannot do safely:** a file carrying deletions against HEAD, where
  "drop these added lines" is ambiguous; a path with changes already
  staged; a pattern that matched nothing; a subset identical to HEAD or
  to the working tree; a bare LF introduced into a CRLF file. After
  staging it reconciles the split and fails loudly if staged plus
  unstaged additions do not equal the original count. Stages through
  `git hash-object -w --path` so the repo's own CRLF clean filter
  applies, since without `--path` the blob differs from HEAD in every
  line. Never modifies the working tree and never commits, so reviewing
  `git diff --cached` stays a separate step. `--dry-run` reports the
  split without touching the index. Requires Python, standard library
  only. Command-line by the Entry 049 decision.

- `tools/sync_memory.py` — mirrors Claude Code's machine-local memory
  into `internal/claude_memory/<machine>/`, so it survives the move
  between laptop and desktop. Resolves the memory folder from the
  repository path rather than a remembered one, since the 2026-08-03
  orphaning happened when that path changed. **Writes one folder per
  machine and never touches another's**, because the sync layer does
  not reconcile and a shared folder would let one machine's sync erase
  the other's memories. It refuses rather than guesses: no `internal/`,
  no memory folder for this project (reporting every path searched),
  a destination escaping the mirror root, or a mirrored file *newer*
  than its local counterpart — that last one means the mirror holds
  something this machine does not, so it is reported and skipped until
  `--force`. Deletion is never propagated, since "gone from this
  machine" and "should be gone everywhere" are different statements.
  `--status` lists every machine's mirror and names what the other one
  holds; `--dry-run` reports without writing. Requires Python, standard
  library only. Command-line by the Entry 049 decision — housekeeping
  at a session boundary, not a learner-facing tool.

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

- **A mirror of that memory in `internal/claude_memory/<machine>/`,
  one folder per machine.** Adopted 2026-08-15 at the creator's
  direction, who moves between laptop and desktop constantly and was
  losing memory and fighting the sync at every switch. `internal/`
  already travels between machines by file sync, and it is gitignored
  and hook-blocked, which suits material that is behavioural and about
  the creator's own environment. `tools/sync_memory.py` writes it.

  **One folder per machine is load-bearing, not tidiness.** The sync
  layer copies whichever version of a file it saw last and does not
  reconcile, so a single shared folder would have the second machine's
  sync silently overwrite the first machine's memories — a worse loss
  than the one the mirror prevents. Each machine writes only its own
  folder. `--status` names what the other machine holds and this one
  does not, which is the reason to run it on arrival.

  This does not supersede the 2026-07-24 decision above. Memory still
  stays out of the *tracked* repo; the mirror is untracked by
  construction. Nor does it replace the extraction pass below: mirroring
  a rule is not capturing it, and anything durable and project-level
  still has to reach this file to travel on the repo's own.

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
**Last run: 2026-08-15.** Nineteen memory files under the current
project path, one more than the last pass counted. Seventeen are
already captured here, or correctly machine-local on the reasoning the
earlier passes recorded, and re-reading them changed nothing. The two
that stay out of this file stay out: `user_hardened_firefox` (the
creator's own environment, not a project rule) and
`project_floated_folder_unit_and_tool_spinout` (three undecided
candidates — the repo logs decisions, not options, and one of them
references an internal contact's work). **Not promoted is no longer
the same as not preserved**: the creator judged both worth keeping as
context, and the same day's memory mirror puts every file in
`internal/claude_memory/`, so a decision to leave something out of the
tracked repo no longer risks losing it at the next machine switch.
**One genuine gap, and the previous pass had it in front of it.**
`feedback_no_autonomous_sending` was written at 09:01 on 2026-08-14 and
the pass that ran later that morning reported eighteen files, so it was
either missed or wrongly counted among the captured. It was not
captured: this file carried no general rule against sending, only three
narrower ones scoped to the internal contacts register, to infographics
and to posting the site link. Promoted above as the outward-sending
rule. The lesson is the one the standing task exists for — a rule
living only in local memory does not travel between machines, and a
file count is not an audit.
Previous line, kept for the record:
**Last run: 2026-08-14.** All eighteen memory files under the current
project path were audited — the count is up because the memory system
has been writing steadily, not because anything was missed before.
Sixteen are already captured here: the interaction rules (ask don't
probe, PowerShell aliases, plain language, model-fit flagging,
proactive tool recommendations, missing-tool flagging, vector-editing
handoff, SVG layer naming, self-check tooling, early-rules-deliberate),
the git rules (commit review, no auto-push), the prose rules
(understatement, voice matching), the OOXML constraints, and the
command-understanding ethos. Two are correctly machine-local and stay:
`user_hardened_firefox` (the creator's own environment, not a project
rule) and `project_floated_folder_unit_and_tool_spinout` (three
undecided ideas — the repo logs decisions, not candidates, and one of
them references an internal contact's work).
**One genuine gap, and it was the day's own evidence that found it.**
`feedback_voice_matching` carries "break comma- and dash-stacked
sentences into two or three short direct ones", which the repo only
covered for commit messages and site copy — not for unit prose, where
two consecutive revision passes on the pilot unit showed it was the
creator's dominant edit. Promoted above as the em-dash apposition rule.
A second rule came from the session rather than from memory: the
canonical-hand-edit reconciliation loop, also above. A third candidate
— units taking a short title plus a subtitle — was **deliberately not
added**, being already recorded in the `md_to_docx.py` index entry and
enforced by the converter; the bias-checklist warning against growing
rule lists applies to this file too.
Previous line, kept for the record:
**Last run: 2026-08-13.** All three memory files under the current
project path were audited and none needed migrating — the fourth
consecutive pass with that result, which is now the expected outcome
rather than a finding. `public-guidance-wording` is machine-local by its
own explicit terms. `feedback-teach-in-house-style` asks whether its
CLAUDE.md rule landed, and it did: the markdown-first lessons rule of
2026-08-09. `feedback-prose-register-ai-tells` asks whether the
paired-rewrite register session's output reached the repo, and it has
not — `project_log.md` Entry 079 records that session as agreed rather
than run, so that memory remains the live record and must stay.
Everything durable came from the session instead: three rules promoted
(read the sent record before drafting a follow-up; text read from an
image is not the text; a completed evidence base still needs checking
against the operating questions) and two research entries logged from an
external technical exchange (Entries 082-083).
Previous line, kept for the record:
**Last run: 2026-08-11.** Both memory files under the current project
path were audited. `feedback-teach-in-house-style` is already captured
here as the markdown-first lessons rule adopted 2026-08-09 — the memory
itself says to check whether that rule landed before treating it as the
only record, and it did. Its one uncaptured element, a preference for
skimmable chat formatting, is interaction-level and stays machine-local
by the same logic that kept agent-spawning and tool preferences there.
`public-guidance-wording` is machine-local by its own explicit terms and
must remain so. So local memory again contributed nothing needing
migration, the third consecutive pass with that result; the pattern is
now consistent enough to treat as the expected outcome rather than a
finding. Everything durable came from the session: two rules promoted
into Working approach (a chart takes the finished-research bar rather
than its source document's; a chart title states the finding), an
extension of the geometry-self-check rule to cover charts, and index
entries for `gap_chart.py` and `build_vram_figures.py`.
Previous line, kept for the record:
**last run 2026-08-06.** That pass confirmed the five pre-move memory
files are all captured in the repo already (short pasted fragments,
community-built tools, the government-recognition goal in
`project_brief.md`, the research workflow, and agent-spawning now
enforced by harness configuration), so nothing needed migrating from
them. They remain orphaned under the old project path and no longer
load in any session. The current path holds one file, on wording public
guidance, which stays machine-local by its own logic. Four rules were
promoted out of the session itself rather than out of memory: feedback
produces a revised draft, claims are re-read from their log entry
rather than recalled, generated visual assets get a geometry
self-check, and both logs are CRLF on append. The structural finding
repeats the last pass's: local memory contributed nothing this time,
and everything durable came from the working session.
Previous line, kept for the record:
**last run 2026-08-03.** That pass found the memory system had been
silently out of service: all six files sat under the *old* project path
(`C--Users-ThinkPad-Documents-grounded-ai-practice`), orphaned when the
repo moved to `C:\dev\`, so no memory had loaded since the move and the
`.claude-memory` junction resolved to nothing. Two items were promoted
into this file — the short-pasted-fragments rule (Working approach) and
an extension of the tool-surfacing bullet to cover community-built
Claude Code tools. Two were already fully captured (the research
workflow here, the government-recognition goal in `project_brief.md`)
and one is now enforced by harness configuration (agent-spawning). The
structural finding matters more than any single item: local memory did
not survive a folder move on one machine, which is the strongest
evidence yet for keeping durable rules in the repo.
Previous line, kept for the record:
**last run 2026-07-31.** That pass audited all six memory files and found
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
