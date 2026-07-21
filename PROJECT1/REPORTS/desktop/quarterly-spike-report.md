---
layout: base
title: QUARTERLY: Thunderbird Desktop — Support Spike Report
---

# QUARTERLY: Thunderbird Desktop — Support Spike Report

_Generated 2023-Q4 … 2026-Q3 · **quarterly** grain · trailing 12 quarters · 39949 questions · no AI (regex + traditional stats)_

- **Volume:** 39949 questions, 3329.1/quarter avg
- **Answered (non-creator):** 30182/39949 (76%)
- **First-answer time (median):** 3.5h (p25 1.0h / p75 12.3h)
- **Total volume trend:** `▇▆▅██▇▆▇▆▅▄▂`

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

## 🚨 Engineering signal — version × cause spikes

Cause clusters over-represented in a specific Thunderbird version. The **Signal** column flags 🆕 **new** (cause never spiked before), ↗ **spreading** (known cause, new version), or ↻ **recurring** (chronic / seen before) — ranked new→spreading→recurring, then by **lift**. Click an ID to read it.


| Signal | Lift | When | Version × Cause | Qs | Served | Trend | Example questions |
|:--|---:|:--|:--|--:|:--|:--|:--|
| 🆕 new | **3.9×** | 2026-06 | v151 × m:spectrum | 12 | 100% ans · 15.8h | `▁▁▁▁▁▁▁▁▁▁█▁` | [1585052](https://support.mozilla.org/questions/1585052 "get error message ＂Unable to log in at server. Probably wrong configuration, use") [1585941](https://support.mozilla.org/questions/1585941 "Unable to send email") [1586383](https://support.mozilla.org/questions/1586383 "Email Accounts are highlighted RED") [1586405](https://support.mozilla.org/questions/1586405 "The certificate for mobile.charter.net does not come from a trusted source.") [1586446](https://support.mozilla.org/questions/1586446 "Unable to receive and send emails.") [1586481](https://support.mozilla.org/questions/1586481 "Connetion error, can't recieve emails") +6 |
| 🆕 new | **3.1×** | 2026-02 | v148 × m:yahooemail | 9 | 100% ans · 2.5h | `▁▁▁▁▁▁▁▁▁█▁▁` | [1567691](https://support.mozilla.org/questions/1567691 "Thunderbird 148.0 breaks AOL authentication") [1567818](https://support.mozilla.org/questions/1567818 "thunderbird update 148 rompe oauth2 de yahoo") [1567871](https://support.mozilla.org/questions/1567871 "Login problem after Thunderbird 148.0 (64-bit) (update) as a client for Yahoo ac") [1567897](https://support.mozilla.org/questions/1567897 "Since v148.0 I cannot use my yahoo and AOL account why?") [1567998](https://support.mozilla.org/questions/1567998 "Duplicate email messages downloading to both my mailboxes") [1568124](https://support.mozilla.org/questions/1568124 "Since installing Thunderbird 148 my yahoo pop connection times out") +3 |
| 🆕 new | **3.1×** | 2026-02 | v148 × proto:oauth | 5 | 100% ans · 4.4h | `▁▁▁▁▁▁▁▁▁█▁▁` | [1567488](https://support.mozilla.org/questions/1567488 "dossier envoyés contient seulements le mois en cours") [1567691](https://support.mozilla.org/questions/1567691 "Thunderbird 148.0 breaks AOL authentication") [1567818](https://support.mozilla.org/questions/1567818 "thunderbird update 148 rompe oauth2 de yahoo") [1567961](https://support.mozilla.org/questions/1567961 "Mail sync issue led to Mail disappearing after troubleshooting then selecting ＂c") [1568282](https://support.mozilla.org/questions/1568282 "Thunderbird suddenly started asking for Crendentials for yahoo account.  ＂Someth") |

## 📮 Cause-level spikes — provider / protocol / AV

Causes surging **regardless of version** vs a trailing month baseline — provider/ISP outages and protocol/AV issues. Not necessarily a Thunderbird bug, but worth a triage look. Ranked by magnitude.


| Rise | When | Cause | Qs | Served | Baseline | Trend | Example questions |
|---:|:--|:--|--:|:--|--:|:--|:--|
| **49.0×** | 2025-08 | av:bitdefender | 49 | 100% ans · 2.6h | 1.0 | `▂▂▁▂▂▄▂█▂▂▂▁` | [1528472](https://support.mozilla.org/questions/1528472 "Messagerie illisible (bitdefender)") [1528498](https://support.mozilla.org/questions/1528498 "Recent emails are coming in unformatted and missing subject and sender info (bit") [1528506](https://support.mozilla.org/questions/1528506 "Recent emails are coming in unformatted and missing subject and sender info (bit") [1528543](https://support.mozilla.org/questions/1528543 "Corrupted btinternet emails (bitdefender)") [1528577](https://support.mozilla.org/questions/1528577 "Strange code dominating incoming emails (bitdefender)") [1528582](https://support.mozilla.org/questions/1528582 "my emails are coming in some strange type of figures and numbers starting today ") +43 |
| **30.0×** | 2023-10 | m:frontier | 15 | ⚠️ 53% ans · 7.9h | 0.5 | `█▂▂▂▄▂▂▂▂▁▂▁` | [1426135](https://support.mozilla.org/questions/1426135 "Email not working after update to SuperNova?  Multiple - gmail, dreamhost, front") [1426500](https://support.mozilla.org/questions/1426500 "Thunderbird Version	119.0b3 - hangs") [1426532](https://support.mozilla.org/questions/1426532 "Thunderbird downloading messages from frontier.com") [1426537](https://support.mozilla.org/questions/1426537 "using Frontier.com for email.  TB v 102 stopped working yesterday.  Updated to v") [1426556](https://support.mozilla.org/questions/1426556 "Tbird 115.2.1 stopped downloading emails on all accounts.") [1426687](https://support.mozilla.org/questions/1426687 "URGENT REQUEST FOR 'basic' HELP - My Email-setting has been changed by 'SKYPE'..") +9 |
| **7.0×** | 2024-12 | m:orange | 14 | ⚠️ 50% ans · 0.6h | 2.0 | `▂▂▂▃██▃▆▄▄▃▁` | [1476744](https://support.mozilla.org/questions/1476744 "Boite mail") [1477337](https://support.mozilla.org/questions/1477337 "suite a une intervention de orange") [1477350](https://support.mozilla.org/questions/1477350 "envoi des messages") [1477378](https://support.mozilla.org/questions/1477378 "impossible d'envoyer mes mails lorsque je suis chez moi en wifi") [1477476](https://support.mozilla.org/questions/1477476 "Paramètres Orange Obsolètes") [1477498](https://support.mozilla.org/questions/1477498 "i cannot inscribe on thunder bird a new code as orange ask me to use thunderbird") +8 |
| **6.8×** | 2025-01 | av:bitdefender | 17 | 88% ans · 3.4h | 2.5 | `▂▂▁▂▂▄▂█▂▂▂▁` | [1482921](https://support.mozilla.org/questions/1482921 "Transferring Thunderbird Profile from Windows 10 Computer to Windows 11 Computer") [1484507](https://support.mozilla.org/questions/1484507 "All'avvio Thunderbird si apre 3 secondo e poi si chiude inaspettatamente") [1484717](https://support.mozilla.org/questions/1484717 "Thunderbird Freezing (＂Not Responding＂) Repeatedly") [1485005](https://support.mozilla.org/questions/1485005 "Thunderbird crashes when trying to open settings, caused by Bitdefender") [1485049](https://support.mozilla.org/questions/1485049 "Thunderbird crashes on startup, caused by Bitdefender") [1485835](https://support.mozilla.org/questions/1485835 "Sent radio buttons do not exist, send unsent email option greyed out under File ") +11 |
| **6.0×** | 2025-08 | m:btinternet | 9 | 89% ans · 10.7h | 1.5 | `▃▆██▆▆▃▇▅▆▆▂` | [1528543](https://support.mozilla.org/questions/1528543 "Corrupted btinternet emails (bitdefender)") [1528732](https://support.mozilla.org/questions/1528732 "I have started receiving emails as attached. (bitdefender)") [1528856](https://support.mozilla.org/questions/1528856 "I no longer receive correct emails from Thunderbird.   Each message received sta") [1528919](https://support.mozilla.org/questions/1528919 "receiving emails with no header (bitdefender)") [1529008](https://support.mozilla.org/questions/1529008 "Incoming emails from my BT email account are in gibberish (bitdefender)") [1529260](https://support.mozilla.org/questions/1529260 "Incoming emails into BT internet account lose formatting and attachements") +3 |
| **6.0×** | 2024-05 | m:cox | 24 | 92% ans · 3.9h | 4.0 | `▂▂█▃▂▂▂▂▁▁▁▁` | [1446257](https://support.mozilla.org/questions/1446257 "Cox / yahoo - User Name keeps changing. The fix I read does not work for me in 2") [1446337](https://support.mozilla.org/questions/1446337 "Cox moving email services to Yahoo") [1446412](https://support.mozilla.org/questions/1446412 "Thunderbird vs the Cox email to Yahoo email migration") [1446501](https://support.mozilla.org/questions/1446501 "New cox.net email") [1446525](https://support.mozilla.org/questions/1446525 "Transitioning to Yahoo from Cox") [1446535](https://support.mozilla.org/questions/1446535 "Rearrange email domains in the left tool box?") +18 |
| **6.0×** | 2024-04 | m:cox | 24 | 83% ans · 6.2h | 4.0 | `▂▂█▃▂▂▂▂▁▁▁▁` | [1443922](https://support.mozilla.org/questions/1443922 "Switching from COX Internet to a competitors 5G wireless network for internet.") [1444186](https://support.mozilla.org/questions/1444186 "email from yahoo") [1444249](https://support.mozilla.org/questions/1444249 "Thunderbird v115.9.0 (32-bit) not sending Yahoo email") [1444457](https://support.mozilla.org/questions/1444457 "Can't send a message with Mozilla Thunderbird - just hangs - no error message") [1444635](https://support.mozilla.org/questions/1444635 "Cox email") [1444650](https://support.mozilla.org/questions/1444650 "Email service") +18 |
| **5.3×** | 2025-12 | m:gmx | 8 | 88% ans · 17.0h | 1.5 | `▄▂▂▅▆▄▂▃▄█▄▂` | [1552704](https://support.mozilla.org/questions/1552704 "GMX IMAP Login Failure") [1553040](https://support.mozilla.org/questions/1553040 "Login to the server pop.gmx.net with username ＂...＂ failed.") [1555220](https://support.mozilla.org/questions/1555220 "warum verlangt https://caldav.gmx.net verlangt einen Benutzernamen und ein Passw") [1555687](https://support.mozilla.org/questions/1555687 "Account creation not possible despite confirmed login credentials") [1556443](https://support.mozilla.org/questions/1556443 "cannot receive mails in my inbox, basis is GMX") [1556657](https://support.mozilla.org/questions/1556657 "Ich kann mit Thunderbird keine Emails mehr versenden u. empfangen und mittlerwei") +2 |
| **5.0×** | 2025-07 | m:verizon | 10 | 80% ans · 3.0h | 2.0 | `▄▅▅█▆▄▃▇▇▁▃▁` | [1520698](https://support.mozilla.org/questions/1520698 "add an email account") [1522140](https://support.mozilla.org/questions/1522140 "Help please - Thunderbird not fetching POP messages") [1523889](https://support.mozilla.org/questions/1523889 "Create an account to access aol/verizon.net email. This should be simple.") [1523914](https://support.mozilla.org/questions/1523914 "verizon.net account  changing from IMAP to POP3") [1524787](https://support.mozilla.org/questions/1524787 "After Thunderbird update email send doesnt work") [1524985](https://support.mozilla.org/questions/1524985 "Email") +4 |
| **4.5×** | 2024-06 | m:verizon | 9 | 89% ans · 34.0h | 2.0 | `▄▅▅█▆▄▃▇▇▁▃▁` | [1448843](https://support.mozilla.org/questions/1448843 "i mistakingly deleted my primary password. i cant remember it and even though i ") [1448978](https://support.mozilla.org/questions/1448978 "Sending Problem") [1450147](https://support.mozilla.org/questions/1450147 "Signing into Primary Email (rshearin@verizon.net) on Yahoo Mail is not working.") [1450157](https://support.mozilla.org/questions/1450157 "Email password issues with Verizon") [1450250](https://support.mozilla.org/questions/1450250 "Thunderbird email login missing") [1450350](https://support.mozilla.org/questions/1450350 "AOL login stopped working") +3 |
| **4.4×** | 2024-06 | m:att | 20 | 80% ans · 3.4h | 4.5 | `▇▃█▇█▇▅█▅▅▃▁` | [1448967](https://support.mozilla.org/questions/1448967 "Downloading email from AT&T") [1449518](https://support.mozilla.org/questions/1449518 "Can't receive/send email") [1450074](https://support.mozilla.org/questions/1450074 "Thunderbird Error Message") [1450110](https://support.mozilla.org/questions/1450110 "inbound failure") [1450112](https://support.mozilla.org/questions/1450112 "Thunderbird stopped sending and receiving email suddenly.") [1450120](https://support.mozilla.org/questions/1450120 "ATT POP3 email just stopped working for no reason") +14 |
| **4.3×** | 2026-03 | m:gmx | 15 | 87% ans · 11.2h | 3.5 | `▄▂▂▅▆▄▂▃▄█▄▂` | [1568896](https://support.mozilla.org/questions/1568896 "Do I need GMX-TopMail or works Thunderbird with FreeMail too?") [1569586](https://support.mozilla.org/questions/1569586 "Ich kann auf meinem Computer keine Mails mehr empfangen , auf dem Handy geht es.") [1569730](https://support.mozilla.org/questions/1569730 "After authenticating one Yahoo account (Oauth2), my second Yahoo account has bec") [1570170](https://support.mozilla.org/questions/1570170 "Cannot Link To My Email Server.....") [1570366](https://support.mozilla.org/questions/1570366 "J'ai déjà un mail gmx , ＂andre.et@gmx.fr＂ est-ce cette adresse qui est crypter ?") [1570603](https://support.mozilla.org/questions/1570603 "problem to add account gmx email") +9 |
| **4.0×** | 2024-06 | m:cox | 16 | 81% ans · 1.9h | 4.0 | `▂▂█▃▂▂▂▂▁▁▁▁` | [1448821](https://support.mozilla.org/questions/1448821 "Spam in TB115 / Cox in Yahoo") [1448920](https://support.mozilla.org/questions/1448920 "Can't get messages from Yahoo mail") [1449059](https://support.mozilla.org/questions/1449059 "Help with configuring account with specific situation") [1449124](https://support.mozilla.org/questions/1449124 "Thunderbird switching servers on my two accounts") [1449230](https://support.mozilla.org/questions/1449230 "accessing email on yahoo servers using thunderbird") [1449525](https://support.mozilla.org/questions/1449525 "Cannot make account with Yahoo in Thunderbird") +10 |
| **3.6×** | 2024-07 | proto:oauth | 49 | 88% ans · 1.7h | 13.5 | `▃▂▄█▅▃▃▃▃▄▃▂` | [1451249](https://support.mozilla.org/questions/1451249 "Email from Microsoft to update Authentication to Oauth") [1451303](https://support.mozilla.org/questions/1451303 "Microsoft Modern Authentication") [1451325](https://support.mozilla.org/questions/1451325 "Microsoft Oauth2 authentification - option not available for outgoing server") [1451346](https://support.mozilla.org/questions/1451346 "Microsoft is changing the authentication method") [1451376](https://support.mozilla.org/questions/1451376 "Reinstalling Google mail") [1451397](https://support.mozilla.org/questions/1451397 "OAuth2 - Passwords not reliably saved.") +43 |
| **3.6×** | 2024-07 | m:att | 16 | 69% ans · 1.6h | 4.5 | `▇▃█▇█▇▅█▅▅▃▁` | [1451218](https://support.mozilla.org/questions/1451218 "Email issues") [1451269](https://support.mozilla.org/questions/1451269 "ATT.net") [1451284](https://support.mozilla.org/questions/1451284 "can't log into my inbound email server At&t") [1451307](https://support.mozilla.org/questions/1451307 "can't get in") [1451574](https://support.mozilla.org/questions/1451574 "unable to receive and send emails thru inbound.att.net and outbound.att.net") [1451715](https://support.mozilla.org/questions/1451715 "Inbound emails from ATT") +10 |
| **3.2×** | 2025-07 | av:norton | 8 | 75% ans · 2.1h | 2.5 | `▃▂▅█▆█▃▇▃▃▄▁` | [1521509](https://support.mozilla.org/questions/1521509 "problem with auto renewal with my domain registrar hostgator, adotname, and the ") [1521569](https://support.mozilla.org/questions/1521569 "not working (locked)") [1522509](https://support.mozilla.org/questions/1522509 "Unable to receive e-mails on Thunderbird, I am prompted to enter a password for ") [1523331](https://support.mozilla.org/questions/1523331 "Migrating Thunderbird 140 To A New Windows Computer. SOLVED Norton 360 was causi") [1523343](https://support.mozilla.org/questions/1523343 "Peer certification expiration") [1523519](https://support.mozilla.org/questions/1523519 "email conver to event not working.") +2 |
| **3.2×** | 2024-07 | m:virginmedia | 8 | 75% ans · 4.9h | 2.5 | `▃▅▅█▅▆▂▃▃▃▃▁` | [1451235](https://support.mozilla.org/questions/1451235 "Cannot send messages") [1451251](https://support.mozilla.org/questions/1451251 "Email") [1451478](https://support.mozilla.org/questions/1451478 "Sending emails") [1451612](https://support.mozilla.org/questions/1451612 "thunderbirds does not recognise my new virgin media password, I have tried creat") [1451720](https://support.mozilla.org/questions/1451720 "Outgoing e-mails") [1452048](https://support.mozilla.org/questions/1452048 "Since Version 115.12.2 ¦ Released June 22, 2024 can receive but not send emails ") +2 |
| **3.1×** | 2024-08 | av:defender | 11 | 64% ans · 2.2h | 3.5 | `▅▇▄█▅▃▂▄▂▂▄▁` | [1456877](https://support.mozilla.org/questions/1456877 "Thunderibrd upgrade to 115 is sluggish.  SOLVED by creating an exception in Defe") [1457294](https://support.mozilla.org/questions/1457294 "Thunderbird 128 (Nebula) Hangs Constantly.  SOLVED caused by Microsoft Defender ") [1457557](https://support.mozilla.org/questions/1457557 "Message ＂Login to server with username failed＂ after software update") [1457806](https://support.mozilla.org/questions/1457806 "a trojan has been identified in an smtp folder how to spot and eliminate") [1457949](https://support.mozilla.org/questions/1457949 "Thunderbird slow downloading/opening email") [1458157](https://support.mozilla.org/questions/1458157 "Cannot delete IMAP Folder") +5 |
| **3.1×** | 2024-05 | m:att | 14 | 71% ans · 2.5h | 4.5 | `▇▃█▇█▇▅█▅▅▃▁` | [1446408](https://support.mozilla.org/questions/1446408 "Cannot connect to att.net account on computer") [1446596](https://support.mozilla.org/questions/1446596 "Reinstall") [1446656](https://support.mozilla.org/questions/1446656 "Unable to sign into Thunderbird Email") [1447039](https://support.mozilla.org/questions/1447039 "Can't reestablish AT&T account in TB") [1447055](https://support.mozilla.org/questions/1447055 "not getting certain emails") [1447077](https://support.mozilla.org/questions/1447077 "Mozilla Thunderbird") +8 |
| **3.0×** | 2024-09 | proto:oauth | 66 | 82% ans · 1.7h | 22.0 | `▃▂▄█▅▃▃▃▃▄▃▂` | [1461626](https://support.mozilla.org/questions/1461626 "thunderbird 128.1.1esr on macbook pro") [1462076](https://support.mozilla.org/questions/1462076 "Can TB hide its client ID when it connects?") [1462199](https://support.mozilla.org/questions/1462199 "Trying to do Microsoft/Thunderbird authentication before Sept 16, 2024") [1462200](https://support.mozilla.org/questions/1462200 "dual authentication not allowing emails") [1462785](https://support.mozilla.org/questions/1462785 "Oauth2 selection option missing in SMTP server setup") [1462816](https://support.mozilla.org/questions/1462816 "Ghost folders with outlook server") +60 |

## 📈 Trends

### Top versions

| Value | Total | Trend |
|:--|--:|:--|
| v140 | 872 | `▁▁▁▁▁▁▁▁▁▄█▂` |
| v150 | 415 | `▁▁▁▁▁▁▁▁▁▁█▁` |
| v152 | 336 | `▁▁▁▁▁▁▁▁▁▁▇█` |
| v151 | 327 | `▁▁▁▁▁▁▁▁▁▁█▁` |
| v149 | 312 | `▁▁▁▁▁▁▁▁▁▂█▁` |
| v148 | 238 | `▁▁▁▁▁▁▁▁▁█▁▁` |

### Top mail providers

| Value | Total | Trend |
|:--|--:|:--|
| m:gmail | 3668 | `▆▆▅██▆▅▆▅▅▄▂` |
| m:microsoftemail | 2982 | `▅▅▄█▇▅▄▅▄▄▄▁` |
| m:yahooemail | 1135 | `▅▄█▇▆▅▄█▇█▆▂` |
| m:comcast | 515 | `▅▇▆██▇▅▇▇▃▆▂` |
| m:spectrum | 435 | `█▆▄▇▅▆▅▆▅▄▆▁` |
| m:att | 293 | `▇▃█▇█▇▅█▅▅▃▁` |

### Top protocols

| Value | Total | Trend |
|:--|--:|:--|
| proto:imap | 2827 | `▆▆▆██▇▅▆▅▅▄▂` |
| proto:smtp | 1804 | `▆▆▆█▇▆▅▆▄▅▃▂` |
| proto:pop | 1771 | `▅▅▄█▇▆▅▆▅▄▄▂` |
| proto:oauth | 704 | `▃▂▄█▅▃▃▃▃▄▃▂` |
| proto:caldav | 135 | `▆▆▃▆█▇▆▆▄▆▄▁` |
| proto:carddav | 75 | `▄▅▅▇▇█▃█▅▇▅▂` |

### Top antivirus

| Value | Total | Trend |
|:--|--:|:--|
| av:bitdefender | 129 | `▂▂▁▂▂▄▂█▂▂▂▁` |
| av:norton | 121 | `▃▂▅█▆█▃▇▃▃▄▁` |
| av:defender | 101 | `▅▇▄█▅▃▂▄▂▂▄▁` |
| av:avast | 81 | `██▄▅▅▇▃▃▅▄▆▂` |
| av:mcafee | 36 | `▅▂▂▁█▅██▅▃▇▁` |
| av:kaspersky | 34 | `▇▅▂█▆▅▇▆▃▂▁▁` |

### OS mix (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| os:windows | 7697 | `▃▂▂▃▃▃▂▃▃██▂` |
| os:linux | 1637 | `▆▅▄▆▆▅▅▅▅█▇▂` |
| os:macos | 1095 | `▄▄▃▄▄▄▃▅▃█▇▂` |
| os:other | 123 | `▁▁▁▁▁▁▁▁▁█▃▂` |
| os:android | 92 | `▁▂▂▂▁▂▂▂▂█▆▂` |

### macOS releases (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| macos:sonoma | 164 | `▄▇▅█▃▂▁▁▂▂▁▁` |
| macos:sequoia | 155 | `▁▁▁▂▆█▄█▄▃▂▁` |
| macos:ventura | 66 | `█▂▂▂▂▂▂▃▂▁▁▁` |
| macos:monterey | 53 | `▆█▆▅▆▇▃▄▃▂▃▁` |
| macos:catalina | 51 | `▃▂▃▃▄▃▂█▂▂▂▁` |
| macos:tahoe | 48 | `▁▁▁▁▁▁▁▃██▄▂` |

---

_Notes: spikes detected at **monthly** grain (coarser grains catch slow-burn incidents a daily threshold misses — e.g. the March 2026 GMX provider outage). Volume / cause / OS trends span the full scraper history (2023-01+). **Version×cause covers 2026-02 onward** — the native `thunderbird_version` field ([Kitsune PR #7443](https://github.com/mozilla/kitsune/pull/7443)) is only populated from Feb 2026 (~27% → 85% by mid-2026), so earlier questions carry no version; cause-level spikes use all history. Thresholds calibrated on the post-backfill baseline. Full IDs per spike in `PROJECT1/desktop-monthly-version-cause-spikes.csv` (version×cause) and `PROJECT1/desktop-monthly-single-spikes.csv` (cause-level); full series in `PROJECT1/desktop-quarterly-rollup.csv`._

_Last updated: 2026-07-21 17:00 UTC_
