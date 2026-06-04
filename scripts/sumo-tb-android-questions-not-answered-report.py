#!/usr/bin/env python3
"""
Report Thunderbird for Android questions not answered by non-creators in 72+ hours.

Usage (no args = use current UTC time):
    uv run scripts/sumo-tb-android-questions-not-answered-report.py

Usage with explicit date/time:
    uv run scripts/sumo-tb-android-questions-not-answered-report.py YEAR MONTH DAY HOUR
    e.g. uv run scripts/sumo-tb-android-questions-not-answered-report.py 2026 4 2 22
"""
import sys
import os
import csv
import re
import html
from datetime import datetime, timezone, timedelta
import pandas as pd

csv.field_size_limit(sys.maxsize)

DATA_DIR = 'aaq-android-data'
MARKDOWN_DIR = 'UNANSWERED_QUESTIONS/MARKDOWN_REPORTS'
CSV_DIR = 'UNANSWERED_QUESTIONS/CSV_REPORTS'
HTML_DIR = 'UNANSWERED_QUESTIONS/HTML_REPORTS'
WINDOW_HOURS = 72
WINDOW_DAYS = 14
Q_SUFFIX = 'tbandroid-creator-answers-desktop-all-locales.csv'
A_SUFFIX = 'tbandroid-answers-for-questions-desktop.csv'


def parse_args():
    if len(sys.argv) == 5:
        return int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    now = datetime.now(timezone.utc)
    return now.year, now.month, now.day, now.hour


def daily_files_in_range(start_dt, end_dt, suffix):
    files = []
    current = start_dt.replace(hour=0, minute=0, second=0, microsecond=0)
    end = end_dt.replace(hour=0, minute=0, second=0, microsecond=0)
    while current <= end:
        y, m, d = current.year, current.month, current.day
        path = os.path.join(DATA_DIR, str(y),
            f'{y}-{m:02d}-{d:02d}-{y}-{m:02d}-{d:02d}-{suffix}')
        if os.path.exists(path):
            files.append(path)
        current += timedelta(days=1)
    return files


def load_dataframes(files):
    if not files:
        return pd.DataFrame()
    dfs = []
    for f in files:
        try:
            dfs.append(pd.read_csv(f, low_memory=False))
        except Exception as e:
            print(f'Warning: could not read {f}: {e}', file=sys.stderr)
    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()


def strip_html(text):
    if not text or (isinstance(text, float) and pd.isna(text)):
        return ''
    text = re.sub(r'<[^>]+>', '', str(text))
    return html.unescape(text)


def escape_for_tooltip(text):
    text = strip_html(text)
    text = text.replace('"', '＂')
    text = text.replace('|', '¦')
    return text


def parse_metadata(meta):
    if meta is None or (isinstance(meta, float) and pd.isna(meta)) or not str(meta).strip():
        return '', ''
    s = str(meta)
    version = ''
    os_str = ''
    m = re.search(r'tb_version:([^;]+)', s)
    if m:
        version = m.group(1).strip()
    m = re.search(r'(?:^|;)os:([^;]+)', s)
    if m:
        os_str = m.group(1).strip()
    return version, os_str


def insert_linebreaks(text, col=64):
    """Insert one <br /> after the first word whose start position exceeds `col`."""
    words = text.split(' ')
    result = ''
    pos = 0
    for i, word in enumerate(words):
        if i > 0:
            result += ' '
            pos += 1
        word_start = pos
        result += word
        pos += len(word)
        if word_start > col:
            result += '<br />'
            result += ' '.join(words[i + 1:])
            break
    return result


def to_utc_str(ts):
    if pd.isna(ts):
        return ''
    return ts.tz_convert('UTC').strftime('%Y-%m-%d %H:%M')


def format_elapsed(created_utc, report_time):
    """Return (display_str, total_hours) for elapsed time since creation."""
    delta = pd.Timestamp(report_time) - created_utc
    total_hours = int(delta.total_seconds()) // 3600
    days, hours = divmod(total_hours, 24)
    display = f'{days}d {hours}h' if days > 0 else f'{hours}h'
    return display, total_hours


def write_markdown(df, path, report_time, window_start, window_end):
    lines = [
        '# Thunderbird for Android - Unanswered Questions',
        '',
        f'Report generated: {report_time.strftime("%Y-%m-%d %H:%M")} UTC',
        '',
        (f'Questions created between {window_start.strftime("%Y-%m-%d %H:%M")} UTC and '
         f'{window_end.strftime("%Y-%m-%d %H:%M")} UTC with no non-creator answers'),
        '',
        f'Total: {len(df)} unanswered questions',
        '',
        '| Date Created (UTC) | Elapsed | Creator | Version | OS | Question |',
        '|---|---|---|---|---|---|',
    ]

    for _, q in df.iterrows():
        date_str = to_utc_str(q['created_utc'])
        elapsed, _ = format_elapsed(q['created_utc'], report_time)
        creator = str(q['creator']) if pd.notna(q.get('creator')) else ''
        creator_link = (f'<a href="https://support.mozilla.org/en-US/user/{creator}/">'
                        f'{creator}</a>')

        version, os_str = parse_metadata(q.get('metadata'))
        os_display = os_str[:20]

        qid = q['id']
        title = str(q['title']) if pd.notna(q.get('title')) else ''
        content = strip_html(q.get('content'))

        tooltip = escape_for_tooltip(content[:255])
        link_text_raw = f'{qid}: {title[:80]}'.replace('|', '¦')
        link_text = insert_linebreaks(link_text_raw, 65)
        url = f'https://support.mozilla.org/questions/{qid}'
        q_cell = f'<a href="{url}" title="{tooltip}">{link_text}</a>'

        lines.append(f'| {date_str} | {elapsed} | {creator_link} | {version} | {os_display} | {q_cell} |')

    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


def write_csv(df, path, report_time):
    fieldnames = [
        'date_created_utc', 'elapsed', 'creator', 'creator_url', 'version', 'os',
        'question_id', 'question_url', 'question_title', 'question_content',
    ]
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for _, q in df.iterrows():
            version, os_str = parse_metadata(q.get('metadata'))
            creator = str(q['creator']) if pd.notna(q.get('creator')) else ''
            qid = q['id']
            title = str(q['title']) if pd.notna(q.get('title')) else ''
            content = strip_html(q.get('content'))
            writer.writerow({
                'date_created_utc': to_utc_str(q['created_utc']),
                'elapsed': format_elapsed(q['created_utc'], report_time)[0],
                'creator': creator,
                'creator_url': f'https://support.mozilla.org/en-US/user/{creator}/',
                'version': version,
                'os': os_str,
                'question_id': qid,
                'question_url': f'https://support.mozilla.org/questions/{qid}',
                'question_title': title,
                'question_content': content,
            })


_SORT_JS = """
  const headers = document.querySelectorAll('th');
  const sortState = {};
  headers.forEach((th, col) => {
    th.style.cursor = 'pointer';
    th.addEventListener('click', () => {
      const tbody = th.closest('table').querySelector('tbody');
      const rows = Array.from(tbody.querySelectorAll('tr'));
      const asc = !sortState[col];
      sortState[col] = asc;
      rows.sort((a, b) => {
        const av = a.cells[col].dataset.sort ?? a.cells[col].textContent.trim();
        const bv = b.cells[col].dataset.sort ?? b.cells[col].textContent.trim();
        const an = parseFloat(av), bn = parseFloat(bv);
        if (!isNaN(an) && !isNaN(bn)) return asc ? an - bn : bn - an;
        return asc ? av.localeCompare(bv) : bv.localeCompare(av);
      });
      rows.forEach(r => tbody.appendChild(r));
      headers.forEach(h => { h.textContent = h.textContent.replace(/ [▲▼]$/, ''); });
      th.textContent += asc ? ' ▲' : ' ▼';
    });
  });
"""

_HTML_CSS = """
  body { font-family: sans-serif; font-size: 13px; margin: 1em; }
  h1 { font-size: 1.2em; }
  table { border-collapse: collapse; width: 100%; }
  th, td { border: 1px solid #ccc; padding: 4px 8px; text-align: left; vertical-align: top; }
  th { background: #f0f0f0; user-select: none; white-space: nowrap; }
  th:hover { background: #ddd; }
  tr:nth-child(even) { background: #f9f9f9; }
  a { color: #0060df; }
"""


def write_html(df, path, report_time, window_start, window_end, title):
    rows = []
    for _, q in df.iterrows():
        date_str = to_utc_str(q['created_utc'])
        elapsed_str, elapsed_hours = format_elapsed(q['created_utc'], report_time)

        creator = str(q['creator']) if pd.notna(q.get('creator')) else ''
        creator_cell = (f'<a href="https://support.mozilla.org/en-US/user/{creator}/">'
                        f'{html.escape(creator)}</a>')

        version, os_str = parse_metadata(q.get('metadata'))
        os_display = html.escape(os_str[:20])

        qid = q['id']
        q_title = str(q['title']) if pd.notna(q.get('title')) else ''
        content = strip_html(q.get('content'))
        tooltip = html.escape(content[:255])
        link_text = html.escape(f'{qid}: {q_title[:80]}')
        link_text = insert_linebreaks(link_text, 65)
        url = f'https://support.mozilla.org/questions/{qid}'
        q_cell = f'<a href="{url}" title="{tooltip}">{link_text}</a>'

        rows.append(f'''    <tr>
      <td>{date_str}</td>
      <td data-sort="{elapsed_hours}">{elapsed_str}</td>
      <td>{creator_cell}</td>
      <td>{html.escape(version)}</td>
      <td>{os_display}</td>
      <td>{q_cell}</td>
    </tr>''')

    rows_html = '\n'.join(rows)
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{html.escape(title)} {report_time.strftime("%Y-%m-%d %H:%M")} UTC</title>
  <style>{_HTML_CSS}</style>
</head>
<body>
  <h1>{html.escape(title)}</h1>
  <p>Report generated: {report_time.strftime("%Y-%m-%d %H:%M")} UTC</p>
  <p>Questions created between {window_start.strftime("%Y-%m-%d %H:%M")} UTC
     and {window_end.strftime("%Y-%m-%d %H:%M")} UTC with no non-creator answers</p>
  <p>Total: {len(df)} unanswered questions</p>
  <table>
    <thead>
      <tr>
        <th>Date Created (UTC)</th>
        <th>Elapsed</th>
        <th>Creator</th>
        <th>Version</th>
        <th>OS</th>
        <th>Question</th>
      </tr>
    </thead>
    <tbody>
{rows_html}
    </tbody>
  </table>
  <script>{_SORT_JS}</script>
</body>
</html>
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(page)


def write_index():
    index_path = os.path.join('UNANSWERED_QUESTIONS', 'index.html')
    html_files = sorted(
        [f for f in os.listdir(HTML_DIR) if f.endswith('.html')],
        reverse=True,
    )

    rows = []
    for fname in html_files:
        parts = fname.replace('-unanswered-questions.html', '').rsplit('-', 1)
        platform = parts[-1].capitalize() if len(parts) == 2 else ''
        date = parts[0] if len(parts) == 2 else fname
        rows.append(
            f'  <tr><td>{date}</td><td>{platform}</td>'
            f'<td><a href="HTML_REPORTS/{fname}">{fname}</a></td></tr>'
        )

    rows_html = '\n'.join(rows)
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Unanswered Questions Reports</title>
  <style>
    body {{ font-family: sans-serif; font-size: 13px; margin: 1em; }}
    h1 {{ font-size: 1.2em; }}
    table {{ border-collapse: collapse; }}
    th, td {{ border: 1px solid #ccc; padding: 4px 8px; text-align: left; }}
    th {{ background: #f0f0f0; }}
    tr:nth-child(even) {{ background: #f9f9f9; }}
    a {{ color: #0060df; }}
  </style>
</head>
<body>
  <h1>Unanswered Questions Reports</h1>
  <p>Thunderbird Desktop and Android questions with no non-creator answers,
     created between {WINDOW_HOURS} hours and {WINDOW_DAYS} days ago. Updated twice daily.</p>
  <table>
    <thead>
      <tr><th>Date</th><th>Platform</th><th>Report</th></tr>
    </thead>
    <tbody>
{rows_html}
    </tbody>
  </table>
</body>
</html>
"""
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(page)
    print(f'Written: {index_path}')


def main():
    year, month, day, hour = parse_args()
    report_time = datetime(year, month, day, hour, 0, 0, tzinfo=timezone.utc)
    window_end = report_time - timedelta(hours=WINDOW_HOURS)
    window_start = report_time - timedelta(days=WINDOW_DAYS)

    print(f'Report time: {report_time.strftime("%Y-%m-%d %H:%M")} UTC')
    print(f'Window: {window_start.strftime("%Y-%m-%d %H:%M")} UTC '
          f'to {window_end.strftime("%Y-%m-%d %H:%M")} UTC')

    q_files = daily_files_in_range(
        window_start - timedelta(days=1),
        window_end + timedelta(days=1),
        Q_SUFFIX,
    )
    a_files = daily_files_in_range(
        window_start - timedelta(days=1),
        report_time,
        A_SUFFIX,
    )

    print(f'Loading {len(q_files)} question files, {len(a_files)} answer files')

    q_df = load_dataframes(q_files)
    a_df = load_dataframes(a_files)

    if q_df.empty:
        print('No question data found.', file=sys.stderr)
        return

    q_df['created_utc'] = pd.to_datetime(q_df['created'], utc=True)
    q_df = q_df[q_df['is_spam'].astype(str).str.lower() != 'true']
    q_df = q_df.sort_values('created_utc').drop_duplicates(subset='id', keep='last')

    window_start_ts = pd.Timestamp(window_start)
    window_end_ts = pd.Timestamp(window_end)
    q_df = q_df[
        (q_df['created_utc'] > window_start_ts) &
        (q_df['created_utc'] <= window_end_ts)
    ]

    print(f'Questions in window: {len(q_df)}')

    answer_creators: dict[int, set] = {}
    if not a_df.empty:
        if 'is_spam' in a_df.columns:
            a_df = a_df[a_df['is_spam'].astype(str).str.lower() != 'true']
        a_df = a_df.drop_duplicates(subset='id', keep='last')
        a_df = a_df[a_df['question_id'].isin(set(q_df['id']))]
        answer_creators = (
            a_df.assign(creator=a_df['creator'].fillna('').astype(str))
            .groupby('question_id')['creator']
            .agg(set)
            .to_dict()
        )

    def has_non_creator_answer(row):
        q_creator = str(row['creator']) if pd.notna(row.get('creator')) else ''
        return bool(answer_creators.get(row['id'], set()) - {q_creator})

    unanswered_df = q_df[~q_df.apply(has_non_creator_answer, axis=1)].sort_values('created_utc')

    print(f'Unanswered questions: {len(unanswered_df)}')

    os.makedirs(MARKDOWN_DIR, exist_ok=True)
    os.makedirs(CSV_DIR, exist_ok=True)
    os.makedirs(HTML_DIR, exist_ok=True)

    ts = f'{year}-{month:02d}-{day:02d}'
    md_path = os.path.join(MARKDOWN_DIR, f'{ts}-android-unanswered-questions.md')
    csv_path = os.path.join(CSV_DIR, f'{ts}-android-unanswered-questions.csv')
    html_path = os.path.join(HTML_DIR, f'{ts}-android-unanswered-questions.html')

    write_markdown(unanswered_df, md_path, report_time, window_start, window_end)
    write_csv(unanswered_df, csv_path, report_time)
    write_html(unanswered_df, html_path, report_time, window_start, window_end,
               'Thunderbird for Android - Unanswered Questions')
    write_index()
    print(f'Written: {md_path}')
    print(f'Written: {csv_path}')
    print(f'Written: {html_path}')


if __name__ == '__main__':
    main()
