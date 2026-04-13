#!/usr/bin/env python3
"""
Analyze GMX-related OAuth/Authentication issues from the pain point report.

This script identifies GMX-related questions within the OAuth/Authentication pain point.
"""

import sys
import csv
from pathlib import Path

# Increase CSV field size limit
csv.field_size_limit(sys.maxsize)


def load_questions(product, year, month):
    """Load questions from CSV file."""
    path = Path('CONCATENATED_FILES') / product.upper() / f'{year:04d}-{month:02d}-sumo-{product}-questions.csv'

    if not path.exists():
        print(f"Error: Questions file not found: {path}")
        sys.exit(1)

    questions = {}
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid = row.get('id')
            if qid:
                questions[qid] = {
                    'title': row.get('title', '') or '',
                    'content': row.get('content', '') or '',
                    'creator': row.get('creator', '') or '',
                    'tags': row.get('tags', '') or '',
                    'locale': row.get('locale', '') or ''
                }

    return questions


def load_oauth_question_ids(csv_path):
    """Load OAuth/Authentication question IDs from pain point CSV."""
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('pain_point') == 'OAuth/Authentication Issues':
                ids_str = row.get('pain_point_ids', '')
                return ids_str.split(';')
    return []


def find_gmx_questions(questions, oauth_ids):
    """Find GMX-related questions within OAuth/Authentication issues."""
    gmx_questions = []

    for qid in oauth_ids:
        if qid not in questions:
            continue

        q = questions[qid]
        title = q['title'].lower()
        content = q['content'].lower()
        combined = title + ' ' + content

        # Check for GMX mentions
        if 'gmx' in combined:
            gmx_questions.append({
                'qid': qid,
                'title': q['title'],
                'content': q['content'],
                'creator': q['creator'],
                'locale': q['locale']
            })

    return gmx_questions


def write_csv_report(csv_path, gmx_questions):
    """Write CSV report for GMX questions."""
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['question_id', 'title', 'locale', 'creator'])

        for q in gmx_questions:
            writer.writerow([
                q['qid'],
                q['title'],
                q['locale'],
                q['creator']
            ])


def make_question_link(qid, title):
    """Create a markdown link for a question ID with title as tooltip."""
    # Truncate to 80 chars
    title_truncated = title[:80]
    # Replace characters that cause issues in markdown tables
    title_escaped = title_truncated.replace('"', '\uff02').replace('|', '¦')
    return f'[{qid}](https://support.mozilla.org/questions/{qid} "{title_escaped}")'


def write_markdown_report(md_path, gmx_questions, total_oauth, year, month):
    """Write markdown report for GMX questions."""
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f'# GMX OAuth/Authentication Issues - {year:04d}-{month:02d}\n\n')
        f.write(f'**Total OAuth/Authentication Issues:** {total_oauth}\n\n')
        f.write(f'**GMX-related issues:** {len(gmx_questions)} ({len(gmx_questions)*100.0/total_oauth:.1f}%)\n\n')
        f.write('| Question ID | Title | Locale | Creator |\n')
        f.write('|-------------|-------|--------|--------|\n')

        for q in gmx_questions:
            link = make_question_link(q['qid'], q['title'])
            title = q['title'][:60] + ('...' if len(q['title']) > 60 else '')
            f.write(f'| {link} | {title} | {q["locale"]} | {q["creator"]} |\n')


def main():
    product = 'desktop'
    year = 2026
    month = 3

    print(f"Analyzing GMX OAuth issues for {product} {year:04d}-{month:02d}")

    # Load questions
    print("Loading questions...")
    questions = load_questions(product, year, month)
    print(f"  Found {len(questions)} questions")

    # Load OAuth/Authentication question IDs
    pain_point_csv = Path('REPORTS') / product.upper() / f'{year:04d}-{month:02d}-{product}-top-pain-points.csv'
    print(f"Loading OAuth/Authentication IDs from {pain_point_csv}")
    oauth_ids = load_oauth_question_ids(pain_point_csv)
    print(f"  Found {len(oauth_ids)} OAuth/Authentication questions")

    # Find GMX questions
    print("Searching for GMX mentions...")
    gmx_questions = find_gmx_questions(questions, oauth_ids)
    print(f"  Found {len(gmx_questions)} GMX-related questions ({len(gmx_questions)*100.0/len(oauth_ids):.1f}%)")

    # Create reports directory
    reports_dir = Path('REPORTS') / product.upper()
    reports_dir.mkdir(parents=True, exist_ok=True)

    # Write CSV report
    csv_filename = f"{year:04d}-{month:02d}-{product}-gmx-oauth-issues.csv"
    csv_path = reports_dir / csv_filename
    write_csv_report(csv_path, gmx_questions)
    print(f"\nWrote CSV report: {csv_path}")

    # Write markdown report
    md_filename = f"{year:04d}-{month:02d}-{product}-gmx-oauth-issues.md"
    md_path = reports_dir / md_filename
    write_markdown_report(md_path, gmx_questions, len(oauth_ids), year, month)
    print(f"Wrote markdown report: {md_path}")


if __name__ == '__main__':
    main()
