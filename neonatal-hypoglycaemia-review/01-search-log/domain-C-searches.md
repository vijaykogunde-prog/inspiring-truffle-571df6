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
