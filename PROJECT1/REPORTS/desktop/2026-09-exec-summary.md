---
layout: base
title: "2026-09 exec summary: Thunderbird Desktop support spikes"
---

# September 2026 — Thunderbird Desktop support spikes

_Executive summary · **2026-09** · 5 questions · regenerated 2026-09-01 05:33 UTC · no AI (regex + traditional stats)_

## ✅ September 2026 was clean

**No spike cleared threshold at any grain.** No provider outage, no protocol surge, no AV breakage, and no release regression in September 2026.

> ⏳ **September 2026 is still in progress** — counts will grow.


| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| **version×cause** (release regressions) | 0 | 0 | 0 |
| **cause-level** (provider · protocol · AV) | 0 | 0 | 0 |

- **Volume:** 5 questions (`█` by day), 3 (60%) carry a cause tag
- **Answered (non-creator):** 0/5 (0%)
- **Release-adoption version spikes:** 1 (expected after a release — not incidents; collapsed below)

> ⏱ **Spike timing lags the incident.** A spike dates when users *piled in*, typically days after onset and often near resolution. Treat these as pain-cluster / triage signals, not real-time detection.

> 🔄 **This verdict is not frozen when the month ends.** Lift is measured against each cause's rate across all history, so later questions shift a closed month's expected values and rows can cross the threshold in either direction; answered-% keeps firming up as late answers land. That is why this page regenerates daily — and because each day's version is committed, `git log -p` on this file shows exactly how the verdict evolved.

<details markdown="1">
<summary><strong>🔍 Near misses (within ~25% of threshold)</strong> — 0 rows</summary>

Clusters the same detectors flag at **0.75× the thresholds** (i.e. within ~25% of firing) but which did NOT clear the real ones. Not incidents — context, so that “clean” is not confused with “quiet”.

_None — nothing came within ~25% of threshold either._

</details>

---

## All September 2026 detail

<details markdown="1">
<summary><strong>🚨 Version × cause spikes</strong> — 0 rows</summary>

_None._

</details>

<details markdown="1">
<summary><strong>📮 Cause-level spikes (provider · protocol · AV)</strong> — 0 rows</summary>

_None._

</details>

<details markdown="1">
<summary><strong>📦 Release-adoption version/OS spikes (not incidents)</strong> — 1 row</summary>

Version and OS are **filters, not causes** — a bare version spike is release adoption, not a regression. Listed for manual checking only.

| Grain | Rise | When | Dimension | Value | Qs | Baseline |
|:--|--:|:--|:--|:--|:--|--:|
| weekly | **46.0×** | 2026-08-31 | tb_version_major | 154 | 23 [1601271](https://support.mozilla.org/questions/1601271 "") [1601273](https://support.mozilla.org/questions/1601273 "") | 0.5 |

</details>

<details markdown="1">
<summary><strong>📈 September 2026 trends</strong> — 6 rows</summary>

**Top versions**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| v140 | 3 | `█` |
| v154 | 1 | `█` |
| v153 | 1 | `█` |

**Top mail providers**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| m:spectrum | 1 | `█` |
| m:icloud | 1 | `█` |

**Top protocols**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| proto:imap | 2 | `█` |
| proto:oauth | 1 | `█` |

**OS mix (filter dimension)**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| os:windows | 4 | `█` |
| os:other | 1 | `█` |


</details>

---

_Detectors run at daily / weekly / monthly grain; a weekly period is included when its week overlaps September 2026. Version×cause requires a known version, which is only populated from 2026-02 onward; cause-level uses all history. Full spike CSVs: `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`._
