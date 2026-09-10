"""Project "LLM Insights" — Stage 2 (reduce): narrative + ranked issues report.

Turns the per-question labels from Stage 1 (llm_insights_classify.py) into the
engineering-management month-over-month deliverable: a plain-English narrative +
a ranked, evidence-linked list of the issues worth engineering attention.

Division of labour (see BUCKET2 key finding — discovered themes are ~all-unique,
so they don't group by string match):
  - Python does ALL the counting (exact per-cluster MoM deltas, severity, value
    signals) — LLMs can't count 1,500 rows reliably.
  - The page is written in PLAIN ENGLISH (the simple-english house style), which
    is now the only style (#83, mirroring #81 for the Project 1 exec summary).
    Both LLM calls are CACHED on disk under LLM_INSIGHTS/cache/, so changing the
    page layout costs nothing; --refresh pays for them again.
  - The LLM does the two things only it can: (1) SEMANTIC CLUSTERING of the free-
    text themes into named engineering issues, and (2) the NARRATIVE + per-issue
    "why / what to look at" prose.
  - Ranking is a transparent Python formula (weights new/emerging + worst-served
    highest, per the project goal); the LLM narrates the ranked result.

Cost is estimated + gated ($50) before each LLM call; actual printed after.

Usage:
  uv run scripts/llm_insights_mom_report.py 2026-08 2026-07 --latest
  uv run scripts/llm_insights_mom_report.py 2026-08 2026-07 --latest --refresh
"""
import sys
import os
import re
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
# Below this many questions in the current month, cluster-level deltas are noise:
# android runs ~40 questions a month across ~60 clusters, so almost every cluster
# holds one or two questions and reads "new this month". The page says so.
LOW_VOLUME = 150


# Both Stage-2 calls are cached on disk, keyed by month pair and product. The
# LLM output does not change when only the PAGE LAYOUT changes, and iterating on
# layout used to cost $0.64 a render. Pass --refresh to pay for them again.
CACHE = "LLM_INSIGHTS/cache/{product}-{cur}-vs-{prev}-{what}.json"
# Facts the corpus cannot know: a shipped fix, a provider's own resolution, a
# duplicate of a Bugzilla bug. One row per fact, matched case-insensitively
# against the cluster label. Hand-maintained, deliberately tiny.
KNOWN_STATUS = "LLM_INSIGHTS/known-status.csv"


def load_known_status(product):
    """Rows for `product` (or `all`). A fix that shipped in the desktop client
    must not annotate an android cluster whose label happens to match."""
    if not os.path.exists(KNOWN_STATUS):
        return []
    df = pd.read_csv(KNOWN_STATUS, dtype=str, keep_default_na=False)
    df = df[df["product"].isin([product, "all"])]
    return [(re.compile(r["pattern"]), r["status"]) for _, r in df.iterrows()]


def status_for(label, known):
    for pattern, text in known:
        if pattern.search(label or ""):
            return text
    return ""


def cached(path, refresh, produce):
    """Return the cached JSON at `path`, or produce it and write it there."""
    if not refresh and os.path.exists(path):
        print(f"   [cache] reusing {path} (no LLM call; --refresh to redo)")
        with open(path) as f:
            return json.load(f)
    value = produce()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(value, f, ensure_ascii=False, indent=1)
    return value


def human_month(m):
    return datetime.strptime(m, "%Y-%m").strftime("%B %Y")


def md_safe(s, limit=80):
    return (s or "").replace("|", "¦").replace('"', "＂")[:limit]


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


# ---- Project 1 cause tags as clustering hints ---------------------------- #
#
# Clustering is not deterministic, and on 2026-09-10 the Spectrum/Charter cluster
# (36 questions, mean severity 4.4) merged into a generic "cannot send or receive"
# cluster and fell out of the top five. Project 1 already knows which mail host /
# protocol / antivirus each question names, so we hand those tags to the model as
# hints AND enforce the split afterwards in Python. Three layers, cheapest last:
#   1. the tags appear on every theme line in the prompt;
#   2. the prompt says to keep host-specific and antivirus-specific clusters apart;
#   3. split_by_cause() splits any cluster that mixes a SPIKING cause tag with
#      other themes, so the separation does not depend on the model at all.
FEATURES = "PROJECT1/{m}-{product}-features.csv"
CAUSE_COLS = ["mail_provider", "av", "protocol"]   # feature is too broad a hint
# Themes are almost all unique (1,633 distinct themes over 1,671 questions), so a
# tag can essentially never cover two questions of the SAME theme. The threshold
# is therefore 1: one tagged question is the whole theme.
HINT_MIN = 1


def cause_tags_by_theme(all_df, months, product):
    """-> {theme: [tag, ...]} from the Project 1 feature tables."""
    frames = []
    for m in months:
        path = FEATURES.format(m=m, product=product)
        if os.path.exists(path):
            frames.append(pd.read_csv(path, dtype=str, keep_default_na=False))
    if not frames:
        return {}
    feats = pd.concat(frames, ignore_index=True)
    tag_by_id = {}
    for _, r in feats.iterrows():
        tags = [t for c in CAUSE_COLS for t in str(r[c]).split(";") if t]
        if tags:
            tag_by_id[r["id"]] = tags
    out = {}
    for theme, g in all_df.groupby("discovered_theme"):
        counts = {}
        for qid in g["id"]:
            for t in tag_by_id.get(qid, []):
                counts[t] = counts.get(t, 0) + 1
        keep = sorted((t for t, n in counts.items() if n >= HINT_MIN),
                      key=lambda t: -counts[t])[:3]
        if keep:
            out[theme] = keep
    return out


def spiking_causes(product, month):
    """Cause values Project 1 flagged as a spike in `month`, at any grain.

    These are the clusters that MUST stay separate: a provider outage that the
    no-AI detector already found should not disappear into a generic bucket on
    the AI page."""
    hits = set()
    for grain in ("daily", "weekly", "monthly"):
        path = f"PROJECT1/{product}-{grain}-single-spikes.csv"
        if not os.path.exists(path):
            continue
        df = pd.read_csv(path, dtype=str, keep_default_na=False)
        if df.empty:
            continue
        rows = df[df["period"].str.startswith(month)
                  & df["dim"].isin(CAUSE_COLS)]
        hits |= set(rows["value"])
    return hits


def split_by_cause(theme_to_label, hints, spiking):
    """Force a cluster apart when it mixes a spiking cause tag with other themes.

    Deterministic: no LLM involved. A theme whose top tag is a spiking cause goes
    into its own "<label> (<tag>)" cluster; everything else keeps the label.

    Applies to BOTH months. Splitting only the current month would leave the
    previous month's questions in the base cluster, so every split cluster would
    read "new this month" and its growth would be measured from zero."""
    if not spiking:
        return theme_to_label, []
    moved = []
    out = dict(theme_to_label)
    for theme, label in theme_to_label.items():
        tag = next((t for t in hints.get(theme, []) if t in spiking), None)
        if not tag:
            continue
        if f"({tag})" in label or tag in label:
            continue
        out[theme] = f"{label} ({tag})"
        moved.append((theme, tag, label))
    return out, moved


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
cluster.

Some lines carry `tags=` — mail-host, antivirus and protocol tags derived \
separately by regex over the question text. KEEP A HOST-SPECIFIC OR \
ANTIVIRUS-SPECIFIC PROBLEM IN ITS OWN CLUSTER: "Spectrum mail stops \
downloading" must NOT merge into a generic "cannot receive mail" cluster, \
because one is a provider incident and the other is a client defect, and they go \
to different people. Name the host or the product in the label when the tag says \
so. Protocol tags are weaker evidence: use them only when the protocol IS the \
problem."""

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


def cluster_themes(client, all_df, usage, hints=None):
    """Return dict theme_string -> cluster_label via one LLM call."""
    # unique themes with count + dominant category
    g = (all_df.groupby("discovered_theme")
         .agg(n=("id", "size"),
              cat=("category", lambda s: s.mode().iat[0] if not s.mode().empty else "other"))
         .reset_index())
    themes = g["discovered_theme"].tolist()
    hints = hints or {}
    lines = []
    for i, r in enumerate(g.itertuples()):
        tg = hints.get(r.discovered_theme)
        tail = f", tags={','.join(tg)}" if tg else ""
        lines.append(f"{i}\t{r.discovered_theme}  (n={r.n}, cat={r.cat}{tail})")
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

# The house style used by the Project 1 pages (simple-english, in the spirit of
# ASD-STE100). Always appended to the system prompt, so the LLM prose matches the
# scaffolding around it. Plain English is the only style as of 2026-09-10 (#83);
# the original format is in git history.
PLAIN_SYS = """

WRITE IN PLAIN ENGLISH. Rules, all of them:
- Short sentences. 25 words at most. One idea per sentence.
- Active voice and simple tenses. Name the actor: "engineering must look at".
- No semicolons, no em dashes, no contractions, no emoji, no bold for emphasis.
- Do not write "should", "may", "might" or "could". Use "can", "will", "must".
- Say the fact, not its importance. Delete "crucial", "significant", "notably", "it is worth noting", "in order to".
- Define a term of art the first time you use it, in a few words.
- A reader outside the Thunderbird team must understand it on one read."""

PLAIN_GLOSSARY = """<details markdown="1">
<summary>Glossary</summary>

| Term | Meaning |
|:--|:--|
| question | One post by a user on the Thunderbird support site. |
| cluster | A group of questions that describe the same concrete problem. Claude reads each question and names the problem, and questions with the same named problem form one cluster. |
| new cluster | A cluster with no questions in the previous month. |
| severity | How much the problem hurts the user, from 1 (cosmetic or a how-to) to 5 (data loss or no mail at all). Claude rates each question. |
| resolved | The question has an accepted solution, or a trusted contributor gave the last answer. |
| unanswered | Nobody except the person who asked has replied. |
| rank | A Python score, not a Claude opinion. It weights new clusters, badly served clusters, severity and volume, in that order. |

</details>
"""

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
    system = [{"type": "text", "text": NARR_SYS + PLAIN_SYS}]

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
    known = load_known_status(product)
    W(f"# Thunderbird {pcap} — LLM Insights (Engineering)")
    W(f"\n## {human_month(cur_m)} against {human_month(prev_m)}\n")

    # ---- TL;DR: the top five, first thing on the page ----------------------
    tldr = list(top.iterrows())[:5]
    if tldr:
        W("## TL;DR: the five issues to look at first {#tldr}\n")
        W(f"| # | Issue | {human_month(prev_m)} | {human_month(cur_m)} | "
          f"Severity | Resolved | Known status |")
        W("|--:|:--|--:|--:|--:|--:|:--|")
        for i, (_, r) in enumerate(tldr, 1):
            low = " (below 50%)" if r["served_pct"] < 50 else ""
            new = ", new this month" if r["is_new"] else ""
            W(f"| [{i}](#issue-{i}) | [{md_safe(r['label'], 130)}](#issue-{i}){new} | "
              f"{r['prev']} | {r['cur']} | {r['mean_sev']} | "
              f"{r['served_pct']}%{low} | {status_for(r['label'], known) or '—'} |")
        W("")
        W("Each number links to the same issue in "
          "[Issues to investigate](#issues-to-investigate) below, which carries "
          "the reason, what to look at, and the example questions.")
        W("")
        if len(cur) < LOW_VOLUME:
            W(f"Read this page as a list of the month's problems, not as a "
              f"trend. {human_month(cur_m)} holds {len(cur)} questions in "
              f"{top.attrs.get('n_clusters', 0)} clusters, so most clusters hold "
              f"one or two questions. A change of one question is noise, and "
              f"\"new this month\" often means only that nobody worded the "
              f"problem that way last month. The severity and the resolved "
              f"figures carry the signal here.")
            W("")

    if True:
        W("Claude read every support question of both months. For each question "
          "it named the concrete problem, guessed a root cause and rated how much "
          "the problem hurts the user. It also read the answers: the follow-ups "
          "from the person who asked, the accepted solution, and the replies from "
          "trusted contributors.")
        W("")
        W("Python did the counting and the ranking. Claude grouped the named "
          "problems and wrote the prose. Read this page as a pointer for triage, "
          "not as proof.")
        W("")
        W(PLAIN_GLOSSARY)


    W("## Headline\n")
    W(f"| | {human_month(prev_m)} | {human_month(cur_m)} | Change |")
    W("|:--|--:|--:|:--|")
    W(f"| Support questions (load) | {len(prev)} | {len(cur)} | {delta(len(prev), len(cur))} |")
    W(f"| Distinct issue clusters | {top.attrs['n_clusters_prev']} | "
      f"{top.attrs['n_clusters']} | {delta(top.attrs['n_clusters_prev'], top.attrs['n_clusters'], pct=False)} |")
    W(f"| New issue clusters this month | — | {int(top['is_new'].sum()) if len(top) else 0} | |")
    W("")
    if narr.get("headline"):
        W(narr["headline"] + "\n")
    if narr.get("narrative_md"):
        W(narr["narrative_md"] + "\n")

    W("## Issues to investigate {#issues-to-investigate}\n")
    W("The order comes from a Python score. It weights new clusters, badly "
      "served clusters, severity and volume, in that order. Resolved means "
      "the question has an accepted solution, or a trusted contributor gave "
      "the last answer. A resolved figure under 50% is marked.\n")
    for i, (_, r) in enumerate(top.iterrows(), 1):
        flag = " (below 50%)" if r["served_pct"] < 50 else ""
        new = ", new this month" if r["is_new"] else ""
        W(f"### {i}. {r['label']}{new} {{#issue-{i}}}\n")
        W(f"| Cluster | {human_month(prev_m)} | {human_month(cur_m)} | Change | "
          f"Sev (≥4) | Resolved | Unanswered |")
        W("|:--|--:|--:|:--|:--|:--|--:|")
        W(f"| {md_safe(r['label'], 130)} ({r['category']}) | {r['prev']} | "
          f"{r['cur']} | "
          f"{delta(r['prev'], r['cur'])} | {r['mean_sev']} ({r['n_sev4']}) | "
          f"{r['served_pct']}%{flag} | {r['unanswered_pct']}% |")
        W("")
        p = issue_prose.get(i)
        st = status_for(r["label"], known)
        if st:
            W(f"- Known status: {st}")
        if p:
            W(f"- Why it matters: {p['why']}")
            W(f"- What to look at: {p['action']}")
        W(f"- Example questions: {links(r['examples'], titles)}")
        W("")

    W("## Category mix, month over month\n")
    W(f"| Category | {human_month(prev_m)} | {human_month(cur_m)} | Change |")
    W("|:--|--:|--:|:--|")
    for c in cat_mom_rows:
        W(f"| {c['category']} | {c['prev']} | {c['cur']} | {delta(c['prev'], c['cur'])} |")
    W("")

    W("---")
    W(f"\nThis is a prototype. Claude {MODEL} wrote the labels for each "
      f"question, and this run of the report cost ${cost:.2f}. The page covers "
      f"{human_month(cur_m)} against {human_month(prev_m)}. Facts the corpus "
      f"cannot know, such as a shipped fix, come from "
      f"`{KNOWN_STATUS}` and appear as Known status.")
    W(f"\nLast updated: {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}")
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
    ap.add_argument("--refresh", action="store_true",
                    help="ignore the cached clustering and narrative for this "
                         "month pair and pay for both LLM calls again")
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

    ckey = dict(product=args.product, cur=args.current, prev=args.previous)
    cluster_path = CACHE.format(what="clusters", **ckey)
    narr_path = CACHE.format(what="narrative", **ckey)

    hints = cause_tags_by_theme(all_df, [args.previous, args.current],
                                args.product)
    spiking = spiking_causes(args.product, args.current)
    print(f"   [hints] {len(hints)} themes carry a Project 1 cause tag; "
          f"{len(spiking)} cause(s) spiking in {args.current}: "
          f"{', '.join(sorted(spiking)) or 'none'}")
    theme_to_label = cached(cluster_path, args.refresh,
                            lambda: cluster_themes(client, all_df, usage, hints))
    theme_to_label, moved = split_by_cause(theme_to_label, hints, spiking)
    if moved:
        print(f"   [split] {len(moved)} theme(s) pulled into a cause-specific "
              f"cluster: " + ", ".join(sorted({t for _, t, _ in moved})))

    # The promise this enforces: a cause Project 1 flagged as spiking has its own
    # cluster on this page. Warn loudly rather than fail — a spike with only one
    # or two questions in the labels legitimately falls under MIN_CLUSTER.
    for tag in sorted(spiking):
        owners = {lb for th, lb in theme_to_label.items()
                  if tag in lb and th in set(cur["discovered_theme"])}
        if not owners:
            print(f"   ⚠️  spiking cause {tag} has no cluster of its own",
                  file=sys.stderr)
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

    narr = cached(narr_path, args.refresh,
                  lambda: narrate(client, args.current, args.previous, featured,
                                  cat_mom, headline_stats, usage))

    cost = actual_cost(usage)
    print(f"\n💵 ACTUAL Stage-2 cost: ${cost:.4f}  "
          f"(in {usage['in']:,} | cache_read {usage['cr']:,} | out {usage['out']:,})")

    rdir = REPORT_DIR.format(product=args.product)
    os.makedirs(rdir, exist_ok=True)
    content = render(args.current, args.previous, cur, prev, featured,
                     cat_mom, narr, titles, cost, args.product)
    paths = [f"{rdir}/monthly-summary-{args.current}-vs-{args.previous}.md"]
    if args.latest:
        paths.append(f"{rdir}/monthly-summary-latest.md")
    for path in paths:
        with open(path, "w") as f:
            f.write(content)
        print(f"   wrote {path}")


if __name__ == "__main__":
    main()
