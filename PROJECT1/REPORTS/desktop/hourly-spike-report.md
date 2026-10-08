---
layout: base
title: HOURLY: Thunderbird Desktop — Support Spike Report
---

# HOURLY: Thunderbird Desktop — Support Spike Report

_Generated 2026-10-01 17:00 … 2026-10-08 16:00 · **hourly** grain · trailing 168 hours · 335 questions · no AI (regex + traditional stats)_

- **Volume:** 335 questions, 2.0/hour avg
- **Answered (non-creator):** 229/335 (68%)
- **First-answer time (median):** 2.2h (p25 0.6h / p75 9.1h)
- **Total volume trend:** `▆▅▇▂▃▁▂▁▂▂▂▂▁▃▁▂▃▄▃▄▄▃▂▃▅▅▃▂▂▃▁▅▂▃▁▁▁▃▁▁▁▂▁▂▄▃▅▃▃▂▁▃▄▃▁▄▁▂▁▁▁▁▃▁▄▁▂▂▄▃▂▄▃▃▂▄▂▂▂▂▂▃▁▂▁▂▄▁▄▆▂▄▅▅▅▅▃▄▅▂▂▂▅▁▂▃▃▂▂▄▃▁▇▂▂▂█▅▃▅▇▅▆▃▂▅▄▃▄▂▁▄▁▄▁▄▆▁▂▃▄▆▇▂▄▂▅▅▂▂▁▂▃▃▁▁▂▂▄▂▄▃▄▄▄▄▄▂`

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

> 🔎 **Want a bump that is not listed below?** The sparklines here are static text. Open the [interactive explorer](explorer.html), pick a grain / version / cause, and **click any point** to read that period's questions — every period, not just the ones that cleared a threshold. Each spike row also links straight to its own bucket.

## 🚨 Engineering signal — version × cause spikes

Cause clusters over-represented in a specific Thunderbird version. The **Signal** column flags 🆕 **new** (cause never spiked before), ↗ **spreading** (known cause, new version), or ↻ **recurring** (chronic / seen before) — ranked new→spreading→recurring, then by **lift**. Click an ID to read it.


| Signal | Lift | When | Version × Cause | Qs | Served | Example questions | Trend |
|:--|---:|:--|:--|--:|:--|:--|:--|
| 🆕 new | **102.6×** | 2026-10-06 | v140 × m:att | 4 | ⚠️ 50% ans · 1.4h | [1610156](https://support.mozilla.org/questions/1610156 "Gives error today - inbound.att.net certificate invalid !!??") [1610258](https://support.mozilla.org/questions/1610258 "The certificate for inbound.att.net does not come from a trusted source.") [1610259](https://support.mozilla.org/questions/1610259 "Why Thunderbird on Linux will no longer connect to att.net email with POP3.") [1610309](https://support.mozilla.org/questions/1610309 "AOL setup on MX Linux... fails authentication") · [explore ↗](explorer.html#grain=daily&version=140&cause=m:att&period=2026-10-06) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁█▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| 🆕 new | **8.5×** | 2026-10-04 | v157 × feat:attachments | 5 | 100% ans · 12.1h | [1609599](https://support.mozilla.org/questions/1609599 "na de laatste update kan ik geen bijlages toevoegen aan een e-mail") [1609601](https://support.mozilla.org/questions/1609601 "Change the app that opens email attachments") [1609642](https://support.mozilla.org/questions/1609642 "Attach button does not respond. Drag and Drop works. (bug2077590)") [1609643](https://support.mozilla.org/questions/1609643 "email beantwoorden, bijlage knop werkt niet") [1609719](https://support.mozilla.org/questions/1609719 "Unable to attach files to email") · [explore ↗](explorer.html#grain=daily&version=157&cause=feat:attachments&period=2026-10-04) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁█▅▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▅▁▅▅▁▅▁▁▁▅▁▁` |
| ↗ spreading | **12.9×** | 2026-10-05 | v153 × feat:attachments | 6 | 83% ans · 0.6h | [1609864](https://support.mozilla.org/questions/1609864 "allegati che non si possono più inserire nell'email") [1609904](https://support.mozilla.org/questions/1609904 "Unable to attach a document to a return email") [1609918](https://support.mozilla.org/questions/1609918 "allegati") [1609979](https://support.mozilla.org/questions/1609979 "why can't i attach files to sent email?") [1609986](https://support.mozilla.org/questions/1609986 "not launching file explorer to attach files") [1610030](https://support.mozilla.org/questions/1610030 "Thunderbird ＂Attach＂ button nor yellow attach bar reminder functioning.") · [explore ↗](explorer.html#grain=daily&version=153&cause=feat:attachments&period=2026-10-05) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▅▁▁▁▅▅▁▁▁▅▁▁▁▁▁▅▅▁▁▅▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁█▁▁▁▁▁▁▅▁▁▅▅▁▁▁▁▅▁▁▁▁▅▁▁▁▁` |
| ↻ recurring | **12.4×** | 2026-10-08 | v157 × feat:attachments | 5 | 100% ans · 1.1h | [1610602](https://support.mozilla.org/questions/1610602 "Nejde mi přidat do mailu příloha") [1610606](https://support.mozilla.org/questions/1610606 "The ＂Attach＂ button doesn't work when composing an email; it is not possible to ") [1610619](https://support.mozilla.org/questions/1610619 "Why can I no longer attach a file by clicking OPEN on the file location and why ") [1610638](https://support.mozilla.org/questions/1610638 "allegati mail") [1610666](https://support.mozilla.org/questions/1610666 "een blokkade om bijlagen te koppelen in email die ik verstuur") · [explore ↗](explorer.html#grain=daily&version=157&cause=feat:attachments&period=2026-10-08) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁█▅▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▅▁▅▅▁▅▁▁▁▅▁▁` |
| ↻ recurring | **11.7×** | 2026-10-08 | v153 × feat:attachments | 4 | 100% ans · 1.1h | [1610569](https://support.mozilla.org/questions/1610569 "The file picker does not open when you click the “Attach” button") [1610581](https://support.mozilla.org/questions/1610581 "Cannot attach files to emails in Thunderbird") [1610617](https://support.mozilla.org/questions/1610617 "Attachment function not accessible anymore") [1610652](https://support.mozilla.org/questions/1610652 "Attachment to an email is not possible with Tunderbird") · [explore ↗](explorer.html#grain=daily&version=153&cause=feat:attachments&period=2026-10-08) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▅▁▁▁▅▅▁▁▁▅▁▁▁▁▁▅▅▁▁▅▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁█▁▁▁▁▁▁▅▁▁▅▅▁▁▁▁▅▁▁▁▁▅▁▁▁▁` |
| ↻ recurring | **10.7×** | 2026-10-07 | v153 × feat:attachments | 5 | 100% ans · 2.0h | [1610392](https://support.mozilla.org/questions/1610392 "Recurring Issue with Attachment Button in Thunderbird Desktop") [1610416](https://support.mozilla.org/questions/1610416 "sinds de update 153.4.0esr van 05 oktober kan ik geen bijlagen meer koppelen aan") [1610444](https://support.mozilla.org/questions/1610444 "Thunderbird has stopped to include attachments via key. Only drag and drop funct") [1610449](https://support.mozilla.org/questions/1610449 "A problem with sending attachments with an email") [1610548](https://support.mozilla.org/questions/1610548 "Unable to add an attachment to the email being sent") · [explore ↗](explorer.html#grain=daily&version=153&cause=feat:attachments&period=2026-10-07) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▅▁▁▁▅▅▁▁▁▅▁▁▁▁▁▅▅▁▁▅▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁█▁▁▁▁▁▁▅▁▁▅▅▁▁▁▁▅▁▁▁▁▅▁▁▁▁` |
| ↻ recurring | **7.0×** | 2026-10-06 | v153 × feat:attachments | 5 | 100% ans · 1.2h | [1610087](https://support.mozilla.org/questions/1610087 "Email attachment - version 153.4.0esr") [1610100](https://support.mozilla.org/questions/1610100 "unable to attach desktop files to outgoing emails when attachment function activ") [1610118](https://support.mozilla.org/questions/1610118 "All of a sudden Thunderbird won't let me attach images") [1610206](https://support.mozilla.org/questions/1610206 "I have lost the attach file link since last up date") [1610244](https://support.mozilla.org/questions/1610244 "I can't add any attachments. The button doesn't work") · [explore ↗](explorer.html#grain=daily&version=153&cause=feat:attachments&period=2026-10-06) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▅▁▁▁▅▅▁▁▁▅▁▁▁▁▁▅▅▁▁▅▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁█▁▁▁▁▁▁▅▁▁▅▅▁▁▁▁▅▁▁▁▁▅▁▁▁▁` |
| ↻ recurring | **5.7×** | 2026-10-06 | v157 × feat:attachments | 5 | 100% ans · 0.9h | [1610097](https://support.mozilla.org/questions/1610097 "Since that last update I can no longer attach files to emails. Can You help?") [1610225](https://support.mozilla.org/questions/1610225 "Suddenly I can neither attach nor insert files into an outgoing email.") [1610267](https://support.mozilla.org/questions/1610267 "Attach File no longer Works as of 10/05 W11") [1610268](https://support.mozilla.org/questions/1610268 "Unable to attach files to emails (the ‘Attachments’ button does not respond)./ A") [1610276](https://support.mozilla.org/questions/1610276 "Attach button not working on new emails") · [explore ↗](explorer.html#grain=daily&version=157&cause=feat:attachments&period=2026-10-06) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁█▅▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▅▁▅▅▁▅▁▁▁▅▁▁` |
| ↻ recurring | **5.4×** | 2026-10-05 | v157 × feat:attachments | 4 | 100% ans · 5.4h | [1609825](https://support.mozilla.org/questions/1609825 "nach dem letzten Update kann ich keine Attachments versenden") [1609880](https://support.mozilla.org/questions/1609880 "I cannot add an attachment, when I press the attachment button nothing happens") [1609897](https://support.mozilla.org/questions/1609897 "The 'Attach' button does not respond to outgoing emails") [1609916](https://support.mozilla.org/questions/1609916 "Attach button dont work after updating to tb 157") · [explore ↗](explorer.html#grain=daily&version=157&cause=feat:attachments&period=2026-10-05) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁█▅▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▅▁▅▅▁▅▁▁▁▅▁▁` |

## 📮 Cause-level spikes — provider / protocol / AV / feature

Causes surging **regardless of version** vs a trailing day baseline — provider/ISP outages and protocol/AV issues. Not necessarily a Thunderbird bug, but worth a triage look. Ranked by magnitude.


| Rise | When | Cause | Qs | Served | Baseline | Example questions | Trend |
|---:|:--|:--|--:|:--|--:|:--|:--|
| **new** | 2026-10-08 | feat:attachments | 9 | 100% ans · 1.1h | 0.0 | [1610569](https://support.mozilla.org/questions/1610569 "The file picker does not open when you click the “Attach” button") [1610581](https://support.mozilla.org/questions/1610581 "Cannot attach files to emails in Thunderbird") [1610602](https://support.mozilla.org/questions/1610602 "Nejde mi přidat do mailu příloha") [1610606](https://support.mozilla.org/questions/1610606 "The ＂Attach＂ button doesn't work when composing an email; it is not possible to ") [1610617](https://support.mozilla.org/questions/1610617 "Attachment function not accessible anymore") [1610619](https://support.mozilla.org/questions/1610619 "Why can I no longer attach a file by clicking OPEN on the file location and why ") +3 · [explore ↗](explorer.html#grain=daily&cause=feat:attachments&period=2026-10-08) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▅▁▁▁▅▁▁▅▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▅▁█▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▅▅▅█▁▁▁▅▅▁▁▁▅▁▁▁▁▁▅█▁▁▅▁▁▁▁▁▁▅█▅█▅▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▅▁█▁▁▁▅▅▁▅▁▁▅▅▁▁▅▁█▅▁▅▁▅▁▅▁▁` |
| **new** | 2026-10-07 | feat:attachments | 8 | 100% ans · 1.3h | 0.0 | [1610366](https://support.mozilla.org/questions/1610366 "Thunderbird, button ＂attach＂") [1610392](https://support.mozilla.org/questions/1610392 "Recurring Issue with Attachment Button in Thunderbird Desktop") [1610416](https://support.mozilla.org/questions/1610416 "sinds de update 153.4.0esr van 05 oktober kan ik geen bijlagen meer koppelen aan") [1610444](https://support.mozilla.org/questions/1610444 "Thunderbird has stopped to include attachments via key. Only drag and drop funct") [1610449](https://support.mozilla.org/questions/1610449 "A problem with sending attachments with an email") [1610512](https://support.mozilla.org/questions/1610512 "Can't use Attachments like I have always done and need for work") +2 · [explore ↗](explorer.html#grain=daily&cause=feat:attachments&period=2026-10-07) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▅▁▁▁▅▁▁▅▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▅▁█▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▅▅▅█▁▁▁▅▅▁▁▁▅▁▁▁▁▁▅█▁▁▅▁▁▁▁▁▁▅█▅█▅▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▅▁█▁▁▁▅▅▁▅▁▁▅▅▁▁▅▁█▅▁▅▁▅▁▅▁▁` |
| **new** | 2026-10-06 | feat:attachments | 11 | 100% ans · 1.2h | 0.0 | [1610087](https://support.mozilla.org/questions/1610087 "Email attachment - version 153.4.0esr") [1610097](https://support.mozilla.org/questions/1610097 "Since that last update I can no longer attach files to emails. Can You help?") [1610100](https://support.mozilla.org/questions/1610100 "unable to attach desktop files to outgoing emails when attachment function activ") [1610118](https://support.mozilla.org/questions/1610118 "All of a sudden Thunderbird won't let me attach images") [1610206](https://support.mozilla.org/questions/1610206 "I have lost the attach file link since last up date") [1610216](https://support.mozilla.org/questions/1610216 "Thunerbird suddenly won't allow me to attach documents") +5 · [explore ↗](explorer.html#grain=daily&cause=feat:attachments&period=2026-10-06) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▅▁▁▁▅▁▁▅▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▅▁█▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▅▅▅█▁▁▁▅▅▁▁▁▅▁▁▁▁▁▅█▁▁▅▁▁▁▁▁▁▅█▅█▅▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▅▁█▁▁▁▅▅▁▅▁▁▅▅▁▁▅▁█▅▁▅▁▅▁▅▁▁` |
| **new** | 2026-10-06 | m:att | 11 | ⚠️ 36% ans · 1.5h | 0.0 | [1610152](https://support.mozilla.org/questions/1610152 "Certificate revoked for inbound.att.net?  What do we do?") [1610156](https://support.mozilla.org/questions/1610156 "Gives error today - inbound.att.net certificate invalid !!??") [1610171](https://support.mozilla.org/questions/1610171 "＂inbound.att.net (POP) .. certificate revoked＂? I can't download eMail!") [1610193](https://support.mozilla.org/questions/1610193 "certificate has been revoked. unable to receive email.") [1610212](https://support.mozilla.org/questions/1610212 "pop from Tbird says connection to server inbound.att.net has been reset") [1610258](https://support.mozilla.org/questions/1610258 "The certificate for inbound.att.net does not come from a trusted source.") +5 · [explore ↗](explorer.html#grain=daily&cause=m:att&period=2026-10-06) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▅▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▅█▁▁█▁▁███▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| **new** | 2026-10-05 | feat:attachments | 10 | 90% ans · 2.9h | 0.0 | [1609825](https://support.mozilla.org/questions/1609825 "nach dem letzten Update kann ich keine Attachments versenden") [1609864](https://support.mozilla.org/questions/1609864 "allegati che non si possono più inserire nell'email") [1609880](https://support.mozilla.org/questions/1609880 "I cannot add an attachment, when I press the attachment button nothing happens") [1609897](https://support.mozilla.org/questions/1609897 "The 'Attach' button does not respond to outgoing emails") [1609904](https://support.mozilla.org/questions/1609904 "Unable to attach a document to a return email") [1609916](https://support.mozilla.org/questions/1609916 "Attach button dont work after updating to tb 157") +4 · [explore ↗](explorer.html#grain=daily&cause=feat:attachments&period=2026-10-05) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▅▁▁▁▅▁▁▅▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▅▁█▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▅▅▅█▁▁▁▅▅▁▁▁▅▁▁▁▁▁▅█▁▁▅▁▁▁▁▁▁▅█▅█▅▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▅▁█▁▁▁▅▅▁▅▁▁▅▅▁▁▅▁█▅▁▅▁▅▁▅▁▁` |

## 📈 Trends

### Top versions

| Value | Total | Trend |
|:--|--:|:--|
| v157 | 145 | `▄▅▂▁▂▁▂▁▁▁▁▁▁▂▁▂▂▂▂▂▅▂▁▂▂▁▂▁▁▂▁▄▂▁▁▁▁▂▁▁▁▂▁▁▂▁▅▂▂▂▁▂▄▂▁▄▁▁▁▁▁▁▄▁▅▁▁▁▅▄▁▁▂▂▂▄▂▁▂▂▁▁▁▂▁▂▂▁▂▄▂▂▄▂▅▄▂▂▄▂▁▁▄▁▁▂▂▁▁▂▂▁▂▁▁▂▂▄▂▅▇▂▅▄▂▅▂▁▂▂▁▂▁▂▁▄▇▁▂▁▁█▄▁▂▁▄▄▁▁▁▁▁▁▁▁▂▁▂▂▂▄▅▁▂▂▄▁` |
| v153 | 89 | `▃▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▃▁▁▃▃▅▆▁▁▁▃▁▃▁▅▁▁▁▁▁▁▁▁▁▃▃▁▃▃▁▁▁▁▃▁▁▃▁▃▁▁▁▁▁▁▁▁▁▃▁▁▁▃▁▁▁▁▁▁▁▁▁▅▁▁▁▁▃▁▁▅▁▃▅▅▁▃▁▅▃▁▁▁▃▁▃▃▃▁▃▅▃▁▆▁▃▁▆▅▃▅▁▆▁▁▁▁▃▃▃▁▁▃▁▃▁▃▅▁▁▁▅▁█▁▁▁▃▁▁▃▁▃▃▃▁▁▁▃▃▁▅▁▁▅▃▃▁▁` |
| v140 | 17 | `▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁█▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▅▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁` |
| v156 | 12 | `█▁█▁█▁▁▁█▁█▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| v115 | 9 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁██▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁` |
| v128 | 7 | `▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### Top mail providers

| Value | Total | Trend |
|:--|--:|:--|
| m:att | 23 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▅▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▅█▁▁█▁▁███▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| m:gmail | 22 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁▅▁▁▁▁▁█▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▅▁▁▁▁▅▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▅▁` |
| m:microsoftemail | 15 | `▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁` |
| m:yahooemail | 14 | `▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁▁▁▅█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| m:shaw | 5 | `█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| m:thundermail | 4 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### Top feature areas

| Value | Total | Trend |
|:--|--:|:--|
| feat:attachments | 54 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▅▁▁▁▅▁▁▅▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▅▁█▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▅▅▅█▁▁▁▅▅▁▁▁▅▁▁▁▁▁▅█▁▁▅▁▁▁▁▁▁▅█▅█▅▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▅▁█▁▁▁▅▅▁▅▁▁▅▅▁▁▅▁█▅▁▅▁▅▁▅▁▁` |
| feat:calendar | 9 | `▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁` |
| feat:junk | 6 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| feat:import_export | 3 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁` |
| feat:addons | 2 | `▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| feat:addressbook | 1 | `▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### Top protocols

| Value | Total | Trend |
|:--|--:|:--|
| proto:imap | 21 | `▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁█▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▅▅▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:pop | 13 | `▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:smtp | 10 | `▁▅▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:oauth | 5 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:caldav | 4 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁` |
| proto:ews | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### Top antivirus

| Value | Total | Trend |
|:--|--:|:--|
| av:norton | 4 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:avast | 3 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:defender | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### OS mix (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| os:windows | 288 | `▅▅▆▂▃▁▂▁▂▂▁▂▁▃▁▂▃▄▂▂▄▃▂▃▅▅▃▂▂▃▁▅▂▃▁▁▁▃▁▁▁▂▁▁▄▃▄▃▃▂▁▃▄▃▁▄▁▂▁▁▁▁▃▁▂▁▂▂▄▃▂▄▃▂▂▄▂▂▂▂▁▂▁▂▁▂▃▁▄▅▂▄▅▄▅▅▃▄▅▂▁▂▅▁▂▃▃▂▂▄▃▁▅▂▂▂█▄▂▅▇▅▄▃▁▄▄▃▃▂▁▃▁▄▁▄▅▁▂▂▃▅▅▁▃▁▅▃▂▂▁▂▃▃▁▁▂▂▄▂▄▂▄▃▄▄▃▂` |
| os:linux | 19 | `▁▁▅▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁█▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁█▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| os:macos | 16 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▅▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▁▅▅▅▁▅▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| os:other | 4 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| os:android | 2 | `█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### macOS releases (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| macos:catalina | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:golden_gate | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:tahoe | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

---

_Notes: spikes detected at **daily** grain (coarser grains catch slow-burn incidents a daily threshold misses — e.g. the March 2026 GMX provider outage). Volume / cause / OS trends span the full scraper history (2023-01+). **Version×cause covers 2026-02 onward** — the native `thunderbird_version` field ([Kitsune PR #7443](https://github.com/mozilla/kitsune/pull/7443)) is only populated from Feb 2026 (~27% → 85% by mid-2026), so earlier questions carry no version; cause-level spikes use all history. Thresholds calibrated on the post-backfill baseline. Full IDs per spike in `PROJECT1/desktop-daily-version-cause-spikes.csv` (version×cause) and `PROJECT1/desktop-daily-single-spikes.csv` (cause-level); full series in `PROJECT1/desktop-hourly-rollup.csv`._

_Last updated: 2026-10-08 16:48 UTC_
