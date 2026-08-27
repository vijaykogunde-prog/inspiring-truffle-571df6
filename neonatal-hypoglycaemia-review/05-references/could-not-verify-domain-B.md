# Could not verify — Domain B — excluded

Anything that could not be confirmed against PubMed or CrossRef during Domain B (point-of-care vs laboratory confirmation) work. Excluded from the synthesis and extraction table. Same format as `05-references/could-not-verify.md`.

| Claimed citation | Where it came from | What failed | Date checked |
|---|---|---|---|
| PMID 20301489 (title/authors unknown — surfaced as a PubMed search hit, not independently identified by title) | Search B1 (PubMed combo #3, "POC glucometer accuracy, term"), top-20 metadata screening batch | `get_article_metadata` silently dropped this PMID from a 20-PMID batch where 18/20 others resolved correctly; a repeat individual call for this PMID alone returned "no articles found for the provided PMIDs" — PMID does not resolve to a retrievable current PubMed record. | 2026-08-27 |
| PMID 31804789 (title/authors unknown — surfaced as a PubMed search hit, not independently identified by title) | Search B1 (PubMed combo #3, "POC glucometer accuracy, term"), top-20 metadata screening batch | Same failure mode as above, same batch: silently dropped, then confirmed non-resolving on individual retry. | 2026-08-27 |

## Disposition note on the nine RESEARCH-BRIEF.md §10 candidate PMIDs

All nine candidate PMIDs listed in RESEARCH-BRIEF.md §10 ("Point-of-care glucose testing accuracy") **did** resolve successfully via `get_article_metadata` this session — none belong on this could-not-verify list. Three were excluded from the synthesis on relevance grounds after reading the title/abstract (not a verification failure): PMID 39206021 (adult diabetic patients in a maternity centre, not neonatal glucose testing), PMID 30829013 (glucometer-based β-glucosidase assay for NEC diagnosis — different analyte and clinical question), and PMID 9325505 (home glucose meter accuracy in pregnant women, not neonates). See `01-search-log/domain-B-searches.md` ("Screening of prior-session candidate PMIDs") for the full disposition of all nine.
