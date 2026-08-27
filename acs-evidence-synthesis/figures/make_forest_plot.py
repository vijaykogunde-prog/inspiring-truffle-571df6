import sys
sys.path.insert(0, "/root/.claude/skills/synced/clinical-figures/scripts")
import matplotlib.pyplot as plt
import numpy as np
import style

style.apply_base_style()

# Panel A: ACS vs no ACS/placebo (McGoldrick 2020, Cochrane CD004454.pub4)
panel_a = [
    ("Perinatal death",              0.85, 0.77, 0.93, 14),
    ("Neonatal death",               0.78, 0.70, 0.87, 22),
    ("Respiratory distress syndrome",0.71, 0.65, 0.78, 26),
    ("Intraventricular haemorrhage", 0.58, 0.45, 0.75, 12),
    ("Developmental delay (childhood)", 0.51, 0.27, 0.97, 3),
]

# Panel B: Dexamethasone vs betamethasone (Williams 2022, Cochrane CD006764.pub4 / ASTEROID)
panel_b = [
    ("Death after randomisation",     1.03, 0.66, 1.63, 5),
    ("Respiratory distress syndrome", 1.06, 0.91, 1.22, 5),
    ("Intraventricular haemorrhage",  0.71, 0.28, 1.81, 4),
    ("Neurodevelopmental disability (2y)", 1.02, 0.85, 1.22, 2),
    ("Cerebral palsy",                2.50, 0.97, 6.39, 1),
]

fig, axes = plt.subplots(2, 1, figsize=(9.5, 8.2), gridspec_kw={"height_ratios": [5, 5]})

def draw_panel(ax, data, title, left_label, right_label, footnote):
    y = np.arange(len(data))[::-1]
    for i, (label, rr, lo, hi, n) in enumerate(data):
        yi = y[i]
        color = style.RED if (lo > 1.0 or hi < 1.0) else style.NAVY
        # use grey for CIs crossing 1 that are still the "high certainty" no-diff outcomes
        ax.plot([lo, hi], [yi, yi], color=style.NAVY, lw=1.6, zorder=2)
        ax.plot(rr, yi, marker="s", markersize=7 + n * 1.1, color=style.BLUE,
                markeredgecolor=style.NAVY, zorder=3)
        ax.text(11.5, yi, f"{rr:.2f} ({lo:.2f}-{hi:.2f})", va="center", ha="left",
                fontsize=8.8, color=style.NAVY)
    ax.axvline(1.0, color=style.GREY, lw=1.0, linestyle="--", zorder=1)
    ax.set_xscale("log")
    ax.set_xlim(0.15, 30)
    ax.set_xticks([0.2, 0.5, 1, 2, 5, 10, 20])
    ax.set_xticklabels(["0.2", "0.5", "1", "2", "5", "10", "20"], fontsize=9)
    ax.set_yticks(y)
    ax.set_yticklabels([d[0] for d in data], fontsize=9.5, color=style.NAVY)
    ax.set_ylim(-0.8, len(data) - 0.2)
    ax.set_xlabel("Risk ratio (log scale), 95% CI", fontsize=9, color=style.NAVY)
    ax.set_title(title, fontsize=11.5, color=style.NAVY, fontweight="bold", loc="left", pad=10)
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(0.15, -0.75, f"← {left_label}", fontsize=8.5, color=style.DARK_GREEN,
            ha="left", style="italic")
    ax.text(30, -0.75, f"{right_label} →", fontsize=8.5, color=style.RED,
            ha="right", style="italic")
    ax.text(11.5, len(data) - 0.15 + 0.55, "RR (95% CI)", fontsize=8.5,
            color=style.GREY, ha="left", style="italic")

draw_panel(axes[0], panel_a, "A. Antenatal corticosteroids vs no treatment / placebo",
           "favours ACS", "favours no treatment", "")
draw_panel(axes[1], panel_b, "B. Dexamethasone vs betamethasone",
           "favours dexamethasone", "favours betamethasone", "")

fig.suptitle("Figure 2. Effect estimates for antenatal corticosteroids: efficacy vs no treatment, and agent-to-agent comparison",
             fontsize=11.5, color=style.NAVY, y=0.995, fontweight="bold")
fig.text(0.02, 0.005,
         "Panel A: McGoldrick E et al, Cochrane Database Syst Rev 2020 (27 RCTs, 11 272 women/11 925 neonates), pooled vs placebo/no treatment.\n"
         "Panel B: Williams MJ et al, Cochrane Database Syst Rev 2022 (9 trials, 2096 women/2319 infants; cerebral palsy from 1 trial, n=1223 children).\n"
         "Marker size reflects relative number of contributing trials. Panel B, cerebral palsy: CI does not exclude an important increase in risk with dexamethasone.",
         fontsize=7.3, color=style.GREY, va="bottom")

plt.tight_layout(rect=[0, 0.045, 1, 0.97])
style.save(fig, "/home/user/inspiring-truffle-571df6/acs-evidence-synthesis/figures/figure2_forest_plot.png")
