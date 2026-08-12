---
layout: base
title: DAILY: Thunderbird Desktop — Support Spike Report
---

# DAILY: Thunderbird Desktop — Support Spike Report

_Generated 2026-05-15 … 2026-08-12 · **daily** grain · trailing 90 days · 2224 questions · no AI (regex + traditional stats)_

- **Volume:** 2224 questions, 24.7/day avg
- **Answered (non-creator):** 1814/2224 (82%)
- **First-answer time (median):** 3.4h (p25 1.0h / p75 12.1h)
- **Total volume trend:** `▇▆▅▅▅▆▇▅▄▅▆▇█▇▅▄▄▅▆▆▅▆▄▄▇▆▆▅▇▄▅▅▅▆▆▅▄▃▄▇▆▇▅▄▅▆▆▅▇▅▅▄▆▆▅▆▅▄▃▆▆▄▄▄▅▄▆▆▅▇▅▃▆▆▆▆▄▇▅▄▇▇▆▇▇▇▄▆▄▄`

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

> 🔎 **Want a bump that is not listed below?** The sparklines here are static text. Open the [interactive explorer](explorer.html), pick a grain / version / cause, and **click any point** to read that period's questions — every period, not just the ones that cleared a threshold. Each spike row also links straight to its own bucket.

## 🚨 Engineering signal — version × cause spikes

Cause clusters over-represented in a specific Thunderbird version. The **Signal** column flags 🆕 **new** (cause never spiked before), ↗ **spreading** (known cause, new version), or ↻ **recurring** (chronic / seen before) — ranked new→spreading→recurring, then by **lift**. Click an ID to read it.


| Signal | Lift | When | Version × Cause | Qs | Served | Example questions | Trend |
|:--|---:|:--|:--|--:|:--|:--|:--|
| 🆕 new | **23.8×** | 2026-06-09 | v151 × m:spectrum | 7 | 100% ans · 14.3h | [1586383](https://support.mozilla.org/questions/1586383 "Email Accounts are highlighted RED") [1586405](https://support.mozilla.org/questions/1586405 "The certificate for mobile.charter.net does not come from a trusted source.") [1586446](https://support.mozilla.org/questions/1586446 "Unable to receive and send emails.") [1586481](https://support.mozilla.org/questions/1586481 "Connetion error, can't recieve emails") [1586486](https://support.mozilla.org/questions/1586486 "Thunderbird is showing Certificate for mobile.charter.net:993 does not come from") [1586494](https://support.mozilla.org/questions/1586494 "Mozilla TWC account failures") +1 · [explore ↗](explorer.html#grain=daily&version=151&cause=m:spectrum&period=2026-06-09) | `▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▂▁▁▁▁▂▁▁█▂▁▂▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁` |
| 🆕 new | **4.7×** | 2026-06-30 | v152 × m:gmail | 4 | ⚠️ 50% ans · 2.5h | [1590372](https://support.mozilla.org/questions/1590372 "Urgent question: Wrong email group when I sign in coming up") [1590393](https://support.mozilla.org/questions/1590393 "Storende pop-up naar aanleiding van verwijderde google-account") [1590463](https://support.mozilla.org/questions/1590463 "Message not visible with no filter activated, all account are synchronized") [1590499](https://support.mozilla.org/questions/1590499 "archive Gmail to local storage　by Tb") · [explore ↗](explorer.html#grain=daily&version=152&cause=m:gmail&period=2026-06-30) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▅▃▅▃▁▃▃▅▁▁▁█▅▆▅▆▅▃▅▃▅▆▃▁▁▃▁▁▁▁▁▁▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| ↗ spreading | **4.6×** | 2026-06-29 | v152 × m:microsoftemail | 6 | 67% ans · 87.5h | [1590178](https://support.mozilla.org/questions/1590178 "Adding 2nd outlook accound") [1590198](https://support.mozilla.org/questions/1590198 "Thunderbird emails have started to only show links and not the pictures within t") [1590208](https://support.mozilla.org/questions/1590208 "Can't connect to my live and outlook accounts since 2 weeks") [1590210](https://support.mozilla.org/questions/1590210 "TBird152.0  is not displaing HTML emails properly.") [1590301](https://support.mozilla.org/questions/1590301 "One-hour delay in the guest's meeting schedule (Atraso de uma hora na agenda do ") [1590307](https://support.mozilla.org/questions/1590307 "I got a message: ＂Authentication failure while connecting to server outlook.offi") · [explore ↗](explorer.html#grain=daily&version=152&cause=m:microsoftemail&period=2026-06-29) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▂▁▂▂▂▂▃▂▁█▁▁▃▁▂▂▁▁▁▅▁▁▃▁▂▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁` |
| ↗ spreading | **3.4×** | 2026-08-10 | v153 × proto:pop | 4 | 75% ans · 1.1h | [1597551](https://support.mozilla.org/questions/1597551 "Thunderbird POP stopped retrieving email from one mail box, No error message") [1597571](https://support.mozilla.org/questions/1597571 "Email collection over pop failed on one account, server settings rejected when I") [1597638](https://support.mozilla.org/questions/1597638 "How logging onto wowway with old password?") [1597683](https://support.mozilla.org/questions/1597683 "Hotmail personal account: IMAP OAuth2 works but SMTP OAuth2 fails with message: ") · [explore ↗](explorer.html#grain=daily&version=153&cause=proto:pop&period=2026-08-10) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▃▁▁▁▃▁▁▆▃▃▅▅▁▅▃▃▅█▁▁` |
| ↗ spreading | **3.1×** | 2026-08-04 | v153 × m:microsoftemail | 5 | 100% ans · 0.8h | [1596545](https://support.mozilla.org/questions/1596545 "Microsoft Outlook authentication failure.") [1596547](https://support.mozilla.org/questions/1596547 "I just had a fake prompt to add a password to a website mimicking Thunderbird") [1596591](https://support.mozilla.org/questions/1596591 "email not collegament to app thunderbird pc (email outlook)") [1596602](https://support.mozilla.org/questions/1596602 "Import from Outlook (M365) Mac OS to Thunderbird?") [1596606](https://support.mozilla.org/questions/1596606 "Cannot import contacts from outlook 2016") · [explore ↗](explorer.html#grain=daily&version=153&cause=m:microsoftemail&period=2026-08-04) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▄▁▁▁▂▄▂▁▂▁▁▂▇█▄▁▂▂▁▅▂▂` |

## 📮 Cause-level spikes — provider / protocol / AV

Causes surging **regardless of version** vs a trailing day baseline — provider/ISP outages and protocol/AV issues. Not necessarily a Thunderbird bug, but worth a triage look. Ranked by magnitude.

_No cause-level spikes in this window at current thresholds._

## 📈 Trends

### Top versions

| Value | Total | Trend |
|:--|--:|:--|
| v140 | 513 | `█▅▄▇▇▅▄▅▂▅▄▇▆▆▆▆▄▅▇█▆▇▂▅▆▄▄▅▅▄▄▅▆▄▇▂▃▂▂▇▆▇▂▄▇▄▅▄▅▅▆▅▆▅▅▇▄▄▂▅▄▅▅▅▄▄▇▅▅▅▇▂▆▅▄▇▃▄▂▂▂▃▄▂▃▄▂▃▃▂` |
| v152 | 375 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▄▆▆▄▄▅▅▆▇█▆▃█▅▆█▄▆▃▆▇▆▆▄▂▃▆█▄▃▁▆▃▅▆▂▂▁▁▂▁▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| v151 | 330 | `▁▁▁▁▂▅▅▄▄▄▄▆██▆▃▄▄▅▅▃▆▅▅▇█▆▅▅▃▄▄▅▂▁▂▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| v153 | 310 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▅▄▂▆▅▅▃▄▇▅▄█▇▆███▆█▅▅` |
| v150 | 150 | `█▅▅▅▅▅▃▃▁▂▃▃▁▂▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▂▁▁▁▁▁▁▂▁▂▁▂▁▁▁▁▁▁▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▂▁▃▁▁▁▁` |
| v115 | 60 | `▁▁▁▁▁▁▃▆▁▃▆▁▃▃▁▁▁▁▁█▃▁▁▆▃▁▆▁█▃▃▆▁▃▁█▃▁▁▆▃▁▁▁▁▁▆▆▃▁▁▁▃▁▁▆▁▁▃▁▃▁▁▆▁▁▁▁▁▆▁▁▁▁▁█▁▃▃▁▃▃▆▁▃▃▁█▁▁` |

### Top mail providers

| Value | Total | Trend |
|:--|--:|:--|
| m:gmail | 186 | `▃▃▆▂▃▅▁▃▂▃▃▅▃█▅▂▁▅▃▃▁▁▁▃▅▁▅▃▂▁▂▅▂▃▁▃▃▃▂▂▃▅▅▂▆▁█▃▅▅▅▆▂▃▅▅▆▅▁▁▆▁▃▅▅▂▁▁▅▂█▂█▃▅▂▆▃▂▁▇▆▂▆▂▆▁▅▁▃` |
| m:microsoftemail | 148 | `▃▇▂▅▂▇▃▃▂▆▁▅▅▃▂▂▁▅▅▂▃▆▅▅▁▅▂▂▅▂▁▃▂▁▂▃▂▁▂▃▃▂▃▂▃█▃▁▅▃▂▂▁▁▃█▁▁▅▁▅▁▃▂▁▁▃▂▃▂▁▁▂▃▂▂▂▁▃▂▆▇▃▁▃▂▁▅▂▂` |
| m:yahooemail | 108 | `▂▅▁▂▁▂▂▅▂▁▁█▂▄▂▅▄▂▁▄▄▂▁▁▁▂▅▂▂▂▂▁▂▅▁▁▁▁▅▁▁▂▁▁▁▄▄▂▄▂▁▅▂▂▂▂▂▁▂▂▁▁▁▁▂▂▁▂▁▁▄▁▄▂▇▄▁▄▂▄▅▄▂▄▂▅▄▇▇▄` |
| m:comcast | 39 | `▁▆▁▁▁▁▃▁▁▁▁█▃▁▃▃▁▃▁▃▁▁▁▃▁▁▃▁▃▃▁▃▃▆▁▁▁▁▆▁▁▃▁▁▁▁▃▁▃▁▃▁▁▁▃▆▁▁▁▁▃▃▁▁▃▁▁▁▁▃▁▁▃▁▁▃▁▆▃▃▁▁▃▁▁▁▁▁▁▁` |
| m:spectrum | 39 | `▁▁▁▂▄▁▂▃▂▁▁▁▃▁▁▁▁▂▂▃▁▁▂▁▂█▅▁▂▁▁▁▂▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▂▂▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▂▁▁▁▁▁▁▂▁▁▂▁▁▂▂▁▁▁` |
| m:icloud | 19 | `▁▁▁▁▁▁▁▁▁▁▅▁▁▁█▁▁▅▅▁▁█▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▅▁▁▁▅▁▁▁▁▁█▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁` |

### Top protocols

| Value | Total | Trend |
|:--|--:|:--|
| proto:imap | 165 | `▃▃▂▅▃▇▆▃▁▂▂▂▃▆▅▃▂▇▆▁▅▁▂▅▂▁▁▃▇▃▁▂▅▂▂▂▂▁▂▃▁▅▃▂▅▅▃▂▆▃▃▂▅▃▃▇▁▁▃▂▃▂▂▂▇▁▃▃▃▆▁▁▅▅▂▃▁▃▃▁▆▃▅▁▁▃▃█▂▁` |
| proto:pop | 119 | `▅▅▁▆▆▅▃▃▁▅▃▅▆▁▅▅▁▃▃▃▅▃▅▁▅▃▁▃▆▃▅▁▁▃▅▁▁▁▁▃▁▅▁▃▃▆▃▁▃▃▅█▅█▅▅▁▁▃▅▁▃▁▁█▅▁▃▃▃▅▃▁▃▆▁▃▆▃▃▅▆▃▅▅▆▅█▁▁` |
| proto:smtp | 83 | `▁▅▁▄▂▂▁▄▁▁▁▁▁▅▁▁▁▁▄▁▂▂▁▇▄▄▂▁▄▁▂▅▂▂▁▁▁▁▁▁▁▂▁▄▁▁▂▂▂▂▁▂▁▄▇█▁▁▂▁▂▄▂▁▁▂▂█▄▁▁▂▂▂▁▂▂▂▁▂▅▁▂▁▂▂▂▄▁▂` |
| proto:oauth | 49 | `▃▃▁▁▃▆▁▁▃▁▁▃▃▃▁▃▁▁▃▁▁▃▁▃▃▃▁▁▁▁▁▃▃▃▃▃▃▁▁▁▁▃▁▁▁▁▁▁▃▁▃▁▁▁▆▆▁▃▃▃▃▁▃▃▁▁▁▆▁▁▁▃▆▃▆▁▁▁▁▁▃▁▁▁▁▆▁█▃▁` |
| proto:caldav | 7 | `▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:ews | 6 | `▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁█▁▁▁▁` |

### Top antivirus

| Value | Total | Trend |
|:--|--:|:--|
| av:defender | 9 | `█▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:norton | 9 | `▁▁▁▁█▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:bitdefender | 7 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▁▁` |
| av:avast | 5 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁` |
| av:mcafee | 4 | `▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:malwarebytes | 4 | `▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### OS mix (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| os:windows | 1770 | `▆▅▄▅▅▆▇▆▄▆▆███▆▄▄▄▆▆▆▆▄▄▇▇▇▅▆▃▅▄▆▆▆▆▄▃▃▇▆▇▆▃▄▆▆▅▆▅▅▄▆▇▅▇▅▄▃▆▆▄▅▄▅▄▇▆▅▇▆▂▆▆▅▆▄▇▄▃▇▆▅▆▅▆▅▆▃▄` |
| os:linux | 205 | `▃▄▂▅▄▄▃▂▁▁▂▃▃▂▁▂▂▄▄▂▂▂▁▂▂▂▂▂▄▁▂▂▂▂▂▁▂▂▂▂▅▅▂▂▄▂▂▅▃▄▁▁▁▂▂▂▂▁▁▃▂▁▂▃▂▂▂▁▃▅▁▂▅▃▄▂▃▂▄▃▃▂▃▄█▅▁▃▄▂` |
| os:macos | 152 | `▅▆▅▂▂▃▂▁▃▂▃▃▅▃▃▂▃▂▁▃▁▁▃▆▂▁▁▅▆▆▃▃▁▅▃▁▁▂▆▃▁▅▂▆▂▁▅▂▇▁▃▁▇▁▅▂▃▂▃▃▃▃▁▂▅▁▃▁▂▃▃▁▁▂▁▅▂▂▂▂▂▅█▅▃▃▃▂▅▂` |
| os:other | 30 | `▁▁▁▅▅▁▅▁▁▁▅▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▅▅▅█▁▁▁▁▁▁▁█▁▁▁▅▁▁▅▅▅█▅▁▁▁▁▁▅▁▁▁▅▁▅▁▁▁▁▁▅▁▅▁▁▅▁▁▁▁▁▅▁▅▁▁█▁▁▁▁▁` |
| os:android | 18 | `▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▅▁▅▁▅▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▅▁▁▁▅▁█▁▁▅▁` |

### macOS releases (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| macos:tahoe | 12 | `▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▅▁█▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▅▁▅▁▁▁▁▁` |
| macos:monterey | 4 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁█▁▁▁` |
| macos:sequoia | 3 | `▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:sonoma | 3 | `▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁` |
| macos:high_sierra | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:sierra | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

---

_Notes: spikes detected at **daily** grain (coarser grains catch slow-burn incidents a daily threshold misses — e.g. the March 2026 GMX provider outage). Volume / cause / OS trends span the full scraper history (2023-01+). **Version×cause covers 2026-02 onward** — the native `thunderbird_version` field ([Kitsune PR #7443](https://github.com/mozilla/kitsune/pull/7443)) is only populated from Feb 2026 (~27% → 85% by mid-2026), so earlier questions carry no version; cause-level spikes use all history. Thresholds calibrated on the post-backfill baseline. Full IDs per spike in `PROJECT1/desktop-daily-version-cause-spikes.csv` (version×cause) and `PROJECT1/desktop-daily-single-spikes.csv` (cause-level); full series in `PROJECT1/desktop-daily-rollup.csv`._

_Last updated: 2026-08-12 16:50 UTC_
