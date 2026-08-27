import sys
sys.path.insert(0, "/root/.claude/skills/synced/clinical-figures/scripts")
import matplotlib.pyplot as plt
import numpy as np
import style

style.apply_base_style()

# ---------------------------------------------------------------------
# Figure 3: PK trough comparison
# ---------------------------------------------------------------------
def frac_remaining(t, half_life):
    return 100 * 0.5 ** (t / half_life)

intervals = [12, 24]
tsuei_hl = 2.37   # Tsuei et al 1980, PMID 7389259, 8mg dose, pregnant women near term
jobe_hl = 5.2      # Jobe et al 2019, PMID 31808984, 6mg dose, non-pregnant reproductive-age women

tsuei_vals = [frac_remaining(t, tsuei_hl) for t in intervals]
jobe_vals = [frac_remaining(t, jobe_hl) for t in intervals]

fig, ax = plt.subplots(figsize=(8.6, 5.6))
x = np.arange(len(intervals))
w = 0.32

b1 = ax.bar(x - w/2, tsuei_vals, width=w, color=style.NAVY, label=f"Tsuei 1980 estimate (t½={tsuei_hl}h, pregnant women, 8mg dose)", zorder=3)
b2 = ax.bar(x + w/2, jobe_vals, width=w, color=style.ORANGE, label=f"Jobe 2019 estimate (t½={jobe_hl}h, non-pregnant, 6mg dose)", zorder=3)

for bars in (b1, b2):
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, h + 0.6, f"{h:.1f}%", ha="center", va="bottom",
                fontsize=11, fontweight="bold", color=style.NAVY)

ax.set_xticks(x)
ax.set_xticklabels(["12-hour redosing\n(current unit practice)", "24-hour redosing\n(RCOG/ASTEROID regimen)"], fontsize=11)
ax.set_ylabel("Plasma concentration remaining at redosing\n(% of peak, modelled)", fontsize=10.5, color=style.NAVY)
ax.set_ylim(0, max(tsuei_vals + jobe_vals) * 1.35)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(loc="upper right", fontsize=8.8, frameon=False)
ax.set_title("Figure 3. Neither available human half-life estimate has been measured\nat the unit's actual 12mg dose in pregnant women — the two disagree more than two-fold",
              fontsize=12.5, color=style.NAVY, fontweight="bold", pad=14)

fig.text(0.02, 0.01,
         "Modelled from single-timepoint half-life values reported in Tsuei SE et al, Clin Pharmacol Ther 1980 (PMID 7389259) and Jobe AH et al,\n"
         "Clin Transl Sci 2019 (PMID 31808984). Neither study measured a 12mg IM dose in pregnant women directly - both figures are extrapolations\n"
         "from different doses, populations and eras, and are shown together to illustrate genuine unresolved uncertainty, not to assert either is correct.",
         fontsize=7.8, color="#555555")

plt.tight_layout(rect=[0, 0.07, 1, 1])
style.save(fig, "/home/user/inspiring-truffle-571df6/acs-interval-review/figures/fig3_pk_trough.png")

# ---------------------------------------------------------------------
# Figure 4: Khandelwal 2012 outcomes
# ---------------------------------------------------------------------
fig2, axes = plt.subplots(1, 2, figsize=(9.4, 5.2))

rds = [36.5, 37.3]
nec = [6.2, 0.0]
labels = ["12-hourly", "24-hourly"]

ax = axes[0]
bars = ax.bar(labels, rds, color=[style.NAVY, "#8FA6C4"], width=0.55, zorder=3)
for bar, v in zip(bars, rds):
    ax.text(bar.get_x() + bar.get_width()/2, v + 1, f"{v}%", ha="center", fontsize=12, fontweight="bold", color=style.NAVY)
ax.set_ylim(0, 50)
ax.set_title("Respiratory distress syndrome\n(p = not significant)", fontsize=11.5, color=style.NAVY, fontweight="bold")
ax.spines[["top", "right"]].set_visible(False)
ax.set_ylabel("% of infants", fontsize=10.5, color=style.NAVY)

ax = axes[1]
bars = ax.bar(labels, nec, color=[style.RED, "#8FA6C4"], width=0.55, zorder=3)
for bar, v in zip(bars, nec):
    ax.text(bar.get_x() + bar.get_width()/2, v + 0.25, f"{v}%", ha="center", fontsize=12, fontweight="bold", color=style.NAVY)
ax.set_ylim(0, 8)
ax.set_title("Necrotising enterocolitis\n(p = .03)", fontsize=11.5, color=style.NAVY, fontweight="bold")
ax.spines[["top", "right"]].set_visible(False)

fig2.suptitle("Figure 4. The only randomised dosing-interval trial for either drug (betamethasone,\nKhandelwal et al 2012): equivalent RDS, but significantly more NEC at the 12-hourly interval",
               fontsize=12.5, color=style.NAVY, fontweight="bold", y=1.06)
fig2.text(0.5, -0.03,
          "Khandelwal M et al, Am J Obstet Gynecol 2012 (PMID 22381601). Single-centre, open-label, n=228 mothers/260 fetuses, betamethasone not dexamethasone.\n"
          "Small, unblinded, unreplicated in the 14 years since publication. Not a dexamethasone trial - shown here as the closest available interval-comparison evidence for either drug.",
          ha="center", fontsize=8, color="#555555")

plt.tight_layout(rect=[0, 0.05, 1, 0.90])
style.save(fig2, "/home/user/inspiring-truffle-571df6/acs-interval-review/figures/fig4_khandelwal.png")
print("done")
