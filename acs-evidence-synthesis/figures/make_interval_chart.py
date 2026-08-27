import sys
sys.path.insert(0, "/root/.claude/skills/synced/clinical-figures/scripts")
import matplotlib.pyplot as plt
import numpy as np
import style

style.apply_base_style()

# Melamed N et al, Obstet Gynecol 2015 (PMID 26000509), n=6870 singletons 24-33+6 weeks.
# Adjusted OR for composite adverse neonatal outcome, relative to the 1-7 day reference group.
categories = ["No ACS", "Partial course\n(<24h before birth)", "ACS 1-7 days\nbefore birth\n(reference)", "ACS >7 days\nbefore birth"]
aor = [2.12, 1.48, 1.00, 1.46]
lo = [1.69, 1.22, 1.00, 1.20]
hi = [2.65, 1.80, 1.00, 1.77]

fig, ax = plt.subplots(figsize=(8.6, 5.6))
x = np.arange(len(categories))
colors = [style.RED, style.ORANGE, style.DARK_GREEN, style.ORANGE]

bars = ax.bar(x, aor, color=colors, width=0.55, zorder=3, edgecolor=style.NAVY, linewidth=1.0)
err_lo = [a - l for a, l in zip(aor, lo)]
err_hi = [h - a for a, h in zip(aor, hi)]
ax.errorbar(x, aor, yerr=[err_lo, err_hi], fmt="none", ecolor=style.NAVY, capsize=5, lw=1.4, zorder=4)

for i, (a, l, h) in enumerate(zip(aor, lo, hi)):
    label = "1.00\n(reference)" if a == 1.00 else f"{a:.2f}\n({l:.2f}-{h:.2f})"
    ax.text(i, h + 0.12, label, ha="center", va="bottom", fontsize=9.5, color=style.NAVY, fontweight="bold")

ax.axhline(1.0, color=style.GREY, lw=1.0, linestyle="--", zorder=1)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=9.8, color=style.NAVY)
ax.set_ylabel("Adjusted odds ratio for composite adverse\nneonatal outcome (95% CI)", fontsize=10, color=style.NAVY)
ax.set_ylim(0, 3.1)
ax.spines[["top", "right"]].set_visible(False)
ax.set_title("Figure 3. A partial course still reduces risk relative to no treatment,\nbut is not equivalent to a completed, well-timed course",
              fontsize=11.5, color=style.NAVY, fontweight="bold", pad=14)

fig.text(0.02, 0.01,
         "Source: Melamed N et al, Obstet Gynecol 2015;125:1377-84 (PMID 26000509). Canadian Neonatal Network cohort, n=6870 singletons, 24+0-33+6 weeks.\n"
         "A single/partial dose closes roughly half the excess risk seen with no treatment at all, relative to the best-timed (1-7 day) group.",
         fontsize=8, color=style.GREY, va="bottom")

plt.tight_layout(rect=[0, 0.06, 1, 1])
style.save(fig, "/home/user/inspiring-truffle-571df6/acs-evidence-synthesis/figures/figure3_interval_benefit.png")
