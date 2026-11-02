"""Teal-led exploration (teal as accents and tints only): Home, About, Impact (blank) and Network on the designer's Layout Design wireframe
(content and layout only), styled from Prototype 1, with teal as the main driver instead of navy.

  prototype-b  teal as accents and tints only (highlights, buttons, borders, tinted panels), navy kept for the footer

White text never sits on teal (2.99:1). Navy text on teal is 5.05:1.
Imported by build.py, which owns the shared helpers and base CSS.
"""
import csv
import os
import re
import random
import build as B
from build import E, img, logo, screen, icon, BASE, MOBILE, JS, FONT, CSS1, VIMEO, CONTACT

SIGN_IN = "https://rack.nrcra.org.au"  # the R.A.C.K address NRCRA gave us (not live yet)
MENU = [("home", "Home"), ("network", "Network"), ("about", "About"), ("impact", "Impact"), ("rack", "R.A.C.K.")]
# Only Prototype C is published. A (two cards) and B (one green card) are archived: their headers stay available as hero variants below, and snapshots are kept in the git-ignored _archive-* folders.
NAMES = {"prototype-c": "Prototype Round 2"}
SHORT = {"prototype-c": "C"}


# Funder strip directly under the menu bar on every page. Logos we hold: FRRR, HELP Fund (NRMA Insurance) and UCRH; NSW Government and Australian Government logos supplied by NRCRA. The Australian Government logo contains the Commonwealth Coat of Arms, so NRCRA must confirm its funding agreement allows it before this goes live.
FUNDERS = [("Federal Government", "aus-gov.png", "https://www.nema.gov.au"), ("State Government", "nsw.png", "https://www.nsw.gov.au"),
           ("HELP Fund", "help.png", "https://www.nrma.com.au/help-fund"), ("FRRR", "frrr.png", "https://frrr.org.au"),
           ("UCRH", "ucrh-trim.png", "https://ucrh.edu.au")]


def funder_strip():
    def pill(n, f, url):
        logo_html = '<img src="../assets/funders/' + f + '" alt="" loading="lazy">' if f else ""
        return f'<li><a href="{url}" target="_blank" rel="noopener">{logo_html}<span>{E(n)}</span></a></li>'
    pills = "".join(pill(*f) for f in FUNDERS)
    return f'<aside class="funders" aria-label="Our funders"><div class="wrap"><p>Thanks to our funders</p><ul>{pills}</ul></div></aside>'


def nav3():
    chev = '<svg viewBox="0 0 12 8" width="12" height="8" aria-hidden="true" focusable="false"><path d="M1.5 1.5L6 6l4.5-4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

    def item(k, t):
        if k not in DROPS:
            return f'<a href="#{k}" data-nav="{k}">{t}</a>'
        sub = "".join(f'<li><a href="#{k}" data-jump="{i}" data-page="{k}">{lbl}</a></li>' for i, lbl in DROPS[k])
        return (f'<div class="navdrop"><a href="#{k}" data-nav="{k}">{t}</a><button type="button" class="dd-btn" aria-expanded="false" aria-controls="{k}-menu" aria-label="{t} page sections">{chev}</button>'
                f'<ul id="{k}-menu" class="ddmenu" aria-label="{t} page sections">{sub}</ul></div>')
    links = "".join(item(k, t) for k, t in MENU)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap head-in"><a href="#home" class="brand" aria-label="NRCRA home">{blogo()}</a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav"><svg class="hb" viewBox="0 0 20 14" width="20" height="14" aria-hidden="true" focusable="false"><path d="M1.5 1.5h17M1.5 7h17M1.5 12.5h17" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>Menu</button>
<nav id="nav" aria-label="Main">{links}<a class="btn btn-cta" href="{SIGN_IN}" target="_blank" rel="noopener">Sign In</a></nav></div></header>
{funder_strip()}'''


def protobar3(cur):
    others = "".join(f'<a class="pb-btn" data-proto="{k}" href="../{k}/" aria-label="{NAMES[k]}"><span class="pb-short" aria-hidden="true">{SHORT[k]}</span><span class="pb-long">{NAMES[k]}</span></a>' for k in NAMES if k != cur)
    return f'''<div class="protobar" role="region" aria-label="Prototype controls"><div class="pb-in">
<p class="pb-label"><b>MOCKUP &amp; PROTOTYPE ONLY</b> by <a href="https://veemercado.com">veemercado.com</a><span class="pb-cur"> &middot; viewing Round 2: {NAMES[cur]}</span></p>
<nav class="pb-nav" aria-label="Round 2 designs"><a class="pb-btn pb-all" href="../#round-2">All prototypes</a>{others}</nav>
<button type="button" class="pb-top" aria-label="Back to top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})"><span class="pb-long">Back to top&nbsp;</span><span aria-hidden="true">&uarr;</span></button></div></div>'''


def vimg(name):
    return f'<img src="{B.IMG}{name}.jpg" alt="" loading="lazy" decoding="async">'


def hl(t):
    return f'<span class="hl">{E(t)}</span>'


def steps():
    st = [("cal", "Come to a gathering", f"{B.GATHER[0]}: {B.GATHER[1]}.", "#home", "Upcoming"),
          ("share", "Share knowledge", "Add what works to the R.A.C.K.", SIGN_IN, "The R.A.C.K"), ("hand", "Partner with us", "Fund or research community-led resilience.", "#impact", "Impact")]
    return '<ol class="steps">' + "".join(f'<li><span class="ci">{icon(i)}</span><b>{E(t)}</b><p>{E(d)}</p><a href="{h}">{E(l)}</a></li>' for i, t, d, h, l in st) + "</ol>"


def part_band():
    return f'<section class="partband"><div class="wrap"><h2>How you can be part of it</h2>{steps()}</div></section>'


# ---------------------------------------------------------------- Home
def hero_card(square=False, cover=False):
    """Two separate cards side by side (A), nearly square video (C), or one green card with the tag above both the title and the video (B)."""
    tag = '<span class="eyebrow">Northern Rivers Community Resilience Alliance</span>'
    tag_top = tag.replace('class="eyebrow"', 'class="eyebrow hsplit-tag"') if cover else ""
    tag_in = "" if cover else tag
    return f'''<div class="hsplit{" hsplit-sq" if square else ""}{" hsplit-bg" if cover else ""}"><div class="wrap"><div class="hsplit-in">{tag_top}<div class="hsolid-text hsplit-l">{tag_in}
<h1>We believe when climate disasters hit, it&rsquo;s the <span class="mark">community{B.SQUIGGLE}</span> that steps up first.</h1><p class="lede">We are a network of grassroots, community-led groups working together to build disaster resilience across the Northern Rivers.</p>
<p class="btnrow"><a class="btn btn-primary" href="#about">Learn About Us</a></p></div>
<div class="hsplit-r" data-video="{VIMEO}">{img("cheer", eager=True, alt="")}<button class="play" aria-label="Play the Alliance sizzle reel video, full screen"><svg viewBox="0 0 88 88" width="88" height="88" aria-hidden="true" focusable="false"><path d="M37 34L55 44L37 54Z" fill="currentColor" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/><path id="wp" d="M13 44A31 31 0 0 0 75 44" fill="none"/><text font-size="8.5" font-weight="800" letter-spacing="1.8" fill="currentColor" text-anchor="middle" style="font-family:inherit"><textPath href="#wp" startOffset="50%">WATCH</textPath></text></svg></button></div></div></div></div>'''


def hero_photo():
    """Prototype B: full-width photo with the teal gradient and white text."""
    return f'''<div class="hero1 herobg"><div class="wrap"><div class="h1-panel tpanel"><span class="eyebrow">Northern Rivers Community Resilience Alliance</span>
<h1>We believe when climate disasters hit, it&rsquo;s the <span class="mark">community{B.SQUIGGLE}</span> that steps up first.</h1><p class="lede">We are a network of grassroots, community-led groups working together to build disaster resilience across the Northern Rivers.</p>
<p class="btnrow"><a class="btn btn-primary" href="#about">Learn About Us</a><button type="button" class="btn btn-ghost hvid watchbtn" data-video="{VIMEO}" aria-label="Watch the Alliance sizzle reel video, full screen"><svg viewBox="0 0 14 16" width="14" height="16" aria-hidden="true" focusable="false"><path d="M3 3l8 5-8 5z" fill="currentColor" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/></svg>Watch reel</button></p></div>
<div class="h1-photo" data-video="{VIMEO}">{img("cheer", eager=True, alt="")}<button class="play" aria-label="Play the Alliance sizzle reel video, full screen"><svg viewBox="0 0 88 88" width="88" height="88" aria-hidden="true" focusable="false"><path d="M37 34L55 44L37 54Z" fill="currentColor" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/><path id="wp" d="M13 44A31 31 0 0 0 75 44" fill="none"/><text font-size="8.5" font-weight="800" letter-spacing="1.8" fill="currentColor" text-anchor="middle" style="font-family:inherit"><textPath href="#wp" startOffset="50%">WATCH</textPath></text></svg></button></div></div></div>'''


def hero_green():
    """Prototype B: a copy of C's header, but one green card covers the back of the video (the video sits on the green)."""
    return hero_card(square=True, cover=True)


def hero_solid():
    """Prototype C: A's header, but the video card is always almost square (a little wider than tall) and sits in the middle of the text card's height."""
    return hero_card(square=True)


HEROES = {"card": hero_card, "photo": hero_photo, "solid": hero_solid, "green": hero_green}
HERO_FOR = {"prototype-a": "card", "prototype-b": "green", "prototype-c": "solid"}  # a and b are archived (not built)


def home_body(hero="photo"):
    lgas = "".join(f'<li><a href="#lga-{slug(n)}">{E(n)} LGA</a></li>' for n in ["Tweed", "Byron", "Kyogle", "Lismore", "Richmond Valley", "Ballina", "Tenterfield", "Clarence Valley"])
    return f'''{HEROES[hero]()}
<section class="sec hwrow" style="padding-top:0"><div class="wrap hwbg"><span class="hwd hwd-blob" aria-hidden="true"></span>{B.deco("rings", "hwd-rings")}<span class="hwd hwd-dot hwd-dt" aria-hidden="true"></span><span class="hwd hwd-dot hwd-do" aria-hidden="true"></span><ul class="hwpills" aria-label="How we work"><li><a class="hp-teal" href="#about" data-jump="ab-how" data-page="about">Connect.</a></li><li><a class="hp-yellow" href="#about" data-jump="ab-how" data-page="about">Share.</a></li><li><a class="hp-orange" href="#about" data-jump="ab-how" data-page="about">Care.</a></li></ul></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><div class="card wwa surface"><div><h2>60+ groups in 8 Local Government Areas,<br>one region, <span class="mark">one network.{B.SQUIGGLE}</span></h2><p class="subline">Community knowledge, lived experience and shared learning.</p><p>Since early 2024, groups and organisations across the Northern Rivers have joined together to form the Resilience Alliance, a community-led network focused on collective care, preparedness and regional strength.</p><p>Neighbours became first responders in 2022. Today, those neighbours are building the systems that will protect communities before the next disaster.</p>
<p class="btnrow"><a class="btn btn-primary" href="#network">Explore the Network</a></p></div><div class="wwa-cluster"><div class="circles">{B.deco("rings", "")}{vimg("group-3")}{vimg("group-2")}<span class="blob" aria-hidden="true"></span></div><ul class="lgapills">{lgas}</ul></div></div></div></section>
<section class="sec"><div class="wrap"><div class="statcard impact"><h2 class="sechead">Our Impact</h2>{B.stats()}<p class="btnrow"><a class="btn btn-tertiary" href="#impact">See Impact</a></p></div></div></section>'''


# ---------------------------------------------------------------- About
MEAL6 = [("Includes Everyone", "People feel respected and able to participate.", "people"), ("Builds Trust", "Relationships and cooperation grow over time.", "connect"),
         ("Shares Power", "Groups influence priorities, leadership and decisions.", "share"), ("Builds Capability", "Groups gain skills, resources and confidence.", "grow"),
         ("Learns and Adapts", "Feedback leads to practical changes.", "improve"), ("Creates Collective Value", "Groups gain what they couldn’t achieve alone.", "strengthen")]


TEAM = [("Kathie Heyman", "Network Lead"), ("Milou Muiser", "Communications, Events and Engagement"),
        ("Marlena Sue Basser", "Capacity Building Coordinator"), ("Claire McLisky", "Capacity Building Coordinator"), ("Barbara Winters", "Capacity Building Coordinator")]


def team():
    lis = [f'<li><span class="tc" aria-hidden="true">{"".join(w[0] for w in n.split()[:2])}</span><b>{n}</b><span>{r}</span></li>' for n, r in TEAM]
    return '<ul class="team2">' + "".join(lis[:2]) + '<li class="brk" aria-hidden="true"></li>' + "".join(lis[2:]) + '</ul>'


STEER = [("Together Pottsville", "https://www.togetherpottsville.org", "together-pottsville.png", ""),
         ("Murwillumbah CORE", "https://www.mcore2484.org", "murwillumbah-core.webp", ""),
         ("Resilient Uki", "https://resilientuki.org", "resilient-uki.png", ""),
         ("South Golden Beach, New Brighton, Ocean Shores", "https://www.facebook.com/groups/431100262102216/", "sgb-nb-os-crt-stacked.png", ""),
         ("Main Arm Disaster Response", "https://www.madr.org.au/", "madr.png", ""),
         ("Resilient Lismore", "https://resilientlismore.org.au", "resilient-lismore.png", ""),
         ("Northern Rivers Community Foundation", "https://nrcf.org.au", "nrcf.png", ""),
         ("Plan C", "https://www.planc.org.au", "plan-c-black.png", ""),
         ("University Centre for Rural Health", "https://ucrh.edu.au", "ucrh.svg", "")]
_FIRST = ["Resilient Lismore", "Northern Rivers Community Foundation", "University Centre for Rural Health", "Resilient Uki", "Main Arm Disaster Response", "Plan C"]
STEER.sort(key=lambda r: _FIRST.index(r[0]) if r[0] in _FIRST else len(_FIRST))


def steer_tiles():
    out = ""
    for n, u, f, x in STEER:
        box = f'<img src="../assets/img/steer/{f}" alt="" loading="lazy">' if f else f'<span class="sinit" aria-hidden="true">{x}</span>'
        out += f'<li><a href="{u}" target="_blank" rel="noopener"><span class="slogo{" dark" if x == "dark" else ""}">{box}</span><span class="sname">{n}</span><span class="sr-only"> (opens in a new tab)</span></a></li>'
    return '<ul class="steer">' + out + '</ul>'


FOCUS = [("Growing the Alliance", "We are strengthening our network by clarifying who we are, why we come together and how we work. Through regular gatherings we are building a clearer picture of who is involved and how we connect."),
         ("Training and Resource Sharing", "We are making knowledge, practical tools and training easier to find through our Resilience Alliance Community Knowledge Hub. Our training is led by experienced locals, with the aim of strengthening our network from within the community."),
         ("Peer Support and Self Care", "Resilience work asks a lot of the people who do it, so we are committed to balanced wellbeing and collective care across our region. We are mapping the support already available, identifying good practice, with the aim to develop an adaptable wellbeing framework that groups can use to look after themselves and each other."),
         ("Funding and Collaborative Projects", "We are working towards a more sustainable and collaborative approach to funding for resilience work across the region. Identifying shared opportunities we aim to reduce competition and increase collective impact."),
         ("Advocacy", "We believe our collective voice is stronger than any single group&rsquo;s. By understanding our own network, identifying key stakeholders and building advocacy skills among members, we are developing a collaborative approach to advocating for resilient communities across the region.")]


FOCUS_PHOTOS = ["group", "workshop", "pair", "table", "speaker"]  # sample photos from the existing set


def focus_cards():
    cards = "".join(f'<li><div class="fph">{img(FOCUS_PHOTOS[i - 1], alt="")}<span class="pi pnum">{i:02d}</span></div><div class="fbody"><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(FOCUS, 1))
    return '<ol class="pillcards focuscards">' + cards + "</ol>"


MEAL_RING = [("Connect", "#00857c", "#fff"), ("Listen", "#f05a28", "#fff"), ("Reflect", "#ffcb2a", "#07293b"), ("Improve", "#00857c", "#fff"), ("Share", "#f05a28", "#fff"), ("Strengthen", "#ffcb2a", "#07293b")]


def meal_ring():
    import math
    dots = ""
    pts = []
    for i, (n, bg, fg) in enumerate(MEAL_RING):
        a = math.radians(-90 + 60 * i)
        x, y = 50 + 36 * math.cos(a), 50 + 36 * math.sin(a)
        pts.append(f"{x:.1f},{y:.1f}")
        dots += f'<li style="left:{x:.1f}%;top:{y:.1f}%;background:{bg};color:{fg}">{n}</li>'
    return (f'<div class="mealwrap"><div class="mealring"><svg viewBox="0 0 100 100" aria-hidden="true"><polygon points="{" ".join(pts)}" fill="none" stroke="#beddda" stroke-width="1.2"/></svg><ol>{dots}</ol></div>'
            '<blockquote class="mealq"><p class="mq">&ldquo;What is your group doing differently as a result of being part of the Alliance?&rdquo;</p>'
            '<p>Rather than only counting activities, we look for real changes in relationships, knowledge, capability and collective action, gathered through conversations at Gatherings and site visits, and turned into shared stories.</p></blockquote></div>')


ABOUT_JUMP = [("ab-vision", "Vision &amp; Mission"), ("ab-how", "How we work"), ("ab-focus", "Our focus"), ("ab-journey", "Our journey"), ("ab-steering", "Steering committee"), ("ab-team", "Meet the team")]


NETWORK_JUMP = [("nw-map", "Region map"), ("nw-stories", "Our stories"), ("our-network", "Explore our network")]
DROPS = {"about": ABOUT_JUMP, "network": NETWORK_JUMP}


def about_body():
    return f'''    <div class="wrap"><div class="splith ab rev"><div class="ph">{img("line", eager=True)}</div><div><span class="eyebrow pill-t">About us</span><h1>We know communities are stronger when they&rsquo;ve built trusted relationships <span class="mark">together.{B.SQUIGGLE}</span></h1></div></div></div>
<section class="sec" id="ab-vision" style="padding-top:0"><div class="wrap"><div class="aboutgrid"><div class="card abt"><h2><span class="hlx hlx-t">The Resilience Alliance</span></h2><p>Established in November 2023. Its roots lie in a run of compounding disasters: the 2017 floods, the 2019&ndash;20 bushfires, and the catastrophic floods and landslides of 2022. In each, local community organisers played a vital role in response, recovery and adaptation. Research in the years that followed found that these grassroots groups wanted stronger connections with each other for peer-to-peer support. That showed the need for regional collaboration in disaster resilience.</p><p>We support a network of place-based resilience groups to develop their own local approaches to risk reduction, preparedness and recovery, for fire, flood, landslides and whatever comes next.</p><p>The Resilience Alliance helps government agencies, councils and emergency services deliver on the commitments of the NSW State Emergency Management Plan, State Disaster Mitigation Plan and regional resilience priorities by connecting formal systems with trusted, community-led action.</p><div class="bar bar-t" aria-hidden="true"></div></div>
<div class="vpcol"><div class="card vpc"><h2><span class="hlx hlx-y">Vision</span></h2><p>Connected, collaborative Northern Rivers communities that are empowered to care for themselves and each other before, during and after disasters.</p><div class="bar bar-y" aria-hidden="true"></div></div>
<div class="card vpc"><h2><span class="hlx hlx-o">Purpose</span></h2><p>To develop a self-sustaining, trusted Alliance of place-based, community-led resilience groups and organisations. The Alliance shares knowledge and resources, provides mutual support and wellbeing, takes collective action and advocates for identified community needs.</p><div class="bar bar-o" aria-hidden="true"></div></div></div></div></div></section>
<section class="sec" id="ab-how" style="padding-top:0"><div class="wrap"><h2 class="sechead">How we work</h2><p class="lede">Through regular gatherings, deep conversations and shared experiences, the Resilience Alliance is building a community-led network focused on collective care, preparedness and regional strength.</p>{how_cards()}</div></section>
<section class="sec" id="ab-focus" style="padding-top:0"><div class="wrap"><h2 class="sechead">{hl("Our Focus")}</h2>{focus_cards()}</div></section>
<section class="sec journey" id="ab-journey"><div class="wrap"><h2 class="sechead">Our journey</h2>{journey_b()}</div></section>
<section class="sec steersec" id="ab-steering" style="padding-top:0"><div class="wrap"><div class="steergrid"><div class="steertxt"><h2 class="sechead">The Steering Committee:</h2><p class="lede">Is the coordinating body for the Resilience Alliance. It is made up of representatives from resilience-related groups and organisations across the region, and operates by agreement among groups and organisations rather than by reporting to a separate incorporated parent body. The steering committee actively aims to maintain a network that reflects the geographic and community diversity of the region.</p></div><div class="steerlist"><p class="lede">The Steering Committee comprises the following groups and organisations.</p>{steer_tiles()}</div></div></div></section>
<section class="sec teamsec" id="ab-team" style="padding-top:0"><div class="wrap"><div class="bar bar-t sbar-top" aria-hidden="true"></div><h2 class="sechead cen teamhead">Resilience Alliance Team:</h2>{team()}<div class="bar bar-t sbar-bot" aria-hidden="true"></div></div></section>'''


# ---------------------------------------------------------------- Network
HOW = [("Connect", "50+ grassroots, community-led groups are connected together across the region so they can build trusting relationships with each other so they know who to contact when the next climate disaster hits.", "teal"),
       ("Share", "Sharing knowledge, experience, practical tools and resources across the network so everyone can benefit from what others have learned.", "yellow"),
       ("Care", "Peer to peer support, reducing the load, removing duplication and placing a real value on the efforts of all.", "orange")]


def how_cards():
    return '<ul class="howcards">' + "".join(f'<li class="hw-{c}"><h3><span>{t}.</span></h3><p>{d}</p></li>' for t, d, c in HOW) + "</ul>"


FUND = lambda t: f'<p class="fund">{t}</p>'
JOURNEY_B = [
    ("2022", [("Floods &amp; disaster:", "Communities responded to the floods, showing local leadership and the need for stronger regional collaboration.", "")]),
    ("2023", [("Building connections:", "A Sydney Environment Institute &amp; UCRH study documents community self organisation after the floods &mdash; the evidence base that leads participants to call for <strong><em>a regional alliance.</em></strong>", "")]),
    ("2024", [("Resilience Alliance established:", "The inaugural regional gathering with 96 participants from 40+ groups across the Northern Rivers formally establishes the Resilience Alliance.", ""),
              ("Co-designing the future:", "Groups develop the Resilience Alliance&rsquo;s distributed governance model and strategic priorities.", "Funded by the University of Centre of Rural Health.")]),
    ("2025", [("Capability in action:", "The Resilience Alliance trains 20 groups on spontaneous volunteer management systems, supporting groups post Cyclone Alfred.", "Funded by the NSW Government&rsquo;s Spontaneous Volunteering Program and Foundation for Regional and Rural Renewal.")]),
    ("2026", [("Connected, Prepared Communities:", "Disaster Ready Fund 3 investment supports the next stage of capability and resilience-building with 60 groups throughout the Northern Rivers.", "Funded by the Australian Government and NSW Government."),
              ("Participatory granting project:", "17 groups receive up to $10,000 in funding as part of the first round of a newly developed participation funding process.", "Funding by The NRMA Help Fund, Monash University and Northern Rivers Community Foundation.")]),
]


# Archived for now (not shown on the site): the 2027+ timeline entry.
JOURNEY_ARCHIVE = [
    ("2027+", [("Onwards:", 'Our research and MEAL process<span class="fund-i">Monitoring, Evaluation, Accountability and Learning</span>continues alongside the Alliance as it supports and resources groups in the network.', "")]),
]


def journey_b():
    return '<ol class="river">' + "".join(
        f'<li><b>{y}</b><div class="jt">' + "".join(f'<h3>{h}</h3><p>{t}</p>' + (f'<p class="fund">{f}</p>' if f else "") for h, t, f in es) + '</div></li>'
        for y, es in JOURNEY_B) + "</ol>"


def pillar_cards(nums=False):
    if nums:
        return '<ol class="pillcards">' + "".join(f'<li><span class="pi pnum">{i:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p></li>' for i, (t, d, k) in enumerate(B.PILLARS, 1)) + "</ol>"
    return '<ol class="pillcards">' + "".join(f'<li><span class="pi">{icon(k)}</span><span class="pn">{i:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p></li>' for i, (t, d, k) in enumerate(B.PILLARS, 1)) + "</ol>"


# Real group list from the Alliance spreadsheet, cleaned by tools/clean_groups.py (visible rows, duplicates removed, LGA and Aboriginal Country split,
# links matched to groups). Membership of the Alliance to be confirmed by NRCRA. A group links to its website, or to Facebook when it has no website.


def short_lga(official):
    return re.sub(r"\s+(Shire|Council|City)$", "", official)


def blogo(cls="logo"):
    """Brand logo (horizontal, supplied artwork). Width and height attributes keep the true 1000x230 ratio."""
    return f'<img src="{B.IMG}logo-brand.png" alt="Northern Rivers Community Resilience Alliance" class="{cls}" width="1000" height="230">'


def slug(t):
    return re.sub(r"[^a-z]+", "-", t.lower()).strip("-")


def all_groups():
    out = []
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "network_groups.csv"), newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out.append((r["Group Name"], r["Location"], short_lga(r["LGA"]), r["LGA"], r["Aboriginal Country"], r["Website"], r["Facebook"]))
    return sorted(out, key=lambda g: g[0].lower())


LGA_ORDER = sorted({g[2] for g in all_groups()})


def group_card(name, loc, key, lga, country, web, fb):
    place = f"{loc}, {lga}" if loc else lga
    ctry = f'<span class="ctry">{E(country)}</span>' if country else ""
    url = web or fb
    btn = f'<a class="btn btn-ghost btn-sm" href="{E(url)}" target="_blank" rel="noopener">Visit Page<span class="sr-only"> (opens in a new tab)</span></a>' if url else ""
    return f'<li><b>{E(name)}</b><span>{E(place)}</span>{ctry}{btn}</li>'


def lga_select(cur=""):
    first = "Browse the region"
    opts = f'<option value="{"network" if cur else ""}">{first}</option>'
    opts += "".join(f'<option value="lga-{slug(l)}"{" selected" if l == cur else ""}>{E(l)} LGA</option>' for l in LGA_ORDER)
    return f'<select class="lgasel" aria-label="Filter the network by Local Government Area (LGA)" data-cur="{"lga-" + slug(cur) if cur else ""}">{opts}</select>'


def dir_head(title, cur="", tag="h2"):
    return f'<div class="dirhead"><{tag} class="sechead">{title}</{tag}>{lga_select(cur)}</div>'


# Quotes are sample content. Names are real Alliance groups from the network list; the 2nd and 6th stories are videos (both the sizzle reel for now).
STORIES = [
    ("laughing", "Like a whole region of neighbours in your corner.", "Resilient Lismore Inc", False),
    ("circle", "Like a family we did not know we had.", "Together Pottsville Inc", True),
    ("hug", "Like finally being heard by people who have been through it too.", "Wardell Community Organised Resilience Effort (CORE)", False),
    ("listening", "We learned more in one afternoon than in a year on our own.", "Resilient Uki", False),
    ("talk", "We went from a few people on a phone tree to a whole street that checks in.", "Main Arm Disaster Recovery Inc", False),
    ("crowd", "Seeing what other groups had done gave us the courage to start.", "Nimbin Disaster Resilience Group", True),
]


def testimonials():
    play = '<svg viewBox="0 0 88 88" width="88" height="88" aria-hidden="true" focusable="false"><path d="M37 34L55 44L37 54Z" fill="currentColor" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/></svg>'

    def card(key, quote, who, video):
        if video:
            ph = f'<div class="tph vid" data-video="{VIMEO}">{img(key, alt="")}<button class="play" aria-label="Play the video: {E(who)}, full screen">{play}</button></div>'
        else:
            ph = f'<div class="tph">{img(key, alt="")}</div>'
        return f'<li>{ph}<blockquote><p>&ldquo;{E(quote)}&rdquo;</p><footer>&mdash; {E(who)}</footer></blockquote></li>'
    cards = "".join(card(*st) for st in STORIES)
    return f'<section class="sec stories" id="nw-stories" style="padding-top:0"><div class="wrap"><div class="bar bar-y sbar-top" aria-hidden="true"></div><h2 class="sechead cen">Our Stories</h2><ul class="tcards">{cards}</ul><div class="bar bar-y sbar-bot" aria-hidden="true"></div></div></section>'


def network_body():
    cards = "".join(group_card(*g) for g in all_groups())
    return f'''<div class="wrap" id="nw-map"><div class="splith net"><div><span class="eyebrow">Network</span><h1>50+ groups,<br>one region,<br><span class="mark">one network.{B.SQUIGGLE}</span></h1><p class="lede">8 Local Government Areas (LGAs) across the Northern Rivers region of New South Wales, Australia.</p></div><div class="ph">{B.map_embed().split('<p class="vnote">')[0]}</div></div></div>
{testimonials()}
<section class="sec" id="our-network"><div class="wrap">{dir_head("Our Network")}<ul class="gsub">{cards}</ul></div></section>'''


def lga_body(lga):
    cards = "".join(group_card(*g) for g in all_groups() if g[2] == lga)
    return f'<section class="sec"><div class="wrap">{dir_head("Our Network", lga, "h1")}<ul class="gsub">{cards}</ul></div></section>'


RACK_CATS = [
    ("Get Ready", "Plans and checklists for before a disaster."),
    ("Volunteers", "Registering, inducting and looking after volunteers."),
    ("Run Your Group", "Governance, templates and running a healthy group."),
    ("Emergencies", "What to do and who to call when it happens."),
    ("Training &amp; Workshops", "Workshops and learning for group leaders."),
]


def rack_body():
    cards = "".join(f'<li><span class="pn">{i:02d}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(RACK_CATS, 1))
    return f'''<div class="wrap"><div class="splith"><div><span class="eyebrow pill-t">Resilience Alliance Community Knowledge.</span><h1>The R.A.C.K.</h1><p class="lede">One shared place where the whole network can find what already works from years of real community experience across the Northern Rivers.</p><p>Access is for Alliance groups. Contact the Network Lead to get set up.</p>
<p class="btnrow"><a class="btn btn-ghost" href="mailto:hello@nrcra.org.au?subject=R.A.C.K.%20access">Request Access</a><a class="btn btn-ghost" href="mailto:hello@nrcra.org.au?subject=R.A.C.K.%20help">Get Help</a><a class="btn btn-primary" href="{SIGN_IN}" target="_blank" rel="noopener">Sign In</a><a class="rackrev" href="#privacy">Privacy Policy</a></p></div>
<div class="ph rackph"><img src="../assets/img/rack-hero.webp" alt="A community member using the R.A.C.K. on a desktop computer, searching the shared resource library." width="1024" height="799" loading="eager" decoding="async"></div></div></div>
<section class="sec"><div class="wrap rackhead"><h2 class="sechead">In this resource library</h2><p class="lede">You&rsquo;ll find templates and guides you can use straight away, and contribute knowledge back in two minutes.</p><ol class="pillcards rackcats">{cards}</ol></div></section>'''


FLAG_ICON = '<svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true" focusable="false"><path d="M6 21V4" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/><path d="M6 5h11.5l-2.8 4.2 2.8 4.2H6z" fill="currentColor"/></svg>'


# Privacy Policy page: simple numbered items. "have" = text already on NRCRA's current Privacy Policy page (or site footer); "add" = consider adding.
PP = [
    ("add", "A legal disclaimer", "Says the page is only a general explanation, is not legal advice, and recommends getting legal advice.", "Template text from the website builder. Replace it with NRCRA's own wording."),
    ("add", "Privacy Policy: the basics", "Explains what a privacy policy is: a statement of how a website collects, uses and manages visitors' information and protects their privacy.", "Template text from the website builder. Replace it with NRCRA's own wording."),
    ("add", "What to include in a Privacy Policy", "Lists the topics a policy usually covers: what is collected and how, why, sharing with others, how people use their rights, and information about minors.", "Advice for the website owner, not a policy for visitors. The items below cover these topics."),
    ("add", "Who we are", "The Northern Rivers Community Resilience Alliance (NRCRA) is a community-led network of local resilience groups across the Northern Rivers of New South Wales.", ""),
    ("add", "What personal information we collect", "Names, email addresses and phone numbers, your group and role, event registrations, messages you send us, and basic details about your visit to our website.", ""),
    ("add", "How we collect it", "From you directly (forms, emails and events), from your group when it nominates you, and automatically through cookies and website analytics.", ""),
    ("add", "Why we collect and use it", "To run the network and events, answer questions, send updates you ask for, manage R.A.C.K. access, report to funders in summary form, and meet legal obligations.", ""),
    ("add", "Who we share it with", "We do not sell personal information. We share it only with providers who help run our website, email, events and the R.A.C.K., with partners when you agree, or when the law requires it.", "To confirm: which providers, and whether any store information outside Australia."),
    ("add", "Storage and security", "We keep personal information in secure systems with limited access, and delete it or remove identifying details when we no longer need it.", ""),
    ("add", "R.A.C.K. sign-in", "Signing in to the R.A.C.K. is part of NRCRA's compliance process. When you sign in, the NRCRA Terms and Conditions and this Privacy Policy apply. We collect your name, email, group, role and sign-in dates and times to manage access and keep the R.A.C.K. secure.", "Needs both documents: this policy and the Terms and Conditions below."),
    ("add", "Terms and Conditions for R.A.C.K. sign-in", "The rules for using the R.A.C.K. that people agree to when they sign in.", "No Terms and Conditions page exists on the current website. NRCRA needs to supply one."),
    ("add", "Cookies and website analytics", "Our website uses cookies to work and to understand how people use it. You can refuse cookies in your browser settings.", ""),
    ("add", "Children and young people", "Whether and how NRCRA handles information about minors.", "The template text mentions minors' information. NRCRA to decide the wording and age."),
    ("add", "Access and correction", "You can ask to see the personal information we hold about you and ask us to correct it.", ""),
    ("add", "Complaints", "Tell us if you think we have handled your information badly. You can also contact the Office of the Australian Information Commissioner at oaic.gov.au.", ""),
    ("add", "Changes to this policy", "We may update this policy and will show the date it was last changed.", ""),
    ("have", "Contact us", "Email hello@nrcra.org.au or contact the Network Lead, Kathie Heyman, on 0417 683 546.", "The Network Lead's details are already in the current website footer."),
]
CHECK_ICON = '<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
FLAG_SMALL = FLAG_ICON.replace('width="26" height="26"', 'width="14" height="14"')


def pp_item(i, kind, title, text, note):
    tag = (f'<span class="pptag tag-have">{CHECK_ICON}Already on the site</span>' if kind == "have"
           else f'<span class="pptag tag-add">{FLAG_SMALL}Not on the site: recommend adding</span>')
    note_html = f'<p class="ppnote">{note}</p>' if note else ""
    return f'<li class="ppitem"><span class="ppnum">{i:02d}</span><div><div class="pprow">{tag}<h2>{title}</h2></div><p>{text}</p>{note_html}</div></li>'


def privacy_body():
    items = "".join(pp_item(i, *row) for i, row in enumerate(PP, 1))
    have = f'<span class="pptag tag-have">{CHECK_ICON}Already on the site</span>'
    add = f'<span class="pptag tag-add">{FLAG_SMALL}Not on the site: recommend adding</span>'
    return f'''<div class="wrap"><div class="pg-head pphead"><span class="eyebrow pill-t">Legal</span><h1>Privacy Policy</h1><p class="lede">How NRCRA collects, uses and protects your personal information.</p>
<p class="pplegend">{have} is on NRCRA&rsquo;s current Privacy Policy page or website footer. {add} means NRCRA does not have this yet, so we recommend adding it. It is new draft wording for NRCRA and its legal adviser to review before anything goes live.</p></div></div>
<section class="sec" style="padding-top:0"><div class="wrap"><ol class="pplist2">{items}</ol></div></section>'''


def impact_body():
    return '<div class="wrap"><div class="pg-head"><h1>Impact</h1></div></div>'


# ---------------------------------------------------------------- CSS
CSS_T = """
body.teal{--bg:#f3f6f7;--r:28px}
.teal .sechead{margin-bottom:28px}
/* title highlight is off for now; the class stays so it can come back */
.hl{padding:0}
.teal .card{border-radius:var(--r);padding:32px}
.wwa{display:grid;grid-template-columns:.9fr 1.1fr;gap:48px;align-items:center}.wwa>*{min-width:0}.wwa-map{max-width:420px;justify-self:center;width:100%}.wwa-cluster{width:100%;order:-1;padding-top:calc(5.7% - 10px)}.mark{isolation:isolate}.mark .squig{z-index:-1}.vp-text{max-width:72ch}
.lgapills{list-style:none;margin:12px 0 0;padding:0;display:flex;flex-wrap:wrap;justify-content:center;gap:6px 6px}.lgapills li{position:relative;isolation:isolate;padding:.25em .85em;font-weight:700;font-size:.88rem;line-height:1.25;color:#586c74}.lgapills li::before{content:"";position:absolute;inset:-4px -7px;z-index:-1;background:url(../assets/brush/brush-1.svg) center/100% 100% no-repeat}.lgapills li:nth-child(3n+2)::before{background:url(../assets/brush/brush-2.svg) center/100% 100% no-repeat}.lgapills li:nth-child(3n)::before{background:url(../assets/brush/brush-3.svg) center/100% 100% no-repeat}
.statrow{display:grid;grid-template-columns:1.1fr .9fr;gap:16px;align-items:center}.statrow>*{min-width:0}.statcard{border-radius:var(--r);padding:32px}.statcard .stats dt{color:var(--navy)}
.framed{border-radius:28px;padding:14px;background:var(--fr,var(--teal))}.framed img{border-radius:14px;width:100%;aspect-ratio:4/3;object-fit:cover}
.pcard2 .p3{align-items:center}
.partband{padding:56px 0 52px;text-align:center}.partband h2{margin-bottom:24px}
.steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.steps li{display:grid;justify-items:center;gap:8px}.steps .ci{width:76px;height:76px;border-radius:50%;background:#fff;border:3px solid var(--ci);display:grid;place-items:center;color:var(--navy)}.steps .ci .ico{width:34px;height:34px}.steps a{font-weight:800}.steps p{margin:0;font-size:.95rem}
.steps li:nth-child(1){--ci:var(--orange)}.steps li:nth-child(2){--ci:var(--navy)}.steps li:nth-child(3){--ci:var(--navy)}.steps li:nth-child(4){--ci:var(--orange)}
@media(max-width:860px){.wwa,.statrow{grid-template-columns:1fr}.steps{grid-template-columns:1fr 1fr}.teal .card{padding:26px 20px}}
.teal .kb li{border-bottom:10px solid var(--kc)}.kb li:nth-child(1){--kc:var(--teal)}.kb li:nth-child(2){--kc:var(--yellow)}.kb li:nth-child(3){--kc:var(--orange)}
.splith{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center;padding:32px 0 12px}.splith>*{min-width:0}.splith .ph img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:28px}.splith .ph .mapbox{height:380px;border-radius:28px}.splith.rev .ph{order:-1}
@media(max-width:860px){.splith{grid-template-columns:1fr}.splith.rev .ph{order:0}}
.script{font:700 1.5rem Caveat,cursive;color:var(--orange-d);display:block;margin-bottom:2px}
.vp-wrap{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center}.vp-wrap>*{min-width:0}@media(max-width:860px){.vp-wrap{grid-template-columns:1fr}}
.circles{position:relative;width:100%;max-width:560px;margin:0 auto -60px;aspect-ratio:1/1.14;transform:translateX(calc(-6.75% - 6px))}.circles img{position:absolute;border-radius:50%;object-fit:cover;border:8px solid #fff;aspect-ratio:1/1;height:auto}
.circles img:nth-of-type(1){width:66%;left:15%;top:0;z-index:2}.circles img:nth-of-type(2){width:60%;left:22%;bottom:calc(-8% + min(50px,11%));z-index:1;translate:0 -60px}
.circles .blob{position:absolute;left:calc(6.5% + 12px);top:calc(-5% + 10px);width:30%;aspect-ratio:1/1;z-index:3;background:var(--yellow);border-radius:62% 38% 55% 45%/48% 60% 40% 52%}

.deco{position:absolute;pointer-events:none;width:150px;height:150px}.circles .deco-rings{z-index:0;width:46%;height:auto;right:-7%;left:auto;top:26%}
@media(max-width:560px){.circles{margin-bottom:-32px}.circles img:nth-of-type(2){translate:0 -36px}}
@media(max-width:760px){.circles img{border-width:6px}}
.meal{margin:18px 0 22px}.mealgrid{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(6,1fr);gap:16px}.mealgrid li{background:var(--grey-6);border-radius:16px;padding:18px 14px}.mealgrid .ico{width:34px;height:34px;color:var(--navy);margin-bottom:8px}.mealgrid h3{font-size:1rem;margin:0 0 .3em}.mealgrid p{margin:0;font-size:.9rem}
@media(max-width:1000px){.mealgrid{grid-template-columns:repeat(3,1fr)}}@media(max-width:560px){.mealgrid{grid-template-columns:1fr 1fr}}
.team2{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;justify-content:center;gap:16px}.team2 li{width:150px;text-align:center;display:grid;justify-items:center;gap:4px}.team2 .tc{width:96px;height:96px;border-radius:50%;background:var(--teal-25);display:grid;place-items:center;font-weight:800;font-size:.9rem}.team2 li span:not(.tc){font-size:.9rem;color:var(--muted)}
.pillcards{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:16px;justify-content:center}.pillcards li{flex:1 1 200px;max-width:230px;background:#fff;border-radius:28px;padding:22px 18px;text-align:center;border-bottom:14px solid var(--pc)}
.pillcards li:nth-child(1){--pc:var(--teal)}.pillcards li:nth-child(2){--pc:var(--yellow)}.pillcards li:nth-child(3){--pc:var(--orange)}.pillcards li:nth-child(4){--pc:var(--navy)}.pillcards li:nth-child(5){--pc:#9fb0b8}
.pillcards .pi{width:52px;height:52px;border-radius:50%;background:var(--grey-6);display:grid;place-items:center;margin:0 auto 6px;color:var(--navy)}.pillcards .pi .ico{width:28px;height:28px}.pillcards .pn{font-weight:900;font-size:.85rem;letter-spacing:.1em}.pillcards h3{margin:.3em 0}.pillcards p{margin:0;font-size:.95rem}
.gdir-c{grid-template-columns:repeat(auto-fill,minmax(220px,1fr))!important;gap:16px!important}.gdir-c li{padding:0 0 16px!important;background:#fff!important;border:1px solid var(--line);border-radius:28px!important;overflow:hidden}.gdir-c .gph{display:block;position:relative;margin-bottom:34px}.gdir-c .gph img{width:100%;height:100px;object-fit:cover}
.gdir-c .gdot{position:absolute;left:14px;bottom:-24px;width:48px;height:48px;border-radius:50%;background:var(--teal);color:var(--navy);border:3px solid #fff;display:grid;place-items:center;font-weight:900}.gdir-c b,.gdir-c span:not(.gph):not(.gdot),.gdir-c em,.gdir-c small{margin:0 16px}.gdir-c small{color:var(--muted);margin-top:6px}

/* Prototype 2's rounded buttons and river-style journey */
body{--btn-r:12px}
ol.river{position:relative;list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(5,1fr);gap:16px}
ol.river::before{content:"";position:absolute;left:0;right:0;top:16px;height:12px;border-radius:99px;background:var(--teal-25)}
ol.river li{position:relative;padding-top:64px;display:block}
ol.river b{position:absolute;top:0;left:0;box-sizing:border-box;height:44px;display:flex;align-items:center;background:#fff;border:3px solid var(--teal);border-radius:99px;padding:0 1.1em;font-weight:900;color:var(--teal-d);font-size:1rem;line-height:1}
ol.river h3{margin:0 0 .25em;font-size:1rem}ol.river p{margin:0 0 .9em;font-size:.95rem}ol.river .jt>*:last-child{margin-bottom:0}ol.river .fund-i{display:block;font-style:italic;font-size:.82rem;color:var(--muted);margin:.15em 0}ol.river .fund{font-style:italic;font-size:.82rem;color:var(--muted);margin-top:-.5em}
@media(max-width:860px){ol.river{grid-template-columns:1fr;gap:16px}ol.river::before{left:42px;right:auto;width:12px;margin-left:-6px;top:0;bottom:0;height:auto}ol.river li{padding:0 0 0 118px;min-height:44px}ol.river b{left:0;width:84px;justify-content:center;padding:0}}
.tb .howcards{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:16px;justify-content:center}.tb .howcards li{flex:1 1 260px;max-width:380px;background:var(--bg);color:var(--navy);border:1px solid var(--line);border-radius:28px;padding:24px 22px 28px;border-bottom:14px solid var(--pc);text-align:left}
.tb .howcards li p{margin:0;color:var(--navy)}.tb .howcards h3{margin:0 0 16px;font-size:1.5rem}.tb .howcards h3 span{text-align:center;display:block;width:100%;box-sizing:border-box;border-radius:99px;padding:.4em 1em;font-weight:900}
.tb .hw-teal{--pc:var(--teal);--bg:var(--teal-25)}.tb .hw-teal h3 span{background:#00857c;color:#fff}.tb .hw-yellow{--pc:var(--yellow);--bg:var(--yellow-40)}.tb .hw-yellow h3 span{background:var(--yellow);color:var(--navy)}.tb .hw-orange{--pc:var(--orange);--bg:var(--orange-25)}.tb .hw-orange h3 span{background:var(--orange);color:#fff}
.pillcards .pnum{font-weight:900;font-size:1.05rem;letter-spacing:.04em}

.tb .aboutgrid{display:grid;grid-template-columns:1.2fr 1fr;gap:16px;align-items:stretch}.tb .aboutgrid>*{min-width:0}
.tb .abt{background:#fff;border:1px solid var(--line)}.tb .abt h2{margin:0 0 .5em}.tb .abt p{margin:0 0 1em}
.tb .vpcol{display:grid;gap:16px}.tb .vpc{background:#fff;border:1px solid var(--line)}.tb .vpc h2{margin:0 0 .6em;font-size:1.6rem}.tb .vpc p{margin:0}
.hlx{padding:0 .12em;display:inline-block;line-height:1.15}.hlx-t{background:linear-gradient(transparent 70%,var(--teal) 70%,var(--teal) 90%,transparent 90%)}.hlx-o{background:linear-gradient(transparent 70%,var(--orange) 70%,var(--orange) 90%,transparent 90%)}.hlx-y{background:linear-gradient(transparent 70%,var(--yellow) 70%,var(--yellow) 90%,transparent 90%)}
.tb .bar{height:8px;border-radius:99px;margin:20px 0 0;max-width:200px}.tb .bar-t{background:var(--teal)}.tb .bar-o{background:var(--orange)}.tb .bar-y{background:var(--yellow)}
@media(max-width:860px){.tb .aboutgrid{grid-template-columns:1fr}}
.tb .steer{list-style:none;margin:28px 0 0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.tb .steer a{display:flex;flex-direction:column;align-items:center;gap:16px;text-decoration:none;color:var(--navy);height:100%;background:#fff;border:1px solid var(--line);border-radius:16px;padding:22px 16px 18px;box-sizing:border-box}
.tb .slogo{display:grid;place-items:center;width:100%;height:56px;box-sizing:border-box}.tb .slogo.dark{background:var(--navy);border-radius:12px;width:auto;padding:0 14px;margin:0 auto}.tb .slogo img{width:auto;height:auto;max-width:100%;height:56px;object-fit:contain}.tb .slogo.dark img{height:40px}
.tb .sinit{width:56px;height:56px;border-radius:50%;background:var(--teal-25);display:grid;place-items:center;font-weight:900;font-size:1.1rem;color:var(--navy)}
.tb .sname{font-weight:800;text-align:center}.tb .steer a:hover .sname,.tb .steer a:focus-visible .sname{text-decoration:underline}.tb .steer a:hover{border-color:var(--teal)}
@media(max-width:860px){.tb .steer{grid-template-columns:repeat(2,1fr)}}@media(max-width:480px){.tb .steer{grid-template-columns:1fr}}
.tb .focus{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:16px;justify-content:center}.tb .focus li{flex:1 1 300px;max-width:360px;background:var(--fb);border-radius:170px 170px 22px 22px;padding:44px 26px 30px;text-align:left}
.tb .focus .fn{display:grid;place-items:center;width:56px;height:56px;border-radius:50%;background:var(--fc);color:var(--ft);font-weight:900;font-size:1.1rem;margin:0 auto 12px}.tb .focus h3{text-align:center;margin:0 0 .6em}.tb .focus p{margin:0;font-size:.97rem}
.tb .focus li:nth-child(1){--fb:var(--teal-25);--fc:#00857c;--ft:#fff}.tb .focus li:nth-child(2){--fb:var(--yellow-40);--fc:var(--yellow);--ft:var(--navy)}.tb .focus li:nth-child(3){--fb:var(--orange-25);--fc:var(--orange);--ft:#fff}.tb .focus li:nth-child(4){--fb:var(--blue-15);--fc:var(--navy);--ft:#fff}.tb .focus li:nth-child(5){--fb:var(--grey-6);--fc:#9fb0b8;--ft:var(--navy)}
.tb .team2 li{width:210px;align-content:start;align-self:flex-start}.tb .team2 b{margin-top:6px}.tb .team2 .tc{width:168px;max-width:100%;height:auto;aspect-ratio:1/1;font-weight:900;font-size:2.3rem;color:var(--navy)}
@media(min-width:861px){.tb .splith.ab{align-items:stretch}.tb .splith.ab>div:not(.ph){align-self:center}.tb .splith.ab .ph{display:flex}.tb .splith.ab .ph img{aspect-ratio:auto;height:auto;min-height:100%;flex:1;object-fit:cover}}
.tb .steergrid{display:grid;grid-template-columns:2fr 3fr;gap:48px;align-items:start}.tb .steergrid>*{min-width:0}.tb .steertxt .sechead{margin-top:0}.tb .steerlist>.lede{margin-top:0}
.tb .steergrid .steer{margin-top:16px;gap:16px}.tb .steergrid .steer a{aspect-ratio:1/1;height:auto;justify-content:center;padding:12px 10px;gap:8px;border-radius:16px}.tb .steergrid .slogo{display:flex;align-items:center;justify-content:center;overflow:hidden;width:100%;height:50px;padding:0}.tb .steergrid .slogo img{flex:0 1 auto;width:auto;height:auto;max-width:100px;max-height:50px;object-fit:contain}.tb .steergrid .sname{font-size:.9rem;font-weight:400;color:var(--muted);line-height:1.3}
.tb .steergrid .steer{grid-template-columns:repeat(3,minmax(0,160px));justify-content:center}@media(max-width:860px){.tb .steergrid{grid-template-columns:1fr;gap:0}.tb .steergrid .steer{margin-top:20px}}@media(max-width:560px){.tb .steergrid .steer{gap:8px}.tb .steergrid .steer a{padding:4px 3px;gap:4px;border-radius:12px;min-height:0}.tb .steergrid .slogo{height:32px;flex:none}.tb .steergrid .slogo img{max-width:100%;max-height:32px}.tb .steergrid .sname{font-size:.6rem;line-height:1.15}}.tb .steerlist>.lede{text-align:center}
.tb .cen{text-align:center}.tb h2.teamhead{margin-bottom:56px}.tb .team2 li.brk{display:block;flex-basis:100%;width:100%;height:0;margin:-24px 0 0;padding:0}@media(min-width:861px){.tb .team2 li.brk{display:none}.tb .team2 li{flex:1 1 0;width:auto;max-width:220px;min-width:0;grid-template-columns:minmax(0,1fr)}.tb .team2 .tc{width:100%;max-width:190px}}.tb .team2 b{font-size:1.2rem;font-weight:800;line-height:1.12}@media(max-width:1060px){.tb .team2 b{min-height:2.24em}}@media(max-width:739px){.tb .team2 li{width:min(150px,calc(50% - 12px))}.tb .team2 .tc{width:100%;max-width:150px}}
.tb .focuscards li{flex:1 1 300px;max-width:360px;padding:24px 22px}
.tb .focuscards .pi{width:76px;height:76px;margin:0 auto 10px}.tb .focuscards .pnum{font-size:1.6rem;font-style:italic;font-weight:400;letter-spacing:.02em}.tb .focuscards li:nth-child(1) .pi{color:#00857c}.tb .focuscards li:nth-child(2) .pi{color:#D9A400}.tb .focuscards li:nth-child(3) .pi{color:#d9481a}.tb .focuscards li:nth-child(4) .pi{color:var(--navy)}.tb .focuscards li:nth-child(5) .pi{color:#6b7f88}.tb .focuscards p{text-align:left;font-size:.97rem}
/* Steering tiles: top 65% is the logo, bottom 35% is the name */
.tb .steergrid .steer a{display:grid;grid-template-rows:minmax(0,65fr) minmax(0,35fr);gap:0;padding:4px 10px 2px;justify-content:stretch;align-content:stretch}.tb .steergrid .slogo{align-self:center;height:auto;min-height:0;max-height:100%}.tb .steergrid .sname{align-self:start;padding-top:0;line-height:1.2}
@media(max-width:560px){.tb .steergrid .steer a{padding:3px;grid-template-rows:minmax(0,1fr) minmax(0,1fr)}.tb .steergrid .slogo{height:auto;max-height:100%;flex:none}.tb .steergrid .sname{padding-top:2px}}
@media(min-width:861px) and (max-width:1000px){.tb .steergrid{grid-template-columns:1fr 2fr}}
/* Our Stories: yellow play button; yellow bars sit exactly midway (100px each side) above Our Stories and between the last row and Our Network */
.tb .tcards .tph .play{background:var(--yellow);color:var(--navy);border:0;box-shadow:0 6px 20px rgba(0,0,0,.25)}.tb .tcards .tph .play:hover{background:#fff;color:var(--navy)}.tb .tcards .tph .play:active{background:#ffe38a;color:var(--navy)}.tb #network>.wrap:first-child{margin-bottom:100px}.tb .sec.stories{padding-bottom:96px!important}.tb .sbar-top{margin:0 auto 100px}.tb .sbar-bot{margin:100px auto 0}.tb #network #our-network{padding-top:96px!important}.tb #network #our-network,.tb [id^="lga-"]>.sec{background:#fff}.tb #our-network .gsub li,.tb [id^="lga-"] .gsub li,.tb #our-network .lgasel,.tb [id^="lga-"] .lgasel{background-color:var(--bg)}
/* Brand logo always keeps its true ratio (the footer logo was squashed at iPad width) */
.tb .logo{width:auto;max-width:100%}.tb .site-foot .foot-logo .logo{height:auto!important;width:200px;max-width:100%}
/* Funder strip above the header: label at the "Who we are" label size (not bold, not capitals), thin white pills like Prototype A's Projects pill */
.tb .funders{background:var(--bg);border-bottom:1px solid var(--line)}.tb .funders .wrap{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:8px 16px;padding:10px 20px}
.tb .funders p{margin:0;font-size:.8rem;font-weight:400;color:var(--navy)}.tb .funders ul{list-style:none;margin:0;padding:0;display:contents}
.tb .funders li a{text-decoration:none;transition:background .15s,border-color .15s;display:inline-flex;align-items:center;gap:8px;background:#fff;border:1px solid var(--line);border-radius:99px;box-sizing:border-box;height:32px;padding:0 1.05em 0 1em;font-weight:400;font-size:.8rem;color:var(--navy);line-height:1}.tb .funders li a:not(:has(img)){padding-left:.95em}.tb .funders img{height:19.8px;width:auto;display:block;flex:none}.tb .funders li a:hover,.tb .funders li a:focus-visible{background:#e8edf0;border-color:#c3ccd1}.tb .funders li a:focus-visible{outline:2px solid var(--teal-d);outline-offset:2px}
@media(max-width:1100px){.tb .funders .wrap{padding:6px 10px;gap:5px 6px}.tb .funders li a{gap:5px;height:28px;padding:0 .7em 0 .8em}.tb .funders li a:not(:has(img)){padding-left:.6em}.tb .funders img{height:14.4px}}
/* Our Focus: full-width cards, photo 40% on the left with the grey number circle centred on it, content on the right */
.tb ol.focuscards{display:flex;flex-direction:column;flex-wrap:nowrap;gap:16px;justify-content:flex-start}
.tb ol.focuscards li{flex:none;max-width:none;width:100%;display:grid;grid-template-columns:40% minmax(0,1fr);padding:0;overflow:hidden;text-align:left}
.tb .focuscards .fph{position:relative;min-height:280px}.tb .focuscards .fph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block;border-radius:0}
.tb .focuscards .fph .pi{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);margin:0;width:88px;height:88px;box-shadow:0 4px 18px rgba(7,41,59,.25)}
.tb .focuscards .fbody{align-self:center;padding:32px 40px}.tb .focuscards .fbody h3{margin:0 0 .5em}.tb .focuscards .fbody p{margin:0;max-width:62ch;font-size:1.05rem;line-height:1.6}
@media(max-width:739px){.tb ol.focuscards li{grid-template-columns:1fr}.tb .focuscards .fph{min-height:0;height:220px}.tb .focuscards .fbody{padding:24px 22px 28px}}
/* About: How we work cards go full width below iPad; Our Focus titles match the Connect/Share/Care titles; number circle 50% see-through and 30% bigger; Our Journey is a white band like Our Network */
.tb .howcards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;justify-content:stretch}.tb .howcards li{max-width:none;min-width:0}
@media(max-width:860px){.tb .howcards{grid-template-columns:1fr}}
.tb .focuscards .fbody h3{font-size:1.6rem}
.tb .focuscards .fph .pi{width:114px;height:114px;background:rgba(238,241,243,.5);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);box-shadow:none}.tb .focuscards .fph .pnum{font-size:clamp(1.6rem,3.2vw,2.4rem);font-weight:800;font-style:italic}
.tb #about>.sec.journey{background:#fff;padding-top:96px!important;padding-bottom:96px!important}.tb #about>.sec.journey+.sec{padding-top:96px!important}
/* Our Journey: timeline items stay transparent so the line shows behind and between the year pills */
.tb ol.river>li{background:transparent;border:0;border-radius:0;box-shadow:none}
/* About: teal bars sit 100px above and below the Resilience Alliance Team section, like the yellow bars around Our Stories */
.tb #about>.sec.steersec,.tb #about>.sec.teamsec{padding-bottom:96px!important}
/* Our Focus numbers: white on the card theme colour at 60% transparent */
.tb .focuscards li .fph .pi{color:#fff;text-shadow:0 1px 8px rgba(7,41,59,.55)}
.tb .focuscards li:nth-child(1) .fph .pi{background:rgba(0,133,124,.4);color:#fff}.tb .focuscards li:nth-child(2) .fph .pi{background:rgba(217,164,0,.4);color:#fff}.tb .focuscards li:nth-child(3) .fph .pi{background:rgba(217,72,26,.4);color:#fff}.tb .focuscards li:nth-child(4) .fph .pi{background:rgba(7,41,59,.4);color:#fff}.tb .focuscards li:nth-child(5) .fph .pi{background:rgba(107,127,136,.4);color:#fff}
/* Funder pills: Federal and State get extra left padding; phone sizes scale smoothly with screen width so the strip stays within two rows */
.tb .funders li:nth-child(-n+2) a{padding-left:1.35em}
@media(max-width:1100px){.tb .funders li:nth-child(-n+2) a{padding-left:1.1em}}
@media(max-width:560px){.tb .funders .wrap{padding:5px 4px;gap:4px 3px}.tb .funders ul{gap:0}.tb .funders p{font-size:clamp(.5rem,2.45vw,.72rem);margin-right:2px}.tb .funders li a{font-size:clamp(.5rem,2.45vw,.72rem);height:2.5em;gap:.3em;padding:0 .4em 0 .5em}.tb .funders li:nth-child(-n+2) a{padding-left:.75em}.tb .funders img{height:1.35em}}
/* Every page starts 36px below the funders strip (Home hero, About, Network, R.A.C.K., Impact, and the heading on each LGA page) */
.tb .page[id^="lga-"]>.sec:first-child{padding-top:32px!important}
/* About sections are reachable from the About menu dropdown; leave room under the sticky header when scrolling to them */
#ab-vision,#ab-how,#ab-focus,#ab-journey,#ab-steering,#ab-team,#nw-map,#nw-stories,#our-network{scroll-margin-top:90px}
/* Main menu: About has a dropdown of its page sections. Hover on desktop, arrow button on touch and the phone menu. */
.tb .navdrop{position:relative;display:flex;align-items:center}
.tb .navdrop .dd-btn{display:grid;place-items:center;background:transparent;border:0;color:var(--navy);cursor:pointer;min-height:36px;min-width:26px;padding:0 .4em 0 0;margin-left:-6px;border-radius:99px}
.tb .navdrop .dd-btn svg{transition:transform .15s}.tb .navdrop.open .dd-btn svg{transform:rotate(180deg)}
.tb .navdrop .dd-btn:focus-visible{outline:2px solid var(--teal-d);outline-offset:2px}
.tb .ddmenu{list-style:none;margin:0;padding:8px;position:absolute;top:100%;left:0;min-width:230px;background:#fff;border:1px solid var(--line);border-radius:16px;box-shadow:0 12px 32px rgba(7,41,59,.14);display:none;z-index:60}
.tb .ddmenu::before{content:"";position:absolute;left:0;right:0;top:-8px;height:8px}
.tb .navdrop.open .ddmenu{display:block}
@media(hover:hover) and (min-width:740px){.tb .navdrop:hover .ddmenu{display:block}.tb .navdrop:hover .dd-btn svg{transform:rotate(180deg)}}
.tb #nav .ddmenu a{display:block;padding:.6em .9em;font-weight:700;border-radius:10px;white-space:nowrap;text-decoration:none;font-size:1rem}
.tb #nav .ddmenu a:hover,.tb #nav .ddmenu a:focus-visible{background:var(--teal-12);text-decoration:none}
@media(max-width:739px){.tb .navdrop{flex-wrap:wrap}.tb .navdrop>a{flex:1}.tb .navdrop .dd-btn{min-width:44px;min-height:44px;margin-left:0;padding:0}.tb .ddmenu{position:static;width:100%;min-width:0;border:0;box-shadow:none;padding:0 0 4px 14px;border-radius:0}.tb .ddmenu::before{display:none}.tb #nav .ddmenu a{white-space:normal}}
@media(min-width:740px) and (max-width:860px){.tb .navdrop .dd-btn{min-width:22px;padding:0 .2em 0 0;margin-left:-4px}}
@media(min-width:861px) and (max-width:960px){.tb #nav a:not(.btn){padding:.5em .6em;font-size:.95rem}.tb #nav .btn{padding:.55em 1em;margin-left:4px;font-size:.95rem}.tb .navdrop .dd-btn{min-width:22px;padding:0 .2em 0 0;margin-left:-4px}.tb #nav{gap:2px}}
/* About header columns match the cards below: photo as wide as Vision, text as wide as The Resilience Alliance (cards are 1 : 1.2 with a 20px gap) */
@media(min-width:861px){.tb .splith.ab{grid-template-columns:1fr 1.2fr;column-gap:20px}.tb .splith.ab>div:not(.ph){padding-left:20px}}
/* so the photo ends exactly where the heading text ends */
.tb .splith.ab h1{margin-bottom:0}
/* Heading scale that stays proportionate on phone, iPad and desktop: page title > section header > card title.
   Section headers also size the Our Focus numbers, which match the Our Focus heading. */
.tb .page h1{font-size:clamp(2.375rem,5vw,3.5rem)}
.tb .page .dirhead h1.sechead{font-size:clamp(2.1rem,4.4vw,2.6rem)}
.tb .page h2.sechead,.tb .page .statcard h2{font-size:clamp(1.875rem,4vw,2.375rem)}.tb .page .wwa h2{font-size:clamp(1.7rem,4vw,2.4rem)}
.tb .page .card.abt h2,.tb .page .vpc h2,.tb .page .howcards h3,.tb .page .focuscards .fbody h3{font-size:clamp(1.375rem,2.4vw,1.5rem)}
.tb .focuscards .fph .pnum{font-size:clamp(1.875rem,4vw,2.375rem)}
/* Home: Connect / Share / Care in their own row between the hero and Our Impact: no pill, text in the three theme colours (deeper yellow and orange so they read on the light page),
   same size as the About titles. Each opens How we work. Hover adds only a 1px white border. */
.tb .hwpills{list-style:none;margin:0 auto;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:8px;width:fit-content;max-width:100%}
.tb .hwpills a{display:block;box-sizing:border-box;border:1px solid transparent;border-radius:var(--btn-r,12px);padding:.4em .8em;text-align:center;font-weight:900;font-size:clamp(1.375rem,2.4vw,1.5rem);line-height:1.2;text-decoration:none!important;background:transparent}
.tb .hwpills a.hp-teal,.tb .hwpills a.hp-teal:hover,.tb .hwpills a.hp-teal:active{color:#00857c;background:transparent}
.tb .hwpills a.hp-yellow,.tb .hwpills a.hp-yellow:hover,.tb .hwpills a.hp-yellow:active{color:#D9A400;background:transparent}
.tb .hwpills a.hp-orange,.tb .hwpills a.hp-orange:hover,.tb .hwpills a.hp-orange:active{color:#d9481a;background:transparent}
.tb .hwpills a:hover,.tb .hwpills a:active{border-color:#fff}
.tb .hwpills a:focus-visible{outline:2px solid var(--teal-d);outline-offset:3px}
/* Type and gap refinements: 16px body, 700 weight for lead and small titles, 16px gaps for cards, tiles and buttons */
body.teal{font-size:16px}
.tb .lede,.tb .pillcards h3{font-size:1.25rem}.tb .lede{font-weight:400}.tb .pillcards h3{font-weight:800}
.tb b,.tb strong{font-weight:800}
.tb .eyebrow,.tb .hsplit .hsolid-text .eyebrow,.tb .hsolid-text .eyebrow,.tb .hsplit-tag{font-size:.6875rem!important}
.tb .btnrow,.tb .hwpills,.tb .stats{gap:16px}
/* About, How we work: white pills, text colours as the Connect. Share. Care. links on Home */
.tb .howcards h3 span{background:#fff!important;border:1px solid var(--line)}
.tb .howcards .hw-teal h3 span{color:#00857c!important}.tb .howcards .hw-yellow h3 span{color:#D9A400!important}.tb .howcards .hw-orange h3 span{color:#d9481a!important}
@media(max-width:560px){.tb .hwpills{gap:4px}.tb .hwpills a{padding:.4em .65em}}
@media(max-width:430px){.tb .hwpills a{font-size:1.25rem;padding:.4em .5em}}@media(max-width:380px){.tb .hwpills a{font-size:1.15rem;padding:.4em .45em}}@media(max-width:345px){.tb .hwpills a{font-size:1.05rem;padding:.4em .4em}}
/* Home: small, light versions of the decorative circles from the "50+ groups" section, as the background of the Connect / Share / Care row */
.tb .hwrow{position:relative;overflow-x:clip}.tb .hwbg{position:relative}.tb .hwbg .hwpills{position:relative;z-index:1}
.tb .hwd{position:absolute;pointer-events:none;z-index:0}
.tb .hwd-blob{width:70px;aspect-ratio:1/1;background:var(--yellow);opacity:.4;border-radius:62% 38% 55% 45%/48% 60% 40% 52%;left:calc(50% - 330px);top:-14px}
.tb .hwbg .hwd-rings{position:absolute;z-index:0;width:96px;height:96px;opacity:.5;right:calc(50% - 345px);left:auto;top:-22px}
.tb .hwd-dot{border-radius:50%}.tb .hwd-dt{width:30px;height:30px;background:var(--teal);opacity:.3;left:calc(50% - 292px);top:44px}.tb .hwd-do{width:20px;height:20px;background:var(--orange);opacity:.35;right:calc(50% - 290px);top:46px}
@media(max-width:560px){.tb .hwd-blob{width:54px;left:-16px;top:-16px}.tb .hwbg .hwd-rings{width:70px;height:70px;right:-24px;top:-10px}.tb .hwd-dt{left:calc(50% - 176px);top:34px}.tb .hwd-do{right:calc(50% - 178px);top:36px}}
/* Footer: no bullets, social icons as round buttons */
.tb .site-foot .flist li{padding-left:0}.tb .site-foot .flist li::before{display:none}
.tb .site-foot .flist.social{display:flex;gap:16px;flex-wrap:wrap;margin-top:16px}.tb .site-foot .flist.social li{margin:0}
.tb .site-foot .flist a.soc{display:grid;place-items:center;width:44px;height:44px;padding:0;margin:0;border-radius:var(--btn-r,12px);background:#fff;color:#07293b;text-decoration:none!important;transition:background .15s}
.tb .site-foot .flist a.soc:hover,.tb .site-foot .flist a.soc:focus-visible{background:#beddda;color:#07293b}
.tb .site-foot .flist a.soc:focus-visible{outline:2px solid #fff;outline-offset:3px}
/* Privacy Policy page; small review link on the R.A.C.K. page */
.tb .rackrev{align-self:center;margin:0 0 0 6px;font-size:.95rem}.tb .rackrev{color:var(--teal-d);font-weight:700;text-decoration:underline;text-underline-offset:3px}.tb .rackrev:hover{text-decoration-thickness:2px}
.tb .pphead{padding-bottom:28px}.tb .pphead .lede{margin:14px 0 0;max-width:62ch}.tb .ppdate{margin:10px 0 22px;color:var(--muted);font-size:.95rem}
.tb .pplist2{list-style:none;margin:0;padding:8px 32px;background:#fff;border-radius:28px;border-bottom:10px solid var(--teal)}
.tb .ppitem{display:grid;grid-template-columns:52px minmax(0,1fr);gap:16px;padding:22px 0;border-top:1px solid var(--line)}.tb .ppitem:first-child{border-top:0}
.tb .ppnum{font-size:clamp(1.375rem,2.4vw,1.5rem);font-weight:800;font-style:italic;color:var(--teal-d);line-height:1.3}
.tb .pprow{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px;margin-bottom:.4em}.tb .ppitem h2{font-size:clamp(1.375rem,2.4vw,1.5rem);margin:0}
.tb .ppitem p{margin:0;max-width:70ch}.tb .ppitem p+p{margin-top:.5em}.tb .ppnote{font-size:.92rem;color:var(--muted)}
.tb .pptag{display:inline-flex;align-items:center;gap:6px;border-radius:99px;padding:.2em .8em .2em .65em;font-size:.82rem;font-weight:800;line-height:1.3;white-space:nowrap;vertical-align:middle}
.tb .tag-have{background:#00857c;color:#fff}.tb .tag-add{background:var(--yellow);color:var(--navy)}
.tb .pplegend{max-width:72ch;margin:18px 0 0;line-height:2}
@media(max-width:739px){.tb .pplist2{padding:4px 18px}.tb .ppitem{grid-template-columns:40px minmax(0,1fr);gap:8px}}
/* Footer layout: logo, Contact and Stay in Touch stacked on the left; Quick Links in the middle; R.A.C.K. links and Privacy Policy on the right; copyright line centred */
.tb .site-foot .fquick{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:48px;min-width:0}.tb .site-foot .fhide{visibility:hidden}
.tb .site-foot .copy{text-align:center}
/* Prototypes A and C header: two separate cards. Left: dark green text card. Right: the video card (full height in A; always almost square and centred in C).
   Desktop (1000px and up): text 60%, video 40%. iPad: half and half.  Phone: stacked. Text card padding: desktop 60px top and bottom; iPad and phone 10% more than the original 28px / 36px. */
.tb .hsplit{--pw:min(580px,calc(100vw - 200px));padding:32px 0 0;margin-bottom:60px}
.tb .hsplit-in{width:calc(100% - 40px);max-width:calc(var(--wrap) - 40px);margin:0 auto;display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:24px;min-height:640px}
.tb .hsplit-l{border-radius:28px;border-top:8px solid var(--teal);border-bottom:8px solid var(--teal)}
.tb .hsplit-r{position:relative;border-radius:28px;overflow:hidden;border-top:8px solid var(--teal);border-bottom:8px solid var(--teal);min-width:0;background:#fff}
.tb .hsplit-r img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;border-radius:0;display:block}
.tb .hsplit-r,.tb .tph.vid,.tb .h1-photo{cursor:pointer}.tb .hsplit-r .play{position:absolute;inset:0;margin:auto;width:92px;height:92px;padding:0;display:grid;place-items:center}.tb .hsplit-r .play svg{display:block;width:100%;height:100%;font-family:var(--font)}
.tb .hsolid-text{background:rgb(0 97 90);color:#fff;padding:60px 44px;display:flex;flex-direction:column;justify-content:center;min-width:0}
.tb .hsolid-text .eyebrow{display:inline-block;align-self:flex-start;background:#fff;color:var(--navy);padding:.55em 1.5em;border-radius:99px;margin-bottom:48px}
.tb .hsolid-text h1{color:#fff;line-height:1.12}.tb .hsolid-text .lede{color:#fff}
.tb .hsolid-text .btn-primary{border-color:#fff}.tb .hsolid-text .btn-primary:hover{background:#fff;color:#07293b;border-color:#fff}.tb .hsolid-text .btn-primary:active{background:#beddda;color:#07293b;border-color:#fff}
@media(min-width:741px) and (max-width:999px){.tb .hsplit-in{grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:20px;min-height:0}.tb .hsplit .hsolid-text{padding:31px 28px 40px}.tb .hsplit .hsolid-text .eyebrow{font-size:.72rem;margin-bottom:28px;padding:.55em 1.2em}.tb .hsplit .hsolid-text h1{font-size:2.1rem}}
@media(max-width:740px){.tb .hsplit-in{grid-template-columns:minmax(0,1fr);min-height:0;gap:16px;width:calc(100% - 24px)}.tb .hsplit .hsolid-text{padding:31px 18px 40px}.tb .hsplit .hsolid-text .eyebrow{font-size:.72rem;margin-bottom:24px}.tb .hsplit-l{border-radius:28px}.tb .hsplit-r{border-radius:28px;aspect-ratio:4/3}}
.tb .hsplit.hsplit-sq .hsplit-r{align-self:center;aspect-ratio:11/10}
/* Prototype B: one green card behind everything. The tag sits above both the title and the video; below it the text takes exactly half and the video exactly the other half */
.tb .hsplit-bg .hsplit-in{background:rgb(0 97 90);border-radius:28px;border-top:8px solid var(--teal);border-bottom:8px solid var(--teal);overflow:hidden;gap:0;align-items:stretch;grid-template-columns:minmax(0,1fr) minmax(0,1fr);grid-template-rows:auto 1fr}
.tb .hsplit-bg .hsplit-tag{grid-column:1/-1;justify-self:start;display:inline-block;background:#fff;color:var(--navy);padding:.55em 1.5em;border-radius:99px;margin:60px 44px 0}
.tb .hsplit-bg .hsplit-l{background:transparent;border:0;border-radius:0;padding:32px 44px 60px}
.tb .hsplit-bg .hsplit-r{border:0;border-radius:28px 0 0 28px;background:transparent;margin:0;align-self:center}
@media(min-width:741px) and (max-width:999px){.tb .hsplit-bg .hsplit-tag{margin:31px 28px 0;font-size:.72rem;padding:.55em 1.2em}.tb .hsplit-bg .hsplit-l{padding:24px 28px 40px}}
@media(max-width:740px){.tb .hsplit-bg .hsplit-in{grid-template-columns:minmax(0,1fr);grid-template-rows:auto;border-radius:28px}.tb .hsplit-bg .hsplit-tag{margin:31px 18px 0;font-size:.72rem}.tb .hsplit-bg .hsplit-l{padding:24px 18px 40px}.tb .hsplit-bg .hsplit-r{margin:0 18px 30px;border-radius:20px;align-self:stretch}}
/* accent bars sit on the bottom edge, not the top */
.arc{border-top:0;border-bottom:6px solid var(--teal)}.arc.y{border-bottom-color:var(--yellow)}.arc.o{border-bottom-color:var(--orange)}
.cards .pcard{border-top:0}.cards .pcard:nth-child(1){border-bottom:6px solid var(--teal)}.cards .pcard:nth-child(2){border-bottom:6px solid var(--yellow)}.cards .pcard:nth-child(3){border-bottom:6px solid var(--orange)}
.v1 .pc{padding:26px 16px 0}.v1 .pc::before{display:none}.v1 .pc>*:nth-last-child(2){margin-bottom:22px}
.v1 .pc::after{content:"";display:block;align-self:stretch;height:18px;margin:auto -16px 0;border-radius:0 0 6px 6px;background:var(--teal)}
.v1 .pc:nth-child(2)::after{background:var(--yellow)}.v1 .pc:nth-child(3)::after{background:var(--orange)}.v1 .pc:nth-child(4)::after{background:var(--navy)}.v1 .pc:nth-child(5)::after{background:#9fb0b8}
.pillcards li{border-top:0;border-bottom:14px solid var(--pc);padding:22px 18px}
.pg-head{padding:32px 0 40px}.pg-head h1{margin:0}
/* brand colour dos and don'ts (see brand-contrast): pins keep a 3px white gap from teal lines, solid colours only behind short lines */
.teal .pmap .dot circle{stroke-width:3}
"""

CSS_B = """
/* hero: the photo is the header background, the panel sits on top (no video) */
.menu-btn{border-radius:var(--btn-r,12px)}
.herobg{--pw:min(580px,calc(100vw - 200px))}
@media(min-width:740px) and (max-width:860px){.menu-btn{display:none}#nav,#nav.open{display:flex;position:static;flex-direction:row;align-items:center;padding:0;border:0;background:transparent}.logo{height:48px}}
.herobg{padding:0!important}
.herobg>.wrap:first-child{display:flex;align-items:center;max-width:none;padding:0;position:relative;min-height:640px}
.herobg .h1-photo{position:absolute;inset:0;border-radius:0;min-height:0}
.herobg .h1-panel{position:relative;z-index:2;max-width:var(--pw,580px);margin:56px 0 56px max(20px,calc((100vw - var(--wrap))/2 + 20px))}
.herobg .h1-photo .play{inset:auto;margin:0;z-index:3;top:50%;left:calc((max(20px,(100vw - var(--wrap))/2 + 20px) + var(--pw,580px) + 100%)/2);transform:translate(-50%,-50%)}

/* B: teal as accents and tints only, navy kept for the footer */
/* button family: teal. Primary: teal with white text and a navy outline (Sign In is primary). Secondary: white with a teal outline. Tertiary: navy. Selected menu item: the lighter teal. */
:root{--btn-teal:#00857c;--teal-12:#f3f9f8;--teal-25:#beddda}
.btn-primary,.btn-cta{background:var(--btn-teal);color:#fff;border-color:var(--navy)}
.btn-primary:hover,.btn-cta:hover{background:var(--navy);color:#fff;border-color:var(--navy)}
.btn-ghost{background:#fff;color:var(--navy);border-color:var(--btn-teal)}.btn-ghost:hover{background:var(--navy);color:#fff;border-color:var(--navy)}
.ready .btn-primary,.ready .btn-cta{border-color:#fff}.ready .btn-ghost{background:transparent;color:#fff;border-color:#fff}
body{--current:var(--teal-25);--hover:var(--teal-12)}
/* menu and links work the same way: hover underlines on the paler PDF tint (links also turn navy), active keeps the tint; the menu stays navy */
a:not(.btn):hover{text-decoration-thickness:3px;text-underline-offset:4px}
main a:not(.btn):hover{color:var(--navy);background:var(--teal-12)}
#nav a:not(.btn):hover{background:var(--teal-12);color:var(--navy);text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:6px}
#nav a:not(.btn):active,main a:not(.btn):active{background:var(--teal-25);color:var(--navy)}
.btn-primary:active,.btn-cta:active,.btn-ghost:active{background:var(--teal-25);color:var(--navy);border-color:var(--navy)}
.ready .btn-primary:active,.ready .btn-cta:active,.ready .btn-ghost:active{border-color:#fff}.ready .btn-ghost:hover{background:#fff;color:var(--navy)}
/* Prototype B header, in the style of Prototype 3: deep teal gradient (left to right) over the photo, white text in a block the size of Prototype A's, yellow squiggle */
.tb .herobg .h1-photo::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgb(0 97 90/.93) 0%,rgb(0 97 90/.88) 52%,rgb(0 97 90/.1) 100%)}
.tb .herobg .h1-panel{background:transparent;border:0;color:#fff}
.tb .herobg .h1-panel h1{color:#fff}.tb .herobg .h1-panel .eyebrow,.tb .herobg .h1-panel .lede{color:#fff}
.tb .herobg .h1-panel .btn-primary{border-color:#fff}
.tb .herobg .h1-panel .eyebrow{display:inline-block;align-self:flex-start;background:#fff;color:var(--navy);padding:.55em 1.5em;border-radius:99px;margin-bottom:48px}
.mark{position:relative;display:inline-block}.mark .squig{position:absolute;left:0;right:0;bottom:-.02em;width:100%;height:.4em}
@media(min-width:740px){.herobg .h1-panel{padding:46.8px 44px}}
@media(max-width:739px){.tb .herobg>.wrap:first-child{display:flex;align-items:flex-start;min-height:0;padding:0}.tb .herobg .h1-panel{margin:0;padding:25.2px 20px 32px;max-width:none}.tb .herobg .h1-photo::after{background:linear-gradient(180deg,rgb(0 97 90/.94) 0%,rgb(0 97 90/.88) 30%,rgb(0 97 90/.5) 48%,rgb(0 97 90/0) 62%)}.herobg .h1-panel h1{font-size:1.75rem;line-height:1.15}.herobg .h1-panel .lede{font-size:1rem}.herobg .h1-panel .eyebrow{font-size:.72rem}}
.tb .h1-panel{background:var(--teal-25);color:var(--navy);border:4px solid var(--teal)}.tb .h1-panel h1,.tb .h1-panel .eyebrow{color:var(--navy)}.tb .h1-panel .btn-ghost{color:var(--navy);border-color:var(--navy);background:#fff}.tb .h1-panel .btn-ghost:hover{background:var(--navy);color:#fff}
.tb #nav a[aria-current=page]{background:var(--teal-25)}
/* Menu items with a dropdown: hover and the current page highlight the label and the arrow together */
.tb #nav .navdrop{border-radius:var(--btn-r,12px)}
.tb #nav .navdrop>a,.tb #nav .navdrop>a:hover,.tb #nav .navdrop>a:active,.tb #nav .navdrop>a[aria-current=page]{background:transparent}
.tb #nav .navdrop:hover,.tb #nav .navdrop.open{background:var(--teal-12)}
.tb #nav .navdrop:active{background:var(--teal-25)}
.tb #nav .navdrop:has(>a[aria-current=page]){background:var(--teal-25)}
.tb #nav .navdrop:hover>a{text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:6px}
.tb .navdrop .dd-btn{border-radius:0 var(--btn-r,12px) var(--btn-r,12px) 0}
/* Pills above page titles: text sits in the middle (text-indent cancels the trailing letter-spacing) */
.tb .eyebrow.pill-t,.tb .hsolid-text .eyebrow,.tb .herobg .h1-panel .eyebrow,.tb .splith .eyebrow{text-align:center;text-indent:.12em;line-height:1.25;padding-top:calc(.55em + .75px)!important;padding-bottom:calc(.55em - .75px)!important}
.tb .surface{background:#fff;border-top:8px solid var(--teal);border-bottom:8px solid var(--teal)}.tb .statcard{background:#fff;border-top:8px solid var(--teal);border-bottom:8px solid var(--teal)}.tb .framed{--fr:var(--teal-25);outline:4px solid var(--teal);outline-offset:-4px}
.tb .kb li{background:#fff}.tb .kb a{color:var(--teal-d);font-weight:800}
.tb .partband{background:var(--teal-12);border-bottom:6px solid var(--teal)}.partband a:not(.btn):hover{background:var(--teal-25)}
.tb .ticker{background:var(--navy);color:var(--teal)}.tb .tk-in .tkd{color:var(--teal-25)}
.tb .site-foot{--foot-h:var(--teal)}
.tb .pmap{--land:#fff;--sea:var(--teal-12);--coast:var(--teal);--river:var(--teal)}
.herobg .play{display:grid;place-items:center;width:92px;height:92px;padding:0}.herobg .play svg{display:block;width:100%;height:100%;font-family:var(--font)}
/* Network section (Who we are): the yellow button set, a yellow bottom border and light yellow pills */
.tb .wwa{border-color:var(--yellow)}
.wwa .btn-primary{background:#ffcb2a;color:#07293b;border-color:#07293b}.wwa .btn-primary:hover{background:#07293b;color:#fff;border-color:#07293b}.wwa .btn-primary:active{background:#ffeaaa;color:#07293b;border-color:#07293b}
/* solid colour band across the top, like Prototype A's five pillars: teal on the header, yellow on Who we are */
/* whenever the photos stack above the text (860px and under, so phones and iPads), the circles spread out in a row across the section, about half the size */
@media(max-width:860px){.wwa-cluster{padding-top:0}.circles{aspect-ratio:2/1;margin:0 auto;transform:none}.circles img{border-width:4px}
.circles img:nth-of-type(1){width:45%;left:7%;top:0;bottom:auto}.circles img:nth-of-type(2){width:41%;left:54%;top:18%;bottom:auto;translate:none}
.circles .blob{width:16%;left:calc(-1 * min(5%, 12px));top:34%}.circles .deco-rings{width:23%;right:calc(-1 * min(6%, 14px));left:auto;top:26%}}
/* B header cropped like Prototype 3: a rounded box inside the page width, not edge to edge */
.herobg{padding:32px 0 0!important}
.herobg>.wrap:first-child{width:calc(100% - 40px);max-width:calc(var(--wrap) - 40px);margin:0 auto;padding:0;border-radius:28px;overflow:hidden;border-top:8px solid var(--teal);border-bottom:8px solid var(--teal)}
.herobg .h1-panel{margin:32px 0}
.herobg .h1-photo .play{left:calc((var(--pw,580px) + 100%)/2)}
@media(max-width:739px){.herobg>.wrap:first-child{border-radius:28px;width:calc(100% - 24px)}.herobg .h1-panel{margin:0}.tb .herobg .h1-panel{padding:25.2px 18px 32.4px}.herobg .btnrow .btn{padding:.7em 1em}}
/* Who we are: when the columns stack, the photos come first, above the title */
/* phones, B: gradient runs left to right and the play circle becomes a normal secondary button beside About */
.watchbtn{display:none}
.watchbtn{gap:.55em}.watchbtn svg{flex:none}
@media(max-width:739px){.tb .herobg .h1-photo .play{display:none}.watchbtn{display:inline-flex}.tb .herobg .watchbtn{background:#fff;color:#07293b;border-color:#fff}.tb .herobg .watchbtn:hover{background:#00857c;color:#fff;border-color:#fff}.tb .herobg .watchbtn:active{background:#beddda;color:#07293b;border-color:#fff}.tb .herobg .h1-photo::after{background:linear-gradient(90deg,rgb(0 97 90/.94) 0%,rgb(0 97 90/.9) 62%,rgb(0 97 90/.62) 100%)}}
@media(max-width:739px){.menu-btn{display:inline-flex;align-items:center;gap:.6em}.menu-btn .hb{flex:none}}
/* button rules, from the teal set. Secondary: white, teal text and outline. Tertiary: navy. On dark: primary hovers white, secondary is white. Hover fills navy (or teal for navy buttons), active takes the light tint. Corners 12px; the play button stays a circle. */
.btn-ghost{background:#fff;color:#00857c;border-color:#00857c}.btn-ghost:hover{background:#07293b;color:#fff;border-color:#07293b}.btn-ghost:active{background:#beddda;color:#07293b;border-color:#07293b}
.ready .btn-ghost{background:#fff;color:#07293b;border-color:#fff}.ready .btn-ghost:hover{background:#00857c;color:#fff;border-color:#fff}.ready .btn-ghost:active{background:#beddda;color:#07293b;border-color:#fff}
.ready .btn-primary:hover,.ready .btn-cta:hover,.tb .herobg .h1-panel .btn-primary:hover{background:#fff;color:#07293b;border-color:#fff}.tb .herobg .h1-panel .btn-primary:active{background:#beddda;color:#07293b;border-color:#fff}
.menu-btn{background:#00857c;color:#fff;border:2px solid #07293b}.menu-btn:hover{background:#07293b;color:#fff;border-color:#07293b}.menu-btn:active{background:#beddda;color:#07293b;border-color:#07293b}
.play{background:#fff;color:#00857c;border:2px solid #00857c;border-radius:50%}.play:hover{background:#07293b;color:#fff;border-color:#07293b}.play:active{background:#beddda;color:#07293b;border-color:#07293b}
/* Our Impact: orange top strip and bottom border, like the other sections */
.tb .statcard.impact{border-color:var(--orange);text-align:center}
.statcard.impact .btnrow{justify-content:center;margin:28px 0 0}
.tb .site-foot .foot-top{display:flex;align-items:flex-start}.tb .site-foot .foot-logo.boxed{display:block;width:fit-content;max-width:100%;padding:10px 14px;line-height:0}.tb .site-foot .foot-logo .logo{width:200px;max-width:100%;display:block}
/* footer, teal design: adjusted teal background, white text, white brush behind each title with adjusted teal text */
.tb .site-foot{background:#07293b;color:#fff;border-top:1px solid var(--line);--foot-line:rgba(255,255,255,.4)}
.tb .site-foot .fcol h2{color:#00857c;background-repeat:no-repeat;background-position:center;background-size:100% 100%;display:inline-block;padding:1.3em 2.6em 1.3em 2.1em;margin:0 0 14px -1.1em;line-height:1.25;position:static}
.tb .site-foot .fcol h2::after{display:none}
.tb .site-foot .fb1{background-image:url(../assets/brush/brush-white-1.svg)}.tb .site-foot .fb2{background-image:url(../assets/brush/brush-white-2.svg)}.tb .site-foot .fb3{background-image:url(../assets/brush/brush-white-3.svg)}
.tb .site-foot .flist li::before{background:#fff;opacity:.7;top:50%;transform:translateY(-50%)}
.tb .site-foot .flist a{display:inline-block;padding:.3em .8em;margin-left:-.8em;color:#fff;font-weight:400;text-decoration:none;border-radius:var(--btn-r,99px);line-height:1.4}
.tb .site-foot .flist li{margin-bottom:6px}
.tb .site-foot .flist a:hover{background:#f3f9f8;color:var(--navy);text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:6px}
.tb .site-foot .flist a:active{background:#beddda;color:var(--navy)}
.tb .site-foot .foot-cols{grid-template-columns:minmax(0,1.1fr) minmax(0,2.1fr) minmax(0,1fr);gap:48px}.tb .fstack .fcol+.fcol{margin-top:24px}.tb .site-foot .fcol h2{white-space:nowrap}
@media(min-width:701px) and (max-width:999px){.tb .site-foot .foot-cols{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}.tb .site-foot .fquick{order:1;grid-column:1/-1}.tb .site-foot .foot-top{order:2}.tb .site-foot .fstack{order:3}}
@media(max-width:700px){.tb .site-foot .foot-cols{grid-template-columns:minmax(0,1fr);gap:16px}.tb .site-foot .fquick{grid-template-columns:minmax(0,1fr);gap:0}.tb .site-foot .fcol h2.fhide{display:none}}
/* border line above the copyright line, so the Acknowledgement of Country sits between two lines */
.tb .site-foot .copyrow{margin:24px 0 0;padding-top:24px;border-top:1px solid var(--foot-line);display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:16px 20px}.tb .site-foot .copy{margin:0;padding:0;border:0;text-align:center}
.tb .site-foot .totop{display:inline-flex;align-items:center;justify-content:center;gap:8px;background:transparent;color:#fff;border:2px solid #fff;border-radius:var(--btn-r,12px);padding:.5em 1.1em;min-height:38px;font:800 .9rem var(--font);cursor:pointer;line-height:1.3}
.tb .site-foot .totop:hover{background:#f3f9f8;color:var(--navy);border-color:#fff}.tb .site-foot .totop:active{background:#beddda;color:var(--navy);border-color:#beddda}.tb .site-foot .totop:focus-visible{outline:2px solid #fff;outline-offset:3px}

/* MEAL: six circles round a ring, like the Layout Design PDF */
.mealwrap{display:grid;grid-template-columns:minmax(0,440px) 1fr;gap:48px;align-items:center;margin:28px 0 0}
.mealring{position:relative;width:100%;max-width:440px;aspect-ratio:1/1;margin:0 auto}.mealring svg{position:absolute;inset:0;width:100%;height:100%}
.mealring ol{list-style:none;margin:0;padding:0}.mealring li{position:absolute;width:30%;aspect-ratio:1/1;translate:-50% -50%;border-radius:50%;display:grid;place-items:center;text-align:center;font-weight:800;font-size:clamp(1.05rem,2.6vw,1.2rem)}
.mealq{margin:0;border-left:4px solid var(--teal);padding-left:24px}.mealq p{margin:0 0 .6em}.mealq .mq{font-weight:800;font-size:1.25rem;line-height:1.35;color:var(--navy)}
@media(max-width:860px){.mealwrap{grid-template-columns:1fr;gap:16px}}
.btn-tertiary{background:#07293b;color:#fff;border-color:#07293b}.btn-tertiary:hover{background:#00857c;color:#fff;border-color:#07293b}.btn-tertiary:active{background:#beddda;color:#07293b;border-color:#07293b}
main a.btn-tertiary:hover{background:#00857c;color:#fff}
/* page titles: Home, Network and About all use the same H1 size */
.tb .herobg .h1-panel h1{font-size:clamp(2.375rem,5vw,3.5rem);line-height:1.12}
/* Network breadcrumb: the Home pill, in yellow with navy text */
.tb .splith .eyebrow{display:inline-block;background:var(--yellow);color:var(--navy);padding:.55em 1.5em;border-radius:99px;margin-bottom:28px}

/* iPad: six menu items now, so tighten the nav to keep it on one line */
@media(min-width:740px) and (max-width:860px){.tb #nav{flex-wrap:nowrap;white-space:nowrap;gap:0}.tb #nav a:not(.btn){padding:.5em .55em;font-size:.95rem}.tb #nav .btn{padding:.55em 1em;margin-left:6px;font-size:.95rem}.tb .logo{height:40px}}
/* phone and iPad: the two photo circles sit closer together, just touching in the middle */
@media(max-width:860px){.circles img:nth-of-type(1){left:10%}.circles img:nth-of-type(2){left:51%}}
/* Home: LGA pills are navy links to the filtered Network pages */
.tb .lgapills li a{color:var(--navy);text-decoration:none;font-weight:700}.tb .lgapills li a:hover{text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:4px}
/* R.A.C.K. page */
.tb .splith .rackph img{height:auto;aspect-ratio:1024/799;object-fit:cover}
.rackhead{text-align:center}.rackhead .lede{max-width:62ch;margin-left:auto;margin-right:auto}
.tb .rackcats li:nth-child(1){--pc:var(--teal)}.tb .rackcats li:nth-child(2){--pc:var(--orange)}.tb .rackcats li:nth-child(3){--pc:var(--yellow)}.tb .rackcats li:nth-child(4){--pc:var(--navy)}.tb .rackcats li:nth-child(5){--pc:#9fb0b8}
.tb .rackcats li{border:1px solid var(--line);border-bottom:14px solid var(--pc)}
@media(min-width:861px){.tb .rackcats{flex-wrap:nowrap}.tb .rackcats li{flex:1 1 0;max-width:none;min-width:0}}
/* one rhythm: 60px between every section on every page */
.tb .sec{padding:0 0 60px!important}.tb .page>.sec:first-child{padding-top:60px!important}
.tb .hero1.herobg{margin-bottom:60px}.tb .page>.wrap:first-child>.splith{padding-bottom:0}.tb .page>.wrap:first-child{margin-bottom:60px}

/* Network only: spacing around Our Stories is set with its two yellow bars (100px each side, the lower one to the top edge of the white Our Network band), see the Our Stories rules */
/* Our Network directory (Network and every LGA page): double the space under the cards */
.tb #network>.sec:last-child,.tb [id^="lga-"]>.sec:last-child{padding-bottom:128px!important}
/* every page ends with the same 128px above the footer */
.tb .page>.sec:last-child{padding-bottom:128px!important}.tb #about>.sec:last-child{padding-bottom:128px!important}.tb #impact>.wrap:first-child{margin-bottom:128px}
/* About: same 128px rhythm as Network */
.tb #about>.wrap:first-child{margin-bottom:32px}.tb #privacy>.wrap:first-child{margin-bottom:32px}.tb #about>.sec{padding-bottom:128px!important}

/* Network page: map as tall as the text, testimonials, suburb directory */
.tb .splith.net{align-items:stretch}.tb .splith.net>div:first-child{align-self:center}.tb .splith.net .ph{display:flex}.tb .splith.net .ph .mapbox{height:auto;min-height:517px;flex:1}
.tb .splith .eyebrow.pill-t,.tb .eyebrow.pill-t{display:inline-block;background:#00857c;color:#fff;padding:.55em 1.5em;border-radius:99px;margin-bottom:28px}
.tcards{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.tcards li{background:#fff;border:1px solid var(--line);border-bottom:10px solid var(--yellow);border-radius:28px;padding:18px 18px 24px;display:flex;flex-direction:column}
.tcards .tph{position:relative;aspect-ratio:4/3;overflow:hidden;border-radius:16px;margin-bottom:16px}.tcards .tph img{width:100%;height:100%;object-fit:cover;display:block;border-radius:0}
.tcards .tph .play{inset:auto;top:50%;left:50%;margin:0;transform:translate(-50%,-50%);width:76px;height:76px;padding:0;display:grid;place-items:center}.tcards .tph .play svg{width:100%;height:100%}
.tcards blockquote{margin:0;padding:0;display:flex;flex-direction:column;gap:14px;flex:1}.tcards blockquote p{margin:0;font-size:1.2rem;line-height:1.4;font-weight:400;font-style:italic}
.tcards blockquote footer{margin-top:auto;color:#586c74;font-weight:800;font-size:.95rem}
.dirhead{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:16px 24px;margin-bottom:35px}.dirhead .sechead{margin:0;grid-column:2;grid-row:1;text-align:center}.dirhead .lgasel{grid-column:3;grid-row:1;justify-self:end}
.lgasel-l{display:flex;flex-direction:column;gap:4px;font-weight:700;font-size:.9rem}.lgasel{font:700 1rem var(--font);color:var(--navy);padding:.7em 2.4em .7em 1em;min-height:44px;border:2px solid #00857c;border-radius:12px;background:#fff;min-width:260px;cursor:pointer}
.dirhead h1.sechead{font-size:clamp(1.6rem,3.2vw,2.4rem);font-weight:800}
.gsub{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px}
.gsub li{background:#fff;border:1px solid var(--line);border-radius:28px;padding:20px;display:flex;flex-direction:column;gap:4px;align-items:flex-start}
.gsub .ctry{font-size:.85rem;font-weight:700;color:var(--teal-d);margin-top:8px}.gsub .ctry+.btn{margin-top:6px}.gsub b{font-size:1.1rem;line-height:1.25}.gsub span{color:#586c74;font-size:.95rem}.gsub .btn{margin-top:14px}
.gsub .sr-only,.rcards .sr-only,.steer .sr-only,.funders .sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.btn-sm{font-size:.9rem;padding:.5em 1.1em;min-height:38px}
@media(max-width:860px){.tcards{grid-template-columns:1fr}.tb .splith.net .ph .mapbox{height:461px;min-height:0;flex:none}}
@media(max-width:739px){.lgasel-l,.lgasel{width:100%}.dirhead{grid-template-columns:1fr}.dirhead .sechead,.dirhead .lgasel{grid-column:1}.dirhead .sechead{grid-row:1}.dirhead .lgasel{grid-row:2}}
"""


SOC_ICONS = {
    "Facebook": '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path fill="currentColor" d="M13.6 21v-8.2h2.8l.5-3.3h-3.3V7.4c0-.9.4-1.7 1.8-1.7h1.6V2.9c-.3 0-1.4-.2-2.6-.2-2.6 0-4.4 1.6-4.4 4.5v2.3H7v3.3h3v8.2h3.6z"/></svg>',
    "LinkedIn": '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path fill="currentColor" d="M6.9 9.3H3.5V20h3.4V9.3zM5.2 3.9c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zM20.5 13.7c0-3.2-1.7-4.7-4-4.7-1.8 0-2.6 1-3 1.7V9.3H10V20h3.4v-6c0-1.6.3-3.1 2.3-3.1s2 1.9 2 3.2V20h3.4v-6.3z"/></svg>',
}


def tfooter():
    def col(n, title, items):
        return f'<div class="fcol"><h2 class="fb{n}">{title}</h2><ul class="flist">' + "".join(f'<li><a href="{u}">{E(t)}</a></li>' for t, u in items) + "</ul></div>"
    contact = [("hello@nrcra.org.au", "mailto:hello@nrcra.org.au")]
    touch = [("Facebook", B.LINKS["fb"]), ("LinkedIn", B.LINKS["li"])]
    social = '<div class="fcol"><h2 class="fb1">Get in touch</h2><ul class="flist">' + "".join(f'<li><a href="{u}">{E(t)}</a></li>' for t, u in contact) + '</ul><ul class="flist social">' + "".join(f'<li><a class="soc" href="{u}" target="_blank" rel="noopener" aria-label="{n} (opens in a new tab)">{SOC_ICONS[n]}</a></li>' for n, u in touch) + "</ul></div>"
    site = [("Alliance Home", "#home"), ("Our Network", "#network"), ("About us", "#about"), ("Our Impact", "#impact")]
    rackcol = [("What is R.A.C.K?", "#rack"), ("R.A.C.K. Sign In", SIGN_IN), ("Privacy Policy", "#privacy")]
    untitled = '<div class="fcol"><h2 class="fb2 fhide" aria-hidden="true">Quick Links</h2><ul class="flist">' + "".join(f'<li><a href="{u}">{E(t)}</a></li>' for t, u in rackcol) + "</ul></div>"
    top = '<div class="foot-top"><span class="foot-logo boxed">' + blogo("logo") + '</span></div>'
    return f'''<footer class="site-foot"><div class="wrap">
<div class="foot-cols">{top}<div class="fquick">{col(2, "Quick Links", site)}{untitled}</div><div class="fstack">{social}</div></div>
<div class="ack">{B.ABORIGINAL_FLAG}<p>{B.ACK}</p></div>
<div class="copyrow"><p class="copy">© 2026 Northern Rivers Community Resilience Alliance &middot; <a href="#privacy">Privacy Policy</a></p><button type="button" class="totop"><svg viewBox="0 0 12 8" width="12" height="8" aria-hidden="true" focusable="false"><path d="M1.5 6.5L6 2l4.5 4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Back to top</button></div>
</div></footer>'''


JSX = JS.replace("var nk=h.indexOf('rack')===0?'rack':h;", "var nk=h.indexOf('rack')===0?'rack':h.indexOf('lga-')===0?'network':h;").replace("'/#'+h}", "'/#'+(h.indexOf('lga-')===0?'network':h==='rack'?'home':h)}")
assert JSX.count("lga-") == 2
JS2 = """(function(){var sel=[].slice.call(document.querySelectorAll('.lgasel'));
sel.forEach(function(s){s.addEventListener('change',function(){var v=s.value||'network';location.hash=v;if(v==='network')setTimeout(function(){var t=document.getElementById('our-network'),h=document.querySelector('.site-head');if(t)window.scrollTo(0,t.getBoundingClientRect().top+window.scrollY-(h?h.offsetHeight:0)-24)},60)})});
window.addEventListener('hashchange',function(){sel.forEach(function(s){s.value=s.getAttribute('data-cur')})});
document.addEventListener('click',function(e){var a=e.target.closest('[data-sample]');if(a)e.preventDefault()});
[].slice.call(document.querySelectorAll('.totop')).forEach(function(b){b.addEventListener('click',function(){window.scrollTo(0,0)})});
var nd=[].slice.call(document.querySelectorAll('.navdrop'));
function closeDD(){nd.forEach(function(n){n.classList.remove('open');var b=n.querySelector('.dd-btn');if(b)b.setAttribute('aria-expanded','false')})}
nd.forEach(function(n){var b=n.querySelector('.dd-btn');b.addEventListener('click',function(e){e.stopPropagation();var o=!n.classList.contains('open');closeDD();n.classList.toggle('open',o);b.setAttribute('aria-expanded',o)})});
document.addEventListener('click',function(e){if(!e.target.closest('.navdrop'))closeDD()});
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeDD()});
[].slice.call(document.querySelectorAll('[data-jump]')).forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();closeDD();var id=a.getAttribute('data-jump');
function go(){var t=document.getElementById(id),h=document.querySelector('.site-head');if(t)window.scrollTo(0,t.getBoundingClientRect().top+window.scrollY-(h?h.offsetHeight:0)-16)}
var pg=a.getAttribute('data-page');if(location.hash==='#'+pg){document.getElementById('nav').classList.remove('open');var mb=document.querySelector('.menu-btn');if(mb)mb.setAttribute('aria-expanded','false');go()}else{location.hash=pg;setTimeout(go,200)}})})})();"""


def page(v):
    css, cls = CSS_B, "tb"
    body = "".join([screen("home", "Home", home_body(HERO_FOR[v])), screen("about", "About", about_body()), screen("impact", "Impact", impact_body()), screen("rack", "R.A.C.K.", rack_body()), screen("privacy", "Privacy Policy", privacy_body()), screen("network", "Network", network_body())] + [screen("lga-" + slug(l), l, lga_body(l)) for l in LGA_ORDER])
    return f'''<!doctype html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>NRCRA teal-led {NAMES[v]}</title><meta name="robots" content="noindex">
<meta name="description" content="Teal-led exploration of the NRCRA website. Sample content only.">
{FONT}<style>{BASE}{CSS1}{CSS_T}{css}{MOBILE}</style></head><body class="v1 teal {cls}">
{nav3()}<main id="main">{body}</main>{tfooter()}{protobar3(v)}<script data-cfasync="false">{JSX}</script><script data-cfasync="false">{JS2}</script></body></html>'''


# Prototypes A, B and C are the same site; they differ only in the Home hero (card, photo, solid). The old hand-kept Prototype A is archived in prototype-a-archive/.
def adjusted_teal(html):
    """Every teal border, background and text in A, B and C is the adjusted teal #00857C (the light tints stay as tints)."""
    html = re.sub(r"#00a79d|#00615a", "#00857c", html, flags=re.I)
    return re.sub(r"rgba\(\s*0\s*,\s*(?:97\s*,\s*90|167\s*,\s*157)\s*,", "rgba(0,133,124,", html)


def weights_4_8(html):
    """Only two font weights are used in Round 2: 400 and 800."""
    m = lambda w: "400" if int(w) < 600 else "800"
    html = re.sub(r"font-weight:\s*(\d{3})", lambda x: "font-weight:" + m(x.group(1)), html)
    return re.sub(r"font:\s*(\d{3}) ", lambda x: "font:" + m(x.group(1)) + " ", html)


def finish(v):
    html = re.sub(r"(?<![0-9])60\+", "50+", page(v)).replace("7 council areas", "8 council areas").replace("<dt>7</dt><dd>local government areas", "<dt>8</dt><dd>local government areas").replace("#6c8590", "#586c74").replace("#e0f4f3", "#f3f9f8").replace("#bfe9e7", "#beddda")
    return weights_4_8(adjusted_teal(html))


def main():
    for v in ("prototype-c",):
        B.write(v + "/index.html", finish(v))
