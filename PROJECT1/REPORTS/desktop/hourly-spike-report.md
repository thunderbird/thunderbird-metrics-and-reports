---
layout: base
title: HOURLY: Thunderbird Desktop — Support Spike Report
---

# HOURLY: Thunderbird Desktop — Support Spike Report

_Generated 2026-10-05 16:00 … 2026-10-12 15:00 · **hourly** grain · trailing 168 hours · 306 questions · no AI (regex + traditional stats)_

- **Volume:** 306 questions, 1.8/hour avg
- **Answered (non-creator):** 244/306 (80%)
- **First-answer time (median):** 2.1h (p25 0.6h / p75 7.5h)
- **Total volume trend:** `▅▃▄▅▂▂▂▅▁▂▃▃▂▂▄▃▁▇▂▂▂█▅▃▅▇▅▆▃▂▅▄▃▄▂▁▄▁▄▁▄▆▁▂▃▄▆▇▂▄▂▅▅▂▂▁▂▃▃▂▁▂▂▄▂▄▃▄▄▄▄▄▃▁▅▄▂▃▂▁▁▂▁▁▁▂▁▁▆▅▄▄▃▇▄▃▃▅▁▃▂▃▄▂▂▁▁▃▂▁▁▃▃▃▃▁▂▅▂▂▂▁▁▁▂▁▂▃▂▁▃▁▁▁▁▁▁▁▁▃▁▃▅▂▃▃▂▂▂▁▁▁▂▂▁▁▁▂▃▃▄▃▃▃▄▁▁▆`

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

> 🔎 **Want a bump that is not listed below?** The sparklines here are static text. Open the [interactive explorer](explorer.html), pick a grain / version / cause, and **click any point** to read that period's questions — every period, not just the ones that cleared a threshold. Each spike row also links straight to its own bucket.

## 🚨 Engineering signal — version × cause spikes

Cause clusters over-represented in a specific Thunderbird version. The **Signal** column flags 🆕 **new** (cause never spiked before), ↗ **spreading** (known cause, new version), or ↻ **recurring** (chronic / seen before) — ranked new→spreading→recurring, then by **lift**. Click an ID to read it.


| Signal | Lift | When | Version × Cause | Qs | Served | Example questions | Trend |
|:--|---:|:--|:--|--:|:--|:--|:--|
| 🆕 new | **104.8×** | 2026-10-06 | v140 × m:att | 4 | 75% ans · 2.7h | [1610156](https://support.mozilla.org/questions/1610156 "Gives error today - inbound.att.net certificate invalid !!??") [1610258](https://support.mozilla.org/questions/1610258 "The certificate for inbound.att.net does not come from a trusted source.") [1610259](https://support.mozilla.org/questions/1610259 "Why Thunderbird on Linux will no longer connect to att.net email with POP3.") [1610309](https://support.mozilla.org/questions/1610309 "AOL setup on MX Linux... fails authentication") · [explore ↗](explorer.html#grain=daily&version=140&cause=m:att&period=2026-10-06) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁█▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| ↻ recurring | **14.1×** | 2026-10-10 | v153 × feat:attachments | 4 | 100% ans · 0.9h | [1611065](https://support.mozilla.org/questions/1611065 "Suddenly I can't attach anything to my emails!") [1611069](https://support.mozilla.org/questions/1611069 "it has not been possible to attach files to emails using the paperclip icon.") [1611096](https://support.mozilla.org/questions/1611096 "Can no longer attach photos with e-mail.") [1611102](https://support.mozilla.org/questions/1611102 "Can no longer attach photos with e-mail. (locked duplicate)") · [explore ↗](explorer.html#grain=daily&version=153&cause=feat:attachments&period=2026-10-10) | `▁▁▅▅▁▁▁▅▁▁▁▁▁▅▅▁▁▅▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁█▁▁▁▁▁▁▅▁▁▅▅▁▁▁▁▅▁▁▁▁▅▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁` |
| ↻ recurring | **11.7×** | 2026-10-08 | v153 × feat:attachments | 5 | 100% ans · 0.6h | [1610569](https://support.mozilla.org/questions/1610569 "The file picker does not open when you click the “Attach” button") [1610581](https://support.mozilla.org/questions/1610581 "Cannot attach files to emails in Thunderbird") [1610617](https://support.mozilla.org/questions/1610617 "Attachment function not accessible anymore") [1610652](https://support.mozilla.org/questions/1610652 "Attachment to an email is not possible with Tunderbird") [1610745](https://support.mozilla.org/questions/1610745 "Why can't I attach a document to my email") · [explore ↗](explorer.html#grain=daily&version=153&cause=feat:attachments&period=2026-10-08) | `▁▁▅▅▁▁▁▅▁▁▁▁▁▅▅▁▁▅▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁█▁▁▁▁▁▁▅▁▁▅▅▁▁▁▁▅▁▁▁▁▅▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁` |
| ↻ recurring | **9.4×** | 2026-10-07 | v153 × feat:attachments | 5 | 100% ans · 2.0h | [1610392](https://support.mozilla.org/questions/1610392 "Recurring Issue with Attachment Button in Thunderbird Desktop") [1610416](https://support.mozilla.org/questions/1610416 "sinds de update 153.4.0esr van 05 oktober kan ik geen bijlagen meer koppelen aan") [1610444](https://support.mozilla.org/questions/1610444 "Thunderbird has stopped to include attachments via key. Only drag and drop funct") [1610449](https://support.mozilla.org/questions/1610449 "A problem with sending attachments with an email") [1610548](https://support.mozilla.org/questions/1610548 "Unable to add an attachment to the email being sent") · [explore ↗](explorer.html#grain=daily&version=153&cause=feat:attachments&period=2026-10-07) | `▁▁▅▅▁▁▁▅▁▁▁▁▁▅▅▁▁▅▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁█▁▁▁▁▁▁▅▁▁▅▅▁▁▁▁▅▁▁▁▁▅▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁` |
| ↻ recurring | **8.2×** | 2026-10-09 | v157 × feat:attachments | 7 | 100% ans · 7.6h | [1610829](https://support.mozilla.org/questions/1610829 "impossibile inserire allegati") [1610832](https://support.mozilla.org/questions/1610832 "No attachment possible") [1610883](https://support.mozilla.org/questions/1610883 "Ik kan geen bijlagen voegen bij mijn email") [1610903](https://support.mozilla.org/questions/1610903 "blokkering van bijlagen koppelen in emailbericht") [1610926](https://support.mozilla.org/questions/1610926 "I cannot attach files") [1610958](https://support.mozilla.org/questions/1610958 "Kan bij email verzenden geen bijlage openen") +1 · [explore ↗](explorer.html#grain=daily&version=157&cause=feat:attachments&period=2026-10-09) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁█▅▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▅▁▅▅▁▅▁▁▁▅▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▅▁▅▁▅▁▅▁▁▅▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▁▁▅▁▁▅` |
| ↻ recurring | **8.0×** | 2026-10-12 | v157 × feat:attachments | 4 | ⚠️ 50% ans · 0.6h | [1611426](https://support.mozilla.org/questions/1611426 "Chci do zprávy vložit přílohu a po kliknutí na ikonu příloha se mi nezobrazí nab") [1611443](https://support.mozilla.org/questions/1611443 "Attach button in write email no no longer working") [1611472](https://support.mozilla.org/questions/1611472 "Kan geen bijlage toevoegen in email") [1611511](https://support.mozilla.org/questions/1611511 "Signature attachment button in account settings no longer working; will not go t") · [explore ↗](explorer.html#grain=daily&version=157&cause=feat:attachments&period=2026-10-12) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁█▅▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▅▁▅▅▁▅▁▁▁▅▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▅▁▅▁▅▁▅▁▁▅▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▁▁▅▁▁▅` |
| ↻ recurring | **7.7×** | 2026-10-08 | v157 × feat:attachments | 6 | 100% ans · 0.7h | [1610602](https://support.mozilla.org/questions/1610602 "Nejde mi přidat do mailu příloha") [1610606](https://support.mozilla.org/questions/1610606 "The ＂Attach＂ button doesn't work when composing an email; it is not possible to ") [1610619](https://support.mozilla.org/questions/1610619 "Why can I no longer attach a file by clicking OPEN on the file location and why ") [1610638](https://support.mozilla.org/questions/1610638 "allegati mail") [1610666](https://support.mozilla.org/questions/1610666 "een blokkade om bijlagen te koppelen in email die ik verstuur") [1610758](https://support.mozilla.org/questions/1610758 "All of a sudden the attach button does nothing.") · [explore ↗](explorer.html#grain=daily&version=157&cause=feat:attachments&period=2026-10-08) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁█▅▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▅▁▅▅▁▅▁▁▁▅▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▅▁▅▁▅▁▅▁▁▅▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▁▁▅▁▁▅` |
| ↻ recurring | **6.1×** | 2026-10-06 | v153 × feat:attachments | 5 | 100% ans · 1.2h | [1610087](https://support.mozilla.org/questions/1610087 "Email attachment - version 153.4.0esr") [1610100](https://support.mozilla.org/questions/1610100 "unable to attach desktop files to outgoing emails when attachment function activ") [1610118](https://support.mozilla.org/questions/1610118 "All of a sudden Thunderbird won't let me attach images") [1610206](https://support.mozilla.org/questions/1610206 "I have lost the attach file link since last up date") [1610244](https://support.mozilla.org/questions/1610244 "I can't add any attachments. The button doesn't work") · [explore ↗](explorer.html#grain=daily&version=153&cause=feat:attachments&period=2026-10-06) | `▁▁▅▅▁▁▁▅▁▁▁▁▁▅▅▁▁▅▁▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁█▁▁▁▁▁▁▅▁▁▅▅▁▁▁▁▅▁▁▁▁▅▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁` |
| ↻ recurring | **5.0×** | 2026-10-06 | v157 × feat:attachments | 5 | 100% ans · 0.9h | [1610097](https://support.mozilla.org/questions/1610097 "Since that last update I can no longer attach files to emails. Can You help?") [1610225](https://support.mozilla.org/questions/1610225 "Suddenly I can neither attach nor insert files into an outgoing email.") [1610267](https://support.mozilla.org/questions/1610267 "Attach File no longer Works as of 10/05 W11") [1610268](https://support.mozilla.org/questions/1610268 "Unable to attach files to emails (the ‘Attachments’ button does not respond)./ A") [1610276](https://support.mozilla.org/questions/1610276 "Attach button not working on new emails") · [explore ↗](explorer.html#grain=daily&version=157&cause=feat:attachments&period=2026-10-06) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁█▅▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▅▁▅▅▁▅▁▁▁▅▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▅▁▅▁▅▁▅▁▁▅▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▁▁▅▁▁▅` |

## 📮 Cause-level spikes — provider / protocol / AV / feature

Causes surging **regardless of version** vs a trailing day baseline — provider/ISP outages and protocol/AV issues. Not necessarily a Thunderbird bug, but worth a triage look. Ranked by magnitude.


| Rise | When | Cause | Qs | Served | Baseline | Example questions | Trend |
|---:|:--|:--|--:|:--|--:|:--|:--|
| **new** | 2026-10-07 | feat:attachments | 8 | 100% ans · 1.3h | 0.0 | [1610366](https://support.mozilla.org/questions/1610366 "Thunderbird, button ＂attach＂") [1610392](https://support.mozilla.org/questions/1610392 "Recurring Issue with Attachment Button in Thunderbird Desktop") [1610416](https://support.mozilla.org/questions/1610416 "sinds de update 153.4.0esr van 05 oktober kan ik geen bijlagen meer koppelen aan") [1610444](https://support.mozilla.org/questions/1610444 "Thunderbird has stopped to include attachments via key. Only drag and drop funct") [1610449](https://support.mozilla.org/questions/1610449 "A problem with sending attachments with an email") [1610512](https://support.mozilla.org/questions/1610512 "Can't use Attachments like I have always done and need for work") +2 · [explore ↗](explorer.html#grain=daily&cause=feat:attachments&period=2026-10-07) | `▁▁▅▅▁▁▁▅▁▁▁▁▁▅█▁▁▅▁▁▁▁▁▁▅█▅█▅▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▅▁█▁▁▁▅▅▁▅▁▁▅▅▁▁▅▁█▅▁▅▁▅▁▅▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁█▁▅▅▁█▅▅▁█▁▅▁▁▅▁▁▁▁▁▁▁▁▁▅▅▅▁▅█▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▅▁▅▁▅█▁▁▅` |
| **new** | 2026-10-09 | feat:attachments | 12 | 100% ans · 3.5h | 0.0 | [1610829](https://support.mozilla.org/questions/1610829 "impossibile inserire allegati") [1610832](https://support.mozilla.org/questions/1610832 "No attachment possible") [1610850](https://support.mozilla.org/questions/1610850 "Waarom kan ik ineens in Thunderbird geen bijlage meer toevoegen?") [1610861](https://support.mozilla.org/questions/1610861 "Best Method to Convert MBOX Files to PDF with Attachments in 2026") [1610871](https://support.mozilla.org/questions/1610871 "Also to find the suggested file mail.compose.attach.dir I can not find to remove") [1610883](https://support.mozilla.org/questions/1610883 "Ik kan geen bijlagen voegen bij mijn email") +6 · [explore ↗](explorer.html#grain=daily&cause=feat:attachments&period=2026-10-09) | `▁▁▅▅▁▁▁▅▁▁▁▁▁▅█▁▁▅▁▁▁▁▁▁▅█▅█▅▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▅▁█▁▁▁▅▅▁▅▁▁▅▅▁▁▅▁█▅▁▅▁▅▁▅▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁█▁▅▅▁█▅▅▁█▁▅▁▁▅▁▁▁▁▁▁▁▁▁▅▅▅▁▅█▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▅▁▅▁▅█▁▁▅` |
| **new** | 2026-10-08 | feat:attachments | 11 | 100% ans · 0.6h | 0.0 | [1610569](https://support.mozilla.org/questions/1610569 "The file picker does not open when you click the “Attach” button") [1610581](https://support.mozilla.org/questions/1610581 "Cannot attach files to emails in Thunderbird") [1610602](https://support.mozilla.org/questions/1610602 "Nejde mi přidat do mailu příloha") [1610606](https://support.mozilla.org/questions/1610606 "The ＂Attach＂ button doesn't work when composing an email; it is not possible to ") [1610617](https://support.mozilla.org/questions/1610617 "Attachment function not accessible anymore") [1610619](https://support.mozilla.org/questions/1610619 "Why can I no longer attach a file by clicking OPEN on the file location and why ") +5 · [explore ↗](explorer.html#grain=daily&cause=feat:attachments&period=2026-10-08) | `▁▁▅▅▁▁▁▅▁▁▁▁▁▅█▁▁▅▁▁▁▁▁▁▅█▅█▅▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▅▁█▁▁▁▅▅▁▅▁▁▅▅▁▁▅▁█▅▁▅▁▅▁▅▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁█▁▅▅▁█▅▅▁█▁▅▁▁▅▁▁▁▁▁▁▁▁▁▅▅▅▁▅█▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▅▁▅▁▅█▁▁▅` |
| **new** | 2026-10-06 | feat:attachments | 11 | 100% ans · 1.2h | 0.0 | [1610087](https://support.mozilla.org/questions/1610087 "Email attachment - version 153.4.0esr") [1610097](https://support.mozilla.org/questions/1610097 "Since that last update I can no longer attach files to emails. Can You help?") [1610100](https://support.mozilla.org/questions/1610100 "unable to attach desktop files to outgoing emails when attachment function activ") [1610118](https://support.mozilla.org/questions/1610118 "All of a sudden Thunderbird won't let me attach images") [1610206](https://support.mozilla.org/questions/1610206 "I have lost the attach file link since last up date") [1610216](https://support.mozilla.org/questions/1610216 "Thunerbird suddenly won't allow me to attach documents") +5 · [explore ↗](explorer.html#grain=daily&cause=feat:attachments&period=2026-10-06) | `▁▁▅▅▁▁▁▅▁▁▁▁▁▅█▁▁▅▁▁▁▁▁▁▅█▅█▅▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▅▁█▁▁▁▅▅▁▅▁▁▅▅▁▁▅▁█▅▁▅▁▅▁▅▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁█▁▅▅▁█▅▅▁█▁▅▁▁▅▁▁▁▁▁▁▁▁▁▅▅▅▁▅█▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▅▁▅▁▅█▁▁▅` |
| **new** | 2026-10-06 | m:att | 11 | 91% ans · 89.3h | 0.0 | [1610152](https://support.mozilla.org/questions/1610152 "Certificate revoked for inbound.att.net?  What do we do?") [1610156](https://support.mozilla.org/questions/1610156 "Gives error today - inbound.att.net certificate invalid !!??") [1610171](https://support.mozilla.org/questions/1610171 "＂inbound.att.net (POP) .. certificate revoked＂? I can't download eMail!") [1610193](https://support.mozilla.org/questions/1610193 "certificate has been revoked. unable to receive email.") [1610212](https://support.mozilla.org/questions/1610212 "pop from Tbird says connection to server inbound.att.net has been reset") [1610258](https://support.mozilla.org/questions/1610258 "The certificate for inbound.att.net does not come from a trusted source.") +5 · [explore ↗](explorer.html#grain=daily&cause=m:att&period=2026-10-06) | `▁▁▁▅▅▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▅█▁▁█▁▁███▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

## 📈 Trends

### Top versions

| Value | Total | Trend |
|:--|--:|:--|
| v157 | 140 | `▄▂▂▄▂▁▁▄▁▁▂▂▁▁▂▂▁▂▁▁▂▂▄▂▅▇▂▅▄▂▅▂▁▂▂▁▂▁▂▁▄▇▁▂▁▁█▄▁▂▁▄▄▁▁▁▁▁▁▁▁▂▁▂▂▂▄▅▁▂▂▄▂▁▅▅▁▂▂▁▁▁▁▁▁▂▁▁▇▄▂▄▂▅▂▂▂▄▁▂▂▂▄▁▁▁▁▂▂▁▁▄▂▂▁▁▂▂▁▁▁▁▁▁▁▁▂▂▂▁▄▁▁▁▁▁▁▁▁▂▁▁▇▂▁▂▁▁▁▁▁▁▁▂▁▁▁▁▂▄▅▄▂▁▄▁▁▄` |
| v153 | 87 | `▃▁▅▃▁▁▁▃▁▃▃▃▁▃▅▃▁▆▁▃▁▆▅▃▅▁▆▁▁▁▁▃▃▃▁▁▃▁▃▁▃▅▁▁▁▅▁█▁▁▁▃▁▁▃▁▃▃▃▁▁▁▃▃▁▅▁▁▅▃▃▁▁▁▁▁▃▁▁▁▁▃▁▁▁▁▁▁▃▃▁▁▃▅▅▁▃▃▁▃▁▁▁▃▁▁▁▃▁▁▁▁▁▃▅▁▁▅▁▃▁▁▁▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▃▁▁▃▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▅▃▁▁█` |
| v140 | 12 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁█▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▅▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| v115 | 10 | `▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁██▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| v128 | 5 | `▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| v156 | 4 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### Top mail providers

| Value | Total | Trend |
|:--|--:|:--|
| m:att | 24 | `▁▁▁▅▅▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▅█▁▁█▁▁███▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| m:gmail | 20 | `▁▅▅▁▁▁▁▅▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▅▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁` |
| m:yahooemail | 17 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▅▁▁▁▅█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▅▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| m:microsoftemail | 11 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁` |
| m:thundermail | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| m:verizon | 2 | `█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### Top feature areas

| Value | Total | Trend |
|:--|--:|:--|
| feat:attachments | 61 | `▁▁▅▅▁▁▁▅▁▁▁▁▁▅█▁▁▅▁▁▁▁▁▁▅█▅█▅▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▅▁█▁▁▁▅▅▁▅▁▁▅▅▁▁▅▁█▅▁▅▁▅▁▅▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁█▁▅▅▁█▅▅▁█▁▅▁▁▅▁▁▁▁▁▁▁▁▁▅▅▅▁▅█▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▅▁▅▁▅█▁▁▅` |
| feat:import_export | 5 | `█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| feat:calendar | 4 | `▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| feat:addressbook | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█` |
| feat:junk | 2 | `▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| feat:addons | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### Top protocols

| Value | Total | Trend |
|:--|--:|:--|
| proto:imap | 13 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁██▁▁▁▁▁█▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁` |
| proto:pop | 11 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁█▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁█▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:oauth | 6 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:smtp | 6 | `▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:caldav | 3 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:ews | 2 | `█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### Top antivirus

| Value | Total | Trend |
|:--|--:|:--|
| av:avast | 5 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:norton | 4 | `▁▁▁▁█▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:defender | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### OS mix (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| os:windows | 258 | `▅▃▄▅▂▁▂▅▁▂▃▃▂▂▄▃▁▅▂▂▂█▄▂▅▇▅▄▃▁▄▄▃▃▂▁▃▁▄▁▄▅▁▂▂▃▅▅▁▃▁▅▃▂▂▁▂▃▃▂▁▂▂▄▂▄▂▄▃▄▄▃▃▁▅▄▂▃▁▁▁▂▁▁▁▂▁▁▆▃▃▄▃▇▄▃▃▅▁▃▂▃▃▂▂▁▁▂▂▁▁▃▂▃▂▁▂▅▂▂▂▁▁▁▂▁▂▂▁▁▃▁▁▁▁▁▁▁▁▂▁▃▅▂▃▂▁▂▂▁▁▁▂▁▁▁▁▂▂▃▃▃▂▃▄▁▁▅` |
| os:linux | 19 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁█▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁█▅▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▅▅▁▁▁▁▁▁▅▁▁▁▁▁▁▅▁▁▁▁▁▁▁` |
| os:macos | 17 | `▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▅▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▁▅▅▅▁▅▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█` |
| os:other | 3 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁` |
| os:android | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### macOS releases (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| macos:tahoe | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

---

_Notes: spikes detected at **daily** grain (coarser grains catch slow-burn incidents a daily threshold misses — e.g. the March 2026 GMX provider outage). Volume / cause / OS trends span the full scraper history (2023-01+). **Version×cause covers 2026-02 onward** — the native `thunderbird_version` field ([Kitsune PR #7443](https://github.com/mozilla/kitsune/pull/7443)) is only populated from Feb 2026 (~27% → 85% by mid-2026), so earlier questions carry no version; cause-level spikes use all history. Thresholds calibrated on the post-backfill baseline. Full IDs per spike in `PROJECT1/desktop-daily-version-cause-spikes.csv` (version×cause) and `PROJECT1/desktop-daily-single-spikes.csv` (cause-level); full series in `PROJECT1/desktop-hourly-rollup.csv`._

_Last updated: 2026-10-12 16:44 UTC_
