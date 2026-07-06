---
layout: base
title: Desktop LLM Insights — June 2026
---

# Thunderbird Desktop — LLM Insights (Engineering)

## June 2026 vs May 2026

_The **AI counterpart to Project 1**: Claude reads every support question (plus the creator's own follow-ups, the accepted solution, and trusted-contributor replies), names the concrete problem, hypothesises a root cause, and rates severity — surfacing emerging / worst-served pain that regex + stats can't. Counts are exact (computed in Python); clustering and prose are LLM-derived. A triage pointer, not proof._

## Headline

| | May 2026 | June 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 812 | 724 | ▼ -88 (-11%) |
| Distinct issue clusters | 201 | 173 | ▼ -28 |
| New issue clusters this month | — | 4 | |

**Startup freeze/crash cases 2.5x'd in June and now dominate pain despite overall volume falling — likely a recent-build regression.**

**Overall support volume dropped (812 → 724), but the pain concentrated.** The performance-crash category rose against the trend (45 → 71), driven almost entirely by rank 1: freeze/hang/crash on startup jumped from 24 to 60 reports (2.5x) with mean severity 3.6 and 37 severity-4+ cases. This shape — a sharp single-cluster spike concentrated in one category while everything else declines — is the classic signature of a regression shipped in a recent build, and it should be engineering's first look this month.

**Four new clusters emerged, and several are badly served.** New provider-specific breakage appeared: rank 5 (Charter/Spectrum untrusted certificate, 0→7) and rank 10 (Orange.fr send/receive), suggesting external cert/config changes at those ISPs that Thunderbird handles poorly. Two new content-integrity clusters are the worst-resolved of the month: rank 8 (attachments dropped on forward, 20% resolved) and rank 9 (mail auto-moved to Trash/Junk, 20% resolved, 40% unanswered).

**Chronic send/receive failures remain the steady baseline pain.** Ranks 2, 4, and 7 are flat in volume but stubbornly low on resolution (48–61%) and high severity (rank 7 at 4.2 mean) — well-known but unfixed. These are lower urgency than the spike and the new clusters, but the persistently low resolved rates suggest missing diagnostics rather than user error.

*This is an LLM-derived triage signal over free-text questions, not proof — treat rankings as pointers for where to dig.*

## 🚨 Issues to investigate

_Ranked by a transparent score weighting new/emerging + worst-served (low resolved %) + severity + volume. **Resolved %** = solved or a trusted contributor gave the last word; ⚠️ marks poorly-served clusters._

### 1. Performance: freeze/hang/crash on startup or use

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Performance: freeze/hang/crash on startup or use (performance-crash) | 24 | 60 | ▲ +36 (+150%) | 3.6 (37) | 57% | 17% |

- **Why:** A 2.5x spike in startup freeze/crash with 37 high-severity cases, rising while total volume fell, is the strongest regression signal this month.
- **Look at:** Diff recent release/build changes for startup, profile-load, and add-on-init paths, and correlate crash reports by version to find the introducing commit.
- **Examples:** [1585718](https://support.mozilla.org/questions/1585718 "BLOCCO DEL SOFTWARE ＂THUNDERBIRD NON RISPONDE＂ DOPO POCHI SECONDI DALL'AVVIO O A") [1587576](https://support.mozilla.org/questions/1587576 "My default thunderbird profile is frozen and I can't even import my files/folder") [1587098](https://support.mozilla.org/questions/1587098 "I can't access my inbox after a crash during a power outage.") [1586470](https://support.mozilla.org/questions/1586470 "non risponde dopo avvio") [1586517](https://support.mozilla.org/questions/1586517 "On Sunday, May 7, my thunderbird program suddenly stopped responding (neither th") +1

### 2. Cannot send email / SMTP send failure (general)

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Cannot send email / SMTP send failure (general) (send-receive) | 34 | 34 | ▬ 0 (+0%) | 3.7 (24) | 50% | 18% |

- **Why:** General SMTP send failures are high-severity and stuck at 50% resolved despite flat volume, showing a persistent unresolved failure mode.
- **Look at:** Improve SMTP send diagnostics/logging to distinguish auth, TLS, and server-reject causes so triage can converge.
- **Examples:** [1586239](https://support.mozilla.org/questions/1586239 "Problems by sending emails") [1590460](https://support.mozilla.org/questions/1590460 "On Thunderbird, repeat message saying SMTP server not working. It is fine for we") [1586922](https://support.mozilla.org/questions/1586922 "Can send but not receive emails") [1588337](https://support.mozilla.org/questions/1588337 "ricevo posta ma non riesco piu' a inviarla") [1588327](https://support.mozilla.org/questions/1588327 "non riesco piu' ad inviare posta") +1

### 3. Profile migration to new computer / lost data

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Profile migration to new computer / lost data (migration-import) | 19 | 28 | ▲ +9 (+47%) | 3.1 (9) | 79% | 4% |

- **Why:** Profile migration to a new computer grew (19→28) and, while well-resolved (79%), represents avoidable data-loss anxiety.
- **Look at:** Assess the profile-migration UX and whether a guided export/import tool would reduce these tickets.
- **Examples:** [1586082](https://support.mozilla.org/questions/1586082 "Data loss transferring T-Bird to another computer") [1587336](https://support.mozilla.org/questions/1587336 "Tbird was not working. Downloaded upgrade verbatim off of website. lost all file") [1588433](https://support.mozilla.org/questions/1588433 "Lost years of emails stored locally on reboot of windows 7 after a bod with not ") [1587467](https://support.mozilla.org/questions/1587467 "migrated to new Mac and Thunderbird damaged/deleted. What to do.") [1586217](https://support.mozilla.org/questions/1586217 "Re-installing Thunderbird on Windows 11") +1

### 4. Cannot receive / no new mail downloading

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Cannot receive / no new mail downloading (send-receive) | 30 | 27 | ▼ -3 (-10%) | 3.3 (14) | 48% ⚠️ | 30% |

- **Why:** No-new-mail-downloading has the highest unanswered rate among top issues (30%) and only 48% resolved, meaning users are left stranded.
- **Look at:** Review IMAP/POP fetch and connection-retry behavior and add clearer failure surfacing when download stalls.
- **Examples:** [1586630](https://support.mozilla.org/questions/1586630 "Why can`t I get my emails on Mozilla Thunderbird, keeps saying server not found") [1587177](https://support.mozilla.org/questions/1587177 "Emails aren't arriving in the inbox, nor is the mail service working.") [1585180](https://support.mozilla.org/questions/1585180 "Thunderbird will not retrieve messages for one of my email accounts.") [1585457](https://support.mozilla.org/questions/1585457 "I can't get any emails since 5-31-2026") [1585519](https://support.mozilla.org/questions/1585519 "can send but not receive emails") +1

### 5. Charter/Spectrum untrusted certificate · 🆕 new this month

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Charter/Spectrum untrusted certificate (encryption-security) | 0 | 7 | ▲ +7 | 3.6 (4) | 43% ⚠️ | 14% |

- **Why:** A brand-new provider cluster (Charter/Spectrum untrusted certificate) points to an external cert change Thunderbird surfaces confusingly, and only 43% get resolved.
- **Look at:** Verify the ISP's current mail-server certificate chain and improve the untrusted-cert dialog/guidance for that hostname pattern.
- **Examples:** [1586405](https://support.mozilla.org/questions/1586405 "The certificate for mobile.charter.net does not come from a trusted source.") [1586446](https://support.mozilla.org/questions/1586446 "Unable to receive and send emails.") [1586504](https://support.mozilla.org/questions/1586504 "The certificate for mobile.charter.net:993 does not come from a trusted source.") [1586525](https://support.mozilla.org/questions/1586525 "I don't have mobile.charter.net.  Why am I blocked from receiving my email on Mo") [1586486](https://support.mozilla.org/questions/1586486 "Thunderbird is showing Certificate for mobile.charter.net:993 does not come from") +1

### 6. Generic account setup authentication error (correct credentials)

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Generic account setup authentication error (correct credentials) (account-login) | 35 | 30 | ▼ -5 (-14%) | 2.8 (7) | 67% | 23% |

- **Examples:** [1586926](https://support.mozilla.org/questions/1586926 "Deixei de conseguir enviar/receber emails no thunderbird") [1586675](https://support.mozilla.org/questions/1586675 "Cannot link thunderbird to my email with new computer.") [1585216](https://support.mozilla.org/questions/1585216 "when trying to access my email on thunderbird, I get the message: ＂ Login to ser") [1589710](https://support.mozilla.org/questions/1589710 "Deixei de receber/enviar emails em uma de minhas contas eliminei-a e não consigo") [1585571](https://support.mozilla.org/questions/1585571 "Estou instalando (várias vezes) o Thunderbird no Windows e, ao adicionar uma con") +1

### 7. Cannot send AND receive / total connectivity loss

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Cannot send AND receive / total connectivity loss (send-receive) | 19 | 18 | ▼ -1 (-5%) | 4.2 (16) | 61% | 22% |

- **Why:** Total connectivity loss carries the highest severity (4.2) and blocks all email use even though volume is steady.
- **Look at:** Examine shared network/proxy/TLS layer failures that would knock out both send and receive simultaneously.
- **Examples:** [1584963](https://support.mozilla.org/questions/1584963 "Recover Lost Emails") [1587704](https://support.mozilla.org/questions/1587704 "I can't receive e-mails at xxx@oh.rr.com. Another error occurred with the POP3ma") [1585599](https://support.mozilla.org/questions/1585599 "unable to receive e-mails. can not send out messages") [1586189](https://support.mozilla.org/questions/1586189 "Thunderbird wont send/receive emails") [1587942](https://support.mozilla.org/questions/1587942 "I can no longer receive or sent emails.") +1

### 8. Attachments dropped/lost when forwarding · 🆕 new this month

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Attachments dropped/lost when forwarding (attachments) | 0 | 5 | ▲ +5 | 3.2 (1) | 20% ⚠️ | 20% |

- **Why:** New and the worst-resolved cluster (20%): silently dropping attachments on forward is a data-integrity bug users can't work around.
- **Look at:** Reproduce forward-with-attachment flows across MIME/compose paths and check for a recent compose or attachment-handling regression.
- **Examples:** [1587025](https://support.mozilla.org/questions/1587025 "Attachment disappear in forwarded maessage after long editing") [1585164](https://support.mozilla.org/questions/1585164 "Problém přeposlání emailu s přílohou") [1586587](https://support.mozilla.org/questions/1586587 "Thunderbird email chains not including attachments when forwarded") [1587679](https://support.mozilla.org/questions/1587679 "inoltro email con allegati ＂Controllare di disporre dei permessi per accedere al") [1588176](https://support.mozilla.org/questions/1588176 "Thunderbird fails to save an inline forwarded email with inherited attachments a")

### 9. Emails auto-moved to Trash/Junk · 🆕 new this month

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Emails auto-moved to Trash/Junk (spam-filters) | 0 | 5 | ▲ +5 | 3.0 (2) | 20% ⚠️ | 40% |

- **Why:** New cluster with 20% resolved and 40% unanswered — mail auto-moved to Trash/Junk risks users losing legitimate messages.
- **Look at:** Investigate junk-filter/message-classification behavior and any recent changes to auto-move rules or filter defaults.
- **Examples:** [1588804](https://support.mozilla.org/questions/1588804 "emails in inbox keep moving to trash box by themselves") [1589173](https://support.mozilla.org/questions/1589173 "emails move on their own from inbox to trash folder (locked duplicate)") [1589217](https://support.mozilla.org/questions/1589217 "Inbox settings/configuration") [1589243](https://support.mozilla.org/questions/1589243 "迷惑メールフォルダーに入っていた迷惑メールが勝手にゴミ箱に移動してしまう") [1589901](https://support.mozilla.org/questions/1589901 "Thunderbird Emties Spam I haven't Seen Yet")

### 10. Orange.fr account send/receive/spam issues · 🆕 new this month

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Orange.fr account send/receive/spam issues (send-receive) | 0 | 4 | ▲ +4 | 3.0 (0) | 50% | 25% |

- **Examples:** [1585333](https://support.mozilla.org/questions/1585333 "Some email addresses are no longer being delivered and are not in the spam folde") [1585684](https://support.mozilla.org/questions/1585684 "installation Thunderbird : problème cpte messagerie et MDP, impossible d'aller p") [1585691](https://support.mozilla.org/questions/1585691 "Why can I not send emails from my Orange.fr email account?") [1586409](https://support.mozilla.org/questions/1586409 "J'ai 2 boites de messagerie Orange : Boite 1 envoie un message qui va ＂anormalem")

### 11. Calendar reminders not shown / snooze issues

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Calendar reminders not shown / snooze issues (calendar-tasks) | 2 | 8 | ▲ +6 | 2.2 (0) | 25% ⚠️ | 38% |

- **Why:** Calendar reminders not firing tripled (2→8) with 25% resolved and 38% unanswered, indicating an unhandled notification defect.
- **Look at:** Check the alarm/reminder scheduler and OS notification delivery path for regressions or timezone/snooze edge cases.
- **Examples:** [1586987](https://support.mozilla.org/questions/1586987 "I can no longer send event reminder notifications by email") [1587939](https://support.mozilla.org/questions/1587939 "buongiorno, da un po di tempo gli appuntamenti sul calendario anteriori all'aper") [1589521](https://support.mozilla.org/questions/1589521 "Event/task reminders are not displayed") [1585181](https://support.mozilla.org/questions/1585181 "Reminder snooze options ＂x minutes before start＂") [1585372](https://support.mozilla.org/questions/1585372 "Local snooze for shared calendars") +1

### 12. Sent mail not saved / saved to wrong folder

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Sent mail not saved / saved to wrong folder (send-receive) | 8 | 12 | ▲ +4 | 2.8 (1) | 67% | 8% |

- **Examples:** [1586646](https://support.mozilla.org/questions/1586646 "Email inviata che scompare da posta inviata") [1585025](https://support.mozilla.org/questions/1585025 "No Copy In Sent Folder") [1586183](https://support.mozilla.org/questions/1586183 "Zmizlo mi z priečinku ＂ odoslaná pošta＂.") [1587455](https://support.mozilla.org/questions/1587455 "Thunderbird stops saving SENT messages to ＂Copies & Folders＂") [1587981](https://support.mozilla.org/questions/1587981 "Wie kann ich die verschwundenen gesendeten mails wieder sichtbar kriegen") +1

## Category mix — month over month

| Category | May 2026 | June 2026 | Change |
|:--|--:|--:|:--|
| send-receive | 180 | 158 | ▼ -22 (-12%) |
| account-login | 135 | 101 | ▼ -34 (-25%) |
| ui-ux | 111 | 86 | ▼ -25 (-23%) |
| performance-crash | 45 | 71 | ▲ +26 (+58%) |
| migration-import | 59 | 64 | ▲ +5 (+8%) |
| settings-config | 64 | 43 | ▼ -21 (-33%) |
| calendar-tasks | 28 | 37 | ▲ +9 (+32%) |
| search-folders | 59 | 35 | ▼ -24 (-41%) |
| spam-filters | 26 | 28 | ▲ +2 (+8%) |
| sync-oauth | 37 | 28 | ▼ -9 (-24%) |
| other | 33 | 27 | ▼ -6 (-18%) |
| encryption-security | 19 | 20 | ▲ +1 (+5%) |
| addons-extensions | 6 | 15 | ▲ +9 |
| attachments | 10 | 11 | ▲ +1 (+10%) |

---

_Prototype LLM-insights report · Claude claude-opus-4-8 over Stage-1 per-question labels · June 2026 vs May 2026 · this run cost $0.60._

_Last updated: 2026-07-05 13:55 UTC_
