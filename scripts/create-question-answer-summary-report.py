#!/usr/bin/env python3
"""
Create a monthly forum question & answer summary report.

This script analyzes SUMO questions AND answers from trusted contributors/creators,
generating summaries using Claude AI.
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


def load_trusted_contributors(product):
    """Load trusted contributors list."""
    path = Path('CONCATENATED_FILES') / product.upper() / f'thunderbird-{product}-trusted-contributors.csv'

    if not path.exists():
        print(f"Warning: Trusted contributors file not found: {path}")
        return set()

    trusted = set()
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            creator = row.get('creator', '').strip()
            if creator:
                trusted.add(creator)

    return trusted


def load_questions(product, year, month):
    """Load questions from CSV file, filtering out spam."""
    path = Path('CONCATENATED_FILES') / product.upper() / f'{year:04d}-{month:02d}-sumo-{product}-questions.csv'

    if not path.exists():
        print(f"Error: Questions file not found: {path}")
        sys.exit(1)

    questions = {}
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

                questions[qid] = {
                    'id': qid,
                    'title': row.get('title', ''),
                    'title_truncated': row.get('title', '')[:80],
                    'content': content_clean,
                    'creator': row.get('creator', '')
                }

    print(f"Loaded {len(questions)} non-spam questions ({spam_count} spam filtered)")
    return questions, spam_count


def load_answers(product, year, month):
    """Load answers from CSV file."""
    path = Path('CONCATENATED_FILES') / product.upper() / f'{year:04d}-{month:02d}-sumo-{product}-answers.csv'

    if not path.exists():
        print(f"Warning: Answers file not found: {path}")
        return {}

    question_answers = {}

    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            question_id = row.get('question_id', '')
            creator = row.get('creator', '')
            content = row.get('content', '')

            # Clean HTML
            content_clean = re.sub(r'<[^>]+>', ' ', content)
            content_clean = re.sub(r'\s+', ' ', content_clean).strip()

            if question_id not in question_answers:
                question_answers[question_id] = []

            question_answers[question_id].append({
                'creator': creator,
                'content': content_clean
            })

    print(f"Loaded answers for {len(question_answers)} questions")
    return question_answers


def filter_qa_data(questions, question_answers, trusted_contributors):
    """Combine questions with filtered answers (trusted contributors or question creator only)."""
    filtered_qa = []
    total_answers = 0
    filtered_answers_count = 0

    for qid, q in questions.items():
        question_creator = q['creator']

        # Get all answers for this question
        all_answers = question_answers.get(qid, [])
        total_answers += len(all_answers)

        # Filter to only trusted contributors or question creator
        filtered_answers = []
        for answer in all_answers:
            answer_creator = answer['creator']
            if answer_creator == question_creator or answer_creator in trusted_contributors:
                filtered_answers.append(answer)
                filtered_answers_count += 1

        filtered_qa.append({
            'id': qid,
            'title': q['title'],
            'title_truncated': q['title_truncated'],
            'question_content': q['content'],
            'answers': filtered_answers
        })

    print(f"Answer filtering: {filtered_answers_count}/{total_answers} kept ({filtered_answers_count/total_answers*100:.1f}%)")
    return filtered_qa, total_answers, filtered_answers_count


def summarize_with_llm(client, qa_batch):
    """Use Claude to summarize a batch of questions with answers."""

    # Build the prompt
    qa_text = ""
    for i, qa in enumerate(qa_batch, 1):
        qa_text += f"\n\n--- Q&A {i} (ID: {qa['id']}) ---\n"
        qa_text += f"Title: {qa['title']}\n"
        qa_text += f"Question: {qa['question_content'][:600]}\n"

        if qa['answers']:
            qa_text += f"\nAnswers ({len(qa['answers'])}):\n"
            for j, answer in enumerate(qa['answers'][:3], 1):  # Limit to first 3 answers
                qa_text += f"  {j}. From {answer['creator']}: {answer['content'][:400]}\n"

    prompt = f"""I need you to create concise summaries for Thunderbird support Q&As (questions with answers).

For each Q&A below, provide a 1-2 sentence summary that explains:
- What the user's issue or request was
- Key details from the question (errors, symptoms, features)
- Resolution, workaround, or guidance provided in answers (if any)

Be concise and factual. Return your response as a JSON array with one object per Q&A, each containing:
- "question_id": the question ID
- "summary": the summary (1-2 sentences covering question and resolution/answer)

Q&As:
{qa_text}

Return ONLY the JSON array, no other text."""

    try:
        message = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=4096,
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


def generate_summaries(qa_data):
    """Generate summaries for all Q&As using Claude API."""
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        print("Please set it with: export ANTHROPIC_API_KEY=your_key_here")
        sys.exit(1)

    client = Anthropic(api_key=api_key)

    # Process in batches of 10
    batch_size = 10
    all_summaries = {}

    for i in range(0, len(qa_data), batch_size):
        batch = qa_data[i:i+batch_size]
        print(f"Processing Q&As {i+1} to {min(i+batch_size, len(qa_data))} of {len(qa_data)}...")

        summaries = summarize_with_llm(client, batch)

        for summary_obj in summaries:
            qid = str(summary_obj.get('question_id'))  # Ensure string type
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


def write_csv_report(csv_path, qa_data, summaries):
    """Write CSV report."""
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'title', 'LLM_Summary', 'Analyst_notes'])

        for qa in qa_data:
            qid = str(qa['id'])  # Ensure string type for lookup
            title = qa['title_truncated']
            summary = summaries.get(qid, '')
            analyst_notes = ''  # Blank column for manual notes

            writer.writerow([qid, title, summary, analyst_notes])


def write_markdown_report(md_path, qa_data, summaries, year, month, product, total_answers, filtered_answers, trusted_contributors):
    """Write markdown report."""
    product_name = "Thunderbird for Android" if product == "android" else "Thunderbird Desktop"
    trusted_list = ', '.join(sorted(trusted_contributors))

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f'# {product_name} Question & Answer Summary - {year:04d}-{month:02d}\n\n')
        f.write(f'**Total Questions:** {len(qa_data)} (spam filtered out)\n\n')
        f.write(f'**Answer Statistics:**\n')
        f.write(f'- Total answers: {total_answers}\n')
        f.write(f'- Answers from trusted contributors or question creators: {filtered_answers} ({filtered_answers/total_answers*100:.1f}%)\n')
        f.write(f'- Trusted contributors: {trusted_list}\n\n')
        f.write('**Note:** Summaries include information from both questions and answers from trusted contributors/creators.\n\n')
        f.write('| ID | Title | Summary | Analyst Notes |\n')
        f.write('|----|-------|---------|---------------|\n')

        for qa in qa_data:
            qid = str(qa['id'])  # Ensure string type for lookup
            title_full = qa['title']
            title_display = qa['title_truncated']
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

    print(f"Creating question & answer summary report for {product} {year:04d}-{month:02d}")

    # Load trusted contributors
    print("\nLoading trusted contributors...")
    trusted_contributors = load_trusted_contributors(product)
    print(f"  Found {len(trusted_contributors)} trusted contributors: {trusted_contributors}")

    # Load questions (spam filtered)
    print("\nLoading questions...")
    questions, spam_count = load_questions(product, year, month)

    # Load answers
    print("\nLoading answers...")
    question_answers = load_answers(product, year, month)

    # Filter Q&A data
    print("\nFiltering answers to trusted contributors and question creators...")
    qa_data, total_answers, filtered_answers = filter_qa_data(questions, question_answers, trusted_contributors)

    # Generate summaries using Claude API
    print("\nGenerating summaries with Claude AI (including answers)...")
    summaries = generate_summaries(qa_data)
    print(f"Generated {len(summaries)} summaries")

    # Create reports directory
    reports_dir = Path('REPORTS') / product.upper()
    reports_dir.mkdir(parents=True, exist_ok=True)

    # Write CSV report with new filename
    csv_filename = f"{year:04d}-{month:02d}-{product}-question-answer-summary.csv"
    csv_path = reports_dir / csv_filename
    write_csv_report(csv_path, qa_data, summaries)
    print(f"\nWrote CSV report: {csv_path}")

    # Write markdown report with new filename
    md_filename = f"{year:04d}-{month:02d}-{product}-question-answer-summary.md"
    md_path = reports_dir / md_filename
    write_markdown_report(md_path, qa_data, summaries, year, month, product, total_answers, filtered_answers, trusted_contributors)
    print(f"Wrote markdown report: {md_path}")


if __name__ == '__main__':
    main()
