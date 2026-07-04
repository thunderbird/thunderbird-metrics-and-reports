"""Project 1 — Bucket 1: feature extraction.

Turns one month of scraper concat CSVs (questions + answers) into one tidy
per-question feature table that every later bucket (spike detection, reporting,
sentiment) builds on.

Per question we derive:
  - native dims: os (native operating_system, regex fallback), tb_version /
    tb_version_major (native thunderbird_version), locale, topic, tags
  - text dims (regex over title+content): mail_provider[], isp[], protocol[],
    av[]
  - answer dims: is_answered / first_answer_hours (first NON-creator, non-spam
    answer), num_answers, is_solved / solved_by
  - question_url for the "clickable example questions" requirement

Spam questions are dropped (and counted). No AI — pure pandas + regex.

Usage:
  uv run scripts/project1_extract_features.py 2026-05 desktop
"""
import sys
import csv
import re
import argparse
import pandas as pd

sys.path.insert(0, "scripts")
from project1_regexes import DIMENSIONS, normalize_os, OS_FALLBACK_PATTERNS

csv.field_size_limit(sys.maxsize)

CONCAT_DIR = "CONCATENATED_FILES/{PRODUCT}"
OUT = "PROJECT1/{month}-{product}-features.csv"
QUESTION_URL = "https://support.mozilla.org/questions/{id}"

# Pre-compile every pattern once.
COMPILED = {
    dim: [(tag, re.compile(pat, re.IGNORECASE)) for tag, pat in pats]
    for dim, pats in DIMENSIONS.items()
}
OS_FALLBACK = [(tag, re.compile(pat, re.IGNORECASE)) for tag, pat in OS_FALLBACK_PATTERNS]


def tag_text(text, compiled):
    """Return ';'-joined tags whose pattern matches text (dedup, ordered)."""
    out = []
    for tag, rx in compiled:
        if rx.search(text):
            out.append(tag)
    return ";".join(out)


def clean_version(raw):
    """'150.0.2 (64-bit)' -> '150.0.2'; '' stays ''."""
    v = (raw or "").strip()
    v = re.sub(r"\s*\(.*?\)\s*", "", v)  # strip (64-bit) etc.
    return v.strip()


def major_version(clean):
    """First plausible live-Thunderbird major (100..199 covers 115/128 ESR
    through current 14x/15x), found ANYWHERE in the string. Recovers
    'Version 150.0.2' forms the leading-anchor missed, and the \\b1\\d\\d\\b
    match naturally rejects junk (333333, 1580) and EOL/typo majors
    (91, 78, 18, 10) without a separate range check."""
    m = re.search(r"\b(1\d\d)\b", clean or "")
    return m.group(1) if m else ""


def build_features(q, a):
    """Core feature extraction, shared by the per-month CLI and the full-history
    backfill (project1_backfill_features.py).

    Inputs are the raw questions/answers DataFrames (str dtype,
    keep_default_na=False, scraper schema). Returns (features_df, total_q,
    n_spam); spam questions are dropped. `created` is parsed with format="mixed"
    so both old-API ('... -0700') and scraper ISO ('...Z') timestamps survive.
    """
    total_q = len(q)
    is_spam = q["is_spam"].str.strip().str.lower().isin(["true", "1", "yes"])
    n_spam = int(is_spam.sum())
    q = q[~is_spam].copy()

    q["created_dt"] = pd.to_datetime(q["created"], utc=True, format="mixed",
                                     errors="coerce")

    # --- first non-creator, non-spam answer time per question ---------------
    a = a.copy()
    a["created_dt"] = pd.to_datetime(a["created"], utc=True, format="mixed",
                                     errors="coerce")
    a_spam = a["is_spam"].str.strip().str.lower().isin(["true", "1", "yes"])
    a = a[~a_spam]
    creator_by_qid = dict(zip(q["id"], q["creator"]))
    a["q_creator"] = a["question_id"].map(creator_by_qid)
    non_creator = a[a["creator"].str.strip() != a["q_creator"].fillna("").str.strip()]
    first_ans = non_creator.groupby("question_id")["created_dt"].min()

    rows = []
    for _, r in q.iterrows():
        qid = r["id"]
        text = f"{r.get('title', '')}\n{r.get('content', '')}"

        os_tag = normalize_os(r.get("operating_system", ""))
        if not os_tag:  # regex fallback only when native is blank
            os_tag = tag_text(text, OS_FALLBACK).split(";")[0] if tag_text(text, OS_FALLBACK) else ""

        ver = clean_version(r.get("thunderbird_version", ""))

        fa = first_ans.get(qid)
        created = r["created_dt"]
        if pd.notna(fa) and pd.notna(created):
            first_answer_hours = round((fa - created).total_seconds() / 3600.0, 2)
        else:
            first_answer_hours = ""

        row = {
            "id": qid,
            "created": r["created"],
            "created_date": created.date().isoformat() if pd.notna(created) else "",
            "locale": r.get("locale", ""),
            "topic": r.get("topic", ""),
            "tags": r.get("tags", ""),
            "creator": r.get("creator", ""),
            "title": (r.get("title", "") or "")[:120],
            "question_url": QUESTION_URL.format(id=qid),
            "os": os_tag,
            "os_raw": r.get("operating_system", ""),
            "macos_release": tag_text(text, COMPILED["macos_release"]),
            "tb_version": ver,
            "tb_version_major": major_version(ver),
            "mail_provider": tag_text(text, COMPILED["mail_provider"]),
            "protocol": tag_text(text, COMPILED["protocol"]),
            "av": tag_text(text, COMPILED["av"]),
            "num_answers": r.get("num_answers", ""),
            "is_answered": "true" if pd.notna(fa) else "false",
            "first_answer_hours": first_answer_hours,
            "is_solved": r.get("is_solved", ""),
            "solved_by": r.get("solved_by", ""),
        }
        rows.append(row)

    return pd.DataFrame(rows), total_q, n_spam


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("month", help="YYYY-MM, e.g. 2026-05")
    ap.add_argument("product", choices=["desktop", "android"])
    args = ap.parse_args()
    month, product = args.month, args.product
    cdir = CONCAT_DIR.format(PRODUCT=product.upper())

    q = pd.read_csv(f"{cdir}/{month}-sumo-{product}-questions.csv",
                    dtype=str, keep_default_na=False)
    a = pd.read_csv(f"{cdir}/{month}-sumo-{product}-answers.csv",
                    dtype=str, keep_default_na=False)

    feats, total_q, n_spam = build_features(q, a)
    out_path = OUT.format(month=month, product=product)
    feats.to_csv(out_path, index=False)

    # --- coverage summary ----------------------------------------------------
    n = len(feats)
    def pct(mask):
        return f"{int(mask.sum())}/{n} ({100*mask.sum()/n:.0f}%)"
    nonblank = lambda c: feats[c].str.strip() != ""
    print(f"=== {month} {product} — feature extraction ===")
    print(f"questions: {total_q} total, {n_spam} spam dropped, {n} kept")
    print(f"wrote {out_path}")
    print()
    print("DIMENSION COVERAGE (questions with >=1 tag):")
    print(f"  os:            {pct(nonblank('os'))}")
    print(f"  tb_version:    {pct(nonblank('tb_version'))}")
    print(f"  mail_provider: {pct(nonblank('mail_provider'))}")
    print(f"  protocol:      {pct(nonblank('protocol'))}")
    print(f"  av:            {pct(nonblank('av'))}")
    print(f"  is_answered:   {pct(feats['is_answered'] == 'true')}")
    fa = pd.to_numeric(feats["first_answer_hours"], errors="coerce").dropna()
    if len(fa):
        print(f"  first_answer_hours (answered): median={fa.median():.1f}h  "
              f"p25={fa.quantile(.25):.1f}h  p75={fa.quantile(.75):.1f}h")
    print()

    def top(col, k=12):
        ctr = {}
        for cell in feats[col]:
            for t in (cell.split(";") if cell else []):
                if t:
                    ctr[t] = ctr.get(t, 0) + 1
        items = sorted(ctr.items(), key=lambda x: -x[1])[:k]
        return ", ".join(f"{t}={c}" for t, c in items) or "(none)"

    for dim in ["os", "mail_provider", "protocol", "av", "macos_release"]:
        print(f"TOP {dim}: {top(dim)}")
    print("TOP tb_version_major:", top("tb_version_major"))


if __name__ == "__main__":
    main()
