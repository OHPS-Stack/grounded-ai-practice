# Grounded AI Practice — Research Log

## Document status

Research-stage working document. This log is maintained as an ongoing record of
findings, not a final report. It follows the recording discipline set out in
RESEARCH_QUESTIONS.md ("Research discipline" section).

## Purpose

Every entry below corresponds to a specific research question from
RESEARCH_QUESTIONS.md and records what was actually found, distinguishing
source-supported fact from inference, and noting any effect on project
direction.

This log is intended to be maintained by Claude during research passes, not
edited by hand. New entries are appended as findings are checked; existing
entries are not silently altered — corrections or supersessions are added as
new entries that reference the one they update, so history stays traceable
(consistent with RESEARCH_QUESTIONS.md's requirement that superseded
information remain traceable).

## How to read this log

Each entry contains:

| Field | Meaning |
|---|---|
| ID | Sequential entry number |
| Date logged | When the entry was added to this log |
| Priority / Question | Which numbered research priority and question (from RESEARCH_QUESTIONS.md) this entry addresses |
| Source | A short tag referencing the Source key below (e.g. `[GT-DSIT25]`) — full citation given once there, not repeated per entry |
| Checked date | When the source was accessed/verified (may differ from date logged) |
| What the source directly supports | Only the claim the source itself makes — no extrapolation |
| Inference drawn | Any conclusion drawn beyond what the source states directly, clearly marked as inference |
| Limitations / conflicting evidence | Gaps, caveats, sample issues, or contradicting sources |
| Effect on project direction | Whether this changes, confirms, or has no current effect on the brief |

---

## Source key

Full citation is given once here; log entries below cite the short tag only.

| Tag | Full source |
|---|---|
| `[GT-DSIT25]` | Gardiner & Theobald for DSIT, *AI Labour Market Survey 2025 report*, published 28 Jan 2026 — PRIMARY, read directly. assets.publishing.service.gov.uk/media/6960ef384343a0da370869b7/AI_Labour_Market_Survey_2025_report.pdf |
| `[MPG26]` | ManpowerGroup, 2026 Talent Shortage Survey (UK: 2,261 businesses). manpowergroup.co.uk |
| `[ONS23]` | ONS, "Understanding AI uptake and sentiment among people and businesses in the UK" (June 2023), cross-checked against the DSIT/CDEI Public Attitudes to Data and AI tracker. ons.gov.uk; rtau.blog.gov.uk |
| `[BCC26]` | British Chambers of Commerce summary of a claimed February 2026 Parliamentary briefing — UNVERIFIED, see Entry 009. britishchambers.org.uk/news/2026/04 |
| `[TURING-ADA]` | Alan Turing Institute / Ada Lovelace Institute, nationally representative UK public-attitudes-to-AI surveys (2023 and 2025). turing.ac.uk/research/research-projects/understanding-public-attitudes-ai |
| `[BLDN26]` | BusinessLDN / Greater London Authority AI and Jobs Taskforce survey (July 2026). resultsense.com/news/2026-07-21 |
| `[GOTO26]` | GoTo / Workplace Intelligence, "Pulse of Work in 2026" survey (2,500 respondents, 10 countries incl. UK). workplaceintelligence.com; businesswire.com |
| `[CBP10003]` | House of Commons Library Research Briefing, "AI regulation in the UK," CBP-10003, 10 June 2026, by Elizabeth Rough — PRIMARY, read directly. researchbriefings.files.parliament.uk/documents/CBP-10003/CBP-10003.pdf |
| `[SE-AMEEN25]` | Dr Nisreen Ameen (Royal Holloway) for Skills England/DSIT, *AI Skills for the UK Workforce*, 30 Oct 2025 — read via secondary summaries only. gov.uk |
| `[DSIT-PROD26]` | UK Government, *Assessment of AI capabilities and the impact on the UK labour market*, 28 Jan 2026 — PRIMARY, read directly. gov.uk/government/publications/assessment-of-ai-capabilities-and-the-impact-on-the-uk-labour-market |
| `[EY26]` | EY UK AI upskilling research, as reported via ivee.jobs/blog/uk-ai-skills-gap — secondary source only. |
| `[SE-WHATWORKS26]` | Dr Nisreen Ameen, British Academy Policy-Led Innovation Fellowship / Skills England, *What Works for AI Upskilling in the UK: Research evidence, analysis and methodology*, 10 June 2026 — PRIMARY, read directly. assets.publishing.service.gov.uk/media/6a26c8d02cdcfdb7436ac0a6/research_evidence_analysis_and_methodology.pdf |

---

## Log entries

### Entry 001 (corrected 2026-07-24 — see note below)

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 1 — "How common are unsafe, ineffective,
  costly or over-dependent forms of AI use?" / "Where are the strongest
  documented gaps between AI adoption and responsible implementation?"
- **Source:** `[GT-DSIT25]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** 97% of respondents identified at
  least one skills gap **in the AI labour market specifically** — this
  survey is about the AI sector/profession workforce (AI specialists,
  technical roles), not general staff AI literacy across all UK
  organisations. 57% report a technical skills gap (programming,
  engineering, modelling); 30% report a non-technical gap. The most common
  gap is "understanding AI concepts and algorithms," rising from 55% to 60%
  of respondents over five years. 28% say technical shortages have already
  affected business goals. The report explicitly states its findings and
  recommendations "do not represent Government views or policy" — they are
  G&T's own analysis, commissioned by DSIT.
- **Inference drawn:** None — corrected from initial secondary-source read.
- **Limitations / conflicting evidence:** This is narrower in scope than it
  first appeared: it measures the AI sector's own labour market (a
  specialist/technical workforce), not everyday workplace AI use across the
  general economy. Citing this as evidence for "the public" or "everyday
  workers" needing AI literacy would overstate what it actually shows. The
  general-literacy framing is better supported by Entry 002 (ManpowerGroup)
  and Entry 010 (Skills England) instead.
- **Effect on project direction:** Corrects the earlier reading. This source
  should be cited specifically for the *specialist AI workforce* skills gap,
  not as general evidence for the "everyday AI literacy" problem the project
  is centred on. Keep as evidence that a technical AI-sector gap exists
  alongside — not instead of — a broader literacy gap.

### Entry 002

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 1 — same as Entry 001; also relevant to
  Priority 3 (capability definition).
- **Source:** `[MPG26]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** Only 10% of UK employers are using
  AI to replace headcount. For the first time, AI-related skill (19%) was
  identified as the hardest skill for employers to find — described in the
  source as being about literacy and confidence in using AI to support
  existing work, not technical/programming skill. The UK skills gap overall
  is reported as declining for a second consecutive year.
- **Inference drawn:** None stated as fact; the literacy-vs-technical framing
  is the source's own characterisation.
- **Limitations / conflicting evidence:** Directly conflicts with Entry 001 on
  how the gap should be characterised (technical vs. general literacy), and
  "gap declining" conflicts with Entry 006 (BusinessLDN, gap widening in
  London). Needs reconciling — possibly a sectoral or regional difference
  rather than a real contradiction.
- **Effect on project direction:** Supports a literacy/confidence framing of
  "practical AI capability" over a narrowly technical one — relevant to
  Priority 3.

### Entry 003

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 1 — "What reliable evidence exists about
  AI use, understanding and capability in the UK public..."
- **Source:** `[ONS23]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** 72% of UK adults could give at least
  a partial explanation of AI (May 2023 ONS Opinions and Lifestyle Survey),
  up from 56% a year earlier (2022 CDEI tracker). In the month before the
  2023 survey, 5% of adults used AI "a lot," 45% "a little," 50% not at all.
- **Inference drawn:** None — figures stated directly by the source.
- **Limitations / conflicting evidence:** Data is from 2022–2023, over two
  years old; usage and awareness have very likely shifted substantially
  since. No 2025/2026 ONS wave found yet.
- **Effect on project direction:** Useful as a historical baseline only —
  should not be cited as current evidence without a more recent wave.

### Entry 004

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 1 — same as Entry 003.
- **Source:** `[BCC26]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** Claims that only 21% of UK adults
  can explain AI in meaningful detail, and only one in five people in work
  feel confident using it.
- **Inference drawn:** None.
- **Limitations / conflicting evidence:** Secondary source only (a business
  lobby group's blog) — the original Parliamentary/Commons Library briefing
  has not yet been read directly to confirm this figure.
- **Effect on project direction:** Potentially strong, directly relevant
  evidence for the core problem statement if verified — flagged as a priority
  for primary-source verification (see Open threads).

### Entry 005

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 1 and Priority 2 (audience and need) —
  identifies a strong existing evidence programme to draw on.
- **Source:** `[TURING-ADA]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** Confirms the existence of a
  repeated, methodologically strong, nationally representative UK survey
  programme covering AI awareness, experience, harms, and views on
  governance.
- **Inference drawn:** Likely one of the best-evidenced sources available for
  this project — inference, not yet confirmed by reading the full reports.
- **Limitations / conflicting evidence:** Only the project description page
  has been read so far, not the actual 2025 report findings.
- **Effect on project direction:** High-priority source to read in full next;
  candidate as a primary evidence base for the project's problem statement.

### Entry 006

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 1 — gaps between adoption and responsible
  implementation.
- **Source:** `[BLDN26]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** Share of London employers saying
  their workforce has the skills the business needs fell from 63% to 50% in
  a year (survey of 2,000+ business leaders). Separate City Hall modelling
  estimates 46% of London workers are in roles where AI could automate part
  of the job, against a 38% UK average.
- **Inference drawn:** None.
- **Limitations / conflicting evidence:** London-specific, not necessarily
  representative of the UK as a whole. Conflicts with Entry 002
  (ManpowerGroup's "gap declining" finding) — may reflect a genuine
  regional/sectoral difference rather than contradictory data.
- **Effect on project direction:** Suggests the gap may be widening in at
  least some regions/sectors even as national aggregate figures show decline
  — worth investigating whether this is a London-specific or sector-specific
  effect.

### Entry 007

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 1 — "How common are unsafe, ineffective,
  costly or over-dependent forms of AI use?"
- **Source:** `[GOTO26]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** Globally, 50% of employees say they
  rely too much on AI, 30% feel they can't function without it, 39% feel
  overreliance is eroding their skills, and 70% have used AI for high-stakes
  tasks such as legal work or strategic decisions.
- **Inference drawn:** None.
- **Limitations / conflicting evidence:** Not UK-specific — the UK is one of
  ten countries in the sample, with no UK-only breakdown found. Vendor
  (GoTo)-commissioned survey, which may carry framing bias toward findings
  supporting a governance/training narrative.
- **Effect on project direction:** Useful directional evidence only; a
  genuinely UK-specific study on unsafe/over-dependent AI use has not yet
  been found (see Open threads).

### Entry 009

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 1 — attempted verification of Entry 004
  (the "21% of adults can explain AI" claim).
- **Source:** `[CBP10003]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** This briefing does not contain the
  "21% of adults can explain AI" figure, nor the "one in five confident using
  it at work" claim, anywhere in its text. It also is dated June 2026, not
  February 2026 as the secondary source (British Chambers of Commerce blog)
  claimed.
- **Inference drawn:** Either the BCC blog cited a different, unnamed
  February 2026 Parliamentary briefing that has not yet been located, or the
  figure is unsourced/misattributed. Cannot currently confirm this statistic
  from a primary source.
- **Limitations / conflicting evidence:** This does not prove the 21% figure
  is false — only that it could not be verified in the briefing most likely
  to contain it. A further search for a February 2026 briefing is needed.
- **Effect on project direction:** Downgrade Entry 004 to "unverified — do
  not cite" until a primary source is found. This is a useful example of why
  the research discipline requires checking secondary claims before treating
  them as evidence.

### Entry 010 (upgraded to primary source 2026-07-24)

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 1 and Priority 2 (audience and need,
  especially barriers by group).
- **Source:** `[SE-AMEEN25]` — PRIMARY SOURCE, report overview page and
  companion methodology report read directly (gov.uk/government/publications/ai-skills-for-the-uk-workforce/report-overview)
- **Checked date:** 2026-07-24
- **What the source directly supports:** Based on 6 national workshops, a
  senior policy roundtable, and focused research (Oct 2025). Analyses AI
  adoption patterns and skills gaps/barriers across the 10 key growth sectors
  in the UK's Modern Industrial Strategy. Identifies common barriers
  affecting organisations of all sizes, with specific issues for SMEs,
  marginalised groups, and areas with little AI training/use. Produced an AI
  Skills Framework, an Adoption Pathway Model, and an Employer Adoption
  Checklist.
- **Inference drawn:** None — confirmed directly, no longer inferred from
  secondary summaries.
- **Limitations / conflicting evidence:** The report author states opinions
  are her own and don't necessarily reflect Skills England's views. See
  Entry 012 for the detailed quantitative barriers and methodology
  limitations from the companion evidence report.
- **Effect on project direction:** Confirmed as a high-value primary source
  for Priority 2. See Entry 012 for the fuller evidence base this connects
  to.

### Entry 011

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 1 — "How common are unsafe, ineffective,
  costly or over-dependent forms of AI use?"
- **Source:** `[DSIT-PROD26]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** From DSIT's AI adoption survey, 56%
  of firms using AI reported productivity gains, most estimating
  improvements of up to 20%. The report itself flags that these are
  self-assessed, not objectively measured, and states there is currently
  limited robust statistical evidence that higher AI adoption at firm level
  is linked to higher overall productivity.
- **Inference drawn:** None — this caveat is stated directly by the source.
- **Limitations / conflicting evidence:** None noted; this is a government
  source explicitly flagging weak evidence quality on its own headline
  statistic, which is unusually direct.
- **Effect on project direction:** Strong, directly relevant evidence for the
  research-discipline point that adoption ≠ effectiveness — self-reported
  productivity gains should not be treated as proof AI use is genuinely
  effective. Useful for framing the "ineffective/costly" sub-question in the
  problem statement with real evidence rather than assumption.

### Entry 012

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 2 (barriers by group), Priority 4
  (learning design), Priority 6 (technical/conceptual scope, sector
  variation).
- **Source:** `[SE-WHATWORKS26]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** Builds on Entry 010, shifting from
  diagnosis to "what works." Evidence base: 23 workshops (~150
  organisations), 10 case studies, and a survey of 536 senior/decision-making
  respondents. Survey: top barriers to AI upskilling participation are cost
  (42%), lack of relevant training provision (42%), fear of failing in
  technical areas (32%), limited digital skills in the workforce (28%).
  Group-level qualitative findings identify distinct barrier patterns for
  low-income learners (access/time/device), women (confidence/representation,
  risk of widening gap), disabled learners (inaccessible platforms/formats),
  younger workers (limited responsible-use understanding, weak career
  pathways), older workers (pace/jargon/assumed fluency), and SME employees
  (informal skills going unrecognised). Barriers are stated to intersect and
  compound rather than act independently. Also derives "PRIMES" — six
  evidence-based principles for effective AI training (Practical, Reachable,
  Integrated, Modular, Expandable, Sustainable), each with detailed
  accreditation-style criteria, grounded in the same workshops/case
  studies/survey.
- **Inference drawn:** PRIMES is presented by the source as directly
  evidence-derived, not an external framework being retrofitted — treating it
  as a strong candidate reference point for Priority 4 is a reasonable
  inference, not yet a project decision.
- **Limitations / conflicting evidence:** The 536-response survey was
  collected via Amazon Mechanical Turk, screened for UK-based senior/
  decision-making respondents; the authors themselves state the sample skews
  toward London-based, AI-engaged organisations and is not representative of
  the wider UK economy, and does not support robust sector-level analysis.
  The 23 workshops are described by the authors as rich but not statistically
  representative. Should be cited as strong illustrative/directional
  evidence, not as a representative national picture.
- **Effect on project direction:** Directly actionable for Priority 4 — PRIMES
  is a genuine candidate to learn from (or adapt) rather than building a
  learning-design model from scratch, consistent with the project's own
  stated approach in Priority 5 of learning from existing work without
  imitating it wholesale. Also meaningfully deepens Priority 2: gives
  specific, evidenced barrier patterns per group rather than a single
  undifferentiated "the public" audience.

### Entry 008

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 2 — "What barriers prevent [learners]
  from using existing learning resources?"
- **Source:** `[EY26]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** Cited claims that only 35% of UK
  business leaders have a mature, organisation-wide AI upskilling programme;
  only 14% of UK workers have undertaken formal AI training; only 11% receive
  what the source calls "adequate" training.
- **Inference drawn:** None.
- **Limitations / conflicting evidence:** Read only via a secondary blog, not
  the original EY report — figures should be treated as provisional until
  verified against the primary source.
- **Effect on project direction:** If verified, directly supports the
  "barriers to existing learning resources" question and strengthens the case
  that fragmented/inadequate training is a real, evidenced gap.

<!--
Entry template (for reference — remove once first real entry is added):

### Entry 001

- **Date logged:** YYYY-MM-DD
- **Priority / Question:** [e.g. Priority 1 — "What reliable evidence exists
  about AI use, understanding and capability in the UK public, education and
  workforce?"]
- **Source:** `[TAG]` — add the full citation to the Source key table above
  first if it's a new source, then reference the tag here
- **Checked date:** YYYY-MM-DD
- **What the source directly supports:** [factual claim only]
- **Inference drawn:** [if any — state plainly that it is an inference]
- **Limitations / conflicting evidence:** [caveats, sample size, contradicting
  sources]
- **Effect on project direction:** [none / confirms X / raises question about Y]

-->

---

## Open threads

*A running list of questions from RESEARCH_QUESTIONS.md that remain
uninvestigated or partially investigated, so gaps are visible at a glance. This
section is updated as entries are added, not filled in ahead of time.*

**Resolved this pass:**
- ~~DSIT AI Labour Market Survey primary-source check~~ — done (Entry 001,
  corrected). Turned out to be scoped to the AI sector specifically, not
  general workforce literacy — an important correction, not just a
  confirmation.
- ~~Cost/ineffectiveness evidence~~ — found (Entry 011): DSIT's own
  assessment flags weak evidence that AI adoption improves productivity.
- ~~Skills England report primary-source read~~ — done (Entry 010 upgraded,
  Entry 012 added). Strong, detailed evidence on group-level barriers plus
  the PRIMES training-design framework — directly useful for Priority 4.
- ~~Small-organisation/individual adoption barriers~~ — substantially
  addressed (Entry 012): SMEs appear consistently across barrier categories
  (cost, informal skills going unrecognised, limited internal capacity).

**Still open:**
- **The 21%-of-adults figure could not be verified** (Entry 009) — checked
  the most likely Commons Library briefing directly and it isn't there.
  Either find the correct February 2026 briefing or drop this claim.
- **EY upskilling statistics (Entry 008) still only checked via secondary
  blog** — primary EY report not yet located.
- **Technical vs. literacy framing conflict** (Entry 001 vs. Entry 002) —
  partly reframed rather than resolved: Entry 012 shows organisations find
  technical skills hardest to support (67%) but non-technical skills least
  reported as difficult (10%), which is a different axis (skill category
  difficulty) than the original technical-vs-literacy framing question. Still
  needs explicit reconciliation before Priority 3 proceeds.
- **Gap widening vs. declining conflict:** Entry 002 (national, declining)
  and Entry 006 (London, widening) still disagree — not yet investigated
  further.
- **No education-sector-specific evidence yet** (schools, further/higher
  education) — Entry 012 covers 10 employment sectors and training provision
  generally, but not schools/universities as learner populations in their
  own right.
- **No UK-specific evidence on unsafe/over-dependent AI use** — the only
  relevant data found (Entry 007) is a global survey with no UK breakdown.
- **Priority 5 (comparable products and programmes) untouched** — no research
  yet on roadmap.sh, LeetCode, or existing AI-literacy programmes. PRIMES
  (Entry 012) is a strong candidate to compare any future learning design
  against.
