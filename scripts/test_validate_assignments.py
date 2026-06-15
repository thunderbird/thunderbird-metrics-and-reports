#!/usr/bin/env python3
"""Tests for the assignments allowlist guard's CSV-header robustness.

Covers the Finding #1 regression: a BOM or non-canonical header must NOT cause
the guard to wipe legitimate rows or wave through off-allowlist ones.

Run from the repo root:  uv run scripts/test_validate_assignments.py
"""
import os
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate_assignments as va
from assignments import load_assignments

ALLOW = ['rtanglao', 'wsmwk']
HEADER = 'question_id,assignee,assigned_at,assigned_by'


def run_guard(csv_text):
    """Write csv_text to a temp file, run main() against it, return
    (file_contents_after, removed_list)."""
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, 'a.csv')
        # csv_text may include a BOM; write bytes verbatim.
        with open(path, 'wb') as f:
            f.write(csv_text.encode('utf-8') if isinstance(csv_text, str) else csv_text)

        removed_capture = []
        with mock.patch.object(va, 'ASSIGNEES', ALLOW), \
             mock.patch.object(va, 'CSV_PATHS', [path]), \
             mock.patch.object(va, 'emit', lambda removed: removed_capture.extend(removed)), \
             mock.patch.dict(os.environ, {}, clear=False):
            # emit writes removed-assignments.json into cwd; do it in the tempdir.
            cwd = os.getcwd()
            os.chdir(d)
            try:
                va.main()
            finally:
                os.chdir(cwd)
        with open(path, encoding='utf-8-sig') as f:
            after = f.read()
        return after, removed_capture


class HeaderRobustness(unittest.TestCase):
    def test_canonical_keeps_allowlisted_removes_offlist(self):
        csv_text = (f'{HEADER}\n'
                    '111,rtanglao,2026-01-01T00:00:00Z,rtanglao\n'
                    '222,attacker,2026-01-01T00:00:00Z,attacker\n')
        after, removed = run_guard(csv_text)
        self.assertIn('111,rtanglao', after)        # legit kept
        self.assertNotIn('attacker', after)          # off-allowlist removed
        self.assertEqual([r['assignee'] for r in removed], ['attacker'])

    def test_bom_does_not_wipe_legit_rows(self):
        # The bug: a BOM made question_id lookups fail, wiping every row.
        csv_text = ('﻿' + f'{HEADER}\n'
                    '111,rtanglao,2026-01-01T00:00:00Z,rtanglao\n')
        after, removed = run_guard(csv_text)
        self.assertIn('111,rtanglao', after)         # NOT wiped
        self.assertEqual(removed, [])                # no false "off-allowlist"

    def test_trailing_space_header_left_untouched(self):
        csv_text = ('question_id ,assignee,assigned_at,assigned_by\n'
                    '111,rtanglao,2026-01-01T00:00:00Z,rtanglao\n')
        after, removed = run_guard(csv_text)
        self.assertIn('111,rtanglao', after)         # untouched, not wiped
        self.assertEqual(removed, [])

    def test_wrong_case_header_left_untouched_not_waved_through(self):
        # Off-allowlist row under a wrong-case header: must not be silently kept
        # as "validated". We leave the file untouched for a human to fix.
        csv_text = ('Question_ID,Assignee,assigned_at,assigned_by\n'
                    '222,attacker,2026-01-01T00:00:00Z,attacker\n')
        after, removed = run_guard(csv_text)
        # File untouched (no rewrite); removed stays empty because we bailed.
        self.assertIn('222,attacker', after)
        self.assertEqual(removed, [])

    def test_forged_assigned_by_blanked_row_kept(self):
        # Off-allowlist assigned_by is forged attribution: blank it, keep claim.
        csv_text = (f'{HEADER}\n'
                    '111,rtanglao,2026-01-01T00:00:00Z,attacker\n')
        after, removed = run_guard(csv_text)
        self.assertIn('111,rtanglao', after)         # claim preserved
        self.assertNotIn('attacker', after)          # forged attribution gone
        self.assertTrue(after.rstrip().endswith('111,rtanglao,2026-01-01T00:00:00Z,'))
        self.assertEqual(removed, [])                # not a removal -> no issue

    def test_legit_assigned_by_preserved(self):
        csv_text = (f'{HEADER}\n'
                    '111,rtanglao,2026-01-01T00:00:00Z,rtanglao\n')
        after, _ = run_guard(csv_text)
        self.assertIn('111,rtanglao,2026-01-01T00:00:00Z,rtanglao', after)


class IssueBodySafety(unittest.TestCase):
    def test_markdown_injection_neutralized(self):
        removed = [{
            'file': 'UNANSWERED_QUESTIONS/desktop-assignments.csv',
            'question_id': '999',
            # Attacker payload: mention, image, fence-breakout attempt, newline.
            'assignee': '@everyone ![x](http://evil/i)\n```\n## injected',
        }]
        body = va.format_issue_body(removed, sha='abc123', actor='pusher')
        lines = body.split('\n')
        # Exactly one fenced block: precisely two lines that ARE a bare fence.
        fences = [i for i, l in enumerate(lines) if l == '```']
        self.assertEqual(len(fences), 2)
        # Payload collapsed to a single line between the fences, starting with
        # the file path -- so its embedded ``` is mid-line and can't close the
        # block, and the @mention/image markdown stays inert inside code.
        inner = lines[fences[0] + 1:fences[1]]
        self.assertEqual(len(inner), 1)
        self.assertTrue(inner[0].startswith('UNANSWERED_QUESTIONS/'))
        self.assertIn('## injected', inner[0])       # stayed inside the block
        self.assertIn('@everyone', inner[0])         # preserved verbatim as data
        self.assertIn('actor: @pusher', body)

    def test_empty_removed_renders_none(self):
        body = va.format_issue_body([], sha='', actor='')
        self.assertIn('(none)', body)
        self.assertEqual(body.count('```'), 2)

    def test_load_assignments_handles_bom(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, 'a.csv')
            with open(path, 'w', encoding='utf-8') as f:
                f.write('﻿' + f'{HEADER}\n111,rtanglao,2026-01-01T00:00:00Z,rtanglao\n')
            loaded = load_assignments(path)
            self.assertEqual(loaded.get(111, {}).get('assignee'), 'rtanglao')


if __name__ == '__main__':
    unittest.main(verbosity=2)
