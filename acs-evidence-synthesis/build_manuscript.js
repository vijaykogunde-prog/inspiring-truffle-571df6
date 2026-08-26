const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ImageRun, BorderStyle,
  ShadingType, PageBreak, Header, Footer, PageNumber, VerticalAlign,
} = require("docx");

const FIGDIR = "/home/user/inspiring-truffle-571df6/acs-evidence-synthesis/figures";

// ---------------------------------------------------------------------
// Citation registry: assigns Vancouver numbers by order of first use
// ---------------------------------------------------------------------
const citeOrder = [];
const citeMap = new Map();
function citeNum(key) {
  if (!citeMap.has(key)) {
    citeMap.set(key, citeOrder.length + 1);
    citeOrder.push(key);
  }
  return citeMap.get(key);
}

// Parses "...text...@@key1,key2@@..." into an array of TextRun objects,
// converting @@...@@ tokens into superscript Vancouver numbers.
function runsFrom(text, opts = {}) {
  const parts = text.split(/@@(.*?)@@/g);
  const runs = [];
  parts.forEach((part, i) => {
    if (i % 2 === 0) {
      if (part.length) runs.push(new TextRun({ text: part, ...opts }));
    } else {
      const nums = part.split(",").map((k) => citeNum(k.trim())).sort((a, b) => a - b);
      runs.push(new TextRun({ text: nums.join(","), superScript: true, ...opts }));
    }
  });
  return runs;
}

function P(text, opts = {}) {
  const { bold, italics, size, color, align, spacingAfter = 200, spacingBefore = 0, style: pStyle } = opts;
  return new Paragraph({
    alignment: align || AlignmentType.JUSTIFIED,
    spacing: { after: spacingAfter, before: spacingBefore, line: 276 },
    children: runsFrom(text, { bold, italics, size, color }),
  });
}

function H1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 400, after: 200 },
    children: [new TextRun({ text, bold: true, size: 26, color: "1F3864" })],
  });
}

function H2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 280, after: 140 },
    children: [new TextRun({ text, bold: true, size: 23, color: "1F3864" })],
  });
}

function figParagraph(file, widthPx, heightPx, caption) {
  const data = fs.readFileSync(`${FIGDIR}/${file}`);
  return [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 240, after: 120 },
      children: [
        new ImageRun({
          type: "png",
          data,
          transformation: { width: widthPx, height: heightPx },
        }),
      ],
    }),
    new Paragraph({
      alignment: AlignmentType.LEFT,
      spacing: { after: 300 },
      children: runsFrom(caption, { size: 18, italics: true, color: "404040" }),
    }),
  ];
}

function cellPara(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 60 },
    children: runsFrom(text, { size: opts.size || 18, bold: opts.bold || false }),
  });
}

function makeTable(headers, rows, colWidths) {
  const totalWidth = 9350;
  const toRow = (cells, isHeader) =>
    new TableRow({
      tableHeader: isHeader,
      children: cells.map((c, i) => new TableCell({
        width: { size: colWidths[i], type: WidthType.DXA },
        shading: isHeader ? { type: ShadingType.CLEAR, fill: "1F3864" } : undefined,
        verticalAlign: VerticalAlign.CENTER,
        margins: { top: 80, bottom: 80, left: 100, right: 100 },
        children: [cellPara(c, { bold: isHeader, size: isHeader ? 18 : 18 })],
      })),
    });
  return new Table({
    width: { size: totalWidth, type: WidthType.DXA },
    columnWidths: colWidths,
    rows: [toRow(headers, true), ...rows.map((r) => toRow(r, false))],
  });
}

// ---------------------------------------------------------------------
// Reference bibliographic data (Vancouver). Every entry PMID/DOI-verified
// via PubMed during the source evidence synthesis for this manuscript.
// ---------------------------------------------------------------------
const REF = {
  Liggins1972: "Liggins GC, Howie RN. A controlled trial of antepartum glucocorticoid treatment for prevention of the respiratory distress syndrome in premature infants. Pediatrics. 1972;50(4):515-525. PMID: 4561295.",
  McGoldrick2020: "McGoldrick E, Stewart F, Parker R, Dalziel SR. Antenatal corticosteroids for accelerating fetal lung maturation for women at risk of preterm birth. Cochrane Database Syst Rev. 2020;12(12):CD004454. doi:10.1002/14651858.CD004454.pub4. PMID: 33368142.",
  RCOG2022: "Stock SJ, Thomson AJ, Papworth S; Royal College of Obstetricians and Gynaecologists. Antenatal corticosteroids to reduce neonatal morbidity and mortality: Green-top Guideline No. 74. BJOG. 2022;129(8):e35-e60. doi:10.1111/1471-0528.17027. PMID: 35172391.",
  WHO2022: "World Health Organization. WHO recommendations on antenatal corticosteroids for improving preterm birth outcomes. Geneva: World Health Organization; 2022.",
  Oladapo2020: "Oladapo OT, Vogel JP, Piaggio G, et al; WHO ACTION-I Trial Collaborators. Antenatal dexamethasone for early preterm birth in low-resource countries. N Engl J Med. 2020;383(26):2514-2525. doi:10.1056/NEJMoa2022398. PMID: 33095526.",
  Jobe2020: "Jobe AH, Kemp M, Schmidt A, Takahashi T, Newnham J, Milad M. Antenatal corticosteroids: a reappraisal of the drug formulation and dose. Pediatr Res. 2020;89(2):318-325. doi:10.1038/s41390-020-01249-w. PMID: 33177675.",
  Khandelwal2012: "Khandelwal M, Chang E, Hansen C, Hunter K, Milcarek B. Betamethasone dosing interval: 12 or 24 hours apart? A randomized, noninferiority open trial. Am J Obstet Gynecol. 2012;206(3):201.e1-11. doi:10.1016/j.ajog.2012.01.025. PMID: 22381601.",
  Bulut2021: "Bulut AN, et al. The effect of betamethasone dosing interval on perinatal outcomes: 12 hours or 24 hours apart. Am J Perinatol. 2021. doi:10.1055/s-0041-1735962. PMID: 34544193.",
  SaldanaGarcia2022b: "Saldana-Garcia N, et al. Antenatal betamethasone every 12 hours in imminent preterm labour. J Clin Med. 2022;11(5):1227. doi:10.3390/jcm11051227. PMID: 35268318.",
  Williams2022: "Williams MJ, Ramson JA, Brownfoot FC. Different corticosteroids and regimens for accelerating fetal lung maturation for babies at risk of preterm birth. Cochrane Database Syst Rev. 2022;8(8):CD006764. doi:10.1002/14651858.CD006764.pub4. PMID: 35943347.",
  Baud2001: "Baud O, et al. Mechanisms of sulfite-associated neuronal injury relevant to dexamethasone preparations [animal/in vitro study]. Pediatr Res. 2001. doi:10.1203/00006450-200112000-00013. PMID: 11726728.",
  Dani2007: "Dani C, et al. Sulfite-related neuronal toxicity of dexamethasone preparations in vitro. J Matern Fetal Neonatal Med. 2007. doi:10.1080/14767050701227992. PMID: 17437241.",
  Baud1999: "Baud O, Foix-L'Helias L, Kaminski M, et al. Antenatal glucocorticoid treatment and cystic periventricular leukomalacia in very premature infants. N Engl J Med. 1999;341(16):1190-1196. doi:10.1056/NEJM199910143411604. PMID: 10519896.",
  Melamed2015: "Melamed N, et al. Association between antenatal corticosteroid administration-to-birth interval and outcomes of preterm neonates. Obstet Gynecol. 2015;125(6):1377-1384. doi:10.1097/AOG.0000000000000840. PMID: 26000509.",
  Norman2017: "Norman M, et al. Association of short antenatal corticosteroid administration-to-birth intervals with survival and morbidity among very preterm infants: results from the EPICE cohort. JAMA Pediatr. 2017;171(7):678-686. doi:10.1001/jamapediatrics.2017.0602. PMID: 28505223.",
  Chawla2025: "Chawla S, et al. Betamethasone-to-delivery interval and outcomes in extremely preterm infants (NICHD Neonatal Research Network). JAMA Netw Open. 2025. doi:10.1001/jamanetworkopen.2024.61312. PMID: 39982720.",
  SaldanaGarcia2021: "Saldana-Garcia N, et al. Benefits of a single dose of betamethasone in imminent preterm labour. J Clin Med. 2021;11(1):20. doi:10.3390/jcm11010020. PMID: 35011761.",
  Schmitz2022: "Schmitz T, et al; BETADOSE study group. Neonatal outcomes for women at risk of preterm delivery given half dose versus full dose of antenatal betamethasone. Lancet. 2022. doi:10.1016/S0140-6736(22)01535-5. PMID: 35988568.",
  Kemp2018: "Kemp MW, et al. Antenatal glucocorticoid exposure duration and fetal lung maturation in sheep. Am J Obstet Gynecol. 2018. doi:10.1016/j.ajog.2018.05.007. PMID: 29758177.",
  Fee2023: "Fee EL, et al. Fetal plasma betamethasone threshold for lung maturation in sheep. Am J Physiol Lung Cell Mol Physiol. 2023. doi:10.1152/ajplung.00139.2023. PMID: 37697929.",
  Been2011: "Been JV, et al. Antenatal steroids and neonatal outcome after chorioamnionitis: a meta-analysis. BJOG. 2011. doi:10.1111/j.1471-0528.2010.02751.x. PMID: 21054759.",
  Amiya2016: "Amiya RM, et al. Antenatal corticosteroids for reducing adverse maternal and child outcomes in special populations of women at risk of imminent preterm birth. PLoS One. 2016. doi:10.1371/journal.pone.0147604. PMID: 26841022.",
  Elimian2000: "Elimian A, et al. Histologic chorioamnionitis, antenatal steroids, and perinatal outcomes. Obstet Gynecol. 2000. doi:10.1016/s0029-7844(00)00928-5. PMID: 10960621.",
  Ryu2019: "Ryu YH, et al. The associations between antenatal corticosteroids and in-hospital outcomes of preterm singleton AGA neonates according to maternal histologic chorioamnionitis. Neonatology. 2019. doi:10.1159/000502650. PMID: 31593959.",
  Crowther2019: "Crowther CA, et al; ASTEROID Study Group. Maternal intramuscular dexamethasone versus betamethasone before preterm birth (ASTEROID): a multicentre, double-blind, randomised controlled trial. Lancet Child Adolesc Health. 2019. doi:10.1016/S2352-4642(19)30292-5. PMID: 31523039.",
  Lee2006: "Lee BH, et al. Adverse neonatal outcomes associated with antenatal dexamethasone versus antenatal betamethasone. Pediatrics. 2006. doi:10.1542/peds.2005-1749. PMID: 16651303.",
  Lee2008: "Lee BH, et al. Neurodevelopmental outcomes of extremely low birth weight infants exposed prenatally to dexamethasone versus betamethasone. Pediatrics. 2008. doi:10.1542/peds.2007-1103. PMID: 18245420.",
  vanderHeijden2024: "van der Heijden JEM, et al. Optimization of the betamethasone and dexamethasone dosing regimen during pregnancy: a combined placenta perfusion and pregnancy physiologically based pharmacokinetic modeling approach. Am J Obstet Gynecol. 2024. doi:10.1016/j.ajog.2024.05.012. PMID: 38763343.",
  Jobe2019: "Jobe AH, et al. Pharmacokinetics and pharmacodynamics of intramuscular and oral betamethasone and dexamethasone in reproductive age women in India. Clin Transl Sci. 2019. doi:10.1111/cts.12724. PMID: 31808984.",
  Dalziel2005a: "Dalziel SR, et al. Cardiovascular risk factors after antenatal exposure to betamethasone: 30-year follow-up of a randomised controlled trial. Lancet. 2005;365(9474):1856-1862. doi:10.1016/S0140-6736(05)66617-2. PMID: 15924982.",
  Dalziel2005b: "Dalziel SR, et al. Psychological functioning and health-related quality of life in adulthood after preterm birth and antenatal betamethasone. BMJ. 2005;331(7518):665. doi:10.1136/bmj.38576.494363.E0. PMID: 16143712.",
  Murphy2008: "Murphy KE, et al; MACS Collaborative Group. Multiple courses of antenatal corticosteroids for preterm birth (MACS): a randomised controlled trial. Lancet. 2008;372(9656):2143-2151. doi:10.1016/S0140-6736(08)61929-7. PMID: 19101390.",
  Asztalos2013: "Asztalos EV, et al. Association between gestational age at birth, antenatal corticosteroids, and outcomes at 5 years: multiple courses of antenatal corticosteroids for preterm birth study at 5 years of age (MACS-5). JAMA Pediatr. 2013;167(12):1102-1110. doi:10.1001/jamapediatrics.2013.2764. PMID: 24126948.",
  Asztalos2014: "Asztalos EV, et al. Gestational age at birth and outcomes after multiple courses of antenatal corticosteroids: the MACS-5 gestational-age-stratified analysis. BMC Pregnancy Childbirth. 2014;14:272. doi:10.1186/1471-2393-14-272. PMID: 25123162.",
  Crowther2006: "Crowther CA, et al; ACTORDS Study Group. Outcomes at 2 years of age after repeat doses of antenatal corticosteroids. Lancet. 2006;367(9526):1913-1919. doi:10.1016/S0140-6736(06)68846-6. PMID: 16765760.",
  McKinlay2015: "McKinlay CJD, et al. Cardiovascular risk factors in children after repeat doses of antenatal glucocorticoids: an RCT. Pediatrics. 2015;135(2):e405-e415. doi:10.1542/peds.2014-2408. PMID: 25601978.",
  May2025: "May LE, et al. Twenty-year follow-up after repeat antenatal corticosteroids (ACTORDS). PLoS Med. 2025;22(5):e1004618. doi:10.1371/journal.pmed.1004618. PMID: 40435347.",
  GyamfiBannerman2016: "Gyamfi-Bannerman C, et al; NICHD MFMU Network. Antenatal betamethasone for women at risk for late preterm delivery. N Engl J Med. 2016;374(14):1311-1320. doi:10.1056/NEJMoa1516783. PMID: 26842679.",
  GyamfiBannerman2024: "Gyamfi-Bannerman C, et al. Neurodevelopmental outcomes at 6 years after antenatal betamethasone for late preterm birth. JAMA. 2024;331(19):1629-1637. doi:10.1001/jama.2024.4303. PMID: 38656759.",
  HutcheonLiauw2022: "Hutcheon JA, Liauw J. External validity of the ALPS trial for late preterm antenatal corticosteroids in a population-based cohort. Paediatr Perinat Epidemiol. 2022. doi:10.1111/ppe.12856. PMID: 34981851.",
  Raikkonen2020: "Raikkonen K, et al. Associations between maternal antenatal corticosteroid treatment and mental and behavioural disorders in children. JAMA. 2020;323(19):1924-1933. doi:10.1001/jama.2020.3937. PMID: 32427304.",
  Ho2025: "Ho C, et al. Antenatal corticosteroid exposure and neurodevelopmental outcomes by term status: a Taiwanese national cohort. Eur J Pediatr. 2025;184(2):181. doi:10.1007/s00431-025-05994-0. PMID: 39912937.",
  Fichtner2016: "Fichtner PM, et al. Cognitive outcome in term-born children of mothers treated for threatened preterm labour. J Clin Endocrinol Metab. 2016;101(4):1345-1354. doi:10.1210/jc.2015-2453. PMID: 26649618.",
};

module.exports = { P, H1, H2, figParagraph, cellPara, makeTable, citeOrder, citeMap, REF, runsFrom, AlignmentType, TextRun, Paragraph, Document, Packer, HeadingLevel, Table, TableRow, TableCell, WidthType, ImageRun, BorderStyle, ShadingType, PageBreak, Header, Footer, PageNumber, VerticalAlign };
