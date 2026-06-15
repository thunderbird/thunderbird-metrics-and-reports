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


def format_issue_body(removed, sha='', actor=''):
    """Render the notification-issue body.

    The removed rows carry attacker-controlled assignee/question_id text (an
    off-allowlist row can hold anything), so it is emitted inside a fenced code
    block with line breaks stripped -- inside a code block GitHub renders no
    @-mentions, links or images, and because every line starts with the file
    path a stray ``` in a value can't close the fence. `sha`/`actor` come from
    GitHub (trusted) but are cleaned the same way for good measure.
    """
    def clean(s):
        return str(s if s is not None else '').replace('\r', ' ').replace('\n', ' ')

    lines = [f"{clean(r.get('file'))} qid={clean(r.get('question_id'))} "
             f"assignee={clean(r.get('assignee'))}" for r in removed]
    block = '\n'.join(lines) if lines else '(none)'
    return (
        'The assignment guard auto-reverted row(s) whose assignee is not in '
        'the ASSIGNEES allowlist.\n\n'
        '**Removed:**\n'
        f'```\n{block}\n```\n\n'
        f'Triggered by commit {clean(sha)} (actor: @{clean(actor)}).\n'
        'Review and, if the person should be allowed, add them to '
        '`ASSIGNEES` in `scripts/assignments.py`.'
    )


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
            # utf-8-sig strips a leading BOM so the first header stays
            # 'question_id' rather than '﻿question_id'.
            with open(path, newline='', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                fieldnames = reader.fieldnames or FIELDNAMES
                rows = list(reader)
        except (OSError, csv.Error) as e:
            print(f'ERROR reading {path}: {e}; leaving it untouched.', file=sys.stderr)
            continue

        # If the header isn't canonical (e.g. trailing space, wrong case), the
        # row.get('question_id'/'assignee') lookups below silently return None.
        # That would make us either wipe every legitimate row (qid='' fails
        # isdigit) or wave through unchecked rows (assignee=''). Neither is safe,
        # so leave the file untouched and let a human fix the header.
        if 'question_id' not in fieldnames or 'assignee' not in fieldnames:
            print(f'WARNING: {path} has a non-canonical header {fieldnames!r}; '
                  f'leaving it untouched.', file=sys.stderr)
            continue

        kept = []
        seen = set()
        dropped_dupes = 0
        blanked_by = 0
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
            # assigned_by should be the (allowlisted) claimer. A non-allowlist
            # value is forged attribution: keep the legitimate claim but blank
            # the bogus metadata rather than dropping the whole row.
            assigned_by = (row.get('assigned_by') or '').strip()
            if assigned_by and assigned_by.lower() not in allow:
                row['assigned_by'] = ''
                blanked_by += 1
            kept.append(row)
        kept.reverse()

        if len(kept) != len(rows) or blanked_by:
            try:
                with open(path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(kept)
            except OSError as e:
                print(f'ERROR writing {path}: {e}', file=sys.stderr)
                sys.exit(1)
            print(f'{path}: removed {len(rows) - len(kept)} row(s) '
                  f'(off-allowlist/malformed; {dropped_dupes} duplicate; '
                  f'{blanked_by} forged assigned_by blanked)')

    for r in removed:
        print(f"Removed: {r['file']} qid={r['question_id']} assignee={r['assignee']}")
    if not removed:
        print('No off-allowlist assignees found.')

    emit(removed)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--render-issue-body':
        # Used by the workflow's notify step: read the removed rows recorded by
        # the validation run and print a markdown-safe issue body to stdout.
        with open('removed-assignments.json', encoding='utf-8') as f:
            sys.stdout.write(format_issue_body(
                json.load(f),
                os.environ.get('TRIGGER_SHA', ''),
                os.environ.get('TRIGGER_ACTOR', ''),
            ))
    else:
        main()
