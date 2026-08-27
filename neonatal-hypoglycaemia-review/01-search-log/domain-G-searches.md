# Domain G search log — Hyperglycaemia and long-term follow-up

All searches run this session (2026-08-27) via the PubMed MCP (`mcp__bb264603-1ec4-441c-aeec-65f23266cfca__search_articles` / `get_article_metadata`) and web search. Verbatim queries, translations where PubMed rewrote them, and hit counts below. Tool note: the PubMed MCP rejects queries with >5 wildcards ("Query too complex") — one query below failed for this reason and was re-run with fewer wildcards.

## 1. Verification of pre-identified seed papers (task-supplied PMIDs, re-verified this session)

`get_article_metadata` batch — PMIDs: 38972961, 33863775, 34199741, 32005719, 37316160.
**Result: 5/5 resolved, 0 dropped.** All five confirmed with full abstract text, correct authors, journal, year, DOI:
- 38972961 — Lagacé & Tam 2024, *Pediatr Res*, DOI 10.1038/s41390-024-03411-0. Confirmed: hypoglycaemia ≤47 mg/dL, hyperglycaemia >150–180 mg/dL operational definitions; "U-shaped" dysglycaemia–outcome relationship; glycaemic lability flagged as key factor. Review, no independent primary data.
- 33863775 — Zamir et al. 2021, *Arch Dis Child Fetal Neonatal Ed*, DOI 10.1136/archdischild-2020-319926, PMC8394751. Confirmed EXPRESS cohort, 533 infants <27 weeks, 436 assessed at 6.5y; FSIQ −0.33 pts/day (95% CI 0.03–0.62) per day of hyperglycaemia >8 mmol/L; MABC-2 adjusted mean difference −4.90 (95% CI −8.90 to −0.89) for ≥3 consecutive days >8 mmol/L; −0.55 pts/day (95% CI 0.17–0.93) for MABC-2; insulin treatment not associated with outcomes.
- 34199741 — Boscarino et al. 2021, *Nutrients*, DOI 10.3390/nu13061930, PMC8227040. Confirmed n=108 (32 exposed/76 unexposed), GA<32wk or BW<1500g, PN-related hyperglycaemia (>180 mg/dL) week 1, 24-month Bayley-III; cognitive delay 44% vs 22% (p=0.024), motor delay 38% vs 8% (p<0.001); hyperglycaemia remained a risk factor for motor delay after adjustment.
- 32005719 — Ramel & Rao 2020, *NeoReviews*, DOI 10.1542/neo.21-2-e89. Confirmed narrative review, <28-week epidemiology, GIR-vs-insulin management tension, explicitly states "limited data" on long-term neurodevelopmental/cardiovascular/metabolic effects and calls for RCTs with long-term follow-up. No independent primary data.
- 37316160 — Puzone et al. 2023, *Arch Dis Child Fetal Neonatal Ed*, DOI 10.1136/archdischild-2023-325592. Confirmed SR/MA, PROSPERO CRD42022368870, 12 studies; hyperglycaemia in NE: 7 studies/807 infants, OR 3.07 (95% CI 2.17–4.35, p<0.00001) for death/neurodisability ≥18 months; hypoglycaemia in NE: 6 studies/685 infants, OR 2.17 (95% CI 1.46–3.25, p=0.0001) — reported here for completeness though hypoglycaemia-in-NE is not this domain's focus.

## 2. New PubMed searches

| # | Query (verbatim) | Hits (returned/total) | Notes |
|---|---|---|---|
| 1 | `("infant, newborn"[Mesh] OR neonat*[tiab] OR newborn*[tiab]) AND ("hyperglycemia"[Mesh] OR hyperglycaemia*[tiab] OR hyperglycemia*[tiab]) AND ("child development"[Mesh] OR neurodevelopment*[tiab] OR "long-term outcome*"[tiab] OR "long term outcome*"[tiab])` | **FAILED — "Query too complex: too many wildcards (max: 5)", 7 wildcards used** | Re-run as query 1b below |
| 1b | `("infant, newborn"[Mesh] OR neonat*[tiab]) AND ("hyperglycemia"[Mesh] OR hyperglycaemia*[tiab] OR hyperglycemia*[tiab]) AND ("child development"[Mesh] OR neurodevelopment*[tiab] OR "long-term outcome"[tiab])` | 30/154 | Term+preterm combined (Mesh "infant, newborn" is broad); scanned top 30 — dominated by hits already captured (Zamir, Boscarino, Lagacé/Tam) plus case reports/ROP/metabolic-programming tangents not independently extracted |
| 2 | `("infant, premature"[Mesh] OR preterm*[tiab] OR "extremely preterm"[tiab] OR ELBW[tiab] OR "extremely low birth weight"[tiab]) AND ("hyperglycemia"[Mesh] OR hyperglycaemia*[tiab] OR hyperglycemia*[tiab]) AND (neurodevelopment*[tiab] OR "long-term outcome*"[tiab] OR "child development"[Mesh])` | 30/94 | Preterm-specific hyperglycaemia+ND; surfaced Boscarino, Zamir, Ramel/Rao already known — screened remainder, no additional independent primary RCT/cohort beyond those separately retrieved below |
| 3 | `insulin therapy preterm neonatal hyperglycemia randomized controlled trial` | 20/26 | Surfaced Beardsall 2008 NEJM (PMID 18971490, "NIRTURE" trial) via follow-up author search below |
| 4 | `"COIN trial" OR "continuous insulin infusion" neonatal hyperglycemia preterm` | 5/5 | **No genuine "COIN trial" exists in the literature** — all 5 hits are false positives matching "continuous insulin infusion" as free text (obstetric CSII pump papers, a French practice survey, a 1988 case series). See §4 below — the brief's "COIN trial" is almost certainly a mis-recollection of the **NIRTURE trial** (Beardsall et al. 2008, NEJM). |
| 5 | `Beardsall insulin therapy very low birth weight infants hyperglycemia` | 8/8 | Retrieved NIRTURE pilot and related Beardsall papers |
| 6 | `Beardsall early insulin therapy very low birth weight infants NEJM` | 1/1 | PMID 18971490 — the landmark early-insulin RCT |
| 7 | `van der Lugt hyperglycemia very preterm infants outcome retrospective follow-up` | 1/1 | PMID 20646308 — key preterm-specific hyperglycaemia+2-year outcome cohort |
| 8 | `hyperglycaemia newborn infant physiology versus pathology review` | 1/1 | PMID 19536671 — screened, off-topic (animal programming review), not used |
| 9 | `continuous glucose monitoring glycaemic variability preterm infant neurodevelopmental outcome` | 1/1 | PMID 41702956 — 2026 CGM/neurobehaviour paper, used |
| 10 | `NIRTURE trial 2 year outcome insulin very low birth weight infants Ahluwalia Dunger` | 0/0 | No published long-term neurodevelopmental follow-up of the NIRTURE cohort found — the trial was stopped early on safety grounds (see §4); flagged as an evidence gap |
| 11 | `hyperglycemia retinopathy of prematurity extremely preterm infants glucose` | 8/8 | Screened for ROP/morbidity signal; PMID 41897099 used as short-term morbidity corroboration |
| 12 | `"glycemic variability" OR "glucose variability" neonatal preterm hyperglycemia outcome` | 5/5 | Core search for the glycaemic-lability question — retrieved Tottman 2017, Jagła 2019, Galderisi 2017 RCT, Battaglini 2026 RCT |

## 3. get_article_metadata batches (new, non-seed)

- `["18971490","20646308","19536671","41702956"]` — 4/4 resolved, 0 dropped.
- `["41984740","38527606","30954975","28916591","28647271"]` — 5/5 resolved, 0 dropped.
- `["41897099"]` — 1/1 resolved.

## 4. Grey literature / web search (labelled separately, never merged into peer-reviewed count)

- `BAPM NICE neonatal hyperglycaemia definition threshold guidance` — web search.
- `bapm.org hyperglycaemia framework preterm insulin glucose infusion` — web search.
- `NICE neonatal hyperglycaemia guideline threshold mmol/L preterm` — web search.
- `"BAPM" hyperglycaemia framework preterm infant 2024` — web search.
- `site:bapm.org hyperglycaemia` — web search.
- `"COIN trial" neonatal insulin glucose infant` — web search, confirmed no trial by this name exists; the real trial matching the brief's description (early insulin therapy for preterm/VLBW hyperglycaemia, multicentre RCT) is **NIRTURE** ("Neonatal Insulin Replacement Therapy in Europe" — Beardsall et al. 2008, *N Engl J Med*, PMID 18971490, DOI 10.1056/NEJMoa0803725).

**Findings, stated plainly:**
- **No BAPM Framework for Practice exists for neonatal hyperglycaemia.** BAPM's only glycaemia-related Framework document, in every version located (including the January 2024 update, hosted at bapm.org and identified via its S3 asset URL), is titled "Identification and Management of Neonatal Hypoglycaemia in the Full Term Infant (Birth–72 hours)" — hyperglycaemia is not addressed. This is a confirmed absence, not a search failure, and is reported as such.
- **No NICE guideline sets a hyperglycaemia threshold for neonates.** NICE NG3 (diabetes in pregnancy) addresses maternal glycaemic control and its neonatal hypoglycaemia risk consequence, not a neonatal hyperglycaemia treatment threshold. No NICE-branded hyperglycaemia cut-off was found.
- The only operational cut-off with any claim to consensus/expert status is the Lagacé & Tam 2024 proposal of >150–180 mg/dL (>8.3–10.0 mmol/L), itself synthesised from prior literature rather than issued as guidance by a body. Individual unit/regional guidelines located in web search (e.g., NHS Greater Glasgow & Clyde "Hyperglycemia in the neonate", Waikato/pre-hPOD-adjacent literature) use figures in the 8–10 mmol/L (144–180 mg/dL) range for treatment consideration, consistent with but not identical to Lagacé & Tam's range — treated as local practice variation, not national guidance.

## 5. Consensus-style claim checks

Consensus/Semantic-Scholar-style tool was not separately queried in this session (PubMed MCP + WebSearch covered the domain adequately per the above); the equivalent claim-checking function was performed by the targeted PubMed searches above (search #12 in particular functioning as the "does glycaemic variability predict outcome" claim check).
