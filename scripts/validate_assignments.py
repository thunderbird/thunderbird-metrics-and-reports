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
    allow = {a.lower() for a in ASSIGNEES}  # GitHub logins are case-insensitive

    if placeholders_present(ASSIGNEES):
        print('ASSIGNEES still contains placeholders (PERSON1-4); validation skipped.')
        emit([])
        return

    removed = []
    for path in CSV_PATHS:
        if not os.path.exists(path):
            continue
        try:
            with open(path, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                fieldnames = reader.fieldnames or FIELDNAMES
                rows = list(reader)
        except (OSError, csv.Error) as e:
            print(f'ERROR reading {path}: {e}; leaving it untouched.', file=sys.stderr)
            continue

        kept = []
        seen = set()
        dropped_dupes = 0
        # Walk in reverse so the LAST row for a question_id wins on dedupe.
        for row in reversed(rows):
            assignee = (row.get('assignee') or '').strip()
            qid = (row.get('question_id') or '').strip()
            if not assignee:
                kept.append(row)            # unassigned row: leave as-is
                continue
            if assignee.lower() not in allow or not qid.isdigit():
                # Off-allowlist or malformed -> a real violation; record + notify.
                removed.append({'file': path, 'question_id': qid, 'assignee': assignee})
                continue
            if qid in seen:
                dropped_dupes += 1          # benign duplicate cleanup; not a violation
                continue
            seen.add(qid)
            kept.append(row)
        kept.reverse()

        if len(kept) != len(rows):
            try:
                with open(path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(kept)
            except OSError as e:
                print(f'ERROR writing {path}: {e}', file=sys.stderr)
                sys.exit(1)
            print(f'{path}: removed {len(rows) - len(kept)} row(s) '
                  f'(off-allowlist/malformed; {dropped_dupes} duplicate)')

    for r in removed:
        print(f"Removed: {r['file']} qid={r['question_id']} assignee={r['assignee']}")
    if not removed:
        print('No off-allowlist assignees found.')

    emit(removed)


if __name__ == '__main__':
    main()
