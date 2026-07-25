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

This decision answers *what shape* the first test should take. It does not
yet decide *which* core capability that first unit should teach — that
remains open.

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

**Status:** the palette and logo type are decided; the logo mark is in
progress. One **symbol-only working candidate** is locked at
`assets/brand/logo/candidates/symbol_v01_terminal_handbook_recolour.svg` —
it reuses the geometry of the approved PAWH "terminal + handbook" symbol
(an open-book/journal shape containing a terminal prompt chevron and
cursor) unchanged, recoloured flat to Ink/Ember/white. This is a candidate
to refine further (the creator intends to edit the SVG paths directly), not
a final asset, and other symbol concepts are still to be explored — it
should not be treated as the decided logo. The wordmark pairing tested
alongside it did not work (didn't match the symbol's style, read as too
long/disconnected) and remains unresolved separately from the symbol.

The existing legacy PAWH icon set (`assets/brand/legacy-pawh-icons/`) uses a
different, superseded palette (navy/orange) and is confirmed **incorrect**
against this decision — it needs a future recolour/overhaul pass before
reuse. Until that overhaul happens, those files should be treated as
shape/structure reference only, not as current-palette assets. Note this is
a distinct system from the symbol candidate above — the icon library is
illustrative content icons, not the brand mark.

**Workflow note (24 July 2026):** fine curve-level refinement of the symbol
candidate (smoothing specific bezier joins, symmetry corrections) was
attempted through iterative AI-described feedback (screenshot annotation →
prose correction, repeated) and the creator found this arduous and
unproductive — a repeat of a discouraging pattern from PAWH. The creator has
moved to editing the SVG directly in Inkscape. Future sessions should treat
`assets/brand/logo/candidates/symbol_v01_terminal_handbook_recolour.svg` as
potentially edited outside this workflow — re-read it fresh rather than
assuming the last-known state, and don't propose resuming described-feedback
curve editing; support concept-level exploration instead, or integration
once the creator brings back a manually-refined version.

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
- which single core capability the first pilot unit should teach;
- its final curriculum or competency levels;
- its permanent repository structure;
- its long-term document and data architecture;
- its visual identity beyond the palette/logo-type/tone decisions recorded
  above — the logo mark itself is not yet designed, and the legacy PAWH
  icon set needs a recolour/overhaul pass before it matches the current
  palette;
- whether it should eventually become a commercial, community or purely
  personal initiative.

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
