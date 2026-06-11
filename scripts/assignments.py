"""Shared helpers and front-end assets for unanswered-question self-assignment.

The assignments CSV is the persistent source of truth for who is handling each
unanswered question. The report scripts only READ it; the HTML report's
Claim/Release buttons WRITE it via the GitHub API. Keeping the report scripts
read-only means a twice-daily regeneration can never clobber a manual claim.

CSV schema (extra columns reserved so a future "take-over" feature is additive):
    question_id,assignee,assigned_at,assigned_by

The HTML/CSS/JS constants (HTML_CSS, SORT_JS, ASSIGN_JS) live here so both the
desktop and android report scripts share one copy and cannot drift — important
for ASSIGN_JS, which handles the user's GitHub token.
"""
import csv
import os

# GitHub usernames allowed to be assignees. Order is not significant
# (assignment is manual, not algorithmic). Enforced by the
# gha-validate-assignments workflow, which auto-reverts off-list assignees.
ASSIGNEES = ['rtanglao', 'lisajill', 'wsmwk', 'monica-thunderbird', 'madhattermattic']

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


SORT_JS = """
  const headers = document.querySelectorAll('th');
  const sortState = {};
  headers.forEach((th, col) => {
    th.style.cursor = 'pointer';
    th.addEventListener('click', () => {
      const tbody = th.closest('table').querySelector('tbody');
      const rows = Array.from(tbody.querySelectorAll('tr'));
      const asc = !sortState[col];
      sortState[col] = asc;
      rows.sort((a, b) => {
        const av = a.cells[col].dataset.sort ?? a.cells[col].textContent.trim();
        const bv = b.cells[col].dataset.sort ?? b.cells[col].textContent.trim();
        const an = parseFloat(av), bn = parseFloat(bv);
        if (!isNaN(an) && !isNaN(bn)) return asc ? an - bn : bn - an;
        return asc ? av.localeCompare(bv) : bv.localeCompare(av);
      });
      rows.forEach(r => tbody.appendChild(r));
      headers.forEach(h => { h.textContent = h.textContent.replace(/ [▲▼]$/, ''); });
      th.textContent += asc ? ' ▲' : ' ▼';
    });
  });
"""

HTML_CSS = """
  body { font-family: sans-serif; font-size: 13px; margin: 1em; }
  h1 { font-size: 1.2em; }
  table { border-collapse: collapse; width: 100%; }
  th, td { border: 1px solid #ccc; padding: 4px 8px; text-align: left; vertical-align: top; }
  th { background: #f0f0f0; user-select: none; white-space: nowrap; }
  th:hover { background: #ddd; }
  tr:nth-child(even) { background: #f9f9f9; }
  a { color: #0060df; }
  .assign-bar { margin: 0.5em 0; padding: 6px 8px; background: #f0f0f0; border: 1px solid #ccc; }
  .assign-bar > * { margin-right: 10px; }
  .assign-msg { color: #444; }
  .assign-cell { white-space: nowrap; }
  .assign-btn { font-size: 12px; cursor: pointer; }
  .assign-btn[disabled] { cursor: default; opacity: 0.6; }
"""

ASSIGN_JS = """
(function () {
  var cfg = window.TBQ || {};
  var TOKEN_KEY = 'tbq_gh_token';
  var me = null;
  var msgEl, statusEl, setBtn, clearBtn;

  function token() { return localStorage.getItem(TOKEN_KEY) || ''; }
  function msg(t, isErr) { if (msgEl) { msgEl.textContent = t || ''; msgEl.style.color = isErr ? '#b00' : '#444'; } }

  function api(method, url, body, tok) {
    var t = tok || token();
    var headers = { 'Accept': 'application/vnd.github+json' };
    if (t) headers['Authorization'] = 'Bearer ' + t;
    var opts = { method: method, headers: headers };
    if (body) { headers['Content-Type'] = 'application/json'; opts.body = JSON.stringify(body); }
    return fetch(url, opts);
  }

  // Soft scope guard: a correctly-scoped fine-grained token can see only this
  // repo, so GET /user/repos returns exactly it. More than one repo (or a
  // different one) means the token is broader than necessary -> reject it and
  // do not store it. Inconclusive checks warn but proceed. When opts.checkWrite
  // is set (on Set-token), also confirm the token can actually write.
  function validateToken(tok, opts) {
    opts = opts || {};
    return api('GET', 'https://api.github.com/user', null, tok).then(function (r) {
      if (!r.ok) throw new Error('Token rejected (authentication failed).');
      return r.json();
    }).then(function (user) {
      return api('GET', 'https://api.github.com/user/repos?per_page=2', null, tok).then(function (r) {
        if (!r.ok) return { login: user.login, warn: 'Could not verify token scope; proceeding.' };
        return r.json().then(function (repos) {
          if (!Array.isArray(repos)) return { login: user.login, warn: 'Could not verify token scope; proceeding.' };
          if (repos.length > 1) {
            throw new Error('Token has access to multiple repositories. Create a token scoped to ONLY ' + cfg.repo + ' (Contents: read & write).');
          }
          if (repos.length === 1 && (repos[0].full_name || '').toLowerCase() !== (cfg.repo || '').toLowerCase()) {
            throw new Error('Token is scoped to ' + repos[0].full_name + ', not ' + cfg.repo + '.');
          }
          if (repos.length === 0) {
            throw new Error('Token cannot access ' + cfg.repo + '. Grant Contents access to this repo.');
          }
          return { login: user.login };
        });
      }).then(function (result) {
        if (!opts.checkWrite) return result;
        return probeWrite(tok).then(function () { return result; });
      });
    });
  }

  // Reliable write check: attempt a contents PUT with a bogus SHA. GitHub
  // authorizes before validating the payload, so a token lacking Contents:write
  // returns 403, while a write-capable token is rejected for the SHA mismatch
  // (409/422) without writing anything. This tests the token's actual write
  // authorization on the real path -- unlike the GET /repos permissions.push
  // flag, which reflects the user's repo role rather than the token's grant.
  function probeWrite(tok) {
    return api('PUT', contentsUrl(), {
      message: 'write-permission probe (no change)',
      content: b64encode('probe'),
      sha: '0000000000000000000000000000000000000000',
      branch: cfg.branch
    }, tok).then(function (r) {
      if (r.status === 403) {
        throw new Error('Token cannot write to ' + cfg.repo + '. Set Contents: Read and write when creating the token.');
      }
      return true;
    });
  }

  function b64encode(s) { return btoa(unescape(encodeURIComponent(s))); }
  function b64decode(s) { return decodeURIComponent(escape(atob(s.replace(/\\s/g, '')))); }

  function contentsUrl() {
    return 'https://api.github.com/repos/' + cfg.repo + '/contents/' + cfg.path;
  }

  function parseCsv(text) {
    var lines = text.split(/\\r?\\n/);
    var header = lines.length ? lines[0] : 'question_id,assignee,assigned_at,assigned_by';
    var rows = [];
    for (var i = 1; i < lines.length; i++) {
      var line = lines[i];
      if (!line.trim()) continue;
      var parts = line.split(',');
      rows.push({
        qid: (parts[0] || '').trim(),
        assignee: (parts[1] || '').trim(),
        assigned_at: (parts[2] || '').trim(),
        assigned_by: (parts[3] || '').trim()
      });
    }
    return { header: header, rows: rows };
  }

  function serializeCsv(parsed) {
    var out = [parsed.header];
    parsed.rows.forEach(function (r) {
      out.push([r.qid, r.assignee, r.assigned_at, r.assigned_by].join(','));
    });
    return out.join('\\n') + '\\n';
  }

  function getContents() {
    return api('GET', contentsUrl() + '?ref=' + cfg.branch).then(function (r) {
      if (!r.ok) throw new Error('GET ' + r.status);
      return r.json();
    }).then(function (j) {
      return { parsed: parseCsv(b64decode(j.content)), sha: j.sha };
    });
  }

  function putContents(parsed, sha, message) {
    return api('PUT', contentsUrl(), {
      message: message,
      content: b64encode(serializeCsv(parsed)),
      sha: sha,
      branch: cfg.branch
    });
  }

  // action(parsed) -> string|null  (return error message to abort, or null to proceed)
  function commit(qid, action, message) {
    var attempt = 0;
    function tryOnce() {
      attempt++;
      return getContents().then(function (state) {
        var err = action(state.parsed);
        if (err) { msg(err, true); return false; }
        return putContents(state.parsed, state.sha, message).then(function (r) {
          if (r.status === 409 && attempt < 5) return tryOnce();
          if (!r.ok) throw new Error('PUT ' + r.status);
          return true;
        });
      });
    }
    return tryOnce();
  }

  function findRow(parsed, qid) {
    for (var i = 0; i < parsed.rows.length; i++) {
      if (parsed.rows[i].qid === String(qid)) return i;
    }
    return -1;
  }

  function claim(qid) {
    var now = new Date().toISOString();
    return commit(qid, function (parsed) {
      var i = findRow(parsed, qid);
      if (i >= 0 && parsed.rows[i].assignee) {
        if (parsed.rows[i].assignee === me) return null;
        return 'Already claimed by @' + parsed.rows[i].assignee;
      }
      if (i >= 0) { parsed.rows[i] = { qid: String(qid), assignee: me, assigned_at: now, assigned_by: me }; }
      else { parsed.rows.push({ qid: String(qid), assignee: me, assigned_at: now, assigned_by: me }); }
      return null;
    }, 'Claim question ' + qid + ' by ' + me);
  }

  function release(qid) {
    return commit(qid, function (parsed) {
      var i = findRow(parsed, qid);
      if (i < 0 || !parsed.rows[i].assignee) return null;
      if (parsed.rows[i].assignee !== me) return 'Not yours (claimed by @' + parsed.rows[i].assignee + ')';
      parsed.rows.splice(i, 1);
      return null;
    }, 'Release question ' + qid + ' by ' + me);
  }

  function renderButton(btn) {
    var qid = btn.getAttribute('data-qid');
    var assignee = btn.getAttribute('data-assignee') || '';
    var span = btn.parentNode.querySelector('.assignee');
    if (span) {
      span.innerHTML = assignee ? '<a href="https://github.com/' + assignee + '">@' + assignee + '</a>' : '';
    }
    btn.parentNode.setAttribute('data-sort', assignee);
    if (!me) { btn.textContent = assignee ? 'Claimed' : 'Claim'; btn.disabled = true; btn.title = 'Set your GitHub token to claim'; return; }
    btn.title = '';
    if (!assignee) { btn.textContent = 'Claim'; btn.disabled = false; }
    else if (assignee === me) { btn.textContent = 'Release'; btn.disabled = false; }
    else { btn.textContent = 'Claimed'; btn.disabled = true; }
  }

  function renderAll() {
    document.querySelectorAll('.assign-btn').forEach(renderButton);
  }

  function refreshStates() {
    if (!token()) return;
    getContents().then(function (state) {
      var map = {};
      state.parsed.rows.forEach(function (r) { if (r.assignee) map[r.qid] = r.assignee; });
      document.querySelectorAll('.assign-btn').forEach(function (btn) {
        btn.setAttribute('data-assignee', map[btn.getAttribute('data-qid')] || '');
      });
      renderAll();
    }).catch(function () { /* keep build-time state */ });
  }

  function onClick(e) {
    var btn = e.target.closest('.assign-btn');
    if (!btn || btn.disabled) return;
    var qid = btn.getAttribute('data-qid');
    var assignee = btn.getAttribute('data-assignee') || '';
    btn.disabled = true;
    msg('Working...');
    var p = (assignee === me) ? release(qid) : claim(qid);
    p.then(function (ok) {
      if (ok) { msg(''); }
      refreshStates();
    }).catch(function (err) {
      msg('Error: ' + err.message + ' (check your token)', true);
      renderAll();
    });
  }

  function updateAuthUI() {
    if (me) {
      statusEl.textContent = 'Signed in as @' + me;
      setBtn.style.display = 'none';
      clearBtn.style.display = '';
    } else {
      statusEl.textContent = 'Not signed in';
      setBtn.style.display = '';
      clearBtn.style.display = 'none';
    }
  }

  function loadMe() {
    if (!token()) { me = null; updateAuthUI(); renderAll(); return; }
    validateToken(token()).then(function (res) {
      me = res.login; updateAuthUI(); renderAll(); refreshStates();
      if (res.warn) msg(res.warn);
    }).catch(function (err) {
      localStorage.removeItem(TOKEN_KEY); me = null; updateAuthUI(); renderAll();
      msg(err.message, true);
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    msgEl = document.getElementById('assign-msg');
    statusEl = document.getElementById('auth-status');
    setBtn = document.getElementById('set-token');
    clearBtn = document.getElementById('clear-token');
    if (setBtn) setBtn.addEventListener('click', function () {
      var t = prompt('Paste a fine-grained GitHub token (this repo only, Contents: read & write):', '');
      if (!t) return;
      t = t.trim();
      msg('Validating token...');
      validateToken(t, { checkWrite: true }).then(function (res) {
        localStorage.setItem(TOKEN_KEY, t);
        me = res.login; updateAuthUI(); renderAll(); refreshStates();
        msg(res.warn || ('Signed in as @' + me));
      }).catch(function (err) {
        msg(err.message, true);
      });
    });
    if (clearBtn) clearBtn.addEventListener('click', function () {
      localStorage.removeItem(TOKEN_KEY); me = null; updateAuthUI(); renderAll();
    });
    document.addEventListener('click', onClick);
    loadMe();
  });
})();
"""
