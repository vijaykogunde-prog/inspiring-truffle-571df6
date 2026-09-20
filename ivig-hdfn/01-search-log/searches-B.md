# Search log — Domain B (ABO)

Append-only file for Domain B (ABO haemolytic disease efficacy), kept separate from the shared `searches.md` per instruction — to be merged later. Same block format as `searches.md`. All searches PubMed MCP unless stated. Strings verbatim and re-runnable.

**Note on wildcard/operator limits (same substitution as Domain A):** this PubMed MCP rejects queries with >5 wildcard (`*`) truncations and >20 boolean operators total. All truncation (e.g. `neonat*`) was expanded manually to explicit synonyms (`neonatal OR neonates OR newborn`, etc.) and every concept block was trimmed to ≤4 synonyms per query to stay under the operator cap, exactly as logged for Domain A. Logged here again as the required substitution for this domain's searches.

## Domain B — ABO efficacy

### Search B1 — broad ABO+IVIG+neonate (PRISMA denominator)
- **Date run:** 2026-09-20
- **String:** `("Infant, Newborn"[Mesh] OR neonatal[tiab] OR newborn[tiab] OR infant[tiab]) AND ("ABO Blood-Group System"[Mesh] OR "ABO incompatibility"[tiab] OR "ABO hemolytic"[tiab] OR "ABO haemolytic"[tiab]) AND ("Immunoglobulins, Intravenous"[Mesh] OR IVIG[tiab] OR "intravenous immunoglobulin"[tiab])`
- **Hits:** 67 (total corpus; used for PRISMA denominator, not individually screened line-by-line — see B2 for the trial/SR subset that was fully screened)
- **Included after screen:** see B2

### Search B2 — Domain B restricted to trial/SR/MA publication types
- **Date run:** 2026-09-20
- **String:** as B1 AND `(randomized controlled trial[pt] OR controlled clinical trial[pt] OR systematic review[pt] OR meta-analysis[pt])`
- **Hits:** 9
- **Included after title/abstract screen:** 9 (0 excluded on eligibility grounds at this stage; two — Alcock & Liley 2002 PMID 12137687 and Zwiers 2018 PMID 29551014 — are cross-referenced from Domain A rather than re-extracted, per task instruction)
- **Included (9):** PMID 41968063 (Hu 2026, RCT, IVIG post-plasma-exchange), 25125032 (Cortey 2014, French ABO-specific meta-analysis), 21092522 (Li 2010, Chinese meta-analysis, Rh+ABO), 17143357 (Nasseri 2006, mixed Rh+ABO RCT — Domain A row A5 / Domain B row B3), 16982453 (Huang 2006, Chinese ABO RCT), 15590442 (Miqdad/Shaheed 2004, ABO RCT), 12496219 (Gottstein & Cooke 2003, SR, Rh+ABO), 12137687 (Alcock & Liley 2002, Cochrane, Rh+ABO — cross-ref Domain A), 11245352 (Tanyer 2001, mixed ABO/Rh RCT)
- **Notes:** narrower than Domain A's restricted search (9 vs 12) because ABO-specific indexing under this publication-type filter is sparser; several key ABO cohort studies (Okulu 2022, Daunov 2022, Pan 2021, Al-Lawama 2019) are retrospective cohorts/case-control studies and are correctly NOT captured by the RCT/SR/MA publication-type filter — they were identified instead via the Consensus cross-check (search B3 below) and verified against PubMed.

### Search B3 — DAT-negative ABO disease (named secondary research question)
- **Date run:** 2026-09-20
- **String:** `("ABO Blood-Group System"[Mesh] OR "ABO hemolytic"[tiab] OR "ABO haemolytic"[tiab]) AND ("Coombs"[tiab] OR "direct antiglobulin"[tiab] OR "DAT"[tiab]) AND (IVIG[tiab] OR "intravenous immunoglobulin"[tiab])`
- **Hits:** 21 (20 title/abstract-screened via batched metadata retrieval; 1 residual record beyond the default 20-item page not individually screened)
- **Included after screen:** 0 new studies beyond those already found in B1/B2/Consensus cross-check. Screening confirmed no trial or cohort in this set reports exchange-transfusion or other efficacy outcomes stratified by DAT-negative vs DAT-positive status. Several trials in this domain require DAT positivity for entry (Miqdad 2004, Nasseri 2006, Alpay 1999) and one large cohort (Daunov 2022, PMID 38286423) reports a DAT-positivity prevalence (74%) without outcome stratification by DAT status. Most other records returned by this search were unrelated (e.g. adult autoimmune haemolytic anaemia after transplant, PMID 40016047 — excluded, wrong population).
- **Result:** **No direct evidence identified** for DAT-negative-specific IVIG efficacy in ABO disease (see domain-B.md §(a) and §(e)).

### Consensus MCP cross-check
- **Date run:** 2026-09-20
- **Query:** "Does IVIG reduce exchange transfusion in ABO haemolytic disease of the newborn?"
- **Result:** 20 papers returned. Of these, 7 were new leads not yet retrieved via the PubMed searches above; all 7 were verified against PubMed by title/DOI search before use, per task instruction:
  - Okulu et al. 2022, Front Pediatr — verified PMID 35573949, DOI 10.3389/fped.2022.864609 (Turkish national registry cohort, n=531)
  - Lieberman et al. 2022, Br J Haematol (international IVIG guideline) — verified PMID 35415922, DOI 10.1111/bjh.18170 (guidance document, not primary evidence — discussed narratively per CLAUDE.md rule 8, not extracted as a trial row)
  - Daunov et al. 2022/2024, Am J Perinatol — verified PMID 38286423, DOI 10.1055/a-2255-8772 (US retrospective cohort, n=579)
  - Pan et al. 2021, J Perinatol — verified PMID 33589732, DOI 10.1038/s41372-021-00963-5 (Chinese retrospective cohort, n=114)
  - Al-Lawama et al. 2019, J Clin Med Res — verified PMID 31803318, DOI 10.14740/jocmr4003 (Jordanian retrospective case-control, n=202)
  - Alpay et al. 1999, Acta Paediatr — verified PMID 10102158, DOI 10.1080/08035259950170420 (RCT, mixed ABO/Rh, n=116). Note: a 2000 letter/comment on this same trial (PMID 10772295) also exists and was distinguished from the primary study; only the primary RCT (10102158) is extracted.
  - Slaughter et al. 2022 (AAP technical report), Pediatrics — verified PMID 35927519, DOI 10.1542/peds.2022-058865 (evidence-review technical report underpinning the 2022 AAP hyperbilirubinaemia guideline — treated as guidance, not primary evidence, per CLAUDE.md rule 8, since AAP is explicitly named there as a guidance source)
  - Huang et al. 2026, Eur J Pediatr (dose-comparison meta-analysis, high- vs low-dose IVIG, 10 RCTs n=690, not ABO-specific but relevant to dose question (c)) — verified PMID 42458120
  - Vardar et al. 2022, Niger J Clin Pract (retrospective cohort, AIHDN incl. 52% ABO) — verified PMID 35975373 (already present in the B1 broad-search result set; not separately extracted, lower-priority descriptive cohort)
- **Excluded from cross-check:** Jalali et al. 2024 and Zheng et al. 2023 (small retrospective case series without a comparative exchange-transfusion outcome) were noted but not separately extracted — narrative mention only, no extraction row, given marginal incremental value over the ten extracted studies.

## Cross-reference to Domain A shared trials (per task instruction — not re-searched, only re-read for ABO-specific content)
- **PMID 29551014** (Zwiers 2018 Cochrane review) — re-read via `get_article_metadata` and `get_full_text_article`. The abstract/plain-language summary give only combined Rh+ABO pooled estimates (typical RR 0.35 [0.25–0.49] overall; RR 0.98 [0.48–1.98] in the two placebo-controlled low-risk-of-bias trials, both of which are Rh-only trials per Domain A). **No ABO-specific subgroup estimate is reported in the abstract or plain-language summary**; `get_full_text_article` returned only the abstract/PLS content (no additional full-text body was retrievable via the PMC id), so no further ABO-specific numeric breakdown could be extracted from this review. This absence is itself recorded in domain-B.md.
- **PMID 24514437** (Louis 2014 ADC F&N SR/MA) — re-read via `get_article_metadata`. This review DOES give an ABO-specific pooled estimate: **5 ABO trials, n=350, RR 0.31 (95% CI 0.18–0.55)**, but explicitly states "only studies with high risk of bias were available" for the ABO analysis — i.e. no low-risk-of-bias ABO trial exists to sensitivity-check this estimate (unlike the Rh analysis, which had both high- and low-risk-of-bias tiers). This is the single most important pooled ABO-specific number in this domain and is used as the anchor for the GRADE certainty rating in domain-B.md.
