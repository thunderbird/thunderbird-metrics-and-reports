# Detector back-test — v154 blank-printing regression, Aug–Sep 2026

The incident that motivated the **`feature` cause dimension** (issue #76). Unlike
the Bitdefender back-test (a *pass* the detectors already got), this one starts as
a documented **MISS** and becomes a pass only after the new dimension existed —
so it is the strongest evidence in the corpus that the cause-dimension *set*, not
the thresholds, was the binding constraint.

## The incident (ground truth, external)

**Bugzilla [2065922](https://bugzilla.mozilla.org/show_bug.cgi?id=2065922)** —
printing from the PDF preview produced **blank/empty pages**. Practically, users
could not print email attachments.

- **Introduced in Thunderbird 154**, which began rolling out **18–19 Aug 2026**
  (v154's share of daily desktop questions went 0% → 5% → 36% → 41% across
  Aug 18–20).
- **Fixed in Thunderbird 155, released 1 Sep 2026.**

## Verdict: MISSED entirely before #76 — then caught on day one

### Before: invisible at every grain, unreachable by any threshold

The 2026-08 exec summary as generated on 2026-09-09 reported **14 spikes** and
none of them was the printing regression. This was **not** a threshold miss:

- The cause dims were `mail_provider`, `protocol`, `av` — all *external* things.
  Printing is a **feature area**, so the cluster had nowhere to land.
- **41 of the 50 questions on 2026-08-31 carried no cause tag at all**, and the
  print questions scattered across providers (gmail, microsoft, yahoo, spectrum,
  none), so no cause value accumulated a count.
- Lowering floors could not have helped: the signal was not small, it was
  **unrepresented**.

What *was* visible were the useless shadows of it: `tb_version_major 154` firing
as a bare release-adoption spike (27 questions on Aug 26, baseline 0), which the
report correctly files under "expected after a release — not incidents".

### After: caught on the onset day, at all three grains

With `feat:printing` (title-only matching — see below):

| Grain | Signal | Observed | Expected | Lift | Novelty |
|:--|:--|--:|--:|--:|:--|
| **daily** | **2026-08-20** v154 × `feat:printing` | 4 | 0.16 | **24.3×** | `new` |
| daily | 2026-08-26 v154 × `feat:printing` | 5 | 0.37 | 13.5× | recurring |
| daily | 2026-08-31 v154 × `feat:printing` | 4 | 0.30 | 13.3× | recurring |
| weekly | wk 2026-08-17 v154 × `feat:printing` | 7 | 0.86 | 8.1× | `new` |
| weekly | wk 2026-08-24 v154 × `feat:printing` | 17 | 1.59 | 10.7× | recurring |
| **monthly** | **2026-08** v154 × `feat:printing` | **29** | **2.77** | **10.5×** | `new` |
| monthly cause-level | 2026-08 `feat:printing` | 36 | 4.5 | 8.0× | above-baseline |

**2026-08-20 is the first day of the cluster** (0 print questions on Aug 15–19,
4 on Aug 20) and the daily detector fires on it at 24.3× lift. That is **one day
after the v154 rollout began** and **12 days before the v155 fix shipped** — a
genuine early warning, not a lagging one.

This is the second incident (after Bitdefender) where total, unmistakable
breakage surfaces immediately, reinforcing that **the lag is a property of the
incident, not of the method**: users retry and wait when something is flaky, but
they post at once when a function is simply dead.

## The fix is visible in the data too — version cohorts, not calendar time

Printing-question rate by cohort (feature table, title-only tagging):

| Cohort | Questions | Printing | Rate |
|:--|--:|--:|--:|
| v154, Aug 20–31 (v154 current) | 191 | 28 | **14.7%** |
| v154, Sep 1–9 (residual users, unpatched) | 38 | 5 | **13.2%** |
| **v155, Sep 1–9 (post-fix)** | **126** | **1** | **0.8%** |
| Jun–Jul 2026 baseline, all versions | 1456 | 9 | 0.6% |

The rate is **version-specific, not time-specific**: it stays at ~13% for v154
users *after* the fix shipped and sits at the historical baseline (0.8% vs 0.6%)
for v155 users. So the support corpus alone reproduces the Bugzilla conclusion —
introduced in 154, fixed in 155 — and the version×cause detector's lift
attribution to v154 is correct rather than coincidental with the release date.

The monthly detector accordingly still flags **2026-09 v154 × `feat:printing`**
(5 questions, 9.6×, `recurring`): correct, and useful — it is measuring the tail
of users who have not yet updated.

## Why title-only matching was required

`feat:*` is the only dimension matched against the **title alone**. Measured on
the corpus, content matching would have buried this signal in noise:

1. **Thunderbird's own Troubleshooting Information** blob — which users paste
   wholesale into questions — contains a literal `Printing / Modified print
   settings` section, so every paste false-matches `feat:printing` regardless of
   the question's subject.
2. **"Please find the attached screenshot"** — matching content tags 237
   questions `feat:attachments` where titles tag 82; the extra 155 are
   overwhelmingly incidental.
3. Ambient vocabulary: "according to a search engine", "I have been searching
   daily for a solution".

A brand name in the body is evidence; a feature word in the body is vocabulary.

## Multilingual confirmation

The cluster appears in eight languages, which is why the `feat:` patterns are
multilingual (~16% of the corpus is non-English):

- en "Thunderbird 154 PDF preview prints blank pages", "URGENT: Thunderbird 154.0
  is unable to print emails"
- it "Stampa completamente bianca dei pdf da anteprima thunderbird"
- nl "Kan bijlage niet meer printen in thunderbird"
- cs "PDF se vytiskne prázdné."
- de/fr/es/pt equivalents via `druck`/`imprim`/`impressão`

## Side effect worth knowing

The same incident also fires `feat:attachments` (wk 2026-08-31, 17 questions,
3.4×) because the titles say "print **attachments**". That is the intended
multi-tag behaviour (a question counts toward every value it matches), but a
reader should recognise the two rows as one incident, not two.
