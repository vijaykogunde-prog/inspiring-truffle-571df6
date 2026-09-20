import sys
sys.path.insert(0, "/root/.claude/skills/synced/2389bb1d-c7ea-4be5-b433-fd35c835aaae_581a2e6a-ab64-4935-b979-d83b41c881a4/clinical-figures/scripts")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from style import apply_base_style, save, NAVY, WHITE

apply_base_style()

rows = [
    "Exchange transfusion",
    "Necrotising enterocolitis",
    "Top-up transfusion /\nlate anaemia",
    "Isoagglutinin-mediated\nhaemolysis",
    "Thromboembolism /\nhyperviscosity",
]
cols = ["Term\nRh-D", "Preterm\nRh-D", "ABO,\nDAT+", "ABO,\nDAT−", "Kell / anti-c /\nanti-E / mixed"]

# 0 = no direct evidence, 1 = very low certainty, 2 = low-moderate certainty
grid = [
    [2, 0, 1, 0, 0],  # Exchange transfusion
    [1, 0, 1, 0, 0],  # NEC
    [2, 0, 1, 0, 0],  # Top-up / late anaemia
    [1, 0, 1, 0, 0],  # Isoagglutinin haemolysis
    [0, 0, 0, 0, 0],  # Thromboembolism/hyperviscosity
]
colors = {0: "#FFFFFF", 1: "#BDD7EE", 2: "#1F3864"}
textcolor = {0: NAVY, 1: NAVY, 2: "white"}
labels = {0: "No direct\nevidence", 1: "Very low\ncertainty", 2: "Low–Moderate\ncertainty"}

n_rows, n_cols = len(rows), len(cols)
cell_w, cell_h = 2.0, 1.15
row_label_w = 4.6
col_label_h = 1.1

fig_w = row_label_w + n_cols * cell_w + 0.3
fig_h = col_label_h + n_rows * cell_h + 2.0
fig, ax = plt.subplots(figsize=(fig_w, fig_h))
ax.set_xlim(0, fig_w)
ax.set_ylim(0, fig_h)
ax.axis("off")

top_y = fig_h - 0.3

# Column headers
for j, c in enumerate(cols):
    x0 = row_label_w + j * cell_w
    ax.text(x0 + cell_w / 2, top_y - col_label_h / 2, c, ha="center", va="center",
            fontsize=10.5, fontweight="bold", color=NAVY)

# Grid + row labels
grid_top = top_y - col_label_h
for i, r in enumerate(rows):
    y0 = grid_top - (i + 1) * cell_h
    ax.text(row_label_w - 0.25, y0 + cell_h / 2, r, ha="right", va="center",
            fontsize=10.5, color=NAVY)
    for j, c in enumerate(cols):
        x0 = row_label_w + j * cell_w
        v = grid[i][j]
        rect = Rectangle((x0, y0), cell_w, cell_h, facecolor=colors[v],
                          edgecolor=NAVY, linewidth=1.2)
        ax.add_patch(rect)
        ax.text(x0 + cell_w / 2, y0 + cell_h / 2, labels[v], ha="center", va="center",
                fontsize=8.8, color=textcolor[v])

# Outer border around the whole grid
grid_bottom = grid_top - n_rows * cell_h
ax.add_patch(Rectangle((row_label_w, grid_bottom), n_cols * cell_w, n_rows * cell_h,
                        facecolor="none", edgecolor=NAVY, linewidth=1.8))

# Legend
legend_y = grid_bottom - 0.75
lx = row_label_w
for v in [0, 1, 2]:
    ax.add_patch(Rectangle((lx, legend_y), 0.5, 0.4, facecolor=colors[v], edgecolor=NAVY, linewidth=1))
    ax.text(lx + 0.65, legend_y + 0.2, labels[v].replace("\n", " "), ha="left", va="center", fontsize=9.5, color=NAVY)
    lx += 0.65 + len(labels[v].replace(chr(10), " ")) * 0.085 + 0.6

ax.text(row_label_w, legend_y - 0.7,
        "GRADE certainty of the evidence, by outcome and clinical subgroup. Blank cells (\"No direct evidence identified\")\n"
        "mean no comparative study addresses that subgroup for that outcome at all — not that IVIG is known to be safe or ineffective there.",
        ha="left", va="top", fontsize=8.3, style="italic", color=NAVY)

plt.tight_layout()
save(fig, sys.argv[1] if len(sys.argv) > 1 else "grade-summary-table.png")
print("done")
