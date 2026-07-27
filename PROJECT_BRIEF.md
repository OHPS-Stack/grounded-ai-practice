# Grounded AI Practice

**Practical AI capability through responsible, hands-on learning.**

*An accessible, research-led learning project for using, evaluating and
building with local, cloud and hybrid AI systems.*

## Document status

Research-stage working brief.

This document records the project direction currently agreed by its creator.
It is intended to orient early research and experimentation. It is not a
finished product specification, curriculum, business plan or claim that the
underlying problem has already been fully validated.

## Purpose

Grounded AI Practice explores how people can develop practical, responsible
and transferable AI capability through a combination of research, guided
learning and hands-on projects.

It is intended to make AI concepts and systems more understandable without
assuming that every learner is—or intends to become—an AI engineer.

## Problem being investigated

AI systems are becoming increasingly accessible across work, education and
daily life. Many users and organisations can now adopt powerful AI tools
without first developing a strong understanding of:

- their capabilities and limitations;
- appropriate verification and human oversight;
- privacy, security and ethical risks;
- cost and operational trade-offs;
- context, retrieval and tool-connected workflows;
- when local, cloud or hybrid approaches are appropriate;
- how to evaluate whether an AI-enabled process is genuinely effective.

This may create both missed opportunities and unsafe, ineffective or
over-dependent forms of adoption.

This problem statement is a working hypothesis. Its scale, affected audiences
and implications must be tested against credible evidence rather than assumed.

## Project response

Grounded AI Practice is a personal and open-ended attempt to investigate that
problem through:

- research into AI skills, adoption, education and responsible practice;
- comparison of existing learning platforms, frameworks and programmes;
- development of practical competency and learning models;
- hands-on experiments with local, cloud and hybrid AI systems;
- accessible explanations of the concepts behind those systems;
- prototypes that test different ways of teaching and applying AI capability.

The project does not claim to provide a universal solution to AI upskilling.

## Intended accessibility

The project should support readers with different goals and technical starting
points.

Potential users may include:

- people seeking stronger everyday AI literacy;
- students and career changers;
- workers adapting to AI-assisted roles;
- technically curious learners;
- educators and trainers;
- small teams or organisations evaluating AI adoption.

These groups are provisional. Research may show that the project needs a
narrower initial audience.

## Primary audience (working decision — 24 July 2026)

Based on research to date, the project's creator has made an explicit —
but still provisional and open to revision — decision to prioritise:

- individuals seeking practical, everyday AI literacy (general public), with
- particular attention to employees at small organisations who lack the
  employer-provided L&D infrastructure that existing frameworks assume.

This combines the broadest-reach model with the most clearly evidenced access
gap found so far. Both PRIMES (`SE-WHATWORKS26`/`SE-PRIMES-EMPLOYER26`) and the
UK AI Skills Hub (`AISKILLSHUB`) are designed around an *employer* rolling out
training to staff; individuals at small organisations without that layer —
alongside the wider general public — are not well served by that model.
Elements of AI (`EOAI`) demonstrates an individual-facing, vendor-neutral
approach can reach large numbers without needing an employer sponsor.

This decision does not resolve every open question under Priority 2 in
RESEARCH_QUESTIONS.md (e.g. barriers and needs specific to this combined
audience, or whether "small organisation employees" should later be split
into narrower sub-groups). It is marked explicitly as a working decision,
subject to change as research and prototyping continue — consistent with the
project's stated approach of not treating early decisions as fixed
governance.

## First public output (working decision — 24 July 2026)

Based on research to date, the project's creator has made an explicit — but
still provisional and open to revision — decision on what to build first:

A **single pilot learning unit**, not a roadmap, full course, repository or
website. Specifically:

- one core practical AI capability, not a full curriculum;
- sized to PRIMES' "Modular" criterion (`SE-PRIMES-EMPLOYER26`) — roughly
  30–90 minutes, stackable, with a clear entry point;
- sequenced using the Gradual Release of Responsibility pattern
  (`GRR-EBIP`): explicit modelling/worked example → guided practice →
  independent practice → reflection;
- tested with a small number of real learners before any wider structure,
  content library or platform is built.

This follows the Royal Society review's pilot-first recommendation
(`RS-AILIT25` — evaluate before scaling, though that source's own evidence
base is scoped to school-age learners, not adults) and directly avoids the
"directory not programme" failure mode documented in the UK AI Skills Hub
critique (`LSE-CARDOSO26`, `TECHOSAURUS26`, `HUMANCO26`): one small, coherent,
well-sequenced unit is a stronger test of the project's learning-design
assumptions than a broad but shallow first release.

This decision answers *what shape* the first test should take. See
"Pilot unit core capability" below for *which* capability it teaches.

## Pilot unit core capability (working decision — 26 July 2026)

The project's creator has decided the pilot unit's core capability:
**effective prompting**, working title **"Effective prompting — what's
really happening when you hit send."**

Chosen from four evidenced candidates researched in `RESEARCH_LOG.md`
(Entries 039–040): critical evaluation of AI output, effective prompting,
a working capability/limitation mental model, and responsible/safe use of
data. The rationale: prompting gives the unit a concrete way to show the
gap between what a learner types and what the model actually does with the
input, teaching an immediately usable skill while also touching on backend
model behaviour — rather than treating "how AI works" as separate
prerequisite content.

This is a deliberate scoping choice, not a claim that responsible-use or
evaluative content matters less — the unit still centres on a practical
"production" skill (what to say to AI) rather than the project's stated
responsible-use/verification framing. Responsible/safe use of data remains
a plausible second unit if the project stacks further pilots later. See
`RESEARCH_LOG.md` Entry 047 for the full decision record.

## Second track: local AI workstation (working decision — 24 July 2026; deferred 24 July 2026)

**Status: deferred.** The creator has confirmed this track is not active
work for now — it remains a confirmed future direction, not the project's
current focus. Do not propose building or drafting workstation-track content
until the creator explicitly reopens it.

Alongside the general-literacy pilot above, the project's creator has
confirmed a second, parallel learning track aimed at a more technically
curious audience (already named as a possible persona under "Intended
accessibility"): building and understanding a personal local/hybrid AI
workstation.

This track is explicitly separate from, not a replacement for, the
general-literacy pilot — the pilot remains the project's first tested output.
The workstation track's own first module is expected to cover terminal/shell
fundamentals (PowerShell, WSL2/Ubuntu shell), since the intended architecture
(see "Inherited workstation architecture" below) depends on that foundation
before Docker, Ollama, Open WebUI and later components become accessible.

This working decision does not yet fix the workstation track's detailed
curriculum, sequencing, or relationship to the general-literacy pilot's
content (e.g. whether the two tracks share any foundational modules) — those
remain open.

## Visual identity (working decision — 24 July 2026)

The project's creator has finalised an initial colour palette and logo
direction for Grounded AI Practice:

- **Logo type:** icon + wordmark (not a wordmark-only mark).
- **Tone:** between "grounded/academic" and "approachable/friendly" —
  credible and evidence-led without reading as dry, institutional or
  intimidating to the pilot's general-public/SME audience.
- **Palette** (six colours, roles noted):

| Name | Hex | Role |
|---|---|---|
| Ink | `#27221E` | primary text, dark surfaces (nav/header) |
| Ember | `#F15E4B` | primary accent — buttons, links, highlights |
| Sand | `#F9E8DC` | light warm section background/tint |
| Paper | `#F9F9F9` | main page background |
| Mist | `#EFEEED` | secondary/alt background |
| Sage | `#D5E2E1` | soft secondary section background |
| Stone | `#6E6E6E` | neutral grey — added 24 July 2026, no warm/cool lean by design (unlike every other colour in the palette, all warm-leaning). Realised use: secondary wordmark text ("AI"/"PRACTICE") in the reversed logo variants. |
| Graphite | `#404040` | darker neutral grey — added 24 July 2026, same zero-lean character as Stone. Realised use: the "GROUNDED" wordmark accent and icon underline in the monochrome logo variants, standing in for Ember where no brand colour is wanted. |

**Status: FINAL.** The palette, logo type, logo symbol, wordmark and icon
set are all **promoted, finished working assets** (symbol/icons promoted
24 July 2026; wordmark and variant set built the same day; final
typographic polish — real typeface, kerning, path-conversion — completed
by the creator in Inkscape 24 July 2026). No outstanding visual-identity
work remains at the direction level.

**Logo** (`assets/brand/logo/`):

- `logo_symbol.svg` — **the logo**, default/primary version. Gradient-shaded
  (book-cover gradient, spine shadow, page depth, rounded highlight on the
  Ember bar) for the 3D/book effect that earlier AI-iterative curve edits
  couldn't satisfyingly achieve. Base palette is still Ink/Ember/Paper;
  gradient stops are tasteful variants around those for the shading effect,
  not deviations from the locked palette.
- `logo_symbol_flat.svg` — flat-colour sibling (Ink `#27221E` / Ember
  `#F15E4B` / Paper `#F9F9F9`, no gradients), for contexts needing flat
  reproduction (favicon, single-colour, print, etc.). All variants below
  derive from this flat version, not the shaded one — gradients don't suit
  monochrome/reversed utility variants, which prioritise clarity over
  polish.
- `logo_symbol_mono.svg` — single-Ink version (Ember underline recoloured
  to Ink) for one-colour print/embossing.
- `logo_symbol_reversed.svg` — white-on-dark version, specifically designed
  for **Ink-coloured backgrounds**: body white, chevron/cursor Ink, Ember
  underline kept as the surviving accent, page-fill area explicitly
  Ink-coloured (a deliberate creator choice made during final polish,
  superseding the original transparent-page-fill design — no longer
  intended to work on arbitrary dark backgrounds, only Ink specifically).
- `logo_lockup_horizontal.svg` / `logo_lockup_vertical.svg` (+ `_mono` /
  `_reversed` for each) — icon + two-line wordmark ("GROUNDED AI" /
  "PRACTICE"), side-by-side and stacked. All wordmark text is now real
  vector paths (Public Sans, converted to outlines in Inkscape) — no font
  dependency remains, consistent with every other text element in the
  brand system. **27 July 2026:** the "page" strip and terminal
  chevron/cursor across `logo_symbol.svg`, `_flat`, `_mono` and all four
  non-reversed lockups were found using Paper (`#F9F9F9`) rather than pure
  white for what's actually a background-matching backing element — same
  issue as the icon-set check below, fixed the same way (corrected to
  `#FFFFFF`; `logo_symbol_reversed.svg` and its lockups were left alone,
  since that variant's Ink page-fill is a confirmed intentional choice, not
  this bug). The two full-colour lockups (`logo_lockup_horizontal.svg`,
  `logo_lockup_vertical.svg`) were originally built from the flat symbol
  geometry rather than the shaded one, so they had flat fills and no spine
  shadow — fixed 27 July 2026 by carrying the exact `bookGrad`/`spineGrad`/
  `emberGrad` gradients and the missing spine-shadow path across from
  `logo_symbol.svg` (book-shape geometry confirmed identical between the
  two, so this is a direct reuse, not a reconstruction).
- `png/` — raster exports, regenerated from final SVGs: symbol and symbol
  variants at 32/64/128/256/512/1024px; lockup variants at 256/512/1024px
  width. All transparent background.
- `profile_picture_square.svg` / `profile_picture_circular.svg` — avatar
  treatments for social/profile use (the circular one specifically for
  GitHub, which auto-crops square uploads to a circle anyway, but this
  file is a true circle with transparent corners for platforms that
  don't). **Redesigned 27 July 2026** per a creator-supplied reference
  image: Ink (`#27221E`) background (was Paper), a Paper ring set flush
  with the outer edge (was a thick Ink ring inset from the edge), and the
  **reversed** logo symbol (white book, Ink chevron/cursor, Ember
  underline) centred on top rather than the shaded/normal-colour symbol —
  the reversed variant's `page_fill` is already Ink, so it disappears
  seamlessly into the new background by construction. The book has a
  subtle depth treatment reusing `logo_symbol.svg`'s spine-shadow
  technique, deliberately narrowed to stay clear of the chevron rather
  than washing across the whole cover. Icon sized slightly larger on the
  square version than the circular one, matching the prior convention.
  PNGs at 256/512/1024px.

All symbol geometry reuses the approved PAWH "terminal + handbook" mark
(an open-book/journal shape containing a terminal prompt chevron and
cursor), refined directly in Inkscape by the creator with proper corner
fillets.

**Wordmark, final treatment:** two-line "GROUNDED AI" / "PRACTICE" set in
**Public Sans**, tightened letter-spacing on "GROUNDED," converted to
outline paths. A two-tone hierarchy was added across every variant during
final polish: **"GROUNDED" always takes the variant's most prominent
tone** (Ember in the full-colour and vertical full-colour lockups,
Graphite in the monochrome lockups, white in the reversed lockups), while
**"AI" and "PRACTICE" take a quieter tone** (Ink in full-colour/mono,
Stone in reversed) — this is the intended, primary use case for Stone and
Graphite, not just the "sparing use" originally anticipated when they were
added to the palette.

**Icon set** (`assets/brand/icons/`, promoted 24 July 2026, recolour
completed the same day): 36 content icons, flat (no batch subfolders),
snake_case names, with an `svg/` source folder, a `png/` folder (64/128/256px,
transparent), and a `README.md` manifest listing every icon and its topic.
Recoloured from the superseded navy/orange palette to the current one
(`#0F1C2F`→Ink `#27221E`, `#FF5A1F`→Ember `#F15E4B`, assorted light
greys→Sage `#D5E2E1`), verified with no old colours remaining, and manually
checked by the creator — all render correctly. This is a distinct system
from the logo symbol above — the icon library is illustrative content
icons, not the brand mark.

During recolour, four icons were flagged for construction issues beyond
colour and fixed: **Vector Database and Embeddings** had a non-standard
1254×1254 viewBox — normalised to the set's standard 512×512 via a single
wrapping `scale()` transform, no path coordinates touched, pixel-identical
output. **Quote Callout** had a stale desc note claiming it needed
CairoSVG specifically — corrected, since its paths use only plain
line/close commands with no renderer-specific features. **Cloud AI** had
two paths sharing identical coordinates by design (an ink ring plus an
explicit white fill needed so the icon works on non-white backgrounds) —
added a comment so this isn't mistaken for accidental duplication and
"simplified" incorrectly later. **API and MCP** used a live `<text>`
element for "API," the only icon in the set built that way — removed, then
the creator hand-set the type directly in Inkscape's text tool and
converted it to a vector path (Path > Object to Path), so it's now true
outline geometry with no font dependency, consistent with every other icon
in the set. Four further icons (Tools and Configuration,
Backup and Recovery, Updates and Maintenance, Learning and Documentation)
were flagged only for having unusually high past revision counts, not any
identified defect — cleared by the creator's manual visual review, no
changes made.

**Consistency refinement pass (27 July 2026):** the creator noticed icons
read as inconsistent sizes despite identical PNG dimensions. Measured
directly (Inkscape's geometry query against each icon's actual drawn
content, not just the declared viewBox): fill-ratio — how much of the
512×512 canvas each icon's content actually occupies — ranged from 0.48 to
0.90 across the set (median 0.64). Every icon was normalised to a 0.70
fill-ratio target via a uniform scale-and-recentre transform (aspect ratio
preserved, no path coordinates touched), the same low-risk technique
already used for the Vector Database viewBox fix. Stroke width was left
alone except for four single-stroke outliers the creator specifically
approved (Information 16→14, Architecture 12→14, Troubleshooting 10→14,
plus Verification's border 16→14 and Tip's speech-bubble outline 11→14,
matching the set's de facto 14-weight standard) — icons mixing multiple
stroke weights deliberately (bold outline + thinner inner accent) were
identified and left as intentional hierarchy, not flattened. Separately,
the creator identified that Ink/Paper used as *background-matching backing
fills* (rather than genuine structural colour) don't actually blend with a
true-white document page, since Paper (`#F9F9F9`) isn't pure white. This
was checked across both icons and logo: Cloud AI's interior backing fill
was already correct (pure white, `#FFFFFF`, from its original
construction); Vector Database and Embedding's database-stack fill was
likewise already pure white, but its circular badge-background element is
a deliberate exception the creator wants kept page-tinted rather than pure
white, so it stays Paper on purpose. Wordmark text and genuine
structural/complementary colour use (e.g. icon linework itself) were
explicitly out of scope for this check. All 36 icons' groups/layers were
also labelled in snake_case for editability (individual paths intentionally
left unnamed) — see `RESEARCH_LOG.md` for the full session record.

**Workflow note (24 July 2026):** fine curve-level refinement of the logo
symbol was attempted through iterative AI-described feedback (screenshot
annotation → prose correction, repeated) and the creator found this
arduous and unproductive — a repeat of a discouraging pattern from PAWH.
The creator moved to editing directly in Inkscape and this worked well:
the resulting `logo_symbol.svg`/`logo_symbol_flat.svg` are a clear
improvement over anything produced through the described-feedback loop.
Future sessions should treat files in `assets/brand/logo/` and
`assets/brand/icons/` as potentially edited outside this workflow at any
time — re-read fresh rather than assuming last-known state — and should
not propose resuming AI-iterative curve editing; support concept-level
exploration instead, or integration (palette-fidelity checks, format/size
variants, documentation) once the creator brings back a manually-refined
version, as happened here.

## Inherited workstation architecture (PAWH reference)

The following summarises the local/hybrid AI workstation as originally
scoped during the PAWH predecessor project, provided by the project's
creator on 24 July 2026 from their own prior work in a separate ChatGPT
project. It is recorded here as **historical intent to evaluate**, per the
"Relationship to PAWH" section below — not a specification the project has
committed to building as described, and not all named tools are confirmed
choices going forward.

**Core concept:** a small, modular, understandable AI platform on a normal
Windows gaming PC, local-first rather than local-only — local AI for privacy,
control, offline use and routine workloads; cloud AI for stronger reasoning
and specialist tasks; hybrid workflows combining both deliberately. Also
conceived as a learning project in its own right, teaching transferable
skills in operating systems, terminals, Linux, containers, networking,
storage, security, Git, APIs and AI infrastructure.

**Intended baseline architecture:** Windows 11 host running Windows
Terminal (PowerShell and WSL2/Ubuntu), with Docker Desktop/Engine and Docker
Compose orchestrating local services — initially Ollama (model serving) and
Open WebUI (chat interface), with SearXNG (metasearch), Whisper (speech
recognition) and Qdrant (vector storage) considered as part of the wider
early architecture. Git/GitHub for version-controlling configuration and
scripts throughout.

**Planned later modules**, roughly in order of consideration:
- document ingestion, embeddings and RAG (via Qdrant), with explicit
  attention to what gets indexed, where derived data lives, how chunking
  affects answers, and how to verify retrieved information actually
  supports a given answer;
- voice interaction (Whisper speech-to-text, text-to-speech), kept as an
  optional module rather than a core dependency;
- model routing/selection — matching task to the right-sized model (fast
  local model for routine work, larger local model for demanding/private
  tasks, coding-specific models, cloud models when local capability is
  insufficient) rather than assuming one model suits every task;
- automation and visual workflow tools (Langflow, n8n) for scheduled/
  event-driven tasks and reusable prompt/workflow templates, introduced
  only after the underlying services and their security implications were
  understood;
- MCP-style integrations connecting models to files, scripts, APIs,
  databases and other services — explicitly taught as **trust boundaries**
  (what an integration can read/modify, which credentials/network access it
  has, how to roll it back), not merely productivity features;
- optional image/media generation as an experimental extension, not a
  baseline requirement.

**Remote access** was deliberately deferred: local binding by default,
trusted-device/private-network or VPN-style access rather than exposed
ports, with public exposure explicitly out of scope for the initial build.

**Storage/maintenance** expectations: roughly 200–400 GB allocated for
models, containers, vector data, documents, configuration, logs and
backups, with explicit persistent-data locations, cleanup routines, backup/
restore procedures, and rollback before risky changes.

**Target hardware:** a Windows 11 desktop (Ryzen 7 7800X3D, Radeon RX 7900
XT/20GB VRAM, 32GB DDR5) also used for gaming — services were intended to
run on demand and stop cleanly (e.g. via Docker Compose profiles) so gaming
performance wasn't compromised.

**Security/maintainability defaults considered:** bind locally unless
remote access is deliberately needed; prefer VPN/private access over public
ports; least privilege; credentials kept out of Git (`.env.example`
placeholders only); version-controlled configuration; backups before major
changes; incremental, verified, rollback-capable changes; understand
commands before running them — consistent with this project's own stated
"commands should never be blind copy-paste" rule.

**Status at time of PAWH work:** an intended, evolving architecture, not a
completed build. Windows 11 was in use and Ollama had been installed
(configuration not confirmed correct); WSL2, Ubuntu, Docker Desktop, Open
WebUI and most other named services had not yet been installed. The named
products were a practical starting point, not fixed permanent choices —
consistent with this project's stated approach of not treating early
decisions as fixed governance.

## Central practical idea

Building and operating a small AI-enabled workflow or system can provide a
valuable hands-on learning environment.

The exact project does not need to be identical for every learner. Depending
on their needs, it might involve:

- improving research and prompting practices;
- evaluating common cloud AI tools;
- building a local AI workspace;
- comparing local and cloud processing;
- designing a hybrid workflow;
- experimenting with retrieval, tools or automation;
- applying responsible-use and verification methods to a workplace task.

The local AI workstation concept from the earlier PAWH project may therefore
survive as one possible learning pathway, but it no longer defines the whole
initiative.

## Current scope of research

The project currently needs to investigate:

- UK AI skills, education, employment and adoption;
- public and organisational AI literacy;
- recognised competency and learning frameworks;
- project-based and experiential learning;
- comparable platforms such as roadmap.sh and LeetCode;
- practical AI evaluation and responsible-use methods;
- context engineering, RAG, MCP, memory and agent tools;
- information architecture for people and AI retrieval;
- the appropriate first public output and delivery format.

## Not yet decided

The project has not yet determined:

- its primary audience beyond the working decision recorded above (still open:
  narrower sub-group definition, and confirmation the decision holds as
  research continues);
- its eventual permanent format (guide, roadmap, course, website, software
  tool, repository, or a combination) — the working decision above only
  fixes the shape of the *first pilot test*, not the project's long-term
  format;
- its final curriculum or competency levels;
- its permanent repository structure;
- its long-term document and data architecture;
- whether it should eventually become a commercial, community or purely
  personal initiative.

Visual identity (palette, logo type, tone, logo symbol, icon set, wordmark)
is no longer an open question — see "Visual identity" above, status FINAL
as of 24 July 2026.

These questions should remain open until supported by research and prototypes.

## Relationship to PAWH

The Personal AI Workstation Handbook was the earlier prototype from which this
project developed.

PAWH contains potentially useful research, technical records, document assets
and lessons. It also contains premature assumptions, complex governance,
duplicated guidance and structures that should not automatically transfer.

PAWH is therefore historical source material, not the operating foundation of
Grounded AI Practice. Individual items may be reconsidered later through an
explicit review process.

## Current working approach

During the research stage:

- factual claims should be supported by traceable sources;
- evidence, inference, personal observation and proposal should be clearly
  distinguished;
- major decisions should be made explicitly rather than inferred from drafts;
- structures and rules should be introduced only when they solve a demonstrated
  need;
- the project should remain understandable without depending on an AI assistant;
- AI tools may support research and production, but human review remains
  necessary.

## Immediate objective

Establish a credible research foundation, clarify the most useful audience and
learning need, and determine what Grounded AI Practice should build first.
