const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, AlignmentType, ImageRun, PageBreak,
  Header, Footer, PageNumber, VerticalAlign,
} = require("docx");

const NAVY = "1F3864";
const PINK_BG = "FBE4D5";
const GREEN_BG = "E2EFDA";
const GREY_BG = "F2F2F2";

// ---- helpers ---------------------------------------------------------
function h1(text) {
  return new Paragraph({ text, heading: HeadingLevel.HEADING_1, spacing: { before: 300, after: 150 } });
}
function h2(text) {
  return new Paragraph({ text, heading: HeadingLevel.HEADING_2, spacing: { before: 240, after: 120 } });
}
function p(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 120 },
    children: [new TextRun({ text, ...opts })],
  });
}
function pRuns(runs, opts = {}) {
  return new Paragraph({ spacing: { after: 120 }, ...opts, children: runs });
}
function bullet(text, opts = {}) {
  return new Paragraph({
    text, bullet: { level: 0 }, spacing: { after: 80 }, ...opts,
  });
}
function numbered(text, ref) {
  return new Paragraph({
    numbering: { reference: ref, level: 0 },
    spacing: { after: 140 },
    children: parseInlineBold(text),
  });
}
// crude **bold** inline parser so recommendation text can bold key phrases
function parseInlineBold(text) {
  const parts = text.split(/(\*\*[^*]+\*\*)/g);
  return parts.filter(x => x.length).map(part => {
    if (part.startsWith("**") && part.endsWith("**")) {
      return new TextRun({ text: part.slice(2, -2), bold: true });
    }
    return new TextRun({ text: part });
  });
}
function cell(text, { bold = false, shade = null, width, align = AlignmentType.LEFT, size } = {}) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: shade ? { type: ShadingType.CLEAR, fill: shade } : undefined,
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 80, bottom: 80, left: 100, right: 100 },
    children: [new Paragraph({
      alignment: align,
      children: [new TextRun({ text, bold, size: size || 20 })],
    })],
  });
}
function calloutBox(lines, { shade = PINK_BG, borderColor = "C55A11" } = {}) {
  const border = { style: BorderStyle.SINGLE, size: 8, color: borderColor };
  return new Table({
    width: { size: 9350, type: WidthType.DXA },
    columnWidths: [9350],
    borders: { top: border, bottom: border, left: border, right: border, insideHorizontal: border, insideVertical: border },
    rows: [
      new TableRow({
        children: [
          new TableCell({
            width: { size: 9350, type: WidthType.DXA },
            shading: { type: ShadingType.CLEAR, fill: shade },
            margins: { top: 160, bottom: 160, left: 200, right: 200 },
            children: lines.map((l, i) => new Paragraph({
              spacing: { after: i === lines.length - 1 ? 0 : 100 },
              children: parseInlineBold(l),
            })),
          }),
        ],
      }),
    ],
  });
}
function imagePar(path, widthPx, heightPx, maxWidthDxa = 9350) {
  const scale = Math.min(1, maxWidthDxa / widthPx);
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 150, after: 150 },
    children: [new ImageRun({
      type: "png",
      data: fs.readFileSync(path),
      transformation: { width: Math.round(widthPx * scale * 0.15), height: Math.round(heightPx * scale * 0.15) },
    })],
  });
}
function figCaption(text) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 200 },
    children: [new TextRun({ text, italics: true, size: 18 })],
  });
}

// ---- version control table --------------------------------------------
function versionTable() {
  const rows = [
    ["Guideline title", "Fortification of human milk in preterm infants"],
    ["Version", "1.0 (draft for local review and sign-off)"],
    ["Author(s)", "[Insert name / role]"],
    ["Date drafted", "2026-09"],
    ["Approved by", "[Insert — Neonatal Guidelines Group / Consultant lead]"],
    ["Approval date", "[Insert]"],
    ["Review date", "[Insert — recommend 3 years, or sooner if a trial named in Section 9 reports]"],
    ["Evidence base", "bmf-preterm-fortification evidence review: 49 PMID-verified studies across 8 domains, GRADE-labelled"],
    ["Supersedes", "[Insert previous version/guideline if applicable]"],
  ];
  return new Table({
    width: { size: 9350, type: WidthType.DXA },
    columnWidths: [2600, 6750],
    borders: allBorders(),
    rows: rows.map(([k, v]) => new TableRow({
      children: [
        cell(k, { bold: true, shade: GREY_BG, width: 2600 }),
        cell(v, { width: 6750 }),
      ],
    })),
  });
}
function allBorders() {
  const b = { style: BorderStyle.SINGLE, size: 4, color: "999999" };
  return { top: b, bottom: b, left: b, right: b, insideHorizontal: b, insideVertical: b };
}

// ---- evidence summary table -------------------------------------------
function evidenceTable() {
  const header = ["Clinical scenario", "Pathway", "What the evidence supports", "Certainty"];
  const widths = [1900, 900, 4800, 1750];
  const data = [
    ["Routine VLBW infant", "D", "Fortify at ~100 mL/kg/day; modest growth benefit; no shown neurodevelopmental benefit", "Low–Moderate (growth); Moderate (ND null)"],
    ["Antenatal AEDF/REDF", "A", "No fortification-specific trial; extrapolated caution", "GPP — not evaluable"],
    ["Post-medical NEC", "C", "Feed restart ~3 days post portal-gas clearance; fortifier timing unaddressed", "Very low (restart); GPP (fortifier)"],
    ["Post-surgical NEC/SIP", "B", "No trial or guideline addresses fortifier timing", "GPP — evidence absent"],
    ["Extremely preterm <28 weeks", "D (individualised)", "Early human-milk-based fortification feasible; fortifier-source benefit unresolved (N-forte null vs 3 meta-analyses)", "Low–Moderate, inconsistent"],
    ["SGA/IUGR without AEDF", "D (extrapolated)", "No dedicated trial; extrapolated from general-VLBW evidence", "Not separately evaluable"],
  ];
  const rows = [
    new TableRow({
      tableHeader: true,
      children: header.map((t, i) => cell(t, { bold: true, shade: NAVY_TEXT_SHADE, width: widths[i] })),
    }),
    ...data.map(r => new TableRow({ children: r.map((t, i) => cell(t, { width: widths[i], shade: i === 3 ? "FFF2CC" : null })) })),
  ];
  return new Table({ width: { size: 9350, type: WidthType.DXA }, columnWidths: widths, borders: allBorders(), rows });
}
const NAVY_TEXT_SHADE = "D9E2F3";

// ---- document -----------------------------------------------------------
const children = [];

children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 60 },
  children: [new TextRun({ text: "UNIT CLINICAL GUIDELINE", bold: true, color: NAVY, size: 22 })],
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 300 },
  children: [new TextRun({ text: "Fortification of Human Milk in Preterm Infants", bold: true, size: 40, color: NAVY })],
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 400 },
  children: [new TextRun({ text: "[Insert Trust / Unit name] — Neonatal Intensive Care Unit", italics: true, size: 24 })],
}));
children.push(versionTable());
children.push(new Paragraph({ spacing: { before: 300 }, children: [new PageBreak()] }));

children.push(h1("How to use this document"));
children.push(p("Every recommendation below carries a certainty label taken directly from the underlying evidence review — High / Moderate / Low / Very low certainty (GRADE), or GPP (Good Practice Point) where no direct trial evidence exists in that exact clinical scenario and the statement instead reflects extrapolation from adjacent evidence and clinical consensus. This distinction is deliberately visible throughout: several of the areas where practice is most established (fortification in Doppler-abnormal growth restriction; fortifier reintroduction after surgical NEC/SIP) are GPP, not evidence-based, and this guideline says so rather than implying otherwise."));

children.push(h1("1. Scope and purpose"));
children.push(p("This guideline covers the timing, dose, product selection, tolerance monitoring, and post-discharge management of human milk fortification for preterm infants fed mother's own milk and/or donor human milk. It applies to infants cared for on this neonatal unit from admission until discharge, and includes discharge-planning guidance for continuing or stopping fortification at home."));
children.push(pRuns([
  new TextRun({ text: "Out of scope: ", bold: true }),
  new TextRun({ text: "parenteral nutrition; nutrient-enriched formula for formula-fed infants (a different intervention — see Section 2); general trophic/minimal-enteral-feeding protocols not specific to fortification; term infant feeding." }),
]));

children.push(h1("2. Definitions"));
children.push(bullet("HMF (human/breast milk fortifier): the generic term used throughout this guideline for any product added to human milk to increase its nutrient density."));
children.push(bullet("BMF / BMBF (bovine milk-based fortifier): reserved specifically for fortifier derived from cow's milk, used only when distinguishing it from human-milk-derived product (HMBF). Do not use \"BMF\" to mean human milk fortifier generically."));
children.push(bullet("HMBF (human milk-based fortifier): fortifier derived from pooled donor human milk rather than bovine milk."));
children.push(bullet("AEDF/REDF: antenatal absent or reversed end-diastolic flow on umbilical artery Doppler — a marker of placental insufficiency, distinct from birthweight-centile-defined IUGR/SGA."));
children.push(bullet("GPP (Good Practice Point): a recommendation based on clinical consensus and extrapolation from adjacent evidence, used explicitly wherever no direct trial evidence exists for the exact scenario in question."));

children.push(h1("3. Summary algorithm"));
children.push(p("All infants should be triaged through the algorithm in Figure 1 before starting or restarting fortification: first for antenatal Doppler abnormality/growth restriction (Pathway A), then for a current or recent NEC/SIP episode (Pathways B and C for surgical and medical NEC respectively). Infants meeting neither criterion follow the routine pathway (Pathway D → Box 1)."));
children.push(imagePar("figures/algorithm.png", 4091, 3525, 9000));
children.push(figCaption("Figure 1. Triage algorithm for human milk fortification in preterm infants."));

children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(h1("4. Box 1 — Routine fortification checklist (Pathway D)"));
children.push(p("For infants with no antenatal AEDF/REDF or growth-restriction history and no current/recent NEC or SIP:"));
children.push(calloutBox([
  "1. **Timing.** Commence HMF once enteral feeds reach the unit's standard threshold (commonly ~100 mL/kg/day). Starting earlier (20–40 mL/kg/day) has not shown a consistent growth or tolerance advantage, and one meta-analysis found early fortification associated with a **longer hospital stay** with no growth benefit. [Low–Very low certainty; do not adopt very-early fortification as routine policy.]",
  "2. **Introduction.** Introduce fortifier gradually rather than at full strength immediately. Rapid/early/full-strength introduction is linked to higher feeding-intolerance risk in observational data. [Very low certainty; low-cost, low-risk to implement.]",
  "3. **Product — source.** Standard bovine-derived HMF remains the default. Whether human-milk-derived fortifier (HMBF) reduces NEC or mortality vs bovine fortifier is **unresolved** — three meta-analyses suggest benefit, but the largest single RCT (N-forte) found no difference. Do not present HMBF to families as an established NEC-prevention strategy. [Low–Moderate certainty, internally inconsistent.]",
  "4. **Product — chemistry.** Where available, prefer a non-acidified liquid fortifier over an acidified one: one adequately sized RCT found substantially more metabolic acidosis (27% vs 5%) with the acidified product. [Moderate certainty.]",
  "5. **Individualised/targeted fortification.** Do not improvise a modular fortification protocol locally. Pooled evidence shows a real growth benefit, but one RCT of a modular approach was **stopped early after serious feeding intolerance in 5 of 39 infants**. Await completed trial evidence before adopting routinely.",
  "6. **Tolerance monitoring.** Monitor and document stool pattern, gastric residual volume, and abdominal distension explicitly as fortification is introduced and advanced. [Low certainty.]",
  "7. **Osmolality.** Keep total feed osmolality — including added medications — near the consensus ~450 mOsm/kg ceiling. This is an expert-consensus safety ceiling, not one validated against hard clinical outcomes in any RCT.",
  "8. **Neurodevelopmental counselling.** Do not imply a neurodevelopmental benefit from fortification when counselling families. No trial of any fortification variable has yet shown one. [Moderate certainty for this null.]",
  "9. **Discharge planning.** Growth and 6-year IQ outcomes do not differ between infants discharged on fortified vs unfortified mother's milk. If continuing home fortification, frame the discussion around supporting continued breastfeeding rather than an expected growth/developmental benefit. [Low–Moderate certainty, consistently null.]",
], { shade: GREEN_BG, borderColor: "375623" }));

children.push(h1("5. Pathway A — Antenatal AEDF/REDF or Doppler-abnormal fetal growth restriction"));
children.push(p("No fortification-specific trial has ever been conducted in this subgroup. Current practice of delaying fortification until full established feeds and clinical stability is an extrapolation from a feed-initiation trial (ADEPT) and from small, decades-old epidemiological studies establishing the AEDF–NEC association — neither tested fortification. A subgroup analysis of the same feed-initiation trial found infants below 29 weeks tolerated an identical feeding protocol far worse than infants ≥29 weeks (39% vs 10% NEC), warning against applying one timing rule uniformly across this population even for feed initiation, let alone fortification."));
children.push(calloutBox([
  "**Recommendation:** manage feed initiation per existing unit protocol for growth-restricted/Doppler-abnormal infants; introduce fortification only once feeds are fully established and the infant is clinically stable, individualised by gestational age and clinical trajectory.",
  "[GPP — no direct evidence; state this explicitly to trainees and, where relevant, to families.]",
]));

children.push(h1("6. Pathways B and C — Necrotising enterocolitis and spontaneous intestinal perforation"));
children.push(pRuns([new TextRun({ text: "Pathway C (medical NEC): ", bold: true }), new TextRun({ text: "enteral feeds may reasonably be restarted once portal-venous gas has been absent on ultrasound for approximately three consecutive days, per the one cohort study addressing this directly — though that study's own authors state it was underpowered to exclude an increased recurrence risk. [Very low certainty.] Fortifier-specific reintroduction timing after feeds restart is not addressed in any identified trial — apply clinical judgement, individualised to the infant's tolerance of unfortified feeds first. [GPP.]" })]));
children.push(pRuns([new TextRun({ text: "Pathway B (surgical NEC/SIP): ", bold: true }), new TextRun({ text: "restart feeds per unit surgical/GI protocol. No trial, and no current international guideline (the 2024 European ERNICA surgical NEC guideline and the 2026 Italian SIN/SICP/SINUPE joint position paper were both checked specifically and both are silent on fortifier-specific timing) addresses when to reintroduce fortifier after surgical NEC or SIP. Whatever this unit's local practice is here, it should be understood and documented as clinical judgement, not as an evidence-based or guideline-based protocol. [GPP — evidence absent, not merely extrapolated.]" })]));

children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(h1("7. Evidence certainty at a glance"));
children.push(p("This quick-reference grid (Figure 2) shows GRADE certainty — not direction of effect — for short-term growth, NEC/mortality, and neurodevelopment, across six clinical scenarios. Several \"well-evidenced\" cells reflect confidently null findings, not confirmed benefits. The visual pattern is deliberate: routine and extremely-preterm populations have at least some graded evidence; the three high-risk/post-NEC scenarios are almost entirely grey — \"not evaluable\" — because no direct trial exists."));
children.push(imagePar("figures/certainty_heatmap.png", 3145, 1099, 9000));
children.push(figCaption("Figure 2. GRADE certainty by clinical scenario and outcome domain."));

children.push(h1("8. Monitoring, escalation and audit"));
children.push(bullet("Any infant developing signs of feeding intolerance, abdominal distension, or suspected NEC/SIP during fortification should have fortification held and escalated per the unit's existing NEC/sepsis escalation pathway — this guideline does not change that pathway."));
children.push(bullet("Suggested local audit measures: proportion of eligible VLBW infants fortified by 100 mL/kg/day feeds; documented fortifier-hold events and their resolution; growth (weight/length/HC z-score change) at discharge; proportion of infants discharged on continued human-milk feeding, fortified or not."));
children.push(bullet("Any local deviation from Pathway A or Pathway B/C recommendations (both GPP) should be documented with rationale, given the absence of direct trial evidence to fall back on."));

children.push(h1("9. What could change this guideline"));
children.push(p("Named trials worth tracking for the next review:"));
children.push(numbered("An adequately powered RCT of fortification timing specifically in AEDF/REDF or Doppler-abnormal growth-restricted infants (none currently registered, so far as this review identified — the largest single gap in the evidence base).", "gaps"));
children.push(numbered("The N-forte trial's planned 2- and 5.5-year neurodevelopmental follow-up (human-milk-based vs bovine-based fortifier, extremely preterm infants) — not yet published as of this guideline's evidence base (2026-09).", "gaps"));
children.push(numbered("The MaxiMoM InForM trial (standard vs target vs BUN-adjustable fortification, n=615 planned, Bayley-IV cognitive score at 18-24 months as primary outcome) — the first adequately powered trial with a hard long-term endpoint for individualised fortification.", "gaps"));
children.push(numbered("Independent replication of the acidified-vs-non-acidified metabolic-acidosis signal (Section 4, point 4), currently resting on one trial.", "gaps"));

children.push(h1("10. Roles and responsibilities"));
children.push(bullet("Bedside nursing and medical staff: follow the algorithm (Figure 1) and Box 1 checklist for all eligible infants; document tolerance monitoring; escalate per Section 8."));
children.push(bullet("Consultant/nutrition lead: approve any deviation from Pathway A/B/C GPP recommendations; review audit data annually."));
children.push(bullet("Pharmacy: support osmolality-aware medication administration practice per Section 4, point 7."));
children.push(bullet("Guideline author/owner: review this document against Section 9's named trials, or at the stated review date, whichever is sooner."));

children.push(h1("11. References"));
children.push(p("Full reference list (50 PMID-verified sources) is maintained in the source evidence review at 02-extraction/extraction.csv and the phase-4 manuscript's bibliography (04-manuscript/manuscript.md). Key sources underlying each numbered recommendation above are cited by PMID in the corresponding domain synthesis file (03-synthesis/domain-1..8-*.md) and the cross-cutting synthesis (03-synthesis/cross-cutting-synthesis.md)."));

children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(h1("Appendix — Evidence summary table"));
children.push(evidenceTable());

const doc = new Document({
  styles: {
    default: {
      document: { run: { font: "Calibri", size: 21 } },
    },
  },
  sections: [
    {
      properties: {
        page: { size: { width: 11906, height: 16838 } }, // A4
        margin: { top: 1000, bottom: 1000, left: 1300, right: 1300 },
      },
      headers: {
        default: new Header({
          children: [new Paragraph({
            alignment: AlignmentType.RIGHT,
            children: [new TextRun({ text: "Fortification of Human Milk in Preterm Infants — Unit Guideline v1.0", size: 16, italics: true, color: "808080" })],
          })],
        }),
      },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({ text: "Page ", size: 16, color: "808080" }),
              new TextRun({ children: [PageNumber.CURRENT], size: 16, color: "808080" }),
              new TextRun({ text: " of ", size: 16, color: "808080" }),
              new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 16, color: "808080" }),
            ],
          })],
        }),
      },
      children,
    },
  ],
  numbering: {
    config: [
      {
        reference: "gaps",
        levels: [{ level: 0, format: "decimal", text: "%1.", alignment: AlignmentType.START, style: { paragraph: { indent: { left: 420, hanging: 360 } } } }],
      },
    ],
  },
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync("unit-guideline.docx", buf);
  console.log("Wrote unit-guideline.docx");
});
