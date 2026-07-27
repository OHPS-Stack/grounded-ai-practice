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

Scoping/creative decisions, design/production work and technical build
notes — anything durable that isn't source-backed research evidence — go in
`PROJECT_LOG.md` instead, not here. This file drifted into a mixed dump of
both for a while (see `PROJECT_LOG.md` Entry 017); the split below restores
the boundary.

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
| `[ROADMAP]` | Vendor/Commercial (product) — studied as a comparable product's design, not cited as evidence for a claim | roadmap.sh, developer-learning platform. Studied via its own site and secondary write-ups, not a full first-hand platform trial. roadmap.sh |
| `[LEETCODE]` | Vendor/Commercial (product) — studied as a comparable product's design, not cited as evidence for a claim | LeetCode, coding-practice platform. Studied via secondary write-ups (educative.io, GitHub study-plan compilations), not a full first-hand platform trial. leetcode.com |
| `[EOAI]` | Independent/Academic (non-profit + university, vendor-neutral by design) | Elements of AI, MinnaLearn & University of Helsinki — free public AI-literacy course, reported to have reached roughly 1 million learners globally. elementsofai.com; studied via Class Central course listing and Wikipedia, not a full first-hand course completion. |
| `[LSE-CARDOSO26]` | Independent/Academic (LSE) — opinion/blog piece, not peer-reviewed | Cardoso-Silva (LSE Data Science Institute) & Brown (LSE Digital Skills Lab), "The UK's AI training ambition deserves better than a course directory," LSE Impact of Social Sciences blog, 17 Feb 2026 — PRIMARY, read directly. blogs.lse.ac.uk/impactofsocialsciences/2026/02/17 |
| `[RS-AILIT25]` | Independent/Academic (Royal Society-commissioned) | Hillman (Goldsmiths), Holmes (UCL), Duarte (We and AI) et al., *A Rapid Review of AI Literacy Frameworks, with Policy Recommendations*, prepared for the Royal Society following a Jan 2025 roundtable — PRIMARY, read directly in full. Views are the authors', not the Royal Society's. royalsociety.org/-/media/policy/projects/ai-in-education/hillman-et-al-a-rapid-review-of-ai-literacy-frameworks.pdf |
| `[FDN26]` | Advocacy/Membership body (business-led digital-skills coalition, backed by major UK employers) | FutureDotNow, *Embedding AI into the Essential Digital Skills Framework* report, 2026 — read via FutureDotNow site summaries and secondary coverage, not the full primary PDF. futuredotnow.uk |
| `[TECHOSAURUS26]` | Vendor/Commercial (AI training company; direct commercial competitor to the platform reviewed) | Quilter (Techosaurus Ltd) & Farmer (Quantum Rise), "We Tested the Government's AI Skills Hub: Five Critical Flaws You Need to Know," Techosaurus News, 30 Jan 2026 — PRIMARY, read directly. techosaurus.co.uk/news/2026/01/30/we-tested-the-governments-ai |
| `[HUMANCO26]` | Vendor/Commercial (AI training/workplace-adoption consultant; direct commercial competitor to the platform reviewed) | Thomas (The Human Co.), "The UK Government's AI Skills Hub: A £4.1m Lesson in How Not to Build Real AI Capability," thehumanco.org, 2026 — PRIMARY, read directly. thehumanco.org/blog/ai-skills-hub-review |
| `[SE-PRIMES-EMPLOYER26]` | Government-commissioned / Academic author (same Ameen/Skills England/British Academy Fellowship programme as Entries 010/012/017) | Dr Nisreen Ameen, *What Works for AI Upskilling in the UK: Employer Guide*, 10 June 2026 — PRIMARY, read directly in full (the actual PRIMES accreditation-criteria document; Entry 012 was based on a secondary summary of this same underlying research programme). assets.publishing.service.gov.uk/media/6a27ec203b15d05a7ce31f3b/employer_guide.pdf |
| `[GRR-EBIP]` | Government/Official (US state education department) — general K-12 instructional-design guidance, not UK- or AI-specific | Kentucky Department of Education, "Evidence-Based Instructional Practices: Explicit Teaching and Modeling" (Gradual Release of Responsibility framework), education.ky.gov — read via search synthesis, not the full primary document. |
| `[KAMALI26]` | Independent/Academic (preprint — not confirmed peer-reviewed) | Kamali, Gerstner, Hullman & Groh, "Generative AI Literacy Training Improves Intelligence Analysts' Discrimination of Real and AI-Generated Images," arxiv.org/pdf/2606.28510 — read via WebFetch summary of the full PDF, not a full manual read. |
| `[AUTOBIAS-MED25]` | Independent/Academic (preprint, medRxiv — not peer-reviewed; primary PDF could not be fetched, UNVERIFIED beyond search-engine synthesis) | "Automation Bias in Large Language Model Assisted Diagnostic Reasoning Among AI-Trained Physicians," medrxiv.org/content/10.1101/2025.08.23.25334280 — direct fetch returned HTTP 403; claims here rely on WebSearch's own synthesis of the abstract, not a verified primary read. |
| `[BCC-ISER26]` | Independent/Academic (University of Essex ISER working paper, ESRC/UKRI-funded; lead author BCC-affiliated as the survey partner, tagged as mixed-interest for that reason) | Bharier (British Chambers of Commerce), Etheridge & Morais (University of Essex), *AI Adoption and Workforce Change in SMEs*, ISER Working Paper No. 2026-1, March 2026 — PRIMARY, read directly in full. iser.essex.ac.uk/wp-content/uploads/files/working-papers/iser/2026-01.pdf |
| `[BENNETT26]` | Independent/Academic (University of Cambridge, Bennett School of Public Policy) | Poquiz & Nguyen, "What does firm-level data tell us about AI adoption in the UK?", Bennett School blog, 13 April 2026, drawing on ONS Management and Expectations Survey and Business Insights and Conditions Survey — read via WebFetch summary, not the full primary analysis. bennettschool.cam.ac.uk/blog/ai-adoption-in-the-uk |
| `[LOCALAI-COST26]` | Vendor/Commercial (multiple SaaS/dev-tooling blogs — aggregate search synthesis, individual sources NOT independently fetched/verified) | Aggregate of local-vs-cloud-LLM cost comparison posts (PromptCost.org, SitePoint, Fungies.io, promptquorum.com, Swfte AI, kunalganglani.com, pristren.com), 2026 — UNVERIFIED beyond search-engine synthesis; treat directional consensus only, not individual figures, as indicative. |
| `[LOCALAI-CAPABILITY26]` | Vendor/Commercial (multiple SaaS/AI-infra blogs — aggregate search synthesis, individual sources NOT independently fetched/verified) | Aggregate of local-vs-frontier-model capability comparison posts (MindStudio, Qubrid AI, TechPlanet, byteiota, promptquorum.com), 2026 — UNVERIFIED beyond search-engine synthesis; treat directional consensus only, not individual figures, as indicative. |
| `[INSTRO26]` | Vendor/Commercial (UK bespoke AI integration company; suggested by the project's creator as a research lead) | Instro AI Solutions, instro.ai — read directly (homepage). UK-based bespoke generative-AI integrator for manufacturing, engineering and education sectors; "integration-first, not rip-and-replace." |
| `[INSTRO-TRIAL26]` | Independent trade press (IT Brief UK, part of the TechDay specialist network) reporting on an Innovation-funded trial coordinated with AMRC Cymru (Advanced Manufacturing Research Centre, a Welsh applied-research/innovation body) — treated as independent of Instro's own marketing, though it reports the vendor's own trial results | "Instro AI trials cut engineering response times by 67%," itbrief.co.uk — read directly. Reports named UK manufacturer outcomes (Colchester Machine Tool Solutions, Poeton Industries, Star Micronics) from an AMRC Cymru-coordinated trial. |
| `[BUYBUILD-KLOTZ26]` | Independent — preprint, institutional affiliation unclear, theoretical/conceptual not empirical, single author | Klotz, D., "The Buy-or-Build Decision, Revisited: How Agentic AI Changes the Economics of Enterprise Software," arXiv:2604.26482 — read directly. Superseded framing, see Entry 033: the project's creator judged this concept unsupported and unfair to Instro as applied here. Retained in the source key for traceability only. |
| `[CHEN-VAROQUAUX26]` | Independent/Academic (Imperial College London; Inria Saclay) | Chen, L. & Varoquaux, G., "What is the Role of Small Models in the LLM Era: A Survey," arXiv:2409.06857v7 (this version dated 19 Feb 2026) — PRIMARY, read directly in full. Systematic survey, not empirical original research, but grounded in and citing extensive empirical literature. |
| `[AGENTMESH26]` | Vendor/Commercial (multiple AI-infra/SaaS blogs — aggregate search synthesis, individual sources NOT independently fetched/verified) | Aggregate of "Executive-Worker" / heterogeneous agentic mesh architecture posts (Medium, futureagi.com, MindStudio, Glean), 2026 — UNVERIFIED beyond search-engine synthesis; the general pattern described (orchestrator model + specialised worker models) converges with `[CHEN-VAROQUAUX26]`'s academically-grounded model-cascading/routing literature, which is the credible version of this claim. |
| `[SE-FOUNDATIONBENCH26]` | Government/Official (Skills England/DSIT) | UK Government, *AI foundation skills for work benchmark*, gov.uk — PRIMARY, read directly. gov.uk/government/publications/ai-foundation-skills-for-work/ai-foundation-skills-for-work-benchmark |
| `[TADIMALLA-MAHER25]` | Independent/Academic (peer-reviewed AAAI journal) | Tadimalla, S.Y. & Maher, M.L., "AI literacy as a core component of AI education," *AI Magazine* (Wiley/AAAI), 2025 — read via WebFetch/search synthesis of the abstract and a ResearchGate-hosted copy; full text paywalled on Wiley (HTTP 402), **not read in full** — treat as a verified-abstract-level read, not a complete primary read. onlinelibrary.wiley.com/doi/10.1002/aaai.70007 |
| `[SAIL4ALL25]` | Independent/Academic (peer-reviewed, *Humanities and Social Sciences Communications*/Springer Nature; validated on UK samples) | "The scale of artificial intelligence literacy for all (SAIL4ALL): assessing knowledge of artificial intelligence in all adult populations," 2025 — read via search-engine synthesis of the abstract/structure only; direct fetch blocked by a Nature.com login wall, **not read in full**. nature.com/articles/s41599-025-05978-3 |
| `[WAGNER26]` | Independent commentary (opinion blog/Substack, no disclosed institutional affiliation — weak/low-credibility, flagged accordingly) | Michael G. Wagner, "Beyond the Tool: Why True AI Literacy is About Critical Thinking, Not Prompting," *The Augmented Educator* (Substack) — read directly via WebFetch. theaugmentededucator.com/p/beyond-the-tool-why-true-ai-literacy |
| `[HALLUC-AWARE26]` | Vendor/Commercial (multiple AI-training/content-marketing blogs — aggregate search synthesis, NOT independently fetched/verified) | Aggregate of workplace-AI-literacy-training blog posts (Thirst, GoWinston, Articulate, Ajaia) citing an unattributed "only 28% of adults know AI can fabricate facts" statistic, 2026 — UNVERIFIED, original source of the 28% figure not traced; treat as an unverified lead only, not evidence. |
| `[USDOL-AILIT26]` | Government/Official (US Department of Labor — **not UK**, included only as an international comparison point) | US Department of Labor, Employment and Training Administration, *Training and Employment Notice 07-25* (national AI Literacy Framework), Feb 2026 — read only via secondary coverage (Ogletree law-firm blog) and search synthesis, **primary PDF not fetched directly**; lists "Evaluating AI Outputs" as one of five key workplace AI-literacy content areas. dol.gov/sites/dolgov/files/ETA/advisories/TEN/2025/TEN%2007-25/TEN%2007-25%20(complete%20document).pdf |
| `[CALDAROLA-CLOUD26]` | Independent/Academic | Caldarola, F. & Fontanelli, L., "Scaling up to the cloud: Cloud technology use and growth rates in small and large firms," arXiv:2409.17035 (2026 revision) — PRIMARY, read directly (via proxy fetch after direct fetch of the PDF returned unreadable binary). Uses French INSEE firm-level administrative + survey data. About cloud technology generally, not AI specifically. |
| `[FRB-MONITORING26]` | Government/Official (US central bank research) | Federal Reserve Board, "Monitoring AI Adoption in the US Economy" (FEDS Notes, accessible version), 3 April 2026 — PRIMARY, read directly. federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-accessible-20260403.htm |
| `[STLFED-ASKMATTERS26]` | Government/Official (US central bank research) | Federal Reserve Bank of St. Louis, "Measuring AI Adoption among Firms: How You Ask Matters," On the Economy blog, June 2026 — read via proxy fetch after direct fetch returned HTTP 403. stlouisfed.org/on-the-economy/2026/jun/measuring-ai-adoption-firms-how-you-ask-matters |
| `[STLFED-MINDGAP26]` | Government/Official (US central bank research) | Federal Reserve Bank of St. Louis, "Mind the Gap: AI Adoption in Europe and the U.S.," On the Economy blog, March 2026 — read via proxy fetch after direct fetch returned HTTP 403. Does not disaggregate by firm size. stlouisfed.org/on-the-economy/2026/mar/mind-gap-ai-adoption-europe-us |
| `[SBA-ADVOCACY25]` | Government/Official (US Small Business Administration) — UNVERIFIED, could not be fetched | SBA Office of Advocacy, "Research Spotlight: AI in Business — Small Firms Closing In," Sept 2025. Both the PDF and blog-post versions returned HTTP 403 on every fetch attempt; claims about this source rest only on WebSearch's own synthesis, not a direct read. Do not cite beyond "a lead not yet confirmed." advocacy.sba.gov |
| `[OECD-SMEAI25]` | Government/Official (international body) — UNVERIFIED beyond search synthesis | OECD, "AI adoption by small and medium-sized enterprises," Dec 2025. PDF fetch returned unreadable binary/image content; findings rest on WebSearch synthesis only (large firms 40% vs small firms 11.9% adoption, OECD-wide). Not UK-specific. Confirms rather than disconfirms the size gap. oecd.org |
| `[MDPI-SMEAI-REVIEW26]` | Independent/Academic (peer-reviewed, open access) | "Artificial Intelligence in SMEs: Enhancing Business Functions Through Technologies and Applications," Information (MDPI), 16(5):415, systematic review of 50 studies 2016–2025 — read via proxy fetch. mdpi.com/2078-2489/16/5/415 |
| `[EPOCH-ECIGAP26]` | Independent/Academic-adjacent (nonprofit AI-trends research organisation; methodology openly published, Creative Commons licensed) | Epoch AI, "Open models lag state-of-the-art closed models by 4 months," Epoch Capabilities Index data insight, May 2026 — PRIMARY, read directly. epoch.ai/data-insights/open-closed-eci-gap |
| `[STANFORD-AIINDEX25]` | Independent/Academic | Stanford Institute for Human-Centered AI (HAI), *The 2025 AI Index Report*, "AI becomes more efficient, affordable and accessible" section — PRIMARY, read directly (partial — the specific section quoted, not the full report). hai.stanford.edu/ai-index/2025-ai-index-report |
| `[PROMPTCOST26]` | Vendor/Commercial — individually verified (was previously only part of the unverified `[LOCALAI-COST26]` aggregate) | PromptCost.org, "Local LLM Total Cost of Ownership 2026: Cloud vs Self-Hosted" — read directly via proxy fetch after direct fetch returned HTTP 403. promptcost.org/en/blog/local-llms-total-cost-ownership-2026/ |
| `[FUNGIES26]` | Vendor/Commercial (a payments/"merchant of record" platform for SaaS, publishing this as promotional content — not an AI or infrastructure company) — individually verified (was previously only part of `[LOCALAI-COST26]`) | Fungies.io, "Local LLM vs Cloud API: The Complete 2026 Cost Breakdown & Break-Even Guide" — read directly via proxy fetch after direct fetch returned HTTP 403. fungies.io/local-llm-vs-cloud-cost-2026/ |
| `[PROMPTQUORUM-COMPARE26]` | Vendor/Commercial (the article promotes PromptQuorum's own multi-model comparison product) — individually verified (was previously only part of `[LOCALAI-COST26]`/`[LOCALAI-CAPABILITY26]`) | PromptQuorum, "Local LLMs vs Cloud APIs 2026: Privacy, Cost, and Quality" — PRIMARY, read directly (fetched without needing a proxy). promptquorum.com/local-llms/local-llms-vs-cloud-apis |
| `[MINDSTUDIO26]` | Vendor/Commercial (MindStudio is a no-code AI workflow platform selling access to 200+ cloud and local models) — individually verified (was previously only part of `[LOCALAI-CAPABILITY26]`) | MindStudio, "Local AI vs Cloud AI in 2026: When to Run Models on Your Own Hardware" — PRIMARY, read directly (fetched without needing a proxy). mindstudio.ai/blog/local-ai-vs-cloud-ai-2026 |

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

### Entry 020 — Comparable platforms: roadmap.sh and LeetCode (Priority 5)

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 5 — "How do roadmap.sh, LeetCode and
  comparable learning systems define progression, prerequisites and
  completion?"
- **Source:** `[ROADMAP]`, `[LEETCODE]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** roadmap.sh presents learning as
  interactive flowchart-style roadmaps; users log in and mark each node as
  done/in-progress/skipped, turning the roadmap into a personal checklist.
  Prerequisites are not formally enforced by the system — they are implied
  by the visual flowchart layout only. Each node links out to curated
  external resources rather than hosting content itself. LeetCode structures
  learning around algorithmic-pattern problem sets of increasing difficulty,
  with points, badges and leaderboards, and frames practice explicitly around
  simulating real technical-interview scenarios.
- **Inference drawn:** Both platforms substitute a strong, low-cost
  progression *signal* (visual sequencing, difficulty tiers, gamified
  scoring) for formal prerequisite enforcement or credentialing — completion
  is self-reported/self-tracked, not assessed. This is an inference from
  how the mechanics are described, not a claim either platform makes about
  itself.
- **Limitations / conflicting evidence:** Checked via the platforms' own
  About pages and secondary write-ups (blogs, an educative.io explainer, a
  GitHub study-plan compilation) rather than a full first-hand trial of
  either platform. Neither is an AI-literacy product — both are included
  because RESEARCH_QUESTIONS.md names them specifically as design-pattern
  comparables, not as AI-literacy competitors.
- **Effect on project direction:** Directly answers the first Priority 5
  question. The transferable pattern for Grounded AI Practice is: visible,
  self-directed progression through a checklist/flowchart structure, paired
  with curated (not necessarily self-hosted) resources per step, is a
  proven low-overhead way to make a learning pathway feel navigable without
  building a full LMS or assessment engine. LeetCode's competitive/gamified
  layer is a design choice, not a requirement — worth noting as optional
  rather than essential, especially since Entry 023 flags gamified
  "confidence to use tools" framing as a risk when applied to AI literacy
  specifically.

### Entry 021 — Elements of AI (Priority 5, comparable AI-literacy programme)

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 5 — "How do existing AI-literacy and
  digital-skills programmes combine theory, practice and assessment?" /
  "Which features should Grounded AI Practice learn from without imitating
  the product as a whole?"
- **Source:** `[EOAI]`; independently referenced as the model the UK should
  have followed in `[LSE-CARDOSO26]` (see Entry 022).
- **Checked date:** 2026-07-24
- **What the source directly supports:** Elements of AI is a free, public,
  vendor-neutral online AI-literacy course from MinnaLearn and the
  University of Helsinki, reported to be the most-taken course in the
  university's history and to have reached roughly 1 million learners
  globally. It is structured as 6 chapters of 3 sections each, requires no
  programming or advanced maths, combines theory with practical exercises
  and self-reflection, uses peer review, and can be completed at a learner's
  own pace.
- **Inference drawn:** None stated as fact by the source; the "vendor-neutral"
  characterisation is repeated across multiple secondary sources
  (`[LSE-CARDOSO26]`, Class Central) rather than a claim Elements of AI makes
  about itself in the material checked here.
- **Limitations / conflicting evidence:** Checked via Class Central's course
  listing and Wikipedia's summary rather than a full first-hand completion of
  the course; no direct read of the course content itself, so claims about
  assessment rigour or actual learning outcomes are not independently
  verified here. Non-UK (Finland), and general-public in scope rather than
  targeted at a specific workforce audience.
- **Effect on project direction:** The strongest single comparable found for
  Priority 5's "existing AI-literacy programme" question — small production
  team, non-commercial, bite-sized modular chapters, no technical
  prerequisite, yet reached genuine scale. Directly relevant to the Priority
  2 audience decision: if a broad, low-barrier public-literacy audience is
  chosen, Elements of AI is the closest existing model to study in detail
  (not necessarily imitate) before finalising a delivery format.

### Entry 022 — UK AI Skills Hub critiqued as "a directory, not a programme" (Priority 5, connects to Entry 018)

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 5 — "Where do existing products appear
  incomplete, inaccessible or overly tool-specific?" Directly extends Entry
  018 (AI Skills Hub) with independent critical perspective, addressing the
  Research discipline requirement to pair confirming evidence with
  disconfirming/critical checks for foundational claims.
- **Source:** `[LSE-CARDOSO26]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** The authors (an LSE data science
  academic and the head of LSE's Digital Skills Lab) argue the UK AI Skills
  Hub (Entry 018) functions as "a mixture of existing training content
  loosely connected by the topic of AI" rather than a structured programme:
  no mapped progression pathways, no explicit mapping of courses to the
  competencies identified by government-commissioned research (i.e. the same
  Ameen/Skills England evidence base as Entries 010/012/017/019), and course
  organisation by technology vendor rather than by competency — despite that
  same evidence base finding non-technical skills (ethics, critical
  thinking) most needed by over 72% of surveyed organisations. They
  explicitly name Elements of AI (Entry 021) as the vendor-neutral,
  structured-pathway model the UK should have followed, summarising their
  argument as "a programme, not a directory."
- **Inference drawn:** None beyond what the authors state; this is their
  own argued position, not presented as new primary data.
- **Limitations / conflicting evidence:** An opinion/blog piece on an
  academic institution's blog, not a peer-reviewed paper — carries the
  authors' institutional credibility but not the same evidentiary weight as
  the primary government sources it critiques. Only one critical source
  found on this specific point; no second independent critique of the AI
  Skills Hub has yet been located to corroborate this reading.
- **Effect on project direction:** Materially changes how Entry 018 should
  be read — the AI Skills Hub is not just "a well-resourced comparable to
  differentiate against" but a concrete, named example of exactly the
  directory-not-programme failure mode Grounded AI Practice should avoid.
  This gives Priority 5's "learn from without imitating" question a sharper
  answer: the differentiation opportunity is not scale (the project cannot
  compete there) but *coherent, competency-mapped progression* — something
  even a major national platform reportedly got wrong.

### Entry 023 — Royal Society rapid review of AI literacy frameworks (Priority 5, also bears on Priority 3/4)

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 5 (comparable frameworks/programmes and
  international case studies), with direct relevance to Priority 3
  (capability definition) and Priority 4 (learning design).
- **Source:** `[RS-AILIT25]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** A systematic (PRISMA-informed)
  review that screened ~68,000 articles down to 115, analysed 20 AI-literacy
  frameworks and 6 national case studies in depth. Its scope is **AI
  literacy for school-age children (5–18) and their teachers** — not adults,
  not the general workforce. Key findings: (1) almost all 20 frameworks
  scored heavily toward the "technological" dimension (how AI works) and
  weakly toward the "human" dimension (societal/ethical impact) — the
  authors argue this makes most existing frameworks "more useful for
  children interested in computing than for all children"; (2) most
  frameworks trace back to only three foundational papers, risking a narrow
  intellectual base; (3) independent evaluation of any framework's real
  classroom impact is "almost entirely absent" across the whole literature;
  (4) SEND/accessibility design is rare to absent; (5) corporate-funded
  frameworks tend to push "confidence to use AI tools" as the goal rather
  than critical judgement about whether to use it at all — flagged as a risk
  of "deterministic, tool-first adoption." Six international case studies
  (Finland, South Korea, Maryland USA, Italy, Singapore, Uruguay) each
  illustrate a different implementation model: cross-disciplinary co-design,
  teacher-first infrastructure, whole-system values-led governance,
  teacher-first CPD cascades, whole-of-society scaffolded pathways, and
  infrastructure-plus-specialist-support respectively. The recommended UK
  implementation pathway is explicitly staged: pilot first (in a small
  number of regions/institutions) → embed independent evaluation from day
  one → only then scale, with inclusion/SEND designed in from the outset
  rather than retrofitted.
- **Inference drawn:** The three-dimension structure (technological /
  practical / human) and the "most frameworks are computing-education in
  disguise" critique are the report's own framing, not this project's
  extrapolation. Applying the pilot-first/inclusion-first pathway or the
  three-dimension structure to an *adult* general-public or workforce
  audience (as opposed to schoolchildren) would be this project's own
  extension — the report does not make that claim itself.
- **Limitations / conflicting evidence:** This is the single most
  significant scope mismatch found in the research log so far: the report's
  entire evidence base, all 20 frameworks and all 6 case studies, concerns
  children in compulsory education, not the adult/workforce audience the
  project's current problem statement centres on (PROJECT_BRIEF.md). Its
  findings about framework design, corporate-influence risk and
  implementation sequencing may transfer to an adult context, but this has
  not been tested and should not be assumed. Also worth flagging: the
  report's own scoring methodology (0–1 per topic, author-judged) is
  explicitly described by its authors as "highly interpretative" and "not
  ... definitive."
- **Effect on project direction:** High value for Priority 4 (learning
  design) and Priority 5 (comparable programmes) as a source of
  *transferable design lessons* — the three-dimension framework, the
  pilot-first/evaluate/scale sequencing, and the corporate-influence caution
  are all directly usable regardless of audience age. But it must not be
  cited as evidence about adult AI literacy or workforce capability — doing
  so would repeat the Entry 001 scoping error (citing a source for a
  population it wasn't about). If schools/education becomes a stronger
  candidate audience following Entry 016, this becomes a much more directly
  applicable source than it currently is for the project's present
  workforce/public framing.

### Entry 024 — FutureDotNow: Essential Digital Skills Framework AI update (Priority 5)

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 5 — comparable frameworks; also touches
  Priority 3 (capability definition), overlapping with but independent in
  origin from the Skills England/Ameen programme (Entries 010/012/017/019).
- **Source:** `[FDN26]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** Recommends four core AI
  competencies for the UK's existing Essential Digital Skills Framework:
  foundational knowledge of what AI is and how it functions, effective AI
  interaction (instruction-writing), critical evaluation of AI-generated
  content, and ethical/responsible use. Frames these as needed consistently
  across sectors (cited examples span NHS administrators to SME
  entrepreneurs). Cites modelled economic benefits (£23bn annual uplift,
  £10bn workforce income increase, £8.5bn industry profitability) from
  closing the essential digital skills gap more broadly, not AI skills
  specifically.
- **Inference drawn:** None stated as fact by the source.
- **Limitations / conflicting evidence:** FutureDotNow is a business-led
  digital-skills coalition backed by major UK employers — an
  Advocacy/Membership-body interest per this log's tagging convention, and
  the economic-benefit figures are modelled projections, not measured
  outcomes. Checked via FutureDotNow's own site summaries and secondary
  coverage rather than the full primary report PDF. The four-competency
  structure is broadly consistent with, but independently framed from, the
  Skills England/Ameen technical/non-technical/responsible three-domain
  model (Entry 017) — a second, differently-sourced convergence on a
  similar shape, which is mildly reassuring but not independent proof, since
  both ultimately feed into the same national Essential Digital Skills
  Framework policy process.
- **Effect on project direction:** A minor additional data point for
  Priority 3's capability definition — mostly useful as a second framework
  shape to sanity-check Skills England's against, and as one more source
  that a four-part (know/interact/evaluate/ethics) or three-part
  (technical/non-technical/responsible) structure recurs across
  independently-authored UK frameworks. Not load-bearing on its own given
  the advocacy-body interest and secondary sourcing.

### Entry 025 — The "directory not programme" critique is not isolated to LSE (Priority 5, corroborates Entry 022)

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 5, specifically testing whether the
  LSE critique (Entry 022) is a one-off academic opinion or a broader,
  corroborated pattern — directly relevant to the project's stated aim of
  positioning as a credible response to AI Skills Hub's problems
  ([[project_government_recognition_goal]]).
- **Source:** `[TECHOSAURUS26]`, `[HUMANCO26]`; a wider search also surfaced
  Computer Weekly, People Management and TechPolicy.Press opinion pieces
  making related but unread arguments (see Limitations).
- **Checked date:** 2026-07-24
- **What the source directly supports:** Both sources conducted hands-on
  testing of the live AI Skills Hub platform (not just its About page) and
  independently converge on the same structural failure as `[LSE-CARDOSO26]`:
  no sequencing or diagnostic-driven personalisation (`[HUMANCO26]` found
  intermediate users shown 71% beginner-level content, inflating study time
  from a claimed 25–35 hours to an actual 50–73 hours), no embedded practice
  environment/sandbox (`[TECHOSAURUS26]`'s "Missing Learning by Play"),
  vendor/platform lock-in from tool-specific rather than transferable
  courses, and — echoing `[LSE-CARDOSO26]`'s 72% non-technical-skills
  finding — a mismatch between what the Hub teaches and what users actually
  need. `[HUMANCO26]` separately reports the Hub's cost as £4.1 million and
  rates its design 3/10 despite judging its underlying course *content*
  adequate. `[TECHOSAURUS26]` additionally flags an "organisational
  readiness" gap: the Hub trains individuals while ignoring whether their
  workplaces are ready to support what they learn.
- **Inference drawn:** The convergence of an independent academic source
  (LSE) with two unconnected commercial-sector hands-on reviews, landing on
  overlapping specific findings (sequencing, personalisation, sandbox
  practice, competency-vs-vendor organisation), is stronger evidence that
  the underlying design problem is real than any single source alone —
  this is an inference about corroboration strength, not a claim any one
  source makes.
- **Limitations / conflicting evidence:** Both `[TECHOSAURUS26]` and
  `[HUMANCO26]` are written by founders of competing commercial AI-training
  businesses reviewing a free government platform — a direct commercial
  interest in positioning the Hub as inferior, tagged Vendor/Commercial per
  this log's convention. Their specific UX findings (e.g. the 71%/50–73
  hour figures) are self-reported from their own limited testing sessions,
  not independently audited. The Computer Weekly, People Management and
  TechPolicy.Press pieces found in the same search were not read in this
  pass — flagged as a lead only, not a finding, consistent with the
  project's "don't chase every thread" discipline. No defence or response
  from DSIT/Skills England to any of this criticism has been located yet.
- **Effect on project direction:** Meaningfully strengthens the basis for
  the project's loosely-held government-recognition aim
  ([[project_government_recognition_goal]]): the "directory not programme"
  critique is corroborated across independent academic and commercial
  sources, not a single contested opinion, which is exactly the kind of
  triangulation this project's research discipline calls for before treating
  something as foundational. Practically, it also sharpens what a credible
  alternative would need to demonstrably fix, beyond just "competency
  mapping": diagnostic-driven sequencing, embedded low-stakes practice
  (a "sandbox"), transferable (not vendor-locked) skills, and attention to
  organisational readiness alongside individual training. These read as
  candidate design requirements for Priority 4, not yet project decisions.

### Entry 026 — PRIMES accreditation criteria in full (Priority 4, supersedes summary in Entry 012)

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 4 — "Which recognised learning frameworks
  are suitable for this project?" Directly extends Entry 012, which described
  PRIMES only at the level of its six names; this entry reads the actual
  accreditation criteria document.
- **Source:** `[SE-PRIMES-EMPLOYER26]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** The full *Employer Guide* sets out
  detailed, checklist-style accreditation criteria for each PRIMES principle
  (reproduced in the source's Table 2). Selected specifics not previously
  captured in Entry 012: **Practical** requires training to recognise and
  build on existing informal/self-taught AI use rather than assuming a
  zero-starting point, and to make explicit *when AI should and should not
  be used*. **Reachable** requires training design to "explicitly consider
  intersecting barriers (e.g. income, age, disability, gender) rather than
  treating learners as single categories," and to build confidence
  alongside skills "particularly for learners with prior exclusion from
  digital or technical education." **Integrated** requires baseline AI
  training to be *mandatory* before staff use workplace AI tools involving
  organisational data, confidential information, regulated activity, safety
  or professional judgement. **Modular** specifies very short (30–90
  minute), stackable units as more practical than long courses for
  time-constrained learners, with entry at different levels and return
  points. **Expandable** prioritises transferable skills applicable "across
  different tools, systems, roles and organisations" over tool-specific
  competence. **Sustainable** requires planned review points (explicitly
  named: revisiting training at 3 and 6 months), outcome monitoring beyond
  satisfaction (confidence, quality of use, decision-making), and
  responsible-use content (confidentiality, data protection, transparency,
  human oversight) treated as core and enduring, not an optional module. The
  guide also lists 13 common pitfalls (e.g. "training is too fast, too
  technical, or assumes prior knowledge," "existing skills and informal AI
  use are not recognised," "training focuses on tools rather than
  transferable skills") and a companion "AI Skills Adoption Pathway" showing
  survey respondents' organisations are still overwhelmingly concentrated in
  early stages (Awareness 21%, Exploration 19%) versus advanced stages
  (Integration 7%, Strategy 4%, Scaling 1%).
- **Inference drawn:** None beyond what the source states — this entry
  intentionally stays close to direct quotation/paraphrase given how
  directly reusable this criteria set is for Priority 4 design work.
- **Limitations / conflicting evidence:** Same underlying evidence base as
  Entries 010/012/017/019 (23 workshops, 10 case studies, 536-response
  survey) — not independent corroboration, just a fuller read of the same
  programme's output. The employer-facing framing (PRIMES is written for
  *employers* designing workforce training) means some criteria assume an
  organisational context (paid/protected learning time, workplace data
  systems, line-management sponsorship) that may not transfer directly to a
  personal/public-facing project without an employing organisation behind
  the learner.
- **Effect on project direction:** This is now the single most directly
  actionable Priority 4 source in the log. Three specific, checkable design
  requirements stand out as strong candidates regardless of what Priority 2
  decides about audience: (1) modular units in the 30–90 minute range with
  clear entry/re-entry points, matching the "short chapters, no
  prerequisites" pattern already found in Elements of AI (Entry 021); (2)
  explicit "when AI should and should not be used" content, not just how-to
  content — a direct answer to Priority 6's scope question; (3) planned
  revisit points (3/6-month equivalents) and outcome tracking beyond
  completion counts, directly addressing the "near-total absence of
  independent evaluation" gap flagged industry-wide in Entry 023.

### Entry 027 — Gradual Release of Responsibility: a named model for the "explanations → practice → reflection" sequencing question

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 4 — "How should explanations, worked
  examples, guided practice, independent practice and reflection be
  sequenced?"
- **Source:** `[GRR-EBIP]`; the general pattern is also implicitly present
  in `[RS-AILIT25]`'s language of "scaffolded progression" (Entry 023) and
  PRIMES' "Modular" principle (Entry 026).
- **Checked date:** 2026-07-24
- **What the source directly supports:** The Gradual Release of
  Responsibility (GRR) model structures instruction in phases that shift
  cognitive load progressively from instructor to learner: focused
  instruction (explicit modelling/worked examples) → guided instruction
  (practice with support) → collaborative learning (practice with peers) →
  independent learning (unsupported application). Evidence-based-practice
  guidance associated with this model also recommends *spaced* rather than
  massed independent practice for retention.
- **Inference drawn:** RESEARCH_QUESTIONS.md's own Priority 4 phrasing
  ("explanations, worked examples, guided practice, independent practice and
  reflection") already closely mirrors GRR's structure — this is noted as an
  observation about the project's own question framing, not a claim the
  source makes. Applying a K-12-focused instructional model to adult,
  self-directed, largely asynchronous AI-literacy learning is this project's
  own extension, not something the source itself addresses; adult-learning
  research (e.g. andragogy, self-directed learning) may complicate the
  direct transfer, which has not yet been checked.
- **Limitations / conflicting evidence:** The source is a US state
  education department's K-12 guidance document, read only via search
  synthesis rather than the full primary document — general pedagogical
  currency (GRR/"I do, we do, you do" is a widely-cited model, originating
  with Pearson & Gallagher 1983) is asserted here based on how commonly it
  recurs in instructional-design literature, not independently verified in
  this pass. Not UK-specific, not AI-specific, not adult-education-specific.
- **Effect on project direction:** Gives the project a named, well-established
  reference model to explicitly adopt, adapt, or consciously depart from for
  Priority 4's sequencing question, rather than inventing a sequencing logic
  from scratch — consistent with the project's stated approach of learning
  from existing frameworks rather than building one unassisted. The one
  specific transferable recommendation from the evidence-based-practice
  literature (spaced rather than massed independent practice) is worth
  testing directly against PRIMES' 3/6-month revisit-point recommendation
  (Entry 026) — the two independently-sourced recommendations point the same
  direction.

### Entry 028 — AI literacy training and overconfidence: a genuine confirm/disconfirm pair

- **Date logged:** 2026-07-24
- **Priority / Question:** Priority 4 ("How should misconceptions, unsafe
  practices and overconfidence be addressed?") and Priority 6 (responsible
  use, human oversight).
- **Source:** `[KAMALI26]` (confirming: training helps) vs. `[AUTOBIAS-MED25]`
  (disconfirming/complicating: training alone may be insufficient) — a
  deliberately paired search per this log's own bias-mitigation discipline
  (see the note above Entry 001).
- **Checked date:** 2026-07-24
- **What the source directly supports:** `[KAMALI26]` reports that targeted
  generative-AI literacy training improved intelligence analysts' ability to
  distinguish real from AI-generated images *and* improved confidence
  calibration — post-training confidence better matched actual accuracy,
  rather than the training simply making people more skeptical across the
  board. `[AUTOBIAS-MED25]`'s abstract, per search-engine synthesis only
  (primary PDF fetch blocked, HTTP 403 — **not independently verified**),
  reportedly found that 44 physicians who completed a 20-hour AI-literacy
  training programme still exhibited automation bias in LLM-assisted
  diagnostic reasoning, suggesting training alone was not sufficient in that
  higher-stakes clinical context. Separately, broader review literature
  found via the same search (not read in full) describes an "overconfidence
  paradox": people with surface-level AI knowledge can become *more*
  susceptible to automation bias than complete novices, because they have
  "just enough knowledge to think they understand AI but not enough to
  recognise its limits" — and that automation bias/trust miscalibration can
  operate unconsciously, so self-reported vigilance may overstate actual
  behaviour.
- **Inference drawn:** The two studies are not strictly contradictory — they
  differ in domain (image authenticity judgement vs. high-stakes clinical
  diagnosis), training design (unspecified vs. 20 hours), and possibly in
  whether calibration or bias-resistance was directly targeted vs. a
  byproduct. A plausible reading (inference, not stated by either source) is
  that literacy training can improve calibration in bounded, well-defined
  judgement tasks but may need reinforcement/behavioural nudges (as
  `[AUTOBIAS-MED25]`'s companion trial reportedly tests) to hold under the
  cognitive load of complex, high-stakes professional decisions.
- **Limitations / conflicting evidence:** `[AUTOBIAS-MED25]` is flagged
  UNVERIFIED — the primary source could not be fetched and this entry relies
  on a search tool's own synthesis of the abstract, which is a weaker
  evidentiary basis than this log's normal standard. `[KAMALI26]` was read
  via WebFetch summary of the full PDF rather than a manual line-by-line
  read. Neither is UK-specific. The "overconfidence paradox" claim is
  currently sourced only to an aggregated search summary, not a named,
  checkable paper — flagged as a lead, not a finding.
- **Effect on project direction:** This is a directly relevant, appropriately
  hedged answer to Priority 4's misconceptions/overconfidence question:
  training can improve calibration, but the "surface knowledge is more
  dangerous than no knowledge" pattern is a specific, concrete risk any
  learning design should guard against explicitly — e.g. by pairing
  knowledge content with deliberate practice at *judging one's own
  confidence* against ground truth (matching `[KAMALI26]`'s apparent design),
  not just teaching facts about how AI works. This reinforces PRIMES'
  "Sustainable" criterion of monitoring "impacts on judgement and
  decision-making" over time (Entry 026) rather than treating a single
  training session as sufficient. Given the primary-source verification gap
  on `[AUTOBIAS-MED25]`, this should be re-checked in a future pass before
  being treated as settled — flagged in Open Threads.

### Entry 029 — Testing the "large orgs benefit disproportionately from AI" hypothesis: a genuine confirm/complicate pair

- **Date logged:** 2026-07-24
- **Priority / Question:** New hypothesis raised by the project's creator
  (2026-07-24): that AI's benefits accrue disproportionately to
  well-resourced organisations relative to individuals/SMEs, and that this
  could be the project's underlying thesis. Bears on Priority 1 (evidence
  for the problem) and directly tests the audience/thesis decision recorded
  in PROJECT_BRIEF.md's "Primary audience" section.
- **Source:** `[BCC-ISER26]` (primary, UK-specific, rigorous) and `[BENNETT26]`
  (primary, UK-specific, ONS-sourced) — deliberately sought together per this
  log's confirm/disconfirm discipline, since this is exactly the kind of
  foundational claim that would change project direction.
- **Checked date:** 2026-07-24
- **What the source directly supports:** `[BCC-ISER26]` surveyed 668 UK
  firms (84% with 1–250 employees) via the British Chambers of Commerce's
  January 2026 Business Outlook Survey. Headline: 54.3% of firms now use AI
  in some form (up from ~23% in 2023), and adoption is "strongly associated"
  with firm size, though the effect size is modest once controls are added
  (OR ≈ 1.09–1.14 per log-unit of firm size, statistically significant but
  not large). Critically, the paper's central and most robust finding is a
  **different** distinction: only 10% of firms have adopted "bespoke"
  AI (custom-built for their operations, typically requiring dedicated AI
  integrators or external vendors) versus the majority using only generic
  tools (ChatGPT/Copilot); it is specifically bespoke adoption — not AI use
  in general — that is associated with real workforce effects (~20% of
  bespoke adopters report staffing reductions vs ~3% of generic-only users;
  bespoke adopters are 3x more likely to restructure job roles). `[BENNETT26]`
  independently reports a starker adoption-rate gap using ONS data: large
  firms (250+ employees) adoption nearly doubled from ~20% (2023) to 44%
  (2025), while small firms (<50 employees) reached only 26% by 2025 — a
  "two-speed race" the authors attribute to "scale... rather than...
  underlying productivity performance," i.e. a structural barrier, not a
  productivity-driven explanation.
- **Inference drawn:** The two sources measure adoption-rate gaps of
  different magnitudes (`[BCC-ISER26]`'s controlled effect is modest;
  `[BENNETT26]`'s raw gap is large) — plausibly reconciled by different
  samples (BCC's is SME-heavy by design, 84% ≤250 employees, so it may
  under-represent the largest firms driving `[BENNETT26]`'s "44%" figure) and
  different methods (controlled regression vs raw ONS trend), not a
  contradiction requiring further resolution before treating "firm size
  correlates with AI adoption" as reasonably well-supported. However, the
  sharper and more actionable finding — supported directly by `[BCC-ISER26]`'s
  data, not an inference — is that the disparity is really about **depth of
  implementation** (generic tool use vs bespoke/integrated deployment) more
  than about using AI at all. This reframes the project's hypothesis: SMEs
  and individuals are not simply "left out of AI" (most now use generic
  tools) — they lack access to the bespoke-implementation capability that
  requires dedicated AI integrators, which is where `[BCC-ISER26]` shows the
  real economic effects concentrate.
- **Limitations / conflicting evidence:** Both sources are cross-sectional/
  observational; `[BCC-ISER26]`'s authors explicitly caution against causal
  interpretation and note their bespoke-adopter subsample is small (65
  firms) — findings on "deep integration" (3.5% of firms) are described by
  the authors themselves as "indicative rather than definitive." A
  significant complication for the project's likely framing: `[BCC-ISER26]`
  finds a "replace-and-train" pattern — firms investing in AI training are
  *more* likely to expect headcount reductions, not less (14% vs 4%), and
  this holds even after controlling for restructuring. This complicates any
  simple "AI literacy protects individual workers" narrative — building
  bespoke AI capability, including at the individual level, could equally
  accelerate an employer's ability to restructure a role. Neither source was
  cited by the other, and neither was found via a search deliberately
  framed to find the *opposite* of the size-disparity claim (a
  "SME-advantage" search in this same session surfaced only vendor-interested
  content-marketing claims — see Entry 020's search log — not credible
  disconfirming academic evidence), so the disconfirming side of this pair is
  currently weak. Flagged in Open Threads as a gap.
- **Effect on project direction:** Meaningfully sharpens rather than simply
  confirms the hypothesis. The evidence supports a firm-size/resource
  disparity in AI adoption *depth* (generic vs bespoke), which is a more
  precise and defensible claim than a blanket "large orgs benefit, small
  ones don't." This suggests the project's differentiator should be framed
  around helping individuals and SME employees build **bespoke, tailored AI
  implementations** — the specific thing `[BCC-ISER26]` shows requires
  resources (dedicated integrators) that SMEs typically lack — rather than
  generic tool literacy alone, which most SMEs already have. It also
  surfaces a genuine tension the project should address explicitly rather
  than gloss over: capability-building of this kind could help an individual
  become more valuable/secure, or could equally help their employer automate
  their role — the "replace-and-train" finding means this isn't a
  straightforwardly feel-good thesis, and PROJECT_BRIEF.md's responsible-use
  framing should account for it.

### Entry 030 — Testing the "local/hybrid AI as cost and capability equalizer" hypothesis

- **Date logged:** 2026-07-24
- **Priority / Question:** Second half of the same hypothesis (Priority 6:
  "When does hands-on local AI provide educational value beyond using a
  cloud application?" / "Which tasks are better suited to local, cloud or
  hybrid processing?").
- **Source:** `[LOCALAI-COST26]`, `[LOCALAI-CAPABILITY26]` — both are
  aggregated search-engine syntheses of multiple vendor/SaaS-blog sources,
  **not independently fetched or verified**; treated as directional leads
  only, consistent with this log's practice of flagging unverified
  aggregate claims rather than citing them as settled fact.
- **Checked date:** 2026-07-24
- **What the source directly supports (directional only, unverified):**
  Local/self-hosted models reportedly become cheaper than cloud APIs only
  above a fairly high usage threshold (roughly 500K–2M tokens/day per one
  aggregated estimate) — below that, cloud remains cheaper once hardware,
  electricity and maintenance are counted, not just per-token price. Upfront
  hardware costs range from ~$700 (a used consumer GPU, low end) to
  $20,000–$30,000 (production-grade multi-GPU setups). On capability, local/
  open-weight models reportedly lag frontier cloud models by anywhere from
  3–6 months to 12–18 months depending on the source and benchmark, with the
  gap most pronounced on complex multi-step agentic tasks and least
  pronounced on common tasks like document processing, summarisation and
  classification. Multiple sources converge on recommending a **hybrid**
  architecture (local for privacy-sensitive/high-volume/production use,
  cloud for capability-critical or variable workloads) rather than a pure
  local-replaces-cloud approach.
- **Inference drawn:** If directionally correct, this complicates rather
  than confirms the "local AI as straightforward equalizer" framing: the
  break-even usage threshold and hardware capital outlay could make local
  AI *less* accessible for a genuinely resource-constrained individual or
  micro-business than for a well-capitalised firm — the opposite of an
  equalizing effect, unless usage patterns or hardware-sharing models change
  that calculus. This is an inference from the (unverified) figures, not a
  claim any source makes explicitly.
- **Limitations / conflicting evidence:** This is the weakest-sourced entry
  in the log to date — no individual source was fetched and read directly;
  all figures come from a search engine's own aggregation across multiple
  vendor-interested blogs (several appear to be SaaS/dev-tooling content
  marketing, plausibly incentivised to make one side of the cost comparison
  look favourable). The specific numbers (break-even thresholds, benchmark
  gaps) should not be treated as reliable without direct primary-source
  verification in a future pass. The directional shape (hybrid is the
  practical answer; pure local isn't uniformly cheaper or more capable) is
  more plausible than any single number here, if only because it recurred
  across independently-named sources.
- **Effect on project direction:** The honest, appropriately hedged
  takeaway is that "local/hybrid AI reduces cost and increases
  independence" is **not a safe assumption to build the project's thesis
  on without further, better-sourced verification** — it may be true for
  some use cases (privacy-sensitive, high-volume, production) and false for
  others (typical individual/SME usage volumes, where cloud may remain
  cheaper and more capable). This actually validates PROJECT_BRIEF.md's
  existing "local, cloud and hybrid" framing (plural, comparative) over a
  "local AI is the answer" framing — the project's original instinct to
  treat this as a *comparison to teach*, not a solution to prescribe, is
  better supported by this pass than a stronger local-AI-equalizer claim
  would have been. Before this technical claim is used in any external-facing
  document (cf. the government-recognition aim in
  [[project_government_recognition_goal]]), it needs primary-source
  verification — flagged in Open Threads.

### Entry 031 — Instro AI as a live illustration of the "bespoke gap" (extends Entry 029)

- **Date logged:** 2026-07-24
- **Priority / Question:** Extends Entry 029's finding that SMEs' real gap is
  *depth of AI implementation* (generic tools vs bespoke, integrator-built
  systems), not AI access itself. Suggested by the project's creator as a
  candidate case-study source.
- **Source:** `[INSTRO26]`, `[INSTRO-TRIAL26]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** Instro AI Solutions is a UK-based
  company doing precisely the "dedicated AI integrator" role Entry 029
  identifies as scarce among SMEs — bespoke generative-AI systems integrated
  into a client's existing ERP/CRM/QMS infrastructure ("integration-first,
  not rip-and-replace"), for manufacturing, engineering and education
  clients, hosted on AWS with UK-based implementation support. An
  Innovation-funded trial coordinated with AMRC Cymru and reported by
  independent trade press (`[INSTRO-TRIAL26]`) gives named, measured
  outcomes: Colchester Machine Tool Solutions cut engineering response
  times 67.3% (5.5 to 1.8 minutes); Poeton Industries cut first-response
  times 40–65%; Star Micronics saw technical decision-making accelerate
  44.6% across 1,222 uses. Critically, AMRC Cymru's own technical lead is
  quoted identifying the real bottleneck: not model capability, but
  "fragmented legacy data... carried for decades" and how information is
  organised across documents, systems and records.
- **Inference drawn:** This is a concrete, named illustration of Entry 029's
  abstract finding — the barrier to real AI benefit at SMEs is
  organisational/data/implementation maturity, not access to capable models.
  Read alongside the "replace-and-train" and vendor-dependency findings
  (Entries 029, 032), a further inference (the project's own synthesis, not
  stated by either source) follows: engaging an integrator like Instro
  closes the *implementation* gap effectively — the trial results are real
  and substantial — but does not, on the evidence available, obviously
  close the *understanding* gap: the client's own team gains a working tool,
  not necessarily the internal capability to evaluate, extend, govern or
  eventually reduce dependency on that system themselves.
- **Limitations / conflicting evidence:** `[INSTRO26]`'s own homepage
  provides no named case studies or figures — all concrete outcomes come from
  `[INSTRO-TRIAL26]`, a single trade-press article; the underlying
  AMRC Cymru trial report itself has not been read directly. This is a
  small, self-selected sample of manufacturing SME trial participants (not
  representative of SMEs broadly), and the trial was funded innovation
  support rather than a normal commercial engagement, which may not
  reflect typical cost/outcome ratios for an SME paying full price. As a
  vendor, Instro has a direct commercial interest in a narrative where
  integrator-led bespoke AI is the answer — tagged accordingly. The
  "outsourcing understanding" reading above is this project's own
  interpretation, not a claim made by either source or by Instro itself.
- **Effect on project direction:** Sharpens the project's differentiation
  question concretely. Instro (and companies like it) appear to do the
  *implementation* work well and demonstrably — this is not a gap Grounded
  AI Practice should try to compete on. The differentiation opportunity is
  specifically the *understanding* layer: helping individuals and SME staff
  build the internal capability to evaluate, question, and eventually reduce
  blind dependency on vendor-delivered AI systems, complementing rather than
  competing with integrators. Worth testing further (see Entry 032) before
  treating "outsourcing understanding" as an established phenomenon rather
  than this project's working hypothesis.

### Entry 032 — "Outsourcing understanding": conceptual backing from buy-vs-build theory

- **Date logged:** 2026-07-24
- **Priority / Question:** Directly tests the project creator's proposed
  concept (2026-07-24) that outsourcing AI integration to vendors means, to
  some degree, "outsourcing understanding." Bears on Priority 3 (which
  capabilities are transferable vs vendor-specific) and Priority 6
  (technical/conceptual scope).
- **Source:** `[BUYBUILD-KLOTZ26]`
- **Checked date:** 2026-07-24
- **What the source directly supports:** A theoretical/conceptual paper
  applying classical "buy vs build" transaction-cost and resource-based
  theory to agentic AI enterprise software decisions. Core argument: relying
  on bought (SaaS/vendor) AI solutions requires minimal internal development
  capability — convenient for firms without strong internal capability, but
  this "forecloses the development of internal AI capabilities," creating
  potential long-term strategic dependency. The paper frames organisational
  capability as a threshold variable: below a minimum level of internal AI
  development capability, in-house building is not viable "regardless of
  how favorable other factors may be" — meaning firms below that threshold
  are structurally pushed toward buying, which in turn keeps them below the
  threshold, a self-reinforcing dynamic.
- **Inference drawn:** This gives the "outsourcing understanding" concept
  real theoretical grounding — it isn't a novel idea invented for this
  project, but a documented pattern in the buy-vs-build/outsourcing
  literature applied here specifically to AI. The self-reinforcing
  "capability threshold" dynamic described is a stronger, more precise
  version of the project's original framing: it's not just that vendors
  don't transfer understanding, but that never building any internal
  capability can structurally trap a firm below the threshold where
  building becomes viable at all — a genuine vicious cycle, if the paper's
  theoretical claim holds empirically.
- **Limitations / conflicting evidence:** This is explicitly
  theoretical/conceptual, not empirical — no survey, case data, or
  quantitative test of the capability-threshold claim is presented in what
  was read. Single-authored, hosted on arXiv without a clear institutional
  affiliation or confirmed peer review, so it should be weighted as a
  reasoned argument worth testing, not as established fact. No disconfirming
  search was run for this specific claim (e.g. evidence that vendor
  relationships sometimes *do* transfer capability, through training,
  co-development or staged handover models) — flagged in Open Threads.
- **Effect on project direction:** Combined with Entry 031's concrete
  illustration, this gives "outsourcing understanding" real standing as a
  framing concept for the project — not proof, but a defensible, theoretically
  grounded hypothesis worth building the project's differentiation around:
  Grounded AI Practice's value is in raising organisations/individuals
  *above* the capability threshold where they can meaningfully evaluate,
  direct, and eventually reduce dependence on vendor-delivered AI — a
  distinct and complementary role to integrators like Instro, not a
  competing one. This is a stronger, more theoretically-grounded version of
  the project's original "local/hybrid as equalizer" framing (Entry 030),
  and notably doesn't depend on the shakier local-vs-cloud cost/capability
  claims that entry flagged as unverified — capability-building is the
  mechanism, not a specific local/cloud technical choice.

### Entry 033 - Correction: "outsourcing understanding" framing retracted (supersedes Entry 032)

- **Date logged:** 2026-07-24
- **Priority / Question:** Correction, per this log's convention of not
  silently altering prior entries (see document status note at the top of
  this log).
- **Source:** Direct instruction from the project's creator, 2026-07-24.
- **What changed:** The project's creator judged the "outsourcing
  understanding" framing (Entry 032, and its application to Instro AI in
  Entry 031) to be (a) unfair to Instro specifically - casting a company
  doing genuinely effective integration work as a source of a "dependency
  trap" was not the intent and is not a fair characterisation of what Instro
  does - and (b) not well supported as a general claim, consistent with
  Entry 032's own logged caveats (single-author preprint, no institutional
  affiliation confirmed, no disconfirming search run, theoretical not
  empirical).
- **Effect on project direction:** The "outsourcing understanding" / buy-vs-build
  capability-threshold framing is retracted as a thesis element. Entry
  031's underlying findings about Instro AI remain valid and useful - it
  continues to serve as a concrete, well-evidenced example of successful
  bespoke AI integration for UK SMEs (the AMRC Cymru trial results:
  Colchester Machine Tool Solutions, Poeton Industries, Star Micronics), and
  as an illustration of Entry 029's implementation-depth finding. It should
  be used and referenced only in that scope - as a positive example of
  current integration options - not as a foil for a vendor-dependency
  narrative. `[BUYBUILD-KLOTZ26]` is retained in the source key for
  traceability but should not be cited going forward.

### Entry 034 - Half two, refined: task/workflow specialisation, not local AI per se, is the real mechanism

- **Date logged:** 2026-07-24
- **Priority / Question:** Refines Entry 030 per direct guidance from the
  project's creator (2026-07-24): local AI is not a realistic standalone
  solution for SMEs/individuals; hybrid use - running local/smaller models
  specifically for custom, private work - is the realistic pattern; and the
  broader, more important idea is that task/workflow specialisation
  can produce better results for fewer tokens using less powerful models,
  which the creator suggested illustrating via Claude Code. Bears on
  Priority 4 (learning design) and Priority 6 (technical scope).
- **Source:** `[CHEN-VAROQUAUX26]` (primary, rigorous academic survey);
  `[AGENTMESH26]` (unverified aggregate, directionally consistent).
- **Checked date:** 2026-07-24
- **What the source directly supports:** `[CHEN-VAROQUAUX26]` is a
  systematic survey (Imperial College London / Inria) examining small
  models' (SMs) relationship to LLMs through Collaboration and
  Competition/Complementarity. Its central architectural argument directly
  supports the creator's framing: "rather than replacing one with the other,
  the optimal ecosystem is hybrid" - small/specialised models handling
  cost-effective, well-defined roles, large models supporting and guiding
  them. Specifically relevant mechanisms it documents: model cascading
  (a small model handles a query first; only queries it can't confidently
  answer are escalated to a larger model), model routing (a router
  directs each input to the most appropriate model in a pool based on task
  type), and speculative decoding (a small model drafts, a large model
  verifies) - all empirically-grounded techniques for "adaptive allocation"
  of compute that "preserves performance where needed while substantially
  reducing overall cost." The survey identifies three scenarios where
  small/specialised models are genuinely favoured on evidence, not just
  cost: computation-constrained environments (edge/low-latency), narrow
  task-specific environments (domain-specific data, tabular reasoning, short
  text - where "narrow semantic scope reduces the need for large contextual
  understanding"), and interpretability-required environments (healthcare,
  finance, law). It also cites Belcak et al. (2025) directly on point:
  "small language models are the future of agentic ai," arguing SMs suit
  the "many small, specialised, and repetitive tasks" that make up agentic
  systems.
- **Inference drawn:** Claude Code's own architecture (separate from any
  source read here - this is the project's own observation, not a claim
  made by `[CHEN-VAROQUAUX26]`) is a live, inspectable illustration of
  exactly this pattern: a capable orchestrating model handles ambiguous,
  multi-step planning, while scoped subagents and skills handle
  well-defined sub-tasks with narrower context - a practical instance of the
  task-decomposition/specialisation principle the survey documents
  academically. This is a strong candidate worked example for Priority 4
  (learning design) - it lets the project teach "specialise the task, not
  just the model" using a tool learners may already have direct access to,
  rather than requiring them to set up local model infrastructure to see
  the principle in action.
- **Limitations / conflicting evidence:** The survey's Section 5
  ("Limitations of Small Models") is an important balance: small/specialised
  models show weak generalisation on complex multi-step reasoning, degrade
  under distribution shift, and are prone to catastrophic forgetting -
  specialisation is a genuine trade-off, not a free efficiency gain, and the
  survey is explicit that the advantage comes from "a better alignment
  between task complexity and available data," not from small models being
  broadly as capable. `[AGENTMESH26]` remains an unverified vendor-blog
  aggregate and is cited only because its directional claims converge with
  the credible academic source, not as independent evidence in its own
  right. No claim here has been tested specifically against UK SME/individual
  usage patterns - this is a general technical-architecture finding, not
  audience-specific evidence.
- **Effect on project direction:** This gives the project a stronger,
  better-evidenced version of half two than either the original "local AI as
  equalizer" framing (now dropped per Entry 030's own hedging) or a vague
  hybrid gesture. The teachable mechanism is: match task complexity to model
  capability rather than defaulting every task to the largest available
  model - genuinely useful, evidence-backed practical AI literacy, and
  demonstrable via tools (like Claude Code) learners can observe directly,
  not just via hardware/local-model setup. This also sidesteps the
  unresolved local-vs-cloud cost verification gap (Entry 030) entirely: the
  specialisation principle holds regardless of whether the "smaller model"
  in question is local or a smaller cloud-hosted model.

### Entry 039 — Candidate core capabilities for the pilot unit (answers the open "which single capability" question)

- **Date logged:** 2026-07-25
- **Priority / Question:** Immediate priority Q5 / Priority 3 — the specific
  gap Open Threads flags as "the immediate next decision point, not yet
  addressed": which single core capability the pilot unit (decided in Entry
  035) should teach.
- **Source:** Synthesis of existing logged evidence — `[SE-TOOLSPKG25]`,
  `[SE-ANNUAL26]`, `[SE-WHATWORKS26]`/`[SE-PRIMES-EMPLOYER26]`, `[RS-AILIT25]`,
  `[FDN26]`, `[EOAI]`, Entry 028's automation-bias findings — plus one new
  primary source read this pass, `[SE-FOUNDATIONBENCH26]`. No new empirical
  data collected; this entry re-reads existing entries specifically through
  the "what's concrete enough for one 30–90 minute sitting" lens, which no
  prior entry had done directly.
- **Checked date:** 2026-07-25
- **What the source directly supports:** Four candidates emerge as
  independently well-evidenced and concrete enough to teach in one sitting:

  **A. Critically evaluating AI-generated output for accuracy/reliability
  before acting on it** (spotting hallucination, checking claims, judging
  when output needs verification). Support: `[SE-TOOLSPKG25]` — workshop
  participants named non-technical skills including critical thinking as
  "the most urgently needed," not technical skill. `[RS-AILIT25]` —
  explicit caution that "confidence to use tools" is a shallow goal
  corporate-funded frameworks tend to push, versus genuine critical
  judgement (a design risk to avoid, not evidence this is the right first
  topic, but relevant to how it should be framed if chosen). `[FDN26]` lists
  "critical evaluation of AI-generated content" as one of four core
  competencies. Entry 028 (`[KAMALI26]`) found targeted literacy training
  measurably improved people's ability to judge real vs. AI-generated
  content and calibrate confidence accordingly — direct evidence a
  short training intervention can move this specific skill.
  Audience fit: no technical prerequisite — a learner can be handed
  AI output to evaluate without needing to already know how to prompt.

  **B. Writing clear, effective instructions for AI tools (prompting/
  interaction)**. Support: `[FDN26]` lists "effective AI interaction/
  instruction-writing" as a core competency; `[SE-FOUNDATIONBENCH26]` lists
  "writing clear instructions for AI tools" as the first item under the
  "technical" domain of the UK Government's own six-skill AI foundation
  benchmark; `[EOAI]` and most comparable courses treat this as early
  content. Audience fit: genuinely no prerequisite, but is a "production"
  skill (what to say to AI) rather than a "judgement" skill (what to do with
  what AI says back) — less directly aimed at the responsible-use gap the
  project's problem statement centres on.

  **C. Understanding what AI systems can and cannot do — a working mental
  model of capability/limitation, not mechanism** (e.g. pattern-matching
  vs. reasoning, why confident-sounding output can still be wrong, what
  "training data" implies about currency/bias). Support: `[FDN26]` lists
  "foundational knowledge of what AI is and how it functions" as its
  first-listed competency; `[EOAI]`'s own chapter 1 opens here;
  `[SE-ANNUAL26]`'s foundation-skills benchmark groups a "how AI works"-
  adjacent skill under its domains. Audience fit: strong — genuinely
  prerequisite-free, and every other candidate arguably depends on some
  version of it. Risk: closest of the four to becoming abstract/lecture-
  style content rather than an active, practiced skill, which PRIMES'
  "Practical" criterion (`[SE-PRIMES-EMPLOYER26]`) and the GRR sequencing
  model (`[GRR-EBIP]`) both push against.

  **D. Responsible/safe use — what not to share with AI tools, when AI use
  needs disclosure or extra caution (confidential data, regulated
  decisions, high-stakes tasks)**. Support: `[FDN26]`'s fourth competency
  ("ethical/responsible use"); `[SE-PRIMES-EMPLOYER26]`'s "Integrated"
  criterion requires baseline training on this to be mandatory before staff
  use AI on organisational/confidential data; `[SE-TOOLSPKG25]`'s
  responsible/ethical domain. Audience fit: strong for the "employees at
  small organisations without an L&D layer" half of the audience
  specifically (this is exactly the training PRIMES says an employer would
  normally mandate, that this audience is least likely to have received) —
  weaker fit for the general-public half, who mostly aren't handling
  organisational data.

- **Inference drawn:** All four are independently attested by at least two
  non-duplicative sources rather than resting on a single framework. None
  requires a technical prerequisite, consistent with the audience decision.
  Candidate A has the broadest direct support across the most independent
  sources (`[SE-TOOLSPKG25]`, `[RS-AILIT25]`, `[FDN26]`, Entry 028) and maps
  most directly onto the project's own problem statement in
  `PROJECT_BRIEF.md` ("appropriate verification and human oversight").
  This is this entry's own reading of the pattern across sources, not a
  conclusion any one source states.
- **Limitations / conflicting evidence:** These four are not mutually
  exclusive — most real frameworks (`[FDN26]`, `[SE-TOOLSPKG25]`) teach some
  version of all of them, just not in one 30–90 minute sitting. Picking one
  is this project's own scoping choice, not something any source instructs.
  See Entry 040 for a direct disconfirm check on Candidate A specifically,
  since it looks strongest on this reading.
- **Effect on project direction:** These are presented as options for the
  project's creator to choose between, not a recommendation. A rough
  tradeoff summary: **A (critical evaluation)** has the strongest/broadest
  evidence as "most urgently needed" and maps closest to the project's
  stated problem, but is arguably the most conceptually demanding of the
  four to teach well in under 90 minutes without also covering some of C
  first (see Entry 040). **B (prompting)** is the easiest to make
  concretely practical and matches what most comparable courses open with,
  but is the weakest fit to the project's specific "responsible/verification"
  framing and the most likely to feel like generic tool-training rather than
  something distinctive. **C (capability/limitation mental model)** is the
  safest prerequisite-free choice and may need to precede A regardless of
  which is chosen as "the" pilot topic (see Entry 040), but risks being
  inert/lecture-like unless deliberately built around an active task. **D
  (responsible/safe use)** best fits the "SME employee without an L&D layer"
  half of the audience specifically and is the most directly tied to
  PRIMES' "Integrated" criterion, but is the weakest fit for the general-
  public half of the audience, who are less often handling organisational
  data day-to-day.

### Entry 040 — Disconfirm/complicate check on Candidate A, plus fresh search for "what's the single best starting point" framing

- **Date logged:** 2026-07-25
- **Priority / Question:** Per this project's confirm/disconfirm discipline
  for foundational claims: does evidence or expert argument exist that
  critical evaluation of AI output (Candidate A in Entry 039) is *not* the
  right capability to teach first, or that something else is more
  foundational and should precede it? Also fulfils the separate instruction
  to search directly for "what's the single best AI-literacy starting
  point" framing, since existing sources mostly answer "what skills matter
  overall," not "what's the best first skill" specifically.
- **Source:** `[TADIMALLA-MAHER25]`, `[SAIL4ALL25]`, re-reading of the
  already-logged `[FDN26]` competency order, and `[SE-FOUNDATIONBENCH26]`.
  Weaker/flagged sources also found and noted for completeness: `[WAGNER26]`
  (opinion blog, argues the opposite conclusion but on weak evidentiary
  grounds) and an unverified vendor-aggregate statistic (`[HALLUC-AWARE26]`).
- **Checked date:** 2026-07-25
- **What the source directly supports:** Several independent sources
  converge on ordering *foundational knowledge of what AI is/does* ahead of
  *critical evaluation of AI output*, rather than treating evaluation as
  the natural entry point:
  - `[TADIMALLA-MAHER25]` (Tadimalla & Maher, "AI literacy as a core
    component of AI education," *AI Magazine* — a peer-reviewed AAAI
    journal, 2025) proposes four curriculum pillars for AI-literacy course
    design: (1) technical foundations, (2) user-focused/interaction
    competencies, (3) sociotechnical considerations, (4) ethical
    perspectives — in that stated order — explicitly noting technical
    understanding "remains fundamental" even as ethical/societal content is
    increasingly integrated alongside it. This journal-published,
    peer-reviewed source directly and explicitly addresses curriculum
    *sequencing*, which is the specific gap this entry checked for.
  - `[SAIL4ALL25]` (peer-reviewed, *Humanities and Social Sciences
    Communications*, validated on three UK adult samples) — an AI-literacy
    *knowledge* assessment scale, not a curriculum, but its four themes are
    ordered "What is AI?" → "What can AI do?" → "How does AI work?" → "How
    should AI be used?" — again placing conceptual/capability knowledge
    ahead of the evaluative/normative "how should it be used" theme that
    critical evaluation belongs to.
  - Re-reading `[FDN26]` (Entry 024): its four competencies are listed in
    the order foundational knowledge → effective interaction → critical
    evaluation → ethical/responsible use — the same ordering pattern,
    independently arrived at.
  - `[SE-FOUNDATIONBENCH26]` (UK Government, Skills England/DSIT — read
    directly this pass): the official "AI foundation skills for work"
    benchmark's first-listed domain is "technical" (writing clear
    instructions for AI tools; using AI tools to support routine tasks),
    with "responsible and ethical" (including judgement/risk-related
    skills) listed third of three. The document itself states no explicit
    priority order or required sequence — this is suggestive from list
    order only, not a stated recommendation, and should be weighted
    accordingly.
- **Inference drawn:** Taken together, this is a real, moderately-supported
  disconfirming pattern (one peer-reviewed source directly on sequencing,
  one peer-reviewed UK-validated instrument whose structure implies the
  same order, one already-logged source with the same ordering, one
  government benchmark whose list order is suggestive but explicitly not a
  stated sequence) — not proof, but enough to complicate treating Candidate
  A as an uncomplicated first choice. A plausible reading (this entry's own
  synthesis, not any source's explicit claim): teaching critical evaluation
  of AI output *without* first giving learners some minimal working model of
  "what AI is doing when it generates this" risks the evaluation skill being
  taught as a checklist ("always double-check") rather than genuine
  judgement grounded in understanding *why* AI output can be wrong — which
  is exactly the "confidence without judgement" risk `[RS-AILIT25]` warns
  against from the opposite direction. This suggests Candidate A and
  Candidate C (foundational capability/limitation mental model, Entry 039)
  may not be a straightforward either/or — a pilot built around A would
  likely need to fold in a compressed version of C as scaffolding, which is
  compatible with a single 30–90 minute unit but is a real design
  constraint, not a reason to discard A.
  Separately, `[WAGNER26]` (a Substack opinion piece, no disclosed
  institutional affiliation) argues the *opposite* of the disconfirming
  pattern above — that critical thinking/judgement, including "the
  conscious decision about when not to use AI," should be positioned as
  AI literacy's *destination*, with tool proficiency treated as
  secondary — but this is asserted rather than evidenced, and is flagged
  as the weakest source in this entry, not a counterweight to the
  peer-reviewed sources above.
- **Limitations / conflicting evidence:** None of the sequencing sources
  found are UK-adult/workforce-specific in the way this project needs.
  `[TADIMALLA-MAHER25]` is framed around computing-education curriculum
  design generally, not specifically a 30–90 minute standalone unit for a
  general-public/SME audience — applying its four-pillar *order* to a
  single short pilot unit (rather than a full course) is this project's own
  extension, not something the paper tested. `[SAIL4ALL25]`'s theme order
  is a measurement-instrument structure, not a curriculum sequencing
  recommendation — treating its ordering as sequencing evidence is an
  inference, clearly weaker than `[TADIMALLA-MAHER25]`'s direct claim.
  `[SE-FOUNDATIONBENCH26]` explicitly does not state a sequence, so its
  list order is the weakest evidence of the four and should not be treated
  as more than suggestive. `[TADIMALLA-MAHER25]` and `[SAIL4ALL25]` were
  both blocked by paywalls/login walls and read only at abstract/summary
  level via search synthesis — not a complete primary read; if either
  becomes load-bearing for the actual capability decision, they should be
  re-checked with a full read first, consistent with this log's existing
  practice for other partially-verified sources (e.g. `[AUTOBIAS-MED25]`).
  No dedicated, UK-specific empirical study comparing learning outcomes
  between an "evaluation-first" and a "foundations-first" short AI-literacy
  unit was found — this remains a genuine evidence gap, not a resolved
  question either way. The direct "what's the single best first AI-literacy
  skill" framing was not found answered head-on by any single authoritative
  source; the sequencing evidence above is the closest available proxy,
  assembled from sources that address curriculum *structure* rather than
  posing "what's the one best starting skill" as their own explicit
  question.
- **Effect on project direction:** Does not disqualify Candidate A, but
  meaningfully complicates treating it as a clean, standalone first choice
  independent of Candidate C. For the creator's decision, this leaves
  (at least) three live options, presented without a recommendation: (1)
  choose Candidate A as designed, accepting the design constraint that a
  compressed capability/limitation primer likely needs to be folded in as
  the unit's "explicit modelling" phase under GRR (`[GRR-EBIP]`) rather
  than assuming learners already have that grounding; (2) choose Candidate
  C (capability/limitation mental model) as the pilot topic in its own
  right, treating critical evaluation as the natural second unit in a
  future stack rather than the first; (3) treat this disconfirming pattern
  as not strong enough to override Candidate A's broader/more direct
  evidence base (Entry 039) given its own limitations (non-UK,
  non-adult-specific, one suggestive-only government source), and proceed
  with A while deliberately designing in a short foundational primer. This
  entry does not resolve which of the three is correct — that judgement
  call belongs to the project's creator.

### Entry 041 — Dedicated search for disconfirming evidence on the SME/large-firm adoption-depth gap (Entry 029)

- **Date logged:** 2026-07-25
- **Priority / Question:** Direct follow-up to the Open Thread flagged after
  Entry 029/030: "No credible disconfirming evidence found yet for the
  SME/large-firm adoption-depth gap... A dedicated search for peer-reviewed
  or ONS/government evidence specifically disputing the size-adoption
  relationship would strengthen (or usefully complicate) this finding."
  Bears on Priority 1 and the audience/thesis decision in `PROJECT_BRIEF.md`.
- **Source:** `[CALDAROLA-CLOUD26]`, `[FRB-MONITORING26]`,
  `[STLFED-ASKMATTERS26]`, `[MDPI-SMEAI-REVIEW26]`, plus `[OECD-SMEAI25]`
  and `[SBA-ADVOCACY25]` as unverified leads. Search was deliberately
  restricted to peer-reviewed, government/central-bank, and
  international-body sources — vendor/marketing content was excluded from
  counting as disconfirmation per this task's brief, even though it kept
  surfacing (e.g. numerous "£78bn opportunity if SMEs caught up"-style UK
  marketing-blog pieces were seen and discarded).
- **Checked date:** 2026-07-25
- **What the source directly supports:**
  - **`[CALDAROLA-CLOUD26]` — the closest thing found to genuine academic
    disconfirmation, but not AI-specific.** Using French firm-level
    administrative data (INSEE), this paper's own abstract states: "Recent
    empirical evidence shows that investments in ICT disproportionately
    improve the performance of larger firms versus smaller ones... We find
    that cloud services positively impact firms' growth rates, with
    **smaller firms experiencing more significant benefits compared to
    larger firms**." A genuine, independently-authored finding that at
    least one modern digital technology category (cloud) produces a
    **small-firm advantage** in growth outcomes — directly contradicting
    the general "digital tech favours large firms" pattern the paper itself
    cites as the norm. It concerns cloud infrastructure broadly, not
    AI/LLM adoption specifically — the most significant limitation.
  - **`[FRB-MONITORING26]`** (US Federal Reserve Board) — a genuine
    measurement-artifact complication, though only a partial one: legacy
    Census Bureau survey data "showed comparable adoption across smaller
    firms (1–249 employees), with higher rates only among the largest
    enterprises (250+)" — historically, most of the size effect was
    concentrated at the very top, not a smooth small-vs-large gradient. It
    also states the Census Bureau's November 2025 revision of the AI survey
    question (from "producing goods or services" to "any of its business
    functions") coincided with growing divergence by firm size, and that
    this "definitional shift likely explains some observed divergence...
    making direct historical comparisons problematic."
  - **`[STLFED-ASKMATTERS26]`** (St. Louis Fed) — cuts the other way on the
    measurement-artifact question: excluding firms with fewer than 10
    employees from adoption calculations (as European surveys do) "does not
    have a major impact" on measured adoption rates, suggesting the
    size-based gap is not primarily a small-firm-exclusion artifact, at
    least for that specific methodological choice.
  - **`[MDPI-SMEAI-REVIEW26]`** (peer-reviewed systematic review of 50
    studies, 2016–2025) — found no SME advantage; reinforces the standard
    narrative (limited financial/human resources, technical skill
    shortages, organisational resistance to change, a distinct SME "data
    scarcity problem"). Logged as a genuine, well-sourced *confirming*
    replication, included for balance rather than as a new disconfirming
    find.
  - A widely-repeated WebSearch-synthesised claim — that "by mid-2025, the
    Federal Reserve found small businesses were adopting AI faster than
    large firms, a reversal that hadn't happened before" — did **not** hold
    up under direct primary-source checking. The Fed sources fetched
    directly describe continued or widening divergence, with one estimate
    that small businesses remain "about a year behind" large-business
    adoption trajectories. A useful example of exactly the verification
    risk this task was checking for.
  - No UK-specific academic or ONS source disputing the size-adoption
    relationship was found despite a dedicated UK-focused search pass.
- **Inference drawn:** Genuine, non-vendor disconfirming/complicating
  evidence for the *AI-specific* SME/large-firm adoption-depth gap remains
  essentially absent — consistent with the prior Open Thread note. The one
  credible academic finding of a small-firm advantage
  (`[CALDAROLA-CLOUD26]`) is in an adjacent domain (cloud infrastructure,
  not AI adoption specifically) and non-UK (France), so it should be read
  as a reason for epistemic humility about assuming digital-tech gaps
  always favour large firms — not as evidence that overturns Entry 029's
  AI-specific finding. The measurement-artifact question is genuinely mixed
  rather than resolved: one Federal Reserve source finds measurement
  changes partly explain a widening gap; another finds a specific
  small-firm-exclusion choice doesn't change much. Neither source claims
  the underlying gap is entirely artifactual.
- **Limitations / conflicting evidence:** All of the most relevant sources
  found are US or cross-European, not UK-specific — a meaningful gap
  against this project's UK evidence-scope preference.
  `[CALDAROLA-CLOUD26]` is a preprint (arXiv), not confirmed
  peer-reviewed/published, and concerns cloud technology rather than AI.
  The OECD and SBA sources could not be directly verified (repeated HTTP
  403s / unreadable PDF binary) and are flagged UNVERIFIED rather than
  cited as confirmed findings. This pass should be read as a genuinely
  thorough but not exhaustive search — a systematic literature search via
  an academic database (rather than web search) was out of scope here and
  might surface UK-specific working papers not indexed by general search.
- **Effect on project direction:** This is itself a valid, useful finding:
  after a real, source-restricted search, no credible independent/academic
  evidence was found that disconfirms Entry 029's core AI-specific
  adoption-depth gap. This should modestly *strengthen* confidence in Entry
  029 as currently framed — not because the gap was re-confirmed by new
  AI-specific evidence, but because a genuine adversarial search came up
  empty on the AI-specific question, while surfacing one adjacent-domain
  academic counter-example (cloud, `[CALDAROLA-CLOUD26]`) worth keeping in
  mind as a caution against overgeneralising "digital tech always favours
  large firms" as a universal law. The measurement-artifact angle is not
  settled and could be revisited if the SME/large-firm gap becomes more
  foundational to the project's thesis — it currently sits at "partially
  complicated, not resolved."

### Entry 042 — Direct verification of the local-AI cost/capability blog aggregate (Entry 030)

- **Date logged:** 2026-07-25
- **Priority / Question:** Direct follow-up to the Open Thread flagged after
  Entry 030: "`[LOCALAI-COST26]` and `[LOCALAI-CAPABILITY26]` are unverified
  aggregate search syntheses... before any local/hybrid cost or capability
  claim appears in an external-facing document, at least 2-3 of the
  underlying individual sources should be fetched and read directly, or a
  UK-specific/independent source... should be found instead." Priority 6.
- **Source:** Individually fetched and read directly: `[PROMPTCOST26]`,
  `[FUNGIES26]`, `[PROMPTQUORUM-COMPARE26]` (cost side); `[MINDSTUDIO26]`
  (capability side) — four of the seven/five named underlying blogs,
  exceeding the requested 2–3. `[EPOCH-ECIGAP26]` and
  `[STANFORD-AIINDEX25]` sought and read as independent/academic
  alternatives. SitePoint was attempted again and again returned HTTP 403;
  a proxy fetch route (`r.jina.ai/<url>`) was used successfully to read
  PromptCost.org and Fungies.io directly after direct HTTP 403s — noted
  here as a technique, since it resolved the exact blocker flagged in the
  prior pass.
- **Checked date:** 2026-07-25
- **What the source directly supports:**
  - **Cost side, directly verified:**
    - `[PROMPTCOST26]` states a 7B-model break-even of "500K–2M tokens/day,"
      with local saving "60–80%" above that threshold — matches Entry 030's
      aggregate figure closely (unsurprising, since Entry 030's aggregate
      was partly built from this same source). Claims "12 months of real
      deployment data" but its actual cited inputs are a mix of real
      external data (hardware prices from Lambda Labs/CoreWeave,
      electricity rates from the US EIA, engineering rates from Glassdoor)
      combined with the author's own cost-model calculations — not a
      published, peer-reviewed, or third-party-audited study.
    - `[FUNGIES26]` uses a different framing (dollar/GPU-based rather than
      token-threshold-based): a solo developer spending ~$80/month on
      Claude API could break even on a local GPU in as little as ~5–15
      months depending on GPU tier. Cites no primary data of its own,
      instead listing other blogs (including SitePoint and PromptQuorum) as
      general references without linking specific figures to specific
      sources. Fungies.io itself is a payments platform for SaaS
      businesses, not an AI or infrastructure company — the article
      functions as promotional content with a sales call-to-action, a step
      further from subject-matter authority than the other sources here.
    - `[PROMPTQUORUM-COMPARE26]` gives current 2026 API rate figures and
      states local LLMs become "cost-effective within weeks for high-volume
      use cases," but — read directly — the article "provides no citations
      or methodology references for benchmark scores, pricing, or
      performance metrics," per its own content. PromptQuorum is itself a
      commercial multi-model comparison tool, so this article also
      functions partly as product marketing.
  - **Capability side, directly verified:**
    - `[MINDSTUDIO26]` states open-weight models are "roughly 3–6 months
      behind frontier on most benchmarks," with the largest gaps in
      reasoning, multimodal, and complex agentic/instruction-following
      tasks, and the smallest gaps in structured extraction, classification
      and straightforward code generation — directionally identical to
      Entry 030's summary. Cites no peer-reviewed benchmarks or specific
      numerical scores, referencing only the LMSYS Chatbot Arena leaderboard
      by name without quoting specific figures. MindStudio is a commercial
      no-code AI workflow platform selling access to both cloud and local
      models.
  - **Independent/academic alternative found and read directly:**
    - `[EPOCH-ECIGAP26]` (Epoch AI, a nonprofit AI-trends research
      organisation with openly published methodology) reports, as of its
      May 2026 measurement (Epoch Capabilities Index, bootstrap-sampled for
      uncertainty): "the most capable open-weight models have lagged
      frontier closed models by **an average of four months**." A
      rigorous, quantified, independently-produced figure that sits at the
      *low end* of Entry 030's originally-cited "3–6 months to 12–18
      months" range — suggesting the upper end of that vendor-blog range
      may be an overstatement, at least by Epoch's measure, though Epoch's
      own caveat is that open labs don't always release their most capable
      models publicly, which could understate the true gap in the other
      direction.
    - `[STANFORD-AIINDEX25]` (Stanford HAI, an independent academic
      institute) reports the open/closed performance gap "reducing... from
      8% to just 1.7%" over a one-year window, alongside a striking
      cost-efficiency trend: "the inference cost for a system performing at
      the level of GPT-3.5 dropped over 280-fold between November 2022 and
      October 2024," with hardware costs declining ~30%/year and energy
      efficiency improving ~40%/year. Note: a separate, not independently
      verified WebSearch snippet suggested this same gap widened again to
      3.3% by a later (2026) edition of the same report — the trend is
      evidently not monotonic, and should not be read as a settled "gap is
      closing" story.
- **Inference drawn:** The directional shape of Entry 030's original claim
  holds up well under direct reading: local/open-weight models do lag
  frontier cloud models by a period best estimated (by the more rigorous
  independent source, Epoch AI) at roughly 3–4 months on general
  capability, with larger gaps concentrated in reasoning/multimodal/agentic
  tasks — consistent with, but more precise than, the vendor-blog
  aggregate. On cost, the general "hybrid is the practical answer, pure
  local isn't uniformly cheaper" framing also holds up, but the specific
  break-even numbers vary meaningfully between the individually-read
  sources themselves (token-threshold framing vs. dollar/GPU-tier framing
  aren't reconciled with each other), which is itself evidence the numbers
  are soft estimates rather than a converged consensus.
- **Limitations / conflicting evidence:** None of the four directly-read
  blog sources cite peer-reviewed, third-party-audited, or even
  fully-linked primary data for their headline figures — direct reading
  confirms rather than resolves the "UNVERIFIED beyond search-engine
  synthesis" concern; it just replaces search-engine-summarised vendor
  claims with directly-read vendor claims, a smaller improvement than
  finding independent verification. Two of the four (Fungies.io,
  PromptQuorum) are commercial products using the article partly as
  marketing for an unrelated or adjacent product, a notable
  interest-conflict not fully visible from the article content alone. No
  UK-specific source (academic or government) was found for either the
  cost or capability side, despite a dedicated search — Epoch AI and
  Stanford HAI are both credible independent/academic sources but are
  US-based and international in scope, not UK-specific. A genuinely
  academic on-device cost/energy paper was also found (arXiv:2512.16531,
  "Scaling Laws for Energy Efficiency of Local LLMs," benchmarking a
  MacBook Pro M2 and Raspberry Pi 5) but was not fetched/read directly in
  this pass due to time — flagged as a lead for a future pass, not logged
  as a finding.
- **Effect on project direction:** The core directional claim in Entry 030
  — that local AI is not a straightforward cost/capability equaliser, that
  break-even depends heavily on usage volume, and that a hybrid approach is
  the practical answer — is now better supported than before, specifically
  by `[EPOCH-ECIGAP26]` and `[STANFORD-AIINDEX25]`, which are genuinely
  independent and more rigorous than the original blog aggregate. The
  `[LOCALAI-CAPABILITY26]` "3–6 months" lag figure can now be anchored to
  Epoch AI's directly-measured "~4 months" rather than left as an
  unverified blog synthesis — this source should be added to, or partially
  replace, `[LOCALAI-CAPABILITY26]` in any external-facing claim.
  `[LOCALAI-COST26]` remains weaker: no independent/academic UK or general
  source was found with comparably rigorous break-even cost figures; the
  cost side of the claim should still be treated as directional-only
  (hybrid is sensible; exact break-even numbers are not reliable) rather
  than citable with specific figures, consistent with Entry 030's original
  hedge.

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

**Resolved this pass (2026-07-24, second pass):**
- ~~Priority 5 (comparable products and programmes) untouched~~ — substantially
  addressed (Entries 020–024): roadmap.sh and LeetCode's progression/
  completion mechanics (Entry 020), Elements of AI as the strongest
  comparable AI-literacy programme found (Entry 021), a direct independent
  critique of the AI Skills Hub naming Elements of AI as the model it should
  have followed (Entry 022, sharpens Entry 018), the Royal Society's
  systematic review of 20 frameworks and 6 international case studies
  (Entry 023 — high value for design lessons, but scoped to children/schools,
  not this project's current adult/workforce audience, so must not be cited
  as adult-population evidence), and a second independently-framed UK
  capability framework converging on a similar shape to Skills England's
  (Entry 024). PRIMES (Entry 012) remains a strong candidate to compare any
  future learning design against, now joined by Elements of AI's structural
  model (short modular chapters, no prerequisites, peer review, vendor-
  neutral) as a second concrete reference point.

**Still open after this pass:**
- Codecademy, Khan Academy, freeCodeCamp and other general (non-AI-specific)
  learning-platform comparables named implicitly by Priority 5's "comparable
  learning systems" framing have not yet been checked — roadmap.sh and
  LeetCode were prioritised as the two platforms RESEARCH_QUESTIONS.md names
  explicitly.
- No comparable found yet that is (a) AI-literacy-specific, (b) UK-based,
  and (c) targeted at general adult/public audiences rather than schools,
  the AI-sector workforce, or a specific employment sector — Elements of AI
  is the closest match but is Finnish in origin. Worth a dedicated check
  before the Priority 2 audience decision is finalised, if a general-public
  audience remains a live candidate.

**Resolved this pass (2026-07-24, Priority 4 pass):**
- ~~Priority 4 (learning design) had only PRIMES-by-name and no detailed
  sequencing/personalisation/misconception evidence~~ — substantially
  addressed (Entries 026–028): PRIMES' full accreditation criteria read
  directly (Entry 026, supersedes the Entry 012 summary), a named
  evidence-based sequencing model (Gradual Release of Responsibility, Entry
  027) matching RESEARCH_QUESTIONS.md's own sequencing question, and a
  confirm/disconfirm pair on whether AI-literacy training actually reduces
  overconfidence/automation bias (Entry 028).

**Still open after this pass:**
- **`[AUTOBIAS-MED25]` (Entry 028) is unverified** — the primary source
  (medRxiv PDF) returned HTTP 403 on fetch; the claim that AI-trained
  physicians still showed automation bias rests only on a search engine's
  own synthesis of the abstract. Needs a direct read (or an alternative
  access route) before being treated as more than a lead.
- Adult-learning-specific pedagogy (andragogy, self-directed learning
  theory) has not been checked against the Gradual Release of Responsibility
  model borrowed from K-12 practice in Entry 027 — flagged there as an
  unexamined transfer assumption.
- PRIMES' criteria are written for *employers* designing *workforce*
  training (Entry 026) — some criteria assume an organisational sponsor
  (paid learning time, workplace systems) that may not apply if Priority 2
  lands on an individual/public audience rather than a workplace one. Not
  yet reconciled.

**Resolved this pass (2026-07-24, benefit-inequality hypothesis test):**
- The user's proposed thesis — that AI benefits accrue disproportionately to
  well-resourced organisations, and that local/hybrid AI could be an
  equalizer — was tested directly against primary evidence (Entries
  029–030). Verdict: the first half is well-supported but sharper than
  originally framed (the real gap is adoption *depth* — generic vs bespoke
  implementation — not simple AI use); the second half is not currently
  safe to assume (local AI's cost/capability advantage is threshold- and
  use-case-dependent, and unverified vendor-sourced figures shouldn't be
  relied on without further checking).

**Still open after this pass:**
- **No credible disconfirming evidence found yet for the SME/large-firm
  adoption-depth gap** (Entry 029) — the search for a "SME advantage"
  counter-narrative surfaced only vendor-interested content-marketing
  claims, not academic or independent evidence. A dedicated search for
  peer-reviewed or ONS/government evidence specifically disputing the
  size-adoption relationship would strengthen (or usefully complicate) this
  finding before it becomes foundational to the project's thesis.
- **`[LOCALAI-COST26]` and `[LOCALAI-CAPABILITY26]` are unverified aggregate
  search syntheses** (Entry 030), not primary sources — before any
  local/hybrid cost or capability claim appears in an external-facing
  document, at least 2-3 of the underlying individual sources should be
  fetched and read directly, or a UK-specific/independent source (e.g.
  academic computing cost-benchmarking) should be found instead.
- The "replace-and-train" finding (Entry 029) — that AI training investment
  is associated with *higher*, not lower, expected headcount reductions —
  has not yet been reconciled with the project's implicit assumption that
  building AI capability benefits the individual learner. This is a
  genuine tension for the project's responsible-use framing, not yet
  addressed.

**Resolved this pass (2026-07-24, "outsourcing understanding" refinement):**
- ~~Half one needed a concrete illustration and a name for the
  implementation-vs-understanding distinction~~ — addressed via Entries
  031–032. Instro AI (suggested by the project's creator) provides a real,
  named UK case study of the integrator role with measured outcomes; a
  buy-vs-build theory paper gives the "outsourcing understanding" concept
  genuine theoretical grounding rather than leaving it as an unsupported
  turn of phrase. The project's differentiation angle has sharpened further:
  not competing with integrators on implementation, but building the
  capability layer above them.

**Still open after this pass:**
- **Half two (local/hybrid AI cost/capability claims) remains unverified** —
  a follow-up attempt to fetch a primary source (SitePoint) was blocked
  (HTTP 403). Still needs 2–3 directly-read sources, or a non-blog
  independent/academic source, before use in any external-facing document.
- **No disconfirming search run yet on the "outsourcing understanding"
  claim** (Entry 032) — e.g. cases where vendor engagements *do* transfer
  capability through staged handover, co-development or embedded training
  models, which would complicate a blanket framing.
- **Instro-specific claims rest on one trade-press article and Instro's own
  homepage** (Entry 031) — the underlying AMRC Cymru trial report has not
  been read directly, and results come from a funded innovation trial, not
  necessarily representative of a typical paid engagement.

**Resolved this pass (2026-07-24, correction and half-two refinement):**
- ~~"Outsourcing understanding" needed testing~~ — retracted per direct
  creator instruction (Entry 033), not carried forward. Instro AI's case
  study value (Entry 031) is preserved but scoped strictly to "example of
  successful integration," per the creator's explicit direction.
- ~~Half two needed a realistic, better-evidenced reframing~~ — done (Entry
  034): local AI dropped as a standalone SME/individual solution; the
  evidenced mechanism is now task/workflow specialisation and model
  cascading/routing (strong academic backing, Chen & Varoquaux 2026),
  illustrated via Claude Code's own subagent/skills architecture as a
  worked example for Priority 4.

**Still open after this pass:**
- The Claude-Code-as-illustrative-example connection (Entry 034) is this
  project's own inference, not sourced from the academic literature — worth
  a lighter validation pass later (e.g. checking whether Anthropic's own
  published material frames Claude Code's subagent design in these terms)
  before treating it as more than a useful teaching analogy.

**Resolved this pass (2026-07-24, Priority 2 working decision):**
- ~~Primary audience undecided~~ — the project's creator made an explicit,
  provisional working decision: individuals seeking practical everyday AI
  literacy generally, with particular attention to employees at small
  organisations lacking employer-provided L&D infrastructure. Recorded in
  PROJECT_BRIEF.md ("Primary audience (working decision — 24 July 2026)"),
  drawing on Entries 012, 019, 021, plus the AI Skills Hub/PRIMES
  employer-assumption gap surfaced in Entries 022/025/026. Explicitly marked
  as subject to change, not a closed question — the PRIMES-assumes-an-employer
  reconciliation point immediately above is now the sharpest open sub-question
  under this working decision, since PRIMES' criteria (Entry 026) may need
  adaptation, not wholesale adoption, for an individual/small-org audience
  without a sponsoring employer.
- Priority 2's other sub-questions from RESEARCH_QUESTIONS.md (specific
  barriers/needs for this *combined* audience, whether "small organisation
  employees" should later be split into narrower sub-groups) remain open and
  are not resolved by this decision alone.

**Resolved this pass (2026-07-24, immediate priority Q5 / first-output decision):**
- ~~What should the project build first?~~ — the creator decided (`PROJECT_LOG.md` Entry 001,
  recorded in `PROJECT_BRIEF.md`): a single pilot learning unit, PRIMES-sized
  and GRR-sequenced, tested with real learners before any wider structure is
  built. Chosen over drafting a full skeleton pathway or deferring the
  decision pending more Priority 7 research.

**Still open after this pass:**
- **Which single core capability the pilot unit should teach** — the
  immediate next decision point, not yet addressed.
- Priority 7's other sub-questions (accessibility requirements, install-free
  access, how Word/web/GitHub outputs should relate) remain unaddressed —
  deliberately deferred rather than researched ahead of need, since only the
  pilot unit's shape was needed to unblock the next build step.
- Priorities 8 (information architecture), 9 (evaluation — e.g. how the pilot
  will actually be tested/assessed with real learners), and 10
  (sustainability/public presentation) remain essentially untouched.

**Resolved this pass (2026-07-24, visual identity):**
- ~~Visual identity beyond the project name~~ — a palette, logo type
  (icon + wordmark) and tone are now decided (`PROJECT_LOG.md` Entry 003,
  `PROJECT_BRIEF.md` "Visual identity").

**Still open after this pass:**
- The legacy PAWH icon set (`assets/brand/legacy-pawh-icons/`) is confirmed
  to need a recolour/overhaul pass against the new palette — unscheduled.

**Resolved this pass (2026-07-24, symbol candidate):**
- ~~No logo mark existed~~ — a symbol-only working candidate is now locked
  (`PROJECT_LOG.md` Entry 004), though explicitly provisional and pending further path-level
  refinement.

**Still open after this pass:**
- Further symbol concepts, beyond the locked candidate, still to be
  explored.
- Wordmark design is unresolved — the tested wordmark didn't pair well with
  the symbol; needs a different approach (typeface, layout, or possibly
  abbreviation) before a full logo lockup exists.
- The locked candidate itself is expected to change (creator intends to
  edit its SVG paths directly) — treat as a snapshot, not a stable
  reference, until re-confirmed.

**Resolved this pass (2026-07-24, workflow correction):** Two rounds of
fine curve-level refinement were attempted via iterative AI-described
feedback (annotated screenshot → prose correction). The creator found this
arduous, echoing a discouraging pattern from PAWH, and has moved to editing
directly in Inkscape (see `PROJECT_BRIEF.md`, "Visual identity" workflow
note). Further AI-iterative curve editing is not the plan going forward.

**Resolved this pass (2026-07-24, Inkscape output):** The handoff produced
two improved candidates (`PROJECT_LOG.md` Entry 005) — `GAP_logo_flat.svg` and
`GAP_logo_shaded.svg` (creator's preferred version) — superseding the
earlier AI-edited file, which has been removed. The "more 3D/book effect"
feedback from `PROJECT_LOG.md` Entry 004's blue arrows is now addressed via gradient shading
rather than curve tweaks.

**Still open after this pass:**
- The wordmark pairing is unretested against the new candidates.

**Resolved this pass (2026-07-24, legacy icon set):**
- ~~The legacy PAWH icon set needs its recolour/overhaul pass~~ — done
  (`PROJECT_LOG.md` Entry 006). Recoloured, verified, manually checked by the creator, and
  four structural issues fixed.

**Resolved this pass (2026-07-24, promotion to working assets):**
- ~~`B04-D_API_MCP.svg` needs its "API" type hand-set~~ — done by the
  creator in Inkscape's text tool.
- ~~Logo symbol and icon set are candidates/legacy, not working assets~~ —
  both promoted (`PROJECT_LOG.md` Entry 007): flat snake_case file structure, PNG
  derivatives generated, folder/status references updated throughout.

**Resolved this pass (2026-07-24, wordmark finalised):**
- ~~The wordmark pairing is the one remaining unresolved piece of the
  visual identity~~ — done (`PROJECT_LOG.md` Entry 008). Two-line arrangement, Public Sans
  recommended, full monochrome/horizontal/vertical/reversed variant set
  produced.

**Resolved (2026-07-24, visual identity closed out — `PROJECT_LOG.md` Entry 011):**
- ~~Inkscape-side typographic polish (real font, kerning, path-conversion)~~
  — done. All wordmark text is now real vector paths in Public Sans.
- The visual identity thread has no further open items. Not carrying a
  "still open" bullet forward for it.

**Resolved (2026-07-24, addendum to `PROJECT_LOG.md` Entry 007):** `api_and_mcp.svg`'s
hand-set "API" type has been converted to a vector path by the creator
(Inkscape's Path > Object to Path) — no font dependency remains, matching
every other icon in the set. Its PNG derivatives (64/128/256px) were
regenerated to match. This was the last loose end from the icon
promotion.

**Resolved this pass (2026-07-24, second track confirmed):**
- ~~Whether shell/terminal basics belongs in the first pilot~~ — resolved
  (`PROJECT_LOG.md` Entry 002): it doesn't belong in the general-literacy pilot, but is a
  sensible first module for a newly-confirmed **second, parallel track**
  (the local AI workstation), seeded from inherited PAWH architecture now
  recorded in `PROJECT_BRIEF.md`.

**Still open after this pass:**
- The two tracks' relationship (shared foundational modules, if any;
  whether the workstation track needs its own audience/barrier research
  the way Priority 2 was done for the general-literacy pilot) is
  unaddressed.
- The inherited workstation architecture (`PROJECT_LOG.md` Entry 002) has not been checked
  against current tool landscape/versions — it reflects PAWH-era planning,
  not a freshly-verified technical review.

**Deferred (2026-07-24):** The creator confirmed the local AI workstation
track (`PROJECT_LOG.md` Entry 002) is not active work for now — parked as a confirmed future
direction, not dropped. Current focus stays on the general-literacy pilot's
core-capability decision (`PROJECT_LOG.md` Entry 001). Do not resume workstation-track
drafting until the creator reopens it.

**Resolved this pass (2026-07-25, core-capability options researched):**
- ~~Which single core capability the pilot unit should teach~~ — options now
  researched (Entries 039–040), not yet decided. Four evidenced candidates
  identified (critical evaluation of AI output; effective prompting;
  capability/limitation mental model; responsible/safe use of data), with a
  disconfirm check complicating the apparent front-runner (critical
  evaluation) by finding several independent sources that order foundational
  "what AI is/does" content ahead of evaluative content. This is genuinely
  "resolved" only in the sense that the open question now has a well-sourced
  set of options in front of it — the actual choice remains the creator's,
  not made by this entry.

**Resolved (2026-07-26, core-capability decided — `PROJECT_LOG.md` Entry 013):**
- ~~The core-capability choice itself~~ — decided. The creator chose
  Candidate B (effective prompting), specifically framed around the gap
  between what a learner types and what the model does with it — resolving
  Entry 040's scaffolding concern by building a compressed version of
  Candidate C into the prompting lesson itself rather than treating it as a
  separate prerequisite. Working title: "Effective prompting — what's really
  happening when you hit send." Unblocks drafting the pilot unit.

**Still open after this pass:**
- `[TADIMALLA-MAHER25]` and `[SAIL4ALL25]` (Entry 040) were only read at
  abstract/summary level (paywalled) — need a full read before being treated
  as more than suggestive, especially if the sequencing question becomes
  load-bearing for the final decision.
- No UK-specific empirical comparison of "evaluation-first" vs.
  "foundations-first" short AI-literacy units was found (Entry 040) — a
  genuine evidence gap, not just an unread source.

**Resolved this pass (2026-07-25, verification debt on Entries 029/030):**
- ~~No disconfirming search run yet on the SME/large-firm adoption-depth
  gap~~ — done (Entry 041). A genuinely restricted, non-vendor search still
  found no AI-specific disconfirmation; one adjacent-domain academic
  counter-example (cloud technology, not AI) was found and logged for
  epistemic humility rather than as an overturn. Net effect: modestly
  strengthens Entry 029.
- ~~`[LOCALAI-COST26]`/`[LOCALAI-CAPABILITY26]` unverified beyond
  search-engine synthesis~~ — substantially addressed (Entry 042). Four
  underlying blogs were individually fetched and read directly (confirming
  but not resolving the "vendor claim, no primary data" concern), and two
  independent/academic alternatives were found: Epoch AI's Capabilities
  Index (rigorous, ~4-month open/closed gap — can now anchor
  `[LOCALAI-CAPABILITY26]`'s figure) and Stanford HAI's AI Index
  (corroborates directionally, non-monotonic). The cost side remains
  genuinely unverifiable beyond vendor estimates — no independent
  alternative was found there.

**Still open after this pass:**
- The measurement-artifact question for the SME/large-firm gap (Entry 041)
  is genuinely mixed, not resolved — one Fed source suggests a definitional
  survey change partly explains a widening gap, another finds a specific
  small-firm-exclusion choice doesn't change much. Worth revisiting only if
  this gap becomes more foundational to the project's thesis.
- The local-AI cost side (Entry 042) still has no independent/academic or
  UK-specific source — remains directional-only, not citable with specific
  figures.
- A genuinely academic on-device cost/energy paper (arXiv:2512.16531) was
  found but not read directly in this pass — flagged as a lead, not a
  finding.

**Resolved (2026-07-27, icon/logo consistency pass — `PROJECT_LOG.md` Entry 014):**
- ~~Icons read as inconsistent sizes despite identical export dimensions~~
  — root cause found (varying fill-ratio, 0.48–0.90 across the set) and
  fixed via normalisation to a 0.70 target across all 36 icons.
- ~~Some icon/logo backing fills use Paper/Ink where pure white/black was
  intended~~ — audited and corrected across icons and the non-reversed
  logo files; `logo_symbol_reversed.svg`'s Ink page-fill confirmed as a
  separate, genuinely intentional choice, not an instance of this bug.
- ~~Profile pictures didn't reflect the creator's preferred border/background
  treatment~~ — redesigned (Ink background, edge-flush Paper ring, reversed
  symbol with a narrow spine-shadow depth treatment), approved by the
  creator.
- ~~Icon/logo SVG groups were unlabelled, making them harder to edit by
  hand~~ — snake_case labels added to all 34 icon files with unlabelled
  groups (`hybrid_ai.svg` and the already-adequately-labelled logo files
  excluded).

**Still open after this pass:**
- Stroke-width normalisation only covered five specific creator-approved
  fixes — the full set of icons mixing multiple stroke weights was reviewed
  but left as intentional hierarchy, not a closed/completed audit of every
  possible outlier.
- `hybrid_ai.svg` has no labelled groups (it currently has none at all,
  having been hand-edited outside this pass) — revisit if/when it gains
  group structure worth labelling.
