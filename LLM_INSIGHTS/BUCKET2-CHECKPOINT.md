# Project "LLM Insights" — resume / Bucket-2 checkpoint (working note, not for publishing)

_Written 2026-07-04 evening so work can resume in the morning even if the session is lost._
_Full plan: `~/.claude/plans/validated-munching-emerson.md`. Persistent decisions are also in Claude memory._

## What this project is
AI counterpart to Project 1 (no-AI regex+stats). **Phase 1 = desktop only**, engineering-management
month-over-month report. **Core decision it drives:** "What emerging or worsening desktop support pain
should engineering look at right now?" PoC = **June 2026 vs May 2026**, output = **narrative + ranked issues**.

## Locked decisions (do not relitigate)
1. **Desktop only** for PoC + Phase 1; android later.
2. **PoC output = narrative + ranked issues** (one-page MoM story + ranked evidence-linked issue list).
3. **Cost discipline:** estimate before every LLM spend; **hard $50/run circuit-breaker** (`gate()`).
   Cost is NOT the constraint (~$0.0065/q, ~$10 for May+June at Opus) — quality is what we optimize.
4. **Model = `claude-opus-4-8`** throughout the PoC.
5. **"Question" = question + all creator answers**; the **accepted solution** and a **trusted
   contributor's last-in-thread answer** are **higher value** — fed to the LLM as authoritative context
   AND carried as per-question signals for Stage-2 ranking. (`build_enriched`)
6. HTML stripped from content; **English themes** (corpus ~16% non-English), verbatim quotes kept.
7. Architecture = **map→reduce**. Map = per-question structured classify. Reduce = cluster in Python +
   one Opus call → narrative + ranked issues → Jekyll page.

## Files
- `scripts/llm_insights_cost.py` — pricing table, `dollars()`, `gate()` ($50), `load_desktop_questions`,
  `build_enriched(month)` (enriched text + value signals), Bucket-0 cost preview (`__main__`).
- `scripts/llm_insights_classify.py` — Stage-1 map. `uv run scripts/llm_insights_classify.py YYYY-MM [--sample N]`.
- Outputs: `LLM_INSIGHTS/{month}-desktop-labels.csv` (LLM labels + value signals).
- Reuse for Bucket 3: `scripts/project1_mom_report.py` (layout: base, `md_safe` `|`→¦ `"`→＂, blank-line-
  before-table, question-id→link+tooltip+`+N`, `-latest` copy). Bucket 4: clone
  `.github/workflows/gha-project1-desktop-spike-reports.yml` + add `ANTHROPIC_API_KEY` secret.

## Bucket status
- ✅ Bucket 0 (cost harness+loader, $0) — counts verified 812/724.
- ✅ Bucket 1 (20-q sample, **$0.126**) — quality good; value signals merged.
- ⏳ **Bucket 2 (full May+June classify) — IN PROGRESS at session end.**
  - **May: DONE — actual $5.40, 812 rows → `LLM_INSIGHTS/2026-05-desktop-labels.csv`.**
  - June: running (~724 q, est ~$4.8). Results appended below when finished.
- ⬜ Bucket 3 (reduce → narrative + ranked issues → Jekyll page) — **GO/NO-GO proof of value.** NOT STARTED.
- ⬜ Bucket 4 (daily + GitHub Action) — only if Bucket 3 proves value.

## NEXT MORNING — do this
1. Confirm `LLM_INSIGHTS/2026-06-desktop-labels.csv` exists with ~724 rows (if June didn't finish,
   re-run: `uv run scripts/llm_insights_classify.py 2026-06`). ANTHROPIC_API_KEY is in `~/.zshenv`.
2. Read the **Bucket-2 results** section below (total cost + theme distribution) — that's the checkpoint.
3. Get user sign-off, then start **Bucket 3** (Stage-2 reduce + Jekyll render).

---

## Bucket-2 results — COMPLETE ✅

**Cost (actual):** May $5.40 + June $4.73 = **$10.13 total** (est was ~$10; under $50 gate). No errors,
every question labeled (no "returned no label" warnings). Prompt caching worked (cache_read 95k May / 86k June).

**Rows:** May 812, June 724 → 1,536. Files: `LLM_INSIGHTS/2026-05-desktop-labels.csv`,
`LLM_INSIGHTS/2026-06-desktop-labels.csv`.

### Category — May → June (Δ) — the MoM signal preview
(Overall volume fell 812→724, ~11%, so read drops relative to that baseline; risers are the real story.)
```
  send-receive          180 → 158  (-22)
  account-login         135 → 101  (-34)
  ui-ux                 111 →  86  (-25)
  performance-crash      45 →  71  (+26)   <-- biggest RISER, against the volume trend
  migration-import       59 →  64  (+5)
  settings-config        64 →  43  (-21)
  calendar-tasks         28 →  37  (+9)
  search-folders         59 →  35  (-24)
  spam-filters           26 →  28  (+2)
  sync-oauth             37 →  28  (-9)
  other                  33 →  27  (-6)
  encryption-security    19 →  20  (+1)
  addons-extensions       6 →  15  (+9)    <-- small base, but doubled+
  attachments            10 →  11  (+1)
```

### Severity (May / June): sev5 steady at 32/32; sev4 185→196; mostly 2-3.
### is_new_or_notable: 260/812 May, 213/724 June (~30% — likely too generous; reduce stage re-ranks).
### Value signals (total 1,536): solved 325 (21%) · has_solution 325 · last_answer_trusted 850 (55%) · has_trusted_answer 1,124 (73%).

### ⚠️ KEY FINDING for Bucket 3 (design decision)
`discovered_theme` is **1,521 unique / 1,536 questions** — raw themes DO NOT cluster by string match.
**Bucket 3's reduce stage MUST do semantic clustering** (an LLM clustering/merge pass over the theme
list, or embeddings), then compute MoM deltas per *cluster*. The category axis (14 buckets) already
clusters well and gives a usable MoM signal on its own — use it as the coarse layer, semantic theme
clusters as the fine layer.
Cross-check win: the LLM independently surfaced the **Charter/Spectrum `mobile.charter.net:993`
certificate-not-trusted** cluster (~5 questions) — the same incident Project 1 validated as
`v151 × m:spectrum`. Good evidence the LLM finds real, engineering-actionable clusters.

## Bucket 3 — COMPLETE ✅ (cost $0.60) — PoC proved out; AWAITING user GO/NO-GO

Script: `scripts/llm_insights_mom_report.py`. Run:
`uv run scripts/llm_insights_mom_report.py 2026-06 2026-05 --latest`
Output: `LLM_INSIGHTS/REPORTS/desktop/monthly-summary-2026-06-vs-2026-05.md` (+ `-latest`). Kramdown-validated.
Preview in browser: strip YAML front matter → kramdown → html → `open` (see the ruby one-liner used;
wrote `/tmp/llm-insights-preview.html`).

**Design (locked):** Python does ALL exact counts + ranking (LLMs can't count 1,500 rows); LLM does only
(a) semantic clustering of the ~1,521 free-text themes into named issues, (b) narrative + per-issue
why/action prose. Ranking score (transparent, in `cluster_stats`): weights **new/emerging + worst-served
(low resolved %) + severity + volume** — resolved% = solved OR trusted-contributor last answer; ⚠️ if <50%.

**What it surfaced (proof of value = STRONG):**
- Rank 1: startup freeze/crash 24→60 (2.5×) against −11% volume — regression signature.
- Ranks 8/9 (NOVEL, regex-invisible, worst-served): attachments dropped on forward 0→5 (20% resolved);
  emails auto-moved to Trash/Junk 0→5 (20% resolved, 40% unanswered).
- Rank 5: Charter/Spectrum untrusted cert 0→7 = Project 1's validated `v151 × m:spectrum` (cross-check ✅).

**PoC TOTAL SPEND ≈ $10.9** (B1 $0.13 + B2 $10.13 + B3 $0.60). Steady-state monthly ~$5.

**Tuning debt (minor, not blockers):** (1) clustering made 166 clusters vs 30-60 target, 89 singletons —
inflates the "distinct clusters" headline only (top-12 clean); tighten via CLUSTER_SYS prompt.
(2) narrative returned why/action for 9/12 issues (ranks 6,10,12 got only links) — enforce full coverage.

## RESUME — awaiting user's GO/NO-GO on the PoC. Three branches:
1. **GO → Bucket 4:** clone `.github/workflows/gha-project1-desktop-spike-reports.yml` (needs `aaq-data/`
   checkout) for a daily/twice-daily run; add `ANTHROPIC_API_KEY` repo secret; classify current month
   incrementally then run the MoM report; commit `LLM_INSIGHTS/`; link `-latest` from repo `index.md`.
   NOTE for daily: switch classify's per-batch count_tokens gate to sample-based (halves wall-clock) —
   user pre-approved this optimization.
2. **Tune first:** fix the two tuning-debt items, regenerate, re-checkpoint, then Bucket 4.
3. **Rethink:** adjust format/ranking if it's not hitting the mark.

All scripts: `scripts/llm_insights_{cost,classify,mom_report}.py`. Key in `~/.zshenv`. Model `claude-opus-4-8`.
Plan: `~/.claude/plans/validated-munching-emerson.md`. Persistent decisions in Claude memory (auto-loads).
