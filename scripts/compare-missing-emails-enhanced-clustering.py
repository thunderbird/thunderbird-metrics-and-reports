#!/usr/bin/env python3
"""
Compare Missing Emails or Folders enhanced clustering between two months.
"""

import sys
import csv
from pathlib import Path

# Increase CSV field size limit
csv.field_size_limit(sys.maxsize)


def load_clustering_data(csv_path):
    """Load clustering data from CSV."""
    data = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            category = row.get('category', '')
            count = int(row.get('num_questions', 0))
            qids = row.get('question_ids', '').split(';') if row.get('question_ids') else []
            data[category] = {
                'count': count,
                'question_ids': qids
            }
    return data


def compare_categories(month1_data, month2_data, month1_name, month2_name):
    """Compare category data between two months."""
    all_categories = set(month1_data.keys()) | set(month2_data.keys())
    comparisons = []

    for category in all_categories:
        month1_count = month1_data.get(category, {}).get('count', 0)
        month2_count = month2_data.get(category, {}).get('count', 0)
        change = month2_count - month1_count

        if month1_count > 0:
            pct_change = (change / month1_count) * 100.0
        elif month2_count > 0:
            pct_change = 100.0  # New in month 2
        else:
            pct_change = 0.0

        comparisons.append({
            'category': category,
            'month1_count': month1_count,
            'month2_count': month2_count,
            'change': change,
            'pct_change': pct_change
        })

    # Sort by absolute change descending
    comparisons.sort(key=lambda x: abs(x['change']), reverse=True)
    return comparisons


def write_csv_report(csv_path, comparisons, month1_name, month2_name):
    """Write comparison CSV report."""
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['category', f'{month1_name}_count', f'{month2_name}_count', 'change', 'pct_change'])

        for comp in comparisons:
            pct_str = f"{comp['pct_change']:+.1f}%"
            writer.writerow([
                comp['category'],
                comp['month1_count'],
                comp['month2_count'],
                comp['change'],
                pct_str
            ])


def write_markdown_report(md_path, comparisons, month1_name, month2_name, month1_total, month2_total, product):
    """Write comparison markdown report."""
    product_name = "Thunderbird for Android" if product == "android" else "Thunderbird Desktop"

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f'# {product_name} Missing Emails or Folders (Enhanced Clustering) - {month1_name} vs {month2_name}\n\n')

        # Overall summary
        f.write('## Overall Summary\n\n')
        f.write(f'- **{month1_name} Total:** {month1_total} Missing Emails or Folders issues\n')
        f.write(f'- **{month2_name} Total:** {month2_total} Missing Emails or Folders issues\n')
        total_change = month2_total - month1_total
        total_pct = (total_change / month1_total * 100.0) if month1_total > 0 else 0.0
        f.write(f'- **Change:** {total_change:+d} ({total_pct:+.1f}%)\n\n')

        # Category breakdown
        f.write('## Category Breakdown\n\n')
        f.write(f'| Category | {month1_name} | {month2_name} | Change | % Change | Trend |\n')
        f.write('|----------|------:|------:|-------:|---------:|------:|\n')

        for comp in comparisons:
            # Determine trend
            if comp['change'] > 0:
                trend = '↑'
            elif comp['change'] < 0:
                trend = '↓'
            else:
                trend = '→'

            f.write(f"| {comp['category']} | {comp['month1_count']} | {comp['month2_count']} | "
                   f"{comp['change']:+d} | {comp['pct_change']:+.1f}% | {trend} |\n")

        # Key insights
        f.write('\n## Key Insights\n\n')

        # Largest increases
        increases = [c for c in comparisons if c['change'] > 0]
        if increases:
            f.write('### Largest Increases\n\n')
            for i, comp in enumerate(increases[:5], 1):
                f.write(f"{i}. **{comp['category']}**: {comp['change']:+d} questions ({comp['pct_change']:+.1f}%)\n")
            f.write('\n')

        # Largest decreases
        decreases = [c for c in comparisons if c['change'] < 0]
        if decreases:
            f.write('### Largest Decreases\n\n')
            for i, comp in enumerate(decreases[:5], 1):
                f.write(f"{i}. **{comp['category']}**: {comp['change']:d} questions ({comp['pct_change']:.1f}%)\n")
            f.write('\n')


def main():
    if len(sys.argv) == 5:
        product = sys.argv[1]
        year = int(sys.argv[2])
        month1 = int(sys.argv[3])
        month2 = int(sys.argv[4])
    else:
        # Default to Feb vs March 2026
        product = 'desktop'
        year = 2026
        month1 = 2
        month2 = 3

    month1_name = f'{year:04d}-{month1:02d}'
    month2_name = f'{year:04d}-{month2:02d}'

    print(f"Comparing {product} Missing Emails or Folders (Enhanced Clustering): {month1_name} vs {month2_name}")

    # Load data
    reports_dir = Path('REPORTS') / product.upper()

    month1_csv = reports_dir / f'{month1_name}-{product}-missing-emails-enhanced-clustering.csv'
    month2_csv = reports_dir / f'{month2_name}-{product}-missing-emails-enhanced-clustering.csv'

    if not month1_csv.exists():
        print(f"Error: {month1_csv} not found")
        sys.exit(1)
    if not month2_csv.exists():
        print(f"Error: {month2_csv} not found")
        sys.exit(1)

    print(f"Loading {month1_name} data...")
    month1_data = load_clustering_data(month1_csv)
    month1_total = sum(d['count'] for d in month1_data.values())
    print(f"  Found {month1_total} questions in {len(month1_data)} categories")

    print(f"Loading {month2_name} data...")
    month2_data = load_clustering_data(month2_csv)
    month2_total = sum(d['count'] for d in month2_data.values())
    print(f"  Found {month2_total} questions in {len(month2_data)} categories")

    # Compare
    print("\nComparing categories...")
    comparisons = compare_categories(month1_data, month2_data, month1_name, month2_name)

    # Write reports
    csv_filename = f"{month1_name}_vs_{month2_name}-{product}-missing-emails-enhanced-clustering-comparison.csv"
    csv_path = reports_dir / csv_filename
    write_csv_report(csv_path, comparisons, month1_name, month2_name)
    print(f"\nWrote CSV report: {csv_path}")

    md_filename = f"{month1_name}_vs_{month2_name}-{product}-missing-emails-enhanced-clustering-comparison.md"
    md_path = reports_dir / md_filename
    write_markdown_report(md_path, comparisons, month1_name, month2_name, month1_total, month2_total, product)
    print(f"Wrote markdown report: {md_path}")


if __name__ == '__main__':
    main()
