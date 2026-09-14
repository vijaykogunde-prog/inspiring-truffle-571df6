#!/usr/bin/env python3
"""Figure 3 — plain-language 'what we know / don't know yet' infographic for
parent communication, built with matplotlib using the same style palette as
the clinical-figures skill (navy/blue clinical theme) for visual consistency
with Figures 1 and 2 in this article."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

NAVY = "#1F3864"
GREEN = "#548235"
GREEN_BG = "#E2EFDA"
AMBER = "#BF8F00"
AMBER_BG = "#FFF2CC"
GREY = "#808080"
GREY_BG = "#F2F2F2"
WHITE = "#FFFFFF"

rows = [
    {
        "q": "Does fortifying milk help my baby grow while in hospital?",
        "verdict": "YES — modestly, reliably",
        "detail": "Well-replicated across large trials and reviews",
        "color": GREEN, "bg": GREEN_BG,
    },
    {
        "q": "Does it help my baby's brain develop in the long run?",
        "verdict": "NOT SHOWN",
        "detail": "No trial of any fortification approach has shown this yet",
        "color": "#C00000", "bg": "#FADBD8",
    },
    {
        "q": "Is cow's-milk-based or breast-milk-based fortifier clearly safer?",
        "verdict": "GENUINELY UNCLEAR",
        "detail": "Smaller studies point one way; the largest trial found no difference",
        "color": AMBER, "bg": AMBER_BG,
    },
    {
        "q": "Is it safe to fortify after an abnormal blood-flow scan in pregnancy?",
        "verdict": "NO RESEARCH YET",
        "detail": "Care here is based on caution and experience, not a trial",
        "color": GREY, "bg": GREY_BG,
    },
    {
        "q": "Is it safe to restart fortifier after bowel surgery (NEC)?",
        "verdict": "NO RESEARCH YET",
        "detail": "Decided case-by-case; no guideline covers this specific step",
        "color": GREY, "bg": GREY_BG,
    },
    {
        "q": "Will continuing fortifier at home help growth or development?",
        "verdict": "NOT SHOWN",
        "detail": "May help keep breastfeeding going instead — a different benefit",
        "color": "#C00000", "bg": "#FADBD8",
    },
]

n = len(rows)
fig_h = 1.1 * n + 1.6
fig, ax = plt.subplots(figsize=(11, fig_h))
plt.rcParams.update({"font.family": "DejaVu Sans"})

ax.set_xlim(0, 11)
ax.set_ylim(0, n + 1.3)
ax.axis("off")

ax.text(5.5, n + 0.85, "What we know — and don't yet know — about milk fortification",
        ha="center", va="center", fontsize=15, fontweight="bold", color=NAVY)
ax.text(5.5, n + 0.35, "A plain-language summary for talking with parents",
        ha="center", va="center", fontsize=10.5, style="italic", color="#444444")

row_h = 0.92
for i, r in enumerate(rows):
    y = n - i - 0.5 + 0.3
    box = FancyBboxPatch((0.3, y - row_h / 2), 10.4, row_h,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          linewidth=1.0, edgecolor=r["color"], facecolor=r["bg"], zorder=1)
    ax.add_patch(box)
    circ = Circle((1.05, y), 0.28, facecolor=r["color"], edgecolor="none", zorder=2)
    ax.add_patch(circ)
    ax.text(1.9, y + 0.14, r["q"], ha="left", va="center", fontsize=10.8,
            fontweight="bold", color=NAVY, zorder=3, wrap=True)
    ax.text(1.9, y - 0.20, r["detail"], ha="left", va="center", fontsize=9.3,
            color="#333333", style="italic", zorder=3)
    ax.text(10.4, y, r["verdict"], ha="right", va="center", fontsize=10.3,
            fontweight="bold", color=r["color"], zorder=3)

ax.text(5.5, -0.15, "Source: bmf-preterm-fortification evidence review, 50 PMID-verified studies. Not a substitute for individual clinical discussion.",
        ha="center", va="top", fontsize=8, style="italic", color="#666666")

fig.tight_layout()
fig.savefig("figure3_parent_infographic.png", dpi=300, bbox_inches="tight", facecolor="white")
print("Saved figure3_parent_infographic.png")
