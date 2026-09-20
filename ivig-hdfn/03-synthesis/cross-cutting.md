# Cross-cutting synthesis

Draws on Domains A–F (`domain-A.md`–`domain-F.md`) and the mechanism note (`00-mechanism.md`); no new searches were run for this file. Extraction-table ids (A1–A7, B1–B10, C1–C15, E1–E24) are cross-referenced rather than re-described.

## 1. The central discrepancy: why early trials showed large effects and later trials do not

The single most important pattern in this evidence base is that **trial era, blinding, and phototherapy intensity move together**, and the apparent efficacy of IVIG in Rh disease tracks that bundle almost perfectly, not the drug itself.

| Trial | Year | Country | Blinding | Phototherapy comparator | Prior IUT | Control-arm ET rate | Result |
|---|---|---|---|---|---|---|---|
| Rübo et al. (A1) | 1992 | Germany | Not blinded | Conventional | Not stated | 69% (11/16) | Positive |
| Voto et al. (A2) | 1995 | Argentina | Not blinded | Conventional | Not stated | Not quantified | Positive (qualitative) |
| Dağoğlu et al. (A3) | 1995 | Turkey | Not blinded, no placebo, untreated controls | Conventional | Not stated | Not quantified | Positive |
| Elalfy et al. (A4) | 2010 | Egypt | Unclear | Conventional | Excluded if antenatally treated | 22% | Positive (dose-dependent) |
| Nasseri et al. (A5/B3) | 2006 | Iran | Unclear | Centre-standard | Not stated | Not quantified | Positive overall; Rh > ABO |
| **Smits-Wintjens et al. (A6)** | **2011** | **Netherlands** | **Double-blind, placebo** | **Modern Dutch NICU standard** | **66% (53/80)** | **15% (6/39)** | **Null** |
| **Santos et al. (A7)** | **2012** | **Brazil** | **Double-blind, placebo** | **Explicit high-intensity** | **Included, proportion not stated** | **15.2% (7/46)** | **Null** |

Every positive Rh trial is open-label or has no placebo; both null trials are double-blind and placebo-controlled under an explicitly modern or high-intensity phototherapy standard. Control-arm exchange-transfusion rates fall from 69% (1992) to ~15% (2011–2012) — consistent with intensive phototherapy alone having already removed most of the exchange-transfusion burden the earlier trials were powered against. The risk-of-bias-stratified meta-analyses (Louis et al. 2014, PMID 24514437; Zwiers et al. 2018 Cochrane, PMID 29551014) make this explicit: pooling high-risk-of-bias trials gives RR ~0.2–0.3 for exchange transfusion; restricting to the two low-risk-of-bias, placebo-controlled trials gives RR 0.98 (95% CI 0.48–1.98) — no effect. **This is the central finding of the entire evidence base: the historical positive-trial literature and the contemporary null-trial literature are not really in disagreement about IVIG's effect once trial quality is accounted for; they are measuring different things (an open-label comparison under old-style phototherapy vs a blinded comparison under modern phototherapy), and the blinded modern comparison is null.**

ABO disease never had the low-risk-of-bias tier to begin with (`domain-B.md` (a)): Louis 2014 found only high-risk-of-bias ABO trials, and no placebo-controlled ABO RCT of the Leiden/Brazil type has ever been conducted. The largest modern ABO datasets are non-randomised cohorts (Okulu 2022 n=531, Daunov 2022 n=579, Pan 2021 n=114, Al-Lawama 2019 n=202) that converge on a null-or-adverse direction, but are themselves confounded by indication in the opposite direction (sicker infants preferentially treated) — so ABO disease has weaker evidence in both directions than Rh disease, not simply "the same problem, smaller trials."

## 2. Is IVIG a rescue therapy, a prophylactic therapy, or neither, in a modern UK NICU?

Per Domain D, **no trial anywhere in this evidence base randomised prophylactic-versus-rescue timing as an independent variable.** What can be said, cautiously, cross-referencing each trial's own protocol:

- The two Rh trials most directly applicable to a modern UK NICU (A6, A7 — both blinded, placebo-controlled, modern/high-intensity phototherapy) both used **prophylactic** dosing and were **null**. This is evidence against a policy of routine prophylactic IVIG in Rh disease under modern phototherapy, specifically because that is what was tested and it failed.
- Every ABO trial and cohort in Domain B uses **rescue** timing (triggered by bilirubin approaching the exchange threshold), and the largest, most recent, non-randomised ABO datasets are themselves null-or-adverse despite rescue timing — so rescue timing has **not** demonstrated benefit in modern ABO practice either.
- No trial has tested rescue-timed IVIG in Rh disease under equally rigorous (blinded, placebo-controlled, modern-phototherapy) conditions to the two prophylactic trials, so the null result in Rh disease cannot be confidently attributed to the *prophylactic* strategy specifically rather than to blinding/era.

**Honest conclusion: on the current evidence, IVIG functions as neither a validated prophylactic therapy nor a validated rescue therapy in a modern UK NICU using intensive phototherapy — both timing strategies lack trial-quality support once phototherapy is already optimised, and the question of which timing strategy (if either) works has never been directly tested.** Any guideline position on timing rests on extrapolation and clinical judgement (targeting a defined bilirubin-rise rate, as a proxy for ongoing active haemolysis, is a plausibility argument, not a finding — Domain D (e)) rather than on trial evidence.

## 3. Harm–benefit balance by subgroup

| Subgroup | Efficacy (exchange transfusion) | Harm signal | Net position |
|---|---|---|---|
| Term Rh-D | Low–Moderate certainty of **no effect** once modern phototherapy is standard (A6, A7 null; Louis 2014/Zwiers 2018 risk-of-bias-stratified) | NEC signal present but very-low-certainty/confounded (Domain E); top-up transfusion **not** increased (A6, A7 — Low–Moderate certainty) | Benefit not demonstrated; harm plausible but unproven — net position does not favour routine use |
| Preterm Rh-D | **No direct evidence identified** — no trial in Domain A enrolled a preterm-only population or reported a preterm-specific subgroup result | Not separately quantified; Domain E's evidence base (Li 2022, Figueras-Aloy 2009) is late-preterm/term, not extremely preterm | Extrapolation from term data only, with lower confidence in a less mature gut (relevant to the NEC mechanism) |
| DAT-positive ABO | Very low certainty; no low-risk-of-bias trial exists at all (`domain-B.md`); largest cohorts null-or-adverse but confounded | Same NEC/harms evidence base as Rh, not antibody-specific in most Domain E studies | Weaker efficacy case than Rh disease; harm-benefit least favourable to routine use of any major subgroup |
| DAT-negative ABO | **No direct evidence identified at all** (every ABO trial requires DAT positivity for entry; Daunov 2022's ~26% DAT-negative fraction not outcome-stratified) | Not separately assessed | Complete evidence vacuum — treat as a distinct unknown, not as "probably similar to DAT-positive" |
| Kell/anti-c/anti-E/mixed | **No direct evidence identified** — case reports only, no comparative study (Domain C) | Not systematically assessable from case reports | Mechanistic plausibility argument (erythroid suppression, not haemolysis) suggests IVIG is a poor biological fit for Kell disease specifically, but this is not an evidence-based efficacy finding |

The NEC question deserves restating precisely because it is easy to over- or under-state. The largest single point estimate (Figueras-Aloy et al. 2009, adjusted OR 31.66, 95% CI 3.25–308.57) and the pooled meta-analytic estimate (Yang et al. 2016, OR 4.53, 95% CI 2.34–8.79) both come from retrospective cohorts that do not adequately separate IVIG's effect from the disease severity that led to IVIG being given in the first place. The one study specifically designed to do so — Li et al. 2022 (n=1259, propensity-score-matched, PMID 35613867) — found no association at all. GRADE for a causal NEC effect is **Very low** in both directions: neither "IVIG causes NEC" nor "IVIG does not cause NEC" can be stated with confidence; what can be stated is that the signal, where present, is very unlikely to be as large as the confounded point estimates suggest, and that a biologically coherent, histopathologically supported mechanism (thrombotic mesenteric microvascular occlusion — Navarro et al. 2009) exists to explain a real, smaller effect if one is present.

## 4. Guidance-vs-evidence gap

Domain F's central finding, restated here because it is the single most decision-relevant fact for the unit guideline: **AAP 2022 (PMID 35927462/35927519) and a 2022 international expert-panel guideline (BJH, DOI 10.1111/bjh.18170) have both explicitly revised their IVIG recommendations downward, citing the same null-trial and NEC-signal evidence this synthesis independently reached. NICE CG98 — the document a UK unit guideline would otherwise default to — shows no confirmed evidence of having revisited its IVIG recommendation's evidence base since 2010**, despite both international re-evaluations occurring in the same year (2022) as NICE's own most recent surveillance activity (2023). This could not be fully confirmed this session (NICE's underlying evidence pages were unreachable — network egress restriction, logged in `could-not-verify.md`), and the unit guideline team should obtain NICE's GDG evidence statements directly before finalising local wording. If confirmed, NICE CG98's IVIG recommendation is very likely still resting on the pre-2011, risk-of-bias-unstratified trial base that this synthesis's own Domain A analysis found does not survive stratification.

The current (2025/2026) Canadian Paediatric Society revision (PMID 42488358) shows the same directional shift as AAP, replacing its 2007 "Grade A"/RR 0.28 framing with conditional, threshold-based wording. Whether the Dutch national guideline (whose own research group authored the pivotal null RCT, A6) has been revised in light of its own country's trial finding could not be determined this session and is flagged as a specific item worth resolving for the *Infant* manuscript's international comparison.

## 5. Late anaemia — a monitoring issue independent of IVIG

Per Domain E (e), this is the one area of this synthesis where the practical message is genuinely reassuring and should not be overcomplicated: **late hyporegenerative anaemia and top-up transfusion requirement are common in HDFN (driven principally by intrauterine-transfusion-related marrow suppression and ongoing extravascular haemolysis) but are not meaningfully increased by IVIG above that baseline rate.** The two highest-directness placebo-controlled RCTs in the entire evidence base (A6, A7) both found no significant difference in top-up transfusion rates between IVIG and placebo arms. The guideline implication is a **disease-based, not an IVIG-based, monitoring recommendation**: post-discharge haemoglobin/reticulocyte surveillance should be recommended for all HDN infants with significant haemolysis or a history of intrauterine transfusion, regardless of whether they received IVIG.

## 6. Research gaps worth a unit audit or multicentre study

1. **No trial has ever tested prophylactic-vs-rescue IVIG timing head-to-head** — a registry-based or multicentre pragmatic trial design (given how rare severe Rh disease now is in a well-immunoprophylaxed population) is the only way to close this gap; a single UK unit is very unlikely to recruit adequate numbers alone.
2. **No trial has enrolled a preterm-only or DAT-negative-ABO-only population.** A prospective unit or network audit that separately records outcomes by gestation band and DAT status for every HDFN infant considered for IVIG (irrespective of whether it is given) would generate exactly the subgroup data this synthesis found absent, at relatively low cost.
3. **The NEC question needs a study design that pre-specifies and adjusts for bilirubin severity/rate of rise at the point IVIG is given** — the confound this synthesis identified as central has not yet been fully resolved even by the best available study (Li et al. 2022), which lacked this specific covariate.
4. **UK haemovigilance (SHOT) does not appear to separately capture IVIG-treatment-specific neonatal harms** (as opposed to anti-D prophylaxis errors) as a distinct reportable category (Domain E, `guidance-table.md`) — this is an addressable governance gap, not a research gap, and the unit guideline should recommend explicit local incident reporting (e.g. Datix) for any suspected IVIG-associated NEC, haemolysis, or thromboembolism in a neonate with HDFN, alongside routine MHRA Yellow Card reporting.
5. **No study has directly compared repeat-dosing intervals or cumulative-dose thresholds against a harms outcome** — the ≥2 g/kg cumulative-dose association with isoagglutinin haemolysis in the (largely adult) vigilance literature (Desborough et al. 2013, PMID 24164446) is the only quantitative anchor available and has not been tested in neonates.

## GRADE summary of findings

| Outcome | Subgroup | Certainty | Direction of effect | Key reason for rating |
|---|---|---|---|---|
| Exchange transfusion | Term Rh-D, modern phototherapy | Low–Moderate | No effect (two placebo RCTs null; risk-of-bias-stratified meta-analyses concordant) | Risk of bias in positive trials; imprecision in the two low-risk-of-bias trials |
| Exchange transfusion | Term/preterm ABO (DAT+) | Very low | Uncertain, largest modern cohorts trend null/adverse | No low-risk-of-bias trial exists at all; serious inconsistency |
| Exchange transfusion | DAT-negative ABO | — | No direct evidence identified | Not studied |
| Exchange transfusion | Kell/anti-c/anti-E/mixed | — | No direct evidence identified | Case reports only, no comparative study |
| Exchange transfusion | Preterm Rh-D | — | No direct evidence identified | No preterm-only trial or subgroup reported |
| Necrotising enterocolitis | Term/late-preterm, IVIG-exposed HDN (any antibody) | Very low | Uncertain; large confounded cohorts suggest harm, one propensity-matched study finds none | Serious risk of bias (confounding by indication) and serious inconsistency between study designs |
| Top-up transfusion / late anaemia | Term Rh-D, placebo-controlled | Low–Moderate | No increase attributable to IVIG | Consistent across the two highest-directness RCTs; disease itself (not IVIG) drives the baseline rate |
| Isoagglutinin-induced haemolysis | All HDFN (mechanism), neonate-specific incidence | Very low | Mechanism established; neonatal-HDFN-specific incidence not quantified | Serious indirectness (evidence largely adult/non-HDFN) |
| Thromboembolism / hyperviscosity | All HDFN | — | No direct evidence identified | Extrapolated only from general adult/all-age labelling |
