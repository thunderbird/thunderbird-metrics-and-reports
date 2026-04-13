#!/usr/bin/env python3
"""
Create a monthly forum question summary report.

This script analyzes SUMO questions and generates summaries using Claude AI.
Requires ANTHROPIC_API_KEY environment variable.
"""

import sys
import csv
import os
import json
import re
from pathlib import Path
from anthropic import Anthropic

# Increase CSV field size limit
csv.field_size_limit(sys.maxsize)


def load_questions(product, year, month):
    """Load questions from CSV file, filtering out spam."""
    path = Path('CONCATENATED_FILES') / product.upper() / f'{year:04d}-{month:02d}-sumo-{product}-questions.csv'

    if not path.exists():
        print(f"Error: Questions file not found: {path}")
        sys.exit(1)

    questions = []
    spam_count = 0

    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid = row.get('id')
            is_spam = row.get('is_spam', 'False').strip().lower() == 'true'

            if is_spam:
                spam_count += 1
                continue

            if qid:
                # Remove HTML tags
                content = row.get('content', '')
                content_clean = re.sub(r'<[^>]+>', ' ', content)
                content_clean = re.sub(r'\s+', ' ', content_clean).strip()

                questions.append({
                    'id': qid,
                    'title': row.get('title', ''),
                    'title_truncated': row.get('title', '')[:80],
                    'content': content_clean
                })

    print(f"Loaded {len(questions)} non-spam questions ({spam_count} spam filtered out)")
    return questions


def summarize_with_llm(client, questions_batch):
    """Use Claude to summarize a batch of questions."""

    # Build the prompt
    questions_text = ""
    for i, q in enumerate(questions_batch, 1):
        questions_text += f"\n\n--- Question {i} (ID: {q['id']}) ---\n"
        questions_text += f"Title: {q['title']}\n"
        questions_text += f"Content: {q['content'][:800]}"  # Limit to avoid token limits

    prompt = f"""I need you to create concise summaries for Thunderbird support questions.

For each question below, provide a 1-2 sentence summary that explains:
- What the user's issue or request is
- Key details (error messages, specific features, symptoms)

Be concise and factual. Return your response as a JSON array with one object per question, each containing:
- "question_id": the question ID
- "summary": the summary (1-2 sentences)

Questions:
{questions_text}

Return ONLY the JSON array, no other text."""

    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=8192,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        response_text = message.content[0].text
        # Parse JSON response
        summaries = json.loads(response_text)
        return summaries
    except Exception as e:
        print(f"Error calling Claude API: {e}")
        return []


def generate_summaries(questions):
    """Generate summaries for all questions using Claude API."""
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        print("Please set it with: export ANTHROPIC_API_KEY=your_key_here")
        sys.exit(1)

    client = Anthropic(api_key=api_key)

    # Process in batches of 10
    batch_size = 10
    all_summaries = {}

    for i in range(0, len(questions), batch_size):
        batch = questions[i:i+batch_size]
        print(f"Processing questions {i+1} to {min(i+batch_size, len(questions))} of {len(questions)}...")

        summaries = summarize_with_llm(client, batch)

        for summary_obj in summaries:
            qid = summary_obj.get('question_id')
            summary = summary_obj.get('summary', '')
            all_summaries[qid] = summary

    return all_summaries


def make_question_link(qid, title):
    """Create a markdown link for a question ID with title as tooltip."""
    # Truncate to 80 chars
    title_truncated = title[:80]
    # Replace characters that cause issues in markdown tables
    title_escaped = title_truncated.replace('"', '\uff02').replace('|', '¦')
    return f'[{qid}](https://support.mozilla.org/questions/{qid} "{title_escaped}")'


def write_csv_report(csv_path, questions, summaries):
    """Write CSV report."""
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'title', 'LLM_Summary', 'Analyst_notes'])

        for q in questions:
            qid = q['id']
            title = q['title_truncated']
            summary = summaries.get(qid, '')
            analyst_notes = ''  # Blank column for manual notes

            writer.writerow([qid, title, summary, analyst_notes])


def write_markdown_report(md_path, questions, summaries, year, month, product):
    """Write markdown report."""
    product_name = "Thunderbird for Android" if product == "android" else "Thunderbird Desktop"

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f'# {product_name} Question Summary - {year:04d}-{month:02d}\n\n')
        f.write(f'**Total Questions:** {len(questions)} (spam filtered out)\n\n')
        f.write('| ID | Title | Summary | Analyst Notes |\n')
        f.write('|----|-------|---------|---------------|\n')

        for q in questions:
            qid = q['id']
            title_full = q['title']
            title_display = q['title_truncated']
            summary = summaries.get(qid, '')
            analyst_notes = ''  # Blank column

            # Create link
            link = make_question_link(qid, title_full)

            # Escape pipes in summary and title for markdown table
            summary_escaped = summary.replace('|', '¦')
            title_escaped = title_display.replace('|', '¦')

            f.write(f'| {link} | {title_escaped} | {summary_escaped} | {analyst_notes} |\n')


def main():
    if len(sys.argv) == 4:
        product = sys.argv[1]
        year = int(sys.argv[2])
        month = int(sys.argv[3])
    else:
        # Default to current month
        product = 'android'
        year = 2026
        month = 3

    print(f"Creating question summary report for {product} {year:04d}-{month:02d}")

    # Load questions (spam filtered)
    print("\nLoading questions...")
    questions = load_questions(product, year, month)

    # Generate summaries using Claude API
    print("\nGenerating summaries with Claude AI...")
    summaries = generate_summaries(questions)
    print(f"Generated {len(summaries)} summaries")

    # Create reports directory
    reports_dir = Path('REPORTS') / product.upper()
    reports_dir.mkdir(parents=True, exist_ok=True)

    # Write CSV report
    csv_filename = f"{year:04d}-{month:02d}-{product}-question-summary.csv"
    csv_path = reports_dir / csv_filename
    write_csv_report(csv_path, questions, summaries)
    print(f"\nWrote CSV report: {csv_path}")

    # Write markdown report
    md_filename = f"{year:04d}-{month:02d}-{product}-question-summary.md"
    md_path = reports_dir / md_filename
    write_markdown_report(md_path, questions, summaries, year, month, product)
    print(f"Wrote markdown report: {md_path}")


if __name__ == '__main__':
    main()
