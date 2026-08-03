# Detector back-test — Bitdefender breakage, 11–14 Aug 2025

A known real-world incident used as a back-test of the Project 1 spike detector.
Companion to `README.md` (which validates *volume*, not detection).

## The incident (ground truth, external)

A **Bitdefender update broke Thunderbird desktop for ~4 days, 11–14 August 2025**.
Symptom: incoming mail rendered as **raw HTML source with no subject and no
sender**. The bug was on the AV side (mail-scanning / content-filter proxy), not
in Thunderbird.

## Verdict: CAUGHT — day one, at all three detector grains

The `av:bitdefender` regex (`bitdefender|gravityzone`, `project1_regexes.py`)
tagged **49 desktop questions in August 2025**, 48 of them inside the incident
window:

| created_date | questions |
|---|---|
| 2025-08-11 | 11 |
| 2025-08-12 | 19 |
| 2025-08-13 | 15 |
| 2025-08-14 | 3 |
| 2025-08-22 | 1 (tail) |

`project1_spike_detect.py` fired on it in every grain (rows are in the committed
spike CSVs — nothing was re-run for this back-test):

**`desktop-daily-single-spikes.csv`** — fired on the incident's *first* day and
the two after:

| period | dim | value | count | baseline_median | magnitude | kind |
|---|---|---|---|---|---|---|
| 2025-08-11 | av | av:bitdefender | 11 | 0.0 | new | new/dormant |
| 2025-08-12 | av | av:bitdefender | 19 | 0.0 | new | new/dormant |
| 2025-08-13 | av | av:bitdefender | 15 | 0.0 | new | new/dormant |

**`desktop-weekly-single-spikes.csv`** — week of 2025-08-11: 48 questions,
baseline 0.0, `new/dormant`.

**`desktop-monthly-single-spikes.csv`** — 2025-08: 49 questions vs baseline
median 1.0 → **49× above baseline**.

Aug 14 (3 questions) fell below the daily `min_count=8` floor, but by then the
detector had already fired three days running. The daily grain is what matters
for a 4-day incident; weekly/monthly are confirmation.

Example questions (from the 2025-08-12 spike row's `example_urls`):
[1528644](https://support.mozilla.org/questions/1528644),
[1528675](https://support.mozilla.org/questions/1528675),
[1528715](https://support.mozilla.org/questions/1528715) — titles like
*"Messages are suddenly not showing subject or from, and body"*, *"Emails
appearing in HTML format (bitdefender)"*, *"Emails are corrupted (bitdefender)"*.

## What would NOT have caught it

**The headline version×cause detector would have shown nothing.** August 2025
predates the version backfill's useful range: **0.1% of all Aug-2025 desktop
questions carry a version**, and 48 of the 49 Bitdefender questions are
`tb_version_major = unknown` (one is v142). The joint spike CSVs start at
2026-02 for exactly this reason.

This is the **second independent argument for keeping the cause-level signal
co-equal with version×cause in the report** — and it is a *different* argument
from the GMX one:

- **GMX (2026-03)** — versioned data existed, but the incident **spanned
  versions** (v140/v148), so version×cause diluted it below threshold.
- **Bitdefender (2025-08)** — version×cause was **structurally blind**: no
  version data existed at all.

Either way, the incident is a cause-level fact, not a release regression. An
AV-vendor breakage is *never* version-correlated in principle — it hits whatever
Thunderbird the user is running.

## Other things this back-test confirms

- **Timing is not always lagging.** The ⏱ caveat (spikes date when users piled
  in, not incident onset — validated on Jun-2023 Libero, where the spike landed
  on the *resolution* date) does **not** bite here: the detector fired on day 1.
  The pile-in was immediate because the symptom was total and unmistakable. So
  the lag is a property of the *incident's* visibility to users, not a fixed
  property of the method — fast, obvious, total-breakage incidents surface fast.
- **The responsiveness amplifier (#68) reads "well-served", not "⚠️".**
  `answered_pct = 100`, median first answer **0.6h on day 1**, 2.6h across the
  week, 0 unanswered. No ⚠️ flag. Read correctly, that is still signal: a large,
  *perfectly*-served cluster means the community knew the fix and was repeating
  it 48 times — a candidate for a KB article / pinned answer, which is a
  community-ops action rather than an engineering one.
- **The detector clusters; it does not attribute.** The output says
  "av:bitdefender is spiking", not "a Bitdefender update broke Thunderbird".
  Causal direction (AV broke Thunderbird vs Thunderbird broke AV interop vs
  coincidence) still needs a human read of the questions — or Project
  "LLM insights".
- The `av` dimension earns its place. It is low-volume most months (Aug 2025
  runner-up: `av:norton`, 6) which is exactly why a `new/dormant` AV spike is
  high-signal.

## Reproducing

Everything below reads committed CSVs; no regeneration needed.

```bash
# the tagged questions
uv run python -c "
import pandas as pd
d = pd.read_csv('PROJECT1/2025-08-desktop-features.csv', engine='python')
bd = d[d.av.fillna('').str.contains('bitdefender')]
print(bd.groupby('created_date').size())"

# the detector rows, all grains
uv run python -c "
import pandas as pd
for g in ['daily','weekly','monthly']:
    d = pd.read_csv(f'PROJECT1/desktop-{g}-single-spikes.csv')
    print(g); print(d[d.value=='av:bitdefender'][
      ['period','count','baseline_median','magnitude','kind','answered_pct',
       'median_first_answer_h']].to_string(index=False))"
```

Note `question_ids` in the spike CSVs is **space**-delimited (the `tags` column
in the source questions CSVs is the semicolon-delimited one).
