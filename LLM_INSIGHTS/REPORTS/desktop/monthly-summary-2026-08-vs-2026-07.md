---
layout: base
title: Desktop LLM Insights — August 2026
---

# Thunderbird Desktop — LLM Insights (Engineering)

## August 2026 vs July 2026

_The **AI counterpart to Project 1**: Claude reads every support question (plus the creator's own follow-ups, the accepted solution, and trusted-contributor replies), names the concrete problem, hypothesises a root cause, and rates severity — surfacing emerging / worst-served pain that regex + stats can't. Counts are exact (computed in Python); clustering and prose are LLM-derived. A triage pointer, not proof._

## Headline

| | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 731 | 940 | ▲ +209 (+29%) |
| Distinct issue clusters | 87 | 98 | ▲ +11 |
| New issue clusters this month | — | 0 | |

**Support volume up 29% (731→940) with no new clusters — the surge is concentrated in a blank-page attachment printing regression, a Spectrum/Charter mail outage pattern, and startup crashes, while Microsoft OAuth remains the worst-served pain point.**

**Outcome first:** August added ~209 questions over July with zero genuinely new clusters, meaning existing defects are amplifying rather than new surface area appearing. Three categories carry nearly all the growth: attachments (17→55, 3.2x), performance-crash (29→69, 2.4x), and send-receive (122→169). The single sharpest movers are rank 1 (blank-page printing, 2→39) and rank 2 (Spectrum/Charter/Roadrunner download failures, 2→36) — both went from noise to top-of-list in one month, which is the classic shape of a shipped regression or an upstream provider change.

**Where users are being failed worst:** rank 11 (Microsoft/Office365 OAuth) is only 29% resolved with 53% of questions unanswered at severity 4.1 — support has no playbook and engineering has no documented fix path. Rank 4 (IMAP silently stops until restart) and rank 9 (slow/memory-leak performance) sit at 47%/37% resolved with ~40% unanswered. These are low-volume-per-thread but high-frustration; they are diagnosis problems, not staffing problems, and only engineering can unblock them.

**Lower priority despite size:** rank 8 (UI elements missing after 153/154) is the biggest single cluster at 44 but mean severity 2.2 and 66% resolved — it's a discoverability/settings-reset issue being handled well. Rank 10 (profile migration) is shrinking and 73% resolved. Rank 7 is 89% resolved. Don't spend engineering cycles there.

*Caveat: these are LLM-derived clusters over free-text support questions — treat as a triage pointer for reproduction work, not as verified defect counts.*

## 🚨 Issues to investigate

_Ranked by a transparent score weighting new/emerging + worst-served (low resolved %) + severity + volume. **Resolved %** = solved or a trusted contributor gave the last word; ⚠️ marks poorly-served clusters._

### 1. PDF/email attachments print as blank pages

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| PDF/email attachments print as blank pages (attachments) | 2 | 39 | ▲ +37 | 3.3 (12) | 38% ⚠️ | 21% |

- **Why:** A 2→39 jump in one month at 38% resolved is the signature of a print-path regression, likely in the PDF viewer/Gecko print pipeline shipped with a recent release, and users have no workaround.
- **Look at:** Bisect print-to-PDF and print-to-physical-printer of attachment previews across the 153/154 builds, focusing on the print-preview render surface and PDF.js integration on Windows print drivers.
- **Examples:** [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") [1600392](https://support.mozilla.org/questions/1600392 "Printing from Thunderbird since version 154.0 on Windows 11 produces only blank ") [1601389](https://support.mozilla.org/questions/1601389 "Problema  con ultimo  aggiornamento") [1601387](https://support.mozilla.org/questions/1601387 "problemi con la stampa degli allegati della posta, stampa e salva tutto bianco,p") [1599285](https://support.mozilla.org/questions/1599285 "PDF attachments now blank when printed.  Worked great til today.") +1

### 2. Spectrum/Charter/Roadrunner IMAP/POP mail stops downloading or times out

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Spectrum/Charter/Roadrunner IMAP/POP mail stops downloading or times out (send-receive) | 2 | 36 | ▲ +34 | 4.4 (35) | 61% | 17% |

- **Why:** A provider-specific cluster exploding 2→36 at mean severity 4.4 almost certainly reflects a Spectrum/Charter server-side change (TLS/cert, hostname consolidation, or auth policy) that Thunderbird handles as a silent timeout rather than an actionable error.
- **Look at:** Reproduce against Spectrum IMAP/POP endpoints, verify autoconfig entries and TLS negotiation, and make connection timeouts surface a specific, actionable error instead of hanging.
- **Examples:** [1599683](https://support.mozilla.org/questions/1599683 "Suddenly not receiving email") [1599681](https://support.mozilla.org/questions/1599681 "I am unable to send and receive emails on two of my computers. I can do that onl") [1600103](https://support.mozilla.org/questions/1600103 "Cannot send or receive email. (locked duplicate)") [1600872](https://support.mozilla.org/questions/1600872 "I can send email but can not receive.") [1600000](https://support.mozilla.org/questions/1600000 "Suddenly can't send/receive emails") +1

### 3. Thunderbird hangs/freezes or crashes at startup

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Thunderbird hangs/freezes or crashes at startup (performance-crash) | 18 | 41 | ▲ +23 (+128%) | 4.3 (38) | 56% | 27% |

- **Why:** 41 startup hangs/crashes at mean severity 4.3 with 38 at severity 4+ and 27% unanswered means a meaningful slice of users cannot open the client at all.
- **Look at:** Pull crash-stat signatures for the same release window and check profile/global-messages-db.sqlite rebuild, add-on incompatibility, and graphics-init paths as the likely blocking causes.
- **Examples:** [1596317](https://support.mozilla.org/questions/1596317 "Dal 17/07 Thunderbird si avvia in background ma non mostra la finestra (funziona") [1598340](https://support.mozilla.org/questions/1598340 "I was deleting old emails a few days ago and my email froze. It hasn’t responded") [1601279](https://support.mozilla.org/questions/1601279 "Thunderbird va in crasi alla connessione") [1601277](https://support.mozilla.org/questions/1601277 "Thundrbird va in crash all'accesso") [1601273](https://support.mozilla.org/questions/1601273 "Al iniciar Thunderbird se bloquea") +1

### 4. IMAP/POP mail silently stops downloading until restart

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| IMAP/POP mail silently stops downloading until restart (send-receive) | 27 | 34 | ▲ +7 (+26%) | 4.1 (29) | 47% ⚠️ | 41% |

- **Why:** 41% unanswered and only 47% resolved on a long-running defect where mail silently stops until restart means we have never actually root-caused it, and users lose mail delivery without any visible signal.
- **Look at:** Instrument IMAP connection-state recovery after network suspend/resume and NIC changes, and add a visible stale-connection indicator plus automatic reconnect.
- **Examples:** [1601356](https://support.mozilla.org/questions/1601356 "I have not received any emails for 2-3 days???") [1600778](https://support.mozilla.org/questions/1600778 "I can not down load Emails from Yahoo to Thunderbird  tired all listed solutions") [1600220](https://support.mozilla.org/questions/1600220 "Emails won’t show from 2024") [1600092](https://support.mozilla.org/questions/1600092 "Folders Enumerate but do not populate") [1598049](https://support.mozilla.org/questions/1598049 "After update 153.0.3 I can't receive emails but I can send them.") +1

### 5. Cannot send or receive at all / connection refused to mail server

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Cannot send or receive at all / connection refused to mail server (send-receive) | 13 | 25 | ▲ +12 (+92%) | 4.4 (22) | 56% | 24% |

- **Why:** Doubling to 25 at severity 4.4 with total loss of send and receive is maximal user impact, and it likely overlaps with the rank 2 provider cluster.
- **Look at:** Cross-reference these reports against rank 2 to determine whether this is one ISP/TLS root cause or a distinct connection-refused path in the socket layer.
- **Examples:** [1599843](https://support.mozilla.org/questions/1599843 "I've been w/o email for two days.  How can I get help?") [1597006](https://support.mozilla.org/questions/1597006 "Although I use the right Password I cannot get any connection to my postbox nor ") [1601287](https://support.mozilla.org/questions/1601287 "Buongiorno, non riesco ad inviare e ricevere mail") [1601282](https://support.mozilla.org/questions/1601282 "Na installatie nwe versie komt er geen mail meer binnen en kan ik geen mail verz") [1598269](https://support.mozilla.org/questions/1598269 "IMAP/SMTP server connected, but receives and send fails") +1

### 6. Password rejected / cannot log in with correct credentials

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Password rejected / cannot log in with correct credentials (account-login) | 25 | 31 | ▲ +6 (+24%) | 3.9 (25) | 58% | 29% |

- **Why:** 31 reports of correct credentials being rejected at 58% resolved suggests password-manager or token-store corruption rather than genuine user error.
- **Look at:** Audit the credential store read/write path and the fallback from OAuth to basic auth, especially where a stale token causes a misleading 'wrong password' prompt.
- **Examples:** [1597026](https://support.mozilla.org/questions/1597026 "Error message login to server pop.wbforme.com with username failed") [1601104](https://support.mozilla.org/questions/1601104 "retrouver messagerie de Thunderbird car mots de passe non reconnus") [1600222](https://support.mozilla.org/questions/1600222 "E-Mail Programm meldet alle Passwörter wären falsch") [1599070](https://support.mozilla.org/questions/1599070 "impossible to connect to my mail serveur; ask always same question about pass wo") [1599264](https://support.mozilla.org/questions/1599264 "this last update completely broke my emails") +1

### 7. Send button / composition toolbar missing in compose window

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Send button / composition toolbar missing in compose window (ui-ux) | 10 | 27 | ▲ +17 (+170%) | 3.1 (9) | 89% | 4% |

- **Why:** 27 reports of a missing Send button is a real compose-window layout defect, though 89% resolved means support already has a reliable fix.
- **Look at:** Ship the known workaround as a defensive default — validate toolbar customization state on compose-window open and restore missing primary actions automatically.
- **Examples:** [1596605](https://support.mozilla.org/questions/1596605 "SEND button vanished after update (bug1989214)") [1598077](https://support.mozilla.org/questions/1598077 "Send, delete, forward boxes have vanished from my Thunderbird write screen (bug1") [1596407](https://support.mozilla.org/questions/1596407 "Errors in compose menu after Update to 153.0.1esr (Menus gone)") [1597318](https://support.mozilla.org/questions/1597318 "THe Send button has vanished in T'bird (bug1989214)") [1597330](https://support.mozilla.org/questions/1597330 "My ＂Send＂ button has disappeared from my Thunderbird mail client.  Is there a ke") +1

### 8. UI elements missing after 153/154 update (toolbars, menus, panes)

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| UI elements missing after 153/154 update (toolbars, menus, panes) (ui-ux) | 33 | 44 | ▲ +11 (+33%) | 2.2 (1) | 66% | 14% |

- **Why:** Largest cluster at 44 but severity 2.2 and 66% resolved — high volume, low pain, and a known consequence of the 153/154 UI changes.
- **Look at:** Reduce load with in-product migration hints on first run after upgrade rather than engineering investigation.
- **Examples:** [1600361](https://support.mozilla.org/questions/1600361 "thinderbird mail tabs blank, show an X on tab, no content.") [1597229](https://support.mozilla.org/questions/1597229 "Thunderbird, versão 153.0esr: Problema com as Pastas favoritas") [1597563](https://support.mozilla.org/questions/1597563 "today I have a FREDOM pop up from thunderbird and now cannot access any mail") [1600623](https://support.mozilla.org/questions/1600623 "v140.13.0esr on Linux Debian 11: impossible to resize windows") [1596413](https://support.mozilla.org/questions/1596413 "The 'Customise Menu＂ function does nothing in v153.0.1 (64-bit)") +1

### 9. Slow performance: sluggish mail loading, sync, memory leaks

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Slow performance: sluggish mail loading, sync, memory leaks (performance-crash) | 7 | 19 | ▲ +12 | 3.4 (8) | 37% ⚠️ | 37% |

- **Why:** 37% resolved and 37% unanswered means sluggishness and memory growth reports are effectively being dropped, and the 7→19 growth tracks the same release window as rank 3.
- **Look at:** Request memory-report and profiler captures from these users and check whether the startup-crash and slow-load clusters share a common indexing or database cause.
- **Examples:** [1600636](https://support.mozilla.org/questions/1600636 "My Thunderbird has stopped working") [1599061](https://support.mozilla.org/questions/1599061 "emails home page open extremely slow, send and receive are extraordinary slow") [1596484](https://support.mozilla.org/questions/1596484 "Thunderbird not downloading gmail") [1598092](https://support.mozilla.org/questions/1598092 "Takes forever opening Thunderbird and when selecting account settings it hangs u") [1598432](https://support.mozilla.org/questions/1598432 "Thunderbird High CPU with status bar on") +1

### 10. Profile migration to new computer loses mail/accounts

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Profile migration to new computer loses mail/accounts (migration-import) | 50 | 44 | ▼ -6 (-12%) | 3.4 (20) | 73% | 7% |

- **Why:** Volume is declining (50→44) and 73% resolved with only 7% unanswered — this is a documentation-served problem, not an engineering one.
- **Look at:** No engineering action; monitor only, and confirm the profile-migration guidance stays current with recent releases.
- **Examples:** [1598972](https://support.mozilla.org/questions/1598972 "updated to 153.0.3 and no folders.") [1597960](https://support.mozilla.org/questions/1597960 "where are all my emails, sent emails and deleted emails? My last PC died and aft") [1597907](https://support.mozilla.org/questions/1597907 "Lost sub folders") [1597858](https://support.mozilla.org/questions/1597858 "After updateing to a new version of Thunderbird my old profile has disappeared") [1599476](https://support.mozilla.org/questions/1599476 "if i download an older version of thunderbird, will i loose all my current email") +1

### 11. Microsoft/Outlook/Office365 OAuth login and authentication failures

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Microsoft/Outlook/Office365 OAuth login and authentication failures (sync-oauth) | 8 | 17 | ▲ +9 | 4.1 (14) | 29% ⚠️ | 53% |

- **Why:** Worst-served issue in the set — 29% resolved, 53% unanswered, severity 4.1 — meaning more than half of users hitting Microsoft OAuth failures get no response at all.
- **Look at:** Own this directly: test the full OAuth flow against Office365 tenants with conditional access and modern-auth-only policies, verify redirect URI and refresh-token renewal, and publish a diagnostic decision tree for support.
- **Examples:** [1598006](https://support.mozilla.org/questions/1598006 "Hotmail authenticator error") [1598566](https://support.mozilla.org/questions/1598566 "Cant get hotmail to work on thunderbird linux ubuntu") [1597324](https://support.mozilla.org/questions/1597324 "No sync on exchange email account after updating to v153") [1598437](https://support.mozilla.org/questions/1598437 "Unable to Connect MS- Email") [1596314](https://support.mozilla.org/questions/1596314 "Unable to add a personal Outlook email to Thunderbird") +1

### 12. SMTP send fails / timeouts while receiving works

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| SMTP send fails / timeouts while receiving works (send-receive) | 33 | 29 | ▼ -4 (-12%) | 4.6 (28) | 66% | 21% |

- **Why:** Highest mean severity in the set at 4.6 and shrinking slightly, but SMTP-only failure while receiving works remains a total send outage for affected users.
- **Look at:** Review SMTP timeout and port-fallback behavior, and check whether these reports concentrate on the same providers as rank 2.
- **Examples:** [1599327](https://support.mozilla.org/questions/1599327 "＂Sending of the message failed. The message could not be sent because the connec") [1598759](https://support.mozilla.org/questions/1598759 "Unable to send email from Thunderbird after Network Solutions changed SMTP serve") [1600308](https://support.mozilla.org/questions/1600308 "unable to send messages after upgrade") [1600281](https://support.mozilla.org/questions/1600281 "unanle to send messages") [1600197](https://support.mozilla.org/questions/1600197 "Email msgs not received") +1

## Category mix — month over month

| Category | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| send-receive | 122 | 169 | ▲ +47 (+39%) |
| account-login | 117 | 141 | ▲ +24 (+21%) |
| ui-ux | 94 | 118 | ▲ +24 (+26%) |
| settings-config | 60 | 75 | ▲ +15 (+25%) |
| other | 64 | 72 | ▲ +8 (+12%) |
| performance-crash | 29 | 69 | ▲ +40 (+138%) |
| search-folders | 58 | 56 | ▼ -2 (-3%) |
| sync-oauth | 38 | 55 | ▲ +17 (+45%) |
| attachments | 17 | 55 | ▲ +38 (+224%) |
| migration-import | 58 | 49 | ▼ -9 (-16%) |
| spam-filters | 24 | 28 | ▲ +4 (+17%) |
| calendar-tasks | 20 | 20 | ▬ 0 (+0%) |
| encryption-security | 16 | 17 | ▲ +1 (+6%) |
| addons-extensions | 14 | 16 | ▲ +2 (+14%) |

---

_Prototype LLM-insights report · Claude claude-opus-5 over Stage-1 per-question labels · August 2026 vs July 2026 · this run cost $0.64._

_Last updated: 2026-09-10 07:11 UTC_
