#!/usr/bin/env python3
"""Builds the three NRCRA prototypes (v1, v2, v3) and the dashboard from one content source.
Run from the repo root:  python3 tools/build.py

v1  Rounded blocks          (Milou's drafts + Waves for Water: colour cards, pill rows, navy hero panel)
v2  Light and fresh         (the R.A.C.K app, Resilient Lismore, Investing for Charity: pastel bands, photos)
v3  Big visuals             (Farm Africa, The Children's Society: big people photos, circle crops, warm blocks)
"""
import html, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = html.escape
IMG = "../assets/img/"
SL = "../assets/sample-logos/"

# ================================================================ content
VIMEO = "https://player.vimeo.com/video/1238627190?h=85714a045a&autoplay=1"
VIMEO_PAGE = "https://vimeo.com/1238627190/85714a045a"
CONTACT = dict(name="Kathie Heyman", email="kathieh@nrcra.org.au", phone="0417 683 546", tel="0417683546")
LINKS = dict(
    fb="https://www.facebook.com/profile.php?id=61585141283356",
    li="https://www.linkedin.com/company/northern-rivers-community-resilience-alliance/?viewAsMember=true",
    wa="https://chat.whatsapp.com/Im7jik2wja81c3w35m3nvr",
    news="https://www.nrcra.org.au/news",
    live="https://www.nrcra.org.au",
)
PAGES = [("home", "Home"), ("about", "About"), ("partners", "Partners"), ("network", "Network"), ("rack", "R.A.C.K")]

H1 = "A growing movement of grassroots community groups building disaster resilience across the Northern Rivers"
WHO = "Since early 2024, more than 60 groups and organisations across the Northern Rivers have joined together to form the Resilience Alliance, a community-led network focused on collective care, preparedness and regional strength."
MORE = "Neighbours became first responders in 2022. Today, those neighbours are building the systems that will protect communities before the next disaster. The Alliance connects prepared communities to each other, sharing knowledge, reducing duplication and making sure no group is doing it alone."
CALLOUT = "Communities know their people, places and strengths. We connect them."
VISION = "Connected, collaborative Northern Rivers communities that are empowered to care for themselves and each other before, during and after disasters."
PURPOSE = "To develop a self-sustaining, trusted Alliance of place-based, community-led resilience groups and organisations. The Alliance shares knowledge and resources, provides mutual support and wellbeing, takes collective action and advocates for identified community needs."
ACK = "The Northern Rivers Community Resilience Alliance acknowledges the Traditional Custodians of the lands and waters on which we live and work: the Bundjalung, Arakwal, Githabul, Yaegl and Gumbaynggirr peoples. We recognise their enduring connection to Country, and their continuing cultures and communities. We pay our respects to Elders past and present."
VALUES = [
    ("Connect", "We connect 60+ community resilience groups across the region so local leaders can find each other, share resources and act together.", "teal"),
    ("Share", "We share knowledge, training and practical tools across the network so every community benefits from what others have learned.", "yellow"),
    ("Care", "We care for the people doing this work: reducing the load on volunteers, removing duplication and supporting community-led resilience.", "orange"),
]
FROM_TO = (["Dependence", "Fragmented organisations", "Competition for funding", "Isolated communities"],
           ["Cooperation", "Shared knowledge", "Local leadership", "Connected communities"])
PILLARS = [
    ("Grow the Alliance", "Welcoming more place-based groups so no group works alone.", "grow"),
    ("Training and resource sharing", "Practical tools, templates and learning passed group to group.", "book"),
    ("Peer support and self care", "Looking after the people who look after their communities.", "heart"),
    ("Funding and collective projects", "Participatory grants and shared projects, decided locally.", "seed"),
    ("Advocacy", "A stronger collective voice in funding, policy and planning.", "mega"),
]
STATS = [("60+", "grassroots groups and organisations"), ("7", "local government areas"), ("3", "projects under way"), ("$800,000", "HELP Fund grants program, over two years")]
PROJECTS = [
    ("Connected and Prepared", "Governance, capacity building and shared digital tools.", "Disaster Ready Fund, 2026 to 2027"),
    ("Resourcing Community Resilience", "Participatory grantmaking, decided by locals.", "NRMA Insurance HELP Fund with partners, 2026 to 2027"),
    ("Learning Together (MEAL)", "Monitoring, Evaluation and Learning with embedded researchers.", "University Centre for Rural Health"),
]
GATHER = ("27 Nov", "Alliance Gathering, Phase 1", "Location to be confirmed")
JOURNEY = [
    ("2022", "After the floods and landslides, groups across the Northern Rivers organised locally and connections began to grow. Research found that grassroots groups wanted peer-to-peer support."),
    ("2024", "The Resilience Alliance took shape, with the University Centre for Rural Health (UCRH) as embedded researchers documenting progress along the way."),
    ("2025", "UCRH completed the first Resilience Alliance Health Check and shared findings with groups in the network."),
    ("2026", "Connected and Prepared brings a Monitoring, Evaluation and Learning Framework and Implementation Plan."),
    ("2027 to 2028", "Research and MEAL continue alongside the Alliance as it supports and resources groups in the network."),
]
MEAL = ["Connect", "Listen", "Reflect", "Improve", "Share", "Strengthen"]
QUOTE = ("It's cutting edge. I don't really know whether this sort of thing has been tried before, certainly for community disaster response groups.", "Alliance participant")
FAQ = [
    ("How is the Alliance different from Community Resilience Networks?", "Community Resilience Networks are hosted by councils in each local government area. The Alliance is a region-wide network that sits outside formal structures, a flexible space for independent grassroots groups to share practical solutions and build capacity."),
    ("How is the Alliance different from Plan C?", "Plan C trains people directly and is one of our valued member organisations. The Alliance is a network of networks: it connects groups, helps them share what they know and gives them a stronger collective voice."),
]
# The R.A.C.K, from NRCRA's own R.A.C.K app (mood board screenshots, Oct 2026)
RACK_NAME = "Resilience Alliance Community Knowledge"
RACK_LINE = "One shared place where the whole network can find what already works."
RACK_INTRO = "Years of real community experience across the Northern Rivers. Find templates and guides you can use straight away, and contribute knowledge back in two minutes."
RACKS = [("Get Ready", 3, "Plans and checklists for before a disaster."), ("Emergency", 5, "What to do and who to call when it happens."),
         ("Volunteers", 14, "Registering, inducting and looking after volunteers."), ("Run Your Group", 12, "Governance, templates and running a healthy group."),
         ("Training & Workshops", 6, "Workshops and learning for group leaders.")]
FILES = [
    ("d", "Community Emergency Hub Guide", "Get Ready", "Dec 2025"), ("s", "Volunteer registration form", "Volunteers", "Sample"),
    ("d", "Inducting volunteers who turn up on the day", "Volunteers", "Sample"), ("p", "Mullumbimby evacuation map", "Emergency", "Sample"),
    ("s", "Resilience Address Book", "Run Your Group", "Jan 2026"), ("s", "One Calendar (regional shared calendar)", "Run Your Group", "Jan 2026"),
    ("p", "Connecting for Impact, UCRH report", "Training & Workshops", "Dec 2025"), ("d", "Group governance template", "Run Your Group", "Sample"),
]
ICONS = {"d": "DOC", "s": "SHEET", "p": "PDF", "f": "FOLDER"}
# Sample directory rows: names are placeholders, not real groups.
DIR = [("Sample group A", "Lismore", "Peer support and self care"), ("Sample group B", "Byron", "Training and resource sharing"),
       ("Sample group C", "Tweed", "Funding and collective projects"), ("Sample group D", "Ballina", "Grow the Alliance"),
       ("Sample group E", "Kyogle", "Advocacy"), ("Sample group F", "Richmond Valley", "Peer support and self care")]
LGAS = ["Tweed", "Byron", "Ballina", "Lismore", "Kyogle", "Richmond Valley", "Clarence Valley"]
MAP_SRC = "https://maps.google.com/maps?q=Northern%20Rivers%20NSW&z=8&output=embed"

# Places hit by the 2022 floods (sources: AIDR, Lismore City Council, Risk Frontiers, NSW Community Resilience Grants).
# (name, lat, lon, label side: r, l or none)
PLACES = [
    ("Tweed", [("Murwillumbah", -28.327, 153.394, "l"), ("South Murwillumbah", -28.338, 153.405, ""), ("Tumbulgum", -28.276, 153.464, "r"), ("Uki", -28.414, 153.336, "l")]),
    ("Byron", [("Mullumbimby", -28.552, 153.500, "l"), ("Billinudgel", -28.504, 153.528, "l"), ("South Golden Beach", -28.497, 153.546, "")]),
    ("Ballina", [("Ballina", -28.866, 153.565, "l"), ("Wardell", -28.953, 153.463, "r")]),
    ("Lismore", [("Lismore CBD", -28.811, 153.278, "r"), ("North Lismore", -28.797, 153.268, ""), ("South Lismore", -28.822, 153.262, "")]),
    ("Richmond Valley", [("Casino", -28.866, 153.048, "l"), ("Coraki", -28.990, 153.288, "r"), ("Bungawalbin", -29.045, 153.240, "l"), ("Woodburn", -29.072, 153.343, "r"), ("Broadwater", -29.013, 153.433, "r")]),
    ("Kyogle", [("Kyogle", -28.620, 153.003, "r")]),
    ("Clarence Valley", [("Grafton", -29.690, 152.933, "r")]),
]
PLACES_SRC = "Towns named in 2022 flood reports by AIDR, Lismore City Council and Risk Frontiers. NRCRA's member list will add every place where Alliance groups work."

# PLACEHOLDER ONLY: logos borrowed from worldnomads.com "Who we fund" to show the layout. Not NRCRA partners.
SAMPLE = [
    ("adventuretravelconservationfund-logo-600x390.png", "Adventure Travel Conservation Fund"), ("wildlifeconservationnetwork-logo-600x390.png", "Wildlife Conservation Network"),
    ("anza-logo-600x390.png", "Anza"), ("abercrombiekentphilanthropy-logo-600x390.png", "Abercrombie & Kent Philanthropy"),
    ("plan-logo-600x390-v2.png", "Plan International"), ("seaturtleconservancy-logo-600x390.png", "Sea Turtle Conservancy"),
    ("surfaid-logo-600x390.png", "SurfAid"), ("fredhollows-logo-600x390.png", "The Fred Hollows Foundation"),
    ("worldexpeditions-logo-600x390.png", "World Expeditions Foundation"), ("wateraid-primary-logo-600px-390px.png", "WaterAid"),
    ("savethechildren-logo-600x390.png", "Save the Children"), ("ahf-logo.png", "The Australian Himalayan Foundation"),
]
SAMPLE_GROUPS = [("Funders", "Whose funding makes this work possible.", SAMPLE[0:4]), ("Delivery partners", "Who we build and deliver programs with.", SAMPLE[4:8]), ("Research partners", "Who listens, reflects and tracks change alongside us.", SAMPLE[8:12])]
PARTNER_LINE = "Our partners have helped the Alliance grow from one part-time coordinator to a regional team of six, fund Connected and Prepared, bring $800,000 in participatory grants to local groups and keep learning with researchers from the University Centre for Rural Health."
# Waves for Water style section: what each kind of partner made possible (logos are placeholders)
WFW = [("Funding for Connected and Prepared, 2026 to 2027", 0), ("Helped establish and grow the Alliance", 1), ("$800,000 for participatory grants over two years", 2), ("Embedded research and Health Checks", 3)]
REAL = "Disaster Ready Fund, FRRR, NRMA Insurance HELP Fund, NSW Government, Northern Rivers Community Foundation, Resilient Lismore, Plan C, University Centre for Rural Health, Monash University"

ALT = dict(
    cheer="Alliance members cheering with raised arms in front of a school building.",
    group="A large group of Alliance members posing together on the lawn.",
    crowd="People gathered outdoors listening beneath trees at a gathering.",
    laughing="Members laughing together around a workshop table.",
    listening="Participants listening closely at a long table.",
    table="Two members talking at a workshop table.",
    speaker="A speaker with a microphone addressing a full room.",
    aerial="A wide view of members spread across a hillside lawn.",
    line="Members standing in a long line on the lawn during an activity.",
    web="Members holding a web of string in a circle on the grass.",
    cards="Members moving between coloured cards laid on the ground.",
    board="Members adding sticky notes to a planning whiteboard.",
    hug="Two community members sharing a hug.",
    meeting="A small team meeting around a table with a screen.",
    house="Members sitting on the lawn outside a brick hall.",
    pair="Two participants in conversation at a table.",
    circle="Members sitting together, smiling, in a bright room.",
    talk="Three members talking closely at a gathering.",
    audience="Members listening in a crowded room.",
    board2="Members working together at a whiteboard covered in sticky notes.",
    cards2="Members walking between coloured cards laid out on the ground.",
    hall="A full hall of members working at tables.",
    lab="Members talking together in a bright room.",
    workshop="Members talking around a workshop table.",
)
FILE = dict(cheer="group-cheer", group="group-photo", crowd="crowd", laughing="laughing", listening="listening", table="table", speaker="speaker",
            aerial="aerial", line="line", web="web", cards="cards", board="board", hug="hug", meeting="meeting", house="house", pair="pair",
            circle="circle", talk="talk", audience="audience", board2="board2", cards2="cards2", hall="hall", lab="lab", workshop="workshop")


# ================================================================ helpers
def img(key, cls="", eager=False, alt=None):
    a = ALT[key] if alt is None else alt
    return f'<img src="{IMG}{FILE[key]}.jpg" alt="{E(a)}" class="{cls}" loading="{"eager" if eager else "lazy"}" decoding="async">'


def logo(cls="logo", white=False):
    return f'<img src="{IMG}logo.png" alt="Northern Rivers Community Resilience Alliance" class="{cls}{" logo-white" if white else ""}" width="260" height="60">'


def screen(id_, label, body, cls=""):
    return f'<section id="{id_}" data-screen data-label="{label}" class="page {cls}" tabindex="-1" aria-label="{label}">{body}</section>'


def nav():
    items = "".join(f'<a href="#{k}" data-nav="{k}">{E(t)}</a>' for k, t in PAGES)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap head-in">
<a href="#home" class="brand" aria-label="NRCRA home">{logo()}</a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav id="nav" aria-label="Main">{items}<a class="btn btn-cta" href="#network">Join the network</a></nav>
</div></header>'''


def footer(white_logo=True):
    return f'''<footer class="site-foot"><div class="wrap foot-in">
<div>{logo("logo", white_logo)}<p class="tag">Connect. Share. Care.</p></div>
<div><h2>Contact</h2><p>Network Lead<br><strong>{CONTACT["name"]}</strong><br><a href="mailto:{CONTACT["email"]}">{CONTACT["email"]}</a><br><a href="tel:{CONTACT["tel"]}">{CONTACT["phone"]}</a></p></div>
<div><h2>Follow</h2><ul class="plain"><li><a href="{LINKS["fb"]}">Facebook</a></li><li><a href="{LINKS["li"]}">LinkedIn</a></li><li><a href="{LINKS["wa"]}">WhatsApp group</a></li><li><a href="{LINKS["news"]}">Resilience Roundup newsletter</a></li></ul></div>
<p class="ack">{ACK}</p><p class="copy">© 2026 Northern Rivers Community Resilience Alliance. <a href="{LINKS["live"]}">nrcra.org.au</a></p>
</div></footer>'''


def video(poster="group", cls="video"):
    return f'''<div class="{cls}" data-video="{VIMEO}">{img(poster, alt="")}
<button class="play" aria-label="Play the Alliance sizzle reel video"><span aria-hidden="true">&#9654;</span></button></div>
<p class="vnote"><a href="{VIMEO_PAGE}">Watch on Vimeo</a></p>'''


def stats(cls="stats"):
    return f'<dl class="{cls}">' + "".join(f"<div><dt>{n}</dt><dd>{t}</dd></div>" for n, t in STATS) + "</dl>"


def icon(name, cls="ico"):
    p = {
        "grow": '<path d="M24 42V22"/><path d="M24 24c0-8 6-13 14-13 0 8-6 13-14 13z"/><path d="M24 30c0-6-5-10-12-10 0 6 5 10 12 10z"/>',
        "book": '<path d="M8 12h12a4 4 0 0 1 4 4v24a3 3 0 0 0-3-3H8z"/><path d="M40 12H28a4 4 0 0 0-4 4v24a3 3 0 0 1 3-3h13z"/>',
        "heart": '<path d="M24 40S8 30 8 19a8 8 0 0 1 16-3 8 8 0 0 1 16 3c0 11-16 21-16 21z"/>',
        "seed": '<circle cx="24" cy="18" r="9"/><path d="M24 27v13"/><path d="M14 40h20"/>',
        "mega": '<path d="M10 20v8h6l14 8V12l-14 8z"/><path d="M36 18a8 8 0 0 1 0 12"/>',
        "people": '<circle cx="16" cy="16" r="5"/><circle cx="32" cy="16" r="5"/><path d="M6 38c0-7 4-12 10-12s10 5 10 12"/><path d="M22 38c0-7 4-12 10-12s10 5 10 12"/>',
        "share": '<circle cx="12" cy="24" r="5"/><circle cx="36" cy="12" r="5"/><circle cx="36" cy="36" r="5"/><path d="M17 22l14-8M17 26l14 8"/>',
        "cal": '<rect x="8" y="12" width="32" height="28" rx="5"/><path d="M8 20h32M16 8v8M32 8v8"/>',
        "hand": '<path d="M14 26V14a3 3 0 0 1 6 0v10M20 22V10a3 3 0 0 1 6 0v12M26 22v-9a3 3 0 0 1 6 0v13c0 8-5 14-12 14-5 0-8-3-10-7l-4-8a3 3 0 0 1 5-3l3 4"/>',
        "connect": '<circle cx="24" cy="24" r="6"/><circle cx="10" cy="10" r="4"/><circle cx="38" cy="10" r="4"/><circle cx="10" cy="38" r="4"/><circle cx="38" cy="38" r="4"/><path d="M13 13l7 7M35 13l-7 7M13 35l7-7M35 35l-7-7"/>',
    }[name]
    return f'<svg class="{cls}" viewBox="0 0 48 48" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'


def pillars_list(cls="pillars", icons=False):
    return f'<ol class="{cls}">' + "".join(f'<li>{icon(k) if icons else ""}<h3>{E(t)}</h3><p>{E(d)}</p></li>' for t, d, k in PILLARS) + "</ol>"


def values_cards(cls="values"):
    ic = {"Connect": "connect", "Share": "share", "Care": "heart"}
    return f'<ul class="{cls}">' + "".join(f'<li class="val val-{c}">{icon(ic[t])}<h3>{t}</h3><p>{E(d)}</p></li>' for t, d, c in VALUES) + "</ul>"


def from_to():
    f, t = FROM_TO
    return f'''<div class="fromto"><div class="ft-from"><h3>From</h3><ul>{"".join(f"<li>{x}</li>" for x in f)}</ul></div>
<div class="ft-arrow" aria-hidden="true">&rarr;</div><div class="ft-to"><h3>To</h3><ul>{"".join(f"<li>{x}</li>" for x in t)}</ul></div></div>'''


def partner_tile(file, name):
    return f'<li class="ptile"><a href="#partners"><span class="plogo"><img src="{SL}{file}" alt="{E(name)}" loading="lazy"></span><span class="pname">{E(name)}</span><span class="pnote">Sample partner, placeholder logo</span></a></li>'


def partner_groups(cls="pgroups"):
    out = f'<div class="{cls}"><p class="lede" style="margin-bottom:20px">{PARTNER_LINE}</p><p class="note"><b>Placeholder partners.</b> These logos are borrowed from another site to show the layout. They are not NRCRA partners. Real partners to be shown here: {REAL}.</p>'
    for title, intro, items in SAMPLE_GROUPS:
        out += f'<section class="pgroup"><h3>{E(title)}</h3><p class="lede-s">{E(intro)}</p><ul class="pgrid">' + "".join(partner_tile(*i) for i in items) + "</ul></section>"
    return out + "</div>"


def wfw_partners():
    def item(i):
        cap, li = WFW[i]
        f, n = SAMPLE[[0, 4, 9, 10][li]]
        return f'<li><span class="wn">0{i + 1}</span><img src="{SL}{f}" alt="{E(n)} (sample logo)" loading="lazy"><span class="wbar" aria-hidden="true"></span><p>{E(cap)}</p></li>'
    return f'''<div class="wfw"><p class="wfw-eye">Thanks to our partners</p><div class="wfw-grid">
<ul class="wfw-col">{item(0)}{item(1)}</ul><div class="wfw-mid">{img("hug", alt="")}<h2>Our partners</h2></div><ul class="wfw-col">{item(2)}{item(3)}</ul></div>
<p class="wfw-line">{PARTNER_LINE}</p><p class="btnrow wfw-btns"><a class="btn btn-primary" href="#partners">View all partners</a><a class="btn btn-ghost" href="mailto:{CONTACT["email"]}">Become a partner</a></p>
<p class="vnote" style="text-align:center">Placeholder logos. The captions show what NRCRA's real partners have made possible.</p></div>'''


def partner_strip():
    return '<ul class="strip">' + "".join(f'<li><a href="#partners"><img src="{SL}{f}" alt="{E(n)} (sample logo)" loading="lazy"></a></li>' for f, n in SAMPLE[:6]) + "</ul>"


def projects_cards(cls="cards"):
    return f'<ul class="{cls}">' + "".join(f'<li class="pcard"><h3>{E(t)}</h3><p>{E(d)}</p><p class="meta">{E(m)}</p></li>' for t, d, m in PROJECTS) + "</ul>"


def journey(cls="journey"):
    return f'<ol class="{cls}">' + "".join(f"<li><b>{y}</b><p>{E(t)}</p></li>" for y, t in JOURNEY) + "</ol>"


def meal(cls="meal"):
    return f'<ol class="{cls}">' + "".join(f"<li>{m}</li>" for m in MEAL) + "</ol>"


def faq():
    return '<div class="faq">' + "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in FAQ) + "</div>"


def quote(cls="quote"):
    return f'<blockquote class="{cls}"><p>&ldquo;{QUOTE[0]}&rdquo;</p><cite>{QUOTE[1]}</cite></blockquote>'


def cta_band():
    return f'<p class="btnrow"><a class="btn btn-primary" href="#network">Find a group near you</a><a class="btn btn-ghost" href="{LINKS["wa"]}">Join the WhatsApp group</a><a class="btn btn-ghost" href="mailto:{CONTACT["email"]}">Email the Network Lead</a></p>'


NET_H1 = "60+ grassroots, place-based groups across the Northern Rivers, working across five pillars."


def network_body(card="card", pcls="pcols", sec_alt=""):
    return f'''<section class="sec"><div class="wrap">{map_embed()}</div></section>
<section class="sec {sec_alt}"><div class="wrap"><h2>Five pillars</h2><p class="lede">Each pillar, and the groups in the network working on it.</p>{pillar_cols(pcls, groups=True)}</div></section>
<section class="sec"><div class="wrap"><div class="{card}"><h2>All groups</h2>{directory()}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="{card} narrow">{contact_form()}</div></div></section>'''


def rack_buttons():
    return '<p class="btnrow"><a class="btn btn-primary" href="#rack-open">Open the R.A.C.K</a><a class="btn btn-ghost" href="#rack-signup">Request access</a><a class="btn btn-ghost" href="#rack-signin">Sign in</a></p>'


def rack_list(cls="racks"):
    return f'<ol class="{cls}">' + "".join(f'<li><span class="rn">{i}</span><div><h3>{E(t)}</h3><p>{E(d)}</p></div><span class="rc">{c} resources</span></li>' for i, (t, c, d) in enumerate(RACKS, 1)) + "</ol>"


# Sample groups per pillar (placeholders, real names come from the Alliance member list)
PILLAR_GROUPS = {
    "Grow the Alliance": [("Sample group A", "Murwillumbah", "Tweed"), ("Sample group B", "Kyogle", "Kyogle"), ("Sample group C", "Grafton", "Clarence Valley")],
    "Training and resource sharing": [("Sample group D", "Mullumbimby", "Byron"), ("Sample group E", "Lismore", "Lismore"), ("Sample group F", "Casino", "Richmond Valley")],
    "Peer support and self care": [("Sample group G", "Wardell", "Ballina"), ("Sample group H", "Uki", "Tweed"), ("Sample group I", "North Lismore", "Lismore")],
    "Funding and collective projects": [("Sample group J", "Woodburn", "Richmond Valley"), ("Sample group K", "Ballina", "Ballina"), ("Sample group L", "Billinudgel", "Byron")],
    "Advocacy": [("Sample group M", "Coraki", "Richmond Valley"), ("Sample group N", "South Lismore", "Lismore"), ("Sample group O", "Tumbulgum", "Tweed")],
}


def pillar_cols(cls="pcols", photos=None, groups=False):
    """The five pillars drawn as pillars: arched columns standing on a shared base."""
    out = f'<div class="pcwrap"><ol class="{cls}">'
    for i, (t, d, k) in enumerate(PILLARS):
        ph = f'<div class="pc-ph">{img(photos[i])}</div>' if photos else ""
        gr = ""
        if groups:
            gr = '<ul class="pc-groups">' + "".join(f'<li><b>{E(n)}</b><span>{a}</span></li>' for n, a, l in PILLAR_GROUPS[t]) + "</ul>"
        out += f'<li class="pc">{ph}<span class="pc-ico">{icon(k)}</span><span class="pc-n">{i + 1:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p>{gr}</li>'
    return out + '</ol><div class="pc-base" aria-hidden="true"></div></div>'


def logo_grid():
    tiles = "".join(f'<li><img src="{SL}{f}" alt="{E(n)}" title="{E(n)}" loading="lazy"></li>' for f, n in SAMPLE)
    return f'<ul class="lgrid">{tiles}</ul><p class="vnote">Placeholder logos borrowed from another site to show the layout. Real partners: {REAL}.</p>'


def map_embed():
    return f'''<div class="mapbox"><iframe title="Map of resilience groups across the Northern Rivers" src="{MAP_SRC}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
<p class="vnote">Placeholder map of the region. In the build this is the Alliance's own Google Map, with a pin for each member group.</p>'''


def directory():
    items = "".join(f'<li data-lga="{l}" data-pillar="{E(p)}"><b>{E(n)}</b><span>{a}, {l}</span><em>{E(p)}</em></li>' for p, gs in PILLAR_GROUPS.items() for n, a, l in gs)
    lopts = "".join(f"<option>{l}</option>" for l in LGAS)
    popts = "".join(f"<option>{E(p[0])}</option>" for p in PILLARS)
    return f'''<div class="dir"><div class="filters">
<label>Location <select data-f="lga"><option value="">All locations</option>{lopts}</select></label>
<label>Pillar <select data-f="pillar"><option value="">All pillars</option>{popts}</select></label>
<label class="dq">Search <input type="search" data-f="q" placeholder="Group name or town"></label></div>
<ul class="gdir">{items}</ul><p class="empty" hidden>No groups match those filters.</p><p class="vnote">Sample groups. Real names and areas come from the Alliance member list.</p></div>'''


def contact_form():
    return '''<form class="cform" onsubmit="event.preventDefault();this.querySelector('.sent').hidden=false">
<h3>Get in touch</h3>
<label>Name<input required autocomplete="name"></label>
<label>Email<input type="email" required autocomplete="email"></label>
<label>Group name (optional)<input></label>
<label>Message<textarea rows="4" required></textarea></label>
<button class="btn btn-primary" type="submit">Send</button>
<p class="sent" role="status" hidden>Prototype only: nothing was sent.</p></form>'''


# ---------------------------------------------------------------- places map (drawn, Wix: upload as SVG vector art or use Google Maps pins)
LON0, LON1, LAT0, LAT1, MW, MH = 152.80, 153.74, -28.12, -29.78, 380, 680


def xy(lat, lon):
    return round((lon - LON0) / (LON1 - LON0) * MW, 1), round((LAT0 - lat) / (LAT0 - LAT1) * MH, 1)


def pts(seq):
    return " ".join("%s,%s" % xy(a, b) for a, b in seq)


COAST = [(-28.12, 153.54), (-28.17, 153.55), (-28.26, 153.58), (-28.39, 153.57), (-28.50, 153.556), (-28.54, 153.56), (-28.64, 153.64), (-28.70, 153.61),
         (-28.79, 153.598), (-28.87, 153.594), (-28.95, 153.55), (-29.03, 153.48), (-29.11, 153.436), (-29.25, 153.40), (-29.41, 153.366), (-29.44, 153.36),
         (-29.60, 153.33), (-29.78, 153.27)]
RIVERS = [
    [(-28.414, 153.336), (-28.327, 153.394), (-28.276, 153.464), (-28.18, 153.55)],
    [(-28.552, 153.500), (-28.54, 153.558)],
    [(-28.66, 153.36), (-28.811, 153.278), (-28.990, 153.288)],
    [(-28.620, 153.003), (-28.866, 153.048), (-28.990, 153.288), (-29.072, 153.343), (-29.013, 153.433), (-28.953, 153.463), (-28.870, 153.594)],
    [(-29.55, 152.83), (-29.690, 152.933), (-29.60, 153.06), (-29.46, 153.20), (-29.43, 153.362)],
]
LGA_LBL = [("Tweed", -28.22, 153.20), ("Byron", -28.66, 153.47), ("Kyogle", -28.45, 152.86), ("Lismore", -28.70, 153.14), ("Ballina", -28.80, 153.44),
           ("Richmond Valley", -29.20, 153.02), ("Clarence Valley", -29.52, 152.86)]


_MAPN = [0]


def places_map(cls="pmap"):
    _MAPN[0] += 1
    mid = f"pmt{_MAPN[0]}"
    land = pts([(LAT0, LON0)] + COAST + [(LAT1, LON0)])
    rivers = "".join(f'<polyline class="river" points="{pts(r)}"/>' for r in RIVERS)
    lgas = "".join('<text class="lga" x="%s" y="%s">%s</text>' % (*xy(a, b), E(n)) for n, a, b in LGA_LBL)
    dots = ""
    for lga, items in PLACES:
        for name, lat, lon, side in items:
            x, y = xy(lat, lon)
            lbl = ""
            if side:
                tx = x + 9 if side == "r" else x - 9
                lbl = f'<text class="lbl" x="{tx}" y="{y + 4}" text-anchor="{"start" if side == "r" else "end"}">{E(name.replace(" CBD", ""))}</text>'
            dots += f'<g class="dot" data-place="{E(name)}"><title>{E(name)}, {lga}</title><circle cx="{x}" cy="{y}" r="6"/>{lbl}</g>'
    return f'''<figure class="{cls}"><svg viewBox="0 0 {MW} {MH}" role="img" aria-labelledby="{mid}"><title id="{mid}">Drawn map of the Northern Rivers showing towns hit by the 2022 floods</title>
<rect class="sea" width="{MW}" height="{MH}"/><polygon class="land" points="{land}"/><polyline class="coast" points="{pts(COAST)}"/>{rivers}{lgas}{dots}</svg></figure>'''


def places_list(cls="places"):
    out = f'<div class="{cls}">'
    for lga, items in PLACES:
        out += f'<div class="pl-lga"><h3>{lga}</h3><ul>' + "".join(f'<li><button type="button" data-place="{E(n)}">{E(n)}</button></li>' for n, *_ in items) + "</ul></div>"
    return out + f'<p class="vnote">{PLACES_SRC}</p></div>'


def places_block(title="Where we are", intro="Alliance groups work in the towns the 2022 floods hit hardest. Tap a town to find it on the map."):
    return f'<div class="placesblk"><div class="pb-text"><h2>{title}</h2><p>{intro}</p>{places_list()}</div><div class="pb-map">{places_map()}</div></div>'


# ---------------------------------------------------------------- R.A.C.K mock (styled after the real R.A.C.K app)
def rack_head():
    return f'''<div class="rk-head"><div class="rk-brand"><svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="9" r="4" fill="#f05a28"/><circle cx="9" cy="15" r="3" fill="#ffcb2a"/><circle cx="31" cy="15" r="3" fill="#00a79d"/><path d="M8 34c3-10 7-16 12-16s9 6 12 16" fill="none" stroke="#f05a28" stroke-width="5" stroke-linecap="round"/></svg>
<div><b>{RACK_NAME}</b><span class="rk-tag"><i class="t">Connect.</i> <i class="y">Share.</i> <i class="o">Care.</i></span></div><span class="rk-badge">RACK</span></div>
<div class="rk-tools"><a class="rk-pill" href="#home">Resilience Alliance site</a><a class="rk-share" href="#rack-signin">Share Knowledge</a></div></div>'''


def rack_screens():
    note = '<p class="note"><b>Prototype mock.</b> This stands in for the real R.A.C.K until the live links are supplied. Nothing is sent or stored.</p>'
    cats = "".join(f'<li><a href="#rack-open"><span class="c">{c}</span><b>{E(t)}</b></a></li>' for t, c, _ in RACKS)
    rows = "".join(f'<tr><th scope="row"><span class="ic {k}" aria-hidden="true">{ICONS[k]}</span>{E(n)}</th><td>{E(c)}</td><td>{m}</td></tr>' for k, n, c, m in FILES)
    signin = f'''<div class="rk">{note}{rack_head()}<div class="rk-auth"><h1>Sign in to the R.A.C.K</h1><p>For groups in the Resilience Alliance.</p>
<form onsubmit="event.preventDefault();location.hash='rack-open'"><label>Email<input type="email" required autocomplete="email"></label><label>Password<input type="password" required autocomplete="current-password"></label>
<button class="rk-btn" type="submit">Sign in</button></form><p class="rk-alt">New to the R.A.C.K? <a href="#rack-signup">Request access</a></p></div></div>'''
    signup = f'''<div class="rk">{note}{rack_head()}<div class="rk-auth"><h1>Request access to the R.A.C.K</h1><p>Access is for Alliance groups. The Network Lead approves new requests.</p>
<form onsubmit="event.preventDefault();this.querySelector('.sent').hidden=false"><label>Your name<input required autocomplete="name"></label><label>Email<input type="email" required autocomplete="email"></label>
<label>Community group or organisation<input required></label><label>Town or locality<input required></label><button class="rk-btn" type="submit">Request access</button><p class="sent" role="status" hidden>Prototype only: nothing was sent. In the build, the Network Lead is notified.</p></form>
<p class="rk-alt">Already have access? <a href="#rack-signin">Sign in</a></p></div></div>'''
    hub = f'''<div class="rk">{note}{rack_head()}
<p class="rk-tabs"><a class="on" href="#rack-open">Full RACK <span>40</span></a><a href="#rack-open">MY RACK <span>0</span></a><a href="#rack-open">Ask RACK <span>LIVE</span></a></p>
<h1 class="rk-h1">{RACK_LINE}</h1><p class="rk-lede">{RACK_INTRO}</p>
<p class="rk-sos" role="note">For life-threatening emergencies, call Triple Zero (000) immediately.</p>
<div class="rk-search"><input type="search" aria-label="Search the R.A.C.K" placeholder="Search guides, templates, forms or towns (e.g. evacuation map, volunteers, Mullumbimby)">
<label>Town or locality <select><option>All towns (Northern Rivers wide)</option>{"".join(f"<option>{n}</option>" for _, it in PLACES for n, *_ in it)}</select></label></div>
<h2 class="rk-sub">Resource categories</h2><ul class="rk-cats"><li class="all"><a href="#rack-open"><span class="c">40</span><b>Full RACK</b></a></li>{cats}</ul>
<div class="rk-files"><table><caption>Sample file list. Real contents live in the R.A.C.K.</caption><thead><tr><th scope="col">Name</th><th scope="col">Category</th><th scope="col">Updated</th></tr></thead><tbody>{rows}</tbody></table></div></div>'''
    return screen("rack-signin", "R.A.C.K sign in", signin, "rkpage") + screen("rack-signup", "R.A.C.K request access", signup, "rkpage") + screen("rack-open", "R.A.C.K workspace", hub, "rkpage")


# ================================================================ shared css + js
BASE = """
:root{--navy:#07293b;--teal:#00a79d;--orange:#f05a28;--yellow:#ffcb2a;--teal-d:#006b64;--orange-d:#b93a0c;--ink:#07293b;--muted:#3d5663;--line:#d6e2e4;
--font:"Nunito Sans",Arial,sans-serif;--wrap:1180px;--r:24px;
/* Tint rule: brand colour mixed with white. Text sits on tints (navy text) or on navy (white text). Full brand colour is for buttons, icons, borders and shapes. */
--teal-12:#e0f4f3;--teal-25:#bfe9e7;--blue-15:#d9e9f2;--grey-6:#eef1f3;--yellow-20:#fff5d4;--yellow-40:#ffeaaa;--orange-12:#fdebe5;--orange-25:#fbd6c9;--navy-8:#ebeef0}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font:400 18px/1.6 var(--font);color:var(--ink);background:var(--bg,#fff)}
img{max-width:100%;display:block}a{color:var(--teal-d)}a:hover{color:var(--navy)}
h1,h2,h3{line-height:1.12;margin:0 0 .5em;font-weight:800;letter-spacing:-.01em}
h1{font-size:clamp(2rem,4.6vw,3.5rem);font-weight:900}h2{font-size:clamp(1.6rem,3.2vw,2.4rem)}h3{font-size:1.2rem}
p{margin:0 0 1em}.wrap{max-width:var(--wrap);margin:0 auto;padding:0 20px}.sec{padding:64px 0}
:focus-visible{outline:3px solid var(--orange-d);outline-offset:3px}
.skip{position:absolute;left:-999px;top:8px;background:var(--yellow);color:var(--navy);padding:10px 16px;z-index:100;font-weight:800}.skip:focus{left:8px}
.plain{list-style:none;margin:0;padding:0}.vnote{font-size:.85rem;color:var(--muted);margin-top:.6em}.vnote a{color:inherit}
.eyebrow{display:block;font-weight:900;text-transform:uppercase;letter-spacing:.12em;font-size:.8rem;margin-bottom:.8em;color:var(--teal-d)}
.lede{font-size:1.2rem;max-width:62ch}.lede-s{color:var(--muted)}
.note{background:#fff8e1;border:2px dashed var(--orange-d);border-radius:14px;padding:10px 14px;font-size:.9rem;margin:0 0 24px;color:var(--navy)}
.btn{display:inline-flex;align-items:center;justify-content:center;font:800 1rem var(--font);padding:.75em 1.4em;text-decoration:none;border:2px solid var(--navy);border-radius:var(--btn-r,99px);cursor:pointer;min-height:44px}
.btn-primary{background:var(--yellow);color:var(--navy);border-color:var(--yellow)}.btn-primary:hover{background:var(--navy);color:#fff;border-color:var(--navy)}
.btn-ghost{background:transparent;color:var(--navy)}.btn-ghost:hover{background:var(--navy);color:#fff}
.btn-cta{background:var(--navy);color:#fff;padding:.5em 1.1em}.btn-cta:hover{background:var(--teal-d);color:#fff;border-color:var(--teal-d)}
.btnrow{display:flex;flex-wrap:wrap;gap:12px;margin:1.2em 0 0}
.site-head{background:#fff;position:sticky;top:0;z-index:50;border-bottom:1px solid var(--line)}
.head-in{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-top:10px;padding-bottom:10px}
.logo{height:48px;width:auto}.logo-white{filter:brightness(0) invert(1)}
#nav{display:flex;align-items:center;gap:4px;flex-wrap:wrap}
#nav a:not(.btn){padding:.45em .9em;color:var(--navy);text-decoration:none;font-weight:700;border-radius:var(--btn-r,99px)}
#nav a:not(.btn):hover{background:var(--hover,#eef5f5)}#nav a[aria-current=page]{background:var(--current,#d8f0ee)}
.menu-btn{display:none;font:800 1rem var(--font);background:var(--navy);color:#fff;border:0;padding:.7em 1.1em;min-height:44px;border-radius:99px}
@media(max-width:860px){.menu-btn{display:block}#nav{display:none;position:absolute;left:0;right:0;top:100%;background:#fff;flex-direction:column;align-items:stretch;padding:12px 20px 20px;border-bottom:1px solid var(--line)}#nav.open{display:flex}.logo{height:40px}}
.page{display:none;outline:0}.page.on{display:block}
.split{display:grid;grid-template-columns:1.05fr .95fr;gap:48px;align-items:center}@media(max-width:860px){.split{grid-template-columns:1fr;gap:28px}}
.split>*,.placesblk>*,.intro1>*{min-width:0}.dir{overflow-x:auto}.r{border-radius:var(--r);overflow:hidden}.photo{width:100%;height:100%;object-fit:cover;border-radius:var(--r)}
ul.cards{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:20px;margin:0}.stats div{margin:0}
.stats dt{font-size:clamp(2.2rem,4.6vw,3.3rem);font-weight:900;line-height:1}.stats dd{margin:.35em 0 0;font-weight:600}
.ico{width:44px;height:44px;display:block}
.pillars{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px}.pillars h3{margin:.3em 0}.pillars p{margin:0}
.values{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px}.values p{margin:0}
.fromto{display:grid;grid-template-columns:1fr auto 1fr;gap:16px;align-items:stretch}.fromto>div{border-radius:var(--r);padding:28px}.fromto ul{margin:0;padding-left:1.1em}
.ft-arrow{display:grid;place-items:center;font-size:2.4rem;font-weight:900;padding:0 10px!important}@media(max-width:700px){.fromto{grid-template-columns:1fr}.ft-arrow{transform:rotate(90deg)}}
.video{position:relative;aspect-ratio:16/9;background:var(--navy);overflow:hidden;border-radius:var(--r)}.video img,.video iframe{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;border:0}
.play{position:absolute;inset:0;margin:auto;width:84px;height:84px;border-radius:50%;border:0;background:var(--yellow);color:var(--navy);font-size:1.8rem;cursor:pointer;display:grid;place-items:center;padding-left:6px;box-shadow:0 6px 20px rgba(0,0,0,.25)}.play:hover{background:#fff}
.pgrid{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:18px}
.ptile a{display:flex;flex-direction:column;height:100%;text-decoration:none;color:var(--navy);padding:14px;border:1px solid var(--line);background:#fff;border-radius:20px}
.ptile a:hover{border-color:var(--navy)}.plogo{display:grid;place-items:center;height:130px;background:#fff;margin-bottom:10px;border-radius:14px;padding:8px}
.plogo img{max-height:100%;width:auto;max-width:100%;object-fit:contain}.pname{font-weight:800}.pnote{font-size:.9rem;color:var(--muted)}.pgroup{margin-bottom:44px}
.strip{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:12px}.strip a{display:grid;place-items:center;background:#fff;border:1px solid var(--line);border-radius:16px;padding:6px 12px}
.strip img{height:60px;width:auto;max-width:140px;object-fit:contain}
.pcard,.gcard,.rcard{list-style:none;padding:24px;border-radius:var(--r)}.meta{font-size:.9rem;margin:0;color:var(--muted)}
.journey{list-style:none;margin:0;padding:0;display:grid;gap:14px}.journey li{display:grid;grid-template-columns:130px 1fr;gap:16px;align-items:start}.journey b{font-size:1.4rem;font-weight:900}.journey p{margin:0}
@media(max-width:600px){.journey li{grid-template-columns:1fr;gap:2px}}
.meal{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:10px}.meal li{padding:.55em 1.2em;font-weight:800;border-radius:99px;background:#fff;color:var(--navy);border:2px solid var(--navy)}
.faq details{border-bottom:1px solid var(--line);padding:14px 0}.faq summary{cursor:pointer;font-weight:800}.faq details p{margin:.6em 0 0}
.quote{margin:0}.quote p{font-size:clamp(1.3rem,2.6vw,1.9rem);font-weight:800;line-height:1.35;margin:0}.quote cite{display:block;font-style:normal;font-weight:600;margin-top:.8em}
.mapbox{width:100%;height:clamp(320px,48vw,560px);background:#eef5f5;border-radius:var(--r);overflow:hidden}.mapbox iframe{width:100%;height:100%;border:0}
.dir table{width:100%;border-collapse:collapse}.dir caption{text-align:left;font-size:.85rem;color:var(--muted);padding-bottom:8px}
.dir th,.dir td{text-align:left;padding:12px;border-bottom:1px solid var(--line)}.filters{display:flex;flex-wrap:wrap;gap:16px;margin-bottom:16px}
.filters label,.cform label,.rk-auth label,.rk-search label{display:flex;flex-direction:column;font-weight:700;gap:4px}
select,input,textarea{font:inherit;padding:.6em .8em;border:2px solid var(--navy);background:#fff;color:var(--navy);min-height:44px;border-radius:12px}
.cform{display:grid;gap:14px}main{overflow-x:clip}
.pcwrap{position:relative}.pcols{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(5,1fr);gap:14px;align-items:stretch}
.pc{position:relative;overflow:hidden;border-radius:999px 999px 18px 18px;padding:44px 18px 26px;text-align:center;display:flex;flex-direction:column;align-items:center;min-height:380px;color:var(--navy)}
.pc-ico{width:56px;height:56px;border-radius:50%;background:#fff;display:grid;place-items:center;margin-bottom:10px;color:var(--navy)}.pc-ico .ico{width:30px;height:30px}
.pc-n{font-weight:900;font-size:.85rem;letter-spacing:.1em;opacity:.8}.pc h3{font-size:1.1rem;margin:.3em 0}.pc p{margin:0;font-size:.95rem}
.pc-ph{width:calc(100% + 36px);margin:-44px -18px 16px;aspect-ratio:1}.pc-ph img{width:100%;height:100%;object-fit:cover}.pc-ph+.pc-ico{margin-top:-44px;position:relative;box-shadow:0 4px 12px -6px rgba(7,41,59,.4)}
.pc-groups{list-style:none;margin:16px 0 0;padding:0;display:grid;gap:8px;width:100%}.pc-groups li{background:rgba(255,255,255,.75);border-radius:12px;padding:8px 10px;text-align:left;font-size:.9rem}.pc-groups b{display:block}.pc-groups span{color:var(--muted)}
.pc-base{height:18px;border-radius:12px;margin-top:10px;background:var(--navy-8)}
@media(max-width:980px){.pcols{grid-template-columns:repeat(3,1fr)}}@media(max-width:640px){.pcols{grid-template-columns:1fr 1fr}.pc{min-height:0;border-radius:160px 160px 16px 16px}}@media(max-width:420px){.pcols{grid-template-columns:1fr}}
.dq{flex:1;min-width:200px}.dq input{width:100%}
.gdir{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}.gdir li{background:var(--grey-6);border-radius:16px;padding:14px 16px;display:flex;flex-direction:column;gap:2px}
.gdir b{font-size:1rem}.gdir span{color:var(--muted);font-size:.9rem}.gdir em{font-style:normal;font-size:.8rem;font-weight:800;margin-top:6px;color:var(--teal-d)}
.lgrid{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:16px}
.lgrid li{background:#fff;border:1px solid var(--line);border-radius:var(--r);aspect-ratio:3/2;display:grid;place-items:center;padding:18px}.lgrid img{max-width:100%;max-height:100%;object-fit:contain}
/* places */
.placesblk{display:grid;grid-template-columns:1fr 380px;gap:40px;align-items:start}@media(max-width:900px){.placesblk{grid-template-columns:1fr}.pb-map{max-width:420px}}
.pmap{margin:0}.pmap svg{width:100%;height:auto;display:block;border-radius:var(--r)}
.pmap .sea{fill:var(--sea,#dff1f6)}.pmap .land{fill:var(--land,#f4f7ef)}.pmap .coast{fill:none;stroke:var(--coast,#9cc9c4);stroke-width:2}
.pmap .river{fill:none;stroke:var(--river,#7fc4e0);stroke-width:3;stroke-linecap:round;stroke-linejoin:round}
.pmap .lga{font:800 11px var(--font);fill:var(--lga,#6c8590);text-transform:uppercase;letter-spacing:.08em}
.pmap .dot circle{fill:var(--dot,#f05a28);stroke:#fff;stroke-width:2;transition:r .2s}.pmap .lbl{font:700 12px var(--font);fill:var(--navy)}
.pmap .dot.hot circle{r:10;fill:var(--hot,#07293b)}.pmap .dot.hot .lbl{font-weight:900}
.places .pl-lga{margin-bottom:12px}.places h3{font-size:.85rem;text-transform:uppercase;letter-spacing:.1em;margin:0 0 6px;color:var(--muted)}
.places ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:8px}
.places button{font:700 .95rem var(--font);padding:.35em .9em;border-radius:99px;border:2px solid var(--chip,#cfe3e1);background:#fff;color:var(--navy);cursor:pointer;min-height:36px}
.places button:hover,.places button[aria-pressed=true]{background:var(--navy);border-color:var(--navy);color:#fff}
/* footer */
.site-foot{background:var(--foot,#07293b);color:var(--foot-ink,#fff);padding:52px 0 32px}.site-foot a{color:inherit}
.site-foot h2{font-size:.9rem;text-transform:uppercase;letter-spacing:.12em;color:var(--foot-h,#ffcb2a)}
.foot-in{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:32px}.foot-in .ack{grid-column:1/-1;font-size:.9rem;border-top:1px solid var(--foot-line,#35566a);padding-top:20px;margin:0;max-width:90ch}
.foot-in .copy{grid-column:1/-1;font-size:.85rem;margin:0}.foot-in .tag{margin-top:12px;font-weight:800;color:var(--foot-h,#ffcb2a)}.site-foot .logo{height:54px}
/* R.A.C.K mock (its own look, shared by all prototypes) */
.rkpage{background:#f7f9fa}.rk{max-width:1100px;margin:0 auto;padding:32px 20px 72px}
.rk-head{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:14px;padding:14px 0 18px;border-bottom:1px solid var(--line);margin-bottom:24px}
.rk-brand{display:flex;align-items:center;gap:10px}.rk-brand svg{width:40px;height:40px}.rk-brand b{display:block;font-size:1.05rem;line-height:1.2}
.rk-tag{font-size:.8rem;font-weight:800}.rk-tag i{font-style:normal}.rk-tag .t{color:var(--teal-d)}.rk-tag .y{color:#8a6a00}.rk-tag .o{color:var(--orange-d)}
.rk-badge{background:var(--teal-d);color:#fff;font-weight:900;padding:.2em .6em;border-radius:8px;letter-spacing:.06em}
.rk-tools{display:flex;gap:10px;flex-wrap:wrap}.rk-pill{border:1px solid var(--line);border-radius:99px;padding:.45em 1em;font-weight:700;font-size:.9rem;text-decoration:none;color:var(--navy);background:#fff}
.rk-share{background:#f5b301;color:var(--navy);border-radius:12px;padding:.5em 1.1em;font-weight:800;text-decoration:none;box-shadow:0 3px 0 #c98f00}
.rk-tabs{display:flex;gap:10px;flex-wrap:wrap}.rk-tabs a{border-radius:12px;padding:.5em 1em;font-weight:800;text-decoration:none;color:#fff;background:var(--navy)}
.rk-tabs a:nth-child(2){background:var(--orange-d)}.rk-tabs a:nth-child(3){background:var(--teal-d)}.rk-tabs span{background:rgba(0,0,0,.3);border-radius:99px;padding:0 .5em;margin-left:6px;font-size:.85rem}
.rk-h1{font-size:clamp(1.7rem,3.4vw,2.4rem);max-width:24ch;margin-top:18px}.rk-lede{color:var(--muted);max-width:64ch}
.rk-sos{background:#fde2df;border:1px solid #f3b4ac;color:#8c1d12;border-radius:12px;padding:12px 16px;font-weight:800}
.rk-search{background:#fff;border:1px solid var(--line);border-radius:18px;padding:18px;display:grid;gap:14px;margin-bottom:24px}.rk-search input{width:100%}
.rk-sub{font-size:.85rem;text-transform:uppercase;letter-spacing:.1em;color:var(--muted)}
.rk-cats{list-style:none;margin:0 0 24px;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px}
.rk-cats a{display:block;background:#fff;border:1px solid var(--line);border-left:5px solid var(--teal);border-radius:12px;padding:12px 14px;text-decoration:none;color:var(--navy)}
.rk-cats li:nth-child(3n) a{border-left-color:var(--orange)}.rk-cats li:nth-child(3n+1) a{border-left-color:var(--yellow)}.rk-cats .all a{background:var(--navy);color:#fff;border-left-color:var(--navy)}
.rk-cats .c{float:right;font-size:.8rem;font-weight:800;background:#eef3f4;color:var(--navy);border-radius:99px;padding:0 .5em}.rk-cats b{display:block;margin-top:14px}
.rk-files{background:#fff;border:1px solid var(--line);border-radius:18px;padding:12px 18px;overflow-x:auto}.rk-files table{width:100%;border-collapse:collapse;min-width:460px}
.rk-files caption{text-align:left;font-size:.85rem;color:var(--muted);padding:6px 0}.rk-files th,.rk-files td{text-align:left;padding:11px 8px;border-bottom:1px solid var(--line);font-size:.95rem}
.ic{display:inline-block;min-width:3.2em;text-align:center;font-size:.7rem;font-weight:800;padding:.15em .4em;border-radius:5px;color:#fff;margin-right:8px}.ic.d{background:#1a56b8}.ic.s{background:#146c2e}.ic.p{background:#b3261e}.ic.f{background:#4a5560}
.rk-auth{max-width:460px;margin:12px auto 0;background:#fff;border:1px solid var(--line);border-radius:20px;padding:32px;box-shadow:0 6px 24px rgba(7,41,59,.08)}
.rk-auth h1{font-size:1.7rem}.rk-auth form{display:grid;gap:14px}.rk-btn{font:800 1rem var(--font);background:var(--teal-d);color:#fff;border:0;border-radius:12px;padding:.8em;cursor:pointer;min-height:44px}.rk-btn:hover{background:var(--navy)}.rk-alt{margin:16px 0 0;font-size:.95rem}
/* prototype bar: fixed, deliberately outside the brand so it never reads as part of the design */
body{padding-bottom:72px}.protobar{position:fixed;left:0;right:0;bottom:0;z-index:90;background:#111;color:#fff;font:600 14px/1.3 var(--font);box-shadow:0 -4px 16px rgba(0,0,0,.25)}
.pb-in{max-width:var(--wrap);margin:0 auto;padding:10px 20px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.pb-label{margin:0;flex:1;min-width:200px}.pb-label b{color:#ffcb2a;letter-spacing:.06em}.pb-cur{color:#ddd}.pb-label a{color:#fff}
.pb-nav{display:flex;gap:8px;flex-wrap:wrap}.pb-btn,.pb-top{font:700 13px var(--font);color:#fff;background:#2b2b2b;border:1px solid #555;border-radius:99px;padding:.55em 1em;text-decoration:none;cursor:pointer;min-height:36px;display:inline-flex;align-items:center}
.pb-btn:hover,.pb-top:hover{background:#ffcb2a;color:#111;border-color:#ffcb2a}.pb-top{background:#ffcb2a;color:#111;border-color:#ffcb2a}
.pb-short{display:none}
@media(max-width:760px){body{padding-bottom:64px}.pb-in{gap:6px;padding:8px 10px;flex-wrap:nowrap}.pb-label{min-width:0;font-size:11px;line-height:1.25}.pb-cur,.pb-long,.pb-all{display:none}.pb-short{display:inline}.pb-btn,.pb-top{padding:.5em .8em;min-width:40px;justify-content:center}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.pmap .dot circle{transition:none}}
"""

JS = """
(function(){
var S=[].slice.call(document.querySelectorAll('[data-screen]')),ids=S.map(function(s){return s.id});
function route(){var h=(location.hash||'#home').slice(1);if(ids.indexOf(h)<0)return;var nk=h.indexOf('rack')===0?'rack':h;
S.forEach(function(s){s.classList.toggle('on',s.id===h)});
[].forEach.call(document.querySelectorAll('[data-nav]'),function(a){if(a.getAttribute('data-nav')===nk)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')});
var cur=document.getElementById(h);document.title=cur.getAttribute('data-label')+' | NRCRA prototype';window.scrollTo(0,0);if(window.__navd)cur.focus({preventScroll:true});window.__navd=1;
[].forEach.call(document.querySelectorAll('[data-proto]'),function(a){a.href='../'+a.getAttribute('data-proto')+'/#'+h});
document.getElementById('nav').classList.remove('open');document.querySelector('.menu-btn').setAttribute('aria-expanded','false')}
window.addEventListener('hashchange',route);route();
if(/shot/.test(location.search)){var pb=document.querySelector('.protobar');if(pb)pb.remove();document.body.style.paddingBottom='0'}
var mb=document.querySelector('.menu-btn');mb.addEventListener('click',function(){var o=document.getElementById('nav').classList.toggle('open');mb.setAttribute('aria-expanded',o)});
document.addEventListener('click',function(e){
 var v=e.target.closest('[data-video]');if(v&&e.target.closest('.play')){var f=document.createElement('iframe');f.src=v.getAttribute('data-video');f.title='NRCRA sizzle reel';f.allow='autoplay; fullscreen; picture-in-picture';f.allowFullscreen=true;v.innerHTML='';v.appendChild(f);return}
 var b=e.target.closest('.places button');if(b){var blk=b.closest('.placesblk')||document,on=b.getAttribute('aria-pressed')!=='true';
  [].forEach.call(blk.querySelectorAll('.places button'),function(x){x.setAttribute('aria-pressed','false')});
  [].forEach.call(blk.querySelectorAll('.dot'),function(d){d.classList.toggle('hot',on&&d.getAttribute('data-place')===b.getAttribute('data-place'))});
  if(on)b.setAttribute('aria-pressed','true')}});
[].forEach.call(document.querySelectorAll('.places button'),function(b){b.setAttribute('aria-pressed','false')});
[].forEach.call(document.querySelectorAll('.dir'),function(d){function ap(){var l=d.querySelector('[data-f=lga]').value,p=d.querySelector('[data-f=pillar]').value,q=d.querySelector('[data-f=q]').value.trim().toLowerCase(),n=0;
 [].forEach.call(d.querySelectorAll('.gdir li'),function(r){var ok=(!l||r.dataset.lga===l)&&(!p||r.dataset.pillar===p)&&(!q||r.textContent.toLowerCase().indexOf(q)>-1);r.hidden=!ok;if(ok)n++});d.querySelector('.empty').hidden=n>0}
 [].forEach.call(d.querySelectorAll('select'),function(s){s.addEventListener('change',ap)});d.querySelector('[data-f=q]').addEventListener('input',ap)});
})();
"""

FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700;800;900&family=Caveat:wght@700&display=swap" rel="stylesheet">'


PROTOS = [("v1", "Prototype 1", "Rounded blocks"), ("v2", "Prototype 2", "Light and fresh"), ("v3", "Prototype 3", "Big visuals")]


def protobar(v):
    # data-proto lets the script point each button at the same page in the other prototype
    others = "".join(f'<a class="pb-btn" data-proto="{k}" href="../{k}/" aria-label="{n}: {d}"><span class="pb-short" aria-hidden="true">P{k[1]}</span><span class="pb-long">{n}</span></a>' for k, n, d in PROTOS if k != v)
    cur = next(f"{n}: {d}" for k, n, d in PROTOS if k == v)
    return f'''<div class="protobar" role="region" aria-label="Prototype controls"><div class="pb-in">
<p class="pb-label"><b>MOCKUP &amp; PROTOTYPE ONLY</b> by <a href="https://veemercado.com">veemercado.com</a><span class="pb-cur"> &middot; viewing {cur}</span></p>
<nav class="pb-nav" aria-label="Other prototypes"><a class="pb-btn pb-all" href="../">All prototypes</a>{others}</nav>
<button type="button" class="pb-top" aria-label="Back to top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})"><span class="pb-long">Back to top&nbsp;</span><span aria-hidden="true">&uarr;</span></button></div></div>'''


def page_shell(title, css, body, v, white_logo=True):
    return f'''<!doctype html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="robots" content="noindex">
<meta name="description" content="Prototype for the Northern Rivers Community Resilience Alliance website. Sample content only.">
{FONT}<style>{BASE}{css}</style></head><body class="{v}">
{nav()}<main id="main">{body}</main>{footer(white_logo)}{protobar(v)}<script>{JS}</script></body></html>'''


def assemble(home, about, partners, network, rack):
    return "".join([screen("home", "Home", home), screen("about", "About", about), screen("partners", "Partners", partners),
                    screen("network", "Network", network), screen("rack", "R.A.C.K", rack), rack_screens()])


# ================================================================ V1: Rounded blocks
CSS1 = """
body{--bg:#f3f6f7}
.hero1{padding:28px 0 8px}.hero1>.wrap:first-child{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.h1-panel{background:var(--navy);color:#fff;border-radius:32px;padding:52px 44px;display:flex;flex-direction:column;justify-content:center}
.h1-panel h1{font-size:clamp(2rem,4vw,3.2rem)}.h1-panel .eyebrow{color:var(--yellow)}.h1-panel .btn-ghost{color:#fff;border-color:#fff}.h1-panel .btn-ghost:hover{background:#fff;color:var(--navy)}
.h1-photo{border-radius:32px;overflow:hidden;min-height:460px}.h1-photo img{width:100%;height:100%;object-fit:cover}
@media(max-width:860px){.hero1>.wrap:first-child{grid-template-columns:1fr}.h1-panel{padding:36px 26px}.h1-photo{min-height:280px}}
.latest{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}.latest a{background:#fff;border:1px solid var(--line);border-radius:99px;padding:.45em 1em;font-weight:700;text-decoration:none;color:var(--navy);font-size:.95rem}
.latest b{color:var(--orange-d);margin-right:6px}
.intro1{display:grid;grid-template-columns:1.3fr 1fr;gap:40px;align-items:center}.callout{border:3px solid var(--orange);border-radius:var(--r);padding:28px;font-size:1.2rem;font-weight:800;background:#fff}
@media(max-width:860px){.intro1{grid-template-columns:1fr}}
.val{border-radius:var(--r);padding:30px}.val .ico{margin-bottom:18px}.val-teal{background:var(--teal-25);color:var(--navy)}.val-yellow{background:var(--yellow-40);color:var(--navy)}.val-orange{background:var(--orange-25);color:var(--navy)}
.val .ico{width:56px;height:56px;padding:10px;border-radius:50%;background:#fff}.val-teal .ico{color:var(--teal-d)}.val-yellow .ico{color:#7a5a00}.val-orange .ico{color:var(--orange-d)}
.pills{list-style:none;margin:0;padding:0;display:grid;gap:12px}.pills li{display:flex;align-items:center;gap:18px;border-radius:99px;padding:16px 26px}
.pills li .ico{flex:none;width:40px;height:40px;background:#fff;border-radius:50%;padding:7px;color:var(--navy)}.pills h3{margin:0;font-size:1.1rem}.pills p{margin:0;font-size:.95rem}
.pills li:nth-child(1){background:var(--teal-25)}.pills li:nth-child(2){background:var(--yellow-40)}.pills li:nth-child(3){background:var(--orange-25)}.pills li:nth-child(4){background:var(--navy);color:#fff}.pills li:nth-child(5){background:#fff;border:2px solid var(--navy)}
.card{background:#fff;border-radius:var(--r);padding:32px;box-shadow:0 1px 0 var(--line)}
.stat-card{background:#fff;border-radius:var(--r);padding:32px}.stat-card dt{color:var(--teal-d)}
.kb{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px}
.kb li{border-radius:var(--r);padding:18px 18px 24px}.kb img{border-radius:18px;aspect-ratio:4/3;object-fit:cover;width:100%;margin-bottom:16px}.kb h3{margin:0 0 .3em}.kb p{margin:0}
.kb li:nth-child(1){background:var(--teal-25);color:var(--navy)}.kb li:nth-child(2){background:var(--yellow-40);color:var(--navy)}.kb li:nth-child(3){background:var(--orange-25);color:var(--navy)}.kb a{color:inherit;font-weight:800}
.ready{position:relative;border-radius:32px;overflow:hidden;color:#fff;text-align:center;padding:96px 24px}.ready>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ready::after{content:"";position:absolute;inset:0;background:rgba(7,41,59,.72)}.ready>div{position:relative;z-index:2;max-width:640px;margin:0 auto}.ready .btn-ghost{color:#fff;border-color:#fff}.ready .btnrow{justify-content:center}
.pg1{padding:40px 0 8px}.pg1 .wrap{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}.pg1 .ph{border-radius:32px;overflow:hidden;aspect-ratio:4/3}.pg1 .ph img{width:100%;height:100%;object-fit:cover}
@media(max-width:860px){.pg1 .wrap{grid-template-columns:1fr}}
.arc{border-radius:var(--r);padding:28px;background:#fff;border-top:6px solid var(--teal)}.arc.y{border-top-color:var(--yellow)}.arc.o{border-top-color:var(--orange)}
.ft-from{background:#fff}.ft-arrow{background:var(--teal-d);border-radius:var(--r);color:#fff}.ft-to{background:var(--teal-25);color:var(--navy)}
.journey li{background:#fff;border-radius:20px;padding:18px 22px}.journey b{color:var(--teal-d)}
.pcard{background:#fff}.cards .pcard:nth-child(1){border-top:6px solid var(--teal)}.cards .pcard:nth-child(2){border-top:6px solid var(--yellow)}.cards .pcard:nth-child(3){border-top:6px solid var(--orange)}
.pgroup h3{font-size:1.4rem}
.racks{list-style:none;margin:0;padding:0;display:grid;gap:12px}.racks li{display:grid;grid-template-columns:auto 1fr auto;gap:18px;align-items:center;border-radius:99px;padding:14px 26px 14px 14px;background:#fff;border:1px solid var(--line)}
.racks .rn{width:46px;height:46px;border-radius:50%;display:grid;place-items:center;font-weight:900;background:var(--teal-25);color:var(--navy)}.racks li:nth-child(2) .rn{background:var(--yellow-40)}.racks li:nth-child(3) .rn{background:var(--orange-25)}.racks li:nth-child(4) .rn{background:var(--navy);color:#fff}
.racks h3{margin:0}.racks p{margin:0;font-size:.95rem;color:var(--muted)}.racks .rc{font-weight:800;font-size:.9rem;background:#eef5f5;border-radius:99px;padding:.3em .8em}
@media(max-width:600px){.racks li{grid-template-columns:auto 1fr;border-radius:24px}.racks .rc{grid-column:2}}
.wfw-eye{text-align:center;font-weight:800;color:var(--teal-d);margin:0 0 18px}
.wfw-grid{display:grid;grid-template-columns:1fr 1.15fr 1fr;gap:32px;align-items:center}
.wfw-col{list-style:none;margin:0;padding:0;display:grid;gap:40px}.wfw-col li{display:grid;gap:10px;justify-items:center;text-align:center}
.wfw-col .wn{justify-self:start;font-weight:900;color:var(--teal-d)}.wfw-col img{height:70px;width:auto;max-width:170px;object-fit:contain}
.wbar{width:100%;height:5px;border-radius:99px;background:var(--teal-25)}.wfw-col p{margin:0;font-weight:700}
.wfw-mid{position:relative;border-radius:32px;overflow:hidden;aspect-ratio:3/4}.wfw-mid img{width:100%;height:100%;object-fit:cover}
.wfw-mid::after{content:"";position:absolute;inset:0;background:rgba(7,41,59,.45)}.wfw-mid h2{position:absolute;inset:0;display:grid;place-items:center;margin:0;z-index:2;color:#fff;text-transform:uppercase;font-size:clamp(2.2rem,4.4vw,3.6rem);font-weight:900;line-height:.95;text-align:center;padding:16px;letter-spacing:.02em}
.wfw-line{text-align:center;max-width:70ch;margin:32px auto 0;font-size:1.1rem}.wfw-btns{justify-content:center}
@media(max-width:860px){.wfw-grid{grid-template-columns:1fr 1fr}.wfw-mid{grid-column:1/-1;grid-row:1;aspect-ratio:16/10}.wfw-col{gap:24px}}
.pmap{--land:#ffffff;--sea:#d8f0ee;--coast:#8fcfc9;--river:#7cc0dd}
.v1 .pc:nth-child(1){background:var(--teal-25)}.v1 .pc:nth-child(2){background:var(--yellow-40)}.v1 .pc:nth-child(3){background:var(--orange-25)}.v1 .pc:nth-child(4){background:var(--blue-15)}.v1 .pc:nth-child(5){background:var(--grey-6)}
.p3{display:grid;grid-template-columns:.9fr 1.1fr 1fr;gap:36px;align-items:center}.p3-img img{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:28px}.p3-txt p{font-size:1.1rem;margin:0}
.p3-logos ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:12px}.p3-logos li{border:1px solid var(--line);border-radius:16px;display:grid;place-items:center;padding:12px;aspect-ratio:3/2;background:#fff}.p3-logos img{max-height:56px;max-width:100%;object-fit:contain}
@media(max-width:900px){.p3{grid-template-columns:1fr}.p3-img img{aspect-ratio:16/10}}
.pgs{padding:48px 0 0}.pgs .lede{max-width:70ch}.narrow{max-width:720px}
"""


def v1_partners():
    logos = "".join(f'<li><img src="{SL}{f}" alt="{E(n)} (sample logo)" loading="lazy"></li>' for f, n in SAMPLE[:6])
    return f'''<div class="p3"><div class="p3-img">{img("hug")}</div><div class="p3-txt"><span class="eyebrow">Thanks to our partners</span><h2>What our partners made possible</h2><p>{PARTNER_LINE}</p></div>
<div class="p3-logos"><ul>{logos}</ul><p class="btnrow"><a class="btn btn-primary" href="#partners">View all partners</a><a class="btn btn-ghost" href="mailto:{CONTACT["email"]}">Become a partner</a></p></div></div>
<p class="vnote">Placeholder logos to show the layout.</p>'''


def v1():
    home = f'''<div class="hero1"><div class="wrap"><div class="h1-panel"><span class="eyebrow">Northern Rivers Community Resilience Alliance</span>
<h1>When disaster strikes, local people are always first to respond.</h1><p class="lede">{H1}.</p>
<p class="btnrow"><a class="btn btn-primary" href="#network">Join the Alliance</a><a class="btn btn-ghost" href="#about">What we do</a></p></div>
<div class="h1-photo">{img("cheer", eager=True)}</div></div>
<div class="wrap"><div class="latest"><a href="{LINKS["news"]}"><b>Latest</b>$800,000 HELP Fund grants program announced</a><a href="#home-focus"><b>Upcoming</b>{GATHER[0]}: {GATHER[1]}</a><a href="#partners"><b>Projects</b>Three projects under way</a></div></div></div>

<section class="sec"><div class="wrap intro1"><div><span class="eyebrow">Who we are</span><h2>This is about more than disaster.</h2><p>{WHO}</p><p>{MORE}</p></div><p class="callout">{CALLOUT}</p></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><h2>How we work</h2>{values_cards()}</div></section>

<section class="sec" style="padding-top:0"><div class="wrap split"><div>{video("group")}</div><div class="stat-card"><span class="eyebrow">What we have achieved</span>{stats()}</div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><span class="eyebrow">Our focus</span><h2>Five pillars</h2>{pillar_cols()}</div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><div class="card">{places_block()}</div></div></section>

<section class="sec" style="padding-top:0" id="home-focus"><div class="wrap"><span class="eyebrow">In focus</span><h2>Upcoming, projects and the R.A.C.K</h2>
<ul class="kb"><li>{img("crowd")}<h3>{GATHER[0]}: {GATHER[1]}</h3><p>{GATHER[2]}.</p></li><li>{img("meeting")}<h3>Projects</h3><p>Connected and Prepared, Resourcing Community Resilience and Learning Together. <a href="#partners">See partners</a></p></li>
<li>{img("board")}<h3>The R.A.C.K</h3><p>{RACK_LINE} <a href="#rack">Explore</a></p></li></ul></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><div class="card">{v1_partners()}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="ready">{img("aerial", alt="")}<div><h2>Ready to connect?</h2><p class="lede" style="margin:0 auto">Whether you are a community group, a local council, a funder or someone who cares about your community, there is a place for you in this Alliance.</p>{cta_band()}</div></div></div></section>'''

    about = f'''<div class="pg1"><div class="wrap"><div class="ph">{img("line", eager=True)}</div><div><span class="eyebrow">About us</span><h1>We're changing the Northern Rivers' resilience culture</h1><p class="lede">{MORE}</p></div></div></div>
<section class="sec"><div class="wrap"><div class="split" style="align-items:stretch"><div class="arc"><h2>Vision</h2><p>{VISION}</p></div><div class="arc y"><h2>Purpose</h2><p>{PURPOSE}</p></div></div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2>Our values</h2>{values_cards()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2>What we are changing</h2>{from_to()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2>Our journey</h2>{journey()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap split"><div class="card"><h2>How we learn</h2><p>Monitoring, Evaluation, Accountability and Learning is our learning cycle, with researchers from the University Centre for Rural Health.</p>{meal()}</div><div class="card" style="background:var(--yellow-40)">{quote()}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap card"><h2>Our structure</h2><p>Steering committee, embedded researchers from UCRH and the Network Lead, {CONTACT["name"]}. Names and roles to be supplied.</p><h3>Common questions</h3>{faq()}</div></section>'''

    partners = f'''<div class="pgs"><div class="wrap"><span class="eyebrow">Impact</span><h1>Our partners</h1><p class="lede">{PARTNER_LINE}</p></div></div>
<section class="sec" style="padding-top:24px"><div class="wrap">{logo_grid()}<p class="btnrow"><a class="btn btn-primary" href="mailto:{CONTACT["email"]}">Become a partner</a></p></div></section>'''

    network = f'''<div class="pg1"><div class="wrap"><div><span class="eyebrow">Network</span><h1>{NET_H1}</h1><p class="lede">Find the resilience groups connected to the Alliance, by place and by focus.</p></div><div class="ph">{img("web", eager=True)}</div></div></div>
{network_body("card")}'''

    rack = f'''<div class="pg1"><div class="wrap"><div><span class="eyebrow">Resources</span><h1>The R.A.C.K</h1><p class="lede"><b>{RACK_NAME}.</b> {RACK_LINE} {RACK_INTRO}</p>{rack_buttons()}</div><div class="ph">{img("table", eager=True)}</div></div></div>
<section class="sec"><div class="wrap"><h2>The 5 RACKs</h2>{rack_list()}<p class="vnote">Counts from the R.A.C.K, October 2026.</p></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2>Funding and grants</h2><ul class="cards"><li class="pcard"><h3>The HELP Fund</h3><p>NRMA Insurance's participatory grants program for the region.</p></li><li class="pcard"><h3>Establishment grants</h3><p>$3,000</p></li><li class="pcard"><h3>Resilience action grants</h3><p>Up to $10,000</p></li></ul></div></section>
<section class="sec" style="padding-top:0"><div class="wrap card"><h2>Need help getting in?</h2><p>Access is for Alliance groups. Contact the Network Lead to get set up.</p><p class="btnrow"><a class="btn btn-primary" href="mailto:{CONTACT["email"]}">Contact the Network Lead</a></p></div></section>'''
    return page_shell("NRCRA prototype 1: Rounded blocks", CSS1, assemble(home, about, partners, network, rack), "v1")


# ================================================================ V2: Light and fresh, illustrated
def illus_hero():
    people = ""
    cols = ["#f05a28", "#ffcb2a", "#00a79d", "#07293b", "#f05a28", "#00a79d", "#ffcb2a"]
    for i, c in enumerate(cols):
        x = 150 + i * 50
        h = 64 if i % 2 else 76
        people += f'<g><circle cx="{x}" cy="{368 - h}" r="13" fill="{c}"/><path d="M{x - 18} 372q0-{h - 22} 18-{h - 22}t18 {h - 22}z" fill="{c}"/></g>'
    hands = '<path d="M150 335 L450 335" stroke="#07293b" stroke-width="3" stroke-linecap="round" opacity=".35"/>'
    return f'''<svg class="illus" viewBox="0 0 600 460" role="img" aria-label="Illustration: a row of people joined together in front of hills, a river and a rising sun">
<circle cx="300" cy="250" r="190" fill="#fff4cc"/><path d="M150 210a150 150 0 0 1 300 0" fill="none" stroke="#ffcb2a" stroke-width="26" stroke-linecap="round"/>
<path d="M195 205a105 105 0 0 1 210 0" fill="none" stroke="#f05a28" stroke-width="18" stroke-linecap="round" opacity=".85"/>
<circle cx="300" cy="96" r="16" fill="#f05a28"/><circle cx="196" cy="140" r="11" fill="#ffcb2a"/><circle cx="404" cy="140" r="11" fill="#00a79d"/>
<path d="M0 330C90 270 170 285 260 315s170 10 340-40V460H0z" fill="#bfe7e3"/><path d="M0 370c120-50 230-30 330 0s180 10 270-20V460H0z" fill="#7fd0c9"/>
<path d="M0 410c160-30 300-10 420 10s140 0 180-10V460H0z" fill="#00a79d"/><path d="M60 460c40-40 130-50 210-55s150-25 170-55" fill="none" stroke="#dff1f6" stroke-width="14" stroke-linecap="round"/>
{hands}{people}</svg>'''


ARC = '<svg class="arc-acc" viewBox="0 0 160 110" aria-hidden="true"><path d="M20 100a60 60 0 0 1 120 0" fill="none" stroke="#ffcb2a" stroke-width="16" stroke-linecap="round"/><path d="M45 100a35 35 0 0 1 70 0" fill="none" stroke="#f05a28" stroke-width="12" stroke-linecap="round"/><circle cx="80" cy="22" r="10" fill="#f05a28"/><circle cx="26" cy="48" r="7" fill="#ffcb2a"/><circle cx="134" cy="48" r="7" fill="#00a79d"/></svg>'


def photo_art(key, cls="h2-art", sticker=""):
    st = f'<span class="sticker">{sticker}</span>' if sticker else ""
    return f'<div class="{cls}"><div class="ph">{img(key, eager=True)}</div>{ARC}{st}</div>'


def blob_icon(name, bg):
    return f'<span class="bico" style="background:{bg}">{icon(name)}</span>'


CSS2 = """
body{--btn-r:12px;--bg:#fff;--foot:#e6f6f4;--foot-ink:#07293b;--foot-h:#006b64;--foot-line:#bfe3df;--current:#fff1c2;--hover:#f2faf9}
.mint{background:#eaf7f5}.butter{background:#fff6d8}.peach{background:#fdece4}.sky{background:#eaf5fb}
.hero2{padding:40px 0 32px;background:#fff}.hero2 .wrap{display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:center}
.hero2 h1{font-size:clamp(2rem,4.2vw,3.3rem)}.hero2 .btn-primary{background:var(--teal-d);border-color:var(--teal-d);color:#fff}.hero2 .btn-primary:hover{background:var(--navy);border-color:var(--navy)}
.illus{width:100%;height:auto;display:block}
@media(max-width:860px){.hero2 .wrap{grid-template-columns:1fr}}
.paths{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px}
.paths a{display:flex;gap:16px;align-items:center;background:#fff;border-radius:24px;padding:20px;text-decoration:none;color:var(--navy);box-shadow:0 8px 24px -14px rgba(7,41,59,.35)}
.paths a:hover{transform:translateY(-2px)}.paths b{display:block;font-size:1.1rem}.paths small{color:var(--muted);font-size:.95rem}
.bico{flex:none;width:64px;height:64px;border-radius:22px;display:grid;place-items:center;color:var(--navy)}.bico .ico{width:36px;height:36px}
.news{display:grid;grid-template-columns:auto 1fr 1fr;gap:16px;align-items:center;border-radius:28px;padding:20px 28px}.news b{font-size:.8rem;text-transform:uppercase;letter-spacing:.12em;color:var(--orange-d)}
.news p{margin:0;font-weight:700}@media(max-width:760px){.news{grid-template-columns:1fr}}
.steps{list-style:none;margin:0;padding:0;position:relative}.steps::before{content:"";position:absolute;left:50%;top:10px;bottom:10px;border-left:3px dotted #9fd6d0}
.steps li{display:grid;grid-template-columns:1fr 80px 1fr;align-items:center;gap:20px;padding:22px 0}.steps .num{width:64px;height:64px;border-radius:50%;background:#fff;border:3px solid var(--teal);display:grid;place-items:center;font-weight:900;font-size:1.5rem;margin:auto;position:relative;color:var(--teal-d)}
.steps .art{display:flex;justify-content:flex-end}.steps li:nth-child(even) .art{order:3;justify-content:flex-start}.steps li:nth-child(even) .txt{order:1;text-align:right}.steps li:nth-child(even) .num{order:2}
.steps .txt h3{font-size:1.35rem;margin:0 0 .3em}.steps .txt p{margin:0;color:var(--muted)}.steps .bico{width:120px;height:120px;border-radius:40px}.steps .bico .ico{width:60px;height:60px}
@media(max-width:760px){.steps::before{left:32px}.steps li{grid-template-columns:64px 1fr;gap:14px}.steps .art{display:none}.steps li:nth-child(even) .txt{order:2;text-align:left}.steps .num{margin:0}}
.statbox{border-radius:32px;padding:40px}.statbox dt{color:var(--teal-d)}
.vframe{background:#fff6d8;border-radius:36px;padding:18px}.vframe .video{border-radius:24px}
.fcards{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px}
.fcards li{background:#fff;border-radius:28px;overflow:hidden;box-shadow:0 8px 24px -14px rgba(7,41,59,.35)}.fcards .top{height:10px}.fcards .in{padding:22px 24px}
.fcards li:nth-child(1) .top{background:var(--teal)}.fcards li:nth-child(2) .top{background:var(--yellow)}.fcards li:nth-child(3) .top{background:var(--orange)}.fcards h3{margin:.4em 0 .3em}.fcards p{margin:0}
.bandcta{border-radius:36px;padding:48px 40px;display:grid;grid-template-columns:1.2fr 1fr;gap:20px;align-items:center}
.bandcta .btn-primary{background:var(--teal-d);border-color:var(--teal-d);color:#fff}@media(max-width:760px){.bandcta{grid-template-columns:1fr}}
.pg2{padding:48px 0 32px}.pg2 .wrap{display:grid;grid-template-columns:1.2fr .8fr;gap:32px;align-items:center}.pg2 p{color:var(--muted)}
.pg2 .chip{display:inline-block;background:#fff1c2;border-radius:99px;padding:.2em .9em;font-weight:800;margin-bottom:1em}@media(max-width:760px){.pg2 .wrap{grid-template-columns:1fr}.pg2 .art{max-width:220px}}
.soft{border-radius:28px;padding:32px}
.val{border-radius:28px;padding:28px;background:#fff;box-shadow:0 8px 24px -14px rgba(7,41,59,.35)}.val .ico{width:56px;height:56px;padding:10px;border-radius:20px;margin-bottom:14px}
.val-teal .ico{background:#d4f0ec}.val-yellow .ico{background:#fff1c2}.val-orange .ico{background:#fde0d4}
.ft-from{background:#fff;border:2px dashed #cfe3e1}.ft-arrow{color:var(--teal-d)}.ft-to{background:#eaf7f5}
.river{position:relative;list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(5,1fr);gap:16px}
.river::before{content:"";position:absolute;left:0;right:0;top:26px;height:12px;border-radius:99px;background:#bfe7e3}
.river li{position:relative;padding-top:64px}.river b{position:absolute;top:0;left:0;background:#fff;border:3px solid var(--teal);border-radius:99px;padding:.35em .9em;font-weight:900;color:var(--teal-d)}
.river p{margin:0;font-size:.95rem}@media(max-width:860px){.river{grid-template-columns:1fr}.river::before{left:24px;right:auto;width:10px;top:0;bottom:0;height:auto}.river li{padding:0 0 0 70px;min-height:60px}.river b{left:0}}
.meal li{border-color:#9fd6d0;background:#fff}.meal li:nth-child(odd){background:#eaf7f5}
.quote p{font-family:"Caveat",cursive;font-size:clamp(1.8rem,3.4vw,2.6rem);font-weight:700}
.pcard{background:#fff;box-shadow:0 8px 24px -14px rgba(7,41,59,.35)}
.racks{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px}
.racks li{border-radius:28px;padding:24px;display:flex;flex-direction:column;gap:6px}.racks .rn{font-weight:900;font-size:2rem;line-height:1;color:var(--teal-d)}.racks h3,.racks p{margin:0}.racks p{color:var(--muted);font-size:.95rem}.racks .rc{margin-top:auto;font-weight:800;font-size:.9rem}
.racks li:nth-child(5n+1){background:#eaf7f5}.racks li:nth-child(5n+2){background:#fff6d8}.racks li:nth-child(5n+3){background:#fdece4}.racks li:nth-child(5n+4){background:#eaf5fb}.racks li:nth-child(5n){background:#f3f0fb}
.pillars.ill li{background:#fff;border-radius:28px;padding:24px;box-shadow:0 8px 24px -14px rgba(7,41,59,.35)}.pillars.ill .ico{width:52px;height:52px;padding:9px;border-radius:18px;background:#eaf7f5;color:var(--teal-d)}
.whitecard{background:#fff;border-radius:28px;padding:32px;box-shadow:0 8px 24px -14px rgba(7,41,59,.35)}
.h2-art{position:relative;padding:24px 0 0 24px}.h2-art .ph{border-radius:40px 40px 40px 140px;overflow:hidden;aspect-ratio:5/4;box-shadow:0 18px 40px -24px rgba(7,41,59,.5)}
.h2-art .ph img{width:100%;height:100%;object-fit:cover}.arc-acc{position:absolute;width:140px;left:-16px;top:-26px}
.sticker{position:absolute;right:16px;bottom:-14px;background:#fff;border-radius:99px;padding:.5em 1.1em;font-weight:900;box-shadow:0 8px 20px -10px rgba(7,41,59,.4)}
.sphoto{position:relative;width:240px}.sphoto img{width:240px;height:170px;object-fit:cover;border-radius:32px}.sbadge{position:absolute;right:-12px;bottom:-12px;width:56px;height:56px;border-radius:50%;background:#fff;display:grid;place-items:center;box-shadow:0 6px 16px -8px rgba(7,41,59,.5);color:var(--teal-d)}.sbadge .ico{width:30px;height:30px}
.fcards img{width:100%;aspect-ratio:16/10;object-fit:cover}
.prow{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:24px}.prow img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:28px}@media(max-width:700px){.prow{grid-template-columns:1fr 1fr}}
.r2{border-radius:32px;aspect-ratio:4/5}.pimg{width:calc(100% + 48px);margin:-24px -24px 14px;aspect-ratio:16/10;object-fit:cover}.pillars.ill li{overflow:hidden}
.pmap{--land:#fbfdf8;--sea:#e3f4f8;--coast:#a9d8d2;--river:#8ccbe3;--dot:#00a79d;--hot:#f05a28}
.places button{--chip:#d4ece9}.places button:hover,.places button[aria-pressed=true]{background:var(--teal-d);border-color:var(--teal-d)}
.site-foot .logo-white{filter:none}
.v2 .pc:nth-child(1){background:var(--teal-12)}.v2 .pc:nth-child(2){background:var(--yellow-20)}.v2 .pc:nth-child(3){background:var(--orange-12)}.v2 .pc:nth-child(4){background:#e6f1f8}.v2 .pc:nth-child(5){background:#f1eefa}
.v2 .pc-base{background:#d4ece9}.plain2 .wrap{grid-template-columns:1fr}.plain2 .lede{max-width:70ch}.narrow{max-width:720px}.v2 .btn-primary{background:var(--teal-d);border-color:var(--teal-d);color:#fff}.v2 .btn-primary:hover{background:var(--navy);border-color:var(--navy)}
"""


def v2():
    home = f'''<div class="hero2"><div class="wrap"><div><span class="eyebrow">Northern Rivers Community Resilience Alliance</span><h1>{H1}</h1>
<p class="lede">{CALLOUT}</p><p class="btnrow"><a class="btn btn-primary" href="#network">Join the network</a><a class="btn btn-ghost" href="#about">What we do</a></p></div>
{photo_art("cheer", sticker="60+ groups, one network")}</div></div>
<section class="mint" style="padding:40px 0 56px"><div class="wrap"><ul class="paths">
<li><a href="#about">{blob_icon("people", "#fff1c2")}<span><b>What we do</b><small>Our focus and purpose</small></span></a></li>
<li><a href="#partners">{blob_icon("seed", "#fde0d4")}<span><b>Projects and HELP Fund</b><small>Who funds this work</small></span></a></li>
<li><a href="#network">{blob_icon("connect", "#d4f0ec")}<span><b>Our impact</b><small>60+ groups, one network</small></span></a></li></ul>
<div class="news butter" style="margin-top:22px"><b>Latest</b><p>$800,000 HELP Fund grants program announced. <a href="{LINKS["news"]}">Read more</a></p><p>{GATHER[0]}: {GATHER[1]}. <a href="#home-focus">Upcoming</a></p></div></div></section>

<section class="sec"><div class="wrap">{places_block("The group made up of groups", WHO + " Tap a town to find it on the map.")}</div></section>

<section class="sec mint"><div class="wrap"><span class="eyebrow">Our focus</span><h2>Five pillars</h2>
{pillar_cols(photos=["circle", "board", "hug", "talk", "speaker"])}</div></section>

<section class="sec"><div class="wrap split"><div class="statbox peach"><span class="eyebrow">What we have achieved</span>{stats()}</div><div class="vframe">{video("laughing")}</div></div></section>

<section class="sec sky" id="home-focus"><div class="wrap"><span class="eyebrow">In focus</span><h2>Upcoming, projects and the R.A.C.K</h2>
<ul class="fcards"><li>{img("crowd")}<div class="top"></div><div class="in"><h3>{GATHER[0]}: {GATHER[1]}</h3><p>{GATHER[2]}.</p></div></li>
<li>{img("meeting")}<div class="top"></div><div class="in"><h3>Projects</h3><p>Three projects growing the Alliance, funding local ideas and learning together. <a href="#partners">See partners</a></p></div></li>
<li>{img("table")}<div class="top"></div><div class="in"><h3>The R.A.C.K</h3><p>{RACK_LINE} <a href="#rack">Explore</a></p></div></li></ul></div></section>

<section class="sec"><div class="wrap"><h2>Thanks to our partners</h2><p class="lede">{PARTNER_LINE}</p>{partner_strip()}<p class="btnrow"><a class="btn btn-ghost" href="#partners">All partners</a></p></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="bandcta butter"><div><h2>Get involved</h2><p>Local experience. Shared learning. Wider impact.</p>{cta_band()}</div><div>{illus_hero()}</div></div></div></section>'''

    def pg(chip, title, text, extra="", pic="group"):
        return f'<div class="pg2"><div class="wrap"><div><span class="chip">{chip}</span><h1>{title}</h1><p class="lede">{text}</p>{extra}</div>{photo_art(pic)}</div></div>'

    about = pg("About us", "Local experience. Shared learning. Wider impact.", WHO) + f'''
<section class="sec mint"><div class="wrap split" style="align-items:stretch"><div class="whitecard"><h2>Vision</h2><p>{VISION}</p></div><div class="whitecard"><h2>Purpose</h2><p>{PURPOSE}</p></div></div></section>
<section class="sec"><div class="wrap"><h2>Our values</h2>{values_cards()}<div class="prow">{img("board2")}{img("cards")}{img("line")}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2>What we are changing</h2>{from_to()}</div></section>
<section class="sec sky"><div class="wrap"><h2>Our journey</h2>{journey("river")}</div></section>
<section class="sec"><div class="wrap split"><div><h2>How we learn</h2><p>Monitoring, Evaluation, Accountability and Learning, with researchers from the University Centre for Rural Health.</p>{meal()}<div class="soft butter" style="margin-top:24px">{quote()}</div></div>{img("listening", "photo r2")}</div></section>
<section class="sec peach"><div class="wrap"><h2>Our structure</h2><p>Steering committee, UCRH embedded researchers and the Network Lead, {CONTACT["name"]}. Names to be supplied.</p><h3>Common questions</h3>{faq()}</div></section>'''

    partners = f'''<div class="pg2 plain2"><div class="wrap"><div><span class="chip">Impact</span><h1>Our partners</h1><p class="lede">{PARTNER_LINE}</p></div></div></div>
<section class="sec mint"><div class="wrap">{logo_grid()}<p class="btnrow"><a class="btn btn-primary" href="mailto:{CONTACT["email"]}">Become a partner</a></p></div></section>'''

    network = pg("Network", NET_H1, "Find the resilience groups connected to the Alliance, by place and by focus.", pic="web") + network_body("whitecard", sec_alt="mint")

    rack = pg("Resources", "The R.A.C.K", f"<b>{RACK_NAME}.</b> {RACK_LINE}", rack_buttons(), pic="workshop") + f'''
<section class="sec mint"><div class="wrap"><h2>The 5 RACKs</h2>{rack_list()}<p class="vnote">Counts from the R.A.C.K, October 2026.</p></div></section>
<section class="sec"><div class="wrap"><h2>Funding and grants</h2><ul class="cards"><li class="pcard"><h3>The HELP Fund</h3><p>Participatory grants for local groups.</p></li><li class="pcard"><h3>Establishment grants</h3><p>$3,000</p></li><li class="pcard"><h3>Resilience action grants</h3><p>Up to $10,000</p></li></ul></div></section>
<section class="sec butter"><div class="wrap"><h2>Need help getting in?</h2><p>Access is for Alliance groups. Contact the Network Lead to get set up.</p><p class="btnrow"><a class="btn btn-ghost" href="mailto:{CONTACT["email"]}">Contact the Network Lead</a></p></div></section>'''
    return page_shell("NRCRA prototype 2: Light and fresh", CSS2, assemble(home, about, partners, network, rack), "v2", white_logo=False)


# ================================================================ V3: Big visuals
SQUIGGLE = '<svg class="squig" viewBox="0 0 300 24" aria-hidden="true"><path d="M4 16c40-12 80-12 120-2s90 8 172-6" fill="none" stroke="#ffcb2a" stroke-width="8" stroke-linecap="round"/></svg>'
ARROW = '<svg class="arrow" viewBox="0 0 60 90" aria-hidden="true"><path d="M30 4c-8 22 10 40 0 70M14 62l16 22 16-22" fill="none" stroke="#f05a28" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def deco(name, pos):
    leaf = lambda x, y, r, c: f'<ellipse cx="{x}" cy="{y}" rx="9" ry="20" transform="rotate({r} {x} {y})" fill="{c}"/>'
    art = {
        "sprig": '<path d="M20 150C50 110 80 70 135 20" fill="none" stroke="#003d38" stroke-width="4" stroke-linecap="round"/>' + leaf(50, 104, -30, "#00a79d") + leaf(70, 118, 60, "#ffcb2a") + leaf(78, 76, -35, "#f05a28") + leaf(100, 86, 55, "#00a79d") + leaf(108, 46, -40, "#ffcb2a") + leaf(128, 52, 50, "#f05a28"),
        "dots": "".join(f'<circle cx="{10 + c * 22}" cy="{10 + r * 22}" r="5" fill="#f05a28" opacity=".55"/>' for r in range(6) for c in range(6)),
        "arcs": '<path d="M15 140a65 65 0 0 1 130 0" fill="none" stroke="#ffcb2a" stroke-width="16" stroke-linecap="round"/><path d="M42 140a38 38 0 0 1 76 0" fill="none" stroke="#f05a28" stroke-width="12" stroke-linecap="round"/><circle cx="80" cy="50" r="10" fill="#f05a28"/><circle cx="24" cy="80" r="7" fill="#ffcb2a"/><circle cx="136" cy="80" r="7" fill="#00a79d"/>',
        "rings": '<circle cx="80" cy="80" r="70" fill="none" stroke="#ffcb2a" stroke-width="6"/><circle cx="80" cy="80" r="48" fill="none" stroke="#00a79d" stroke-width="5" stroke-dasharray="4 10" stroke-linecap="round"/><circle cx="80" cy="80" r="26" fill="#f05a28" opacity=".85"/>',
    }[name]
    return f'<svg class="deco deco-{name} {pos}" viewBox="0 0 160 160" aria-hidden="true">{art}</svg>'


CSS3 = """
body{--btn-r:4px;--bg:#fbf6ec;--foot:#003d38;--foot-line:#21605a;--current:#ffe5a0;--hover:#f7ecd6;--deep:#003d38}
.hero3{padding:20px 0 0}.h3-box{position:relative;border-radius:40px;overflow:hidden;min-height:620px;display:flex;align-items:flex-end;color:#fff}
.h3-box>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.h3-box::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,40,36,.55),rgba(0,40,36,.85))}
.h3-box .in{position:relative;z-index:2;padding:48px;max-width:860px}.h3-box h1{font-size:clamp(2.2rem,5.4vw,4.4rem)}.h3-box .btn-ghost{color:#fff;border-color:#fff}.h3-box .btn-ghost:hover{background:#fff;color:var(--deep)}
.mark{position:relative;white-space:nowrap}.mark .squig{position:absolute;left:0;right:0;bottom:-.25em;width:100%;height:.4em}
@media(max-width:760px){.h3-box{min-height:520px}.h3-box .in{padding:28px}}
.h3-box .eyebrow,.pg3 .eyebrow{display:inline-block;background:rgba(0,40,36,.9);padding:.35em .9em;border-radius:99px}
.hand{font-family:"Caveat",cursive;font-weight:700;color:var(--orange-d);font-size:1.6rem}
.circles{position:relative;height:440px}.circles img{position:absolute;border-radius:50%;object-fit:cover;border:8px solid #fbf6ec}
.circles img:nth-child(1){width:300px;height:300px;left:0;top:0}.circles img:nth-child(2){width:220px;height:220px;right:0;top:40px}.circles img:nth-child(3){width:200px;height:200px;left:150px;bottom:0}
.circles .blob{position:absolute;right:30px;bottom:30px;width:150px;height:150px;background:var(--yellow);border-radius:62% 38% 55% 45%/48% 60% 40% 52%}
@media(max-width:760px){.circles{height:360px}.circles img:nth-child(1){width:220px;height:220px}.circles img:nth-child(2){width:160px;height:160px}.circles img:nth-child(3){width:150px;height:150px;left:90px}}
.big{font-size:clamp(1.8rem,3.6vw,2.8rem);font-weight:900;line-height:1.15;max-width:22ch}
.collage{display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:200px;gap:14px}.collage figure{margin:0;position:relative;border-radius:28px;overflow:hidden}
.collage img{width:100%;height:100%;object-fit:cover}.collage figcaption{position:absolute;left:12px;bottom:12px;background:#fbf6ec;color:var(--navy);border-radius:99px;padding:.25em .8em;font-weight:800;font-size:.85rem}
.collage .w2{grid-column:span 2}.collage .h2{grid-row:span 2}@media(max-width:760px){.collage{grid-template-columns:1fr 1fr;grid-auto-rows:150px}}
.orange{background:var(--orange-25);color:var(--navy)}.yellow{background:var(--yellow-40);color:var(--navy)}.yellow a,.orange a:not(.btn){color:var(--navy)}.deep{background:var(--deep);color:#fff}.deep a{color:#fff}
.oblock{border-radius:40px;padding:56px 48px;position:relative;overflow:hidden}.oblock .stats dt{font-size:clamp(2.6rem,5vw,4rem)}.oblock .stats dd{font-weight:800}
.oblock .shape{position:absolute;width:220px;height:220px;right:-90px;bottom:-100px;background:var(--orange);border-radius:58% 42% 62% 38%/45% 55% 45% 55%;opacity:.9}
.oblock>*{position:relative}.oblock .hand{color:var(--navy);margin:0 0 .4em}.oblock .stats dd,.oblock .big-b{font-size:1.2rem;font-weight:800}.oblock .pcard p{font-weight:600}
.words{display:grid;grid-template-columns:auto 1fr;gap:40px;align-items:center}.words .face{width:260px;height:260px;border-radius:50%;overflow:hidden}.words .face img{width:100%;height:100%;object-fit:cover}
.quote p{font-family:"Caveat",cursive;font-size:clamp(2rem,4vw,3rem);font-weight:700;line-height:1.15}@media(max-width:760px){.words{grid-template-columns:1fr}.words .face{width:180px;height:180px}}
.stories{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px}
.stories li{background:#fff;border-radius:28px;overflow:hidden}.stories img{aspect-ratio:4/3;object-fit:cover;width:100%}.stories .in{padding:18px 22px}.stories h3{margin:0 0 .3em}.stories p{margin:0;color:var(--muted)}
.bigv{border-radius:40px;overflow:hidden}.bigv .video{border-radius:40px;aspect-ratio:21/9;min-height:320px}
.help{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:24px}
.help li{text-align:center}.help .hico{width:110px;height:110px;margin:0 auto 14px;border-radius:50%;display:grid;place-items:center;background:#fff;color:var(--navy);border:4px solid var(--orange)}.help .hico .ico{width:56px;height:56px}
.help li:nth-child(2) .hico{border-color:var(--teal)}.help li:nth-child(3) .hico{border-color:var(--navy)}.help li:nth-child(4) .hico{border-color:var(--orange-d)}
.help a{font-weight:800}
.arrow{width:46px;height:70px;display:block;margin:10px auto}
.pg3{padding:20px 0 0}.pg3 .box{position:relative;border-radius:40px;overflow:hidden;min-height:400px;display:flex;align-items:flex-end;color:#fff}
.pg3 .box>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.pg3 .box::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,40,36,.55),rgba(0,40,36,.85))}
.pg3 .in{position:relative;z-index:2;padding:40px;max-width:760px}.pg3 .btn-ghost{color:#fff;border-color:#fff}.pg3 .btn-ghost:hover{background:#fff;color:var(--deep)}
.val{border-radius:28px;padding:28px}.val .ico{width:52px;height:52px;margin-bottom:12px}.val-teal{background:var(--teal-25);color:var(--navy)}.val-yellow{background:var(--yellow-40);color:var(--navy)}.val-orange{background:var(--orange-25);color:var(--navy)}
.ft-from{background:#fff}.ft-arrow{color:var(--orange-d)}.ft-to{background:var(--yellow-40)}
.tline{list-style:none;margin:0;padding:0;display:grid;gap:22px}.tline li{display:grid;grid-template-columns:200px 1fr;gap:28px;align-items:center}.tline img{border-radius:50%;width:180px;height:180px;object-fit:cover}
.tline li:nth-child(even) img{border-radius:62% 38% 55% 45%/48% 60% 40% 52%}.tline b{font-size:1.8rem;font-weight:900;color:var(--orange-d)}.tline p{margin:.2em 0 0}
@media(max-width:700px){.tline li{grid-template-columns:1fr}.tline img{width:140px;height:140px}}
.team{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:20px;text-align:center}
.team .av{width:130px;height:130px;border-radius:50%;margin:0 auto 10px;background:#efe3cb;display:grid;place-items:center;color:var(--muted);font-weight:800}
.pillars.ppl li{background:#fff;border-radius:28px;overflow:hidden;padding:0}.pillars.ppl img{aspect-ratio:1;object-fit:cover;width:100%}.pillars.ppl h3,.pillars.ppl p{padding:0 18px}.pillars.ppl h3{margin:.8em 0 .3em}.pillars.ppl p{padding-bottom:18px}
.pcard{background:#fff}.cards .pcard:nth-child(2){background:var(--yellow-40)}.cards .pcard:nth-child(3){background:var(--teal-25)}.pcard .meta{color:var(--navy)}
.pgroup h3{font-family:"Caveat",cursive;font-size:2.2rem;color:var(--orange-d)}
.racks{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:18px}
.racks li{background:#fff;border-radius:28px;padding:24px;display:flex;flex-direction:column;gap:6px;border-top:10px solid var(--orange)}.racks li:nth-child(2n){border-top-color:var(--yellow)}.racks li:nth-child(3n){border-top-color:var(--teal)}
.racks .rn{font-family:"Caveat",cursive;font-size:2.6rem;line-height:1;color:var(--orange-d)}.racks h3,.racks p{margin:0}.racks p{color:var(--muted);font-size:.95rem}.racks .rc{margin-top:auto;font-weight:800}
.warmcard{background:#fff;border-radius:28px;padding:32px}
.pmap{--land:#fffaf0;--sea:#f6e6c8;--coast:#e2c48d;--river:#9ccfd6;--dot:#f05a28;--hot:#003d38;--lga:#8a7350}
.places button{--chip:#ecd9b4}.places button:hover,.places button[aria-pressed=true]{background:var(--deep);border-color:var(--deep)}
.site-foot h2{color:var(--yellow)}
.rel{position:relative}.deco{position:absolute;z-index:3;pointer-events:none;width:150px;height:150px}
.d-tr{top:-34px;right:-6px}.d-tl{top:-30px;left:-6px}.d-bl{bottom:-34px;left:-6px}.d-br{bottom:-30px;right:-6px}
.deco-dots{width:130px;height:130px;z-index:1}.circles .deco-rings{z-index:0;width:190px;height:190px;left:40%;top:30%}
@media(max-width:760px){.deco{width:96px;height:96px}.d-tr{top:-22px;right:4px}.d-tl{top:-20px;left:4px}.d-bl{bottom:-22px;left:4px}.d-br{bottom:-20px;right:4px}}
.yellow.rel{overflow:hidden}.yellow .deco{opacity:.5}
.v3 .pc{background:#fff;border:3px solid var(--yellow)}.v3 .pc:nth-child(2){border-color:var(--orange)}.v3 .pc:nth-child(3){border-color:var(--teal)}.v3 .pc:nth-child(4){border-color:var(--orange-d)}.v3 .pc:nth-child(5){border-color:var(--teal-d)}
.v3 .pc-ico{background:var(--yellow-40)}.v3 .pc-n{font-family:"Caveat",cursive;font-size:1.8rem;letter-spacing:0;color:var(--orange-d);opacity:1}.v3 .pc-groups li{background:var(--grey-6)}.v3 .pc-base{background:#ecd9b4}
.pgs3{padding:48px 0 8px}.pgs3 .lede{max-width:70ch}.narrow{max-width:720px}
"""


def v3():
    home = f'''<div class="hero3"><div class="wrap rel">{deco("sprig", "d-tr")}{deco("dots", "d-bl")}<div class="h3-box">{img("cheer", eager=True)}<div class="in"><span class="eyebrow" style="color:var(--yellow)">Northern Rivers Community Resilience Alliance</span>
<h1>Neighbours looking after neighbours, across the <span class="mark">Northern Rivers{SQUIGGLE}</span></h1><p class="lede">{H1}.</p>
<p class="btnrow"><a class="btn btn-primary" href="#network">Join the network</a><a class="btn btn-ghost" href="#about">Meet the Alliance</a></p></div></div></div></div>

<section class="sec"><div class="wrap split"><div><p class="hand">Who we are</p><p class="big">The group made up of groups.</p><p>{WHO}</p><p class="btnrow"><a class="btn btn-ghost" href="#about">Our story</a></p></div>
<div class="circles">{deco("rings", "")}{img("laughing")}{img("talk")}{img("circle")}<span class="blob" aria-hidden="true"></span></div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap rel">{deco("arcs", "d-tr")}<div class="collage">
<figure class="w2 h2">{img("crowd")}<figcaption>Alliance Gathering</figcaption></figure><figure>{img("board")}<figcaption>Planning together</figcaption></figure><figure>{img("hug")}<figcaption>Peer support</figcaption></figure>
<figure class="w2">{img("web")}<figcaption>Connected</figcaption></figure></div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><div class="oblock orange"><span class="shape" aria-hidden="true"></span><p class="hand">What we have achieved</p>{stats()}<p class="big-b" style="margin:28px 0 6px">Thanks to our partners</p><p class="big-b" style="font-weight:600;max-width:70ch">{PARTNER_LINE}</p>{partner_strip()}</div></div></section>

<section class="sec"><div class="wrap"><p class="hand">In their own words</p><div class="words"><div class="face">{img("pair")}</div>{quote()}</div>
<ul class="stories" style="margin-top:40px"><li>{img("listening")}<div class="in"><h3>Story to come</h3><p>A member group's story, supplied by NRCRA.</p></div></li><li>{img("house")}<div class="in"><h3>Story to come</h3><p>A member group's story, supplied by NRCRA.</p></div></li><li>{img("audience")}<div class="in"><h3>Story to come</h3><p>A member group's story, supplied by NRCRA.</p></div></li></ul></div></section>

<section class="sec" style="padding-top:0"><div class="wrap rel">{deco("dots", "d-tl")}{deco("sprig", "d-br")}<div class="bigv">{video("aerial")}</div></div></section>

<section class="sec"><div class="wrap"><div class="warmcard">{places_block("Where we are")}</div></div></section>

<section class="sec yellow rel" id="home-focus">{deco("rings", "d-tl")}{deco("arcs", "d-br")}<div class="wrap"><h2 style="text-align:center">How you can be part of it</h2>{ARROW}
<ul class="help"><li><div class="hico">{icon("people")}</div><h3>Join the network</h3><p>Bring your group into the Alliance.</p><a href="#network">Find out how</a></li>
<li><div class="hico">{icon("cal")}</div><h3>Come to a gathering</h3><p>{GATHER[0]}: {GATHER[1]}.</p><a href="#home-focus">Upcoming</a></li>
<li><div class="hico">{icon("share")}</div><h3>Share knowledge</h3><p>Add what works to the R.A.C.K.</p><a href="#rack">The R.A.C.K</a></li>
<li><div class="hico">{icon("hand")}</div><h3>Partner with us</h3><p>Fund or research community-led resilience.</p><a href="#partners">Our partners</a></li></ul></div></section>'''

    def pg(eyebrow, title, text, pic, extra=""):
        return f'<div class="pg3"><div class="wrap rel">{deco("sprig", "d-tr")}{deco("dots", "d-bl")}<div class="box">{img(pic, eager=True)}<div class="in"><span class="eyebrow" style="color:var(--yellow)">{eyebrow}</span><h1>{title}</h1><p class="lede">{text}</p>{extra}</div></div></div></div>'

    jpics = ["board2", "meeting", "hall", "lab", "line"]
    about = pg("About us", "Local experience. Shared learning. Wider impact.", WHO, "group") + f'''
<section class="sec"><div class="wrap split"><div><p class="hand">Our vision</p><p class="big">{VISION}</p></div><div class="warmcard"><h2>Purpose</h2><p>{PURPOSE}</p></div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2>Our values</h2>{values_cards()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2>What we are changing</h2>{from_to()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2>Our journey</h2><ol class="tline">{"".join(f'<li>{img(jpics[i])}<div><b>{y}</b><p>{E(t)}</p></div></li>' for i, (y, t) in enumerate(JOURNEY))}</ol></div></section>
<section class="sec deep"><div class="wrap split"><div><h2>How we learn</h2><p>Monitoring, Evaluation, Accountability and Learning, with researchers from the University Centre for Rural Health.</p>{meal()}</div>{quote()}</div></section>
<section class="sec"><div class="wrap"><h2>Our people</h2><ul class="team">{"".join(f'<li><div class="av">Photo</div><b>Name</b><br><span class="lede-s">{r}</span></li>' for r in ["Network Lead", "Steering committee", "Steering committee", "UCRH researcher", "UCRH researcher"])}</ul><p class="vnote">Names, roles and photos to be supplied.</p><h3 style="margin-top:28px">Common questions</h3>{faq()}</div></section>'''

    partners = f'''<div class="pgs3"><div class="wrap rel">{deco("arcs", "d-tr")}<p class="hand">Thank you</p><h1>Our partners</h1><p class="lede">{PARTNER_LINE}</p></div></div>
<section class="sec" style="padding-top:24px"><div class="wrap">{logo_grid()}<p class="btnrow"><a class="btn btn-primary" href="mailto:{CONTACT["email"]}">Become a partner</a></p></div></section>'''

    network = pg("Network", NET_H1, "Find the resilience groups connected to the Alliance, by place and by focus.", "cards") + network_body("warmcard")

    rack = pg("Resources", "The R.A.C.K", f"<b>{RACK_NAME}.</b> {RACK_LINE}", "table", rack_buttons()) + f'''
<section class="sec"><div class="wrap"><p class="hand">What's inside</p><h2>The 5 RACKs</h2>{rack_list()}<p class="vnote">Counts from the R.A.C.K, October 2026.</p></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="oblock orange"><span class="shape" aria-hidden="true"></span><h2>Funding and grants</h2><ul class="cards"><li class="pcard"><h3>The HELP Fund</h3><p>Participatory grants for local groups.</p></li><li class="pcard"><h3>Establishment grants</h3><p>$3,000</p></li><li class="pcard"><h3>Resilience action grants</h3><p>Up to $10,000</p></li></ul>
<p class="big-b" style="margin-top:28px">Access is for Alliance groups. Need help getting in?</p><p class="btnrow"><a class="btn btn-ghost" href="mailto:{CONTACT["email"]}">Contact the Network Lead</a></p></div></div></section>'''
    return page_shell("NRCRA prototype 3: Big visuals", CSS3, assemble(home, about, partners, network, rack), "v3")


# ================================================================ dashboard
INSPO = {
    "v1": [("v1-milou-home", "Milou's NRCRA draft: home"), ("v1-milou-knowledge", "Milou's draft: Knowledge Bank"), ("v1-waves-for-water", "Waves for Water")],
    "v2": [("v2-rack", "The R.A.C.K app"), ("v2-resilient-lismore", "Resilient Lismore"), ("v2-investing-for-charity", "Investing for Charity")],
    "v3": [("v3-farm-africa", "Farm Africa"), ("v3-childrens-society", "The Children's Society"), ("v3-save-the-children", "Save the Children concept")],
}


def dashboard():
    cards = [
        ("v1", "Rounded blocks", "Built from Milou's drafts and Waves for Water. Rounded cards in light teal, yellow and orange tints, a navy hero panel beside a big rounded photo, pill buttons.", ["Colour cards with photos inside", "Five pillars as arched columns", "Partner section: photo, story and logos"]),
        ("v2", "Light and fresh", "Built from the R.A.C.K app and Resilient Lismore. Airy white and pastel bands with photos front and centre. Soft rounded photo shapes, small logo-arc accents, one illustration and softly rounded buttons.", ["Photo hero with logo-arc accent", "Five pillars as photo-topped columns", "River-style journey timeline"]),
        ("v3", "Big visuals", "People first: a big rounded photo hero, circle and blob photo crops, a photo collage, warm cream, orange and yellow tints, hand-drawn illustration decor and crisp buttons.", ["Circle photo cluster and collage", "Illustration decor on big images", "In their own words stories"]),
    ]
    rows = ""
    for i, (slug, t, d, feats) in enumerate(cards, 1):
        ins = "".join(f'<figure><img src="assets/inspo/{f}.jpg" alt="Mood board reference: {E(c)}" loading="lazy"><figcaption>{E(c)}</figcaption></figure>' for f, c in INSPO[slug])
        fl = "".join(f"<li>{E(x)}</li>" for x in feats)
        rows += f'''<article class="row row{i}"><a class="shot" href="{slug}/" aria-label="Open prototype {i}: {t}"><span class="bar" aria-hidden="true"><i></i><i></i><i></i></span><img src="assets/shots/{slug}.jpg" alt="Screenshot of prototype {i} home page, {t}" loading="lazy"></a>
<div class="info"><span class="num">Prototype {i}</span><h2><a href="{slug}/">{t}</a></h2><p>{d}</p><ul class="feats">{fl}</ul><p><a class="btn btn-primary" href="{slug}/">Open prototype {i}</a></p>
<h3>Inspired by the mood board</h3><div class="ins">{ins}</div></div></article>'''
    return f'''<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NRCRA website prototypes</title><meta name="robots" content="noindex">{FONT}
<style>{BASE}body{{background:#f3f6f7;padding-bottom:0}}main{{max-width:1240px;margin:0 auto;padding:40px 20px 64px}}
.top{{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:end;gap:20px;margin-bottom:28px}}.top p{{max-width:62ch;margin:0}}
.flag{{display:inline-block;background:#111;color:#ffcb2a;font-weight:900;letter-spacing:.06em;border-radius:99px;padding:.35em 1em;font-size:.85rem;margin-bottom:14px}}.flag a{{color:#fff}}
.row{{display:grid;grid-template-columns:1.15fr 1fr;gap:36px;align-items:start;background:#fff;border-radius:32px;padding:28px;margin-bottom:28px;border-left:12px solid var(--yellow)}}
.row2{{border-left-color:var(--teal)}}.row3{{border-left-color:var(--orange)}}
.shot{{display:block;border-radius:18px;overflow:hidden;box-shadow:0 18px 40px -22px rgba(7,41,59,.55);border:1px solid var(--line);background:#fff}}.shot img{{width:100%;display:block}}.shot:hover{{transform:translateY(-3px)}}
.bar{{display:flex;gap:6px;padding:9px 12px;background:#eef1f3;border-bottom:1px solid var(--line)}}.bar i{{width:10px;height:10px;border-radius:50%;background:#c9d2d6}}
.num{{display:inline-block;background:var(--navy-8);border-radius:99px;padding:.2em .9em;font-weight:900;font-size:.85rem}}.info h2{{margin:.35em 0 .3em}}.info h2 a{{color:var(--navy);text-decoration:none}}
.feats{{margin:0 0 16px;padding-left:1.2em}}.info h3{{font-size:.85rem;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);margin:22px 0 10px}}
.pl{{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:8px}}.pl a{{display:block;padding:.4em .9em;border:2px solid var(--navy);border-radius:99px;color:var(--navy);text-decoration:none;font-weight:700}}.pl a:hover{{background:var(--navy);color:#fff}}
.ins{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}}.ins figure{{margin:0}}.ins img{{width:100%;aspect-ratio:5/4;object-fit:cover;object-position:top;border-radius:12px;border:1px solid var(--line)}}.ins figcaption{{font-size:.8rem;color:var(--muted);margin-top:4px;line-height:1.3}}
@media(max-width:900px){{.row{{grid-template-columns:1fr;padding:18px;border-left-width:8px}}}}</style></head>
<body><main><div class="top"><div><span class="flag">MOCKUP &amp; PROTOTYPE ONLY &middot; by <a href="https://veemercado.com">veemercado.com</a></span><br><img src="assets/img/logo.png" alt="Northern Rivers Community Resilience Alliance" style="height:52px;margin:6px 0 12px"><h1>Website prototypes</h1></div>
<p>Three directions for the five-page NRCRA website (Home, About, Partners, Network, R.A.C.K), each drawn from a different part of the mood board. Sample content only. To be built in Wix Classic. Status: draft for direction review.</p></div>
{rows}</main></body></html>'''


def write(path, s):
    p = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(s)


if __name__ == "__main__":
    write("v1/index.html", v1())
    write("v2/index.html", v2())
    write("v3/index.html", v3())
    write("index.html", dashboard())
    write("robots.txt", "User-agent: *\nDisallow: /\n")
    print("built")
