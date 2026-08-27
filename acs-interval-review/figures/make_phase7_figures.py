import sys
sys.path.insert(0, "/root/.claude/skills/synced/clinical-figures/scripts")
import matplotlib.pyplot as plt
import numpy as np
import style

style.apply_base_style()
NAVY = style.NAVY
GREEN = "#2E7D32"
RED = "#C00000"
GREY = "#8FA6C4"

# ---------------------------------------------------------------------
# Figure 5: Direct evidence that now exists for Regimen C itself
# ---------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.4))

ax = axes[0]
labels = ["Dexamethasone\n12mg x2/12h\n(n=130)", "Placebo\n(n=122)"]
vals = [3.8, 25.4]
bars = ax.bar(labels, vals, color=[GREEN, GREY], width=0.55, zorder=3)
for bar, v in zip(bars, vals):
    ax.text(bar.get_x() + bar.get_width()/2, v + 0.8, f"{v}%", ha="center", fontsize=13, fontweight="bold", color=NAVY)
ax.set_ylim(0, 32)
ax.set_ylabel("% of infants", fontsize=10.5, color=NAVY)
ax.set_title("Shittu et al 2024 (n=286)\nRegimen C vs placebo\nRespiratory morbidity, P=.000003", fontsize=11, color=NAVY, fontweight="bold")
ax.spines[["top", "right"]].set_visible(False)

ax = axes[1]
x = np.arange(2)
w = 0.32
bw = [2.49, 2.89]
ge = [36.6, 37.7]
bw_bars = ax.bar(x - w/2, [b/3.0*100 for b in bw], width=w, color="#8FA6C4", label="Birth weight\n(% of 3.0kg reference)", zorder=3)
ge_bars = ax.bar(x + w/2, [g/38*100 for g in ge], width=w, color=GREEN, label="GA at delivery\n(% of 38wk reference)", zorder=3)
ax.set_xticks(x)
ax.set_xticklabels(["Regimen A\n6mg x4/12h\n(n=30)", "Regimen C\n12mg x2/12h\n(n=30)"], fontsize=9.5)
ax.set_ylabel("Normalised to reference (%)", fontsize=9.5, color=NAVY)
ax.set_ylim(0, 115)
for bars, raw, unit in [(bw_bars, bw, "kg"), (ge_bars, ge, "wk")]:
    for bar, v in zip(bars, raw):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, f"{v}{unit}", ha="center", fontsize=9.5, fontweight="bold", color=NAVY)
ax.legend(loc="lower center", fontsize=7.6, frameon=False, ncol=1)
ax.set_title("Sukarna et al 2021 (n=60)\nRegimen C vs Regimen A\nSecondary neonatal outcomes, both p<.05", fontsize=11, color=NAVY, fontweight="bold")
ax.spines[["top", "right"]].set_visible(False)

fig.suptitle("Figure 5. Two small RCTs directly used the unit's current regimen (Regimen C) and\nreport reassuring, not alarming, results — but neither tested it against the 24-hourly alternative",
              fontsize=13, color=NAVY, fontweight="bold", y=1.05)
fig.text(0.5, -0.06,
         "Shittu KA et al, BMC Pregnancy Childbirth 2024 (PMID 38698318) and Sukarna N et al, Arch Gynecol Obstet 2021 (PMID 33452923). Both are small, single-centre\n"
         "trials not designed to detect rare neonatal harms (NEC, IVH, long-term neurodevelopment were not reported by either). Neither compared Regimen C against\n"
         "Regimen B (12mg 24-hourly) - the specific comparison this document is concerned with remains untested by any study identified.",
         ha="center", fontsize=8, color="#555555")

plt.tight_layout(rect=[0, 0.02, 1, 0.90])
style.save(fig, "/home/user/inspiring-truffle-571df6/acs-interval-review/figures/fig5_direct_evidence_regimen_c.png")

# ---------------------------------------------------------------------
# Figure 6: What the verified administration-to-birth interval evidence
# actually says (replaces an unverifiable "Canadian Neonatal Network"
# hour-scale claim found in supplementary material reviewed for this
# update). No point-estimates are invented - this is a timeline of the
# reported categorical finding only, not a plotted curve.
# ---------------------------------------------------------------------
fig2, ax = plt.subplots(figsize=(10, 5.0))
ax.set_xlim(0, 28)
ax.set_ylim(0, 3.9)
ax.axis("off")

ax.annotate("", xy=(28, 1.5), xytext=(0, 1.5),
            arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=2))

ax.axvspan(0, 1, ymin=0.42, ymax=0.58, color=RED, alpha=0.18, zorder=1)
ax.text(0.5, 3.35, "Hour 12-13\n(this document's focus)", ha="center", fontsize=9.5, color=RED, fontweight="bold")
ax.annotate("", xy=(0.5, 1.75), xytext=(0.7, 3.1), arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.4))
ax.text(0.5, 0.9, "No mechanism or\ndataset identifies a\nbenefit specific to\nthis window", ha="center", fontsize=8, color=RED)

for day, label in [(0, "Day 0\nFirst dose"), (13.5, "Days 13-14\nPeak reported\nbenefit"), (28, "Day 28\nBenefit has\ndiminished")]:
    ax.plot([day], [1.5], marker="o", markersize=9, color=NAVY, zorder=3)
    va = "bottom" if day != 13.5 else "top"
    ypos = 1.85 if day != 13.5 else 1.1
    ax.text(day, ypos, label, ha="center", va=va, fontsize=9.5, color=NAVY, fontweight="bold")

ax.set_title("Figure 6. The verified administration-to-birth interval evidence: benefit builds over\nDAYS, peaking around days 13-14 - not over hours, and not near hour 12",
              fontsize=12.5, color=NAVY, fontweight="bold", pad=6)

fig2.text(0.5, 0.02,
         "Oladapo OT et al, EClinicalMedicine 2022 (PMID 36467459), a secondary analysis of the WHO ACTION-I trial (2638 women/2904 babies): neonatal mortality benefit\n"
         "increased with longer administration-to-birth interval, reaching peak benefit at days 13-14, then diminishing toward day 28. The paper did not publish exact\n"
         "risk values by hour, so none are shown here. This replaces an hour-scale claim (\"mortality reduction plateaus at 12 hours\") attributed in supplementary material\n"
         "reviewed for this update to a \"Canadian Neonatal Network\" dataset that could not be located in PubMed and is not used.",
         ha="center", fontsize=7.6, color="#555555")

plt.tight_layout(rect=[0, 0.1, 1, 0.94])
style.save(fig2, "/home/user/inspiring-truffle-571df6/acs-interval-review/figures/fig6_interval_to_birth_benefit.png")
print("done")
