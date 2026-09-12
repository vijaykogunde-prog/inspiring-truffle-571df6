#!/usr/bin/env python3
"""Build the unit guideline PDF directly with reportlab (soffice/LibreOffice
in this environment cannot convert docx->pdf: the LO install here is missing
its core Writer/Calc filter libraries, confirmed by inspection of
/usr/lib/libreoffice/program, so this generates the PDF independently rather
than via the .docx)."""
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    Image as RLImage, ListFlowable, ListItem, KeepTogether, HRFlowable,
)
from reportlab.pdfgen import canvas as canvas_mod
from PIL import Image as PILImage

NAVY = colors.HexColor("#1F3864")
PINK_BG = colors.HexColor("#FBE4D5")
PINK_BORDER = colors.HexColor("#C55A11")
GREEN_BG = colors.HexColor("#E2EFDA")
GREEN_BORDER = colors.HexColor("#375623")
GREY_BG = colors.HexColor("#F2F2F2")
HEADER_SHADE = colors.HexColor("#D9E2F3")
CERT_SHADE = colors.HexColor("#FFF2CC")

styles = getSampleStyleSheet()

def esc(t):
    """Convert **bold** markers to reportlab <b> tags and escape raw & < >."""
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return t

styleTitle = ParagraphStyle("TitleMain", parent=styles["Title"], fontSize=22, textColor=NAVY, spaceAfter=6, alignment=TA_CENTER)
styleKicker = ParagraphStyle("Kicker", parent=styles["Normal"], fontSize=12, textColor=NAVY, alignment=TA_CENTER, spaceAfter=4)
styleSub = ParagraphStyle("Sub", parent=styles["Normal"], fontSize=11, textColor=colors.black, alignment=TA_CENTER, italic=True, spaceAfter=16)
styleH1 = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=14, textColor=NAVY, spaceBefore=16, spaceAfter=8)
styleH2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=12, textColor=NAVY, spaceBefore=12, spaceAfter=6)
styleBody = ParagraphStyle("Body", parent=styles["Normal"], fontSize=10, leading=14, spaceAfter=8)
styleBullet = ParagraphStyle("Bullet", parent=styleBody, leftIndent=14, bulletIndent=0, spaceAfter=6)
styleCallout = ParagraphStyle("Callout", parent=styleBody, fontSize=9.5, leading=13, spaceAfter=6)
styleCaption = ParagraphStyle("Caption", parent=styles["Normal"], fontSize=9, italic=True, alignment=TA_CENTER, textColor=colors.HexColor("#555555"), spaceAfter=14)
styleTableCell = ParagraphStyle("TableCell", parent=styles["Normal"], fontSize=9, leading=12)
styleTableHead = ParagraphStyle("TableHead", parent=styles["Normal"], fontSize=9, leading=12, textColor=NAVY, fontName="Helvetica-Bold")

def P(text, style=styleBody):
    return Paragraph(esc(text), style)

def callout_box(lines, bg=PINK_BG, border=PINK_BORDER):
    inner = [P(l, styleCallout) for l in lines]
    t = Table([[inner]], colWidths=[165 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 1.1, border),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t

def fitted_image(path, max_w_mm=165, max_h_mm=230):
    im = PILImage.open(path)
    w_px, h_px = im.size
    aspect = h_px / w_px
    w = max_w_mm
    h = w * aspect
    if h > max_h_mm:
        h = max_h_mm
        w = h / aspect
    return RLImage(path, width=w * mm, height=h * mm)

def kv_table(rows):
    data = [[P(k, ParagraphStyle("k", parent=styleTableCell, fontName="Helvetica-Bold")), P(v, styleTableCell)] for k, v in rows]
    t = Table(data, colWidths=[45 * mm, 120 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), GREY_BG),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#999999")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t

def evidence_table():
    header = ["Clinical scenario", "Pathway", "What the evidence supports", "Certainty"]
    rows = [
        ["Routine VLBW infant", "D", "Fortify at ~100 mL/kg/day; modest growth benefit; no shown neurodevelopmental benefit", "Low–Moderate (growth); Moderate (ND null)"],
        ["Antenatal AEDF/REDF", "A", "No fortification-specific trial; extrapolated caution", "GPP — not evaluable"],
        ["Post-medical NEC", "C", "Feed restart ~3 days post portal-gas clearance; fortifier timing unaddressed", "Very low (restart); GPP (fortifier)"],
        ["Post-surgical NEC/SIP", "B", "No trial or guideline addresses fortifier timing", "GPP — evidence absent"],
        ["Extremely preterm <28 weeks", "D (individ.)", "Early human-milk-based fortification feasible; fortifier-source benefit unresolved (N-forte null vs 3 meta-analyses)", "Low–Moderate, inconsistent"],
        ["SGA/IUGR without AEDF", "D (extrap.)", "No dedicated trial; extrapolated from general-VLBW evidence", "Not separately evaluable"],
    ]
    data = [[P(h, styleTableHead) for h in header]]
    for r in rows:
        data.append([P(r[0], styleTableCell), P(r[1], styleTableCell), P(r[2], styleTableCell), P(r[3], styleTableCell)])
    t = Table(data, colWidths=[38 * mm, 20 * mm, 78 * mm, 29 * mm], repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), HEADER_SHADE),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#999999")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    for i in range(1, len(data)):
        style.append(("BACKGROUND", (3, i), (3, i), CERT_SHADE))
    t.setStyle(TableStyle(style))
    return t

def bullets(items):
    return ListFlowable([ListItem(P(i, styleBullet), leftIndent=12) for i in items], bulletType="bullet", start="•")

def numbered(items):
    return ListFlowable([ListItem(P(i, styleBullet), leftIndent=12) for i in items], bulletType="1")

# ---- header/footer ------------------------------------------------------
def header_footer(canvas: canvas_mod.Canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica-Oblique", 8)
    canvas.setFillColor(colors.HexColor("#808080"))
    canvas.drawRightString(A4[0] - 20 * mm, A4[1] - 12 * mm, "Fortification of Human Milk in Preterm Infants — Unit Guideline v1.0")
    canvas.drawCentredString(A4[0] / 2, 12 * mm, f"Page {doc.page}")
    canvas.restoreState()

# ---- build story ----------------------------------------------------------
story = []

story.append(Spacer(1, 20 * mm))
story.append(Paragraph("UNIT CLINICAL GUIDELINE", styleKicker))
story.append(Paragraph("Fortification of Human Milk<br/>in Preterm Infants", styleTitle))
story.append(Paragraph("[Insert Trust / Unit name] — Neonatal Intensive Care Unit", styleSub))
story.append(Spacer(1, 8 * mm))
story.append(kv_table([
    ("Guideline title", "Fortification of human milk in preterm infants"),
    ("Version", "1.0 (draft for local review and sign-off)"),
    ("Author(s)", "[Insert name / role]"),
    ("Date drafted", "2026-09"),
    ("Approved by", "[Insert — Neonatal Guidelines Group / Consultant lead]"),
    ("Approval date", "[Insert]"),
    ("Review date", "[Insert — recommend 3 years, or sooner if a trial named in Section 9 reports]"),
    ("Evidence base", "bmf-preterm-fortification evidence review: 49 PMID-verified studies across 8 domains, GRADE-labelled"),
    ("Supersedes", "[Insert previous version/guideline if applicable]"),
]))
story.append(PageBreak())

story.append(Paragraph("How to use this document", styleH1))
story.append(P("Every recommendation below carries a certainty label taken directly from the underlying evidence review — High / Moderate / Low / Very low certainty (GRADE), or GPP (Good Practice Point) where no direct trial evidence exists in that exact clinical scenario and the statement instead reflects extrapolation from adjacent evidence and clinical consensus. This distinction is deliberately visible throughout: several of the areas where practice is most established (fortification in Doppler-abnormal growth restriction; fortifier reintroduction after surgical NEC/SIP) are GPP, not evidence-based, and this guideline says so rather than implying otherwise."))

story.append(Paragraph("1. Scope and purpose", styleH1))
story.append(P("This guideline covers the timing, dose, product selection, tolerance monitoring, and post-discharge management of human milk fortification for preterm infants fed mother's own milk and/or donor human milk. It applies to infants cared for on this neonatal unit from admission until discharge, and includes discharge-planning guidance for continuing or stopping fortification at home."))
story.append(P("**Out of scope:** parenteral nutrition; nutrient-enriched formula for formula-fed infants (a different intervention — see Section 2); general trophic/minimal-enteral-feeding protocols not specific to fortification; term infant feeding."))

story.append(Paragraph("2. Definitions", styleH1))
story.append(bullets([
    "**HMF (human/breast milk fortifier):** the generic term used throughout this guideline for any product added to human milk to increase its nutrient density.",
    "**BMF / BMBF (bovine milk-based fortifier):** reserved specifically for fortifier derived from cow's milk, used only when distinguishing it from human-milk-derived product (HMBF). Do not use “BMF” to mean human milk fortifier generically.",
    "**HMBF (human milk-based fortifier):** fortifier derived from pooled donor human milk rather than bovine milk.",
    "**AEDF/REDF:** antenatal absent or reversed end-diastolic flow on umbilical artery Doppler — a marker of placental insufficiency, distinct from birthweight-centile-defined IUGR/SGA.",
    "**GPP (Good Practice Point):** a recommendation based on clinical consensus and extrapolation from adjacent evidence, used explicitly wherever no direct trial evidence exists for the exact scenario in question.",
]))

story.append(Paragraph("3. Summary algorithm", styleH1))
story.append(P("All infants should be triaged through the algorithm in Figure 1 before starting or restarting fortification: first for antenatal Doppler abnormality/growth restriction (Pathway A), then for a current or recent NEC/SIP episode (Pathways B and C for surgical and medical NEC respectively). Infants meeting neither criterion follow the routine pathway (Pathway D → Box 1)."))
story.append(fitted_image("figures/algorithm.png", max_w_mm=155, max_h_mm=225))
story.append(Paragraph("Figure 1. Triage algorithm for human milk fortification in preterm infants.", styleCaption))
story.append(PageBreak())

story.append(Paragraph("4. Box 1 — Routine fortification checklist (Pathway D)", styleH1))
story.append(P("For infants with no antenatal AEDF/REDF or growth-restriction history and no current/recent NEC or SIP:"))
story.append(callout_box([
    "1. **Timing.** Commence HMF once enteral feeds reach the unit's standard threshold (commonly ~100 mL/kg/day). Starting earlier (20–40 mL/kg/day) has not shown a consistent growth or tolerance advantage, and one meta-analysis found early fortification associated with a **longer hospital stay** with no growth benefit. [Low–Very low certainty; do not adopt very-early fortification as routine policy.]",
    "2. **Introduction.** Introduce fortifier gradually rather than at full strength immediately. Rapid/early/full-strength introduction is linked to higher feeding-intolerance risk in observational data. [Very low certainty; low-cost, low-risk to implement.]",
    "3. **Product — source.** Standard bovine-derived HMF remains the default. Whether human-milk-derived fortifier (HMBF) reduces NEC or mortality vs bovine fortifier is **unresolved** — three meta-analyses suggest benefit, but the largest single RCT (N-forte) found no difference. Do not present HMBF to families as an established NEC-prevention strategy. [Low–Moderate certainty, internally inconsistent.]",
    "4. **Product — chemistry.** Where available, prefer a non-acidified liquid fortifier over an acidified one: one adequately sized RCT found substantially more metabolic acidosis (27% vs 5%) with the acidified product. [Moderate certainty.]",
    "5. **Individualised/targeted fortification.** Do not improvise a modular fortification protocol locally. Pooled evidence shows a real growth benefit, but one RCT of a modular approach was **stopped early after serious feeding intolerance in 5 of 39 infants**. Await completed trial evidence before adopting routinely.",
    "6. **Tolerance monitoring.** Monitor and document stool pattern, gastric residual volume, and abdominal distension explicitly as fortification is introduced and advanced. [Low certainty.]",
    "7. **Osmolality.** Keep total feed osmolality — including added medications — near the consensus ~450 mOsm/kg ceiling. This is an expert-consensus safety ceiling, not one validated against hard clinical outcomes in any RCT.",
    "8. **Neurodevelopmental counselling.** Do not imply a neurodevelopmental benefit from fortification when counselling families. No trial of any fortification variable has yet shown one. [Moderate certainty for this null.]",
    "9. **Discharge planning.** Growth and 6-year IQ outcomes do not differ between infants discharged on fortified vs unfortified mother's milk. If continuing home fortification, frame the discussion around supporting continued breastfeeding rather than an expected growth/developmental benefit. [Low–Moderate certainty, consistently null.]",
], bg=GREEN_BG, border=GREEN_BORDER))

story.append(Paragraph("5. Pathway A — Antenatal AEDF/REDF or Doppler-abnormal fetal growth restriction", styleH1))
story.append(P("No fortification-specific trial has ever been conducted in this subgroup. Current practice of delaying fortification until full established feeds and clinical stability is an extrapolation from a feed-initiation trial (ADEPT) and from small, decades-old epidemiological studies establishing the AEDF–NEC association — neither tested fortification. A subgroup analysis of the same feed-initiation trial found infants below 29 weeks tolerated an identical feeding protocol far worse than infants ≥29 weeks (39% vs 10% NEC), warning against applying one timing rule uniformly across this population even for feed initiation, let alone fortification."))
story.append(callout_box([
    "**Recommendation:** manage feed initiation per existing unit protocol for growth-restricted/Doppler-abnormal infants; introduce fortification only once feeds are fully established and the infant is clinically stable, individualised by gestational age and clinical trajectory.",
    "[GPP — no direct evidence; state this explicitly to trainees and, where relevant, to families.]",
]))

story.append(Paragraph("6. Pathways B and C — Necrotising enterocolitis and spontaneous intestinal perforation", styleH1))
story.append(P("**Pathway C (medical NEC):** enteral feeds may reasonably be restarted once portal-venous gas has been absent on ultrasound for approximately three consecutive days, per the one cohort study addressing this directly — though that study's own authors state it was underpowered to exclude an increased recurrence risk. [Very low certainty.] Fortifier-specific reintroduction timing after feeds restart is not addressed in any identified trial — apply clinical judgement, individualised to the infant's tolerance of unfortified feeds first. [GPP.]"))
story.append(P("**Pathway B (surgical NEC/SIP):** restart feeds per unit surgical/GI protocol. No trial, and no current international guideline (the 2024 European ERNICA surgical NEC guideline and the 2026 Italian SIN/SICP/SINUPE joint position paper were both checked specifically and both are silent on fortifier-specific timing) addresses when to reintroduce fortifier after surgical NEC or SIP. Whatever this unit's local practice is here, it should be understood and documented as clinical judgement, not as an evidence-based or guideline-based protocol. [GPP — evidence absent, not merely extrapolated.]"))
story.append(PageBreak())

story.append(Paragraph("7. Evidence certainty at a glance", styleH1))
story.append(P("This quick-reference grid (Figure 2) shows GRADE certainty — not direction of effect — for short-term growth, NEC/mortality, and neurodevelopment, across six clinical scenarios. Several “well-evidenced” cells reflect confidently null findings, not confirmed benefits. The visual pattern is deliberate: routine and extremely-preterm populations have at least some graded evidence; the three high-risk/post-NEC scenarios are almost entirely grey — “not evaluable” — because no direct trial exists."))
story.append(fitted_image("figures/certainty_heatmap.png", max_w_mm=165, max_h_mm=110))
story.append(Paragraph("Figure 2. GRADE certainty by clinical scenario and outcome domain.", styleCaption))

story.append(Paragraph("8. Monitoring, escalation and audit", styleH1))
story.append(bullets([
    "Any infant developing signs of feeding intolerance, abdominal distension, or suspected NEC/SIP during fortification should have fortification held and escalated per the unit's existing NEC/sepsis escalation pathway — this guideline does not change that pathway.",
    "Suggested local audit measures: proportion of eligible VLBW infants fortified by 100 mL/kg/day feeds; documented fortifier-hold events and their resolution; growth (weight/length/HC z-score change) at discharge; proportion of infants discharged on continued human-milk feeding, fortified or not.",
    "Any local deviation from Pathway A or Pathway B/C recommendations (both GPP) should be documented with rationale, given the absence of direct trial evidence to fall back on.",
]))

story.append(Paragraph("9. What could change this guideline", styleH1))
story.append(P("Named trials worth tracking for the next review:"))
story.append(numbered([
    "An adequately powered RCT of fortification timing specifically in AEDF/REDF or Doppler-abnormal growth-restricted infants (none currently registered, so far as this review identified — the largest single gap in the evidence base).",
    "The N-forte trial's planned 2- and 5.5-year neurodevelopmental follow-up (human-milk-based vs bovine-based fortifier, extremely preterm infants) — not yet published as of this guideline's evidence base (2026-09).",
    "The MaxiMoM InForM trial (standard vs target vs BUN-adjustable fortification, n=615 planned, Bayley-IV cognitive score at 18–24 months as primary outcome) — the first adequately powered trial with a hard long-term endpoint for individualised fortification.",
    "Independent replication of the acidified-vs-non-acidified metabolic-acidosis signal (Section 4, point 4), currently resting on one trial.",
]))

story.append(Paragraph("10. Roles and responsibilities", styleH1))
story.append(bullets([
    "Bedside nursing and medical staff: follow the algorithm (Figure 1) and Box 1 checklist for all eligible infants; document tolerance monitoring; escalate per Section 8.",
    "Consultant/nutrition lead: approve any deviation from Pathway A/B/C GPP recommendations; review audit data annually.",
    "Pharmacy: support osmolality-aware medication administration practice per Section 4, point 7.",
    "Guideline author/owner: review this document against Section 9's named trials, or at the stated review date, whichever is sooner.",
]))

story.append(Paragraph("11. References", styleH1))
story.append(P("Full reference list (50 PMID-verified sources) is maintained in the source evidence review at 02-extraction/extraction.csv and the phase-4 manuscript's bibliography (04-manuscript/manuscript.md). Key sources underlying each numbered recommendation above are cited by PMID in the corresponding domain synthesis file (03-synthesis/domain-1..8-*.md) and the cross-cutting synthesis (03-synthesis/cross-cutting-synthesis.md)."))

story.append(PageBreak())
story.append(Paragraph("Appendix — Evidence summary table", styleH1))
story.append(evidence_table())

doc = SimpleDocTemplate(
    "unit-guideline.pdf", pagesize=A4,
    topMargin=18 * mm, bottomMargin=18 * mm, leftMargin=20 * mm, rightMargin=20 * mm,
    title="Fortification of Human Milk in Preterm Infants — Unit Guideline",
    author="Evidence-review-pipeline (bmf-preterm-fortification project)",
)
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("Wrote unit-guideline.pdf")
