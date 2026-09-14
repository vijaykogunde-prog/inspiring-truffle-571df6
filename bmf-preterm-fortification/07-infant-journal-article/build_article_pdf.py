#!/usr/bin/env python3
"""Build the Infant-journal-style article PDF from article_numbered.md,
inserting Table 1 after the growth section, Figure 1 after the special-
populations section, Table 2 + Figure 3 in the parent-communication section,
and Figure 2 near 'Evidence certainty'. Built directly with reportlab (see
06-guideline/build_guideline_pdf.py note: this environment's LibreOffice
install cannot convert docx->pdf, confirmed by inspection)."""
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    Image as RLImage, KeepTogether,
)
from reportlab.pdfgen import canvas as canvas_mod
from PIL import Image as PILImage

NAVY = colors.HexColor("#1F3864")
GREEN_BG = colors.HexColor("#E2EFDA")
GREEN_BORDER = colors.HexColor("#375623")
BLUE_BG = colors.HexColor("#DCE6F1")
BLUE_BORDER = colors.HexColor("#1F3864")
HEADER_SHADE = colors.HexColor("#D9E2F3")
GREY_ROW = colors.HexColor("#F7F7F7")

styles = getSampleStyleSheet()

def esc(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)
    t = re.sub(r"\[([\d,]+)\]", lambda m: f'<super><font size=7 color="#1F3864">[{m.group(1)}]</font></super>', t)
    return t

styleTitle = ParagraphStyle("TitleMain", parent=styles["Title"], fontSize=18, textColor=NAVY, spaceAfter=8, alignment=TA_CENTER, leading=22)
styleStandfirst = ParagraphStyle("Standfirst", parent=styles["Normal"], fontSize=10.5, leading=15, italic=True, textColor=colors.HexColor("#333333"), spaceAfter=14, alignment=TA_JUSTIFY)
styleH1 = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=13, textColor=NAVY, spaceBefore=14, spaceAfter=7)
styleBody = ParagraphStyle("Body", parent=styles["Normal"], fontSize=9.7, leading=13.6, spaceAfter=8, alignment=TA_JUSTIFY)
styleKeyBullet = ParagraphStyle("KeyBullet", parent=styleBody, leftIndent=12, spaceAfter=5)
styleCaption = ParagraphStyle("Caption", parent=styles["Normal"], fontSize=8.7, italic=True, alignment=TA_CENTER, textColor=colors.HexColor("#555555"), spaceAfter=12)
styleTableCell = ParagraphStyle("TableCell", parent=styles["Normal"], fontSize=8.6, leading=11.5)
styleTableHead = ParagraphStyle("TableHead", parent=styles["Normal"], fontSize=8.6, leading=11.5, textColor=NAVY, fontName="Helvetica-Bold")

def P(text, style=styleBody):
    return Paragraph(esc(text), style)

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

def key_points_box():
    items = [
        "Fortification gives a modest, well-replicated boost to short-term growth, but no trial of any fortification variable has yet shown a clear benefit to long-term neurodevelopment.",
        "The evidence on exactly when to start fortifying does not favour starting earlier; one meta-analysis links early fortification to a longer hospital stay.",
        "For babies with an abnormal antenatal Doppler scan, and for babies restarting feeds after surgical NEC or SIP, there is no fortification-specific trial evidence at all — current practice in these groups is extrapolated, not evidence-based.",
        "Whether human-milk-based fortifier reduces NEC or death compared with cows’-milk-based fortifier is unresolved: several meta-analyses suggest benefit, but the largest single trial found none.",
        "Parents can be told plainly that fortification helps babies grow a little faster in hospital, and that this has not been shown to change how they develop later — a message that is often more reassuring than clinicians expect.",
    ]
    inner = [Paragraph("<b>Key points</b>", ParagraphStyle("kpTitle", parent=styleBody, fontSize=10.5, textColor=NAVY, spaceAfter=6))]
    inner += [P("• " + i, styleKeyBullet) for i in items]
    t = Table([[inner]], colWidths=[165 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BLUE_BG),
        ("BOX", (0, 0), (-1, -1), 1.0, BLUE_BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t

def table1_evidence():
    header = ["Question", "What the evidence shows", "Certainty", "Ref"]
    widths = [34 * mm, 92 * mm, 24 * mm, 15 * mm]
    rows = [
        ["Does fortification help growth?", "Modest, consistent increase in weight/length/head-growth velocity across large reviews", "Low–Moderate", "1,2"],
        ["Does timing (when to start) matter?", "No consistent advantage to starting earlier; one meta-analysis links early start to longer hospital stay", "Low–Very low", "4–6"],
        ["Is it safe in Doppler-abnormal/growth-restricted babies?", "No fortification-specific trial exists; practice is extrapolated from feed-initiation trials", "Not evaluable", "10–11"],
        ["When to restart after NEC/SIP?", "Some evidence for restarting feeds; no evidence at all for fortifier-specific timing", "Very low / absent", "15–18"],
        ["Does fortifier source (cow’s milk vs human milk) matter?", "Smaller meta-analyses suggest benefit for human-milk-based; largest single trial found no difference", "Low–Moderate, inconsistent", "19,22"],
        ["Does it upset babies’ tummies?", "Stool hardening tracks with fortifier dose regardless of product; early/fast/full-strength introduction raises intolerance risk", "Low–Very low", "31,32"],
        ["Does it help the brain long-term?", "No trial of any fortification variable has shown a neurodevelopmental benefit", "Moderate (for the null)", "23,36"],
        ["Does continuing it at home help?", "No growth/IQ benefit shown; may help sustain breastfeeding instead", "Low–Moderate", "39–41"],
    ]
    data = [[P(h, styleTableHead) for h in header]]
    for r in rows:
        data.append([P(r[0], styleTableCell), P(r[1], styleTableCell), P(r[2], styleTableCell), P(r[3], styleTableCell)])
    t = Table(data, colWidths=widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), HEADER_SHADE),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#999999")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    for i in range(1, len(data), 2):
        style.append(("BACKGROUND", (0, i), (-1, i), GREY_ROW))
    t.setStyle(TableStyle(style))
    return t

def table2_parent_talk():
    header = ["Scenario", "A form of words that fits the evidence"]
    widths = [40 * mm, 125 * mm]
    rows = [
        ["Explaining fortification generally", "“Adding a fortifier to your milk gives your baby a bit more protein and energy than breast milk alone provides, which helps growth while in hospital.”"],
        ["Doppler-abnormal / growth-restricted baby", "“We wait until your baby is tolerating full feeds well because babies like yours can have a more sensitive tummy — we don’t yet have research on the best timing here specifically, so we’re being cautious.”"],
        ["After NEC or bowel surgery", "“We have evidence about safely restarting milk feeds. We don’t have specific research on exactly when to add fortifier back in — your team will judge that step-by-step.”"],
        ["Choosing a fortifier product", "“There are different types of fortifier. The evidence doesn’t clearly favour one over another for safety, so we use our unit’s standard product unless there’s a specific reason to change.”"],
        ["Asked about long-term development", "“Fortifying milk helps your baby grow a bit faster now. We don’t have good evidence that it changes how your baby’s brain develops later — growing well now is good, but it isn’t a guarantee about the future.”"],
        ["Discharge planning", "“If we suggest continuing fortifier for a while at home, it’s mainly to help you keep breastfeeding successfully — not because it will speed up growth or development beyond what your milk alone would do.”"],
    ]
    data = [[P(h, styleTableHead) for h in header]]
    for r in rows:
        data.append([P(r[0], styleTableCell), P(r[1], styleTableCell)])
    t = Table(data, colWidths=widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), HEADER_SHADE),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#999999")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    for i in range(1, len(data), 2):
        style.append(("BACKGROUND", (0, i), (-1, i), GREY_ROW))
    t.setStyle(TableStyle(style))
    return t

def header_footer(c: canvas_mod.Canvas, doc):
    c.saveState()
    c.setFont("Helvetica-Oblique", 7.5)
    c.setFillColor(colors.HexColor("#808080"))
    c.drawRightString(A4[0] - 18 * mm, A4[1] - 12 * mm, "Fortifying human milk for preterm babies — for Infant journal")
    c.drawCentredString(A4[0] / 2, 11 * mm, f"Page {doc.page}")
    c.restoreState()

# ---- parse article_numbered.md into sections ----------------------------
raw = open("article_numbered.md", encoding="utf-8").read()
raw = raw.split("---\n*Word count")[0]  # drop trailing word-count note
lines = raw.split("\n")

story2 = []
story2.append(Spacer(1, 4 * mm))
story2.append(Paragraph("Fortifying human milk for preterm babies: what the evidence supports, and what to tell parents", styleTitle))
i = 0
para_buf = []
def flush2():
    global para_buf
    if para_buf:
        text = " ".join(para_buf).strip()
        if text:
            story2.append(P(text))
        para_buf = []

def insert_for(heading):
    """Append the table/figure block that belongs at the END of this heading's section."""
    if heading == "Does fortification actually help growth?":
        story2.append(Spacer(1, 2 * mm))
        story2.append(table1_evidence())
        story2.append(Paragraph("Table 1. What the evidence shows, by clinical question. Reference numbers match the main text; full citations in the separate References document.", styleCaption))
    elif heading == "Babies with growth restriction or an abnormal Doppler scan":
        story2.append(PageBreak())
        story2.append(fitted_image("figures/figure1_algorithm.png", max_w_mm=150, max_h_mm=225))
        story2.append(Paragraph("Figure 1. Triage pathway for fortification decisions, from the companion unit guideline built on the same evidence base.", styleCaption))
    elif heading == "Does fortification upset babies' tummies?":
        story2.append(Spacer(1, 2 * mm))
        story2.append(fitted_image("figures/figure2_certainty_heatmap.png", max_w_mm=160, max_h_mm=100))
        story2.append(Paragraph("Figure 2. GRADE certainty by clinical scenario and outcome domain — colour shows certainty of evidence, not direction of effect.", styleCaption))
    elif heading == "Bringing it together: talking with parents":
        story2.append(Spacer(1, 2 * mm))
        story2.append(table2_parent_talk())
        story2.append(Paragraph("Table 2. Suggested talking points by clinical scenario — adapt to how each family is taking the information.", styleCaption))
        story2.append(Spacer(1, 3 * mm))
        story2.append(fitted_image("figures/figure3_parent_infographic.png", max_w_mm=165, max_h_mm=140))
        story2.append(Paragraph("Figure 3. Plain-language summary for parent conversations.", styleCaption))

INSERT_TRIGGERS = {
    "Does fortification actually help growth?",
    "Babies with growth restriction or an abnormal Doppler scan",
    "Does fortification upset babies' tummies?",
    "Bringing it together: talking with parents",
}

current_heading = None
while i < len(lines):
    line = lines[i].rstrip()
    if line.startswith("# "):
        i += 1; continue
    if line.startswith("**Standfirst:**"):
        flush2()
        story2.append(P(line.replace("**Standfirst:**", "").strip(), styleStandfirst))
        i += 1; continue
    if line == "## Key points":
        flush2()
        story2.append(key_points_box())
        story2.append(Spacer(1, 4 * mm))
        i += 1
        while i < len(lines) and not lines[i].startswith("## "):
            i += 1
        continue
    if line.startswith("## "):
        flush2()
        if current_heading in INSERT_TRIGGERS:
            insert_for(current_heading)
        current_heading = line[3:]
        story2.append(Paragraph(esc(current_heading), styleH1))
        i += 1
        continue
    if line.strip() == "":
        flush2()
        i += 1
        continue
    para_buf.append(line.strip())
    i += 1
flush2()
if current_heading in INSERT_TRIGGERS:
    insert_for(current_heading)

story2.append(Spacer(1, 6 * mm))
story2.append(Paragraph(
    "<i>Word count (main text, excluding key points, tables, figures and references): 2923 words. "
    "The full reference list (43 sources, all PMID-verified live against PubMed, with clickable links) "
    "is provided as a separate document.</i>",
    ParagraphStyle("wc", parent=styles["Normal"], fontSize=8.3, textColor=colors.HexColor("#555555"))
))

doc = SimpleDocTemplate(
    "article.pdf", pagesize=A4,
    topMargin=16 * mm, bottomMargin=16 * mm, leftMargin=18 * mm, rightMargin=18 * mm,
    title="Fortifying human milk for preterm babies", author="Infant journal article draft",
)
doc.build(story2, onFirstPage=header_footer, onLaterPages=header_footer)
print("Wrote article.pdf")
