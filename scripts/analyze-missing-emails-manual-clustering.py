#!/usr/bin/env python3
"""
Manual/rule-based clustering of Missing Emails or Folders issues.

This script uses enhanced rule-based analysis to categorize questions more accurately.
"""

import sys
import csv
from pathlib import Path
from collections import defaultdict

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


def categorize_question(question):
    """Categorize a single question using enhanced rules."""
    title = question['title'].lower()
    content = question['content'].lower()
    combined = title + ' ' + content

    # Remove HTML tags for better matching
    import re
    combined = re.sub(r'<[^>]+>', ' ', combined)

    # Priority-ordered categories (check specific patterns first)

    # 1. Not actually missing emails/folders (misclassified)
    if any(kw in combined for kw in [
        'grouping', 'thread', 'formatting', 'bold', 'italic',
        'attachment', 'pgp', 'encryption', 'signature',
        'how do i create', 'how to create'
    ]):
        return 'Misclassified (Not Missing Emails/Folders)'

    # 2. All emails disappeared/inbox empty
    if any(phrase in combined for phrase in [
        'all of my emails', 'all my emails', 'all emails have', 'all emails disappeared',
        'all my inbox', 'inbox has disappeared', 'inbox have disappeared',
        'suddenly have no emails', 'everything disappeared', 'everything is gone'
    ]):
        return 'All Emails Disappeared'

    # 3. After update/upgrade
    if any(phrase in combined for phrase in [
        'since last update', 'after update', 'after upgrade', 'after installing',
        'since update', 'since upgrade', 'new version', 'after moving to'
    ]):
        return 'After Update/Upgrade'

    # 4. Compact folder related
    if any(kw in combined for kw in ['compact', 'compacting', 'compacted', 'disk space']):
        return 'Compact Folder Related'

    # 5. Profile issues
    if any(kw in combined for kw in ['profile', 'reinstall', 'new installation']):
        return 'Profile/Installation Issues'

    # 6. Trash/Deleted folder
    if any(kw in combined for kw in ['trash', 'deleted items', 'deleted folder', 'recycle']):
        return 'Trash/Deleted Folder'

    # 7. Junk/Spam folder
    if any(kw in combined for kw in ['junk', 'spam folder']):
        return 'Junk/Spam Folder'

    # 8. Archive
    if any(kw in combined for kw in ['archive', 'archived']):
        return 'Archive Related'

    # 9. Sent folder
    if 'sent' in combined and 'folder' in combined:
        return 'Sent Folder Issues'

    # 10. Draft folder
    if 'draft' in combined:
        return 'Draft Folder Issues'

    # 11. Local folders
    if 'local folder' in combined:
        return 'Local Folders'

    # 12. IMAP sync/folder visibility
    if any(kw in combined for kw in ['imap', 'subscri', 'folder not showing', 'folders not visible',
                                       'can\'t see folder', 'cannot see folder']):
        return 'IMAP Sync/Folder Visibility'

    # 13. POP to IMAP migration
    if 'pop' in combined and 'imap' in combined:
        return 'POP to IMAP Migration'

    # 14. Search/filter/view issues (emails exist but not visible)
    if any(kw in combined for kw in ['search', 'filter', 'view', 'find', 'quick filter']):
        return 'Search/Filter/View Issues'

    # 15. Emails disappeared (general)
    if any(kw in combined for kw in ['disappeared', 'vanished', 'gone', 'missing', 'lost']):
        return 'Emails/Folders Disappeared'

    # 16. Folder structure/organization
    if any(kw in combined for kw in ['folder structure', 'folder hierarchy', 'subfolder']):
        return 'Folder Structure Issues'

    # Default
    return 'Other/Uncategorized'


def categorize_all(questions, missing_ids):
    """Categorize all questions."""
    category_questions = defaultdict(list)

    for qid in missing_ids:
        if qid not in questions:
            continue

        q = questions[qid]
        category = categorize_question(q)

        category_questions[category].append({
            'qid': qid,
            'title': q['title'],
            'locale': q['locale'],
            'creator': q['creator']
        })

    return category_questions


def write_csv_report(csv_path, category_questions):
    """Write CSV report sorted by count descending."""
    sorted_cats = sorted(
        category_questions.items(),
        key=lambda x: len(x[1]),
        reverse=True
    )

    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['category', 'num_questions', 'question_ids'])

        for category, questions in sorted_cats:
            qids = [q['qid'] for q in questions]
            writer.writerow([
                category,
                len(qids),
                ';'.join(qids)
            ])


def make_question_link(qid, title):
    """Create a markdown link for a question ID with title as tooltip."""
    title_truncated = title[:80]
    title_escaped = title_truncated.replace('"', '\uff02').replace('|', '¦')
    return f'[{qid}](https://support.mozilla.org/questions/{qid} "{title_escaped}")'


def write_markdown_report(md_path, category_questions, total_missing, year, month, product):
    """Write markdown report sorted by count descending."""
    product_name = "Thunderbird for Android" if product == "android" else "Thunderbird Desktop"
    sorted_cats = sorted(
        category_questions.items(),
        key=lambda x: len(x[1]),
        reverse=True
    )

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f'# {product_name} Missing Emails or Folders (Enhanced Clustering) - {year:04d}-{month:02d}\n\n')
        f.write(f'**Total Missing Emails or Folders Issues:** {total_missing}\n\n')
        f.write('**Analysis Method:** Enhanced rule-based classification with improved pattern matching.\n\n')
        f.write('| Category | Count | % | Sample Question IDs |\n')
        f.write('|----------|------:|--:|--------------------|\n')

        for category, questions in sorted_cats:
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

            f.write(f'| {category} | {count} | {percentage:.1f}% | {sample_str} |\n')


def main():
    if len(sys.argv) == 4:
        product = sys.argv[1]
        year = int(sys.argv[2])
        month = int(sys.argv[3])
    else:
        product = 'desktop'
        year = 2026
        month = 3

    print(f"Analyzing Missing Emails or Folders with enhanced clustering for {product} {year:04d}-{month:02d}")

    # Load questions
    print("Loading questions...")
    questions = load_questions(product, year, month)
    print(f"  Found {len(questions)} questions")

    # Load Missing Emails or Folders question IDs
    pain_point_csv = Path('REPORTS') / product.upper() / f'{year:04d}-{month:02d}-{product}-top-pain-points.csv'
    print(f"Loading Missing Emails or Folders IDs from {pain_point_csv}")
    missing_ids = load_missing_emails_question_ids(pain_point_csv)
    print(f"  Found {len(missing_ids)} Missing Emails or Folders questions")

    # Categorize
    print("Categorizing with enhanced rules...")
    category_questions = categorize_all(questions, missing_ids)

    print(f"\nBreakdown by category:")
    sorted_cats = sorted(
        category_questions.items(),
        key=lambda x: len(x[1]),
        reverse=True
    )
    for category, questions in sorted_cats:
        count = len(questions)
        percentage = count * 100.0 / len(missing_ids)
        print(f"  {category}: {count} ({percentage:.1f}%)")

    # Create reports directory
    reports_dir = Path('REPORTS') / product.upper()
    reports_dir.mkdir(parents=True, exist_ok=True)

    # Write CSV report
    csv_filename = f"{year:04d}-{month:02d}-{product}-missing-emails-enhanced-clustering.csv"
    csv_path = reports_dir / csv_filename
    write_csv_report(csv_path, category_questions)
    print(f"\nWrote CSV report: {csv_path}")

    # Write markdown report
    md_filename = f"{year:04d}-{month:02d}-{product}-missing-emails-enhanced-clustering.md"
    md_path = reports_dir / md_filename
    write_markdown_report(md_path, category_questions, len(missing_ids), year, month, product)
    print(f"Wrote markdown report: {md_path}")


if __name__ == '__main__':
    main()
