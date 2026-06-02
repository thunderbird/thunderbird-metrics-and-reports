#!/usr/bin/env python3
"""
Report Thunderbird desktop questions not answered by non-creators in 72+ hours.

Usage (no args = use current UTC time):
    uv run scripts/sumo-tb-desktop-questions-not-answered-report.py

Usage with explicit date/time:
    uv run scripts/sumo-tb-desktop-questions-not-answered-report.py YEAR MONTH DAY HOUR
    e.g. uv run scripts/sumo-tb-desktop-questions-not-answered-report.py 2026 4 2 22
"""
import sys
import os
import csv
import re
import html
from datetime import datetime, timezone, timedelta
import pandas as pd

csv.field_size_limit(sys.maxsize)

DATA_DIR = 'aaq-data'
MARKDOWN_DIR = 'UNANSWERED_QUESTIONS/MARKDOWN_REPORTS'
CSV_DIR = 'UNANSWERED_QUESTIONS/CSV_REPORTS'
WINDOW_HOURS = 72
WINDOW_DAYS = 14
Q_SUFFIX = 'thunderbird-creator-answers-desktop-all-locales.csv'
A_SUFFIX = 'thunderbird-answers-for-questions-desktop.csv'


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
    if pd.isna(meta) or not str(meta).strip():
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
    delta = pd.Timestamp(report_time) - created_utc
    total_hours = int(delta.total_seconds()) // 3600
    days, hours = divmod(total_hours, 24)
    if days > 0:
        return f'{days}d {hours}h'
    return f'{hours}h'


def write_markdown(df, path, report_time, window_start, window_end):
    lines = [
        '# Thunderbird Desktop - Unanswered Questions',
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
        elapsed = format_elapsed(q['created_utc'], report_time)
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
                'elapsed': format_elapsed(q['created_utc'], report_time),
                'creator': creator,
                'creator_url': f'https://support.mozilla.org/en-US/user/{creator}/',
                'version': version,
                'os': os_str,
                'question_id': qid,
                'question_url': f'https://support.mozilla.org/questions/{qid}',
                'question_title': title,
                'question_content': content,
            })


def main():
    year, month, day, hour = parse_args()
    report_time = datetime(year, month, day, hour, 0, 0, tzinfo=timezone.utc)
    window_end = report_time - timedelta(hours=WINDOW_HOURS)
    window_start = report_time - timedelta(days=WINDOW_DAYS)

    print(f'Report time: {report_time.strftime("%Y-%m-%d %H:%M")} UTC')
    print(f'Window: {window_start.strftime("%Y-%m-%d %H:%M")} UTC '
          f'to {window_end.strftime("%Y-%m-%d %H:%M")} UTC')

    # Question files: window_start to window_end (extra day buffer each side)
    q_files = daily_files_in_range(
        window_start - timedelta(days=1),
        window_end + timedelta(days=1),
        Q_SUFFIX,
    )
    # Answer files: window_start to report_time (catch all answers received)
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

    # Build map: question_id -> set of answer creators (non-spam only)
    answer_creators: dict[int, set] = {}
    if not a_df.empty:
        if 'is_spam' in a_df.columns:
            a_df = a_df[a_df['is_spam'].astype(str).str.lower() != 'true']
        a_df = a_df.drop_duplicates(subset='id', keep='last')
        for _, ans in a_df.iterrows():
            qid = ans['question_id']
            ans_creator = str(ans['creator']) if pd.notna(ans.get('creator')) else ''
            answer_creators.setdefault(qid, set()).add(ans_creator)

    unanswered = []
    for _, q in q_df.iterrows():
        qid = q['id']
        q_creator = str(q['creator']) if pd.notna(q.get('creator')) else ''
        answerers = answer_creators.get(qid, set())
        non_creator_answerers = answerers - {q_creator}
        if not non_creator_answerers:
            unanswered.append(q)

    if unanswered:
        unanswered_df = pd.DataFrame(unanswered).sort_values('created_utc')
    else:
        unanswered_df = pd.DataFrame()

    print(f'Unanswered questions: {len(unanswered_df)}')

    os.makedirs(MARKDOWN_DIR, exist_ok=True)
    os.makedirs(CSV_DIR, exist_ok=True)

    ts = f'{year}-{month:02d}-{day:02d}'
    md_path = os.path.join(MARKDOWN_DIR, f'{ts}-desktop-unanswered-questions.md')
    csv_path = os.path.join(CSV_DIR, f'{ts}-desktop-unanswered-questions.csv')

    write_markdown(unanswered_df, md_path, report_time, window_start, window_end)
    write_csv(unanswered_df, csv_path, report_time)
    print(f'Written: {md_path}')
    print(f'Written: {csv_path}')


if __name__ == '__main__':
    main()
