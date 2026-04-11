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
    calendar month. product defaults to 'desktop'.

Outputs:
  - REPORTS/<product>/<start1>-<end1>-<regex_filename>.csv  (date,num-<regex>-matches)
  - REPORTS/<product>/<start1>-<end1>-<regex_filename>.png  (plot comparing the two ranges)

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
    # date-range-2 is same period starting n_days earlier
    start2 = start1 - timedelta(days=n_days)
    end2 = end1 - timedelta(days=n_days)

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
    for d in dates:
        total = 0
        dstr = d.isoformat()
        # questions created on this date
        for qid, q in questions.items():
            if q.get('created_date') == d:
                for field in ('title','content','tags'):
                    text = q.get(field,'') or ''
                    total += len(pattern.findall(text))
                # answers for this question created on this date
                for ans in answers_by_q.get(qid, []):
                    if ans.get('created_date') == d:
                        total += len(pattern.findall(ans.get('content','') or ''))
        counts.append(total)
    return counts


def ensure_reports_dir(product):
    rpt = Path('REPORTS') / product.upper()
    rpt.mkdir(parents=True, exist_ok=True)
    return rpt


def write_csv(report_path, dates1, counts1, counts2, regex_fname):
    with open(report_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        header = ['date', f'num-{regex_fname}-matches-range1', f'num-{regex_fname}-matches-range2']
        writer.writerow(header)
        for d, c1, c2 in zip(dates1, counts1, counts2):
            writer.writerow([d.isoformat(), c1, c2])


def plot_png(png_path, dates1, counts1, dates2, counts2, regex_fname, start1, end1):
    if plt is None:
        print('matplotlib not available; skipping PNG generation')
        return
    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(dates1, counts1, label=f'{start1.isoformat()} to {end1.isoformat()}')
    ax.plot(dates1, counts2, label='previous period')
    ax.set_xlabel('Date')
    ax.set_ylabel(f'num-{regex_fname}-matches')
    ax.set_title(f'Keyword matches: {regex_fname}')
    ax.legend()
    fig.autofmt_xdate()
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

    counts1 = count_matches_for_range(dates1, questions, answers_by_q, pattern)
    counts2 = count_matches_for_range(dates2, questions, answers_by_q, pattern)

    # write CSV
    rpt_dir = ensure_reports_dir(product)
    # Filename includes both date-range-1 and date-range-2
    report_name = f"{start1.isoformat()}_{end1.isoformat()}__{start2.isoformat()}_{end2.isoformat()}_{regex_fname}.csv"
    report_path = rpt_dir / report_name
    # CSV contains dates and counts for both ranges side-by-side
    write_csv(report_path, dates1, counts1, counts2, regex_fname)
    print(f'Wrote CSV: {report_path}')

    # plot PNG
    png_name = f"{start1.isoformat()}_{end1.isoformat()}__{start2.isoformat()}_{end2.isoformat()}_{regex_fname}.png"
    png_path = rpt_dir / png_name
    plot_png(png_path, dates1, counts1, dates2, counts2, regex_fname, start1, end1)
    if png_path.exists():
        print(f'Wrote PNG: {png_path}')

if __name__ == '__main__':
    main(sys.argv[1:])
