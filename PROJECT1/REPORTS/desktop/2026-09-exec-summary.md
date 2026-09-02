---
layout: base
title: "2026-09 exec summary: Thunderbird Desktop support spikes"
---

# September 2026 — Thunderbird Desktop support spikes

_Executive summary · **2026-09** · 41 questions · regenerated 2026-09-02 05:35 UTC · no AI (regex + traditional stats)_

## ✅ September 2026 was clean

**No spike cleared threshold at any grain.** No provider outage, no protocol surge, no AV breakage, and no release regression in September 2026.

> ⏳ **September 2026 is still in progress** — counts will grow.


| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| **version×cause** (release regressions) | 0 | 0 | 0 |
| **cause-level** (provider · protocol · AV) | 0 | 0 | 0 |

- **Volume:** 41 questions (`█▂` by day), 14 (34%) carry a cause tag
- **Answered (non-creator):** 25/41 (61%) · median first answer 1.2h
- **Release-adoption version spikes:** 3 (expected after a release — not incidents; collapsed below)

> ⏱ **Spike timing lags the incident.** A spike dates when users *piled in*, typically days after onset and often near resolution. Treat these as pain-cluster / triage signals, not real-time detection.

> 🔄 **This verdict is not frozen when the month ends.** Lift is measured against each cause's rate across all history, so later questions shift a closed month's expected values and rows can cross the threshold in either direction; answered-% keeps firming up as late answers land. That is why this page regenerates daily — and because each day's version is committed, `git log -p` on this file shows exactly how the verdict evolved.

<details markdown="1">
<summary><strong>🔍 Near misses (within ~25% of threshold)</strong> — 1 row</summary>

Clusters the same detectors flag at **0.75× the thresholds** (i.e. within ~25% of firing) but which did NOT clear the real ones. Not incidents — context, so that “clean” is not confused with “quiet”.

**Version × cause**

| Grain | Lift | When | Version × Cause | Qs | Served | Example questions |
|:--|--:|:--|:--|--:|:--|:--|
| daily | 2.7× | 2026-09-01 | v154 × proto:imap | 4 | ⚠️ 25% ans · 7.2h | [1601433](https://support.mozilla.org/questions/1601433 "Uable to add new account over one that's been hacked.") [1601534](https://support.mozilla.org/questions/1601534 "Thunderbird on Win11 will not send or receive emails") [1601629](https://support.mozilla.org/questions/1601629 "Login to inbound server fails") [1601635](https://support.mozilla.org/questions/1601635 "missing email from flders") |


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
<summary><strong>📦 Release-adoption version/OS spikes (not incidents)</strong> — 3 rows</summary>

Version and OS are **filters, not causes** — a bare version spike is release adoption, not a regression. Listed for manual checking only.

| Grain | Rise | When | Dimension | Value | Qs | Baseline |
|:--|--:|:--|:--|:--|:--|--:|
| daily | **11.3×** | 2026-09-01 | tb_version_major | 154 | 17 [1601433](https://support.mozilla.org/questions/1601433 "Uable to add new account over one that's been hacked.") [1601478](https://support.mozilla.org/questions/1601478 "Thunderbird non si carica su Apple Tahoe 26.6.2") | 1.5 |
| monthly | **new** | 2026-09 | tb_version_major | 154 | 18 [1601433](https://support.mozilla.org/questions/1601433 "Uable to add new account over one that's been hacked.") [1601478](https://support.mozilla.org/questions/1601478 "Thunderbird non si carica su Apple Tahoe 26.6.2") | 0.0 |
| weekly | **80.0×** | 2026-08-31 | tb_version_major | 154 | 40 [1601271](https://support.mozilla.org/questions/1601271 "") [1601273](https://support.mozilla.org/questions/1601273 "") | 0.5 |

</details>

<details markdown="1">
<summary><strong>📈 September 2026 trends</strong> — 6 rows</summary>

**Top versions**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| v154 | 18 | `█▁` |
| v153 | 4 | `█▃` |
| v140 | 4 | `█▁` |
| v155 | 1 | `▁█` |

**Top mail providers**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| m:gmail | 3 | `█▅` |
| m:spectrum | 2 | `█▁` |
| m:yahooemail | 2 | `██` |
| m:icloud | 1 | `█▁` |
| m:virginmedia | 1 | `█▁` |
| m:microsoftemail | 1 | `█▁` |

**Top protocols**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| proto:imap | 6 | `█▂` |
| proto:oauth | 2 | `█▁` |
| proto:smtp | 2 | `█▁` |
| proto:pop | 1 | `█▁` |

**Top antivirus**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| av:avast | 1 | `█▁` |
| av:malwarebytes | 1 | `█▁` |
| av:norton | 1 | `█▁` |

**OS mix (filter dimension)**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| os:windows | 32 | `█▂` |
| os:other | 3 | `█▁` |
| os:macos | 2 | `█▁` |
| os:android | 2 | `██` |

**macOS releases (filter dimension)**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| macos:tahoe | 2 | `█▁` |


</details>

---

_Detectors run at daily / weekly / monthly grain; a weekly period is included when its week overlaps September 2026. Version×cause requires a known version, which is only populated from 2026-02 onward; cause-level uses all history. Full spike CSVs: `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`._
