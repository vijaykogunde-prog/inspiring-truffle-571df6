import sys
sys.path.insert(0, "/root/.claude/skills/synced/clinical-figures/scripts")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import style

style.apply_base_style()

NAVY = style.NAVY
GREEN = "#2E7D32"
RED = "#B3261E"
GREY = "#F2F2F2"
LIGHTGREEN = "#E8F5E9"
LIGHTRED = "#FBEAE9"

cards = [
    {
        "title": "Regimen A\nWHO / ACOG standard",
        "dose": "6 mg IM",
        "interval": "every 12 hours",
        "n": "x4 doses",
        "total": "24 mg total",
        "evidence": "WHO ACTION-I RCT\n(n=2852 women)\nGuideline-endorsed",
        "color": GREEN, "fill": LIGHTGREEN, "stamp": "TRIAL-TESTED", "stampcolor": GREEN,
    },
    {
        "title": "Regimen B\nRCOG / ASTEROID",
        "dose": "12 mg IM",
        "interval": "every 24 hours",
        "n": "x2 doses",
        "total": "24 mg total",
        "evidence": "ASTEROID RCT\n(n=1346 women)\nRCOG GTG74 primary\nrecommendation",
        "color": GREEN, "fill": LIGHTGREEN, "stamp": "RECOMMENDED", "stampcolor": GREEN,
    },
    {
        "title": "Regimen C\nCurrent unit practice",
        "dose": "12 mg IM",
        "interval": "every 12 hours",
        "n": "x2 doses",
        "total": "24 mg total",
        "evidence": "No RCT\nNo guideline endorsement\nNo SPC licence identified\n(0 studies of this exact\nregimen for efficacy or\nsafety)",
        "color": RED, "fill": LIGHTRED, "stamp": "NOT EVIDENCE-BASED", "stampcolor": RED,
    },
]

fig, axes = plt.subplots(1, 3, figsize=(12.6, 6.6))

for ax, c in zip(axes, cards):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    box = FancyBboxPatch((0.03, 0.03), 0.94, 0.94, boxstyle="round,pad=0.02,rounding_size=0.05",
                          linewidth=2.2, edgecolor=c["color"], facecolor=c["fill"], transform=ax.transAxes, zorder=1)
    ax.add_patch(box)
    ax.text(0.5, 0.92, c["title"], ha="center", va="top", fontsize=13.5, fontweight="bold",
            color=NAVY, transform=ax.transAxes, linespacing=1.3)
    ax.text(0.5, 0.72, c["dose"], ha="center", va="center", fontsize=22, fontweight="bold",
            color=NAVY, transform=ax.transAxes)
    ax.text(0.5, 0.63, c["interval"], ha="center", va="center", fontsize=13, color=NAVY, transform=ax.transAxes)
    ax.text(0.5, 0.565, f"{c['n']}  •  {c['total']}", ha="center", va="center", fontsize=10.5,
            color="#555555", transform=ax.transAxes)
    ax.plot([0.12, 0.88], [0.50, 0.50], color=c["color"], lw=1.2, alpha=0.5, transform=ax.transAxes)
    ax.text(0.5, 0.40, c["evidence"], ha="center", va="center", fontsize=10, color=NAVY,
            transform=ax.transAxes, linespacing=1.6)
    stampbox = FancyBboxPatch((0.09, 0.06), 0.82, 0.10, boxstyle="round,pad=0.02,rounding_size=0.04",
                               linewidth=0, facecolor=c["stampcolor"], transform=ax.transAxes, zorder=2)
    ax.add_patch(stampbox)
    ax.text(0.5, 0.11, c["stamp"], ha="center", va="center", fontsize=11.5, fontweight="bold",
            color="white", transform=ax.transAxes, zorder=3)

fig.suptitle("Three dexamethasone regimens in global use — only two have ever been tested",
              fontsize=15.5, color=NAVY, fontweight="bold", y=1.01)
fig.text(0.5, -0.02,
         "Regimen C combines the per-dose amount of Regimen B with the interval of Regimen A. This specific combination\n"
         "has never been the subject of a randomised trial, cohort study, or named guideline recommendation, in any jurisdiction identified.",
         ha="center", fontsize=9.5, color="#555555", style="italic")

plt.tight_layout(rect=[0, 0.02, 1, 0.96])
style.save(fig, "/home/user/inspiring-truffle-571df6/acs-interval-review/figures/fig1_three_regimens.png")
