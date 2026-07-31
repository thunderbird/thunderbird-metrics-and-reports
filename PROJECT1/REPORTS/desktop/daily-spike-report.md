---
layout: base
title: DAILY: Thunderbird Desktop — Support Spike Report
---

# DAILY: Thunderbird Desktop — Support Spike Report

_Generated 2026-05-03 … 2026-07-31 · **daily** grain · trailing 90 days · 2217 questions · no AI (regex + traditional stats)_

- **Volume:** 2217 questions, 24.6/day avg
- **Answered (non-creator):** 1822/2217 (82%)
- **First-answer time (median):** 3.4h (p25 1.0h / p75 12.0h)
- **Total volume trend:** `▄▅▇█▆▆▆▅▆▇▅▅▇▆▅▅▅▆▇▅▄▅▆▇█▇▅▄▄▅▆▆▅▆▄▄▇▆▆▅▇▄▅▅▅▆▆▅▄▃▄▇▆▇▅▄▅▆▆▅▇▅▅▄▆▆▅▆▅▄▃▆▆▄▄▄▅▄▆▆▅▇▅▃▆▆▆▆▄▅`

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

## 🚨 Engineering signal — version × cause spikes

Cause clusters over-represented in a specific Thunderbird version. The **Signal** column flags 🆕 **new** (cause never spiked before), ↗ **spreading** (known cause, new version), or ↻ **recurring** (chronic / seen before) — ranked new→spreading→recurring, then by **lift**. Click an ID to read it.


| Signal | Lift | When | Version × Cause | Qs | Served | Trend | Example questions |
|:--|---:|:--|:--|--:|:--|:--|:--|
| 🆕 new | **23.7×** | 2026-06-09 | v151 × m:spectrum | 7 | 100% ans · 14.3h | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▂▁▁▁▁▂▁▁█▂▁▂▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` | [1586383](https://support.mozilla.org/questions/1586383 "Email Accounts are highlighted RED") [1586405](https://support.mozilla.org/questions/1586405 "The certificate for mobile.charter.net does not come from a trusted source.") [1586446](https://support.mozilla.org/questions/1586446 "Unable to receive and send emails.") [1586481](https://support.mozilla.org/questions/1586481 "Connetion error, can't recieve emails") [1586486](https://support.mozilla.org/questions/1586486 "Thunderbird is showing Certificate for mobile.charter.net:993 does not come from") [1586494](https://support.mozilla.org/questions/1586494 "Mozilla TWC account failures") +1 |
| 🆕 new | **5.7×** | 2026-05-06 | v150 × proto:smtp | 6 | 100% ans · 1.0h | `▂▂▁█▁▁▂▂▁▅▃▂▁▂▁▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` | [1580225](https://support.mozilla.org/questions/1580225 "errore in Invio Posta") [1580247](https://support.mozilla.org/questions/1580247 "New Security Codes for vodafonemail.de, TLS Code not in Thunderbird available") [1580282](https://support.mozilla.org/questions/1580282 "messaggio di errore") [1580326](https://support.mozilla.org/questions/1580326 "I installed thunderbird 150 and get always an authentication error, when adding ") [1580352](https://support.mozilla.org/questions/1580352 "i can receive emails but cannot sent, password problem") [1580362](https://support.mozilla.org/questions/1580362 "cannot send out email to new Yahoo server and thunderbird does not ask for a pas") |
| 🆕 new | **4.9×** | 2026-05-13 | v150 × proto:pop | 4 | ⚠️ 50% ans · 1.6h | `▃▁▆▅▁▁▃▃▁▃█▁▃▃▁▅▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▁▁▁▁▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` | [1581365](https://support.mozilla.org/questions/1581365 "Unable to add new account by POP") [1581376](https://support.mozilla.org/questions/1581376 "Authentification Error") [1581474](https://support.mozilla.org/questions/1581474 "Can’t send email via AT&T account") [1581477](https://support.mozilla.org/questions/1581477 "Unable to write email to mailbox") |
| 🆕 new | **4.7×** | 2026-06-30 | v152 × m:gmail | 4 | ⚠️ 50% ans · 2.5h | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▅▃▅▃▁▃▃▅▁▁▁█▅▆▅▆▅▃▅▃▅▆▃▁▁▃▁▁▁▁▁▁▁▃▁▁▁▁▁▁▁▁▁` | [1590372](https://support.mozilla.org/questions/1590372 "Urgent question: Wrong email group when I sign in coming up") [1590393](https://support.mozilla.org/questions/1590393 "Storende pop-up naar aanleiding van verwijderde google-account") [1590463](https://support.mozilla.org/questions/1590463 "Message not visible with no filter activated, all account are synchronized") [1590499](https://support.mozilla.org/questions/1590499 "archive Gmail to local storage　by Tb") |
| 🆕 new | **3.1×** | 2026-05-05 | v150 × proto:imap | 5 | 80% ans · 6.8h | `▂▁█▄▅▁▂▂▄█▂▁▂▁▁▅▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▂▁▁▂▁▁▁▁▁▁▁▁▁▁` | [1579996](https://support.mozilla.org/questions/1579996 "Import more outlook accounts into the local folder in thunderbird") [1580004](https://support.mozilla.org/questions/1580004 "Add New Folder") [1580007](https://support.mozilla.org/questions/1580007 "Change pop 3 to IMAP") [1580121](https://support.mozilla.org/questions/1580121 "Stop downloading archived gmails to thunderbird POP") [1580187](https://support.mozilla.org/questions/1580187 "Adding hotmail (live, outlook) accounts to Thunderbird") |
| ↗ spreading | **4.6×** | 2026-06-29 | v152 × m:microsoftemail | 6 | 67% ans · 87.5h | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▂▁▂▂▂▂▃▂▁█▁▁▃▁▂▂▁▁▁▅▁▁▃▁▂▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁` | [1590178](https://support.mozilla.org/questions/1590178 "Adding 2nd outlook accound") [1590198](https://support.mozilla.org/questions/1590198 "Thunderbird emails have started to only show links and not the pictures within t") [1590208](https://support.mozilla.org/questions/1590208 "Can't connect to my live and outlook accounts since 2 weeks") [1590210](https://support.mozilla.org/questions/1590210 "TBird152.0  is not displaing HTML emails properly.") [1590301](https://support.mozilla.org/questions/1590301 "One-hour delay in the guest's meeting schedule (Atraso de uma hora na agenda do ") [1590307](https://support.mozilla.org/questions/1590307 "I got a message: ＂Authentication failure while connecting to server outlook.offi") |
| ↻ recurring | **4.0×** | 2026-05-14 | v150 × m:microsoftemail | 4 | 100% ans · 5.5h | `▃▃▅▆▁▃▁▅▃▆▆█▃▆▁▅▃▅▃▁▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` | [1581591](https://support.mozilla.org/questions/1581591 "cannot send emails") [1581623](https://support.mozilla.org/questions/1581623 "can't add my new GMX account to Thunderbird") [1581643](https://support.mozilla.org/questions/1581643 "Thunderbird no envía correos con Outlook/Office365: error STARTTLS smtp.office36") [1581688](https://support.mozilla.org/questions/1581688 "Line throught emails.") |
| ↻ recurring | **3.3×** | 2026-05-12 | v150 × proto:imap | 5 | 100% ans · 2.7h | `▂▁█▄▅▁▂▂▄█▂▁▂▁▁▅▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▂▁▁▂▁▁▁▁▁▁▁▁▁▁` | [1581184](https://support.mozilla.org/questions/1581184 "Problem Creating ＂New SubFolder＂ and ＂New Folder＂") [1581273](https://support.mozilla.org/questions/1581273 "Unable to add personal Hotmail/Outlook.com 🥹 _ Any help is appreciated❤️") [1581275](https://support.mozilla.org/questions/1581275 "Deleted mails are not removed from Gmail All Mails folder even though I transfer") [1581279](https://support.mozilla.org/questions/1581279 "Sending of the message failed. The message could not be sent because the connect") [1581355](https://support.mozilla.org/questions/1581355 "Migrating from Outlook Classic to IMAP Server, but unable to reconfigure to IMAP") |

## 📮 Cause-level spikes — provider / protocol / AV

Causes surging **regardless of version** vs a trailing day baseline — provider/ISP outages and protocol/AV issues. Not necessarily a Thunderbird bug, but worth a triage look. Ranked by magnitude.

_No cause-level spikes in this window at current thresholds._

## 📈 Trends

### Top versions

| Value | Total | Trend |
|:--|--:|:--|
| v140 | 557 | `▃▄▅▅▆▆▅▂▇▅▆▄█▅▄▇▇▅▄▅▂▅▄▇▆▆▆▆▄▅▇█▆▇▂▅▆▄▄▅▅▄▄▅▆▄▇▂▃▂▂▇▆▇▂▄▇▄▅▄▅▅▆▅▆▅▅▇▄▄▂▅▄▅▅▅▄▄▇▅▅▅▇▂▆▅▄▇▃▄` |
| v152 | 370 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▄▆▆▄▄▅▅▆▇█▆▃█▅▆█▄▆▃▆▇▆▆▄▂▃▆█▄▃▁▆▃▅▆▂▂▁▁▂▁▂▂▁▁` |
| v151 | 329 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▅▅▄▄▄▄▆██▆▃▄▄▅▅▃▆▅▅▇█▆▅▅▃▄▄▅▂▁▂▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| v150 | 302 | `▄▃▇█▅▅▅▅▄▇▆▅▇▅▄▅▅▄▂▂▁▂▂▃▁▂▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▂▁▁▁▁▁▁▂▁▂▁▂▁▁▁▁▁▁▂▂▂▂▁▁▁▁▁▁▁▁▁▁` |
| v153 | 97 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▆▅▃█▆▆▄▅▆` |
| v115 | 63 | `▃▆▃▆▃▁▆▆▁▆▁▁▁▁▁▁▁▁▃▆▁▃▆▁▃▃▁▁▁▁▁█▃▁▁▆▃▁▆▁█▃▃▆▁▃▁█▃▁▁▆▃▁▁▁▁▁▆▆▃▁▁▁▃▁▁▆▁▁▃▁▃▁▁▆▁▁▁▁▁▆▁▁▁▁▁█▁▃` |

### Top mail providers

| Value | Total | Trend |
|:--|--:|:--|
| m:gmail | 195 | `▃▂█▆▆▄▂▄▂▅▃▃▃▃▅▂▃▄▁▃▂▃▃▄▃▇▄▂▁▄▃▃▁▁▁▃▄▁▄▃▂▁▂▄▂▃▁▃▃▃▂▂▃▄▄▂▅▁▇▃▄▄▄▅▂▃▄▄▅▄▁▁▅▁▃▄▄▂▁▁▄▂▇▂▆▃▄▂▅▂` |
| m:microsoftemail | 160 | `▃▃▅▇▂▅▂▅▆▅▅▆▃▇▂▅▂▇▃▃▂▆▁▅▅▃▂▂▁▅▅▂▃▆▅▅▁▅▂▂▅▂▁▃▂▁▂▃▂▁▂▃▃▂▃▂▃█▃▁▅▃▂▂▁▁▃█▁▁▅▁▅▁▃▂▁▁▃▂▃▂▁▁▂▃▂▂▂▁` |
| m:yahooemail | 96 | `▁▁▄▄▄▁▄▂▂▄▅▂▂▅▁▂▁▂▂▅▂▁▁█▂▄▂▅▄▂▁▄▄▂▁▁▁▂▅▂▂▂▂▁▂▅▁▁▁▁▅▁▁▂▁▁▁▄▄▂▄▂▁▅▂▂▂▂▂▁▂▂▁▁▁▁▂▂▁▂▁▁▄▁▄▂▇▄▁▂` |
| m:spectrum | 44 | `▂▁▁▁▁▁▆▂▁▁▂▂▁▁▁▂▄▁▂▃▂▁▁▁▃▁▁▁▁▂▂▃▁▁▂▁▂█▅▁▂▁▁▁▂▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▂▂▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▂▁▁▁▁▁` |
| m:comcast | 37 | `▁▁▁▃▃▁▃▁▁▁▁▁▁▆▁▁▁▁▃▁▁▁▁█▃▁▃▃▁▃▁▃▁▁▁▃▁▁▃▁▃▃▁▃▃▆▁▁▁▁▆▁▁▃▁▁▁▁▃▁▃▁▃▁▁▁▃▆▁▁▁▁▃▃▁▁▃▁▁▁▁▃▁▁▃▁▁▃▁▁` |
| m:icloud | 19 | `▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁█▁▁▅▅▁▁█▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▅▁▁▁▅▁▁▁▁▁█▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▅▁▁▁▁▁` |

### Top protocols

| Value | Total | Trend |
|:--|--:|:--|
| proto:imap | 168 | `▃▁█▅▅▂▃▂▃▇▂▁▃▃▂▅▃▇▆▃▁▂▂▂▃▆▅▃▂▇▆▁▅▁▂▅▂▁▁▃▇▃▁▂▅▂▂▂▂▁▂▃▁▅▃▂▅▅▃▂▆▃▃▂▅▃▃▇▁▁▃▂▃▂▂▂▇▁▃▃▃▆▁▁▅▅▂▃▁▂` |
| proto:pop | 112 | `▂▁▇▄▁▁▂▂▁▂█▁▄▄▁▅▅▄▂▂▁▄▂▄▅▁▄▄▁▂▂▂▄▂▄▁▄▂▁▂▅▂▄▁▁▂▄▁▁▁▁▂▁▄▁▂▂▅▂▁▂▂▄▇▄▇▄▄▁▁▂▄▁▂▁▁▇▄▁▂▂▂▄▂▁▂▅▁▂▄` |
| proto:smtp | 95 | `▃▂▃█▁▁▆▂▁▅▅▃▁▅▁▃▂▂▁▃▁▁▁▁▁▅▁▁▁▁▃▁▂▂▁▆▃▃▂▁▃▁▂▅▂▂▁▁▁▁▁▁▁▂▁▃▁▁▂▂▂▂▁▂▁▃▆▇▁▁▂▁▂▃▂▁▁▂▂▇▃▁▁▂▂▂▁▂▂▁` |
| proto:oauth | 48 | `▁▅▅▁▁▁▁▁▁█▁█▅▅▁▁▅█▁▁▅▁▁▅▅▅▁▅▁▁▅▁▁▅▁▅▅▅▁▁▁▁▁▅▅▅▅▅▅▁▁▁▁▅▁▁▁▁▁▁▅▁▅▁▁▁██▁▅▅▅▅▁▅▅▁▁▁█▁▁▁▅█▅█▁▁▁` |
| proto:caldav | 7 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁` |
| proto:ews | 5 | `▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### Top antivirus

| Value | Total | Trend |
|:--|--:|:--|
| av:defender | 9 | `▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:norton | 8 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁` |
| av:bitdefender | 6 | `▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:avast | 5 | `▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:mcafee | 4 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁` |
| av:malwarebytes | 4 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁` |

### OS mix (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| os:windows | 1794 | `▄▅▇█▆▇▆▅▅▇▅▄▆▅▄▅▅▆▇▆▄▆▆██▇▅▄▄▄▅▆▅▆▄▄▇▇▇▅▆▃▅▄▅▆▆▆▄▃▃▇▅▇▆▃▄▆▆▄▆▄▅▄▅▇▅▇▄▄▃▆▆▄▄▄▅▄▇▆▄▇▆▂▅▆▅▅▄▅` |
| os:linux | 184 | `▂▅▃▂▃▃▂▃▆▂▅▁▅▆▃█▆▆▅▂▁▁▂▅▅▂▁▃▃▆▆▂▃▃▁▂▃▂▃▃▆▁▂▃▃▂▃▁▂▃▃▃█▇▂▃▆▃▃▇▅▆▁▁▁▃▃▂▂▁▁▅▂▁▃▅▂▂▃▁▅▇▁▃█▅▆▃▅▃` |
| os:macos | 146 | `▄▂▅▅▂▁▄▁▄▇▂▄▅▇▅▂▂▄▂▁▄▂▄▄▅▄▄▂▄▂▁▄▁▁▄▇▂▁▁▅▇▇▄▄▁▅▄▁▁▂▇▄▁▅▂▇▂▁▅▂█▁▄▁█▁▅▂▄▂▄▄▄▄▁▂▅▁▄▁▂▄▄▁▁▂▁▅▂▁` |
| os:other | 29 | `▁▅▁▁█▁▁▁▁▁▁▁▁▁▁▅▅▁▅▁▁▁▅▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▅▅▅█▁▁▁▁▁▁▁█▁▁▁▅▁▁▅▅▅█▅▁▁▁▁▁▅▁▁▁▅▁▅▁▁▁▁▁▅▁▅▁▁▅▁▁▁▁` |
| os:android | 17 | `█▁██▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁█▁█▁██▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁` |

### macOS releases (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| macos:tahoe | 11 | `▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▅▁█▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁` |
| macos:sequoia | 5 | `▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁` |
| macos:sonoma | 3 | `▁▁█▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:high_sierra | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:monterey | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁` |
| macos:sierra | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁` |

---

_Notes: spikes detected at **daily** grain (coarser grains catch slow-burn incidents a daily threshold misses — e.g. the March 2026 GMX provider outage). Volume / cause / OS trends span the full scraper history (2023-01+). **Version×cause covers 2026-02 onward** — the native `thunderbird_version` field ([Kitsune PR #7443](https://github.com/mozilla/kitsune/pull/7443)) is only populated from Feb 2026 (~27% → 85% by mid-2026), so earlier questions carry no version; cause-level spikes use all history. Thresholds calibrated on the post-backfill baseline. Full IDs per spike in `PROJECT1/desktop-daily-version-cause-spikes.csv` (version×cause) and `PROJECT1/desktop-daily-single-spikes.csv` (cause-level); full series in `PROJECT1/desktop-daily-rollup.csv`._

_Last updated: 2026-07-31 17:04 UTC_
