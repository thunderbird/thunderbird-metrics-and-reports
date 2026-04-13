#!/usr/bin/env python3
"""
Analyze Missing Emails or Folders issues by subcategory.

This script breaks down Missing Emails or Folders pain points by subcategory
using keyword pattern matching.
"""

import sys
import csv
from pathlib import Path
from collections import defaultdict
import re

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


def load_missing_emails_question_ids(csv_path):
    """Load Missing Emails or Folders question IDs from pain point CSV."""
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('pain_point') == 'Missing Emails or Folders':
                ids_str = row.get('pain_point_ids', '')
                return ids_str.split(';')
    return []


def identify_subcategory(question):
    """Identify the subcategory from question title and content."""
    title = question['title'].lower()
    content = question['content'].lower()
    combined = title + ' ' + content

    # Define subcategory patterns (order matters - check more specific ones first)
    subcategories = [
        # Compact folder related
        {
            'name': 'compact_folder',
            'display_name': 'Compact Folder Related',
            'patterns': ['compact', 'compacting', 'compacted']
        },
        # After update/upgrade
        {
            'name': 'after_update',
            'display_name': 'After Update/Upgrade',
            'patterns': ['after update', 'after upgrade', 'updated to', 'upgraded to',
                        'new version', 'latest version', 'version 128', 'version 115']
        },
        # IMAP sync/folder visibility
        {
            'name': 'imap_sync',
            'display_name': 'IMAP Sync/Folder Visibility',
            'patterns': ['imap', 'folder not showing', 'folders not visible',
                        'can\'t see folder', 'cannot see folder', 'folder missing',
                        'subscribed folder', 'subscribe to folder', 'folder disappeared',
                        'folder not appear']
        },
        # Trash/Deleted folder
        {
            'name': 'trash_deleted',
            'display_name': 'Trash/Deleted Folder Issues',
            'patterns': ['trash', 'deleted items', 'deleted folder', 'recycle bin']
        },
        # Junk/Spam folder
        {
            'name': 'junk_spam',
            'display_name': 'Junk/Spam Folder Issues',
            'patterns': ['junk', 'spam folder', 'junk mail']
        },
        # Archive related
        {
            'name': 'archive',
            'display_name': 'Archive Related',
            'patterns': ['archive', 'archived messages', 'archived emails']
        },
        # Local folders
        {
            'name': 'local_folders',
            'display_name': 'Local Folders',
            'patterns': ['local folder', 'local storage', 'local mail']
        },
        # POP vs IMAP
        {
            'name': 'pop_imap',
            'display_name': 'POP vs IMAP',
            'patterns': ['pop to imap', 'pop3', 'changed to imap', 'switch to imap']
        },
        # Search/Filter issues (emails exist but not visible)
        {
            'name': 'search_filter',
            'display_name': 'Search/Filter Issues',
            'patterns': ['search', 'filter', 'view settings', 'quick filter',
                        'can\'t find', 'cannot find']
        },
        # Emails disappeared/lost (more general than folders)
        {
            'name': 'emails_disappeared',
            'display_name': 'Emails Disappeared/Lost',
            'patterns': ['emails disappeared', 'emails vanished', 'emails gone',
                        'lost emails', 'lost messages', 'messages disappeared',
                        'messages vanished', 'messages gone', 'emails missing',
                        'messages missing', 'deleted accidentally', 'emails deleted']
        },
        # Folder disappeared/missing (specific to folders)
        {
            'name': 'folder_disappeared',
            'display_name': 'Folder Disappeared/Missing',
            'patterns': ['folder gone', 'lost folder', 'folder structure changed',
                        'folders disappeared', 'folders vanished']
        },
        # Other/Unknown
        {
            'name': 'other',
            'display_name': 'Other/Unknown',
            'patterns': []  # Will be used for questions that don't match any subcategory
        }
    ]

    # Check each subcategory
    for subcat in subcategories:
        if subcat['name'] == 'other':
            continue  # Skip the catch-all for now

        for pattern in subcat['patterns']:
            if pattern in combined:
                return subcat['name'], subcat['display_name']

    # If no match, return 'other'
    return 'other', 'Other/Unknown'


def categorize_by_subcategory(questions, missing_ids):
    """Categorize Missing Emails questions by subcategory."""
    subcat_questions = defaultdict(list)
    subcat_display_names = {}

    for qid in missing_ids:
        if qid not in questions:
            continue

        q = questions[qid]
        subcat_name, display_name = identify_subcategory(q)

        subcat_questions[subcat_name].append({
            'qid': qid,
            'title': q['title'],
            'locale': q['locale'],
            'creator': q['creator']
        })
        subcat_display_names[subcat_name] = display_name

    return subcat_questions, subcat_display_names


def write_csv_report(csv_path, subcat_questions, subcat_display_names):
    """Write CSV report sorted by count descending."""
    # Sort subcategories by count
    sorted_subcats = sorted(
        subcat_questions.items(),
        key=lambda x: len(x[1]),
        reverse=True
    )

    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['subcategory', 'num_questions', 'question_ids'])

        for subcat_name, questions in sorted_subcats:
            display_name = subcat_display_names[subcat_name]
            qids = [q['qid'] for q in questions]
            writer.writerow([
                display_name,
                len(qids),
                ';'.join(qids)
            ])


def make_question_link(qid, title):
    """Create a markdown link for a question ID with title as tooltip."""
    # Truncate to 80 chars
    title_truncated = title[:80]
    # Replace characters that cause issues in markdown tables
    title_escaped = title_truncated.replace('"', '\uff02').replace('|', '¦')
    return f'[{qid}](https://support.mozilla.org/questions/{qid} "{title_escaped}")'


def write_markdown_report(md_path, subcat_questions, subcat_display_names, total_missing, year, month, product):
    """Write markdown report sorted by count descending."""
    product_name = "Thunderbird for Android" if product == "android" else "Thunderbird Desktop"
    # Sort subcategories by count
    sorted_subcats = sorted(
        subcat_questions.items(),
        key=lambda x: len(x[1]),
        reverse=True
    )

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f'# {product_name} Missing Emails or Folders by Subcategory - {year:04d}-{month:02d}\n\n')
        f.write(f'**Total Missing Emails or Folders Issues:** {total_missing}\n\n')
        f.write('| Subcategory | Count | % | Sample Question IDs |\n')
        f.write('|-------------|------:|--:|--------------------|\n')

        for subcat_name, questions in sorted_subcats:
            display_name = subcat_display_names[subcat_name]
            count = len(questions)
            percentage = count * 100.0 / total_missing

            # Get first 5 questions as samples
            sample_links = []
            for q in questions[:5]:
                link = make_question_link(q['qid'], q['title'])
                sample_links.append(link)

            sample_str = ', '.join(sample_links)
            if count > 5:
                sample_str += f' ... and {count - 5} more'

            f.write(f'| {display_name} | {count} | {percentage:.1f}% | {sample_str} |\n')


def main():
    if len(sys.argv) == 4:
        product = sys.argv[1]
        year = int(sys.argv[2])
        month = int(sys.argv[3])
    else:
        # Default to March 2026
        product = 'desktop'
        year = 2026
        month = 3

    print(f"Analyzing Missing Emails or Folders by subcategory for {product} {year:04d}-{month:02d}")

    # Load questions
    print("Loading questions...")
    questions = load_questions(product, year, month)
    print(f"  Found {len(questions)} questions")

    # Load Missing Emails or Folders question IDs
    pain_point_csv = Path('REPORTS') / product.upper() / f'{year:04d}-{month:02d}-{product}-top-pain-points.csv'
    print(f"Loading Missing Emails or Folders IDs from {pain_point_csv}")
    missing_ids = load_missing_emails_question_ids(pain_point_csv)
    print(f"  Found {len(missing_ids)} Missing Emails or Folders questions")

    # Categorize by subcategory
    print("Categorizing by subcategory...")
    subcat_questions, subcat_display_names = categorize_by_subcategory(questions, missing_ids)

    print(f"\nBreakdown by subcategory:")
    # Sort for display
    sorted_subcats = sorted(
        subcat_questions.items(),
        key=lambda x: len(x[1]),
        reverse=True
    )
    for subcat_name, questions in sorted_subcats:
        display_name = subcat_display_names[subcat_name]
        count = len(questions)
        percentage = count * 100.0 / len(missing_ids)
        print(f"  {display_name}: {count} ({percentage:.1f}%)")

    # Create reports directory
    reports_dir = Path('REPORTS') / product.upper()
    reports_dir.mkdir(parents=True, exist_ok=True)

    # Write CSV report
    csv_filename = f"{year:04d}-{month:02d}-{product}-missing-emails-subcategories.csv"
    csv_path = reports_dir / csv_filename
    write_csv_report(csv_path, subcat_questions, subcat_display_names)
    print(f"\nWrote CSV report: {csv_path}")

    # Write markdown report
    md_filename = f"{year:04d}-{month:02d}-{product}-missing-emails-subcategories.md"
    md_path = reports_dir / md_filename
    write_markdown_report(md_path, subcat_questions, subcat_display_names, len(missing_ids), year, month, product)
    print(f"Wrote markdown report: {md_path}")


if __name__ == '__main__':
    main()
