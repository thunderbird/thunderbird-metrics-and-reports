#!/usr/bin/env python3
"""
Analyze OAuth/Authentication issues by email provider.

This script breaks down OAuth/Authentication pain points by email provider.
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


def load_oauth_question_ids(csv_path):
    """Load OAuth/Authentication question IDs from pain point CSV."""
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('pain_point') == 'OAuth/Authentication Issues':
                ids_str = row.get('pain_point_ids', '')
                return ids_str.split(';')
    return []


def identify_email_provider(question):
    """Identify the email provider from question title and content."""
    title = question['title'].lower()
    content = question['content'].lower()
    combined = title + ' ' + content

    # Define provider patterns (order matters - check more specific ones first)
    providers = [
        # Microsoft hosted
        {
            'name': 'microsoft_hosted_email',
            'display_name': 'Microsoft Hosted Email (Hotmail/Outlook/Office365)',
            'patterns': ['hotmail', 'outlook', 'office365', 'office 365', 'live.com', 'msn.com']
        },
        # Yahoo hosted
        {
            'name': 'yahoo_hosted_email',
            'display_name': 'Yahoo Hosted Email (Yahoo/AOL/AT&T)',
            'patterns': ['yahoo', 'ymail', 'aol', 'att.net', 'sbcglobal', 'bellsouth.net']
        },
        # Gmail/Google
        {
            'name': 'gmail',
            'display_name': 'Gmail/Google',
            'patterns': ['gmail', 'google mail', 'googlemail', 'google workspace']
        },
        # GMX
        {
            'name': 'gmx',
            'display_name': 'GMX',
            'patterns': ['gmx.com', 'gmx.net', 'gmx.de', ' gmx']
        },
        # Proton
        {
            'name': 'protonmail',
            'display_name': 'ProtonMail',
            'patterns': ['proton', 'protonmail']
        },
        # Apple
        {
            'name': 'apple_email',
            'display_name': 'Apple Email (iCloud/me.com)',
            'patterns': ['icloud', 'me.com', 'mac.com', 'apple mail']
        },
        # Fastmail
        {
            'name': 'fastmail',
            'display_name': 'Fastmail',
            'patterns': ['fastmail']
        },
        # Mailfence
        {
            'name': 'mailfence',
            'display_name': 'Mailfence',
            'patterns': ['mailfence']
        },
        # Comcast/Xfinity
        {
            'name': 'comcast',
            'display_name': 'Comcast/Xfinity',
            'patterns': ['comcast', 'xfinity']
        },
        # T-Online (German)
        {
            'name': 't-online',
            'display_name': 'T-Online',
            'patterns': ['t-online']
        },
        # Mail.com
        {
            'name': 'mail_com',
            'display_name': 'Mail.com',
            'patterns': ['mail.com']
        },
        # Generic IMAP/SMTP (catch general server issues)
        {
            'name': 'other',
            'display_name': 'Other/Unknown Provider',
            'patterns': []  # Will be used for questions that don't match any provider
        }
    ]

    # Check each provider
    for provider in providers:
        if provider['name'] == 'other':
            continue  # Skip the catch-all for now

        for pattern in provider['patterns']:
            if pattern in combined:
                return provider['name'], provider['display_name']

    # If no match, return 'other'
    return 'other', 'Other/Unknown Provider'


def categorize_by_provider(questions, oauth_ids):
    """Categorize OAuth questions by email provider."""
    provider_questions = defaultdict(list)
    provider_display_names = {}

    for qid in oauth_ids:
        if qid not in questions:
            continue

        q = questions[qid]
        provider_name, display_name = identify_email_provider(q)

        provider_questions[provider_name].append({
            'qid': qid,
            'title': q['title'],
            'locale': q['locale'],
            'creator': q['creator']
        })
        provider_display_names[provider_name] = display_name

    return provider_questions, provider_display_names


def write_csv_report(csv_path, provider_questions, provider_display_names):
    """Write CSV report sorted by count descending."""
    # Sort providers by count
    sorted_providers = sorted(
        provider_questions.items(),
        key=lambda x: len(x[1]),
        reverse=True
    )

    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['provider', 'num_questions', 'question_ids'])

        for provider_name, questions in sorted_providers:
            display_name = provider_display_names[provider_name]
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


def write_markdown_report(md_path, provider_questions, provider_display_names, total_oauth, year, month, product):
    """Write markdown report sorted by count descending."""
    product_name = "Thunderbird for Android" if product == "android" else "Thunderbird Desktop"
    # Sort providers by count
    sorted_providers = sorted(
        provider_questions.items(),
        key=lambda x: len(x[1]),
        reverse=True
    )

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f'# {product_name} OAuth/Authentication Issues by Email Provider - {year:04d}-{month:02d}\n\n')
        f.write(f'**Total OAuth/Authentication Issues:** {total_oauth}\n\n')
        f.write('| Provider | Count | % | Sample Question IDs |\n')
        f.write('|----------|------:|--:|--------------------|\n')

        for provider_name, questions in sorted_providers:
            display_name = provider_display_names[provider_name]
            count = len(questions)
            percentage = count * 100.0 / total_oauth

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

    print(f"Analyzing OAuth issues by provider for {product} {year:04d}-{month:02d}")

    # Load questions
    print("Loading questions...")
    questions = load_questions(product, year, month)
    print(f"  Found {len(questions)} questions")

    # Load OAuth/Authentication question IDs
    pain_point_csv = Path('REPORTS') / product.upper() / f'{year:04d}-{month:02d}-{product}-top-pain-points.csv'
    print(f"Loading OAuth/Authentication IDs from {pain_point_csv}")
    oauth_ids = load_oauth_question_ids(pain_point_csv)
    print(f"  Found {len(oauth_ids)} OAuth/Authentication questions")

    # Categorize by provider
    print("Categorizing by email provider...")
    provider_questions, provider_display_names = categorize_by_provider(questions, oauth_ids)

    print(f"\nBreakdown by provider:")
    # Sort for display
    sorted_providers = sorted(
        provider_questions.items(),
        key=lambda x: len(x[1]),
        reverse=True
    )
    for provider_name, questions in sorted_providers:
        display_name = provider_display_names[provider_name]
        count = len(questions)
        percentage = count * 100.0 / len(oauth_ids)
        print(f"  {display_name}: {count} ({percentage:.1f}%)")

    # Create reports directory
    reports_dir = Path('REPORTS') / product.upper()
    reports_dir.mkdir(parents=True, exist_ok=True)

    # Write CSV report
    csv_filename = f"{year:04d}-{month:02d}-{product}-oauth-by-provider.csv"
    csv_path = reports_dir / csv_filename
    write_csv_report(csv_path, provider_questions, provider_display_names)
    print(f"\nWrote CSV report: {csv_path}")

    # Write markdown report
    md_filename = f"{year:04d}-{month:02d}-{product}-oauth-by-provider.md"
    md_path = reports_dir / md_filename
    write_markdown_report(md_path, provider_questions, provider_display_names, len(oauth_ids), year, month, product)
    print(f"Wrote markdown report: {md_path}")


if __name__ == '__main__':
    main()
