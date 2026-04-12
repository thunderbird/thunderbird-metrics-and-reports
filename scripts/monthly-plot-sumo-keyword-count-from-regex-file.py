#!/usr/bin/env python3
"""
Count regex matches from a CSV file of regexes in SUMO concatenated question and answer files on a MONTHLY basis.

Usage:
  - Five args mode:
      monthly-plot-sumo-keyword-count-from-regex-file.py <product> YYYY1 MM1 <num_months> <regex_file>.csv
    where <product> is 'desktop' or 'android', starts at YYYY1-MM1 and works backwards for the
    previous <num_months> calendar months. <regex_file>.csv is a CSV file with columns: regex_name, regex

  - Zero arg mode:
      monthly-plot-sumo-keyword-count-from-regex-file.py
    where it starts at the current calendar month and ends at the previous calendar month.
    product defaults to 'desktop'. <regex_file>.csv defaults to 'REPORTS/DESKTOP/desktop-regular_expressions.csv'.

Outputs:
  - REPORTS/<product>/<start_month>-<end_month>-<regex_file_base>.csv (monthly data)
  - REPORTS/<product>/<start_month>-<end_month>-<regex_file_base>.md (markdown table with linked question IDs)
  - REPORTS/<product>/<start_month>-<end_month>-<regex_file_base>.png (line plots)
  - REPORTS/<product>/<start_month>-<end_month>-<regex_file_base>_bar.png (bar graph)

All dates/times are handled in UTC.
"""

import sys
import re
import csv
from pathlib import Path
from datetime import datetime, timedelta, timezone, date
from dateutil.relativedelta import relativedelta
import os

# Increase the CSV field size limit to handle large content fields
csv.field_size_limit(sys.maxsize)

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
    if len(argv) == 5:
        product = argv[0]
        y1, m1 = int(argv[1]), int(argv[2])
        num_months = int(argv[3])
        regex_file = argv[4]
        start_month = date(y1, m1, 1)
    elif len(argv) == 0:
        product = 'desktop'
        regex_file = 'REPORTS/DESKTOP/desktop-regular_expressions.csv'
        today = datetime.utcnow().date()
        start_month = today.replace(day=1)
        num_months = 2  # Current month + previous month
    else:
        print("Usage:\n  monthly-plot-sumo-keyword-count-from-regex-file.py <product> YYYY MM <num_months> <regex_file>.csv\n  or\n  monthly-plot-sumo-keyword-count-from-regex-file.py")
        sys.exit(2)

    if num_months < 1:
        raise ValueError("num_months must be >= 1")

    # Calculate end month (going backwards)
    end_month = start_month - relativedelta(months=num_months - 1)

    return product, start_month, end_month, num_months, regex_file


def generate_month_list(start_month, end_month):
    """Generate list of months from end_month to start_month (chronological order)."""
    months = []
    current = end_month
    while current <= start_month:
        months.append(current)
        current = current + relativedelta(months=1)
    return months


def load_regex_file(regex_file_path):
    """Load regexes from CSV file with columns: regex_name, regex"""
    regexes = []
    try:
        # Pre-process file to handle backslash line continuations
        with open(regex_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Join lines that end with backslash (within quoted fields)
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


def months_to_load(month_list):
    """Convert list of month dates to (year, month) tuples."""
    return [(m.year, m.month) for m in month_list]


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


def count_matches_for_range_monthly(month_list, questions, answers_by_q, compiled_regexes):
    """Count matches for multiple regexes on a MONTHLY basis. Returns dict of {regex_name: (counts, ids)}"""
    results = {}

    for regex_info in compiled_regexes:
        name = regex_info['name']
        pattern = regex_info['compiled']
        counts = []
        matching_ids = []

        for month_date in month_list:
            month_matching_qids = set()
            year = month_date.year
            month = month_date.month

            # questions created in this month
            for qid, q in questions.items():
                created = q.get('created_date')
                if created and created.year == year and created.month == month:
                    for field in ('title','content','tags'):
                        text = q.get(field,'') or ''
                        if pattern.search(text):
                            month_matching_qids.add(qid)
                            break

            # answers created in this month (for any question, regardless of when question was created)
            for qid, answers in answers_by_q.items():
                for ans in answers:
                    created = ans.get('created_date')
                    if created and created.year == year and created.month == month:
                        if pattern.search(ans.get('content','') or ''):
                            month_matching_qids.add(qid)
                            break

            counts.append(len(month_matching_qids))
            matching_ids.append(';'.join(sorted(month_matching_qids)))

        results[name] = (counts, matching_ids)

    return results


def ensure_reports_dir(product):
    rpt = Path('REPORTS') / product.upper()
    rpt.mkdir(parents=True, exist_ok=True)
    return rpt


def write_csv(report_path, month_list, results, regex_names):
    """Write CSV with columns for each regex (monthly data)."""
    with open(report_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)

        # Build header
        header = ['month']
        # Add count columns for each regex
        for name in regex_names:
            header.append(f'num-{name}-matches')
        # Add ID columns for each regex
        for name in regex_names:
            header.append(f'{name}-matching-ids')

        writer.writerow(header)

        # Write data rows
        for i, month_date in enumerate(month_list):
            month_str = month_date.strftime('%Y-%m')
            row = [month_str]
            # Add counts
            for name in regex_names:
                counts, _ = results[name]
                row.append(counts[i])
            # Add IDs
            for name in regex_names:
                _, ids = results[name]
                row.append(ids[i])

            writer.writerow(row)


def make_question_link(qid, questions):
    """Create a markdown link for a question ID with title as tooltip."""
    title = questions.get(qid, {}).get('title', '') or ''
    # Truncate to 80 chars
    title_truncated = title[:80]
    # Replace characters that cause issues in markdown tables
    title_escaped = title_truncated.replace('"', '\uff02').replace('|', '¦')
    return f'[{qid}](https://support.mozilla.org/questions/{qid} "{title_escaped}")'


def write_markdown(markdown_path, month_list, results, regex_names, questions):
    """Write markdown table with linked question IDs for all regexes (monthly data)."""
    with open(markdown_path, 'w', encoding='utf-8') as f:
        # Write header
        f.write(f'# Monthly keyword matches from regex file\n\n')
        f.write(f'Period: **{month_list[0].strftime("%Y-%m")} to {month_list[-1].strftime("%Y-%m")}**\n\n')
        f.write(f'Regexes analyzed: {", ".join(regex_names)}\n\n')

        # Write table header
        f.write('| Month | ')
        for name in regex_names:
            f.write(f'num-{name}-matches | ')
        for name in regex_names:
            f.write(f'{name}-matching-ids')
            if name != regex_names[-1]:
                f.write(' | ')
        f.write(' |\n')

        # Write separator
        f.write('|------|')
        for _ in regex_names:
            f.write('---:|')
        for i, _ in enumerate(regex_names):
            f.write('----')
            if i < len(regex_names) - 1:
                f.write('|')
        f.write('|\n')

        # Write data rows
        for i, month_date in enumerate(month_list):
            month_str = month_date.strftime('%Y-%m')
            f.write(f'| {month_str} | ')

            # Write counts
            for name in regex_names:
                counts, _ = results[name]
                f.write(f'{counts[i]} | ')

            # Write IDs with links
            for j, name in enumerate(regex_names):
                _, ids = results[name]

                if ids[i]:
                    id_list = ids[i].split(';')
                    linked_ids = ', '.join([make_question_link(qid, questions) for qid in id_list])
                else:
                    linked_ids = ''
                f.write(f'{linked_ids}')
                if j < len(regex_names) - 1:
                    f.write(' | ')

            f.write('\n')


def plot_png(png_path, month_list, results, regex_names):
    """Plot line graphs for all regexes (monthly data)."""
    if plt is None:
        print('matplotlib not available; skipping PNG generation')
        return

    fig, ax = plt.subplots(figsize=(12,6))

    # Plot each regex as a separate line
    colors = plt.cm.tab10.colors
    month_labels = [m.strftime('%Y-%m') for m in month_list]

    for i, name in enumerate(regex_names):
        counts, _ = results[name]
        color = colors[i % len(colors)]
        ax.plot(month_labels, counts, label=name, color=color, marker='o', markersize=5)

    ax.set_xlabel('Month')
    ax.set_ylabel('Number of matches')
    ax.set_title(f'Monthly keyword matches')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    fig.savefig(png_path, bbox_inches='tight')
    plt.close(fig)


def plot_bar_png(png_path, month_list, results, regex_names):
    """Plot grouped bar chart for all regexes (monthly data)."""
    if plt is None:
        print('matplotlib not available; skipping PNG generation')
        return
    import numpy as np

    fig, ax = plt.subplots(figsize=(14,6))
    month_labels = [m.strftime('%Y-%m') for m in month_list]
    x = np.arange(len(month_labels))

    # Calculate bar width based on number of regexes
    total_width = 0.8
    n_regexes = len(regex_names)
    width = total_width / n_regexes

    colors = plt.cm.tab10.colors

    # Plot bars for each regex
    for i, name in enumerate(regex_names):
        counts, _ = results[name]
        color = colors[i % len(colors)]
        offset = (i - n_regexes/2 + 0.5) * width
        ax.bar(x + offset, counts, width, label=name, color=color, alpha=0.8)

    ax.set_xlabel('Month')
    ax.set_ylabel('Number of matches')
    ax.set_title(f'Monthly keyword matches (bar chart)')
    ax.set_xticks(x)
    ax.set_xticklabels(month_labels, rotation=45, ha='right')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    fig.savefig(png_path, bbox_inches='tight')
    plt.close(fig)


def main(argv):
    product, start_month, end_month, num_months, regex_file = parse_args(argv)

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
    print(f"Monthly analysis from {end_month.strftime('%Y-%m')} to {start_month.strftime('%Y-%m')} ({num_months} months)")

    # Generate month list
    month_list = generate_month_list(start_month, end_month)

    # Load necessary month files
    months_tuple = months_to_load(month_list)
    questions, answers_by_q = load_questions_and_answers(product, months_tuple)

    # Count matches for all regexes
    results = count_matches_for_range_monthly(month_list, questions, answers_by_q, compiled_regexes)

    # Generate output filenames
    rpt_dir = ensure_reports_dir(product)
    regex_file_base = Path(regex_file).stem

    start_str = end_month.strftime('%Y-%m')
    end_str = start_month.strftime('%Y-%m')

    # write CSV
    report_name = f"{start_str}_{end_str}_{regex_file_base}.csv"
    report_path = rpt_dir / report_name
    write_csv(report_path, month_list, results, regex_names)
    print(f'Wrote CSV: {report_path}')

    # write markdown table
    markdown_name = f"{start_str}_{end_str}_{regex_file_base}.md"
    markdown_path = rpt_dir / markdown_name
    write_markdown(markdown_path, month_list, results, regex_names, questions)
    print(f'Wrote Markdown: {markdown_path}')

    # plot line graph PNG
    png_name = f"{start_str}_{end_str}_{regex_file_base}.png"
    png_path = rpt_dir / png_name
    plot_png(png_path, month_list, results, regex_names)
    if png_path.exists():
        print(f'Wrote PNG: {png_path}')

    # plot bar graph PNG
    bar_png_name = f"{start_str}_{end_str}_{regex_file_base}_bar.png"
    bar_png_path = rpt_dir / bar_png_name
    plot_bar_png(bar_png_path, month_list, results, regex_names)
    if bar_png_path.exists():
        print(f'Wrote bar graph PNG: {bar_png_path}')

if __name__ == '__main__':
    main(sys.argv[1:])
