# Deep Research Brief — Human Milk (Breast Milk) Fortification in Preterm Infants

**Target use:** Run in a fresh Claude Code session with **PubMed MCP** and **Consensus MCP** enabled. Before starting, run `claude mcp list` and confirm both are present — they are configured separately from chat and are not automatically available in Code.
**Intended output:** A phase-1–3 evidence base (search log, deduplicated hit list, extraction table, GRADE-labelled synthesis) that a later session will turn into a narrative review manuscript. This brief does not write the manuscript.
**Clinical framing defaults:** UK (NICE, BAPM, RCPCH), cross-checked against ESPGHAN, AAP, and Cochrane Neonatal where relevant.
**Track:** Narrative review (systematised — search must be documented and reproducible even though synthesis is narrative, not meta-analytic).
**Target journal:** Not yet fixed. Candidates to discuss with the requester once synthesis is complete: *Archives of Disease in Childhood – Education & Practice* (fits the requester's existing ADC record and this topic's practice-change framing), *Seminars in Fetal & Neonatal Medicine*, or *Journal of Perinatology*. This does not change the search strategy below and can be decided after phase 4.

---

## 1. Role

You are acting as a consultant-neonatologist-level evidence synthesiser. The reader of your eventual output already knows neonatal nutrition; they need the evidence, the mechanisms, the certainty, and the disagreements — not a primer. Your output at the end of this brief is a **referenced synthesis with a documented, reproducible search**, not an essay written from general knowledge. Every claim that ends up in the synthesis must trace to a study you retrieved and can cite by PMID/DOI.

## 2. Non-negotiable rules

Copy these into `CLAUDE.md` at project start (see Running Instructions) and re-read them at the start of every session — they degrade first when context gets long.

- **Nothing enters any file without a verified PMID or DOI retrieved this session.** Do not use a citation you recall from training; retrieve it fresh.
- Unverifiable references go on a "could not verify" list and are **dropped**, never hedged into the text with a soft qualifier.
- **Numbers are transcribed exactly as reported** — effect sizes, CIs, denominators, percentages. Never re-derive, round, or convert units silently. Mark `[abstract only]` where full text was not available.
- **Every interventional claim carries a GRADE label** (High/Moderate/Low/Very low) with a one-line reason naming the downgrade domain (risk of bias, imprecision, inconsistency, indirectness, publication bias).
- **Flag directness.** State plainly when a finding is extrapolated from a different population (e.g., term infants, adjacent GI conditions) rather than the preterm/VLBW population this brief targets.
- **Null and non-replication findings get equal billing.** This field has several underpowered positive single-centre reports and at least a few large trials/Cochrane reviews that found "no difference" — the nulls are often the most clinically useful finding and must not be buried under positive small studies.
- **Write to disk incrementally.** Append to the search log as each search runs. Do not hold a domain's findings in context only.
- **Say plainly when evidence is weak or absent.** "The evidence for X is limited to two small trials with serious risk of bias" is a finding, not a failure to find something better.

## 3. Research question

**Primary question (PICO):** In preterm and very-low-birth-weight infants fed human milk (Population), what is the evidence for the timing, dose, product choice, and safety of human milk fortification (Intervention), compared with no/delayed/alternative fortification strategies (Comparator), on short-term growth and tolerance and long-term neurodevelopmental outcomes (Outcome)?

**Secondary questions** (each becomes one domain in Section 5):

1. At what postnatal age or enteral feed volume should fortification be initiated, and is there trial evidence favouring a specific volume threshold (e.g., 20–40 mL/kg/d "early" vs 80–100 mL/kg/d "standard/late")?
2. What are the absolute and relative contraindications to initiating or continuing fortification — specifically antenatal absent/reversed end-diastolic umbilical artery flow (AEDF/REDF) and small-for-gestational-age/growth-restricted infants?
3. What is the evidence on the safety and timing of introducing or resuming fortification after surgical NEC or spontaneous intestinal perforation (SIP)?
4. What is the evidence that fortification improves short-term growth (weight, length, head-circumference velocity) compared with unfortified human milk?
5. What is the long-term neurodevelopmental outcome evidence for fortification — by fortifier type, timing, and dose?
6. What is the evidence that fortification causes constipation and other GI side effects (feeding intolerance, abdominal distension, metabolic acidosis), and what is the mechanistic link to feed osmolality?
7. Is there evidence to support discharging infants home on fortified milk (post-discharge fortification), and what outcomes does it affect?
8. What is the evidence for concentrated/high-dose, liquid, or targeted/adjustable fortification strategies compared with standard fixed-dose powdered fortifier?

## 4. Conceptual framing to establish first

**Resolve the "BMF" ambiguity before searching — this is a real trap in this literature.** The requester uses "BMF" colloquially to mean *breast milk fortifier* (synonymous with the more standard abbreviation **HMF**, human milk fortifier). However, several papers in this exact field use **"BMF" to mean *bovine milk-based fortifier***, as the explicit comparator to "HMBF" (human-milk-based fortifier) — e.g. the Nordic N-forte trial (Jensen et al., *eClinicalMedicine* 2024) and a 2026 *Archives of Disease in Childhood* network meta-analysis both define BMF this way. Do not let this collapse two different concepts in the synthesis: (a) "should we fortify at all / when / how much" and (b) "if fortifying, bovine-derived vs human-milk-derived fortifier." Use **HMF** as the working abbreviation for "human/breast milk fortifier" throughout the brief and reserve **BMF** exclusively for "bovine milk-based fortifier" when quoting a paper that uses it that way. State this convention explicitly in the eventual synthesis so a reader isn't misled either.

**Other terms to fix early:**
- **"Early" vs "late" fortification** has no single agreed definition. Cochrane (Thanigainathan 2019) used early = <100 mL/kg/d feeds **or** <7 days postnatal age; late = ≥100 mL/kg/d **or** ≥7 days. Individual trials have used thresholds as low as 20 mL/kg/d (Shah 2016) and as high as 100 mL/kg/d (most "standard" practice). Record each trial's actual definition in the extraction table rather than forcing it into a binary.
- **Fortifier types** to keep distinct in extraction: powdered bovine-derived HMF; liquid/acidified bovine-derived HMF; human-milk-derived fortifier (HMBF, e.g. Prolacta-type products); concentrated liquid preterm formula used *as* a fortifier; targeted/adjustable/individualised fortification (blood-urea-nitrogen-adjusted or milk-analyser-based).
- **AEDF/REDF** — antenatal Doppler findings in the umbilical artery (absent or reversed end-diastolic flow), a marker of placental insufficiency and a well-established, distinct risk factor for feeding intolerance, NEC and SIP, independent of birthweight/gestation. Keep separate from the broader "IUGR/SGA" category, which is defined postnatally by birthweight centile and is a larger, more heterogeneous group.
- **SIP vs NEC** are distinct pathologies (focal, typically earlier-onset, often associated with early indomethacin/steroid exposure for SIP vs a more diffuse ischaemic-inflammatory process for NEC) with separate nutritional literatures; do not merge them in the extraction table even though many papers report them as a combined outcome.

## 5. Domain-by-domain investigation

For each domain below, use this five-part structure so the domains are mergeable into one synthesis later: **(a)** what the trials/practice actually show and how consistent it is; **(b)** the physiological or mechanistic rationale; **(c)** what's been tried (trial designs, comparators); **(d)** where the evidence fails to settle the question (gaps, conflicting findings, populations excluded from trials); **(e)** a one-line note on relevance to a UK level-3 NICU setting.

### Domain 1 — Timing/volume threshold for initiation
Known landmarks to locate and formally extract (do not rely on this list — retrieve and verify): Cochrane review of early vs late fortification (Thanigainathan et al. 2019, and its predecessor systematic review by Alyahya et al. 2019); a 2020 meta-analysis (Basu et al.) reporting longer hospital stay with early fortification; the Shah 2016 RCT (20 vs 100 mL/kg/d); more recent RCTs assessing fortification from day 2–7 of life against fat-free mass and other body-composition endpoints (Salas et al., multiple 2023/2025 trials). Distinguish trials that manipulate *volume threshold* from those that manipulate *postnatal day* — some do both simultaneously and confound the two.

### Domain 2 — Contraindications: AEDF/REDF and IUGR/SGA
This domain sits at the intersection of two separate trial traditions: (i) the ADEPT trial tradition (Leaf et al., feeding timing in Doppler-abnormal growth-restricted infants) and (ii) observational Doppler-stratified cohorts specifically reporting GI outcomes (e.g. Martini et al. 2022, stratifying UA-AEDF alone vs UA+ductus-venosus-AEDF vs brain-sparing redistribution). Note that ADEPT and related trials address *when to start any enteral feeds*, not specifically *when/whether to fortify* — most fortification guidelines extrapolate a "wait for full feeds and clinical stability" rule from the feeding-initiation literature rather than from fortification-specific trials in this subgroup. Flag this extrapolation explicitly; it is likely the single biggest evidence gap in the whole brief. Also retrieve the older AREDF–NEC association literature (Malcolm 1991, Wilson 1991) for mechanistic/epidemiological context, clearly labelled as older, small, and hypothesis-generating rather than as a fortification trial.

### Domain 3 — Post-surgical NEC and SIP
Distinguish three sub-questions: (i) when to restart *any* enteral feeding after medical/surgical NEC or SIP; (ii) when it is then safe to add fortifier once feeds have restarted; (iii) whether fortifier choice (bovine vs human-milk-derived) affects recurrence or subsequent NEC/SIP risk. Most retrievable evidence will address (i); (ii) and (iii) are likely to be thin — check specifically for post-hoc/subgroup analyses within the N-forte/Jensen trial data and within NEC surgical guideline documents (e.g. the 2024 ERNICA European surgical NEC guideline) for any fortification-specific recommendation, and report if none exists.

### Domain 4 — Short-term growth outcomes
The dense part of the literature — multiple Cochrane reviews (Brown et al. multi-nutrient fortification 2016) and recent meta-analyses (a 2026 update, Rallis et al.) give pooled weight/length/head-circumference velocity estimates for fortified vs unfortified milk. Extract pooled effect sizes with CIs and the GRADE certainty Cochrane itself assigned, not a re-derived certainty.

### Domain 5 — Long-term neurodevelopmental outcome
Separate the evidence into three tiers by directness: (i) trials that randomised fortification (or fortifier type/timing) and followed to a formal neurodevelopmental endpoint (Bayley, WISC, IQ) — e.g. Klamer et al. 2022 (6-year IQ, post-discharge fortification, essentially null); the N-forte trial's planned follow-up at 2 and 5.5 years (check whether results are published yet); (ii) trials/cohorts that report neurodevelopment as a secondary or associated outcome without fortification being the randomised variable (e.g. donor-milk-vs-formula trials that happen to also report fortification exposure); (iii) mechanistic/surrogate outcome studies (head-circumference growth velocity as a proxy, which several groups use because it correlates with later cognitive outcome but is not the same as measuring it). Be explicit in the synthesis about which tier each claim sits in — this is the domain most at risk of surrogate-outcome conflation.

### Domain 6 — GI side effects: constipation, feeding intolerance, osmolality
Constipation is not well captured as a named outcome in most fortification RCTs — check whether it is reported at all as a distinct adverse event versus subsumed under "feeding intolerance" or "abdominal distension." Retrieve the osmolality-mechanism literature (Herranz Barbero 2020; Choi et al. target-fortification osmolality prediction 2016; Chandran et al. on medications compounding osmolality 2016) separately from the clinical-outcome literature, and connect them explicitly rather than assuming osmolality data proves a clinical constipation/NEC link — the AAP's 450 mOsm/kg threshold is a consensus safety ceiling, not one validated against hard clinical outcomes in RCTs; say so.

### Domain 7 — Post-discharge / home fortification
A dedicated Cochrane review line exists (Young et al., multiple update years, "nutrient-enriched formula" and "multinutrient fortification of human breast milk following hospital discharge") plus a smaller, more clinically-framed literature (Zachariassen 2011; Marino et al. 2018 QI project; a 2023 Lamport et al. paper on continuing HMF at home vs formula-based enrichment). Separate "nutrient-enriched formula" trials (a different intervention, relevant to formula-fed infants) from genuine "continue HMF on human milk at home" trials — they are frequently conflated in secondary sources.

### Domain 8 — Concentrated/high-dose and targeted fortification
Cover: (i) fixed high-dose vs standard-dose powdered HMF; (ii) concentrated liquid preterm-formula-as-fortifier strategies (Lin et al. 2020; Pillai et al. 2018, both reporting this as a rescue strategy for feed-intolerant infants); (iii) targeted/adjustable/individualised fortification based on blood urea nitrogen or milk analysis (Rochow 2015 review; Seliga-Siwecka 2023 RCT, which was stopped early for intolerance — an important null/harm signal to give full prominence to, not a footnote); (iv) acidified vs non-acidified liquid fortifier, which is really a product-chemistry question but has generated a clear safety signal (metabolic acidosis, poorer growth with acidified product — Schanler 2018, Thoene 2014) that is easily missed if the search is framed only around "dose."

## 6. Cross-cutting synthesis

This is where the requester's clinical emphasis lives — build toward it explicitly rather than leaving it implicit:

- A **decision-relevant table**: by clinical scenario (routine VLBW infant; AEDF/REDF antenatal history; post-medical-NEC; post-surgical NEC/SIP; extremely preterm <28 weeks; SGA/IUGR without AEDF) — what does the evidence support for timing and product choice, and at what certainty?
- An explicit **statement of what is extrapolated vs directly evidenced** for each high-risk subgroup (Domains 2 and 3 are where most of the extrapolation will sit).
- A **harms ledger**: every adverse signal found across domains (feed intolerance, NEC, SIP, metabolic acidosis, constipation, discontinued/stopped trials) collected in one place rather than scattered per-domain, so a null-heavy picture cannot be diluted by being spread across eight sections.
- A short section on **what would change practice**: the specific trials (registered, ongoing, or an identified evidence gap) that would most change the recommendation if they reported — e.g., an adequately powered RCT of fortification timing specifically in the AEDF/SGA subgroup, or long-term (school-age) follow-up of any of the major recent RCTs.

## 7. Search strategy

Build per-concept blocks, then combine explicitly. Include UK and US spellings throughout (`randomised`/`randomized`, `fetal`/`foetal`, `oesophag*`/`esophag*`).

### 7.1 Concept blocks (PubMed syntax)

**Block P — Population**
```
("Infant, Premature"[Mesh] OR "Infant, Very Low Birth Weight"[Mesh] OR "Infant, Extremely Low Birth Weight"[Mesh] OR "Infant, Extremely Premature"[Mesh]
OR preterm*[tiab] OR pre-term*[tiab] OR premature*[tiab] OR "very low birth weight"[tiab] OR VLBW[tiab] OR "extremely low birth weight"[tiab] OR ELBW[tiab] OR "extremely preterm"[tiab])
```

**Block I — Fortification (the core intervention)**
```
("Food, Fortified"[Mesh] OR "Milk, Human"[Mesh]
OR "human milk fortif*"[tiab] OR "breast milk fortif*"[tiab] OR "fortified human milk"[tiab] OR "fortified breast milk"[tiab]
OR HMF[tiab] OR HMBF[tiab] OR "human milk-based fortifier*"[tiab] OR "bovine milk-based fortifier*"[tiab] OR "bovine-derived fortifier*"[tiab]
OR "multinutrient fortif*"[tiab] OR "multi-nutrient fortif*"[tiab] OR "target* fortification"[tiab] OR "adjustable fortification"[tiab] OR "individuali?ed fortification"[tiab])
```

**Block T — Timing/dose**
```
("early fortification"[tiab] OR "late fortification"[tiab] OR "delayed fortification"[tiab] OR "timing of fortification"[tiab]
OR "trophic feed*"[tiab] OR "minimal enteral"[tiab] OR "enteral feed volume"[tiab] OR "feed advancement"[tiab])
```

**Block C — Contraindication/high-risk subgroup**
```
("Fetal Growth Retardation"[Mesh] OR "Infant, Small for Gestational Age"[Mesh]
OR IUGR[tiab] OR "intrauterine growth restrict*"[tiab] OR "small for gestational age"[tiab] OR SGA[tiab]
OR "absent end-diastolic flow"[tiab] OR "absent end diastolic flow"[tiab] OR AEDF[tiab] OR AREDF[tiab]
OR "reversed end-diastolic flow"[tiab] OR "reversed end diastolic flow"[tiab] OR REDF[tiab]
OR "umbilical artery Doppler"[tiab] OR "abnormal Doppler"[tiab])
```

**Block S — Surgical NEC/SIP**
```
("Enterocolitis, Necrotizing"[Mesh] OR "Intestinal Perforation"[Mesh]
OR "necrotizing enterocolitis"[tiab] OR "necrotising enterocolitis"[tiab] OR NEC[tiab]
OR "spontaneous intestinal perforation"[tiab] OR SIP[tiab] OR "surgical NEC"[tiab])
```

**Block G1 — Growth outcomes**
```
("Weight Gain"[Mesh] OR "Body Weight"[Mesh] OR "Infant, Growth"[tiab]
OR "weight gain"[tiab] OR "growth velocity"[tiab] OR "linear growth"[tiab] OR "head circumference"[tiab] OR "extrauterine growth restrict*"[tiab] OR EUGR[tiab])
```

**Block G2 — Neurodevelopmental outcomes**
```
("Child Development"[Mesh] OR "Neurodevelopmental Disorders"[Mesh]
OR "neurodevelopmental outcome*"[tiab] OR neurodevelopment*[tiab] OR "Bayley"[tiab] OR cognitive[tiab] OR "developmental outcome*"[tiab] OR IQ[tiab])
```

**Block G3 — GI tolerance/constipation**
```
("Constipation"[Mesh]
OR constipation[tiab] OR "feeding intoleran*"[tiab] OR "feed intoleran*"[tiab] OR "gastric residual*"[tiab] OR "abdominal distension"[tiab] OR "abdominal distention"[tiab] OR osmolality[tiab] OR osmolarity[tiab] OR "metabolic acidosis"[tiab])
```

**Block D — Post-discharge**
```
("Patient Discharge"[Mesh]
OR "post-discharge"[tiab] OR postdischarge[tiab] OR "after discharge"[tiab] OR "home fortif*"[tiab] OR "post-discharge formula"[tiab] OR "nutrient-enriched formula"[tiab])
```

**Block H — Concentrated/high-dose/targeted**
```
("concentrated"[tiab] OR "high dose fortif*"[tiab] OR "high-dose fortif*"[tiab] OR "liquid fortifier*"[tiab] OR "acidified"[tiab] OR "non-acidified"[tiab] OR "target* fortification"[tiab] OR "adjustable fortification"[tiab] OR "corrected fortification"[tiab])
```

### 7.2 Combinations to run (numbered — run and log each separately)

1. P AND I — baseline fortification literature (large; use to sanity-check recall)
2. P AND I AND T — Domain 1
3. P AND I AND C — Domain 2
4. P AND (I OR feed*) AND C AND S — Domain 2/3 overlap (Doppler-abnormal infants who go on to NEC/SIP)
5. P AND I AND S — Domain 3
6. P AND I AND G1 — Domain 4
7. P AND I AND G2 — Domain 5
8. P AND I AND G3 — Domain 6
9. P AND I AND D — Domain 7
10. P AND I AND H — Domain 8
11. I AND G2 without P, restricted to systematic reviews/RCTs — checks for transferable evidence from term-infant fortification/supplementation literature (expect this to be a thin, mostly-inapplicable yield; run it anyway and report the count)
12. Design-filtered re-runs of 2–10 restricted to `Meta-Analysis[pt] OR Systematic Review[pt] OR Randomized Controlled Trial[pt]` to isolate the highest-evidence tier per domain

### 7.3 Consensus MCP claim queries (log separately from PubMed strings — not reproducible in the same sense)

Run these as natural-language questions, one per domain, and use them to (a) sanity-check whether the PubMed strings are missing anything and (b) get a fast read on the overall direction of evidence before full extraction:

- "What feed volume or postnatal day is supported by evidence for starting human milk fortifier in preterm infants?"
- "Is human milk fortification safe in infants with antenatal absent or reversed end-diastolic flow?"
- "When is it safe to reintroduce human milk fortifier after surgical necrotizing enterocolitis or spontaneous intestinal perforation?"
- "Does human milk fortification improve long-term neurodevelopmental outcome in preterm infants?"
- "Does human milk fortifier cause constipation or feeding intolerance in preterm infants?"
- "Does sending preterm infants home on fortified breast milk improve growth after NICU discharge?"
- "Is concentrated or high-dose human milk fortification safe and effective compared with standard dosing?"

Use `medical_mode=true`, `exclude_preprints=true` for all of the above; do not set `study_types` narrowly at this stage (it will exclude valid observational safety data, especially for Domains 2–3 where RCTs are scarce).

### 7.4 Filters and design decisions

- No date limit by default — several key trials (AEDF/AREDF association literature) are from the early 1990s and remain the primary evidence for that mechanism; a "last 10 years" filter would silently delete them. If a date filter is applied for any sub-search, state the reason.
- English-language only is a real limitation — state it, do not treat it as neutral.
- Do not filter on full-text availability.
- Citation-chain forward and backward on every Cochrane review found (they are efficient hubs for this topic) and on every included RCT.

### 7.5 Validate before committing

Before running the full set, confirm the strategy retrieves at minimum: Thanigainathan 2019 (Cochrane, PMID to be confirmed), Brown 2016 (Cochrane multi-nutrient fortification), Shah 2016 (*J Pediatr*), Leaf 2012 (ADEPT trial, *Pediatrics*), and Battersby 2016 (*Lancet Gastroenterol Hepatol*, UK NEC surveillance). If any is missed, repair the relevant block before running the rest.

## 8. Evidence matrix specification

Use `02-extraction/extraction.csv` with the standard columns (id, author_year, country, setting, level_of_care, design, n_patients, n_events, population_detail, intervention, comparator, outcomes_measured, primary_result, effect_size, ci_lower, ci_upper, p_value, secondary_results, ascertainment_method, rob_tool, rob_domains, rob_overall, directness, grade_certainty, grade_reason, funding, conflicts, key_limitation, abstract_only, pmid, doi, notes), plus these question-specific columns:

- `domain` (1–8, per Section 5)
- `fortifier_type` (bovine powder / bovine liquid acidified / bovine liquid non-acidified / human-milk-derived / concentrated preterm formula / targeted-adjustable)
- `fortification_definition` (verbatim threshold used: volume mL/kg/d and/or postnatal day)
- `subgroup_flag` (AEDF-REDF / IUGR-SGA / post-medical-NEC / post-surgical-NEC / post-SIP / general VLBW / extremely preterm <28wk / none specified)
- `bmf_terminology_check` (note explicitly whether the paper uses "BMF" to mean bovine-milk-based fortifier — see Section 4 — to prevent mis-extraction)

## 9. Deliverables

Numbered, each a named file:

1. `01-search-log/searches.md` — every PubMed string and Consensus query run, with hit counts and inclusion counts, appended as you go.
2. `02-extraction/extraction.csv` — the evidence matrix per Section 8.
3. `02-extraction/could-not-verify.md` — any reference that could not be confirmed with a PMID/DOI, with the reason, excluded from all other files.
4. `03-synthesis/domain-1-timing-dose.md` through `03-synthesis/domain-8-concentrated-targeted.md` — one file per domain, five-part structure per Section 5.
5. `03-synthesis/cross-cutting-synthesis.md` — Section 6 output: decision table, extrapolation statement, harms ledger, evidence-gap note.
6. `03-synthesis/prisma-style-flow-counts.md` — identified / deduplicated / screened / full-text assessed / excluded-with-reasons / included, even though this is a narrative not systematic review — modern editors expect it.

## 10. Candidate seed literature — VERIFY EVERY ONE

The lines below are **search leads from a scoping pass, not verified citations.** They describe papers surfaced during scoping (via Consensus, medical-mode, 2025-09 search) that looked relevant to specific domains — retrieve each independently through PubMed, confirm the PMID/DOI, and **discard and report** anything that cannot be confirmed or that turns out on full-text read not to match what its abstract implied.

- **Domain 1 (timing/dose):** a Cochrane review of early-vs-late fortification (Thanigainathan and coauthors, ~2019/2020, *Cochrane Database Syst Rev*); an earlier systematic review on the same question (Alyahya and coauthors, ~2019, *Neonatology*); a meta-analysis reporting longer hospital stay with early fortification (Basu and coauthors, ~2020, *Eur J Pediatr*); an RCT comparing fortification at 20 vs 100 mL/kg/d (Shah and coauthors, ~2016, *J Pediatr*); more recent body-composition-endpoint RCTs of very early (day 2–7) fortification (Salas and coauthors, multiple papers ~2023–2025, *Pediatrics* and *Am J Clin Nutr*).
- **Domain 2 (AEDF/IUGR):** the ADEPT trial line of work on feeding timing in Doppler-abnormal growth-restricted infants (Leaf and coauthors, ~2010–2012, *Pediatrics*/*Arch Dis Child*); a Doppler-stratified cohort specifically reporting GI outcomes including SIP (Martini and coauthors, ~2022, *Nutrients*); older case-series/cohort work establishing the AREDF–NEC association (Malcolm and coauthors and a related Wilson and coauthors correspondence, both ~1991, *Arch Dis Child*).
- **Domain 3 (post-surgical NEC/SIP):** a systematic review specifically on nutrition and SIP (Olaloye and coauthors, ~2020, *Nutrients*); an early-refeeding-after-NEC cohort (Bohnhorst and coauthors, ~2003, *J Pediatr*); a 2024 European surgical NEC guideline with a nutrition/neurodevelopment recommendation (ERNICA network, *Neonatology*); a joint Italian neonatology/surgery/nutrition position paper on post-operative GI-surgery nutrition (De Rose and coauthors and the SIN/SICP/SINUPE panel, ~2025/2026).
- **Domain 4 (growth):** the core Cochrane multi-nutrient fortification review (Brown and coauthors, ~2016, *Cochrane Database Syst Rev*) and a more recent meta-analysis update (Rallis and coauthors, ~2026).
- **Domain 5 (neurodevelopment):** a 6-year IQ follow-up of post-discharge fortification (Klamer and coauthors, ~2022, *Nutrients*), reported as null; the Swedish/Nordic N-forte trial and its planned longer-term follow-up protocol (Jensen and coauthors, ~2021 protocol in *BMJ Open*, ~2024 short-term results in *eClinicalMedicine*).
- **Domain 6 (GI/osmolality):** osmolality-of-fortified-milk measurement work (Herranz Barbero and coauthors, ~2020, *PLoS ONE*; Choi and coauthors on a prediction model, ~2016, *PLoS ONE*); a medication-and-osmolality safety study (Chandran and coauthors, ~2016, *Neonatology*); a Chinese cohort specifically studying HMF and feeding intolerance with dose-response thresholds (Zhang and coauthors, ~2022, *Nutrients*).
- **Domain 7 (post-discharge):** the relevant Cochrane review line (Young and coauthors, several update years, "multinutrient fortification... following hospital discharge" and "nutrient-enriched formula... following hospital discharge"); a UK QI project on home BMF (Marino and coauthors, ~2018, *Arch Dis Child*); a more recent report on continuing HMF at home vs formula-based enrichment (Lamport and coauthors, ~2023, *J Nutr*).
- **Domain 8 (concentrated/targeted):** concentrated-preterm-formula-as-fortifier reports (Lin and coauthors, ~2020, *Nutrients*, with 2-year follow-up; Pillai and coauthors, ~2018, *Nutrients*); a targeted/adjustable fortification RCT stopped early for intolerance (Seliga-Siwecka and coauthors, ~2023, *Nutrients*) — treat this null/harm signal as high-priority, not a footnote; an acidified-vs-non-acidified liquid fortifier RCT (Schanler and coauthors, ~2018, *J Pediatr*) and a related retrospective comparison (Thoene and coauthors, ~2014, *Nutrients*).

**Report what you discarded** from this list in the search log, with the reason (could not verify PMID/DOI; abstract did not match description; superseded by a later version).

## 11. Quality control checklist

Report against these explicitly in the QC file — an unreported check is indistinguishable from a skipped one.

- [ ] Every reference in every synthesis file carries a PMID or DOI verified this session
- [ ] Every interventional claim carries a GRADE label and downgrade reason
- [ ] Every claim flagged direct vs extrapolated (especially Domains 2 and 3)
- [ ] Null/negative findings given equal prominence to positive ones in each domain file (spot-check: does each domain file contain at least one "no difference" or "insufficient evidence" statement where the underlying evidence actually says that?)
- [ ] The BMF-terminology check (Section 4) applied to every extracted paper using the abbreviation "BMF"
- [ ] Search log is append-only and complete — every string run, including ones that returned few or zero hits
- [ ] Could-not-verify list produced even if empty (state "none" explicitly, do not omit the file)
- [ ] PRISMA-style flow counts recorded even though this is a narrative review
- [ ] Seed literature list cross-checked against Section 10 and discards reported

## 12. Output style

Consultant-level register — assume the reader already knows the clinical content. Prose over bullets within each domain's synthesis narrative; use tables for the evidence matrix and the cross-cutting decision table. No restating of the research question, no motivational framing, no filler transitions. State plainly, without hedging into vagueness, wherever the evidence is thin, conflicting, or absent — particularly expected in Domains 2, 3, and parts of 5.

---

## Running instructions

1. Scaffold the project (adapt path/name as needed): `scripts/init_project.sh bmf-preterm-fortification` from the evidence-review-pipeline skill, or create the six-folder structure manually (`00-protocol/ 01-search-log/ 02-extraction/ 03-synthesis/ 04-manuscript/ 05-references/`).
2. Save this file as `RESEARCH-BRIEF.md` in the project root.
3. Create `CLAUDE.md` from the skill's `assets/CLAUDE-md-template.md`, filling in the Section 2 rules above so they persist across every session rather than living only in this file.
4. Run `claude mcp list` and confirm PubMed and Consensus MCPs are available in this Code session before starting Domain 1.
5. **Run Domain 1 alone first and inspect the results** before launching the rest — search strings are usually wrong on the first attempt, and Domain 1 has the densest, best-indexed literature (an existing Cochrane review) to calibrate recall against.
6. Where subagents are available, run one domain per subagent from Domain 2 onward, each writing to its own `03-synthesis/domain-N-*.md` file and reporting back only hit counts and exclusion counts — not summarised findings — to keep the parent context clean.
7. After all eight domains are extracted, run Section 6 (cross-cutting synthesis) in a session with all eight domain files loaded from disk, not from conversation memory.
8. Hand off to `reference-builder` for final PMID/DOI verification and Vancouver numbering once the target journal is fixed, and to `clinical-figures` if a PRISMA-style flow diagram or evidence-matrix heatmap is wanted for the eventual manuscript.
