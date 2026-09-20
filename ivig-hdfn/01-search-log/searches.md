# Search log

Append one block per search, as it runs. Strings verbatim and re-runnable. All searches PubMed MCP unless stated.

## §7.5 Known-item calibration test (run before full execution)

### KI-1 — Cochrane review
- **Source:** PubMed
- **Date run:** 2026-09-20
- **String:** `intravenous immunoglobulin Cochrane systematic review haemolytic disease newborn alloimmune`
- **Hits:** 2 (PMID 38588966, 29551014)
- **Result:** PASS. PMID 29551014 = Zwiers et al., "Immunoglobulin for alloimmune hemolytic disease in neonates," Cochrane Database Syst Rev 2018;3:CD003313 (Dutch group, Leiden). DOI 10.1002/14651858.CD003313.pub2. Confirms Cochrane review found and dated correctly (2018 update). PMID 38588966 is a 2024 IPD meta-analysis of *maternal antenatal* IVIG for severe alloimmunisation — correctly out of scope per §7.7 exclusion (antenatal maternal IVIG); logged to `00-protocol/out-of-scope.md`.

### KI-2 — Early-1990s positive Rh RCT
- **Source:** PubMed
- **Date run:** 2026-09-20
- **String:** `"Rh" AND "intravenous immunoglobulin" AND "exchange transfusion" AND (randomized OR randomised) AND newborn`, date-limited 1988–1996
- **Hits:** 1 (PMID 7589769)
- **Result:** PASS. Dağoğlu et al. 1995, J Int Med Res, Istanbul — RCT, IVIG 500 mg/kg vs no treatment, n=41, positive (exchange transfusion reduced). DOI 10.1177/030006059502300406.

### KI-3 — Later null Rh RCTs (Dutch and Brazilian)
- **Source:** PubMed
- **Date run:** 2026-09-20
- **String:** `intravenous immunoglobulin Rh haemolytic disease newborn placebo randomized controlled trial exchange transfusion`, date-limited 2005–2016
- **Hits:** 3 (PMID 26159803, 22882285, 21422084)
- **Result:** PASS. PMID 21422084 = Smits-Wintjens et al. 2011, Pediatrics — Leiden (Dutch) RCT, n=80, IVIG 0.75 g/kg vs placebo, null (exchange transfusion 17% vs 15%, p=.99). DOI 10.1542/peds.2010-3242. PMID 22882285 = Santos et al. 2012, Transfusion — Brazilian RCT, n=92, IVIG 500 mg/kg vs placebo under high-intensity phototherapy, null (13% vs 15.2%, p=.765). DOI 10.1111/j.1537-2995.2012.03827.x. PMID 26159803 = van Klink et al. 2015, Fetal Diagn Ther — long-term neurodevelopmental follow-up of the Leiden trial cohort, also null.

### KI-4 — NEC association
- **Source:** PubMed
- **Date run:** 2026-09-20
- **String:** `(IVIG[tiab] OR "intravenous immunoglobulin"[tiab]) AND ("necrotizing enterocolitis"[tiab] OR "necrotising enterocolitis"[tiab]) AND ("haemolytic"[tiab] OR "hemolytic"[tiab] OR "isoimmune"[tiab] OR "alloimmune"[tiab])`
- **Hits:** 15 (matches §7.6 scoping count exactly — calibration confirms search strings reproduce prior scoping)
- **Result:** PASS (count match); NEC-specific content to be confirmed at full-text/abstract screen in Domain E.

**Overall: known-item test passed 4/4. No block repair required. Proceeding to full search execution starting with Domain A.**

## Domain A — Rh efficacy (run alone first per brief §0.6)

### Search A1 — broad Rh+IVIG+neonate (PubMed MCP)
- **Note on wildcard/operator limits:** this PubMed MCP rejects >5 wildcards per query and >20 boolean operators per query — both stricter than assumed in brief §7.1. All truncation (`neonat*` etc.) expanded manually and all concept blocks trimmed to ≤4 synonyms per query to stay under the operator cap. Logged here as the required substitution.
- **Date run:** 2026-09-20
- **String:** `("Infant, Newborn"[Mesh] OR neonatal[tiab] OR newborn[tiab] OR infant[tiab]) AND ("Rh Isoimmunization"[Mesh] OR rhesus[tiab] OR "Rh incompatibility"[tiab] OR "anti-D"[tiab]) AND ("Immunoglobulins, Intravenous"[Mesh] OR IVIG[tiab] OR "intravenous immunoglobulin"[tiab])`
- **Hits:** 151 (total corpus; used for PRISMA denominator, not individually screened line-by-line — see A2 for the trial/SR subset that was fully screened)
- **Included after screen:** see A2

### Search A2 — Domain A restricted to trial/SR/MA publication types
- **Date run:** 2026-09-20
- **String:** as A1 AND `(randomized controlled trial[pt] OR controlled clinical trial[pt] OR systematic review[pt] OR meta-analysis[pt])`
- **Hits:** 12
- **Included after title/abstract screen:** 10 (2 excluded — see below)
- **Excluded:** PMID 38588966 (maternal antenatal IVIG IPD meta-analysis — out of scope per §7.7, logged to `00-protocol/out-of-scope.md`); PMID 8079448 (Dooren 1994 — IVIgG given to the *fetus* during intrauterine transfusion, not postnatally to the neonate — out of scope per §7.7 postnatal-administration criterion, logged to could-not-verify... actually verified to exist but excluded on eligibility grounds, noted in domain-A.md instead)
- **Included (10):** PMID 1306646 (Rübo 1992), 8904473 (Voto 1995), 7589769 (Dağoğlu 1995), 20924607 (Elalfy 2010), 17143357 (Nasseri 2006 — mixed Rh+ABO), 21422084 (Smits-Wintjens/Leiden 2011), 22882285 (Santos/Brazil 2012), 26159803 (van Klink 2015 f/u), 12137687 (Cochrane 2002, Alcock & Liley), 29551014 (Cochrane 2018, Zwiers), 24514437 (Louis 2014 ADC F&N SR/MA)
- **Notes:** known-item test items (i)–(iii) all recovered inside this restricted search, confirming the calibration.




# Search log — Domain B (ABO)

Append-only file for Domain B (ABO haemolytic disease efficacy), kept separate from the shared `searches.md` per instruction — to be merged later. Same block format as `searches.md`. All searches PubMed MCP unless stated. Strings verbatim and re-runnable.

**Note on wildcard/operator limits (same substitution as Domain A):** this PubMed MCP rejects queries with >5 wildcard (`*`) truncations and >20 boolean operators total. All truncation (e.g. `neonat*`) was expanded manually to explicit synonyms (`neonatal OR neonates OR newborn`, etc.) and every concept block was trimmed to ≤4 synonyms per query to stay under the operator cap, exactly as logged for Domain A. Logged here again as the required substitution for this domain's searches.

## Domain B — ABO efficacy

### Search B1 — broad ABO+IVIG+neonate (PRISMA denominator)
- **Date run:** 2026-09-20
- **String:** `("Infant, Newborn"[Mesh] OR neonatal[tiab] OR newborn[tiab] OR infant[tiab]) AND ("ABO Blood-Group System"[Mesh] OR "ABO incompatibility"[tiab] OR "ABO hemolytic"[tiab] OR "ABO haemolytic"[tiab]) AND ("Immunoglobulins, Intravenous"[Mesh] OR IVIG[tiab] OR "intravenous immunoglobulin"[tiab])`
- **Hits:** 67 (total corpus; used for PRISMA denominator, not individually screened line-by-line — see B2 for the trial/SR subset that was fully screened)
- **Included after screen:** see B2

### Search B2 — Domain B restricted to trial/SR/MA publication types
- **Date run:** 2026-09-20
- **String:** as B1 AND `(randomized controlled trial[pt] OR controlled clinical trial[pt] OR systematic review[pt] OR meta-analysis[pt])`
- **Hits:** 9
- **Included after title/abstract screen:** 9 (0 excluded on eligibility grounds at this stage; two — Alcock & Liley 2002 PMID 12137687 and Zwiers 2018 PMID 29551014 — are cross-referenced from Domain A rather than re-extracted, per task instruction)
- **Included (9):** PMID 41968063 (Hu 2026, RCT, IVIG post-plasma-exchange), 25125032 (Cortey 2014, French ABO-specific meta-analysis), 21092522 (Li 2010, Chinese meta-analysis, Rh+ABO), 17143357 (Nasseri 2006, mixed Rh+ABO RCT — Domain A row A5 / Domain B row B3), 16982453 (Huang 2006, Chinese ABO RCT), 15590442 (Miqdad/Shaheed 2004, ABO RCT), 12496219 (Gottstein & Cooke 2003, SR, Rh+ABO), 12137687 (Alcock & Liley 2002, Cochrane, Rh+ABO — cross-ref Domain A), 11245352 (Tanyer 2001, mixed ABO/Rh RCT)
- **Notes:** narrower than Domain A's restricted search (9 vs 12) because ABO-specific indexing under this publication-type filter is sparser; several key ABO cohort studies (Okulu 2022, Daunov 2022, Pan 2021, Al-Lawama 2019) are retrospective cohorts/case-control studies and are correctly NOT captured by the RCT/SR/MA publication-type filter — they were identified instead via the Consensus cross-check (search B3 below) and verified against PubMed.

### Search B3 — DAT-negative ABO disease (named secondary research question)
- **Date run:** 2026-09-20
- **String:** `("ABO Blood-Group System"[Mesh] OR "ABO hemolytic"[tiab] OR "ABO haemolytic"[tiab]) AND ("Coombs"[tiab] OR "direct antiglobulin"[tiab] OR "DAT"[tiab]) AND (IVIG[tiab] OR "intravenous immunoglobulin"[tiab])`
- **Hits:** 21 (20 title/abstract-screened via batched metadata retrieval; 1 residual record beyond the default 20-item page not individually screened)
- **Included after screen:** 0 new studies beyond those already found in B1/B2/Consensus cross-check. Screening confirmed no trial or cohort in this set reports exchange-transfusion or other efficacy outcomes stratified by DAT-negative vs DAT-positive status. Several trials in this domain require DAT positivity for entry (Miqdad 2004, Nasseri 2006, Alpay 1999) and one large cohort (Daunov 2022, PMID 38286423) reports a DAT-positivity prevalence (74%) without outcome stratification by DAT status. Most other records returned by this search were unrelated (e.g. adult autoimmune haemolytic anaemia after transplant, PMID 40016047 — excluded, wrong population).
- **Result:** **No direct evidence identified** for DAT-negative-specific IVIG efficacy in ABO disease (see domain-B.md §(a) and §(e)).

### Consensus MCP cross-check
- **Date run:** 2026-09-20
- **Query:** "Does IVIG reduce exchange transfusion in ABO haemolytic disease of the newborn?"
- **Result:** 20 papers returned. Of these, 7 were new leads not yet retrieved via the PubMed searches above; all 7 were verified against PubMed by title/DOI search before use, per task instruction:
  - Okulu et al. 2022, Front Pediatr — verified PMID 35573949, DOI 10.3389/fped.2022.864609 (Turkish national registry cohort, n=531)
  - Lieberman et al. 2022, Br J Haematol (international IVIG guideline) — verified PMID 35415922, DOI 10.1111/bjh.18170 (guidance document, not primary evidence — discussed narratively per CLAUDE.md rule 8, not extracted as a trial row)
  - Daunov et al. 2022/2024, Am J Perinatol — verified PMID 38286423, DOI 10.1055/a-2255-8772 (US retrospective cohort, n=579)
  - Pan et al. 2021, J Perinatol — verified PMID 33589732, DOI 10.1038/s41372-021-00963-5 (Chinese retrospective cohort, n=114)
  - Al-Lawama et al. 2019, J Clin Med Res — verified PMID 31803318, DOI 10.14740/jocmr4003 (Jordanian retrospective case-control, n=202)
  - Alpay et al. 1999, Acta Paediatr — verified PMID 10102158, DOI 10.1080/08035259950170420 (RCT, mixed ABO/Rh, n=116). Note: a 2000 letter/comment on this same trial (PMID 10772295) also exists and was distinguished from the primary study; only the primary RCT (10102158) is extracted.
  - Slaughter et al. 2022 (AAP technical report), Pediatrics — verified PMID 35927519, DOI 10.1542/peds.2022-058865 (evidence-review technical report underpinning the 2022 AAP hyperbilirubinaemia guideline — treated as guidance, not primary evidence, per CLAUDE.md rule 8, since AAP is explicitly named there as a guidance source)
  - Huang et al. 2026, Eur J Pediatr (dose-comparison meta-analysis, high- vs low-dose IVIG, 10 RCTs n=690, not ABO-specific but relevant to dose question (c)) — verified PMID 42458120
  - Vardar et al. 2022, Niger J Clin Pract (retrospective cohort, AIHDN incl. 52% ABO) — verified PMID 35975373 (already present in the B1 broad-search result set; not separately extracted, lower-priority descriptive cohort)
- **Excluded from cross-check:** Jalali et al. 2024 and Zheng et al. 2023 (small retrospective case series without a comparative exchange-transfusion outcome) were noted but not separately extracted — narrative mention only, no extraction row, given marginal incremental value over the ten extracted studies.

## Cross-reference to Domain A shared trials (per task instruction — not re-searched, only re-read for ABO-specific content)
- **PMID 29551014** (Zwiers 2018 Cochrane review) — re-read via `get_article_metadata` and `get_full_text_article`. The abstract/plain-language summary give only combined Rh+ABO pooled estimates (typical RR 0.35 [0.25–0.49] overall; RR 0.98 [0.48–1.98] in the two placebo-controlled low-risk-of-bias trials, both of which are Rh-only trials per Domain A). **No ABO-specific subgroup estimate is reported in the abstract or plain-language summary**; `get_full_text_article` returned only the abstract/PLS content (no additional full-text body was retrievable via the PMC id), so no further ABO-specific numeric breakdown could be extracted from this review. This absence is itself recorded in domain-B.md.
- **PMID 24514437** (Louis 2014 ADC F&N SR/MA) — re-read via `get_article_metadata`. This review DOES give an ABO-specific pooled estimate: **5 ABO trials, n=350, RR 0.31 (95% CI 0.18–0.55)**, but explicitly states "only studies with high risk of bias were available" for the ABO analysis — i.e. no low-risk-of-bias ABO trial exists to sensitivity-check this estimate (unlike the Rh analysis, which had both high- and low-risk-of-bias tiers). This is the single most important pooled ABO-specific number in this domain and is used as the anchor for the GRADE certainty rating in domain-B.md.


# Search log — Domains C and D

Append one block per search, as it runs. Strings verbatim and re-runnable. All searches PubMed MCP unless stated. Companion to `01-search-log/searches.md` (Domain A); this file covers Domain C (other alloantibodies) and Domain D (dose/timing/repeat-dosing).

## Domain C — Other alloantibodies (Kell, anti-c, anti-E, mixed)

### Search C1 — Kell/anti-c/anti-E + IVIG + neonate (PubMed MCP)
- **Date run:** 2026-09-20
- **String (used verbatim as specified, no truncation/operator-limit substitution needed — 11 boolean operators, 0 wildcards, within the ≤20-operator/≤5-wildcard limits):** `("Infant, Newborn"[Mesh] OR neonatal[tiab] OR newborn[tiab] OR infant[tiab]) AND (Kell[tiab] OR "anti-c"[tiab] OR "anti-E"[tiab] OR "Kell alloimmunization"[tiab] OR "Kell alloimmunisation"[tiab]) AND ("Immunoglobulins, Intravenous"[Mesh] OR IVIG[tiab] OR "intravenous immunoglobulin"[tiab])`
- **Hits:** 36
- **Screening:** Full metadata (title+abstract+MeSH) pulled for all 36 records via `get_article_metadata` (two batches of 20 and 16 — the tool silently caps at 20 records per call even when more PMIDs are passed; logged here as a tool-behaviour note, not a query substitution).
- **Included as Domain C case reports/case series (14, PMIDs C1–C14 in `02-extraction/extraction-C.csv`):** 41930090 (Paez 2026, anti-k/Cellano), 37013314 (Durrani 2022, anti-D+anti-C), 36344387 (Gutiérrez-Vélez 2022, anti-c — title/MeSH-only, no abstract text available), 35944885 (Pandey 2022, anti-D+anti-C+anti-E), 34170643 (Soler-Noda 2021, anti-e), 31948214 (Gustavsen 2020, anti-Ku/Kell K0), 28854515 (Venkataraman 2017, anti-SARA), 23559775 (Usman 2013, anti-E ×2 cases), 20092394 (Onesimo 2010, anti-E), 10827261 (Wagner 2000, anti-Ce), 8580635 (Gottvall 1995, Rh(D)+(C)+Kell mixed), 1709770 (Sato 1991, Infant 1 only: anti-E+anti-c — Infants 2–3 are ABO/Domain B), 42570441 (Safić Stanić 2026, mixed anti-D+anti-C+anti-Fya+anti-M), 15332750 (Felc 2001, anti-c — abstract unavailable, title/MeSH-only).
- **Included as one additional Domain C extraction row, a retrospective cohort rather than a case report (C15):** 30723901 (Healsmith 2019, Acta Obstet Gynecol Scand — 115 non-D Rh alloimmunized pregnancies, Royal Women's Hospital Victoria, Australia, 2009–2013; 10/115 neonates received postnatal IVIG, not disaggregated by antibody subtype or compared against a non-IVIG group). This is the largest-N and highest-design-tier source identified for Domain C, but still cannot support an efficacy claim (no comparator, no antibody-specific breakdown for the IVIG subgroup) — logged as such in `domain-C.md`.
- **Excluded — antenatal maternal IVIG only, not postnatal neonatal administration (out of scope per `00-protocol/out-of-scope.md` / brief §7.7 postnatal-administration criterion, same rule used to exclude Dooren 1994 in Domain A):** 41170822 (anti-K, IVIG given weekly to the mother from 15 weeks gestation; neonate received phototherapy+erythropoietin only, not IVIG), 39583478 (K+ sensitized pregnancy, maternal TPE+IVIG), 38238203 (Kell alloimmunization in pregnancy, maternal IVIG), 38028069 (maternal plasmapheresis+IVIG), 29250791 (maternal TPE+IVIG+IUT), 26829179 (anti-C+G, intrauterine treatment only, no postnatal IVIG mentioned), 16260562 (anti-g+anti-C, maternal IVIG+plasmapheresis), 8160535 (cohort of alloimmunized pregnancies, maternal high-dose IVIG/IUT — newborn treatment not disaggregated by antibody), 2120641 (Chitkara 1990 — weekly maternal IV gamma globulin in 4 Rh + 1 Kell pregnancy; the Kell case is the historical basis for the "IVIG's role in Kell disease deserves further evaluation" observation, but is antenatal-only and therefore not cited as evidence in `domain-C.md`, consistent with the out-of-scope handling of antenatal maternal IVIG project-wide).
- **Excluded — not neonatal alloimmune HDFN / false-positive MeSH match:** 42090996 (prenatal management consensus — guidance document, not primary evidence), 39689914 (RCOG Scientific Impact Paper — guidance document), 39547350 (Delphi consensus — guidance document), 37229151 (US live-birth prevalence epidemiology, no treatment data), 37193525 (Rh disease, not Kell/anti-c/anti-E/mixed — belongs to Domain A), 29732576 (adult transfusion-medicine patients, not neonates), 27879540 (IVIG-*induced* haemolysis in an infant with Kawasaki disease — reverse causal direction, an IVIG harm not an HDFN treatment; noted for Domain E awareness only, not extracted here), 11570779 (neonatal rat sepsis model, not human HDFN), 41347987 (adult autoimmune haemolytic anaemia review), 33839095 (fetal/neonatal alloimmune thrombocytopenia review — platelet, not red-cell, alloimmunisation), 31974030 (FNAIT review, platelet not red-cell), 17845901 (alloimmune neonatal *neutropenia*, not haemolytic disease), 17683353 (monoclonal anti-D mechanism review, no neonatal IVIG treatment data), 8043933 (Rh antibody mechanism review, background only).
- **Cited narratively but not given extraction rows (reviews/editorials, not individual-patient case or cohort data):** 30170792 (editorial, "Revisiting the use of IVIG for Kell alloimmunization," *Am J Obstet Gynecol* 2018 — PubMed record has no abstract text, so its content could not be verified this session and it is cited only by title/existence, not for any specific claim it might contain), 18704776 (Gottvall 2008 — 14-year Swedish alloimmunized-pregnancy cohort; reports 7/29 postnatal exchange transfusions attributable to anti-c/anti-E combined, used for background incidence only, no postnatal IVIG dosing detail given), 17430078 (HDFN update review, background only), 11284186 (general HDN review, background only).

## Domain D — Dose, timing, repeat dosing and thresholds

### Search D1 — prophylactic vs rescue timing / repeat-dose strategy (PubMed MCP)
- **Date run:** 2026-09-20
- **Note on wildcard substitution:** the brief's specified string used `isoimmun*[tiab]` and `alloimmun*[tiab]`. Per the documented PubMed MCP quirk (`searches.md` A1 note), these were expanded manually to `isoimmunization[tiab] OR isoimmunisation[tiab]` and `alloimmunization[tiab] OR alloimmunisation[tiab]` respectively, and `neonat*[tiab]` was expanded to `neonatal[tiab] OR neonate[tiab]`, to keep the query wildcard-free. This raised the boolean-operator count but stayed under the ≤20 cap (17 operators total after expansion).
- **String as run:** `("Immunoglobulins, Intravenous"[Mesh] OR IVIG[tiab]) AND (prophylactic[tiab] OR rescue[tiab] OR "repeat dose"[tiab] OR "second dose"[tiab]) AND (hemolytic[tiab] OR haemolytic[tiab] OR HDFN[tiab] OR isoimmunization[tiab] OR isoimmunisation[tiab] OR alloimmunization[tiab] OR alloimmunisation[tiab]) AND (newborn[tiab] OR neonatal[tiab] OR neonate[tiab])`
- **Hits:** 9 (PMIDs: 41347987, 33839095, 31974030, 26159803, 24514437, 21422084, 17845901, 17683353, 8043933)
- **Screening:** All 9 screened via `get_article_metadata` (metadata already retrieved for 41347987/33839095/31974030/17845901/17683353/8043933 as part of Domain C's cross-check; 26159803/24514437/21422084 were already extracted/synthesised in Domain A).
- **Already accounted for in Domain A (not re-extracted):** 26159803 (van Klink 2015, Leiden f/u), 24514437 (Louis 2014 SR/MA), 21422084 (Smits-Wintjens/Leiden 2011).
- **Excluded as off-topic (matched on IVIG+hemolytic/neonatal MeSH terms but not on the prophylactic-vs-rescue or repeat-dose question):** 41347987 (adult AIHA management review), 33839095 (FNAIT review, platelet alloimmunisation), 31974030 (FNAIT review, platelet alloimmunisation), 17845901 (alloimmune neonatal neutropenia case reports), 17683353 (monoclonal anti-D mechanism review), 8043933 (Rh antibody mechanism review).
- **Result: no trial (RCT, quasi-RCT or comparative cohort) directly randomising or comparing prophylactic-vs-rescue IVIG timing, or comparing repeat-dose strategies/intervals, was identified.** This confirms the brief's expectation and is reported as "No direct evidence identified" in `domain-D.md` per CLAUDE.md rule 10; Domain D's dose/timing/repeat-dose synthesis instead cross-references the dose/timing/repeat_doses/comparator columns already extracted for Domain A (rows A1–A7) and the one Domain C case (C6, Gustavsen 2020) that documents an explicit repeat-dosing course.


# Search log — Domain E (Harms)

Appended to the project search log per CLAUDE.md rule 9. Strings verbatim and re-runnable. All searches PubMed MCP unless stated. Date run: 2026-09-20.

**Note on wildcard/operator limits (carried over from searches.md):** this PubMed MCP rejects >5 wildcards per query and >20 boolean operators per query. Where the brief's suggested string used `*` truncation and was rejected, truncation was expanded manually and logged inline; where `neonat*`-style truncation was accepted without rejection, it is noted as such below (the limit appears to bind on total wildcard *count*, not on any single truncation).

## Search E1 — NEC core search (pre-calibrated, KI-4)

- **String:** `(IVIG[tiab] OR "intravenous immunoglobulin"[tiab]) AND ("necrotizing enterocolitis"[tiab] OR "necrotising enterocolitis"[tiab]) AND ("haemolytic"[tiab] OR "hemolytic"[tiab] OR "isoimmune"[tiab] OR "alloimmune"[tiab])`
- **Hits:** 15 (exact match to §7.6 scoping run and to KI-4 calibration test in searches.md — confirms reproducibility)
- **Screened:** all 15, on design, population, effect estimate, and explicit assessment of confounding-by-indication control
- **Included (13):** PMID 19948572 (Figueras-Aloy 2009, cohort), 22882154 (Corvaglia 2012, cohort), 35613867 (Li 2022, propensity-score cohort), 27735024 (Yang 2016, meta-analysis), 19397554 (Navarro 2009, case series), 23930883 (Kara 2013, case report), 25899199 (Atikan 2015, case report), 36344387 (Gutiérrez-Vélez 2022, case report), 40405449 (Çıplak 2025, case report), 25598445 (Louis/Patil 2015, mechanistic Doppler study, negative), 2332014 (Merlob 1990, case report — **flagged INDIRECT**: neonatal alloimmune *thrombocytopenia*, not HDFN, but same product/mechanism hypothesis), 22171016 (Freyne 2011, cohort letter, abstract not available), 20097047 (Senterre/Viellevoye/Rigo 2010, letter, French, abstract not available)
- **Treated narratively, not given individual extraction rows (precedent: Domain A's SRs):** PMID 35927519 (Slaughter/AAP 2022 technical report — peer-reviewed evidence synthesis underpinning the 2022 AAP hyperbilirubinaemia CPG; explicitly concludes "possible risk of harm due to necrotizing enterocolitis"); PMID 33158209 (Alsaleem 2020, narrative review, background only)
- **Excluded (2):** PMID 27459953 (Lieberman 2016 — descriptive 11-year audit of NICU IVIG indications; no IVIG-vs-comparator harm data, so not extractable as a harms effect-estimate row; mentioned narratively for context on real-world indication-mixing); PMID 21929710 (Ignace-Girerd 2011 — adult kidney-transplant patient, wrong population/species entirely; mentioned narratively only as mechanistic cross-age plausibility for IVIG-associated bowel ischaemia)
- **Confounding-by-indication assessment (per task instruction):** of the 3 studies giving a quantitative IVIG-vs-no-IVIG NEC comparison, only Li 2022 (PMID 35613867) uses propensity-score/multivariable adjustment explicitly designed to separate IVIG's effect from disease severity; Figueras-Aloy 2009 and Corvaglia 2012 are unadjusted-for-severity retrospective cohorts (Figueras-Aloy's multivariable model adjusts for caesarean delivery and Apgar score, not for bilirubin severity/rate of rise, i.e. not for the specific "indication" that drives both IVIG use and NEC risk). This is discussed in domain-E.md part (b).

## Search E2a — Late anaemia / top-up transfusion, brief's exact string (expanded manually)

- **String as attempted:** `("Infant, Newborn"[Mesh] OR neonatal[tiab] OR newborn[tiab]) AND ("hemolytic disease"[tiab] OR "haemolytic disease"[tiab] OR isoimmun*[tiab] OR alloimmun*[tiab]) AND ("late anemia"[tiab] OR "late anaemia"[tiab] OR "top-up transfusion"[tiab] OR "top up transfusion"[tiab] OR hyporegenerative[tiab])` — `isoimmun*`/`alloimmun*` expanded manually to `isoimmune[tiab] OR isoimmunization[tiab] OR alloimmune[tiab] OR alloimmunization[tiab]` (4 terms, under the 5-wildcard/20-operator cap)
- **Hits:** 65 (too broad to screen exhaustively at title/abstract level within scope; the Mesh/tiab combination pulls in FNAIT, general neonatal anaemia, and unrelated blood-group case reports)
- **Action taken:** narrowed to a tighter, disease-name-anchored string (E2b) to make full screening tractable, per CLAUDE.md's spirit of transparent, re-runnable methodology; the 65-hit run is logged here as the primary string and is re-runnable if fuller screening is wanted later.

## Search E2b — Late anaemia / top-up transfusion, narrowed (disease-name-anchored)

- **String:** `("hemolytic disease of the newborn"[tiab] OR "haemolytic disease of the newborn"[tiab] OR "Rh isoimmunization"[tiab] OR "Rh haemolytic disease"[tiab] OR "ABO hemolytic disease"[tiab] OR "ABO haemolytic disease"[tiab]) AND ("late anemia"[tiab] OR "late anaemia"[tiab] OR "top-up transfusion"[tiab] OR "top up transfusion"[tiab] OR hyporegenerative[tiab])`
- **Hits:** 29
- **Screened:** all 29 on title/abstract
- **Finding:** the overwhelming majority (≈25/29) describe late/hyporegenerative anaemia as a feature of the underlying disease process (intrauterine-transfusion-related bone marrow suppression, ongoing extravascular haemolysis) and its treatment with erythropoietin — **not** an IVIG-attributable outcome. Per the task brief, these are treated as background/context in domain-E.md part (a) with PMID citations, not given individual extraction rows (the CSV schema's IVIG-specific columns would be "not applicable" for nearly all of them).
- **Included as extraction rows (direct IVIG-vs-comparator or IVIG-cohort late-anaemia data):** PMID 15590442 (Miqdad 2004, RCT, ABO HDN, IVIG vs phototherapy — reports late anaemia rate by arm); PMID 17143357 (Nasseri 2006 — **already extracted as Domain A row A5**; cross-referenced only, not duplicated, per task instruction)
- **Background citations used narratively (not extraction rows), selected for informativeness:** PMID 20212966 (Mitchell & James 1999, severe late anaemia case series/review), PMID 8726237 (Ovali 1996, placebo-RCT of EPO for late anaemia — transfusions 1.8 vs 4.2), PMID 19452083 (Donato 2009, case series n=50, 14% required transfusion during EPO therapy), PMID 10379500 (al-Alaiyan & al Omran 1999, n=36, 83% developed late anaemia regardless of IUT; exchange transfusion associated with *less* late anaemia), PMID 40999656 (Prakash 2025, prospective cohort, top-up transfusion 55% overall, higher after IUT), PMID 37218889 (Morales Painamil 2023, anti-Kell case, hyporegenerative anaemia mechanism)
- **Not pursued further (very old, non-English, or abstract-not-available; low marginal value given the above already establish the point):** PMID 4969530, 14282062, 14192623, 3082104, 3141104, 2081378

## Search E3 — Indirect neonatal IVIG safety data (non-HDFN indications)

- **String:** `(IVIG[tiab] OR "intravenous immunoglobulin"[tiab]) AND ("necrotizing enterocolitis"[tiab] OR thrombo*[tiab] OR "adverse effect"[tiab]) AND (neonat*[tiab] OR newborn[tiab]) AND (sepsis[tiab] OR "randomized controlled trial"[pt] OR "systematic review"[pt])` — run exactly as given; `thrombo*` and `neonat*` (2 wildcards total) were accepted without rejection, so no manual expansion was needed here (below the operator/wildcard cap unlike the brief's assumption).
- **Hits:** 20 (has_more: false)
- **Screened:** all 20
- **Included, flagged INDIRECT/extrapolated (2):** PMID 31995650 (Cochrane 2020 update, Ohlsson & Lacy — IVIG for preventing infection in preterm/LBW infants — 19 RCTs, ~5000 infants, prophylactic low-to-moderate-dose IVIG in a *different indication*; no significant difference in NEC, BPD, IVH, or mortality; "no major adverse effects... reported in any of these studies"); PMID 41543094 (2026, IVIG-induced severe anaemia and cross-matching incompatibility in 30 neonates — indication was sepsis/NEC/undetermined, **not HDFN**, but directly informs the isoagglutinin-haemolysis mechanism that would apply equally, or more, in HDFN infants already haemolysing)
- **Not separately extracted (already synthesised inside the Cochrane review above; citing the review itself avoids double-counting):** PMID 1951212 (1991 RCT, high-risk neonates, no NEC signal), 3099267 (1986 RCT, preterm sepsis prevention, no adverse effect noted) — both are among the 19 trials pooled in PMID 31995650
- **Excluded as off-topic (keyword-coincidence hits — thrombosis/NEC/sepsis terms matched unrelated case reports):** PMID 42440440 (SJS/TEN case), 39867692 (MIS-C aortoiliac thrombosis), 38957821 (Group A strep toxic shock/portal vein thrombosis), 26459642 (neutropenia in SGA infants), 32241699 (enteral erythropoietin RCT), 25751631 (pentoxifylline Cochrane), 21975741/14584000 (granulocyte transfusion Cochrane), 9053888 (general NEC risk factors, French), 2114035 (general review), 20569818 (general review) — none report IVIG-attributable harm data
- **Duplicate/superseded Cochrane versions (not separately extracted):** PMID 23821390 (pub3, 2013), 14973955 (pub2, 2004), 11405962/10796199 (pub1, 2000/2001) — superseded by PMID 31995650 (pub4, 2020), the version extracted

## Search E4 — Consensus MCP claim queries

### E4a — "Is IVIG in neonatal haemolytic disease associated with necrotising enterocolitis?"
- **Tool:** Consensus MCP
- **Hits surfaced:** 20; new leads not already found by PubMed searches E1/E3 were verified against PubMed before use (per task instruction), individually logged below
- **New leads verified via PubMed (PMID confirmed):** Freyne et al. 2011 → PMID 22171016 (already folded into E1's included list above); Christensen et al. 2015 "Increased hemolysis after administering IVIG..." → PMID 26074177 (**direct evidence for the isoagglutinin-haemolysis harm**, end-tidal CO monitoring showing increased haemolysis after IVIG in a single Rh-disease neonate); Lieberman et al. 2022 "International guidelines regarding the role of IVIG..." → PMID 35415922 (BJH; international expert-panel evidence-based recommendation against routine IVIG use — treated narratively, like a guideline/SR, not as an extraction row); Huang et al. 2026 dose-comparison meta-analysis → PMID 42458120 (10 RCTs, n=690, no significant difference in adverse-reaction rates between high- and low-dose IVIG); Mohamed et al. 2012 "Transfusion Associated NEC" → PMID 22351894 (mechanism/confounding-pathway context: transfusion itself, independent of IVIG, is an established NEC risk factor — relevant because IVIG-treated infants receive more top-up transfusions)
- **New leads that FAILED PubMed verification this session — excluded, logged to `05-references/could-not-verify-E.md`:** Kandemir et al. 2024 "Severe Gastrointestinal Complications After IVIG Infusion in Newborns" (Iranian J Pediatr, DOI 10.5812/ijp-144488 — no PMID returned by any PubMed search attempted); Mao Ji 2015 "Neonatal ABO hemolytic lead to necrotizing enterocolitis with gammaglobulin" (Chinese journal, not PubMed-indexed)
- **Leads already covered by verified PubMed searches (not re-logged):** Li 2022 (35613867), Çıplak 2025 (40405449), Figueras-Aloy 2009 (19948572), Navarro 2009 (19397554), Gutiérrez-Vélez 2022 (36344387), Corvaglia 2012 (22882154), Zwiers 2018 Cochrane (29551014, already Domain A), Slaughter/AAP 2022 (35927519)
- **Out of scope, not pursued (background NEC-pathogenesis literature unrelated to IVIG, or antenatal-maternal IVIG):** Gopalakrishna 2019 (maternal IgA/NEC mechanism), Cho 2016 (NEC immunology review), MohanKumar 2019 (murine transfusion-NEC model), Kaplina 2023 (NEC review), Mani 2023 (viral infection/NEC meta-analysis), Zhao 2024 (China NEC risk-factor meta-analysis), Ji 2026 IPD meta-analysis on maternal alloimmunisation (antenatal, out of scope per `00-protocol/out-of-scope.md`)

### E4b — "Does IVIG for neonatal alloimmune hemolytic disease increase late anemia or top-up transfusions?"
- **Tool:** Consensus MCP
- **New leads verified via PubMed (PMID confirmed):** Okulu et al. 2022 → PMID 35573949 (Turkish Neonatal Jaundice Registry, n=531 ABO-HDN — IVIG group had higher exchange-transfusion rate, longer phototherapy, more rehospitalisation and acute bilirubin encephalopathy — a striking illustration of confounding by indication, used narratively in part (b)); Al-lawama et al. 2019 → PMID 31803318 (case-control, n=94 vs 108 — IVIG group had more severe hemolysis at baseline and more downstream transfusion/exchange-transfusion, again consistent with confounding by indication rather than IVIG-caused harm); Ono et al. 2023 → PMID 38037498 (Japan national NICU survey, n=916 BTHDN, 219 IVIG-treated — ~20% of IVIG-treated infants had late-onset anaemia requiring treatment; single-arm, no comparator); Zheng et al. 2023 → PMID 38143377 (case series, repeat 3–4-dose IVIG, n=11, no adverse events); Vardar et al. 2022 → PMID 35975373 (retrospective, n=63, apnoea the only complication, 1/63)
- **New leads that FAILED PubMed verification this session — excluded, logged to `05-references/could-not-verify-E.md`:** Al-Alaiyan et al. 2014 "Effects of intravenous human immunoglobulin on late hyporegenerative anemia..." (Int J Pediatr Adolesc Med, DOI 10.1016/j.ijpam.2014.11.003 — no PMID found; note a *different*, verified 1999 al-Alaiyan paper on late anaemia risk factors, PMID 10379500, was retrieved independently via search E2b and does not report IVIG data)
- **Leads out of scope (antenatal/maternal IVIG — excluded per `00-protocol/out-of-scope.md`):** Mustafa et al. 2024 (IPD meta-analysis, maternal IVIG), Vlachodimitropoulou et al. 2022 (maternal IVIG case-control), Zwiers/PETIT 2018 (maternal IVIG cohort)
- **Leads already covered / cross-referenced, not re-logged:** Zwiers 2018 Cochrane (Domain A), Smits-Wintjens 2011 and Santos 2012 (Domain A rows A6/A7 — top-up transfusion data already extracted there, per task instruction not re-extracted here), Pan et al. 2021 (efficacy-focused, Domain B/ABO territory, no distinct harms data beyond what Okulu/Al-lawama already give), Lieberman 2022 guideline (already logged under E4a), de Winter et al. 2025 → verified PMID 39792381 (JAMA Netw Open, 31-centre international HDFN cohort — used narratively for practice-variation context in IVIG/EPO/exchange-transfusion use, not a harms-effect-estimate row), Moise 2025 (general FNAIT/HDFN biologics review, background only)

## Search E5 — Grey literature / regulatory (WebSearch; WebFetch blocked for medicines.org.uk and shotuk.org by the session's network egress proxy, so content below is drawn from search-result snippets only, not the full source documents — flagged as a limitation)

- **UK SPCs (electronic Medicines Compendium) searched:** Privigen 100 mg/mL (product 6428), KIOVIG 100 mg/mL (product 9198), Flebogamma DIF 50 mg/mL and 100 mg/mL (product 6648) — see `02-extraction/guidance-table.md` for extracted content. **Exact SPC revision/version dates could not be confirmed** because the emc pages themselves could not be fetched (egress-blocked); this is recorded as a limitation in the guidance table rather than a fabricated date.
- **SHOT (Serious Hazards of Transfusion) UK haemovigilance:** searched for IVIG-specific neonatal haemolysis/thrombosis case entries. No SHOT annual-report chapter specifically reporting IVIG-associated haemolysis or thrombosis in a neonate with HDFN was located via search snippets; SHOT's neonatal/HDFN-related haemovigilance content that *was* found concerns anti-D **immunoprophylaxis administration errors** (omitted/delayed/wrong-dose anti-D to the mother) and general delayed/acute hemolytic transfusion reactions from red-cell transfusion — not IVIG treatment of established HDFN. **Absence is a finding** (CLAUDE.md rule 10): UK haemovigilance does not appear to separately capture IVIG-treatment-related neonatal harms as a distinct category, which is itself relevant to the guideline (recommend explicit local incident reporting for any suspected IVIG-associated NEC/haemolysis given this national gap). Source PMID (verified, informs this section rather than being an SPC/SHOT primary document itself): 24164446 (Desborough et al. 2013, review of MHRA/FDA/EU/Canada vigilance data on IVIG-induced haemolysis, 925 cases identified 1998–2012, mostly adult).
- **FDA boxed warning (US, cited for international regulatory comparator context only, not a UK source):** thromboembolism boxed warning added to all IVIG products in 2013 following retrospective claims-database analysis; risk factors listed include hyperviscosity, indwelling catheters, hypercoagulable states — general population, not neonate-specific.


# Domain F — Guidance and governance: search log

All searches run 2026-09-20. Domain F is grey literature (WebSearch) plus PubMed MCP verification for any guidance document with a companion peer-reviewed publication. Grey-literature searches are logged with query text, what was found, and URL, per rule 9 (not full Boolean-string rigour, per the brief).

**Tooling note:** `WebFetch` was attempted repeatedly against nice.org.uk, onlinelibrary.wiley.com, medicines.org.uk, sciencedirect.com, b-s-h.org.uk, cps.ca, pmc.ncbi.nlm.nih.gov, england.nhs.uk, eoeneonatalpccsicnetwork.nhs.uk, perinatalnetwork.nhs.scot, and en.wikipedia.org (as a connectivity control) — every one of these returned `EGRESS_BLOCKED` from the session's network egress proxy (organisational policy, not a per-site failure; confirmed via `/root/.ccr/README.md` guidance not to route around 403/407-class blocks). This is logged once here rather than per-call. Consequently Domain F extraction relies on (a) `WebSearch`, which returns server-side-fetched synthesised snippets with source URLs and evidently is not subject to the same block, and (b) PubMed MCP tools (`search_articles`, `get_article_metadata`, `get_full_text_article`) for anything with a PMID. Where a detail could only be seen in a WebSearch snippet and not independently confirmed against the primary document's full text, this is noted in the extraction table and, where material, logged to `05-references/could-not-verify-F.md`.

## PubMed verification searches

### F-PM1 — AAP 2022 guideline PMIDs
- **Tool:** `mcp__PubMed__search_articles`
- **Query:** `Kemper Newman clinical practice guideline hyperbilirubinemia newborn 35 weeks 2022`
- **Hits:** 2 — PMID 35927519 (Slaughter/Kemper/Newman, "Technical Report: Diagnosis and Management of Hyperbilirubinemia in the Newborn Infant 35 or More Weeks of Gestation", Pediatrics 2022;150(3), DOI 10.1542/peds.2022-058865) and PMID 35927462 (Kemper et al., "Clinical Practice Guideline Revision: Management of Hyperbilirubinemia in the Newborn Infant 35 or More Weeks of Gestation", Pediatrics 2022;150(3), DOI 10.1542/peds.2022-058859, article type "Practice Guideline").
- **Result:** Both verified via `get_article_metadata`. The Technical Report's own abstract states: "IVIG has unclear benefit for preventing exchange transfusion in infants with isoimmune hemolytic disease, with a possible risk of harm due to necrotizing enterocolitis... Limited evidence for effectiveness with some evidence of risk of harm support the revised recommendations to limit IVIG use." This is a peer-reviewed, PMID-verified statement and is used directly in `domain-F.md`.

### F-PM2 — NICE CG98 companion peer-reviewed summary
- **Tool:** `mcp__PubMed__search_articles` (via WebSearch lead) then `get_article_metadata`
- **Lead:** WebSearch surfaced "Jaundice in newborn babies under 28 days: NICE guideline 2023 (CG98) - PubMed"
- **Verified:** PMID 40889816, Innerarity J et al., Arch Dis Child Educ Pract Ed. 2026 May 18;111(3):119-122, DOI 10.1136/archdischild-2025-329317. This is an educational summary article of the NICE guideline (London REACH Network), not an independent evidence review — noted as such in the extraction table.

### F-PM3 — CPS current guideline PMID
- **Tool:** `get_article_metadata`
- **Lead:** WebSearch surfaced cps.ca "Guidelines for detection and management of hyperbilirubinemia in term and late preterm newborns (≥35 weeks gestational age)"
- **Verified:** PMID 42488358, Ng E, Altit G, Joynt C, Radziminski N, Narvey M, Paediatr Child Health. 2026 Apr 28;31(5):496-526, DOI 10.1093/pch/pxaf034, PMCID PMC13390605. This is the CURRENT CPS position statement (replaces the 2007 statement cps.ca/uploads/.../6_CPS_Hyperbilirubinemia.pdf). `get_full_text_article` on PMC13390605 returned only the abstract (no full text available through the tool) — full IVIG recommendation wording therefore taken from WebSearch snippets of the CPS web page, flagged as not independently full-text-verified in the extraction table.

### F-PM4 — BSH 2016 transfusion guideline + 2020 addendum
- **Tool:** `get_article_metadata`
- **Verified:** PMID 27861734, New HV, Berryman J, Bolton-Maggs PHB et al., "Guidelines on transfusion for fetuses, neonates and older children", Br J Haematol. 2016;175(5):784-828, DOI 10.1111/bjh.14233. Lead author New HV is affiliated with Imperial College Healthcare NHS Trust (the commissioning trust for this project) — noted for relevance. A 2020 addendum (BJH 2020, DOI 10.1111/bjh.17109) was also found by WebSearch but its content could not be fetched (wiley blocked); logged to could-not-verify-F.md as unconfirmed whether the addendum touches the IVIG recommendation specifically.

## WebSearch — guidance documents

### F-WS1 — NICE CG98 current status
- **Query:** `NICE CG98 neonatal jaundice guideline status 2026 updated surveillance`
- **Found:** NICE CG98 "Jaundice in newborn babies under 28 days", originally published 19 May 2010, last amended 31 October 2023 (exceptional surveillance review; TSB-threshold wording clarified and prolonged-jaundice urine-culture advice updated). No further update planned as of the October 2023 surveillance decision. CG98 has NOT been superseded/replaced by an NG-numbered guideline — it remains current as CG98.
- **URL:** https://www.nice.org.uk/guidance/cg98

### F-WS2 — NICE CG98 IVIG recommendation exact wording
- **Query:** `NICE CG98 "intravenous immunoglobulin" recommendation 1.5 Rhesus ABO phototherapy exact wording`
- **Found:** Recommendation 1.8.1 (per WebSearch synthesis of the NICE recommendations page): "Use intravenous immunoglobulin (IVIG) (500 mg/kg over 4 hours) as an adjunct to continuous intensified phototherapy in cases of rhesus haemolytic disease or ABO haemolytic disease when the serum bilirubin continues to rise by more than 8.5 micromol/litre per hour." Direct WebFetch of the NICE page to confirm the recommendation number and check for repeat-dosing wording and cited evidence was blocked (EGRESS_BLOCKED); the quoted wording is a WebSearch-tool synthesis of the live NICE page and is flagged in the extraction table as not independently primary-source-verified for exact recommendation numbering, though the dose/trigger text matches the wording as widely quoted in secondary UK neonatal network guidelines cross-checked below (F-WS9, F-WS10).
- **URL:** https://www.nice.org.uk/guidance/cg98/chapter/recommendations

### F-WS3 — NHS England Ig Commissioning Policy, current edition and colour classification
- **Query:** `"Clinical Commissioning Policy" therapeutic immunoglobulin 2025 "haemolytic disease" blue OR grey OR red priority panel approval database`
- **Found:** Current edition = "Clinical Commissioning Policy for the use of therapeutic immunoglobulin (Ig) in England (2025)", NHS England, superseding the "NHSE Commissioning Criteria for the use of Ig" V1.4 (November 2019). WebSearch synthesis states the 2025 edition **removed the historical Red/Blue/Grey colour-coding system** used in prior editions (Red = highest priority/risk to life without treatment; Blue = reasonable evidence base, other options exist; Grey = limited/little-no evidence). The 2025 policy operates via the National Immunoglobulin Database e-referral platform, findings reported to the Immunoglobulin Oversight Group and relevant Clinical Reference Group (CRG). Direct fetch of the PDF (england.nhs.uk and igd.mdsas.com mirror) was blocked; the specific current-edition classification/priority label for "haemolytic disease of the fetus and newborn" by name, and whether panel approval is required specifically for neonatal HDFN, could NOT be independently confirmed — logged to could-not-verify-F.md.
- **URLs:** https://www.england.nhs.uk/publication/commissioning-criteria-policy-for-the-use-of-therapeutic-immunoglobulin-ig-in-england/ ; https://www.england.nhs.uk/wp-content/uploads/2021/12/ccp-for-the-use-of-therapeutic-immunoglobulin-england-2025.pdf ; mirror: https://igd.mdsas.com/wp-content/uploads/ccp-for-the-use-of-therapeutic-immunoglobulin-england-2025.pdf ; prior edition: https://igd.mdsas.com/wp-content/uploads/NHSE_Commissioning_Criteria_for_the_use_of_Ig_V1.4_November_2019.pdf

### F-WS4 — BSH guideline(s) covering HDFN
- **Query:** `British Society for Haematology guideline haemolytic disease fetus newborn HDFN management` and `BSH guideline transfusion management neonate haemolytic disease newborn postnatal IVIG exchange transfusion 2024 2025`
- **Found:** Three distinct current BSH documents touch this area: (1) "Guideline for the investigation and management of red cell antibodies in pregnancy" (antenatal, updates 2016 guidance) — antenatal scope, out of Domain F's postnatal focus but logged; (2) "Guideline for the use of anti-D immunoglobulin for the prevention of HDFN" — prophylaxis, not treatment, out of scope; (3) **"Guidelines on transfusion for fetuses, neonates and older children"** (New et al. 2016, BJH, PMID 27861734, + 2020 addendum) — this is the BSH document containing the postnatal neonatal IVIG-for-HDFN recommendation and is the one tabulated. WebSearch synthesis (not full-text-verified) of the IVIG content: "IVIG use should be considered when managing a baby with haemolytic disease of the newborn if there is delay in commencing an exchange transfusion due to availability of blood, and can be used as an adjunct to phototherapy to try and reduce the need for exchange transfusion, at a dose of IVIG 500mg/kg over 4 hours."
- **URLs:** https://b-s-h.org.uk/media/2884/2016-neonates-final-v2.pdf ; https://onlinelibrary.wiley.com/doi/10.1111/bjh.14233 ; addendum https://onlinelibrary.wiley.com/doi/10.1111/bjh.17109

### F-WS5 — CPS position statement, current vs superseded version
- **Query:** `Canadian Paediatric Society position statement hyperbilirubinemia jaundice IVIG newborn`
- **Found:** Two CPS documents exist: the ORIGINAL 2007 position statement (fn 2007-02; "Guidelines for detection, management and prevention of hyperbilirubinemia in term and late preterm newborn infants", Paediatr Child Health 2007) which recommended IVIG 1 g/kg "Grade A" citing a systematic review (RR 0.28, 95% CI 0.17–0.47, NNT 3) — this is the Alcock & Liley 2002 Cochrane-era pooled estimate, i.e. the risk-of-bias-unstratified figure Domain A found does not survive stratification; and the CURRENT 2025/2026 revision (PMID 42488358, Ng et al., Paediatr Child Health 2026;31(5):496-526 — see F-PM3) which replaces it. **Important finding for the guidance-vs-evidence gap:** it could not be confirmed via WebSearch snippets alone whether the current 2025/2026 CPS revision retains the "Grade A"/RR 0.28 framing from 2007 or has revised it in light of the null trials; this is logged to could-not-verify-F.md as a specific, material unresolved question, since the 2007 text is still live on the cps.ca site in parallel with the new statement's technical annex.
- **URLs:** https://cps.ca/en/documents/position/hyperbilirubinemia-newborns ; https://cps.ca/uploads/documents/6_CPS_Hyperbilirubinemia.pdf (2007 archived) ; https://cps.ca/uploads/documents/12022025_-_Hyperbili_Technical_Annex(2).pdf (2025 technical annex)

### F-WS6 — AAP 2022 IVIG recommendation detail and escalation-of-care threshold
- **Query:** `AAP 2022 Kemper hyperbilirubinemia guideline IVIG escalation of care threshold recommendation text "necrotizing enterocolitis"`
- **Found:** Recommendation text (WebSearch synthesis of publications.aap.org and aap.org FAQ pages): "IVIG (0.5 to 1 g/kg) over 2 hours may be provided to infants with isoimmune hemolytic disease (positive DAT) whose TSB reaches or exceeds the escalation-of-care threshold [i.e. the AAP's threshold for considering/preparing for exchange transfusion, which sits below the exchange-transfusion threshold itself]. The dose can be repeated in 12 hours." Guideline explicitly frames IVIG as conditional/weak: "may be provided," factoring in phototherapy response, TSB rate of rise, and feasibility of timely exchange transfusion. Confirmed independently via the Technical Report's own PubMed-verified abstract (F-PM1): "IVIG has unclear benefit... possible risk of harm due to necrotizing enterocolitis... Limited evidence for effectiveness with some evidence of risk of harm support the revised recommendations to limit IVIG use."
- **URLs:** https://publications.aap.org/pediatrics/article/150/3/e2022058859/188726/ ; https://publications.aap.org/pediatrics/article/150/3/e2022058865/188725/ ; https://www.aap.org/en/patient-care/hyperbilirubinemia/frequently-asked-questions-about-the-2022-aap-guideline-on-the-management-of-hyperbilirubinemia/

### F-WS7 — Dutch guidance
- **Query:** `Dutch guideline neonatal jaundice hyperbilirubinemia IVIG NVK richtlijn hemolytische ziekte`
- **Found:** Two relevant Dutch (NVK, via Richtlijnendatabase) documents: (1) "Hyperbilirubinemie bij de pasgeborene ... na 35 weken" (national NVK guideline on hyperbilirubinaemia >=35 weeks) — module "Effect behandelingen voor hyperbilirubinemie" gives IVIG a role for severe hyperbilirubinaemia specifically due to blood-group antagonism; (2) "Preventie en behandeling hemolytische ziekte van de foetus en pasgeborene" (prevention/treatment of HDFN specifically), part of the national blood transfusion policy richtlijn. Both are hosted on richtlijnendatabase.nl; direct fetch blocked, so exact dose/threshold wording not independently confirmed (logged to could-not-verify-F.md). Note: the Dutch group (Leiden — Lopriore/Smits-Wintjens) authored the pivotal null RCT in Domain A (PMID 21422084), so Dutch national guidance is of particular interest for whether it has been revised in light of its own group's null trial.
- **URLs:** https://richtlijnendatabase.nl/richtlijn/hyperbilirubinemie_in_de_eerste_twee_levensweken_bij_de_pasgeborene_geboren_na_een_zwangerschapsduur_35_weken/effect_behandelingen_voor_hyperbilirubinemie.html ; https://richtlijnendatabase.nl/richtlijn/bloedtransfusiebeleid/transfusiebeleid_bij_de_niet_acuut_bloedende_patient/preventie_en_behandeling_hemolytische_ziekte_van_de_foetus_en_pasgeborene.html
