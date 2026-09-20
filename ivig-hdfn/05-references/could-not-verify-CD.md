# Could not verify — excluded (Domains C and D)

Companion to `05-references/could-not-verify.md`. Anything claimed that could not be confirmed against PubMed/CrossRef this session, for Domains C and D. Excluded from all deliverables.

| Claimed citation / lead | Where it came from | What failed | Date checked |
|---|---|---|---|

No unverifiable leads arose during the Domain C/D searches this session. Two records returned a real, verified PMID/DOI but no abstract text ("[Abstract not available]" from PubMed) — PMID 36344387 (Gutiérrez-Vélez 2022) and PMID 15332750 (Felc 2001). These are **not** logged here because the citation itself is verified (real PMID/DOI, confirmed via `get_article_metadata`); only their narrative/numeric content is unavailable, which is handled in `02-extraction/extraction-C.csv` (rows C3, C14) by marking every unconfirmable field "not stated (abstract not available)" rather than by exclusion.
