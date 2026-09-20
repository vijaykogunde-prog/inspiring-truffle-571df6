# PRISMA-style numbers

This is a systematised narrative review (§ track decision in the brief), not a full systematic review — no formal PRISMA flow diagram or dual independent screening was performed, and these numbers are reported for transparency of the single-reviewer (Claude, across five parallel research sessions covering Domains A–F) search-and-screen process, not as a PRISMA-registered SR.

## Records identified (by domain, PubMed unless stated)

| Domain | Broad/PRISMA-denominator search hits | Restricted (trial/SR/MA or domain-specific) search hits | Included after screening |
|---|---|---|---|
| A — Rh efficacy | 151 | 12 | 10 (2 excluded: 1 antenatal-maternal-IVIG SR out of scope, 1 fetal-administration-during-IUT RCT out of scope) |
| B — ABO efficacy | 67 | 9 (RCT/SR/MA filter) + 7 additional verified Consensus leads (cohorts missed by the publication-type filter) + 21 (DAT-negative-specific search, 0 new inclusions) | 10 primary studies extracted (6 RCTs, 4 cohorts); 3 SRs + 2 guidance documents synthesised narratively, not extracted |
| C — Other alloantibodies | 36 | — (full screen of all 36) | 15 (14 case reports/series + 1 cohort); 9 antenatal-only excluded, 13 off-topic excluded, 4 narrative-only reviews |
| D — Dose/timing | — (cross-sectional over A/B/C) | 9 (supplementary search) | 0 new extraction rows (3 already in Domain A, 6 off-topic); synthesis draws on 18 existing rows by id |
| E — Harms (NEC) | 15 (pre-calibrated, matches known-item test) | — | 15/15 screened; contributes to 13 of the 24 Domain E extraction rows |
| E — Harms (late anaemia) | 65 (brief's exact string, too broad, not exhaustively screened — logged as a limitation) → 29 (tightened, disease-name-anchored version) | — | 29/29 screened |
| E — Harms (indirect/non-HDFN safety) | 20 | — | 20/20 screened, contributes 2 extraction rows explicitly flagged INDIRECT |
| E — Harms (Consensus cross-check) | 12 verified leads used; 2 additional leads found unverifiable | — | 12 used, 2 excluded to `could-not-verify.md` |
| F — Guidance/governance | Not a PubMed-hit-counted search (grey literature via WebSearch + targeted PubMed verification of companion peer-reviewed publications) | — | 18 guidance-table rows across 10 bodies/products; see `02-extraction/guidance-table.md` |

## Consolidated extraction

- **Total extraction rows (peer-reviewed studies):** 56, across Domains A–E (`02-extraction/extraction.csv`)
  - Domain A: 7 rows (10 studies included; 3 systematic reviews synthesised narratively without individual rows, per the convention set in Domain A and followed in B)
  - Domain B: 10 rows
  - Domain C: 15 rows
  - Domain E: 24 rows
- **Guidance/grey-literature table rows:** 18, across NICE, AAP, NHS England, BSH, CPS (2007 superseded + current), Dutch NVK, Australian/NZ (Queensland representative), Norwegian, and UK product SPCs (Privigen, KIOVIG, Flebogamma DIF), plus MHRA/FDA/SHOT vigilance sources (`02-extraction/guidance-table.md`)
- **Excluded and logged with reason:** every exclusion is recorded inline in the relevant domain's search-log block (`01-search-log/searches.md`) rather than in a separate exclusion table, given the narrative-review track; the two out-of-scope exclusions specific to postnatal-vs-antenatal administration (PMID 38588966, 8079448) are additionally logged in `00-protocol/out-of-scope.md`
- **Could not verify / excluded on citation-integrity grounds:** 6 leads total (1 in Domain E's Al-Alaiyan 2014 lead, 1 Kandemir 2024, 1 "Mao Ji" 2015, 1 Viellevoye 2008 conference abstract — all Domain E; plus Domain F's inability to retrieve a PMID for the BJH 2022 international guideline itself, corroborated instead via two verified secondary sources) — full detail in `05-references/could-not-verify.md`

## Known-item calibration (run before full execution, §7.5)

4/4 passed: Cochrane review (PMID 29551014) found; an early-1990s positive Rh RCT (PMID 7589769) found; two later null Rh RCTs, Dutch and Brazilian (PMID 21422084, 22882285) found; the pre-specified NEC search returned exactly 15 hits, matching the prior scoping run count. No search-block repair was required.

## Tooling limitations affecting these numbers

1. **PubMed MCP query limits** (undocumented in the original brief): rejects >5 wildcard truncations and >20 boolean operators per query. All domains expanded truncation manually and trimmed concept blocks to ≤4 synonyms; logged inline in `01-search-log/searches.md` for each domain.
2. **WebFetch network egress** was blocked for essentially every primary grey-literature domain attempted (nice.org.uk, wiley, medicines.org.uk, sciencedirect.com, b-s-h.org.uk, cps.ca, pmc.ncbi.nlm.nih.gov, england.nhs.uk, nhs.scot, ema.europa.eu) throughout Domains E and F. All grey-literature content therefore rests on WebSearch snippet synthesis, not primary-document text, and is flagged as such row-by-row in `guidance-table.md` and item-by-item in `could-not-verify.md`. **This is the single most important limitation for the guideline-writing team to address before finalising unit wording** — in particular, NICE CG98's actual GDG evidence citations and the BSH 2016/2020 full text should be obtained directly rather than relied on via this session's WebSearch-only synthesis.
3. No dual/independent screening was performed (single-reviewer narrative-review track, consistent with the brief's stated track decision).
