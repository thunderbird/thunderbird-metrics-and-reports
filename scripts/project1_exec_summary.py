"""Project 1 — one-month EXECUTIVE summary: "was <month> clean?", verdict first.

Audience: Thunderbird engineering (and their management) who want the answer, not
the analysis. The page leads with a single verdict and a detector x grain count
table, then hides ALL of the month's detail behind collapsed <details> blocks.

Distinct from the two existing Project 1 pages:
  - {grain}-spike-report.md  — a trailing window per grain, browsing-oriented.
  - monthly-summary-*.md     — current vs previous month, a "what moved" narrative.
  - THIS                     — one calendar month, clean-or-not, everything else
                               collapsed. Answers "do we need to look at July?"

Run per month (auto-rolls in CI: the most recent COMPLETE month plus the
in-progress one, so July keeps refreshing through August):
  uv run scripts/project1_exec_summary.py 2026-07 desktop --latest
  uv run scripts/project1_exec_summary.py 2026-08 desktop

--latest also writes exec-summary-latest.md, the bookmarkable copy.

WHY REGENERATE A CLOSED MONTH DAILY: the month's verdict is NOT frozen when the
month ends. Lift = observed / (version_volume_in_period x cause_rate_overall), and
BOTH inputs keep moving after the period closes — chiefly the denominator, because
a past week keeps gaining questions as the scraper backfills and versions get
re-derived. Measured on 2026-08-03: the July `v140 x proto:smtp` week of 07-20 read
lift 3.00 in the morning and 1.8 that evening. The cause rate barely moved
(0.0493 -> 0.0480); what changed is that week's own v140 volume, 27 -> 46, which
pushed expected from 1.33 to 2.21. Answered-% and first-answer-time firm up the
same way as late answers land. Rows therefore cross the threshold in EITHER
direction for weeks after a month ends.

STYLE: the page is written in plain English (the simple-english house style,
in the spirit of ASD-STE100). Short sentences, active voice, simple tenses, one
idea per sentence. No emoji, no bold for emphasis, and every term of art defined
in the collapsed glossary at the top. The verdict, the numbers and the links are
unchanged — only the wording is. Keep it that way when editing: a reader outside
the team has to get the answer on one read.

No AI — pure pandas + stdlib. Run AFTER the detectors for all three grains.
"""
import os
import sys
import shutil
import argparse
import tempfile
import subprocess
from datetime import datetime, timezone

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from project1_report import (  # noqa: E402  (shared with the spike reports)
    JOINT_CSV, SINGLE_CSV, QUESTION_URL, CAUSE_DIMS, TREND_DIMS,
    spark, md_safe, load_features,
)
from project1_grains import GRAIN_DEFAULTS  # noqa: E402

REPORT_DIR = "PROJECT1/REPORTS/{product}"
# Every term of art the page uses, defined once, collapsed. A table rather than a
# bold-led list: the house style keeps bold out of the prose, and a Term/Meaning
# table reads the same in the browser and in the raw markdown.
# Plain-English name for a cause tag, so the summary reads "Spectrum" rather than
# "m:spectrum". The tag itself is always printed next to it, so an entry missing
# here degrades to a capitalised tag, never to a wrong name.
CAUSE_NAMES = {
    "m:microsoftemail": "Microsoft mail", "m:yahooemail": "Yahoo Mail",
    "m:gmail": "Gmail", "m:icloud": "iCloud", "m:gmx": "GMX", "m:aol": "AOL",
    "m:att": "AT&T", "m:sbcglobal": "SBCGlobal", "m:bellsouth": "BellSouth",
    "m:btinternet": "BT Internet", "m:earthlink": "EarthLink",
    "m:optonline": "Optimum Online", "m:virginmedia": "Virgin Media",
    "m:talktalk": "TalkTalk", "m:mailcom": "Mail.com", "m:web_de": "Web.de",
    "m:t_online": "T-Online", "m:free_fr": "Free.fr",
    "m:mailbox_org": "Mailbox.org", "m:1and1": "1&1",
    "proto:oauth": "OAuth", "proto:caldav": "CalDAV", "proto:carddav": "CardDAV",
    "feat:import_export": "Import and export", "feat:addressbook": "Address book",
    "feat:spellcheck": "Spell check", "feat:junk": "Junk mail",
    "feat:addons": "Add-ons",
}
CAUSE_PREFIX_STYLE = {"proto": str.upper, "av": str.capitalize,
                      "m": str.capitalize, "feat": str.capitalize}


def cause_name(tag):
    """`m:spectrum` -> 'Spectrum', `proto:pop` -> 'POP'."""
    if tag in CAUSE_NAMES:
        return CAUSE_NAMES[tag]
    prefix, _, rest = tag.partition(":")
    rest = rest.replace("_", " ")
    return CAUSE_PREFIX_STYLE.get(prefix, str.capitalize)(rest) if rest else tag


GLOSSARY = """<details markdown="1">
<summary>Glossary</summary>

| Term | Meaning |
|:--|:--|
| question | One post by a user on the Thunderbird support site. |
| cause tag | What a question is about. `m:spectrum` is the mail host Spectrum. `proto:pop` is the mail protocol POP. `av:avast` is the antivirus product Avast. `feat:printing` is the printing feature of Thunderbird. |
| spike | A period with many more questions of one kind than normal. |
| baseline | The normal count for that kind of question. The tool takes the middle value of earlier periods. |
| rise | The measured count divided by the baseline. A rise of 3.0× means three times as many questions as normal. |
| lift | The same idea for one version and one cause together. The tool divides the count by the count it expects from the number of questions about that version and the normal rate of that cause. A lift above 1 means the cause hits that version harder than the rest. |
| grain | The length of the period that the tool measured: one day, one week, or one month. |
| served | How many of the questions got an answer from somebody other than the person who asked, and the time to the first answer. Below 60% is marked. |
| novelty | Whether the tool saw the pair before. `new` is the first time. `spreading` is a known cause on a new version. `recurring` is a pair that fires again. |
| version×cause spike | A rise tied to one Thunderbird version and one cause. It points to a problem that a Thunderbird release caused. |
| cause-level spike | A rise that ignores the version. It points to a problem at a mail host, in a protocol, in an antivirus product, or in one Thunderbird feature. |
| release-adoption spike | A rise in the bare count of one version or one operating system. Users move to a new release, so the count rises. This is not an incident. |

</details>
"""
DETECTOR_GRAINS = ["daily", "weekly", "monthly"]
# A weekly period is keyed by its Monday, so a week can straddle two months. For a
# "did anything happen in <month>" verdict we take any week that OVERLAPS the
# month — missing an incident because its week began on the 29th of the previous
# month would be the worse error.
WEEK_LEN_DAYS = 7


def month_bounds(month):
    """(first instant, LAST instant) of the month, tz-naive UTC.

    Deliberately not `start + MonthEnd(1)`: that returns the last DAY at 00:00:00,
    so an inclusive `<= end` silently drops everything created during the final day
    of the month (32 of July 2026's 731 questions, when this was first written)."""
    start = pd.Timestamp(month + "-01")
    return start, start + pd.offsets.MonthBegin(1) - pd.Timedelta(nanoseconds=1)


def in_month(periods, month, grain):
    """Boolean mask: which detector period labels fall in `month`."""
    if periods.empty:
        return periods.astype(bool)
    if grain == "monthly":
        return periods.astype(str) == month
    start, end = month_bounds(month)
    dt = pd.to_datetime(periods, errors="coerce")
    if grain == "weekly":  # overlap, not containment
        return (dt <= end) & (dt + pd.Timedelta(days=WEEK_LEN_DAYS - 1) >= start)
    return (dt >= start) & (dt <= end)


def load_spikes(product, month, from_dir=None):
    """-> {(kind, grain): DataFrame of that grain's spikes inside `month`}.

    from_dir reads the same filenames out of a side directory (the relaxed-
    threshold run used for near-misses) instead of the committed PROJECT1/ ones."""
    out = {}
    for grain in DETECTOR_GRAINS:
        for kind, tmpl in (("joint", JOINT_CSV), ("single", SINGLE_CSV)):
            path = tmpl.format(product=product, dgrain=grain)
            if from_dir:
                path = os.path.join(from_dir, os.path.basename(path))
            df = (pd.read_csv(path, dtype=str, keep_default_na=False)
                  if os.path.exists(path) else pd.DataFrame())
            if not df.empty:
                df = df[in_month(df["period"], month, grain)]
            out[(kind, grain)] = df
    return out


# A near-miss is defined operationally: a cluster the SAME detector flags once its
# thresholds are scaled by `factor`, but that does not clear the real ones. Running
# the detectors twice (rather than reimplementing lift/baseline here) keeps exactly
# one source of truth for the detection maths.
#
# Only the MAGNITUDE bar (lift / baseline-multiple) is relaxed — the min_count
# floor is kept at its real value. Relaxing both floods the block with tiny
# clusters carrying huge ratios (July 2026: 18 rows, topped by "10.4x" on three
# questions), which is precisely the noise min_count exists to suppress. The
# interesting near-miss is "big enough to matter, but not over-represented enough
# to fire", not "three questions that happen to share a tag".
JOINT_KEY = ["period", "version_major", "cause_dim", "cause_value"]
SINGLE_KEY = ["period", "dim", "value"]


def run_relaxed_detectors(product, factor, workdir):
    """Re-run both detectors at `factor` x thresholds into workdir. -> ok?"""
    here = os.path.dirname(os.path.abspath(__file__))
    for grain in DETECTOR_GRAINS:
        d = GRAIN_DEFAULTS[grain]
        jobs = [  # min_count stays REAL; only the magnitude bar moves
            ("project1_spike_detect.py", SINGLE_CSV,
             ["--min-count", str(d["single_min_count"]),
              "--mult", str(round(d["single_mult"] * factor, 3))]),
            ("project1_joint_spike_detect.py", JOINT_CSV,
             ["--min-count", str(d["joint_min_count"]),
              "--lift", str(round(d["joint_lift"] * factor, 3))]),
        ]
        for script, tmpl, thresholds in jobs:
            out = os.path.join(workdir, os.path.basename(
                tmpl.format(product=product, dgrain=grain)))
            r = subprocess.run(
                [sys.executable, os.path.join(here, script), product,
                 "--grain", grain, "--out", out] + thresholds,
                capture_output=True, text=True)
            if r.returncode:
                print(f"  near-miss: {script} --grain {grain} failed, skipping "
                      f"({r.stderr.strip().splitlines()[-1:]})", file=sys.stderr)
                return False
    return True


def near_misses(product, month, factor):
    """-> (joint_df, single_cause_df) of clusters that ALMOST fired, or (None,None)
    if the relaxed run could not be done."""
    workdir = tempfile.mkdtemp(prefix="p1-nearmiss-")
    try:
        if not run_relaxed_detectors(product, factor, workdir):
            return None, None
        real = load_spikes(product, month)
        relaxed = load_spikes(product, month, from_dir=workdir)

        def only_relaxed(kind, key):
            frames = []
            for grain in DETECTOR_GRAINS:
                r, x = real[(kind, grain)], relaxed[(kind, grain)]
                if x.empty:
                    continue
                fired = set(map(tuple, r[key].values)) if not r.empty else set()
                extra = x[[tuple(v) not in fired for v in x[key].values]]
                if not extra.empty:
                    frames.append(extra.assign(_g=grain))
            return pd.concat(frames) if frames else pd.DataFrame()

        joint = only_relaxed("joint", JOINT_KEY)
        single = only_relaxed("single", SINGLE_KEY)
        if not single.empty:  # causes only — version/OS near-misses are adoption
            single = single[single["dim"].isin(CAUSE_DIMS)]
        return joint, single
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("month", help="YYYY-MM")
    ap.add_argument("product", choices=["desktop", "android"])
    ap.add_argument("--latest", action="store_true",
                    help="also write exec-summary-latest.md (the bookmarkable copy)")
    ap.add_argument("--near-miss-factor", type=float, default=0.75,
                    help="threshold multiplier for the near-miss block: clusters "
                         "the same detectors flag at this fraction of the real "
                         "thresholds but not at the real ones (default 0.75; "
                         "0 disables the block)")
    args = ap.parse_args()
    product, month = args.product, args.month
    start, end = month_bounds(month)

    df, _ = load_features(product)
    all_titles = dict(zip(df["id"], df["title"]))
    naive = df["created_dt"].dt.tz_convert(None)
    df = df[(naive >= start) & (naive <= end)].copy()
    if df.empty:
        sys.exit(f"no {product} questions in {month} — nothing to summarise")
    df["day"] = df["created_dt"].dt.tz_convert(None).dt.normalize()

    spikes = load_spikes(product, month)
    # Cause-level = the single-dim detector restricted to CAUSE dims. The
    # tb_version_major / os rows are release-adoption noise by design and are
    # reported separately, never as an incident.
    cause = {g: (s[s["dim"].isin(CAUSE_DIMS)] if not s.empty else s)
             for g, s in ((g, spikes[("single", g)]) for g in DETECTOR_GRAINS)}
    verdim = {g: (s[~s["dim"].isin(CAUSE_DIMS)] if not s.empty else s)
              for g, s in ((g, spikes[("single", g)]) for g in DETECTOR_GRAINS)}
    joint = {g: spikes[("joint", g)] for g in DETECTOR_GRAINS}

    n_joint = sum(len(v) for v in joint.values())
    n_cause = sum(len(v) for v in cause.values())
    incidents = n_joint + n_cause

    n = len(df)
    answered = (df["is_answered"] == "true").sum()
    fat = pd.to_numeric(df["first_answer_hours"], errors="coerce").dropna()
    tagged = df[CAUSE_DIMS].apply(lambda r: any(r), axis=1).sum()
    days = pd.date_range(start, min(end, df["day"].max()), freq="D")
    # Titles come from ALL history, not just this month: a weekly period can
    # straddle the month end, so its example questions are often next month's and
    # used to render with an empty tooltip.
    title_by_id = all_titles

    def links_for(ids, limit=6, more=True):
        ids = [i for i in ids if i]
        s = " ".join(f'[{i}]({QUESTION_URL.format(id=i)} "{md_safe(title_by_id.get(i, ""))}")'
                     for i in ids[:limit])
        return s + (f" +{len(ids) - limit}" if more and len(ids) > limit else "")

    def qs_cell(count, ids):
        """Count plus the first two questions as direct links.

        ONLY for tables that have no 'Example questions' column — currently just
        the release-adoption dump, whose rows would otherwise be unclickable
        despite being labelled "for manual checking". Everywhere else the Qs column
        stays a bare count, because duplicating two of the six links already in
        'Example questions' just widens the table."""
        return f"{count} {links_for(str(ids).split(), limit=2, more=False)}".strip()

    def served(r):
        ap_ = str(r.get("answered_pct", "")).strip()
        if not ap_:
            return ""
        ap_ = int(float(ap_))
        md = str(r.get("median_first_answer_h", "")).strip()
        low = " (below 60%)" if ap_ < 60 else ""
        return f"{ap_}% answered{low}{f', {md}h' if md else ''}"

    out, W = [], None
    W = out.append
    label = start.strftime("%B %Y")
    # month_bounds is tz-naive UTC, like created_dt after tz_convert(None)
    partial = end > pd.Timestamp.now(tz="UTC").tz_localize(None).normalize()

    anchor = f"all-{label.lower().replace(' ', '-')}-detail"

    W("---")
    W("layout: base")  # minima 3.x renamed 'default' -> 'base' (#72)
    W(f"title: \"{month} exec summary: Thunderbird {product.title()} support spikes\"")
    W("---")
    W("")
    W(f"# {label}: Thunderbird {product.title()} support spikes")
    W("")
    W(f"Executive summary for {month}. It covers {n} Thunderbird "
      f"{product.title()} support questions. The tool wrote this page on "
      f"{datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}. No AI read the "
      f"questions. The tool uses regular expressions and standard statistics "
      f"only.")
    W("")
    W(GLOSSARY)

    # ---- the verdict ------------------------------------------------------
    if incidents == 0:
        W(f"## {label} was clean")
        W("")
        W("No spike cleared the threshold at any grain. The tool found no mail "
          "host outage, no protocol surge, no antivirus breakage and no release "
          f"regression in {label}.")
        W("")
    else:
        W(f"## {label}: {incidents} spike"
          f"{'s' if incidents != 1 else ''} to investigate")
        W("")
        if n_joint and n_cause:
            split = (f"{n_joint} of them tie to a Thunderbird version. "
                     f"{n_cause} of them are cause-level.")
        elif n_joint:
            split = (f"All {n_joint} tie to a Thunderbird version. None of them "
                     f"are cause-level.")
        else:
            split = (f"None of them tie to a Thunderbird version. All "
                     f"{n_cause} are cause-level.")
        W(f"{split} Every row is in the collapsed blocks below.")
        W("")
    if partial:
        W(f"{label} is still in progress. The counts will grow.")
        W("")
    # The one-line summary is written further down, once the clusters are ranked,
    # but it belongs HERE, directly under the verdict. Remember the slot.
    in_short_at = len(out)

    W("| Detector | daily | weekly | monthly |")
    W("|:--|--:|--:|--:|")
    W("| version×cause (a release caused the problem) | "
      + " | ".join(str(len(joint[g])) for g in DETECTOR_GRAINS) + " |")
    W("| cause-level (mail host, protocol, antivirus, feature) | "
      + " | ".join(str(len(cause[g])) for g in DETECTOR_GRAINS) + " |")
    W("")

    # A zero in the version×cause row means one of two very different things.
    # Before 2026-02 the scraper has almost no version, so the detector CANNOT
    # fire, and reading that as "no release regression" is the worse error.
    known_version = df["tb_version_major"].str.fullmatch(r"\d+").fillna(False).mean()
    if known_version < 0.2:
        lead = (f"Almost no {label} question carries a Thunderbird version."
                if known_version < 0.02 else
                f"Only {100*known_version:.0f}% of the {label} questions carry a "
                f"Thunderbird version.")
        W(f"{lead} The version×cause detector therefore cannot fire. Read its "
          f"zero as missing data, not as a clean result.")
        W("")

    nv = sum(len(v) for v in verdim.values())
    first_day, last_day = days[0], days[-1]
    W("Three more numbers for context:")
    W("")
    W(f"- Volume: {n} questions. {tagged} of them ({100*tagged/n:.0f}%) carry a "
      f"cause tag. The count per day was "
      f"`{spark([int((df['day'] == d).sum()) for d in days])}`, one block per day "
      f"from {first_day:%B} {first_day.day} to {last_day:%B} {last_day.day}.")
    W(f"- Answers: {answered} of the {n} questions ({100*answered/n:.0f}%) got an "
      f"answer from somebody other than the person who asked."
      + (f" The middle time to the first answer was {fat.median():.1f} hours."
         if len(fat) else ""))
    W(f"- Release-adoption version spikes: {nv}. Users move to a new release, so "
      f"the bare counts rise. These are not incidents.")
    W("")
    W(f"Every spike row, with its example questions, is in "
      f"[All {label} detail](#{anchor}) below.")
    W("")

    def details(summary, body_fn, count):
        """One collapsed block. kramdown needs markdown="1" to parse markdown
        inside a block-level HTML element."""
        W(f'<details markdown="1">')
        W(f"<summary>{summary}, {count} row"
          f"{'s' if count != 1 else ''}</summary>")
        W("")
        body_fn()
        W("")
        W("</details>")
        W("")

    def joint_body():
        rows = pd.concat([j.assign(_g=g) for g, j in joint.items() if not j.empty]) \
            if any(len(j) for j in joint.values()) else pd.DataFrame()
        if rows.empty:
            W("None.")
            return
        rows = rows.assign(_l=pd.to_numeric(rows["lift"], errors="coerce")) \
                   .sort_values("_l", ascending=False)
        W("| Grain | Lift | When | Version × Cause | Questions | Served | Novelty | Example questions |")
        W("|:--|--:|:--|:--|--:|:--|:--|:--|")
        for _, r in rows.iterrows():
            W(f"| {r['_g']} | {r['lift']}× | {r['period']} | "
              f"v{r['version_major']} × {r['cause_value']} | {r['observed']} | "
              f"{served(r)} | {r.get('novelty','')} | "
              f"{links_for(str(r['question_ids']).split())} |")

    def cause_body():
        rows = pd.concat([c.assign(_g=g) for g, c in cause.items() if not c.empty]) \
            if any(len(c) for c in cause.values()) else pd.DataFrame()
        if rows.empty:
            W("None.")
            return
        rows = rows.assign(_m=pd.to_numeric(rows["magnitude"].replace("new", 1e9),
                                            errors="coerce")) \
                   .sort_values(["_m", "count"], ascending=False)
        W("| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |")
        W("|:--|--:|:--|:--|--:|:--|--:|:--|")
        for _, r in rows.iterrows():
            mag = "new" if r["magnitude"] == "new" else f"{float(r['magnitude']):.1f}×"
            W(f"| {r['_g']} | {mag} | {r['period']} | {r['value']} | "
              f"{r['count']} | {served(r)} | {r['baseline_median']} | "
              f"{links_for(str(r['question_ids']).split())} |")

    def verdim_body():
        rows = pd.concat([v.assign(_g=g) for g, v in verdim.items() if not v.empty]) \
            if any(len(v) for v in verdim.values()) else pd.DataFrame()
        if rows.empty:
            W("None.")
            return
        W("Version and operating system are filters, not causes. A rise in the "
          "bare count of one version is release adoption, not a regression. The "
          "rows are here for manual checking only.\n")
        W("| Grain | Rise | When | Dimension | Value | Questions | Baseline |")
        W("|:--|--:|:--|:--|:--|:--|--:|")  # the count cell holds links -> left
        for _, r in rows.sort_values(["_g", "period"]).iterrows():
            mag = "new" if r["magnitude"] == "new" else f"{float(r['magnitude']):.1f}×"
            W(f"| {r['_g']} | {mag} | {r['period']} | {r['dim']} | "
              f"{r['value']} | {qs_cell(r['count'], r['question_ids'])} | "
              f"{r['baseline_median']} |")

    def trends_body():
        for dim, heading in [
                ("tb_version_major", "The Thunderbird versions named most often were:"),
                ("mail_provider", "The mail hosts named most often were:"),
                ("feature", "The Thunderbird features named most often were:"),
                ("protocol", "The protocols named most often were:"),
                ("av", "The antivirus products named most often were:"),
                ("os", "The operating systems named most often were:"),
                ("macos_release", "The macOS releases named most often were:")]:
            exploded = (df[dim].str.split(";").explode().dropna())
            exploded = exploded[exploded != ""]
            if exploded.empty:
                continue
            W(heading)
            W("")
            W("| Value | Questions | Count per day |")
            W("|:--|--:|:--|")
            for value, cnt in exploded.value_counts().head(6).items():
                mask = df[dim].apply(lambda c: value in (c.split(";") if c else []))
                by_day = [int(((df["day"] == d) & mask).sum()) for d in days]
                disp = f"v{value}" if dim == "tb_version_major" else value
                W(f"| {disp} | {cnt} | `{spark(by_day)}` |")
            W("")

    # ---- what stands out ---------------------------------------------------
    # Mechanical, never interpretive: the pair that fired most often, the cause
    # that fired most often, and the clusters that were served badly. A reader
    # gets the shape of the month without opening a 17-row table.
    def _concat(d):
        frames = [x.assign(_g=g) for g, x in d.items() if not x.empty]
        return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()

    def when(grain, period):
        """A period label read out loud. A weekly period is keyed by its Monday,
        so the bare date would read as a single day."""
        if grain == "weekly":
            return f"in the week of {period}"
        return f"on {period}" if grain == "daily" else f"in {period}"

    short_month = start.strftime("%B")
    jall, sall = _concat(joint), _concat(cause)
    if incidents:
        # One paragraph per distinct CAUSE, ranked by its strongest rise, so a
        # cluster that fires at several grains (or on several versions) is one
        # story and not eight table rows. Five at most: in a busy month the
        # sixth onward stop being a summary.
        MAX_CLUSTERS = 5
        if not jall.empty:
            jall["_r"] = pd.to_numeric(jall["lift"], errors="coerce")
            jall["_cause"] = jall["cause_value"].astype(str)
        if not sall.empty:
            sall["_r"] = pd.to_numeric(sall["magnitude"].replace("new", 1e9),
                                       errors="coerce")
            sall["_cause"] = sall["value"].astype(str)

        def strongest(tag):
            """Biggest rise for `tag`, joint or cause-level. A cause that fires
            in only one of the two detectors gives NaN for the other, and
            max([nan, 3.5]) is nan, which used to scramble the ranking."""
            vals = []
            for frame in (jall, sall):
                if frame.empty:
                    continue
                v = frame.loc[frame["_cause"] == tag, "_r"].max()
                if pd.notna(v):
                    vals.append(float(v))
            return max(vals) if vals else 0.0

        tags = sorted(
            set(jall["_cause"] if not jall.empty else [])
            | set(sall["_cause"] if not sall.empty else []),
            key=lambda t: (-strongest(t), t))

        def peak_sentence(tag):
            """The single hardest period for `tag`, joint or cause-level.

            -> (sentence, used_the_monthly_cause_row). The flag stops the month
            sentence from repeating a peak that IS the monthly row."""
            jr = jall[jall["_cause"] == tag] if not jall.empty else pd.DataFrame()
            sr = sall[sall["_cause"] == tag] if not sall.empty else pd.DataFrame()
            jbest = jr.loc[jr["_r"].idxmax()] if not jr.empty else None
            sbest = sr.loc[sr["_r"].idxmax()] if not sr.empty else None
            use_joint = sbest is None or (
                jbest is not None and jbest["_r"] >= sbest["_r"])
            r = jbest if use_joint else sbest
            wh = when(r["_g"], r["period"])
            if use_joint:
                return (f"It peaked {wh} at {r['lift']} times expected, on "
                        f"Thunderbird {r['version_major']}."), False
            monthly_peak = r["_g"] == "monthly"
            if r["magnitude"] == "new":
                return (f"It peaked {wh} with {r['count']} questions, where "
                        f"earlier periods had none."), monthly_peak
            return (f"It peaked {wh} at {float(r['magnitude']):.1f} times its "
                    f"baseline."), monthly_peak

        def month_sentence(tag):
            """The monthly cause-level row if there is one, else the raw count."""
            monthly = cause["monthly"]
            row = monthly[monthly["value"] == tag] if not monthly.empty \
                else pd.DataFrame()
            if not row.empty:
                r = row.iloc[0]
                if r["magnitude"] == "new":
                    return (f"{r['count']} questions in {short_month}, where "
                            f"earlier months had none.")
                return (f"{r['count']} questions in {short_month}, "
                        f"{float(r['magnitude']):.1f} times the baseline of "
                        f"{r['baseline_median']}.")
            dim = next((d for d in CAUSE_DIMS
                        if df[d].str.contains(tag, regex=False).any()), None)
            if dim is None:
                return ""
            hits = df[dim].apply(lambda c: tag in (c.split(";") if c else "")).sum()
            return (f"{hits} question{'s' if hits != 1 else ''} in "
                    f"{short_month}, under the monthly bar.")

        # The explorer page is committed per product (desktop today); link to it
        # only when it is there, so an android page never emits a dead link. The
        # deep link uses the MONTHLY grain, which is the cluster's own scale.
        explorer_exists = os.path.exists(
            f"{REPORT_DIR.format(product=product)}/explorer.html")

        def cluster_link(tag):
            if not explorer_exists:
                return f"`{tag}`"
            return (f"[`{tag}`](explorer.html#grain=monthly&cause={tag}"
                    f"&period={month})")

        shown = tags[:MAX_CLUSTERS]
        lead = " and ".join(cause_name(t) for t in shown[:2])
        rest_n = len(tags) - len(shown[:2])
        in_short = f"In short: {lead}." + (
            f" Both are in the list below, with {rest_n} smaller cluster"
            f"{'s' if rest_n != 1 else ''}." if len(shown[:2]) == 2 and rest_n
            else (f" The list below has {rest_n} smaller cluster"
                  f"{'s' if rest_n != 1 else ''} as well." if rest_n
                  else " The list below has the detail."))
        out.insert(in_short_at, "")
        out.insert(in_short_at, in_short)

        W("## What stands out")
        W("")
        for i_, tag in enumerate(shown, start=1):
            nj = int((jall["_cause"] == tag).sum()) if not jall.empty else 0
            ns = int((sall["_cause"] == tag).sum()) if not sall.empty else 0
            k = nj + ns
            peak, is_monthly_peak = peak_sentence(tag)
            W(f"{i_}. {cause_name(tag)} ({cluster_link(tag)}, {k} spike"
              f"{'s' if k != 1 else ''}): {month_sentence(tag)}"
              + ("" if is_monthly_peak else " " + peak))
        W("")
        if len(tags) > MAX_CLUSTERS:
            rest = ", ".join(cluster_link(t) for t in tags[MAX_CLUSTERS:])
            k = len(tags) - MAX_CLUSTERS
            W(f"{k} more cluster{'s' if k != 1 else ''} fired: {rest}. "
              f"{'They are' if k != 1 else 'It is'} in the detail below.")
            W("")

        bad = []
        for frame, name in ((jall, lambda r: f"`v{r['version_major']} × {r['cause_value']}`"),
                            (sall, lambda r: f"`{r['value']}`")):
            if frame.empty:
                continue
            pct = pd.to_numeric(frame["answered_pct"], errors="coerce")
            for _, r in frame[pct < 60].iterrows():
                bad.append(f"{name(r)} {when(r['_g'], r['period'])} "
                           f"({int(float(r['answered_pct']))}% answered)")
        if bad:
            more = f", and {len(bad) - 4} more" if len(bad) > 4 else ""
            W(f"In {len(bad)} cluster{'s' if len(bad) != 1 else ''}, fewer than "
              f"60% of the questions got an answer: "
              + ", ".join(bad[:4]) + more + ".")
            W("")

    # ---- what the dates do and do not mean ---------------------------------
    W("## Two limits of these dates")
    W("")
    W("Read the date of a spike as the day users came to the support site, not "
      "as the day the problem started. Users retry and wait before they post, so "
      "a spike usually dates days after the start of a problem, often close to "
      "the fix. Use this page to find clusters of pain, not to detect a live "
      "incident.")
    W("")
    W("A closed month can also change its verdict later. The tool measures each "
      "rise against the rate of that cause across all history. Questions that "
      "arrive later therefore move the expected count for a past month. Rows can "
      "cross the threshold in both directions, and the answered percentage rises "
      "as late answers land. This page regenerates every day, and each day's "
      "version is committed, so `git log -p` on this file shows how the verdict "
      "moved.")
    W("")

    # ---- near misses, right after the verdict ------------------------------
    # Deliberately BEFORE the detail section: "nothing fired" and "three clusters
    # sat just under the line" are different answers to the executive question,
    # and the verdict table alone cannot tell them apart.
    if args.near_miss_factor > 0:
        nm_j, nm_s = near_misses(product, month, args.near_miss_factor)
        pct = round((1 - args.near_miss_factor) * 100)

        def nearmiss_body():
            if nm_j is None:
                W("The relaxed detector pass failed on this run, so this block "
                  "is empty. The verdict above is not affected.")
                return
            W(f"The tool runs the same detectors a second time at "
              f"{args.near_miss_factor:g} times the thresholds. The rows below "
              f"came out of that second run and did not clear the real "
              f"thresholds. They are not incidents. They are context, so that a "
              f"quiet month is not read as a clean month.\n")
            if not nm_j.empty:
                W("Version and cause together:")
                W("")
                W("| Grain | Lift | When | Version × Cause | Questions | Served | Example questions |")
                W("|:--|--:|:--|:--|--:|:--|:--|")
                for _, r in nm_j.assign(
                        _l=pd.to_numeric(nm_j["lift"], errors="coerce")
                ).sort_values("_l", ascending=False).iterrows():
                    W(f"| {r['_g']} | {r['lift']}× | {r['period']} | "
                      f"v{r['version_major']} × {r['cause_value']} | "
                      f"{r['observed']} | {served(r)} | "
                      f"{links_for(str(r['question_ids']).split())} |")
                W("")
            if not nm_s.empty:
                W("Cause alone:")
                W("")
                W("| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |")
                W("|:--|--:|:--|:--|--:|:--|--:|:--|")
                for _, r in nm_s.assign(
                        _m=pd.to_numeric(nm_s["magnitude"].replace("new", 1e9),
                                         errors="coerce")
                ).sort_values("_m", ascending=False).iterrows():
                    mag = "new" if r["magnitude"] == "new" else f"{float(r['magnitude']):.1f}×"
                    W(f"| {r['_g']} | {mag} | {r['period']} | {r['value']} | "
                      f"{r['count']} | {served(r)} | {r['baseline_median']} | "
                      f"{links_for(str(r['question_ids']).split())} |")
                W("")
            if nm_j.empty and nm_s.empty:
                W(f"None. Nothing came within about {pct}% of the threshold "
                  f"either.")

        n_nm = 0 if nm_j is None else len(nm_j) + len(nm_s)
        details(f"Near misses (within about {pct}% of the threshold)",
                nearmiss_body, n_nm)

    # ---- collapsed detail --------------------------------------------------
    W("---\n")
    # explicit id: the context paragraph links here, and an auto-id would change
    # with the heading text
    W(f"## All {label} detail {{#{anchor}}}\n")

    details("Version × cause spikes", joint_body, n_joint)
    details("Cause-level spikes (mail host, protocol, antivirus, feature)",
            cause_body, n_cause)
    details("Release-adoption version and operating-system spikes (not incidents)",
            verdim_body, nv)
    details(f"{label} trends", trends_body, len(TREND_DIMS))

    W("---")
    W(f"\nThe tool ran its detectors at daily, weekly and monthly grain. A "
      f"weekly period counts toward {label} when its week overlaps the month. "
      f"Version×cause needs a known Thunderbird version, which the data carries "
      f"only from 2026-02 onward. Cause-level uses all history. The full spike "
      f"tables are in "
      f"`PROJECT1/{product}-{{daily,weekly,monthly}}-{{single,version-cause}}-spikes.csv`.")

    os.makedirs(REPORT_DIR.format(product=product), exist_ok=True)
    body = "\n".join(out) + "\n"
    paths = [f"{REPORT_DIR.format(product=product)}/{month}-exec-summary.md"]
    if args.latest:
        paths.append(f"{REPORT_DIR.format(product=product)}/exec-summary-latest.md")
    for p in paths:
        with open(p, "w") as f:
            f.write(body)
        print(f"wrote {p}")
    print(f"=== {month} {product}: {incidents} incident spike(s) "
          f"({n_joint} version×cause, {n_cause} cause-level), "
          f"{nv} release-adoption, {n} questions ===")


if __name__ == "__main__":
    main()
