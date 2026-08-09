---
layout: base
title: HOURLY: Thunderbird Desktop — Support Spike Report
---

# HOURLY: Thunderbird Desktop — Support Spike Report

_Generated 2026-08-01 16:00 … 2026-08-08 15:00 · **hourly** grain · trailing 168 hours · 198 questions · no AI (regex + traditional stats)_

- **Volume:** 198 questions, 1.2/hour avg
- **Answered (non-creator):** 141/198 (71%)
- **First-answer time (median):** 2.4h (p25 0.9h / p75 6.7h)
- **Total volume trend:** `▁▂▇▁▄▂▂▄▁▁▁▂▁▁▂▁▁▂▁▂▂▁▁▁▁▁▂▁▅▄▂▄▁▂▁▂▄▁▄▄▄▁▁▄▂▂█▄▄▄▂▂▂▄▅▁▄▁▂▁▁▁▂▄▂▁▂▁▂▇▇▂▄▁▄▂▄█▂▂▄▂▂▁▅▁▁▁▁▅▂▄▁▂▂▇▂▄▄▂▅▁▁▁▂▄▁▂▁▁▁▁▅▄▄▄▂▄▁▂▂▄▂▅▄▁▂▄▂▄▂▁▂▁▁▂▅▁▂▂▂▇▄▇▄▁▁▇▂▂▄▄▂▅▂▄▂▁▂▂▂▄▁▁▁▂▂▄`

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

> 🔎 **Want a bump that is not listed below?** The sparklines here are static text. Open the [interactive explorer](explorer.html), pick a grain / version / cause, and **click any point** to read that period's questions — every period, not just the ones that cleared a threshold. Each spike row also links straight to its own bucket.

## 🚨 Engineering signal — version × cause spikes

Cause clusters over-represented in a specific Thunderbird version. The **Signal** column flags 🆕 **new** (cause never spiked before), ↗ **spreading** (known cause, new version), or ↻ **recurring** (chronic / seen before) — ranked new→spreading→recurring, then by **lift**. Click an ID to read it.


| Signal | Lift | When | Version × Cause | Qs | Served | Example questions | Trend |
|:--|---:|:--|:--|--:|:--|:--|:--|
| ↗ spreading | **3.0×** | 2026-08-04 | v153 × m:microsoftemail | 5 | 100% ans · 0.8h | [1596545](https://support.mozilla.org/questions/1596545 "Microsoft Outlook authentication failure.") [1596547](https://support.mozilla.org/questions/1596547 "I just had a fake prompt to add a password to a website mimicking Thunderbird") [1596591](https://support.mozilla.org/questions/1596591 "email not collegament to app thunderbird pc (email outlook)") [1596602](https://support.mozilla.org/questions/1596602 "Import from Outlook (M365) Mac OS to Thunderbird?") [1596606](https://support.mozilla.org/questions/1596606 "Cannot import contacts from outlook 2016") · [explore ↗](explorer.html#grain=daily&version=153&cause=m:microsoftemail&period=2026-08-04) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▅▅▁▁▁▁▁▅▁▁▁▁▁▁▁▅▅▁▁▁▁▁▅█▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

## 📮 Cause-level spikes — provider / protocol / AV

Causes surging **regardless of version** vs a trailing day baseline — provider/ISP outages and protocol/AV issues. Not necessarily a Thunderbird bug, but worth a triage look. Ranked by magnitude.

_No cause-level spikes in this window at current thresholds._

## 📈 Trends

### Top versions

| Value | Total | Trend |
|:--|--:|:--|
| v153 | 125 | `▁▁█▁▅▁▃▃▁▁▁▃▁▁▃▁▁▁▁▃▃▁▁▁▁▁▃▁▃▅▃▃▁▃▁▁▃▁▁▅▃▁▁▅▃▁█▅▅▅▃▁▁▁▅▁▁▁▁▁▁▁▃▅▃▁▃▁▃▆█▃▁▁▁▃▃▆▃▁▁▁▁▁▆▁▁▁▁▅▃▅▁▁▃▃▁▃▅▁▅▁▁▁▁▃▁▃▁▁▁▁▅▅▃▃▃▅▁▃▃▃▃▁▅▁▃▅▁▃▃▁▃▁▁▃▃▁▃▃▁▃▅▅▃▁▁▅▃▃▅▅▃▅▃▁▃▁▁▃▃▃▁▁▁▁▃▃` |
| v140 | 17 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁█▁▁▁▁▁██▁▁█▁▁▁▁█▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁█▁▁` |
| v115 | 7 | `▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅` |
| v150 | 7 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁` |
| v152 | 3 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| v151 | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### Top mail providers

| Value | Total | Trend |
|:--|--:|:--|
| m:gmail | 15 | `▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁█▁▁▁▁██▁▁▁█▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| m:yahooemail | 14 | `▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| m:microsoftemail | 14 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▅▅▁▁▁▁▁▅▁▁▁▁▁▁▁▅▅▁▁▁▁▁▅█▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| m:comcast | 3 | `▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| m:spectrum | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| m:alice_it | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### Top protocols

| Value | Total | Trend |
|:--|--:|:--|
| proto:imap | 12 | `▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁█▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁█▁▁▁▁▁█▁█▁▁▁▁█▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:pop | 12 | `▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:smtp | 6 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:oauth | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### Top antivirus

| Value | Total | Trend |
|:--|--:|:--|
| av:avast | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:bitdefender | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### OS mix (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| os:windows | 133 | `▁▁▇▁▁▂▂▂▁▁▁▁▁▁▁▁▁▂▁▂▁▁▁▁▁▁▂▁▂▄▂▂▁▂▁▂▄▁▂▄▄▁▁▄▂▂█▄▂▄▂▁▂▄▄▁▄▁▂▁▁▁▁▄▂▁▂▁▂▅▄▁▂▁▄▂▄▇▂▂▁▂▁▁▂▁▁▁▁▄▂▂▁▂▁▄▂▂▄▂▅▁▁▁▂▄▁▂▁▁▁▁▄▄▁▄▂▄▁▁▂▄▂▄▂▁▂▁▁▄▂▁▂▁▁▁▄▁▂▂▁▅▁▄▄▁▁▄▂▁▂▁▁▁▁▁▂▁▁▂▂▄▁▁▁▂▁▂` |
| os:linux | 30 | `▁▁▁▁▅▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▅█▅▁▁▁▅▁▅▅█▅█▅▁▁▁▁▁▁▁▁▁▁▁▁▅` |
| os:macos | 19 | `▁▁▁▁▅▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▁▁▁▁▅▁▁█▁▁▁▅▁▁▁▁▁▁▅▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▁` |
| os:android | 5 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁` |
| os:other | 4 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### macOS releases (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| macos:tahoe | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:monterey | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:sonoma | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

---

_Notes: spikes detected at **daily** grain (coarser grains catch slow-burn incidents a daily threshold misses — e.g. the March 2026 GMX provider outage). Volume / cause / OS trends span the full scraper history (2023-01+). **Version×cause covers 2026-02 onward** — the native `thunderbird_version` field ([Kitsune PR #7443](https://github.com/mozilla/kitsune/pull/7443)) is only populated from Feb 2026 (~27% → 85% by mid-2026), so earlier questions carry no version; cause-level spikes use all history. Thresholds calibrated on the post-backfill baseline. Full IDs per spike in `PROJECT1/desktop-daily-version-cause-spikes.csv` (version×cause) and `PROJECT1/desktop-daily-single-spikes.csv` (cause-level); full series in `PROJECT1/desktop-hourly-rollup.csv`._

_Last updated: 2026-08-08 23:59 UTC_
