const fs = require("fs");

const citeOrder = [];
const citeMap = new Map();
function citeNum(key) {
  if (!citeMap.has(key)) { citeMap.set(key, citeOrder.length + 1); citeOrder.push(key); }
  return citeMap.get(key);
}
function esc(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
function inline(text) {
  const parts = text.split(/@@(.*?)@@/g);
  return parts.map((part, i) => {
    if (i % 2 === 0) return esc(part);
    const nums = part.split(",").map((k) => citeNum(k.trim())).sort((a, b) => a - b);
    return `<sup>${nums.join(",")}</sup>`;
  }).join("");
}
function p(text) { return `<p>${inline(text)}</p>\n`; }
function h1(text) { return `<h1>${esc(text)}</h1>\n`; }
function h2(text) { return `<h2>${esc(text)}</h2>\n`; }
function li(text) { return `<li>${inline(text)}</li>\n`; }
function fig(file, widthPct, caption) {
  return `<div class="figwrap"><img src="figures/${file}" style="width:${widthPct}%;" />${caption ? `<p class="figcap">${inline(caption)}</p>` : ""}</div>\n`;
}
function table(headers, rows, widths) {
  const thead = `<tr>${headers.map((h, i) => `<th style="width:${widths ? widths[i] : ""}">${esc(h)}</th>`).join("")}</tr>`;
  const tbody = rows.map((r) => `<tr>${r.map((c) => `<td>${inline(c)}</td>`).join("")}</tr>`).join("\n");
  return `<table>\n${thead}\n${tbody}\n</table>\n`;
}

const REF = {
  RCOG2022: "Stock SJ, Thomson AJ, Papworth S; Royal College of Obstetricians and Gynaecologists. Antenatal corticosteroids to reduce neonatal morbidity and mortality: Green-top Guideline No. 74. BJOG. 2022;129(8):e35-e60. PMID: 35172391. DOI: 10.1111/1471-0528.17027.",
  Crowther2019: "Crowther CA, Ashwood P, Middleton PF, et al; ASTEROID Study Group. Maternal intramuscular dexamethasone versus betamethasone before preterm birth (ASTEROID): a multicentre, double-blind, randomised controlled trial. Lancet Child Adolesc Health. 2019;3(11):769-780. PMID: 31523039. DOI: 10.1016/S2352-4642(19)30292-5.",
  Oladapo2020: "Oladapo OT, Vogel JP, Piaggio G, et al; WHO ACTION-I Trial Collaborators. Antenatal dexamethasone for early preterm birth in low-resource countries. N Engl J Med. 2020;383(26):2514-2525. PMID: 33095526. DOI: 10.1056/NEJMoa2022398.",
  Williams2022: "Williams MJ, Ramson JA, Brownfoot FC. Different corticosteroids and regimens for accelerating fetal lung maturation for babies at risk of preterm birth. Cochrane Database Syst Rev. 2022;8(8):CD006764. PMID: 35943347. DOI: 10.1002/14651858.CD006764.pub4.",
  Chawanpaiboon2023: "Chawanpaiboon S, Chukaew R, Pooliam J. A comparison of 2 doses of antenatal dexamethasone for the prevention of respiratory distress syndrome: an open-label, noninferiority, pragmatic randomized trial. Am J Obstet Gynecol. 2023;230(2):260.e1-260.e19. PMID: 37442247. DOI: 10.1016/j.ajog.2023.07.006.",
  Jobe2019: "Jobe AH, Milad MA, Peppard T, Jusko WJ. Pharmacokinetics and pharmacodynamics of intramuscular and oral betamethasone and dexamethasone in reproductive age women in India. Clin Transl Sci. 2019. PMID: 31808984. DOI: 10.1111/cts.12724.",
  Petersen1983: "Petersen MC, Collier CB, Ashley JJ, et al. Disposition of betamethasone in parturient women after intravenous administration. Eur J Clin Pharmacol. 1983. PMID: 6662178. DOI: 10.1007/BF00542524.",
  Tsuei1980: "Tsuei SE, Petersen MC, Ashley JJ, et al. Disposition of synthetic glucocorticoids. II. Dexamethasone in parturient women. Clin Pharmacol Ther. 1980;28(1):88-98. PMID: 7389259. DOI: 10.1038/clpt.1980.136.",
  Blanford1977: "Blanford AT, Murphy BEP. In vitro metabolism of prednisolone, dexamethasone, betamethasone, and cortisol by the human placenta. Am J Obstet Gynecol. 1977. PMID: 835623. DOI: 10.1016/0002-9378(77)90466-5.",
  vanderHeijden2024: "van der Heijden JEM, et al. Optimization of the betamethasone and dexamethasone dosing regimen during pregnancy: a combined placenta perfusion and pregnancy physiologically based pharmacokinetic modeling approach. Am J Obstet Gynecol. 2024. PMID: 38763343. DOI: 10.1016/j.ajog.2024.05.012.",
  Samtani2006: "Samtani MN, Pyszczynski NA, Dubois DC, Almon RR, Jusko WJ. Modeling glucocorticoid-mediated fetal lung maturation I and II. J Pharmacol Exp Ther. 2006. PMID: 16371449 / 16371448. DOI: 10.1124/jpet.105.095851 / 10.1124/jpet.105.095869.",
  Ballard1996: "Ballard PL, Ertsey R, Gonzales LW, Gonzales J. Transcriptional regulation of human pulmonary surfactant proteins SP-B and SP-C by glucocorticoids. Am J Respir Cell Mol Biol. 1996. PMID: 8652188. DOI: 10.1165/ajrcmb.14.6.8652188.",
  Venkatesh1993: "Venkatesh VC, Ballard PL. Differential glucocorticoid regulation of the pulmonary hydrophobic surfactant proteins SP-B and SP-C. Am J Respir Cell Mol Biol. 1993. PMID: 8427712. DOI: 10.1165/ajrcmb/8.2.222.",
  Khandelwal2012: "Khandelwal M, Chang E, Hansen C, Hunter K, Milcarek B. Betamethasone dosing interval: 12 or 24 hours apart? A randomized, noninferiority open trial. Am J Obstet Gynecol. 2012;206(3):201.e1-11. PMID: 22381601. DOI: 10.1016/j.ajog.2012.01.025.",
  Brownfoot2013: "Brownfoot FC, Gagliardi DI, Bain E, Middleton P, Crowther CA. Different corticosteroids and regimens for accelerating fetal lung maturation for women at risk of preterm birth. Cochrane Database Syst Rev. 2013. PMID: 23990333. DOI: 10.1002/14651858.CD006764.pub3.",
  Daskalakis2023: "Daskalakis G, et al. European guidelines on perinatal care: corticosteroids for women at risk of preterm birth. J Matern Fetal Neonatal Med. 2023. PMID: 36689999. DOI: 10.1080/14767058.2022.2160628.",
  Kaushal2003: "Kaushal K, Gibson JM, Railton A, Hounsome B, New JP, Young RJ. A protocol for improved glycaemic control following corticosteroid therapy in diabetic pregnancies. Diabet Med. 2003;20(1):73-75. PMID: 12519324. DOI: 10.1046/j.1464-5491.2003.00853.x.",
  Hong2021: "Hong JGS, Tan PC, Kamarudin M, Omar SZ. Prophylactic metformin after antenatal corticosteroids (PROMAC): a double blind randomized controlled trial. BMC Pregnancy Childbirth. 2021;21(1):138. PMID: 33588801. DOI: 10.1186/s12884-021-03628-5.",
  Carter2024: "Carter SW, et al. Antenatal steroids elicited neurodegenerative-associated transcriptional changes in the hippocampus of preterm fetal sheep independent of lung maturation. BMC Med. 2024. PMID: 39183288. DOI: 10.1186/s12916-024-03542-5.",
  Karmoker2020: "Karmoker RK, et al. Antenatal corticosteroid-to-delivery interval and RDS, Mymensingh Medical College Hospital. Mymensingh Med J. 2020. PMID: 31915337.",
  McDougall2023: "McDougall ARA, et al. Effect of antenatal corticosteroid administration-to-birth interval on maternal and newborn outcomes: a systematic review. EClinicalMedicine. 2023. PMID: 37007738. DOI: 10.1016/j.eclinm.2023.101916.",
  Gulersen2021: "Gulersen M, et al. Administration-to-birth interval and neonatal outcomes in late preterm birth. Am J Obstet Gynecol MFM. 2021. PMID: 34153514. DOI: 10.1016/j.ajogmf.2021.100426.",
  Kraft2025: "Kraft K, et al. Hour-scale antenatal corticosteroid administration-to-birth interval and neonatal outcomes. Eur J Obstet Gynecol Reprod Biol. 2025. PMID: 41014996. DOI: 10.1016/j.ejogrb.2025.114732.",
  Gross1983: "Gross I, Wilson CM, Ingleson LD, Brehier A, Rooney SA. The influence of hormones on the biochemical development of fetal rabbit lung in organ culture. Endocrinology. 1983. DOI: 10.1210/endo-112-3-829.",
  Liley1988: "Liley HG, White RT, Warr RG, Benson BJ, Hawgood S, Ballard PL. Glucocorticoids both stimulate and inhibit production of pulmonary surfactant protein A in fetal human lung. Proc Natl Acad Sci USA. 1988. DOI: 10.1073/pnas.85.23.9096.",
  SaldanaGarcia2021: "Saldaña-García N, et al. Benefits of a single dose of betamethasone in imminent preterm labour. J Clin Med. 2021;11(1):20. PMID: 35011761. DOI: 10.3390/jcm11010020.",
  Edut2026: "Edut K, et al. Late preterm antenatal corticosteroid administration-to-birth interval and neonatal outcomes stratified by gestational age. J Clin Med. 2026. PMID: 41753292. DOI: 10.3390/jcm15041605.",
  Li2026: "Li W, et al. Antenatal corticosteroid-to-birth interval and late preterm neonatal outcomes. BMC Pregnancy Childbirth. 2026. PMID: 41872805. DOI: 10.1186/s12884-026-08961-1.",
  Zigron2021: "Zigron R, et al. Antenatal corticosteroid-to-delivery interval and neonatal hypoglycaemia. Int J Gynaecol Obstet. 2021. PMID: 34625970. DOI: 10.1002/ijgo.13975.",
  Tuohy2021: "Tuohy JF, et al. Maternal and neonatal glycaemic control after antenatal corticosteroid administration in women with diabetes in pregnancy: a retrospective cohort study. PLoS One. 2021. PMID: 33600450. DOI: 10.1371/journal.pone.0246175.",
  Roberts2017: "Roberts D, Brown J, Medley N, Dalziel SR. Antenatal corticosteroids for accelerating fetal lung maturation for women at risk of preterm birth. Cochrane Database Syst Rev. 2017. PMID: 28321847. DOI: 10.1002/14651858.CD004454.pub3.",
  McGoldrick2020: "McGoldrick E, Stewart F, Parker R, Dalziel SR. Antenatal corticosteroids for accelerating fetal lung maturation for women at risk of preterm birth. Cochrane Database Syst Rev. 2020;12(12):CD004454. PMID: 33368142. DOI: 10.1002/14651858.CD004454.pub4.",
  Vermillion1999: "Vermillion ST, Soper DE, Bland ML, Newman RB. Effectiveness of antenatal corticosteroid administration after preterm premature rupture of the membranes. Am J Obstet Gynecol. 1999. PMID: 10454676. DOI: 10.1016/s0002-9378(99)70555-7.",
  McKenna2004: "McKenna DS, et al. Maternal adrenal function after a single course of betamethasone: ACTH-stimulation testing at term. J Matern Fetal Neonatal Med. 2004. PMID: 15370080. DOI: 10.1080/14767050412331283102.",
  McKenna2000: "McKenna DS, Wittber GM, Nagaraja HN, Samuels P. The effects of repeat doses of antenatal corticosteroids on maternal adrenal function. Am J Obstet Gynecol. 2000. PMID: 10992191. DOI: 10.1067/mob.2000.106755.",
  Murphy2008: "Murphy KE, et al; MACS Collaborative Group. Multiple courses of antenatal corticosteroids for preterm birth (MACS): a randomised controlled trial. Lancet. 2008. PMID: 19101390. DOI: 10.1016/S0140-6736(08)61929-7.",
  Asztalos2013: "Asztalos EV, et al. Association between gestational age at birth, antenatal corticosteroids, and outcomes at 5 years (MACS-5). JAMA Pediatr. 2013;167(12):1102-1110. PMID: 24126948. DOI: 10.1001/jamapediatrics.2013.2764.",
  Crowther2006: "Crowther CA, et al; ACTORDS Study Group. Outcomes at 2 years of age after repeat doses of antenatal corticosteroids. Lancet. 2006. PMID: 16765760. DOI: 10.1016/S0140-6736(06)68846-6.",
  Wapner2007: "Wapner RJ, et al. Long-term outcomes after repeat doses of antenatal corticosteroids. N Engl J Med. 2007. PMID: 17881751. DOI: 10.1056/NEJMoa071453.",
};

let body = "";

// ---------------------------------------------------------------------
// Cover
// ---------------------------------------------------------------------
body += `
<div class="kicker">DEPARTMENTAL EVIDENCE SYNTHESIS &amp; PRACTICE PROPOSAL</div>
<h1 class="title">Aligning Antenatal Dexamethasone Dosing with RCOG Guidance</h1>
<p class="subtitle">The case for discontinuing the unlicensed 12&nbsp;mg 12-hourly regimen in favour of the RCOG/ASTEROID-tested 12&nbsp;mg 24-hourly schedule</p>
<p class="corresp">Prepared for departmental review and clinical governance discussion. Author and unit details to be completed by the submitting clinician.</p>
`;

// ---------------------------------------------------------------------
// Purpose box
// ---------------------------------------------------------------------
body += `
<div class="keybox">
  <div class="keybox-title">What this document asks the department to do</div>
  <p>Adopt <strong>dexamethasone 12&nbsp;mg IM, two doses, 24 hours apart</strong> &mdash; the regimen named in RCOG Green-top Guideline No.&nbsp;74 and tested in the ASTEROID trial &mdash; as the unit's standard, in place of the current practice of giving the same 12&nbsp;mg dose at a compressed <strong>12-hour</strong> interval.</p>
  <p>This is not a claim that the current practice has been shown to cause harm. It is a claim, supported by a systematic search of the trial, guideline, and pharmacological literature, that the current practice has never been shown to be <em>safe or effective</em> either &mdash; it sits entirely outside the evidence base that justifies antenatal corticosteroid use in the first place. Where a tested, guideline-endorsed alternative exists at no cost to the woman or her baby, that absence of evidence is itself sufficient reason to change practice.</p>
</div>
`;

// ---------------------------------------------------------------------
// Figure 1 up front - headline visual
// ---------------------------------------------------------------------
body += fig("fig1_three_regimens.png", 98);

// ---------------------------------------------------------------------
// Executive summary
// ---------------------------------------------------------------------
body += h1("Executive summary");
body += "<ul>" +
  li("Three dexamethasone regimens exist in global use. Two are trial-tested and guideline-endorsed. The unit's current practice is a third, untested hybrid: it combines the per-dose amount of the RCOG regimen with the interval of the WHO regimen, and this specific combination has never been the subject of a randomised trial, cohort study, or named guideline recommendation, in any jurisdiction identified.@@RCOG2022,Oladapo2020,Crowther2019@@") +
  li("The pharmacological rationale sometimes offered for tolerating a shorter interval (that betamethasone's depot formulation justifies dexamethasone doing the same) does not hold up: the UK betamethasone preparation is confirmed to be a plain, non-depot phosphate ester, not the US depot mixture.@@Jobe2019@@ The genuine mechanistic literature on surfactant induction favours sustained exposure over peak concentration, meaning a compressed interval is not expected to add benefit and could plausibly reduce it.@@Samtani2006,Ballard1996@@") +
  li("The only randomised dosing-interval trial for either drug &mdash; betamethasone, not dexamethasone &mdash; found equivalent respiratory outcomes but a significant excess of necrotising enterocolitis at the shorter interval, in a signal that has never been replicated or refuted in fourteen years.@@Khandelwal2012@@") +
  li("Short administration-to-delivery intervals are consistently associated with more, not less, neonatal hypoglycaemia across multiple contemporary cohorts, undermining any assumption that a compressed second dose is a low-risk way to \"complete the course\" before an anticipated birth.@@Gulersen2021,Li2026,Edut2026,Zigron2021@@") +
  li("A fetal sheep study modelling this exact regimen (12&nbsp;mg dexamethasone, two doses, 12 hours apart) found a hippocampal transcriptional signal enriched for neurodegeneration-associated pathways, independent of any respiratory benefit &mdash; animal evidence only, but the single most directly relevant finding identified anywhere in this search regarding the specific regimen under review.@@Carter2024@@") +
  li("None of this constitutes proof of harm. It constitutes a consistent absence of supporting evidence, a plausible mechanistic case against added benefit, and enough scattered signal of concern that continuing an untested regimen, when a tested and equally practical alternative exists, is difficult to justify on clinical-governance grounds.") +
  "</ul>";

// ---------------------------------------------------------------------
// Background
// ---------------------------------------------------------------------
body += h1("1. Background and scope");
body += p("Antenatal corticosteroids are one of the most consistently effective interventions in perinatal medicine, and this document does not question that. The question is narrower and more specific: when dexamethasone is the chosen agent, and 12&nbsp;mg is the chosen per-dose amount, should the two doses be given 12 hours apart, as is current practice in this unit, or 24 hours apart, as recommended by the Royal College of Obstetricians and Gynaecologists?@@RCOG2022@@");
body += p("This document was produced through a systematic search of PubMed and academic literature databases for trials, systematic reviews, cohort studies, and pharmacokinetic data addressing dexamethasone regimen and dosing interval specifically, cross-checked against RCOG, WHO, and European guideline positions. Every reference cited carries a verified PMID and/or DOI. Every clinical claim is labelled with its certainty, and mechanistic or pharmacological reasoning is explicitly distinguished from direct clinical trial evidence throughout. The full evidence synthesis, including sections not reproduced here in full (maternal glycaemic management, the imminent-delivery scenario, and a complete GRADE summary table), is available as a companion document.");

// ---------------------------------------------------------------------
// Section 2: The regimens and the gap
// ---------------------------------------------------------------------
body += h1("2. Three regimens, one of them untested");
body += p("RCOG Green-top Guideline No.&nbsp;74 names two dexamethasone options, both totalling 24&nbsp;mg: 12&nbsp;mg IM twice, 24 hours apart (matching the ASTEROID trial, the largest and best-characterised head-to-head comparison against betamethasone), or 6&nbsp;mg IM four times, 12 hours apart (matching the WHO/ACOG standard and the WHO ACTION-I trial).@@RCOG2022,Crowther2019,Oladapo2020@@ Neither RCOG, the WHO 2022 recommendation, ACOG guidance, nor a 2023 European perinatal-care consensus statement names a third option combining the 12&nbsp;mg per-dose amount with a 12-hourly interval.@@Daskalakis2023@@");
body += p("This is confirmed, not assumed. The 2022 Cochrane review dedicated specifically to comparing antenatal corticosteroid regimens identifies only three studies anywhere in the global trial base that compare any regimen variant of any agent &mdash; and states plainly that the evidence \"does not support the use of one particular corticosteroid regimen over another.\"@@Williams2022@@ None of the three concerns dexamethasone interval. One compares betamethasone at 12-hourly versus 24-hourly intervals, rated very-low certainty.@@Khandelwal2012@@ A search of six independent strategies in this review found no RCT, no comparative cohort, and no study of any design comparing dexamethasone 12&nbsp;mg at a 12-hourly interval against 24-hourly, for any outcome.");
body += p("A fair reading of the record shows the regimen has real clinical precedent: a UK protocol paper (Salford, 2003) and a Malaysian trial (2021) both describe this exact schedule as the background ACS practice at their respective institutions.@@Kaushal2003,Hong2021@@ Neither paper tested the regimen's own efficacy or safety &mdash; both simply used it as the fixed backdrop while studying something else (glycaemic control). The regimen has therefore persisted in scattered international practice for at least two decades without ever itself being the subject of a trial measuring respiratory outcome, brain injury, or survival against the tested alternative. That longevity is not evidence of safety; it is a description of how an untested practice can become routine.");

body += h2("Table 1. The three regimens compared");
body += table(
  ["", "Regimen A — WHO/ACOG", "Regimen B — RCOG/ASTEROID (recommended)", "Regimen C — current unit practice"],
  [
    ["Dose per injection", "6 mg IM", "12 mg IM", "12 mg IM"],
    ["Interval", "Every 12 hours", "Every 24 hours", "Every 12 hours"],
    ["Doses / total", "4 doses / 24 mg", "2 doses / 24 mg", "2 doses / 24 mg"],
    ["Trial evidence", "WHO ACTION-I, n=2852", "ASTEROID, n=1346", "None identified"],
    ["Guideline status", "WHO/ACOG endorsed", "RCOG primary recommendation", "Not named by any guideline identified"],
  ],
  ["20%", "27%", "27%", "26%"]
);

// ---------------------------------------------------------------------
// Section 3: The pharmacological case
// ---------------------------------------------------------------------
body += h1("3. The pharmacological case for concern is real, but genuinely unresolved");
body += p("The intuitive explanation sometimes offered for tolerating a compressed dexamethasone interval &mdash; that betamethasone's own 24-hourly interval reflects a slow-release depot mechanism dexamethasone lacks, so betamethasone's interval logic simply doesn't transfer &mdash; turns out to rest on a factual error about the UK preparation. Betamethasone as used in the UK is confirmed to be the plain sodium phosphate ester, without the acetate depot fraction found in the US Celestone Chronodose product.@@Jobe2019@@ The two drugs are, in the UK, pharmacokinetically more alike than commonly assumed: both are non-depot phosphate esters, and the genuine distinguishing factor is that betamethasone phosphate clears roughly twice as slowly as dexamethasone phosphate.@@Jobe2019,Petersen1983,Tsuei1980@@");
body += p("This does not settle the interval question &mdash; it sharpens it. Two human pharmacokinetic datasets give discordant dexamethasone half-life estimates that disagree by more than two-fold (2.37 hours in pregnant women near term at an 8&nbsp;mg dose, versus 5.2 hours in non-pregnant women at a 6&nbsp;mg dose), and neither has ever been measured at the unit's actual 12&nbsp;mg dose in pregnant women.@@Tsuei1980,Jobe2019@@ Figure 3 shows both pictures side by side, honestly, rather than picking the one that makes the strongest case.");

body += fig("fig3_pk_trough.png", 92);

body += p("What tips the balance toward caution is not the unresolved half-life arithmetic alone, but the mechanistic literature on how glucocorticoids actually induce surfactant production. The best-characterised pharmacokinetic/pharmacodynamic modelling and human fetal lung explant data converge on a time-dependent, not peak-dependent, mechanism: sustained receptor occupancy above a threshold drives the maturational effect, and a rat model of exactly this kind of frequent dosing found the effect on one surfactant protein became partly <em>inhibitory</em> rather than simply diminishing.@@Samtani2006,Ballard1996,Venkatesh1993@@ In plain terms: compressing the interval is not expected, on this evidence, to make the injection work better or faster &mdash; and cannot be assumed to be a harmless variant of a proven regimen simply because the total milligram dose is unchanged.");

// ---------------------------------------------------------------------
// Section 4: The clinical signal
// ---------------------------------------------------------------------
body += h1("4. The one interval trial that exists shows a safety signal, not a reassurance");
body += p("Khandelwal and colleagues randomised 228 women to betamethasone given 12 hours or 24 hours apart &mdash; the only interval-comparison RCT for either drug in the entire literature.@@Khandelwal2012@@ Respiratory outcomes were equivalent. Necrotising enterocolitis was not.");

body += fig("fig4_khandelwal.png", 92);

body += p("This trial is not proof that dexamethasone at 12 hours causes NEC. It is small, single-centre, unblinded, concerns a different drug, and has never been replicated despite the original authors' own call for a larger confirmatory trial. But it is the only direct experimental evidence anywhere on whether compressing an antenatal corticosteroid interval carries a downside, and the answer it gives is not reassuring. A regimen decision that rests on \"no evidence of harm\" should account for the fact that the one study that actually looked found a harm signal.");

// ---------------------------------------------------------------------
// Section 5: Imminent delivery
// ---------------------------------------------------------------------
body += h1("5. The scenario that drives current practice does not withstand scrutiny");
body += p("The stated rationale for the 12-hourly interval is operational: it lets a course be completed before an anticipated early delivery. This section addresses that scenario directly.");
body += p("The evidence on treatment-to-delivery timing consistently shows little or no respiratory benefit when delivery occurs under 24 hours from the first dose, with benefit concentrated in the 24-hour-to-7-day window.@@McDougall2023,Gulersen2021@@ The one study to examine hour-scale bands from the first dose specifically found no significant difference in outcome across bands under 36 hours.@@Kraft2025@@ No study identified reports a benefit specifically attributable to a dose landing in the 12&ndash;13-hour window.");
body += p("The mechanistic case is, if anything, more decisive. The fastest biochemical response to glucocorticoid exposure documented in any experimental system &mdash; fetal rabbit lung organ culture &mdash; first appears after 12 hours of continuous exposure and rises over the following 24 hours; human fetal lung explants require 24&ndash;48 hours for maximal surfactant protein induction.@@Gross1983,Liley1988@@ A second dose given at hour 12, with birth at hour 13, contributes roughly one additional hour of exposure before delivery &mdash; shorter than the fastest response ever reported in any system tested. There is no plausible mechanism by which that specific second dose, as distinct from the first dose already circulating, could measurably influence fetal lung maturation before this birth.");
body += p("Nor is the second dose free of downside risk merely because it may not have time to help. Shorter administration-to-delivery intervals are repeatedly associated with <em>increased</em> neonatal hypoglycaemia across several contemporary cohorts.@@Gulersen2021,Li2026,Edut2026,Zigron2021@@ A dose given in the final hour before birth cannot be assumed harm-free on the basis that it \"probably didn't have time to do much\" &mdash; the harm side of that argument does not hold even where the benefit side fails.");

body += fig("fig2_decision_pathway.png", 90);

body += p("The first dose should never be withheld or delayed &mdash; even a partial course reduces risk relative to none, and this is well established and not in question.@@SaldanaGarcia2021@@ What this section challenges is specifically the practice of compressing the <em>second</em> dose to 12 hours in order to \"finish the course\" before an anticipated birth. That specific action has no identified mechanistic basis for benefit and a real, if unquantified, basis for concern.");

// ---------------------------------------------------------------------
// Section 6: Maternal safety - balanced
// ---------------------------------------------------------------------
body += h1("6. Maternal safety: a fair account, not a one-sided one");
body += p("In the interest of an accurate picture, this section states plainly where the evidence does not support alarm. Two institutions that have used the unit's actual 12&nbsp;mg/12-hourly regimen as their background protocol &mdash; Salford, UK, and Kuala Lumpur, Malaysia &mdash; report a real but self-limited hyperglycaemic pattern, concentrated on day 1 and largely resolved by day 2&ndash;3.@@Kaushal2003,Hong2021@@ This is not obviously more alarming in shape than the wider literature on maternal hyperglycaemia after any antenatal corticosteroid regimen, though no study has directly compared the two intervals for this outcome, so equivalence cannot be claimed &mdash; only that no interval-specific alarm signal has been incidentally observed where this regimen happens to have been studied for other reasons.@@Tuohy2021@@");
body += p("Single-course antenatal corticosteroids, at the standard interval, do not significantly increase maternal chorioamnionitis or endometritis, and adrenal suppression after a single course resolves without clinical sequelae by term.@@Roberts2017,McGoldrick2020,Vermillion1999,McKenna2004@@ The infection and adrenal-suppression signal in the literature concerns <em>repeat courses</em> (McKenna et al 2000, PMID 10992191), not the spacing of two doses within a single course &mdash; a distinct exposure pattern that this document does not conflate with the interval question.@@McKenna2000@@ No study has isolated dosing interval as a variable for maternal infection or adrenal outcomes in either direction; this is an honest absence of evidence, not a hidden reassurance.");

// ---------------------------------------------------------------------
// Section 7: Long-term
// ---------------------------------------------------------------------
body += h1("7. The long-term picture: one genuine mechanistic warning, kept in proportion");
body += p("No trial or cohort reporting neurodevelopmental outcomes after the 12-hourly dexamethasone regimen exists. This is confirmed, not inferred from silence &mdash; a targeted search found nothing. The single most directly relevant piece of evidence identified anywhere in this review is a fetal sheep study that explicitly modelled this exact clinical regimen (two 12&nbsp;mg dexamethasone doses, 12 hours apart, described by the authors as representing current practice in at least one other jurisdiction) and found hippocampal transcriptional changes enriched for neurodegeneration-associated pathways, independent of any respiratory benefit, while a comparator arm producing a smoother fetal exposure profile did not show the same signal.@@Carter2024@@ This is animal evidence. It does not establish that the regimen causes harm in human infants. It is, however, a biologically specific and directly relevant finding, not a generic caution, and a department deciding whether to continue an untested regimen is entitled to weigh it.");
body += p("For context, and to keep this in proportion: repeat antenatal corticosteroid <em>courses</em> (given days to weeks apart, with near-complete drug clearance between exposures) have been extensively studied across four large RCT programmes and show no consistent adverse neurodevelopmental signal at follow-up to 5&ndash;8 years.@@Murphy2008,Asztalos2013,Crowther2006@@ One isolated repeat-course trial found a numerically large but statistically imprecise excess of cerebral palsy that has not been replicated in the larger programmes.@@Wapner2007@@ This reassurance cannot be extended with confidence to interval compression <em>within</em> a single course, since the two exposure patterns are pharmacologically distinct &mdash; but it demonstrates that this literature, when it has looked for long-term harm from glucocorticoid exposure patterns, has generally not found it, which is worth stating alongside the Carter et al signal rather than instead of it.");
body += p("Separately, and for completeness rather than because it bears directly on the interval question: ASTEROID's own long-term comparison of dexamethasone against betamethasone, both given at the standard 24-hourly interval, found a cerebral palsy risk ratio of 2.50 with a 95% confidence interval of 0.97 to 6.39 &mdash; a result compatible with both no difference and a more than sixfold increase in risk with dexamethasone.@@Crowther2019,Williams2022@@ This concerns choice of agent, not interval, and must not be read as evidence about the 12-hourly question. It is included here only because it means dexamethasone's overall long-term safety record carries a genuinely open question even at the guideline-recommended interval, and a proposal to standardise on that interval should say so plainly rather than imply the recommended regimen is risk-free by comparison.");

// ---------------------------------------------------------------------
// Section 8: Recommendation
// ---------------------------------------------------------------------
body += h1("8. Recommendation");
body += `
<div class="recbox">
  <p><strong>Adopt dexamethasone 12&nbsp;mg IM, two doses, 24 hours apart, as the unit standard for dexamethasone-based antenatal corticosteroid therapy</strong>, in line with RCOG Green-top Guideline No.&nbsp;74 and the ASTEROID trial.</p>
  <p><strong>Discontinue the practice of giving the second dose at 12 hours to "complete the course" when delivery is anticipated within 24 hours.</strong> Give the first dose immediately regardless of how imminent delivery appears &mdash; this remains correct and is not in question &mdash; but give the second dose at the standard 24-hour mark, or not at all if delivery has already occurred.</p>
  <p><strong>Where the WHO/ACOG four-dose regimen (6&nbsp;mg IM every 12 hours) is preferred for operational reasons, use that regimen in full</strong>, rather than a hybrid that borrows only its interval.</p>
</div>
`;
body += p("This recommendation is built on an absence of supporting evidence for the current practice, a coherent pharmacological argument against expecting any efficacy benefit from compression, one small but unreplicated safety signal in the only relevant interval trial, a consistent association between short administration-to-delivery intervals and neonatal hypoglycaemia, and one directly relevant animal mechanistic finding. No single piece of this evidence is individually conclusive. Together, weighed against a tested and equally practical alternative that costs nothing extra to adopt, they support changing practice on ordinary clinical-governance grounds: when a guideline-endorsed, trial-tested option exists and an untested option does not offer a demonstrated advantage, the tested option should be preferred.");
body += p("This is not a criticism of clinicians who have used the current regimen. It has real documented precedent, including in the UK, and was reasonably adopted as a practical response to the operational pressure of imminent delivery. The evidence assembled here simply was not available in a synthesised form until now.");

// ---------------------------------------------------------------------
// Section 9: What would change this
// ---------------------------------------------------------------------
body += h1("9. What would change this recommendation");
body += "<ul>" +
  li("A randomised trial directly comparing dexamethasone 12mg at 12-hourly versus 24-hourly intervals, adequately powered for NEC, hypoglycaemia, and longer-term outcome, would directly answer the question this document can only address by inference.") +
  li("Direct pharmacokinetic measurement of maternal and fetal dexamethasone concentrations after a 12mg IM dose in pregnant women, at both intervals, would resolve the two-fold discrepancy in current half-life estimates and remove the single largest evidentiary gap in the pharmacological case.") +
  li("Replication (or refutation) of the Khandelwal necrotising enterocolitis signal in a larger, multicentre trial would materially change the confidence with which this document's caution is held.") +
  li("Any clinical (as opposed to animal) neurodevelopmental data specific to the 12-hourly dexamethasone regimen would be the single most informative addition to this evidence base.") +
  "</ul>";

// ---------------------------------------------------------------------
// Limitations
// ---------------------------------------------------------------------
body += h1("10. Access limitations and honest caveats");
body += p("The network environment used to prepare this synthesis blocked direct access to medicines.org.uk (SPC/EMC), nice.org.uk, rcog.org.uk, and acog.org throughout the search. Guideline wording quoted or summarised in this document is therefore reconstructed from search-engine snippets and previously verified secondary sources, not read directly from primary PDFs or the Summary of Product Characteristics. The finding that no guideline endorses the current regimen is a convergent negative finding across every source checked, and is very likely to hold, but should be independently confirmed against the primary RCOG, NICE, and SPC documents before this document is used as the sole basis for a formal guideline change. Two source papers on fetal lung explant time-course (Gross 1983, Liley 1988) were verified by DOI but did not return a PMID from the search tools used in this review.");

// ---------------------------------------------------------------------
// References
// ---------------------------------------------------------------------
body += `<div class="pagebreak"></div>`;
body += h1("References");
body += `<ol class="refs">\n`;
citeOrder.forEach((key) => {
  const text = REF[key] || `[Reference data missing for key: ${key}]`;
  body += `<li>${text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")}</li>\n`;
});
body += `</ol>\n`;

// ---------------------------------------------------------------------
// CSS
// ---------------------------------------------------------------------
const css = `
@page {
  size: A4;
  margin: 20mm 18mm 22mm 18mm;
  @bottom-center { content: counter(page); font-size: 8.5pt; color: #888; }
}
* { box-sizing: border-box; }
body { font-family: Calibri, "Liberation Sans", Arial, sans-serif; font-size: 10.8pt; line-height: 1.5; color: #16202a; }
.kicker { font-size: 9.5pt; font-weight: 700; letter-spacing: 1.6px; color: #C55A11; margin-bottom: 8pt; }
.title { font-size: 22pt; color: #1F3864; margin: 0 0 10pt 0; line-height: 1.25; }
.subtitle { font-size: 12.5pt; font-style: italic; color: #3A4A5A; margin: 0 0 8pt 0; }
.corresp { font-size: 9pt; font-style: italic; color: #888; margin: 0 0 16pt 0; }
h1 { font-size: 15pt; color: #1F3864; margin: 20pt 0 9pt 0; border-bottom: 1.5pt solid #1F3864; padding-bottom: 4pt; }
h2 { font-size: 12pt; color: #1F3864; margin: 12pt 0 6pt 0; }
p { margin: 0 0 9pt 0; text-align: justify; }
sup { color: #1F3864; font-weight: 600; }
.keybox { background: #EAF1FB; border: 0.75pt solid #B9CDE8; border-radius: 4pt; padding: 12pt 16pt; margin: 4pt 0 16pt 0; }
.keybox-title { font-size: 12.5pt; font-weight: 700; color: #1F3864; margin-bottom: 8pt; }
.keybox p { margin-bottom: 7pt; }
.recbox { background: #EAF6EC; border-left: 4pt solid #2E7D32; padding: 12pt 16pt; margin: 8pt 0 12pt 0; }
.recbox p { margin-bottom: 8pt; }
ul { padding-left: 18pt; margin: 0 0 12pt 0; }
li { margin-bottom: 6pt; }
table { width: 100%; border-collapse: collapse; margin: 6pt 0 16pt 0; font-size: 9.6pt; }
th { background: #1F3864; color: white; text-align: left; padding: 6pt 8pt; font-weight: 600; }
td { padding: 6pt 8pt; border-bottom: 0.5pt solid #D9D9D9; vertical-align: top; text-align: left; }
tr:nth-child(even) td { background: #F7F9FC; }
.figwrap { text-align: center; margin: 10pt 0 16pt 0; page-break-inside: avoid; }
.figwrap img { max-width: 100%; }
.figcap { text-align: left; font-size: 9pt; color: #555; margin-top: 6pt; }
.refs { font-size: 9.2pt; padding-left: 20pt; word-break: break-word; }
.refs li { margin-bottom: 7pt; }
.pagebreak { page-break-before: always; }
`;

const html = `<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Aligning Antenatal Dexamethasone Dosing with RCOG Guidance</title><style>${css}</style></head>
<body>${body}</body>
</html>`;

const fixedHtml = html
  .replace(/&amp;nbsp;/g, "&nbsp;")
  .replace(/&amp;mdash;/g, "&mdash;")
  .replace(/&amp;ndash;/g, "&ndash;")
  .replace(/&lt;em&gt;/g, "<em>")
  .replace(/&lt;\/em&gt;/g, "</em>")
  .replace(/&lt;strong&gt;/g, "<strong>")
  .replace(/&lt;\/strong&gt;/g, "</strong>");

const outPath = "/home/user/inspiring-truffle-571df6/acs-interval-review/ACS_interval_practice_change_proposal.html";
fs.writeFileSync(outPath, fixedHtml);
console.log("Wrote", outPath, "with", citeOrder.length, "references cited.");
