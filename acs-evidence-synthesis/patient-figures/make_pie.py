import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

TEAL = "#1B7A72"
LIGHT = "#E3F3F1"
GREY = "#E7E7E7"
TEXT = "#0F4C4C"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})

fig, axes = plt.subplots(1, 2, figsize=(9.5, 5.4))

data = [
    ("Without the injection", 14.4, "#E8A33D", axes[0]),
    ("With the injection", 11.6, TEAL, axes[1]),
]

for label, pct, color, ax in data:
    sizes = [pct, 100 - pct]
    wedges, _ = ax.pie(
        sizes,
        colors=[color, GREY],
        startangle=90,
        counterclock=False,
        wedgeprops={"width": 0.42, "edgecolor": "white", "linewidth": 2},
    )
    ax.text(0, 0.06, f"{pct:.1f}%", ha="center", va="center", fontsize=26, fontweight="bold", color=color)
    ax.text(0, -0.22, "needed help\nbreathing", ha="center", va="center", fontsize=10.5, color=TEXT)
    ax.set_title(label, fontsize=13.5, color=TEXT, fontweight="bold", pad=14)

fig.suptitle("For babies born a little early (34-37 weeks),\ndoes the injection change the chance of needing help breathing?",
              fontsize=13.5, color=TEXT, fontweight="bold", y=1.04)
fig.text(0.5, -0.03,
         "Based on a large study (ALPS) of over 2800 women whose babies were expected between 34 and 37 weeks.\nOf the babies whose mothers had the injection, fewer needed breathing support after birth.",
         ha="center", fontsize=9.3, color="#5B6B6B")

plt.tight_layout()
fig.savefig("/home/user/inspiring-truffle-571df6/acs-evidence-synthesis/patient-figures/p2_pie.png",
            dpi=300, bbox_inches="tight", facecolor="white")
print("saved")
