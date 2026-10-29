"""Round 2: the two prototypes the client and designer compare with each other.

  client       Prototype 1 (colour block sections) rebuilt from the client's written feedback
  recommended  The same client content laid out on the designer's audited wireframes (Layout Design.pdf)
  accessibility  Notes on where the requested design does not meet WCAG 2.2 AA, with visual references

Imported by build.py, which owns the shared helpers, base CSS and the dashboard.
"""
import build as B
from build import E, img, logo, screen, icon, CONTACT, LINKS, RACK_URL, ACK, ABORIGINAL_FLAG, FLAG, LOGO_DOTS, BASE, MOBILE, JS, FONT, CSS1, VIMEO

FUND = "../assets/funders/"
DOC_URL = "https://docs.google.com/document/d/1NaC61OZYomUhRGzN3M5WOgimnBq-7E3khqsOiFFaZfQ/edit?usp=sharing"
HELLO = "hello@nrcra.org.au"

# ================================================================ content (client's own wording, from their feedback document)
HERO = "We believe when climate disasters hit, it’s the community that steps up first."
HERO_SUB = "We are a network of grassroots, community-led groups working together to build disaster resilience across the Northern Rivers."
GROUPS_H = "60+ groups, one region, one network."
GROUPS_SUB = "Community knowledge, lived experience and shared learning."
HOW_INTRO = "Through regular gatherings, deep conversations and shared experiences, the Resilience Alliance is building a community-led network focused on collective care, preparedness and regional strength."
HOW = [
    ("Connect", "60+ grassroots, community-led groups are connected together across the region so they can build trusting relationships with each other so they know who to contact when the next climate disaster hits.", "t"),
    ("Share", "Sharing knowledge, experience, practical tools and resources across the network so everyone can benefit from what others have learned.", "y"),
    ("Care", "Peer to peer support, reducing the load, removing duplication and placing a real value on the efforts of all.", "o"),
]
FOCUS = [
    ("Growing the Alliance", "We are strengthening our network by clarifying who we are, why we come together and how we work. Through regular gatherings we are building a clearer picture of who is involved and how we connect.", "t"),
    ("Training and Resource Sharing", "We are making knowledge, practical tools and training easier to find through our Resilience Alliance Community Knowledge Hub. Our training is led by experienced locals, with the aim of strengthening our network from within the community.", "y"),
    ("Peer Support and Self Care", "Resilience work asks a lot of the people who do it, so we are committed to balanced wellbeing and collective care across our region. We are mapping the support already available, identifying good practice, with the aim to develop an adaptable wellbeing framework that groups can use to look after themselves and each other.", "o"),
    ("Funding and Collaborative Projects", "We are working towards a more sustainable and collaborative approach to funding for resilience work across the region. Identifying shared opportunities we aim to reduce competition and increase collective impact.", "n"),
    ("Advocacy", "We believe our collective voice is stronger than any single group’s. By understanding our own network, identifying key stakeholders and building advocacy skills among members, we are developing a collaborative approach to advocating for resilient communities across the region.", "g"),
]
IMPACT_N = ("60+", "grassroots community-led groups and organisations")
IMPACT_NOTE = "Key impact highlights will be supplied by Eunice. This space is held for them."
ABOUT_H = "We know communities are stronger when they’ve built trusted relationships together."
ABOUT_P = [
    "The Resilience Alliance was established in November 2023. Its roots lie in a run of compounding disasters: the 2017 floods, the 2019–20 bushfires, and the catastrophic floods and landslides of 2022. In each, local community organisers played a vital role in response, recovery and adaptation. Research in the years that followed found that these grassroots groups wanted stronger connections with each other for peer-to-peer support. That showed the need for regional collaboration in disaster resilience.",
    "The Resilience Alliance supports a network of place-based resilience groups to develop their own local approaches to risk reduction, preparedness and recovery, for fire, flood, landslides and whatever comes next.",
    "The Resilience Alliance helps government agencies, councils and emergency services deliver on the commitments of the NSW State Emergency Management Plan, State Disaster Mitigation Plan and regional resilience priorities by connecting formal systems with trusted, community-led action.",
]
VISION = "Connected, collaborative Northern Rivers communities that are empowered to care for themselves and each other before, during and after disasters."
PURPOSE = "To develop a self-sustaining, trusted Alliance of place-based, community-led resilience groups and organisations. The Alliance will share knowledge and resources; provide mutual support and wellbeing; take collective action, and advocate for identified community needs."
# year, [(title, text, funded-by)]
JOURNEY2 = [
    ("2022", [("Floods and disaster", "Communities respond to the floods, showing local leadership and the need for stronger regional collaboration.", "")]),
    ("2023", [("Building connections", "A Sydney Environment Institute and UCRH study documents community self organisation after the floods — the evidence base that leads participants to call for a regional alliance.", "")]),
    ("2024", [("Resilience Alliance established", "The inaugural regional gathering with 96 participants from 40+ groups across the Northern Rivers formally establishes the Resilience Alliance.", ""),
              ("Co-designing the future", "Groups develop the Resilience Alliance’s distributed governance model and strategic priorities.", "Funded by the University Centre for Rural Health.")]),
    ("2025", [("Capability in action", "The Resilience Alliance trains 20 groups on spontaneous volunteer management systems, supporting groups post Cyclone Alfred.", "Funded by the NSW Government’s Spontaneous Volunteering Program and Foundation for Regional and Rural Renewal.")]),
    ("2026", [("Connected, Prepared Communities", "Disaster Ready Fund 3 investment supports the next stage of capability and resilience-building with 60 groups throughout the Northern Rivers.", "Funded by the Australian Government and NSW Government."),
              ("Participatory granting project", "17 groups receive up to $10,000 in funding as part of the first round of a newly developed participation funding process.", "Funding by the NRMA Help Fund, Monash University and Northern Rivers Community Foundation.")]),
]
GOVERNANCE = ("Distributed Governance Model", "The Resilience Alliance recognises that groups and organisations in its network differ in size, capacity and access to power. We will endeavour to ensure every group and or organisation in the network has the opportunity to participate fairly and thus keeping the Resilience Alliance healthy.")
STEERING = ("The Steering Committee", "Is the coordinating body for the Resilience Alliance. It is made up of representatives from resilience-related groups and organisations across the region, and operates by agreement among groups and organisations rather than by reporting to a separate incorporated parent body. The steering committee actively aims to maintain a network that reflects the geographic and community diversity of the region.")
STEERING_GROUPS = ["Together Pottsville", "Murwillumbah CORE", "Resilient Uki", "South Golden Beach, New Brighton, Ocean Shores", "Main Arm Disaster Response", "Resilient Lismore", "Northern Rivers Community Foundation", "Plan C", "University Centre for Rural Health"]
TEAM = [("Kathie Heyman", "Network Lead"), ("Milou Muiser", "Communications, Events and Engagement"), ("Marlena Sue Basser", "Capacity Building Coordinator"), ("Claire McLisky", "Capacity Building Coordinator"), ("Barbara Winters", "Capacity Building Coordinator")]
NET_HERO = "60+ groups, one region, one network."
# Project summaries condensed from the three project one-pagers
PROJECTS2 = [
    ("Connected and Prepared", "o", "Enabling regional readiness through the Resilience Alliance.", "Supported by the Australian Government’s National Emergency Agency through the Disaster Ready Fund. At least 60 grassroots resilience groups will receive tailored governance support, shared digital tools, capacity building support, peer learning opportunities and strengthened regional collaboration."),
    ("Resourcing Community Resilience", "y", "Resources directed to the priorities communities identify themselves.", "Supported by the NRMA Help Fund, with the Northern Rivers Community Foundation and Monash University’s Fire to Flourish initiative. Groups co-designed a participatory approach to collectively decide where resources can have the greatest impact."),
    ("Learning Together", "t", "Listening, reflecting and tracking change together.", "With embedded researchers from the University Centre for Rural Health, our Monitoring, Evaluation, Accountability and Learning (MEAL) approach turns what we learn into action."),
]
COMMENTS_NOTE = "More positive comments from the gathering data will go here. They will be supplied by NRCRA."
FOCUS_NAMES = [f[0] for f in FOCUS]
FOCUS_GROUPS = {FOCUS_NAMES[i]: gs for i, gs in enumerate(B.PILLAR_GROUPS.values())}
RES = [("Get Ready", "Plans and checklists for before a disaster.", "board"), ("Volunteers", "Registering, inducting and looking after volunteers.", "laughing"),
       ("Run Your Group", "Governance, templates and running a healthy group.", "cards"), ("Emergencies", "What to do and who to call when it happens.", "meeting"),
       ("Training and Workshops", "Workshops and learning for group leaders.", "hall"), ("Share", "Add what works to the R.A.C.K and help another group.", "talk")]

DOTS_W = '<svg class="dots" viewBox="0 0 48 40" aria-hidden="true"><circle cx="24" cy="9" r="8" fill="#fff"/><circle cx="9" cy="28" r="6.5" fill="#fff"/><circle cx="39" cy="28" r="6.5" fill="#fff"/></svg>'


# ================================================================ shared parts
def funders_strip():
    ph = lambda n: f'<li class="fund-ph">{n}<small>logo to be added</small></li>'
    logos = "".join(f'<li><img src="{FUND}{f}" alt="{E(n)}" height="34"></li>' for f, n in [("help.png", "NRMA Insurance, a Help Company"), ("frrr.png", "Foundation for Rural and Regional Renewal"), ("ucrh.png", "University Centre for Rural Health")])
    return f'<div class="fund"><div class="wrap"><p class="fund-t">Thanks to our funders</p><ul>{ph("Federal Government")}{ph("State Government")}{logos}</ul></div></div>'


def nav2(items, cta_label, cta_href, ext=False):
    links = "".join(f'<a href="#{k}" data-nav="{k}">{E(t)}</a>' for k, t in items)
    cta = f'<a class="btn btn-cta" href="{cta_href}"' + (' target="_blank" rel="noopener"' if ext else ' data-nav="rack"') + f'>{E(cta_label)}</a>'
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap head-in">
<a href="#home" class="brand" aria-label="NRCRA home">{logo()}</a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav id="nav" aria-label="Main">{links}{cta}</nav></div></header>'''


def footer2(menu, sign_href, ext):
    def col(t, items):
        return f'<div class="fcol"><h2>{t}</h2><ul class="flist">' + "".join(f'<li><a href="{u}"{x}>{E(n)}</a></li>' for n, u, x in items) + "</ul></div>"
    ex = ' target="_blank" rel="noopener"' if ext else ""
    m = [(t, f"#{k}", "") for k, t in menu] + [("Sign In", sign_href, ex)]
    return f'''<footer class="site-foot"><div class="wrap"><div class="foot-cols">
<div class="foot-top"><span class="foot-logo boxed">{logo("logo")}</span></div>
{col("Contact", [(HELLO, f"mailto:{HELLO}", "")])}{col("Stay in touch", [("Facebook", LINKS["fb"], ""), ("LinkedIn", LINKS["li"], "")])}{col("Menu", m)}</div>
<div class="ack">{ABORIGINAL_FLAG}<p>{ACK}</p></div><p class="copy">© 2026 Northern Rivers Community Resilience Alliance &middot; <a href="https://www.nrcra.org.au/copy-of-terms-conditions">Privacy Policy</a></p></div></footer>'''


def protobar2(cur):
    names = {"client": "Client request", "recommended": "Recommended"}
    short = {"client": "Client", "recommended": "Rec."}
    others = "".join(f'<a class="pb-btn" data-proto="{k}" href="../{k}/" aria-label="{names[k]}"><span class="pb-short" aria-hidden="true">{short[k]}</span><span class="pb-long">{names[k]}</span></a>' for k in names if k != cur)
    here = names.get(cur, "Accessibility notes")
    return f'''<div class="protobar" role="region" aria-label="Prototype controls"><div class="pb-in">
<p class="pb-label"><b>MOCKUP &amp; PROTOTYPE ONLY</b> by <a href="https://veemercado.com">veemercado.com</a><span class="pb-cur"> &middot; viewing Round 2: {here}</span></p>
<nav class="pb-nav" aria-label="Round 2 prototypes"><a class="pb-btn pb-all" href="../#round-2">All prototypes</a>{others}<a class="pb-btn" href="../accessibility/" aria-label="Accessibility notes"><span class="pb-short" aria-hidden="true">AA</span><span class="pb-long">AA notes</span></a></nav>
<button type="button" class="pb-top" aria-label="Back to top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})"><span class="pb-long">Back to top&nbsp;</span><span aria-hidden="true">&uarr;</span></button></div></div>'''


def shell(title, css, body, cur, nav_html, foot_html, extra="", pre_footer=""):
    return f'''<!doctype html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="robots" content="noindex">
<meta name="description" content="Round 2 prototype for the Northern Rivers Community Resilience Alliance website. Sample content only.">
{FONT}<style>{BASE}{CSS1}{CSS2}{css}{MOBILE}{MOBILE2}</style></head><body class="r2 {cur} {extra}">
{funders_strip()}{nav_html}<main id="main">{body}</main>{pre_footer}{foot_html}{protobar2(cur)}<script>{JS}{JS2}</script></body></html>'''


def hl(text, c="y"):
    return f'<span class="hl hl-{c}">{E(text)}</span>'


def band():
    return '<ul class="csband"><li class="cs-t">Connect</li><li class="cs-y">Share</li><li class="cs-o">Care</li></ul>'


def how_cards(cls="how"):
    return f'<ul class="{cls}">' + "".join(f'<li class="hw-{c}">{DOTS_W}<h3>{t}</h3><p>{E(d)}</p></li>' for t, d, c in HOW) + "</ul>"


def focus_rows(cls="focus"):
    return f'<ol class="{cls}">' + "".join(f'<li class="fo-{c}"><h3><span>{E(t)}</span></h3><p>{E(d)}</p></li>' for t, d, c in FOCUS) + "</ol>"


def impact_block():
    return f'''<div class="impact"><div class="big"><b>{IMPACT_N[0]}</b><span>{IMPACT_N[1]}</span></div>
<ul class="hi"><li>Impact highlight</li><li>Impact highlight</li><li>Impact highlight</li></ul><p class="note-x">{IMPACT_NOTE}</p></div>'''


def comments(alt=False):
    q = B.QUOTE
    return f'''<ul class="cmts"><li class="cm-q"><blockquote><p>&ldquo;{q[0]}&rdquo;</p><cite>{q[1]}</cite></blockquote></li><li class="cm-ph"><p>{COMMENTS_NOTE}</p></li></ul>'''


def vtile(photo, title):
    return f'<li class="vt" data-video="{VIMEO}">{img(photo, alt="")}<button class="play" aria-label="Play video: {E(title)} (placeholder, the sizzle reel stands in)"><span aria-hidden="true">&#9654;</span></button><span class="vtag">{E(title)}</span></li>'


def stories():
    return '<ul class="vts">' + vtile("crowd", "Group story: video to come") + vtile("laughing", "Group story: video to come") + vtile("listening", "Group story: video to come") + '</ul><p class="vnote">Videos of groups from the gathering will sit here. The sizzle reel stands in until they are supplied.</p>'


def directory2(cards=False):
    ph = ["crowd", "laughing", "listening", "cards", "table", "pair", "talk", "house"]
    n = 0
    items = ""
    for p, gs in FOCUS_GROUPS.items():
        for name, area, lga in gs:
            top = f'<span class="gph">{img(ph[n % len(ph)], alt="")}<span class="gdot" aria-hidden="true">{name[-1]}</span></span>' if cards else ""
            n += 1
            items += f'<li data-lga="{lga}" data-pillar="{E(p)}">{top}<b>{E(name)}</b><span>{area}, {lga}</span><em>{E(p)}</em>' + ('<small>Group description to come.</small>' if cards else "") + "</li>"
    lopts = "".join(f"<option>{l}</option>" for l in B.LGAS)
    popts = "".join(f"<option>{E(p)}</option>" for p in FOCUS_NAMES)
    return f'''<div class="dir"><div class="filters">
<label>Location <select data-f="lga"><option value="">All locations</option>{lopts}</select></label>
<label>Focus <select data-f="pillar"><option value="">All areas of focus</option>{popts}</select></label>
<label class="dq">Search <input type="search" data-f="q" placeholder="Group name or town"></label></div>
<ul class="gdir{" gdir-c" if cards else ""}">{items}</ul><p class="empty" hidden>No groups match those filters.</p><p class="vnote">Sample groups. In the build, one Google Sheet of groups drives both the map pins and this list, so updating a row updates both.</p></div>'''


def funder_tiles(cls="ftiles"):
    t = [("help.png", "NRMA Insurance, a Help Company"), ("frrr.png", "Foundation for Rural and Regional Renewal"), ("ucrh.png", "University Centre for Rural Health"), ("nrcf.png", "Northern Rivers Community Foundation")]
    ph = "".join(f'<li class="fund-ph tile">{n}<small>logo to be added (follow the logo protocols)</small></li>' for n in ["Australian Government", "NSW Government"])
    return f'<ul class="{cls}">{ph}' + "".join(f'<li><img src="{FUND}{f}" alt="{E(n)}" loading="lazy"></li>' for f, n in t) + "</ul>"


def projects_tiles(cls="proj"):
    return f'<ul class="{cls}">' + "".join(f'<li class="pj-{c}"><h3>{E(t)}</h3><p class="pj-l">{E(l)}</p><p>{E(d)}</p></li>' for t, c, l, d in PROJECTS2) + "</ul>"


def htl_cards():
    out = '<ol class="htl">'
    for i, (y, es) in enumerate(JOURNEY2):
        body = "".join(f'<div class="he"><h3>{E(t)}</h3><p>{E(d)}</p>' + (f'<p class="fnote">{E(f)}</p>' if f else "") + "</div>" for t, d, f in es)
        out += f'<li class="hk{i % 5}"><span class="hy">{y}</span>{body}</li>'
    return out + "</ol>"


def team_circles():
    ini = lambda n: "".join(w[0] for w in n.split()[:2])
    return '<ul class="team2">' + "".join(f'<li><span class="tc" aria-hidden="true">{ini(n)}</span><b>{E(n)}</b><span>{E(r)}</span></li>' for n, r in TEAM) + '</ul><p class="vnote" style="text-align:center">Photos to come.</p>'


def steering():
    return f'<h2>{STEERING[0]}</h2><p>{STEERING[1]}</p><p><b>The Steering Committee comprises the following groups and organisations.</b></p><ul class="chips">' + "".join(f"<li>{E(g)}</li>" for g in STEERING_GROUPS) + "</ul>"


def from_to2():
    return B.from_to()


# ================================================================ CSS
CSS2 = """
body.r2{--bg:#f3f6f7}
.fund{background:#fff;border-bottom:1px solid var(--line)}.fund .wrap{display:flex;align-items:center;gap:8px 24px;flex-wrap:wrap;padding-top:10px;padding-bottom:10px}
.fund-t{margin:0;font-weight:800;font-size:.9rem;white-space:nowrap}.fund ul{list-style:none;margin:0;padding:0;display:flex;align-items:center;gap:8px 24px;flex-wrap:wrap}
.fund img{height:34px;width:auto;max-width:150px;object-fit:contain}
.fund-ph{border:2px dashed var(--navy);border-radius:10px;padding:.25em .8em;font-weight:800;font-size:.85rem;line-height:1.15}.fund-ph small{display:block;font-weight:600;font-size:.75rem}
.btn-navy{background:var(--navy);color:#fff;border-color:var(--navy)}.btn-navy:hover{background:#fff;color:var(--navy)}
.hl{background:linear-gradient(transparent 56%,var(--hc,var(--yellow)) 56%,var(--hc,var(--yellow)) 94%,transparent 94%);padding:0 .12em;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.hl-y{--hc:var(--yellow)}.hl-t{--hc:var(--teal)}.hl-o{--hc:var(--orange)}
.site-foot{--foot:var(--teal);--foot-ink:var(--navy);--foot-h:var(--navy);--foot-line:rgba(7,41,59,.4)}
.site-foot a{text-decoration:underline}.site-foot :focus-visible{outline-color:var(--navy)}.site-foot .foot-logo.boxed{max-width:260px}
.g-panel{background:var(--teal)!important;color:var(--navy)}.g-panel h1{color:var(--navy)}.g-panel .lede{margin:0}.g-panel :focus-visible{outline-color:var(--navy)}
.g-panel .btn-ghost{color:var(--navy);border-color:var(--navy)}.g-panel .btn-ghost:hover{background:var(--navy);color:#fff}
.csband{list-style:none;margin:28px 0 0;padding:0;display:grid;grid-template-columns:repeat(3,1fr)}
.csband li{padding:24px 10px;text-align:center;font-weight:900;font-size:clamp(1.15rem,3vw,2.2rem);color:var(--navy)}.cs-t{background:var(--teal)}.cs-y{background:var(--yellow)}.cs-o{background:var(--orange)}
.grp{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center}.grp>*{min-width:0}
.framed{border-radius:36px;padding:14px;background:var(--fr,var(--orange))}.framed img{border-radius:24px;width:100%;aspect-ratio:4/3;object-fit:cover}.fr-y{--fr:var(--yellow)}
@media(max-width:860px){.grp{grid-template-columns:1fr;gap:28px}}
.how{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.how li{border-radius:var(--r);padding:30px;color:var(--navy)}
.hw-t{background:var(--teal)}.hw-y{background:var(--yellow)}.hw-o{background:var(--orange)}.how .dots{width:64px;height:54px;display:block;margin:0 0 14px}.how h3{font-size:1.7rem}.how p{margin:0;font-size:1.05rem}.hw-o p{font-weight:700;font-size:1.18rem}
@media(max-width:860px){.how{grid-template-columns:1fr}}
.how-intro{max-width:70ch;font-size:1.15rem}
.focus{list-style:none;margin:0;padding:0;display:grid;gap:16px}.focus li{display:grid;grid-template-columns:minmax(220px,300px) 1fr;gap:12px 32px;align-items:start;border-radius:var(--r);padding:28px 30px;color:var(--navy)}
.focus h3{margin:0;font-size:1.3rem}.focus h3 span{display:inline-block;border-radius:14px;padding:.35em .8em;background:var(--fc)}.focus p{margin:0;font-size:1.05rem}
.fo-t{background:var(--teal-12);--fc:var(--teal)}.fo-y{background:var(--yellow-20);--fc:var(--yellow)}.fo-o{background:var(--orange-12);--fc:var(--orange)}.fo-n{background:var(--blue-15);--fc:var(--navy)}.fo-n h3 span{color:#fff}.fo-g{background:var(--grey-6);--fc:#9fb0b8}
@media(max-width:760px){.focus li{grid-template-columns:1fr}}
.impact{display:grid;grid-template-columns:1fr 1.2fr;gap:28px 40px;align-items:center}.big{background:var(--navy);color:#fff;border-radius:var(--r);padding:36px;display:grid;gap:6px}.big b{font-size:clamp(3.4rem,8vw,5.4rem);line-height:1;color:var(--yellow);font-weight:900}.big span{font-size:1.25rem;font-weight:700}
.hi{list-style:none;margin:0;padding:0;display:grid;gap:12px}.hi li{border:2px dashed var(--navy);border-radius:18px;padding:18px 20px;font-weight:700;background:#fff;color:var(--navy)}.note-x{grid-column:1/-1;margin:0;font-weight:700}
@media(max-width:860px){.impact{grid-template-columns:1fr}}
.cmts{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1.4fr 1fr;gap:20px}.cm-q,.cm-ph{border-radius:var(--r);padding:30px}.cm-q{background:var(--yellow-40)}.cm-q blockquote{margin:0}.cm-q p{font-size:clamp(1.3rem,2.6vw,1.8rem);font-weight:800;line-height:1.35;margin:0}.cm-q cite{display:block;font-style:normal;font-weight:700;margin-top:.8em}
.cm-ph{border:2px dashed var(--navy);background:#fff;display:grid;align-items:center}.cm-ph p{margin:0;font-weight:700}@media(max-width:760px){.cmts{grid-template-columns:1fr}}
.netband{background:var(--teal);color:var(--navy);border-radius:32px;padding:44px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:20px}.netband h2{margin:0}.netband :focus-visible{outline-color:var(--navy)}.netband p{margin:.4em 0 0}
.vts{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.vt{position:relative;aspect-ratio:16/10;border-radius:var(--r);overflow:hidden;background:var(--navy);cursor:pointer}.vt img{width:100%;height:100%;object-fit:cover}.vt .play{width:68px;height:68px}
@media(max-width:760px){.vts{grid-template-columns:1fr}}
.htl{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(5,1fr);gap:18px;align-items:start}.htl li{background:#fff;border-radius:var(--r);padding:0 18px 22px;border-top:8px solid var(--hc);overflow:hidden}
.hk0{--hc:var(--orange)}.hk1{--hc:var(--teal)}.hk2{--hc:var(--yellow)}.hk3{--hc:var(--orange)}.hk4{--hc:var(--navy)}
.hy{display:inline-block;margin:-4px 0 14px;background:var(--hc);color:var(--navy);font-weight:900;font-size:1.25rem;border-radius:0 0 14px 14px;padding:.3em .9em}.hk4 .hy{color:#fff}
.he h3{font-size:1.05rem;margin:.9em 0 .3em}.he:first-of-type h3{margin-top:0}.he p{margin:0 0 .4em;font-size:.95rem}.fnote{font-style:italic}
@media(max-width:1100px){.htl{grid-template-columns:repeat(3,1fr)}}@media(max-width:760px){.htl{grid-template-columns:1fr}}
.two{display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:start}.two>*{min-width:0}@media(max-width:860px){.two{grid-template-columns:1fr}}
.tcard2{background:#fff;border-radius:var(--r);padding:30px}.tcard2 h2{font-size:1.6rem}.tcard2 p:last-child{margin-bottom:0}
.chips{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:10px}.chips li{background:var(--teal-12);border-radius:99px;padding:.4em 1em;font-weight:700}
.vpx{border-radius:var(--r);padding:34px}.vpx h2{margin-bottom:14px}.vpx p{margin:0;font-size:1.15rem}.vpx-t{background:var(--teal-25)}.vpx-y{background:var(--yellow-40)}
.team2{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;justify-content:center;gap:24px}.team2 li{width:190px;text-align:center;display:grid;justify-items:center;gap:4px}.team2 .tc{width:96px;height:96px;border-radius:50%;background:var(--yellow-40);display:grid;place-items:center;font-weight:900;font-size:1.6rem}.team2 li:nth-child(even) .tc{background:var(--teal-25)}.team2 li span:not(.tc){font-size:.9rem;color:var(--muted)}
.proj{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.proj li{background:#fff;border-radius:var(--r);padding:26px;border-top:10px solid var(--pc)}.pj-o{--pc:var(--orange)}.pj-y{--pc:var(--yellow)}.pj-t{--pc:var(--teal)}.proj .pj-l{font-weight:800}.proj p:last-child{margin:0}
@media(max-width:860px){.proj{grid-template-columns:1fr}}
.ftiles{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:16px}.ftiles li{background:#fff;border:1px solid var(--line);border-radius:var(--r);aspect-ratio:3/2;display:grid;place-items:center;padding:18px;text-align:center}.ftiles img{max-width:100%;max-height:70px;object-fit:contain}.ftiles .tile{border:2px dashed var(--navy)}
.ft2 .gdir{grid-template-columns:repeat(auto-fill,minmax(210px,1fr))}
.pg-head .eyebrow{color:var(--navy)}.pg-head{padding:48px 0 40px}.pg-head .wrap>*:last-child{margin-bottom:0}.pg-head h1{margin-bottom:.4em}
.sechead{margin-bottom:36px}
"""

MOBILE2 = """
@media(max-width:760px){
.focus li{padding:22px}.netband{padding:30px 24px}
body .filters label{flex:1 1 100%;min-width:0}body .filters select{width:100%;max-width:100%}
body .proj,body .vts,body .ftiles{display:flex;flex-wrap:wrap;justify-content:center;gap:16px}body .proj>*,body .vts>*{flex:1 1 100%}body .ftiles>*{flex:0 1 calc(50% - 8px)}
}
@media(max-width:520px){body .ftiles>*{flex-basis:100%}}
"""

JS2 = """
(function(){var b=document.querySelector('.tk-pause'),t=document.querySelector('.tk-in');if(b&&t){b.addEventListener('click',function(){var p=t.style.animationPlayState==='paused';t.style.animationPlayState=p?'running':'paused';b.textContent=p?'Pause':'Play';b.setAttribute('aria-pressed',String(!p))})}})();
"""


# ================================================================ Client request
def client():
    hero = f'''<div class="hero1"><div class="wrap"><div class="h1-panel g-panel"><h1>{HERO}</h1><p class="lede">{HERO_SUB}</p>
<p class="btnrow"><a class="btn btn-navy" href="#about">About</a></p></div>
<div class="h1-photo">{img("speaker", eager=True)}</div></div></div>{band()}'''
    home = f'''{hero}
<section class="sec"><div class="wrap grp"><div><h2>{hl(GROUPS_H)}</h2><p class="lede">{GROUPS_SUB}</p></div><div class="framed">{img("group")}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2 class="sechead">{hl("How we work", "t")}</h2><p class="how-intro">{HOW_INTRO}</p>{how_cards()}</div></section>
<section class="sec bk-navy-x" style="background:var(--navy);color:#fff"><div class="wrap"><h2 class="sechead" style="color:#fff">Our Impact</h2>{impact_block()}</div></section>
<section class="sec"><div class="wrap"><h2 class="sechead">{hl("What people say", "o")}</h2>{comments()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2 class="sechead">{hl("Our Focus")}</h2>{focus_rows()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="netband"><div><h2>Meet the groups across the region</h2><p>See who is in the network and where they work.</p></div><a class="btn btn-navy" href="#network">Visit the Network</a></div></div></section>'''
    network = f'''<div class="hero1"><div class="wrap"><div class="h1-panel g-panel"><h1>{NET_HERO}</h1><p class="lede">Community knowledge, lived experience and shared learning.</p></div>
<div class="h1-photo hvid" data-video="{VIMEO}">{img("speaker", eager=True)}<button class="play" aria-label="Play a group video, full screen (placeholder: the sizzle reel stands in)"><span aria-hidden="true">&#9654;</span></button><span class="vtag">Group video: placeholder</span></div></div></div>
<section class="sec"><div class="wrap"><h2 class="sechead">{hl("Our Network")}</h2>{B.map_embed()}<div class="card" style="margin-top:28px"><h3>All groups</h3>{directory2()}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2 class="sechead">{hl("Our Stories", "t")}</h2>{stories()}<div style="margin-top:28px">{comments()}</div></div></section>'''
    about = f'''<div class="pg-head bk-yellow-x" style="background:var(--yellow)"><div class="wrap"><span class="eyebrow">About us</span><h1>{ABOUT_H}</h1></div></div>
<section class="sec"><div class="wrap narrow">{"".join(f'<p class="lede" style="max-width:none">{E(p)}</p>' for p in ABOUT_P)}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2 class="sechead">{hl("Our Journey")}</h2>{htl_cards()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap two"><div class="vpx vpx-t"><h2>Vision</h2><p>{VISION}</p></div><div class="vpx vpx-y"><h2>Purpose</h2><p>{PURPOSE}</p></div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap">{comments()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap two"><div class="tcard2"><h2>{GOVERNANCE[0]}</h2><p>{GOVERNANCE[1]}</p></div><div class="tcard2">{steering()}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2 class="sechead">{hl("Resilience Alliance Team", "t")}</h2>{team_circles()}</div></section>'''
    impact = f'''<div class="pg-head" style="background:var(--yellow)"><div class="wrap"><span class="eyebrow">Impact</span><h1>Our Impact</h1><p class="lede">Led by Eunice’s work. Draft layout while the key highlights are gathered.</p></div></div>
<section class="sec"><div class="wrap">{impact_block()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2 class="sechead">{hl("What we are changing")}</h2>{from_to2()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2 class="sechead">{hl("Our projects", "t")}</h2>{projects_tiles()}<p class="vnote">Condensed from the three project one-pagers.</p></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2 class="sechead">{hl("Thanks to our funders", "o")}</h2>{funder_tiles()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap">{comments()}</div></section>'''
    menu = [("home", "Home"), ("network", "Network"), ("about", "About"), ("impact", "Impact")]
    body = "".join([screen("home", "Home", home), screen("network", "Network", network), screen("about", "About", about), screen("impact", "Impact", impact)])
    return shell("NRCRA Round 2: Client request", "", body, "client", nav2(menu, "Sign In", RACK_URL, True), footer2(menu, RACK_URL, True))


# ================================================================ Recommended (designer's wireframe)
CSS_W = """
body.recommended{--bg:#f3f6f7}
.recommended .card2{background:#fff;border-radius:32px;padding:44px}.recommended .sec{padding:28px 0}
.recommended .hero1{padding:28px 0 0}
.recommended .rband{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;list-style:none;margin:0;padding:0}.recommended .rband li{border-radius:28px;padding:30px 12px;text-align:center;font-weight:900;font-size:clamp(1.1rem,3vw,2rem);color:var(--navy)}
.recommended .how{gap:16px}
.recommended .impact-w{display:grid;grid-template-columns:1.1fr 1fr;gap:24px;align-items:center}.recommended .peach{background:var(--orange-12);border-radius:32px;padding:36px}.recommended .peach .big{background:transparent;padding:0;color:var(--navy)}.recommended .peach .big b{color:var(--orange-d)}
.recommended .peach .hi li{background:#fff}.recommended .impact{grid-template-columns:1fr}.recommended .impact .big span{font-size:1.2rem}
.recommended .focusg{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:16px;justify-content:center}.recommended .focusg li{flex:1 1 320px;max-width:380px;background:#fff;border-radius:20px 20px 28px 28px;overflow:hidden;color:var(--navy)}
.recommended .focusg li::before{content:"";display:block;height:14px;background:var(--fc)}.recommended .focusg h3{margin:22px 24px 10px;font-size:1.25rem}.recommended .focusg h3 span{display:inline-block;background:var(--fc);border-radius:12px;padding:.25em .7em}.recommended .focusg p{margin:0 24px 26px;font-size:1rem}
.recommended .fg-n h3 span{color:#fff}.recommended .fg-g{--fc:#9fb0b8}.recommended .fg-t{--fc:var(--teal)}.recommended .fg-y{--fc:var(--yellow)}.recommended .fg-o{--fc:var(--orange)}.recommended .fg-n{--fc:var(--navy)}
.partband{background:var(--yellow-40);padding:56px 0 52px;text-align:center}.partband h2{margin-bottom:6px}.partband .arrow{display:block;margin:0 auto 22px}
.pbsteps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,1fr);gap:20px}.pbsteps li{display:grid;justify-items:center;gap:8px}.pbsteps .ci{width:76px;height:76px;border-radius:50%;background:#fff;border:3px solid var(--ci);display:grid;place-items:center;color:var(--navy)}.pbsteps .ci .ico{width:34px;height:34px}.pbsteps a{font-weight:800;color:var(--navy)}.pbsteps p{margin:0;font-size:.95rem}
.pbsteps li:nth-child(1){--ci:var(--orange)}.pbsteps li:nth-child(2){--ci:var(--teal)}.pbsteps li:nth-child(3){--ci:var(--navy)}.pbsteps li:nth-child(4){--ci:var(--orange)}
@media(max-width:860px){.recommended .impact-w{grid-template-columns:1fr}.pbsteps{grid-template-columns:1fr 1fr}.recommended .card2{padding:28px 22px}}
.splith{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;padding:36px 0 12px}.splith>*{min-width:0}.splith .ph img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:32px}.splith .ph.vidph{position:relative;border-radius:32px;overflow:hidden}.splith .ph.vidph img{border-radius:0}
.splith.rev .ph{order:-1}@media(max-width:860px){.splith{grid-template-columns:1fr}.splith.rev .ph{order:0}}
.vp-wrap{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}.vp-wrap>*{min-width:0}.script{font:700 1.5rem Caveat,cursive;color:var(--orange-d);display:block;margin-bottom:2px}
.cluster{position:relative;aspect-ratio:1;max-width:460px;margin:0 auto;width:100%}.cluster img,.cluster i{position:absolute;border-radius:50%;object-fit:cover}.cluster .c1{width:62%;height:62%;left:0;top:6%;border:6px solid #fff;box-shadow:0 8px 24px -12px rgba(7,41,59,.5)}.cluster .c2{width:42%;height:42%;right:0;top:0;border:6px solid #fff}.cluster .c3{width:38%;height:38%;left:30%;bottom:0;border:6px solid #fff}
.cluster .b1{width:30%;height:30%;right:4%;bottom:6%;background:var(--yellow)}.cluster .b2{width:12%;height:12%;left:58%;top:52%;background:var(--orange)}
@media(max-width:860px){.vp-wrap{grid-template-columns:1fr}}
.htl2{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(5,1fr);gap:24px}.htl2 li{position:relative;padding-top:44px}.htl2 li::before{content:"";position:absolute;left:0;right:-24px;top:14px;height:4px;background:var(--teal-25);border-radius:2px}.htl2 li:last-child::before{right:0}
.htl2 li::after{content:"";position:absolute;left:0;top:0;width:32px;height:32px;border-radius:50%;background:#fff;border:8px solid var(--hc)}.htl2 .hy{background:none;color:var(--navy);padding:0;margin:0 0 8px;border-radius:0;font-size:1.3rem;display:block}.htl2 .he h3{font-size:1.05rem;margin:.6em 0 .3em}.htl2 .he:first-of-type h3{margin-top:0}.htl2 .he p{margin:0 0 .4em;font-size:.95rem}.htl2 li:nth-child(3n+2) .he:nth-child(2){margin-top:0}
.htl2 .hk0,.htl2 .hk3{--hc:var(--orange)}.htl2 .hk1{--hc:var(--teal)}.htl2 .hk2{--hc:var(--yellow)}.htl2 .hk4{--hc:var(--navy)}
@media(max-width:1100px){.htl2{grid-template-columns:repeat(3,1fr)}.htl2 li::before{right:-24px}}@media(max-width:760px){.htl2{grid-template-columns:1fr;gap:0}.htl2 li{padding:0 0 28px 52px}.htl2 li::before{left:15px;right:auto;top:30px;bottom:-4px;width:4px;height:auto}.htl2 li:last-child::before{display:none}}
.gdir-c{grid-template-columns:repeat(auto-fill,minmax(230px,1fr))!important;gap:18px!important}.gdir-c li{padding:0 0 16px!important;background:#fff!important;border:1px solid var(--line);border-radius:20px!important;overflow:hidden;position:relative}.gdir-c .gph{display:block;position:relative;margin-bottom:34px}.gdir-c .gph img{width:100%;height:110px;object-fit:cover}
.gdir-c .gdot{position:absolute;left:14px;bottom:-24px;width:48px;height:48px;border-radius:50%;background:var(--yellow);color:var(--navy);border:3px solid #fff;display:grid;place-items:center;font-weight:900}.gdir-c b,.gdir-c span:not(.gph):not(.gdot),.gdir-c em,.gdir-c small{margin:0 16px}.gdir-c small{color:var(--muted);margin-top:6px}
.rtiles{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.rtiles li{background:var(--grey-6);border-radius:20px;overflow:hidden;display:grid;grid-template-rows:auto 1fr auto}.rtiles img{width:100%;aspect-ratio:16/9;object-fit:cover}.rtiles div{padding:14px 18px 4px}.rtiles h3{margin:0 0 .2em;font-size:1.1rem}.rtiles p{margin:0;font-size:.95rem}.rtiles .btn{margin:12px 18px 18px}
@media(max-width:860px){.rtiles{grid-template-columns:1fr 1fr}}@media(max-width:520px){.rtiles{grid-template-columns:1fr}}
.ticker-w{position:relative}.tk-pause{position:absolute;right:12px;top:50%;transform:translateY(-50%);z-index:3;font:800 .8rem var(--font);background:#fff;color:var(--navy);border:0;border-radius:99px;padding:.4em .9em;min-height:32px;cursor:pointer}
.recommended .proj{margin-top:0}.recommended .ftiles{margin:0}
"""


def pb_steps():
    st = [("people", "Explore the network", "See who is in the Alliance and where they work.", "#network", "Visit the Network"), ("book", "Read our story", "How the Alliance began and where it is heading.", "#about", "About us"),
          ("share", "See our impact", "What we are changing and who made it possible.", "#impact", "Our Impact"), ("hand", "Sign in to the R.A.C.K", "Find what already works, and add what you know.", "#rack", "The R.A.C.K")]
    return '<ol class="pbsteps">' + "".join(f'<li><span class="ci">{icon(i)}</span><b>{E(t)}</b><p>{E(d)}</p><a href="{h}">{E(l)}</a></li>' for i, t, d, h, l in st) + "</ol>"


def part_band():
    return f'<section class="partband"><div class="wrap"><h2>How you can be part of it</h2>{pb_steps()}</div></section>'


def focus_cards():
    cl = {"t": "fg-t", "y": "fg-y", "o": "fg-o", "n": "fg-n", "g": "fg-g"}
    return '<ol class="focusg">' + "".join(f'<li class="{cl[c]}"><h3><span>{E(t)}</span></h3><p>{E(d)}</p></li>' for t, d, c in FOCUS) + "</ol>"


def ticker_w():
    words = ["60+ groups", "One region", "One network"]
    inner = "".join(f'<span>{w}</span><b class="tkd">&#9679;</b>' for w in words * 6)
    return f'<div class="ticker-w"><div class="ticker" aria-hidden="true"><div class="tk-in">{inner}</div></div><button type="button" class="tk-pause" aria-pressed="false">Pause</button></div>'


def recommended():
    hero = f'''<div class="hero1"><div class="wrap"><div class="h1-panel g-panel"><h1>{HERO}</h1><p class="lede">{HERO_SUB}</p><p class="btnrow"><a class="btn btn-navy" href="#about">About</a></p></div>
<div class="h1-photo">{img("speaker", eager=True)}</div></div></div>'''
    home = f'''{hero}
<section class="sec"><div class="wrap"><ul class="rband"><li class="cs-t">Connect</li><li class="cs-y">Share</li><li class="cs-o">Care</li></ul></div></section>
<section class="sec"><div class="wrap"><div class="card2 grp"><div><h2>{hl(GROUPS_H)}</h2><p class="lede">{GROUPS_SUB}</p></div><div class="framed fr-y">{img("group")}</div></div></div></section>
<section class="sec"><div class="wrap"><div class="card2"><h2 class="sechead">{hl("How we work", "t")}</h2><p class="how-intro">{HOW_INTRO}</p>{how_cards()}</div></div></section>
<section class="sec"><div class="wrap impact-w"><div class="peach"><h2>Our Impact</h2>{impact_block()}</div><div class="framed fr-y">{img("cheer")}</div></div></section>
<section class="sec"><div class="wrap"><div class="card2"><h2 class="sechead">{hl("What people say", "o")}</h2>{comments()}</div></div></section>
<section class="sec"><div class="wrap"><h2 class="sechead">{hl("Our Focus")}</h2>{focus_cards()}<p class="btnrow" style="justify-content:center"><a class="btn btn-navy" href="#network">Visit the Network</a></p></div></section>
{part_band()}'''
    about = f'''<div class="wrap"><div class="splith rev"><div class="ph">{img("line", eager=True)}</div><div><span class="eyebrow">About us</span><h1>{ABOUT_H}</h1><p class="lede">{E(ABOUT_P[0])}</p></div></div></div>
<section class="sec"><div class="wrap"><div class="card2 two"><p style="margin:0">{E(ABOUT_P[1])}</p><p style="margin:0">{E(ABOUT_P[2])}</p></div></div></section>
<section class="sec"><div class="wrap card2 vp-wrap"><div><span class="script">Our goal</span><h2>Vision</h2><p>{VISION}</p><span class="script" style="margin-top:28px">Our why</span><h2>Purpose</h2><p>{PURPOSE}</p></div>
<div class="cluster">{img("circle", "c1", alt="")}{img("house", "c2", alt="")}{img("talk", "c3", alt="")}<i class="b1" aria-hidden="true"></i><i class="b2" aria-hidden="true"></i></div></div></section>
<section class="sec"><div class="wrap"><div class="card2"><span class="script">Progress so far</span><h2 class="sechead">Our Journey</h2>{htl_cards().replace('class="htl"', 'class="htl2"')}</div></div></section>
<section class="sec"><div class="wrap">{comments()}</div></section>
<section class="sec"><div class="wrap two"><div class="tcard2"><h2>{GOVERNANCE[0]}</h2><p>{GOVERNANCE[1]}</p></div><div class="tcard2">{steering()}</div></div></section>
<section class="sec"><div class="wrap"><div class="card2"><h2 class="sechead">Resilience Alliance Team</h2>{team_circles()}</div></div></section>
{part_band()}'''
    impact = f'''<div class="wrap"><div class="pg-head" style="padding-bottom:12px"><span class="eyebrow">Impact</span><h1>Our Impact</h1><p class="lede">Led by Eunice’s work. Draft layout while the key highlights are gathered.</p></div></div>
<section class="sec"><div class="wrap impact-w"><div class="peach"><h2>At a glance</h2>{impact_block()}</div><div class="framed fr-y">{img("cheer")}</div></div></section>
<section class="sec"><div class="wrap"><div class="card2"><h2 class="sechead">Thanks to our funders</h2>{funder_tiles()}</div></div></section>
<section class="sec"><div class="wrap"><h2 class="sechead">Our projects</h2>{projects_tiles()}</div></section>
<section class="sec"><div class="wrap"><div class="card2"><h2 class="sechead">What we are changing</h2>{from_to2()}</div></div></section>
<section class="sec"><div class="wrap">{comments()}</div></section>
{part_band()}'''
    network = f'''<div class="wrap"><div class="splith"><div><span class="eyebrow">Network</span><h1>{NET_HERO}</h1><p class="lede">Community knowledge, lived experience and shared learning.</p></div>
<div class="ph vidph hvid" data-video="{VIMEO}">{img("speaker", eager=True)}<button class="play" aria-label="Play a group video, full screen (placeholder: the sizzle reel stands in)"><span aria-hidden="true">&#9654;</span></button><span class="vtag">Group video: placeholder</span></div></div></div>
<section class="sec"><div class="wrap"><div class="card2"><h2 class="sechead">Our Network</h2>{B.map_embed()}</div></div></section>
<section class="sec"><div class="wrap"><div class="card2 ft2"><h2 class="sechead">All groups</h2>{directory2(True)}</div></div></section>
<section class="sec"><div class="wrap"><div class="card2"><h2 class="sechead">Our Stories</h2>{stories()}<div style="margin-top:28px">{comments()}</div></div></div></section>
{part_band()}'''
    rack = f'''<div class="wrap"><div class="splith"><div><span class="eyebrow">Resources</span><h1>The R.A.C.K</h1><p class="lede"><b>Resilience Alliance Community Knowledge.</b> One shared place where the whole network can find what already works from years of real community experience across the Northern Rivers.</p><p>Access is for Alliance groups. Contact the Network Lead to get set up.</p>
<p class="btnrow"><a class="btn btn-primary" href="{RACK_URL}" target="_blank" rel="noopener">Sign in</a><a class="btn btn-ghost" href="mailto:{CONTACT["email"]}?subject=R.A.C.K%20access">Request access</a><a class="btn btn-ghost" href="mailto:{HELLO}?subject=R.A.C.K%20help">Get help</a></p></div><div class="ph">{img("table", eager=True)}</div></div></div>
<section class="sec"><div class="wrap"><div class="card2"><span class="eyebrow">Resource library</span><h2 class="sechead">What you’ll find</h2><p>Find templates and guides you can use straight away, and contribute knowledge back in two minutes.</p>
<ul class="rtiles">{"".join(f'<li>{img(p, alt="")}<div><h3>{E(t)}</h3><p>{E(d)}</p></div><a class="btn btn-ghost" href="{RACK_URL}" target="_blank" rel="noopener">Open in the R.A.C.K</a></li>' for t, d, p in RES)}</ul></div></div></section>
{part_band()}'''
    menu = [("home", "Home"), ("about", "About"), ("impact", "Impact"), ("network", "Network")]
    body = "".join([screen("home", "Home", home), screen("about", "About", about), screen("impact", "Impact", impact), screen("network", "Network", network), screen("rack", "R.A.C.K", rack)])
    foot = footer2(menu, "#rack", False)
    return shell("NRCRA Round 2: Recommended", CSS_W, body, "recommended", nav2(menu, "R.A.C.K sign in", "#rack"), foot, pre_footer=ticker_w())


# ================================================================ accessibility notes
def _lum(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])


def ratio(a, b):
    la, lb = _lum(a), _lum(b)
    if la < lb:
        la, lb = lb, la
    return (la + 0.05) / (lb + 0.05)


def sw(fg, bg, label, big=False, extra=""):
    r = ratio(fg, bg)
    need = 3 if big else 4.5
    ok = r >= need
    return f'<figure class="sw {"ok" if ok else "bad"}"><div class="sample" style="color:{fg};background:{bg};{"font-size:1.7rem;font-weight:900" if big else "font-size:1rem"}">{E(label)}</div><figcaption><b>{r:.2f}:1</b> {"passes" if ok else "fails"} AA ({"large text, needs 3:1" if big else "needs 4.5:1"}). {E(extra)}</figcaption></figure>'


NAVY, TEAL, ORANGE, YELLOW, WHITE, TEALD, ORANGED = "#07293b", "#00a79d", "#f05a28", "#ffcb2a", "#ffffff", "#00615a", "#b93a0c"


def accessibility():
    items = []

    def item(n, title, why, body, fix):
        items.append(f'<article class="issue"><h2><span class="n">{n}</span>{E(title)}</h2><p>{why}</p><div class="swrow">{body}</div><p class="fix"><b>What the Round 2 builds do:</b> {fix}</p></article>')
    item(1, "White text on brand green", "The feedback asks for the hero and footer blocks in brand green. White text on that green (#00a79d) is below the minimum.",
         sw(WHITE, TEAL, "We believe when climate disasters hit") + sw(NAVY, TEAL, "We believe when climate disasters hit"),
         "Uses navy text on the green hero and footer (5.05:1). If white text on green is a must, the green has to be the darker #00615a, which is not a brand colour.")
    item(2, "White text on the Connect, Share, Care band", "The three project one-pagers put white text on teal, yellow and orange. White on teal and on yellow fails even as large text, and white on yellow is almost unreadable. White on orange only scrapes through because the words are large.",
         f'<img class="ref" src="../assets/refs/pdf-band.png" alt="Crop of the project one-pager: a teal, yellow and orange band with white words Connect, Share and Care.">' + sw(WHITE, TEAL, "Connect", True) + sw(WHITE, YELLOW, "Share", True) + sw(WHITE, ORANGE, "Care", True),
         "The band uses navy words, bold and large. Navy on orange is 4.46:1, which is under 4.5:1, so it only passes as large text. Body copy on solid orange is set bold and at least 19px to qualify, or sits on a white or tinted panel.")
    item(3, "Brand orange and teal as heading colours", "The one-pagers colour headings in bright orange on peach and teal on mint. Teal on mint fails even as large text. Orange on peach scrapes through at about 3.1:1 only because the headings are large, so any smaller use fails.",
         f'<img class="ref" src="../assets/refs/pdf-headings.png" alt="Crop of the project one-pager: headings in orange on peach and teal on mint.">' + sw(ORANGE, "#fdf3ec", "RESILIENCE & PREPAREDNESS", True) + sw(TEAL, "#f2f9f9", "MITIGATION & PREVENTION", True),
         "Strong brand colour is used as a highlight behind navy text (marker bars and pill labels), not as the text colour. Where a coloured heading is wanted, the dark versions work: #b93a0c on white is " + f"{ratio(ORANGED, WHITE):.1f}:1 and #00615a on white is {ratio(TEALD, WHITE):.1f}:1.")
    item(4, "Connect. Share. Care. in the tagline colours", "The sampled tagline colours are all well under the minimum on white. Logotypes are exempt from the rule, but the client has said this is not a tagline, so the words behave as ordinary text.",
         sw("#58b0ac", WHITE, "Connect.", True) + sw("#d8b044", WHITE, "Share.", True) + sw("#e47848", WHITE, "Care.", True),
         "The tagline is removed from the footer. The words appear only in the navy-on-colour band.")
    item(5, "Highlights and white text do not mix", "A marker highlight is safe behind navy text. If someone later sets that title in white, the half of the word over the bar fails.",
         sw(NAVY, YELLOW, "Our Focus", True) + sw(NAVY, TEAL, "How we work", True) + sw(NAVY, ORANGE, "What people say", True) + sw(WHITE, YELLOW, "Our Focus", True),
         "Highlights are only used on light backgrounds with navy text. On navy sections the title is plain white with no bar.")
    item(6, "Focus ring on brand green", "The site uses a dark orange focus ring. On the green hero panel and footer that ring is almost invisible, which fails the 3:1 rule for focus indicators.",
         sw(ORANGED, TEAL, "Focus ring colour", True, "Needs 3:1 against the green.") + sw(NAVY, TEAL, "Focus ring colour", True, "Navy ring used on green."),
         "The green hero panel, the Visit the Network band and the footer switch to a navy focus ring.")
    item(7, "Yellow and orange icons on pale tints", "Meaningful icons need 3:1 against their background. The Round 1 yellow and grey pillar icons on cream and grey are under that.",
         sw(YELLOW, "#fff5d4", "Yellow icon on cream", True) + sw("#9fb0b8", "#eef1f3", "Grey icon on grey", True),
         "The feedback removes the symbols from How we work and Our Focus, so this is settled. The few icons that remain (the part-of-it steps in Recommended) are navy.")
    item(8, "Scrolling ticker", "Moving text that starts by itself and lasts more than five seconds needs a way to pause it (WCAG 2.2.2). Round 1 Prototype 1 has the ticker with no control.",
         '<p class="plain-note">The Round 1 ticker above the footer has no pause control.</p>',
         "The Client request build has no ticker. The Recommended build keeps one, with a Pause button and no motion for people who ask their device for less. Round 1 Prototype 1 should be fixed the same way if it is used.")
    item(9, "Videos need captions, a transcript and audio description", "The sizzle reel and the group story videos cannot be checked from here. AA needs captions (1.2.2) and audio description or a text alternative (1.2.5) for recorded video.",
         '<p class="plain-note">Placeholder videos only. The play buttons open the Vimeo sizzle reel full screen.</p>',
         "Ask for captioned files, or turn captions on in Vimeo, and put a transcript link under each video. The play button has a text label, and Escape closes the player.")
    item(10, "Maps and logos", "The Google Map embed cannot be explored by keyboard or screen reader. Funder and partner logos are exempt from the contrast rule but still need alt text. The Federal and State Government logos are not supplied yet.",
         '<p class="plain-note">Map plus list on the Network page. Logos have alt text. Government logos are marked "logo to be added".</p>',
         "The group list and its filters sit next to the map, so the information is not map-only. Add the government logos once the protocol files arrive.")
    item(11, "Wix Classic build risks", "Wix Classic positions elements by pixel, so these cannot be proved in a prototype: text boxes that overlap when text is enlarged or spacing is changed (1.4.4, 1.4.12), a reading order that follows the visual order (1.3.2), and a separate mobile layout (1.4.10).",
         '<p class="plain-note">Build checks, not visual fails.</p>',
         "Use strips and boxes that grow with their text instead of fixed-height text boxes, reorder the tab order in the editor, and check the mobile editor at 320px and with browser zoom at 200%.")
    passed = [(NAVY, WHITE, "Body text on white"), (NAVY, "#bfe9e7", "Text on teal tint"), (NAVY, "#ffeaaa", "Text on yellow tint"), (NAVY, "#fbd6c9", "Text on orange tint"), (WHITE, NAVY, "White on navy"), (YELLOW, NAVY, "Yellow on navy"), (NAVY, TEAL, "Navy on brand green"), (NAVY, YELLOW, "Navy on brand yellow"), (TEALD, WHITE, "Dark teal links on white"), (ORANGED, WHITE, "Dark orange on white")]
    plist = "".join(f'<li><span class="chip" style="color:{f};background:{b}">Aa</span><span>{E(l)}</span><b>{ratio(f, b):.2f}:1</b></li>' for f, b, l in passed)
    return f'''<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NRCRA accessibility notes</title><meta name="robots" content="noindex">{FONT}
<style>{BASE}body{{background:#f3f6f7}}main{{max-width:1000px;margin:0 auto;padding:36px 20px 40px}}
.top .flag{{display:inline-block;background:#111;color:#ffcb2a;font-weight:900;letter-spacing:.06em;border-radius:99px;padding:.35em 1em;font-size:.85rem;margin-bottom:14px}}.top .flag a{{color:#fff}}
.issue{{background:#fff;border-radius:28px;padding:30px;margin:0 0 22px}}.issue h2{{display:flex;gap:14px;align-items:center;font-size:1.5rem}}.n{{flex:none;width:40px;height:40px;border-radius:50%;background:var(--navy);color:#fff;display:grid;place-items:center;font-size:1.1rem}}
.swrow{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:18px 0}}.sw{{margin:0;border-radius:16px;overflow:hidden;border:2px solid var(--line)}}.sw.bad{{border-color:#b3261e}}.sw.ok{{border-color:#1f7a3a}}
.sample{{padding:22px 16px;font-weight:800}}.sw figcaption{{padding:10px 14px;font-size:.9rem;background:#fff}}.sw.bad figcaption b{{color:#b3261e}}.sw.ok figcaption b{{color:#1f7a3a}}
.ref{{grid-column:1/-1;width:100%;max-width:560px;border:1px solid var(--line);border-radius:12px}}.fix{{background:var(--teal-12);border-radius:14px;padding:14px 18px;margin:0}}.plain-note{{margin:0;font-weight:700}}
.pass{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:10px}}.pass li{{display:flex;align-items:center;gap:12px;background:#fff;border-radius:14px;padding:10px 14px;border:1px solid var(--line)}}.chip{{flex:none;width:48px;height:36px;border-radius:8px;display:grid;place-items:center;font-weight:900}}.pass b{{margin-left:auto}}
.protobar{{position:fixed}}</style></head>
<body><main><div class="top"><span class="flag">MOCKUP &amp; PROTOTYPE ONLY &middot; by <a href="https://veemercado.com">veemercado.com</a></span><br><h1>Where the requested design does not meet AA</h1>
<p class="lede">Notes on the experience the client asked for, checked against WCAG 2.2 level AA. Each card shows the combination, its measured contrast ratio and what the Round 2 builds do instead. Ratios use the WCAG formula: 4.5:1 for normal text, 3:1 for large text (24px, or bold from about 19px) and for icons and focus rings.</p>
<p class="btnrow"><a class="btn btn-primary" href="../client/">Client request</a><a class="btn btn-ghost" href="../recommended/">Recommended</a><a class="btn btn-ghost" href="../#round-2">All prototypes</a></p></div>
<div style="margin-top:28px">{"".join(items)}</div>
<section class="issue"><h2>Combinations that pass</h2><p>Safe pairs from the brand palette, used across both builds.</p><ul class="pass">{plist}</ul></section>
<section class="issue"><h2>Still open</h2><ul><li>Real text and colour contrast should be re-checked in Wix once built. Wix does not check it for you.</li><li>The Federal and State Government logos, and the logo protocols, are still to come.</li><li>Group story and sizzle reel videos need captions, a transcript and audio description.</li><li>The Round 1 and Round 2 pages use sample groups and placeholder impact highlights.</li></ul></section></main></body></html>'''


def main():
    B.write("client/index.html", client())
    B.write("recommended/index.html", recommended())
    B.write("accessibility/index.html", accessibility())
