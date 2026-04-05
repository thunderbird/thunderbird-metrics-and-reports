#!/usr/bin/env python3
"""
Generate Markdown pages from CSV report files.
Converts semi-colon delimited question IDs to links with tooltips.
Creates both summary and details tables.
"""

import csv
import os
import sys
from pathlib import Path
from datetime import datetime


def load_questions_map(questions_csv_path):
    """Load questions CSV and create a map of id -> title."""
    questions_map = {}
    try:
        with open(questions_csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                question_id = row.get('id', '')
                title = row.get('title', '')
                if question_id and title:
                    questions_map[question_id] = title
    except FileNotFoundError:
        print(f"Warning: Questions file not found: {questions_csv_path}", file=sys.stderr)
    return questions_map


def create_question_link(question_id, questions_map):
    """Create a Markdown link for a question ID."""
    title = questions_map.get(question_id, "Question")
    tooltip = title[:80] if len(title) > 80 else title
    return f'[{question_id}](https://support.mozilla.org/questions/{question_id} "{tooltip}")'


def process_question_ids(ids_string, questions_map):
    """Convert semi-colon delimited question IDs to Markdown links."""
    if not ids_string or ';' not in ids_string:
        return ids_string
    
    ids = ids_string.split(';')
    links = [create_question_link(id.strip(), questions_map) for id in ids if id.strip()]
    return '; '.join(links)


def escape_markdown_cell(text):
    """Escape pipe characters in cell content."""
    if not text:
        return ""
    return str(text).replace('|', '\\|')


def generate_markdown_page(csv_path, output_path, questions_csv_path, product, month_year):
    """Generate a Markdown page with summary and details tables from a CSV report file."""
    
    # Load questions map for creating links
    questions_map = load_questions_map(questions_csv_path)
    
    # Read CSV and prepare data
    rows = []
    columns = []
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            columns = reader.fieldnames or []
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        print(f"Error: CSV file not found: {csv_path}", file=sys.stderr)
        return False
    
    if not rows:
        print(f"Warning: No data in CSV file: {csv_path}", file=sys.stderr)
        return False
    
    # Define which columns go in which table
    summary_columns = [
        'Date',
        'num_questions',
        'num_solved',
        'solved-percentage',
        'num_ignored',
        'ignored-percentage',
        'synthetic_solved_by_random_contributors',
        'synthetic_solved_by_random_contributors-percentage',
        'synthetic_solved_by_trusted_contributors',
        'synthetic_solved_by_trusted_contributors-percentage',
        'synthetic_solved_rate'
    ]
    
    details_columns = [
        'Date',
        'question_ids_question_creator_answered_last',
        'question_ids_trusted_contributor_answered_last',
        'question_ids_random_contributor_answered_last'
    ]
    
    # Start building Markdown
    product_display = "Thunderbird Desktop" if product == "desktop" else "Thunderbird Android"
    page_title = f"{product_display} Report - {month_year}"
    
    markdown_content = f"""---
layout: default
title: {page_title}
---

# {page_title}

*Last updated: {datetime.now().isoformat()}*

## Summary

"""
    
    # Generate Summary Table
    markdown_content += "| " + " | ".join(col.replace('_', ' ').replace('-', ' ').title() for col in summary_columns) + " |\n"
    markdown_content += "| " + " | ".join("---" for _ in summary_columns) + " |\n"
    
    for row in rows:
        row_cells = [escape_markdown_cell(row.get(col, '')) for col in summary_columns]
        markdown_content += "| " + " | ".join(row_cells) + " |\n"
    
    # Generate Details Table
    markdown_content += "\n## Details\n\n"
    markdown_content += "| " + " | ".join(col.replace('_', ' ').replace('-', ' ').title() for col in details_columns) + " |\n"
    markdown_content += "| " + " | ".join("---" for _ in details_columns) + " |\n"
    
    for row in rows:
        row_cells = []
        for col in details_columns:
            value = row.get(col, '')
            # Process question ID columns to convert to links
            if col in ['question_ids_question_creator_answered_last', 
                      'question_ids_trusted_contributor_answered_last',
                      'question_ids_random_contributor_answered_last']:
                value = process_question_ids(value, questions_map)
            row_cells.append(escape_markdown_cell(value))
        markdown_content += "| " + " | ".join(row_cells) + " |\n"
    
    markdown_content += "\n[Back to Dashboard](/)\n"
    
    # Create output directory if needed
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Write markdown file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"Generated: {output_path}")
        return True
    except Exception as e:
        print(f"Error writing file {output_path}: {e}", file=sys.stderr)
        return False


def main():
    """Main function to generate all report pages."""
    base_path = Path(__file__).parent.parent
    reports_path = base_path / "REPORTS"
    concat_path = base_path / "CONCATENATED_FILES"
    output_base_path = base_path / "html_reports"
    
    # Create html_reports directory if it doesn't exist
    output_base_path.mkdir(exist_ok=True)
    
    # Define products and their configs
    products = {
        'DESKTOP': {
            'reports_dir': reports_path / 'DESKTOP',
            'concat_dir': concat_path / 'DESKTOP',
            'output_dir': output_base_path / 'desktop',
            'product': 'desktop'
        },
        'ANDROID': {
            'reports_dir': reports_path / 'ANDROID',
            'concat_dir': concat_path / 'ANDROID',
            'output_dir': output_base_path / 'android',
            'product': 'android'
        }
    }
    
    total_generated = 0
    
    for product_name, config in products.items():
        reports_dir = config['reports_dir']
        concat_dir = config['concat_dir']
        output_dir = config['output_dir']
        product = config['product']
        
        if not reports_dir.exists():
            print(f"Warning: Reports directory not found: {reports_dir}")
            continue
        
        # Find all report CSV files
        for report_file in sorted(reports_dir.glob('*-sumo-*-report.csv')):
            # Extract month_year from filename (e.g., "2026-02-sumo-desktop-report.csv")
            filename = report_file.name
            month_year_match = filename.split('-sumo')[0]
            
            # Find corresponding questions CSV
            questions_file = concat_dir / f"{month_year_match}-sumo-{product}-questions.csv"
            
            if not questions_file.exists():
                print(f"Warning: Questions file not found: {questions_file}")
                questions_file = None
            else:
                questions_file = str(questions_file)
            
            # Generate output filename with .md extension
            output_file = output_dir / f"{month_year_match}-sumo-{product}-report.md"
            
            # Generate Markdown page
            if generate_markdown_page(
                str(report_file),
                str(output_file),
                questions_file,
                product,
                month_year_match
            ):
                total_generated += 1
    
    print(f"\nGenerated {total_generated} report page(s)")
    return 0 if total_generated > 0 else 1


if __name__ == '__main__':
    sys.exit(main())
