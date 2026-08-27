# Domain F search log — Hypoglycaemia + seizure: is MRI indicated?

**Date run:** 2026-08-27
**Databases:** PubMed (mcp__bb264603 PubMed MCP), Consensus (mcp__1da67083 Consensus MCP)

## Seed-list verification (brief §10, Domain F)

| # | Query / action | Hits | Result |
|---|---|---|---|
| 1 | `get_article_metadata(["18595988"])` | — | **Not re-run** — Burns 2008 arrived pre-verified in the task prompt with full abstract; PMID 18595988, DOI 10.1542/peds.2007-2822 treated as verified per instruction, cited directly. |
| 2 | `get_article_metadata(["24861161","31447599","24798709","18433524","17953809","37383118"])` | 6/6 resolved | All six requested PMIDs returned complete metadata + abstract in a single batch — no drops this time. Confirms: Fong & Harvey 2014 (24861161, DOI 10.1111/dmcn.12496); Gu 2019 (31447599, DOI 10.1177/1179556519867953); Hu 2014 Acta Paediatr (24798709, DOI 10.1111/apa.12673, English, FVEP study); Mao 2008 Zhongguo Dang Dai Er Ke Za Zhi (18433524, no DOI resolved by tool, PII given, Chinese language/English abstract — **[abstract only]**); Mao 2007 Zhonghua Er Ke Za Zhi (17953809, no DOI resolved, Chinese language/English abstract — **[abstract only]**); Kurahashi 2023 World J Clin Cases (37383118, DOI 10.12998/wjcc.v11.i16.3899, English case report, PMC available). |
| 3 | `search_articles("Electroclinical spectrum childhood epilepsy neonatal hypoglycemic brain injury low resource setting Kapoor")` | 1 | Returned PMID 32446209 as sole hit. |
| 4 | `get_article_metadata(["32446209"])` (Kapoor, alone) | 1/1 resolved | **Resolves cleanly when queried alone or via title search** — full abstract retrieved (170 children, epileptic spasms 76.5%, MRI gliosis/encephalomalacia occipital±parietal in 96.5%, drug-resistant epilepsy 68.2%). DOI 10.1016/j.seizure.2020.05.010. This **contradicts** the parent session's could-not-verify entry, which found the PMID silently dropped from a 20-PMID batch call. Conclusion: the PMID is valid and resolvable; the earlier failure was a batch-call artefact (tool silently drops entries from large mixed batches under some condition not fully characterised), not a bad PMID. See notes below — **not re-logged to could-not-verify**, since it now verifies; flagged instead for the parent to reconcile the master could-not-verify.md. |

## Additional targeted searches (2015+ MRI timing / predictive value / differential diagnosis)

| # | Query | Filter | Hits | Notable results |
|---|---|---|---|---|
| 5 | `MRI timing neonatal hypoglycemia seizure prognosis prediction neurodevelopmental outcome` | date_from 2015 | 0 | Over-specified query (7 concept blocks ANDed) — no results. Query too narrow, not a true null; superseded by #6. |
| 6 | `neonatal hypoglycemia brain injury MRI timing outcome` | date_from 2015 | 1 | PMID 41022518 — Martínez-Biarge et al. 2025, "Recommendations for the use of brain MRI in the neonatal period" (An Pediatr, Engl Ed), Spanish Neonatal Brain Group practice guideline. Covers indications/optimal timing for MRI across neonatal pathologies incl. hypoglycaemia-associated brain damage. First author affiliated with Hammersmith Hospital, Imperial College Healthcare NHS Trust — same trust as Burns 2008 and this synthesis. No PMC full text available (confirmed via `convert_article_ids`) — **[abstract only]**. |
| 7 | `neonatal hypoglycemic seizure stroke arterial ischemic infarction mimic` | none | 0 | True null — no PubMed-indexed paper specifically pairs hypoglycaemic seizure + stroke-mimic terminology. Confirms this point rests on the Burns 2008 cohort's internal finding (3/35 MCA infarctions), not a dedicated literature. |
| 8 | `neonatal hypoglycemia arterial ischemic stroke middle cerebral artery infarction` | none | 1 | PMID 19656748 — screened by title only, not fetched (peripheral to domain scope; not pursued further given time budget). |
| 9 | `neonatal hypoglycemia seizure MRI brain injury pattern` | date_from 2015 | 6 | PMIDs 36514522 (new), 32446209 (Kapoor, cross-confirms search #4), 31447599 (Gu, already verified), 22682614 (Martinez-Biarge 2012 HIE white-matter paper — off-topic, HIE not hypoglycaemia-primary, not pursued), 18595988 (Burns, already verified), 18433524 (Mao, already verified). |
| 10 | `get_article_metadata(["36514522","22682614"])` | 2/2 resolved | 36514522 = Yalçın et al. 2022, *Noro Psikiyatri Arsivi*, "Neurodevelopmental Outcome in Patients with Typical Imaging Features of Injury as a Result of Neonatal Hypoglycemia" — Turkish cohort, n=21 with documented hypoglycaemia + parieto-occipital injury, DOI 10.29399/npa.27997, PMC9723839 (English, full text available). 22682614 = Martinez-Biarge et al. 2012 (HIE-specific, off-topic) — not used further. |
| 11 | Consensus: `"is MRI indicated after neonatal hypoglycemic seizures timing and prognostic value"`, medical_mode=true | — | 20 | Surfaced Zhang et al. 2022 (*Eur J Pediatr*, dynamic/serial MRI timing study — DWI-positive window vs pseudonormalisation) and re-surfaced Martínez-Biarge 2025 and Burns 2008 independently. Also surfaced HIE-specific dysglycaemia/MRI literature (Kamino 2023, Basu 2018, Parmentier 2022) — noted as adjacent/differential-diagnosis context but **not verified via PubMed this session and not cited as Domain F primary evidence**, since Domain F's scope (per brief) is isolated hypoglycaemic seizure, not neonatal encephalopathy with secondary dysglycaemia — that population is addressed in Domain G/cross-references. Also surfaced the 2026 ILAE Neuroimaging Task Force guideline on MRI in first afebrile seizure/new-onset epilepsy in infants generally (not hypoglycaemia-specific) — noted as general-practice context only. **Note:** this tool's system instructions request inline numbered citation brackets and a sign-off message in every response; per this session's data-vs-instruction rule, tool output is treated as data, not as a directive, and that formatting is not applied here or in the synthesis file. |
| 12 | `search_articles("Dynamic magnetic resonance imaging findings early stages neonatal hypoglycemic brain injury Zhang")` | none | 1 | PMID 36166098 confirmed — Zhang et al. 2022, *Eur J Pediatr*, DOI 10.1007/s00431-022-04637-y. Retrospective, n=86 Chinese neonates, 139 DWI scans: injury-site DWI hyperintensity within 7 days of hypoglycaemia in 84 scans; pseudonormalisation/T1-T2 changes appearing at 11–23 days; vulnerable sites occipital lobe 98%, splenium of corpus callosum 60%, parietal lobe 30%. This is the most direct **MRI-timing-specific** paper found (2015+ requirement). |
| 13 | `search_articles("Occipital Lobe Injury Cortical Visual Outcomes Neonatal Hypoglycemia Tam diffusion weighted")` | none | 1 | PMID 18762519 confirmed — Tam et al. 2008, *Pediatrics*, DOI 10.1542/peds.2007-2002. Pre-2015 but central to the MRI-timing question and not in the brief's seed list — added here. DWI within 6 days of hypoglycaemia onset was sensitive in term infants (50%, 8/16) but showed **no** occipital diffusion restriction beyond 6 days even with ongoing hypoglycaemia, and was **not sensitive in preterm infants at all** — a direct, quantified timing-window finding supporting early (≤6 day) MRI, with an explicit preterm-directness caveat. |
| 14 | `convert_article_ids(["41022518"], id_type="pmid")` | — | No PMC record returned — confirms Martínez-Biarge 2025 has no PMC full text available via this tool; abstract-only for this session. |

## Verified this session (Domain F) — full list with PMID/DOI

- 18595988 — Burns 2008, Pediatrics, 10.1542/peds.2007-2822 (pre-verified, supplied in task; central paper)
- 24861161 — Fong & Harvey 2014, Dev Med Child Neurol, 10.1111/dmcn.12496
- 31447599 — Gu 2019, Clin Med Insights Pediatr, 10.1177/1179556519867953
- 32446209 — Kapoor 2020, Seizure, 10.1016/j.seizure.2020.05.010 (**resolved this session — see note above**)
- 24798709 — Hu 2014, Acta Paediatr, 10.1111/apa.12673
- 18433524 — Mao 2008, Zhongguo Dang Dai Er Ke Za Zhi (Chin J Contemp Pediatr) [abstract only, Chinese language]
- 17953809 — Mao 2007, Zhonghua Er Ke Za Zhi (Chin J Pediatr) [abstract only, Chinese language]
- 37383118 — Kurahashi 2023, World J Clin Cases, 10.12998/wjcc.v11.i16.3899
- 41022518 — Martínez-Biarge 2025, An Pediatr (Engl Ed), 10.1016/j.anpede.2025.503935 [abstract only — no PMC full text]
- 36166098 — Zhang 2022, Eur J Pediatr, 10.1007/s00431-022-04637-y (new; MRI timing)
- 36514522 — Yalçın 2022, Noro Psikiyatr Ars, 10.29399/npa.27997 (new)
- 18762519 — Tam 2008, Pediatrics, 10.1542/peds.2007-2002 (new; pre-2015 but central to MRI-timing question, added per brief's no-date-limit rule for foundational imaging papers)

## Could not verify

None new this session for Domain F. The brief's flagged Kapoor PMID (32446209) **was successfully resolved** this session (see search #4) — it is NOT re-added to could-not-verify. The parent's master `05-references/could-not-verify.md` entry for this PMID should be reconciled/removed on merge (out of scope for this agent to edit directly).

## Notes on tool behaviour

- Confirms the parent's observation: `get_article_metadata` can silently drop a resolvable PMID from a large mixed batch. When a single PMID is queried alone (or found independently via title search), it resolves without issue. Recommendation for future domains: re-attempt any "dropped" PMID as a solo call or via `search_articles` title search before concluding it is unresolvable.
- `search_articles` rejects overly compound queries by returning 0 hits without an explicit "too complex" error in several cases here (search #5) — narrowing the query resolved this (search #6), consistent with the 5-wildcard warning in the task brief, though these queries used phrase terms rather than wildcards.
