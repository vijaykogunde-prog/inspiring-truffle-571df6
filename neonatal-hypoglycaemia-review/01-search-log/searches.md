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
