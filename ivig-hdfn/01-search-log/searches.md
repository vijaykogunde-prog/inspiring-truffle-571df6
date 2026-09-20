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


