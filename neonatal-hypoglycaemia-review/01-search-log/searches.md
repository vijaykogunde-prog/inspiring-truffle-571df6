# Search log

Append one block per search, as it runs. Strings must be verbatim and re-runnable.

## Domain E — term/late-preterm neurodevelopmental outcomes (calibration domain, run first)

### Search E1 (PubMed, calibration test against brief §7.3 seed set)
- **Source:** PubMed (mcp__PubMed__search_articles)
- **Date run:** 2026-08-27
- **String:** `(neonat*[tiab] OR newborn*[tiab]) AND hypoglyc*[tiab] AND (neurodevelopment*[tiab] OR "cognitive outcome"[tiab] OR "long-term outcome"[tiab] OR "school age"[tiab])`
- **Note on query construction:** original brief block (§7.1 combo #6, `#1 AND #3 AND #5`) used 8 wildcards and was rejected by this PubMed MCP with "Query too complex: too many wildcards (max: 5)" — simplified to the string above (4 wildcards) to fit the server's limit. This constraint is not documented in the brief and should be carried forward into all subsequent domain searches.
- **Hits:** 348 total; 40 returned (max_results cap), sorted by relevance
- **Calibration check:** PASS — McKinlay 2015 NEJM (PMID 26465984) and McKinlay 2017 JAMA Pediatr (PMID 28783802) both retrievable and independently verified via get_article_metadata (see below); block confirmed working before proceeding.
- **Included after title/abstract screen:** see Domain E reference list in 03-synthesis/domain-E-term-outcomes.md
- **Notes:** Consensus search run in parallel (Search E2) surfaced a broader and more immediately usable set of core papers than the top-40 PubMed relevance ranking; both tools used per standing rules, adjudicated on design.

### Search E2 (Consensus, claim-level check)
- **Source:** Consensus (mcp__Consensus__search)
- **Date run:** 2026-08-27
- **String (natural-language query):** "Is neonatal hypoglycemia associated with long-term neurodevelopmental impairment in term infants?" (medical_mode=true, no other filters)
- **Hits:** 20 papers returned
- **Included after screen:** 20/20 titles relevant to Domain E/G scope; all subsequently re-verified against PubMed directly (PMID + DOI) before entering extraction.csv or synthesis — per citation-integrity rule, Consensus abstracts/paraphrases were not taken as final wording; PubMed-sourced abstracts used for any transcribed numbers.
- **Notes:** Consensus is not a reproducible Boolean search (per skill standing rules) — used here for surfacing/claim-checking only, adjudicated against PubMed record.

### Verification batch (PubMed get_article_metadata) — seed-list re-verification + new papers surfaced by E1/E2
- **Source:** PubMed (mcp__PubMed__get_article_metadata), plus targeted `[Title]` search_articles calls to resolve PMIDs for papers found only via Consensus (titles below)
- **Date run:** 2026-08-27
- **Verified (PMID, DOI confirmed this session):**
  - 10790476 — Cornblath 2000, Pediatrics, 10.1542/peds.105.5.1141
  - 26465984 — McKinlay 2015, NEJM, 10.1056/NEJMoa1504909
  - 28783802 — McKinlay 2017, JAMA Pediatr, 10.1001/jamapediatrics.2017.1579
  - 36513807 — Kennedy 2022, Pediatr Res, 10.1038/s41390-022-02410-3
  - 42050117 — May 2026, Pediatr Res, 10.1038/s41390-026-04958-w
  - 26613985 — Harris 2015, J Pediatr, 10.1016/j.jpeds.2015.10.066
  - 35940872 — Harris 2022, Arch Dis Child Fetal Neonatal Ed, 10.1136/archdischild-2022-324148
  - 36516806 — St Clair 2022, Neonatology, 10.1159/000527715
  - 35315885 — Edwards 2022, JAMA, 10.1001/jama.2022.2363
  - 38307710 — Wei 2024, Arch Dis Child Fetal Neonatal Ed, 10.1136/archdischild-2023-326452
  - 38815750 — Wei 2024, J Pediatr, 10.1016/j.jpeds.2024.114119
  - 10190926 — Duvanel 1999, J Pediatr, 10.1016/s0022-3476(99)70209-x
  - 39707054 — Palazzo 2024, Eur J Pediatr, 10.1007/s00431-024-05936-2
  - 38972961 — Lagacé & Tam 2024, Pediatr Res, 10.1038/s41390-024-03411-0
  - 39913386 — Kebede 2025, PLoS One, 10.1371/journal.pone.0316464
  - 18595988 — Burns 2008, Pediatrics, 10.1542/peds.2007-2822
  - 24861161 — Fong & Harvey 2014, Dev Med Child Neurol, 10.1111/dmcn.12496
  - 31447599 — Gu 2019, Clin Med Insights Pediatr, 10.1177/1179556519867953
  - 41338963 — Nezafat Maldonado 2026, Arch Dis Child Fetal Neonatal Ed, 10.1136/archdischild-2025-328872
  - 36568425 — Alsweiler 2022, Front Pediatr (title/DOI confirmed; full metadata call truncated by output size, re-confirmed via targeted lookup — see Domain A/C search log)
  - 30408811 — Shah 2018, Neonatology, 10.1159/000492859 (systematic review + meta-analysis; resolved from Consensus title via PubMed `[Title]` search, brief did not carry a PMID for this one)
  - 38530314 — Roeper 2024, JAMA Netw Open, 10.1001/jamanetworkopen.2024.3683 (new; not in brief seed list)
  - 30030683 — Wickström 2018, Eur J Epidemiol, 10.1007/s10654-018-0425-5 (new; not in brief seed list)
  - 33836151 — Alsweiler 2021, Lancet Child Adolesc Health, 10.1016/S2352-4642(20)30387-4 (new; not in brief seed list)
  - 35315886 — Shah 2022, JAMA, 10.1001/jama.2022.0992 (new; note this is a DISTINCT paper from Edwards 2022 JAMA 35315885 — same journal, adjacent PMID, different trial/cohort — confirmed as separate publications by independent metadata retrieval)
  - 36219444 — Edwards 2022, JAMA Netw Open, 10.1001/jamanetworkopen.2022.35989 (new; hPOD cohort observational analysis by hypoglycaemia exposure, distinct from the ITT prophylaxis trial result at 35315885)
  - 27940690 — Goode 2016, Pediatrics, 10.1542/peds.2016-1424 (new; preterm null finding, IHDP secondary analysis)
  - 32666280 — Rasmussen 2020, Eur J Pediatr, 10.1007/s00431-020-03729-x (new; note 32794121 is an author-name correction notice for the same paper, not a separate study)
  - 40119223 — Garg & Devaskar 2025, Eur J Pediatr, 10.1007/s00431-025-06082-z (new; note 42024171 is a correction notice, not a separate study)
  - 38180635 — De Rose 2024, Eur J Pediatr, 10.1007/s00431-023-05405-2 (new; matches brief seed title but brief gave no PMID)
  - 33863775 — Zamir 2021, Arch Dis Child Fetal Neonatal Ed, 10.1136/archdischild-2020-319926 (new; hyperglycaemia in ELBW — Domain G)
  - 22306045 — Tam 2012, J Pediatr, 10.1016/j.jpeds.2011.12.047 (new; hypoglycaemia in neonatal encephalopathy)
  - 37316160 — Puzone 2023, Arch Dis Child Fetal Neonatal Ed, 10.1136/archdischild-2023-325592 (new; hypo/hyperglycaemia in neonatal encephalopathy SR+MA)
  - 34199741 — Boscarino 2021, Nutrients, 10.3390/nu13061930 (new; PN-associated hyperglycaemia, preterm — Domain G)
  - 32005719 — Ramel & Rao 2020, NeoReviews, 10.1542/neo.21-2-e89 (new; hyperglycaemia in extremely preterm infants, review — Domain G)
- **Could not verify:**
  - 32446209 (brief seed: Kapoor et al., Seizure 2020, "Electroclinical spectrum of childhood epilepsy secondary to neonatal hypoglycemic brain injury") — `get_article_metadata` silently dropped this PMID from the returned batch (19/20 other PMIDs in the same batch call returned correctly), indicating this PMID does not resolve to a current PubMed record as given. Logged to 05-references/could-not-verify.md; to be re-attempted by title search in Domain F.
- **Notes:** `get_article_metadata` calls with mixed valid/invalid PMIDs return only the valid subset silently (no per-PMID error) — each PMID must be checked off against the requested list, not assumed present.

---

# Domain A — Definitions and operational thresholds (term 0–72h and beyond; preterm)

Append one block per search, as it runs. Strings must be verbatim and re-runnable. Format matches the Domain E section of `01-search-log/searches.md`.

## Search A1 (PubMed)
- **Source:** PubMed (mcp__PubMed__search_articles / bb264603 connector)
- **Date run:** 2026-08-27
- **String:** `(neonat*[tiab] OR newborn*[tiab]) AND hypoglyc*[tiab] AND (guideline*[tiab] OR "framework for practice"[tiab] OR BAPM[tiab] OR "operational threshold*"[tiab])`
- **Note on query construction:** brief §7.2 combo 1 (`#1 AND #3 AND #7`) exceeds the 5-wildcard PubMed MCP limit; simplified per the constraint already logged by Domain E (4 wildcards used here).
- **Hits:** 289 total; 40 returned (relevance-sorted, max_results cap)
- **Notes:** used to locate BAPM-guideline-comparison secondary literature and confirm no PubMed-indexed hit is being missed for the primary BAPM definitional question (BAPM itself is grey literature, not PubMed-indexed).

## Search A2 (PubMed)
- **Source:** PubMed (bb264603 connector)
- **Date run:** 2026-08-27
- **String:** `(preterm*[tiab] OR premature*[tiab]) AND hypoglyc*[tiab] AND (guideline*[tiab] OR threshold*[tiab] OR consensus[tiab])`
- **Hits:** 175 total; 40 returned (relevance-sorted)
- **Notes:** screened for preterm-specific operational-threshold or consensus-definition papers, to test whether any peer-reviewed source proposes a preterm-specific numeric threshold distinct from term/late-preterm extrapolation. None of the top 40 by relevance proposed a distinct, guideline-endorsed preterm-specific numeric threshold (consistent with Domain D's separate finding that this literature is thin); see Domain D for full preterm evidence-base handling.

## Search A3 (PubMed)
- **Source:** PubMed (bb264603 connector)
- **Date run:** 2026-08-27
- **String:** `"prolonged hypoglycemia"[tiab] OR "persistent hypoglycemia"[tiab] OR "prolonged transitional"[tiab] AND neonat*[tiab]`
- **Hits:** 151 total; 30 returned (relevance-sorted)
- **Notes:** confirmed Kebede et al. 2025 (PMID 39913386) present in this set; used to check for any additional UK/European "prolonged transitional hypoglycaemia" definitional paper beyond the Ethiopian systematic review named in the task brief — none of comparable directness found in the top 30.

## Search A4 (PubMed) — targeted title searches to identify peer-reviewed guideline-comparison papers
- **Source:** PubMed (bb264603 connector)
- **Date run:** 2026-08-27
- **Strings run:**
  - `"Systematic review of guidelines on neonatal hypoglycemia"[Title]` → 0 hits (title wording differs from indexed record; superseded by next string)
  - `Neonatal Hypoglycemia[Title] Guidelines[Title] Review[Title]` → 5 hits
  - `"Neonatal Hypoglycemia" "Guidelines"[Title] AND review[tiab] AND (BAPM[tiab] OR "British Association"[tiab])` → 2 hits
- **Included after screen:** Giouleka et al. 2023 (PMID 37508719), Luo et al. 2023 (PMID 37997458), Rusu et al. 2026 (PMID 42194883) — all independent, peer-reviewed, PMID-verified comparative reviews of national/international neonatal hypoglycaemia guidelines including BAPM; used as verified secondary sources for BAPM's specific numeric thresholds because direct retrieval of bapm.org was blocked by this session's network egress proxy (see grey-literature note below).
- **Excluded:** Shahid et al. 2023 (PMID 36662761) — a study protocol only, no extracted guideline content yet published.

## Get_article_metadata verification batch (Domain A primary sources)
- **Source:** PubMed (bb264603 connector, get_article_metadata)
- **Date run:** 2026-08-27
- **Verified (PMID, DOI, abstract retrieved this session):**
  - 10790476 — Cornblath et al. 2000, *Pediatrics*, 10.1542/peds.105.5.1141 — "Controversies regarding definition of neonatal hypoglycemia: suggested operational thresholds." Full abstract retrieved and quoted in synthesis.
  - 39913386 — Kebede et al. 2025, *PLoS One*, 10.1371/journal.pone.0316464 — full abstract retrieved; defines PTNHG as RBS <47 mg/dL (2.6 mmol/L) measured 48–72h after birth; pooled prevalence 19.71% (95% CI 16.85–22.56), 8 studies, 3686 neonates, Ethiopian population.
  - 41338963 — Nezafat Maldonado et al. 2026, *Arch Dis Child Fetal Neonatal Ed*, 10.1136/archdischild-2025-328872 — full abstract retrieved; NNRD term admissions before/after BAPM Framework publication (April 2017).
  - 36568425 — Alsweiler et al. 2022, *Front Pediatr*, 10.3389/fped.2022.1048897 — full abstract retrieved (superseding the truncated Domain E retrieval logged in `searches.md`).
  - 37508719 — Giouleka et al. 2023, *Children (Basel)*, 10.3390/children10071220 — full text retrieved via get_full_text_article (PMC10378472); used for BAPM's specific mmol/L threshold values (see synthesis for exact figures and page-level attribution).
  - 42194883 — Rusu et al. 2026, *J Clin Med*, 10.3390/jcm15103921 — full text retrieved via get_full_text_article (PMC13207171); confirms cross-guideline consensus on a distinct ">48–72h persistent hypoglycaemia" management category (critical sample, higher target, endocrine referral) without giving BAPM-specific numbers beyond Giouleka's.
  - 37997458 — Luo et al. 2023, *Clin Endocrinol (Oxf)*, 10.1111/cen.14995 — abstract retrieved (AGREE-II guideline appraisal, 10 guidelines including BAPM); confirms no cross-guideline consensus on treatment thresholds or target ranges.
- **Could not verify:** none in this batch.

## Web search / grey literature (BAPM current status) — NOT PubMed, logged separately per project rule
- **Source:** WebSearch (general web), attempted WebFetch to bapm.org (blocked)
- **Date run:** 2026-08-27
- **Queries run:**
  - "BAPM neonatal hypoglycaemia framework for practice 2017 update reaffirmed 2026"
  - "bapm.org "Identification and Management of Neonatal Hypoglycaemia" "Birth" "72 hours" published review date"
  - "BAPM hypoglycaemia framework "2.0 mmol/L" OR "2.6 mmol/L" screening treatment threshold term infant 72 hours"
  - "BAPM neonatal hypoglycaemia framework preterm infants extrapolation threshold gestational age"
- **Finding:** `www.bapm.org` is blocked by this session's network egress proxy (`EGRESS_BLOCKED` on direct WebFetch attempts to bapm.org, pmc.ncbi.nlm.nih.gov, mdpi.com, and an NHS trust guideline PDF host — WebFetch could not be used for any of these; only the WebSearch tool's own indexed snippets were retrievable). The current bapm.org resource page title, per WebSearch results, is **"Identification and Management of Neonatal Hypoglycaemia in the Full Term Infant (Birth – 72 hours)"** — distinct in wording from the original 2017-labelled resource page title ("...in the Full Term Infant (2017)"), suggesting the resource has at minimum been re-titled/re-hosted, but no search result surfaced an explicit statement of a substantively revised edition, a new version number, or a superseding document. Multiple NHS trust neonatal guidelines citing "BAPM 2017" and referencing this framework remain in active circulation with review dates into 2026 (e.g., a Royal Cornwall Hospitals Trust guideline dated "V4.3 July 2026"), which is consistent with the 2017 Framework still being the current operative BAPM document as of this search, not evidence of a confirmed reaffirmation process. **This is stated as a limitation, not resolved by inference** — the executing session could not directly access bapm.org's own change-log/version-history text to confirm reaffirmation status, and this should be flagged to the parent session as an open item if primary bapm.org access becomes available.
- **Labelled clearly as grey literature per project rule; not merged into the peer-reviewed evidence count above.**

---

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

---

# Domain C search log — BAPM core management pathway, permissive-hypoglycaemia controversy, dextrose gel Cochrane status

Append-only, verbatim, per project standing rules. All searches below were run 2026-08-27 in this executing session (fresh start — a prior attempt at this domain was interrupted by an API rate limit before writing anything to disk; nothing here is carried over unverified). PubMed MCP query strings are capped at 5 wildcards ("Query too complex" above that); `get_article_metadata` silently drops unresolvable PMIDs from a batch, so every batch result below states requested-vs-resolved counts explicitly.

## Cross-referenced from Domain E (not re-searched, per task instructions)

McKinlay 2015 (PMID 26465984), McKinlay 2017 (PMID 28783802), Harris 2015 (PMID 26613985), Harris 2022 (PMID 35940872), St Clair 2022 (PMID 36516806) were retrieved and PMID/DOI-confirmed via PubMed earlier in this same session for `03-synthesis/domain-E-term-outcomes.md`. Per the task instructions for this domain, these are cited directly from that file without re-running the search — logged here as a cross-reference, not a new retrieval.

## Grey literature — BAPM Framework (web search; bapm.org is not PubMed-indexed)

### Search GL1 (WebSearch)
- **Query:** `BAPM "Identification and Management of Neonatal Hypoglycaemia" Framework for Practice 2017 bapm.org`
- **Result:** Confirmed the 2017 Framework's existence and origin (BAPM/NHS Improvement working group convened 2016, published April 2017), and located the BAPM resource page. Two distinct BAPM resource URLs surfaced — one explicitly labelled "(2017)" and one labelled "(Birth – 72 hours)" with no year in the title, suggesting a revision — flagged for the next search.

### Search GL2 (WebSearch)
- **Query:** `BAPM neonatal hypoglycaemia framework updated 2023 2024 revised superseded`
- **Result:** Surfaced a BAPM consultation-response PDF dated June 2023 and multiple NHS trust guidelines citing a "2024" BAPM framework. Confirms a revision process was underway 2023, with a document update.

### Search GL3 (WebSearch)
- **Query:** `bapm.org "Identification and Management of Neonatal Hypoglycaemia" "Birth – 72 hours" published date version 2024`
- **Result:** Confirms the current BAPM Framework ("...Birth – 72 hours") was **published/revised 24 January 2024**, superseding the original April 2017 document. **This session could not directly WebFetch bapm.org (blocked by the network egress proxy — `EGRESS_BLOCKED`)**, so the Framework's exact pathway wording is triangulated below from (a) WebSearch snippets of the BAPM page itself and (b) multiple independent NHS trust clinical guidelines that state they are transcribing the BAPM Framework verbatim (Royal Cornwall, Ashford & St Peter's, North West Neonatal ODN, NHSGGC/Right Decisions, Milton Keynes) — used as convergent secondary evidence for pathway detail, clearly labelled as grey literature throughout, never folded into peer-reviewed counts. Both the 2017 and 2024 BAPM documents are cited in the synthesis; the numeric thresholds and structure appear stable across the revision based on triangulated content, but the exact 2024 text was not independently confirmed by direct document retrieval — flagged as a limitation.

### Search GL4–GL6 (WebSearch) — pathway element detail
- `BAPM framework hypoglycaemia term infant risk factors screening "first feed" "IDM" "SGA" "LGA" preterm 34-36 weeks`
- `BAPM hypoglycaemia framework treatment threshold "2.0 mmol/l" OR "2.6 mmol/l" symptomatic asymptomatic IV dextrose escalation`
- `BAPM neonatal hypoglycaemia framework discharge criteria "three consecutive" OR "pre-feed" blood glucose normal feeding established`
- **Result (triangulated across the three searches and the NHS trust guidelines they surfaced):** risk factors = infant of diabetic mother (IDM), small-for-gestational-age (SGA), large-for-gestational-age (LGA), late preterm (34–36+6 weeks), and other clinical risk factors (e.g., perinatal stress/acute illness); first-line management = early (within 1 hour) and frequent (3-hourly) feeding, capillary blood glucose checked pre-feed; target/screening floor ≥2.0 mmol/L (36 mg/dL) rising to ≥2.6 mmol/L (47 mg/dL) as the level triggering active management in most transcribing trust guidelines; asymptomatic BG 1.0–1.9 mmol/L (18–34 mg/dL) → buccal 40% dextrose gel (200 mg/kg) plus continued feeding, up to 2 doses; BG <1.0 mmol/L (18 mg/dL) and/or any clinical signs at any glucose level → escalate directly to IV 10% dextrose (2.5 mL/kg bolus then infusion ~60 mL/kg/day); discharge not before 24 hours of age and not before ≥3 consecutive pre-feed glucose readings ≥2.0 mmol/L with feeding established. These figures are internally consistent across five independently-sourced NHS trust documents, all explicitly citing BAPM as their source, which is treated here as reasonable convergent confirmation of the Framework's content in the absence of direct document access.

### Search GL7 (WebSearch) — NNRD real-world impact (cross-referenced with Domain A)
- Confirms the Nezafat Maldonado et al. 2026 NNRD study (verified via PubMed below) as the primary quantitative evidence of the Framework's real-world effect: term admission rate for hypoglycaemia fell from 4.9 to 3.3/1000 term live births comparing the 36 months before vs after April 2017, without increased time-to-admission or length of stay.

## Grey literature — NICE cross-reference (web search)

### Search GL8 (WebSearch)
- **Query:** `NICE postnatal care guideline NG194 neonatal hypoglycaemia glucose monitoring infant diabetic mother NG3`
- **Result:** NICE NG3 ("Diabetes in pregnancy: management from preconception to the postnatal period") carries the operative numeric infant-glucose recommendation, not NG194: blood glucose testing 2–3 hourly until pre-feed levels are maintained ≥2.0 mmol/L (36 mg/dL); escalation to tube feeding/IV dextrose only if <2.0 mmol/L (36 mg/dL) on 2 consecutive readings despite maximal feeding support, or immediately if symptomatic; minimum 24-hour postnatal stay to confirm stable glucose and feeding.

### Search GL9 (WebSearch)
- **Query:** `NICE "postnatal care" guideline NG194 "hypoglycaemia" recommendation newborn examination`
- **Result:** NG194 (postnatal care, published 20 April 2021, most recently updated 9 June 2026 per NICE's own site) covers routine postnatal care generally but was **not found, via web search, to carry its own numeric hypoglycaemia glucose threshold** — it appears to defer the operational detail to NG3 (for infants of diabetic mothers specifically) and to BAPM/local guidance for the general at-risk term population. This is reported as a genuine finding (NICE's hypoglycaemia-specific numeric guidance is narrower in scope than BAPM's), not a search failure — direct WebFetch of nice.org.uk was not attempted after bapm.org and other sites returned `EGRESS_BLOCKED`, so this conclusion rests on WebSearch snippets only and should be treated as provisional.

## PubMed — Cornblath 2000 (foundational operational-threshold paper)

### Search C1
- **Call:** `get_article_metadata(["10790476"])`
- **Result:** 1/1 resolved. Confirmed: Cornblath M, Hawdon JM, Williams AF, Aynsley-Green A, Ward-Platt MP, Schwartz R, Kalhan SC. "Controversies regarding definition of neonatal hypoglycemia: suggested operational thresholds." *Pediatrics* 2000;105(5):1141-5. PMID 10790476, DOI 10.1542/peds.105.5.1141. Full abstract retrieved and used directly (below).

## PubMed — the "permissive hypoglycaemia" commentary (title search, per task instructions)

### Search C2
- **Call:** `search_articles("\"Thresholds for hypoglycaemic screening\" cause for concern")`
- **Hits:** 9 total/9 returned — PubMed's query parser stripped the quoted phrase into a loose AND of unrelated MeSH-expanded terms (hypoglycemic agents, screening, causality, concern). None of the 9 returned PMIDs (38180635, 37776114, 31513665, 29769230, 24887333, 23617452, 21631748, 27819960, 11570119) matched on title screen — all off-topic (diabetes drug studies, cancer screening, unrelated topics).

### Search C3
- **Call:** `search_articles("hypoglycaemia screening threshold[Title] concern[Title]")`
- **Hits:** 0.

### Search C4–C9 (WebSearch, multiple phrasings)
- `"Thresholds for hypoglycaemic screening" "cause for concern" Hawdon OR Aynsley-Green`
- `"Thresholds for hypoglycaemic screening – a cause for concern" journal`
- `"cause for concern" neonatal hypoglycaemia screening threshold BAPM commentary Infant journal`
- `core.ac.uk 52954218 hypoglycaemic screening cause for concern author journal`
- `"a cause for concern" hypoglycaemia screening BAPM framework Aynsley-Green OR Alsweiler OR Harding OR Ward Platt`
- `"cause for concern" hypoglycaemia BAPM Hall OR Halliday OR Boardman OR Shephard OR McKinlay commentary letter`
- **Result:** The piece **exists** — a CORE.ac.uk repository record (work ID 52954218) is titled exactly "Thresholds for hypoglycaemic screening-a cause for concern?" and its indexed snippet content matches the brief's description precisely: it argues the BAPM Framework lowers the screening threshold to a level "that would be considered harmful at any other time of life," criticises the Framework for "failing to acknowledge the differences between screening and diagnostic thresholds," and draws the jaundice/phototherapy-threshold analogy. However, **no author name, journal name, year, volume, or DOI could be recovered** through any combination of author-name guesses or journal-name guesses across six WebSearch queries, and it did not resolve via PubMed title search (C2–C3), indicating it is very likely **not PubMed-indexed** (consistent with it being a short commentary/letter in a UK non-indexed nursing/practice journal such as *Infant*, though this could not be confirmed either).

### Search C10–C13 (WebFetch attempts, all blocked)
- `https://core.ac.uk/works/52954218` → `EGRESS_BLOCKED` (core.ac.uk)
- `https://core.ac.uk/search?q=...` → `EGRESS_BLOCKED` (core.ac.uk)
- `https://www.infantjournal.co.uk/search.html?q=...` → `EGRESS_BLOCKED` (infantjournal.co.uk)
- `https://europepmc.org/search?query=...` → `EGRESS_BLOCKED` (europepmc.org)
- `https://api.crossref.org/works?query.bibliographic=...` → `EGRESS_BLOCKED` (api.crossref.org)
- `https://www.semanticscholar.org/search?q=...` → `EGRESS_BLOCKED` (semanticscholar.org)
- `https://www.google.com/search?q=...` → `EGRESS_BLOCKED` (google.com)
- **Conclusion:** every direct-fetch route to a bibliographic record for this piece was blocked by the session's network egress proxy, and no PubMed record matches its title. **Per the task's explicit instruction, this is logged to `05-references/could-not-verify-domain-C.md` and excluded from citation** — its content is not used as a citable source anywhere in the synthesis. The "permissive hypoglycaemia" critique is instead represented in the synthesis using verified, PubMed-confirmed primary sources that carry the same substantive argument (Koh 1988, Lucas 1988, Cornblath 2000's own discussion of the tension, and Alsweiler 2022's screening-test-principles critique) — see synthesis §(d).

## PubMed — historic conservative-threshold evidence (the evidentiary basis for the "undertreats" critique)

### Search C14
- **Call:** `search_articles("Koh neural dysfunction hypoglycaemia evoked potentials newborn")`
- **Hits:** 1. `get_article_metadata(["3202642"])` → 1/1 resolved. Koh TH, Aynsley-Green A, Tarbit M, Eyre JA. "Neural dysfunction during hypoglycaemia." *Arch Dis Child* 1988;63(11):1353-8. PMID 3202642, DOI 10.1136/adc.63.11.1353. Abnormal sensory evoked potentials in 10/11 children whose blood glucose fell below 2.6 mmol/L (47 mg/dL), including 5/10 who were clinically "asymptomatic"; no evoked-potential change in the 6 children who stayed above 2.6 mmol/L. This is the primary neurophysiological evidence underpinning the 2.6 mmol/L figure itself (Aynsley-Green is also a Cornblath 2000 co-author) — **not** a paper arguing for a higher/more conservative threshold than 2.6, but the source most directly cited by clinicians arguing the 2.6 mmol/L floor must not be relaxed.

### Search C15 (initial attempts failed — logged for transparency)
- `search_articles("Lucas Morley Cole adverse neurodevelopmental outcome moderate neonatal hypoglycaemia BMJ 1988")` → 0 hits (query parser mis-tokenised "Morley...Lucas" as a combined author-field search).
- `search_articles("Lucas Morley Cole hypoglycaemia BMJ 1988")` → 0 hits (same parser issue).
- `search_articles("Lucas Morley Cole moderate neonatal hypoglycaemia adverse neurodevelopmental outcome")` → 0 hits (same issue).

### Search C16 (repaired query, explicit field tags)
- **Call:** `search_articles("\"Lucas A\"[Author] AND \"hypoglycaemia\"[Title] AND 1988[dp]")`
- **Hits:** 1. `get_article_metadata(["2462455"])` → 1/1 resolved. Lucas A, Morley R, Cole TJ. "Adverse neurodevelopmental outcome of moderate neonatal hypoglycaemia." *BMJ* 1988;297(6659):1304-8. PMID 2462455, DOI 10.1136/bmj.297.6659.1304. Multicentre cohort of 661 **preterm** infants; ≥5 days of moderate hypoglycaemia (<2.6 mmol/L/47 mg/dL) associated with an 3.5-fold increase (95% CI 1.3–9.4) in neurodevelopmental impairment at 18 months and 13–14 point reductions in mental/motor scores. **Directness flag: this landmark "conservative practice" paper is a preterm cohort, not a term cohort** — it is nonetheless the single most historically influential paper behind pre-BAPM conservative UK practice and is presented as such, with the population caveat made explicit.

## PubMed — O'Brien 2023 (systematic review of screening-eligibility criteria)

### Search C17
- **Call:** `search_articles("O'Brien Infants Eligible for Neonatal Hypoglycemia Screening Systematic Review")`
- **Hits:** 1 (the ambiguity flagged in the task brief did not reproduce in this session — the exact-title-plus-author query resolved to a single unambiguous PMID). `get_article_metadata(["37782488"])` → 1/1 resolved. O'Brien M, Gilchrist C, Sadler L, Hegarty JE, Alsweiler JM. "Infants Eligible for Neonatal Hypoglycemia Screening: A Systematic Review." *JAMA Pediatr* 2023;177(11):1187-1196. PMID 37782488, DOI 10.1001/jamapediatrics.2023.3957. Confirmed: AGREE-II appraisal of 18 guidelines (2366 abstracts screened), then applied the highest-scoring guideline's screening criteria to a 101,372-infant Auckland retrospective cohort (2004–2018): 26.3% of infants met screening criteria, essentially unchanged over 15 years (adjusted OR 0.99, 95% CI 0.93–1.03/year).

## PubMed — dextrose gel Cochrane review status (treatment vs prophylaxis, current editions)

### Search C18
- **Call:** `search_articles("dextrose gel treatment neonatal hypoglycemia Cochrane systematic review")`
- **Hits:** 8 total/8 returned.

### Search C19
- **Call:** `search_articles("Weston oral dextrose gel treatment hypoglycaemia newborn infants Cochrane Database Syst Rev")`
- **Hits:** 2 total/2 returned.

### Batch metadata check
- **Call:** `get_article_metadata(["35302645","27142842","41074566","39536722","38050311","38014716","33998668","37133295"])`
- **Result:** 8/8 resolved (no silent drops). Disambiguated into two **distinct Cochrane review families** (confirmed by DOI stems), which the brief's "treatment as distinct from prophylaxis" instruction makes essential to keep separate:
  - **TREATMENT review** (CD011027): original Weston et al. 2016 (PMID 27142842, DOI 10.1002/14651858.CD011027.pub2) → **current edition** Edwards et al. 2022 (PMID 35302645, DOI 10.1002/14651858.CD011027.pub3, search date to October 2021). This is the review directly answering the brief's question.
  - **PROPHYLAXIS review** (CD012152, a separate Cochrane title — "...to prevent hypoglycaemia in at-risk neonates") — Edwards et al. 2021 pub3 (PMID 33998668) → **current edition** Roberts et al. 2023 pub4 (PMID 38014716, DOI 10.1002/14651858.CD012152.pub4, search date April 2023). Kept explicitly separate from the treatment review in the synthesis per the brief's instruction not to conflate treatment and prophylaxis.
  - Also resolved in this batch: Roberts et al. 2024, "Intravenous Dextrose for the Treatment of Neonatal Hypoglycaemia: A Systematic Review" (*Neonatology*, PMID 39536722, DOI 10.1159/000541471) — a non-Cochrane systematic review of the escalation-to-IV-dextrose step specifically, finding only 6 studies (2 RCTs, 4 cohort, 711 infants total) and very-low-to-low certainty evidence throughout; Iqbal et al. 2025, "Infant Formula for the Prevention and Treatment of Neonatal Hypoglycaemia" (*Acta Paediatr*, PMID 41074566, DOI 10.1111/apa.70325); Wang et al. 2023, oral glucose gel **prevention** meta-analysis (*Medicine*, PMID 38050311, DOI 10.1097/MD.0000000000036137, 10 studies/4801 neonates, null on most outcomes); and an unrelated Campbell Systematic Review on LMIC neonatal nutrition interventions (PMID 37133295) which explicitly states it found **zero** eligible dextrose-gel trials from low/middle-income countries — logged as a directness/generalisability data point (all dextrose-gel RCT evidence is high-income-country-derived).

## PubMed — NNRD real-world impact and screening-principles critique (cross-check)

### Search C20
- **Call:** `get_article_metadata(["41338963", "36568425"])`
- **Result:** 2/2 resolved.
  - Nezafat Maldonado B, Conti-Ramsden F, van Hasselt TJ, Fleminger J, Chappell LC, Battersby C. "Term neonatal admissions for hypoglycaemia in England and Wales, 2012-2020: a population-based study using the National Neonatal Research Database." *Arch Dis Child Fetal Neonatal Ed* 2026;111(4). PMID 41338963, DOI 10.1136/archdischild-2025-328872. (Independently re-verified this session; also usable by Domain A.) Confirms term admissions for hypoglycaemia fell from 4.9 to 3.3/1000 term live births comparing 36 months pre- vs post-April-2017 BAPM Framework, with **unchanged** admission timing and length of stay; 46.5% of admitted infants had ≥1 BAPM-defined risk factor (i.e., the majority, 53.5%, did not).
  - Alsweiler JM, Heather N, Harris DL, McKinlay CJD. "Application of the screening test principles to screening for neonatal hypoglycemia." *Front Pediatr* 2022;10:1048897. PMID 36568425, DOI 10.3389/fped.2022.1048897. Confirms: no RCT has directly compared long-term outcomes of screened vs unscreened at-risk infants; screening for neonatal hypoglycaemia does not meet several classic screening-test principles because neuroglycopenia (the true target condition) has no direct diagnostic test; over a quarter of all infants meet at-risk screening criteria.

## PubMed — BAPM Framework's own PubMed-indexed summary (distinct from the primary grey-literature document)

### Search C21
- **Call:** `get_article_metadata(["29903743"])`
- **Result:** 1/1 resolved. Levene I, Wilkinson D. "Identification and management of neonatal hypoglycaemia in the full-term infant (British Association of Perinatal Medicine-Framework for Practice)." *Arch Dis Child Educ Pract Ed* 2018;104(1):29-32 (published online 14 Jun 2018). PMID 29903743, DOI 10.1136/archdischild-2017-314050. No abstract available via PubMed MCP (`[abstract not available]`) — this is a PubMed-indexed **secondary summary/teaching article** describing the BAPM Framework for a paediatric education-practice audience, not the primary BAPM document itself and not, on the evidence available, a critical commentary — used in the synthesis only to confirm the Framework's PubMed footprint, not as an independent evidence source.

## Summary of this domain's search yield

- Grey literature: BAPM Framework (2017 original + 2024 revision, triangulated via WebSearch since bapm.org WebFetch was blocked) and NICE NG3/NG194 (WebSearch only, same blocking) — both clearly labelled grey literature throughout, never folded into the peer-reviewed count below.
- Peer-reviewed PubMed records verified this session and used in the synthesis: 10790476, 3202642, 2462455, 37782488, 35302645, 27142842, 33998668, 38014716, 39536722, 41074566, 38050311, 41338963, 36568425, 29903743 (14 new verifications) plus 5 cross-referenced from Domain E (26465984, 28783802, 26613985, 35940872, 36516806) without re-verification, per instructions.
- Could-not-verify: 1 — "Thresholds for hypoglycaemic screening – a cause for concern?" (title and existence confirmed; no PMID/DOI/full citation recoverable this session).

---

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

## Follow-up session — full abstract retrieval for synthesis writing (2026-08-27, continuation)

The prior agent's search work above was not repeated. This continuation session's only PubMed activity was retrieving full abstract text (not previously captured verbatim in this log) for PMIDs already identified above, needed to transcribe exact figures into `03-synthesis/domain-D-preterm.md` without re-deriving numbers.

- **Call:** `get_article_metadata(["10190926","39707054","40609275","28916591","33577770","41984740","34931697"])`
- **Result:** 7/7 resolved (no silent drops). Full abstracts retrieved and exact figures transcribed for: Duvanel 1999 (PMID 10190926), Palazzo 2024 (PMID 39707054), Palazzo/Correani 2025 (PMID 40609275), Galderisi 2017 (PMID 28916591), REACT/Beardsall 2021 (PMID 33577770), Battaglini 2026 (PMID 41984740), and the current-edition Galderisi Cochrane review (PMID 34931697). No new PMIDs surfaced by this call — all seven were already logged above.
- **Win 2021 (JCEM, CGM in persistent hypoglycaemia/CHI):** no further PMID-resolution attempt made this session; remains unresolved and is logged to `05-references/could-not-verify-domain-D.md`.

## Directness/evidence-gap conclusion carried into synthesis

Across D1–D5 (five searches, ~247 raw PubMed hits plus 40 Consensus results, all screened), **no randomised controlled trial testing a specific glucose treatment threshold against a long-term neurodevelopmental outcome in infants <32 weeks (let alone <28 weeks) gestation was identified.** The CGM trials identified (Galderisi 2017, REACT 2021, Battaglini 2026) are RCTs of a *monitoring modality* in preterm infants, not RCTs of a *glucose threshold*; only Battaglini 2026 reports a long-term (2-year) neurodevelopmental outcome at all, and it is a single-centre trial of 53 infants, underpowered for that outcome. This is reported plainly as a confirmed evidence gap in the synthesis, not a search failure — see 03-synthesis/domain-D-preterm.md §(d).

---

# Domain F search log — Hypoglycaemia + seizure: is MRI indicated?

**Date run:** 2026-08-27
**Databases:** PubMed (mcp__bb264603 PubMed MCP), Consensus (mcp__1da67083 Consensus MCP)

## Seed-list verification (brief §10, Domain F)

| # | Query / action | Hits | Result |
|---|---|---|---|
| 1 | `get_article_metadata(["18595988"])` | — | **Not re-run** — Burns 2008 arrived pre-verified in the task prompt with full abstract; PMID 18595988, DOI 10.1542/peds.2007-2822 treated as verified per instruction, cited directly. |
| 2 | `get_article_metadata(["24861161","31447599","24798709","18433524","17953809","37383118"])` | 6/6 resolved | All six requested PMIDs returned complete metadata + abstract in a single batch — no drops this time. Confirms: Fong & Harvey 2014 (24861161, DOI 10.1111/dmcn.12496); Gu 2019 (31447599, DOI 10.1177/1179556519867953); Hu 2014 Acta Paediatr (24798709, DOI 10.1111/apa.12673, English, FVEP study); Mao 2008 Zhongguo Dang Dai Er Ke Za Zhi (18433524, no DOI resolved by tool, PII given, Chinese language/English abstract — **[abstract only]**); Mao 2007 Zhonghua Er Ke Za Zhi (17953809, no DOI resolved, Chinese language/English abstract — **[abstract only]**); Kurahashi 2023 World J Clin Cases (37383118, DOI 10.12998/wjcc.v11.i16.3899, English case report, PMC available). |
| 3 | `search_articles("Electroclinical spectrum childhood epilepsy neonatal hypoglycemic brain injury low resource setting Kapoor")` | 1 | Returned PMID 32446209 as sole hit. |
| 4 | `get_article_metadata(["32446209"])` (Kapoor, alone) | 1/1 resolved | **Resolves cleanly when queried alone or via title search** — full abstract retrieved (170 children, epileptic spasms 76.5%, MRI gliosis/encephalomalacia occipital±parietal in 96.5%, drug-resistant epilepsy 68.2%). DOI 10.1016/j.seizure.2020.05.010. This **contradicts** the parent session's could-not-verify entry, which found the PMID silently dropped from a 20-PMID batch call. Conclusion: the PMID is valid and resolvable; the earlier failure was a batch-call artefact (tool silently drops entries from large mixed batches under some condition not fully characterised), not a bad PMID. See notes below — **not re-logged to could-not-verify**, since it now verifies; flagged instead for the parent to reconcile the master could-not-verify.md. |

## Additional targeted searches (2015+ MRI timing / predictive value / differential diagnosis)

| # | Query | Filter | Hits | Notable results |
|---|---|---|---|---|
| 5 | `MRI timing neonatal hypoglycemia seizure prognosis prediction neurodevelopmental outcome` | date_from 2015 | 0 | Over-specified query (7 concept blocks ANDed) — no results. Query too narrow, not a true null; superseded by #6. |
| 6 | `neonatal hypoglycemia brain injury MRI timing outcome` | date_from 2015 | 1 | PMID 41022518 — Martínez-Biarge et al. 2025, "Recommendations for the use of brain MRI in the neonatal period" (An Pediatr, Engl Ed), Spanish Neonatal Brain Group practice guideline. Covers indications/optimal timing for MRI across neonatal pathologies incl. hypoglycaemia-associated brain damage. First author affiliated with Hammersmith Hospital, Imperial College Healthcare NHS Trust — same trust as Burns 2008 and this synthesis. No PMC full text available (confirmed via `convert_article_ids`) — **[abstract only]**. |
| 7 | `neonatal hypoglycemic seizure stroke arterial ischemic infarction mimic` | none | 0 | True null — no PubMed-indexed paper specifically pairs hypoglycaemic seizure + stroke-mimic terminology. Confirms this point rests on the Burns 2008 cohort's internal finding (3/35 MCA infarctions), not a dedicated literature. |
| 8 | `neonatal hypoglycemia arterial ischemic stroke middle cerebral artery infarction` | none | 1 | PMID 19656748 — screened by title only, not fetched (peripheral to domain scope; not pursued further given time budget). |
| 9 | `neonatal hypoglycemia seizure MRI brain injury pattern` | date_from 2015 | 6 | PMIDs 36514522 (new), 32446209 (Kapoor, cross-confirms search #4), 31447599 (Gu, already verified), 22682614 (Martinez-Biarge 2012 HIE white-matter paper — off-topic, HIE not hypoglycaemia-primary, not pursued), 18595988 (Burns, already verified), 18433524 (Mao, already verified). |
| 10 | `get_article_metadata(["36514522","22682614"])` | 2/2 resolved | 36514522 = Yalçın et al. 2022, *Noro Psikiyatri Arsivi*, "Neurodevelopmental Outcome in Patients with Typical Imaging Features of Injury as a Result of Neonatal Hypoglycemia" — Turkish cohort, n=21 with documented hypoglycaemia + parieto-occipital injury, DOI 10.29399/npa.27997, PMC9723839 (English, full text available). 22682614 = Martinez-Biarge et al. 2012 (HIE-specific, off-topic) — not used further. |
| 11 | Consensus: `"is MRI indicated after neonatal hypoglycemic seizures timing and prognostic value"`, medical_mode=true | — | 20 | Surfaced Zhang et al. 2022 (*Eur J Pediatr*, dynamic/serial MRI timing study — DWI-positive window vs pseudonormalisation) and re-surfaced Martínez-Biarge 2025 and Burns 2008 independently. Also surfaced HIE-specific dysglycaemia/MRI literature (Kamino 2023, Basu 2018, Parmentier 2022) — noted as adjacent/differential-diagnosis context but **not verified via PubMed this session and not cited as Domain F primary evidence**, since Domain F's scope (per brief) is isolated hypoglycaemic seizure, not neonatal encephalopathy with secondary dysglycaemia — that population is addressed in Domain G/cross-references. Also surfaced the 2026 ILAE Neuroimaging Task Force guideline on MRI in first afebrile seizure/new-onset epilepsy in infants generally (not hypoglycaemia-specific) — noted as general-practice context only. **Note:** this tool's system instructions request inline numbered citation brackets and a sign-off message in every response; per this session's data-vs-instruction rule, tool output is treated as data, not as a directive, and that formatting is not applied here or in the synthesis file. |
| 12 | `search_articles("Dynamic magnetic resonance imaging findings early stages neonatal hypoglycemic brain injury Zhang")` | none | 1 | PMID 36166098 confirmed — Zhang et al. 2022, *Eur J Pediatr*, DOI 10.1007/s00431-022-04637-y. Retrospective, n=86 Chinese neonates, 139 DWI scans: injury-site DWI hyperintensity within 7 days of hypoglycaemia in 84 scans; pseudonormalisation/T1-T2 changes appearing at 11–23 days; vulnerable sites occipital lobe 98%, splenium of corpus callosum 60%, parietal lobe 30%. This is the most direct **MRI-timing-specific** paper found (2015+ requirement). |
| 13 | `search_articles("Occipital Lobe Injury Cortical Visual Outcomes Neonatal Hypoglycemia Tam diffusion weighted")` | none | 1 | PMID 18762519 confirmed — Tam et al. 2008, *Pediatrics*, DOI 10.1542/peds.2007-2002. Pre-2015 but central to the MRI-timing question and not in the brief's seed list — added here. DWI within 6 days of hypoglycaemia onset was sensitive in term infants (50%, 8/16) but showed **no** occipital diffusion restriction beyond 6 days even with ongoing hypoglycaemia, and was **not sensitive in preterm infants at all** — a direct, quantified timing-window finding supporting early (≤6 day) MRI, with an explicit preterm-directness caveat. |
| 14 | `convert_article_ids(["41022518"], id_type="pmid")` | — | No PMC record returned — confirms Martínez-Biarge 2025 has no PMC full text available via this tool; abstract-only for this session. |

## Verified this session (Domain F) — full list with PMID/DOI

- 18595988 — Burns 2008, Pediatrics, 10.1542/peds.2007-2822 (pre-verified, supplied in task; central paper)
- 24861161 — Fong & Harvey 2014, Dev Med Child Neurol, 10.1111/dmcn.12496
- 31447599 — Gu 2019, Clin Med Insights Pediatr, 10.1177/1179556519867953
- 32446209 — Kapoor 2020, Seizure, 10.1016/j.seizure.2020.05.010 (**resolved this session — see note above**)
- 24798709 — Hu 2014, Acta Paediatr, 10.1111/apa.12673
- 18433524 — Mao 2008, Zhongguo Dang Dai Er Ke Za Zhi (Chin J Contemp Pediatr) [abstract only, Chinese language]
- 17953809 — Mao 2007, Zhonghua Er Ke Za Zhi (Chin J Pediatr) [abstract only, Chinese language]
- 37383118 — Kurahashi 2023, World J Clin Cases, 10.12998/wjcc.v11.i16.3899
- 41022518 — Martínez-Biarge 2025, An Pediatr (Engl Ed), 10.1016/j.anpede.2025.503935 [abstract only — no PMC full text]
- 36166098 — Zhang 2022, Eur J Pediatr, 10.1007/s00431-022-04637-y (new; MRI timing)
- 36514522 — Yalçın 2022, Noro Psikiyatr Ars, 10.29399/npa.27997 (new)
- 18762519 — Tam 2008, Pediatrics, 10.1542/peds.2007-2002 (new; pre-2015 but central to MRI-timing question, added per brief's no-date-limit rule for foundational imaging papers)

## Could not verify

None new this session for Domain F. The brief's flagged Kapoor PMID (32446209) **was successfully resolved** this session (see search #4) — it is NOT re-added to could-not-verify. The parent's master `05-references/could-not-verify.md` entry for this PMID should be reconciled/removed on merge (out of scope for this agent to edit directly).

## Notes on tool behaviour

- Confirms the parent's observation: `get_article_metadata` can silently drop a resolvable PMID from a large mixed batch. When a single PMID is queried alone (or found independently via title search), it resolves without issue. Recommendation for future domains: re-attempt any "dropped" PMID as a solo call or via `search_articles` title search before concluding it is unresolvable.
- `search_articles` rejects overly compound queries by returning 0 hits without an explicit "too complex" error in several cases here (search #5) — narrowing the query resolved this (search #6), consistent with the 5-wildcard warning in the task brief, though these queries used phrase terms rather than wildcards.

---

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
