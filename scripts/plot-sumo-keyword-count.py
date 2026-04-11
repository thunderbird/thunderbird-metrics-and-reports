#!/usr/bin/env python3
"""
Count regex matches in SUMO concatenated question and answer files and plot counts.

Usage:
  - Eight args mode:
      plot-sumo-keyword-count.py <product> YYYY1 MM1 DD1 YYYY2 MM2 DD2 <regex>
    where <product> is 'desktop' or 'android', date-range1 starts at YYYY1-MM1-DD1 and
    ends at YYYY2-MM2-DD2 (inclusive). Let n be number of days in date-range1. Date-range2
    is the same period starting n days earlier. <regex> is a Python regular expression.

  - One arg mode:
      plot-sumo-keyword-count.py <regex>
    where date-range1 is the current calendar month and date-range2 is the previous
    calendar month, adjusted to match the length of the current month (by adding or
    removing days from the start of the previous month). product defaults to 'desktop'.

Outputs:
  - REPORTS/<product>/<start1>-<end1>-<regex_filename>.csv  (date,num-<regex>-matches)
  - REPORTS/<product>/<start1>-<end1>-<regex_filename>.md  (markdown table with linked question IDs)
  - REPORTS/<product>/<start1>-<end1>-<regex_filename>.png  (line plot comparing the two ranges)
  - REPORTS/<product>/<start1>-<end1>-<regex_filename>_bar.png  (bar graph comparing the two ranges)
  - REPORTS/<product>/<start1>-<end1>-<regex_filename>_overall.png  (overall bar chart with 2 bars: totals for each range)

All dates/times are handled in UTC.
"""

import sys
import re
import csv
from pathlib import Path
from datetime import datetime, timedelta, timezone, date
import os

try:
    import pandas as pd
except Exception:
    pd = None

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
except Exception:
    plt = None


def parse_args(argv):
    if len(argv) == 8:
        product = argv[0]
        y1, m1, d1, y2, m2, d2 = map(int, argv[1:7])
        regex = argv[7]
        start1 = date(y1, m1, d1)
        end1 = date(y2, m2, d2)
    elif len(argv) == 1:
        regex = argv[0]
        product = 'desktop'
        today = datetime.utcnow().date()
        start1 = today.replace(day=1)
        # end1 is last day of current month
        if start1.month == 12:
            end1 = date(start1.year, 12, 31)
        else:
            end1 = (start1.replace(month=start1.month+1) - timedelta(days=1))
    else:
        print("Usage:\n  plot-sumo-keyword-count.py <product> YYYY1 MM1 DD1 YYYY2 MM2 DD2 <regex>\n  or\n  plot-sumo-keyword-count.py <regex>")
        sys.exit(2)

    if start1 > end1:
        raise ValueError("start date must be <= end date")

    # compute n days
    n_days = (end1 - start1).days + 1
    # date-range-2 is same period starting n_days earlier by default
    start2 = start1 - timedelta(days=n_days)
    end2 = end1 - timedelta(days=n_days)

    # If script was invoked in single-arg mode, set date-range-2 to the previous calendar month
    if len(argv) == 1:
        # previous month first day
        if start1.month == 1:
            start2 = date(start1.year - 1, 12, 1)
        else:
            start2 = date(start1.year, start1.month - 1, 1)
        # previous month last day
        if start2.month == 12:
            end2 = date(start2.year, 12, 31)
        else:
            end2 = (start2.replace(month=start2.month + 1) - timedelta(days=1))

        # Adjust date-range-2 to match the length of date-range-1
        n_days_1 = (end1 - start1).days + 1
        n_days_2 = (end2 - start2).days + 1
        if n_days_1 > n_days_2:
            # Current month has more days: add extra days to start of previous month
            start2 = start2 - timedelta(days=(n_days_1 - n_days_2))
        elif n_days_1 < n_days_2:
            # Current month has fewer days: move start of previous month forward
            start2 = start2 + timedelta(days=(n_days_2 - n_days_1))

    return product, start1, end1, start2, end2, regex


def months_between(sdate, edate):
    # yield (year, month) tuples covering inclusive month range
    cur = date(sdate.year, sdate.month, 1)
    last = date(edate.year, edate.month, 1)
    months = []
    while cur <= last:
        months.append((cur.year, cur.month))
        if cur.month == 12:
            cur = date(cur.year+1, 1, 1)
        else:
            cur = date(cur.year, cur.month+1, 1)
    return months


def load_questions_and_answers(product, months):
    base = Path('CONCATENATED_FILES') / product.upper()
    questions = {}
    answers_by_q = {}

    for y, m in months:
        fname_q = base / f"{y:04d}-{m:02d}-sumo-{product}-questions.csv"
        fname_a = base / f"{y:04d}-{m:02d}-sumo-{product}-answers.csv"
        if fname_q.exists():
            with open(fname_q, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    qid = row.get('id')
                    if not qid:
                        continue
                    created = row.get('created','')
                    # parse created to UTC date
                    try:
                        dt = parse_datetime_to_utc(created)
                        created_date = dt.date()
                    except Exception:
                        created_date = None
                    questions[qid] = {
                        'title': row.get('title','') or '',
                        'content': row.get('content','') or '',
                        'tags': row.get('tags','') or '',
                        'created_date': created_date
                    }
        if fname_a.exists():
            with open(fname_a, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    qid = row.get('question_id')
                    if not qid:
                        continue
                    created = row.get('created','')
                    try:
                        dt = parse_datetime_to_utc(created)
                        created_date = dt.date()
                    except Exception:
                        created_date = None
                    content = row.get('content','') or ''
                    answers_by_q.setdefault(qid, []).append({'created_date': created_date, 'content': content})

    return questions, answers_by_q


def parse_datetime_to_utc(s):
    # s examples: '2026-01-31 17:00:48 -0800'
    # Try several formats
    if not s or s.strip()=='' or s.strip().upper()=='NULL':
        raise ValueError('empty datetime')
    # Remove any surrounding quotes
    s = s.strip().strip('"')
    # Try to parse with %z
    try:
        dt = datetime.strptime(s, '%Y-%m-%d %H:%M:%S %z')
        return dt.astimezone(timezone.utc)
    except Exception:
        # try without tz
        try:
            dt = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
            return dt.replace(tzinfo=timezone.utc)
        except Exception:
            # fallback: parse date only
            return datetime.strptime(s.split()[0], '%Y-%m-%d').replace(tzinfo=timezone.utc)


def regex_to_filename(regex):
    # make a safe filename from regex: remove or replace non-alnum
    fname = re.sub(r'[^A-Za-z0-9]+', '_', regex)
    fname = fname.strip('_')
    if not fname:
        fname = 'regex'
    return fname


def count_matches_for_range(dates, questions, answers_by_q, pattern):
    counts = []
    matching_ids = []
    for d in dates:
        date_matching_qids = set()
        dstr = d.isoformat()
        # questions created on this date
        for qid, q in questions.items():
            if q.get('created_date') == d:
                for field in ('title','content','tags'):
                    text = q.get(field,'') or ''
                    if pattern.search(text):
                        date_matching_qids.add(qid)
                        break
        # answers created on this date (for any question, regardless of when question was created)
        for qid, answers in answers_by_q.items():
            for ans in answers:
                if ans.get('created_date') == d:
                    if pattern.search(ans.get('content','') or ''):
                        date_matching_qids.add(qid)
                        break
        counts.append(len(date_matching_qids))
        matching_ids.append(';'.join(sorted(date_matching_qids)))
    return counts, matching_ids


def ensure_reports_dir(product):
    rpt = Path('REPORTS') / product.upper()
    rpt.mkdir(parents=True, exist_ok=True)
    return rpt


def write_csv(report_path, dates1, counts1, counts2, ids1, ids2, regex_fname, start1, end1, start2, end2):
    with open(report_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        range1_label = f'{start1.isoformat()}_to_{end1.isoformat()}'
        range2_label = f'{start2.isoformat()}_to_{end2.isoformat()}'
        header = ['date', f'num-{regex_fname}-matches-{range1_label}', f'num-{regex_fname}-matches-{range2_label}',
                  f'{range1_label}-matching-ids', f'{range2_label}-matching-ids']
        writer.writerow(header)
        for d, c1, c2, id1, id2 in zip(dates1, counts1, counts2, ids1, ids2):
            writer.writerow([d.isoformat(), c1, c2, id1, id2])


def make_question_link(qid, questions):
    """Create a markdown link for a question ID with title as tooltip."""
    title = questions.get(qid, {}).get('title', '') or ''
    # Truncate to 80 chars
    title_truncated = title[:80]
    # Replace double quotes with U+FF02 (fullwidth quotation mark)
    title_escaped = title_truncated.replace('"', '\uff02')
    return f'[{qid}](https://support.mozilla.org/questions/{qid} "{title_escaped}")'


def write_markdown(markdown_path, dates1, counts1, counts2, ids1, ids2, regex_fname, start1, end1, start2, end2, questions):
    """Write markdown table with linked question IDs."""
    range1_label = f'{start1.isoformat()}_to_{end1.isoformat()}'
    range2_label = f'{start2.isoformat()}_to_{end2.isoformat()}'

    with open(markdown_path, 'w', encoding='utf-8') as f:
        # Write header
        f.write(f'# Keyword matches: {regex_fname}\n\n')
        f.write(f'Comparing **{start1.isoformat()} to {end1.isoformat()}** vs **{start2.isoformat()} to {end2.isoformat()}**\n\n')

        # Write table header
        f.write('| Date | ')
        f.write(f'num-{regex_fname}-matches-{range1_label} | ')
        f.write(f'num-{regex_fname}-matches-{range2_label} | ')
        f.write(f'{range1_label}-matching-ids | ')
        f.write(f'{range2_label}-matching-ids |\n')

        # Write separator
        f.write('|------|')
        f.write('---:|')
        f.write('---:|')
        f.write('----|')
        f.write('----|\n')

        # Write data rows
        for d, c1, c2, id_str1, id_str2 in zip(dates1, counts1, counts2, ids1, ids2):
            # Convert ID strings to markdown links
            if id_str1:
                ids1_list = id_str1.split(';')
                linked_ids1 = ', '.join([make_question_link(qid, questions) for qid in ids1_list])
            else:
                linked_ids1 = ''

            if id_str2:
                ids2_list = id_str2.split(';')
                linked_ids2 = ', '.join([make_question_link(qid, questions) for qid in ids2_list])
            else:
                linked_ids2 = ''

            f.write(f'| {d.isoformat()} | ')
            f.write(f'{c1} | ')
            f.write(f'{c2} | ')
            f.write(f'{linked_ids1} | ')
            f.write(f'{linked_ids2} |\n')


def plot_png(png_path, dates1, counts1, dates2, counts2, regex_fname, start1, end1, start2, end2):
    if plt is None:
        print('matplotlib not available; skipping PNG generation')
        return
    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(dates1, counts1, label=f'{start1.isoformat()} to {end1.isoformat()}')
    ax.plot(dates1, counts2, label=f'{start2.isoformat()} to {end2.isoformat()}')
    ax.set_xlabel('Date')
    ax.set_ylabel(f'num-{regex_fname}-matches')
    ax.set_title(f'Keyword matches: {regex_fname}')
    ax.legend()
    fig.autofmt_xdate()
    plt.tight_layout()
    fig.savefig(png_path)
    plt.close(fig)


def plot_bar_png(png_path, dates1, counts1, dates2, counts2, regex_fname, start1, end1, start2, end2):
    if plt is None:
        print('matplotlib not available; skipping PNG generation')
        return
    import numpy as np

    fig, ax = plt.subplots(figsize=(12,5))
    x = np.arange(len(dates1))
    width = 0.35

    bars1 = ax.bar(x - width/2, counts1, width, label=f'{start1.isoformat()} to {end1.isoformat()}')
    bars2 = ax.bar(x + width/2, counts2, width, label=f'{start2.isoformat()} to {end2.isoformat()}')

    ax.set_xlabel('Date')
    ax.set_ylabel(f'num-{regex_fname}-matches')
    ax.set_title(f'Keyword matches (bar chart): {regex_fname}')
    ax.set_xticks(x[::max(1, len(x)//15)])  # Show ~15 labels max to avoid crowding
    ax.set_xticklabels([dates1[i].isoformat() for i in range(0, len(dates1), max(1, len(x)//15))], rotation=45, ha='right')
    ax.legend()
    plt.tight_layout()
    fig.savefig(png_path)
    plt.close(fig)


def plot_overall_bar_png(png_path, counts1, counts2, regex_fname, start1, end1, start2, end2):
    if plt is None:
        print('matplotlib not available; skipping PNG generation')
        return

    total1 = sum(counts1)
    total2 = sum(counts2)

    fig, ax = plt.subplots(figsize=(8,6))
    periods = [f'{start1.isoformat()}\nto\n{end1.isoformat()}',
               f'{start2.isoformat()}\nto\n{end2.isoformat()}']
    totals = [total1, total2]
    colors = ['#1f77b4', '#ff7f0e']  # Blue and orange to match other plots

    bars = ax.bar(periods, totals, color=colors, width=0.6)

    # Add value labels on top of bars
    for bar, total in zip(bars, totals):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(total)}',
                ha='center', va='bottom', fontsize=12, fontweight='bold')

    ax.set_ylabel(f'Total num-{regex_fname}-matches', fontsize=11)
    ax.set_title(f'Overall keyword matches comparison: {regex_fname}', fontsize=12, fontweight='bold')
    ax.set_ylim(0, max(totals) * 1.15)  # Add 15% headroom for labels
    plt.tight_layout()
    fig.savefig(png_path)
    plt.close(fig)


def main(argv):
    product, start1, end1, start2, end2, regex = parse_args(argv)

    # build date lists
    dates1 = [start1 + timedelta(days=i) for i in range((end1-start1).days+1)]
    dates2 = [start2 + timedelta(days=i) for i in range((end2-start2).days+1)]
    if len(dates1) != len(dates2):
        print('Error: date ranges must be same length (they will be by construction)')
        sys.exit(1)

    # compile regex (case-insensitive)
    pattern = re.compile(regex, flags=re.IGNORECASE)
    regex_fname = regex_to_filename(regex)

    # load necessary month files
    earliest = min(start2, start1)
    latest = max(end2, end1)
    months = months_between(earliest, latest)

    questions, answers_by_q = load_questions_and_answers(product, months)

    counts1, ids1 = count_matches_for_range(dates1, questions, answers_by_q, pattern)
    counts2, ids2 = count_matches_for_range(dates2, questions, answers_by_q, pattern)

    # write CSV
    rpt_dir = ensure_reports_dir(product)
    # Filename includes both date-range-1 and date-range-2
    report_name = f"{start1.isoformat()}_{end1.isoformat()}__{start2.isoformat()}_{end2.isoformat()}_{regex_fname}.csv"
    report_path = rpt_dir / report_name
    # CSV contains dates and counts for both ranges side-by-side
    write_csv(report_path, dates1, counts1, counts2, ids1, ids2, regex_fname, start1, end1, start2, end2)
    print(f'Wrote CSV: {report_path}')

    # write markdown table
    markdown_name = f"{start1.isoformat()}_{end1.isoformat()}__{start2.isoformat()}_{end2.isoformat()}_{regex_fname}.md"
    markdown_path = rpt_dir / markdown_name
    write_markdown(markdown_path, dates1, counts1, counts2, ids1, ids2, regex_fname, start1, end1, start2, end2, questions)
    print(f'Wrote Markdown: {markdown_path}')

    # plot line graph PNG
    png_name = f"{start1.isoformat()}_{end1.isoformat()}__{start2.isoformat()}_{end2.isoformat()}_{regex_fname}.png"
    png_path = rpt_dir / png_name
    plot_png(png_path, dates1, counts1, dates2, counts2, regex_fname, start1, end1, start2, end2)
    if png_path.exists():
        print(f'Wrote PNG: {png_path}')

    # plot bar graph PNG
    bar_png_name = f"{start1.isoformat()}_{end1.isoformat()}__{start2.isoformat()}_{end2.isoformat()}_{regex_fname}_bar.png"
    bar_png_path = rpt_dir / bar_png_name
    plot_bar_png(bar_png_path, dates1, counts1, dates2, counts2, regex_fname, start1, end1, start2, end2)
    if bar_png_path.exists():
        print(f'Wrote bar graph PNG: {bar_png_path}')

    # plot overall bar chart PNG
    overall_bar_png_name = f"{start1.isoformat()}_{end1.isoformat()}__{start2.isoformat()}_{end2.isoformat()}_{regex_fname}_overall.png"
    overall_bar_png_path = rpt_dir / overall_bar_png_name
    plot_overall_bar_png(overall_bar_png_path, counts1, counts2, regex_fname, start1, end1, start2, end2)
    if overall_bar_png_path.exists():
        print(f'Wrote overall bar chart PNG: {overall_bar_png_path}')

if __name__ == '__main__':
    main(sys.argv[1:])
