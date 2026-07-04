"""Shared time-grain config for the Project 1 spike DETECTORS.

Detection runs at three grains — **daily / weekly / monthly**. This is distinct
from the *reporting* grains (hourly..yearly) in project1_report.py: those are how
trends are displayed; these are the windows over which a spike is *detected*.

Multi-grain detection exists because a slow-burn incident can never clear a daily
threshold. The March 2026 GMX provider outage is the canonical case: ~1–2
questions/day spread across the whole month (15 total, split across v140/v148,
half unversioned) — invisible to the daily version×cause detector, but an obvious
4.3× spike at monthly grain (15 vs a trailing ~3.5 median). Weekly sits between
for incidents that resolve within days.

Thresholds are calibrated on the post-backfill baseline (2026-07) and, like the
daily ones, are just defaults — override per-grain on the CLI.
"""
import pandas as pd

# grain -> offset alias for building the CONTIGUOUS period axis (date_range) that
# baselines are computed over. Must align with period_dt(): daily/'D' -> day
# start, weekly/'7D' from a Monday -> Mondays, monthly/'MS' -> month start.
GRAIN_FREQ = {"daily": "D", "weekly": "7D", "monthly": "MS"}

# Per-grain detector defaults. window/min_periods are in PERIODS (days, weeks or
# months). single_* = single-dimension floor/multiplier; joint_* = version×cause
# floor/lift. Coarser grains accumulate more volume, so floors rise a little.
GRAIN_DEFAULTS = {
    "daily":   dict(window=28, min_periods=14,
                    single_min_count=8, single_mult=3.0,
                    joint_min_count=4, joint_lift=3.0),
    "weekly":  dict(window=8, min_periods=4,
                    single_min_count=6, single_mult=3.0,
                    joint_min_count=4, joint_lift=3.0),
    "monthly": dict(window=6, min_periods=3,
                    single_min_count=8, single_mult=3.0,
                    joint_min_count=5, joint_lift=3.0),
}

GRAINS = list(GRAIN_FREQ)


def period_start(created_date):
    """'YYYY-MM-DD' string -> tz-naive Timestamp (or NaT). Central parse point so
    every detector treats the day the same way."""
    return pd.to_datetime(created_date, errors="coerce")


def period_dt(series_of_dates, grain):
    """Map a Series of 'YYYY-MM-DD' strings to the start Timestamp of the period
    (grain) each falls in — the key detectors group and reindex on."""
    ts = pd.to_datetime(series_of_dates, errors="coerce")
    if grain == "daily":
        return ts.dt.normalize()
    if grain == "weekly":  # Monday 00:00 of each date's ISO week (Mon–Sun inclusive)
        return ts.dt.normalize() - pd.to_timedelta(ts.dt.weekday, unit="D")
    return ts.dt.to_period("M").dt.start_time


def period_label(dt, grain):
    """Timestamp -> display label. daily/weekly -> 'YYYY-MM-DD' (week = its
    Monday); monthly -> 'YYYY-MM'."""
    if pd.isna(dt):
        return ""
    return dt.strftime("%Y-%m" if grain == "monthly" else "%Y-%m-%d")
