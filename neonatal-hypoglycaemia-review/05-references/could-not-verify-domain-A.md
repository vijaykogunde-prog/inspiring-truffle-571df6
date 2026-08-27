# Could not verify — excluded (Domain A)

Anything that could not be confirmed against PubMed or CrossRef, for Domain A (Definitions and operational thresholds). Excluded from the Domain A synthesis. Same table format as `05-references/could-not-verify.md`.

| Claimed citation | Where it came from | What failed | Date checked |
|---|---|---|---|

No Domain A citation failed PubMed/DOI verification this session — all six references used in `03-synthesis/domain-A-definitions.md` (Cornblath 2000 PMID 10790476; Nezafat Maldonado 2026 PMID 41338963; Alsweiler 2022 PMID 36568425; Kebede 2025 PMID 39913386; Giouleka 2023 PMID 37508719; Rusu 2026 PMID 42194883) were independently confirmed via `get_article_metadata` and/or `get_full_text_article` this session (2026-08-27), with PMID and DOI cross-checked.

**Note — not a citation-verification failure, but a related access limitation flagged for the parent session:** `www.bapm.org` itself (the BAPM Framework's own primary-source page) returned `EGRESS_BLOCKED` on every `WebFetch` attempt this session, as did `pmc.ncbi.nlm.nih.gov` and `www.mdpi.com` when accessed directly by URL (as opposed to via the PubMed MCP connector's `get_full_text_article`, which retrieves PMC content through a different channel and worked normally). This did not cause any reference to fail verification — the BAPM-specific numeric thresholds reported in the Domain A synthesis are instead sourced from two independent, PMID-verified peer-reviewed secondary characterisations of the BAPM document (Giouleka et al. 2023, PMID 37508719; Rusu et al. 2026, PMID 42194883), which are internally consistent with each other where they overlap. This is recorded here for transparency and is also flagged in the synthesis document's section (d) as the domain's most important limitation, to be re-checked against bapm.org directly if primary access becomes available in a different session/environment.
