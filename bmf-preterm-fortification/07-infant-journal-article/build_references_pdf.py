#!/usr/bin/env python3
"""Build a standalone references PDF with real clickable PubMed hyperlinks
(reportlab <link> tags -> proper PDF annotations, not just blue text), parsed
from references.md so numbering can never drift from the article."""
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfgen import canvas as canvas_mod

NAVY = colors.HexColor("#1F3864")
styles = getSampleStyleSheet()

styleTitle = ParagraphStyle("T", parent=styles["Title"], fontSize=15, textColor=NAVY, alignment=TA_CENTER, spaceAfter=6)
styleIntro = ParagraphStyle("I", parent=styles["Normal"], fontSize=9.3, leading=13, spaceAfter=12, textColor=colors.HexColor("#333333"))
styleRef = ParagraphStyle("R", parent=styles["Normal"], fontSize=9.3, leading=13.5, spaceAfter=9)

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

lines = [l for l in open("references.md", encoding="utf-8").read().split("\n") if l.strip()]
entries = [l for l in lines if re.match(r"^\d+\.\s", l)]

story = [
    Spacer(1, 4 * mm),
    Paragraph("References", styleTitle),
    Paragraph(
        "Vancouver-numbered to match the in-text citation numbers in the accompanying article "
        "(<i>Fortifying human milk for preterm babies: what the evidence supports, and what to tell parents</i>). "
        "Every entry was re-verified live against PubMed this session. Click any link, or the underlined PMID, "
        "to open the source directly for independent manual verification.",
        styleIntro,
    ),
]

url_re = re.compile(r"(https://pubmed\.ncbi\.nlm\.nih\.gov/\d+/)")
for entry in entries:
    m = url_re.search(entry)
    if not m:
        story.append(Paragraph(esc(entry), styleRef))
        continue
    url = m.group(1)
    before = entry[: m.start()]
    linked = f'<link href="{url}" color="#1F3864"><u>{esc(url)}</u></link>'
    text = esc(before) + linked
    story.append(Paragraph(text, styleRef))

def footer(c: canvas_mod.Canvas, doc):
    c.saveState()
    c.setFont("Helvetica-Oblique", 7.5)
    c.setFillColor(colors.HexColor("#808080"))
    c.drawCentredString(A4[0] / 2, 11 * mm, f"Page {doc.page}")
    c.restoreState()

doc = SimpleDocTemplate(
    "references.pdf", pagesize=A4,
    topMargin=18 * mm, bottomMargin=16 * mm, leftMargin=20 * mm, rightMargin=20 * mm,
    title="References — Fortifying human milk for preterm babies",
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(f"Wrote references.pdf with {len(entries)} linked entries")
