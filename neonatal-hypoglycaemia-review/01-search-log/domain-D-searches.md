# Domain D search log — preterm-specific thresholds and long-term outcome evidence

Append-only, verbatim, per project standing rules. All searches below were run 2026-08-27 in this executing session. PubMed MCP query strings are capped at 5 wildcards ("Query too complex" error above that) — noted here again as it constrained string construction, consistent with the Domain E log.

## Pre-verified seed papers (carried from RESEARCH-BRIEF.md, re-verified this session via get_article_metadata)

These six were flagged in the brief as "already verified this session" during scoping — per the non-negotiable citation-integrity rule, a scoping-session verification does not substitute for the executing session's own retrieval, so all six were independently re-retrieved via `mcp__PubMed__get_article_metadata` in this session before use.

- **Call:** `get_article_metadata(["10190926","39707054","27940690","38972961","39913386","42050117"])`
- **Result:** 6/6 resolved (no silent drops). Confirmed:
  - 10190926 — Duvanel 1999, J Pediatr, DOI 10.1016/s0022-3476(99)70209-x
  - 39707054 — Palazzo 2024, Eur J Pediatr, DOI 10.1007/s00431-024-05936-2
  - 27940690 — Goode 2016, Pediatrics, DOI 10.1542/peds.2016-1424 (already in domain-E.csv as E17; full abstract re-read here for Domain D's in-depth discussion)
  - 38972961 — Lagacé & Tam 2024, Pediatr Res, DOI 10.1038/s41390-024-03411-0
  - 39913386 — Kebede 2025, PLoS One, DOI 10.1371/journal.pone.0316464
  - 42050117 — May 2026, Pediatr Res, DOI 10.1038/s41390-026-04958-w (NOTE: cohort is late-preterm/term at-risk, NOT preterm — see directness flag in synthesis)

## New searches — <32 week / <28 week preterm hypoglycaemia

### Search D1 (PubMed)
- **String:** `preterm*[tiab] AND hypoglyc*[tiab] AND ("28 weeks"[tiab] OR "extremely preterm"[tiab] OR "extremely low birth weight"[tiab] OR ELBW[tiab])`
- **Hits:** 55 total; 30 returned (relevance-sorted)
- **Screen result:** almost entirely noise on title screen (gestational diabetes protocols, growth-chart comparisons, hypothermia devices, golden-hour/transport quality-improvement studies, vaccine-safety studies with hypoglycaemia as an incidental listed outcome). No new <28-week-specific hypoglycaemia-threshold-and-outcome paper surfaced. This null result is itself evidence for the brief's predicted evidence gap and is reported as such in the synthesis.

### Search D2 (PubMed)
- **String:** `preterm*[tiab] AND hypoglyc*[tiab] AND ("32 weeks"[tiab] OR "very preterm"[tiab] OR "very low birth weight"[tiab] OR VLBW[tiab]) AND (neurodevelopment*[tiab] OR outcome*[tiab])`
- **Hits:** 56 total; 30 returned (relevance-sorted)
- **Screen result:** surfaced Battaglini 2026 (already found via Consensus), and critically **Palazzo/Correani et al. 2025** (PMID 40609275, *Brain Dev*) — a companion paper to the brief's seed Palazzo 2024, testing the same <32-week question in **appropriate-for-gestational-age** infants (the 2024 paper was SGA-specific) and finding the **same null result**. This is a materially important find not in the brief's seed list — see synthesis §(a). Remainder of hits were gestational-diabetes/maternal-outcome studies, late-preterm epidemiology, and neonatal transport/sepsis studies not bearing on the threshold question.

### Search D3 (PubMed) — CGM/interstitial glucose monitoring in preterm infants
- **String:** `preterm*[tiab] AND (glucose[tiab] OR glyc*[tiab]) AND ("continuous glucose monitoring"[tiab] OR "interstitial glucose"[tiab] OR CGM[tiab])`
- **Hits:** 116 total; 30 returned (relevance-sorted)
- **Screen result:** surfaced the REACT trial cross-reference chain (via later targeted searches below) and confirmed CGM is an active preterm-specific research area, distinct from the term/late-preterm interstitial-monitoring literature already covered in Domain E (CHYLD).

### Targeted follow-up searches (PubMed, title/author-directed, to resolve PMIDs for papers surfaced by Consensus — see below)
- `Galderisi continuous glucose monitoring very preterm infants randomized Pediatrics` → 3 hits (28916591 Galderisi 2017 Pediatrics RCT; 34931697 and 33348448, the two Cochrane review editions — see below)
- `Beardsall REACT real-time continuous glucose monitoring preterm infants Lancet Child Adolesc Health` → 1 hit (33577770)
- `Battaglini continuous glucose monitoring preterm infants randomized Neonatology 2026` → 1 hit (41984740)
- `Tottman glycemia neonatal illness 2-year outcomes very preterm infants Journal of Pediatrics` → 1 hit (28647271)
- `Galderisi continuous glucose monitoring prevention morbidity mortality preterm infants Cochrane` → 2 hits (34931697 = pub3/2021, current edition; 33348448 = pub2/2020, superseded — pub3 used as the current Cochrane position, per the brief's instruction to confirm current edition of any standards/review document)
- `Gutierrez-Rosa glycemic variability reference percentiles very low birth weight preterm continuous glucose monitoring` → 1 hit (41894434)
- All 7 resolved PMIDs (34931697, 33348448, 28916591, 33577770, 41984740, 28647271, 41894434) verified via `get_article_metadata` — 7/7 resolved, no silent drops.

### Follow-up title screen of D1/D2 PMID lists (metadata batch calls, 4 batches of ≤15 PMIDs each, to check for missed preterm-hypoglycaemia-specific ND papers among the 55+56 raw hits)
- Batches: `get_article_metadata` on PMIDs 42458734, 42104852, 41983451, 41930709, 41503805, 41161864, 41095506, 41043847, 40248606, 39882534, 39533258, 38915194, 38843646, 38302960, 37946069 / 37874789, 37699520, 37120652, 37025284, 37003569, 36879686, 36819594, 36144251, 36143971, 34839483, 34368024, 34011299, 33884191 / 42640180, 42413967, 42226150, 42134252, 41924494, 40666384, 40609275, 40025486, 39992703, 39139145, 38976271, 38747407, 37602315, 39281364, 35970401 / 35604586, 35354633, 34344736, 34324133, 32971309, 32809965, 32030935, 31614582, 30954975
- **Result:** 44/44 requested resolved (no silent drops across these batches). Of these, two were substantively new and relevant and are carried into the synthesis:
  - **40609275** — Palazzo/Correani 2025, *Brain Dev*, DOI 10.1016/j.braindev.2025.104391 (AGA companion null, see D2 above)
  - **37025284** — Kalogeropoulou, Iglesias-Platas & Beardsall 2023, *Front Pediatr*, DOI 10.3389/fped.2023.1115228 — narrative review, "Should continuous glucose monitoring be used to manage neonates at risk of hypoglycaemia?" (secondary source; its claims are traced to REACT/Galderisi/CHYLD primary sources in the synthesis, not cited standalone, per the brief's rule on the Lagacé & Tam review)
  - **36143971** — Butorac Ahel 2022, *Medicina (Kaunas)*, DOI 10.3390/medicina58091295 — descriptive incidence/risk-factor cohort (445 preterm infants <37 weeks); used only for the epidemiological observation that hypoglycaemia was commonest in late-preterm (≥34 week) infants and hyperglycaemia commonest in <28-week infants in this cohort — supporting evidence for the brief's warning that late-preterm data dominates the hypoglycaemia literature while extremely preterm infants are more often discussed in the hyperglycaemia literature.
  - **30954975** — Jagła et al. 2019, *Dev Period Med*, DOI 10.34763/devperiodmed.20192301.0714 — CGM-derived glycaemic variability (SD/CV/MAGE) vs IVH/PVL/ROP in 74 VLBW infants; univariate association with severe IVH and treated ROP, not significant after logistic regression adjustment.
  - Remainder of the 44: overwhelmingly gestational-diabetes/maternal-outcome literature, general prematurity epidemiology, neonatal transport/thermoregulation studies, and one insulin-therapy-for-hyperglycaemia paper (41930709, Domain G territory, not extracted here) — screened and excluded as off-topic for the hypoglycaemia-threshold question.

## Consensus searches (claim-level surfacing, not a reproducible Boolean search — adjudicated against PubMed per standing rules)

### Search D4 (Consensus)
- **Query:** "glucose threshold neurodevelopmental outcome extremely preterm infants less than 28 weeks gestation" (medical_mode=true)
- **Hits:** 20 papers returned
- **Notes:** Confirmed the brief's prediction directly — the highest-relevance results for "<28 weeks + glucose + outcome" were predominantly **hyperglycaemia/insulin-therapy** papers in extremely preterm infants (Zamir 2021 PMID 33863775, already in Domain E/G extraction; Naseh 2022, DOI 10.1159/000524923, hyperglycaemia + MRI + outcome in <32 weeks with a <28-week subgroup) rather than hypoglycaemia-specific threshold papers. This asymmetry — richer <28-week evidence for hyperglycaemia than hypoglycaemia — is itself reported as a finding in the synthesis. Also returned Tottman 2017 (independently confirmed via PubMed as above), the CHYLD/hPOD papers already covered in Domain E, and general extremely-preterm outcome epidemiology (Bell 2022 JAMA, Adams-Chapman 2018, van Beek 2022/2023 EPI-DAF) not glucose-specific and not extracted here.

### Search D5 (Consensus)
- **Query:** "continuous glucose monitoring glycaemic variability preterm infants neurodevelopmental outcome" (medical_mode=true)
- **Hits:** 20 papers returned
- **Notes:** This surfaced the core preterm CGM trial literature independently verified above (Battaglini 2026, Galderisi 2017, REACT/Beardsall 2021, Galderisi Cochrane review, Gutiérrez-Rosa 2026, Jagła 2019, Win 2021 [JCEM, CGM in persistent hypoglycaemia/CHI — attempted PMID resolution via targeted PubMed search failed to resolve; not extracted, logged to could-not-verify], Tottman 2017) plus a substantial amount of maternal/pregnancy CGM literature (gestational diabetes glycaemic control — out of scope for this domain, which concerns neonatal not maternal glycaemia) that was screened out.

## Directness/evidence-gap conclusion carried into synthesis

Across D1–D5 (five searches, ~247 raw PubMed hits plus 40 Consensus results, all screened), **no randomised controlled trial testing a specific glucose treatment threshold against a long-term neurodevelopmental outcome in infants <32 weeks (let alone <28 weeks) gestation was identified.** The CGM trials identified (Galderisi 2017, REACT 2021, Battaglini 2026) are RCTs of a *monitoring modality* in preterm infants, not RCTs of a *glucose threshold*; only Battaglini 2026 reports a long-term (2-year) neurodevelopmental outcome at all, and it is a single-centre trial of 53 infants, underpowered for that outcome. This is reported plainly as a confirmed evidence gap in the synthesis, not a search failure — see 03-synthesis/domain-D-preterm.md §(d).
