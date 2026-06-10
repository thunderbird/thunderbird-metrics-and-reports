"""Shared helpers for unanswered-question self-assignment.

The assignments CSV is the persistent source of truth for who is handling each
unanswered question. The report scripts only READ it; the HTML report's
Claim/Release buttons WRITE it via the GitHub API. Keeping the report scripts
read-only means a twice-daily regeneration can never clobber a manual claim.

CSV schema (extra columns reserved so a future "take-over" feature is additive):
    question_id,assignee,assigned_at,assigned_by
"""
import csv
import os

# TODO: replace placeholders with the 4 real GitHub usernames.
# Order is not significant (assignment is manual, not algorithmic).
ASSIGNEES = ['PERSON1', 'PERSON2', 'PERSON3', 'PERSON4']

FIELDNAMES = ['question_id', 'assignee', 'assigned_at', 'assigned_by']


def load_assignments(path):
    """Return {question_id(int): {assignee, assigned_at, assigned_by}}.

    Missing/empty file -> {}. Rows missing the optional columns are tolerated.
    Rows with a blank assignee are treated as unassigned (skipped).
    """
    if not path or not os.path.exists(path):
        return {}
    result = {}
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid_raw = (row.get('question_id') or '').strip()
            assignee = (row.get('assignee') or '').strip()
            if not qid_raw or not assignee:
                continue
            try:
                qid = int(qid_raw)
            except ValueError:
                continue
            result[qid] = {
                'assignee': assignee,
                'assigned_at': (row.get('assigned_at') or '').strip(),
                'assigned_by': (row.get('assigned_by') or '').strip(),
            }
    return result
