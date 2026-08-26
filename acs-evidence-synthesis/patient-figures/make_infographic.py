import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

TEAL = "#1B7A72"
LIGHT = "#E3F3F1"
AMBER = "#E8A33D"
TEXT = "#0F4C4C"
plt.rcParams.update({"font.family": "DejaVu Sans"})

cards = [
    ("2", "injections", "Usually given 24 hours apart\n(or 4 smaller ones, 12 hours apart)"),
    ("<10", "minutes", "How long each injection\ntakes to give"),
    ("48", "hours", "Time for the injection to have\nits full effect on your baby's lungs"),
    ("50+", "years", "How long doctors have been\nusing this treatment safely"),
]

fig, axes = plt.subplots(1, 4, figsize=(11.5, 3.6))

for ax, (big, unit, desc) in zip(axes, cards):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    box = FancyBboxPatch((0.04, 0.04), 0.92, 0.92, boxstyle="round,pad=0.02,rounding_size=0.08",
                          linewidth=1.6, edgecolor=TEAL, facecolor=LIGHT, transform=ax.transAxes)
    ax.add_patch(box)
    ax.text(0.5, 0.66, big, ha="center", va="center", fontsize=30, fontweight="bold", color=TEAL, transform=ax.transAxes)
    ax.text(0.5, 0.47, unit, ha="center", va="center", fontsize=12, color=TEXT, transform=ax.transAxes)
    ax.text(0.5, 0.22, desc, ha="center", va="center", fontsize=8.8, color="#3A5252", transform=ax.transAxes, linespacing=1.4)

fig.suptitle("At a glance", fontsize=17, color=TEXT, fontweight="bold", y=1.03)
plt.tight_layout()
fig.savefig("/home/user/inspiring-truffle-571df6/acs-evidence-synthesis/patient-figures/p4_infographic.png",
            dpi=300, bbox_inches="tight", facecolor="white")
print("saved")
