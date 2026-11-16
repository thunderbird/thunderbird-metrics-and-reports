---
layout: base
title: HOURLY: Thunderbird Desktop — Support Spike Report
---

# HOURLY: Thunderbird Desktop — Support Spike Report

_Generated 2026-11-09 04:00 … 2026-11-16 03:00 · **hourly** grain · trailing 168 hours · 220 questions · no AI (regex + traditional stats)_

- **Volume:** 220 questions, 1.3/hour avg
- **Answered (non-creator):** 172/220 (78%)
- **First-answer time (median):** 1.7h (p25 0.5h / p75 5.1h)
- **Total volume trend:** `▁▃▁▁▁▃▃▃▂▅▂▃▅▇▂▂▅▃▁▂▂▁▂▂▂▃▂▂▃▃▅▁▂▃▃▅▂▃▂▁▁▂▅▂▁▁▁▁▁▂▂▂▁▂▃▃▃▅▃▇▃▃▁▃▃▃▇▂▁▅▁▁▁▃▃▂▁▃▂▂▁▂▃▃▂▅▂▇▁▂▂▃▃▂▁▁▁▁▂▁▃▆▂▂▂▅▃▂▂▅▂▃▃▅▂▃▁▂▁▁▂▁▁▁▃▃▁▁▁▂▅▅▂▁▃▃▃▂▁▁▆▂▃▁▁▁▁▁▁▂▂▂▂▃▃▁▃█▁▃▁▃▃▁▃▂▂▃`

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

> 🔎 **Want a bump that is not listed below?** The sparklines here are static text. Open the [interactive explorer](explorer.html), pick a grain / version / cause, and **click any point** to read that period's questions — every period, not just the ones that cleared a threshold. Each spike row also links straight to its own bucket.

## 🚨 Engineering signal — version × cause spikes

Cause clusters over-represented in a specific Thunderbird version. The **Signal** column flags 🆕 **new** (cause never spiked before), ↗ **spreading** (known cause, new version), or ↻ **recurring** (chronic / seen before) — ranked new→spreading→recurring, then by **lift**. Click an ID to read it.


| Signal | Lift | When | Version × Cause | Qs | Served | Example questions | Trend |
|:--|---:|:--|:--|--:|:--|:--|:--|
| ↗ spreading | **7.1×** | 2026-11-15 | v153 × proto:smtp | 4 | ⚠️ 50% ans · 1.0h | [1618157](https://support.mozilla.org/questions/1618157 "I can receive Thunderbird message but I cannot send.") [1618242](https://support.mozilla.org/questions/1618242 "Email body is not showing in Thundirbird, but is visible in Apple Mail") [1618251](https://support.mozilla.org/questions/1618251 "Ogni volta che apro Thunderbird con più finestre aperte, si blocca con il menu v") [1618325](https://support.mozilla.org/questions/1618325 "New Outlook.com account – SMTP OAuth2 fails with “SmtpClientAuthentication is di") · [explore ↗](explorer.html#grain=daily&version=153&cause=proto:smtp&period=2026-11-15) | `▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁█▁▁▁▁▁` |
| ↗ spreading | **6.0×** | 2026-11-10 | v153 × m:gmail | 5 | ⚠️ 40% ans · 2.0h | [1617146](https://support.mozilla.org/questions/1617146 "I have one email that will not allow other emails to forward to it (inbox doesn'") [1617152](https://support.mozilla.org/questions/1617152 "Thunderbird cannot send emails from multiple accounts – SMTP timeouts and OAuth2") [1617168](https://support.mozilla.org/questions/1617168 "email scomparse") [1617219](https://support.mozilla.org/questions/1617219 "missing emails") [1617255](https://support.mozilla.org/questions/1617255 "su un PC non scarico più la posta di una casella Aruba e di una casella Gmail") · [explore ↗](explorer.html#grain=daily&version=153&cause=m:gmail&period=2026-11-10) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅█▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| ↗ spreading | **4.1×** | 2026-11-15 | v153 × proto:imap | 4 | 75% ans · 0.6h | [1618159](https://support.mozilla.org/questions/1618159 "Error on login to server") [1618251](https://support.mozilla.org/questions/1618251 "Ogni volta che apro Thunderbird con più finestre aperte, si blocca con il menu v") [1618320](https://support.mozilla.org/questions/1618320 "Reordering accounts in left pane; non-GUI method feasible?") [1618325](https://support.mozilla.org/questions/1618325 "New Outlook.com account – SMTP OAuth2 fails with “SmtpClientAuthentication is di") · [explore ↗](explorer.html#grain=daily&version=153&cause=proto:imap&period=2026-11-15) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁██▁▁▁▁▁` |

## 📮 Cause-level spikes — provider / protocol / AV / feature

Causes surging **regardless of version** vs a trailing day baseline — provider/ISP outages and protocol/AV issues. Not necessarily a Thunderbird bug, but worth a triage look. Ranked by magnitude.


| Rise | When | Cause | Qs | Served | Baseline | Example questions | Trend |
|---:|:--|:--|--:|:--|--:|:--|:--|
| **3.6×** | 2026-11-10 | m:gmail | 9 | 67% ans · 3.6h | 2.5 | [1617048](https://support.mozilla.org/questions/1617048 "How can I change to new email provider but keep all my folders?") [1617070](https://support.mozilla.org/questions/1617070 "Outlook.com IMAP OAuth2 fails with ＂User is authenticated but not connected＂") [1617146](https://support.mozilla.org/questions/1617146 "I have one email that will not allow other emails to forward to it (inbox doesn'") [1617152](https://support.mozilla.org/questions/1617152 "Thunderbird cannot send emails from multiple accounts – SMTP timeouts and OAuth2") [1617168](https://support.mozilla.org/questions/1617168 "email scomparse") [1617219](https://support.mozilla.org/questions/1617219 "missing emails") +3 · [explore ↗](explorer.html#grain=daily&cause=m:gmail&period=2026-11-10) | `▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▅█▁▁▅▅▅▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁█▁▁▁▁▅▅▁▁▁▁▁▁▁▅▁▁▁▅▁▅▁▅▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▅▁▁▁▁▁` |

## 📈 Trends

### Top versions

| Value | Total | Trend |
|:--|--:|:--|
| v153 | 60 | `▁▁▁▁▁▁▃▃▁▃▁▃▆▁▁▁▁▃▁▁▃▁▁▁▁▁▁▁▁▃█▁▁▃▁▃▃▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▃▃▁▃▃▁▆▃▃▆▃▁▁▁▁▁▁▁▁▁▁▃▁▁▁▃▃▃▆▁▃▁▁▁▁▃▁▁▁▁▁▁▁▁▃▁▁▁▁▁▁▁▃▁▁▁▆▁▁▁▁▁▁▁▁▁▁▁▃▁▁▁▁▃█▁▁▃▁▁▃▁▁▆▃▁▁▁▁▁▁▁▃▁▁▁▃▆▁▃▃▁▁▁▃▃▁▁▁▃▃` |
| v160 | 47 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▆▁▁▁▁▁▁▁▁▁▁▁▃▁▃▁▁█▁▁▁▁▁▁▆▁▁▁▁▁▁▃▁▁▁▁▁▁▁▁▁▁▁▁▃▆▁▃▃▃▁▃▁▁▁▁▃▁▃▃▃▁▁▆▆▁▁▃▃▃▁▃▁▆▁▃▁▁▁▁▁▁▃▃▁▁▁▁▃▁▃▁▃▃▁▁▁▁▆▁▃▁▁▁▁▁▁▁▁▃▁▁▁▁▃▆▁▁▁▁▁▁▃▃▁▁` |
| v159 | 45 | `▁▆▁▁▁▃▃▃▁▆▃▃▁█▃▁▆▃▁▁▁▁▃▁▁▃▃▃▆▃▁▁▁▃▁▃▁▆▁▁▁▁▃▃▁▁▁▁▁▁▁▃▁▃▃▃▁▁▁▁▃▃▁▁▁▃▁▁▁▃▁▁▁▁▁▁▁▁▁▁▁▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▆▁▁▁▃▁▁▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▁▁▁▁▁▁▁▁▁▁▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▁▁▁▁▁▁▁` |
| v140 | 14 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁█▁▁▁▁██▁▁▁█▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| v158 | 4 | `▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁` |
| v115 | 3 | `▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### Top mail providers

| Value | Total | Trend |
|:--|--:|:--|
| m:gmail | 30 | `▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▅█▁▁▅▅▅▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁█▁▁▁▁▅▅▁▁▁▁▁▁▁▅▁▁▁▅▁▅▁▅▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▅▁▁▁▁▁` |
| m:microsoftemail | 15 | `▁▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁█▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁` |
| m:spectrum | 13 | `▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▅▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▅▁` |
| m:yahooemail | 7 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| m:tonline | 3 | `▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| m:alice_it | 3 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### Top feature areas

| Value | Total | Trend |
|:--|--:|:--|
| feat:import_export | 9 | `▁▁▁▁▁▁▁▁▁▁▁▁█▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁` |
| feat:junk | 4 | `▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| feat:calendar | 3 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| feat:addressbook | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| feat:search | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| feat:filters | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### Top protocols

| Value | Total | Trend |
|:--|--:|:--|
| proto:imap | 26 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▅▁▁▅▁▁▅▁▁▁▁▁▁▁▅▁▁▁▁▁▁▅▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▅▁▁▅▁▅▁▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▅▅▁▁▅▁▁` |
| proto:smtp | 19 | `▁▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁▁▁▁▁▁▁▅▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁▁▅▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁█▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▅▁▁▅▁▁` |
| proto:pop | 14 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▅▁▅▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:oauth | 7 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁` |
| proto:carddav | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:caldav | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁` |

### Top antivirus

| Value | Total | Trend |
|:--|--:|:--|
| av:avast | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:bitdefender | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁` |
| av:defender | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:eset | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:mcafee | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:norton | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### OS mix (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| os:windows | 173 | `▁▃▁▁▁▂▂▃▂▃▂▃▅▆▁▁▅▂▁▂▂▁▁▂▁▂▂▂▂▃▅▁▂▃▃▅▂▂▂▁▁▂▅▁▁▁▁▁▁▂▂▂▁▂▂▂▂▅▃▃▃▃▁▂▃▃▇▂▁▅▁▁▁▂▂▁▁▃▂▂▁▁▃▂▂▅▂▆▁▁▂▃▂▂▁▁▁▁▁▁▃▃▂▁▂▅▃▂▂▃▂▃▃▅▁▃▁▂▁▁▁▁▁▁▃▃▁▁▁▂▃▃▂▁▃▃▃▁▁▁▆▂▃▁▁▁▁▁▁▂▁▂▂▃▁▁▂█▁▃▁▁▂▁▂▂▂▂` |
| os:macos | 25 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▅▁▅▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁▅▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▁▁▅▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▁▁▁▁█▁▁▅▁▁▅` |
| os:linux | 16 | `▁▁▁▁▁▅▅▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁█▁▁▁▅▁▁▁▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| os:android | 5 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁` |
| os:other | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### macOS releases (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| macos:tahoe | 4 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:catalina | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:ventura | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█` |

---

_Notes: spikes detected at **daily** grain (coarser grains catch slow-burn incidents a daily threshold misses — e.g. the March 2026 GMX provider outage). Volume / cause / OS trends span the full scraper history (2023-01+). **Version×cause covers 2026-02 onward** — the native `thunderbird_version` field ([Kitsune PR #7443](https://github.com/mozilla/kitsune/pull/7443)) is only populated from Feb 2026 (~27% → 85% by mid-2026), so earlier questions carry no version; cause-level spikes use all history. Thresholds calibrated on the post-backfill baseline. Full IDs per spike in `PROJECT1/desktop-daily-version-cause-spikes.csv` (version×cause) and `PROJECT1/desktop-daily-single-spikes.csv` (cause-level); full series in `PROJECT1/desktop-hourly-rollup.csv`._

_Last updated: 2026-11-16 04:40 UTC_
