"""Project "LLM Insights" — Stage 2 (reduce): narrative + ranked issues report.

Turns the per-question labels from Stage 1 (llm_insights_classify.py) into the
engineering-management month-over-month deliverable: a plain-English narrative +
a ranked, evidence-linked list of the issues worth engineering attention.

Division of labour (see BUCKET2 key finding — discovered themes are ~all-unique,
so they don't group by string match):
  - Python does ALL the counting (exact per-cluster MoM deltas, severity, value
    signals) — LLMs can't count 1,500 rows reliably.
  - The LLM does the two things only it can: (1) SEMANTIC CLUSTERING of the free-
    text themes into named engineering issues, and (2) the NARRATIVE + per-issue
    "why / what to look at" prose.
  - Ranking is a transparent Python formula (weights new/emerging + worst-served
    highest, per the project goal); the LLM narrates the ranked result.

Cost is estimated + gated ($50) before each LLM call; actual printed after.

Usage:
  uv run scripts/llm_insights_mom_report.py 2026-06 2026-05 --latest
"""
import sys
import os
import json
import argparse
from datetime import datetime, timezone

import pandas as pd

sys.path.insert(0, "scripts")
from llm_insights_cost import (dollars, gate, response_text, PRICING,
                               CONCAT_DIR)
from llm_insights_classify import CATEGORIES

MODEL = "claude-opus-5"
LABELS = "LLM_INSIGHTS/{m}-{product}-labels.csv"
REPORT_DIR = "LLM_INSIGHTS/REPORTS/{product}"
QUESTION_URL = "https://support.mozilla.org/questions/{id}"
TOP_N = 12          # ranked issues to feature
MIN_CLUSTER = 3     # a featured cluster needs >= this many current-month questions


def human_month(m):
    return datetime.strptime(m, "%Y-%m").strftime("%B %Y")


def md_safe(s):
    return (s or "").replace("|", "¦").replace('"', "＂")[:80]


def delta(old, new, pct=True):
    d = new - old
    arrow = "▲" if d > 0 else ("▼" if d < 0 else "▬")
    txt = f"{arrow} {'+' if d > 0 else ''}{d:g}"
    if pct and old >= 10:
        txt += f" ({'+' if d >= 0 else ''}{100 * d / old:.0f}%)"
    return txt


def tb(series):
    return series.astype(str).str.strip().str.lower() == "true"


def load_labels(m, product="desktop"):
    df = pd.read_csv(LABELS.format(m=m, product=product), dtype=str, keep_default_na=False)
    df["severity"] = pd.to_numeric(df["severity"], errors="coerce").fillna(0).astype(int)
    df["n_answers"] = pd.to_numeric(df["n_answers"], errors="coerce").fillna(0).astype(int)
    df["solved_b"] = tb(df["is_solved"])
    df["trusted_last_b"] = tb(df["last_answer_trusted"])
    df["new_b"] = tb(df["is_new_or_notable"])
    return df


def load_titles(m, product="desktop"):
    p = (f"{CONCAT_DIR.format(PRODUCT=product.upper())}/"
         f"{m}-sumo-{product}-questions.csv")
    q = pd.read_csv(p, dtype=str, keep_default_na=False)
    return dict(zip(q["id"], q["title"]))


# ---- Stage 2b: LLM semantic clustering of themes -------------------------- #

CLUSTER_SYS = """You are grouping Thunderbird support-question THEMES into named \
engineering issues. You are given a numbered list of distinct theme phrases (each \
with how many questions used it and its category). Group them so that themes \
describing THE SAME underlying problem share a cluster, even when worded \
differently (e.g. "can receive but cannot send email", "smtp relay access denied \
on send", "outgoing mail fails" → one cluster). Aim for roughly 30-60 clusters; \
do not over-merge distinct problems. Give each cluster a concise, specific, \
engineering-facing label (a problem, not a category — e.g. "Spectrum/Charter IMAP \
certificate not trusted", not "email issues"). Assign EVERY index to EXACTLY ONE \
cluster."""

CLUSTER_SCHEMA = {
    "type": "object", "additionalProperties": False,
    "properties": {
        "clusters": {
            "type": "array",
            "items": {
                "type": "object", "additionalProperties": False,
                "properties": {
                    "label": {"type": "string"},
                    "category": {"type": "string", "enum": CATEGORIES},
                    "member_indices": {"type": "array", "items": {"type": "integer"}},
                },
                "required": ["label", "category", "member_indices"],
            },
        }
    },
    "required": ["clusters"],
}


def cluster_themes(client, all_df, usage):
    """Return dict theme_string -> cluster_label via one LLM call."""
    # unique themes with count + dominant category
    g = (all_df.groupby("discovered_theme")
         .agg(n=("id", "size"),
              cat=("category", lambda s: s.mode().iat[0] if not s.mode().empty else "other"))
         .reset_index())
    themes = g["discovered_theme"].tolist()
    lines = [f"{i}\t{r.discovered_theme}  (n={r.n}, cat={r.cat})"
             for i, r in enumerate(g.itertuples())]
    user = ("Cluster these themes. Return every index exactly once.\n\n"
            + "\n".join(lines))
    system = [{"type": "text", "text": CLUSTER_SYS,
               "cache_control": {"type": "ephemeral"}}]

    ct = client.messages.count_tokens(model=MODEL, system=system,
                                      messages=[{"role": "user", "content": user}])
    est = dollars(ct.input_tokens, len(themes) * 6 + 3000, MODEL)
    print(f"[cluster] {len(themes)} unique themes, est input {ct.input_tokens:,} tok")
    gate(est, label="Stage-2 clustering")

    resp = client.messages.create(
        model=MODEL, max_tokens=12000, system=system,
        # Disabled deliberately: opus-5 thinks by default, and this is a
        # mechanical grouping pass whose max_tokens must all go to the JSON.
        thinking={"type": "disabled"},
        output_config={"format": {"type": "json_schema", "schema": CLUSTER_SCHEMA},
                       "effort": "low"},
        messages=[{"role": "user", "content": user}],
    )
    _add_usage(usage, resp)
    clusters = json.loads(response_text(resp, "Stage-2 clustering"))["clusters"]

    theme_to_label = {}
    assigned = set()
    for c in clusters:
        for idx in c["member_indices"]:
            if 0 <= idx < len(themes) and idx not in assigned:
                theme_to_label[themes[idx]] = c["label"]
                assigned.add(idx)
    # fallback for any theme the model dropped: its own theme as a singleton label
    for i, t in enumerate(themes):
        theme_to_label.setdefault(t, t[:60])
    print(f"[cluster] {len(clusters)} clusters; "
          f"{len(themes) - len(assigned)} themes fell back to singletons")
    return theme_to_label


# ---- Stage 2 (Python): per-cluster stats + ranking ------------------------ #

def cluster_stats(cur, prev, theme_to_label, titles):
    cur = cur.copy(); prev = prev.copy()
    cur["cluster"] = cur["discovered_theme"].map(theme_to_label)
    prev["cluster"] = prev["discovered_theme"].map(theme_to_label)
    prev_counts = prev["cluster"].value_counts().to_dict()

    rows = []
    for label, grp in cur.groupby("cluster"):
        n_cur = len(grp)
        n_prev = int(prev_counts.get(label, 0))
        served = (grp["solved_b"] | grp["trusted_last_b"]).mean()
        unanswered = (grp["n_answers"] == 0).mean()
        mean_sev = grp["severity"].mean()
        n_sev4 = int((grp["severity"] >= 4).sum())
        cat = grp["category"].mode().iat[0] if not grp["category"].mode().empty else "other"
        # example ids: current month, severity desc, up to 6
        ex = (grp.sort_values("severity", ascending=False)["id"].head(6).tolist())
        is_new = n_prev == 0 and n_cur >= 2
        growth = n_cur - n_prev
        unserved = 1 - served
        score = (n_cur * (mean_sev / 3.0) * (0.6 + 0.8 * unserved)
                 + max(growth, 0) * 1.5 + (8 if is_new else 0))
        rows.append({
            "label": label, "category": cat, "cur": n_cur, "prev": n_prev,
            "growth": growth, "mean_sev": round(mean_sev, 1), "n_sev4": n_sev4,
            "served_pct": int(round(served * 100)),
            "unanswered_pct": int(round(unanswered * 100)),
            "is_new": is_new, "score": round(score, 1), "examples": ex,
        })
    df = pd.DataFrame(rows).sort_values("score", ascending=False)
    return df


# ---- Stage 2c: LLM narrative --------------------------------------------- #

NARR_SYS = """You are writing a month-over-month support-insights briefing for \
Thunderbird ENGINEERING MANAGEMENT (not community/support ops). You are given \
exact statistics (already computed — trust them, do not invent numbers) for the \
top issues this month vs last, plus category totals. Audience wants to know: what \
emerging or worsening problem should engineering look at now? Weight NEW/EMERGING \
issues and WORST-SERVED user pain (low resolved rate) highest; big-but-well-handled \
load is lower priority. Be concrete and specific; name likely root causes; never \
pad. This is an LLM-derived signal over free-text support questions — a triage \
pointer, not proof."""

NARR_SCHEMA = {
    "type": "object", "additionalProperties": False,
    "properties": {
        "headline": {"type": "string"},
        "narrative_md": {"type": "string"},
        "issues": {
            "type": "array",
            "items": {
                "type": "object", "additionalProperties": False,
                "properties": {
                    "rank": {"type": "integer"},
                    "why": {"type": "string"},
                    "action": {"type": "string"},
                },
                "required": ["rank", "why", "action"],
            },
        },
    },
    "required": ["headline", "narrative_md", "issues"],
}


def narrate(client, cur_m, prev_m, top, cat_mom, headline_stats, usage):
    payload = {
        "current_month": human_month(cur_m),
        "previous_month": human_month(prev_m),
        "headline": headline_stats,
        "category_totals": cat_mom,
        "top_issues": [
            {"rank": i + 1, "label": r["label"], "category": r["category"],
             "prev": r["prev"], "cur": r["cur"], "growth": r["growth"],
             "mean_severity": r["mean_sev"], "n_severity4plus": r["n_sev4"],
             "resolved_pct": r["served_pct"], "unanswered_pct": r["unanswered_pct"],
             "is_new_this_month": r["is_new"]}
            for i, (_, r) in enumerate(top.iterrows())
        ],
    }
    user = ("Write the briefing. Return: a one-line headline; a 2-4 short-"
            "paragraph narrative in markdown (lead with the outcome); and for each "
            "ranked issue a 1-sentence `why` it matters and a 1-sentence `action` "
            "(what engineering should look at). Reference issues by their rank.\n\n"
            + json.dumps(payload, ensure_ascii=False))
    system = [{"type": "text", "text": NARR_SYS}]

    ct = client.messages.count_tokens(model=MODEL, system=system,
                                      messages=[{"role": "user", "content": user}])
    est = dollars(ct.input_tokens, 4000, MODEL)
    print(f"[narrate] est input {ct.input_tokens:,} tok")
    gate(est, label="Stage-2 narrative")

    resp = client.messages.create(
        model=MODEL, max_tokens=8000, system=system,
        thinking={"type": "adaptive"},
        output_config={"format": {"type": "json_schema", "schema": NARR_SCHEMA},
                       "effort": "high"},
        messages=[{"role": "user", "content": user}],
    )
    _add_usage(usage, resp)
    return json.loads(response_text(resp, "Stage-2 narrative"))


# ---- rendering ------------------------------------------------------------ #

def links(ids, titles):
    L = " ".join(f'[{i}]({QUESTION_URL.format(id=i)} "{md_safe(titles.get(i, ""))}")'
                 for i in ids[:5])
    return L + (f" +{len(ids) - 5}" if len(ids) > 5 else "")


def render(cur_m, prev_m, cur, prev, top, cat_mom_rows, narr, titles, cost,
           product="desktop"):
    issue_prose = {x["rank"]: x for x in narr.get("issues", [])}
    pcap = product.capitalize()
    out, W = [], lambda s: out.append(s)
    W("---")
    W("layout: base")
    W(f"title: {pcap} LLM Insights — {human_month(cur_m)}")
    W("---")
    W("")
    W(f"# Thunderbird {pcap} — LLM Insights (Engineering)")
    W(f"\n## {human_month(cur_m)} vs {human_month(prev_m)}\n")
    W("_The **AI counterpart to Project 1**: Claude reads every support question "
      "(plus the creator's own follow-ups, the accepted solution, and trusted-"
      "contributor replies), names the concrete problem, hypothesises a root cause, "
      "and rates severity — surfacing emerging / worst-served pain that regex + "
      "stats can't. Counts are exact (computed in Python); clustering and prose are "
      "LLM-derived. A triage pointer, not proof._\n")

    W("## Headline\n")
    W(f"| | {human_month(prev_m)} | {human_month(cur_m)} | Change |")
    W("|:--|--:|--:|:--|")
    W(f"| Support questions (load) | {len(prev)} | {len(cur)} | {delta(len(prev), len(cur))} |")
    W(f"| Distinct issue clusters | {top.attrs['n_clusters_prev']} | "
      f"{top.attrs['n_clusters']} | {delta(top.attrs['n_clusters_prev'], top.attrs['n_clusters'], pct=False)} |")
    W(f"| New issue clusters this month | — | {int(top['is_new'].sum()) if len(top) else 0} | |")
    W("")
    if narr.get("headline"):
        W(f"**{narr['headline']}**\n")
    if narr.get("narrative_md"):
        W(narr["narrative_md"] + "\n")

    W("## 🚨 Issues to investigate\n")
    W("_Ranked by a transparent score weighting new/emerging + worst-served "
      "(low resolved %) + severity + volume. **Resolved %** = solved or a trusted "
      "contributor gave the last word; ⚠️ marks poorly-served clusters._\n")
    for i, (_, r) in enumerate(top.iterrows(), 1):
        flag = " ⚠️" if r["served_pct"] < 50 else ""
        new = " · 🆕 new this month" if r["is_new"] else ""
        W(f"### {i}. {r['label']}{new}\n")
        W(f"| Cluster | {human_month(prev_m)} | {human_month(cur_m)} | Change | "
          f"Sev (≥4) | Resolved | Unanswered |")
        W("|:--|--:|--:|:--|:--|:--|--:|")
        W(f"| {md_safe(r['label'])} ({r['category']}) | {r['prev']} | {r['cur']} | "
          f"{delta(r['prev'], r['cur'])} | {r['mean_sev']} ({r['n_sev4']}) | "
          f"{r['served_pct']}%{flag} | {r['unanswered_pct']}% |")
        W("")
        p = issue_prose.get(i)
        if p:
            W(f"- **Why:** {p['why']}")
            W(f"- **Look at:** {p['action']}")
        W(f"- **Examples:** {links(r['examples'], titles)}")
        W("")

    W("## Category mix — month over month\n")
    W(f"| Category | {human_month(prev_m)} | {human_month(cur_m)} | Change |")
    W("|:--|--:|--:|:--|")
    for c in cat_mom_rows:
        W(f"| {c['category']} | {c['prev']} | {c['cur']} | {delta(c['prev'], c['cur'])} |")
    W("")

    W("---")
    W(f"\n_Prototype LLM-insights report · Claude {MODEL} over Stage-1 per-question "
      f"labels · {human_month(cur_m)} vs {human_month(prev_m)} · this run cost "
      f"${cost:.2f}._")
    W(f"\n_Last updated: {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}_")
    return "\n".join(out) + "\n"


def _add_usage(usage, resp):
    u = resp.usage
    usage["in"] += u.input_tokens
    usage["out"] += u.output_tokens
    usage["cr"] += getattr(u, "cache_read_input_tokens", 0) or 0
    usage["cw"] += getattr(u, "cache_creation_input_tokens", 0) or 0


def actual_cost(usage):
    ir, orr = PRICING[MODEL]
    return (usage["in"] / 1e6 * ir + usage["cw"] / 1e6 * ir * 1.25
            + usage["cr"] / 1e6 * ir * 0.10 + usage["out"] / 1e6 * orr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("current", help="YYYY-MM")
    ap.add_argument("previous", help="YYYY-MM")
    ap.add_argument("product", nargs="?", default="desktop",
                    choices=["desktop", "android"])
    ap.add_argument("--latest", action="store_true")
    args = ap.parse_args()

    if not os.getenv("ANTHROPIC_API_KEY"):
        print("🛑 ANTHROPIC_API_KEY not set.", file=sys.stderr); sys.exit(2)
    from anthropic import Anthropic
    client = Anthropic()

    cur = load_labels(args.current, args.product)
    prev = load_labels(args.previous, args.product)
    titles = {**load_titles(args.previous, args.product),
              **load_titles(args.current, args.product)}
    all_df = pd.concat([prev, cur], ignore_index=True)
    usage = {"in": 0, "out": 0, "cr": 0, "cw": 0}

    theme_to_label = cluster_themes(client, all_df, usage)
    top = cluster_stats(cur, prev, theme_to_label, titles)
    top.attrs["n_clusters"] = int(cur["discovered_theme"].map(theme_to_label).nunique())
    top.attrs["n_clusters_prev"] = int(prev["discovered_theme"].map(theme_to_label).nunique())

    featured = top[(top["cur"] >= MIN_CLUSTER) | top["is_new"]].head(TOP_N)

    # category MoM (deterministic)
    cc = cur["category"].value_counts().to_dict()
    pc = prev["category"].value_counts().to_dict()
    cats = sorted(set(cc) | set(pc), key=lambda c: -cc.get(c, 0))
    cat_mom = [{"category": c, "cur": int(cc.get(c, 0)), "prev": int(pc.get(c, 0))}
               for c in cats]
    headline_stats = {"questions_prev": len(prev), "questions_cur": len(cur),
                      "new_clusters": int(featured["is_new"].sum())}

    narr = narrate(client, args.current, args.previous, featured, cat_mom,
                   headline_stats, usage)

    cost = actual_cost(usage)
    print(f"\n💵 ACTUAL Stage-2 cost: ${cost:.4f}  "
          f"(in {usage['in']:,} | cache_read {usage['cr']:,} | out {usage['out']:,})")

    content = render(args.current, args.previous, cur, prev, featured, cat_mom,
                     narr, titles, cost, args.product)
    rdir = REPORT_DIR.format(product=args.product)
    os.makedirs(rdir, exist_ok=True)
    path = f"{rdir}/monthly-summary-{args.current}-vs-{args.previous}.md"
    with open(path, "w") as f:
        f.write(content)
    print(f"   wrote {path}")
    if args.latest:
        latest = f"{rdir}/monthly-summary-latest.md"
        with open(latest, "w") as f:
            f.write(content)
        print(f"   wrote {latest}")


if __name__ == "__main__":
    main()
