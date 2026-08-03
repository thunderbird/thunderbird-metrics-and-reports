"""Guard against SILENTLY corrupted markdown tables in the generated reports.

Kramdown (GitHub Pages) does not raise or warn when a table is malformed — it
degrades the whole block to paragraphs. A page can therefore lose every table it
has and still "build fine", which is exactly what shipped on 2026-08-03: an
unescaped backtick in a SUMO question title ("won`t download e-mail from
xfinity") opened a code span that ran past the end of its row, ate the pipes of
following rows until it paired with a later backtick (every spike row carries
two, from the sparkline), and collapsed both spike tables to literal pipe text.

That bug is invisible to the obvious checks: kramdown reported zero warnings, and
a table COUNT passes a page that lost two of them. It also only manifests when
particular rows co-occur, so any single row renders fine in isolation.

So this checks the structure directly, per table block:
  1. every row has the same cell count as the separator row (after code spans are
     removed, since pipes inside `...` are not cell separators);
  2. no row has unbalanced backticks (an odd count = a code span leaking into the
     following rows — the actual failure above);
  3. a blank line precedes the block (kramdown requires it).

Pure stdlib, no Ruby needed, so it runs in the Python workflows that generate the
reports. If `ruby -rkramdown` happens to be available it ALSO does the
authoritative render cross-check (separator rows in source == <table> in HTML,
and no "<p>|" in the output); that is skipped silently when Ruby isn't there.

  uv run scripts/check_report_render.py PROJECT1/REPORTS/desktop/*.md
Exit status is non-zero if any file fails, so it can gate a workflow.
"""
import re
import sys
import glob
import subprocess

SEP_RE = re.compile(r"^\|[-:\s|]+\|\s*$")
CODE_SPAN_RE = re.compile(r"`[^`]*`")
FRONT_MATTER_RE = re.compile(r"\A---.*?---\n", re.DOTALL)


def cells(line):
    """Cell count of a table row, ignoring pipes inside code spans (`…`), which
    are literal text rather than separators."""
    return CODE_SPAN_RE.sub("", line).count("|")


def check_structure(path):
    """-> list of human-readable problems (empty = clean)."""
    lines = FRONT_MATTER_RE.sub("", open(path).read()).split("\n")
    problems, i, blocks = [], 0, 0
    while i < len(lines):
        if not SEP_RE.match(lines[i]) or i == 0 or not lines[i - 1].startswith("|"):
            i += 1
            continue
        # found a separator; the block is header + separator + following | rows
        blocks += 1
        start = i - 1
        if start == 0 or lines[start - 1].strip():
            problems.append(f"line {start+1}: no blank line before the table block "
                            f"(kramdown will not parse it as a table)")
        want = cells(lines[i])
        end = i + 1
        while end < len(lines) and lines[end].startswith("|"):
            end += 1
        for n in range(start, end):
            row = lines[n]
            if row.count("`") % 2:
                problems.append(
                    f"line {n+1}: unbalanced backtick ({row.count('`')}) — a code "
                    f"span will leak into the following rows and collapse the "
                    f"table. Route SUMO text through md_safe(). Row starts: "
                    f"{row[:60]!r}")
            got = cells(row)
            if got != want:
                problems.append(f"line {n+1}: {got} cells, separator has {want} — "
                                f"row starts: {row[:60]!r}")
        i = end
    if not blocks:
        problems.append("no table blocks found — did the report generate?")
    return problems


def check_kramdown(paths):
    """Authoritative render check, when Ruby + kramdown are installed.
    -> (list of problems, ran?)"""
    script = r'''
      require "kramdown"; require "kramdown-parser-gfm"
      ARGV.each do |f|
        s = File.read(f).sub(/\A---.*?---\n/m, "")
        h = Kramdown::Document.new(s, input: "GFM").to_html
        want = s.lines.count { |l| l =~ /^\|[-:\s|]+\|\s*$/ }
        got  = h.scan(/<table/).size
        leak = h.scan(/<p>\|[^<\n]{0,60}/)
        puts "#{f}\t#{want}\t#{got}\t#{leak.size}\t#{leak.first.to_s[0, 70]}"
      end'''
    try:
        r = subprocess.run(["ruby", "-e", script, *paths],
                           capture_output=True, text=True, timeout=120)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return [], False
    if r.returncode:
        return [], False
    problems = []
    for line in r.stdout.strip().split("\n"):
        f, want, got, leaks, sample = (line.split("\t") + [""])[:5]
        if want != got or leaks != "0":
            problems.append(f"{f}: {want} tables in source but {got} rendered, "
                            f"{leaks} leaked as paragraphs {sample!r}")
    return problems, True


def main():
    paths = sorted(p for a in (sys.argv[1:] or ["PROJECT1/REPORTS/**/*.md"])
                   for p in glob.glob(a, recursive=True))
    if not paths:
        sys.exit("no markdown files matched")
    failed = 0
    for p in paths:
        problems = check_structure(p)
        print(f"{'FAIL' if problems else 'ok  '} {p}")
        for msg in problems:
            print(f"       {msg}")
        failed += bool(problems)
    kd, ran = check_kramdown(paths)
    print(f"--- kramdown render cross-check: "
          f"{'clean' if ran and not kd else 'FAILED' if ran else 'skipped (no ruby/kramdown)'}")
    for msg in kd:
        print(f"       {msg}")
    failed += len(kd)
    if failed:
        sys.exit(f"{failed} problem(s) — pages would render with missing tables")
    print(f"all {len(paths)} page(s) render every table")


if __name__ == "__main__":
    main()
