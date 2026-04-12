#!/usr/bin/env python3
"""
Calculate trending tags for SUMO questions in a given calendar month.

Usage:
  - Three args mode:
      monthly-trending-sumo-tags.py <product> YYYY MM
    where <product> is 'desktop' or 'android'

  - Zero arg mode:
      monthly-trending-sumo-tags.py
    where it uses the current calendar month and product defaults to 'desktop'

Outputs:
  - REPORTS/<product>/YYYY-MM-<product>-top_tags.csv (tag statistics sorted by count)
  - REPORTS/<product>/YYYY-MM-<product>-top_tags.md (markdown table with linked question IDs)

Tags are extracted from the 'tags' column (semicolon-delimited). The 'thunderbird' tag is ignored.
"""

import sys
import csv
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def parse_args(argv):
    if len(argv) == 3:
        product = argv[0]
        year = int(argv[1])
        month = int(argv[2])
    elif len(argv) == 0:
        product = 'desktop'
        today = datetime.now()
        year = today.year
        month = today.month
    else:
        print("Usage:\n  monthly-trending-sumo-tags.py <product> YYYY MM\n  or\n  monthly-trending-sumo-tags.py")
        sys.exit(2)

    return product, year, month


def load_questions(product, year, month):
    """Load questions from CSV file and extract tags."""
    base = Path('CONCATENATED_FILES') / product.upper()
    fname = base / f"{year:04d}-{month:02d}-sumo-{product}-questions.csv"

    if not fname.exists():
        print(f"Error: Questions file not found: {fname}")
        sys.exit(1)

    questions = {}
    with open(fname, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid = row.get('id')
            if not qid:
                continue
            questions[qid] = {
                'title': row.get('title', '') or '',
                'tags': row.get('tags', '') or ''
            }

    return questions


def extract_tags(questions):
    """Extract and count tags, ignoring 'thunderbird' tag."""
    tag_counts = defaultdict(int)
    tag_question_ids = defaultdict(list)

    for qid, q in questions.items():
        tags_str = q.get('tags', '') or ''
        if not tags_str:
            continue

        # Split by semicolon and strip whitespace
        tags = [tag.strip() for tag in tags_str.split(';') if tag.strip()]

        for tag in tags:
            # Ignore 'thunderbird' tag
            if tag.lower() == 'thunderbird':
                continue

            tag_counts[tag] += 1
            tag_question_ids[tag].append(qid)

    return tag_counts, tag_question_ids


def sort_tags_by_count(tag_counts, tag_question_ids):
    """Sort tags by count in descending order."""
    sorted_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)

    results = []
    for tag, count in sorted_tags:
        qids = tag_question_ids[tag]
        results.append({
            'tag': tag,
            'count': count,
            'ids': ';'.join(qids)
        })

    return results


def ensure_reports_dir(product):
    rpt = Path('REPORTS') / product.upper()
    rpt.mkdir(parents=True, exist_ok=True)
    return rpt


def write_csv(csv_path, results):
    """Write CSV with tag statistics."""
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['tag', 'tag_count', 'tag_ids'])

        for item in results:
            writer.writerow([item['tag'], item['count'], item['ids']])


def make_question_link(qid, questions):
    """Create a markdown link for a question ID with title as tooltip."""
    title = questions.get(qid, {}).get('title', '') or ''
    # Truncate to 80 chars
    title_truncated = title[:80]
    # Replace characters that cause issues in markdown tables
    title_escaped = title_truncated.replace('"', '\uff02').replace('|', '¦')
    return f'[{qid}](https://support.mozilla.org/questions/{qid} "{title_escaped}")'


def write_markdown(md_path, results, questions, year, month):
    """Write markdown table with linked question IDs."""
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f'# Top tags for {year:04d}-{month:02d}\n\n')
        f.write('| Tag | Count | Question IDs |\n')
        f.write('|-----|------:|-------------|\n')

        for item in results:
            tag = item['tag']
            count = item['count']
            ids_str = item['ids']

            if ids_str:
                id_list = ids_str.split(';')
                linked_ids = ', '.join([make_question_link(qid, questions) for qid in id_list])
            else:
                linked_ids = ''

            f.write(f'| {tag} | {count} | {linked_ids} |\n')


def main(argv):
    product, year, month = parse_args(argv)

    print(f"Processing {product} tags for {year:04d}-{month:02d}")

    # Load questions
    questions = load_questions(product, year, month)
    print(f"Loaded {len(questions)} questions")

    # Extract and count tags
    tag_counts, tag_question_ids = extract_tags(questions)
    print(f"Found {len(tag_counts)} unique tags (excluding 'thunderbird')")

    # Sort by count
    results = sort_tags_by_count(tag_counts, tag_question_ids)

    # Ensure reports directory exists
    rpt_dir = ensure_reports_dir(product)

    # Write CSV
    csv_name = f"{year:04d}-{month:02d}-{product}-top_tags.csv"
    csv_path = rpt_dir / csv_name
    write_csv(csv_path, results)
    print(f'Wrote CSV: {csv_path}')

    # Write markdown
    md_name = f"{year:04d}-{month:02d}-{product}-top_tags.md"
    md_path = rpt_dir / md_name
    write_markdown(md_path, results, questions, year, month)
    print(f'Wrote Markdown: {md_path}')


if __name__ == '__main__':
    main(sys.argv[1:])
