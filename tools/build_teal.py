"""Teal-led exploration (teal as accents and tints only): Home, About, Impact (blank) and Network on the designer's Layout Design wireframe
(content and layout only), styled from Prototype 1, with teal as the main driver instead of navy.

  prototype-b  teal as accents and tints only (highlights, buttons, borders, tinted panels), navy kept for the footer

White text never sits on teal (2.99:1). Navy text on teal is 5.05:1.
Imported by build.py, which owns the shared helpers and base CSS.
"""
import re
import random
import build as B
from build import E, img, logo, screen, icon, BASE, MOBILE, JS, FONT, CSS1, VIMEO, CONTACT

SIGN_IN = "https://rack.nrcra.org.au"  # the R.A.C.K address NRCRA gave us (not live yet)
MENU = [("home", "Home"), ("network", "Network"), ("about", "About"), ("impact", "Impact"), ("rack", "R.A.C.K.")]
NAMES = {"prototype-a": "Prototype A", "prototype-b": "Prototype B"}
SHORT = {"prototype-a": "A", "prototype-b": "B"}


def nav3():
    links = "".join(f'<a href="#{k}" data-nav="{k}">{t}</a>' for k, t in MENU)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap head-in"><a href="#home" class="brand" aria-label="NRCRA home">{logo()}</a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav"><svg class="hb" viewBox="0 0 20 14" width="20" height="14" aria-hidden="true" focusable="false"><path d="M1.5 1.5h17M1.5 7h17M1.5 12.5h17" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>Menu</button>
<nav id="nav" aria-label="Main">{links}<a class="btn btn-cta" href="{SIGN_IN}" target="_blank" rel="noopener">Sign In</a></nav></div></header>'''


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
def home_body():
    lgas = "".join(f'<li><a href="#lga-{slug(n)}">{E(n)} LGA</a></li>' for n in ["Tweed", "Byron", "Kyogle", "Lismore", "Richmond Valley", "Ballina", "Tenterfield", "Clarence Valley"])
    return f'''<div class="hero1 herobg"><div class="wrap"><div class="h1-panel tpanel"><span class="eyebrow">Northern Rivers Community Resilience Alliance</span>
<h1>We believe when climate disasters hit, it&rsquo;s the <span class="mark">community{B.SQUIGGLE}</span> that steps up first.</h1><p class="lede">We are a network of grassroots, community-led groups working together to build disaster resilience across the Northern Rivers.</p>
<p class="btnrow"><a class="btn btn-primary" href="#about">Learn About us</a><button type="button" class="btn btn-ghost hvid watchbtn" data-video="{VIMEO}" aria-label="Watch the Alliance sizzle reel video, full screen"><svg viewBox="0 0 14 16" width="14" height="16" aria-hidden="true" focusable="false"><path d="M3 3l8 5-8 5z" fill="currentColor" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/></svg>Watch reel</button></p></div>
<div class="h1-photo" data-video="{VIMEO}">{img("cheer", eager=True, alt="")}<button class="play" aria-label="Play the Alliance sizzle reel video, full screen"><svg viewBox="0 0 88 88" width="88" height="88" aria-hidden="true" focusable="false"><path d="M37 34L55 44L37 54Z" fill="currentColor" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/><path id="wp" d="M13 44A31 31 0 0 0 75 44" fill="none"/><text font-size="8.5" font-weight="800" letter-spacing="1.8" fill="currentColor" text-anchor="middle" style="font-family:inherit"><textPath href="#wp" startOffset="50%">WATCH</textPath></text></svg></button></div></div></div>

<section class="sec"><div class="wrap"><div class="statcard impact"><h2 class="sechead">Our Impact</h2>{B.stats()}<p class="btnrow"><a class="btn btn-tertiary" href="#impact">See Impact</a></p></div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><div class="card wwa surface"><div><h2>60+ groups in 8 Local Government Areas,<br>one region, <span class="mark">one network.{B.SQUIGGLE}</span></h2><p class="subline">Community knowledge, lived experience and shared learning.</p><p>Since early 2024, groups and organisations across the Northern Rivers have joined together to form the Resilience Alliance, a community-led network focused on collective care, preparedness and regional strength.</p><p>Neighbours became first responders in 2022. Today, those neighbours are building the systems that will protect communities before the next disaster.</p>
<p class="btnrow"><a class="btn btn-primary" href="#network">Explore the Network</a></p></div><div class="wwa-cluster"><div class="circles">{B.deco("rings", "")}{vimg("group-3")}{vimg("group-2")}<span class="blob" aria-hidden="true"></span></div><ul class="lgapills">{lgas}</ul></div></div></div></section>'''


# ---------------------------------------------------------------- About
MEAL6 = [("Includes Everyone", "People feel respected and able to participate.", "people"), ("Builds Trust", "Relationships and cooperation grow over time.", "connect"),
         ("Shares Power", "Groups influence priorities, leadership and decisions.", "share"), ("Builds Capability", "Groups gain skills, resources and confidence.", "grow"),
         ("Learns and Adapts", "Feedback leads to practical changes.", "improve"), ("Creates Collective Value", "Groups gain what they couldn’t achieve alone.", "strengthen")]


TEAM = [("Kathie Heyman", "Network Lead"), ("Milou Muiser", "Communications, Events and Engagement"),
        ("Marlena Sue Basser", "Capacity Building Coordinator"), ("Claire McLisky", "Capacity Building Coordinator"), ("Barbara Winters", "Capacity Building Coordinator")]


def team():
    return '<ul class="team2">' + "".join(f'<li><span class="tc" aria-hidden="true">{"".join(w[0] for w in n.split()[:2])}</span><b>{n}</b><span>{r}</span></li>' for n, r in TEAM) + '</ul>'


STEER = [("Together Pottsville", "https://www.togetherpottsville.org", "together-pottsville.png", ""),
         ("Murwillumbah CORE", "https://www.mcore2484.org", "murwillumbah-core.webp", ""),
         ("Resilient Uki", "https://resilientuki.org", "resilient-uki.png", ""),
         ("South Golden Beach, New Brighton, Ocean Shores", "https://www.byron.nsw.gov.au/Environment-Resilience/Emergency-Recovery/Byron-Shire-Community-Resilience-Network", "", "SG"),
         ("Main Arm Disaster Response", "https://www.byron.nsw.gov.au/Environment-Resilience/Emergency-Recovery/Byron-Shire-Community-Resilience-Network", "", "MA"),
         ("Resilient Lismore", "https://resilientlismore.org.au", "resilient-lismore.png", ""),
         ("Northern Rivers Community Foundation", "https://nrcf.org.au", "nrcf.png", ""),
         ("Plan C", "https://www.planc.org.au", "plan-c.webp", "dark"),
         ("University Centre for Rural Health", "https://ucrh.edu.au", "ucrh.svg", "")]


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


def focus_cards():
    return '<ol class="focus">' + "".join(f'<li><span class="fn">{i:02d}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(FOCUS, 1)) + "</ol>"


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


def about_body():
    return f'''    <div class="wrap"><div class="splith"><div><span class="eyebrow pill-t">About us</span><h1>We know communities are stronger when they&rsquo;ve built trusted relationships <span class="mark">together.{B.SQUIGGLE}</span></h1></div><div class="ph">{img("line", eager=True)}</div></div></div>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="aboutgrid"><div class="card abt"><h2><span class="hlx hlx-y">The Resilience Alliance</span></h2><p>Established in November 2023. Its roots lie in a run of compounding disasters: the 2017 floods, the 2019&ndash;20 bushfires, and the catastrophic floods and landslides of 2022. In each, local community organisers played a vital role in response, recovery and adaptation. Research in the years that followed found that these grassroots groups wanted stronger connections with each other for peer-to-peer support. That showed the need for regional collaboration in disaster resilience.</p><p>We support a network of place-based resilience groups to develop their own local approaches to risk reduction, preparedness and recovery, for fire, flood, landslides and whatever comes next.</p><p>The Resilience Alliance helps government agencies, councils and emergency services deliver on the commitments of the NSW State Emergency Management Plan, State Disaster Mitigation Plan and regional resilience priorities by connecting formal systems with trusted, community-led action.</p><div class="bar bar-y" aria-hidden="true"></div></div>
<div class="vpcol"><div class="card vpc"><h2><span class="hlx hlx-t">Vision</span></h2><p>Connected, collaborative Northern Rivers communities that are empowered to care for themselves and each other before, during and after disasters.</p><div class="bar bar-t" aria-hidden="true"></div></div>
<div class="card vpc"><h2><span class="hlx hlx-o">Purpose</span></h2><p>To develop a self-sustaining, trusted Alliance of place-based, community-led resilience groups and organisations. The Alliance shares knowledge and resources, provides mutual support and wellbeing, takes collective action and advocates for identified community needs.</p><div class="bar bar-o" aria-hidden="true"></div></div></div></div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2 class="sechead">The Steering Committee:</h2><p class="lede">Is the coordinating body for the Resilience Alliance. It is made up of representatives from resilience-related groups and organisations across the region, and operates by agreement among groups and organisations rather than by reporting to a separate incorporated parent body. The steering committee actively aims to maintain a network that reflects the geographic and community diversity of the region.</p><p class="lede">The Steering Committee comprises the following groups and organisations.</p>{steer_tiles()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2 class="sechead">How we work</h2><p class="lede">Through regular gatherings, deep conversations and shared experiences, the Resilience Alliance is building a community-led network focused on collective care, preparedness and regional strength.</p>{how_cards()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2 class="sechead">{hl("Our Focus")}</h2>{focus_cards()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="card surface"><h2 class="sechead">Our journey</h2>{journey_b()}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="card surface"><h2 class="sechead">Resilience Alliance Team:</h2>{team()}</div></div></section>'''


# ---------------------------------------------------------------- Network
HOW = [("Connect", "50+ grassroots, community-led groups are connected together across the region so they can build trusting relationships with each other so they know who to contact when the next climate disaster hits.", "teal"),
       ("Share", "Sharing knowledge, experience, practical tools and resources across the network so everyone can benefit from what others have learned.", "yellow"),
       ("Care", "Peer to peer support, reducing the load, removing duplication and placing a real value on the efforts of all.", "orange")]


def how_cards():
    return '<ul class="howcards">' + "".join(f'<li class="hw-{c}"><h3><span>{t}.</span></h3><p>{d}</p></li>' for t, d, c in HOW) + "</ul>"


FUND = lambda t: f'<p class="fund">{t}</p>'
JOURNEY_B = [
    ("2022", [("Floods &amp; disaster:", "Communities respond to the floods, showing local leadership and the need for stronger regional collaboration.", "")]),
    ("2023", [("Building connections:", "A Sydney Environment Institute &amp; UCRH study documents community self organisation after the floods &mdash; the evidence base that leads participants to call for a regional alliance.", "")]),
    ("2024", [("Resilience Alliance established:", "The inaugural regional gathering with 96 participants from 40+ groups across the Northern Rivers formally establishes the Resilience Alliance.", ""),
              ("Co-designing the future:", "Groups develop the Resilience Alliance&rsquo;s distributed governance model and strategic priorities.", "Funded by the University of Centre of Rural Health.")]),
    ("2025", [("Capability in action:", "The Resilience Alliance trains 20 groups on spontaneous volunteer management systems, supporting groups post Cyclone Alfred.", "Funded by the NSW Government&rsquo;s Spontaneous Volunteering Program and Foundation for Regional and Rural Renewal.")]),
    ("2026", [("Connected, Prepared Communities:", "Disaster Ready Fund 3 investment supports the next stage of capability and resilience-building with 60 groups throughout the Northern Rivers.", "Funded by the Australian Government and NSW Government."),
              ("Participatory granting project:", "17 groups receive up to $10,000 in funding as part of the first round of a newly developed participation funding process.", "Funding by The NRMA Help Fund, Monash University and Northern Rivers Community Foundation.")]),
    ("2027+", [("Onwards:", "Our research and MEAL process continues alongside the Alliance as it supports and resources groups in the network.", "Monitoring, Evaluation, Accountability and Learning")]),
]


def journey_b():
    return '<ol class="river">' + "".join(
        f'<li><b>{y}</b><div class="jt">' + "".join(f'<h3>{h}</h3><p>{t}</p>' + (f'<p class="fund">{f}</p>' if f else "") for h, t, f in es) + '</div></li>'
        for y, es in JOURNEY_B) + "</ol>"


def pillar_cards(nums=False):
    if nums:
        return '<ol class="pillcards">' + "".join(f'<li><span class="pi pnum">{i:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p></li>' for i, (t, d, k) in enumerate(B.PILLARS, 1)) + "</ol>"
    return '<ol class="pillcards">' + "".join(f'<li><span class="pi">{icon(k)}</span><span class="pn">{i:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p></li>' for i, (t, d, k) in enumerate(B.PILLARS, 1)) + "</ol>"


# 58 suburbs and localities across the 8 LGAs (public locality lists). Group names and websites are random sample content.
SUBURBS = {
    "Tweed": ["Banora Point", "Cabarita Beach", "Kingscliff", "Murwillumbah", "Pottsville", "Tumbulgum", "Tweed Heads", "Uki"],
    "Byron": ["Bangalow", "Billinudgel", "Brunswick Heads", "Byron Bay", "Mullumbimby", "Ocean Shores", "Suffolk Park"],
    "Ballina": ["Alstonville", "Ballina", "Lennox Head", "Skennars Head", "Wardell", "Wollongbar"],
    "Lismore": ["Bexhill", "Clunes", "Dunoon", "Goonellabah", "Lismore", "Nimbin", "Rosebank", "The Channon"],
    "Kyogle": ["Bonalbo", "Kyogle", "Mallanganee", "Tabulam", "Urbenville", "Woodenbong"],
    "Richmond Valley": ["Broadwater", "Casino", "Coraki", "Evans Head", "Rappville", "Woodburn"],
    "Tenterfield": ["Drake", "Jennings", "Mingoola", "Tenterfield", "Torrington", "Wallangarra"],
    "Clarence Valley": ["Brooms Head", "Grafton", "Harwood", "Iluka", "Lawrence", "Maclean", "Nymboida", "South Grafton", "Ulmarra", "Wooli", "Yamba"],
}
NAME_FORMS = ["{} Survivors", "{} Resilience Crew", "Rising {}", "Strong {} Collective", "{} Ready Crew", "Brave {} Hearts", "{} Together", "Phoenix {}",
              "{} Neighbours United", "Tough Mob of {}", "{} Grit and Grace", "{} Rapid Responders", "Rebuild {}", "{} Storm Sisters", "Steady {}", "{} Good Hands"]
LGA_ORDER = sorted(SUBURBS)


def slug(t):
    return re.sub(r"[^a-z]+", "-", t.lower()).strip("-")


# Real groups where both the name and a working website are known (checked 30 Oct 2026). Membership of the Alliance to be confirmed by NRCRA.
REAL = {
    "Lismore": ("Resilient Lismore", "https://resilientlismore.org.au"),
    "Uki": ("Resilient Uki", "https://resilientuki.org"),
    "Wardell": ("WardellCORE", "https://www.wardellcore.community"),
    "Mullumbimby": ("Mullumbimby District Neighbourhood Centre", "https://www.mdnc.org.au"),
    "Nimbin": ("Nimbin Disaster Resilience Group", "https://nnic.org.au/pub/index.php/disasters"),
    "The Channon": ("The Channon Resilience", "https://thechannonhub.org/"),
    "Rosebank": ("Minyon Resilience Network", "https://minyonresiliencenetwork.com/"),
}


def all_groups():
    rnd = random.Random(58)
    forms = NAME_FORMS[:]
    rnd.shuffle(forms)
    rows = []
    for lga, subs in SUBURBS.items():
        for sub in subs:
            rows.append([sub, lga])
    rows.sort(key=lambda r: r[0].lower())
    out = []
    for i, (sub, lga) in enumerate(rows):
        has_web = rnd.random() < .7
        if sub in REAL:
            out.append((REAL[sub][0], sub, lga, REAL[sub][1]))
        else:
            out.append((forms[i % len(forms)].format(sub), sub, lga, "#" if has_web else ""))
    return out


def group_card(name, sub, lga, web):
    if web == "#":
        btn = '<a class="btn btn-ghost btn-sm" href="#" data-sample="1">Visit website</a>'
    elif web:
        btn = f'<a class="btn btn-ghost btn-sm" href="{web}" target="_blank" rel="noopener">Visit website<span class="sr-only"> (opens in a new tab)</span></a>'
    else:
        btn = ""
    return f'<li><b>{E(name)}</b><span>{E(sub)}, {E(lga)}</span>{btn}</li>'


def lga_select(cur=""):
    first = "Browse the region"
    opts = f'<option value="{"network" if cur else ""}">{first}</option>'
    opts += "".join(f'<option value="lga-{slug(l)}"{" selected" if l == cur else ""}>{E(l)} LGA</option>' for l in LGA_ORDER)
    return f'<select class="lgasel" aria-label="Filter the network by Local Government Area (LGA)" data-cur="{"lga-" + slug(cur) if cur else ""}">{opts}</select>'


def dir_head(title, cur="", tag="h2"):
    return f'<div class="dirhead"><{tag} class="sechead">{title}</{tag}>{lga_select(cur)}</div>'


TESTIMONIALS = [
    ("laughing", "Like a whole region of neighbours in your corner.", "Kingscliff Survivors"),
    ("hug", "Like finally being heard by people who have been through it too.", "Rising Lismore"),
]


def testimonials():
    def card(img_html, quote, who):
        return f'<li><div class="tph">{img_html}</div><blockquote><p>&ldquo;{E(quote)}&rdquo;</p><footer>&mdash; {E(who)}</footer></blockquote></li>'
    vid = f'<div class="tph vid" data-video="{VIMEO}">{img("circle", alt="")}<button class="play" aria-label="Play the video: The Alliance feels like a family, full screen"><svg viewBox="0 0 88 88" width="88" height="88" aria-hidden="true" focusable="false"><path d="M37 34L55 44L37 54Z" fill="currentColor" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/></svg></button></div>'
    c1 = card(img(TESTIMONIALS[0][0], alt=""), TESTIMONIALS[0][1], TESTIMONIALS[0][2])
    c2 = f'<li>{vid}<blockquote><p>&ldquo;Like a family we did not know we had.&rdquo;</p><footer>&mdash; Phoenix Casino</footer></blockquote></li>'
    c3 = card(img(TESTIMONIALS[1][0], alt=""), TESTIMONIALS[1][1], TESTIMONIALS[1][2])
    return f'<section class="sec" style="padding-top:0"><div class="wrap"><h2 class="sechead">Our Stories</h2><ul class="tcards">{c1}{c2}{c3}</ul></div></section>'


def network_body():
    cards = "".join(group_card(*g) for g in all_groups())
    return f'''<div class="wrap"><div class="splith net rev"><div><span class="eyebrow">Network</span><h1>50+ groups,<br>one region,<br><span class="mark">one network.{B.SQUIGGLE}</span></h1><p class="lede">8 Local Government Areas (LGAs) across the Northern Rivers region of New South Wales, Australia.</p></div><div class="ph">{B.map_embed().split('<p class="vnote">')[0]}</div></div></div>
{testimonials()}
<section class="sec" id="our-network" style="padding-top:0"><div class="wrap">{dir_head("Our Network")}<ul class="gsub">{cards}</ul></div></section>'''


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
<p class="btnrow"><a class="btn btn-ghost" href="mailto:hello@nrcra.org.au?subject=R.A.C.K.%20access">Request access</a><a class="btn btn-ghost" href="mailto:hello@nrcra.org.au?subject=R.A.C.K.%20help">Get help</a><a class="btn btn-primary" href="{SIGN_IN}" target="_blank" rel="noopener">Sign in</a></p></div>
<div class="ph rackph"><img src="../assets/img/rack-hero.webp" alt="A community member using the R.A.C.K. on a desktop computer, searching the shared resource library." width="1024" height="799" loading="eager" decoding="async"></div></div></div>
<section class="sec"><div class="wrap rackhead"><h2 class="sechead">In this resource library</h2><p class="lede">You&rsquo;ll find templates and guides you can use straight away, and contribute knowledge back in two minutes.</p><ol class="pillcards rackcats">{cards}</ol></div></section>'''


def impact_body():
    return '<div class="wrap"><div class="pg-head"><h1>Impact</h1></div></div>'


# ---------------------------------------------------------------- CSS
CSS_T = """
body.teal{--bg:#f3f6f7}
.teal .sechead{margin-bottom:28px}
/* title highlight is off for now; the class stays so it can come back */
.hl{padding:0}
.teal .card{border-radius:var(--r);padding:36px}
.wwa{display:grid;grid-template-columns:.9fr 1.1fr;gap:40px;align-items:center}.wwa>*{min-width:0}.wwa-map{max-width:420px;justify-self:center;width:100%}.wwa-cluster{width:100%;order:-1;padding-top:calc(5.7% - 10px)}.mark{isolation:isolate}.mark .squig{z-index:-1}.vp-text{max-width:72ch}
.lgapills{list-style:none;margin:12px 0 0;padding:0;display:flex;flex-wrap:wrap;justify-content:center;gap:6px 6px}.lgapills li{position:relative;isolation:isolate;padding:.25em .85em;font-weight:700;font-size:.88rem;line-height:1.25;color:#586c74}.lgapills li::before{content:"";position:absolute;inset:-4px -7px;z-index:-1;background:url(../assets/brush/brush-1.svg) center/100% 100% no-repeat}.lgapills li:nth-child(3n+2)::before{background:url(../assets/brush/brush-2.svg) center/100% 100% no-repeat}.lgapills li:nth-child(3n)::before{background:url(../assets/brush/brush-3.svg) center/100% 100% no-repeat}
.statrow{display:grid;grid-template-columns:1.1fr .9fr;gap:24px;align-items:center}.statrow>*{min-width:0}.statcard{border-radius:var(--r);padding:36px}.statcard .stats dt{color:var(--navy)}
.framed{border-radius:36px;padding:14px;background:var(--fr,var(--teal))}.framed img{border-radius:24px;width:100%;aspect-ratio:4/3;object-fit:cover}
.pcard2 .p3{align-items:center}
.partband{padding:56px 0 52px;text-align:center}.partband h2{margin-bottom:24px}
.steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.steps li{display:grid;justify-items:center;gap:8px}.steps .ci{width:76px;height:76px;border-radius:50%;background:#fff;border:3px solid var(--ci);display:grid;place-items:center;color:var(--navy)}.steps .ci .ico{width:34px;height:34px}.steps a{font-weight:800}.steps p{margin:0;font-size:.95rem}
.steps li:nth-child(1){--ci:var(--orange)}.steps li:nth-child(2){--ci:var(--navy)}.steps li:nth-child(3){--ci:var(--navy)}.steps li:nth-child(4){--ci:var(--orange)}
@media(max-width:860px){.wwa,.statrow{grid-template-columns:1fr}.steps{grid-template-columns:1fr 1fr}.teal .card{padding:26px 20px}}
.teal .kb li{border-bottom:10px solid var(--kc)}.kb li:nth-child(1){--kc:var(--teal)}.kb li:nth-child(2){--kc:var(--yellow)}.kb li:nth-child(3){--kc:var(--orange)}
.splith{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;padding:36px 0 12px}.splith>*{min-width:0}.splith .ph img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:32px}.splith .ph .mapbox{height:380px;border-radius:32px}.splith.rev .ph{order:-1}
@media(max-width:860px){.splith{grid-template-columns:1fr}.splith.rev .ph{order:0}}
.script{font:700 1.5rem Caveat,cursive;color:var(--orange-d);display:block;margin-bottom:2px}
.vp-wrap{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}.vp-wrap>*{min-width:0}@media(max-width:860px){.vp-wrap{grid-template-columns:1fr}}
.circles{position:relative;width:100%;max-width:560px;margin:0 auto -60px;aspect-ratio:1/1.14;transform:translateX(calc(-6.75% - 6px))}.circles img{position:absolute;border-radius:50%;object-fit:cover;border:8px solid #fff;aspect-ratio:1/1;height:auto}
.circles img:nth-of-type(1){width:66%;left:15%;top:0;z-index:2}.circles img:nth-of-type(2){width:60%;left:22%;bottom:calc(-8% + min(50px,11%));z-index:1;translate:0 -60px}
.circles .blob{position:absolute;left:calc(6.5% + 12px);top:calc(-5% + 10px);width:30%;aspect-ratio:1/1;z-index:3;background:var(--yellow);border-radius:62% 38% 55% 45%/48% 60% 40% 52%}

.deco{position:absolute;pointer-events:none;width:150px;height:150px}.circles .deco-rings{z-index:0;width:46%;height:auto;right:-7%;left:auto;top:26%}
@media(max-width:560px){.circles{margin-bottom:-36px}.circles img:nth-of-type(2){translate:0 -36px}}
@media(max-width:760px){.circles img{border-width:6px}}
.meal{margin:18px 0 22px}.mealgrid{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(6,1fr);gap:12px}.mealgrid li{background:var(--grey-6);border-radius:18px;padding:18px 14px}.mealgrid .ico{width:34px;height:34px;color:var(--navy);margin-bottom:8px}.mealgrid h3{font-size:1rem;margin:0 0 .3em}.mealgrid p{margin:0;font-size:.9rem}
@media(max-width:1000px){.mealgrid{grid-template-columns:repeat(3,1fr)}}@media(max-width:560px){.mealgrid{grid-template-columns:1fr 1fr}}
.team2{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;justify-content:center;gap:24px}.team2 li{width:150px;text-align:center;display:grid;justify-items:center;gap:4px}.team2 .tc{width:96px;height:96px;border-radius:50%;background:var(--teal-25);display:grid;place-items:center;font-weight:800;font-size:.9rem}.team2 li span:not(.tc){font-size:.9rem;color:var(--muted)}
.pillcards{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:16px;justify-content:center}.pillcards li{flex:1 1 200px;max-width:230px;background:#fff;border-radius:22px;padding:22px 18px;text-align:center;border-bottom:14px solid var(--pc)}
.pillcards li:nth-child(1){--pc:var(--teal)}.pillcards li:nth-child(2){--pc:var(--yellow)}.pillcards li:nth-child(3){--pc:var(--orange)}.pillcards li:nth-child(4){--pc:var(--navy)}.pillcards li:nth-child(5){--pc:#9fb0b8}
.pillcards .pi{width:52px;height:52px;border-radius:50%;background:var(--grey-6);display:grid;place-items:center;margin:0 auto 6px;color:var(--navy)}.pillcards .pi .ico{width:28px;height:28px}.pillcards .pn{font-weight:900;font-size:.85rem;letter-spacing:.1em}.pillcards h3{margin:.3em 0}.pillcards p{margin:0;font-size:.95rem}
.gdir-c{grid-template-columns:repeat(auto-fill,minmax(220px,1fr))!important;gap:16px!important}.gdir-c li{padding:0 0 16px!important;background:#fff!important;border:1px solid var(--line);border-radius:20px!important;overflow:hidden}.gdir-c .gph{display:block;position:relative;margin-bottom:34px}.gdir-c .gph img{width:100%;height:100px;object-fit:cover}
.gdir-c .gdot{position:absolute;left:14px;bottom:-24px;width:48px;height:48px;border-radius:50%;background:var(--teal);color:var(--navy);border:3px solid #fff;display:grid;place-items:center;font-weight:900}.gdir-c b,.gdir-c span:not(.gph):not(.gdot),.gdir-c em,.gdir-c small{margin:0 16px}.gdir-c small{color:var(--muted);margin-top:6px}

/* Prototype 2's rounded buttons and river-style journey */
body{--btn-r:12px}
ol.river{position:relative;list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(6,1fr);gap:16px}
ol.river::before{content:"";position:absolute;left:0;right:0;top:16px;height:12px;border-radius:99px;background:var(--teal-25)}
ol.river li{position:relative;padding-top:64px;display:block}
ol.river b{position:absolute;top:0;left:0;box-sizing:border-box;height:44px;display:flex;align-items:center;background:#fff;border:3px solid var(--teal);border-radius:99px;padding:0 1.1em;font-weight:900;color:var(--teal-d);font-size:1rem;line-height:1}
ol.river h3{margin:0 0 .25em;font-size:1rem}ol.river p{margin:0 0 .9em;font-size:.95rem}ol.river .jt>*:last-child{margin-bottom:0}ol.river .fund{font-style:italic;font-size:.82rem;color:var(--muted);margin-top:-.5em}
@media(max-width:860px){ol.river{grid-template-columns:1fr;gap:28px}ol.river::before{left:42px;right:auto;width:12px;margin-left:-6px;top:0;bottom:0;height:auto}ol.river li{padding:0 0 0 118px;min-height:44px}ol.river b{left:0;width:84px;justify-content:center;padding:0}}
.tb .howcards{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:16px;justify-content:center}.tb .howcards li{flex:1 1 260px;max-width:380px;background:var(--bg);color:var(--navy);border:1px solid var(--line);border-radius:22px;padding:24px 22px 28px;border-bottom:14px solid var(--pc);text-align:left}
.tb .howcards li p{margin:0;color:var(--navy)}.tb .howcards h3{margin:0 0 16px}.tb .howcards h3 span{text-align:center;display:block;width:100%;box-sizing:border-box;border-radius:99px;padding:.45em 1em;font-weight:900}
.tb .hw-teal{--pc:var(--teal);--bg:var(--teal-25)}.tb .hw-teal h3 span{background:#00857c;color:#fff}.tb .hw-yellow{--pc:var(--yellow);--bg:var(--yellow-40)}.tb .hw-yellow h3 span{background:var(--yellow);color:var(--navy)}.tb .hw-orange{--pc:var(--orange);--bg:var(--orange-25)}.tb .hw-orange h3 span{background:var(--orange);color:#fff}
.pillcards .pnum{font-weight:900;font-size:1.05rem;letter-spacing:.04em}

.tb .aboutgrid{display:grid;grid-template-columns:1.2fr 1fr;gap:20px;align-items:stretch}.tb .aboutgrid>*{min-width:0}
.tb .abt{background:#fff;border:1px solid var(--line)}.tb .abt h2{margin:0 0 .5em}.tb .abt p{margin:0 0 1em}
.tb .vpcol{display:grid;gap:20px}.tb .vpc{background:#fff;border:1px solid var(--line)}.tb .vpc h2{margin:0 0 .6em;font-size:1.6rem}.tb .vpc p{margin:0}
.hlx{padding:0 .12em;display:inline-block;line-height:1.15}.hlx-t{background:linear-gradient(transparent 70%,var(--teal) 70%,var(--teal) 90%,transparent 90%)}.hlx-o{background:linear-gradient(transparent 70%,var(--orange) 70%,var(--orange) 90%,transparent 90%)}.hlx-y{background:linear-gradient(transparent 70%,var(--yellow) 70%,var(--yellow) 90%,transparent 90%)}
.tb .bar{height:8px;border-radius:99px;margin:20px 0 0;max-width:200px}.tb .bar-t{background:var(--teal)}.tb .bar-o{background:var(--orange)}.tb .bar-y{background:var(--yellow)}
@media(max-width:860px){.tb .aboutgrid{grid-template-columns:1fr}}
.tb .steer{list-style:none;margin:28px 0 0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.tb .steer a{display:flex;flex-direction:column;align-items:center;gap:12px;text-decoration:none;color:var(--navy);height:100%;background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px 16px 18px;box-sizing:border-box}
.tb .slogo{display:grid;place-items:center;width:100%;height:56px;box-sizing:border-box}.tb .slogo.dark{background:var(--navy);border-radius:12px;width:auto;padding:0 14px;margin:0 auto}.tb .slogo img{width:auto;height:auto;max-width:100%;height:56px;object-fit:contain}.tb .slogo.dark img{height:40px}
.tb .sinit{width:56px;height:56px;border-radius:50%;background:var(--teal-25);display:grid;place-items:center;font-weight:900;font-size:1.1rem;color:var(--navy)}
.tb .sname{font-weight:800;text-align:center}.tb .steer a:hover .sname,.tb .steer a:focus-visible .sname{text-decoration:underline}.tb .steer a:hover{border-color:var(--teal)}
@media(max-width:860px){.tb .steer{grid-template-columns:repeat(2,1fr)}}@media(max-width:480px){.tb .steer{grid-template-columns:1fr}}
.tb .focus{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:18px;justify-content:center}.tb .focus li{flex:1 1 300px;max-width:360px;background:var(--fb);border-radius:170px 170px 22px 22px;padding:44px 26px 30px;text-align:left}
.tb .focus .fn{display:grid;place-items:center;width:56px;height:56px;border-radius:50%;background:var(--fc);color:var(--ft);font-weight:900;font-size:1.1rem;margin:0 auto 12px}.tb .focus h3{text-align:center;margin:0 0 .6em}.tb .focus p{margin:0;font-size:.97rem}
.tb .focus li:nth-child(1){--fb:var(--teal-25);--fc:#00857c;--ft:#fff}.tb .focus li:nth-child(2){--fb:var(--yellow-40);--fc:var(--yellow);--ft:var(--navy)}.tb .focus li:nth-child(3){--fb:var(--orange-25);--fc:var(--orange);--ft:#fff}.tb .focus li:nth-child(4){--fb:var(--blue-15);--fc:var(--navy);--ft:#fff}.tb .focus li:nth-child(5){--fb:var(--grey-6);--fc:#9fb0b8;--ft:var(--navy)}
.tb .team2 li{width:190px}.tb .team2 b{margin-top:6px}.tb .team2 .tc{font-weight:900;font-size:1.3rem;color:var(--navy)}
/* accent bars sit on the bottom edge, not the top */
.arc{border-top:0;border-bottom:6px solid var(--teal)}.arc.y{border-bottom-color:var(--yellow)}.arc.o{border-bottom-color:var(--orange)}
.cards .pcard{border-top:0}.cards .pcard:nth-child(1){border-bottom:6px solid var(--teal)}.cards .pcard:nth-child(2){border-bottom:6px solid var(--yellow)}.cards .pcard:nth-child(3){border-bottom:6px solid var(--orange)}
.v1 .pc{padding:26px 16px 0}.v1 .pc::before{display:none}.v1 .pc>*:nth-last-child(2){margin-bottom:22px}
.v1 .pc::after{content:"";display:block;align-self:stretch;height:18px;margin:auto -16px 0;border-radius:0 0 6px 6px;background:var(--teal)}
.v1 .pc:nth-child(2)::after{background:var(--yellow)}.v1 .pc:nth-child(3)::after{background:var(--orange)}.v1 .pc:nth-child(4)::after{background:var(--navy)}.v1 .pc:nth-child(5)::after{background:#9fb0b8}
.pillcards li{border-top:0;border-bottom:14px solid var(--pc);padding:22px 18px}
.pg-head{padding:48px 0 40px}.pg-head h1{margin:0}
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
.tb .herobg .h1-photo::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,97,90,.93) 0%,rgba(0,97,90,.88) 52%,rgba(0,97,90,.1) 100%)}
.tb .herobg .h1-panel{background:transparent;border:0;color:#fff}
.tb .herobg .h1-panel h1{color:#fff}.tb .herobg .h1-panel .eyebrow,.tb .herobg .h1-panel .lede{color:#fff}
.tb .herobg .h1-panel .btn-primary{border-color:#fff}
.tb .herobg .h1-panel .eyebrow{display:inline-block;align-self:flex-start;background:#fff;color:var(--navy);padding:.55em 1.5em;border-radius:99px;margin-bottom:48px}
.mark{position:relative;display:inline-block}.mark .squig{position:absolute;left:0;right:0;bottom:-.02em;width:100%;height:.4em}
@media(min-width:740px){.herobg .h1-panel{padding:52px 44px}}
@media(max-width:739px){.tb .herobg>.wrap:first-child{display:flex;align-items:flex-start;min-height:0;padding:0}.tb .herobg .h1-panel{margin:0;padding:28px 20px 40px;max-width:none}.tb .herobg .h1-photo::after{background:linear-gradient(180deg,rgba(0,97,90,.94) 0%,rgba(0,97,90,.88) 30%,rgba(0,97,90,.5) 48%,rgba(0,97,90,0) 62%)}.herobg .h1-panel h1{font-size:1.75rem;line-height:1.15}.herobg .h1-panel .lede{font-size:1rem}.herobg .h1-panel .eyebrow{font-size:.72rem}}
.tb .h1-panel{background:var(--teal-25);color:var(--navy);border:4px solid var(--teal)}.tb .h1-panel h1,.tb .h1-panel .eyebrow{color:var(--navy)}.tb .h1-panel .btn-ghost{color:var(--navy);border-color:var(--navy);background:#fff}.tb .h1-panel .btn-ghost:hover{background:var(--navy);color:#fff}
.tb #nav a[aria-current=page]{background:var(--teal-25)}
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
.herobg{padding:20px 0 0!important}
.herobg>.wrap:first-child{width:calc(100% - 40px);max-width:calc(var(--wrap) - 40px);margin:0 auto;padding:0;border-radius:40px;overflow:hidden;border-top:8px solid var(--teal);border-bottom:8px solid var(--teal)}
.herobg .h1-panel{margin:40px 0}
.herobg .h1-photo .play{left:calc((var(--pw,580px) + 100%)/2)}
@media(max-width:739px){.herobg>.wrap:first-child{border-radius:28px;width:calc(100% - 24px)}.herobg .h1-panel{margin:0}.tb .herobg .h1-panel{padding:28px 18px 36px}.herobg .btnrow .btn{padding:.7em 1em}}
/* Who we are: when the columns stack, the photos come first, above the title */
/* phones, B: gradient runs left to right and the play circle becomes a normal secondary button beside About */
.watchbtn{display:none}
.watchbtn{gap:.55em}.watchbtn svg{flex:none}
@media(max-width:739px){.tb .herobg .h1-photo .play{display:none}.watchbtn{display:inline-flex}.tb .herobg .watchbtn{background:#fff;color:#07293b;border-color:#fff}.tb .herobg .watchbtn:hover{background:#00857c;color:#fff;border-color:#fff}.tb .herobg .watchbtn:active{background:#beddda;color:#07293b;border-color:#fff}.tb .herobg .h1-photo::after{background:linear-gradient(90deg,rgba(0,97,90,.94) 0%,rgba(0,97,90,.9) 62%,rgba(0,97,90,.62) 100%)}}
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
.tb .site-foot .foot-cols{grid-template-columns:repeat(3,minmax(0,1fr))}.tb .fstack .fcol+.fcol{margin-top:24px}@media(max-width:700px){.tb .site-foot .foot-cols{grid-template-columns:1fr}}

/* MEAL: six circles round a ring, like the Layout Design PDF */
.mealwrap{display:grid;grid-template-columns:minmax(0,440px) 1fr;gap:48px;align-items:center;margin:28px 0 0}
.mealring{position:relative;width:100%;max-width:440px;aspect-ratio:1/1;margin:0 auto}.mealring svg{position:absolute;inset:0;width:100%;height:100%}
.mealring ol{list-style:none;margin:0;padding:0}.mealring li{position:absolute;width:30%;aspect-ratio:1/1;translate:-50% -50%;border-radius:50%;display:grid;place-items:center;text-align:center;font-weight:800;font-size:clamp(1.05rem,2.6vw,1.2rem)}
.mealq{margin:0;border-left:4px solid var(--teal);padding-left:24px}.mealq p{margin:0 0 .6em}.mealq .mq{font-weight:800;font-size:1.25rem;line-height:1.35;color:var(--navy)}
@media(max-width:860px){.mealwrap{grid-template-columns:1fr;gap:28px}}
.btn-tertiary{background:#07293b;color:#fff;border-color:#07293b}.btn-tertiary:hover{background:#00857c;color:#fff;border-color:#07293b}.btn-tertiary:active{background:#beddda;color:#07293b;border-color:#07293b}
main a.btn-tertiary:hover{background:#00857c;color:#fff}
/* page titles: Home, Network and About all use the same H1 size */
.tb .herobg .h1-panel h1{font-size:clamp(2rem,4.6vw,3.5rem);line-height:1.12}
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
/* one rhythm: 65px between every section on every page */
.tb .sec{padding:0 0 65px!important}.tb .page>.sec:first-child{padding-top:65px!important}
.tb .hero1.herobg{margin-bottom:65px}.tb .page>.wrap:first-child>.splith{padding-bottom:0}.tb .page>.wrap:first-child{margin-bottom:65px}

/* Network only: double the space (130px) between sections */
.tb #network>.wrap:first-child{margin-bottom:130px}.tb #network>.sec:not(:last-child){padding-bottom:130px!important}
/* Stories from the Alliance: the text above is centred against the tall map, so it looks 79px more open above; give the space below the same */
.tb #network>section.sec:first-of-type{padding-bottom:209px!important}
/* Our Network directory (Network and every LGA page): double the space under the cards */
.tb #network>.sec:last-child,.tb [id^="lga-"]>.sec:last-child{padding-bottom:130px!important}

/* Network page: map as tall as the text, testimonials, suburb directory */
.tb .splith.net{align-items:stretch}.tb .splith.net>div:first-child{align-self:center}.tb .splith.net .ph{display:flex}.tb .splith.net .ph .mapbox{height:auto;min-height:517px;flex:1}
.tb .splith .eyebrow.pill-t,.tb .eyebrow.pill-t{display:inline-block;background:#00857c;color:#fff;padding:.55em 1.5em;border-radius:99px;margin-bottom:28px}
.tcards{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
.tcards li{background:#fff;border:1px solid var(--line);border-bottom:10px solid var(--yellow);border-radius:20px;padding:18px 18px 24px;display:flex;flex-direction:column}
.tcards .tph{position:relative;aspect-ratio:4/3;overflow:hidden;border-radius:18px;margin-bottom:16px}.tcards .tph img{width:100%;height:100%;object-fit:cover;display:block;border-radius:0}
.tcards .tph .play{inset:auto;top:50%;left:50%;margin:0;transform:translate(-50%,-50%);width:76px;height:76px;padding:0;display:grid;place-items:center}.tcards .tph .play svg{width:100%;height:100%}
.tcards blockquote{margin:0;padding:0;display:flex;flex-direction:column;gap:14px;flex:1}.tcards blockquote p{margin:0;font-size:1.2rem;line-height:1.4;font-weight:700}
.tcards blockquote footer{margin-top:auto;color:#586c74;font-weight:800;font-size:.95rem}
.dirhead{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:16px 24px;margin-bottom:35px}.dirhead .sechead{margin:0;grid-column:2;grid-row:1;text-align:center}.dirhead .lgasel{grid-column:3;grid-row:1;justify-self:end}
.lgasel-l{display:flex;flex-direction:column;gap:4px;font-weight:700;font-size:.9rem}.lgasel{font:700 1rem var(--font);color:var(--navy);padding:.7em 2.4em .7em 1em;min-height:44px;border:2px solid #00857c;border-radius:12px;background:#fff;min-width:260px;cursor:pointer}
.dirhead h1.sechead{font-size:clamp(1.6rem,3.2vw,2.4rem);font-weight:800}
.gsub{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px}
.gsub li{background:#fff;border:1px solid var(--line);border-radius:20px;padding:20px;display:flex;flex-direction:column;gap:4px;align-items:flex-start}
.gsub b{font-size:1.1rem;line-height:1.25}.gsub span{color:#586c74;font-size:.95rem}.gsub .btn{margin-top:14px}
.gsub .sr-only,.rcards .sr-only,.steer .sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.btn-sm{font-size:.9rem;padding:.5em 1.1em;min-height:38px}
@media(max-width:860px){.tcards{grid-template-columns:1fr}.tb .splith.net .ph .mapbox{height:461px;min-height:0;flex:none}}
@media(max-width:739px){.lgasel-l,.lgasel{width:100%}.dirhead{grid-template-columns:1fr}.dirhead .sechead,.dirhead .lgasel{grid-column:1}.dirhead .sechead{grid-row:1}.dirhead .lgasel{grid-row:2}}
"""


def tfooter():
    def col(n, title, items):
        return f'<div class="fcol"><h2 class="fb{n}">{title}</h2><ul class="flist">' + "".join(f'<li><a href="{u}">{E(t)}</a></li>' for t, u in items) + "</ul></div>"
    contact = [("hello@nrcra.org.au", "mailto:hello@nrcra.org.au")]
    touch = [("Facebook", B.LINKS["fb"]), ("LinkedIn", B.LINKS["li"])]
    site = [("Alliance Home", "#home"), ("Network", "#network"), ("About", "#about"), ("Impact", "#impact"), ("R.A.C.K.", "#rack"), ("Sign In", SIGN_IN)]
    top = '<div class="foot-top"><span class="foot-logo boxed">' + logo("logo") + '</span></div>'
    return f'''<footer class="site-foot"><div class="wrap">
<div class="foot-cols">{top}{col(3, "Site map", site)}<div class="fstack">{col(2, "Stay in Touch", touch)}{col(1, "Contact", contact)}</div></div>
<div class="ack">{B.ABORIGINAL_FLAG}<p>{B.ACK}</p></div>
<p class="copy">© 2026 Northern Rivers Community Resilience Alliance &middot; <a href="https://www.nrcra.org.au/copy-of-terms-conditions">Privacy Policy</a></p>
</div></footer>'''


JSX = JS.replace("var nk=h.indexOf('rack')===0?'rack':h;", "var nk=h.indexOf('rack')===0?'rack':h.indexOf('lga-')===0?'network':h;").replace("'/#'+h}", "'/#'+(h.indexOf('lga-')===0?'network':h==='rack'?'home':h)}")
assert JSX.count("lga-") == 2
JS2 = """(function(){var sel=[].slice.call(document.querySelectorAll('.lgasel'));
sel.forEach(function(s){s.addEventListener('change',function(){var v=s.value||'network';location.hash=v;if(v==='network')setTimeout(function(){var t=document.getElementById('our-network'),h=document.querySelector('.site-head');if(t)window.scrollTo(0,t.getBoundingClientRect().top+window.scrollY-(h?h.offsetHeight:0)-24)},60)})});
window.addEventListener('hashchange',function(){sel.forEach(function(s){s.value=s.getAttribute('data-cur')})});
document.addEventListener('click',function(e){var a=e.target.closest('[data-sample]');if(a)e.preventDefault()})})();"""


def page(v):
    css, cls = CSS_B, "tb"
    body = "".join([screen("home", "Home", home_body()), screen("about", "About", about_body()), screen("impact", "Impact", impact_body()), screen("rack", "R.A.C.K.", rack_body()), screen("network", "Network", network_body())] + [screen("lga-" + slug(l), l, lga_body(l)) for l in LGA_ORDER])
    return f'''<!doctype html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>NRCRA teal-led {NAMES[v]}</title><meta name="robots" content="noindex">
<meta name="description" content="Teal-led exploration of the NRCRA website. Sample content only.">
{FONT}<style>{BASE}{CSS1}{CSS_T}{css}{MOBILE}</style></head><body class="v1 teal {cls}">
{nav3()}<main id="main">{body}</main>{tfooter()}{protobar3(v)}<script data-cfasync="false">{JSX}</script><script data-cfasync="false">{JS2}</script></body></html>'''


# prototype-a/index.html is a frozen, hand-kept file (Prototype A). It is not built from build.py, so changes to Round 1 never reach it.
def main():
    B.write("prototype-b/index.html", re.sub(r"(?<![0-9])60\+", "50+", page("prototype-b")).replace("7 council areas", "8 council areas").replace("<dt>7</dt><dd>local government areas", "<dt>8</dt><dd>local government areas").replace("#6c8590", "#586c74").replace("#e0f4f3", "#f3f9f8").replace("#bfe9e7", "#beddda"))
