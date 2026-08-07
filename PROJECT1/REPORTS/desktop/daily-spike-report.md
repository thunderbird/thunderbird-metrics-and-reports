---
layout: base
title: DAILY: Thunderbird Desktop — Support Spike Report
---

# DAILY: Thunderbird Desktop — Support Spike Report

_Generated 2026-05-10 … 2026-08-07 · **daily** grain · trailing 90 days · 2216 questions · no AI (regex + traditional stats)_

- **Volume:** 2216 questions, 24.6/day avg
- **Answered (non-creator):** 1804/2216 (81%)
- **First-answer time (median):** 3.3h (p25 1.0h / p75 11.9h)
- **Total volume trend:** `▅▆▇▅▅▇▆▅▅▅▆▇▅▄▅▆▇█▇▅▄▄▅▆▆▅▆▄▄▇▆▆▅▇▄▅▅▅▆▆▅▄▃▄▇▆▇▅▄▅▆▆▅▇▅▅▄▆▆▅▆▅▄▃▆▆▄▄▄▅▄▆▆▅▇▅▃▆▆▆▆▄▇▅▄▇▇▆▆▅`

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

## 🚨 Engineering signal — version × cause spikes

Cause clusters over-represented in a specific Thunderbird version. The **Signal** column flags 🆕 **new** (cause never spiked before), ↗ **spreading** (known cause, new version), or ↻ **recurring** (chronic / seen before) — ranked new→spreading→recurring, then by **lift**. Click an ID to read it.


| Signal | Lift | When | Version × Cause | Qs | Served | Trend | Example questions |
|:--|---:|:--|:--|--:|:--|:--|:--|
| 🆕 new | **23.9×** | 2026-06-09 | v151 × m:spectrum | 7 | 100% ans · 14.3h | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▂▁▁▁▁▂▁▁█▂▁▂▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁` | [1586383](https://support.mozilla.org/questions/1586383 "Email Accounts are highlighted RED") [1586405](https://support.mozilla.org/questions/1586405 "The certificate for mobile.charter.net does not come from a trusted source.") [1586446](https://support.mozilla.org/questions/1586446 "Unable to receive and send emails.") [1586481](https://support.mozilla.org/questions/1586481 "Connetion error, can't recieve emails") [1586486](https://support.mozilla.org/questions/1586486 "Thunderbird is showing Certificate for mobile.charter.net:993 does not come from") [1586494](https://support.mozilla.org/questions/1586494 "Mozilla TWC account failures") +1 |
| 🆕 new | **4.8×** | 2026-05-13 | v150 × proto:pop | 4 | ⚠️ 50% ans · 1.6h | `▃▁▃█▁▃▃▁▅▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▁▁▁▁▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` | [1581365](https://support.mozilla.org/questions/1581365 "Unable to add new account by POP") [1581376](https://support.mozilla.org/questions/1581376 "Authentification Error") [1581474](https://support.mozilla.org/questions/1581474 "Can’t send email via AT&T account") [1581477](https://support.mozilla.org/questions/1581477 "Unable to write email to mailbox") |
| 🆕 new | **4.7×** | 2026-06-30 | v152 × m:gmail | 4 | ⚠️ 50% ans · 2.5h | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▅▃▅▃▁▃▃▅▁▁▁█▅▆▅▆▅▃▅▃▅▆▃▁▁▃▁▁▁▁▁▁▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` | [1590372](https://support.mozilla.org/questions/1590372 "Urgent question: Wrong email group when I sign in coming up") [1590393](https://support.mozilla.org/questions/1590393 "Storende pop-up naar aanleiding van verwijderde google-account") [1590463](https://support.mozilla.org/questions/1590463 "Message not visible with no filter activated, all account are synchronized") [1590499](https://support.mozilla.org/questions/1590499 "archive Gmail to local storage　by Tb") |
| ↗ spreading | **4.5×** | 2026-06-29 | v152 × m:microsoftemail | 6 | 67% ans · 87.5h | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▂▁▂▂▂▂▃▂▁█▁▁▃▁▂▂▁▁▁▅▁▁▃▁▂▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁` | [1590178](https://support.mozilla.org/questions/1590178 "Adding 2nd outlook accound") [1590198](https://support.mozilla.org/questions/1590198 "Thunderbird emails have started to only show links and not the pictures within t") [1590208](https://support.mozilla.org/questions/1590208 "Can't connect to my live and outlook accounts since 2 weeks") [1590210](https://support.mozilla.org/questions/1590210 "TBird152.0  is not displaing HTML emails properly.") [1590301](https://support.mozilla.org/questions/1590301 "One-hour delay in the guest's meeting schedule (Atraso de uma hora na agenda do ") [1590307](https://support.mozilla.org/questions/1590307 "I got a message: ＂Authentication failure while connecting to server outlook.offi") |
| ↗ spreading | **3.0×** | 2026-08-04 | v153 × m:microsoftemail | 5 | 100% ans · 0.8h | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▄▁▁▁▂▄▂▁▂▁▁▂▇█▄▁▂` | [1596545](https://support.mozilla.org/questions/1596545 "Microsoft Outlook authentication failure.") [1596547](https://support.mozilla.org/questions/1596547 "I just had a fake prompt to add a password to a website mimicking Thunderbird") [1596591](https://support.mozilla.org/questions/1596591 "email not collegament to app thunderbird pc (email outlook)") [1596602](https://support.mozilla.org/questions/1596602 "Import from Outlook (M365) Mac OS to Thunderbird?") [1596606](https://support.mozilla.org/questions/1596606 "Cannot import contacts from outlook 2016") |
| ↻ recurring | **4.0×** | 2026-05-14 | v150 × m:microsoftemail | 4 | 100% ans · 5.5h | `▅▃▆▆█▃▆▁▅▃▅▃▁▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` | [1581591](https://support.mozilla.org/questions/1581591 "cannot send emails") [1581623](https://support.mozilla.org/questions/1581623 "can't add my new GMX account to Thunderbird") [1581643](https://support.mozilla.org/questions/1581643 "Thunderbird no envía correos con Outlook/Office365: error STARTTLS smtp.office36") [1581688](https://support.mozilla.org/questions/1581688 "Line throught emails.") |
| ↻ recurring | **3.3×** | 2026-05-12 | v150 × proto:imap | 5 | 100% ans · 2.7h | `▂▄█▂▁▂▁▁▅▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▂▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` | [1581184](https://support.mozilla.org/questions/1581184 "Problem Creating ＂New SubFolder＂ and ＂New Folder＂") [1581273](https://support.mozilla.org/questions/1581273 "Unable to add personal Hotmail/Outlook.com 🥹 _ Any help is appreciated❤️") [1581275](https://support.mozilla.org/questions/1581275 "Deleted mails are not removed from Gmail All Mails folder even though I transfer") [1581279](https://support.mozilla.org/questions/1581279 "Sending of the message failed. The message could not be sent because the connect") [1581355](https://support.mozilla.org/questions/1581355 "Migrating from Outlook Classic to IMAP Server, but unable to reconfigure to IMAP") |

## 📮 Cause-level spikes — provider / protocol / AV

Causes surging **regardless of version** vs a trailing day baseline — provider/ISP outages and protocol/AV issues. Not necessarily a Thunderbird bug, but worth a triage look. Ranked by magnitude.

_No cause-level spikes in this window at current thresholds._

## 📈 Trends

### Top versions

| Value | Total | Trend |
|:--|--:|:--|
| v140 | 531 | `▂▇▅▆▄█▅▄▇▇▅▄▅▂▅▄▇▆▆▆▆▄▅▇█▆▇▂▅▆▄▄▅▅▄▄▅▆▄▇▂▃▂▂▇▆▇▂▄▇▄▅▄▅▅▆▅▆▅▅▇▄▄▂▅▄▅▅▅▄▄▇▅▅▅▇▂▆▅▄▇▃▄▂▂▂▃▄▂▃` |
| v152 | 374 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▄▆▆▄▄▅▅▆▇█▆▃█▅▆█▄▆▃▆▇▆▆▄▂▃▆█▄▃▁▆▃▅▆▂▂▁▁▂▁▂▂▁▁▁▁▁▁▁▁▁` |
| v151 | 330 | `▁▁▁▁▁▁▁▁▁▂▅▅▄▄▄▄▆██▆▃▄▄▅▅▃▆▅▅▇█▆▅▅▃▄▄▅▂▁▂▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| v153 | 216 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▅▄▂▆▅▅▃▄▇▅▄██▆█▅` |
| v150 | 209 | `▅▅█▇▆█▅▅▅▅▅▃▃▁▂▃▃▁▂▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▂▁▁▁▁▁▁▂▁▂▁▂▁▁▁▁▁▁▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▂▁` |
| v115 | 60 | `▆▁▆▁▁▁▁▁▁▁▁▃▆▁▃▆▁▃▃▁▁▁▁▁█▃▁▁▆▃▁▆▁█▃▃▆▁▃▁█▃▁▁▆▃▁▁▁▁▁▆▆▃▁▁▁▃▁▁▆▁▁▃▁▃▁▁▆▁▁▁▁▁▆▁▁▁▁▁█▁▃▃▁▃▃▆▁▃` |

### Top mail providers

| Value | Total | Trend |
|:--|--:|:--|
| m:gmail | 187 | `▅▂▆▃▃▃▃▆▂▃▅▁▃▂▃▃▅▃█▅▂▁▅▃▃▁▁▁▃▅▁▅▃▂▁▂▅▂▃▁▃▃▃▂▂▃▅▅▂▆▁█▃▅▅▅▆▂▃▅▅▆▅▁▁▆▁▃▅▅▂▁▁▅▂█▂█▃▅▂▆▃▂▁▇▆▂▅▁` |
| m:microsoftemail | 160 | `▅▆▅▅▆▃▇▂▅▂▇▃▃▂▆▁▅▅▃▂▂▁▅▅▂▃▆▅▅▁▅▂▂▅▂▁▃▂▁▂▃▂▁▂▃▃▂▃▂▃█▃▁▅▃▂▂▁▁▃█▁▁▅▁▅▁▃▂▁▁▃▂▃▂▁▁▂▃▂▂▂▁▃▂▆▇▃▁▅` |
| m:yahooemail | 101 | `▂▂▄▅▂▂▅▁▂▁▂▂▅▂▁▁█▂▄▂▅▄▂▁▄▄▂▁▁▁▂▅▂▂▂▂▁▂▅▁▁▁▁▅▁▁▂▁▁▁▄▄▂▄▂▁▅▂▂▂▂▂▁▂▂▁▁▁▁▂▂▁▂▁▁▄▁▄▂▇▄▁▄▂▄▅▄▂▄▂` |
| m:spectrum | 40 | `▂▁▁▂▂▁▁▁▂▄▁▂▃▂▁▁▁▃▁▁▁▁▂▂▃▁▁▂▁▂█▅▁▂▁▁▁▂▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▂▂▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▂▁▁▁▁▁▁▂▁▁▂▁▁` |
| m:comcast | 39 | `▁▁▁▁▁▁▆▁▁▁▁▃▁▁▁▁█▃▁▃▃▁▃▁▃▁▁▁▃▁▁▃▁▃▃▁▃▃▆▁▁▁▁▆▁▁▃▁▁▁▁▃▁▃▁▃▁▁▁▃▆▁▁▁▁▃▃▁▁▃▁▁▁▁▃▁▁▃▁▁▃▁▆▃▃▁▁▃▁▁` |
| m:icloud | 18 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁█▁▁▅▅▁▁█▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▅▁▁▁▅▁▁▁▁▁█▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▅▁▁` |

### Top protocols

| Value | Total | Trend |
|:--|--:|:--|
| proto:imap | 164 | `▂▄█▂▁▄▄▂▅▄█▇▄▁▂▂▂▄▇▅▄▂█▇▁▅▁▂▅▂▁▁▄█▄▁▂▅▂▂▂▂▁▂▄▁▅▄▂▅▅▄▂▇▄▄▂▅▄▄█▁▁▄▂▄▂▂▂█▁▄▄▄▇▁▁▅▅▂▄▁▄▄▁▇▄▇▁▁` |
| proto:pop | 117 | `▂▁▂█▁▄▄▁▅▅▄▂▂▁▄▂▄▅▁▄▄▁▂▂▂▄▂▄▁▄▂▁▂▅▂▄▁▁▂▄▁▁▁▁▂▁▄▁▂▂▅▂▁▂▂▄▇▄▇▄▄▁▁▂▄▁▂▁▁▇▄▁▂▂▂▄▂▁▂▅▁▂▅▂▂▄▅▄▂▄` |
| proto:smtp | 88 | `▂▁▅▅▄▁▅▁▄▂▂▁▄▁▁▁▁▁▅▁▁▁▁▄▁▂▂▁▇▄▄▂▁▄▁▂▅▂▂▁▁▁▁▁▁▁▂▁▄▁▁▂▂▂▂▁▂▁▄▇█▁▁▂▁▂▄▂▁▁▂▂█▄▁▁▂▂▂▁▂▂▂▁▂▅▁▂▁▄` |
| proto:oauth | 47 | `▁▁█▁█▅▅▁▁▅█▁▁▅▁▁▅▅▅▁▅▁▁▅▁▁▅▁▅▅▅▁▁▁▁▁▅▅▅▅▅▅▁▁▁▁▅▁▁▁▁▁▁▅▁▅▁▁▁██▁▅▅▅▅▁▅▅▁▁▁█▁▁▁▅█▅█▁▁▁▁▁▅▁▁▁▁` |
| proto:caldav | 7 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:ews | 5 | `▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁` |

### Top antivirus

| Value | Total | Trend |
|:--|--:|:--|
| av:defender | 9 | `▁▁▁▁▁█▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁` |
| av:norton | 9 | `▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁▁▁▁▁▁▁` |
| av:avast | 6 | `▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁` |
| av:bitdefender | 6 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁` |
| av:mcafee | 4 | `▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:malwarebytes | 4 | `▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### OS mix (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| os:windows | 1771 | `▅▅▇▅▄▆▅▄▅▅▆▇▆▄▆▆███▆▄▄▄▆▆▆▆▄▄▇▇▇▅▆▃▅▄▆▆▆▆▄▃▃▇▆▇▆▃▄▆▆▅▆▅▅▄▆▇▅▇▅▄▃▆▆▄▅▄▅▄▇▆▅▇▆▂▆▆▅▆▄▇▄▃▇▆▅▆▄` |
| os:linux | 195 | `▃▆▂▅▁▅▆▃█▆▆▅▂▁▁▂▅▅▂▁▃▃▆▆▂▃▃▁▂▃▂▃▃▆▁▂▃▃▂▃▁▂▃▃▃█▇▂▃▆▃▃▇▅▆▁▁▁▃▃▂▂▁▁▅▂▁▃▅▂▂▃▁▅▇▁▃█▅▆▃▅▃▆▅▅▃▅▆▆` |
| os:macos | 152 | `▁▃▆▂▃▅▆▅▂▂▃▂▁▃▂▃▃▅▃▃▂▃▂▁▃▁▁▃▆▂▁▁▅▆▆▃▃▁▅▃▁▁▂▆▃▁▅▂▆▂▁▅▂▇▁▃▁▇▁▅▂▃▂▃▃▃▃▁▂▅▁▃▁▂▃▃▁▁▂▁▅▂▂▂▂▂▅█▅▃` |
| os:other | 29 | `▁▁▁▁▁▁▁▁▅▅▁▅▁▁▁▅▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▅▅▅█▁▁▁▁▁▁▁█▁▁▁▅▁▁▅▅▅█▅▁▁▁▁▁▅▁▁▁▅▁▅▁▁▁▁▁▅▁▅▁▁▅▁▁▁▁▁▅▁▅▁▁▅` |
| os:android | 17 | `█▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁█▁█▁██▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁█▁▁██▁` |

### macOS releases (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| macos:tahoe | 13 | `▁▁▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▅▁█▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▅▁▅` |
| macos:sequoia | 5 | `▁▁█▁█▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:monterey | 3 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁` |
| macos:sonoma | 3 | `▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█` |
| macos:high_sierra | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:sierra | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

---

_Notes: spikes detected at **daily** grain (coarser grains catch slow-burn incidents a daily threshold misses — e.g. the March 2026 GMX provider outage). Volume / cause / OS trends span the full scraper history (2023-01+). **Version×cause covers 2026-02 onward** — the native `thunderbird_version` field ([Kitsune PR #7443](https://github.com/mozilla/kitsune/pull/7443)) is only populated from Feb 2026 (~27% → 85% by mid-2026), so earlier questions carry no version; cause-level spikes use all history. Thresholds calibrated on the post-backfill baseline. Full IDs per spike in `PROJECT1/desktop-daily-version-cause-spikes.csv` (version×cause) and `PROJECT1/desktop-daily-single-spikes.csv` (cause-level); full series in `PROJECT1/desktop-daily-rollup.csv`._

_Last updated: 2026-08-07 16:50 UTC_
