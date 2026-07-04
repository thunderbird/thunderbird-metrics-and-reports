"""Project 1 detection dictionaries (no AI — pure regex/keyword matching).

Ported from thunderbird/github-action-thunderbird-aaq/regexes.rb (the existing
emoji-tagging regexes), preserving the `os:` / `av:` / `m:` tag-name convention,
plus net-new PROTOCOL and ISP dimensions and regional providers (GMX, Telus)
that the Ruby file did not cover.

DESIGN NOTE (provider vs ISP):
  The Ruby provider buckets fold ISP-hosted mail into a provider bucket
  (e.g. roadrunner/spectrum/twc -> m:microsoftemail, att/bellsouth/sbcglobal ->
  m:yahooemail) because that is where the mail is actually hosted. Project 1
  also wants ISP mentions as their OWN dimension. So we keep the provider
  buckets verbatim AND detect ISP brands independently in ISP_PATTERNS — a
  question can legitimately be tagged in both. Whether to keep them split or
  strip ISP brands out of the provider buckets is a CHECKPOINT decision.

All matching is case-insensitive (handled by the consumer with re.IGNORECASE).
Each dimension is a list of (tag_name, pattern) tuples; a question is tagged
with every tag whose pattern matches its title+content.
"""

# --- MAIL PROVIDERS (hosting buckets) — ported verbatim, + GMX/Telus ----------
PROVIDER_PATTERNS = [
    ("m:gmail", r"gmail|google mail|googlemail"),
    ("m:microsoftemail",
     r"live(\.|-)*com|msn|ms365|outlook|office365|office 365|hotmail|livemail|"
     r"passport|microsoft365|microsoft 365|o365|ms 365|verizon|microsoft mail|"
     r"microsoftmail|timewarner|twc|godaddy|msexchange|ms exchange|"
     r"microsoft exchange|microsoftexchange|spectrum|time warner|roadrunner"),
    ("m:protonmail", r"protonmail|proton\.me|pm\.me"),
    ("m:fastmail", r"fastmail\.fm|fastmail"),
    ("m:yahooemail",
     r"yahoo|ameritech|at&t|att\.net|bellsouth|currently\.com|nvbell|pacbell|"
     r"prodigy|sbcglobal|snet|swbell|wans"),
    ("m:mailfence", r"mailfence"),
    # NET-NEW regional providers the user named explicitly:
    ("m:gmx", r"\bgmx\b"),
    ("m:telus", r"telus"),
]

# --- ANTIVIRUS — ported verbatim (14 vendors; user wants ~25, expand at CP) ----
# eset/avg word-boundaried to avoid 'reset'/'average' false positives.
ANTIVIRUS_PATTERNS = [
    ("av:kaspersky", r"kaspersky"),
    ("av:bitdefender", r"bitdefender"),
    ("av:avast", r"avast|\bavg\b"),
    ("av:avira", r"avira"),
    ("av:zonealarm", r"zonealarm|zone alarm|checkpoint|check point|check-point"),
    ("av:comodo", r"comodo"),
    ("av:eset", r"\beset\b|nod32"),
    ("av:fsecure", r"fsecure|f-secure|f secure"),
    ("av:malwarebytes", r"malwarebytes"),
    ("av:mcafee", r"mcafee"),
    ("av:norton", r"norton"),
    ("av:sophos", r"sophos"),
    ("av:trendmicro", r"trendmicro|titanium"),
    ("av:defender", r"\bdefender\b"),
]

# --- PROTOCOLS / email-specific terms — NET-NEW (user named JMAP/SMTP/IMAP/POP)
# POP is noisy (\bpop3?\b still matches the word "pop"); flagged at checkpoint.
PROTOCOL_PATTERNS = [
    ("proto:jmap", r"\bjmap\b"),
    ("proto:imap", r"\bimap\b"),
    ("proto:smtp", r"\bsmtp\b"),
    ("proto:pop", r"\bpop3\b|\bpop\b(?![\s-]*up)"),  # exclude 'pop up'/'pop-up'
    ("proto:oauth", r"\boauth2?\b"),
    ("proto:ews", r"\bews\b|exchange web services"),
    ("proto:carddav", r"carddav"),
    ("proto:caldav", r"caldav"),
]

# --- ISP brands — NET-NEW independent dimension (starter list, expand at CP) ---
ISP_PATTERNS = [
    ("isp:comcast", r"comcast|xfinity"),
    ("isp:verizon", r"verizon|fios"),
    ("isp:att", r"at&t|\batt\b|att\.net|ameritech|bellsouth|sbcglobal|"
                r"pacbell|\bswbell\b|\bsnet\b|prodigy|nvbell"),
    ("isp:spectrum", r"spectrum|charter|time warner|timewarner|\btwc\b|"
                     r"roadrunner|\brr\.com\b"),
    ("isp:cox", r"\bcox\b"),
    ("isp:centurylink", r"centurylink|lumen|\bqwest\b"),
    ("isp:frontier", r"frontier"),
    ("isp:windstream", r"windstream"),
    ("isp:mediacom", r"mediacom"),
    ("isp:optimum", r"optimum|altice|optonline"),
    ("isp:telus", r"telus"),
    ("isp:bell", r"\bbell\b|sympatico"),
    ("isp:rogers", r"rogers"),
    ("isp:shaw", r"\bshaw\b"),
    ("isp:btinternet", r"btinternet|\bbt\b"),
    ("isp:orange", r"\borange\b|wanadoo"),
    ("isp:freenet", r"freenet"),
    ("isp:tonline", r"t-online|telekom"),
]

# --- macOS RELEASES — NET-NEW per-release dimension (refines the os:macos
# FILTER; NOT a cause, so it does not feed the version×cause joint detector).
# Names + version numbers from the Wikipedia "Timeline of releases" table
# (10.0 Cheetah .. 27 Golden Gate). Newest first. In the Thunderbird support
# corpus a bare "Sonoma"/"Ventura"/"Sequoia" is almost always macOS, so
# word-boundaried name matching is safe enough; the ambiguous common-word ancient
# names (Cheetah/Puma/Tiger/Lion) are anchored to a "mac os x <name>" form or the
# 10.x number to avoid false positives. Lookbehinds keep "high sierra"/"snow
# leopard"/"mountain lion" from also matching the shorter Sierra/Leopard/Lion tags.
# Every 10.x number is anchored to a "mac os"/"os x" prefix — a BARE 10.N is a
# false-positive magnet (private IPs 10.0.0.0/8, unrelated version strings), as
# testing on the corpus confirmed. Modern 11-27 likewise require the "mac os"
# prefix (a bare "15" is meaningless). Distinctive marketing names match on their
# own; ambiguous common-word ancient names (Cheetah/Puma/Tiger/Lion) only match
# in an explicit "mac os x <name>" form.
MACOS_RELEASE_PATTERNS = [
    ("macos:golden_gate",   r"golden ?-?gate|mac ?os ?27\b"),
    ("macos:tahoe",         r"\btahoe\b|mac ?os ?26\b"),
    ("macos:sequoia",       r"\bsequoia\b|mac ?os ?(x ?)?15\b"),
    ("macos:sonoma",        r"\bsonoma\b|mac ?os ?(x ?)?14\b"),
    ("macos:ventura",       r"\bventura\b|mac ?os ?(x ?)?13\b"),
    ("macos:monterey",      r"\bmonterey\b|mac ?os ?(x ?)?12\b"),
    ("macos:big_sur",       r"big ?-?sur|mac ?os ?(x ?)?11\b"),
    ("macos:catalina",      r"\bcatalina\b|mac ?os ?x? ?10\.15\b"),
    ("macos:mojave",        r"\bmojave\b|mac ?os ?x? ?10\.14\b"),
    ("macos:high_sierra",   r"high ?-?sierra|mac ?os ?x? ?10\.13\b"),
    ("macos:sierra",        r"(?<!high[ -])\bsierra\b|mac ?os ?x? ?10\.12\b"),
    ("macos:el_capitan",    r"el ?-?capitan|mac ?os ?x? ?10\.11\b"),
    ("macos:yosemite",      r"\byosemite\b|mac ?os ?x? ?10\.10\b"),
    ("macos:mavericks",     r"\bmavericks\b|mac ?os ?x? ?10\.9\b"),
    ("macos:mountain_lion", r"mountain ?-?lion|mac ?os ?x? ?10\.8\b"),
    ("macos:lion",          r"mac ?os ?x ?lion|mac ?os ?x? ?10\.7\b"),
    ("macos:snow_leopard",  r"snow ?-?leopard|mac ?os ?x? ?10\.6\b"),
    ("macos:leopard",       r"(?<!snow[ -])\bleopard\b|mac ?os ?x? ?10\.5\b"),
    ("macos:tiger",         r"mac ?os ?x ?tiger|mac ?os ?x? ?10\.4\b"),
    ("macos:panther",       r"\bpanther\b|mac ?os ?x? ?10\.3\b"),
    ("macos:jaguar",        r"\bjaguar\b|mac ?os ?x? ?10\.2\b"),
    ("macos:puma",          r"mac ?os ?x ?puma|mac ?os ?x? ?10\.1\b"),
    ("macos:cheetah",       r"mac ?os ?x ?cheetah|mac ?os ?x? ?10\.0\b"),
]

# OS native-column -> tag normalization (regex fallback used only when the
# scraper's native operating_system value is blank).
OS_FALLBACK_PATTERNS = [
    ("os:macos",
     r"ventura|panther|snow ?-?leopard|leopard|jaguar|monterey|mavericks|"
     r"sonoma|high ?-?sierra|sierra|el ?-?capitan|mojave|catalina|big ?-?sur|"
     r"yosemite|sequoia|tahoe|golden ?-?gate|mountain ?-?lion|"
     r"mac ?-?os ?-?x?|osx|os-x"),
    ("os:linux", r"linux|ubuntu|redhat|debian|bsd"),
    ("os:windows",
     r"windows ?-?1[01]|windows ?-?[78]|win ?-?1[01]|win ?-?[78]|"
     r"windows1[01]|windows[78]|win1[01]|win[78]"),
]

DIMENSIONS = {
    "mail_provider": PROVIDER_PATTERNS,
    "isp": ISP_PATTERNS,
    "protocol": PROTOCOL_PATTERNS,
    "av": ANTIVIRUS_PATTERNS,
    "macos_release": MACOS_RELEASE_PATTERNS,
}


def normalize_os(native_value):
    """Map the scraper's native operating_system string to an os: tag.
    Returns a tag string or '' if unrecognized/blank."""
    v = (native_value or "").strip().lower()
    if not v:
        return ""
    if "android" in v:
        return "os:android"
    if v.startswith("win") or "windows" in v:
        return "os:windows"
    if "mac" in v or "osx" in v or "os x" in v:
        return "os:macos"
    if any(k in v for k in ("linux", "ubuntu", "debian", "fedora", "bsd")):
        return "os:linux"
    return "os:other"
