---
layout: base
title: "Incident: AT&T POP certificate, from 2026-10-05"
---

# Incident: AT&T POP certificate, from 2026-10-05

This page analyzes a live cluster of Thunderbird Desktop questions. AT&T users stopped receiving mail on 2026-10-05. Sending still worked. The error names the AT&T POP server `inbound.att.net`, and it says that the server certificate is revoked, expired, or "does not come from a trusted source". The data runs to 2026-10-08 02:51 UTC. The certificate checks ran on 2026-10-08 at 03:30 UTC.

<details markdown="1">
<summary>Glossary</summary>

| Term | Meaning |
|:--|:--|
| POP | A protocol that downloads mail from the server to the computer. AT&T serves it at `inbound.att.net`. |
| IMAP | A protocol that keeps mail on the server. AT&T serves it at `imap.mail.att.net`. |
| SMTP | The protocol that sends mail. AT&T serves it at `smtp.mail.att.net`. |
| certificate | A file that a server shows to prove its name. A certificate authority signs it. |
| DigiCert | The certificate authority that signs the AT&T mail certificates. |
| revoked | The certificate authority cancelled the certificate before its end date. |
| OCSP | The service that a client asks whether a certificate is revoked. |
| email shield | A feature of Avast and AVG that reads mail traffic and checks the certificate itself. Norton has a similar feature. |
| cluster | The 23 questions in the table at the end of this page. |

</details>

## Summary

The evidence points to the AT&T server, not to Thunderbird and not to old antivirus software.

1. The cluster holds 23 questions over three days. AT&T normally gets about 5 questions a month (median 4.5 over the 12 months to 2026-09).
2. No other mail host moved. Every certificate question from 2026-10-05 to 2026-10-07 names AT&T or names no host.
3. Thunderbird fails without antivirus too. Two Linux users with no antivirus got the error ([1610258](https://support.mozilla.org/questions/1610258), [1610259](https://support.mozilla.org/questions/1610259)).
4. The users run Thunderbird 115, 128, 140, 153 and 157. A defect in one release cannot explain that spread.
5. AT&T now serves a new POP certificate. Its start date is 2026-10-06, and OCSP reports it as good.
6. Only 6 of the 23 questions got an answer from somebody other than the asker, and 2 are solved.

## What the support crew said

Lin Sprague started the thread "AT&T certificate problems" on the Thunderbird support-crew Topicbox group on 2026-10-07. Lin listed six questions: [1610484](https://support.mozilla.org/questions/1610484), [1610479](https://support.mozilla.org/questions/1610479), [1610322](https://support.mozilla.org/questions/1610322), [1610312](https://support.mozilla.org/questions/1610312), [1610297](https://support.mozilla.org/questions/1610297) and [1610275](https://support.mozilla.org/questions/1610275). Lin suspected a combination of AT&T and Norton. Wayne Mery linked three Reddit threads, in r/ATT ("inbound.att.net not responding"), r/pwnhub and r/sysadmin ("ATT email DigiCert certificate revoked"). Lin then concluded that the certificate problem is at AT&T, that it affects Outlook as well as Thunderbird, and that Norton detects it but does not cause it. This page read only the first three posts of the thread.

## What r/sysadmin said

The Reddit thread [ATT email / DigiCert certificate revoked](https://www.reddit.com/r/sysadmin/comments/1wzamuq/att_email_digicert_certificate_revoked/) started on 2026-10-06. This page read a screenshot of it from 2026-10-08 03:40 UTC.

1. The revoked certificate was issued to `inbound.att.net` by "DigiCert Global G2 TLS RSA SHA256 2020 CA1". It was valid from 2026-04-12 to 2026-10-28. Those are the dates of the IMAP and SMTP certificates that AT&T still serves today.
2. DigiCert revoked it on 2026-10-05 and gave no reason code. A new certificate was issued the same day. A commenter concluded that the owner, AT&T, asked for the revocation and the new certificate.
3. Two other incidents are unrelated. The DigiCert cyberattack of April 2026 covered other CA certificates, and DigiCert closed it two months ago. The counterfeit TLS certificates for Google in October 2026 do not include `inbound.att.net`, which is revoked through the DigiCert CRL only.
4. Outlook users have the same problem. Several fixed it with the Outlook account Repair function.
5. When Norton users turned off Norton 360 email protection, the warning stopped. One user installed the certificate by hand, and it did not help.
6. A Thunderbird user reported "Connection to server inbound.att.net reset" popping up constantly, about 8 hours before the screenshot. That is around 2026-10-07 20:00 UTC, after the new certificate started.
7. Wayne Mery asked whether AT&T or Yahoo had posted a status. Nobody found one.

## The certificates today

The tool connected to each AT&T mail host and asked DigiCert's OCSP service for the status of each certificate.

| Host | Protocol | Certificate start | Certificate end | OCSP status |
|:--|:--|:--|:--|:--|
| `inbound.att.net:995` | POP | 2026-10-06 | 2027-04-22 | good |
| `imap.mail.att.net:993` | IMAP | 2026-04-13 | 2026-10-28 | good |
| `smtp.mail.att.net:465` | SMTP | 2026-04-13 | 2026-10-28 | good |

`inbound.att.net` is an alias of `pop-att.mail.yahoo.com`. Both of its addresses (67.195.12.14 and .15) serve the new certificate. Only the POP host got a new certificate. The IMAP and SMTP certificates were probably never revoked. That matches the questions. Users could send, and 18 of the 23 questions name POP, `inbound.att.net` or port 995. Only [1610354](https://support.mozilla.org/questions/1610354) names IMAP, and that user tried both IMAP and POP. It also matches a live test: on 2026-10-07, an AT&T test account on IMAP sent and received mail in Thunderbird. That test does not cover POP. The r/sysadmin thread confirms the old POP certificate: it had the same dates as the IMAP and SMTP certificates, and DigiCert revoked only that one, on 2026-10-05.

The IMAP and SMTP certificates end on 2026-10-28. If AT&T does not renew them in time, a second wave of questions will start on that date, and it will include sending.

## Timeline

| Day (UTC) | Questions |
|:--|--:|
| 2026-10-05 | 5 |
| 2026-10-06 | 10 |
| 2026-10-07 | 8 |

The first question is [1609929](https://support.mozilla.org/questions/1609929) at 2026-10-05 15:34 UTC. Questions kept arriving on 2026-10-07, after the new certificate started. Some of them describe a failure from the day before: [1610484](https://support.mozilla.org/questions/1610484) says that it started "Oct 6, at 3:20 pm". Users post late, so this does not prove that the server is still broken. The test that settles it is in the issue checklist.

Project 1 caught the incident on the second day. The daily detector flagged `m:att` as a new cause-level spike on 2026-10-06, with 11 questions against a baseline of 0. It also flagged `v140 × m:att` at 4 questions, 111 times the expected count.

## The antivirus hypothesis

The Topicbox thread asked whether an old Norton or AVG with an expired certificate is the cause. The data argues against it as the root cause, for three reasons.

1. Users without antivirus fail too (see the Linux users above).
2. An expired certificate inside the antivirus breaks every host that the antivirus checks. No other mail host moved.
3. The antivirus messages agree with each other. Norton, AVG and Avast all say that the certificate for `inbound.att.net` from "DigiCert Global G2 TLS RSA SHA256 2020 CA1" is revoked ([1610002](https://support.mozilla.org/questions/1610002), [1610193](https://support.mozilla.org/questions/1610193)).

Antivirus does change what the user sees. 8 of the 23 questions name Norton, AVG, Avast or "email shield", and those users see a message from the antivirus instead of from Thunderbird. One user fixed it by turning off Norton email protection ([1610002](https://support.mozilla.org/questions/1610002)). That workaround removes the antivirus check only. It does not fix a revoked server certificate for Thunderbird itself.

## Open points

1. [1610322](https://support.mozilla.org/questions/1610322) says "(from Sept 16)" and "the second time this has happened to me in as many months". No AT&T certificate questions arrived in September, so this is one user, not a September cluster.
2. [1610523](https://support.mozilla.org/questions/1610523) reports "connection was refused", a different error. It is in the cluster because it names `inbound.att.net` on the same day.
3. Four questions in the cluster name AT&T and a receive failure but no certificate: [1609983](https://support.mozilla.org/questions/1609983), [1610037](https://support.mozilla.org/questions/1610037), [1610354](https://support.mozilla.org/questions/1610354) and [1610509](https://support.mozilla.org/questions/1610509). The timing puts them in the cluster.
4. Excluded: [1610309](https://support.mozilla.org/questions/1610309) (an AOL password) and [1610310](https://support.mozilla.org/questions/1610310) (mail goes to Local Folders) name `att.net` but describe other problems. [1610583](https://support.mozilla.org/questions/1610583) is about the AT&T PIN and password. [1610140](https://support.mozilla.org/questions/1610140) shows a certificate message without a host.

## Every question in the cluster

<details markdown="1">
<summary>23 questions, 2026-10-05 to 2026-10-07</summary>

"Answered" means that somebody other than the asker replied. "Solved" is the SUMO `is_solved` flag. "Trusted last answer" means that the most recent answer came from somebody on the trusted-contributors list.

| Created (UTC) | Question | Version | Antivirus named | Title | Answered | Solved | Trusted last answer |
|:--|:--|:--|:--|:--|:--|:--|:--|
| 2026-10-05 15:34 | [1609929](https://support.mozilla.org/questions/1609929) | 157 | email shield | ＂We've identified a site certificate problem＂ | no | no | no |
| 2026-10-05 19:02 | [1609983](https://support.mozilla.org/questions/1609983) | 115 |  | I cannot bring mail from AT&T  into my Thunderbird app on my home computer, what | no | no | no |
| 2026-10-05 20:50 | [1610002](https://support.mozilla.org/questions/1610002) | 157 | Norton | 'Digicert Global G2' revoked Oct 5, 2026 | no | no | no |
| 2026-10-05 23:09 | [1610029](https://support.mozilla.org/questions/1610029) | 157 | Norton | Norton is blocking Thunderbird because it says DigiCert Global G2 TLS RSA SHA256 | no | no | no |
| 2026-10-05 23:33 | [1610037](https://support.mozilla.org/questions/1610037) |  |  | Thunderbird suddenly stopped receiving AT&T email ? | yes | no | no |
| 2026-10-06 13:34 | [1610152](https://support.mozilla.org/questions/1610152) | 115 | Avast | Certificate revoked for inbound.att.net?  What do we do? | no | no | no |
| 2026-10-06 13:50 | [1610156](https://support.mozilla.org/questions/1610156) | 140 |  | Gives error today - inbound.att.net certificate invalid !!?? | yes | no | yes |
| 2026-10-06 15:05 | [1610171](https://support.mozilla.org/questions/1610171) | 153 |  | ＂inbound.att.net (POP) .. certificate revoked＂? I can't download eMail! | yes | yes | no |
| 2026-10-06 16:05 | [1610193](https://support.mozilla.org/questions/1610193) | 157 | AVG | certificate has been revoked. unable to receive email. | yes | yes | no |
| 2026-10-06 16:54 | [1610212](https://support.mozilla.org/questions/1610212) | 153 | AVG, email shield | pop from Tbird says connection to server inbound.att.net has been reset | no | no | no |
| 2026-10-06 19:03 | [1610258](https://support.mozilla.org/questions/1610258) | 140 |  | The certificate for inbound.att.net does not come from a trusted source. | yes | no | no |
| 2026-10-06 19:08 | [1610259](https://support.mozilla.org/questions/1610259) | 140 |  | Why Thunderbird on Linux will no longer connect to att.net email with POP3. | no | no | no |
| 2026-10-06 20:24 | [1610275](https://support.mozilla.org/questions/1610275) | 157 | Norton | indication is that certificate has expired, email will not download (new problem | no | no | no |
| 2026-10-06 22:04 | [1610297](https://support.mozilla.org/questions/1610297) | 157 |  | Unable to receive messages due to certificate problem | no | no | no |
| 2026-10-06 23:18 | [1610312](https://support.mozilla.org/questions/1610312) | 153 | Norton | Norton blocks Thunderbird email due to ＂expired certificate＂ | no | no | no |
| 2026-10-07 00:16 | [1610321](https://support.mozilla.org/questions/1610321) | 115 |  | I can't recieve emails but can send the certification is revoked for inbound.att | yes | no | no |
| 2026-10-07 00:54 | [1610322](https://support.mozilla.org/questions/1610322) | 153 |  | No E-mail because of ＂The certificate for inbound.att.net:995 does not come from | no | no | no |
| 2026-10-07 04:32 | [1610354](https://support.mozilla.org/questions/1610354) | 128 |  | Thunderbird not connecting to my sbcglobal.net account | no | no | no |
| 2026-10-07 17:24 | [1610479](https://support.mozilla.org/questions/1610479) | 128 |  | No longer able to receive emails | no | no | no |
| 2026-10-07 17:40 | [1610484](https://support.mozilla.org/questions/1610484) | 157 |  | tbird cannot download emails from my browser. | no | no | no |
| 2026-10-07 19:35 | [1610509](https://support.mozilla.org/questions/1610509) |  |  | i can send emails but cannot receive them all of the sudden?? | no | no | no |
| 2026-10-07 20:18 | [1610518](https://support.mozilla.org/questions/1610518) | 115 |  | suddenly can't retrieve ATT Yahoo emails with Thunderbird after trying every sug | no | no | no |
| 2026-10-07 20:38 | [1610523](https://support.mozilla.org/questions/1610523) | 157 |  | Thunderbird could not connect to server inbound.att.net. The connection was refu | no | no | no |

</details>
