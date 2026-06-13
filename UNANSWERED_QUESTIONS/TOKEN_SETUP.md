# Setting up your GitHub token to claim questions

The **Claim / Release** buttons in the unanswered-questions HTML report write to
the assignments file in this repository on your behalf. To do that, your browser
needs a GitHub **fine-grained personal access token (PAT)** with permission to
write to *only this repository*.

You do this **once per browser** (e.g. once for Firefox release, once for Firefox Nightly, once for any other browser you use like Chrome. The token is stored in your browser's
`localStorage` and is sent only to GitHub's API — it is never committed to the
repo or shared with anyone.

---

## TL;DR (clickpath)

1. <https://github.com/settings/personal-access-tokens> > Click **Generate new token**
   * Set **Token name:** to something relevant like **2026-06-sumo-assignment**.
   * Select **Resource owner**: **thunderbird**.
   * Set **Expiration** to: **90 days** or less.
   * Set **Repository access** to **Only select repositories**  and then select **thunderbird/thunderbird-metrics-and-reports**.
   * Click **Add permissions**, then tick **✓** **Contents** and under **Access:** select  **Read and write**. You can ignore **Metadata** (its defaults are fine).
7. Click **Generate token** and then **copy it to your password manager immediately because it will only be visible once**.
8. Open the report ([desktop](HTML_REPORTS/desktop-latest-unanswered-questions.html) · [android](HTML_REPORTS/android-latest-unanswered-questions.html)) → **Set GitHub token** → paste the token from the previous step that you saved in your password manager.
---

# Details with full explanatory info
## Part 1 — Create the token at github.com

1. Sign in to <https://github.com>.
2. Click your **profile photo** (top-right corner) → **Settings**.
3. In the left sidebar, scroll to the bottom and click **Developer settings**.
4. Click **Personal access tokens** → **Fine-grained tokens**.
   (Direct link: <https://github.com/settings/personal-access-tokens>)
5. Click **Generate new token** (top-right).
6. Fill in the form:
   - **Token name:** something memorable, e.g. `tb-metrics-assignments`.
   - **Expiration:** choose a short window, e.g. **90 days** (you'll repeat
     these steps when it expires — that's intentional, it limits risk).
   - **Resource owner:** select **`thunderbird`** (the organization that owns
     this repo), *not* your personal account.
     > ⚠️ If the `thunderbird` org requires admin approval for fine-grained
     > tokens, your token will be created in a **pending** state and won't work
     > until an org owner approves it. Ask an org admin to approve it if so.
7. Under **Repository access**, choose **Only select repositories**, then in the
   dropdown select **`thunderbird/thunderbird-metrics-and-reports`**.
8. Under **Permissions** → **Repository permissions**, find **Contents** and set
   **Access: Read and write**.
   - Leave everything else at *No access*.
   - (**Metadata: Read-only** is added automatically and is required — that's
     fine.)
9. Click **Generate token** at the bottom.
10. **Copy the token immediatly to your password manager** e.g, 1Password — GitHub shows it only once. It looks like
    `github_pat_XXXXXXXXXXXXXXXXXXXXXXXX`.

> 🔒 **Why these exact settings?** Single repo + Contents-only + short expiry
> keeps the blast radius small: even if the token leaked, it could only **write**
> to files in this one repo, and only until it expires. You can revoke it any
> time from the same Fine-grained tokens page.
>
> ⚠️ **One thing you can't turn off:** GitHub gives *every* fine-grained token
> read-only access to *all* public repositories — this is platform behavior,
> not something we or you can disable. So a leaked token could also *read* public
> repos as you. It still can't **write** anywhere except this repo, and the data
> it could read is already public. That's why short expiry and keeping the token
> in your own browser are the real protections.

---

## Part 2 — Add the token to the report page

1. Open the report you want to work from, e.g. the
   **[latest desktop report](HTML_REPORTS/desktop-latest-unanswered-questions.html)**
   or **[latest android report](HTML_REPORTS/android-latest-unanswered-questions.html)**.
2. In the bar near the top of the page, click **Set GitHub token**.
3. Paste the token you copied into the prompt and confirm.
4. The page calls GitHub to verify the token and then shows
   **“Signed in as @your-username”**, and the **Set GitHub token** button is
   replaced by **Sign out**.

That's it — you're ready to claim.

---

## Part 3 — Claiming and releasing

- On any **unassigned** question, the Assignee column shows a **Claim** button.
  Click it → your username is committed to the assignments file and the cell
  updates to **@you**.
- On a question **you** own, the button reads **Release**. Click it to give the
  question back (your row is removed).
- Questions claimed by someone else show **Claimed** (read-only). If you and a
  teammate click the same open question at almost the same moment, the second
  click shows **“Already claimed by @x”** — no duplicate is written.

Assignments persist across the twice-daily report regeneration, because the
report only *reads* the assignments file.

---

## Troubleshooting

When you paste a token, the page **authenticates** it (`GET /user`) and verifies
it can **write to this repo** by running a harmless write probe — a `PUT` with a
bogus SHA that changes nothing; a `403` means the token lacks write and it is
rejected. (We don't try to verify "single-repo scope" from the browser: every
fine-grained token also has implicit read-only access to all public repos, and
GitHub's repo-listing reflects your account's repos rather than the token's
selected-repo grant, so it can't tell a single-repo token from a broad one. What
matters — that **write** is confined to this repo — is exactly what the probe
checks.)

| Symptom | Cause / fix |
|---|---|
| **“Token rejected…”** after pasting | Token typo, expired, or still pending org approval. Re-copy it, or ask an org admin to approve the fine-grained token for `thunderbird`. |
| **“Token cannot write to …”** | The token can read but lacks write. At set-time the page runs a harmless write probe (a `PUT` with a bogus SHA that changes nothing); a 403 means no write access. Recreate the token with **Contents: Read and write**. |
| Buttons stay disabled / say **Claim** but won't click | You're not signed in. Click **Set GitHub token** and add a token. |
| **Error: … PUT 403** when clicking | The token lacks **Contents: Read and write** on this repo, or isn't scoped to this repo. Regenerate with the correct permission. |
| **Error: … PUT 409** repeatedly | A rare write collision; just click again. (The page already retries up to 5 times automatically.) |
| You switched browsers/machines and buttons don't work | The token lives per-browser in `localStorage`. Repeat **Part 2** on the new browser. |

To remove your token from a browser, click **Sign out** on the report page.

## Note: only team members can be assignees

A server-side guard (`gha-validate-assignments`) auto-removes any assignee that
isn't on the `ASSIGNEES` allowlist in `scripts/assignments.py`, within ~1 minute,
and files an issue. So even with a valid write token, claims only "stick" for
the listed team members. (Inert until the placeholder usernames are replaced.)

---

## See also

- [README.md](README.md) — overview of the self-assignment system and the
  manual (no-token) claiming option.
