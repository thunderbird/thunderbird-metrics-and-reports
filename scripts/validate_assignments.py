#!/usr/bin/env python3
"""Validate the assignments CSVs against the ASSIGNEES allowlist and revert
off-allowlist rows in place.

Run by the gha-validate-assignments workflow on every push that touches an
assignments CSV. An "offending row" is one whose `assignee` is non-empty and not
in ASSIGNEES; such rows are removed (blank-assignee rows are kept — they're just
unassigned). The workflow commits the corrected files and notifies rtanglao.

SAFETY: while ASSIGNEES still contains placeholders (PERSON1-4), validation is
skipped entirely — otherwise every real claim would be reverted. It activates
automatically once real usernames replace the placeholders.

Stdlib only; no third-party dependencies.
"""
import csv
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from assignments import ASSIGNEES, FIELDNAMES

CSV_PATHS = [
    'UNANSWERED_QUESTIONS/desktop-assignments.csv',
    'UNANSWERED_QUESTIONS/android-assignments.csv',
]


def placeholders_present(allow):
    return any(str(a).startswith('PERSON') for a in allow)


def emit(removed):
    """Write removed_count to GITHUB_OUTPUT and dump details for the workflow."""
    out = os.environ.get('GITHUB_OUTPUT')
    if out:
        with open(out, 'a', encoding='utf-8') as f:
            f.write(f'removed_count={len(removed)}\n')
    with open('removed-assignments.json', 'w', encoding='utf-8') as f:
        json.dump(removed, f, indent=2)


def main():
    allow = set(ASSIGNEES)

    if placeholders_present(ASSIGNEES):
        print('ASSIGNEES still contains placeholders (PERSON1-4); validation skipped.')
        emit([])
        return

    removed = []
    for path in CSV_PATHS:
        if not os.path.exists(path):
            continue
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames or FIELDNAMES
            rows = list(reader)

        kept = []
        for row in rows:
            assignee = (row.get('assignee') or '').strip()
            if assignee and assignee not in allow:
                removed.append({
                    'file': path,
                    'question_id': (row.get('question_id') or '').strip(),
                    'assignee': assignee,
                })
            else:
                kept.append(row)

        if len(kept) != len(rows):
            with open(path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(kept)
            print(f'{path}: removed {len(rows) - len(kept)} off-allowlist row(s)')

    for r in removed:
        print(f"Removed: {r['file']} qid={r['question_id']} assignee={r['assignee']}")
    if not removed:
        print('No off-allowlist assignees found.')

    emit(removed)


if __name__ == '__main__':
    main()
