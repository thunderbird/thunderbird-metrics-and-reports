# Unanswered Questions — Self-Assignment

Each unanswered-questions report has an **Assignee** column so the support team
can divide up who is handling which question. Assignments are stored in:

- `desktop-assignments.csv`
- `android-assignments.csv`

These files are the **persistent source of truth**. The reports are regenerated
twice daily; the report scripts only *read* these files, so assignments survive
regeneration.

CSV schema:

```csv
question_id,assignee,assigned_at,assigned_by
1024891,rtanglao,2026-06-09T10:00:00Z,rtanglao
```

(`assigned_at` / `assigned_by` are optional and reserved for a future
"take-over" feature. Presence of a row = assigned; remove the row to unassign.)

## Claiming a question — one click (recommended)

In the HTML report:

1. Click **Set GitHub token** (one-time per browser).
   - Create a **fine-grained personal access token** scoped to **only this
     repository**, with **Contents: Read and write**, and a **short expiry**
     (e.g. 90 days): GitHub → Settings → Developer settings → Fine-grained tokens.
   - Paste it when prompted. It is stored in your browser's `localStorage` and is
     never committed or sent anywhere except the GitHub API.
2. The report shows **Signed in as @you**.
3. Click **Claim** on any open question → it commits a row to the assignments CSV.
4. Click **Release** on one of your own to give it back.

Others' claims show **Claimed** (read-only). If two people claim the same
question, the second sees *"Already claimed by @x"* — no duplicate is written.

## Claiming manually (no token)

Use the **Claim manually (edit CSV)** link in the report header (or open the
`*-assignments.csv` directly), add a line `question_id,your-github-id`, and
commit. The next report run shows it.

## Security notes

- Use a **fine-grained, single-repo, Contents-only, short-expiry** token. Revoke
  it anytime from GitHub settings.
- The token lives only in your browser. Don't paste it into untrusted pages.

## Setup TODO

Replace the placeholder usernames `PERSON1`–`PERSON4` in
`scripts/assignments.py` with the 4 real GitHub usernames. The column renders
whatever is in the CSV regardless, so the system works as soon as real usernames
are committed.
