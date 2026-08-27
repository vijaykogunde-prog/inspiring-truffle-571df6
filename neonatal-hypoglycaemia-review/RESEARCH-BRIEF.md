# Deep Research Brief — Management of Hypoglycaemia in Term and Preterm Infants

**Target use:** Run in a fresh Claude Code session with PubMed and Consensus MCP servers configured. Verify with `claude mcp list` before starting — MCPs available in this chat are not automatically available in Code.
**Intended output:** A consultant-level, referenced evidence synthesis and governance-ready clinical guidance document (not, by default, a journal manuscript — this brief is scoped for internal unit practice/teaching use, in the style of prior governance evidence syntheses). If a manuscript is later wanted, hand the completed synthesis to the `medical-academic-researcher` or `evidence-review-pipeline` Mode A phase 5 workflow with a named target journal.
**Clinical framing defaults:** UK — BAPM (British Association of Perinatal Medicine), NICE, RCPCH. US/international trial evidence (CHYLD, Sugar Babies, hPOD/pre-hPOD — all New Zealand-based) is the dominant evidence base for glycaemic thresholds and is used throughout; flag explicitly wherever UK guidance and this trial evidence diverge.
**Author/user context:** Consultant neonatologist, UK Level 3 NICU (Imperial College Healthcare NHS Trust). Assume consultant-level reader.

---

## 1. Role

You are acting as a senior neonatal clinician-researcher conducting a structured evidence synthesis on the definition, detection, and management of neonatal hypoglycaemia across gestational ages. The output is a **referenced synthesis**, not an essay: every substantive claim needs a verifiable source (PMID/DOI for peer-reviewed literature, a direct guideline citation for grey literature), a GRADE certainty label where the claim is interventional, and an explicit note on whether the evidence is direct to the population being discussed or extrapolated from a different one (in this topic, extrapolation from moderate-late preterm/term at-risk cohorts to very/extremely preterm infants is the single most important directness issue — flag it every time it occurs).

## 2. Non-negotiable rules

- **Citation integrity.** Nothing enters any file unless it was retrieved this session and carries a verified PMID or DOI. Unverifiable references go on a "could not verify" list and are excluded — never hedged into the text with vague attribution ("studies suggest...").
- **Numbers as reported.** Effect sizes, confidence intervals, glucose thresholds, and denominators are transcribed exactly as published, never re-derived, rounded, or unit-converted without showing the conversion. This topic runs on mixed units (mmol/L vs mg/dL) — **always report both**, and state the conversion factor used (1 mmol/L = 18.0 mg/dL) rather than assuming the reader will convert.
- **GRADE certainty on every interventional claim** (treatment thresholds, dextrose gel, feeding protocols, screening protocols) — High/Moderate/Low/Very low, with a one-line reason naming the downgrade domain (risk of bias, imprecision, indirectness, inconsistency, publication bias).
- **Directness flagged explicitly.** State whether evidence is from term, late-preterm, moderate-preterm, very preterm, or extremely preterm infants, and whether a claim applied to one group is being extrapolated to another. This is the central methodological problem in this topic — the major RCT evidence (CHYLD, Sugar Babies, hPOD) enrolled **late preterm and term infants at risk of hypoglycaemia**, not the extremely preterm population that dominates a Level 3 NICU caseload. Do not let this distinction blur.
- **Nulls get equal billing.** Several of the seed trials below are neutral or show unexpected harms in secondary outcomes (e.g., dextrose gel and visual-motor scores) — report these with the same prominence as positive findings.
- **Say when evidence is weak or absent.** For the extremely preterm-specific glucose threshold question in particular, state plainly if the literature search does not surface a modern RCT-based answer — this is a known and clinically important evidence gap, not a search failure.
- **Write to disk incrementally.** Append to `01-search-log/searches.md` as each search runs, not at the end. Do not hold a domain's findings in context alone.
- **Grey literature labelled separately.** BAPM, NICE, and RCPCH documents are guidance, not peer-reviewed primary evidence. Cite them as such and never fold them into a peer-reviewed study count.

## 3. Research question

**Primary question:** How should hypoglycaemia be defined, detected, and managed in term and preterm infants in the first days of life and beyond, and what evidence underpins current UK (BAPM) practice?

**Secondary questions:**
1. What operational definition(s) of neonatal hypoglycaemia exist, and how (and why) do they differ from a statistical/population definition?
2. What glucose threshold defines hypoglycaemia in a term infant in the first 72 hours, and does the threshold change after 72 hours?
3. What threshold(s) are used or proposed for preterm infants, and is there a single agreed value or a gestation/postnatal-age-dependent range?
4. Is hypoglycaemia diagnosed on a point-of-care (bedside) glucometer reading, or does diagnosis require laboratory/blood gas confirmation? At what point-of-care reading does device inaccuracy become clinically important enough to mandate laboratory confirmation before acting?
5. What does the BAPM Framework for Practice recommend for term infants in the first 48 hours, and what is the primary evidence (trial or cohort) underpinning each element of that pathway (screening threshold, treatment threshold, escalation steps)?
6. At what glucose level, and over what duration/frequency, does concern rise for preterm infants specifically, and what is the long-term neurodevelopmental outcome evidence for preterm-specific thresholds (as distinct from the term/late-preterm RCT evidence)?
7. What long-term neurodevelopmental outcomes are attributable to neonatal hypoglycaemia in term infants, and how strong/consistent is the dose-response relationship (severity, recurrence, "occult"/undetected hypoglycaemia)?
8. In an infant presenting with hypoglycaemia and seizures, is MRI indicated, what is the expected injury pattern, and what does early MRI add to prognosis beyond the biochemical severity of the hypoglycaemic episode?
9. Which infants with neonatal hyperglycaemia require long-term neurodevelopmental follow-up, and what is the evidence base for that recommendation?
10. (Cross-cutting) Where do UK guidance (BAPM/NICE) and the trial evidence base agree, and where is there a recognised tension or open controversy (e.g., "permissive hypoglycaemia" debate, screening vs diagnostic thresholds)?

## 4. Conceptual framing to establish first

Before searching, establish and state clearly in the synthesis:

- **The screening/diagnostic threshold distinction.** A recurring theme in the primary literature (see seed set) is that operational thresholds for *initiating clinical action* are deliberately set well above the level at which neuroglycopenic injury is believed to occur, by analogy with phototherapy thresholds for jaundice. Confusing "the threshold at which we intervene" with "the threshold at which harm occurs" is a common source of clinical and educational error — the synthesis must keep these conceptually separate throughout.
- **Units.** UK practice uses mmol/L; most North American and much older literature uses mg/dL. State both throughout (2.6 mmol/L = 47 mg/dL; 2.0 mmol/L = 36 mg/dL).
- **"Hypoglycaemia" vs "neuroglycopenia".** There is no direct clinical test for neuroglycopenia (brain glucose deprivation) — blood/plasma glucose is a proxy. This distinction underlies why screening for neonatal hypoglycaemia does not cleanly satisfy classic screening-test principles (see Alsweiler et al. 2022 in the seed set) and should be stated explicitly when discussing detection strategy.
- **Time-windows that matter clinically:** (a) first hours of transitional physiology (birth to ~4h), (b) first 48–72h (the window BAPM's framework and most RCTs target), (c) after 72h/"persistent or recurrent" hypoglycaemia (a different differential diagnosis — congenital hyperinsulinism, metabolic disease, endocrinopathy — and a different management pathway, typically requiring critical sample and specialist endocrine input, which the synthesis should flag as out of primary scope but signpost).

## 5. Domain-by-domain investigation

Give each domain the same five-part internal structure so the outputs are mergeable: **(a)** what the definition/threshold/finding is and how it was derived; **(b)** why (physiological or methodological rationale); **(c)** what evidence supports it (trial/cohort, with GRADE label); **(d)** where the evidence is weak, contested, or extrapolated; **(e)** the practical implication for a UK Level 3 unit.

### Domain A — Definitions and operational thresholds (term, 0–72h and beyond; preterm)
- Trace the definition from Cornblath et al. 2000 "operational thresholds" framing through to the current BAPM 2017 Framework threshold(s).
- Establish explicitly: does the BAPM threshold change between the first 72 hours and thereafter? Search specifically for "prolonged" or "persistent" transitional hypoglycaemia (defined in some literature as hypoglycaemia persisting beyond 48–72h) as a distinct, higher-concern category with its own differential diagnosis.
- Establish whether a single numeric threshold is used across all gestational ages in BAPM guidance, or whether preterm infants are handled separately/by extrapolation.
- Include the NNRD-based real-world evaluation of the BAPM framework's impact on term admissions (seed set) as evidence of what the guidance *achieves* in practice, not just what it recommends.

### Domain B — Point-of-care glucometer vs laboratory/blood gas confirmation
- Establish the accuracy characteristics of bedside glucometers/reagent strips in neonates specifically (they are validated primarily in adults; neonatal accuracy, especially at low glucose values and in the presence of high haematocrit/bilirubin, is a recognised limitation).
- Identify the specific point-of-care reading (or range) below which UK/BAPM guidance and the device-accuracy literature recommend laboratory or blood gas analyser confirmation before treatment escalation, and whether this differs from the level at which a point-of-care reading alone is considered actionable for immediate feeding/first-line treatment.
- Search for CLSI POCT12-A3 standards and any UK-specific point-of-care glucose testing guidance (as grey literature) alongside the peer-reviewed accuracy studies.
- State clearly whether "diagnosis" of hypoglycaemia for governance/audit purposes should be made on point-of-care or laboratory-confirmed values, and what BAPM says on this point specifically.

### Domain C — BAPM core management pathway for term infants, first 48 hours, with evidence base
- Extract the BAPM 2017 Framework pathway element by element (risk-factor identification, feeding-based first-line management, screening timing/frequency, treatment threshold, escalation to IV dextrose, discharge criteria).
- For **each** element, identify the primary evidence cited or citable (Cornblath 2000, CHYLD, Sugar Babies dextrose gel trials, and any others found in scoping/search) and grade it.
- Explicitly address the "permissive hypoglycaemia" controversy — search for and include the critical commentary literature (see seed set: "Thresholds for hypoglycaemic screening — a cause for concern?") that argues the BAPM/CHYLD-derived threshold undertreats risk relative to older, more conservative UK practice, and present both sides with their evidentiary basis.
- Include dextrose gel as first-line/adjunct treatment specifically — search for the Cochrane review status of buccal dextrose gel and the NNRD/national uptake data if available.

### Domain D — Preterm-specific thresholds and long-term outcome evidence
- This is the domain most likely to be evidence-poor for extremely preterm infants specifically — say so plainly if confirmed.
- Establish what evidence exists for glucose thresholds specifically in preterm (all severities) versus extrapolation from the term/late-preterm RCT base.
- The seed set contains a landmark small-for-gestational-age **preterm-specific** cohort (Duvanel et al. 1999) showing recurrent hypoglycaemia associated with reduced head circumference and lower psychometric scores to 5 years — trace how much subsequent, more modern evidence (2015 onward) exists specifically for preterm/very preterm/SGA preterm infants, and whether it confirms, refines, or contradicts this.
- Search specifically for evidence in infants <32 weeks and <28 weeks gestation — flag if the search returns predominantly late-preterm (34–36 weeks) data being generalised downward.
- Address glycaemic variability/lability as a preterm-relevant concept distinct from a single threshold breach (see seed set: continuous/interstitial glucose monitoring literature).

### Domain E — Term long-term neurodevelopmental outcomes
- Synthesise the CHYLD and Sugar Babies follow-up literature (2 years, 4.5 years, 9–10 years / mid-childhood, school age) as the core evidence base.
- Report the dose-response findings specifically: severity (single vs severe episode), recurrence (≥3 episodes), and "occult"/clinically undetected (interstitial-only) hypoglycaemia, and which outcome domains (executive function, visual-motor function, global neurosensory impairment) are and are not affected according to the trial evidence.
- Report the mid-childhood/school-age data on educational achievement and visual processing specifically, including the unexpected dextrose-gel-associated visual-processing signal — report this as a null/adverse-signal finding with equal prominence, not as a footnote.
- Report structural correlates (caudate volume) where available and state clearly whether these have been shown to explain the behavioural/cognitive associations or remain a parallel, not-yet-linked finding.

### Domain F — Hypoglycaemia + seizure: is MRI indicated?
- Establish the injury pattern literature (predominantly posterior/parieto-occipital, but note the broader pattern described by Burns et al. 2008 including white matter, basal ganglia/thalamic, and haemorrhagic patterns not confined to the posterior region).
- Address directly: does early MRI change management or add prognostic information beyond clinical/biochemical severity in a hypoglycaemic infant who has seized? Search specifically for evidence on the *predictive value* of MRI timing and findings for neurodevelopmental outcome (Burns et al. is central here), versus MRI's role in excluding alternative/coexisting pathology (HIE, stroke, structural lesion, metabolic/genetic disease).
- Note the practical corollary: MRI findings in hypoglycaemic seizure can mimic or coexist with arterial ischaemic stroke (middle cerebral artery territory infarction is described in the seed set) — flag this as a reason MRI may be indicated for differential diagnosis even where prognosis is thought to track glucose severity.
- State a working UK-practice-relevant recommendation on **when** MRI should be requested (timing after the event, and whether every hypoglycaemic seizure warrants imaging or only symptomatic/severe/prolonged cases) and support it with the evidence located, flagging clearly if this recommendation is extrapolated from small, heterogeneous, largely non-UK case series rather than a guideline-level source.

### Domain G — Hyperglycaemia and long-term follow-up
- Establish the operational definition(s) of neonatal hyperglycaemia in use (search confirmed one recent proposed cut-off >150–180 mg/dL in the seed set — verify, and check for a UK/BAPM-specific figure or NICE guidance).
- Identify which populations are described in the literature as needing long-term follow-up after neonatal hyperglycaemia: extremely preterm infants requiring insulin therapy, infants with neonatal encephalopathy who develop secondary hyperglycaemia, and any others surfaced by the search.
- Report the "U-shaped" dysglycaemia-outcome relationship described in the seed review (Lagacé & Tam 2024) and trace it back to its primary supporting studies rather than relying on the secondary review alone.
- Address glycaemic variability/lability specifically for hyperglycaemia as well as hypoglycaemia, since several sources treat this as the more clinically important construct than either threshold in isolation.

## 6. Cross-cutting synthesis

This is where the user's practical emphasis lives — build these explicitly, not just as domain summaries:

1. **A single reference table**: gestation category (term / late preterm / preterm / very preterm / extremely preterm) × time window (0–4h / 4–48h / 48–72h / >72h) × screening threshold × treatment threshold × source (BAPM / trial-derived / extrapolated), with a column stating directness of evidence for each cell.
2. **A point-of-care-vs-laboratory decision point**: the specific glucometer reading below which confirmation is recommended, stated once, clearly, with its source.
3. **An evidence-strength summary** for the BAPM 48-hour term pathway: which elements are RCT-supported (dextrose gel, treatment threshold from CHYLD), which are consensus/operational (Cornblath-style pragmatic thresholds), and which are unsupported by direct RCT evidence and are extrapolated from physiological reasoning or cohort data alone.
4. **The permissive-hypoglycaemia controversy**, presented as a genuine open disagreement between two evidence-literate positions, not resolved artificially.
5. **A preterm evidence-gap statement**: an explicit paragraph stating what is and is not known for very/extremely preterm infants specifically, since this is the population most relevant to a Level 3 NICU and the domain most likely to be thin.
6. **An MRI-in-hypoglycaemic-seizure practical recommendation**, evidence-graded.
7. **A hyperglycaemia follow-up population list**, with the supporting evidence for each group named.

## 7. Search strategy

Run PubMed and Consensus in parallel per the standing rules. Build in blocks, combine explicitly, and log every search verbatim in `01-search-log/searches.md` as it runs — do not reconstruct the log afterward.

### 7.1 Core concept blocks (reuse across domains)

```
#1 Population — term/general neonate
("infant, newborn"[Mesh] OR neonat*[tiab] OR newborn*[tiab] OR "new born"[tiab] OR "new-born"[tiab])

#2 Population — preterm
("infant, premature"[Mesh] OR preterm*[tiab] OR premature*[tiab] OR "very low birth weight"[tiab] OR VLBW[tiab]
 OR "extremely low birth weight"[tiab] OR ELBW[tiab] OR "extremely preterm"[tiab] OR "very preterm"[tiab])

#3 Hypoglycaemia
("hypoglycemia"[Mesh] OR hypoglycaemia*[tiab] OR hypoglycemia*[tiab] OR "low blood glucose"[tiab]
 OR "low blood sugar"[tiab] OR neuroglycopeni*[tiab])

#4 Hyperglycaemia
("hyperglycemia"[Mesh] OR hyperglycaemia*[tiab] OR hyperglycemia*[tiab])

#5 Neurodevelopmental outcome
("child development"[Mesh] OR "neurodevelopmental disorders"[Mesh] OR neurodevelopment*[tiab]
 OR "cognitive outcome*"[tiab] OR "long-term outcome*"[tiab] OR "long term outcome*"[tiab]
 OR "school age"[tiab] OR "mid-childhood"[tiab])

#6 Point-of-care / device accuracy
("point-of-care testing"[Mesh] OR "point of care"[tiab] OR glucometer*[tiab] OR "reagent strip*"[tiab]
 OR "test strip*"[tiab] OR "blood gas"[tiab] OR "blood gas analys*"[tiab] OR "blood gas analyz*"[tiab]
 OR "bedside glucose"[tiab] OR "capillary glucose"[tiab])

#7 Guidance/framework
(guideline*[tiab] OR "framework for practice"[tiab] OR BAPM[tiab] OR consensus[tiab] OR "operational threshold*"[tiab])

#8 Seizure / neuroimaging
(seizure*[tiab] OR convulsion*[tiab] OR "magnetic resonance imaging"[Mesh] OR MRI[tiab] OR neuroimaging[tiab]
 OR "brain injury"[tiab] OR "cerebral injury"[tiab])

#9 Treatment — dextrose gel
("glucose"[Mesh] OR dextrose[tiab] OR "dextrose gel"[tiab] OR "buccal dextrose"[tiab] OR "oral dextrose gel"[tiab])
```

### 7.2 Numbered combinations to run

```
1.  #1 AND #3 AND #7                                   → term definitions/guidance (Domain A)
2.  #2 AND #3 AND #7                                   → preterm definitions/guidance (Domain A/D)
3.  #1 AND #3 AND #6                                   → POC glucometer accuracy, term (Domain B)
4.  #2 AND #3 AND #6                                   → POC glucometer accuracy, preterm (Domain B)
5.  #1 AND #3 AND #9 AND #5                             → dextrose gel + neurodevelopmental follow-up (Domain C/E)
6.  #1 AND #3 AND #5                                    → term hypoglycaemia + ND outcome, broad (Domain E)
7.  #2 AND #3 AND #5                                    → preterm hypoglycaemia + ND outcome (Domain D)
8.  #1 AND #3 AND #8                                    → hypoglycaemia + seizure/MRI, term (Domain F)
9.  #2 AND #3 AND #8                                    → hypoglycaemia + seizure/MRI, preterm (Domain F)
10. #1 AND #4 AND #5                                    → term hyperglycaemia + ND outcome (Domain G)
11. #2 AND #4 AND #5                                    → preterm hyperglycaemia + ND outcome (Domain G)
12. #3 AND #5 without #1/#2, restricted to SR/RCT filter → transferable indirect evidence check
13. citation chase (both directions) on every included RCT/cohort from searches 1–11
```

### 7.3 Filters

- No date limit for definitional/foundational searches (Cornblath 2000, Duvanel 1999, Burns 2008 are all pre-2015 and must not be filtered out).
- For neurodevelopmental-outcome searches, no language filter beyond English — state this as a limitation.
- Do not filter on full-text availability.
- Use `[tiab]` as default; widen to `[tw]` only if a specific combination returns implausibly few hits (test against the seed set below — search 6 should retrieve McKinlay et al. 2015 NEJM (PMID 26465984) and McKinlay et al. 2017 JAMA Pediatr (PMID 28783802); if it doesn't, the block needs repair before proceeding).

### 7.4 Consensus queries (claim-level checking, run and log separately — not reproducible in the same sense as PubMed)

- "Is neonatal hypoglycaemia associated with long-term neurodevelopmental impairment in term infants?"
- "Does treating neonatal hypoglycaemia with dextrose gel improve neurodevelopmental outcomes?"
- "What blood glucose threshold defines hypoglycaemia in preterm infants?"
- "Are point-of-care glucose meters accurate at low glucose concentrations in neonates?"
- "Is MRI indicated after neonatal hypoglycaemic seizures?"
- "What glucose level defines neonatal hyperglycaemia and which infants need follow-up?"
- "Is there evidence that recurrent hypoglycaemia is more harmful than a single severe episode in neonates?"

### 7.5 Grey literature (search web, not PubMed; label clearly, never merge into peer-reviewed count)

- BAPM: "Identification and Management of Neonatal Hypoglycaemia in the Full Term Infant — A Framework for Practice" (2017) — full text at bapm.org; confirm whether a newer edition has superseded 2017 before treating it as current.
- NICE guidance on neonatal hypoglycaemia (check NG or CG series; NICE NG194/postnatal care and any diabetes-in-pregnancy guideline cross-references, since infants of diabetic mothers are a major risk-factor group).
- RCPCH / national neonatal audit programme (NNAP) — check for any published standard on hypoglycaemia admission or screening.
- CLSI POCT12-A3 (point-of-care glucose testing standard) — confirm current edition.

## 8. Evidence matrix specification

Build on `assets/extraction-template.csv` (columns: id, author_year, country, setting, level_of_care, design, n_patients, n_events, n_clinicians, population_detail, intervention, comparator, outcomes_measured, primary_result, effect_size, ci_lower, ci_upper, p_value, secondary_results, ascertainment_method, rob_tool, rob_domains, rob_overall, directness, grade_certainty, grade_reason, funding, conflicts, key_limitation, abstract_only, pmid, doi, notes).

Add these topic-specific columns:
- `gestational_age_range` (explicit weeks, not just "preterm"/"term" label)
- `glucose_threshold_used` (value in both mmol/L and mg/dL)
- `glucose_measurement_method` (point-of-care / laboratory / interstitial CGM / mixed)
- `outcome_timepoint` (age at follow-up assessment)
- `dose_response_reported` (Y/N — whether severity/recurrence gradient was analysed)

## 9. Deliverables

1. `00-protocol/protocol.md` — scope statement and the four framing questions from §4, confirmed.
2. `01-search-log/searches.md` — every search, verbatim, with hit counts (deliverable in its own right).
3. `02-extraction/extraction.csv` — populated evidence matrix.
4. `03-synthesis/synthesis.md` — domain-by-domain synthesis (§5) plus the cross-cutting synthesis (§6), including the reference table.
5. `05-references/could-not-verify.md` — anything that failed verification (deliverable in its own right, even if empty).
6. A final **plain-language threshold reference table** (markdown, suitable for pinning to a unit guideline or teaching slide) summarising gestation × time-window × threshold × source × evidence strength.

## 10. Candidate seed literature — VERIFY EVERY ONE

**Status note:** the studies below were retrieved and their PMID/DOI confirmed via the PubMed MCP during scoping for this brief (2026-08-27). They are a strong starting point, not a finished reference list — the executing agent must still independently re-retrieve and re-verify each one before it enters any file, per the citation-integrity rule (a scoping-session verification does not substitute for the executing session's own retrieval). Treat anything below as a lead, not a citation, until re-confirmed.

**Definitions, thresholds, and guidance impact**
- Cornblath M, Hawdon JM, Williams AF, et al. "Controversies regarding definition of neonatal hypoglycemia: suggested operational thresholds." *Pediatrics* 2000. PMID 10790476 — the foundational operational-threshold paper; UK co-authors (Hawdon) link directly to BAPM's later framework.
- Nezafat Maldonado B, Conti-Ramsden F, van Hasselt TJ, et al. "Term neonatal admissions for hypoglycaemia in England and Wales, 2012–2020: a population-based study using the National Neonatal Research Database." *Arch Dis Child Fetal Neonatal Ed* 2026. PMID 41338963 — real-world before/after evaluation of the BAPM 2017 Framework's impact on admissions; directly useful for the governance angle.
- A short critical commentary titled (approximately) "Thresholds for hypoglycaemic screening — a cause for concern?" was identified responding directly to the BAPM Framework and arguing the lowered screening threshold under-protects at-risk infants relative to prior UK practice — locate this properly via PubMed/journal search (it surfaced via web search, not yet PubMed-verified) and use it to represent the "permissive hypoglycaemia" critique fairly.
- Alsweiler JM, Heather N, Harris DL, McKinlay CJD. "Application of the screening test principles to screening for neonatal hypoglycemia." *Front Pediatr* 2022. PMID 36568425 — directly addresses the screening-vs-diagnostic-threshold conceptual problem in §4.

**Term/late-preterm RCT and cohort evidence (CHYLD and Sugar Babies programmes — Auckland group)**
- McKinlay CJD, Alsweiler JM, Ansell JM, et al. "Neonatal Glycemia and Neurodevelopmental Outcomes at 2 Years." *N Engl J Med* 2015. PMID 26465984 — CHYLD study primary 2-year outcome; central to Domain E.
- McKinlay CJD, Alsweiler JM, Anstice NS, et al. "Association of Neonatal Glycemia With Neurodevelopmental Outcomes at 4.5 Years." *JAMA Pediatr* 2017. PMID 28783802 — CHYLD 4.5-year follow-up; dose-response by severity/recurrence/occult hypoglycaemia.
- Kennedy E, Nivins S, Thompson B, McKinlay CJD, Harding JE. "Neurodevelopmental correlates of caudate volume in children born at risk of neonatal hypoglycaemia." *Pediatr Res* 2022. PMID 36513807 — structural MRI correlate at 9–10 years.
- May RW, Gamble GD, McKinlay CJD, Harris D, Harding JE. "Measures of neonatal glycemia from blood glucose concentrations and neurodevelopmental outcomes at 2 years." *Pediatr Res* 2026. PMID 42050117 — very recent; glycaemic variability vs dichotomous threshold measures — check publication status (may be online-ahead-of-print) before treating as final.
- Harris DL, Alsweiler JM, Ansell JM, et al. "Outcome at 2 Years after Dextrose Gel Treatment for Neonatal Hypoglycemia: Follow-Up of a Randomized Trial." *J Pediatr* 2015. PMID 26613985 — Sugar Babies 2-year follow-up.
- Harris DL, Gamble GD, Harding JE. "Outcome at 4.5 years after dextrose gel treatment of hypoglycaemia: follow-up of the Sugar Babies randomised trial." *Arch Dis Child Fetal Neonatal Ed* 2022. PMID 35940872.
- St Clair SL, Dai DWT, Harris DL, et al. "Mid-Childhood Outcomes after Dextrose Gel Treatment of Neonatal Hypoglycaemia: Follow-Up of the Sugar Babies Randomized Trial." *Neonatology* 2022. PMID 36516806 — 9–10 year outcomes; note the visual-processing adverse signal (report as null/adverse, not omitted).

**hPOD / pre-hPOD (prophylactic dextrose gel) programme**
- Edwards T, Alsweiler JM, Crowther CA, et al. "Prophylactic Oral Dextrose Gel and Neurosensory Impairment at 2-Year Follow-up of Participants in the hPOD Randomized Trial." *JAMA* 2022. PMID 35315885 — note the motor-delay secondary-outcome signal in the dextrose group.
- Wei X, Franke N, Alsweiler JM, et al. "Dextrose gel prophylaxis for neonatal hypoglycaemia and neurocognitive function at early school age: a randomised dosage trial." *Arch Dis Child Fetal Neonatal Ed* 2024. PMID 38307710.
- Wei X, Franke N, Alsweiler JM, et al. "Neonatal Hypoglycemia and Neurocognitive Function at School Age: A Prospective Cohort Study." *J Pediatr* 2024. PMID 38815750.

**Preterm-specific**
- Duvanel CB, Fawer CL, Cotting J, Hohlfeld P, Matthieu JM. "Long-term effects of neonatal hypoglycemia on brain growth and psychomotor development in small-for-gestational-age preterm infants." *J Pediatr* 1999. PMID 10190926 — the landmark preterm/SGA-specific cohort; central to Domain D and likely the single most important paper for the preterm threshold question given the thinness of modern preterm-specific RCT evidence.
- Palazzo M, Correani A, Bonanni M, et al. "Early hypoglycemia is not an independent risk factor for 2-year cognitive impairment in small for gestational age preterm infants of less than 32 weeks." *Eur J Pediatr* 2024. PMID 39707054 — modern, <32-week-specific, and a **null** finding — must be reported alongside Duvanel with equal prominence, not subordinated to it.
- Lagacé M, Tam EWY. "Neonatal dysglycemia: a review of dysglycemia in relation to brain health and neurodevelopmental outcomes." *Pediatr Res* 2024. PMID 38972961 — secondary review proposing operational definitions (≤47 mg/dL hypoglycaemia; >150–180 mg/dL hyperglycaemia) and the "U-shaped" dysglycaemia-outcome relationship; use to identify primary sources, don't cite the review's claims without tracing them back.
- Kebede SD, Kassaw A, Aytenew TM, Agmas K, Kefale D. "Prevalence of prolonged transitional neonatal hypoglycemia and associated factors in Ethiopia: A systematic review and meta-analysis." *PLoS One* 2025. PMID 39913386 — defines "prolonged transitional hypoglycaemia" as persistence >48–72h; useful for Domain A's post-72h question, but note the population (Ethiopian cohorts) is not directly UK-generalisable — flag directness explicitly.

**Hypoglycaemic seizure and MRI**
- Burns CM, Rutherford MA, Boardman JP, Cowan FM. "Patterns of cerebral injury and neurodevelopmental outcomes after symptomatic neonatal hypoglycemia." *Pediatrics* 2008. PMID 18595988 — the central paper for Domain F; note the lead author's affiliation (Hammersmith Hospital, Imperial College Healthcare NHS Trust) — same trust as this brief's intended use, which may be worth noting in the final document. Establishes that MRI pattern predicted outcome better than glucose severity/duration alone.
- Fong CY, Harvey AS. "Variable outcome for epilepsy after neonatal hypoglycaemia." *Dev Med Child Neurol* 2014. PMID 24861161 — later epilepsy phenotype and its variability.
- Gu MH, Amanda F, Yuan TM. "Brain Injury in Neonatal Hypoglycemia: A Hospital-Based Cohort Study." *Clin Med Insights Pediatr* 2019. PMID 31447599 — notes duration of hypoglycaemia, not lowest glucose value, tracked with abnormal MRI.
- Kapoor D, Sidharth, Sharma S, et al. "Electroclinical spectrum of childhood epilepsy secondary to neonatal hypoglycemic brain injury in a low resource setting: A 10-year experience." *Seizure* 2020. PMID 32446209 — large case series; low-resource setting, flag directness.
- Additional MRI case-series/case-report material was identified (PMIDs 24798709, 18433524, 17953809, 37383118) — lower individual evidentiary weight (small series, case reports, non-English with abstract only for two) but useful for describing the injury-pattern phenotype; do not let these substitute for the Burns 2008 cohort as the primary evidence source.

**Point-of-care glucose testing accuracy** — a further targeted PubMed search returned candidate papers (PMIDs 42493372, 40818947, 39206021, 37248091, 30829013, 29895035, 20574734, 9566281, 9325505) that were identified but **not yet read or metadata-confirmed individually** — this is a genuine gap in the scoping and the first priority sub-search for the executing session. Do not assume these are all relevant; screen titles/abstracts properly.

**Not yet searched — priority gaps for the executing session**
- Cochrane systematic review status of buccal/oral dextrose gel for treatment (as distinct from prophylaxis) of confirmed neonatal hypoglycaemia.
- NICE guidance cross-reference (postnatal care guideline and any diabetes-in-pregnancy guideline provisions on infant glucose monitoring).
- Continuous/interstitial glucose monitoring literature in preterm infants specifically (glycaemic variability as a preterm-relevant construct — Domain D/G).
- Insulin-treated hyperglycaemia in extremely preterm infants and its neurodevelopmental follow-up literature specifically (the COIN trial and related preterm insulin-therapy trials were not retrieved in scoping and should be searched directly).
- A dedicated search for the current (post-2017) status of the BAPM Framework — confirm whether it has been updated, reaffirmed, or superseded, since guidance currency matters for a governance document.

## 11. Quality control checklist

Report against these explicitly in the final synthesis — an unreported check reads as a skipped one:

- [ ] Every claim carries a PMID/DOI verified this session (not carried over from this brief's seed list without re-verification).
- [ ] Every mmol/L value is paired with its mg/dL equivalent (and vice versa).
- [ ] Every interventional claim carries a GRADE label with a named downgrade domain.
- [ ] Every claim states whether it is direct evidence for the population under discussion or extrapolated, and from which population.
- [ ] The preterm/very preterm evidence gap is stated explicitly, not papered over with term-derived extrapolation presented as preterm-specific evidence.
- [ ] Null and adverse secondary-outcome findings (dextrose gel visual-processing and motor signals; Palazzo 2024 null finding) are reported with equal prominence to positive findings.
- [ ] The permissive-hypoglycaemia controversy is presented as a genuine two-sided disagreement, not resolved by fiat.
- [ ] Grey literature (BAPM/NICE/RCPCH) is clearly labelled and never merged into the peer-reviewed evidence count.
- [ ] The could-not-verify list is produced even if empty.
- [ ] The final reference table (gestation × time-window × threshold × source × evidence strength) is present and internally consistent with the domain sections.

## 12. Output style

Consultant-level register. Assume the reader is a practising neonatologist who needs the evidence, the mechanism, and the uncertainty — not a primer on what hypoglycaemia is. Prose over bullets in the domain synthesis sections; tables where they genuinely aid comparison (especially the cross-cutting reference table in §6.1). No filler, no restating the question, no motivational framing. State plainly, in the relevant section, wherever the evidence is thin, contested, or extrapolated — hedging into vagueness is not acceptable, but neither is false confidence where the literature does not support it.
