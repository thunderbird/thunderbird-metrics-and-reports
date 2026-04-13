#!/usr/bin/env python3
"""
Create a Top 3 User Pain Point Report from Thunderbird Support Forum data.

This script analyzes questions and answers to identify the top user pain points
that make it hard for non-power users to read, write, compose, and send email.

Usage:
    create-pain-point-report.py <product> YYYY MM

Outputs:
    - REPORTS/<product>/YYYY-MM-<product>-top-pain-points.csv
    - REPORTS/<product>/YYYY-MM-<product>-top-pain-points.md
"""

import sys
import csv
from pathlib import Path
from collections import defaultdict, Counter
import re

# Increase CSV field size limit
csv.field_size_limit(sys.maxsize)


def load_trusted_contributors(product):
    """Load trusted contributors from CSV file."""
    path = Path('CONCATENATED_FILES') / product.upper() / f'thunderbird-{product}-trusted-contributors.csv'
    trusted = set()

    if not path.exists():
        print(f"Warning: Trusted contributors file not found: {path}")
        return trusted

    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            creator = row.get('creator', '').strip()
            if creator:
                trusted.add(creator)

    return trusted


def is_english(locale):
    """Check if locale is English."""
    if not locale:
        return False
    return locale.startswith('en')


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
            locale = row.get('locale', '')

            # Only include English questions
            if qid and is_english(locale):
                questions[qid] = {
                    'title': row.get('title', '') or '',
                    'content': row.get('content', '') or '',
                    'creator': row.get('creator', '') or '',
                    'tags': row.get('tags', '') or '',
                    'locale': locale
                }

    return questions


def load_answers(product, year, month, questions, trusted_contributors):
    """Load answers from CSV file, filtered by creator or trusted contributors."""
    path = Path('CONCATENATED_FILES') / product.upper() / f'{year:04d}-{month:02d}-sumo-{product}-answers.csv'

    if not path.exists():
        print(f"Error: Answers file not found: {path}")
        sys.exit(1)

    answers_by_question = defaultdict(list)

    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid = row.get('question_id')
            creator = row.get('creator', '') or ''
            content = row.get('content', '') or ''

            # Only include answers for English questions
            if qid not in questions:
                continue

            question_creator = questions[qid]['creator']

            # Only include answers from question creator or trusted contributors
            if creator == question_creator or creator in trusted_contributors:
                answers_by_question[qid].append({
                    'creator': creator,
                    'content': content
                })

    return answers_by_question


def categorize_pain_points(questions, answers_by_question):
    """
    Analyze questions and answers to categorize pain points.

    Returns a dict mapping pain point category to list of question IDs.
    """
    pain_points = defaultdict(list)

    # Define pain point categories based on common issues
    categories = {
        'oauth_authentication': {
            'keywords': ['oauth', 'authentication', 'login', 'password', 'sign in', 'yahoo', 'aol', 'gmail', 'google'],
            'title': 'OAuth/Authentication Issues'
        },
        'cannot_send_receive': {
            'keywords': ['cannot send', 'can\'t send', 'not sending', 'cannot receive', 'can\'t receive', 'not receiving', 'smtp', 'imap', 'pop'],
            'title': 'Cannot Send/Receive Emails'
        },
        'email_setup_configuration': {
            'keywords': ['setup', 'configure', 'add account', 'new account', 'server settings', 'connection'],
            'title': 'Email Account Setup/Configuration'
        },
        'missing_emails_folders': {
            'keywords': ['missing', 'disappeared', 'lost', 'deleted', 'folders', 'messages gone'],
            'title': 'Missing Emails or Folders'
        },
        'calendar_issues': {
            'keywords': ['calendar', 'appointment', 'event', 'google calendar'],
            'title': 'Calendar/Events Issues'
        },
        'performance_crashes': {
            'keywords': ['slow', 'freeze', 'crash', 'hang', 'not responding', 'loading'],
            'title': 'Performance/Crashes'
        },
        'upgrade_update_issues': {
            'keywords': ['update', 'upgrade', 'version', 'after update', 'latest version'],
            'title': 'Update/Upgrade Issues'
        }
    }

    for qid, question in questions.items():
        title = question['title'].lower()
        content = question['content'].lower()
        combined_text = title + ' ' + content

        # Also include answer text if available
        if qid in answers_by_question:
            for answer in answers_by_question[qid]:
                combined_text += ' ' + answer['content'].lower()

        # Categorize based on keywords
        matched = False
        for category, info in categories.items():
            for keyword in info['keywords']:
                if keyword in combined_text:
                    pain_points[category].append(qid)
                    matched = True
                    break
            if matched:
                break

    # Convert to dict with category info
    result = {}
    for category, qids in pain_points.items():
        if qids:  # Only include categories with questions
            result[category] = {
                'title': categories[category]['title'],
                'qids': list(set(qids))  # Remove duplicates
            }

    return result


def get_top_3_pain_points(pain_points):
    """Get top 3 pain points by count."""
    sorted_pain_points = sorted(
        pain_points.items(),
        key=lambda x: len(x[1]['qids']),
        reverse=True
    )

    return sorted_pain_points[:3]


def write_csv_report(csv_path, top_pain_points):
    """Write CSV report."""
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['pain_point', 'num_with_this_pain_point', 'pain_point_ids'])

        for category, info in top_pain_points:
            qids = info['qids']
            writer.writerow([
                info['title'],
                len(qids),
                ';'.join(qids)
            ])


def make_question_link(qid, questions):
    """Create a markdown link for a question ID with title as tooltip."""
    title = questions.get(qid, {}).get('title', '') or ''
    # Truncate to 80 chars
    title_truncated = title[:80]
    # Replace characters that cause issues in markdown tables
    title_escaped = title_truncated.replace('"', '\uff02').replace('|', '¦')
    return f'[{qid}](https://support.mozilla.org/questions/{qid} "{title_escaped}")'


def write_markdown_report(md_path, top_pain_points, questions, year, month, product):
    """Write markdown report."""
    product_name = "Thunderbird for Android" if product == "android" else "Thunderbird Desktop"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f'# {product_name} Top 3 User Pain Points - {year:04d}-{month:02d}\n\n')
        f.write('| Pain Point | Count | Question IDs |\n')
        f.write('|------------|------:|-------------|\n')

        for category, info in top_pain_points:
            title = info['title']
            qids = info['qids']
            count = len(qids)

            # Create linked question IDs
            linked_ids = ', '.join([make_question_link(qid, questions) for qid in qids[:10]])
            if len(qids) > 10:
                linked_ids += f' ... and {len(qids) - 10} more'

            f.write(f'| {title} | {count} | {linked_ids} |\n')


def main():
    if len(sys.argv) != 4:
        print("Usage: create-pain-point-report.py <product> YYYY MM")
        sys.exit(1)

    product = sys.argv[1]
    year = int(sys.argv[2])
    month = int(sys.argv[3])

    print(f"Creating pain point report for {product} {year:04d}-{month:02d}")

    # Load trusted contributors
    print("Loading trusted contributors...")
    trusted_contributors = load_trusted_contributors(product)
    print(f"  Found {len(trusted_contributors)} trusted contributors")

    # Load questions (English only)
    print("Loading questions...")
    questions = load_questions(product, year, month)
    print(f"  Found {len(questions)} English questions")

    # Load answers (from question creator or trusted contributors)
    print("Loading answers...")
    answers_by_question = load_answers(product, year, month, questions, trusted_contributors)
    print(f"  Found answers for {len(answers_by_question)} questions")

    # Categorize pain points
    print("Analyzing pain points...")
    pain_points = categorize_pain_points(questions, answers_by_question)
    print(f"  Identified {len(pain_points)} pain point categories")

    # Get top 3
    top_3 = get_top_3_pain_points(pain_points)

    print("\nTop 3 Pain Points:")
    for i, (category, info) in enumerate(top_3, 1):
        print(f"  {i}. {info['title']}: {len(info['qids'])} questions")

    # Create reports directory
    reports_dir = Path('REPORTS') / product.upper()
    reports_dir.mkdir(parents=True, exist_ok=True)

    # Write CSV report
    csv_filename = f"{year:04d}-{month:02d}-{product}-top-pain-points.csv"
    csv_path = reports_dir / csv_filename
    write_csv_report(csv_path, top_3)
    print(f"\nWrote CSV report: {csv_path}")

    # Write markdown report
    md_filename = f"{year:04d}-{month:02d}-{product}-top-pain-points.md"
    md_path = reports_dir / md_filename
    write_markdown_report(md_path, top_3, questions, year, month, product)
    print(f"Wrote markdown report: {md_path}")


if __name__ == '__main__':
    main()
