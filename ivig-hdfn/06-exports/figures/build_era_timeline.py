import sys
sys.path.insert(0, "/root/.claude/skills/synced/2389bb1d-c7ea-4be5-b433-fd35c835aaae_581a2e6a-ab64-4935-b979-d83b41c881a4/clinical-figures/scripts")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from style import apply_base_style, save, NAVY

apply_base_style()

# Only trials with a numerically reported control-arm exchange-transfusion
# rate in their abstract are plotted (Domain A extraction table, rows A1, A4,
# A6, A7) -- no value is estimated or interpolated.
trials = [
    {"year": 1992, "rate": 69, "label": "Rübo et al. 1992\n(Germany)\nopen-label, positive", "blinded": False, "positive": True},
    {"year": 2010, "rate": 22, "label": "Elalfy et al. 2010\n(Egypt)\nunclear blinding, positive", "blinded": False, "positive": True},
    {"year": 2011, "rate": 15, "label": "Smits-Wintjens et al. 2011\n(Netherlands)\ndouble-blind placebo, NULL", "blinded": True, "positive": False},
    {"year": 2012, "rate": 15.2, "label": "Santos et al. 2012\n(Brazil)\ndouble-blind placebo, NULL", "blinded": True, "positive": False},
]

fig, ax = plt.subplots(figsize=(11, 7.5))

for t in trials:
    color = "#548235" if t["positive"] else NAVY
    marker = "o" if t["blinded"] else "s"
    facecolor = color if t["blinded"] else "white"
    ax.scatter([t["year"]], [t["rate"]], s=420, marker=marker,
               facecolor=facecolor, edgecolor=color, linewidth=2.6, zorder=3)

# Connecting line to show the trend
years = [t["year"] for t in trials]
rates = [t["rate"] for t in trials]
ax.plot(years, rates, color="#808080", linewidth=1.4, linestyle="--", zorder=1)

# Annotations
offsets = [(-0.35, 8), (0.15, 8), (-2.7, -13), (0.55, 1)]
for t, (dx, dy) in zip(trials, offsets):
    ax.annotate(t["label"], (t["year"], t["rate"]), xytext=(t["year"] + dx, t["rate"] + dy),
                fontsize=9.3, color=NAVY, ha="left" if dx >= 0 else "left",
                linespacing=1.35)

ax.set_xlim(1990, 2015)
ax.set_ylim(0, 80)
ax.set_xlabel("Trial publication year", fontsize=11.5, color=NAVY)
ax.set_ylabel("Exchange-transfusion rate in the\nno-IVIG / placebo control arm (%)", fontsize=11.5, color=NAVY)
ax.set_title("The era effect in Rh haemolytic disease: as phototherapy improved\nand trial blinding tightened, IVIG's apparent benefit disappeared",
             fontsize=13, color=NAVY, fontweight="bold", pad=14)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", color="#E0E0E0", linewidth=0.8, zorder=0)

# Legend (manual, since markers encode two dimensions at once)
from matplotlib.lines import Line2D
legend_elems = [
    Line2D([0], [0], marker="s", color="w", markerfacecolor="white", markeredgecolor="#548235",
           markeredgewidth=2.2, markersize=13, label="Open-label / unblinded — IVIG reported effective"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor=NAVY, markeredgecolor=NAVY,
           markersize=13, label="Double-blind, placebo-controlled — IVIG NULL (no effect)"),
]
ax.legend(handles=legend_elems, loc="upper right", fontsize=9.3, frameon=False)

ax.text(1990, -14,
        "Only the four Domain A trials reporting a numeric control-arm exchange-transfusion rate are plotted (extraction rows A1, A4, A6, A7).\n"
        "Every trial that also reports a large IVIG benefit is open-label or unblinded; both placebo-controlled trials are null.",
        fontsize=8.6, style="italic", color=NAVY)

plt.tight_layout()
save(fig, sys.argv[1] if len(sys.argv) > 1 else "era-timeline.png")
