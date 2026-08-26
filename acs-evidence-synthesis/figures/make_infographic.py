import sys
sys.path.insert(0, "/root/.claude/skills/synced/clinical-figures/scripts")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import style

style.apply_base_style()

# Absolute effects per 1000 women/babies treated, as reported/computable from
# McGoldrick E et al, Cochrane Database Syst Rev 2020 (PMID 33368142).
rows = [
    ("Perinatal death",               23, "fewer", "11 to 36 fewer per 1000"),
    ("Neonatal death",                26, "fewer", "15 to 36 fewer per 1000"),
    ("Respiratory distress syndrome", 43, "fewer", "32 to 52 fewer per 1000"),
    ("Intraventricular haemorrhage",  14, "fewer", "8 to 18 fewer per 1000"),
    ("Developmental delay (childhood)", 38, "fewer", "2 to 57 fewer per 1000"),
]

fig, ax = plt.subplots(figsize=(9.2, 5.4))
y = np.arange(len(rows))[::-1]
max_val = 50

for i, (label, val, direction, ci_text) in enumerate(rows):
    yi = y[i]
    # baseline track (per 1000)
    ax.barh(yi, max_val, height=0.55, color=style.LIGHT_GREY, zorder=1)
    ax.barh(yi, val, height=0.55, color=style.BLUE, zorder=2)
    ax.text(val + 1.0, yi, f"{val} fewer per 1000", va="center", ha="left",
            fontsize=10, color=style.NAVY, fontweight="bold")
    ax.text(-1.5, yi, label, va="center", ha="right", fontsize=10.3, color=style.NAVY)
    ax.text(max_val + 24, yi, ci_text, va="center", ha="left", fontsize=8.3,
            color=style.GREY, style="italic")

ax.set_xlim(0, max_val + 55)
ax.set_ylim(-0.8, len(rows) - 0.2)
ax.axis("off")

ax.set_title("Figure 4. What one course of antenatal corticosteroids changes,\nper 1000 women treated compared with no treatment",
              fontsize=12.5, color=style.NAVY, fontweight="bold", pad=18, loc="center")

fig.text(0.5, 0.055,
         "Source: McGoldrick E et al, Cochrane Database Syst Rev 2020;12:CD004454 (PMID 33368142). 27 RCTs, 11 272 women / 11 925 neonates, all preterm strata pooled.\n"
         "Absolute risk differences as reported by the review; magnitude of benefit is generally larger at earlier gestational ages and smaller closer to term.",
         fontsize=8, color=style.GREY, ha="center", va="bottom")

plt.tight_layout(rect=[0.02, 0.08, 1, 0.94])
style.save(fig, "/home/user/inspiring-truffle-571df6/acs-evidence-synthesis/figures/figure4_infographic.png")
