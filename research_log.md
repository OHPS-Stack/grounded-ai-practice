# Grounded AI Practice — Research Log

## Document status

Research-stage working document. This log is maintained as an ongoing record of
findings, not a final report. It follows the recording discipline set out in
research_questions.md ("Research discipline" section).

## Purpose

Every entry below corresponds to a specific research question from
research_questions.md and records what was actually found, distinguishing
source-supported fact from inference, and noting any effect on project
direction.

Scoping/creative decisions, design/production work and technical build
notes — anything durable that isn't source-backed research evidence — go in
`project_log.md` instead, not here. This file drifted into a mixed dump of
both for a while (see `project_log.md` Entry 017); the split below restores
the boundary.

This log is intended to be maintained by Claude during research passes, not
edited by hand. New entries are appended as findings are checked; existing
entries are not silently altered — corrections or supersessions are added as
new entries that reference the one they update, so history stays traceable
(consistent with research_questions.md's requirement that superseded
information remain traceable).

## How to read this log

Each entry contains:

| Field | Meaning |
|---|---|
| ID | Sequential entry number |
| Date logged | When the entry was added to this log |
| Priority / Question | Which numbered research priority and question (from research_questions.md) this entry addresses |
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
| `[OECD-SMEAI25]` | Government/Official (international body) — PRIMARY, read directly | OECD, "AI adoption by small and medium-sized enterprises," discussion paper for the G7, Dec 2025. Read directly 2026-08-05, pp. 1–12 (adoption trends and gaps) — see Entry 065; earlier PDF fetch failures resolved by downloading the file itself. 40% large (250+) / 20.4% medium (50–249) / 11.9% small (10–49 employees) firms using AI, 2024 or latest available year per country (UK: 2020); enterprises with 10+ employees; unweighted average. Underlying data: OECD ICT Access and Usage by Businesses database. Not UK-specific. oecd.org |
| `[STARMER-RESIGN26]` | Independent/Media (multiple outlets, single public fact) | NPR, CNN, Al Jazeera, CBS News, 22 Jun 2026: Keir Starmer resigns as Prime Minister; a Labour leadership contest follows, with Andy Burnham reported as the likely successor. Used for one dated fact on the landing-site chart. npr.org / edition.cnn.com / aljazeera.com / cbsnews.com |
| `[MDPI-SMEAI-REVIEW26]` | Independent/Academic (peer-reviewed, open access) | "Artificial Intelligence in SMEs: Enhancing Business Functions Through Technologies and Applications," Information (MDPI), 16(5):415, systematic review of 50 studies 2016–2025 — read via proxy fetch. mdpi.com/2078-2489/16/5/415 |
| `[EPOCH-ECIGAP26]` | Independent/Academic-adjacent (nonprofit AI-trends research organisation; methodology openly published, Creative Commons licensed) | Epoch AI, "Open models lag state-of-the-art closed models by 4 months," Epoch Capabilities Index data insight, May 2026 — PRIMARY, read directly. epoch.ai/data-insights/open-closed-eci-gap |
| `[STANFORD-AIINDEX25]` | Independent/Academic | Stanford Institute for Human-Centered AI (HAI), *The 2025 AI Index Report*, "AI becomes more efficient, affordable and accessible" section — PRIMARY, read directly (partial — the specific section quoted, not the full report). hai.stanford.edu/ai-index/2025-ai-index-report |
| `[PROMPTCOST26]` | Vendor/Commercial — individually verified (was previously only part of the unverified `[LOCALAI-COST26]` aggregate) | PromptCost.org, "Local LLM Total Cost of Ownership 2026: Cloud vs Self-Hosted" — read directly via proxy fetch after direct fetch returned HTTP 403. promptcost.org/en/blog/local-llms-total-cost-ownership-2026/ |
| `[FUNGIES26]` | Vendor/Commercial (a payments/"merchant of record" platform for SaaS, publishing this as promotional content — not an AI or infrastructure company) — individually verified (was previously only part of `[LOCALAI-COST26]`) | Fungies.io, "Local LLM vs Cloud API: The Complete 2026 Cost Breakdown & Break-Even Guide" — read directly via proxy fetch after direct fetch returned HTTP 403. fungies.io/local-llm-vs-cloud-cost-2026/ |
| `[PROMPTQUORUM-COMPARE26]` | Vendor/Commercial (the article promotes PromptQuorum's own multi-model comparison product) — individually verified (was previously only part of `[LOCALAI-COST26]`/`[LOCALAI-CAPABILITY26]`) | PromptQuorum, "Local LLMs vs Cloud APIs 2026: Privacy, Cost, and Quality" — PRIMARY, read directly (fetched without needing a proxy). promptquorum.com/local-llms/local-llms-vs-cloud-apis |
| `[MINDSTUDIO26]` | Vendor/Commercial (MindStudio is a no-code AI workflow platform selling access to 200+ cloud and local models) — individually verified (was previously only part of `[LOCALAI-CAPABILITY26]`) | MindStudio, "Local AI vs Cloud AI in 2026: When to Run Models on Your Own Hardware" — PRIMARY, read directly (fetched without needing a proxy). mindstudio.ai/blog/local-ai-vs-cloud-ai-2026 |
| `[IUK-WP2-26]` | Government/Official (Innovate UK / UKRI, delivered under the BridgeAI programme) — note the delivery-partner interest below | Innovate UK, *Unlocking UK Economic Growth through Artificial Intelligence: case studies and guidance for employers* (second White Paper of the AI Skills Hub programme), February 2026, 54pp — PRIMARY, full PDF downloaded and read directly. Authorship credit on the cover page is "calyo". Its own quantitative benchmarking is stated (Annex A) to be "mainly drawn from" PwC datasets — and PwC was separately commissioned to build the AI Skills Hub the paper promotes, so the paper is not independent of the product it evaluates. iuk-business-connect.org.uk |
| `[IUK-BRIDGEAI-YR3]` | Government/Official (Digital Catapult, a BridgeAI consortium delivery partner, writing for Innovate UK) — self-reported programme delivery data, not independent evaluation | *Bridging the AI divide — Innovate UK BridgeAI: Year three in review, 2025–2026*, produced by Digital Catapult for Innovate UK, March 2026, 81pp — PRIMARY, full PDF downloaded and read directly. Ministerial foreword by Kanishka Narayan MP, Parliamentary Under-Secretary of State, Minister for AI and Online Safety. iuk-business-connect.org.uk |
| `[PAC-AIGOV25]` | Government/Official (parliamentary select committee — independent scrutiny of the executive; the strongest source-independence in this log to date) | Committee of Public Accounts, *Use of AI in Government*, Eighteenth Report of Session 2024–25, HC 356, March 2025, 29pp — PRIMARY, full PDF downloaded and read directly. Scope is the public sector's own internal adoption of AI, **not** BridgeAI or the AI Skills Hub. committees.parliament.uk |
| `[PUBLICFIRST-MSFT]` | Vendor/Commercial (consultancy research commissioned by a technology vendor) | Public First, *Unlocking the UK's AI Potential: Harnessing AI for Economic Growth*, commissioned by Microsoft — read directly. Microsoft's own £2.5bn UK investment commitment is stated on the report page. Headline there is £550bn by 2035; the £400bn-by-2030 figure is the related number cited by Innovate UK and the AI Opportunities Action Plan. microsoftuk.publicfirst.co.uk |
| `[AISKILLSHUB]` (status update 2026-07-28) | Government/Official — **still not directly readable** | Unauthenticated fetch of aiskillshub.org.uk now returns HTTP 403 (previously HTTP 402 at Entry 018). Two independent failure modes across two passes; treat unauthenticated fetching as a closed route. The project's creator holds an active Hub account — first-hand platform evidence should be collected through that logged-in session rather than by further fetch attempts. |
| `[NIST-1270]` | Government/Official (US National Institute of Standards and Technology) — **not UK**, and voluntary guidance rather than regulation | Schwartz, Vassilev, Greene, Perine, Burt & Hall, *Towards a Standard for Identifying and Managing Bias in Artificial Intelligence*, NIST Special Publication 1270, March 2022, 86pp — PRIMARY, read directly (Executive Summary, §2.1–2.3, §3.3 Human Factors, and the Glossary read in full; §3.1 datasets and §3.2 TEVV not read, being computational rather than human-factors material). doi.org/10.6028/NIST.SP.1270 |
| `[AIOPP-PLAN25]` | Government/Official — but note the status: an **independent report to government**, written in the first person by Matt Clifford, an appointed adviser, not a departmental policy statement | HM Government, *AI Opportunities Action Plan*, 13 January 2025, Command Paper CP1241, ISBN 978-1-5286-5362-6 — PRIMARY, full text read directly via the gov.uk content API. Makes 50 recommendations. gov.uk |
| `[AIOPP-1YEAR26]` | Government/Official (DSIT reporting its own progress against its own plan — self-assessment, not evaluation) | HM Government, *AI Opportunities Action Plan: One Year On*, 29 January 2026 — PRIMARY, full text read directly. Forewords by the Prime Minister and by Liz Kendall MP as Secretary of State for DSIT. gov.uk |
| `[AISKILLSBOOST26]` | Government/Official (DSIT, publishing figures supplied to it by eleven commercial delivery partners) | DSIT, *AI Skills Boost: explainer*, 28 January 2026 — PRIMARY, read directly. Source of the 1,001,147 course-completion figure, of the definition of what that figure counts, and of DSIT's own hedged economic modelling. gov.uk |
| `[AILMS25]` | Government/Official (DSIT-commissioned, delivered by Gardiner & Theobald, a consultancy). The report itself states its findings "do not represent Government views or policy and are instead G&T views" | DSIT / Gardiner & Theobald, *AI Labour Market Survey 2025* — PRIMARY, full PDF obtained and sections 1–3 (executive summary, methodology, respondent overview) read directly. n=119 self-selected organisations, 3% response rate, scoped to the AI sector. See Entry 056. gov.uk |
| `[AIOPP-RESP25]` | Government/Official (the government's formal reply to its own commissioned adviser — a statement of policy intent, unlike `[AIOPP-PLAN25]` which is not) | HM Government, *AI Opportunities Action Plan: government response*, 13 January 2025, Command Paper CP 1242, ISBN 978-1-5286-5363-3 — PRIMARY, read directly. Answers each of the 50 recommendations individually with a verdict and a target date. gov.uk |
| `[AISKILLSLIFE-RER26]` | Independent/Academic, government-supported (authored by Prof Rob Procter, Warwick University and the Alan Turing Institute; supported by DSIT and the DCMS R&D Science and Analysis Programme) — a materially better interest position than the vendor and consultancy sources elsewhere in this log | DSIT/DCMS, *AI Skills for Life and Work: Rapid Evidence Review*, published 28 January 2026 — PRIMARY, obtained in full and read at section level rather than end to end. gov.uk |
| `[FEWEEK-HUB26]` | Independent (education-sector trade journalism; no commercial stake in AI training provision — a materially better source position than the vendor reviewers in Entries 022/025) | FE Week, "AI Skills Hub risks 'copy and paste of past failure'", 30 January 2026, by Anviksha Patel — article retrieved and its content extracted directly, superseding the earlier fetch-summary read. Carries quotes from Skills England chair Phil Smith and from Sue Pember of HOLEX, and the three-minute completion detail. feweek.co.uk |
| `[SKILLSTOOLKIT-OSR21]` | Independent/Official (the UK statistics regulator) | Office for Statistics Regulation, *Mary Gregory to Neil McIvor: Use of unpublished data during Parliamentary Questions*, 8 March 2021 — PRIMARY, **now read directly** via OSR's published correspondence archive, superseding the "not retrieved" status this row previously carried. Full letter text read salutation to sign-off; the PDF attachment was not opened separately. Concerns two uses of unpublished Skills Toolkit data in answers to Parliamentary Questions, and two requested presentational improvements. See Entry 059 for what it does **not** say. osr.statisticsauthority.gov.uk |
| `[FEWEEK-TOOLKIT21]` | Independent (education-sector trade journalism) | FE Week's Skills Toolkit reporting: "Registrations for DfE's £1m 'skills toolkit' could be from all around the globe", 29 January 2021; "DfE knuckles rapped by stats watchdog over Skills Toolkit data", 22 March 2021; "DfE admits official Skills Toolkit completion data may just be starts", 25 March 2021. **Headlines and search-result summaries only — none of the three read in full.** This is the actual source of the web-hits, geography and starts-not-completions findings that Entry 055 wrongly attributed to the regulator. feweek.co.uk |
| `[SKILLSENGLAND-GOV]` | Government/Official (the body's own listing) | Skills England organisation page, gov.uk, with establishment and machinery-of-government dates corroborated by the House of Commons Library briefing *Skills policy in England* (CBP-10365). Executive agency; created in shadow form 22 July 2024 under DfE; fully established 2 June 2025; skills brief moved to DWP 7 September 2025. Used for a descriptive gloss only. gov.uk |
| `[INNOVATEUK-GOV]` | Government/Official (the body's own listing) | Innovate UK organisation page, gov.uk — "the UK's innovation agency", part of UK Research and Innovation. Used for a descriptive gloss only. gov.uk |
| `[DIGICAT-ABOUT]` | Vendor/Commercial-adjacent (the organisation's own self-description; part of the Innovate UK Catapult Network, so not independent of the body it reports to) | Digital Catapult, About us — describes itself as a deep tech innovation organisation and as part of the Innovate UK Catapult Network. Used for a descriptive gloss, and for the observation in the report's §8 that the BridgeAI delivery figures are reported to a funder whose own network the reporter belongs to. digicatapult.org.uk |
| `[OSR-ABOUT]` | Independent/Official (the regulator describing its own remit) | Office for Statistics Regulation, *What we do*, and its *Official Statistics in Development* policy page. Source of the OSR's self-description as "the regulatory arm of the UK Statistics Authority", and of the September 2023 renaming of "experimental statistics" to "official statistics in development". osr.statisticsauthority.gov.uk |
| `[AIOPP-DELIVERY26]` | Government/Official — **self-assessment**, the strongest caveat in this table. DSIT and Number 10 Data Science scoring their own department's delivery against their own plan, with no stated criterion for what "Commitment Met" requires and no external verification | *AI Opportunities Action Plan — 2026 Progress*, delivery.ai.gov.uk, January 2026 — PRIMARY, read directly. A page per recommendation carrying the CP 1242 response and a 2026 progress update; all 50 are served from `/data/ai-opportunities.json`, which is how they were read. Headline: 38 of 50 met (76%), 12 in progress. **Blocks ordinary fetching (403 site-wide); reachable through a browser.** See Entries 060 and 061. |
| `[AISKILLS-JUN25]` | Government/Official (DSIT announcing its own partnership) | DSIT, "Tech giants join government to kick off plans to boost British worker AI skills", 14 June 2025 — PRIMARY, read via fetch extraction rather than raw text. Source of the original **7.5 million workers by 2030** target, the eleven named partners, and the separate projection that "around 10 million workers" would be *using* AI by **2035**. gov.uk |
| `[PMLTW25]` | Government/Official (the Prime Minister's published remarks) | Prime Minister's remarks at London Tech Week, 9 June 2025, Olympia — PRIMARY. The page is headed "Transcript of the speech, exactly as it was delivered" and runs roughly 3,100 words. **Read only via scoped extractions, never end to end** (a full reproduction was declined on copyright grounds), and the first pass missed a claim in plain text — treat every extraction from it as a search, not a read, until a human has read the page. Source of "7.5 million workers", "£185 million", and "50 recommendations, all of them accepted by the government". gov.uk |
| `[AISKILLSBOOST-EXPAND26]` | Government/Official (DSIT announcing its own programme's expansion) | DSIT, "Free AI training for all as government and industry programme expands to provide 10 million workers with key AI skills by 2030", 28 January 2026 — PRIMARY, comprehensive extraction, not read end to end. Source of universal adult eligibility, the 27-partner list, the 2-million-SME-employee target, the AI foundations badge, and the absence of any stated measurement framework. gov.uk |
| `[AIPLAYBOOK25]` | Government/Official (GDS, Cabinet Office) | *Artificial Intelligence Playbook for the UK Government*, published 10 February 2025, superseding the Generative AI Framework for HMG (January 2024) — PRIMARY, comprehensive extraction, **not read end to end**; a human read is required before characterising it in print. Written for civil servants and public sector organisations, not the public. Ten principles; states "We didn't pretend to have all of the answers". gov.uk |
| `[IAI-GOV]` | Government/Official (Cabinet Office delivery unit) | Incubator for AI (i.AI), ai.gov.uk — PRIMARY, read in the browser after WebFetch returned 403. A product-building unit, not a public resource: Extract, Consult, Lex, Minute, Medguard, Caddy, AI Classroom Tutors, Sovereign Benchmark. Careers at /opportunities. Contact via cabinetoffice.gov.uk. |
| `[AIKNOWLEDGEHUB]` | Government/Official (i.AI, Cabinet Office) | AI Knowledge Hub, ai.gov.uk/knowledge-hub — PRIMARY, read in the browser. Task-oriented resource for public-sector teams ("Find tools. Explore approaches. Improve delivery."), populated by the public sector community. The artefact government cites as delivering Action Plan Recommendation 45. |
| `[PMLTW25-VIDEO]` | Government/Official content via Broadcast/Commercial host (Sky News upload of the speech) | Sky News, "Starmer says artificial intelligence 'makes us more human' — London Tech Week speech", YouTube `KB4DzJhHZU8`, 45m24s — **NOT read.** The only caption track is auto-generated (ASR); YouTube returns HTTP 200 with an empty body to every programmatic caption request, signed out, across all formats. Auto-captions would in any case be an unsafe basis for quoting a head of government, since ASR mis-renders exactly the numbers this project cites. Any use requires the timestamped-verification protocol in `CLAUDE.md`. |
| `[TECHFIRST25]` | Government/Official (No.10/DSIT press release) | "PM launches national skills drive to unlock opportunities for young people in tech", 8 June 2025 — PRIMARY, read via targeted extraction. States "£187 million" for TechFirst and "7.5 million UK workers to gain essential AI skills by 2030 through industry partnership". gov.uk |
| `[OPENBADGES]` | Independent/Reference (an open technical standard) | Mozilla Open Badges, published 15 September 2011 with MacArthur Foundation funding; version 1.0 in 2012; stewardship passed to IMS Global, now 1EdTech, in 2017. Used here only to date the technology, not as evidence about its effectiveness. |

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
  capability gap described in project_brief.md doesn't exist. They establish
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
  because research_questions.md names them specifically as design-pattern
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
  project's current problem statement centres on (project_brief.md). Its
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
  (see `project_brief.md`, "Longer-term direction and positioning").

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
  (see `project_brief.md`, "Longer-term direction and positioning"): the "directory not programme"
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

- **Inference drawn:** research_questions.md's own Priority 4 phrasing
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
  in project_brief.md's "Primary audience" section.

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
  straightforwardly feel-good thesis, and project_brief.md's responsible-use
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
  cheaper and more capable). This actually validates project_brief.md's
  existing "local, cloud and hybrid" framing (plural, comparative) over a
  "local AI is the answer" framing — the project's original instinct to
  treat this as a *comparison to teach*, not a solution to prescribe, is
  better supported by this pass than a stronger local-AI-equalizer claim
  would have been. Before this technical claim is used in any external-facing
  document (cf. the government-recognition aim in
  `project_brief.md`, "Longer-term direction and positioning"), it needs primary-source
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
  `project_brief.md` ("appropriate verification and human oversight").
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
  Bears on Priority 1 and the audience/thesis decision in `project_brief.md`.

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

### Entry 043 — Innovate UK's second White Paper: the government's own guidance contradicts its own platform

- **Date logged:** 2026-07-28

- **Priority / Question:** Priority 1 (evidence/problem framing) and
  Priority 5 (comparables) — first direct read of a primary
  government-programme document behind the AI Skills Hub, supplied by the
  project's creator as a key source.

- **Source:** `[IUK-WP2-26]`

- **Checked date:** 2026-07-28

- **What the source directly supports:**

  - **The headline economic figure, and its actual provenance.** "The AI
    Opportunities Action Plan and Public First's research identifies that
    AI adoption could boost the UK economy by up to £400 billion by 2030
    (Public First, 2024)." This is the figure the project has seen cited
    as government-backed; the White Paper attributes it to Public First,
    a consultancy, not to an official statistical body.

  - **The Hub's own description of itself.** UKRI established the AI
    Skills Hub in June 2025 as "the UK's first-of-its-kind,
    government-funded, free at point-of-use, digital platform," funded by
    Innovate UK under BridgeAI, supported by DSIT. **"PwC was
    commissioned, following a robust competitive tender process, to
    design, build, and run the Hub."** The Hub is described as providing
    "sector-specific, role-based and skill-level-tailored learning
    pathways, all curated by experts."

  - **Skills-gap figures.** 96% of employers across four sectors reported
    a persistent mismatch between AI skills required and available (UKRI's
    own first White Paper, June 2025); nearly half of UK CEOs view skills
    shortages as the single biggest barrier to AI adoption (PwC, 2025a);
    15% of the UK workforce use GenAI daily (PwC, 2025c); only 18% of
    workers felt AI skill levels were adequate — sourced to The Alan
    Turing Institute & UK AI Council, **2021**.

  - **Its own five-step adoption guidance**, whose fifth step
    ("Upskill the workforce") tells employers to "**use diagnostics** and
    workforce planning tools to map required capabilities" and to
    "**design targeted, role-specific learning pathways** — create
    differentiated learning journeys for leaders, operational teams,
    technical specialists, and frontline workers."

  - **Its own focus-group data:** skills gaps are the No. 1 reported
    barrier when implementing AI (AI Skills Hub focus groups, November
    2025, 99 UK businesses); 66% of employers say upskilling/reskilling
    are vital; **86% view tailored, role-relevant AI training as critical
    to successful adoption.**

  - **A competency framework already exists.** The Alan Turing Institute's
    "AI Skills for Business Competency Framework," developed with DSIT and
    Innovate UK BridgeAI, was formally launched in May 2024, and is
    described as giving "a clear, role-aligned articulation of the
    knowledge, skills, and behaviours required."

- **Inference drawn:** Three findings here are the project's own reading,
  not claims the source makes about itself.

  1. **The document contradicts the platform it promotes.** Its guidance
     tells employers to use diagnostics and build differentiated,
     role-specific pathways — the exact four capabilities three
     independent reviews found missing from the Hub (Entries 022/025).
     The Hub's self-description ("skill-level-tailored learning
     pathways") is directly contradicted by the reviewer finding that
     intermediate learners were served ~71% beginner-level content.

  2. **The contradiction is visible inside the document itself.** Its
     "Skills for success" table lists three skills (self-development, AI
     governance and compliance, change management) against a column
     headed "Relevant courses on the AI Skills Hub" — and every one of
     the three rows says only "AI Skills Hub course catalogue." Asked to
     name specific courses for specific skills, the government's own
     white paper points three times at the undifferentiated catalogue.
     That is the "directory, not a programme" critique demonstrated in
     the government's own document, not merely alleged by outside
     reviewers.

  3. **The evidence base is not independent of the delivery partner.**
     PwC built the Hub; PwC's own surveys (`PwC 2025a/b/c`) are, per
     Annex A, the main source of the paper's quantitative benchmarking
     ("mainly drawn from large-scale datasets such as the PwC Global CEO
     Survey, the AI Jobs Barometer, and the Global Hopes and Fears
     Survey"). The commercial party paid to build the platform is also a
     principal supplier of the evidence used to argue the platform is
     needed. This is a structural interest-concentration issue of exactly
     the kind this log's source-tagging convention exists to surface.

- **Limitations / conflicting evidence:** This is a promotional
  government-programme document, not an evaluation — it makes no claim to
  independently assess the Hub, so "contradiction" here means a gap
  between stated guidance and independently-reported delivery, not
  self-refutation within a single evidential claim. The 18%-of-workers
  figure is a 2021 source used in a 2026 paper without a freshness caveat
  and should not be cited as current. The £400bn figure is
  consultancy-produced (Public First) and has not been traced to its
  underlying method in this pass — treat as "widely cited in official
  documents," not as verified. The 96% figure comes from UKRI's own
  earlier white paper, i.e. the same programme, not independent
  corroboration.

- **Effect on project direction:** Materially strengthens the AI Skills
  Hub critique thread (Entries 018/022/025) by moving part of the evidence
  from third-party review onto the government's own record. Directly
  supplies the "government posture vs. delivered results" spine of the
  planned UK-climate report (`project_log.md` Entry 020). Also gives the
  project a named, official competency framework (Turing/DSIT, May 2024)
  that a credible alternative could map against — relevant to Priority 3.

### Entry 044 — BridgeAI year-three delivery figures: £100m programme, 1,700 course completions

- **Date logged:** 2026-07-28

- **Priority / Question:** Priority 1 (problem framing) and Priority 5 —
  the "actually delivered results" half of the planned UK-climate report.

- **Source:** `[IUK-BRIDGEAI-YR3]`

- **Checked date:** 2026-07-28

- **What the source directly supports:**

  - **Programme scale:** BridgeAI is backed by £100 million from UKRI's
    Technologies Mission Fund and Innovate UK, launched 2023, delivered by
    a consortium of Innovate UK, Digital Catapult, The Alan Turing
    Institute, BSI and the STFC Hartree Centre.

  - **Reported delivery at end of 2025:** £74.6 million of grant funding
    allocated; 5,000+ organisations supported; ~12,000 individuals
    reached; 820+ AI projects funded; **1,700+ AI skills courses
    completed**; **126 accreditations gained**; 10,000+ engagements with
    BridgeAI content (views, comments and downloads).

  - **The Hub is nearly absent from the report.** Across 81 pages, the AI
    Skills Hub is named exactly once, in a single subordinate clause:
    training work "was supported through activity within the AI Skills
    Hub, which has helped to sustain and expand access to high-quality AI
    upskilling." No Hub-specific usage, completion or outcome figures are
    reported.

  - **Its own conclusions concede the gap.** Under "Skills and
    leadership": "There is growing demand for AI-related skills across all
    levels of business... **This needs follow-through with relevant
    development pathways and curriculums**, facilitated by collaboration
    across all levels of education." Under "Scaling beyond early
    adopters": "many businesses remain at the margins of AI adoption.
    Future efforts could focus on deepening regional engagement and
    **tailoring support to different levels of readiness**."

  - A quoted BBC duty manager states "The AI skills ecosystem can feel
    fragmented," positioning the Turing competency framework as potential
    "glue."

  - Ministerial foreword by **Kanishka Narayan MP**, Parliamentary
    Under-Secretary of State, Minister for AI and Online Safety.

- **Inference drawn:** The delivery numbers are strikingly small relative
  to stated ambition, and this is the project's own comparison, not one
  the report draws. The AI Skills Hub carries a publicly stated ambition
  to upskill 10 million workers by 2030 (Entry 018); its parent programme
  reports 1,700+ course completions and 126 accreditations after three
  years and £74.6m allocated. Even allowing that these are
  whole-programme figures rather than Hub-specific ones, and that the Hub
  launched only mid-2025, the order-of-magnitude distance between
  ambition and reported delivery is the single most concrete piece of
  "posture vs. results" evidence the project has found. A second inference:
  the report's own "needs follow-through with relevant development
  pathways and curriculums" and "tailoring support to different levels of
  readiness" are, in substance, the same diagnosis as the external
  "directory not a programme" critique — stated by a delivery partner in
  a government-published report.

- **Limitations / conflicting evidence:** These are self-reported figures
  from a consortium delivery partner (Digital Catapult) writing for the
  funder (Innovate UK), not an independent evaluation — there is no
  external audit of them in this source. The report does not define
  "courses completed" (individual modules vs. full programmes), does not
  disaggregate Hub activity from wider BridgeAI training, and gives no
  denominator for what completion was targeted, so the ambition-vs-delivery
  comparison above is directional, not a like-for-like shortfall
  calculation. No independent evaluation of BridgeAI has been located yet.

- **Effect on project direction:** Supplies the delivered-results evidence
  for the planned UK-climate report. Establishes that the strongest
  version of the project's critique can be built almost entirely from
  government-published material, which is a substantially more defensible
  position than relying on commercially-interested reviewers (Entry 025).
  Raises a specific, checkable open question: what are the Hub's own usage
  and completion figures, and have they been published anywhere?

### Entry 045 — AI Skills Hub remains unfetchable; Innovate UK Business Connect scoping

- **Date logged:** 2026-07-28

- **Priority / Question:** Priority 5 — access route for first-hand
  platform evidence, plus scoping of the Innovate UK Business Connect
  knowledge base as a source vein.

- **Source:** `[AISKILLSHUB]` (status update), plus the Innovate UK
  Business Connect BridgeAI programme page and its BridgeAI-filtered
  "Perspectives" listing.

- **Checked date:** 2026-07-28

- **What the source directly supports:** aiskillshub.org.uk returned HTTP
  403 to an unauthenticated fetch, a different failure mode from the HTTP
  402 recorded at Entry 018 but the same practical outcome across two
  separate passes. The BridgeAI programme page confirms the programme is
  still active and accepting applications, targets four low-adoption
  sectors (agriculture, construction, creative industries, transport/
  logistics), and offers an "AI Adoption Framework" for organisations to
  locate their stage in the AI journey; it gives no programme end date and
  no mention of a successor. The BridgeAI "Perspectives" listing carries
  eight BridgeAI-tagged articles between July 2025 and July 2026,
  including "Training and skills gaps for AI in four selected sectors"
  (8 July 2026) and "BridgeAI three years on: Shaping the future AI
  ecosystem" (21 April 2026) — neither read in this pass.

- **Inference drawn:** None beyond the practical conclusion that
  unauthenticated fetching of the Hub is a closed route and should not be
  retried; the creator's active account is the only viable path to
  first-hand platform evidence.

- **Limitations / conflicting evidence:** Note a discrepancy worth
  resolving: `[IUK-WP2-26]` states the second White Paper is dated
  February 2026, while the Business Connect listing dates its
  corresponding article 16 July 2026, and the PDF's own URL path is
  `/2026/07/`. Publication vs. web-posting dates are the likely
  explanation but this has not been confirmed.

- **Effect on project direction:** Fixes the evidence-collection route for
  the Hub itself (creator's logged-in session, per `project_brief.md`
  "Longer-term direction and positioning"). Identifies two unread
  BridgeAI perspectives pieces and the first (June 2025) White Paper as
  the next primary sources in this vein.

### Entry 046 — Delivery-partner interest concentration; "outsourcing understanding" revived against a new target (see Entry 033 retraction)

- **Date logged:** 2026-07-28

- **Priority / Question:** Priority 1 (problem framing) — an analytical
  entry building on Entries 043–045, not new source material. Also
  revisits the framing retracted in Entry 033.

- **Source:** `[IUK-WP2-26]` and `[IUK-BRIDGEAI-YR3]` (already logged,
  Entries 043–044), plus a direct reading offered by the project's
  creator, 2026-07-28. No new external sources fetched for this entry.

- **What the sources directly support (evidenced, no inference):** PwC was
  commissioned to design, build and run the AI Skills Hub
  (`[IUK-WP2-26]`). The same White Paper's Annex A states its quantitative
  benchmarking was "mainly drawn from large-scale datasets such as the PwC
  Global CEO Survey, the AI Jobs Barometer, and the Global Hopes and Fears
  Survey," and PwC surveys are cited three times in its own argument for
  the scale of the skills gap (`PwC 2025a/b/c`). PwC is additionally named
  as a delivery partner of the Hub in the same document. These are three
  distinct roles — builder, evidence supplier, delivery partner — held by
  one commercial firm, stated on the record in the government's own
  publication.

- **Inference drawn (this entry's own, clearly separated):** The
  interest concentration above is structural rather than incidental: the
  party paid to build the platform is also a principal supplier of the
  evidence used to establish that the platform is needed. This does not
  establish that the evidence is wrong — PwC's survey work may be
  perfectly sound — but it does mean the paper's skills-gap case is not
  independent of its delivery arrangements, and the project should not
  treat those figures as independent corroboration.

- **Creator's reading (opinion, not evidence — held internally):** the
  creator holds an editorial position on institutional capacity and on
  what the delegation to a commercial supplier represents. It is recorded
  in full in the project's internal working notes rather than here,
  because this repository is intended to become publicly visible and the
  parties assessed are prospective funders, collaborators or interviewees
  (see `CLAUDE.md`, "Public repo vs. internal working files"). What
  matters for this log: the position is **not evidenced** by anything in
  Entries 043–046. No source read so far speaks to ministerial or
  civil-service intent, capability or motive. It is usable in an
  explicitly editorial register — as already established for the AI
  Skills Hub briefing's "Overview/Editorial" section — and not in sourced
  sections. The *structural* observation it rests on (PwC's dual role) is
  documented above and stands on its own without it.

- **Relationship to the Entry 033 retraction — the reason this entry
  exists:** The "outsourcing understanding" framing was **retracted by the
  creator's own instruction on 2026-07-24** (Entry 033), on two grounds:
  it was unfair to Instro AI specifically, and it was not well supported
  as a general claim (resting on `[BUYBUILD-KLOTZ26]`, a single-author
  preprint with no confirmed affiliation and no disconfirming search).
  The framing above is a **deliberate revival against a different target**,
  confirmed with the creator before logging. What has changed:

  - **Target:** government/consultancy, not SME/integrator. Entry 033's
    fairness objection was specific to Instro and does not transfer.

  - **Evidential basis:** a documented, on-the-record arrangement in a
    government publication, not a theoretical buy-vs-build claim.
    `[BUYBUILD-KLOTZ26]` is **not** revived and remains uncitable per
    Entry 033.

  - **Scope:** a specific observation about one programme's evidence
    base, not a general thesis about capability transfer.
  Entry 033's substantive caution still applies to the *general* form of
  the claim: "outsourcing understanding" as a broad thesis about
  organisations remains unsupported, and should not be reintroduced as
  one. Entry 031's Instro findings remain in their Entry 033 scope — a
  positive example of successful integration, never a foil.

- **Correction of a figure conflation (recorded to stop it recurring):**
  three separate money figures are in play and were briefly merged during
  discussion. For the record: **£4.1m** is the reported cost of the AI
  Skills Hub alone, and its only source is `[HUMANCO26]`, a commercially
  competing reviewer — it is **not** government-confirmed. **£100m** is
  the whole BridgeAI programme (UKRI Technologies Mission Fund + Innovate
  UK), of which **£74.6m** was allocated by end of 2025. The **1,700+
  course completions / 126 accreditations** are BridgeAI **programme-wide**
  skills figures, not Hub figures and not purchased by the £4.1m. Most of
  the £74.6m went to 820+ funded AI projects, so pairing it with the
  skills numbers would also misstate the case. The defensible statements
  are: (a) the Hub has a 10-million-worker-by-2030 ambition and no
  published usage figures whatsoever; (b) BridgeAI's programme-wide
  three-year skills output is 1,700+ completions and 126 accreditations.

- **Limitations / conflicting evidence:** No source consulted so far
  offers a government or PwC response to the interest-concentration point,
  and none has been sought — this is one-sided until it is. Competitive
  tender is the normal route for public procurement, and the White Paper
  states the tender was competitive, so the arrangement is not
  irregular on its face; the observation is about evidential
  independence, not procurement propriety, and should be worded that way
  to stay defensible. The delivery figures underlying the whole critique
  remain self-reported and unaudited (Entry 044).

- **Effect on project direction:** Gives the planned UK-climate report a
  documented, government-sourced structural critique that does not depend
  on commercially-interested reviewers. Establishes the register boundary
  for the report: interest concentration and delivery figures are
  evidenced and belong in sourced sections; institutional-capacity and
  political-motive readings are the creator's own and belong in an
  editorial section, labelled. Adds a disconfirmation task: seek any
  government, PwC or parliamentary response before publishing the
  interest-concentration point.

### Entry 047 — Parliament on government's own AI capability: the first genuinely independent scrutiny source

- **Date logged:** 2026-07-28

- **Priority / Question:** Priority 1 (problem framing). Directly addresses
  the standing Open Thread that no independent evaluation of government AI
  activity had been located — every prior delivery figure was self-reported.

- **Source:** `[PAC-AIGOV25]`

- **Checked date:** 2026-07-28

- **What the source directly supports:**

  - 70% of government bodies responding to the National Audit Office's
    survey identified difficulties recruiting and retaining staff with AI
    skills as a barrier to AI adoption.

  - Around 50% of roles advertised in civil service digital and data
    recruitment campaigns were unfilled in 2024.

  - Of 72 highest-risk legacy digital systems prioritised under the
    2022–2025 digital and data roadmap, 21 still lacked remediation funding.

  - **DSIT's own admission to the Committee**, quoted in the report: it
    "had to be self-critical about digital leadership across government,
    observing that digital leaders are not well represented at executive
    level across the public sector and many public sector leaders do not
    have enough technical expertise or training."

  - The Committee's own verdict: "We remain sceptical that these reforms
    will address the issue where previous attempts have failed."

  - "There is no systematic mechanism for bringing together and
    disseminating the learning from all the pilot activity across
    government," risking duplicated effort and cost across siloed pilots.

- **Inference drawn:** Two readings, both this entry's own.

  1. **This partially evidences a claim previously logged as unfounded.**
     The creator's flagged claim that policymakers lack practical
     understanding (`project_brief.md`) now has partial official support:
     the responsible department told a select committee that many public
     sector leaders lack technical expertise or training. The match is not
     exact — the PAC finding is about public sector leadership generally,
     not specifically about those writing AI policy or setting budgets —
     so the claim is upgraded from "unfounded" to "partially evidenced,
     with a scope caveat," not to "established."

  2. **The pilots-don't-scale failure appears on both sides.** Parliament
     found government cannot systematically capture learning from its own
     AI pilots; BridgeAI's own report (Entry 044) concluded that barriers
     persist in translating pilots into production for the businesses it
     supports. The same structural failure is diagnosed internally and
     externally in the same period.

- **Limitations / conflicting evidence:** **Scope discipline matters here.**
  This report is about government's *internal* use of AI. It is not an
  evaluation of BridgeAI or the AI Skills Hub, and must not be presented as
  one. It is legitimate evidence about institutional capability and context;
  it is not evidence about the Hub's delivery. The report predates the
  BridgeAI year-three figures (March 2025 vs March 2026). The still-open
  gap is unchanged in one respect: no independent evaluation of BridgeAI or
  the Hub *specifically* has been found.

- **Effect on project direction:** Supplies the first genuinely independent
  scrutiny source in this log — a parliamentary committee auditing the
  executive, materially stronger than any prior source on
  interest-independence grounds. Forms §4 of the UK-climate report
  (`project_log.md` Entry 022). Also identifies the NAO as a source vein
  worth mining further.

### Entry 048 — The £400bn figure traced: vendor-commissioned consultancy research

- **Date logged:** 2026-07-28

- **Priority / Question:** Priority 1 — closes the Open Thread flagged at
  Entry 043 that the headline economic figure was untraced.

- **Source:** `[PUBLICFIRST-MSFT]`, traced from `[IUK-WP2-26]`'s citation.

- **Checked date:** 2026-07-28

- **What the source directly supports:** Public First's UK AI economic
  research in this area was **commissioned by Microsoft**, which has
  separately committed £2.5 billion of UK investment over three years —
  stated on the report's own page. Its method classified more than 17,000
  task-occupation combinations **using GPT-4**, applied to the United
  States **O*NET** occupational database, aggregated using ONS occupational
  data through a 20-year diffusion S-curve modelled on historical
  general-purpose-technology adoption. The headline figure on that page is
  £550bn added to UK GDP by 2035; the £400bn-by-2030 figure cited by
  Innovate UK and the AI Opportunities Action Plan is the related nearer-term
  number.

- **Inference drawn:** The figure underpinning UK AI policy communications
  is not an official statistical projection. It is consultancy modelling
  commissioned by a technology vendor with a direct commercial interest in
  UK AI adoption, built on US occupational data classified by an AI model.
  None of that makes it wrong, and the method is at least transparently
  documented — which is more than several sources in this log manage. But
  it should not be repeated as though it carried ONS or OBR authority, and
  the project should say so plainly whenever it cites the number.

- **Limitations / conflicting evidence:** The relationship between the
  £400bn/2030 and £550bn/2035 figures has not been fully disentangled —
  some secondary coverage attributes a £400bn figure to Google research
  rather than Public First, which has not been resolved. The underlying
  model has not been independently reviewed, only its stated provenance and
  method read. Treat "commissioned by a technology vendor" as established
  and the precise figure lineage as partially traced.

- **Effect on project direction:** Gives the UK-climate report a documented
  provenance for its opening figure and a second, independent instance of
  the interest-concentration pattern found with PwC (Entry 046) — this time
  at the level of the economic case itself rather than the delivery
  arrangements.

- **Attribution corrected 2026-07-31 — see Entry 052.** The £400bn figure
  does not come from the Microsoft-commissioned report named above. The
  Action Plan's own footnote cites Public First's *Google's Impact in the
  UK 2023*. The provenance reasoning in this entry stands; the specific
  attribution, and the GPT-4/O*NET method described above, belong to the
  Microsoft study and must not be attached to the £400bn number.

### Entry 049 — First-hand account: the creator's own AI Skills Hub user journey (primary testimony)

- **Date logged:** 2026-07-29

- **Priority / Question:** Priority 1 (problem framing) and Priority 5 —
  the first-hand platform evidence whose access route Entry 045 fixed
  (the creator's account is the only viable path; unauthenticated
  fetching is closed).

- **Source:** First-hand account given by the project's creator,
  2026-07-29. Participant testimony (n=1), not an external source; the
  full primary text is held in the project's internal working notes,
  with this entry as its evidence-formatted derivative. No source-key
  tag, following the Entry 033/046 precedent for creator-direct
  material.

- **Checked date:** 2026-07-29 (date of recording — the experience
  itself predates the project's founding and is not precisely dated;
  see limitations).

- **What the account directly supports (as testimony):**

  - The creator sought out the AI Skills Hub as an earnest prospective
    user before this project existed, aiming to move from conceptual
    familiarity with AI (long-standing interest, podcasts, videos) to
    practical capability — backend systems, infrastructure, conventions,
    best practices. The project was founded partly *because of* what
    followed, not the other way round.

  - Route in: the relevant government skills-guidance pages, then Hub
    signup. The stated reason for choosing the official route over
    better-known free alternatives (Khan Academy, LeetCode, roadmap.sh
    — in the creator's words, "more accessible, better built"): the
    hope that official pathways would be **better accredited and
    recognised**.

  - What they found on signup: a large catalogue of loosely related
    content with no learning guidance, pathways or personalisation;
    jargon-heavy copy; presentation quality conceded ("well presented
    and polished").

  - The course-signup pattern: selecting a course redirected to a
    third-party provider requiring new account creation — first Google,
    with indications of possible future payment obligations, then
    Microsoft with a similar result. The creator abandoned both signups,
    and stopped after the pattern repeated further.

  - The experience directly prompted starting the predecessor project
    (PAWH, in ChatGPT) — the production history of which is recorded at
    `project_log.md` Entry 025.

- **Inference drawn (each clearly this entry's own):**

  1. The account converges, unprompted, with the two strongest external
     critiques already logged: LSE's "course directory rather than a
     structured programme" (Entry 022) and the Innovate UK White
     Paper's own undifferentiated-catalogue evidence (Entry 043). A
     user experience matching published analysis it had no knowledge of
     is modest corroboration in both directions.

  2. The redirect-to-vendor pattern raises a concrete
     metrics-attribution question: if courses are taken and completed
     on third-party platforms after an outbound redirect, published
     delivery/completion claims need a stated data basis — does any
     completion data flow back at all? This connects directly to the
     Hub's missing usage figures (Entry 044) and has been sharpened
     into a specific FOI question set, held in the internal register.

  3. The stated signup motivation points at the Hub's one asset no
     third-party platform can replicate: official recognition. A
     redirect portal adds no accreditation value to a vendor
     certificate the learner could obtain directly from that vendor —
     *if* the Hub confers nothing of its own, which has not been
     verified (Open Thread). If that holds, the "earnest user drawn by
     official status" is exactly the user the current model wastes.

  4. The barrier pattern the account describes (redirects, account
     creation, possible payment steps, no pathway) bears directly on
     the plausibility of the 10-million-worker-by-2030 ambition (Entry

     018) — a directional observation, not a quantified one.

- **Limitations / conflicting evidence:** n=1; memory-based and not
  precisely dated; and from the project's founder — a motivated
  observer whose project benefits if the Hub looks bad. The chronology
  is the main defence against that objection: the experience preceded
  and caused the project rather than being sought to justify it, and is
  corroborable (Hub account creation date is retrievable; PAWH
  artefacts date the aftermath). The generalisation to other users ("I
  imagine many prospective users may have shared a similar experience")
  is speculation, flagged as such in the account itself. The current
  site may have changed since the experience; this is evidence of the
  then-state, not the now-state. One recalled figure — a "1 million
  delivered" claim — has not been located in any logged source and must
  be traced to primary published wording or not used; the figures this
  log actually holds are the 10m ambition (Entry 018) and BridgeAI's
  programme-wide 1,700+/126 (Entry 044, with the Entry 046 conflation
  warning still in force). The creator's editorial readings recorded
  alongside the account (delivery-partner selection, metrics-as-
  presented-to-Parliament) are held in the internal working notes per
  the established register boundary — not evidenced here, usable only
  in an explicitly editorial register. Fuller biographical context for
  the account — who the user was and what career change prompted the
  search — is likewise held internally rather than here: it adds
  nothing to the evidential weight of the testimony, but is available
  to the published report if the creator decides it belongs there. That
  decision is deliberately deferred to report-drafting rather than made
  by this entry (creator's call, 2026-07-29).

- **Effect on project direction:** Gives the planned UK-climate report
  a documented user-journey spine to hang the already-logged numbers on
  — subject to the creator's decision on how much personal framing to
  publish, which is not made here. Fulfils the first half of Entry
  045's evidence route; the second half — a current-state walkthrough
  with dated screenshots via the creator's logged-in session — is now
  the obvious next evidence task (Open Thread). Sharpens the FOI
  target list (internal register) from "ask for the missing figures" to
  "ask what the published figures count and whether portal-model
  completions are attributable at all". Adds the accreditation-claims
  check as a new verification task before inference 3 is used
  externally.

### Entry 050 — NIST on bias: awareness is not a mitigation, and the disconfirming finding lands on this project's own proposed self-check

- **Date logged:** 2026-07-29

- **Priority / Question:** Priority 4 ("How should misconceptions, unsafe
  practices and overconfidence be addressed?") and Priority 6 (responsible
  use, human oversight). Also bears directly on this log's own method.

- **Source:** `[NIST-1270]` — PRIMARY, read directly.

- **Checked date:** 2026-07-29

- **Origin of the question:** the creator proposed researching human and AI
  biases in order to add bias-prevention measures as a lightweight
  self-check in the project's own working rules, and to reuse the material
  as learning content. This entry is the first research pass against that
  proposal. It substantially complicates it.

- **What the source directly supports:**

  - NIST identifies **three categories of AI bias — systemic, statistical/
    computational, and human** — and argues the field over-attends to the
    computational category. Its Fig. 1 renders this as an iceberg, with
    statistical/computational bias above the waterline and human and
    systemic bias below it.

  - The **human** category is subdivided into *individual* and *group*
    biases. Named individual biases include automation complacency,
    anchoring, availability heuristic, confirmation, Dunning–Kruger,
    implicit, loss of situational awareness, mode confusion, user
    interaction, interpretation, selective adherence, streetlight effect,
    Rashomon effect, presentation and ranking. Named group biases are
    groupthink, funding, deployment and sunk cost fallacy. NIST states the
    list is "not exhaustive."

  - Glossary definitions relevant here, quoted precisely because the
    distinctions matter: **selective adherence** is "Decision-makers'
    inclination to selectively adopt algorithmic advice when it matches
    their pre-existing beliefs and stereotypes"; **automation complacency**
    is "When humans over-rely on automated systems or have their skills
    attenuated by such over-reliance"; **user interaction bias** "Arises
    when a user imposes their own self-selected biases and behavior during
    interaction with data, output, results"; **streetlight effect** is "A
    bias whereby people tend to search only where it is easiest to look";
    **funding bias** arises when results are reported to satisfy a funder,
    "but it can also be the individual researcher"; the **McNamara
    fallacy** is "The belief that quantitative information is more valuable
    than other information."

  - **The disconfirming finding.** NIST states twice, in near-identical
    terms, that awareness does not fix bias: human heuristics and biases
    "are implicit; as such, simply increasing awareness of bias does not
    ensure control over it" (§2.1.2, repeated §3.3.2), and biases impacting
    human decision-making "are usually implicit and unconscious, and
    therefore unable to be easily controlled or mitigated. Any assumption
    that biases can be remedied by human control or awareness is not a
    recipe for success" (§2.1.1).

  - It extends this to oversight arrangements specifically: the perception
    that a human "can effectively and objectively oversee the use of
    algorithmic decision systems is a problematic assumption," and, in a
    framed warning, "Reliance on various downstream professionals to act as
    a governor on automated processes in complex societal systems is not a
    viable approach" (§3.3.1).

  - It further warns that surfacing bias information to downstream users
    "does not always result in a directly positive outcome, and can in fact
    create the opposite" (§3.3.2) — i.e. a flagging mechanism can make
    things worse, not merely fail.

  - **What it recommends instead** (§3.3.2, "Human Factors Guidance") is
    structural rather than attitudinal: *effective challenge* — described
    as a practice creating an environment where practitioners "can actively
    challenge and question steps in modeling and engineering," with
    practitioners required to defend their techniques to others; *impact
    assessment applied at a recurring cadence*, noting that a "misstep with
    impact assessments is to only apply them once at the beginning";
    *independence of assessment*, warning that those being assessed "may
    have undue influence on building or using the assessment"; and
    multi-stakeholder engagement and diversity of perspective.

- **Inference drawn (this entry's own, not NIST's):**

  1. The proposal as originally framed — a self-check that raises awareness
     of biases — is the specific intervention NIST says does not work.
     Taken at face value the finding does not kill the idea, but it
     redirects it: the useful artefact is a small set of **procedural
     triggers attached to specific moments of work**, not a list of biases
     to hold in mind.

  2. Three practices this project already runs are recognisable instances
     of what NIST recommends, arrived at independently and without this
     framing: the confirm/disconfirm pairing on foundational claims is
     effective challenge applied to evidence; the repo audit's
     second-model pass plus required human verification is independence of
     assessment; and that audit being scheduled monthly rather than ad hoc
     is cadence. This is convergence, not validation — but it means the
     self-check should mostly *name and connect* existing practice rather
     than add new machinery.

  3. `selective adherence` is the precise term for a failure mode this
     project is structurally exposed to and has not named: Entry 013 caught
     the *input* form (framing queries to find support), whereas selective
     adherence is the *output* form (accepting AI results that fit the
     thesis with less scrutiny than results that don't). The existing rules
     cover the first and not the second.

  4. The `streetlight effect` describes something already visible in this
     log's own evidence base rather than a hypothetical risk: `[AISKILLSHUB]`
     (402 then 403), `[SBA-ADVOCACY25]` (403), `[AUTOBIAS-MED25]` (403) and
     `[SAIL4ALL25]` (login wall) are all unfetchable, so what the log
     contains is shaped in part by what happened to be retrievable.

  5. The `McNamara fallacy` is a live risk for the UK climate report
     specifically, whose argument rests on the contrast between published
     numbers. The fallacy would be to let what is counted stand in for what
     matters.

- **Limitations / conflicting evidence:**

  - **Published March 2022, and this matters more than the date alone
    suggests.** It predates general public use of conversational LLM
    assistants. Its subject is algorithmic *decision* systems — hiring,
    credit, criminal justice — with a human overseeing a model's output,
    not a person working alongside a general-purpose assistant. The named
    human biases are general cognitive phenomena and transfer reasonably;
    the deployment picture does not transfer cleanly and should not be
    treated as though it does.

  - US, not UK. Voluntary guidance explicitly "not intended to serve as or
    supersede existing regulations," and by its own description a "first
    step on the roadmap" rather than a settled standard.

  - Its primary audience is those "designing, developing, deploying,
    evaluating, and governing AI systems" — organisations, not individual
    practitioners. Applying it to a one-person project is an extension
    beyond its stated scope, and specifically, its diversity and
    multi-stakeholder recommendations have no direct single-operator
    analogue. The second-model audit pass is a thin substitute at best.

  - It offers **no empirical effect sizes** for any recommended mitigation.
    Effective challenge, cadence and independence are presented as
    reasoned recommendations drawn from a literature review, not as
    measured interventions. The strength of the negative claim (awareness
    doesn't work) is not matched by comparable evidence that the
    alternatives do.

  - Not yet paired with a disconfirming source. The claim that awareness
    training fails is *convergent* with Entry 028's `[AUTOBIAS-MED25]`
    (trained physicians still showed automation bias) and in tension with
    Entry 028's `[KAMALI26]` (targeted training improved calibration).
    Entry 028's unresolved question — when does training work? — is
    unresolved still, and this entry does not settle it. Flagged in Open
    Threads.

- **Effect on project direction:** Provides the evidence base for a bias
  self-check, and changes its shape before anything was built: procedural
  triggers at named moments, not an awareness checklist. Adds
  `selective adherence` as a genuinely uncovered gap in the existing
  research rules. The adoption decision and the resulting rule text are
  recorded at `project_log.md` Entry 028, this log being for the finding
  rather than the decision. The learning-content use of this material is a
  separate track and is not decided here.

---

### Entry 051 — The AI Opportunities Action Plan, read directly: government states it does not know the size of the skills gap

- **Date logged:** 2026-07-31

- **Priority / Question:** Priority 1 — the upstream policy document every
  programme this log has examined descends from. Cited repeatedly across
  Entries 043–048, never read.

- **Source:** `[AIOPP-PLAN25]`

- **Checked date:** 2026-07-31

- **What the source directly supports:**

  - **Status.** An independent report by Matt Clifford, written in the first
    person ("my judgement is", "I have tried to draw"), commissioned by the
    Secretary of State and presented to Parliament as CP1241 on 13 January
    2025. It makes 50 recommendations. It is not itself a statement of
    government policy, and must not be cited as one.

  - **The skills gap was unmeasured, and the plan says so.** Recommendation
    14: "Accurately assess the size of the skills gap. Current estimates are
    imprecise and outdated; the last government-funded AI labour market
    survey was in 2020 and the Unit for Future Skills' jobs and skills
    dashboard, while a step in the right direction, still uses supply data
    from 2019. The success of the following recommendations depends on
    accurately understanding the skills gap, and so government must make
    efforts to come to a concrete and up-to-date number."

  - **The skills section is about AI professionals, not the workforce.**
    Section 1.3 is titled "Training, attracting and retaining the next
    generation of AI scientists and founders". Recommendations 15–22 cover
    AI graduates, diversity in the AI pipeline, routes into the AI
    profession, a Rhodes-scale scholarship, internal headhunting, visa
    routes and Turing fellowships. Recommendation 19, "Ensure its lifelong
    skills programme is ready for AI", is the only one addressing the wider
    working population, and commits to nothing specific — government "should
    ensure there are sufficient opportunities" and might "consider the merit"
    of approaches used in Singapore and South Korea.

  - **SMEs get one sentence.** Recommendation 49: "A particular focus should
    be put on supporting SMEs and the specific challenges they face."

  - **Footnote provenance.** The two concrete productivity claims in section
    2.1 — AI assistants "freeing up to 20% of an employee's time", and
    drafting cutting document production times "by 20-80%" — are both
    footnoted to "Business leader interviews, August 2024": unpublished,
    unquantified, no sample stated. The "tens of thousands of AI
    professionals" target is "Based on internal DSIT estimates".
    Recommendation 36's civil-service pay benchmarking is sourced to the
    Tony Blair Institute.

  - Recommendation 45 proposes a single "AI Knowledge Hub" as "a single
    place to access frameworks and insights" for technical and non-technical
    users alike.

- **Inference drawn:** The plan the UK's AI skills programmes descend from
  states that it does not know the size of the problem, and makes fixing
  that a stated precondition for everything else in its skills section.
  Separately, the general adult workforce — this project's chosen audience —
  is addressed by one non-committal recommendation inside a section
  explicitly about scientists and founders. That is a gap at the top of the
  policy chain, not only at delivery level, and it is visible in the
  government's own published text.

- **Limitations / conflicting evidence:** The government's formal response
  was published the same day but has **not been read**. The claim that it
  accepted all 50 recommendations rests on secondary coverage and must be
  verified before use — nothing here supports "the government committed to
  X" — **resolved 2026-07-31, see Entry 057: the response has now been read,
  and the correct statement is 48 recommendations agreed and 2 partially
  agreed, not "all 50 accepted".** Matt Clifford's own position (co-founder of Entrepreneur First, chair
  of ARIA) sits alongside a plan that repeatedly recommends startup-
  favourable measures, including that Innovate UK prioritise AI funding for
  startups; that is an observation with no disconfirming search run against
  it, and it is not usable externally in its current state. The gov.uk page
  carries an `updated` timestamp of 23 July 2026, which is a bulk
  republication — five related documents were re-stamped within two minutes
  — not a content change.

- **Effect on project direction:** Supplies the upstream frame the UK-climate
  report lacks. Recommendation 14 in particular gives that report a
  documented starting point in the government's own words: the ambition was
  set before the gap was measured. Whether it was measured afterwards is
  Entry 054.

### Entry 052 — Correction: the £400bn figure is Google-commissioned, not Microsoft-commissioned (supersedes part of Entry 048)

- **Date logged:** 2026-07-31

- **Priority / Question:** Priority 1 — corrects an attribution in Entry 048
  that has already been repeated in a drafted external-facing document.

- **Source:** `[AIOPP-PLAN25]` footnote 19; `[PUBLICFIRST-MSFT]`

- **Checked date:** 2026-07-31

- **What the source directly supports:** The Action Plan's section 2.4
  states "AI adoption could grow the UK economy by an additional £400
  billion by 2030 through enhancing innovation and productivity in the
  workplace", and attaches footnote 19. Footnote 19 reads: "Public First,
  'Google's Impact in the UK 2023', 2024 (accessed 15 October 2024)". The
  plan's nineteen footnotes were counted through to confirm the mapping.

- **Inference drawn:** Entry 048 attributed the £400bn figure to Public
  First's **Microsoft-commissioned** report, whose own headline is £550bn by
  2035, and recorded the competing Google attribution as unresolved. The
  Action Plan's own citation resolves it the other way. Both reports exist
  and both are by the same consultancy. This does not weaken the
  interest-concentration finding of Entries 046/048 — it sharpens it: one
  consultancy produced headline UK AI economic figures for two different
  large technology vendors, and the government's flagship AI plan cites one
  of them.

- **Limitations / conflicting evidence:** Public First's Google report has
  **not** been read, so unlike the Microsoft report its method is untraced.
  The GPT-4 / O*NET / 17,000-task-combination method described in Entry 048
  belongs to the Microsoft study and must not be attached to the £400bn
  figure. Entry 048's reasoning about provenance stands; only its
  attribution is wrong.

- **Effect on project direction:** `drafts/UK_AI_Skills_Ambition_Report.docx`
  §1, its NOTE callout and its source list all carry the wrong attribution
  and the wrong method description. They must be corrected before the report
  goes anywhere.

### Entry 053 — AI Skills Boost: what the million-course figure actually counts

- **Date logged:** 2026-07-31

- **Priority / Question:** Priority 1 — the delivered-results figure for the
  programme that carries the 10-million-worker target. Supersedes the
  BridgeAI 1,700-completions figure (Entry 044) as the right number to set
  against that target.

- **Source:** `[AISKILLSBOOST26]`, `[AIOPP-1YEAR26]`

- **Checked date:** 2026-07-31

- **What the source directly supports:**

  - AI Skills Boost is the programme carrying the target: "a
    government-industry initiative to improve UK workforce readiness by
    upskilling 10 million UK workers in AI skills by 2030, which was
    announced by the Prime Minister in June 2025 at London Tech Week." The
    revamped AI Skills Hub is its platform.

  - The figure: "1,001,147 AI training courses have been completed according
    to course completion data shared with DSIT by industry partners in
    January 2026."

  - What it covers: "all AI skills courses delivered by partners since June
    2025, from introductory AI literacy to advanced training in areas like
    data science and machine learning engineering, for both external
    learners (customers, clients, platform users) and internal learners
    (partner employees)."

  - The eleven partners: Accenture, Amazon, BT, Barclays, IBM, Google,
    Intuit, Microsoft, SAS, Sage and Salesforce.

  - It "includes courses delivered through the government's One Big Thing
    initiative in 2025" — the civil service's own internal learning day.

  - "Specific partner or course-level breakdowns of course completion are
    not shareable due to commercial sensitivity."

  - Benchmarking is partial: the launch release states that "A selection of
    industry-developed AI courses, newly available on government's AI Skills
    Hub, have been checked against Skills England's AI foundation skills for
    work benchmark."

  - `[AIOPP-1YEAR26]` reports "38 of the 50 actions" met and repeats the
    million-course figure in both the Prime Minister's and the Secretary of
    State's forewords.

  - DSIT's own economic modelling in the explainer publishes its equations
    and states of its £55–140 billion GVA estimate: "This estimate is highly
    uncertain."

- **Inference drawn:** The target is expressed in workers; the reported
  progress is expressed in courses. Those are different units, and one
  worker completing several short courses counts several times. The count is
  supplied by eleven companies with a direct commercial interest in AI
  adoption, spans their own employees as well as their customers, includes a
  civil service internal training day, and carries no published breakdown.
  The Skills England benchmark covers a selection of courses on the Hub,
  while the figure spans all partner courses since June 2025 including
  advanced machine-learning training well outside a foundation-skills
  standard — so what proportion of the million meets the government's own
  benchmark is not publicly knowable. None of this makes the figure false.
  It makes it unverifiable.

- **Limitations / conflicting evidence:** The explainer does not state
  whether the figure is restricted to UK learners, or by what mechanism,
  although the programme is described throughout as targeting UK workers.
  Individual partner claims quoted in the launch release — Microsoft "more
  than 1.5 million people", Google "1.2 million" — each exceed the
  programme's own total, which indicates a different accounting basis; that
  was read only through a fetch summary and is not established. DSIT's
  hedged modelling is a point in the department's favour and should be
  reported alongside the criticism, not omitted: it contrasts with the
  unhedged £400bn figure (Entry 052).

- **Effect on project direction:** Materially changes the UK-climate report.
  Setting BridgeAI's 1,700 completions against the 10-million target
  compares a different programme's figure to that ambition, and a reader who
  knows the million-course number will read the report as cherry-picked. It
  also gives the planned FOI a precise target: UK filtering, the
  internal/external split, the operational definition of "completed", and
  the benchmarked proportion.

### Entry 054 — Recommendation 14 was delivered: the AI Labour Market Survey 2025

- **Date logged:** 2026-07-31

- **Priority / Question:** Priority 1 — tests whether the Action Plan's own
  stated precondition (Entry 051) was ever met. Run as a deliberate
  disconfirming check on the assumption that it was not.

- **Source:** `[AILMS25]`

- **Checked date:** 2026-07-31

- **What the source directly supports:** DSIT commissioned Gardiner &
  Theobald "to examine the UK AI skills labour market in 2025", building on
  the 2020 study. The executive summary states: "The findings contribute to
  the delivery of the AI Opportunities Action Plan (2025), aimed at
  accurately identifying AI skills shortages and supporting policy decisions
  to strengthen the UK's AI ecosystem." Headline findings: 97% of
  respondents identified at least one gap in the AI labour market; 57% of
  businesses reported a technical skills gap and 30% a non-technical one;
  the largest single gap is in "understanding AI concepts and algorithms",
  rising from 55% to 60% over five years.

- **Inference drawn:** Recommendation 14 was acted on. The project **cannot**
  claim the gap went unmeasured, and an argument built on that claim would
  have been wrong. This is a disconfirming finding against the convenient
  version of the project's own argument, produced by looking for it
  deliberately rather than by accident.

- **Limitations / conflicting evidence:** **The survey's scope is
  unverified, and it is the load-bearing question.** The executive summary
  refers throughout to "the UK AI skills labour market" — the same framing
  that required Entry 001 to be corrected, when the 2020 survey turned out
  to be scoped to the AI sector rather than the general workforce. If 2025
  repeats that scoping, then the general-workforce gap that the
  10-million-worker target addresses is still unmeasured, and Entry 051's
  finding survives in a narrower but still substantial form. The full PDF
  has not been read; sample size and surveyed population are unknown.

- **Effect on project direction:** Blocks an overstatement the project was
  close to making, and makes a full read of this survey the highest-priority
  remaining check before the report is redrafted.

- **Scope resolved 2026-07-31 — see Entry 056.** The full report was
  obtained and its methodology read. The survey is scoped to the AI sector,
  covers 119 self-selected organisations at a 3% response rate, and half its
  respondents are in Greater London.

### Entry 055 — The Skills Toolkit precedent, and what the statistics regulator found about its numbers

- **Date logged:** 2026-07-31

- **Priority / Question:** Priority 1/5 — whether the AI Skills Boost
  delivery model has a documented predecessor, and whether that predecessor
  was evaluated.

- **Source:** `[FEWEEK-HUB26]`, `[SKILLSTOOLKIT-OSR21]`, `[OPENBADGES]`

- **Checked date:** 2026-07-31

- **What the source directly supports:**

  - DfE launched The Skills Toolkit in April 2020: over £1 million of public
    money on a page within the National Careers Service signposting to free
    online courses from Amazon, Microsoft, LinkedIn, the Open University and
    Google Digital Garage.

  - Per FE Week's reporting of an OSR letter to DfE's chief statistician in
    March 2021, the regulator found that registration figures included web
    hits and were unfiltered by geography, so could come from anywhere in
    the world; that "a completion may simply represent that a user has
    accessed learning material, not necessarily that they completed the
    course"; and that the data sat in an "additional analysis section" that
    "may not be clear to users looking for these data in the release".
    The letter went to DfE's chief statistician, Neil McIvor, and also
    challenged the department's use of unpublished Skills Toolkit data in
    answers to multiple parliamentary questions. DfE moved to publishing the
    figures as experimental statistics under the Code of Practice.

  - Sue Pember, policy lead at HOLEX, draws the comparison to AI Skills
    Boost directly: "While the ambition is positive, the lesson from the
    skills toolkit should be that take-up and outcomes matter more than
    headline registration numbers."

  - Skills England chair Phil Smith, on the new programme: "It's also a huge
    step forward that everyone who completes these short courses will get
    digital badges that properly recognise what they've learned. It's a
    simple idea that will make a huge difference."

  - The Open Badges standard was published by Mozilla on 15 September 2011.

- **Inference drawn:** The delivery model has a close documented predecessor
  — government-branded signposting to free vendor courses, with headline
  figures supplied by those same vendors — and the statistics regulator
  found that predecessor's numbers unreliable in precisely the two respects
  that apply to the 1,001,147 figure in Entry 053: what "completion"
  operationally means, and whether the count is geographically filtered.
  This is the strongest structural argument found so far, because it needs
  no characterisation: the facts and the dates carry it. Separately, digital
  badging was a fourteen-year-old open standard at the point it was
  described as a step forward.

- **Limitations / conflicting evidence:** **The OSR correspondence has not
  been read directly.** All of it rests on FE Week's reporting across two
  March 2021 articles, and the FE Week piece on AI Skills Boost was read via
  a fetch summary rather than in full. Both need direct reads before
  publication; the £1m figure is likewise second-hand. HOLEX is a membership
  body for adult and community education, so it has an institutional
  interest in how adult skills funding is directed — though not a commercial
  stake in the platform, which is a materially better source position than
  two of the three reviewers relied on in Entries 022/025. Phil Smith's
  public roles (former CEO and chair of Cisco UK & Ireland, former chair of
  Innovate UK) are relevant context, but the dates have not been checked and
  any characterisation of a named individual belongs in internal notes and
  requires right of reply first.

- **Effect on project direction:** Gives the report a documented precedent
  with a regulator's findings attached — structurally stronger than the
  three platform reviews currently carrying its critique, two of which are
  commercially interested. The badge observation is usable in the project's
  understated register: quote the claim, state the year the standard was
  published, and stop.

- **Attribution corrected 2026-07-31 — see Entry 059.** The OSR letter has
  since been retrieved and read directly. It does **not** contain the
  completion-definition or geographic-filtering findings this entry credits
  to the regulator; those are FE Week's, and the department's own admissions.
  The facts stand, the attribution in this entry does not.

### Entry 056 — What "accurately assess the size of the skills gap" delivered: 119 self-selected AI-sector organisations

- **Date logged:** 2026-07-31

- **Priority / Question:** Priority 1 — resolves the scope question Entry 054
  flagged as load-bearing.

- **Source:** `[AILMS25]`, sections 1–3 of the full report read directly.

- **Checked date:** 2026-07-31

- **What the source directly supports:**

  - **Scope is the AI sector, not the working population.** "This market is
    defined as UK organisations that fall into the three categories outlined
    within Section 3, which are those who are commercially developing AI,
    those who are internally developing AI and those who are procuring AI."
    66% of respondents are commercially developing AI solutions.

  - **Sample: 119 organisations**, from 3,940 contacted. The report states:
    "Although that represents a 3% response rate, it is a similar number of
    responses and response rate to the 2020 survey." Twenty interviews were
    conducted, down from fifty in 2020.

  - **Self-selecting, and flagged as such by its authors.** Under "To note
    before reading": "Self-selection participation to the survey may create a
    biased sample."

  - **Concentrated.** 93% of respondents are SMEs and 82% are small or micro
    organisations. Greater London accounts for 50% of responses and the
    South of England a further 27%; regions outside southern England make up
    24%. Scotland returned six organisations, Wales two, Northern Ireland one.

  - **Not a statement of government view.** "subsequent findings or
    recommendations do not represent Government views or policy and are
    instead G&T views."

  - Its own account of its role: "The findings of this report contribute to
    meeting that recommendation, as well as forming part of DSIT's wider work
    assessing trends in the UK's AI labour market."

- **Inference drawn:** Entry 054 established that Recommendation 14 was acted
  on, and that stands. What it could not then say is what the action
  consisted of. The survey describing itself as contributing to that
  recommendation covers 119 self-selected organisations inside the AI sector,
  half of them in Greater London, at a 3% response rate, with its authors'
  own caveat about bias — and it measures the AI industry's demand for AI
  professionals, not whether the general working population can use AI tools.
  That is a different question from the one the 10-million-worker target
  addresses. The Action Plan called the existing estimates "imprecise and
  outdated"; its successor is precise about a different and far smaller
  population.

- **Limitations / conflicting evidence:** This survey is explicitly one input
  among several, **not** the whole of the government's response to
  Recommendation 14 — the response committed Skills England to a wider
  assessment (Entry 057), and Skills England's own published work is already
  in this log at Entries 017 and 019. The report must not claim this survey
  *is* the government's skills-gap assessment. The 97% / 57% / 30% figures
  widely reported from it are the responses of 119 self-selected AI companies
  and should never be quoted without that denominator attached.

- **Effect on project direction:** Entry 051's finding survives in its
  stronger form: the general-workforce gap the 10-million-worker target
  addresses is not measured by this survey. The report can now state
  precisely what was measured instead, in the survey's own published numbers.

### Entry 057 — The government response (CP 1242): what was committed on skills, and by when

- **Date logged:** 2026-07-31

- **Priority / Question:** Priority 1 — closes the open item in Entry 051,
  where the response was identified but unread and the "accepted all 50"
  claim rested on secondary coverage.

- **Source:** `[AIOPP-RESP25]`

- **Checked date:** 2026-07-31

- **What the source directly supports:**

  - Command Paper CP 1242, presented to Parliament on 13 January 2025 — the
    same day as the plan it answers.

  - Each of the 50 recommendations receives an individual verdict and a
    target date. **48 are answered "Agree" and 2 "Partially agree"** — the
    copyright-cleared British media training dataset, and the immigration
    and visa recommendation. The widely repeated claim that government
    "accepted all 50" is very nearly, but not exactly, right.

  - **Recommendation 14, in full:** "Agree. Working closely with DSIT and the
    Industrial Strategy Council, Skills England will bring businesses,
    training partners and unions together with national and local government
    to develop a clear assessment of the country's skills need – including AI
    and digital skills – and map pathways by which they can be filled.
    Updated assessments will be published regularly." Target date given:
    **Spring 2025.**

  - **Recommendation 19** ("Ensure its lifelong skills programme is ready for
    AI"): "Agree. DFE will take this forward with Skills England, aligning
    with the work of the independent Curriculum and Assessment Review."
    Target date: Autumn 2025.

- **Inference drawn:** The commitment was to assess **the country's** skills
  need, led by Skills England, with businesses, unions and local government
  at the table, published on a repeating basis, by Spring 2025. That is a
  materially wider undertaking than the AI-sector survey in Entry 056, which
  is the artefact most visibly produced under that heading.

- **Limitations / conflicting evidence:** Whether Skills England's own
  published assessments (Entries 017 and 019) satisfy the Recommendation 14
  commitment has **not** been tested directly, and this entry does not claim
  the commitment was unmet — only that the commitment and the survey are not
  the same thing. Target dates are as stated in the response; delivery
  against them has not been checked beyond Recommendation 14.

- **Effect on project direction:** Gives the report the government's own
  words on what it promised and by when. Promise and delivery can now be set
  beside each other from two government documents, which is a stronger
  construction than either alone.

### Entry 058 — Government's own evidence review: policy has focused on AI professionals, and evidence on AI skills for life is "necessarily limited"

- **Date logged:** 2026-07-31

- **Priority / Question:** Priority 1/3 — independent corroboration, from
  inside government's own evidence base, of Entry 051's reading of where UK
  AI skills policy has directed its attention.

- **Source:** `[AISKILLSLIFE-RER26]`

- **Checked date:** 2026-07-31

- **What the source directly supports:**

  - Published 28 January 2026 — the same day as the AI Skills Boost launch,
    and the day before *One Year On*. Authored by Prof Rob Procter of Warwick
    University and the Alan Turing Institute, supported by DSIT and the DCMS
    R&D Science and Analysis Programme.

  - **On where attention has gone:** "The UK's focus to-date has largely been
    on increasing the supply of AI skills for work through investment in
    tertiary education."

  - **On the evidence base:** "The evidence on current levels of AI skills
    for life in the UK is necessarily limited at this time but it is
    reasonable to assume that they are at a relatively low base compared to
    EDS for Life."

  - Its stated research questions include "To what extent does the UK have or
    lack these skills in the labour force?"

  - **On public recognition of AI**, citing ONS: 17% of adults report they
    can often or always recognise when they are using AI; 50% some of the
    time or occasionally; 33% hardly ever or never. Adults aged 70 and over
    are least likely to recognise it.

  - **On the underlying constraint:** a significant proportion of the UK
    population hold only partial Essential Digital Skills, and the review
    argues AI skills for life cannot be realised without that digital
    literacy foundation.

- **Inference drawn:** The observation that UK AI skills policy has
  concentrated on professional supply is not this project's inference alone —
  it is stated in a review government itself commissioned and published.
  That materially strengthens Entry 051, which rested on this project's own
  reading of the Action Plan's structure. The review also supplies a
  government-supported statement that evidence on AI skills for life is
  limited, for exactly the population the 10-million-worker target names.

- **Limitations / conflicting evidence:** Read at section level rather than
  end to end — roughly 167,000 characters, of which the executive summary,
  introduction and the AI-skills-gap sections were read. Its ONS figures date
  from 2023, so "17% of adults" is not a current statistic and must not be
  presented as one. The juxtaposition of its publication date with the AI
  Skills Boost launch is a fact about publication dates only; whether the
  review was written substantially earlier has not been checked, and its 2023
  citations suggest it may have been. The companion *Labour market and skills
  projections* report remains unread.

- **Effect on project direction:** Replaces this project's own structural
  reading of the Action Plan with a government-published, academically
  authored source making the same point. For a report whose argument is built
  on government's own material, that is the difference between an inference
  and a citation.

### Entry 059 — The OSR letter, read directly: the regulator did not find what Entry 055 attributed to it (supersedes part of Entry 055)

- **Date logged:** 2026-07-31

- **Priority / Question:** Priority 1/5 — closes the "not read directly"
  limitation Entry 055 flagged against its own central source, and tests
  whether that entry's inference survives contact with the document.

- **Source:** `[SKILLSTOOLKIT-OSR21]`, `[FEWEEK-TOOLKIT21]`, `[FEWEEK-HUB26]`

- **Checked date:** 2026-07-31

- **What the source directly supports:**

  - **The letter is public.** OSR publishes its correspondence as a matter of
    course. It was not paywalled, login-gated or FOI-only. Entry 055's
    "has not been retrieved" recorded not having looked, not unavailability —
    a materially different evidential position, and the report's wording
    implied the wrong one.

  - Mary Gregory, Deputy Director for Regulation, OSR, to Neil McIvor, Chief
    Data Officer and Chief Statistician, DfE, 8 March 2021, headed *Use of
    unpublished data during Parliamentary Questions*.

  - Its subject is two uses of unpublished Skills Toolkit data in answers to
    Parliamentary Questions: registrations in October 2020, where OSR's view
    was that "the response should have drawn on the latest published data"
    and the figures "have since been revised and updated"; and course
    completions in January 2021.

  - Two presentational improvements requested: that the data sit under an
    "Additional Analysis section. This may not be clear to users looking for
    these data in the release", and that "not all limitations of the data are
    included for example they do not currently inform users of what the
    geographical coverage is".

  - The undertaking obtained: the department "will follow the principles of
    the Code of Practice, in particular ensuring that sufficient
    methodological detail is available for readers to fully understand the
    figures".

  - Its register throughout is cooperative — "We welcome…", "It is positive
    that you sought to provide analytical support…", "some improvements we
    would like to see" — not the reprimand secondary coverage describes.

- **What the letter does not contain:** web hits counted as registrations; a
  three-minute completion threshold; any statement that a completion may mean
  a user merely accessed material; any finding that registrations were
  globally unfiltered; any mention of experimental statistics.

- **Inference drawn:** Entry 055 stated that "the statistics regulator found
  that predecessor's numbers unreliable in precisely the two respects that
  apply to the 1,001,147 figure in Entry 053: what 'completion' operationally
  means, and whether the count is geographically filtered." **That attribution
  is wrong.** Those were FE Week's findings and the department's own
  subsequent admissions. The regulator's letter is narrower and procedural:
  unpublished figures used in Parliament, and how limitations are presented.
  The underlying facts survive unchanged and the 2021-versus-2026 comparison
  still holds — only the credit was misassigned. The corrected version is
  arguably the stronger one: a trade paper's investigation found the defects,
  and the regulator's own response was mild.

- **Limitations / conflicting evidence:** The letter was read as published
  HTML; the PDF attachment was not opened separately. **The three 2021 FE Week
  articles still have not been read in full** — the web-hits, geography and
  starts-not-completions claims rest on their headlines and on search-result
  summaries. The geography claim has no direct-read source at all and is the
  weakest thing now standing in the report's §4. The 30 January 2026 FE Week
  article was retrieved directly and does support the web-hits and
  three-minute details. The £1 million cost figure remains untraced to any
  departmental publication.

- **Effect on project direction:** `drafts/UK_AI_Skills_Ambition_Report.docx`
  §4 rebuilt on the corrected attribution, with the letter's undertaking
  sentence added as a pull quote — a 2021 commitment that enough
  methodological detail be published for readers to understand the figures,
  set against 2026's withheld breakdowns and undefined "completed". The
  general lesson is that Entry 055's own honest limitation note is what made
  this correction findable; the practice of recording what was *not* read is
  doing real work and should not be relaxed.

### Entry 060 — The government's own delivery tracker: Recommendation 14 marked met, and the one recommendation about ordinary workers is not

- **Date logged:** 2026-07-31

- **Priority / Question:** Priority 1 — resolves the Entry 056/057 open thread
  on whether Skills England's assessment work satisfies Recommendation 14, by
  going to what government itself claims it delivered.

- **Source:** `[AIOPP-DELIVERY26]`

- **Checked date:** 2026-07-31

- **What the source directly supports:**

  - A per-recommendation progress site published by DSIT and Number 10 Data
    Science, dated January 2026. Headline score: **38 of 50 met (76%)**, 12 in
    progress.

  - **Recommendation 14 is marked "Commitment Met."** Five publications are
    named as the delivery: *Skills for Growth and Opportunity* (June 2025),
    *AI Skills for the UK Workforce* (October 2025), *UK Standard Skills
    Classification* (November 2025), *The AI Skills for Life and Work
    Collection* (January 2026), and *AI Skills in the UK Labour Market*
    (January 2026). Skills England "will continue to produce regular Skills
    Needs Assessments".

  - The last of those five is `[AILMS25]`, and government's own description of
    it scopes it exactly as Entry 056 found: it assesses "trends, skills,
    gaps, and evolving skills needs **in the AI sector**."

  - **Skills & Talent: 7 met, 2 in progress.** The two outstanding are
    Recommendation 16 (diversity of the talent pool) and **Recommendation 19,
    "Ensure its lifelong skills programme is ready for AI."** Recommendations
    15, 17, 18, 20, 21 and 22 — graduates, education pathways, the Spärck AI
    scholarship, internal headhunting, visa routes, Turing fellowships — are
    all marked met.

  - Recommendation 49, "Drive AI adoption across the whole country", is also
    in progress. Recommendation 45's AI Knowledge Hub launched 23 May 2025 and
    reports "over 50,000 views since May 2025" — a different platform from the
    AI Skills Hub, aimed at public sector teams.

- **Inference drawn:** Entry 051 established that Recommendation 19 is the only
  one in the plan addressing the general working population, inside a section
  otherwise about scientists and founders. The government's own tracker now
  scores every AI-professional recommendation in that section as met, and the
  one covering everyone else as still in progress. That is the Entry 051 and
  Entry 058 finding restated in the government's own delivery scoring, which
  is a stronger evidential position than this project's reading of the plan's
  structure. Separately, the project **cannot** claim Recommendation 14 went
  undelivered: five artefacts are named, three of which are already in this log.

- **Limitations / conflicting evidence:** **This is self-assessment**, and the
  interest tag should travel with every citation of it — DSIT and Number 10
  scoring their own plan, with no stated test for what "Commitment Met"
  requires and no external audit. "38 of 50" is government's own mark of its
  own homework. Two of the five Recommendation 14 publications (*Skills for
  Growth and Opportunity*, *UK Standard Skills Classification*) have not been
  read. The site returns 403 to ordinary fetching and was read through a
  browser via its underlying JSON, so the rendered pages themselves were
  sampled rather than each read individually.

- **Effect on project direction:** Closes the Entry 056/057 thread. The
  UK-climate report's §2 must stop implying the AI Labour Market Survey is the
  artefact produced under Recommendation 14, and its callout must name the
  wider assessment work. The Recommendation 19 finding is the strongest
  single-sentence corroboration the report has for its central claim about
  where attention went.

### Entry 061 — The target was 7.5 million, not 10 million: three government sources disagree (bears on the report's opening paragraph)

- **Date logged:** 2026-07-31

- **Priority / Question:** Priority 1 — tests the figure the UK-climate report
  opens with, after `[AIOPP-DELIVERY26]` gave a different number from
  `[AISKILLSBOOST26]`.

- **Source:** `[AISKILLS-JUN25]`, `[AIOPP-DELIVERY26]`, `[AISKILLSBOOST26]`

- **Checked date:** 2026-07-31

- **What the source directly supports:**

  - **The June 2025 announcement set 7.5 million, not 10 million.** DSIT,
    14 June 2025: "Leading tech firms join talks with ambitions to train 7.5
    million UK workers in essential AI skills" — by 2030, roughly a fifth of
    the workforce. The eleven partners named are exactly those the report
    lists.

  - The same release contains a 10 million figure, but as a different measure
    entirely: "we expect around 10 million workers to be **using** AI in their
    day-to-day role by **2035**." Different verb, different year, a projection
    rather than a target.

  - The delivery tracker's Recommendation 19 entry: 7.5 million agreed with
    eleven companies in June 2025; the AI Skills Boost platform launched
    January 2026 with 24 partners, and government "announced it would expand
    the programme to provide 10 million workers with key AI skills by 2030."

  - `[AISKILLSBOOST26]`, January 2026, describes the 10-million-by-2030 target
    as "announced by the Prime Minister in June 2025 at London Tech Week."

- **Inference drawn:** The explainer's attribution is not supported by the
  June 2025 announcement, and is contradicted by the department's own delivery
  tracker. On the documented sequence the target was set at 7.5 million in June
  2025 and raised to 10 million in January 2026 — the same month the first
  progress figure, 1,001,147 courses, was published. The million courses
  therefore accrued against a target a third smaller than the one they are now
  reported against.

- **Limitations / conflicting evidence:** The June 2025 release was read
  through a fetch extraction rather than raw text, and it now carries the
  report's opening paragraph, so it needs a direct read before publication.
  The Prime Minister's 9 June Tech Week speech has **not** been read and is a
  separate artefact from this 14 June DSIT release; the tracker says only "In
  June 2025", so what was said on stage is unestablished and it remains
  possible the explainer is describing that. **The coincidence between the
  10m/2035 usage projection and the later 10m/2030 target is noted and must
  not be presented as a finding** — there is no evidence connecting them, and
  implying one would be exactly the kind of inference this report criticises.

- **Effect on project direction:** Changes the UK-climate report's first two
  sentences, which currently attach the million-course figure to a target that
  did not exist while those courses accrued. The corrected sequence is both
  more accurate and a stronger construction, since every element is
  government-published and needs no characterisation.

### Entry 062 — The Prime Minister's speech, read: 7.5 million in his own words, and a budget misstated against the previous day's release

- **Date logged:** 2026-08-01

- **Priority / Question:** Priority 1 — closes the speech thread left open
  by Entry 061, and begins the evidence base for the
  policymaker-communications claim the creator reinstated (see
  `project_log.md` Entry 043).

- **Source:** `[PMLTW25]`, `[TECHFIRST25]`, cross-checked against
  `[AISKILLS-JUN25]`, `[AISKILLSBOOST26]`, `[AIOPP-DELIVERY26]`.

- **Checked date:** 2026-08-01

- **What the source directly supports:**

  - Speech, verbatim: "A partnership with 11 major companies to train 7.5
    million workers in AI by 2030."

  - Speech, verbatim: "That's a £185 million investment, embedding AI
    right through our education system, starting in our secondary
    schools." The press release announcing the same programme the
    previous day states "£187 million investment in national skills
    programme". The Prime Minister's published remarks misstate the
    budget of the programme they announce, against the government's own
    release of the day before.

  - TechFirst release, 8 June, verbatim: "7.5 million UK workers to gain
    essential AI skills by 2030 through industry partnership" — a third
    contemporaneous government statement of the 7.5 million target.

  - Further claims in the speech catalogued, none yet checked against a
    primary: "in 2023, our AI sector grew 30 times faster than the rest
    of the economy"; "This industry supports over 2 million jobs" (no
    source named); a "£1.5 billion" investment figure; and the Extract
    anecdote ("A hundred planning records per day, and the usual average
    up till now is five").

- **Inference drawn:** Entry 061's last caveat is closed. The explainer's
  claim that the 10-million target was "announced by the Prime Minister
  in June 2025 at London Tech Week" is contradicted by the Prime
  Minister's own published words — and now by three contemporaneous
  government sources. The documented sequence stands: 7.5 million
  announced June 2025, raised to 10 million in January 2026, the month
  the first progress figure appeared, with the department's explainer
  misattributing the target's origin. Separately, the £185m/£187m
  misstatement is small in magnitude but exact in kind: the flagship
  speech does not withstand checking against the government's own
  release of the previous day.

- **Limitations / conflicting evidence:** The speech was read via
  targeted extraction with verbatim passages captured, not end to end; a
  full read is still advisable before quoting it in print. A £2 million
  misstatement could be a drafting slip and on its own must not carry
  more weight than that — one confirmed error is a data point, not a
  pattern, which is why the four-claim verification catalogue matters
  more than this single confirmation. An initial search found no press
  fact-check of the speech to lean on either way.

- **Effect on project direction:** The reframed report's comprehension
  argument now has its evidential form: state the checkable record — a
  speech misstating its own announcement, an explainer misattributing
  its own target, productivity claims footnoted to unpublished
  interviews (Entry 051), estimates the plan itself called imprecise and
  outdated — and let the reader conclude. Completing the catalogue is
  the remaining work before any of it is published.

- **Second error confirmed, same day, after creator challenge.** The
  creator identified a further inaccuracy this entry had missed, and it
  is on the same gov.uk page. Verbatim: **"We put that plan out at the
  beginning of the year. We're really proud of it—50 recommendations,
  all of them accepted by the government."** Entry 057 established from
  Command Paper CP 1242 that 48 were agreed and 2 partially agreed —
  the copyright-cleared British media training dataset, and the
  immigration and visa recommendation. Partial agreement is not
  acceptance, so the statement is wrong, though only narrowly.

  Its value is not the magnitude but the attribution. The UK-climate
  report's §1 NOTE callout already records that "the widely repeated
  claim that all fifty were accepted is very nearly, but not exactly,
  right." That claim now has a named source: the Prime Minister, in the
  flagship speech, on a page gov.uk heads "Transcript of the speech,
  exactly as it was delivered." The report can stop calling it widely
  repeated and attribute it.

  **Two confirmed errors in one speech** — this and the £185m/£187m
  misstatement — moves the finding past what a single drafting slip
  supports, which is what the creator argued and what this entry
  originally under-read.

  **Method note, recorded because it caused the miss.** This source was
  extracted twice with scoped prompts (skills and figures the first
  time, Action Plan terms the second) and the first pass missed a claim
  sitting in plain text on the same page. A scoped extraction is a
  search, not a read, and must not be logged as though it were a read.
  The gov.uk page could not subsequently be reproduced in full — the
  fetch declined on copyright grounds — so a complete claim catalogue
  requires a human read of the page.

### Entry 063 — The full London Tech Week recording: gov.uk publishes the prepared half, and the unscripted half is where the Action Plan gets misdescribed

- **Date logged:** 2026-08-01

- **Priority / Question:** Priority 1 — resolves whether `[PMLTW25]` is the
  complete record, and continues the policymaker-communications catalogue
  opened in Entry 062.

- **Source:** `[PMLTW25-VIDEO]` — auto-generated transcript of the Sky News
  recording, supplied by the creator after YouTube blocked every
  programmatic route. Cross-checked against `[PMLTW25]`, `[AIOPP-PLAN25]`,
  `[AIOPP-RESP25]`, `[TECHFIRST25]`.

- **Checked date:** 2026-08-01

- **What the source directly supports:**

  - **The event has two halves, and gov.uk publishes one.** Prepared
    remarks run 0:00–18:49; a conversation between the Prime Minister,
    Jensen Huang of NVIDIA and a host runs 19:01–45:22. The gov.uk
    transcript, headed "exactly as it was delivered", corresponds to the
    prepared remarks. The creator's contention that the published page is
    not the whole speech is **correct**: roughly 26 of 45 minutes are
    absent from the official record.

  - **"50 recommendations, all of them accepted by the government"** at
    8:16, matching the gov.uk text word for word. This is the one claim in
    this entry independently confirmed against a published transcript and
    therefore safe to quote. Against `[AIOPP-RESP25]`: 48 agreed, 2
    partially agreed.

  - **The Action Plan described as the government's own work**, in the
    unscripted half at 35:24: "Almost everything we had in our action plan
    that we produced in January of this year was as a result of
    conversations with people in this room and beyond this room." At 8:16
    the same framing: "We put that plan out at the beginning of the year."
    Entry 051 established from the document itself that it is an
    independent report by Matt Clifford, written in the first person and
    explicitly not a statement of government policy.

  - **Further numeric claims, located and timestamped, none yet verified:**
    "over 2 million jobs" (6:11); "in 2023 our AI sector grew 30 times
    faster than the rest of the economy" (6:25); Liquidity's "£1.5 billion
    investment into our economy" (7:56); "an extra £1 billion of funding to
    scale up our compute power by a factor of 20" (8:41); Extract's "100
    planning records a day… the average up till now is five" (11:57); "up
    to 1 million young people" and "£185 million" (15:06–15:15); "we're in
    the top three in the world" (43:51).

  - **The compute figure needs reconciling.** The speech says "an extra £1
    billion"; the delivery tracker's Recommendation 1 entry (Entry 060)
    describes the UK Compute Roadmap as "backed by £2 billion". These may
    be consistent — different baselines, or one figure inside the other —
    but the relationship is unestablished and the report must not use
    either figure until it is.

  - **A vendor's claims delivered from the same platform, unchallenged.**
    Huang, whose company sells the hardware the compute announcement buys,
    states that the UK has "the third largest AI venture capital
    investment anywhere in the world" (32:13), that it is "the largest AI
    ecosystem in the world without its own infrastructure" (32:50), and
    that "in the last 10 years, AI has advanced 1 million times" (40:39).

- **Inference drawn:** The "all fifty accepted" error is not isolated
  phrasing. Across both halves the Prime Minister treats an independent
  adviser's commissioned report as a plan his government produced and then
  accepted — a construction that cannot be right in both directions, since
  a government does not accept its own plan. The distinction the
  UK-climate report spends a paragraph of §1 establishing is one the Prime
  Minister does not observe. That is a stronger and fairer finding than any
  single misstated figure, because it concerns what the plan *is* rather
  than a number that could be a briefing slip.

  Separately, the structure of the record matters in its own right: the
  unscripted half, where a speaker departs from the brief, is the half not
  published.

- **Limitations / conflicting evidence:** **This transcript is
  auto-generated and demonstrably unreliable at exactly the points this
  project cites** — it renders "in AI by 2030" as "in a by 2030", "extra £1
  billion" as "extra1 billion", the Prime Minister's name as "Kia" and
  President Zelensky as "Zalinski". Every timestamp above is a locator, not
  a quotation, and nothing here may be quoted without hearing it, per the
  protocol now in `CLAUDE.md`. The single exception is the 8:16 passage,
  which the gov.uk transcript independently corroborates.

  **"Our action plan" admits a weaker reading** — it may be loose speech
  for "the action plan of this government" rather than a claim of
  authorship, and it should be recorded as an observation supported by the
  8:16 error rather than asserted as a second error on its own.
  Huang's statements are a vendor's and carry that interest; they are noted
  as context for the concentration argument, not adopted as evidence.
  Publishing prepared remarks rather than a full event transcript is
  ordinary government practice and must not be characterised as
  concealment.

- **Effect on project direction:** Closes the completeness thread on
  `[PMLTW25]`. Gives the reframed report a second, better-grounded strand
  for its accountability argument, and sharpens §1: the report already
  distinguishes the adviser's plan from the government's response, and can
  now show that distinction being collapsed at the top. Seven claims remain
  to verify before the catalogue is publishable.

- **Audio verification completed for the two load-bearing passages,
  2026-08-01.** The creator listened to the recording and confirms that
  35:24 ("our action plan that we produced in January of this year") and
  15:15 ("£185 million") are said as the transcript renders them. Under the
  spoken-source protocol both are now quotable, cited to speaker, event,
  date and timestamp. The 8:16 passage was already corroborated by the
  gov.uk text. The remaining six timestamps stay unverified and unquotable,
  and are only worth verifying if the underlying claims fail fact-checking.

### Entry 064 — The January 2026 expansion, and the government AI estate: several criticisms already answered, and a fragmentation finding that is stronger than either

- **Date logged:** 2026-08-01

- **Priority / Question:** Priority 1/5 — tests the reframed argument
  (`project_log.md` Entry 042) against the current state of government
  provision, at the creator's direction.

- **Source:** `[AISKILLSBOOST-EXPAND26]`, `[AIPLAYBOOK25]`, `[IAI-GOV]`,
  `[AIKNOWLEDGEHUB]`; cross-checked against `[AIOPP-DELIVERY26]`,
  `[AISKILLS-JUN25]`, `[AIOPP-PLAN25]`.

- **Checked date:** 2026-08-01

- **What the sources directly support:**

  - **Universal eligibility is stated.** The 28 January 2026 expansion
    release: "Every adult in the UK is eligible to take free, newly
    benchmarked courses." The programme is not, on its own terms,
    restricted to industry professionals.

  - **The partner base is now 27, not 11**, and includes public bodies and
    SME representative organisations: the eleven founding companies plus
    the British Chambers of Commerce, Cisco, Cognizant, the CBI, the
    Department for Education, the Department for Work and Pensions, the
    Federation of Small Businesses, the Institute of Directors, the Local
    Government Association, Multiverse, the NHS and techUK, with Pax8,
    LinkedIn and PwC also named.

  - **SMEs are explicitly targeted**: "at least 2 million SME employees",
    consistent with the delivery tracker's Recommendation 19 entry.

  - **Benchmarking has a visible artefact.** A selection of courses is
    checked against Skills England's AI foundation skills for work
    benchmark, and completers receive "a virtual AI foundations badge".

  - **No measurement framework is stated.** The release describes no
    mechanism for tracking progress toward ten million beyond partner
    self-reporting, which its own footnote identifies as the source of the
    course figure.

  - **The target moves without being described as moving.** The release
    presents "a major expansion to upskill 10 million workers" against
    "one million courses since June". The 7.5 million figure appears only
    inside a partner's quoted statement, not as the previous government
    target being revised.

  - **The government AI estate is spread across at least three owners.**
    `ai.gov.uk` is the Incubator for AI, a Cabinet Office delivery unit
    building products (Extract, Consult, Lex, Minute, Medguard, Caddy, AI
    Classroom Tutors). `ai.gov.uk/knowledge-hub` is a public-sector
    practitioner resource, itself an i.AI project. `delivery.ai.gov.uk` is
    the DSIT and No.10 Data Science progress tracker. The AI Playbook is
    GDS/Cabinet Office guidance for civil servants. The AI Skills Hub is
    DSIT's public-facing platform. The Playbook additionally directs
    readers to Civil Service Learning, Government Campus AI courses, the
    Digital Excellence Programme, separate "AI insights articles", the
    Algorithmic Transparency Recording Standard hub, the Technology Code
    of Practice and the Service Standard — and situates itself against the
    Action Plan, the 2021 National AI Strategy, the 2024 Generative AI
    Framework and the 2023 pro-innovation white paper.

  - **The Playbook is explicit about audience and about uncertainty.** It
    is for "government departments and public sector organisations", and
    its preface states: "We didn't pretend to have all of the answers in
    such a fast-moving field." Its ten principles open with "You know what
    AI is and what its limitations are" and include "You have the skills
    and expertise needed to implement and use AI solutions". It notes "the
    current shortage of AI talent".

- **Inference drawn:** Three of the reframed argument's intended criticisms
  are weaker than the sketch assumed, and must be corrected before
  drafting. Eligibility is universal, not professional-only. SMEs are
  explicitly targeted and their representative bodies are now programme
  partners. A benchmark exists and has a learner-visible credential. A
  report attacking those points would be answered from a single press
  release.

  What survives is narrower and better evidenced: the count is still
  courses rather than people; it is still supplied by the delivering
  partners with no stated verification; only a selection of courses is
  benchmarked; and the target grew by a third in an announcement that does
  not present it as a change.

  **The stronger argument is the creator's own observation**, and it is
  new to this log: provision is not absent, it is scattered. A citizen or
  small employer looking for what government offers on AI faces at least
  eight distinct properties across DSIT, the Cabinet Office, GDS, i.AI and
  No.10, each with a different audience and none presenting the others.
  The Action Plan's Recommendation 45 asked for exactly one thing — "a
  single place to access frameworks and insights" — and that instinct has
  been delivered narrowly, for public-sector practitioners, while the
  wider estate has multiplied around it. This is a constructive criticism
  with an obvious remedy, which suits the reframed report better than an
  absence claim would.

- **Limitations / conflicting evidence:** All four sources were read
  through model-mediated extraction with comprehensive prompts, **not end
  to end**; per Entry 062's method note these are searches, not reads, and
  the Playbook in particular is long enough that a human read is needed
  before it is characterised in print. `gds.blog.gov.uk/category/ai` and
  the Public Sector Executive taskforce article were **not** read this
  pass. Whether Recommendation 45's single-hub commitment is met is a
  matter of scope, not fact: the Knowledge Hub does exist as a single
  place for its stated audience, so the report must argue fragmentation
  across the estate, not non-delivery of R45. The count of "at least
  eight properties" is this project's own enumeration and is not a
  published figure.

- **Effect on project direction:** Requires the reframed argument to drop
  or rewrite its eligibility, SME and benchmark-absence criticisms, and to
  lead instead on unverifiable counting, partial benchmarking, the moved
  target and fragmentation. Materially improves the report's fairness and
  its usefulness, since fragmentation is fixable and the remedy is cheap.

- **Refined 2026-08-01, and the refinement is better than what it
  replaces.** The creator's response to the above moves both criticisms
  from provision to composition: eligibility is not in question, *uptake*
  is — how many completions were self-initiated by members of the public
  rather than directed by an employer; and the SME target is not in
  question, *delivery against it* is — what proportion of the million
  reached small firms rather than large ones.

  Checked, and **neither is published.** DSIT withholds partner and
  course-level breakdowns as commercially sensitive (Entry 053); the "at
  least 2 million SME employees" figure is a target, not measured delivery
  (`[AISKILLSBOOST-EXPAND26]`); and no employer-directed versus
  self-initiated split appears anywhere in the published material. The
  two questions the creator asks are precisely the two the withheld
  breakdown would answer.

  This converts the planned Freedom of Information request from a
  supporting action into the load-bearing one, with six specific
  questions: (1) whether the figure is restricted to UK learners;
  (2) the internal — partner employees — versus external learner split;
  (3) the operational definition of "completed"; (4) what proportion of
  counted courses meets Skills England's benchmark; (5) any breakdown by
  employer size, against the 2-million SME commitment; and (6) whether
  completions are recorded as employer-directed or self-initiated. A "not
  held" answer to (5) or (6) is itself a finding: it would mean the
  department cannot know whether the programme is reaching the population
  its own target names.

  **Leads not yet followed**, both surfaced while checking this and both
  Advocacy/Commentary rather than primary: "The UK's AI strategy isn't
  built for small businesses" (thehumansintheloop.ai) and the LSE Impact
  blog's February 2026 piece on the programme as a course directory,
  which may overlap the existing `[LSE-CARDOSO26]` entry.

## Open threads

*Currently open questions only, grouped by `research_questions.md`
priority, so gaps are visible at a glance. **Resolution history is not
kept here** — when a thread closes it is deleted from this list, and the
dated entry that closed it is the record. Consolidated 2026-07-29
(`project_log.md` Entry 026) from a chronological resolved/still-open
log that had reached ~600 lines and stopped serving the purpose stated
in this sentence.*

**Standing constraint, not a thread:** no approach to any external party
— for comment, right of reply, FOI or funding — is made without the
creator's explicit per-approach instruction. The register of
possibilities is held in the project's internal working notes.

### Priority 1 — Problem and evidence

**Verification debt on the early evidence base**

- **The systematic re-check has never been run** (Entry 013). Entries
  001, 002, 006, 008, 010 and 012 have not been tested against
  disconfirming evidence or independent replication. Find UK-specific,
  non-commercial sources that corroborate or complicate them before the
  "capability gap" is treated as settled. Entry 041 did this for the SME
  adoption-depth gap only.

- **The 21%-of-adults figure could not be verified** (Entry 009) — the
  most likely Commons Library briefing was checked directly and does not
  contain it. Find the correct February 2026 briefing or drop the claim.

- **EY upskilling statistics** (Entry 008) are still only checked via a
  secondary blog; the primary EY report has not been located.

- **The 18%-of-workers-feel-skills-are-adequate figure is from 2021**
  and is used in a 2026 White Paper without a freshness caveat (Entry

  043) — find current data or do not repeat it as current.

**Unresolved conflicts and tensions**

- **Technical vs. literacy framing** (Entries 001/002, reframed by 012
  and 019). Entry 019 gives official backing to "practical literacy
  first, technical specialism for a smaller share," but traces back to
  the same Ameen research programme as Entries 010/012/017 rather than
  independent triangulation; Entry 012 measures a different axis
  (skill-category difficulty) than the original question. Needs explicit
  reconciliation — **Priority 3 is blocked behind it.**

- **Gap widening vs. declining** — Entry 002 (national, declining) and
  Entry 006 (London, widening) still disagree; not investigated further.

- **The replace-and-train finding** (Entry 029) — AI training investment
  is associated with *higher*, not lower, expected headcount reductions.
  This sits against the project's implicit assumption that building AI
  capability benefits the individual learner, and is a genuine tension
  for the responsible-use framing. Unaddressed.

- **The measurement-artifact question on the SME/large-firm gap** (Entry

  041) is genuinely mixed rather than resolved — one Fed source suggests
  a definitional survey change partly explains the widening, another
  finds a small-firm-exclusion choice changes little. Revisit only if
  this gap becomes foundational to the thesis.

**Evidence gaps**

- **No UK-specific evidence on unsafe or over-dependent AI use** — the
  only relevant data found (Entry 007) is a global survey with no UK
  breakdown.

### Priority 1 (continued) — The government programmes

**The Hub's own numbers remain unknown**

- **No independent evaluation of BridgeAI or the AI Skills Hub
  specifically** has been located (Entries 044/047). Entry 047 is
  genuine independent scrutiny but covers government's *internal* AI
  use, not these programmes. An NAO value-for-money study, a PAC session
  or a departmental evaluation would close this. Not searched for
  directly.

- **The Hub's usage and completion figures are unpublished** (Entry
  044). The FOI route is now named in a published document, so this
  should actually be done. The sharpened question set — definitions,
  third-party attribution and data-sharing, funnel numbers,
  accreditation, contract value — is held in the internal register.

- **Pin every figure to exact published wording before drafting any
  FOI** (Entry 049). The recalled "1 million delivered" claim is not
  located in any logged source; the figures this log holds are the 10m
  ambition (Entry 018) and BridgeAI's programme-wide 1,700+/126 (Entry
  044, with Entry 046's conflation warning still in force).

- **The Hub's accreditation and recognition claims are unread** (Entry
  049). The inference that a redirect portal adds no accreditation value
  of its own depends entirely on what the Hub actually promises. Verify
  before any external use.

- **Current-state re-verification of the Hub user journey** (Entry 049)
  — walk the signup-to-course path via the creator's logged-in session
  (the route Entry 045 fixed) with dated screenshots at each step,
  including the gov.uk guidance pages that funnel into it. This
  documents the *current* state; Entry 049 is testimony about the
  then-state, and the two must be labelled separately if they differ.
  Screenshots carry the creator's account identity and stay in internal
  working files until redacted.

- **Hub signup date corroboration** (Entry 049) — the creator's
  account-creation date would date the experience and evidence its
  before-the-project chronology.

**Right of reply — the largest standards gap**

- **No response has been sought** from Innovate UK, PwC, Digital
  Catapult or DSIT on the interest-concentration findings (Entries
  046/048). This is the single largest gap between the project's output
  and ordinary research-publication standards, and the published report
  states it as a limitation inside itself. Required *before*
  publication, never after.

**Unread and untraced primary material**

- **Three identified sources, none read** (Entry 045): the *first*
  Innovate UK White Paper (June 2025, the 96%-of-employers source),
  "Training and skills gaps for AI in four selected sectors" (8 July
  2026), and "BridgeAI three years on" (21 April 2026).

- **NAO as a source vein is unmined** — only the March 2024 *Use of
  artificial intelligence in government* report has been identified, and
  it has not been read directly.

- **The £400bn vs. £550bn figure lineage** is only partially
  disentangled (Entry 048), including a competing attribution to Google
  research.

- **PwC interest-concentration is identified but not quantified** (Entry

  043) — worth checking whether any non-PwC-sourced UK figures support
  the same skills-gap magnitude.

- **Date discrepancy on the second White Paper** — stated February 2026,
  posted July 2026, PDF path `/2026/07/` (Entry 045). Publication vs.
  posting is the likely explanation, unconfirmed.

**Editorial positions needing evidence or containment**

- **Policymakers' practical understanding** — upgraded to *partially
  evidenced with a scope caveat* (Entry 047): DSIT told the Committee
  that many public sector leaders lack sufficient technical expertise or
  training, which is not the same as those writing AI policy and setting
  budgets. The phrasing in `project_brief.md` still overstates what is
  evidenced. Confirm the current ministerial line-up before any
  positioning argument depends on it — the only sourced name this
  project holds is Kanishka Narayan MP (Entry 044).

- **Institutional-capacity and political-motive readings** (Entry 046,
  held in internal working notes) have no supporting evidence in this
  log at all. Either find direct evidence — policymaker quotes,
  select-committee transcripts, NAO commentary on departmental AI
  capability — or keep them confined to an explicitly editorial
  register.

- **"Outsourcing understanding" scope creep** — retracted for
  SME/integrator use (Entry 033), deliberately revived against
  government/consultancy (Entry 046). The *general* form of the claim
  remains unsupported and must not be reintroduced as a thesis;
  `[BUYBUILD-KLOTZ26]` remains uncitable. Watch for drift back toward
  the retracted version.

- **Instro-specific claims rest on thin sourcing** (Entry 031) — one
  trade-press article and Instro's own homepage. The underlying AMRC
  Cymru trial report has not been read directly, and the results come
  from a funded innovation trial rather than a typical paid engagement.

### Priority 2 — Audience and need

- **Priority 2's remaining sub-questions** are unresolved by the
  2026-07-24 working decision: the specific barriers and needs of the
  *combined* audience, and whether "small organisation employees" should
  later be split into narrower sub-groups.

- **Schools and universities as learner populations in their own right**
  remain uncovered — Entry 012 covers employment sectors and training
  provision, Entry 016 covers education-sector adoption. Low priority
  while the current audience decision stands; reopen if it changes.

### Priority 3 — Practical AI capability

- Blocked behind the technical-vs-literacy reconciliation under Priority
  1 above. No separate open items.

### Priority 4 — Learning design

- **`[AUTOBIAS-MED25]` is unverified** (Entry 028) — the medRxiv PDF
  returned HTTP 403, so the claim that AI-trained physicians still
  showed automation bias rests only on a search engine's synthesis of
  the abstract. Needs a direct read or an alternative access route.

- **`[TADIMALLA-MAHER25]` and `[SAIL4ALL25]` were read at abstract level
  only** (Entry 040, paywalled) — need full reads before being treated
  as more than suggestive, especially if the sequencing question becomes
  load-bearing.

- **Adult-learning pedagogy is unchecked** — andragogy and
  self-directed learning theory have not been tested against the
  Gradual Release of Responsibility model borrowed from K-12 practice
  (Entry 027), which flags this as an unexamined transfer assumption.

- **PRIMES assumes an organisational sponsor** (Entry 026) — paid
  learning time, workplace systems — which may not hold for an
  individual or small-org audience without a sponsoring employer.
  Adaptation vs. wholesale adoption is unreconciled, and this is the
  sharpest open sub-question under the Priority 2 working decision.

- **No UK-specific empirical comparison of "evaluation-first" vs.
  "foundations-first" short AI-literacy units** (Entry 040) — a genuine
  evidence gap, not merely an unread source.

- **The Claude-Code-as-illustrative-example connection** (Entry 034) is
  this project's own inference rather than sourced from the literature —
  worth a light validation pass before treating it as more than a
  teaching analogy.

- **When does bias/literacy training actually work?** Unresolved across
  Entries 028 and 050. `[KAMALI26]` found targeted training improved
  calibration; `[AUTOBIAS-MED25]` found trained physicians still showed
  automation bias; `[NIST-1270]` states flatly that awareness does not
  ensure control. The three are not strictly contradictory — they differ
  in domain, stakes and what was trained — but the project now teaches
  and applies bias material without having settled the boundary
  condition. The specific question: does the distinction lie in
  *awareness of a bias* vs. *practised judgement against ground truth*?
  Entry 028 already suspected this; Entry 050 sharpens it but adds no
  evidence either way.

- **`[NIST-1270]` disconfirming pair — judged not required** (creator
  decision, 2026-07-29, closing the debt Entry 050 flagged). NIST was
  read because it was named as an approved source rather than found
  through a balanced search, and Entry 050 logged the missing pair as
  outstanding. The decision: existing precedent for the practices it
  supports is strong enough without one, and the confirm/disconfirm rule
  is reserved for claims that would change project direction, which this
  does not. Recorded as a decision, not an open task.

- **A post-2023 source on human–LLM interaction is still wanted** (low
  priority, Entry 050). `[NIST-1270]` predates conversational AI
  assistants and addresses algorithmic decision systems, so it cannot
  speak to the usage pattern this project actually has. A source on
  working alongside an assistant would add something no
  decision-systems source can — worth picking up opportunistically
  rather than as a dedicated pass.

### Priority 5 — Comparable products and programmes

- **General learning platforms unchecked** — Codecademy, Khan Academy,
  freeCodeCamp and others implied by Priority 5's framing. roadmap.sh
  and LeetCode were prioritised because `research_questions.md` names
  them explicitly.

- **No comparable found that is simultaneously AI-literacy-specific,
  UK-based and aimed at general adults** rather than schools, the
  AI-sector workforce or one employment sector. Elements of AI is the
  closest match but is Finnish in origin. Worth a dedicated check if a
  general-public audience remains live.

### Priority 6 — Technical and conceptual scope

**The local AI workstation track is parked**, not dropped — a confirmed
future direction per the creator's decision of 2026-07-24. Do not resume
drafting until the creator reopens it. Its carried open items:

- **The local-AI cost side has no independent, academic or UK-specific
  source** (Entry 042) and remains directional-only, not citable with
  specific figures. The capability side is now anchored by Epoch AI's
  Capabilities Index.

- **A genuinely academic on-device cost/energy paper**
  (arXiv:2512.16531) was found but not read — a lead, not a finding.

- **The two tracks' relationship is unaddressed** — shared foundational
  modules if any, and whether the workstation track needs its own
  audience/barrier research the way Priority 2 was done for the
  general-literacy pilot.

- **The inherited workstation architecture reflects PAWH-era planning**
  and has never been checked against the current tool landscape or
  versions.

### Priorities 7–10 — Largely untouched

- **Priority 7 (delivery format)** — accessibility requirements,
  install-free access, and how Word/web/GitHub outputs should relate
  remain unaddressed. Deliberately deferred rather than researched ahead
  of need, since only the pilot unit's shape was required to unblock the
  build.

- **Priorities 8 (information and knowledge architecture), 9
  (evaluation) and 10 (sustainability and public presentation)** remain
  essentially untouched. Priority 9 — including how the pilot will
  actually be tested and assessed with real learners — becomes
  load-bearing as soon as the pilot unit is testable, which is the
  nearest of the three.

### External engagement and funding

Held in the internal register; the standing constraint at the top of
this section governs all of it.

- **Entity status is an unresolved gate**, not an administrative
  detail. Most innovation funding requires a registered UK entity (sole
  trader and CIC both qualify); most research fellowship funding
  requires an academic post. Neither currently applies. This carries
  tax, liability and governance consequences and needs proper external
  advice rather than project-internal reasoning.

- **The route that funded PRIMES is closed to the project as
  constituted** — the British Academy Policy-Led Innovation Fellowship
  requires a HEI/IRO post. Reachable only via academic partnership,
  which makes the academic contacts strategically relevant rather than
  only editorially useful.

- **The funding-route scan is a first pass, not a shortlist** — schemes
  open, close and change criteria, so every eligibility statement
  recorded needs re-checking at point of use. No published evaluation of
  the closed AI Upskilling Fund has been searched for yet.

### Production items tracked here for continuity

*Not research questions. These would sit better in `project_log.md` if
it ever grows its own open-items list.*

- **Icon stroke-width normalisation is not a closed audit** (Entry 014)
  — it covered five specific creator-approved fixes; the wider set of
  icons mixing stroke weights was reviewed and left as intentional
  hierarchy.

- **`hybrid_ai.svg` has no labelled groups** — it has none at all,
  having been hand-edited outside that pass. Revisit if it gains group
  structure worth labelling.

**Resolved this pass (2026-07-31, upstream policy read — Entries 051–055):**

- ~~The AI Opportunities Action Plan had never been read directly~~ — done
  (Entry 051). It is an adviser's report rather than government policy, and
  it states in its own words that the size of the skills gap was unknown.

- ~~The £400bn figure's attribution~~ — corrected (Entry 052). It traces to
  Public First's Google-commissioned research, not the Microsoft-commissioned
  report named in Entry 048.

- ~~No delivered-results figure for the programme carrying the
  10-million-worker target~~ — found (Entry 053): 1,001,147 courses,
  supplied by eleven commercial partners, no published breakdown.

- ~~Whether Recommendation 14 was ever delivered~~ — it was (Entry 054), and
  the project cannot claim the gap went unmeasured.

- ~~No independent, non-commercially-interested critique of the Hub~~ —
  partly resolved (Entry 055): FE Week and HOLEX have no stake in the
  AI-training market, unlike two of the three reviewers in Entries 022/025.

**Still open after this pass:**

- ~~The AI Labour Market Survey 2025's scope is unverified~~ — resolved
  (Entry 056). It does repeat the AI-sector scoping that Entry 001 had to be
  corrected for, so the general-workforce gap remains unmeasured and Entry
  051's finding survives in its stronger form.

- ~~`AI Skills for Life and Work: Rapid Evidence Review` unread~~ — read at
  section level (Entry 058). Its companion `Labour market and skills
  projections` and a third document, `Assessment of AI capabilities and the
  impact on the UK labour market`, both remain unread.

- **The OSR correspondence on The Skills Toolkit has not been read
  directly** (Entry 055) — the entire precedent argument currently rests on
  trade-press reporting of it.

- ~~The government's formal response to the Action Plan is unread~~ — read
  (Entry 057). The correct statement is **48 agreed, 2 partially agreed**,
  not "all 50 accepted".

- **Public First's Google-commissioned report is unread** (Entry 052), so
  the £400bn figure's method remains untraced even though its provenance is
  now settled.

- **Whether the 1,001,147 figure is UK-only is unknown** (Entry 053), and is
  now the sharpest FOI question alongside the internal/external learner
  split and the operational definition of "completed".

- **Matt Clifford's interest position** (Entry 051) is recorded as a
  one-sided observation with no disconfirming search run — not usable in
  external-facing work in its current state.

**Resolved this pass (2026-07-31, second research pass — Entries 056–058):**

- ~~The AI Labour Market Survey 2025's scope~~ — resolved (Entry 056), and it
  is the AI sector: 119 self-selected organisations, 3% response rate, half
  of them in Greater London. Entry 051's finding survives in its stronger
  form.

- ~~The government response to the Action Plan was unread~~ — read (Entry
  057). 48 recommendations agreed, 2 partially agreed. Recommendation 14's
  commitment was a Skills England assessment of "the country's skills need",
  due Spring 2025.

- ~~`AI Skills for Life and Work: Rapid Evidence Review` unread~~ — read at
  section level (Entry 058). It states in government's own commissioned
  words that UK focus has been on professional supply, and that evidence on
  AI skills for life is "necessarily limited".

**Still open after this pass:**

- **The June 2025 announcement needs a direct read** (Entry 061). It was read
  through a fetch extraction, and it now carries the report's opening
  paragraph — the 7.5 million target, the eleven named partners and the
  separate 10-million-by-2035 *usage* projection all rest on it.

- **Two of the five publications government names as delivering
  Recommendation 14 are unread** (Entry 060): *Skills for Growth and
  Opportunity* (June 2025) and *UK Standard Skills Classification*
  (November 2025).

- **No "Commitment Met" status has been independently verified** (Entry 060).
  The tracker is DSIT and Number 10 scoring their own plan and states no test
  for what the label requires. Its 38-of-50 headline should never be quoted
  without that attached.

- **The three 2021 FE Week Skills Toolkit articles have not been read in
  full** (Entry 059). The web-hits, geography and starts-not-completions
  claims rest on headlines and search-result summaries; the geography claim
  has no direct-read source at all and is the weakest thing now standing in
  the report's §4.

- **`AI Skills for Life and Work: Labour market and skills projections`**
  remains unread, as does `Assessment of AI capabilities and the impact on
  the UK labour market`.

- **Public First's Google-commissioned report is unread** (Entry 052), so the
  £400bn method remains untraced.

- **Whether the 1,001,147 figure is UK-only is unknown** (Entry 053) and
  remains the sharpest FOI question.

**Opened by the 2026-08-01 reframe (`project_log.md` Entry 042):**

- **Policymaker-communications error catalogue: in progress** (Entry 062).
  **Two confirmed:** "50 recommendations, all of them accepted by the
  government" against CP 1242's 48 agreed and 2 partially agreed; and
  the speech's "£185 million" against the previous day's release stating
  "£187 million". Separately the explainer's 10-million attribution is
  contradicted by three contemporaneous government sources. Still to
  verify against primaries: "AI sector grew 30 times faster than the
  rest of the economy" in 2023 (against the DSIT AI Sector Study); "over
  2 million jobs" (no source named in the speech); the "£1.5 billion"
  investment figure; and the Extract planning anecdote, "a hundred
  planning records per day, and the usual average up till now is five".
  The claim stays scoped to what the communications show, not to what
  ministers understand.

- **Seven London Tech Week claims need verifying before the catalogue is
  publishable** (Entry 063), each located with a timestamp: the 2-million
  jobs figure, the "30 times faster" AI sector growth claim for 2023, the
  £1.5bn Liquidity investment, the "extra £1 billion" compute figure and
  its relationship to the Compute Roadmap's £2 billion, the Extract
  planning productivity numbers, the £185m/£187m TechFirst discrepancy,
  and the "top three in the world" ranking. Under the spoken-source
  protocol none may be quoted until heard on the recording.

- **Audio verification: partially complete** (Entry 063). 35:24 and 15:15
  are confirmed by ear and quotable; 8:16 is corroborated by the gov.uk
  text. The remaining six timestamps rest on the auto-transcript alone and
  should only be verified if fact-checking shows the underlying claim is
  wrong.

- **Whether the AI Skills Hub's courses are pitched at the general public
  or at employees is unexamined**, and is answerable without an FOI. The
  creator holds an active Hub account (`project_brief.md`, "Research
  asset"), so the catalogue, entry requirements and framing can be
  inspected directly. This addresses the uptake question from the
  provision side while the FOI addresses it from the numbers side.

- **Partner-claimed totals are unverified** (Entry 053): Microsoft "more
  than 1.5 million", Google "1.2 million" — each exceeding the
  programme's own 1,001,147 total — were read via fetch summary only.
  Verify directly before the report uses "the partners' own claims exceed
  the programme total" or leans on the internal-training-inflation point.

- **"AI is increasingly embedded in everyday products, exposing people
  without their knowledge" needs a citable source.** The ONS-2023
  recognition figures (Entry 058) cover awareness, not embedding. Find a
  primary source for the embedding claim itself.

- **SME share of the business population needs an official cite** (DBT
  business population estimates or equivalent) if the reach argument
  quantifies who a corporate-centred delivery structure misses.

- **Regulator capability: in scope or out.** The reframe sketch touched
  "ill-equipped to independently educate and regulate"; the evidence base
  currently holds nothing on regulator capability. Either a research pass
  (the delivery tracker's R25–R28 entries are the lead) or an explicit
  exclusion from the reframed report.

### Entry 065 — OECD SME adoption paper read directly: figures confirmed, year and scope corrected

- **Date logged:** 2026-08-05

- **Priority / Question:** Priority 1/2 — the large/small adoption gap
  underpinning the product direction (`project_log.md` Entry 044) and
  now charted on the public landing site. Upgrades `[OECD-SMEAI25]`
  from search synthesis to a direct read, at the creator's direction
  that landing-site claims rest on read sources, not synthesis.

- **Source:** `[OECD-SMEAI25]`, pp. 1–12 read directly (cover through
  the adoption-gap section, including Figures 1 and 2 and their notes).

- **Checked date:** 2026-08-05

- **What the source directly supports:**

  - The headline figures as previously synthesised, verbatim: "across
    the OECD, while 40% of firms with 250 or more employees were using
    AI in 2024 (or in the most recent available year), only 20.4% of
    firms of between 50 to 249 employees and only 11.9% of firms with
    between 10 and 49 employees used AI." Firms with 10–49 employees
    "were less than one-third as likely to use AI" than large firms.

  - **The year is not uniformly 2024.** Figure 2's note lists latest
    available years by country — "2020 for Colombia, Israel, United
    Kingdom; 2021 for Japan, Switzerland, United States; 2022 for
    Australia, New Zealand; 2023 for Canada, Korea; 2024 for the
    remaining countries." The United Kingdom's data point in this
    dataset is therefore five years old.

  - **Scope:** enterprises with 10 or more employees only — micro
    firms are outside the data entirely; unweighted averages across
    member countries; "years and definitions may differ across
    countries." Underlying data is the OECD ICT Access and Usage by
    Businesses database, accessed July 2025.

  - SME depth of use, page 11: generative AI among micro firms and
    SMEs "is mostly used for peripheral rather than core tasks", and
    "Among SMEs using generative AI, only 29% report using it in their
    core activities", citing a representative OECD survey. The paper's
    case-study taxonomy (AI Novices relying on embedded tools, through
    to AI Champions embedding AI across operations) spans the full
    range. Noted 2026-08-05, same day as the original read: the landing
    site now cites the 29% figure.

  - Growth context: the share of firms using AI across OECD members
    rose from 5.6% (2020) to 14% (2024).

  - Document identity: an OECD discussion paper prepared at the
    request of Canada's 2025 G7 Presidency, published under the
    Secretary-General's responsibility, CC BY 4.0. A discussion paper
    informing the proposed G7 SME AI Adoption Blueprint, not an OECD
    statistical release.

- **Inference drawn:** None new — the size-gap finding stands as
  logged. The correction is to precision, not direction.

- **Limitations / conflicting evidence:** Pages 13–47 (taxonomy, case
  studies, enablers, policy chapters) were not read; nothing on the
  site rests on them. The UK's 2020 vintage in this dataset means the
  paper cannot say what the UK gap is now.

- **Effect on project direction:** The landing-site adoption figure's
  caption and caveat are corrected to "2024 or latest available year",
  with the 10+-employee scope and the UK's 2020 vintage stated
  (`tools/build_site_figures.py`). Source key upgraded. Any future use
  of these figures should carry the same qualifiers.
### Entry 066 — The change of Prime Minister, verified for the site's timeline; no course figure newer than January 2026 found

- **Date logged:** 2026-08-05

- **Priority / Question:** Priority 1 context — the institutional
  continuity of the skills promise, needed because the landing-site
  chart now marks the change of Prime Minister on its promise lane.

- **Source:** `[STARMER-RESIGN26]`; cross-checked against
  `[AIOPP-DELIVERY26]` and `[AISKILLSBOOST26]` for the target's
  continuity, plus a fresh search for any later completion figure.

- **Checked date:** 2026-08-05

- **What the sources directly support:**

  - Keir Starmer resigned as Prime Minister on 22 June 2026, with a
    Labour leadership contest following. Contemporaneous reporting
    named Andy Burnham as the likely successor.

  - The 10-million-by-2030 target predates the resignation (January
    2026 expansion) and its programme pages remain live. Nothing found
    retracts or revises the target.

  - A search for a course-completion figure newer than January 2026's
    1,001,147 found none; the January figure is the latest located,
    and the chart labels it "the latest figure published". This is a
    looked-and-not-found result, recorded as such — not an
    unfetchable source.

- **Inference drawn:** The promise has institutional continuity
  independent of the person who announced its first version. Usable on
  the site in exactly that factual form, with no motive attached.

- **Limitations / conflicting evidence:** Media sources, used for a
  single dated public fact; who holds office now was not needed for
  the chart and was not separately verified. The creator's own
  statement that the 10-million figure was said directly by the
  departing Prime Minister matches the department explainer's
  attribution, which Entry 061 found contradicted by the department's
  own tracker and by the speech itself; the chart therefore carries
  the documented sequence (7.5 million, June 2025; raised to 10
  million, January 2026), and the discrepancy was raised with the
  creator rather than silently resolved either way.

- **Effect on project direction:** The chart's promise lane carries
  the milestone "The Prime Minister leaves office (June 2026); the
  target stands." Source key gains `[STARMER-RESIGN26]`.
