# Search Log — Antenatal Corticosteroid Evidence Synthesis

All searches run via the PubMed MCP connector (`mcp__PubMed__search_articles` / `get_article_metadata`), the Consensus MCP connector (`mcp__Consensus__search`), and web search/fetch for guideline grey literature. Log compiled 2026-08-26. Work was split between the lead session (Q0 premise check, guideline verification) and six parallel research subagents (Q1, Q2/Q6, Q3, Q4, Q5, Q7), each logging its own searches; their sub-logs are appended below as they report back.

## Lead session — Q0 premise check

| # | Tool | Query | Date run | Hits | Notes |
|---|---|---|---|---|---|
| 1 | WebSearch | RCOG Green-top Guideline 74 Antenatal Corticosteroids dexamethasone betamethasone dose regimen | 2026-08-26 | — | Surfaced RCOG GTG74 PubMed record and secondary summaries |
| 2 | PubMed get_article_metadata | PMID 35172391 (RCOG GTG74) | 2026-08-26 | 1 | Confirmed PMID/DOI; abstract not indexed for guideline |
| 3 | WebFetch | mastermrcog.com GTG74 PDF | 2026-08-26 | — | **Blocked by egress proxy** — could not retrieve full text this route |
| 4 | WebSearch | NICE NG25 preterm labour antenatal corticosteroids dexamethasone regimen | 2026-08-26 | — | Confirmed GA thresholds (24+0–33+6 offer; 34+0–35+6 consider), 2-course repeat limit |
| 5 | WebFetch | nice.org.uk/guidance/ng25/chapter/recommendations | 2026-08-26 | — | **Blocked by egress proxy** |
| 6 | WebFetch | ncbi.nlm.nih.gov/books/NBK585372 (WHO regimen chapter) | 2026-08-26 | — | **Blocked by egress proxy** — relied on WebSearch snippet instead |
| 7 | WebSearch | WHO recommendations antenatal corticosteroids preterm birth dexamethasone dose regimen 2022 | 2026-08-26 | — | Confirmed WHO 2022 preferred regimens |
| 8 | WebSearch | "dexamethasone" "12 mg" "24 hours apart" OR "6 mg" "12 hours apart" antenatal corticosteroid regimen Neonatal Formulary BNF | 2026-08-26 | — | Cross-confirmed ACOG/WHO regimen wording |
| 9 | WebSearch | Liggins Howie 1972 antenatal corticosteroid trial betamethasone dose regimen | 2026-08-26 | — | Confirmed original betamethasone phosphate+acetate 12 mg ×2, 24 h apart; also surfaced Khandelwal 2012 interval RCT and Jobe 2020 reappraisal paper |
| 10 | PubMed search_articles | Betamethasone dosing interval 12 or 24 hours apart randomized noninferiority | 2026-08-26 | 65 | Located candidate PMIDs |
| 11 | PubMed search_articles | Antenatal corticosteroids reappraisal drug formulation and dose | 2026-08-26 | 1 | PMID 33177675 (Jobe et al 2020) |
| 12 | PubMed search_articles | betamethasone dosing interval hours apart noninferiority open trial preterm | 2026-08-26 | 1 | PMID 22381601 (Khandelwal et al 2012) confirmed |
| 13 | PubMed get_article_metadata | PMID 33177675 | 2026-08-26 | 1 | Full abstract retrieved |
| 14 | PubMed get_article_metadata | PMID 22381601 | 2026-08-26 | 1 | Full abstract retrieved — RDS 36.5% vs 37.3%; NEC 6.2% vs 0%, P=.03 |
| 15 | PubMed search_articles | Betamethasone dosing interval 12 24 hours systematic review meta-analysis (2024–2026) | 2026-08-26 | 0 | No PubMed-indexed record found for the ScienceDirect 2025 title surfaced by web search — treated as **could not verify** unless the Q1 subagent locates it independently |
| 16 | PubMed search_articles | Antenatal corticosteroids accelerating fetal lung maturation women risk preterm birth Cochrane | 2026-08-26 | 14 | Located both Cochrane review PMIDs |
| 17 | PubMed get_article_metadata | PMID 35943347 (Williams 2022, regimen/agent comparison Cochrane review, CD006764.pub4) | 2026-08-26 | 1 | Full abstract retrieved — key source for Q0/Q1/Q4 |
| 18 | PubMed get_article_metadata | PMID 33368142 (McGoldrick 2020, ACS vs placebo Cochrane review, CD004454.pub4) | 2026-08-26 | 1 | Full abstract retrieved — key source for Q0/Q2/Q7 |
| 19 | PubMed get_article_metadata | PMID 28321847 (Roberts 2017, superseded version, CD004454.pub3) | 2026-08-26 | 1 | Retained only as historical/superseded comparator, not primary source |
| 20 | PubMed search_articles | ASTEROID trial betamethasone dexamethasone antenatal randomized | 2026-08-26 | 3 | PMIDs handed to Q4 subagent for full extraction |
| 21 | WebSearch | RCOG Green-top 74 "sulphite"/"sulfite" dexamethasone preparation UK | 2026-08-26 | — | Inconclusive via web search alone — handed to Q1 subagent |

**Access note:** the egress proxy blocked direct WebFetch of mastermrcog.com, nice.org.uk, and ncbi.nlm.nih.gov/books in this session. Guideline wording below is therefore reconstructed from WebSearch result snippets (which quote the source pages) plus PubMed-verified abstracts, not from directly fetched full guideline PDFs. Where a guideline quote could not be independently confirmed against primary text, it is flagged as such in the synthesis.

## Subagent search logs (Q1, Q2/Q6, Q3, Q4, Q5, Q7)

All six subagents completed and reported back on 2026-08-26. Each ran PubMed `search_articles`/`get_article_metadata` (and `get_full_text_article` where abstracts were ambiguous), 1–2 Consensus `search` calls per the tool's mandatory citation format, and WebSearch/WebFetch for guideline text. Aggregate tool usage across the six agents: 295 tool calls, ~1.01M subagent tokens. Every PMID/DOI pair reported by each agent was returned directly from a PubMed metadata lookup (not fabricated or inferred); each agent's report includes its own "could not verify" list, consolidated into the master synthesis document's final section.

**Access limitations (consistent across all six agents):** the network egress proxy blocked WebFetch to `rcog.org.uk`, `nice.org.uk`, `acog.org`, `publications.smfm.org`, `ncbi.nlm.nih.gov/books`, `medicines.org.uk`/`emc`, `mastermrcog.com`, `obgyn.onlinelibrary.wiley.com`, `researchgate.net`, and `web.archive.org` throughout this session. All guideline-society **wording** (as opposed to PubMed-indexed trial/review data) in the synthesis is therefore sourced from WebSearch result snippets, not directly fetched primary text, and is flagged as such at every point of use. This is the single most important caveat for whoever finalises the unit guideline: **re-verify every quoted RCOG/NICE/WHO/ACOG position against the primary document before publication.**

Representative search strings actually run (non-exhaustive; full detail lives in each agent's completion report, referenced in the synthesis document's inline citations):
- `Betamethasone dosing interval 12 24 hours randomized noninferiority` (Q1) — located Khandelwal 2012 (PMID 22381601), the only interval RCT identified for either agent.
- `(dexamethasone[tiab] AND (sulfite*[tiab] OR sulphite*[tiab])) AND (neonat*[tiab] OR neurotox*[tiab])` (Q1) — located Baud 2001 and Dani 2007 mouse/cell-culture studies.
- `ASTEROID trial betamethasone dexamethasone antenatal randomized` (Q4) — located the definitive head-to-head RCT and its secondary/follow-up publications.
- `WHO ACTION-I dexamethasone early preterm low-resource` (Q4) — located Oladapo 2020 NEJM and its administration-to-birth-interval secondary analysis (also used by Q2/Q6).
- `chorioamnionitis AND (antenatal corticosteroid* OR betamethasone OR dexamethasone)` (Q3) — located Been 2011 and Amiya 2016 meta-analyses plus individual cohort studies.
- `Liggins Howie 1972 antenatal betamethasone trial` / `MACS multiple courses antenatal corticosteroids` / `ACTORDS repeat doses antenatal corticosteroids` / `ALPS late preterm steroids NEJM` / `ASTECS betamethasone elective caesarean term` / `Räikkönen antenatal corticosteroid mental behavioural disorders Finland register` (Q7) — located and verified all six named landmark-trial threads plus their long-term follow-up publications.
- `betamethasone AND dexamethasone AND (mixed OR sequential OR switch) AND antenatal` (Q5) — returned zero results; confirmed absence of any mixed-agent-course literature.

Consensus searches run (per-agent, citation format followed per tool instructions): "Antenatal dexamethasone and betamethasone produce equivalent neonatal outcomes in preterm birth"; "Antenatal dexamethasone increases the risk of adverse neurodevelopmental outcome compared with betamethasone"; "Shorter dosing intervals for antenatal corticosteroids reduce effectiveness"; "Antenatal corticosteroids are beneficial when chorioamnionitis is present"; "Antenatal corticosteroid exposure in infants ultimately born at term is associated with adverse neurodevelopmental outcomes"; "Repeat courses of antenatal corticosteroids reduce fetal growth"; plus two additional agent-formulated queries on treatment-to-delivery interval and mixed-course pharmacology. Results and citations are reproduced in full within each agent's section of `acs-evidence-synthesis.md`'s source material (condensed into the narrative and reference list; full Consensus citation blocks are preserved in the task-completion transcripts if needed for audit).
