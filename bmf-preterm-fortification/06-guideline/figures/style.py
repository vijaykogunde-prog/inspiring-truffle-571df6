"""
Shared visual style for the clinical-figures skill.

All five generators (flowchart, patient_flow, domain_heatmap, stacked_bar,
likert_bars) import from here so that a whole paper's figure set stays
visually consistent, matching the look of typical neonatology / clinical-trial
figures (navy-blue outlines, restrained severity palette, Calibri/Arial-style
sans-serif, 300 DPI export).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# ---- Palette -----------------------------------------------------------
NAVY = "#1F3864"
BLUE = "#2E5FA3"
LIGHT_BLUE = "#BDD7EE"
GREEN = "#4CAF50"
DARK_GREEN = "#375623"
TAN = "#F5DEB8"        # "mild" fill used in Fig 3 style
ORANGE = "#C55A11"      # "moderate" fill
DARKBLUE_FILL = "#1F4E79"  # "cool" action boxes
RED = "#C00000"          # "severe"
GREY = "#808080"
LIGHT_GREY = "#F2F2F2"
WHITE = "#FFFFFF"

# Ordinal severity ramp used by domain_heatmap.py and stacked_bar.py.
# Index 0 = normal/no abnormality ... index 3 = severe.
SEVERITY_COLORS = ["#FFFFFF", "#BDD7EE", "#2E75B6", "#1F3864"]
SEVERITY_LABELS = ["Normal", "Mild", "Moderate", "Severe"]

# Alternate 3-tier severity ramp (mild / moderate / severe) matching Figure 4.
SEVERITY3_COLORS = ["#BDD7EE", "#2E75B6", "#C00000"]
SEVERITY3_LABELS = ["Mild", "Moderate", "Severe"]

FONT_FAMILY = "DejaVu Sans"  # widely available fallback that renders like Calibri/Arial


def apply_base_style():
    plt.rcParams.update({
        "font.family": FONT_FAMILY,
        "font.size": 11,
        "axes.edgecolor": GREY,
        "axes.linewidth": 0.8,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    })


def save(fig, path, dpi=300):
    fig.savefig(path, dpi=dpi, bbox_inches="tight", facecolor="white")
    print(f"Saved {path} at {dpi} DPI")
