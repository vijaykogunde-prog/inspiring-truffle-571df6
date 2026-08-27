# Antenatal Dexamethasone Dosing Interval: 12 mg 12-Hourly vs 12 mg 24-Hourly vs 6 mg 12-Hourly
## Evidence Synthesis for a UK Level 3 NICU

*Compiled 2026-08-27. Vancouver-numbered references with PMID and DOI verified via the PubMed MCP connector unless otherwise flagged. Status: written incrementally — sections marked [PENDING] are being completed by parallel research threads and will be filled in place.*

**Access note:** the network egress proxy in this environment blocks direct WebFetch to medicines.org.uk (EMC/SPC), nice.org.uk, rcog.org.uk, and ncbi.nlm.nih.gov/books. Guideline **wording** below is reconstructed from WebSearch snippets and previously PubMed-verified abstracts, not a directly fetched primary PDF or SPC. This is flagged at each point of use — independently confirm against primary text before this synthesis is used to withdraw a clinical practice.

---

## Premise statement

**There is no RCT evidence for dexamethasone 12 mg given at a 12-hourly interval.** This is confirmed, not assumed. The 2022 Cochrane review dedicated specifically to comparing antenatal corticosteroid regimens (Williams et al, PMID 35943347) identifies only three studies anywhere in the global trial base that compare any regimen variant of any agent, and none of them is a dexamethasone-interval comparison. One of the three is a comparison of **betamethasone** given 12-hourly versus 24-hourly — a different drug, with a different formulation (depot acetate ester) that provides an independent pharmacokinetic rationale for its own interval. No trial of dexamethasone at any interval other than the two studied in major RCTs (6 mg × 4 doses 12-hourly, or 12 mg × 2 doses 24-hourly) has been identified anywhere in this search. The regimen under review at this unit — 12 mg IM, 12-hourly, two doses — combines the RCOG/ASTEROID per-dose amount with the WHO/ACOG per-dose interval, and in doing so, creates a hybrid regimen that neither trial base actually tested. It is not a licensed indication of any dexamethasone SPC identified, and it is not named in RCOG GTG74, NICE NG25 (so far as securely established), WHO 2022, or ACOG guidance.

This is a genuine **absence of evidence**, and the synthesis below treats it as such throughout: absence of evidence for benefit is not evidence of safety, and absence of evidence of harm is not reassurance that none exists. The reasoning that follows is built from pharmacokinetics and mechanism, explicitly labelled as inference, because no direct trial data exist to answer the question any other way.

---

## Executive summary

1. **Three distinct regimens exist and must not be conflated**: WHO/ACOG standard (6 mg IM q12h × 4 = 24 mg), RCOG/ASTEROID (12 mg IM q24h × 2 = 24 mg), and the regimen under review (12 mg IM q12h × 2 = 24 mg, untested). *Certainty: High that this factual mapping is correct — definitional, drawn directly from guideline and trial texts.*
2. **No guideline anywhere endorses the 12 mg 12-hourly regimen.** RCOG GTG74 explicitly offers only the 24-hourly two-dose option alongside the WHO four-dose 12-hourly option; it does not name a 12-hourly two-dose alternative. [Q1]
3. **Dexamethasone sodium phosphate has no depot fraction**; its pharmacokinetics are structurally different from betamethasone's depot-containing preparation, which is the actual reason betamethasone is given 24-hourly. Transplanting a 24-hourly-appropriate total dose (12 mg) onto a 12-hourly schedule is not pharmacologically neutral. [Q2 — pending integration]
4. **The only interval RCT for either drug (betamethasone, not dexamethasone) found equivalent RDS rates but a significantly higher NEC rate with the 12-hourly interval**, in a small, unreplicated, single-centre trial. [Q3 — pending integration]
5. **No study has isolated the specific scenario of a second dose given ~1 hour before delivery.** The mechanistic evidence on time-to-transcriptional-effect argues against that dose having time to act on fetal lung maturation, while also arguing against it having time to cause the harms that require sustained exposure. [Q4 — pending integration]
6. **No study has directly compared maternal hyperglycaemia or adrenal suppression by dosing interval.** [Q5 — pending integration]
7. **ASTEROID's cerebral palsy comparison between dexamethasone and betamethasone (at the STANDARD 24-hourly interval) remains statistically unresolved**, and this finding concerns agent, not interval — it must not be used as if it were evidence about the 12-hourly regimen, but it does mean the evidence base for dexamethasone generally carries an open safety question that a guideline should not paper over. [Q6 — pending integration]

---

## Q1 — Premise verification and regimen mapping

### The three regimens, stated precisely

| Regimen | Dose per injection | Interval | Number of injections | Total course dose | Guideline / trial source |
|---|---|---|---|---|---|
| **WHO / ACOG standard** | 6 mg IM | Every 12 hours | 4 | 24 mg | WHO 2022 recommendation (preferred regimen in most included trials); used in the WHO ACTION-I trial, Oladapo OT et al 2020, PMID 33095526, DOI 10.1056/NEJMoa2022398 — verified: "dexamethasone sodium phosphate... 6 mg intramuscularly every 12 hours, to a maximum of four doses"[1] |
| **RCOG / ASTEROID** | 12 mg IM | Every 24 hours | 2 | 24 mg | RCOG Green-top Guideline No. 74 (Stock SJ et al 2022, PMID 35172391, DOI 10.1111/1471-0528.17027)[2]; ASTEROID trial (Crowther CA et al 2019, PMID 31523039, DOI 10.1016/S2352-4642(19)30292-5) — dexamethasone sodium phosphate 12 mg IM × 2, 24 hours apart, against betamethasone 11.4 mg IM × 2, 24 hours apart[3] |
| **Regimen under review** | 12 mg IM | Every 12 hours | 2 | 24 mg | **No RCT evidence identified. Not named in RCOG GTG74, WHO 2022, or ACOG guidance as reconstructed in this search.** |

RCOG GTG74 itself lists two dexamethasone options — 2 × 12 mg 24-hourly, and 4 × 6 mg 12-hourly — as alternatives with the SAME total dose (24 mg), matching the WHO/ACOG standard and the RCOG/ASTEROID regimen respectively.[2] It does not, on any source identified in this search, name a third option combining the 12 mg per-dose amount with a 12-hourly interval. **This is the central factual finding of this premise check: the regimen under review is a hybrid of the per-dose amount from one guideline-endorsed regimen and the interval from a different guideline-endorsed regimen, and this specific combination has not itself been validated by any trial or named by any guideline identified.**

### Trials establishing dexamethasone efficacy, and their exact regimens

| Trial | PMID | Regimen used |
|---|---|---|
| WHO ACTION-I (Oladapo et al 2020) | 33095526 | Dexamethasone 6 mg IM q12h, max 4 doses, vs placebo[1] |
| ASTEROID (Crowther et al 2019) | 31523039 | Dexamethasone 12 mg IM q24h × 2, vs betamethasone 11.4mg IM q24h × 2[3] |
| Chawanpaiboon et al 2023 (dose-comparison, not interval) | 37442247, DOI 10.1016/j.ajog.2023.07.006 | 5 mg vs 6 mg dexamethasone IM, **both given q12h × 4** — tests per-dose amount, not interval; confirms the 12-hourly four-dose schedule is the standard comparator used in a contemporary (2023) RCT.[4] Primary outcome (RDS) 2.2% (5mg) vs 1.6% (6mg), proportional difference 0.6% (95% CI within the predefined 10% noninferiority margin); most women delivered after 34 weeks; a substantial proportion did not complete the full course. This trial is evidence about dose AMOUNT, not interval, and must not be cited as interval evidence. |

### Is 12 mg 12-hourly endorsed anywhere?

No. Across RCOG GTG74, the WHO 2022 recommendation, ACOG guidance (as reconstructed from secondary sources), and the trial literature searched, no source names a 12 mg dexamethasone dose given at a 12-hourly interval. The BNF, UK Neonatal Formulary, and the Summary of Product Characteristics for the UK-licensed dexamethasone sodium phosphate injection could not be directly fetched in this session (network egress blocked to medicines.org.uk and related hosts) — **this specific negative finding (that no source recommends the regimen) should be independently re-confirmed against those primary UK prescribing documents before the guideline states it as definitively established**, though the convergence of every other source checked makes it very likely to hold.

### The size and nature of the evidence gap

The gap is total, not partial: there is no RCT, no comparative cohort, and (per the dedicated Cochrane regimen-comparison review) no study of any design comparing dexamethasone 12 mg at 12-hourly versus 24-hourly intervals for ANY outcome — not RDS, not IVH, not NEC, not neurodevelopment, not maternal glycaemia, not adrenal suppression. The only regimen-interval comparison in the entire literature identified by the Cochrane reviewers concerns betamethasone, a pharmacologically distinct preparation (see Q2). This means the guideline cannot appeal to "no evidence of harm" as reassurance, because there is equally no evidence that the practice is safe, effective, or ineffective — the practice sits entirely outside the evidence base that justifies antenatal corticosteroid use at all.

**Implication for the guideline:** State plainly, at the top of any unit document, that the 12 mg 12-hourly regimen is not supported by any identified guideline or trial. Recommend adoption of the RCOG/ASTEROID regimen (12 mg IM × 2, 24 hours apart) as the evidence-matched option if 12 mg per dose is the unit's preferred amount, or the WHO/ACOG regimen (6 mg IM × 4, 12 hours apart) if the 12-hourly interval is preferred for operational reasons — but not the untested combination of both. *Certainty: High, that this factual gap exists; the recommendation itself is a judgement built on absence of evidence, not a graded clinical-trial finding.*

**What we do not know (Q1):** Whether any jurisdiction outside the sources searched (RCOG, WHO, ACOG, and UK formulary sources so far as reachable) endorses this regimen — a wider international guideline search (e.g. SOGC, RANZCOG, individual European national guidelines) was not exhaustively performed and could be a useful supplementary check. Whether the UK SPC for dexamethasone sodium phosphate injection licenses antenatal use at all, or whether this use is off-label regardless of interval (off-label antenatal corticosteroid use is common practice internationally but should be explicitly stated in the guideline's medicolegal framing).

---

## Q2 — Pharmacokinetics of dexamethasone in pregnancy [PENDING — subagent research in progress]

---

## Q3 — Clinical evidence: does dosing interval affect neonatal outcomes? [PENDING]

---

## Q4 — Imminent delivery: does a second dose at 12 hours add anything? [PENDING]

---

## Q5 — Maternal risks: hyperglycaemia, immune suppression, adrenal suppression [PENDING]

---

## Q6 — Long-term neurodevelopmental outcomes [PENDING]

---

## Q7 — Guideline recommendations and parent counselling [TO BE WRITTEN after Q2–Q6 integrated]

---

## Overall GRADE summary table [TO BE COMPLETED]

## What we do not know — consolidated [TO BE COMPLETED]

## References [TO BE COMPLETED — full Vancouver list once all sections finalised]

## Could not verify

- Direct primary-text confirmation of the BNF, UK Neonatal Formulary, and dexamethasone sodium phosphate SPC dosing sections — medicines.org.uk and related hosts blocked by network egress proxy in this session. The finding that none of these endorses 12 mg 12-hourly is based on convergent secondary evidence, not direct primary-text reading, and should be independently re-checked.
- Direct primary-text confirmation of NICE NG25's exact recommendation wording — nice.org.uk blocked by network egress proxy in this session.
