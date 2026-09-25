---
layout: base
title: DAILY: Thunderbird Desktop — Support Spike Report
---

# DAILY: Thunderbird Desktop — Support Spike Report

_Generated 2026-06-28 … 2026-09-25 · **daily** grain · trailing 90 days · 2561 questions · no AI (regex + traditional stats)_

- **Volume:** 2561 questions, 28.5/day avg
- **Answered (non-creator):** 1968/2561 (77%)
- **First-answer time (median):** 3.3h (p25 1.0h / p75 11.2h)
- **Total volume trend:** `▄▄▅▄▅▄▄▃▅▅▄▅▄▃▃▅▅▃▃▃▄▃▅▄▄▅▄▂▅▅▄▄▃▅▄▃▅▅▄▅▅▆▃▅▃▅▅▅▄▅▅▆▄▅▆▅▄▆▅█▆▅▄▄▇▅▇▇▅▄▄▇▆▆▅▆▃▄▅▆▆▅▄▃▃▅▆█▆▁`

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

> 🔎 **Want a bump that is not listed below?** The sparklines here are static text. Open the [interactive explorer](explorer.html), pick a grain / version / cause, and **click any point** to read that period's questions — every period, not just the ones that cleared a threshold. Each spike row also links straight to its own bucket.

## 🚨 Engineering signal — version × cause spikes

Cause clusters over-represented in a specific Thunderbird version. The **Signal** column flags 🆕 **new** (cause never spiked before), ↗ **spreading** (known cause, new version), or ↻ **recurring** (chronic / seen before) — ranked new→spreading→recurring, then by **lift**. Click an ID to read it.


| Signal | Lift | When | Version × Cause | Qs | Served | Example questions | Trend |
|:--|---:|:--|:--|--:|:--|:--|:--|
| 🆕 new | **76.3×** | 2026-09-23 | v153 × m:alice_it | 5 | 100% ans · 3.1h | [1606888](https://support.mozilla.org/questions/1606888 "non mi funziona la mail alice.it") [1606928](https://support.mozilla.org/questions/1606928 "non ricevo le mail di Alicemail") [1606938](https://support.mozilla.org/questions/1606938 "Alice mail") [1607000](https://support.mozilla.org/questions/1607000 "non scarico messaggi") [1607026](https://support.mozilla.org/questions/1607026 "Non riesco a scaricare posta alice su thunderbid, mi da errore di collegamento..") · [explore ↗](explorer.html#grain=daily&version=153&cause=m:alice_it&period=2026-09-23) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▂▁█▄▁` |
| 🆕 new | **26.7×** | 2026-08-20 | v154 × feat:printing | 4 | 75% ans · 3.2h | [1599257](https://support.mozilla.org/questions/1599257 "Print emails") [1599261](https://support.mozilla.org/questions/1599261 "Perchè non si riesce a stampare diretta mente da Thunderbird un allegato ad un m") [1599285](https://support.mozilla.org/questions/1599285 "PDF attachments now blank when printed.  Worked great til today.") [1599333](https://support.mozilla.org/questions/1599333 "can not print attachments") · [explore ↗](explorer.html#grain=daily&version=154&cause=feat:printing&period=2026-08-20) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▇▄▂▁▄▄█▅▂▅▂▇▇▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| 🆕 new | **7.2×** | 2026-09-16 | v153 × m:yahooemail | 4 | 75% ans · 0.8h | [1604613](https://support.mozilla.org/questions/1604613 "Error messages.  t-bird Linux Mint ＂.p＂ and ＂UID Fetch＂") [1604699](https://support.mozilla.org/questions/1604699 "I messaggi di un account vanno anche in un secondo account") [1604799](https://support.mozilla.org/questions/1604799 "thunderbird deleting my emails from the POP server") [1604953](https://support.mozilla.org/questions/1604953 "Thunderbird won't send emails between  2 AOL accounts") · [explore ↗](explorer.html#grain=daily&version=153&cause=m:yahooemail&period=2026-09-16) | `▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▅▁▆▃▁▅▃▃▆▃▃▃▃▃▃▃▆▅▃▅▃▆▃▁▁▅▃▃▁▁▃▁▁▁▁▁▃▁▁▁▃▁▃▁▅▃▃▅▁▅▃▃█▁▃▃▁▁▁▁▃▁` |
| 🆕 new | **4.8×** | 2026-06-30 | v152 × m:gmail | 4 | ⚠️ 50% ans · 2.5h | [1590372](https://support.mozilla.org/questions/1590372 "Urgent question: Wrong email group when I sign in coming up") [1590393](https://support.mozilla.org/questions/1590393 "Storende pop-up naar aanleiding van verwijderde google-account") [1590463](https://support.mozilla.org/questions/1590463 "Message not visible with no filter activated, all account are synchronized") [1590499](https://support.mozilla.org/questions/1590499 "archive Gmail to local storage　by Tb") · [explore ↗](explorer.html#grain=daily&version=152&cause=m:gmail&period=2026-06-30) | `▁▁█▅▆▅▆▅▃▅▃▅▆▃▁▁▃▁▁▁▁▁▁▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| ↗ spreading | **4.9×** | 2026-06-29 | v152 × m:microsoftemail | 6 | 67% ans · 87.5h | [1590178](https://support.mozilla.org/questions/1590178 "Adding 2nd outlook accound") [1590198](https://support.mozilla.org/questions/1590198 "Thunderbird emails have started to only show links and not the pictures within t") [1590208](https://support.mozilla.org/questions/1590208 "Can't connect to my live and outlook accounts since 2 weeks") [1590210](https://support.mozilla.org/questions/1590210 "TBird152.0  is not displaing HTML emails properly.") [1590301](https://support.mozilla.org/questions/1590301 "One-hour delay in the guest's meeting schedule (Atraso de uma hora na agenda do ") [1590307](https://support.mozilla.org/questions/1590307 "I got a message: ＂Authentication failure while connecting to server outlook.offi") · [explore ↗](explorer.html#grain=daily&version=152&cause=m:microsoftemail&period=2026-06-29) | `▁█▁▁▃▁▂▂▁▁▁▅▁▁▃▁▂▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| ↗ spreading | **4.0×** | 2026-09-16 | v156 × m:microsoftemail | 4 | 75% ans · 50.5h | [1604594](https://support.mozilla.org/questions/1604594 "Still can't sync outlook outgoing mail with thunderbird, i receive emails just f") [1604697](https://support.mozilla.org/questions/1604697 "Authentication Failure outlook.office365.com only on startup") [1604835](https://support.mozilla.org/questions/1604835 "ERROR AL AÑADIR CUENTA DE OUTLOOK") [1604859](https://support.mozilla.org/questions/1604859 "autenticazione non riuscita durante la connessione al server outlook su thunderb") · [explore ↗](explorer.html#grain=daily&version=156&cause=m:microsoftemail&period=2026-09-16) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▅▁▁▅▁▅▃▅▁` |
| ↗ spreading | **3.7×** | 2026-09-07 | v155 × proto:pop | 4 | 75% ans · 5.2h | [1602660](https://support.mozilla.org/questions/1602660 "pop3 account creation error") [1602682](https://support.mozilla.org/questions/1602682 "Login to server pop3.virginmedia.com with username ******* failed") [1602703](https://support.mozilla.org/questions/1602703 "Thunderbird freezes downloading messages when it reaches a message from aliexpre") [1602714](https://support.mozilla.org/questions/1602714 "Is syncronization bidirectional with IMAP accounts?") · [explore ↗](explorer.html#grain=daily&version=155&cause=proto:pop&period=2026-09-07) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▆▁▃▃▁█▁▁▃▆▃▁▁▃▁▁▃▁▁▁▁▁▁▁` |
| ↗ spreading | **3.3×** | 2026-08-04 | v153 × m:microsoftemail | 5 | 100% ans · 0.8h | [1596545](https://support.mozilla.org/questions/1596545 "Microsoft Outlook authentication failure.") [1596547](https://support.mozilla.org/questions/1596547 "I just had a fake prompt to add a password to a website mimicking Thunderbird") [1596591](https://support.mozilla.org/questions/1596591 "email not collegament to app thunderbird pc (email outlook)") [1596602](https://support.mozilla.org/questions/1596602 "Import from Outlook (M365) Mac OS to Thunderbird?") [1596606](https://support.mozilla.org/questions/1596606 "Cannot import contacts from outlook 2016") · [explore ↗](explorer.html#grain=daily&version=153&cause=m:microsoftemail&period=2026-08-04) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▄▁▁▁▂▄▂▁▂▁▁▂▇█▄▁▂▂▁▅▂▄▄▂▁▂▂▁▁▂▂▁▁▁▂▁▁▂▁▁▂▁▁▂▁▁▁▁▂▄▁▁▁▁▄▂▅▁▂▁▁▂▁▁▁▂` |
| ↗ spreading | **3.2×** | 2026-08-10 | v153 × proto:pop | 4 | 75% ans · 1.1h | [1597551](https://support.mozilla.org/questions/1597551 "Thunderbird POP stopped retrieving email from one mail box, No error message") [1597571](https://support.mozilla.org/questions/1597571 "Email collection over pop failed on one account, server settings rejected when I") [1597638](https://support.mozilla.org/questions/1597638 "How logging onto wowway with old password?") [1597683](https://support.mozilla.org/questions/1597683 "Hotmail personal account: IMAP OAuth2 works but SMTP OAuth2 fails with message: ") · [explore ↗](explorer.html#grain=daily&version=153&cause=proto:pop&period=2026-08-10) | `▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▃▁▁▁▃▁▁▆▃▃▅▅▁▅▃▃▅█▁▁██▁▁▃▃▁▃▁▁▁▁▁▁▃▃▃▁▆▁▁▁▁▁▃▁▃▁▁▃▁▁▃▃▅▅▁▁▃▁▃▆▆▁` |
| ↻ recurring | **18.8×** | 2026-09-01 | v154 × feat:printing | 4 | 100% ans · 13.8h | [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601564](https://support.mozilla.org/questions/1601564 "Can no longer highlight text in a .pdf being previewed in Thunderbird and Printi") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") · [explore ↗](explorer.html#grain=daily&version=154&cause=feat:printing&period=2026-09-01) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▇▄▂▁▄▄█▅▂▅▂▇▇▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| ↻ recurring | **14.8×** | 2026-08-26 | v154 × feat:printing | 5 | 100% ans · 13.8h | [1600392](https://support.mozilla.org/questions/1600392 "Printing from Thunderbird since version 154.0 on Windows 11 produces only blank ") [1600397](https://support.mozilla.org/questions/1600397 "Problema anteprima di stampa") [1600407](https://support.mozilla.org/questions/1600407 "PDF direct print from mozilla wil print an blanc page") [1600408](https://support.mozilla.org/questions/1600408 "Problem printing PDF files from Thunderbird.") [1600481](https://support.mozilla.org/questions/1600481 "Print Preview Printing Blanks") · [explore ↗](explorer.html#grain=daily&version=154&cause=feat:printing&period=2026-08-26) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▇▄▂▁▄▄█▅▂▅▂▇▇▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| ↻ recurring | **14.6×** | 2026-08-31 | v154 × feat:printing | 4 | 100% ans · 2.9h | [1601286](https://support.mozilla.org/questions/1601286 "Ik kan niet meer printen vanuit Thunderbird. Is er een storing?") [1601306](https://support.mozilla.org/questions/1601306 "Problemi di stampa") [1601367](https://support.mozilla.org/questions/1601367 "PDF se vytiskne prázdné.") [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") · [explore ↗](explorer.html#grain=daily&version=154&cause=feat:printing&period=2026-08-31) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▇▄▂▁▄▄█▅▂▅▂▇▇▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| ↻ recurring | **3.3×** | 2026-08-14 | v153 × proto:pop | 4 | 100% ans · 8.0h | [1598311](https://support.mozilla.org/questions/1598311 "Thunderbird went goofy for multiple gmail accounts - deleted email does not show") [1598314](https://support.mozilla.org/questions/1598314 "Email from Roadrunner.com does not show but server test works") [1598327](https://support.mozilla.org/questions/1598327 "Unable to receive e-mail") [1598357](https://support.mozilla.org/questions/1598357 "Recently Unable to send (SMTP) from Thunderbird from Cox.com (now thru Yahoo).") · [explore ↗](explorer.html#grain=daily&version=153&cause=proto:pop&period=2026-08-14) | `▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▃▁▁▁▃▁▁▆▃▃▅▅▁▅▃▃▅█▁▁██▁▁▃▃▁▃▁▁▁▁▁▁▃▃▃▁▆▁▁▁▁▁▃▁▃▁▁▃▁▁▃▃▅▅▁▁▃▁▃▆▆▁` |
| ↻ recurring | **3.2×** | 2026-08-13 | v153 × proto:pop | 4 | 100% ans · 1.2h | [1598091](https://support.mozilla.org/questions/1598091 "thunderbird has stopped receiving emails from century link") [1598146](https://support.mozilla.org/questions/1598146 "Can't access my account") [1598151](https://support.mozilla.org/questions/1598151 "How to set up automatic email forwarding from Thunderbird to Gmail") [1598175](https://support.mozilla.org/questions/1598175 "Thunderbird won't download email messages from Yahoo (formerly Cox) account") · [explore ↗](explorer.html#grain=daily&version=153&cause=proto:pop&period=2026-08-13) | `▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▃▁▁▁▃▁▁▆▃▃▅▅▁▅▃▃▅█▁▁██▁▁▃▃▁▃▁▁▁▁▁▁▃▃▃▁▆▁▁▁▁▁▃▁▃▁▁▃▁▁▃▃▅▅▁▁▃▁▃▆▆▁` |

## 📮 Cause-level spikes — provider / protocol / AV / feature

Causes surging **regardless of version** vs a trailing day baseline — provider/ISP outages and protocol/AV issues. Not necessarily a Thunderbird bug, but worth a triage look. Ranked by magnitude.


| Rise | When | Cause | Qs | Served | Baseline | Example questions | Trend |
|---:|:--|:--|--:|:--|--:|:--|:--|
| **new** | 2026-09-23 | m:alice_it | 9 | 100% ans · 0.8h | 0.0 | [1606888](https://support.mozilla.org/questions/1606888 "non mi funziona la mail alice.it") [1606928](https://support.mozilla.org/questions/1606928 "non ricevo le mail di Alicemail") [1606938](https://support.mozilla.org/questions/1606938 "Alice mail") [1606943](https://support.mozilla.org/questions/1606943 "Non riesco più a scaricare la posta in arrivo.") [1606967](https://support.mozilla.org/questions/1606967 "non mi scarica più i messaggi") [1607000](https://support.mozilla.org/questions/1607000 "non scarico messaggi") +3 · [explore ↗](explorer.html#grain=daily&cause=m:alice_it&period=2026-09-23) | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▂▁▁▂▃█▅▁` |
| **8.0×** | 2026-09-16 | m:microsoftemail | 8 | 62% ans · 35.0h | 1.0 | [1604594](https://support.mozilla.org/questions/1604594 "Still can't sync outlook outgoing mail with thunderbird, i receive emails just f") [1604613](https://support.mozilla.org/questions/1604613 "Error messages.  t-bird Linux Mint ＂.p＂ and ＂UID Fetch＂") [1604697](https://support.mozilla.org/questions/1604697 "Authentication Failure outlook.office365.com only on startup") [1604774](https://support.mozilla.org/questions/1604774 "I receive this reply when launching email:   ＂Looks like there’s a problem with ") [1604835](https://support.mozilla.org/questions/1604835 "ERROR AL AÑADIR CUENTA DE OUTLOOK") [1604859](https://support.mozilla.org/questions/1604859 "autenticazione non riuscita durante la connessione al server outlook su thunderb") +2 · [explore ↗](explorer.html#grain=daily&cause=m:microsoftemail&period=2026-09-16) | `▃▆▃▁▄▃▂▂▁▁▃▆▁▁▄▁▄▁▃▂▁▁▃▂▃▂▁▁▂▃▂▂▂▁▃▂▅▅▃▁▃▂▁▄▂▃▄▃▁▂▂▂▂▃▄▃▂▂▃▂▂▃▁▃▅▂▄▂▁▁▁▂▅▅▂▂▁▃▅▅█▃▃▁▃▂▅▂▃▂` |

## 📈 Trends

### Top versions

| Value | Total | Trend |
|:--|--:|:--|
| v153 | 699 | `▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▄▃▂▅▄▄▃▄▆▅▄▇▇▅▇▇▇▅▇▄▇▇▇▅▇▇█▄▄▅▃▃▄▂▄▅▃▂▂▅▂▃▃▂▁▂▃▃▄▃▃▂▃▄▄▄▃▂▂▂▃▂▅▄▁` |
| v140 | 314 | `▇▅▅▅▆▆▇▆▇▅▅█▅▄▂▅▅▅▅▆▄▅▇▅▅▅█▂▇▅▄▇▃▅▂▂▂▃▄▃▃▄▂▃▄▂▁▂▃▂▂▂▁▃▂▃▃▂▂▂▂▂▂▂▄▄▄▃▂▂▁▂▂▃▂▂▁▂▂▁▃▁▂▁▁▂▂▂▄▁` |
| v152 | 250 | `▃█▅▆█▄▆▃▆▇▆▆▄▂▃▆█▄▃▁▆▃▅▆▂▂▁▁▂▁▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| v154 | 246 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▃▄▆▄▄▆▃█▅▅▅▄▇▅▃▂▂▁▁▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| v155 | 233 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▇▇▅▅▇▅▆▅▇▅▄▅█▃▂▂▁▁▁▂▁▁▁` |
| v156 | 126 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▆▅▂▄▅▅█▆▁` |

### Top mail providers

| Value | Total | Trend |
|:--|--:|:--|
| m:gmail | 217 | `▅▁▇▃▄▄▄▅▂▃▄▄▅▄▁▁▅▁▃▄▄▂▁▁▄▂▇▂▇▃▄▂▅▃▂▁▆▅▂▅▂▅▁▄▂▃▄▃▄▁▄█▃▅▃▄▄▁▄▄▂▁▄▄▅▃▄▄▆▁▃▂█▄▅▄▂▃▅▁▆▃▂▂▂▂▆▃▂▁` |
| m:microsoftemail | 149 | `▃▆▃▁▄▃▂▂▁▁▃▆▁▁▄▁▄▁▃▂▁▁▃▂▃▂▁▁▂▃▂▂▂▁▃▂▅▅▃▁▃▂▁▄▂▃▄▃▁▂▂▂▂▃▄▃▂▂▃▂▂▃▁▃▅▂▄▂▁▁▁▂▅▅▂▂▁▃▅▅█▃▃▁▃▂▅▂▃▂` |
| m:yahooemail | 137 | `▁▃▃▂▃▂▁▅▂▂▂▂▂▁▂▂▁▁▁▁▂▂▁▂▁▁▃▁▃▂▆▃▁▃▂▃▅▃▂▃▂▅▃▆▆▃▂▅▂▆▂▃▁▃▃▂▁▁▃▂▁▃▂▂▆▁▂▃▅▁▂▅▅▅▃▇▂▅▂▂█▂▃▂▃▁▅▁▆▁` |
| m:spectrum | 59 | `▁▁▁▁▁▃▁▁▁▁▃▃▁▁▁▁▁▁▁▁▁▃▁▁▁▁▁▁▃▁▁▁▁▁▁▃▁▁▃▁▁▃▃▁▁▅▁▃▁▁▁▃▁▁▅███▃▁▃▃██▃▅▅▃▁▃▅▁▃▃█▃▁▁▁▃▁▃▁▁▁▁▅▃▁▁` |
| m:comcast | 33 | `▁▁▃▁▃▁▃▁▁▁▃▆▁▁▁▁▃▃▁▁▃▁▁▁▁▃▁▁▃▁▁▃▁▆▃▃▁▁▃▁▁▁▁▁▁▁▁▁▃█▁▃▁▁▃▃▁▁▁▃▃▁▁▁▁▁▁▁▁▁▃▃▁▁▁▃▁▁▁▆▁▁▁▃▃▁▁▁▁▁` |
| m:alice_it | 21 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▂▁▁▂▃█▅▁` |

### Top feature areas

| Value | Total | Trend |
|:--|--:|:--|
| feat:attachments | 65 | `▂▁▂▁▂▁▁▁▂▂▁▄▂▁▂▁▁▁▁▁▁▁▂▁▁▁▇▁▁▄▁▄▁▁▂▁▁▁▁▂▁▂▂▂▁▂▁▂▁▁▅▁▂▅▁▂▁▂▂▂▄▄▂▂▅▇█▂▄▄▁▁▁▁▄▁▁▂▁▁▂▂▁▁▁▂▁▁▁▁` |
| feat:import_export | 63 | `▁▁▁▃▆▃▁▁▁▆▆▃▃▁▃▃▆▃▁▁▁▁█▁▁▆▁▃█▃▁▁▁▆▁▃▁█▁▃▃█▁▃▆▁▁▁▁▁▁▁▁▃▁▃▁▃▁█▁▆▁▁█▁█▁▁▁▃▃▁▁▁▃▃▁▆▁▃▁▁▁▁▃▃▁▃▁` |
| feat:junk | 58 | `▂▂▁▂▂▂▁▂▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▂▁▁▂▁▄▁▁▁▇▁▂▁█▁▁▁▁▂▄▂▁▁▂▂▁▂▂▁▂▄▄▁▁▂▂▁▁▂▄▁▁▁▂▂▄▂▂▄▄▂▂▄▁▂▄▁▁▁▁▁▁▂▁▁▂▁` |
| feat:addressbook | 50 | `▁▁▁▃▁▁▁▁▁▃▃▁▁▁▁▁▁▁▃▃█▁▁▁▁▃▁▁▁▁▁▆▃▆▁▁▃▃▁▆▁█▃▃▃▃▁▃▁▆▃▆▁▁▁▃▃▃▁▃▁▆▃▁▃▃▁▁▃▃▁▁▁▁▁▁▁▆▁▃▃▁▁▁▁▃▃▁▆▁` |
| feat:filters | 50 | `▁▁▂▂▂▁▁▁▄▁▁▂▁▁▁▂▁▁▂▁▂▁▄▂▂▂▁▁▁▂▁▂▁▄▂▁▁▁▂▂▁▄▁▁▁▁▁▁▁▄▁▁▁▁▁▁▁▂▁▁▁▁▄▁▂▁▂▂▁▂▁▄█▂▄▂▁▂▂▂▂▁▁▁▅▁▁▁▁▁` |
| feat:printing | 50 | `▁▃▁▁▁▁▁▁▁▁▁▁▁▁▂▂▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▆▅▂▁▃▅█▅▂▅▂█▆▂▁▂▂▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### Top protocols

| Value | Total | Trend |
|:--|--:|:--|
| proto:imap | 198 | `▄▄▃▂▅▃▃▂▄▃▃▆▁▁▃▂▃▂▂▂▆▁▃▃▃▅▁▁▄▄▂▃▁▃▃▁▆▃▄▁▁▃▃▇▂▂▄▅▃▂▄▅▃▁▃▄▃▅▂▆▃▂▄▃▄▆▆▅▂▂▅█▂▅▂▆▂▁▇▃▅▄▃▁▃▃▂▂▂▁` |
| proto:pop | 142 | `▂▅▂▁▂▂▃▆▃▆▃▃▁▁▂▃▁▂▁▁▆▃▁▂▂▂▃▂▁▂▅▁▂▅▂▂▃▅▂▃▃▅▃▆▁▁▆▆▁▁▃▃▁▂▂▂▁▂▁▁▅▂▂▂▅▂▅▁▂▂▂█▃▁▃▇▂▁▃▃▃▃▃▂▃▃▃▆▇▁` |
| proto:smtp | 124 | `▁▁▂▂▂▂▁▂▁▄▇█▁▁▂▁▂▄▂▁▁▂▂█▄▁▁▂▂▂▁▂▂▂▁▂▅▁▂▁▂▂▂▄▁▄▄▄▂▁▂▂▂▄▅▄▂▄▂▅▂▄▅▂▅▂▅▄▅▁▄▂▄▅▂▄▂▂▄▅▇▅▅▁▁▅▄▄▁▁` |
| proto:oauth | 59 | `▁▁▁▁▃▁▃▁▁▁▅▅▁▃▃▃▃▁▃▃▁▁▁▅▁▁▁▃▅▃▅▁▁▁▁▁▃▁▁▁▁▅▁▆▃▁▃▁▃▁▃▁▃▁▁▃▁▁▅▁▁▅▃▃▅▃▃▁█▃▁▁▃▅▁▃▁▃▅▁▅▁▃▁▁▃▃▁▁▁` |
| proto:caldav | 6 | `▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁` |
| proto:ews | 6 | `▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█` |

### Top antivirus

| Value | Total | Trend |
|:--|--:|:--|
| av:bitdefender | 10 | `▁▁▅▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▁▅▁▁▁` |
| av:norton | 9 | `▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁█▁█▁` |
| av:defender | 7 | `▁▁▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:mcafee | 6 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁██▁▁` |
| av:avast | 6 | `▁▁▁▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁` |
| av:malwarebytes | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

### OS mix (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| os:windows | 2090 | `▃▄▄▃▄▃▃▃▄▅▄▅▃▃▂▄▄▃▃▃▃▃▅▄▃▅▄▂▄▄▄▄▃▅▃▂▅▄▃▄▄▄▃▅▂▄▅▄▃▃▅▅▄▅▆▅▄▆▄█▅▅▄▃▆▅▇▇▅▃▄▇▅▄▅▅▃▄▅▆▆▅▄▂▃▅▅█▅▁` |
| os:linux | 207 | `▄▂▂▅▃▄▁▁▁▂▂▂▂▁▁▃▂▁▂▃▂▂▂▁▃▅▁▂▅▃▄▂▃▂▄▃▃▂▃▅█▅▁▃▄▂▂▃▄▅▂▃▂▂▂▃▂▂▄▂▂▂▁▄▅▁▂▂▅▂▁▂▄▅▂▂▂▂▂▁▄▂▂▂▁▂▄▁▃▁` |
| os:macos | 156 | `▂▁▅▂▇▁▃▁▇▁▅▂▃▂▃▃▃▃▁▂▅▁▃▁▂▃▃▁▁▂▁▅▂▂▂▂▂▅█▅▃▃▃▂▅▂▂▁▅█▂▆▂▁▃▃▂▅▂▂▃▁▂▃▃▃▂▂▃▂▃▅▅▆▂▆▂▁▂█▂▂▁▂▃▂▅▅▆▁` |
| os:other | 23 | `▁▁▃▃▃▆▃▁▁▁▁▁▃▁▁▁▃▁▃▁▁▁▁▁▃▁▃▁▁▃▁▁▁▁▁▃▁▃▁▁▆▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▃▁▁▁▁█▁▁▁▁▁▃▁▁▁▁▁▁▁▁▃▁▁▁▁▁▁▁▁▁` |
| os:android | 22 | `▁▁▃▃▁▁▁▃▁▃▁▃▃▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▁▁▁▁▁▃▁▁▁▃▁▆▁▁▃▃▁▁▁▁▁█▁▁▁▁▁▁▁▃▁▁▁▁▁▁▆▁▁▁▁▁▁▁▁▁▁▁▁▁▃▁▁▃▁▁▁▁▁▁` |

### macOS releases (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| macos:tahoe | 13 | `▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁▁▅▁▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁█▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:sequoia | 8 | `▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁█▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁` |
| macos:golden_gate | 3 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁█▁` |
| macos:monterey | 3 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:sierra | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:sonoma | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

---

_Notes: spikes detected at **daily** grain (coarser grains catch slow-burn incidents a daily threshold misses — e.g. the March 2026 GMX provider outage). Volume / cause / OS trends span the full scraper history (2023-01+). **Version×cause covers 2026-02 onward** — the native `thunderbird_version` field ([Kitsune PR #7443](https://github.com/mozilla/kitsune/pull/7443)) is only populated from Feb 2026 (~27% → 85% by mid-2026), so earlier questions carry no version; cause-level spikes use all history. Thresholds calibrated on the post-backfill baseline. Full IDs per spike in `PROJECT1/desktop-daily-version-cause-spikes.csv` (version×cause) and `PROJECT1/desktop-daily-single-spikes.csv` (cause-level); full series in `PROJECT1/desktop-daily-rollup.csv`._

_Last updated: 2026-09-25 04:40 UTC_
