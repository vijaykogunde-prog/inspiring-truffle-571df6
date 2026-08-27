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
