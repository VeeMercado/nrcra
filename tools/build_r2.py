"""Round 2: Prototype 1 duplicated, with only the changes from the client's feedback document applied.

Feedback document: https://docs.google.com/document/d/1NaC61OZYomUhRGzN3M5WOgimnBq-7E3khqsOiFFaZfQ/edit?usp=sharing
Everything not mentioned in the document is left exactly as it is in Prototype 1 (build.v1).
Imported by build.py, which owns the shared helpers, base CSS and the dashboard.
"""
import build as B
from build import E, img, logo, screen, LINKS, RACK_URL, ACK, ABORIGINAL_FLAG, FLAG, LOGO_DOTS, BASE, MOBILE, JS, FONT, CSS1, VIMEO, CONTACT

FUND = "../assets/funders/"
HELLO = "hello@nrcra.org.au"

# ---------------------------------------------------------------- content, in the client's words
HERO = "We believe when climate disasters hit, it’s the community that steps up first."
HERO_SUB = "We are a network of grassroots, community-led groups working together to build disaster resilience across the Northern Rivers."
HOW_INTRO = "Through regular gatherings, deep conversations and shared experiences, the Resilience Alliance is building a community-led network focused on collective care, preparedness and regional strength."
HOW = [
    ("Connect", "60+ grassroots, community-led groups are connected together across the region so they can build trusting relationships with each other so they know who to contact when the next climate disaster hits.", "teal"),
    ("Share", "Sharing knowledge, experience, practical tools and resources across the network so everyone can benefit from what others have learned.", "yellow"),
    ("Care", "Peer to peer support, reducing the load, removing duplication and placing a real value on the efforts of all.", "orange"),
]
FOCUS = [
    ("Growing the Alliance", "We are strengthening our network by clarifying who we are, why we come together and how we work. Through regular gatherings we are building a clearer picture of who is involved and how we connect."),
    ("Training and Resource Sharing", "We are making knowledge, practical tools and training easier to find through our Resilience Alliance Community Knowledge Hub. Our training is led by experienced locals, with the aim of strengthening our network from within the community."),
    ("Peer Support and Self Care", "Resilience work asks a lot of the people who do it, so we are committed to balanced wellbeing and collective care across our region. We are mapping the support already available, identifying good practice, with the aim to develop an adaptable wellbeing framework that groups can use to look after themselves and each other."),
    ("Funding and Collaborative Projects", "We are working towards a more sustainable and collaborative approach to funding for resilience work across the region. Identifying shared opportunities we aim to reduce competition and increase collective impact."),
    ("Advocacy", "We believe our collective voice is stronger than any single group’s. By understanding our own network, identifying key stakeholders and building advocacy skills among members, we are developing a collaborative approach to advocating for resilient communities across the region."),
]
ABOUT_H = "We know communities are stronger when they’ve built trusted relationships together."
ABOUT_P = [
    "The Resilience Alliance was established in November 2023. Its roots lie in a run of compounding disasters: the 2017 floods, the 2019–20 bushfires, and the catastrophic floods and landslides of 2022. In each, local community organisers played a vital role in response, recovery and adaptation. Research in the years that followed found that these grassroots groups wanted stronger connections with each other for peer-to-peer support. That showed the need for regional collaboration in disaster resilience.",
    "The Resilience Alliance supports a network of place-based resilience groups to develop their own local approaches to risk reduction, preparedness and recovery, for fire, flood, landslides and whatever comes next.",
    "The Resilience Alliance helps government agencies, councils and emergency services deliver on the commitments of the NSW State Emergency Management Plan, State Disaster Mitigation Plan and regional resilience priorities by connecting formal systems with trusted, community-led action.",
]
VISION = B.VISION
PURPOSE = "To develop a self-sustaining, trusted Alliance of place-based, community-led resilience groups and organisations. The Alliance will share knowledge and resources; provide mutual support and wellbeing; take collective action, and advocate for identified community needs."
JOURNEY = [
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
TEAM = [("Network Lead", "Kathie Heyman"), ("Communications, Events and Engagement", "Milou Muiser"), ("Capacity Building Coordinators", "Marlena Sue Basser, Claire McLisky, Barbara Winters")]
NET_HERO = "60+ groups, one region, one network."
COMMENTS_NOTE = "More positive comments from the gathering data will go here, supplied by NRCRA."
FOCUS_NAMES = [f[0] for f in FOCUS]
FOCUS_GROUPS = {FOCUS_NAMES[i]: gs for i, gs in enumerate(B.PILLAR_GROUPS.values())}
GATHER = ("27 Nov", "Alliance Gathering", B.GATHER[2])
DOTS_W = '<svg class="dots" viewBox="0 0 48 40" aria-hidden="true"><circle cx="24" cy="9" r="8" fill="#fff"/><circle cx="9" cy="28" r="6.5" fill="#fff"/><circle cx="39" cy="28" r="6.5" fill="#fff"/></svg>'

MENU = [("home", "Home"), ("network", "Network"), ("about", "About"), ("impact", "Impact")]


# ---------------------------------------------------------------- page furniture
def funders_strip():
    ph = lambda n: f'<li class="fund-ph">{n}<small>logo to be added</small></li>'
    logos = "".join(f'<li><img src="{FUND}{f}" alt="{E(n)}" height="34"></li>' for f, n in [("help.png", "NRMA Insurance, a Help Company"), ("frrr.png", "Foundation for Rural and Regional Renewal"), ("ucrh.png", "University Centre for Rural Health")])
    return f'<div class="fund"><div class="wrap"><p class="fund-t">Thanks to our funders</p><ul>{ph("Federal Government")}{ph("State Government")}{logos}</ul></div></div>'


def nav2():
    links = "".join(f'<a href="#{k}" data-nav="{k}">{E(t)}</a>' for k, t in MENU)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap head-in">
<a href="#home" class="brand" aria-label="NRCRA home">{logo()}</a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav id="nav" aria-label="Main">{links}<a class="btn btn-cta" href="#rack" data-nav="rack">Sign In</a></nav></div></header>'''


def footer2():
    def col(t, items):
        return f'<div class="fcol"><h2>{t}</h2><ul class="flist">' + "".join(f'<li><a href="{u}">{E(n)}</a></li>' for n, u in items) + "</ul></div>"
    menu = [(t, f"#{k}") for k, t in MENU] + [("Sign In", "#rack")]
    return f'''<footer class="site-foot"><div class="wrap"><div class="foot-cols">
<div class="foot-top"><span class="foot-logo boxed">{logo("logo")}</span></div>
{col("Contact", [(HELLO, f"mailto:{HELLO}")])}{col("Stay in touch", [("Facebook", LINKS["fb"]), ("LinkedIn", LINKS["li"])])}{col("Menu", menu)}</div>
<div class="ack">{ABORIGINAL_FLAG}<p>{ACK}</p></div><p class="copy">© 2026 Northern Rivers Community Resilience Alliance &middot; <a href="https://www.nrcra.org.au/copy-of-terms-conditions">Privacy Policy</a></p></div></footer>'''


def protobar2():
    return '''<div class="protobar" role="region" aria-label="Prototype controls"><div class="pb-in">
<p class="pb-label"><b>MOCKUP &amp; PROTOTYPE ONLY</b> by <a href="https://veemercado.com">veemercado.com</a><span class="pb-cur"> &middot; viewing Round 2: Client request</span></p>
<nav class="pb-nav" aria-label="Prototypes"><a class="pb-btn pb-all" href="../#round-2">All prototypes</a><a class="pb-btn" data-proto="v1" href="../v1/" aria-label="Prototype 1 before the changes"><span class="pb-short" aria-hidden="true">P1</span><span class="pb-long">Prototype 1</span></a></nav>
<button type="button" class="pb-top" aria-label="Back to top" onclick="window.scrollTo({top:0,behavior:'smooth'})"><span class="pb-long">Back to top&nbsp;</span><span aria-hidden="true">&uarr;</span></button></div></div>'''


CSS2 = """
.fund{background:#fff;border-bottom:1px solid var(--line)}.fund .wrap{display:flex;align-items:center;gap:8px 24px;flex-wrap:wrap;padding-top:10px;padding-bottom:10px}
.fund-t{margin:0;font-weight:800;font-size:.9rem;white-space:nowrap}.fund ul{list-style:none;margin:0;padding:0;display:flex;align-items:center;gap:8px 24px;flex-wrap:wrap}
.fund img{height:34px;width:auto;max-width:150px;object-fit:contain}
.fund-ph{border:2px dashed var(--navy);border-radius:10px;padding:.25em .8em;font-weight:800;font-size:.85rem;line-height:1.15}.fund-ph small{display:block;font-weight:600;font-size:.75rem}
.site-foot{--foot:var(--teal);--foot-ink:var(--navy);--foot-h:var(--navy);--foot-line:rgba(7,41,59,.4)}.site-foot a{text-decoration:underline}.site-foot :focus-visible{outline-color:var(--navy)}.site-foot .foot-logo.boxed{max-width:260px}
.g-panel{background:var(--teal)!important;color:var(--navy)}.g-panel h1,.g-panel .eyebrow{color:var(--navy)}.g-panel .lede{margin:0}.g-panel :focus-visible{outline-color:var(--navy)}
.cs3{list-style:none;margin:20px 0 0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);border-radius:20px;overflow:hidden}
.cs3 li{padding:22px 10px;text-align:center;font-weight:900;font-size:clamp(1.15rem,3vw,2rem);color:var(--navy)}.cs3 li:nth-child(1){background:var(--teal)}.cs3 li:nth-child(2){background:var(--yellow)}.cs3 li:nth-child(3){background:var(--orange)}
.callcard.orange{background:var(--orange)}.callcard.orange::after{background:var(--yellow)}.callcard.orange blockquote{color:var(--navy)}
.how-intro{max-width:70ch;margin:0 0 28px}
.val-teal{background:var(--teal)}.val-yellow{background:var(--yellow)}.val-orange{background:var(--orange)}.val .dots{width:56px;height:48px;display:block;margin:0 0 18px}.val-orange p{font-weight:700;font-size:1.18rem}
.v1 .focusrows{grid-template-columns:1fr;gap:16px}.v1 .focusrows .pc{display:grid;grid-template-columns:minmax(220px,300px) 1fr;gap:6px 36px;align-items:start;text-align:left;border-radius:12px 12px 6px 6px;padding:0 28px 28px}
.v1 .focusrows .pc::before{grid-column:1/-1}.focusrows .pc h3{min-height:0;display:block;margin:0}.focusrows .pc p{font-size:1.05rem}
@media(max-width:760px){.v1 .focusrows .pc{grid-template-columns:1fr;padding:0 20px 24px}}
.stat-card .stats{grid-template-columns:1fr}.stat-card h2{margin-bottom:.4em}
.pg1 .ph.hvid{position:relative;cursor:pointer}.pg1 .ph .play{width:84px;height:84px}
.about-p p{max-width:none}
.htr{list-style:none;margin:56px 0 0;padding:0;display:grid;grid-template-columns:repeat(5,1fr);gap:18px;position:relative}
.htr::before{content:"";position:absolute;left:10%;right:10%;top:46px;border-top:4px dotted rgba(7,41,59,.55)}
.htr li{position:relative;display:flex;flex-direction:column;align-items:center;gap:16px}
.hstop{position:relative;z-index:2;width:92px;height:92px;border-radius:50%;display:grid;place-items:center;background:#fff;border:6px solid var(--bc);font-weight:900;font-size:1.2rem}
.htr li:nth-child(1){--bc:var(--teal)}.htr li:nth-child(2){--bc:var(--yellow)}.htr li:nth-child(3){--bc:var(--orange)}.htr li:nth-child(4){--bc:var(--navy)}.htr li:nth-child(5){--bc:var(--teal-d)}
.htr .tdeco{left:calc(50% + 38px);top:-14px}.htr .tcard{display:block;width:100%;height:100%}.htr .he+.he{margin-top:16px;padding-top:14px;border-top:2px solid var(--line)}
.htr h3{font-size:1.05rem;margin:0 0 .3em}.htr .he p{margin:0 0 .4em;font-size:.95rem}.htr .fnote{font-style:italic}
@media(max-width:1100px){.htr{grid-template-columns:repeat(3,1fr);row-gap:40px}.htr::before{display:none}}@media(max-width:700px){.htr{grid-template-columns:1fr}}
.two{display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:start}.two>*{min-width:0}@media(max-width:860px){.two{grid-template-columns:1fr}}
.chips{list-style:none;margin:0 0 1em;padding:0;display:flex;flex-wrap:wrap;gap:10px}.chips li{background:var(--teal-12);border-radius:99px;padding:.4em 1em;font-weight:700}
.team dl{margin:0}.team dt{font-weight:800}.team dd{margin:0 0 .8em}
.cmts{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1.4fr 1fr;gap:20px}.cm-q,.cm-ph{border-radius:var(--r);padding:30px}.cm-q{background:var(--yellow-40)}.cm-q blockquote{margin:0}.cm-q p{font-size:clamp(1.3rem,2.6vw,1.8rem);font-weight:800;line-height:1.35;margin:0}.cm-q cite{display:block;font-style:normal;font-weight:700;margin-top:.8em}
.cm-ph{border:2px dashed var(--navy);background:#fff;display:grid;align-items:center}.cm-ph p{margin:0;font-weight:700}@media(max-width:760px){.cmts{grid-template-columns:1fr}}
.vts{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.vt{position:relative;aspect-ratio:16/10;border-radius:var(--r);overflow:hidden;background:var(--navy);cursor:pointer}.vt img{width:100%;height:100%;object-fit:cover}.vt .play{width:68px;height:68px}
@media(max-width:760px){.vts{grid-template-columns:1fr}}
.sechead{margin-bottom:28px}
"""

MOBILE2 = """
@media(max-width:760px){body .filters label{flex:1 1 100%;min-width:0}body .filters select{width:100%;max-width:100%}body .vts{display:flex;flex-wrap:wrap}body .vts>*{flex:1 1 100%}}
"""


# ---------------------------------------------------------------- components
def band():
    return '<ul class="cs3"><li>Connect</li><li>Share</li><li>Care</li></ul>'


def how_cards():
    return '<ul class="values">' + "".join(f'<li class="val val-{c}">{DOTS_W}<h3>{t}</h3><p>{E(d)}</p></li>' for t, d, c in HOW) + "</ul>"


def focus_rows():
    return '<ol class="pcols focusrows">' + "".join(f'<li class="pc"><h3>{E(t)}</h3><p>{E(d)}</p></li>' for t, d in FOCUS) + "</ol>"


def comments():
    q = B.QUOTE
    return f'<ul class="cmts"><li class="cm-q"><blockquote><p>&ldquo;{q[0]}&rdquo;</p><cite>{q[1]}</cite></blockquote></li><li class="cm-ph"><p>{COMMENTS_NOTE}</p></li></ul>'


def htrail():
    out = '<ol class="htr">'
    for i, (y, es) in enumerate(JOURNEY):
        art = FLAG if i % 2 == 0 else LOGO_DOTS
        body = "".join(f'<div class="he"><h3>{E(t)}</h3><p>{E(d)}</p>' + (f'<p class="fnote">{E(f)}</p>' if f else "") + "</div>" for t, d, f in es)
        out += f'<li><span class="hstop">{y}</span><span class="tdeco">{art}</span><div class="tcard">{body}</div></li>'
    return out + "</ol>"


def stories():
    t = lambda p: f'<li class="vt" data-video="{VIMEO}">{img(p, alt="")}<button class="play" aria-label="Play video: group story (placeholder, the sizzle reel stands in)"><span aria-hidden="true">&#9654;</span></button><span class="vtag">Group story: video to come</span></li>'
    return f'<ul class="vts">{t("crowd")}{t("laughing")}{t("listening")}</ul><p class="vnote">Videos of groups from the gathering will sit here. The sizzle reel stands in until they are supplied.</p>'


def directory2():
    items = "".join(f'<li data-lga="{l}" data-pillar="{E(p)}"><b>{E(n)}</b><span>{a}, {l}</span><em>{E(p)}</em></li>' for p, gs in FOCUS_GROUPS.items() for n, a, l in gs)
    lopts = "".join(f"<option>{l}</option>" for l in B.LGAS)
    popts = "".join(f"<option>{E(p)}</option>" for p in FOCUS_NAMES)
    return f'''<div class="dir"><div class="filters">
<label>Location <select data-f="lga"><option value="">All locations</option>{lopts}</select></label>
<label>Focus <select data-f="pillar"><option value="">All areas of focus</option>{popts}</select></label>
<label class="dq">Search <input type="search" data-f="q" placeholder="Group name or town"></label></div>
<ul class="gdir">{items}</ul><p class="empty" hidden>No groups match those filters.</p><p class="vnote">Sample groups. In the build, one Google Sheet of groups drives both the map pins and this list, so updating a row updates both.</p></div>'''


# ---------------------------------------------------------------- Prototype 1, with the document's changes
def client():
    home = f'''<div class="hero1"><div class="wrap"><div class="h1-panel g-panel"><span class="eyebrow">Northern Rivers Community Resilience Alliance</span>
<h1>{HERO}</h1><p class="lede">{HERO_SUB}</p>
<p class="btnrow"><a class="btn btn-primary" href="#about">About</a></p></div>
<div class="h1-photo">{img("speaker", eager=True)}</div></div>
<div class="wrap">{band()}</div></div>

<section class="sec bk-white"><div class="wrap intro1"><div><h2>60+ groups, one region, one network.</h2><p>Community knowledge, lived experience and shared learning.</p></div><figure class="callcard orange"><div class="cc-ph">{img("group")}</div><blockquote>{B.CALLOUT}</blockquote></figure></div></section>

<section class="sec bk-navy" style="padding-top:0"><div class="wrap"><h2>How we work</h2><p class="how-intro">{HOW_INTRO}</p>{how_cards()}</div></section>

<section class="sec bk-teal" style="padding-top:0"><div class="wrap"><div class="stat-card"><h2>Our Impact</h2><dl class="stats"><div><dt>60+</dt><dd>grassroots community-led groups and organisations</dd></div></dl></div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><h2>Our Focus</h2>{focus_rows()}</div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><p class="btnrow" style="justify-content:center;margin:0"><a class="btn btn-primary" href="#network">Network</a></p></div></section>

<section class="sec bk-navy" style="padding-top:0" id="home-focus"><div class="wrap"><span class="eyebrow">In focus</span><h2>Upcoming, projects and the R.A.C.K</h2>
<ul class="kb"><li>{img("crowd")}<h3>{GATHER[0]}: {GATHER[1]}</h3><p>{GATHER[2]}.</p></li><li>{img("meeting")}<h3>Projects</h3><p>Connected and Prepared, Resourcing Community Resilience and Learning Together. <a href="#impact">See partners</a></p></li>
<li>{img("board")}<h3>The R.A.C.K</h3><p>{B.RACK_LINE} <a href="#rack">Explore</a></p></li></ul></div></section>

<section class="sec bk-teal" style="padding-top:0"><div class="wrap"><div class="card">{B.v1_partners().replace('href="#partners"', 'href="#impact"')}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2 class="sechead">What people say</h2>{comments()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="ready">{img("aerial", alt="")}<div><h2>Ready to connect?</h2><p class="lede" style="margin:0 auto">Whether you are a community group, a local council, a funder or someone who cares about your community, there is a place for you in this Alliance.</p>{B.cta_band()}</div></div></div></section>'''

    about = f'''<div class="pg1"><div class="wrap"><div class="ph">{img("line", eager=True)}</div><div class="about-p"><span class="eyebrow">About Us</span><h1>{ABOUT_H}</h1>{"".join(f'<p>{E(p)}</p>' for p in ABOUT_P)}</div></div></div>
<section class="sec bk-navy"><div class="wrap"><div class="split" style="align-items:stretch"><div class="vp vp-t"><h2>Vision</h2><p>{VISION}</p></div><div class="vp vp-y"><h2>Purpose</h2><p>{PURPOSE}</p></div></div></div></section>
<section class="sec bk-teal" style="padding-top:0"><div class="wrap"><h2>Our Journey</h2>{htrail()}</div></section>
<section class="sec bk-orange" style="padding-top:0"><div class="wrap"><div class="card" style="background:var(--yellow-40)">{B.quote()}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap card"><h2>Our structure</h2><div class="two"><div><h3>{GOVERNANCE[0]}</h3><p>{GOVERNANCE[1]}</p></div><div><h3>{STEERING[0]}</h3><p>{STEERING[1]}</p><p><b>The Steering Committee comprises the following groups and organisations.</b></p><ul class="chips">{"".join(f"<li>{E(g)}</li>" for g in STEERING_GROUPS)}</ul></div></div>
<div class="team" style="margin-top:28px"><h3>Resilience Alliance Team</h3><dl>{"".join(f"<dt>{E(r)}</dt><dd>{E(n)}</dd>" for r, n in TEAM)}</dl></div><h3>Common questions</h3>{B.faq()}</div></section>'''

    impact = f'''<div class="pgs bk-yellow"><div class="wrap"><span class="eyebrow">Impact</span><h1>Impact</h1><p class="lede">{B.PARTNER_LINE}</p></div></div>
<section class="sec" style="padding-top:24px"><div class="wrap">{B.logo_grid()}<p class="btnrow"><a class="btn btn-primary" href="mailto:{CONTACT["email"]}">Become a partner</a></p></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2 class="sechead">What people say</h2>{comments()}</div></section>'''

    network = f'''<div class="pg1"><div class="wrap"><div><span class="eyebrow">Network</span><h1>{NET_HERO}</h1><p class="lede">Find the resilience groups connected to the Alliance, by place and by focus.</p></div>
<div class="ph hvid" data-video="{VIMEO}">{img("speaker", eager=True)}<button class="play" aria-label="Play a group video, full screen (placeholder: the sizzle reel stands in)"><span aria-hidden="true">&#9654;</span></button><span class="vtag">Group video: placeholder</span></div></div></div>
<section class="sec"><div class="wrap"><h2 class="sechead">Our Network</h2>{B.map_embed()}<div class="card" style="margin-top:28px"><h3>All groups</h3>{directory2()}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2 class="sechead">Our Stories</h2>{stories()}<div style="margin-top:28px">{comments()}</div></div></section>'''

    rack = f'''<div class="pg1"><div class="wrap"><div><span class="eyebrow">Resources</span><h1>The R.A.C.K</h1><p class="lede"><b>{B.RACK_NAME}.</b> {B.RACK_LINE} {B.RACK_INTRO}</p>{B.rack_buttons()}</div><div class="ph">{img("table", eager=True)}</div></div></div>
<section class="sec bk-yellow"><div class="wrap"><h2>The 5 RACKs</h2>{B.rack_list()}<p class="vnote">Counts from the R.A.C.K, October 2026.</p></div></section>
<section class="sec bk-navy" style="padding-top:0"><div class="wrap"><h2>Funding and grants</h2><ul class="cards"><li class="pcard"><h3>The HELP Fund</h3><p>NRMA Insurance's participatory grants program for the region.</p></li><li class="pcard"><h3>Establishment grants</h3><p>$3,000</p></li><li class="pcard"><h3>Resilience action grants</h3><p>Up to $10,000</p></li></ul></div></section>
<section class="sec bk-orange" style="padding-top:0"><div class="wrap card"><h2>Need help getting in?</h2><p>Access is for Alliance groups. Contact the Network Lead to get set up.</p><p class="btnrow"><a class="btn btn-primary" href="mailto:{CONTACT["email"]}">Contact the Network Lead</a></p></div></section>'''

    body = "".join([screen("home", "Home", home), screen("network", "Network", network), screen("about", "About", about), screen("impact", "Impact", impact), screen("rack", "R.A.C.K", rack)])
    return f'''<!doctype html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>NRCRA Round 2: Client request</title><meta name="robots" content="noindex">
<meta name="description" content="Round 2 prototype for the Northern Rivers Community Resilience Alliance website. Sample content only.">
{FONT}<style>{BASE}{CSS1}{CSS2}{MOBILE}{MOBILE2}</style></head><body class="v1 r2">
{funders_strip()}{nav2()}<main id="main">{body}</main>{B.TICKER}{footer2()}{protobar2()}<script>{JS}</script></body></html>'''




# ---------------------------------------------------------------- brand red and yellow: contrast guidance (single page)
def _lum(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])


def _ratio(a, b):
    la, lb = _lum(a), _lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def _row(fg, bg, fgname, bgname):
    r = _ratio(fg, bg)
    url = f"https://webaim.org/resources/contrastchecker/?fcolor={fg[1:].upper()}&bcolor={bg[1:].upper()}"
    n = "pass" if r >= 4.5 else "fail"
    l = "pass" if r >= 3 else "fail"
    return (f'<tr><td><span class="chip" style="color:{fg};background:{bg}">Aa</span> {fgname} on {bgname}</td><td><b>{r:.2f}:1</b></td>'
            f'<td class="{n}">{n.title()}</td><td class="{l}">{l.title()}</td><td><a href="{url}">Check in WebAIM</a></td></tr>')


def brand_contrast():
    NAVY, WHITE, BLACK, RED, YEL = "#07293b", "#ffffff", "#000000", "#f05a28", "#ffcb2a"
    def block(name, bg):
        rows = "".join(_row(fg, bg, n, name) for fg, n in [(WHITE, "White text"), (NAVY, "Navy text"), (BLACK, "Black text")])
        rows += "".join(_row(bg, b, name + " text", n) for b, n in [(WHITE, "white")])
        return f'<section class="blk"><h2>Brand {name} <code>{bg.upper()}</code></h2><table><thead><tr><th>Pairing</th><th>Ratio</th><th>Body text (4.5:1)</th><th>Large text (3:1)</th><th>WebAIM</th></tr></thead><tbody>{rows}</tbody></table></section>'
    para = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    return f'''<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Brand red and yellow contrast</title><meta name="robots" content="noindex">{FONT}
<style>{BASE}body{{background:#f3f6f7}}main{{max-width:980px;margin:0 auto;padding:36px 20px 56px}}
.flag{{display:inline-block;background:#111;color:#ffcb2a;font-weight:900;letter-spacing:.06em;border-radius:99px;padding:.35em 1em;font-size:.85rem;margin-bottom:14px}}.flag a{{color:#fff}}
.rule{{background:#fff;border-left:10px solid var(--orange);border-radius:20px;padding:22px 26px;margin:22px 0}}.rule p{{margin:0}}
.blk,.card2{{background:#fff;border-radius:28px;padding:28px;margin:0 0 22px}}table{{width:100%;border-collapse:collapse;font-size:.95rem}}th,td{{text-align:left;padding:10px 8px;border-bottom:1px solid var(--line)}}th{{font-size:.8rem;text-transform:uppercase;letter-spacing:.06em}}
.chip{{display:inline-grid;place-items:center;width:44px;height:32px;border-radius:8px;font-weight:900;vertical-align:middle;border:1px solid rgba(7,41,59,.25)}}.pass{{color:#1f6b35;font-weight:800}}.fail{{color:#a3201a;font-weight:800}}code{{font-size:.85em;background:var(--grey-6);padding:.1em .4em;border-radius:6px}}
.demo{{display:grid;grid-template-columns:1fr 1fr;gap:18px}}.demo>div{{border-radius:20px;padding:22px;border:2px solid var(--line)}}.demo h3{{margin-top:0}}.dont{{border-color:#a3201a!important}}.do{{border-color:#1f6b35!important}}
.big{{border-radius:16px;padding:18px;margin:0 0 10px}}.by{{background:var(--yellow);color:#fff}}.br{{background:var(--orange);color:#fff}}
.hl{{background:linear-gradient(transparent 56%,var(--yellow) 56%,var(--yellow) 94%,transparent 94%);padding:0 .12em}}.pill{{display:inline-block;background:var(--orange);color:var(--navy);font-weight:800;font-size:1.2rem;border-radius:99px;padding:.3em 1em}}
.bar{{height:12px;border-radius:99px;background:var(--orange);margin:10px 0 16px;max-width:200px}}.ex>*{{margin-bottom:14px}}
@media(max-width:760px){{.demo{{grid-template-columns:1fr}}table{{font-size:.85rem}}}}</style></head>
<body><main><span class="flag">MOCKUP &amp; PROTOTYPE ONLY &middot; by <a href="https://veemercado.com">veemercado.com</a></span>
<h1>Using the brand red and yellow</h1>
<p class="lede">Contrast ratios for the brand red (orange, <code>{RED.upper()}</code>) and yellow (<code>{YEL.upper()}</code>) against white, navy and black text. Ratios use the WCAG formula, the same one the <a href="https://webaim.org/resources/contrastchecker/">WebAIM Contrast Checker</a> uses, and each row links to WebAIM with the colours filled in.</p>
<div class="rule"><p><b>Red &amp; yellow elements.</b> To maintain readability, red and yellow shouldn&rsquo;t be used as background colours for large chunks of text, as standard text colours (white, navy or black) won&rsquo;t pass contrast requirements. They work well for smaller accents, like title backgrounds or buttons (for example yellow paired with navy).</p></div>
{block("yellow", YEL)}{block("red", RED)}
<section class="card2"><h2>What this means</h2><ul><li><b>Yellow:</b> white text fails everywhere ({_ratio(WHITE, YEL):.2f}:1). Navy passes comfortably ({_ratio(NAVY, YEL):.2f}:1), so yellow is safe for buttons and title backgrounds with navy text.</li>
<li><b>Red:</b> white fails for body text ({_ratio(WHITE, RED):.2f}:1) and only passes as large text. Navy is {_ratio(NAVY, RED):.2f}:1, just under 4.5:1, so it only passes when the text is large (24px, or bold from about 19px). Black does pass ({_ratio(BLACK, RED):.2f}:1) but is off brand.</li>
<li><b>As text colour:</b> red on white is {_ratio(RED, WHITE):.2f}:1 and yellow on white is {_ratio(YEL, WHITE):.2f}:1, so neither works for words on a white page.</li></ul></section>
<section class="card2"><h2>Don&rsquo;t and do</h2><div class="demo"><div class="dont"><h3>Don&rsquo;t: large blocks of text</h3><p class="big by">{para}</p><p class="big br">{para}</p></div>
<div class="do ex"><h3>Do: small accents</h3><p><span class="hl" style="font-weight:900;font-size:1.5rem">Title with a yellow highlight</span></p><p><a class="btn btn-primary" href="#">Yellow button, navy text</a></p><p><span class="pill">Red pill, navy bold large text</span></p><div class="bar" aria-hidden="true"></div><p style="margin:0">Body copy stays navy on white or on a light tint. Red and yellow stay as the accent.</p></div></div></section>
</main></body></html>'''


def main():
    B.write("client/index.html", client())
    B.write("brand-contrast/index.html", brand_contrast())
