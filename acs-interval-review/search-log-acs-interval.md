# Search Log — Antenatal Dexamethasone Dosing Interval Review

Compiled 2026-08-27. Lead session covered Q1 (premise/regimen verification) directly; five parallel research subagents covered Q2 (pharmacokinetics), Q3 (clinical interval evidence), Q4 (imminent-delivery scenario), Q5 (maternal hyperglycaemia/adrenal suppression), and Q6 (long-term neurodevelopmental outcomes). All PubMed lookups used the PubMed MCP connector (`search_articles` / `get_article_metadata` / `get_full_text_article` / `find_related_articles`); Consensus-style searches used the academic search connector; guideline text used WebSearch/WebFetch.

## Lead session — Q1 premise and regimen verification

| # | Tool | Query / target | Date | Result |
|---|---|---|---|---|
| 1 | WebSearch | BNF dexamethasone antenatal corticosteroid preterm labour dose "12 mg" OR "6 mg" injection | 2026-08-27 | Confirmed WHO/ACOG-referenced standard = 4x6mg 12h apart; RCOG alternative = betamethasone 2x12mg 24h apart |
| 2 | WebSearch | dexamethasone sodium phosphate injection SPC EMC "preterm labour" dose interval antenatal | 2026-08-27 | medicines.org.uk not directly reachable; secondary sources confirm 6mg q12h x4 as WHO ACTION-I protocol regimen |
| 3 | PubMed get_article_metadata | PMID 37442247 (Chawanpaiboon 2023, 5mg vs 6mg dexamethasone dose-comparison RCT) | 2026-08-27 | Verified: compares per-dose AMOUNT (5mg vs 6mg), both given 12-hourly x4 — confirms 12-hourly x4 as the standard comparator regimen in a recent (2023) RCT, but does NOT address the interval question (12h vs 24h) directly |
| 4 | WebFetch | medicines.org.uk/emc search | 2026-08-27 | **Blocked by network egress proxy** |
| 5 | WebFetch | nice.org.uk/guidance/ng25/chapter/recommendations | 2026-08-27 | **Blocked by network egress proxy** |
| 6 | WebSearch | "Neonatal Formulary" dexamethasone antenatal "6 mg" OR "12 mg" maternal dose interval | 2026-08-27 | No direct Neonatal Formulary text retrievable; corroborates 6mg q12h x4 as standard regimen from secondary sources |

**Carried forward from the prior evidence synthesis session (2026-08-26), independently PubMed-verified at that time and re-used here without re-verification since the underlying facts are unchanged:**
- RCOG Green-top Guideline No. 74 (Stock SJ et al 2022, PMID 35172391, DOI 10.1111/1471-0528.17027) — regimen table confirmed via WebSearch snippet of the guideline text.
- WHO ACTION-I trial (Oladapo OT et al 2020, PMID 33095526, DOI 10.1056/NEJMoa2022398) — regimen confirmed via PubMed abstract: dexamethasone 6mg IM q12h, maximum 4 doses.
- ASTEROID trial (Crowther CA et al 2019, PMID 31523039, DOI 10.1016/S2352-4642(19)30292-5) — regimen and 2-year outcome data confirmed via PubMed abstract in prior session; re-verified in this session's Q6 subagent for exact figure precision.
- Williams MJ et al 2022 Cochrane review (PMID 35943347, DOI 10.1002/14651858.CD006764.pub4) — full abstract retrieved via get_article_metadata in prior session, confirming the "three regimen-comparison studies" finding (including 12h-vs-24h betamethasone) and very-low certainty rating.

**Access limitation carried forward:** the network egress proxy in this environment blocks direct WebFetch to medicines.org.uk (EMC/SPC), nice.org.uk, rcog.org.uk, and ncbi.nlm.nih.gov/books. All guideline **wording** in this synthesis is therefore reconstructed from WebSearch result snippets and previously-verified PubMed abstracts, not directly fetched primary PDFs/SPC text. This is flagged at every point of use and listed in the "could not verify" section.

## Subagent search logs (Q2–Q6)

*Appended below as each subagent completes — see their full search strategies reflected in the citations and "could not verify" notes within `acs-interval-synthesis.md`.*
