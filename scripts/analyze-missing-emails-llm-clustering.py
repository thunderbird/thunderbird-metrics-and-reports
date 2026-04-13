#!/usr/bin/env python3
"""
Analyze Missing Emails or Folders issues using LLM-based clustering.

This script uses Claude AI to read and categorize each question intelligently.
Requires ANTHROPIC_API_KEY environment variable.
"""

import sys
import csv
import os
import json
from pathlib import Path
from collections import defaultdict
from anthropic import Anthropic

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


CATEGORIES = [
    "IMAP Sync/Folder Visibility - folders not syncing, not showing up, subscription issues",
    "Emails Disappeared/Lost - emails vanished, deleted unexpectedly, lost messages",
    "Folder Disappeared/Missing - entire folders gone, folder structure issues",
    "After Update/Upgrade - issues appearing after Thunderbird update or version change",
    "Trash/Deleted Items Folder - problems with trash or deleted items folder",
    "Compact Folder Related - emails lost during compacting or corruption from compacting",
    "Search Not Finding Emails - search or filter problems preventing finding existing emails",
    "Local Folders Issues - local folder specific problems",
    "Junk/Spam Folder - junk or spam folder visibility or sync issues",
    "Archive Issues - archiving problems or finding archived messages",
    "POP vs IMAP Migration - issues when switching between POP and IMAP",
    "Profile/Data Corruption - profile corruption causing missing data",
    "Other/Unknown - doesn't clearly fit the above categories"
]


def categorize_with_llm(client, questions_batch):
    """Use Claude to categorize a batch of questions."""

    # Build the prompt
    questions_text = ""
    for i, (qid, q) in enumerate(questions_batch, 1):
        questions_text += f"\n\n--- Question {i} (ID: {qid}) ---\n"
        questions_text += f"Title: {q['title']}\n"
        questions_text += f"Content: {q['content'][:1000]}"  # Limit content to avoid token limits

    categories_text = "\n".join([f"{i+1}. {cat}" for i, cat in enumerate(CATEGORIES)])

    prompt = f"""I need you to categorize Thunderbird support questions about missing emails or folders.

Categories:
{categories_text}

Please analyze each question below and assign it to the MOST APPROPRIATE category.
Return your response as a JSON array with one object per question, each containing:
- "question_id": the question ID
- "category_number": the category number (1-{len(CATEGORIES)})
- "reasoning": brief explanation of why this category was chosen

Questions:
{questions_text}

Return ONLY the JSON array, no other text."""

    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4096,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        response_text = message.content[0].text
        # Parse JSON response
        categorizations = json.loads(response_text)
        return categorizations
    except Exception as e:
        print(f"Error calling Claude API: {e}")
        return []


def categorize_all_questions(questions, missing_ids):
    """Categorize all questions using LLM in batches."""
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    client = Anthropic(api_key=api_key)

    # Prepare questions
    questions_to_categorize = []
    for qid in missing_ids:
        if qid in questions:
            questions_to_categorize.append((qid, questions[qid]))

    # Process in batches of 10
    batch_size = 10
    all_categorizations = {}

    for i in range(0, len(questions_to_categorize), batch_size):
        batch = questions_to_categorize[i:i+batch_size]
        print(f"Processing questions {i+1} to {min(i+batch_size, len(questions_to_categorize))} of {len(questions_to_categorize)}...")

        categorizations = categorize_with_llm(client, batch)

        for cat in categorizations:
            qid = cat.get('question_id')
            cat_num = cat.get('category_number', 13)  # Default to "Other"
            reasoning = cat.get('reasoning', '')

            # Get category name
            if 1 <= cat_num <= len(CATEGORIES):
                category_full = CATEGORIES[cat_num - 1]
                category_name = category_full.split(' - ')[0]
            else:
                category_name = "Other/Unknown"

            all_categorizations[qid] = {
                'category': category_name,
                'reasoning': reasoning
            }

    return all_categorizations


def organize_by_category(questions, missing_ids, categorizations):
    """Organize questions by their assigned category."""
    category_questions = defaultdict(list)

    for qid in missing_ids:
        if qid not in questions:
            continue

        q = questions[qid]
        cat_info = categorizations.get(qid, {'category': 'Other/Unknown', 'reasoning': ''})
        category = cat_info['category']

        category_questions[category].append({
            'qid': qid,
            'title': q['title'],
            'locale': q['locale'],
            'creator': q['creator'],
            'reasoning': cat_info['reasoning']
        })

    return category_questions


def write_csv_report(csv_path, category_questions):
    """Write CSV report sorted by count descending."""
    # Sort categories by count
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
    # Truncate to 80 chars
    title_truncated = title[:80]
    # Replace characters that cause issues in markdown tables
    title_escaped = title_truncated.replace('"', '\uff02').replace('|', '¦')
    return f'[{qid}](https://support.mozilla.org/questions/{qid} "{title_escaped}")'


def write_markdown_report(md_path, category_questions, total_missing, year, month, product):
    """Write markdown report sorted by count descending."""
    product_name = "Thunderbird for Android" if product == "android" else "Thunderbird Desktop"
    # Sort categories by count
    sorted_cats = sorted(
        category_questions.items(),
        key=lambda x: len(x[1]),
        reverse=True
    )

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f'# {product_name} Missing Emails or Folders (LLM Clustering) - {year:04d}-{month:02d}\n\n')
        f.write(f'**Total Missing Emails or Folders Issues:** {total_missing}\n\n')
        f.write('**Analysis Method:** Claude AI analyzed each question to determine the most appropriate category.\n\n')
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
        # Default to March 2026
        product = 'desktop'
        year = 2026
        month = 3

    print(f"Analyzing Missing Emails or Folders using LLM clustering for {product} {year:04d}-{month:02d}")

    # Load questions
    print("Loading questions...")
    questions = load_questions(product, year, month)
    print(f"  Found {len(questions)} questions")

    # Load Missing Emails or Folders question IDs
    pain_point_csv = Path('REPORTS') / product.upper() / f'{year:04d}-{month:02d}-{product}-top-pain-points.csv'
    print(f"Loading Missing Emails or Folders IDs from {pain_point_csv}")
    missing_ids = load_missing_emails_question_ids(pain_point_csv)
    print(f"  Found {len(missing_ids)} Missing Emails or Folders questions")

    # Categorize using LLM
    print("\nCategorizing with Claude AI (this may take a while)...")
    categorizations = categorize_all_questions(questions, missing_ids)

    # Organize by category
    print("\nOrganizing by category...")
    category_questions = organize_by_category(questions, missing_ids, categorizations)

    print(f"\nBreakdown by category:")
    # Sort for display
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
    csv_filename = f"{year:04d}-{month:02d}-{product}-missing-emails-llm-clustering.csv"
    csv_path = reports_dir / csv_filename
    write_csv_report(csv_path, category_questions)
    print(f"\nWrote CSV report: {csv_path}")

    # Write markdown report
    md_filename = f"{year:04d}-{month:02d}-{product}-missing-emails-llm-clustering.md"
    md_path = reports_dir / md_filename
    write_markdown_report(md_path, category_questions, len(missing_ids), year, month, product)
    print(f"Wrote markdown report: {md_path}")


if __name__ == '__main__':
    main()
