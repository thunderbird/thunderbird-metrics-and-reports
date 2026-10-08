---
layout: base
title: "Incident: the Attach button does nothing, from 2026-10-02 (bug 2077590)"
---

# Incident: the Attach button does nothing, from 2026-10-02 (bug 2077590)

This page analyzes a live cluster of Thunderbird Desktop questions. From 2026-10-02, users click the Attach button or the paperclip, and no file picker opens. Drag and drop still works. The cause is a known regression, [bug 2077590](https://bugzilla.mozilla.org/show_bug.cgi?id=2077590). The data runs to 2026-10-08 02:48 UTC.

<details markdown="1">
<summary>Glossary</summary>

| Term | Meaning |
|:--|:--|
| file picker | The window in which the user selects a file to attach. |
| remembered directory | The folder that the file picker opened last time. Thunderbird stores it in the preference `mail.compose.attach.dir`. |
| regression | A defect that a new release brings into a feature that worked before. |
| uplift | Copying a fix into a release branch that is already shipping. |
| ESR | Extended Support Release, the yearly Thunderbird branch with slower changes. 153 is the current ESR. |
| cluster | The 32 questions in the table at the end of this page. |

</details>

## Summary

1. The cluster holds 32 questions from 2026-10-02 to 2026-10-08. Before 2026-10-02, no question in two weeks described this symptom.
2. The users run Thunderbird 157.0.1 and 153.4.0esr. Both builds shipped around 2026-09-30, and [1609202](https://support.mozilla.org/questions/1609202) says "since the Thunderbird update of 30 Sept".
3. The cause is known. If the remembered directory no longer exists, the file picker fails without a message. A Firefox platform change caused it, and Mozilla backported that change to every branch, back to ESR 115.
4. A fix exists. Bugzilla marks the bug fixed by bug 2077980. The fix is uplifted to Thunderbird 158 and ESR 153, and comment 18 plans it for "next Tuesday's releases", which is 2026-10-13.
5. A workaround exists (see below). The support crew uses it: 29 of the 32 questions got an answer from somebody other than the asker, and 12 are solved.
6. The cluster is multilingual: 21 English, 8 Italian, 2 Dutch and 1 Spanish question. On Topicbox, Michele reported at least 9 Italian reports.

## What the support crew said

Wayne Mery forwarded bug 2077590 to the support-crew Topicbox group on 2026-10-04 and warned that reports would come from 140 ESR, 153 ESR, 157 and 158. Lin Sprague confirmed the defect on 153.4.0esr on Windows 10. On Ubuntu with 153.0, Lin got an error message ("Unable to find ...") and could then browse, so the failure is silent on some platforms only. Michele logged at least 9 reports in the Italian section of SUMO on 2026-10-05.

## Bugzilla

| Bug | What | Status on 2026-10-08 |
|:--|:--|:--|
| [2077590](https://bugzilla.mozilla.org/show_bug.cgi?id=2077590) | The Attach File dialog fails without a message when the remembered directory no longer exists | Fixed by bug 2077980. Status flags: 157 wontfix, 158 affected, ESR 153 affected, ESR 140 affected. 10 duplicates. |
| [2077526](https://bugzilla.mozilla.org/show_bug.cgi?id=2077526) | Attachment menu item not functional | Duplicate of 2077590. A SUMO user quotes it in [1609344](https://support.mozilla.org/questions/1609344). |
| [2077390](https://bugzilla.mozilla.org/show_bug.cgi?id=2077390) | macOS downloads fail with "ask where to save files" | Fixed. Part of the same platform regression, macOS only. |

The workaround, from [comment 2](https://bugzilla.mozilla.org/show_bug.cgi?id=2077590#c2):

1. Open Settings, General, Config Editor.
2. Search for `mail.compose.attach.dir`.
3. Change the value to a folder that exists, for example `C:\`, or reset the preference.
4. Restart Thunderbird.

## Timeline

| Day (UTC) | Questions |
|:--|--:|
| 2026-10-02 | 5 |
| 2026-10-03 | 3 |
| 2026-10-04 | 5 |
| 2026-10-05 | 5 |
| 2026-10-06 | 6 |
| 2026-10-07 | 6 |
| 2026-10-08 (to 02:48) | 2 |

The first question is [1609189](https://support.mozilla.org/questions/1609189), in Italian, at 2026-10-02 12:27 UTC. The first Bugzilla report, bug 2077526, arrived two hours later. The rate is steady at about 5 a day, and it will stay there until the fixed releases ship. Users who skip updates keep the defect after that.

## Detection

Project 1 caught the incident two days after onset. The daily detector flagged `v157 × feat:attachments` on 2026-10-04 (5 questions, 9 times the expected count) and `feat:attachments` as a new cause-level spike on 2026-10-05 (10 questions, baseline 0). The weekly detector flagged the week of 2026-10-05 for both versions: v153 at 10 times and v157 at 5 times the expected count.

The `feature` dimension matches titles only, and its attachments pattern misses some Italian titles. For example, "Il selettore di file non si apre cliccando sul pulsante Allega" ([1609189](https://support.mozilla.org/questions/1609189)) has no tag, because the pattern knows `allegato` and `allegati` but not `allega` or `allegare`. It also misses the German plural "Anhänge" ([1610397](https://support.mozilla.org/questions/1610397)). The detector therefore undercounts this cluster.

## Open points

1. The Bugzilla status flags say that ESR 140 is affected, but no question in the cluster runs 140. [1609430](https://support.mozilla.org/questions/1609430) reports 150.4 in the version field and 153.4.0 in its title.
2. Excluded: [1610442](https://support.mozilla.org/questions/1610442) (quick filter), [1610394](https://support.mozilla.org/questions/1610394) (Thunderbird does not start on Ubuntu) and [1610447](https://support.mozilla.org/questions/1610447) (the Send and Attach controls are gone, on 128). They mention attachments but describe other problems.

## Every question in the cluster

<details markdown="1">
<summary>32 questions, 2026-10-02 to 2026-10-08</summary>

"Answered" means that somebody other than the asker replied. "Solved" is the SUMO `is_solved` flag. "Trusted last answer" means that the most recent answer came from somebody on the trusted-contributors list.

| Created (UTC) | Question | Locale | Version | OS | Title | Answered | Solved | Trusted last answer |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| 2026-10-02 12:27 | [1609189](https://support.mozilla.org/questions/1609189) | it | 157.0 | Mac OS x 10.15 | Il selettore di file non si apre cliccando sul pulsante Allega. | yes | yes | no |
| 2026-10-02 13:39 | [1609202](https://support.mozilla.org/questions/1609202) | en-US | 157.0 | Windows 11 | Unable to attach files to emails since 30 Sept update (bug2077590) | yes | no | no |
| 2026-10-02 17:22 | [1609259](https://support.mozilla.org/questions/1609259) | en-US | 157.01 | Windows 11 | attachment dialogue not executing! | yes | no | yes |
| 2026-10-02 18:09 | [1609267](https://support.mozilla.org/questions/1609267) | it | 153.4 | Windows 11 | Pulsante ＂Allega＂ non apre la finestra dei file (Thunderbird 153.4.0esr - Window | yes | yes | no |
| 2026-10-02 22:51 | [1609328](https://support.mozilla.org/questions/1609328) | en-US | 153.4 | Windows 10/11 | Can't add attachment to email message | yes | no | yes |
| 2026-10-03 00:54 | [1609344](https://support.mozilla.org/questions/1609344) | en-US |  | Windows 11 | Bug 2077526 - Attachment menu item not functional | yes | yes | no |
| 2026-10-03 13:29 | [1609430](https://support.mozilla.org/questions/1609430) | en-US | 150.4 | Windows 11 | attachment button(s) no longer responsive ¦ TB 153.4.0 | yes | yes | no |
| 2026-10-03 16:56 | [1609478](https://support.mozilla.org/questions/1609478) | en-US | 153.4 | Windows 11 | Thunderbird Email senden mit Anhang funktioniert nicht mehr | yes | yes | no |
| 2026-10-04 11:42 | [1609624](https://support.mozilla.org/questions/1609624) | en-US |  | Win 11 | Cant add attachment to file | yes | yes | no |
| 2026-10-04 13:28 | [1609642](https://support.mozilla.org/questions/1609642) | en-US | 157.0 | Windows 11 | Attach button does not respond. Drag and Drop works. (bug2077590) | yes | no | no |
| 2026-10-04 13:48 | [1609649](https://support.mozilla.org/questions/1609649) | it | 157.0 | Windows 10 | il pulsante allega non apre la finestra dei file per la scelta. tutte le e-mail  | yes | no | no |
| 2026-10-04 18:55 | [1609713](https://support.mozilla.org/questions/1609713) | es | 157.0 | Windows 10 | Thunderbird 157.0.1 no abre la ventana para seleccionar archivos adjuntos | yes | no | yes |
| 2026-10-04 19:39 | [1609719](https://support.mozilla.org/questions/1609719) | it | 157.0 | Windows 11 | Unable to attach files to email | yes | no | no |
| 2026-10-05 11:44 | [1609880](https://support.mozilla.org/questions/1609880) | en-US | 157.0 | Windows 11 | I cannot add an attachment, when I press the attachment button nothing happens | yes | yes | no |
| 2026-10-05 14:02 | [1609914](https://support.mozilla.org/questions/1609914) | it | 153.4 | Mac OS 27.0.1 (26A434) | Non posso allegare file | yes | no | no |
| 2026-10-05 14:17 | [1609916](https://support.mozilla.org/questions/1609916) | en-US | 157 | Windows 11 | Attach button dont work after updating to tb 157 | yes | yes | no |
| 2026-10-05 19:16 | [1609986](https://support.mozilla.org/questions/1609986) | en-US | 153.4 | Windows 11 | not launching file explorer to attach files | no | no | no |
| 2026-10-05 23:14 | [1610030](https://support.mozilla.org/questions/1610030) | en-US | 153.4 | Windows 11 Home ,Version 25H2. | Thunderbird ＂Attach＂ button nor yellow attach bar reminder functioning. | yes | yes | no |
| 2026-10-06 05:20 | [1610087](https://support.mozilla.org/questions/1610087) | en-US | 153.4 | Windows 11 | Email attachment - version 153.4.0esr | yes | no | yes |
| 2026-10-06 06:56 | [1610100](https://support.mozilla.org/questions/1610100) | en-US | 153.4 | Windows 11 | unable to attach desktop files to outgoing emails when attachment function activ | yes | no | yes |
| 2026-10-06 07:38 | [1610105](https://support.mozilla.org/questions/1610105) | it | 157.0 | Windows 11 | Non fulziona allega file quando creo un nuovo messaggio | yes | no | no |
| 2026-10-06 09:24 | [1610118](https://support.mozilla.org/questions/1610118) | en-US | 153.4 | Windows 10 | All of a sudden Thunderbird won't let me attach images | yes | yes | no |
| 2026-10-06 16:38 | [1610206](https://support.mozilla.org/questions/1610206) | en-US | 153.4 | Windows 10/11 | I have lost the attach file link since last up date | yes | no | yes |
| 2026-10-06 16:55 | [1610213](https://support.mozilla.org/questions/1610213) | nl | 157.0 | Windows 11 | Thunderbird is onbruikbaar geworden | yes | no | yes |
| 2026-10-07 09:24 | [1610392](https://support.mozilla.org/questions/1610392) | en-US | 153.4 | Windows 11 | Recurring Issue with Attachment Button in Thunderbird Desktop | yes | no | yes |
| 2026-10-07 09:47 | [1610397](https://support.mozilla.org/questions/1610397) | en-US | 157.0 | Mac OS x 10.15 | Keine Anhänge mehr möglich. | yes | yes | yes |
| 2026-10-07 13:28 | [1610418](https://support.mozilla.org/questions/1610418) | it | 153.4 | Edizione	Windows 10 Pro Versione	22H2 Data installazione:	‎17/‎03/‎2021 Build sistema operativo	19045.6466 | Facendo clic sia su Allega sia sulla graffetta  non permette di Navigare fino a  | yes | no | no |
| 2026-10-07 14:54 | [1610438](https://support.mozilla.org/questions/1610438) | nl | 157.01 | Windows 10/11 | Bijjlage toevoegen aan mail lukt niet bij klikken op paperclip. Windows verkenne | yes | yes | yes |
| 2026-10-07 15:17 | [1610441](https://support.mozilla.org/questions/1610441) | it | 157.0 | Windows 11 | tasto allega in alto a dx | yes | no | no |
| 2026-10-07 20:23 | [1610520](https://support.mozilla.org/questions/1610520) | en-US | 157.0 | Windows 11 | why has attachments stopped working | yes | no | yes |
| 2026-10-08 01:46 | [1610569](https://support.mozilla.org/questions/1610569) | en-US | 153.4 | Windows 10/11 | The file picker does not open when you click the “Attach” button | no | no | no |
| 2026-10-08 02:48 | [1610581](https://support.mozilla.org/questions/1610581) | en-US | 153.4 | Windows 11 | Cannot attach files to emails in Thunderbird | no | no | no |

</details>
