"""Project 1 detection dictionaries (no AI — pure regex/keyword matching).

Ported from thunderbird/github-action-thunderbird-aaq/regexes.rb (the existing
emoji-tagging regexes), preserving the `os:` / `av:` / `m:` tag-name convention,
plus net-new PROTOCOL and ISP dimensions and regional providers (GMX, Telus)
that the Ruby file did not cover.

DESIGN NOTE (issue #70 decision — mail_provider only, no isp dimension):
  ISP-provided email (Comcast, BT, Free, Telstra…) IS a mail provider — a
  "@comcast.net" question is about Comcast *mail*, not Comcast *connectivity*.
  Many brands are BOTH an ISP and an email host; tagging them in two cause
  dimensions would double-report the same spike (v151×m:comcast AND
  v151×isp:comcast). So the separate `isp:` cause dimension was RETIRED and every
  email host — webmail and ISP-mail alike — lives in `mail_provider`, one tag per
  brand. The old Ruby hosting-folds (roadrunner→microsoft, att→yahoo) were
  stripped out into their own brand tags (m:spectrum, m:att) so brand identity
  survives (e.g. the validated v151 × spectrum cert spike).

All matching is case-insensitive (handled by the consumer with re.IGNORECASE).
Each dimension is a list of (tag_name, pattern) tuples; a question is tagged
with every tag whose pattern matches its title+content.
"""

# --- MAIL PROVIDERS — every email host in ONE dimension (webmail + ISP-mail).
# Sources: the original Ruby buckets (ISP-brand folds stripped into their own
# brand tags), Thunderbird's ISPDB (corpus-present entries), and named regionals.
# Word-/dot-anchored to limit false positives (validated on the corpus).
PROVIDER_PATTERNS = [
    # --- global webmail ---
    ("m:gmail", r"gmail|google ?mail"),
    ("m:microsoftemail",
     r"live(\.|-)*com|\bmsn\b|ms365|outlook|office ?365|hotmail|livemail|passport|"
     r"microsoft ?365|o365|ms 365|microsoft ?mail|ms ?exchange|"
     r"microsoft ?exchange|godaddy"),
    ("m:yahooemail", r"yahoo|\baol\b"),                 # AOL is Yahoo-hosted
    ("m:icloud", r"icloud|\bme\.com\b|\bmac\.com\b|@apple\.com"),
    ("m:protonmail", r"protonmail|proton\.me|pm\.me"),
    ("m:fastmail", r"fastmail\.fm|fastmail"),
    ("m:gmx", r"\bgmx\b"),
    ("m:webde", r"\bweb\.de\b"),
    ("m:mailcom", r"\bmail\.com\b"),                    # NOT gmail.com/hotmail.com (\b guards)
    ("m:zoho", r"\bzoho\b"),
    ("m:yandex", r"yandex"),
    ("m:mailru", r"mail\.ru"),
    ("m:tutanota", r"tutanota|\btuta\b|tuta\.(?:com|io)"),
    ("m:posteo", r"posteo"),
    ("m:mailfence", r"mailfence"),
    ("m:onecom", r"\bone\.com\b"),
    ("m:ovh", r"\bovh\b"),
    ("m:gandi", r"\bgandi\b"),
    # --- US ISP-provided email ---
    ("m:comcast", r"comcast|xfinity"),
    ("m:att", r"at&t|\batt\b|att\.net|ameritech|bellsouth|sbcglobal|pacbell|"
              r"\bswbell\b|\bsnet\b|prodigy|nvbell|currently\.com"),
    ("m:verizon", r"verizon|fios"),
    ("m:spectrum", r"spectrum|charter|time ?warner|\btwc\b|roadrunner|\brr\.com\b"),
    ("m:cox", r"\bcox\b"),
    ("m:centurylink", r"centurylink|lumen|\bqwest\b|centurytel"),
    ("m:earthlink", r"earthlink"),
    ("m:frontier", r"frontier"),
    ("m:windstream", r"windstream"),
    ("m:mediacom", r"mediacom"),
    ("m:optimum", r"optimum|altice|optonline"),
    # --- Canada ---
    ("m:telus", r"telus"),
    ("m:bell", r"\bbell\b|sympatico|bell\.net"),
    ("m:rogers", r"rogers"),
    ("m:shaw", r"\bshaw\b"),
    # --- UK / IE ---
    ("m:btinternet", r"btinternet|\bbt\b"),
    ("m:virginmedia", r"virgin ?media|ntlworld|blueyonder"),
    ("m:sky", r"\bsky\.com\b|sky ?broadband"),
    # --- France ---
    ("m:orange", r"\borange\b|wanadoo"),
    ("m:free_fr", r"\bfree\.fr\b"),
    ("m:sfr", r"\bsfr\b|sfr\.fr|neuf\.fr"),
    ("m:laposte", r"laposte"),
    # --- Germany / Austria / Switzerland ---
    ("m:tonline", r"t-online|telekom"),
    ("m:ionos", r"\bionos\b|1and1|1&1|1und1"),
    ("m:strato", r"\bstrato\b"),
    ("m:freenet", r"freenet"),
    ("m:vodafone", r"vodafone"),
    ("m:bluewin", r"bluewin|swisscom"),
    # --- Italy ---
    ("m:libero", r"\blibero\b"),
    ("m:tiscali", r"tiscali"),
    ("m:virgilio", r"\bvirgilio\b|\btim\.it\b|\btin\.it\b"),
    ("m:alice_it", r"\balice\.it\b"),
    ("m:fastweb", r"fastweb"),
    # --- Netherlands / Belgium ---
    ("m:ziggo", r"ziggo"),
    ("m:kpn", r"\bkpn\b|kpnmail"),
    ("m:skynet_be", r"skynet\.be|\bproximus\b"),
    # --- Central / Eastern Europe ---
    ("m:seznam", r"\bseznam\b|\bszn\.cz\b"),
    ("m:wppl", r"\bwp\.pl\b"),
    ("m:onet", r"\bonet\.pl\b|\bop\.pl\b"),
    # --- Australia / New Zealand ---
    ("m:bigpond", r"bigpond|telstra"),
    ("m:xtra_nz", r"\bxtra\b"),
]

# --- ANTIVIRUS — expanded from the Wikipedia antivirus category + corpus (#70).
# Ambiguous tokens anchored (g-data avoids "big data"; panda/360 need a qualifier;
# eset/avg/k7/vipre word-boundaried) to avoid false positives.
ANTIVIRUS_PATTERNS = [
    ("av:kaspersky", r"kaspersky"),
    ("av:bitdefender", r"bitdefender|gravityzone"),
    ("av:avast", r"avast|\bavg\b"),
    ("av:avira", r"avira"),
    ("av:zonealarm", r"zonealarm|zone alarm|checkpoint|check point|check-point"),
    ("av:comodo", r"comodo"),
    ("av:eset", r"\beset\b|nod32"),
    ("av:fsecure", r"fsecure|f-secure|f secure"),
    ("av:malwarebytes", r"malwarebytes"),
    ("av:mcafee", r"mcafee"),
    ("av:norton", r"norton|symantec"),
    ("av:sophos", r"sophos"),
    ("av:trendmicro", r"trend ?micro|titanium"),
    ("av:defender", r"\bdefender\b|security essentials"),
    # NET-NEW (issue #70)
    ("av:gdata", r"\bg[ -]?data\b"),
    ("av:surfshark", r"surfshark"),
    ("av:webroot", r"webroot"),
    ("av:emsisoft", r"emsisoft"),
    ("av:drweb", r"dr\.?web"),
    ("av:totalav", r"total ?av\b|totalav"),
    ("av:pcmatic", r"pc ?-?matic"),
    ("av:k7", r"\bk7\b"),
    ("av:vipre", r"\bvipre\b"),
    ("av:quickheal", r"quick ?heal"),
    ("av:clamav", r"clamx?av|clamwin|clamtk"),
    ("av:qihoo360", r"\bqihoo\b|360 ?(?:total ?security|safe|antivirus)"),
    ("av:iobit", r"iobit"),
    ("av:intego", r"\bintego\b"),
    ("av:mackeeper", r"mackeeper"),
    ("av:kingsoft", r"kingsoft"),
    ("av:cylance", r"cylance"),
    ("av:panda", r"panda ?(?:dome|cloud|security|antivirus|free)"),
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

# (ISP_PATTERNS retired — issue #70: ISP-provided email folded into mail_provider
# above; a separate isp cause dimension double-reported the same brand.)

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
