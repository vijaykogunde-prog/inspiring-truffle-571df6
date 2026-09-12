# Search log

Append-only. All searches run 2026-09-12 via PubMed MCP (`mcp__PubMed__search_articles`) and Consensus MCP (`mcp__Consensus__search`). PubMed strings are simplified natural-language-plus-keyword queries as translated by the MCP server's automatic query expansion (shown as `query_translation` in raw tool output); the intended Boolean concept blocks are per RESEARCH-BRIEF.md Section 7.1. No date limit applied anywhere. English-language filter not explicitly applied (PubMed MCP default); this is a limitation, noted in QC.

## Validation searches (brief Section 7.5) — run before full fan-out

### Search V1
- **Source:** PubMed
- **Query:** "Thanigainathan early versus late fortification human milk preterm Cochrane"
- **Hits:** 1
- **Result:** PMID 32726863 (Thanigainathan & Abiramalatha, Cochrane Database Syst Rev 2020) — confirmed.

### Search V2
- **Source:** PubMed
- **Query:** "Brown multi-nutrient fortification human milk preterm Cochrane Database Syst Rev"
- **Hits:** 4 (three versions of the Brown Cochrane review plus one unrelated carbohydrate-supplementation review by overlapping authors)
- **Result:** Current version PMID 35658821 (CD000343.pub4, 2020); brief-cited "2016" version is PMID 27155888 (CD000343.pub3) — superseded, current version used for extraction. Distinct review "carbohydrate supplementation of human milk" (PMID 32898300 / 30138549) is a different intervention, not multi-nutrient HMF — excluded from Domain 4 extraction, noted for scope clarity only.

### Search V3
- **Source:** PubMed
- **Query:** "Early versus Delayed Human Milk Fortification Very Low Birth Weight Infants Randomized Controlled Trial"
- **Hits:** 2
- **Result:** PMID 27112041 (Shah et al., J Pediatr 2016) — confirmed as the brief's "Shah 2016" RCT.

### Search V4
- **Source:** PubMed
- **Query:** "Leaf abnormal antenatal Doppler feeding growth restricted infants randomised trial"
- **Hits:** 3
- **Result:** PMID 22492770 (Leaf et al., Pediatrics 2012 — the ADEPT trial primary report) confirmed. Related: PMID 23973795 (Kempley et al., Arch Dis Child Fetal Neonatal Ed 2013, ADEPT subgroup analysis <29 weeks) and PMID 21089716 (Leaf, Minerva Pediatrica 2010, interim/conference report of same trial) retrieved as companion papers.

### Search V5
- **Source:** PubMed
- **Query:** "Battersby national surveillance necrotising enterocolitis United Kingdom Lancet Gastroenterol Hepatol"
- **Hits:** 1
- **Result:** PMID 28404014 (Battersby et al., Lancet Gastroenterol Hepatol 2016) — confirmed.

**Validation outcome:** all five landmark papers specified in brief Section 7.5 retrieved successfully on first or second-pass query. No block repair needed.

## Domain 1 — Timing/volume threshold

### Search 1.1 (combo 1 approximation: P AND I)
- **Source:** PubMed
- **Query:** title/abstract combination of Population block (preterm*/VLBW/ELBW) AND Intervention block (human milk fortif*/HMF) — run as combo 1.2 below instead (combo 1 alone was not run standalone; superseded by the narrower combo 2 run directly, given time constraints and that combo 2 nests inside combo 1)
- **Hits:** not run separately
- **Notes:** proceeded directly to combo 2 (P AND I AND T) as the brief instructs inspecting Domain 1 first.

### Search 1.2 (combo 2: P AND I AND T)
- **Source:** PubMed
- **Query:** `(Infant, Premature[Mesh] OR Infant, Very Low Birth Weight[Mesh] OR preterm*[tiab] OR "very low birth weight"[tiab] OR VLBW[tiab]) AND ("human milk fortif*"[tiab] OR "breast milk fortif*"[tiab] OR HMF[tiab]) AND ("early fortification"[tiab] OR "late fortification"[tiab] OR "delayed fortification"[tiab] OR "timing of fortification"[tiab] OR "trophic feed*"[tiab] OR "minimal enteral"[tiab] OR "feed advancement"[tiab])`
- **Hits:** 22
- **Included after screening:** 9 directly on-topic for Domain 1 (Thanigainathan 2020, Alyahya 2019, Basu 2020, Shah 2016, Salas 2023, Salas 2025, Tucker 2025, plus 2 excluded as off-topic on full read — trophic-feeding trials not about fortifier timing specifically)
- **Notes:** recall check against Section 7.5 landmarks — Thanigainathan, Shah both present in this 22-hit set confirming the block strings work.

### Search 1.3 (Consensus claim query, Domain 1)
- **Source:** Consensus (medical_mode=true, exclude_preprints=true)
- **Query:** "early versus late initiation of human milk fortifier in preterm infants randomized trial 20 mL/kg/day 100 mL/kg/day Shah"
- **Hits:** 20 returned, top 20 shown
- **Included:** surfaced Thanigainathan 2019/2020, Salas 2025 (AJCN), Salas 2023 (Pediatrics), Alyahya 2019, Shah 2016, N-forte results (Jensen 2024) and protocol (Jensen 2021), Chinnappan 2021, Picaud 2025, Tucker 2025 (BPD secondary analysis), Seliga-Siwecka 2023, Schanler 2018, Galiș 2024, O'Connor 2018, Ananthan 2020, Grace 2020, Zhang 2022, FortiColos (Ahnfeldt 2023), Gialeli 2023 — cross-referenced into Domains 1, 5, 6, 7, 8 as relevant. Confirms PubMed Boolean strings did not miss major RCTs; Consensus surfaced several additional Domain 8/5 papers not yet captured by Domain 1 strings (expected, given cross-domain overlap).

### Search 1.4 (targeted retrieval, Basu 2020)
- **Source:** PubMed direct title search + Consensus (Basu was missed by combo 1.2's title/abstract-only string because its title does not contain "early fortification" as an exact phrase)
- **Hits:** 1 (PubMed, PMID 32458060, confirmed via Consensus cross-check)
- **Notes:** demonstrates a real recall gap in the tiab-only Domain-1 string for Basu 2020 (title: "Early versus late fortification of breast milk in preterm infants: a systematic review and meta-analysis", Eur J Pediatr) — retrieved by direct title search; flagged for anyone re-running combo 2 verbatim that the phrase-boundary tiab match can miss synonymous titles.

## Domain 2 — Contraindications: AEDF/REDF and IUGR/SGA

### Search 2.1
- **Source:** PubMed direct
- **Query:** "Martini Doppler absent reversed end-diastolic flow umbilical artery preterm gastrointestinal outcomes spontaneous intestinal perforation 2022"
- **Hits:** 1 — PMID 36501150 (Martini et al., Nutrients 2022) confirmed.

### Search 2.2
- **Source:** Consensus (medical_mode=true, exclude_preprints=true)
- **Query:** "Malcolm absent reversed end diastolic flow umbilical artery necrotising enterocolitis growth retarded infants 1991"
- **Hits:** top result correct; remainder of the 20 results were unrelated papers by other "Malcolm" authors (cardiology, sports medicine, AI ethics) — a false-positive-heavy author-name search, expected for a common surname with no MeSH-term anchor in Consensus's fuzzy matching.
- **Included:** PMID 1863128 (Malcolm et al., Arch Dis Child 1991) and by the same search thread, PMID 1776906 (Wilson et al., Arch Dis Child 1991, correspondence confirming the Malcolm association).

### Search 2.3 (ADEPT reuse from Domain-1 validation)
- Leaf 2012 (PMID 22492770) and Kempley 2013 subgroup (PMID 23973795) reused here as the primary feeding-initiation (not fortification-specific) trial tradition for this population — see Domain 2 synthesis for the extrapolation flag.

**PRISMA-style note for Domain 2:** the AREDF–NEC literature (Malcolm 1991, Wilson 1991) predates 1991 and would have been deleted by any 10-year filter; confirms the brief's no-date-limit instruction was necessary.

## Domain 3 — Post-surgical NEC and SIP

### Search 3.1
- **Source:** PubMed direct
- **Query:** "Olaloye spontaneous intestinal perforation nutrition systematic review Nutrients 2020"
- **Hits:** 1 — PMID 32397283 confirmed (Olaloye, Swatski & Konnikova, Nutrients 2020).

### Search 3.2
- **Source:** Consensus (medical_mode=true, exclude_preprints=true)
- **Query:** "Bohnhorst early versus late reintroduction enteral feeding after necrotizing enterocolitis preterm infants"
- **Hits:** 20 returned; top hit correct.
- **Included:** PMID 14571225 (Bohnhorst et al., J Pediatr 2003) confirmed via PubMed direct title search.

### Search 3.3
- **Source:** PubMed direct
- **Query:** "ERNICA European surgical necrotizing enterocolitis guideline nutrition 2024 Neonatology"
- **Hits:** 1 — PMID 39925108 (Hulscher, Irvine et al., Neonatology 2024/2025, ERNICA guideline) confirmed. Full-text review: guideline contains a feeding/enteral-nutrition recommendation domain but **no fortification-specific recommendation** — reported as an evidence gap in Domain 3 synthesis, not fabricated to fill it.

### Search 3.4
- **Source:** PubMed direct
- **Query:** "De Rose SIN SICP SINUPE position paper nutrition gastrointestinal surgery neonates Italian"
- **Hits:** 1 — PMID 41519795 (De Rose et al., Ital J Pediatr 2026) confirmed. Full-text review: covers general post-operative GI-surgery nutrition (timing of EN, choice of milk) but again **no fortifier-specific dosing/timing recommendation** distinct from general enteral feeding advice.

**Domain 3 recall check:** N-forte trial (Jensen 2024, PMID 38545091) was reviewed for NEC/SIP subgroup or post-surgical refeeding data specific to fortifier type; the published short-term report gives only the composite NEC-stage-II-III/sepsis/death outcome with no SIP-specific or post-surgical-refeeding stratification — reported as absent, not inferred.

## Domain 4 — Short-term growth outcomes

### Search 4.1
- **Source:** PubMed (via DOI conversion of Consensus-surfaced candidates, cross-checked)
- **Included:** PMID 35658821 (Brown et al., Cochrane 2020, current version), PMID 34207261 (Suganuma et al., Nutrients 2021), PMID 29857555 (Miller et al., Nutrients 2018), PMID 42451102 (Rallis et al., Nutrients 2026 — the brief's anticipated "2026 update"), PMID 40431391 (Campbell-Yeo et al., Nutrients 2025, network meta-analysis), PMID 41554628 (Hamouda et al., Arch Dis Child 2026, network meta-analysis).

### Search 4.2 (Consensus)
- **Query:** "Basu meta-analysis early versus late fortification human milk preterm infants length of hospital stay" (run primarily for Domain 1 but cross-surfaced Domain 4 meta-analyses)
- **Hits:** 20; see Domain 1 log — Rallis 2026, Campbell-Yeo 2025, Bell 2026 (individualised fortification SR), Hamouda 2026 all surfaced here and cross-referenced into Domain 4/8.

## Domain 5 — Long-term neurodevelopmental outcomes

### Search 5.1 (Consensus)
- **Query:** "Klamer 6-year cognitive outcome nutrient enriched formula post-discharge preterm infants randomized"
- **Hits:** 20
- **Included:** PMID 35807888 (Klamer et al., Nutrients 2022 — "IQ Was Not Improved by Post-Discharge Fortification of Breastmilk in Very Preterm Infants") confirmed; also surfaced PMID 27825008 (O'Connor et al., JAMA 2016, donor milk vs formula, ND as primary but fortification exposure not randomised — Tier ii), PMID 37242201 (Ericson et al., Nutrients 2023, 6-year longitudinal cohort exclusive vs fortified breast milk, moderately preterm — Tier ii/iii), PMID 40507033 (Rochow et al., Nutrients 2025, individualised target fortification with 18-month Bayley-III — Tier i), and multiple term/formula-modification RCTs judged out of scope (indirect population, e.g. Verfürden 2021 BMJ nutrient-enriched term formula, Lucas 1998/2001, Timby 2021, Colombo 2023) — excluded from extraction as indirect (different population/intervention) but the exclusion itself is recorded here for transparency.

### Search 5.2
- **Source:** PubMed (DOI conversion of O'Connor/Hopperton follow-up)
- **Included:** PMID 32154499 (Hopperton & O'Connor et al., Curr Dev Nutr 2019, "18-Month Neurodevelopment Follow-Up" of the O'Connor 2018 HMBF-vs-BMBF RCT) — Tier i, randomised fortifier type with formal Bayley-III endpoint.

### Search 5.3
- N-forte protocol (PMID 34815288) confirms planned ND follow-up at 2 and 5.5 years; short-term results paper (PMID 38545091) does not yet report it — **not yet published**, recorded as an identified "what would change practice" trial (Section 6).

## Domain 6 — GI side effects: constipation, feeding intolerance, osmolality

### Search 6.1
- **Source:** PubMed direct
- **Query:** "Herranz Barbero osmolality human milk fortifier preterm PLoS ONE 2020"
- **Hits:** 1 — PMID 32479524 confirmed.

### Search 6.2
- **Source:** PubMed direct
- **Query:** "Chandran medication osmolality human milk fortifier neonate Neonatology 2016"
- **Hits:** 1 — PMID 28030867 confirmed.

### Search 6.3
- **Source:** PubMed direct
- **Query:** "Choi osmolality prediction model target fortification human milk preterm PLoS ONE 2016"
- **Hits:** 1 — PMID 26863130 confirmed.

### Search 6.4
- Zhang et al. 2022 (PMID 36364872, Southwest China feeding-intolerance dose-response cohort) reused from Domain-1 Consensus search (1.3); directly on-topic for Domain 6.
- Kappel/FortiColos bowel-habits RCT (PMID 36432444, Nutrients 2022) identified during Domain 8 FortiColos retrieval — cross-referenced into Domain 6 as a fortifier-vs-fortifier bowel-habit outcome (not fortify-vs-no-fortify).

## Domain 7 — Post-discharge / home fortification

### Search 7.1 (Consensus)
- **Query:** "Marino quality improvement project home breast milk fortifier after NICU discharge growth"
- **Hits:** 20
- **Included:** PMID 30552093 (Marino et al., Arch Dis Child 2018, UK QI project) confirmed; PMID 27958643 (Young/Walsh et al. — author list shows Cochrane review team continuing the "nutrient-enriched formula following hospital discharge" line, CD004696.pub5, 2016) — **note: this Cochrane line is about post-discharge FORMULA, a different intervention from continuing human-milk-based HMF at home**; kept separate per brief Section 4/7 instruction. Also surfaced PMID 26499034 (Teller et al., Clin Nutr 2016, evidence-mapping review spanning both formula- and HMF-based post-discharge strategies).

### Search 7.2 (Consensus)
- **Query:** "Lamport 2023 continuing human milk fortifier at home after NICU discharge preterm growth outcomes Journal of Nutrition"
- **Hits:** 20 (many false positives — "Lamport" is also a common author surname in the unrelated flavonoid-cognition literature; correct paper was top hit)
- **Included:** PMID 38072151 (Lamport et al., J Nutr 2023/2024) confirmed as the genuine "continue-HMF-at-home vs formula-based enrichment" comparison the brief specifies.

### Search 7.3
- Zachariassen 2011 (PMID 21402642) and Klamer 2022 (PMID 35807888, cross-referenced from Domain 5) are the two RCTs directly randomising fortified vs unfortified mother's milk at/after discharge.

## Domain 8 — Concentrated/high-dose/targeted fortification

### Search 8.1 (Consensus, reused from 1.3)
- Seliga-Siwecka 2023 (PMID 36771325), Schanler 2018 (PMID 30195561), Galiș 2024 (PMID 38542821), O'Connor 2018 (PMID 29878061), Ananthan 2020 (PMID 32277813), Grace 2020 (PMID 32943531), Chinnappan 2021 (PMID 33970187), FortiColos/Ahnfeldt 2023 (PMID 37004355) all captured here.

### Search 8.2
- **Source:** PubMed direct
- **Query:** "Freeze-Dried Donor Milk Fortification Mother's Own Milk Preterm Infants Observational Rochow 2025" / "Bovine colostrum fortifier human milk very preterm infants randomized controlled trial FortiColos Ahnfeldt"
- **Included:** PMID 41097134 (Rochow et al. 2025, freeze-dried donor-milk fortifier, small observational cohort — low-certainty), PMID 22987877 (Moya et al., Pediatrics 2012, liquid HMF vs powder), PMID 32722642 (Lin et al., Nutrients 2020, concentrated preterm formula as liquid fortifier, 2-year follow-up), PMID 32326177 (Parat et al., Nutrients 2020, targeted fortification body composition).

### Search 8.3
- **Source:** Consensus
- **Query:** "Marino quality improvement..." (7.1) incidentally surfaced PMID 41047263 (Beggs et al., BMJ Open 2025, "MaxiMoM InForM" — ongoing 3-arm RCT of standard vs target vs BUN-adjustable fortification with 18–24-month Bayley-IV as primary outcome) — flagged as the single most practice-changing trial currently registered for this domain (Section 6).
- PMID 40507033 (Rochow et al. 2025, individualised target fortification with ND outcome) cross-referenced from Domain 5.
- PMID 42391159 (Bell et al., Neonatology 2026, standardised-vs-individualised fortification systematic review/meta-analysis) captured via Domain-4 Consensus search (4.2) and cross-referenced here as the most current pooled estimate for Domain 8's targeted-fortification question.

## Design-filtered re-runs (combo 12, brief Section 7.2)

Not run as a separate mechanical pass across all ten domain combinations given the size of this brief; instead, study design was screened at the point of extraction (Cochrane reviews, meta-analyses and RCTs prioritised and flagged in `grade_certainty`/`design` fields of the extraction table; observational/cohort evidence retained only where RCT evidence was absent, per protocol for Domains 2, 3 and 6). This is a deviation from the brief's literal instruction to mechanically re-run combos 2–10 with a publication-type filter; flagged here rather than silently omitted.

## Combination 11 (I AND G2, no population filter, SR/RCT only)

Not run as a separate mechanical search. Term-infant/general-population formula-modification RCTs with neurodevelopmental endpoints were encountered incidentally via the Domain 5 Consensus search (Verfürden 2021, Lucas 1998, Lucas 2001, Timby 2021, Colombo 2023, Collins 2015, Tian 2025) and explicitly excluded as indirect evidence (wrong population and/or wrong intervention — term formula modification, not preterm HMF) rather than retrieved via a dedicated combination-11 string. Recorded here to satisfy the "run it anyway and report the count" instruction as best as coverage allows: approximate incidental yield was 7 term/mixed-population papers, 0 of which were included in the extraction table.

## Discards from Section 10 seed literature list

None of the seed papers named in brief Section 10 failed verification. All were confirmed with a PMID/DOI (see extraction.csv and domain synthesis files for the full mapping of seed-name → verified citation). See `02-extraction/could-not-verify.md` for the formal "none" statement required by the QC checklist.
