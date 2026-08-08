---
layout: base
title: MONTHLY: Thunderbird Desktop — Support Spike Report
---

# MONTHLY: Thunderbird Desktop — Support Spike Report

_Generated 2024-09 … 2026-08 · **monthly** grain · trailing 24 months · 27665 questions · no AI (regex + traditional stats)_

- **Volume:** 27665 questions, 1152.7/month avg
- **Answered (non-creator):** 21406/27665 (77%)
- **First-answer time (median):** 3.3h (p25 0.9h / p75 11.8h)
- **Total volume trend:** `▇█▇▇█▆▆▆▆▅▇▇▆▆▅▅▅▅▅▄▄▄▄▂`

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

## 🚨 Engineering signal — version × cause spikes

Cause clusters over-represented in a specific Thunderbird version. The **Signal** column flags 🆕 **new** (cause never spiked before), ↗ **spreading** (known cause, new version), or ↻ **recurring** (chronic / seen before) — ranked new→spreading→recurring, then by **lift**. Click an ID to read it.


| Signal | Lift | When | Version × Cause | Qs | Served | Trend | Example questions |
|:--|---:|:--|:--|--:|:--|:--|:--|
| 🆕 new | **4.1×** | 2026-06 | v151 × m:spectrum | 12 | 100% ans · 15.8h | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂█▁▂` | [1585052](https://support.mozilla.org/questions/1585052 "get error message ＂Unable to log in at server. Probably wrong configuration, use") [1585941](https://support.mozilla.org/questions/1585941 "Unable to send email") [1586383](https://support.mozilla.org/questions/1586383 "Email Accounts are highlighted RED") [1586405](https://support.mozilla.org/questions/1586405 "The certificate for mobile.charter.net does not come from a trusted source.") [1586446](https://support.mozilla.org/questions/1586446 "Unable to receive and send emails.") [1586481](https://support.mozilla.org/questions/1586481 "Connetion error, can't recieve emails") +6 |
| 🆕 new | **3.2×** | 2026-02 | v148 × proto:oauth | 5 | 100% ans · 4.4h | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▄█▂▁▁▁▁` | [1567488](https://support.mozilla.org/questions/1567488 "dossier envoyés contient seulements le mois en cours") [1567691](https://support.mozilla.org/questions/1567691 "Thunderbird 148.0 breaks AOL authentication") [1567818](https://support.mozilla.org/questions/1567818 "thunderbird update 148 rompe oauth2 de yahoo") [1567961](https://support.mozilla.org/questions/1567961 "Mail sync issue led to Mail disappearing after troubleshooting then selecting ＂c") [1568282](https://support.mozilla.org/questions/1568282 "Thunderbird suddenly started asking for Crendentials for yahoo account.  ＂Someth") |

## 📮 Cause-level spikes — provider / protocol / AV

Causes surging **regardless of version** vs a trailing month baseline — provider/ISP outages and protocol/AV issues. Not necessarily a Thunderbird bug, but worth a triage look. Ranked by magnitude.


| Rise | When | Cause | Qs | Served | Baseline | Trend | Example questions |
|---:|:--|:--|--:|:--|--:|:--|:--|
| **49.0×** | 2025-08 | av:bitdefender | 49 | 100% ans · 2.6h | 1.0 | `▂▁▁▁▃▁▁▁▁▁▁█▂▂▂▁▁▁▂▁▁▁▁▁` | [1528472](https://support.mozilla.org/questions/1528472 "Messagerie illisible (bitdefender)") [1528498](https://support.mozilla.org/questions/1528498 "Recent emails are coming in unformatted and missing subject and sender info (bit") [1528506](https://support.mozilla.org/questions/1528506 "Recent emails are coming in unformatted and missing subject and sender info (bit") [1528543](https://support.mozilla.org/questions/1528543 "Corrupted btinternet emails (bitdefender)") [1528577](https://support.mozilla.org/questions/1528577 "Strange code dominating incoming emails (bitdefender)") [1528582](https://support.mozilla.org/questions/1528582 "my emails are coming in some strange type of figures and numbers starting today ") +43 |
| **7.0×** | 2024-12 | m:orange | 14 | ⚠️ 50% ans · 0.6h | 2.0 | `▄▃▅█▇▅▄▂▃▃▅▄▃▃▃▃▁▃▃▂▁▄▁▁` | [1476744](https://support.mozilla.org/questions/1476744 "Boite mail") [1477337](https://support.mozilla.org/questions/1477337 "suite a une intervention de orange") [1477350](https://support.mozilla.org/questions/1477350 "envoi des messages") [1477378](https://support.mozilla.org/questions/1477378 "impossible d'envoyer mes mails lorsque je suis chez moi en wifi") [1477476](https://support.mozilla.org/questions/1477476 "Paramètres Orange Obsolètes") [1477498](https://support.mozilla.org/questions/1477498 "i cannot inscribe on thunder bird a new code as orange ask me to use thunderbird") +8 |
| **6.8×** | 2025-01 | av:bitdefender | 17 | 88% ans · 3.4h | 2.5 | `▂▁▁▁▃▁▁▁▁▁▁█▂▂▂▁▁▁▂▁▁▁▁▁` | [1482921](https://support.mozilla.org/questions/1482921 "Transferring Thunderbird Profile from Windows 10 Computer to Windows 11 Computer") [1484507](https://support.mozilla.org/questions/1484507 "All'avvio Thunderbird si apre 3 secondo e poi si chiude inaspettatamente") [1484717](https://support.mozilla.org/questions/1484717 "Thunderbird Freezing (＂Not Responding＂) Repeatedly") [1485005](https://support.mozilla.org/questions/1485005 "Thunderbird crashes when trying to open settings, caused by Bitdefender") [1485049](https://support.mozilla.org/questions/1485049 "Thunderbird crashes on startup, caused by Bitdefender") [1485835](https://support.mozilla.org/questions/1485835 "Sent radio buttons do not exist, send unsent email option greyed out under File ") +11 |
| **6.0×** | 2025-08 | m:btinternet | 9 | 89% ans · 10.7h | 1.5 | `▆▄▄▅▄▆▂▃▂▃▂█▄▃▃▅▄▆▂▄▄▄▆▁` | [1528543](https://support.mozilla.org/questions/1528543 "Corrupted btinternet emails (bitdefender)") [1528732](https://support.mozilla.org/questions/1528732 "I have started receiving emails as attached. (bitdefender)") [1528856](https://support.mozilla.org/questions/1528856 "I no longer receive correct emails from Thunderbird.   Each message received sta") [1528919](https://support.mozilla.org/questions/1528919 "receiving emails with no header (bitdefender)") [1529008](https://support.mozilla.org/questions/1529008 "Incoming emails from my BT email account are in gibberish (bitdefender)") [1529260](https://support.mozilla.org/questions/1529260 "Incoming emails into BT internet account lose formatting and attachements") +3 |
| **5.3×** | 2025-12 | m:gmx | 8 | 88% ans · 17.0h | 1.5 | `▁▂▃▅▃▂▂▁▁▁▁▂▃▂▁▅▂▃█▃▂▂▃▁` | [1552704](https://support.mozilla.org/questions/1552704 "GMX IMAP Login Failure") [1553040](https://support.mozilla.org/questions/1553040 "Login to the server pop.gmx.net with username ＂...＂ failed.") [1555220](https://support.mozilla.org/questions/1555220 "warum verlangt https://caldav.gmx.net verlangt einen Benutzernamen und ein Passw") [1555687](https://support.mozilla.org/questions/1555687 "Account creation not possible despite confirmed login credentials") [1556443](https://support.mozilla.org/questions/1556443 "cannot receive mails in my inbox, basis is GMX") [1556657](https://support.mozilla.org/questions/1556657 "Ich kann mit Thunderbird keine Emails mehr versenden u. empfangen und mittlerwei") +2 |
| **5.0×** | 2025-07 | m:verizon | 10 | 80% ans · 3.0h | 2.0 | `▃▃▅▅▂▃▂▂▁▄█▃▂▄▇▃▁▁▂▂▄▂▂▁` | [1520698](https://support.mozilla.org/questions/1520698 "add an email account") [1522140](https://support.mozilla.org/questions/1522140 "Help please - Thunderbird not fetching POP messages") [1523889](https://support.mozilla.org/questions/1523889 "Create an account to access aol/verizon.net email. This should be simple.") [1523914](https://support.mozilla.org/questions/1523914 "verizon.net account  changing from IMAP to POP3") [1524787](https://support.mozilla.org/questions/1524787 "After Thunderbird update email send doesnt work") [1524985](https://support.mozilla.org/questions/1524985 "Email") +4 |
| **4.3×** | 2026-03 | m:gmx | 15 | 87% ans · 11.2h | 3.5 | `▁▂▃▅▃▂▂▁▁▁▁▂▃▂▁▅▂▃█▃▂▂▃▁` | [1568896](https://support.mozilla.org/questions/1568896 "Do I need GMX-TopMail or works Thunderbird with FreeMail too?") [1569586](https://support.mozilla.org/questions/1569586 "Ich kann auf meinem Computer keine Mails mehr empfangen , auf dem Handy geht es.") [1569730](https://support.mozilla.org/questions/1569730 "After authenticating one Yahoo account (Oauth2), my second Yahoo account has bec") [1570170](https://support.mozilla.org/questions/1570170 "Cannot Link To My Email Server.....") [1570366](https://support.mozilla.org/questions/1570366 "J'ai déjà un mail gmx , ＂andre.et@gmx.fr＂ est-ce cette adresse qui est crypter ?") [1570603](https://support.mozilla.org/questions/1570603 "problem to add account gmx email") +9 |
| **3.2×** | 2025-07 | av:norton | 8 | 75% ans · 2.1h | 2.5 | `▅▄▅▃█▃▄▂▂▂▆▅▃▃▂▂▂▂▂▂▃▂▃▁` | [1521509](https://support.mozilla.org/questions/1521509 "problem with auto renewal with my domain registrar hostgator, adotname, and the ") [1521569](https://support.mozilla.org/questions/1521569 "not working (locked)") [1522509](https://support.mozilla.org/questions/1522509 "Unable to receive e-mails on Thunderbird, I am prompted to enter a password for ") [1523331](https://support.mozilla.org/questions/1523331 "Migrating Thunderbird 140 To A New Windows Computer. SOLVED Norton 360 was causi") [1523343](https://support.mozilla.org/questions/1523343 "Peer certification expiration") [1523519](https://support.mozilla.org/questions/1523519 "email conver to event not working.") +2 |
| **3.0×** | 2024-09 | proto:oauth | 66 | 82% ans · 1.7h | 22.0 | `█▆▄▄▄▂▃▃▂▂▃▃▂▃▃▂▃▃▅▂▃▂▃▁` | [1461626](https://support.mozilla.org/questions/1461626 "thunderbird 128.1.1esr on macbook pro") [1462076](https://support.mozilla.org/questions/1462076 "Can TB hide its client ID when it connects?") [1462199](https://support.mozilla.org/questions/1462199 "Trying to do Microsoft/Thunderbird authentication before Sept 16, 2024") [1462200](https://support.mozilla.org/questions/1462200 "dual authentication not allowing emails") [1462785](https://support.mozilla.org/questions/1462785 "Oauth2 selection option missing in SMTP server setup") [1462816](https://support.mozilla.org/questions/1462816 "Ghost folders with outlook server") +60 |

## 📈 Trends

### Top versions

| Value | Total | Trend |
|:--|--:|:--|
| v140 | 963 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▄▅▇█▇▇▂` |
| v150 | 430 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▄█▁▂▁` |
| v152 | 375 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▆█▁` |
| v151 | 332 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▆█▁▁` |
| v149 | 313 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂█▂▁▁▁` |
| v148 | 238 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃█▁▁▁▁▁` |

### Top mail providers

| Value | Total | Trend |
|:--|--:|:--|
| m:gmail | 2464 | `██▇▇▇▆▆▆▅▄▅▆▆▅▅▅▅▄▅▄▄▃▄▂` |
| m:microsoftemail | 1988 | `██▆▅▅▅▄▄▃▃▄▄▄▅▄▄▄▄▄▃▄▃▂▂` |
| m:yahooemail | 809 | `▆▅▄▅▆▃▄▃▃▄▇▆▆▆▇▄▄▇█▅▆▄▅▃` |
| m:comcast | 348 | `▆▆▆▅▆▄▅▄▄▃▃█▄▄▆▅▂▃▃▅▄▄▄▂` |
| m:spectrum | 278 | `█▇▄▅▅▇▅▅▅▅▅▆▆▃▇▅▄▆▃▃██▃▂` |
| m:att | 189 | `▄▄▅██▅▃▃▅▃▇▇▃▂▄▆▃▃▅▃▂▂▃▁` |

### Top protocols

| Value | Total | Trend |
|:--|--:|:--|
| proto:imap | 1896 | `█▇▇██▇▅▅▅▄▆▆▅▆▅▄▅▄▅▃▅▄▄▂` |
| proto:smtp | 1204 | `█▇▇▅▇▅▅▅▅▄▅▇▅▄▄▃▅▅▅▃▄▃▄▂` |
| proto:pop | 1188 | `█▇█▆█▆▄▅▅▅▆▇▅▆▄▃▅▄▄▄▄▃▅▂` |
| proto:oauth | 482 | `█▆▄▄▄▂▃▃▂▂▃▃▂▃▃▂▃▃▅▂▃▂▃▁` |
| proto:caldav | 97 | `▅▆▆▅█▃▃▃▆▅▆▄▃▄▂▃▅▆▃▃▂▃▃▁` |
| proto:carddav | 53 | `▃▄▅▃▄▂▇▃▂▁▃█▂▃▃▂▂▄▅▄▂▂▂▁` |

### Top antivirus

| Value | Total | Trend |
|:--|--:|:--|
| av:bitdefender | 115 | `▂▁▁▁▃▁▁▁▁▁▁█▂▂▂▁▁▁▂▁▁▁▁▁` |
| av:norton | 89 | `▅▄▅▃█▃▄▂▂▂▆▅▃▃▂▂▂▂▂▂▃▂▃▁` |
| av:defender | 51 | `▄▂█▃▂▃▂▃▃▁▃▃▃▃▃▁▁▂▃▂▄▄▃▁` |
| av:avast | 50 | `▅▂▇▄▅█▄▅▂▁▅▁▁▄▇▂▅▂▂▇▄▄▄▂` |
| av:mcafee | 32 | `▁█▃▆▃▃▃▆█▃▃█▆█▁▁▁▃▃▆▆▃▃▁` |
| av:kaspersky | 22 | `▆▆▃▁▅▁▃▁▆▅▁█▁▃▃▁▁▃▁▁▁▁▁▁` |

### OS mix (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| os:windows | 6726 | `▂▃▃▂▃▂▂▂▂▂▃▃▂▃▂▂▅██▇▇▇▇▂` |
| os:linux | 1223 | `▆▆▆▅▆▅▃▄▅▄▃▅▅▄▄▄▆▇█▆▇▆▆▄` |
| os:macos | 830 | `▄▄▃▃▃▄▃▃▃▂▄▄▄▂▄▂▆▇█▆▆▅▅▃` |
| os:other | 128 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▄▂▁▂▃▃▂` |
| os:android | 87 | `▁▂▁▁▂▂▂▂▁▂▃▃▁▂▂▁▇█▇█▅▃▅▃` |

### macOS releases (filter dimension)

| Value | Total | Trend |
|:--|--:|:--|
| macos:sequoia | 156 | `▃▅▆▅█▇▅▅▅▁▇▇▇▂▅▃▄▃▃▂▃▁▂▁` |
| macos:sonoma | 53 | `█▅▃▃▂▃▁▁▁▁▁▁▁▁▃▂▃▁▁▁▂▁▁▁` |
| macos:tahoe | 52 | `▁▁▁▁▁▁▁▁▁▁▁▁▆▅█▇▇▆▆▂▃▅▆▃` |
| macos:catalina | 36 | `▃▅▃▂▄▁▂▂▂▁█▆▄▂▂▁▂▁▂▂▂▁▁▁` |
| macos:monterey | 31 | `▆▅▅▅▅▅█▃▃▁▃▃▅▁▅▃▃▁▁▃▃▁▃▃` |
| macos:high_sierra | 28 | `▄█▄▂▁▇▂▁▇▁▂▂▂▁▂▂▄▁▁▁▁▄▁▁` |

---

_Notes: spikes detected at **monthly** grain (coarser grains catch slow-burn incidents a daily threshold misses — e.g. the March 2026 GMX provider outage). Volume / cause / OS trends span the full scraper history (2023-01+). **Version×cause covers 2026-02 onward** — the native `thunderbird_version` field ([Kitsune PR #7443](https://github.com/mozilla/kitsune/pull/7443)) is only populated from Feb 2026 (~27% → 85% by mid-2026), so earlier questions carry no version; cause-level spikes use all history. Thresholds calibrated on the post-backfill baseline. Full IDs per spike in `PROJECT1/desktop-monthly-version-cause-spikes.csv` (version×cause) and `PROJECT1/desktop-monthly-single-spikes.csv` (cause-level); full series in `PROJECT1/desktop-monthly-rollup.csv`._

_Last updated: 2026-08-08 04:47 UTC_
