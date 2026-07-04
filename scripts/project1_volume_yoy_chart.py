"""One-off documentation chart: Thunderbird Desktop SUMO questions per month,
year-over-year, from the BigQuery ground-truth export (see PROJECT1/validation/).

Renders a year-over-year overlay (12 months on x, one line per year) that makes
the 2025→2026 volume decline visible at a glance. Static PNG for the record — not
part of any pipeline; re-run only if the BQ export is refreshed:

  uv run scripts/project1_volume_yoy_chart.py

Palette: dataviz categorical slots 1–4 (validated: worst adjacent CVD ΔE 24.2).
aqua/yellow are sub-3:1 on the light surface, so every line is DIRECT-LABELLED
(the skill's relief rule) — identity never rests on colour alone.
"""
import calendar
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CSV = "PROJECT1/validation/bq-desktop-questions-by-month-2023-01_2026-07.csv"
OUT = "PROJECT1/validation/desktop-questions-yoy.png"

# dataviz reference palette — categorical slots 1..4 (fixed order), + ink tokens
SERIES = ["#2a78d6", "#1baf7a", "#eda100", "#008300"]  # blue, aqua, yellow, green
INK, INK2, MUTED = "#0b0b0b", "#52514e", "#898781"
GRID, AXIS, SURFACE = "#e1e0d9", "#c3c2b7", "#fcfcfb"

# A month is "complete" only if a later month exists in the data (so the current
# partial month isn't drawn as a cliff). Here: everything through 2026-06.
LAST_COMPLETE = "2026-06"


def main():
    df = pd.read_csv(CSV)
    df["year"] = df["month"].str[:4].astype(int)
    df["m"] = df["month"].str[5:7].astype(int)
    df = df[df["month"] <= LAST_COMPLETE]

    plt.rcParams.update({"font.family": "sans-serif", "font.size": 11,
                         "figure.facecolor": SURFACE, "axes.facecolor": SURFACE})
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

    years = sorted(df["year"].unique())
    for i, yr in enumerate(years):
        g = df[df["year"] == yr].sort_values("m")
        color = SERIES[i % len(SERIES)]
        partial = g["m"].max() < 12
        ax.plot(g["m"], g["num_questions"], color=color, lw=2,
                marker="o", ms=5, mec=SURFACE, mew=1, zorder=3,
                solid_capstyle="round")
        # direct label at the line's right end (relief rule + YoY identity)
        last = g.iloc[-1]
        ax.annotate(f"{yr}" + (" ▪" if partial else ""),
                    (last["m"], last["num_questions"]),
                    xytext=(8, 0), textcoords="offset points",
                    va="center", ha="left", color=color, fontweight="bold",
                    fontsize=11)

    ax.set_xticks(range(1, 13))
    ax.set_xticklabels([calendar.month_abbr[m][0] for m in range(1, 13)], color=MUTED)
    ax.set_xlim(0.6, 12.9)
    ax.set_ylim(0, df["num_questions"].max() * 1.08)
    ax.tick_params(colors=MUTED, length=0)
    for lbl in ax.get_yticklabels():
        lbl.set_color(MUTED)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(AXIS)
    ax.grid(axis="y", color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)

    ax.set_ylabel("questions created / month", color=INK2)

    # stacked header (title + short subtitle) with a bottom source footnote —
    # keeps them from colliding / overflowing the plot.
    fig.text(0.055, 0.965, "Thunderbird Desktop — SUMO questions per month, "
             "year over year", color=INK, fontsize=14, fontweight="bold", va="top")
    fig.text(0.055, 0.915, "Support volume ~halved from 2024/2025 to 2026  ·  "
             "▪ 2026 partial (Jan–Jun)", color=INK2, fontsize=10, va="top")
    fig.text(0.055, 0.02, "Source: BigQuery moz-fx-sumo-prod.sumo."
             "metrics_thunderbird_questions · product=thunderbird · is_spam=FALSE "
             "· created (UTC)", color=MUTED, fontsize=8, va="bottom")

    fig.subplots_adjust(top=0.86, bottom=0.12, left=0.09, right=0.93)
    fig.savefig(OUT, facecolor=SURFACE)
    print(f"wrote {OUT}  ({len(years)} years, through {LAST_COMPLETE})")


if __name__ == "__main__":
    main()
