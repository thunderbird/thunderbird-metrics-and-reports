#!/usr/bin/env python3
"""
Count regex matches from a CSV file of regexes in SUMO concatenated question and answer files and plot counts.

Usage:
  - Eight args mode:
      plot-sumo-keyword-count-from-regex-file.py <product> YYYY1 MM1 DD1 YYYY2 MM2 DD2 <regex_file>.csv
    where <product> is 'desktop' or 'android', date-range1 starts at YYYY1-MM1-DD1 and
    ends at YYYY2-MM2-DD2 (inclusive). Let n be number of days in date-range1. Date-range2
    is the same period starting n days earlier. <regex_file>.csv is a CSV file with columns:
    regex_name, regex

  - Zero arg mode:
      plot-sumo-keyword-count-from-regex-file.py
    where date-range1 is the current calendar month and date-range2 is the previous
    calendar month, adjusted to match the length of the current month (by adding or
    removing days from the start of the previous month). product defaults to 'desktop'.
    <regex_file>.csv defaults to 'REPORTS/DESKTOP/desktop-regular_expressions.csv'.

Outputs:
  - REPORTS/<product>/<start1>-<end1>-<regex_file_base>.csv
  - REPORTS/<product>/<start1>-<end1>-<regex_file_base>.md (markdown table with linked question IDs)
  - REPORTS/<product>/<start1>-<end1>-<regex_file_base>.png (line plots comparing the two ranges)
  - REPORTS/<product>/<start1>-<end1>-<regex_file_base>_bar.png (bar graph comparing the two ranges)

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
        regex_file = argv[7]
        start1 = date(y1, m1, d1)
        end1 = date(y2, m2, d2)
    elif len(argv) == 0:
        product = 'desktop'
        regex_file = 'REPORTS/DESKTOP/desktop-regular_expressions.csv'
        today = datetime.utcnow().date()
        start1 = today.replace(day=1)
        # end1 is last day of current month
        if start1.month == 12:
            end1 = date(start1.year, 12, 31)
        else:
            end1 = (start1.replace(month=start1.month+1) - timedelta(days=1))
    else:
        print("Usage:\n  plot-sumo-keyword-count-from-regex-file.py <product> YYYY1 MM1 DD1 YYYY2 MM2 DD2 <regex_file>.csv\n  or\n  plot-sumo-keyword-count-from-regex-file.py")
        sys.exit(2)

    if start1 > end1:
        raise ValueError("start date must be <= end date")

    # compute n days
    n_days = (end1 - start1).days + 1
    # date-range-2 is same period starting n_days earlier by default
    start2 = start1 - timedelta(days=n_days)
    end2 = end1 - timedelta(days=n_days)

    # If script was invoked in zero-arg mode, set date-range-2 to the previous calendar month
    if len(argv) == 0:
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

    return product, start1, end1, start2, end2, regex_file


def load_regex_file(regex_file_path):
    """Load regexes from CSV file with columns: regex_name, regex"""
    regexes = []
    try:
        # Pre-process file to handle backslash line continuations
        with open(regex_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Join lines that end with backslash (within quoted fields)
        # This is a simple approach: replace backslash-newline with nothing
        content = content.replace('\\\n', ' ').replace('\\\r\n', ' ')

        # Parse the processed content as CSV
        import io
        reader = csv.DictReader(io.StringIO(content))

        # Strip whitespace from fieldnames
        if reader.fieldnames:
            reader.fieldnames = [name.strip() if name else name for name in reader.fieldnames]

        for row in reader:
            # Get values, handling None case
            name = row.get('regex_name') or row.get('regex_name ') or ''
            pattern = row.get('regex') or row.get(' regex') or ''

            name = name.strip() if name else ''
            pattern = pattern.strip() if pattern else ''

            # Remove surrounding quotes (both single, double, and triple quotes)
            if pattern:
                # Remove triple quotes
                if pattern.startswith('"""') and pattern.endswith('"""'):
                    pattern = pattern[3:-3]
                # Remove single or double quotes
                elif (pattern.startswith('"') and pattern.endswith('"')) or \
                     (pattern.startswith("'") and pattern.endswith("'")):
                    pattern = pattern[1:-1]
                pattern = pattern.strip()

            if name and pattern:
                regexes.append({'name': name, 'pattern': pattern})
    except FileNotFoundError:
        print(f"Error: Regex file not found: {regex_file_path}")
        sys.exit(1)

    if not regexes:
        print(f"Error: No valid regexes found in {regex_file_path}")
        sys.exit(1)

    return regexes


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


def count_matches_for_range(dates, questions, answers_by_q, compiled_regexes):
    """Count matches for multiple regexes. Returns dict of {regex_name: (counts, ids)}"""
    results = {}

    for regex_info in compiled_regexes:
        name = regex_info['name']
        pattern = regex_info['compiled']
        counts = []
        matching_ids = []

        for d in dates:
            date_matching_qids = set()
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

        results[name] = (counts, matching_ids)

    return results


def ensure_reports_dir(product):
    rpt = Path('REPORTS') / product.upper()
    rpt.mkdir(parents=True, exist_ok=True)
    return rpt


def write_csv(report_path, dates1, results1, results2, regex_names, start1, end1, start2, end2):
    """Write CSV with columns for each regex."""
    range1_label = f'{start1.isoformat()}_to_{end1.isoformat()}'
    range2_label = f'{start2.isoformat()}_to_{end2.isoformat()}'

    with open(report_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)

        # Build header
        header = ['date']
        # Add count columns for each regex
        for name in regex_names:
            header.append(f'num-{name}-matches-{range1_label}')
            header.append(f'num-{name}-matches-{range2_label}')
        # Add ID columns for each regex
        for name in regex_names:
            header.append(f'{range1_label}-{name}-matching-ids')
            header.append(f'{range2_label}-{name}-matching-ids')

        writer.writerow(header)

        # Write data rows
        for i, d in enumerate(dates1):
            row = [d.isoformat()]
            # Add counts
            for name in regex_names:
                counts1, _ = results1[name]
                counts2, _ = results2[name]
                row.append(counts1[i])
                row.append(counts2[i])
            # Add IDs
            for name in regex_names:
                _, ids1 = results1[name]
                _, ids2 = results2[name]
                row.append(ids1[i])
                row.append(ids2[i])

            writer.writerow(row)


def make_question_link(qid, questions):
    """Create a markdown link for a question ID with title as tooltip."""
    title = questions.get(qid, {}).get('title', '') or ''
    # Truncate to 80 chars
    title_truncated = title[:80]
    # Replace characters that cause issues in markdown tables
    title_escaped = title_truncated.replace('"', '\uff02').replace('|', '¦')
    return f'[{qid}](https://support.mozilla.org/questions/{qid} "{title_escaped}")'


def write_markdown(markdown_path, dates1, results1, results2, regex_names, start1, end1, start2, end2, questions):
    """Write markdown table with linked question IDs for all regexes."""
    range1_label = f'{start1.isoformat()}_to_{end1.isoformat()}'
    range2_label = f'{start2.isoformat()}_to_{end2.isoformat()}'

    with open(markdown_path, 'w', encoding='utf-8') as f:
        # Write header
        f.write(f'# Keyword matches from regex file\n\n')
        f.write(f'Comparing **{start1.isoformat()} to {end1.isoformat()}** vs **{start2.isoformat()} to {end2.isoformat()}**\n\n')
        f.write(f'Regexes analyzed: {", ".join(regex_names)}\n\n')

        # Write table header
        f.write('| Date | ')
        for name in regex_names:
            f.write(f'num-{name}-matches-{range1_label} | ')
            f.write(f'num-{name}-matches-{range2_label} | ')
        for name in regex_names:
            f.write(f'{range1_label}-{name}-matching-ids | ')
            f.write(f'{range2_label}-{name}-matching-ids | ')
        f.write('\n')

        # Write separator
        f.write('|------|')
        for _ in regex_names:
            f.write('---:|---:|')
        for _ in regex_names:
            f.write('----|----')
            if _ != regex_names[-1]:
                f.write('|')
        f.write('|\n')

        # Write data rows
        for i, d in enumerate(dates1):
            f.write(f'| {d.isoformat()} | ')

            # Write counts
            for name in regex_names:
                counts1, _ = results1[name]
                counts2, _ = results2[name]
                f.write(f'{counts1[i]} | ')
                f.write(f'{counts2[i]} | ')

            # Write IDs with links
            for j, name in enumerate(regex_names):
                _, ids1 = results1[name]
                _, ids2 = results2[name]

                # Range 1 IDs
                if ids1[i]:
                    id_list = ids1[i].split(';')
                    linked_ids = ', '.join([make_question_link(qid, questions) for qid in id_list])
                else:
                    linked_ids = ''
                f.write(f'{linked_ids} | ')

                # Range 2 IDs
                if ids2[i]:
                    id_list = ids2[i].split(';')
                    linked_ids = ', '.join([make_question_link(qid, questions) for qid in id_list])
                else:
                    linked_ids = ''
                f.write(f'{linked_ids}')
                if j < len(regex_names) - 1:
                    f.write(' | ')

            f.write('\n')


def plot_png(png_path, dates1, results1, results2, regex_names, start1, end1, start2, end2):
    """Plot line graphs for all regexes."""
    if plt is None:
        print('matplotlib not available; skipping PNG generation')
        return

    fig, ax = plt.subplots(figsize=(12,6))

    # Plot each regex as a separate line
    colors = plt.cm.tab10.colors
    for i, name in enumerate(regex_names):
        counts1, _ = results1[name]
        counts2, _ = results2[name]
        color = colors[i % len(colors)]

        ax.plot(dates1, counts1, label=f'{name} ({start1.isoformat()} to {end1.isoformat()})',
                color=color, linestyle='-', marker='o', markersize=3)
        ax.plot(dates1, counts2, label=f'{name} ({start2.isoformat()} to {end2.isoformat()})',
                color=color, linestyle='--', marker='s', markersize=3)

    ax.set_xlabel('Date')
    ax.set_ylabel('Number of matches')
    ax.set_title(f'Keyword matches comparison')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    fig.autofmt_xdate()
    plt.tight_layout()
    fig.savefig(png_path, bbox_inches='tight')
    plt.close(fig)


def plot_bar_png(png_path, dates1, results1, results2, regex_names, start1, end1, start2, end2):
    """Plot grouped bar chart for all regexes."""
    if plt is None:
        print('matplotlib not available; skipping PNG generation')
        return
    import numpy as np

    fig, ax = plt.subplots(figsize=(14,6))
    x = np.arange(len(dates1))

    # Calculate bar width based on number of regexes
    total_width = 0.8
    n_regexes = len(regex_names)
    width = total_width / (n_regexes * 2)  # 2 for range1 and range2

    colors = plt.cm.tab10.colors

    # Plot bars for each regex
    for i, name in enumerate(regex_names):
        counts1, _ = results1[name]
        counts2, _ = results2[name]
        color = colors[i % len(colors)]

        offset1 = (i * 2 - n_regexes) * width
        offset2 = (i * 2 + 1 - n_regexes) * width

        ax.bar(x + offset1, counts1, width, label=f'{name} ({start1.isoformat()[:7]})',
               color=color, alpha=0.8)
        ax.bar(x + offset2, counts2, width, label=f'{name} ({start2.isoformat()[:7]})',
               color=color, alpha=0.5, hatch='//')

    ax.set_xlabel('Date')
    ax.set_ylabel('Number of matches')
    ax.set_title(f'Keyword matches (bar chart)')
    ax.set_xticks(x[::max(1, len(x)//15)])  # Show ~15 labels max to avoid crowding
    ax.set_xticklabels([dates1[i].isoformat() for i in range(0, len(dates1), max(1, len(x)//15))],
                       rotation=45, ha='right')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    fig.savefig(png_path, bbox_inches='tight')
    plt.close(fig)


def main(argv):
    product, start1, end1, start2, end2, regex_file = parse_args(argv)

    # Load regexes from file
    regexes = load_regex_file(regex_file)
    regex_names = [r['name'] for r in regexes]

    # Compile all regexes (case-insensitive)
    compiled_regexes = []
    for r in regexes:
        try:
            compiled = re.compile(r['pattern'], flags=re.IGNORECASE)
            compiled_regexes.append({'name': r['name'], 'compiled': compiled})
        except re.error as e:
            print(f"Error compiling regex '{r['name']}': {e}")
            sys.exit(1)

    print(f"Processing {len(compiled_regexes)} regexes: {', '.join(regex_names)}")

    # build date lists
    dates1 = [start1 + timedelta(days=i) for i in range((end1-start1).days+1)]
    dates2 = [start2 + timedelta(days=i) for i in range((end2-start2).days+1)]
    if len(dates1) != len(dates2):
        print('Error: date ranges must be same length (they will be by construction)')
        sys.exit(1)

    # load necessary month files
    earliest = min(start2, start1)
    latest = max(end2, end1)
    months = months_between(earliest, latest)

    questions, answers_by_q = load_questions_and_answers(product, months)

    # Count matches for all regexes
    results1 = count_matches_for_range(dates1, questions, answers_by_q, compiled_regexes)
    results2 = count_matches_for_range(dates2, questions, answers_by_q, compiled_regexes)

    # Generate output filenames
    rpt_dir = ensure_reports_dir(product)
    regex_file_base = Path(regex_file).stem  # Get filename without extension

    # write CSV
    report_name = f"{start1.isoformat()}_{end1.isoformat()}__{start2.isoformat()}_{end2.isoformat()}_{regex_file_base}.csv"
    report_path = rpt_dir / report_name
    write_csv(report_path, dates1, results1, results2, regex_names, start1, end1, start2, end2)
    print(f'Wrote CSV: {report_path}')

    # write markdown table
    markdown_name = f"{start1.isoformat()}_{end1.isoformat()}__{start2.isoformat()}_{end2.isoformat()}_{regex_file_base}.md"
    markdown_path = rpt_dir / markdown_name
    write_markdown(markdown_path, dates1, results1, results2, regex_names, start1, end1, start2, end2, questions)
    print(f'Wrote Markdown: {markdown_path}')

    # plot line graph PNG
    png_name = f"{start1.isoformat()}_{end1.isoformat()}__{start2.isoformat()}_{end2.isoformat()}_{regex_file_base}.png"
    png_path = rpt_dir / png_name
    plot_png(png_path, dates1, results1, results2, regex_names, start1, end1, start2, end2)
    if png_path.exists():
        print(f'Wrote PNG: {png_path}')

    # plot bar graph PNG
    bar_png_name = f"{start1.isoformat()}_{end1.isoformat()}__{start2.isoformat()}_{end2.isoformat()}_{regex_file_base}_bar.png"
    bar_png_path = rpt_dir / bar_png_name
    plot_bar_png(bar_png_path, dates1, results1, results2, regex_names, start1, end1, start2, end2)
    if bar_png_path.exists():
        print(f'Wrote bar graph PNG: {bar_png_path}')

if __name__ == '__main__':
    main(sys.argv[1:])
