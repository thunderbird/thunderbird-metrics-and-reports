#!/usr/bin/env python3
"""
Compare OAuth/Authentication issues by email provider across two months.

This script compares provider breakdowns between two months.
"""

import sys
import csv
from pathlib import Path
from collections import defaultdict

# Increase CSV field size limit
csv.field_size_limit(sys.maxsize)


def load_provider_data(csv_path):
    """Load provider data from CSV file."""
    providers = {}

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            provider_name = row.get('provider', '')
            count = int(row.get('num_questions', 0))
            qids = row.get('question_ids', '')

            providers[provider_name] = {
                'count': count,
                'qids': qids.split(';') if qids else []
            }

    return providers


def compare_providers(month1_data, month2_data, month1_name, month2_name):
    """Compare provider data between two months."""
    # Get all unique providers
    all_providers = set(month1_data.keys()) | set(month2_data.keys())

    comparisons = []

    for provider in all_providers:
        month1_count = month1_data.get(provider, {}).get('count', 0)
        month2_count = month2_data.get(provider, {}).get('count', 0)

        change = month2_count - month1_count

        # Calculate percentage change
        if month1_count > 0:
            pct_change = (change / month1_count) * 100.0
        elif month2_count > 0:
            pct_change = 100.0  # New in month 2
        else:
            pct_change = 0.0

        comparisons.append({
            'provider': provider,
            f'{month1_name}_count': month1_count,
            f'{month2_name}_count': month2_count,
            'change': change,
            'pct_change': pct_change
        })

    # Sort by month2 count descending
    comparisons.sort(key=lambda x: x[f'{month2_name}_count'], reverse=True)

    return comparisons


def write_csv_report(csv_path, comparisons, month1_name, month2_name):
    """Write CSV comparison report."""
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'provider',
            f'{month1_name}_count',
            f'{month2_name}_count',
            'change',
            'pct_change'
        ])

        for comp in comparisons:
            writer.writerow([
                comp['provider'],
                comp[f'{month1_name}_count'],
                comp[f'{month2_name}_count'],
                comp['change'],
                f"{comp['pct_change']:.1f}%"
            ])


def write_markdown_report(md_path, comparisons, month1_name, month2_name, month1_total, month2_total, product):
    """Write markdown comparison report."""
    product_name = "Thunderbird for Android" if product == "android" else "Thunderbird Desktop"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f'# {product_name} OAuth/Authentication Issues by Email Provider - {month1_name} vs {month2_name}\n\n')

        # Overall summary
        total_change = month2_total - month1_total
        total_pct_change = (total_change / month1_total) * 100.0 if month1_total > 0 else 0.0

        f.write(f'## Overall Summary\n\n')
        f.write(f'- **{month1_name} Total:** {month1_total} OAuth/Authentication issues\n')
        f.write(f'- **{month2_name} Total:** {month2_total} OAuth/Authentication issues\n')
        f.write(f'- **Change:** {total_change:+d} ({total_pct_change:+.1f}%)\n\n')

        # Provider breakdown
        f.write(f'## Provider Breakdown\n\n')
        f.write(f'| Provider | {month1_name} | {month2_name} | Change | % Change | Trend |\n')
        f.write(f'|----------|------:|------:|-------:|---------:|------:|\n')

        for comp in comparisons:
            provider = comp['provider']
            m1_count = comp[f'{month1_name}_count']
            m2_count = comp[f'{month2_name}_count']
            change = comp['change']
            pct_change = comp['pct_change']

            # Determine trend indicator
            if change > 0:
                trend = '↑'
            elif change < 0:
                trend = '↓'
            else:
                trend = '→'

            # Format percentage change with sign
            pct_str = f'{pct_change:+.1f}%' if m1_count > 0 else 'NEW' if m2_count > 0 else '—'

            f.write(f'| {provider} | {m1_count} | {m2_count} | {change:+d} | {pct_str} | {trend} |\n')

        # Key insights
        f.write(f'\n## Key Insights\n\n')

        # Find biggest increases
        increases = [c for c in comparisons if c['change'] > 0]
        increases.sort(key=lambda x: x['change'], reverse=True)

        if increases:
            f.write(f'### Largest Increases\n\n')
            for i, comp in enumerate(increases[:3], 1):
                provider = comp['provider']
                change = comp['change']
                pct = comp['pct_change']
                f.write(f'{i}. **{provider}**: +{change} questions ({pct:+.1f}%)\n')
            f.write('\n')

        # Find biggest decreases
        decreases = [c for c in comparisons if c['change'] < 0]
        decreases.sort(key=lambda x: x['change'])

        if decreases:
            f.write(f'### Largest Decreases\n\n')
            for i, comp in enumerate(decreases[:3], 1):
                provider = comp['provider']
                change = comp['change']
                pct = comp['pct_change']
                f.write(f'{i}. **{provider}**: {change} questions ({pct:.1f}%)\n')
            f.write('\n')

        # New providers in month2
        new_providers = [c for c in comparisons if c[f'{month1_name}_count'] == 0 and c[f'{month2_name}_count'] > 0]
        if new_providers:
            f.write(f'### New Providers in {month2_name}\n\n')
            for comp in new_providers:
                provider = comp['provider']
                count = comp[f'{month2_name}_count']
                f.write(f'- **{provider}**: {count} questions\n')
            f.write('\n')

        # Disappeared providers
        disappeared = [c for c in comparisons if c[f'{month1_name}_count'] > 0 and c[f'{month2_name}_count'] == 0]
        if disappeared:
            f.write(f'### Providers No Longer Appearing in {month2_name}\n\n')
            for comp in disappeared:
                provider = comp['provider']
                count = comp[f'{month1_name}_count']
                f.write(f'- **{provider}**: Had {count} questions in {month1_name}\n')
            f.write('\n')


def main():
    if len(sys.argv) == 5:
        product = sys.argv[1]
        year = int(sys.argv[2])
        month1 = int(sys.argv[3])
        month2 = int(sys.argv[4])
    else:
        # Default: Compare Feb 2026 vs Mar 2026
        product = 'desktop'
        year = 2026
        month1 = 2
        month2 = 3

    month1_name = f'{year:04d}-{month1:02d}'
    month2_name = f'{year:04d}-{month2:02d}'

    print(f"Comparing OAuth provider data: {month1_name} vs {month2_name}")

    # Load provider data
    reports_dir = Path('REPORTS') / product.upper()

    month1_csv = reports_dir / f'{month1_name}-{product}-oauth-by-provider.csv'
    month2_csv = reports_dir / f'{month2_name}-{product}-oauth-by-provider.csv'

    if not month1_csv.exists():
        print(f"Error: File not found: {month1_csv}")
        sys.exit(1)

    if not month2_csv.exists():
        print(f"Error: File not found: {month2_csv}")
        sys.exit(1)

    print(f"Loading {month1_name} data...")
    month1_data = load_provider_data(month1_csv)
    month1_total = sum(p['count'] for p in month1_data.values())
    print(f"  Total: {month1_total} OAuth/Authentication issues")

    print(f"Loading {month2_name} data...")
    month2_data = load_provider_data(month2_csv)
    month2_total = sum(p['count'] for p in month2_data.values())
    print(f"  Total: {month2_total} OAuth/Authentication issues")

    # Compare
    print("Comparing providers...")
    comparisons = compare_providers(month1_data, month2_data, month1_name, month2_name)

    # Write reports
    csv_filename = f'{month1_name}_vs_{month2_name}-{product}-oauth-provider-comparison.csv'
    csv_path = reports_dir / csv_filename
    write_csv_report(csv_path, comparisons, month1_name, month2_name)
    print(f"\nWrote CSV report: {csv_path}")

    md_filename = f'{month1_name}_vs_{month2_name}-{product}-oauth-provider-comparison.md'
    md_path = reports_dir / md_filename
    write_markdown_report(md_path, comparisons, month1_name, month2_name, month1_total, month2_total, product)
    print(f"Wrote markdown report: {md_path}")


if __name__ == '__main__':
    main()
