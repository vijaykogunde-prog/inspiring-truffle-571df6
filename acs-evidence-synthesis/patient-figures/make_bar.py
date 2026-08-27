import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

TEAL = "#1B7A72"
GREY = "#E7E7E7"
TEXT = "#0F4C4C"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})

# Source: McGoldrick E et al, Cochrane Database Syst Rev 2020 (PMID 33368142).
rows = [
    ("Not surviving the newborn period", 26),
    ("Needing help breathing\n(respiratory distress)", 43),
    ("Bleeding inside the brain", 14),
    ("Delay in development\nlater in childhood", 38),
]

fig, ax = plt.subplots(figsize=(9.2, 5.0))
y = np.arange(len(rows))[::-1]
max_val = 50

for i, (label, val) in enumerate(rows):
    yi = y[i]
    ax.barh(yi, max_val, height=0.5, color=GREY, zorder=1)
    ax.barh(yi, val, height=0.5, color=TEAL, zorder=2)
    ax.text(val + 1.2, yi, f"{val} fewer babies", va="center", ha="left",
            fontsize=11.5, color=TEXT, fontweight="bold")
    ax.text(-1.5, yi, label, va="center", ha="right", fontsize=11, color=TEXT)

ax.set_xlim(0, max_val + 34)
ax.set_ylim(-0.7, len(rows) - 0.3)
ax.axis("off")
ax.set_title("Out of every 1000 babies given the injection,\ncompared with 1000 babies who were not:",
              fontsize=14, color=TEXT, fontweight="bold", pad=16)

fig.text(0.5, 0.02,
         "Source: Cochrane Review 2020, a summary of 27 studies from around the world (over 11 000 babies).\nThe benefit is usually bigger the earlier a baby is born, and smaller closer to full term.",
         ha="center", fontsize=9, color="#5B6B6B")

plt.tight_layout(rect=[0, 0.06, 1, 1])
fig.savefig("/home/user/inspiring-truffle-571df6/acs-evidence-synthesis/patient-figures/p3_bar.png",
            dpi=300, bbox_inches="tight", facecolor="white")
print("saved")
