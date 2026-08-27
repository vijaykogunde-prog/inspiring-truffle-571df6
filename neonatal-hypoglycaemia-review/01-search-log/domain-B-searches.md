# Domain B — Point-of-care glucometer vs laboratory/blood gas confirmation

Append one block per search, as it runs. Strings must be verbatim and re-runnable. Format matches the Domain E section of `01-search-log/searches.md`.

## Screening of prior-session candidate PMIDs (not yet screened)

### Screen S1 (PubMed get_article_metadata — verification/screening batch)
- **Source:** PubMed (mcp PubMed get_article_metadata)
- **Date run:** 2026-08-27
- **PMIDs screened (from RESEARCH-BRIEF.md §10, "further targeted PubMed search... not yet read or metadata-confirmed"):** 42493372, 40818947, 39206021, 37248091, 30829013, 29895035, 20574734, 9566281, 9325505
- **Result:** 9/9 resolved (no silent drops in this batch).
- **Disposition after title/abstract screen:**
  - **Included (6):** 42493372 (Sundar 2026, Clin Ther — 4 glucometers vs CLSI POCT12-A3/ISO/UNICEF); 40818947 (Bond 2025, BMC Pediatr — simulated neonatal blood, hematocrit 18–55%, low-resource); 37248091 (Sheen 2023, Clin Ther — Contour Plus/Plus One neonates + critically ill adults, ISO 15197:2013); 29895035 (Glasgow 2018, Neonatology — cost analysis enzymatic vs non-enzymatic cot-side screening, NZ); 20574734 (Roth-Kleiner 2010, Eur J Pediatr — 3 POCT systems vs hexokinase reference, none met ISO 15197); 9566281 (Schlebusch 1998, Pediatr Pathol Lab Med — 4 portable analysers, hematocrit/temperature/oxygen effects).
  - **Excluded, relevance (3):** 39206021 (Ayadi 2024, Womens Health Rep — glucometer comparison in adult diabetic patients admitted to a maternity centre, not neonatal glucose testing); 30829013 (Jin 2018, J Zhejiang Univ Sci B — glucometer-based β-glucosidase assay for NEC diagnosis, unrelated analyte/purpose); 9325505 (Moses 1997, Aust NZ J Obstet Gynaecol — home meter accuracy in the pregnancy glucose range, population is pregnant women, not neonates). Not entered into extraction.csv or synthesis; not citation failures (all 3 verified as real, retrievable records), so not logged to could-not-verify.md — excluded on relevance only.

## Fresh searches per RESEARCH-BRIEF.md §7 combos #3 and #4

### Search B1 (PubMed, combo #3 — POC glucometer accuracy, term)
- **Source:** PubMed (mcp PubMed search_articles)
- **Date run:** 2026-08-27
- **String:** `(neonat*[tiab] OR newborn*[tiab]) AND hypoglyc*[tiab] AND (glucometer*[tiab] OR "point of care"[tiab] OR "reagent strip*"[tiab] OR "blood gas"[tiab])`
- **Note on query construction:** 5 wildcards, within this PubMed MCP's 5-wildcard cap (see Domain E log for the constraint). Sort: relevance.
- **Hits:** 141 total; 40 returned (max_results cap).
- **Screened:** top 20 of 40 fetched via get_article_metadata (see Screen B1 below); remainder not individually fetched (diminishing relevance beyond top 20, consistent with relevance sort).

### Search B2 (PubMed, combo #4 — POC glucometer accuracy, preterm)
- **Source:** PubMed (mcp PubMed search_articles)
- **Date run:** 2026-08-27
- **String:** `(preterm*[tiab] OR premature*[tiab]) AND hypoglyc*[tiab] AND (glucometer*[tiab] OR "point of care"[tiab] OR "capillary glucose"[tiab])`
- **Hits:** 34 total; 34 returned (below cap). Sort: relevance.
- **Screened:** top 20 of 34 fetched via get_article_metadata (see Screen B2 below); tail 12 fetched in a second batch to confirm no further Domain-B-relevant items were missed (result: tail batch was Domain D/G-relevant — hyperglycaemia/CGM/insulin — or non-neonatal diabetes-in-pregnancy material, not Domain B).

### Search B3 (PubMed, supplementary — POC testing MeSH + accuracy/validation)
- **Source:** PubMed (mcp PubMed search_articles)
- **Date run:** 2026-08-27
- **String:** `"point-of-care testing"[Mesh] AND neonat*[tiab] AND glucose[tiab] AND (accura*[tiab] OR valid*[tiab])`
- **Hits:** 8 total; 8 returned.
- **Screened:** all 8 fetched via get_article_metadata.

### Search B4 (Consensus, claim-level check)
- **Source:** Consensus (mcp Consensus search)
- **Date run:** 2026-08-27
- **String (natural-language query):** "Are point-of-care glucose meters accurate at low glucose concentrations in neonates?" (medical_mode=true, no other filters)
- **Hits:** 20 papers returned.
- **Notes:** Surfaced the key modern systematic review (St Clair et al. 2024, *J Pediatr*, 71 studies, PROSPERO CRD42023488539) not returned in the top-40 of Search B1, plus several device-specific accuracy studies (Dietzen 2013, Kitsommart 2013, Demers 1999, Innanen 1997, Warner 2011) and two CGM-in-preterm systematic reviews (Nava 2020, Bonet 2024). All titles subsequently re-resolved to PMID+DOI via targeted PubMed title searches and independently verified via get_article_metadata — Consensus abstracts/paraphrases not taken as final wording for any transcribed number; PubMed-sourced abstracts used throughout.

## Verification batches (PubMed get_article_metadata) — screening the search hits and resolving Consensus-surfaced titles to PMIDs

### Screen B1 (metadata batch, term search top 20)
- **PMIDs requested:** 20301489, 24783355, 30819340, 39045480, 39539783, 32946820, 31804789, 36718904, 39382930, 31844395, 15922680, 31587009, 30385513, 39558467, 38107727, 34849508, 42387304, 32518926, 32028531, 34974442
- **Returned:** 18/20 — **20301489 and 31804789 silently dropped** (re-attempted individually, both returned "no articles found"; logged to `05-references/could-not-verify-domain-B.md`).
- **Included after screen (relevant to Domain B):** 24783355 (Lang & Hussain 2014, Adv Clin Chem, review — "analytical limitations of point-of-care testing instruments at low glucose concentration continue to persist"); 30819340 (Rozance & Wolfsdorf 2019, Pediatr Clin North Am, review); 39045480 (Shaw et al. 2023, Paediatr Child Health, commentary "Challenges with point of care glucose measurements for management of hypoglycemia in neonates"); 39539783 (Shaw et al. 2024, Paediatr Child Health, "Precision of point of care glucose metre measurements in the context of neonatal hypoglycemia"); 31844395 (Narvey & Marks 2019, Paediatr Child Health — Canadian Paediatric Society statement, grey lit, non-UK comparator); 15922680 (Deshpande & Ward Platt 2005, Semin Fetal Neonatal Med — UK authors, "most point-of-care technologies are... unsuitable for use in neonates"); 42387304 (Hamama et al. 2026, J Pediatr Endocrinol Metab — **erratum**; original article resolved separately, see below).
- **Excluded, relevance:** 32946820 (MiTy metformin-in-pregnancy RCT — no neonatal POC glucose accuracy content), 36718904 (adrenal crisis case report, Norwegian), 39382930 (single IDM hypoglycaemia case report), 31587009 (neonatal hyperkalaemia case report), 30385513 (Harris/Weston/Harding 2018 — POC blood **ketone** measurement, not glucose; tangential, not used), 39558467 (equine/veterinary — foals, not human), 38107727 (GDM India perspective review, no neonatal POC content), 34849508 (posterior urethral valve case report), 32518926 (CSF glucose via glucometer for meningitis diagnosis — different clinical question), 32028531 (neonatal polycythaemia vs hypoglycaemia association — uses a POC device incidentally, not an accuracy study), 34974442 (DOL2 screening incidence study — Domain A/C relevant, not device accuracy).

### Screen B2 (metadata batch, preterm search top 20 + supplementary MeSH batch)
- **PMIDs requested (preterm top 20):** 39761054, 41511771, 34974442 (dup), 36969114, 28832100, 22791467, 31929210, 40818947 (dup), 26388895, 41820921, 35170173, 25177612, 33945304, 32637004, 37864354, 40695483, 34723449, 36962972, 40022493, 33588801, 28916591, 23612555
- **PMIDs requested (Search B3 MeSH batch, 5 of 8 not already covered):** 38591468, 40448557, 41419656, 26457784, 29173326
- **Included after screen (relevant to Domain B):** 22791467 (Beardsall et al. 2012, Arch Dis Child Fetal Neonatal Ed — CGM sensor validation in the NIRTURE-trial VLBW cohort); 26388895 (Hwang et al. 2015, Korean J Pediatr — 3 glucometers vs lab in preterm/LBW infants); 25177612 (Reddy et al. 2014, J Clin Diagn Res — B Braun glucometer & HemoCue 201+ vs centralised NICU testing); 37864354 (Brooks et al. 2023, J Diabetes Sci Technol — arterial BGM reliable, capillary BGM "warrants caution" for hypoglycaemia in preterm/ill neonates); 40022493 (Kuboi et al. 2025, Ann Clin Biochem, Shikoku Neonatal Medical Research Group — multicentre POC meter vs blood gas analyser across all gestational ages, n=2943 measurements/285 infants); 28916591 (Galderisi et al. 2017, Pediatrics — CGM-guided glucose titration RCT, very preterm; Domain D-primary but accuracy-adjacent); 23612555 (Tendl et al. 2013, Clin Chem Lab Med — StatStrip two-site NICU evaluation, unaffected by haematocrit/pH); 38591468 (Koyano et al. 2024, Ann Clin Biochem — device modification improves accuracy in early neonatal period); 40448557 (Goodman et al. 2025, J Diabetes Sci Technol — multicentre CobasPulse evaluation including neonatal arterial/heel-stick samples); 41419656 (Parikh et al. 2025, J Perinatol — POC systematically underestimated glucose vs central lab by 2.3 mg/dL in NICU inborn infants); 26457784 (Luukkonen et al. 2016, Clin Chem Lab Med — epoc hand-held blood gas analyser evaluation, general ICU, included for blood-gas-analyser-as-comparator context).
- **Excluded, relevance:** 39761054/41511771/28832100/33588801 (antenatal diabetes RCTs, no neonatal POC device content), 36969114 (breastfeeding + hypoglycaemia, no device accuracy), 31929210 (Nigerian hyperglycaemia admission study — Domain G), 41820921/35170173/33945304/32637004 (maternal glycaemic control / perioperative glucose solutions / insulin-glucose relationship — not device accuracy), 40695483 (burden of repeat heel-pricks — practical/pain outcome, not accuracy), 36962972 (hypothermia clinical decision support tool), 29173326 (capillary blood **ketone**, not glucose, for breast-milk-intake adequacy).
- **Tail batch (remaining 12 of the 34 preterm hits, fetched to confirm no further Domain-B items missed):** 41145727, 27462585, 41630786, 31529717, 30232094, 40003276, 40576801, 41588396, 41087081, 21631748, 30134937, 24741538 — all screened; **none met Domain B inclusion** (all are Domain A/D/G material: hyperglycaemia epidemiology, CGM-in-preterm efficacy/feasibility studies not focused on device accuracy per se, cord-blood insulin/glucagon physiology, antenatal diabetes management, general-movements/hypoglycaemia correlation, nursing/midwifery management review). One exception noted for completeness but not extracted: 30232094 (Thomson/Beardsall 2018, Arch Dis Child Fetal Neonatal Ed, Cambridge UK — CGM pilot accuracy vs POC, mean bias −0.27 mmol/L) is UK-based CGM-accuracy-adjacent and is mentioned narratively in the synthesis (d) as supporting context, not as a separately extracted row.

### Title-resolution batch (Consensus-surfaced papers → PMID/DOI via PubMed search_articles, then get_article_metadata)
- **Resolved and verified (PMID, DOI confirmed this session):**
  - 39675663 — St Clair et al. 2024, J Pediatr, 10.1016/j.jpeds.2024.114438 (systematic review + meta-analysis, 71 studies, PROSPERO CRD42023488539) — **the key modern SR for this domain**
  - 23931714 — Dietzen et al. 2013, Diabetes Technol Ther, 10.1089/dia.2013.0160
  - 23644649 — Kitsommart et al. 2013, Eur J Pediatr, 10.1007/s00431-013-2019-2
  - 22317986 — Ngerncham et al. 2011, Indian Pediatr, 10.1007/s13312-012-0133-2 (companion/related group to Kitsommart; defines POC confirmation range 39–63 mg/dL, 2.2–3.5 mmol/L)
  - 9003866 — Innanen et al. 1997, J Pediatr, 10.1016/s0022-3476(97)70326-3
  - 39579867 — Bonet et al. 2024, J Pediatr, 10.1016/j.jpeds.2024.114416 (CGM accuracy, very preterm)
  - 33361084 — Nava et al. 2020, BMJ Open, 10.1136/bmjopen-2020-045335 (CGM accuracy SR+MA, preterm; PROSPERO CRD42020152248)
  - 21175272 — Warner et al. 2011, Diabetes Technol Ther, 10.1089/dia.2010.0129
  - 10471670 — Demers & Smith 1999, Clin Chem, [letter, no DOI resolved by PubMed record]
  - 36734399 — Tran et al. 2023, Crit Rev Clin Lab Sci, 10.1080/10408363.2023.2170316
  - 40859885 — Grzych et al. 2025, Crit Rev Clin Lab Sci, 10.1080/10408363.2025.2533855
  - 42137950 — Hamama et al. 2026, J Pediatr Endocrinol Metab, 10.1515/jpem-2025-0736 (original article; 42387304 is its erratum, same authors/journal)
  - 24124969 — Krouwer 2013, J Diabetes Sci Technol, 10.1177/193229681300700532 ("The new glucose standard POCT12-A3 misses the mark" — critique of CLSI POCT12-A3)
  - 29903743 — Levene & Wilkinson 2018, Arch Dis Child Educ Pract Ed, 10.1136/archdischild-2017-314050 (peer-reviewed synopsis of the BAPM 2017 Framework)
- **Notes:** `get_article_metadata` again silently dropped 2/20 PMIDs from one batch (see Screen B1) — consistent with the Domain E log's finding that mixed valid/invalid batches drop invalid PMIDs without a per-PMID error; every requested PMID was checked off against the returned set.

## Grey literature (web search, not PubMed — labelled separately, never merged into peer-reviewed count)

### Search B5 (WebSearch — CLSI POCT12-A3 current edition)
- **Date run:** 2026-08-27
- **Query:** `CLSI POCT12-A3 point-of-care glucose testing standard current edition status 2024 2025`
- **Finding:** POCT12-A3 is the **Third Edition** (published 2013), **reaffirmed September 2018**. No newer edition identified as of this search (2026) — the standard is now 13 years old at its original text and 8 years past its last reaffirmation. A contemporaneous critique (Krouwer 2013, PMID 24124969) argues the standard's accuracy-tier structure leaves ~2% of results with no specified performance limit at all.
- **Source:** ANSI/CLSI webstore listing (webstore.ansi.org/standards/clsi/clsipoct12a3); clsi.org/shop/standards/poct12/.

### Search B6 (WebSearch — BAPM framework wording on POC vs lab confirmation)
- **Date run:** 2026-08-27
- **Query:** `BAPM framework neonatal hypoglycaemia point of care glucose laboratory confirmation threshold` and `"BAPM" hypoglycaemia framework "near patient testing" OR "point of care" glucometer "2.6mmol" OR "blood gas" confirmation full term infant 2017`
- **Finding:** BAPM Framework (Oct 2017, and per a follow-up search a **2024 revision** titled "Identification and Management of Neonatal Hypoglycaemia in the Full Term Infant (Birth – 72 hours) 2024" appears to supersede it — flagged for the parent session/Domain A and C authors to confirm and reconcile, since this affects the currency of the guidance cited across domains): "Near patient testing devices tend to be less accurate in the lower range, especially <2.0mmol/l, and therefore all low values (≤2.6mmol/L) require confirmation using blood gas analysis as this is considered the gold standard for measuring blood glucose." Also: handheld glucometers "should meet ISO standards (ISO15197:2013) and have CE marking." Screening protocol: capillary POC testing immediately pre-feed, 3-hourly.
- **Source:** bapm.org resource pages (direct WebFetch blocked by this session's egress proxy; content obtained via WebSearch result snippets, cross-checked across two independent queries returning consistent wording) and a Scottish NHS (GGC) clinical guideline explicitly citing the BAPM Framework with matching wording.
- **Status:** Grey literature — BAPM guidance, not peer-reviewed primary evidence. Not entered into extraction.csv; cited narratively in synthesis (a)/(c) as guidance, clearly labelled.

### Search B7 (WebSearch — UK MHRA point-of-care glucose meter guidance)
- **Date run:** 2026-08-27
- **Query:** `MHRA point of care blood glucose meters neonates safety guidance UK` and a follow-up query for the specific gov.uk PDF
- **Finding:** MHRA "Point of care testing – Blood glucose meters" (advice for healthcare professionals; document identified via gov.uk/assets.publishing.service.gov.uk, direct PDF fetch blocked by this session's egress proxy, content obtained via WebSearch snippets): glucose meters are "unreliable in the detection of hypoglycaemia in neonates, but are accurate for values above 3 mmol/l. Laboratory blood glucose estimation should be used for screening of neonatal hypoglycaemia until a more reliable technique becomes available." Staff must perform a laboratory venous-sample measurement when contraindications are suspected or results are abnormal/unexpected.
- **Status:** Grey literature — MHRA device-safety guidance, not peer-reviewed. Not entered into extraction.csv; cited narratively, clearly labelled. **Note the internal UK tension this creates**: MHRA's stated accuracy cut-off (reliable only >3 mmol/L / 54 mg/dL) is more conservative than BAPM's operative confirmation threshold (≤2.6 mmol/L / 47 mg/dL) — flagged explicitly in synthesis (d).

## Egress note

Direct WebFetch of bapm.org and assets.publishing.service.gov.uk was blocked by this session's network egress proxy (`EGRESS_BLOCKED`) on two attempts each. All grey-literature wording above was obtained via WebSearch result snippets (which quote source text directly) rather than full-document WebFetch, and cross-checked across independent queries for consistency. This is a genuine limitation on this session's ability to verify grey-literature wording against the full source document — flagged rather than silently worked around.
