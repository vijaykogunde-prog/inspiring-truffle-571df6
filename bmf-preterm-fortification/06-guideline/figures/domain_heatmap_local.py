#!/usr/bin/env python3
"""
domain_heatmap.py — per-subject, per-domain severity grid.

Reproduces the style of "Figure 3" (progression at t1/t2) and "Figure 5"
(per-case domain profile with an aEEG/CFM status bar) in the eScreener/COMET
manuscript: one column per subject (or per subject-timepoint), one row per
clinical domain, cells colour-coded by ordinal severity, subjects optionally
clustered into labelled groups with a thin separating gap, a small text
marker overlay (e.g. "S" for seizure) on individual cells, an optional
coloured footer strip (e.g. aEEG normal/abnormal), and a legend.

Usage:
    python3 domain_heatmap.py spec.json output.png

Spec format (JSON) — see examples/example_domain_heatmap.json for a full
worked example reproducing Figure 5's structure.
{
  "row_labels": ["Consciousness", "Spontaneous activity", "Posture", "Tone",
                 "Reflexes", "Autonomic system"],
  "severity_colors": ["#FFFFFF", "#BDD7EE", "#2E75B6", "#1F3864"],
  "severity_labels": ["Normal", "Mild", "Moderate", "Severe"],
  "groups": [
    {"label": "NICHD +Toby", "columns": ["1","2","3", "...": "21"]},
    {"label": "NICHD only",  "columns": ["22", "...": "30"]}
  ],
  "cells": {"1": {"Consciousness": 2, "Tone": 3, "...": "..."}, "2": {...}},
  "marks": {"17": {"Consciousness": "S"}},
  "footer": {
    "row_label": "aEEG",
    "colors": {"abnormal": "#C00000", "normal": "#548235"},
    "values": {"1": "abnormal", "22": "normal"}
  },
  "column_number_row": true
}
"""
import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

sys.path.insert(0, str(Path(__file__).parent))
from style import apply_base_style, save, SEVERITY_COLORS, SEVERITY_LABELS, GREY


def build(spec_path, out_path):
    spec = json.loads(Path(spec_path).read_text())
    row_labels = spec["row_labels"]
    sev_colors = spec.get("severity_colors", SEVERITY_COLORS)
    sev_labels = spec.get("severity_labels", SEVERITY_LABELS)
    groups = spec["groups"]
    cells = spec["cells"]
    marks = spec.get("marks", {})
    footer = spec.get("footer")
    show_col_numbers = spec.get("column_number_row", False)

    n_rows = len(row_labels)
    gap = 1.4  # gap (in column-widths) between groups — widened locally so group labels do not collide
    all_cols = []
    group_spans = []  # (label, start_x, end_x)
    x_cursor = 0.0
    for g in groups:
        start = x_cursor
        for c in g["columns"]:
            all_cols.append((c, x_cursor))
            x_cursor += 1
        group_spans.append((g["label"], start, x_cursor))
        x_cursor += gap

    total_width = x_cursor - gap
    footer_rows = 1 if footer else 0
    header_rows = 1 if show_col_numbers else 0
    total_rows = n_rows + footer_rows

    apply_base_style()
    fig_w = max(10, total_width * 0.55 + 3)
    fig_h = max(4.5, total_rows * 0.42 + header_rows * 0.3 + 2.2)
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))

    def color_for(v):
        if isinstance(v, str) and v in sev_labels:
            return sev_colors[sev_labels.index(v)]
        if isinstance(v, int):
            return sev_colors[v]
        return v  # assume already a hex color

    # column number header row
    y_top = total_rows
    if show_col_numbers:
        for col_id, x in all_cols:
            ax.text(x + 0.5, y_top + header_rows - 0.5, str(col_id),
                     ha="center", va="center", fontsize=8)

    # domain rows (drawn top-to-bottom)
    for ri, row_label in enumerate(row_labels):
        y = total_rows - 1 - ri
        for col_id, x in all_cols:
            val = cells.get(str(col_id), {}).get(row_label, 0)
            fc = color_for(val)
            ax.add_patch(Rectangle((x, y), 1, 1, facecolor=fc, edgecolor="black", linewidth=0.8))
            mark = marks.get(str(col_id), {}).get(row_label)
            if mark:
                ax.text(x + 0.5, y + 0.5, mark, ha="center", va="center",
                         fontsize=9, fontweight="bold")
        ax.text(-0.3, y + 0.5, row_label, ha="right", va="center", fontsize=10.5)

    # footer strip (e.g. aEEG normal/abnormal)
    if footer:
        y = 0 - 1
        for col_id, x in all_cols:
            v = footer["values"].get(str(col_id), None)
            fc = footer["colors"].get(v, "#FFFFFF") if v else "#FFFFFF"
            ax.add_patch(Rectangle((x, y), 1, 1, facecolor=fc, edgecolor="black", linewidth=0.8))
        ax.text(-0.3, y + 0.5, footer.get("row_label", ""), ha="right", va="center", fontsize=10.5, fontweight="bold")
        y_bottom = y
    else:
        y_bottom = 0

    # group labels underneath
    for label, start, end in group_spans:
        ax.text((start + end) / 2, y_bottom - 0.9, label, ha="center", va="top", fontsize=8.8, wrap=True)

    ax.set_xlim(-2.6, total_width + 0.3)
    ax.set_ylim(y_bottom - 1.6, y_top + header_rows + 0.3)
    ax.axis("off")

    # legend
    handles = [Rectangle((0, 0), 1, 1, facecolor=c, edgecolor="black") for c in sev_colors]
    ax.legend(handles, sev_labels, loc="lower left", bbox_to_anchor=(1.01, 0.0),
               frameon=False, fontsize=10, handlelength=1.4, handleheight=1.4)

    save(fig, out_path)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 domain_heatmap.py spec.json output.png")
        sys.exit(1)
    build(sys.argv[1], sys.argv[2])
