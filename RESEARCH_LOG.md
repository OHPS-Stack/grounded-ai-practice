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

## Research calibration for the current project stage (added 2026-07-24)

The bias-mitigation discipline above remains valid, but the project is still
in scoping — outlining direction, not producing citable final claims — so the
practical application of it is deliberately lighter for now:

- **Source scope, going forward:** prefer official/government sources
  (gov.uk, ONS, Parliament), independent academic sources (universities,
  established research institutes), and established international bodies.
  Vendor/commercial and advocacy sources are deprioritised, not banned —
  they're still useful for spotting a claim worth checking, but not treated
  as evidence on their own for anything scope-defining.
- **Confirm/disconfirm pairing applies to foundational claims only** — the
  ones that would actually change project direction — not to every
  statistic. Exhaustive adversarial verification of every entry is deferred
  to dedicated deep-research passes later, once scope is firmer and the
  cost of a dedicated pass is justified by what's riding on the answer.
- **Known unresolved tensions are parked, not chased further right now:**
  the technical-vs-literacy framing question (Entry 001 vs. Entry 002 vs.
  Entry 012) and the gap-widening-vs-declining conflict (Entry 002 vs.
  Entry 006) remain open, flagged for a dedicated pass later rather than
  something to keep re-litigating in every session. General research from
  here should inform direction without needing every internal tension fully
  resolved first.

A review of this log's own contents on 2026-07-24 found a real problem: every
search run so far was framed to find evidence *for* an AI capability gap, none
were framed to test the opposite, and most sources found have a commercial or
institutional interest in reporting a large gap (recruitment firms,
consultancies, training vendors, or bodies whose funding is tied to
demonstrating need). This is confirmation bias in both query design and
source selection. See Entry 013 for the specific correction.

Going forward, this log follows two additional rules:

1. **Paired search discipline.** For any foundational or headline claim, a
   "does the opposite hold" or "is this framing contested" search is run
   alongside the confirming search — not as an afterthought, but before the
   claim is logged as evidence.
2. **Source interest tagging.** The Source key table below now includes an
   "Interest" column, classifying each source as `Independent/Academic`,
   `Government/Official`, `Vendor/Commercial`, or `Advocacy/Membership body`.
   This makes it possible to see at a glance how concentrated the evidence
   base is in parties with a stake in the answer — which was invisible while
   this information only existed inside individual entries.

## Source key

Full citation is given once here; log entries below cite the short tag only.

| Tag | Interest | Full source |
|---|---|---|
| `[GT-DSIT25]` | Government-commissioned / Consultancy-authored | Gardiner & Theobald for DSIT, *AI Labour Market Survey 2025 report*, published 28 Jan 2026 — PRIMARY, read directly. assets.publishing.service.gov.uk/media/6960ef384343a0da370869b7/AI_Labour_Market_Survey_2025_report.pdf |
| `[MPG26]` | Vendor/Commercial (recruitment firm) | ManpowerGroup, 2026 Talent Shortage Survey (UK: 2,261 businesses). manpowergroup.co.uk |
| `[ONS23]` | Independent/Official statistics | ONS, "Understanding AI uptake and sentiment among people and businesses in the UK" (June 2023), cross-checked against the DSIT/CDEI Public Attitudes to Data and AI tracker. ons.gov.uk; rtau.blog.gov.uk |
| `[BCC26]` | Advocacy/Membership body — UNVERIFIED | British Chambers of Commerce summary of a claimed February 2026 Parliamentary briefing — see Entry 009. britishchambers.org.uk/news/2026/04 |
| `[TURING-ADA]` | Independent/Academic | Alan Turing Institute / Ada Lovelace Institute, nationally representative UK public-attitudes-to-AI surveys (2023 and 2025). turing.ac.uk/research/research-projects/understanding-public-attitudes-ai |
| `[BLDN26]` | Advocacy/Membership body (business membership org + consultancy) | BusinessLDN / Greater London Authority AI and Jobs Taskforce survey (July 2026). resultsense.com/news/2026-07-21 |
| `[GOTO26]` | Vendor/Commercial (software company) | GoTo / Workplace Intelligence, "Pulse of Work in 2026" survey (2,500 respondents, 10 countries incl. UK). workplaceintelligence.com; businesswire.com |
| `[CBP10003]` | Independent/Official (Parliamentary research service) | House of Commons Library Research Briefing, "AI regulation in the UK," CBP-10003, 10 June 2026, by Elizabeth Rough — PRIMARY, read directly. researchbriefings.files.parliament.uk/documents/CBP-10003/CBP-10003.pdf |
| `[SE-AMEEN25]` | Government-commissioned / Academic author | Dr Nisreen Ameen (Royal Holloway) for Skills England/DSIT, *AI Skills for the UK Workforce*, 30 Oct 2025 — PRIMARY, read directly. gov.uk |
| `[DSIT-PROD26]` | Government/Official | UK Government, *Assessment of AI capabilities and the impact on the UK labour market*, 28 Jan 2026 — PRIMARY, read directly. gov.uk/government/publications/assessment-of-ai-capabilities-and-the-impact-on-the-uk-labour-market |
| `[EY26]` | Vendor/Commercial (consultancy) | EY UK AI upskilling research, as reported via ivee.jobs/blog/uk-ai-skills-gap — secondary source only. |
| `[SE-WHATWORKS26]` | Government-commissioned / Academic author | Dr Nisreen Ameen, British Academy Policy-Led Innovation Fellowship / Skills England, *What Works for AI Upskilling in the UK*, 10 June 2026 — PRIMARY, read directly. assets.publishing.service.gov.uk/media/6a26c8d02cdcfdb7436ac0a6/research_evidence_analysis_and_methodology.pdf |
| `[CRS-SKILLSGAP]` | Independent/Official (US Congressional Research Service) | Congressional Research Service, "Skills Gaps: A Review of Underlying Concepts and Evidence," Congress.gov, R47059. congress.gov/crs-product/R47059 |
| `[FASTCO-MYTH]` | Independent commentary (opinion/trade press) | Fast Company, "The skills gap is a myth," Jan 2026. fastcompany.com/91469508/the-skills-gap-is-a-myth |
| `[ONS-BICS26]` | Independent/Official statistics | ONS, "Artificial intelligence in UK businesses: 2023 to 2026" and "Business insights and impact on the UK economy" bulletin (2 July 2026), Business Insights and Conditions Survey (BICS) — PRIMARY, read directly. ons.gov.uk/businessindustryandtrade/business/businessservices/articles/artificialintelligenceinukbusinesses/2023to2026 |
| `[DFE-TECHSURVEY25]` | Government/Official (DfE, fieldwork by independent agency IFF Research) | Department for Education, *Technology in Schools Survey: 2024 to 2025*, Nov 2025 — PRIMARY, read directly. assets.publishing.service.gov.uk/media/692834a6ce50d215cae9610e/Technology_in_schools_survey_2024_to_2025_research_report.pdf |
| `[DFE-EARLYADOPTERS25]` | Government/Official | Department for Education, "The biggest risk is doing nothing: insights from early adopters of AI in schools and FE colleges," June 2025 — PRIMARY, read directly (includes a cited National Literacy Trust figure, not independently re-verified). gov.uk/government/publications/ai-in-schools-and-further-education-findings-from-early-adopters |
| `[PEARSON25]` | Vendor/Commercial (ed-tech/publishing company promoting its own AI certification products) | Pearson, *Pearson School Report 2025*, cited via stocktitan.net — secondary source, flagged for its commercial interest. |
| `[SE-TOOLSPKG25]` | Government/Official (Skills England, authored by Dr Nisreen Ameen) | Skills England / DfE, *AI skills tools package* (AI Skills Framework, Adoption Pathway Model, Employer Adoption Checklist), updated 4 Nov 2025 — PRIMARY, read directly. gov.uk/government/publications/ai-skills-for-the-uk-workforce/ai-skills-tools-package |
| `[AISKILLSHUB]` | Government/Official (Innovate UK, in partnership with Skills England; delivery supported by PwC and industry partners) | UK AI Skills Hub, a national training-navigation platform under the BridgeAI programme, expanded 28 Jan 2026 to all UK adults with an ambition to upskill 10 million workers by 2030 — read via aiskillshub.org.uk/about-us/ and secondary coverage (direct fetch of the homepage returned a 402 error). |
| `[SE-ANNUAL26]` | Government/Official | Skills England, *Annual Skills Report 2026*, 1 June 2026, especially Chapter 3 "Accelerating adoption of AI" — PRIMARY, read directly. assets.publishing.service.gov.uk/media/6a19740bb95db968c8f3bc3d/skills_england_annual_skills_report_2026.pdf |

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

### Entry 003 (updated with current data 2026-07-24)

- **Date logged:** 2026-07-24 (originally), updated 2026-07-24
- **Priority / Question:** Priority 1 — "What reliable evidence exists about
  AI use, understanding and capability in the UK public..."
- **Source:** `[ONS23]` (original baseline) and `[ONS-BICS26]` (current
  trend, added on update)
- **Checked date:** 2026-07-24
- **What the source directly supports:** Original 2022–2023 baseline: 72% of
  UK adults could give at least a partial explanation of AI (May 2023), up
  from 56% a year earlier; only 5% used AI "a lot" in the prior month.
  **Updated with `[ONS-BICS26]` (business-side, current):** since September
  2023, the average number of AI technologies used per business has risen
  only modestly, from around 1.4 to 1.6 by June 2026 — ONS's own
  interpretation is that this implies relatively limited transformative
  impact so far for most AI-adopting firms. The clearest growth is in large
  language model use (text generation), up from roughly 5% to 17–18% of
  businesses with 10+ employees since Sept 2023; visual content creation
  rose similarly. Older (2023) sector data shows adoption concentrated in
  services (9%) versus manufacturing (5%) and construction (3%). Public
  sector 2023 data shows AI use highest in central government (47%), health
  boards and local government (42% each), lower in fire/police (30%), and
  lowest in education (24%) among the categories tracked.
- **Inference drawn:** None — figures stated directly by ONS.
- **Limitations / conflicting evidence:** ONS explicitly labels the business
  AI figures "official statistics in development" and advises caution. The
  adoption measure only captures whether a business uses *any* of a list of
  specific technologies — it doesn't distinguish trial/light use from
  deep, production-level use, so headline "adoption" figures likely overstate
  genuine embedded capability. The sector and public-sector breakdowns are
  still 2023-vintage even in this update; only the business-technology-type
  figures are current to June 2026.
- **Effect on project direction:** No longer just a historical baseline —
  now shows a genuine, official, current trend: adoption is rising but
  unevenly and modestly, with education the lowest-adopting public-sector
  category tracked. Useful if education becomes a candidate audience
  (Priority 2), and useful independent counterweight to the vendor-sourced
  "urgent gap" framing in Entries 001/002/012 — ONS's own read is closer to
  "slow, uneven change" than "crisis."

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

### Entry 005 (updated with findings 2026-07-24)

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 1 and Priority 2 (audience and need,
  especially equity dimensions).
- **Source:** `[TURING-ADA]` — wave 2 (fieldwork 2024/25, published 2025):
  Modhvadia, Sippy, Field Reid & Margetts, "How Do People Feel About AI?
  Wave two... designed through a lens of equity and inclusion," Ada Lovelace
  Institute and Alan Turing Institute — read directly.
- **Checked date:** 2026-07-24
- **What the source directly supports:** Nearly three-quarters of the
  British public say laws and regulation would make them more comfortable
  with AI, up from 62% in 2023. Strong majorities see clear benefit in
  specific high-stakes uses: 91% for facial recognition in policing, 86% for
  AI-driven cancer risk assessment; 63% see general-purpose LLMs as
  beneficial overall. Notable equity finding: 80% of each surveyed
  minoritised ethnic group see general-purpose LLMs as beneficial, compared
  with 63% of the general population — higher, not lower, perceived benefit.
  Separately, people on lower incomes and those with fewer digital skills are
  less likely to perceive AI as beneficial — a different-direction pattern
  from the ethnicity finding, not a contradiction of it.
- **Inference drawn:** None stated as fact by the source; noted as a genuine
  tension in the findings, not smoothed over.
- **Limitations / conflicting evidence:** The authors themselves caution that
  even where sample sizes for specific minoritised groups are large enough
  to report, these remain broad categories (e.g. "Bangladeshi") that obscure
  real diversity within them.
- **Effect on project direction:** Upgrades this from "a strong survey
  programme exists" to real, usable findings. Directly relevant to Priority
  2: perceived benefit and need don't map onto a single "disadvantaged
  groups are more sceptical" assumption — some groups see more benefit in
  some AI uses and less in others, which argues against treating "the
  underserved" as a single undifferentiated group when defining an audience.

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

### Entry 013 — Bias check on the evidence base as a whole

- **Date logged:** 2026-07-24
- **Priority / Question:** Meta — applies across Priority 1 and the evidence
  underlying Entries 001, 002, 004 (unverified), 006, 008, 010, 012.
- **Source:** `[CRS-SKILLSGAP]`, `[FASTCO-MYTH]`, plus a structural review of
  this log's own source list (see updated Source key "Interest" column).
- **Checked date:** 2026-07-24
- **What the source directly supports:** `[CRS-SKILLSGAP]` (US-focused, not
  AI-specific) documents recognised measurement problems with "skills gap"
  claims generally: employer-reported vacancies can reflect turnover rather
  than genuine skill shortages, and employers' own skill requirements shift
  over time as firms change processes — meaning a reported "gap" can
  partly reflect employer-side change rather than worker deficit.
  `[FASTCO-MYTH]` argues a specific sector's "skills gap" is better
  characterised as a knowledge-transfer gap (retiring experts' undocumented
  knowledge) than a training deficiency — an alternative framing, not a
  UK-specific rebuttal. Separately, reviewing this log's own Source key
  shows 5 of 13 sources are Vendor/Commercial (recruitment firms,
  consultancies, software vendors) and 2 more are Advocacy/Membership
  bodies — a majority of the evidence base has some institutional interest
  in reporting a gap.
- **Inference drawn:** The searches conducted for Priority 1 so far were
  framed exclusively to find evidence *for* a capability gap; no searches
  were run to test the opposite or to check whether "skills gap" as a
  category is itself contested. This is a process failure, not just a
  source-quality issue — it would have persisted regardless of how many
  more confirming sources were added.
- **Limitations / conflicting evidence:** Neither `[CRS-SKILLSGAP]` nor
  `[FASTCO-MYTH]` is UK-specific or AI-specific, and neither proves the UK AI
  capability gap described in PROJECT_BRIEF.md doesn't exist. They establish
  that the concept is measurement-contested in general, which is a reason for
  caution, not a disconfirmation of Entries 001–012.
- **Effect on project direction:** Does not overturn prior entries, but
  changes how they should be read: employer/employee self-report survey
  statistics on "AI skills gaps" should be treated as one contested framing
  among others, not as settled fact, until independently corroborated. Also
  changes research process going forward — see the new "Bias-mitigation
  discipline" note above this log's entries.

### Entry 016 — Education sector (fills previously open gap)

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 1 — fills the "no education-sector-
  specific evidence" gap flagged since the first pass.
- **Source:** `[DFE-TECHSURVEY25]`, `[DFE-EARLYADOPTERS25]`; `[PEARSON25]`
  noted separately as vendor context, not core evidence.
- **Checked date:** 2026-07-24
- **What the source directly supports:** Half of teachers in England
  responding to a DfE survey now use generative AI tools; of those who
  don't, 64% say they don't know enough about AI to use it in their role.
  32% of school/college leaders in England are not considering any changes
  to account for AI. A National Literacy Trust survey (cited within the DfE
  report, not independently re-verified here) found the proportion of
  13–18-year-olds who say they've used generative AI rose from 37% in 2023
  to 77% in 2024 — a very fast rise if accurate. DfE's own framing across
  both reports is cautious: adoption is real but early-stage and uneven, not
  a settled transformation.
- **Inference drawn:** None stated as fact by DfE; the National Literacy
  Trust figure is reported secondhand via the DfE document, not checked
  against the original NLT publication.
- **Limitations / conflicting evidence:** `[PEARSON25]` (a vendor survey,
  14,000+ respondents) reports lower teacher confidence — only 9% of
  teachers feel confident *teaching* AI, 23% not confident *using* it — but
  as an ed-tech company actively promoting its own AI certification products,
  it's flagged per this log's interest-tagging convention rather than
  treated as equivalent to the DfE figures. A TES headline referencing a
  paper by a former DfE adviser warning uncritical generative AI use could
  risk pupil "cognitive collapse" was noted but not read in full — flagged
  as a lead for a future pass, not logged as a finding.
- **Effect on project direction:** Closes a real gap in the evidence base.
  DfE's own posture — real but early, uneven adoption, with confidence
  varying sharply by teacher — is consistent with the "slow, uneven change"
  reading from Entry 003 (ONS) rather than the "urgent crisis" framing from
  the vendor-heavy sources. Useful if education becomes a candidate
  audience or comparison sector for Priority 2/5.

### Entry 017 — AI Skills Framework, Adoption Pathway, and Employer Checklist

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 3 (capability definition) and Priority 4
  (learning design) — directly, not tangentially.
- **Source:** `[SE-TOOLSPKG25]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** A full, official skills framework
  dividing AI skills into three domains — technical, responsible/ethical,
  non-technical — across three job levels (entry, mid, managerial), explicitly
  designed to be cumulative (higher levels retain lower-level skills like AI
  literacy, prompt writing, output evaluation) rather than replacing them.
  Explicitly aligns with the UK Standard Skills Classification, the SFIA AI
  Skills Framework, and the Alan Turing Institute's AI Skills for Business
  Competency Framework. A companion 9-stage Adoption Pathway Model (Awareness
  → Exploration → Assessment → Experimentation → Reflection → Upskilling →
  Integration → Strategy → Scaling) links organisational maturity to which
  skill types become critical at each stage. A companion Employer AI
  Adoption Checklist provides self-assessment prompts across strategic
  alignment, experimentation, skills/capacity, risk, equity/inclusion,
  support, and evaluation. Notably, the source states non-technical skills
  (critical thinking, describing AI's relevance to your role, adapting to
  new tools) were identified by workshop participants as "the most urgently
  needed" — not technical skills.
- **Inference drawn:** None — content read directly from the primary
  document.
- **Limitations / conflicting evidence:** The framework's authors state it
  does not yet address sector-specific technical/ethical demands (health,
  finance, creative, etc. all vary) and should be treated as a starting
  point rather than a finished standard. It is explicitly derived from the
  same evidence base as Entries 010/012, so it isn't independent
  corroboration — it's the same research programme's output.
- **Effect on project direction:** This is a genuine candidate reference
  point for defining "practical AI capability" (Priority 3) and structuring
  a learning pathway (Priority 4) — potentially more directly usable than
  building a framework from scratch, consistent with the project's stated
  approach of learning from existing work rather than imitating a whole
  product. The "non-technical skills are most urgently needed" finding is
  also a second, independent-ish confirmation of the literacy-over-technical
  framing first suggested in Entry 002.

### Entry 018 — UK AI Skills Hub (Priority 5 — comparable existing programme)

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 5 — comparable products and programmes;
  also relevant to Priority 10 (positioning/sustainability).
- **Source:** `[AISKILLSHUB]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** A live, government-backed national
  platform (Innovate UK, with Skills England and PwC/industry support) that
  curates AI training resources for employers and individuals, benchmarked
  against Skills England's AI Foundation Skills standard. Initially focused
  on four sectors (agriculture/food processing, construction, creative, and
  transport/logistics/warehousing) under the BridgeAI programme, then
  expanded on 28 Jan 2026 to all UK adults, with a stated ambition to
  upskill 10 million workers by 2030. Offers curated course libraries, a
  diagnostic/personalised pathway tool, sector use cases, and a completion
  badge aligned to the official skills benchmark.
- **Inference drawn:** None stated as fact; direct homepage fetch failed (402
  error), so this entry relies on the site's own "About us" page plus
  secondary press coverage rather than a full first-hand read of the
  platform itself.
- **Limitations / conflicting evidence:** Scale and funding here are very
  different from anything Grounded AI Practice could realistically build —
  this is a large, funded, multi-partner national platform, not a
  comparable-sized project. The comparison value is in understanding what
  already exists and where it does or doesn't serve the project's intended
  audience, not in matching its scale.
- **Effect on project direction:** Directly answers a previously untouched
  Priority 5 question: a well-resourced, official comparable already
  exists and directly targets UK workforce AI upskilling. This raises a
  real question for later: what would Grounded AI Practice do differently
  or in addition to this platform, rather than duplicate it? Worth reading
  the platform itself directly (not just its About page) in a future pass.

### Entry 019 — Skills England Annual Skills Report 2026 (Chapter 3: AI)

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 1 (evidence and problem framing), Priority
  3 (capability definition) — a major source for both.
- **Source:** `[SE-ANNUAL26]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** The UK's high AI exposure means
  significant potential benefit — OECD (2025) estimates AI could lift UK
  productivity growth by 0.4 to 1.3 percentage points over the next decade;
  IMF analysis (Cazzaniga et al., 2024) estimates around 70% of UK workers
  are in occupations containing tasks AI could perform or enhance. AI
  exposure is highest in professional, analytical, higher-paid occupations
  (cognitive, clerical, data-driven work) and lowest in construction and
  hospitality. On organisational adoption, ONS (2025) data shows firms with
  stronger management practices are more likely to adopt AI and realise
  productivity gains; common barriers are cost/time of implementation, lack
  of relevant skills, and difficulty identifying viable use cases —
  especially acute for SMEs despite their usual agility advantage. PwC's AI
  Jobs Barometer (2025) finds UK employer requirements for AI roles evolving
  66% faster than other jobs, with a 56% wage premium for AI-skilled
  workers, and finds AI is "largely being used to support workers rather
  than replace them." Directly relevant to the technical-vs-literacy framing
  question open since Entry 001/002: Skills England states, drawing on the
  Ameen "AI Skills for the UK Workforce" research, that most workers will
  require practical AI literacy (using, verifying, and safely integrating AI
  tools) while only a smaller share need specialist technical skills, with
  employers valuing judgement, problem-solving, collaboration, and
  responsible AI capability over routine technical execution. The report
  also introduces a distilled "AI foundation skills for work" benchmark: 6
  foundation skills across 3 domains (technical, non-technical, responsible/
  ethical) underpinning the national AI Skills Boost / AI Skills Hub
  programme (see Entry 018).
- **Inference drawn:** None beyond what's stated.
- **Limitations / conflicting evidence:** Notably, the report itself
  presents a genuine, unresolved disagreement rather than picking a side:
  KCL research (Klein Teeselink, 2025) and Adzuna (2026) data suggest AI is
  hurting graduate/entry-level hiring (firms cutting junior roles, fewer
  vacancies, graduate ads down 45% in 2025), while the LinkedIn Economic
  Graph Research Institute and an FT analysis (Burn-Murdoch & O'Connor,
  2026) find no clear evidence AI specifically (rather than post-COVID or
  cyclical effects) is driving the graduate slowdown. Skills England's own
  conclusion is "too early to say." This is a good model of the
  confirm/disconfirm discipline discussed earlier in this log — worth
  noting as an example, not just a data point. As with Entries 010/012/017,
  this report draws on the same Ameen research programme for its literacy-
  vs-technical conclusion, so it isn't fully independent corroboration.
- **Effect on project direction:** Likely the single most load-bearing
  official source found so far for both Priority 1 and Priority 3. It gives
  authoritative current national context, explicit official support for a
  literacy-first (not technical-first) capability definition, and a
  ready-made official skills benchmark to reference for Priority 3/4. The
  technical-vs-literacy tension flagged since Entry 001 is now well-supported
  toward "literacy first" — not fully independently resolved, but no longer
  an open coin-flip either.

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

**Resolved this pass:**
- ~~Stale ONS baseline~~ — updated (Entry 003) with current official data
  through June 2026. ONS's own framing is "slow, uneven adoption," a useful
  independent counterweight to vendor-sourced "urgent gap" claims.
- ~~Turing/Ada Lovelace findings unread~~ — done (Entry 005 upgraded). Real
  findings now logged, including a genuine equity nuance rather than a
  single "disadvantaged = more sceptical" story.

**Resolved this pass:**
- ~~No education-sector-specific evidence~~ — filled (Entry 016). DfE's own
  data shows real but early, uneven adoption — consistent with the ONS
  "slow, uneven change" reading rather than the vendor-sourced "crisis"
  framing.

**Resolved this pass:**
- ~~Priority 3/4 capability definition~~ — a genuine candidate framework now
  exists (Entry 017) rather than needing to be built from scratch.
- ~~Priority 5 comparables~~ — no longer completely untouched (Entry 018): a
  well-resourced official comparable exists, raising a real differentiation
  question for later.

**Partially followed up:** Skills England's Annual Skills Report has now
been read directly (Entry 019). Its companion Sectoral Skills Needs
Assessments (10 sector-specific reports, published alongside it) have not
been read individually — flagged as a lead for later if a specific sector
becomes relevant to Priority 2's audience decision.

**Resolved this pass:**
- ~~Skills England Annual Skills Report unread~~ — read directly (Entry
  019). Confirms this was worth prioritising: it's the strongest single
  official source found for Priority 1/3 so far.

**Substantially addressed, not fully closed:**
- **Technical-vs-literacy framing tension** (open since Entry 001/002) — now
  has explicit official backing toward "practical literacy first, technical
  specialism for a smaller share" (Entry 019), though this traces back to
  the same Ameen research programme as Entries 010/012/017 rather than
  fully independent triangulation.

**Still open:**
- **Systematic re-check needed on prior "skills gap" claims** (Entry 013) —
  no entry so far has been tested against disconfirming evidence or an
  independent replication. Priority: find UK-specific, non-commercial
  sources (academic, ONS, independent think tank) that either corroborate or
  complicate Entries 001, 002, 006, 008, 010, 012 before treating the
  "capability gap" as settled.
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
