#!/usr/bin/env python3
"""Builds the three NRCRA prototypes (v1, v2, v3) and the dashboard from one content source.
Run from the repo root:  python3 tools/build.py
"""
import html, os, textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = html.escape

# ---------------------------------------------------------------- content
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

PILLARS = [
    ("Grow the Alliance", "Welcoming more place-based groups so no group works alone."),
    ("Training and resource sharing", "Practical tools, templates and learning passed group to group."),
    ("Peer support and self care", "Looking after the people who look after their communities."),
    ("Funding and collective projects", "Participatory grants and shared projects, decided locally."),
    ("Advocacy", "A stronger collective voice in funding, policy and planning."),
]
LGAS = ["Tweed", "Byron", "Ballina", "Lismore", "Kyogle", "Clarence", "Richmond"]
STATS = [("60+", "grassroots groups and organisations"), ("7", "local government areas"), ("3", "projects under way"), ("$800,000", "HELP Fund grants program, over two years")]

# (name, kind, note, url). No logo files were supplied: tiles show the name and a "logo to supply" flag.
PARTNERS = [
    ("Funders", "Whose funding makes this work possible.", [
        ("Disaster Ready Fund", "Funds Connected and Prepared, 2026 to 2027.", "https://www.nrcra.org.au/projects"),
        ("FRRR", "The Foundation for Rural and Regional Renewal. Helped establish and grow the Alliance.", "https://www.nrcra.org.au/projects"),
        ("NRMA Insurance HELP Fund", "$800,000 over two years for participatory grants.", "https://www.nrcra.org.au/general-5"),
        ("NSW Government", "Supported the Supporting Spontaneous Volunteers Program.", "https://www.nrcra.org.au/projects"),
    ]),
    ("Delivery partners", "Who we build and deliver programs with.", [
        ("Northern Rivers Community Foundation", "Co-designs and facilitates community-led grant decisions.", "https://www.nrcra.org.au/general-5"),
        ("Resilient Lismore", "Hosts the Alliance and is a founding member group.", "https://www.nrcra.org.au/about"),
        ("Plan C", "Trains Community Carers and Responders. A valued member organisation.", "https://www.nrcra.org.au/about"),
    ]),
    ("Research partners", "Who listens, reflects and tracks change alongside us.", [
        ("University Centre for Rural Health", "Embedded researchers for Monitoring, Evaluation and Learning.", "https://www.nrcra.org.au/about"),
        ("Monash University", "Fire to Flourish, the participatory grants model we build on.", "https://www.nrcra.org.au/general-5"),
    ]),
]
PROJECTS = [
    ("Connected and Prepared", "Governance, capacity building and shared digital tools.", "Funded by the Disaster Ready Fund, 2026 to 2027"),
    ("Resourcing Community Resilience", "Participatory grantmaking, decided by locals.", "Supported by the NRMA HELP Fund with partners, 2026 to 2027"),
    ("Learning Together (MEAL)", "Monitoring, Evaluation and Learning with embedded researchers.", "University Centre for Rural Health"),
]
GATHER = [("27 Nov", "Alliance Gathering, Phase 1", "Location to be confirmed"), ("2027", "Resilience Alliance Health Check", "Dates to be confirmed")]
RACK_ITEMS = [
    ("Training", "Short guides and learning for group leaders."),
    ("Templates", "Policies, plans and forms you can copy and adapt."),
    ("Funding", "Grant guides, the HELP Fund and shared project calls."),
    ("Tools", "Community Emergency Hub Guide, One Calendar and the Resilience Address Book."),
    ("Peer support", "Self care resources and ways to reach other groups."),
    ("Research", "Health Check findings and UCRH reports."),
]
# Sample directory rows: names are placeholders, not real groups.
DIR = [("Sample group A", "Lismore", "Peer support and self care"), ("Sample group B", "Byron", "Training and resource sharing"),
       ("Sample group C", "Tweed", "Funding and collective projects"), ("Sample group D", "Ballina", "Grow the Alliance"),
       ("Sample group E", "Kyogle", "Advocacy"), ("Sample group F", "Clarence", "Peer support and self care")]
MAP_SRC = "https://maps.google.com/maps?q=Northern%20Rivers%20NSW&z=8&output=embed"
IMG = "../assets/img/"


def img(name, alt, cls="", eager=False):
    return f'<img src="{IMG}{name}.jpg" alt="{E(alt)}" class="{cls}" loading="{"eager" if eager else "lazy"}" decoding="async">'


ALT = dict(
    cheer="Alliance members cheering with raised arms in front of a school building.",
    group="A large group of Alliance members posing together on the lawn.",
    crowd="People gathered outdoors listening beneath trees at a gathering.",
    laugh="Members laughing together around a workshop table.",
    listen="Participants listening closely at a long table.",
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
    circle="Members sitting in a circle, smiling, in a bright room.",
)


def logo(cls="logo", white=False):
    return f'<img src="{IMG}logo.png" alt="Northern Rivers Community Resilience Alliance" class="{cls}{" logo-white" if white else ""}" width="260" height="60">'


def nav(v):
    items = "".join(f'<a href="#{k}" data-nav="{k}">{E(t)}</a>' for k, t in PAGES)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap head-in">
<a href="#home" class="brand" aria-label="NRCRA home">{logo()}</a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav id="nav" aria-label="Main">{items}<a class="btn btn-cta" href="#network">Join the network</a></nav>
</div></header>'''


def footer():
    return f'''<footer class="site-foot"><div class="wrap foot-in">
<div>{logo("logo", True)}<p class="tag">Stronger together.</p></div>
<div><h2>Contact</h2><p>Network Lead<br><strong>{CONTACT["name"]}</strong><br><a href="mailto:{CONTACT["email"]}">{CONTACT["email"]}</a><br><a href="tel:{CONTACT["tel"]}">{CONTACT["phone"]}</a></p></div>
<div><h2>Follow</h2><ul class="plain"><li><a href="{LINKS["fb"]}">Facebook</a></li><li><a href="{LINKS["li"]}">LinkedIn</a></li><li><a href="{LINKS["wa"]}">WhatsApp group</a></li><li><a href="{LINKS["news"]}">Resilience Roundup newsletter</a></li></ul></div>
<p class="ack">Acknowledgement of Country: wording to be supplied by NRCRA. © 2025 Northern Rivers Community Resilience Alliance. <a href="{LINKS["live"]}">nrcra.org.au</a></p>
</div></footer>'''


def video(cls="video"):
    return f'''<div class="{cls}" data-video="{VIMEO}">
<img src="{IMG}group-photo.jpg" alt="" loading="lazy">
<button class="play" aria-label="Play the Alliance sizzle reel video"><span aria-hidden="true">&#9654;</span></button>
</div>
<p class="vnote"><a href="{VIMEO_PAGE}">Watch on Vimeo</a></p>'''


def stats(cls="stats"):
    return f'<dl class="{cls}">' + "".join(f"<div><dt>{n}</dt><dd>{t}</dd></div>" for n, t in STATS) + "</dl>"


def pillars_list(cls="pillars"):
    return f'<ol class="{cls}">' + "".join(f"<li><h3>{E(t)}</h3><p>{E(d)}</p></li>" for t, d in PILLARS) + "</ol>"


def partner_tile(name, note, url):
    return f'<li class="ptile"><a href="{url}"><span class="plogo" aria-hidden="true"><b>{E(name)}</b><i>logo to supply</i></span><span class="pname">{E(name)}</span><span class="pnote">{E(note)}</span></a></li>'


def partner_groups(cls="pgroups"):
    out = f'<div class="{cls}">'
    for title, intro, items in PARTNERS:
        out += f'<section class="pgroup"><h3>{E(title)}</h3><p class="lede-s">{E(intro)}</p><ul class="pgrid">' + "".join(partner_tile(*i) for i in items) + "</ul></section>"
    return out + "</div>"


def partner_strip():
    names = [i[0] for _, _, items in PARTNERS for i in items]
    return '<ul class="strip">' + "".join(f'<li><a href="#partners">{E(n)}</a></li>' for n in names[:8]) + "</ul>"


def gather_cards():
    return "".join(f'<li class="gcard"><span class="gdate">{d}</span><h3>{E(t)}</h3><p>{E(w)}</p></li>' for d, t, w in GATHER)


def lga_chips():
    return '<ul class="chips">' + "".join(f"<li>{n}</li>" for n in LGAS) + "</ul>"


def projects_cards():
    return "".join(f'<li class="pcard"><h3>{E(t)}</h3><p>{E(d)}</p><p class="meta">{E(m)}</p></li>' for t, d, m in PROJECTS)


def rack_cards():
    return "".join(f'<li class="rcard"><h3>{E(t)}</h3><p>{E(d)}</p></li>' for t, d in RACK_ITEMS)


def directory():
    rows = "".join(f'<tr data-lga="{l}" data-pillar="{E(p)}"><th scope="row">{E(n)}</th><td>{l}</td><td>{E(p)}</td></tr>' for n, l, p in DIR)
    lopts = "".join(f"<option>{l}</option>" for l in LGAS)
    popts = "".join(f"<option>{E(p[0])}</option>" for p in PILLARS)
    return f'''<div class="dir"><div class="filters">
<label>Location <select data-f="lga"><option value="">All locations</option>{lopts}</select></label>
<label>Pillar <select data-f="pillar"><option value="">All pillars</option>{popts}</select></label></div>
<table><caption>Sample directory rows. Real group names come from the Alliance member list.</caption>
<thead><tr><th scope="col">Group</th><th scope="col">Location</th><th scope="col">Pillar</th></tr></thead><tbody>{rows}</tbody></table>
<p class="empty" hidden>No groups match those filters.</p></div>'''


def map_embed():
    return f'''<div class="mapbox"><iframe title="Map of resilience groups across the Northern Rivers" src="{MAP_SRC}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
<p class="vnote">Placeholder map of the region. In the build this is replaced by the Alliance's own Google Map of member groups.</p>'''


def contact_form():
    return '''<form class="cform" onsubmit="event.preventDefault();this.querySelector('.sent').hidden=false">
<h3>Get in touch</h3>
<label>Name<input required autocomplete="name"></label>
<label>Email<input type="email" required autocomplete="email"></label>
<label>Group name (optional)<input></label>
<label>Message<textarea rows="4" required></textarea></label>
<button class="btn btn-primary" type="submit">Send</button>
<p class="sent" role="status" hidden>Prototype only: nothing was sent.</p></form>'''


def gh_note():
    return '<p class="vnote">Prototype note: these buttons link to the RACK sign-in, sign-up and platform pages (set up on GitHub per the project schedule). Final links to be supplied.</p>'


def rack_buttons():
    return '<p class="btnrow"><a class="btn btn-primary" href="#rack-open">Open the R.A.C.K</a><a class="btn btn-ghost" href="#rack-signup">Sign up</a><a class="btn btn-ghost" href="#rack-signin">Sign in</a></p>'


def cta_band():
    return f'''<p class="btnrow"><a class="btn btn-primary" href="#network">Find a group near you</a><a class="btn btn-ghost" href="{LINKS["wa"]}">Join the WhatsApp group</a><a class="btn btn-ghost" href="mailto:{CONTACT["email"]}">Email the Network Lead</a></p>'''


H1 = "A growing movement of grassroots community groups building disaster resilience across the Northern Rivers"
WHO = "Since early 2024, more than 60 groups and organisations across the Northern Rivers have joined together to form the Resilience Alliance, a community-led network focused on collective care, preparedness and regional strength."
VISION = "Connected, collaborative Northern Rivers communities that are empowered to care for themselves and each other before, during and after disasters."
PURPOSE = "To develop a self-sustaining, trusted Alliance of place-based, community-led resilience groups and organisations. The Alliance shares knowledge and resources, provides mutual support and wellbeing, takes collective action and advocates for identified community needs."
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


def faq():
    return "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in FAQ)


def journey():
    return '<ol class="journey">' + "".join(f"<li><b>{y}</b><p>{E(t)}</p></li>" for y, t in JOURNEY) + "</ol>"


def meal():
    return '<ol class="meal">' + "".join(f"<li>{m}</li>" for m in MEAL) + "</ol>"


def screen(id_, label, body, cls=""):
    return f'<section id="{id_}" data-screen data-label="{label}" class="page {cls}" tabindex="-1" aria-label="{label}">{body}</section>'


# ---------------------------------------------------------------- shared css + js
TOKENS = """
:root{--navy:#07293b;--teal:#00a79d;--orange:#f05a28;--yellow:#ffcb2a;
--teal-d:#006b64;--orange-d:#b93a0c;--ink:#07293b;--muted:#3d5663;--paper:#fff;--tint:#eef7f6;--cream:#fff8e1;--line:#cfdde0;
--font:"Nunito Sans",Arial,sans-serif;--wrap:1180px}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font:400 18px/1.6 var(--font);color:var(--ink);background:var(--paper)}
img{max-width:100%;display:block}a{color:var(--teal-d)}a:hover{color:var(--navy)}
h1,h2,h3{line-height:1.12;margin:0 0 .5em;font-weight:800;letter-spacing:-.01em}
h1{font-size:clamp(2rem,5vw,3.6rem);font-weight:900}h2{font-size:clamp(1.6rem,3.4vw,2.5rem)}h3{font-size:1.25rem}
p{margin:0 0 1em}.wrap{max-width:var(--wrap);margin:0 auto;padding:0 20px}
:focus-visible{outline:3px solid var(--orange-d);outline-offset:3px}
.skip{position:absolute;left:-999px;top:8px;background:var(--yellow);color:var(--navy);padding:10px 16px;z-index:100;font-weight:800}.skip:focus{left:8px}
.plain{list-style:none;margin:0;padding:0}.vnote{font-size:.85rem;color:var(--muted)}.vnote a{color:inherit}
.btn{display:inline-block;font:800 1rem var(--font);padding:.8em 1.4em;text-decoration:none;border:3px solid var(--navy);cursor:pointer;min-height:44px}
.btn-primary{background:var(--yellow);color:var(--navy)}.btn-primary:hover{background:var(--navy);color:var(--yellow)}
.btn-ghost{background:transparent;color:var(--navy)}.btn-ghost:hover{background:var(--navy);color:#fff}
.btn-cta{background:var(--navy);color:#fff;padding:.55em 1.1em}.btn-cta:hover{background:var(--teal-d);color:#fff}
.btnrow{display:flex;flex-wrap:wrap;gap:12px;margin:1.2em 0 0}
.site-head{background:#fff;position:sticky;top:0;z-index:50;border-bottom:1px solid var(--line)}
.head-in{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-top:10px;padding-bottom:10px}
.logo{height:48px;width:auto}.logo-white{filter:brightness(0) invert(1)}
#nav{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
#nav a:not(.btn){padding:.5em .9em;color:var(--navy);text-decoration:none;font-weight:700;border-bottom:3px solid transparent}
#nav a:not(.btn):hover,#nav a[aria-current=page]{border-bottom-color:var(--orange-d)}
.menu-btn{display:none;font:800 1rem var(--font);background:var(--navy);color:#fff;border:0;padding:.7em 1.1em;min-height:44px}
@media(max-width:860px){.menu-btn{display:block}#nav{display:none;position:absolute;left:0;right:0;top:100%;background:#fff;flex-direction:column;align-items:stretch;padding:12px 20px 20px;border-bottom:1px solid var(--line)}#nav.open{display:flex}.logo{height:40px}}
.page{display:none;outline:0}.page.on{display:block}
.chips{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:8px}.chips li{background:#fff;color:var(--navy);border:2px solid var(--navy);padding:.2em .8em;font-weight:700;border-radius:99px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:20px;margin:0}.stats div{margin:0}
.stats dt{font-size:clamp(2.2rem,5vw,3.4rem);font-weight:900;line-height:1}.stats dd{margin:.3em 0 0;font-weight:600}
.pillars{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px;counter-reset:p}
.pillars li{counter-increment:p;padding:20px}.pillars li::before{content:counter(p);display:block;font-weight:900;font-size:2rem;line-height:1;margin-bottom:.4em}
.pillars h3{margin-bottom:.3em}.pillars p{margin:0}
.video{position:relative;aspect-ratio:16/9;background:var(--navy);overflow:hidden}.video img,.video iframe{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;border:0}
.play{position:absolute;inset:0;margin:auto;width:84px;height:84px;border-radius:50%;border:4px solid var(--navy);background:var(--yellow);color:var(--navy);font-size:1.8rem;cursor:pointer;display:grid;place-items:center;padding-left:6px}.play:hover{background:#fff}
.pgrid{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:20px}
.ptile a{display:flex;flex-direction:column;height:100%;text-decoration:none;color:var(--navy);padding:16px;border:2px solid var(--line);background:#fff}
.ptile a:hover{border-color:var(--navy)}.plogo{display:grid;place-items:center;text-align:center;height:110px;background:var(--tint);margin-bottom:12px;padding:8px;position:relative}
.plogo b{font-size:1.05rem}.plogo i{position:absolute;bottom:4px;right:8px;font-size:.7rem;color:var(--muted);font-style:normal}
.pname{font-weight:800}.pnote{font-size:.95rem;color:var(--muted)}.lede-s{color:var(--muted)}
.strip a:not(.btn){color:var(--navy) !important}
.strip{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:10px}.strip a{display:block;padding:.5em 1em;background:#fff;color:var(--navy);font-weight:700;text-decoration:none;border:2px solid var(--line)}.strip a:hover{border-color:var(--navy)}
.gcard,.pcard,.rcard{list-style:none;padding:22px}.gcard,.pcard{color:var(--navy)}.gdate{font-weight:900;font-size:1.6rem}
ul.cards{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px}
.meta{font-size:.9rem;color:var(--muted);margin:0}
.mapbox{aspect-ratio:16/9;min-height:320px;border:3px solid var(--navy);background:var(--tint)}.mapbox iframe{width:100%;height:100%;border:0}
.dir table{width:100%;border-collapse:collapse}.dir caption{text-align:left;font-size:.85rem;color:var(--muted);padding-bottom:8px}
.dir th,.dir td{text-align:left;padding:12px;border-bottom:1px solid var(--line)}.filters{display:flex;flex-wrap:wrap;gap:16px;margin-bottom:16px}
.filters label,.cform label{display:flex;flex-direction:column;font-weight:700;gap:4px}
select,input,textarea{font:inherit;padding:.6em;border:2px solid var(--navy);background:#fff;color:var(--navy);min-height:44px}
.cform{display:grid;gap:14px;max-width:560px}
.journey{list-style:none;margin:0;padding:0;display:grid;gap:18px}.journey li{display:grid;grid-template-columns:130px 1fr;gap:16px}.journey b{font-size:1.5rem;font-weight:900}.journey p{margin:0}
@media(max-width:600px){.journey li{grid-template-columns:1fr;gap:2px}}
.meal{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px}.meal li{padding:16px;text-align:center;font-weight:800;border:2px solid var(--navy);background:#fff}
details{border-bottom:1px solid var(--line);padding:14px 0}summary{cursor:pointer;font-weight:800}details p{margin:.6em 0 0}
blockquote{margin:0;font-size:clamp(1.3rem,2.6vw,1.9rem);font-weight:700;line-height:1.35}blockquote cite{display:block;font-size:1rem;font-weight:600;font-style:normal;margin-top:.8em}
.site-foot{background:var(--navy);color:#fff;padding:48px 0 32px;margin-top:0}.site-foot a{color:#fff}.site-foot h2{font-size:1rem;text-transform:uppercase;letter-spacing:.1em;color:var(--yellow)}
.foot-in{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:32px}.foot-in .ack{grid-column:1/-1;font-size:.85rem;border-top:1px solid #35566a;padding-top:20px;margin:0;color:#d5e3e8}
.foot-in .tag{margin-top:12px;font-weight:800;color:var(--yellow)}.logo-white{height:54px}
.eyebrow{font-weight:900;text-transform:uppercase;letter-spacing:.12em;font-size:.85rem;margin-bottom:.8em;display:block}
.split{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center}@media(max-width:860px){.split{grid-template-columns:1fr}}
.tiles{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px}
.tiles a{display:block;padding:18px 20px;text-decoration:none;font-weight:800;color:var(--navy)}
.tiles small{display:block;font-weight:600;margin-top:.2em}
.photo{width:100%;height:100%;object-fit:cover}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
"""

JS = """
(function(){
var ids=[].map.call(document.querySelectorAll('[data-screen]'),function(s){return s.id}),
titles={};[].forEach.call(document.querySelectorAll('[data-screen]'),function(s){titles[s.id]=s.getAttribute('data-label')});
function route(){var h=(location.hash||'#home').slice(1);if(ids.indexOf(h)<0){if(h.indexOf('rack-')===0){h='rack'}else return}
[].forEach.call(document.querySelectorAll('[data-screen]'),function(s){s.classList.toggle('on',s.id===h)});
[].forEach.call(document.querySelectorAll('[data-nav]'),function(a){if(a.getAttribute('data-nav')===h)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')});
document.title=titles[h]+' | NRCRA prototype';window.scrollTo(0,0);var s=document.getElementById(h);if(s&&window.__navd){s.focus({preventScroll:true})}window.__navd=1;
document.getElementById('nav').classList.remove('open');var b=document.querySelector('.menu-btn');if(b)b.setAttribute('aria-expanded','false')}
window.addEventListener('hashchange',route);route();
var mb=document.querySelector('.menu-btn');mb.addEventListener('click',function(){var o=document.getElementById('nav').classList.toggle('open');mb.setAttribute('aria-expanded',o)});
document.addEventListener('click',function(e){var v=e.target.closest('[data-video]');if(v&&e.target.closest('.play')){var f=document.createElement('iframe');f.src=v.getAttribute('data-video');f.title='NRCRA sizzle reel';f.allow='autoplay; fullscreen; picture-in-picture';f.allowFullscreen=true;v.innerHTML='';v.appendChild(f)}});
[].forEach.call(document.querySelectorAll('.dir'),function(d){function ap(){var l=d.querySelector('[data-f=lga]').value,p=d.querySelector('[data-f=pillar]').value,n=0;
[].forEach.call(d.querySelectorAll('tbody tr'),function(r){var ok=(!l||r.dataset.lga===l)&&(!p||r.dataset.pillar===p);r.hidden=!ok;if(ok)n++});d.querySelector('.empty').hidden=n>0}
[].forEach.call(d.querySelectorAll('select'),function(s){s.addEventListener('change',ap)})});
})();
"""

FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700;800;900&display=swap" rel="stylesheet">'


def page_shell(title, css, body, v):
    return f'''<!doctype html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="robots" content="noindex">
<meta name="description" content="Prototype for the Northern Rivers Community Resilience Alliance website. Sample content only.">
{FONT}<style>{TOKENS}{css}</style></head><body class="{v}">
{nav(v)}<main id="main">{body}</main>{footer()}<script>{JS}</script></body></html>'''


# ================================================================ V1: Visual & colour blocks
CSS1 = """
.page{--r:0}
.blk{padding:72px 0}.blk-navy{background:var(--navy);color:#fff}.blk-yellow{background:var(--yellow)}.blk-teal{background:var(--teal)}.blk-orange{background:var(--orange);color:var(--navy)}.blk-cream{background:var(--cream)}
.blk-navy a:not(.btn){color:#fff}.blk-navy .btn-ghost{color:#fff;border-color:#fff}.blk-navy .btn-ghost:hover{background:#fff;color:var(--navy)}.blk-navy .btn-primary{border-color:var(--yellow)}
.blk-navy .lede-s,.blk-navy .meta,.blk-navy .vnote{color:#d5e3e8}
.hl{display:inline;background:var(--yellow);color:var(--navy);padding:.02em .22em;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.hero1{background:var(--navy);color:#fff;padding:0}.hero1 .grid{display:grid;grid-template-columns:1.05fr .95fr;min-height:560px}
.hero1 .txt{padding:64px 20px 64px max(20px,calc((100vw - var(--wrap))/2 + 20px));display:flex;flex-direction:column;justify-content:center}
.hero1 .pics{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:6px;background:var(--navy)}.hero1 .pics img:first-child{grid-row:1/3}
.hero1 .pics img{width:100%;height:100%;object-fit:cover}
@media(max-width:860px){.hero1 .grid{grid-template-columns:1fr}.hero1 .txt{padding:40px 20px}.hero1 .pics{height:320px}}
.hero1 .tiles a{background:var(--yellow);border:3px solid var(--yellow)}.hero1 .tiles li:nth-child(2) a{background:var(--teal);border-color:var(--teal)}.hero1 .tiles li:nth-child(3) a{background:#fff;border-color:#fff}.hero1 .tiles a:hover{background:var(--orange);border-color:var(--orange)}
.latest{background:var(--yellow);color:var(--navy)}.latest .wrap{display:flex;flex-wrap:wrap;gap:8px 28px;padding-top:14px;padding-bottom:14px;align-items:center}.latest b{text-transform:uppercase;letter-spacing:.1em;font-size:.85rem}.latest a{color:var(--navy);font-weight:700}
.bgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:0}.bgrid>*{padding:40px 28px}
.pillars li{border-top:8px solid var(--navy);background:#fff}.pillars li:nth-child(1){border-color:var(--orange)}.pillars li:nth-child(2){border-color:var(--teal)}.pillars li:nth-child(3){border-color:var(--yellow)}.pillars li:nth-child(4){border-color:var(--navy)}.pillars li:nth-child(5){border-color:var(--orange)}
.blk-navy .stats dt{color:var(--yellow)}.blk-navy .pillars li{color:var(--navy)}
.gcard{background:var(--teal);color:var(--navy)}.pcard{background:var(--yellow)}.rcard{background:var(--navy);color:#fff}.rcard p{color:#e4eef2}.pcard .meta{color:var(--navy)}
.photo-band{display:grid;grid-template-columns:repeat(4,1fr);gap:0}.photo-band img{height:260px;width:100%;object-fit:cover}@media(max-width:700px){.photo-band{grid-template-columns:1fr 1fr}}
.pg-hero{background:var(--navy);color:#fff;padding:72px 0 56px}.pg-hero h1{max-width:20ch}.pg-hero p{font-size:1.25rem;max-width:60ch}
.pg-hero.teal{background:var(--teal);color:var(--navy)}.pg-hero.yellow{background:var(--yellow);color:var(--navy)}.pg-hero.orange{background:var(--orange);color:var(--navy)}
.pgroup{margin-bottom:56px}.pgroup h3{display:inline-block;background:var(--navy);color:#fff;padding:.2em .7em;font-size:1.4rem}
.map-wrap{background:var(--navy);padding:0}.rackhero .btn-primary{border-color:var(--navy)}
"""


def v1():
    home = f'''<div class="hero1"><div class="grid"><div class="txt">
<span class="eyebrow" style="color:var(--yellow)">Northern Rivers Community Resilience Alliance</span>
<h1>A growing movement of <span class="hl">grassroots community groups</span> building disaster resilience across the Northern Rivers</h1>
<ul class="tiles" style="margin-top:20px"><li><a href="#about">What we do<small>Our focus and purpose</small></a></li><li><a href="#partners">Projects and the HELP Fund<small>Who funds this work</small></a></li><li><a href="#network">This is our impact<small>60+ groups, one network</small></a></li></ul>
</div><div class="pics">{img("group-cheer", ALT["cheer"], "", True)}{img("laughing", ALT["laugh"], "", True)}{img("web", ALT["web"], "", True)}</div></div></div>
<div class="latest"><div class="wrap"><b>Latest</b><span>$800,000 HELP Fund grants program announced. <a href="{LINKS["news"]}">Read the news</a></span><span>27 Nov: Alliance Gathering, Phase 1. <a href="#home-gather">See upcoming</a></span></div></div>

<section class="blk blk-cream"><div class="wrap split"><div><span class="eyebrow" style="color:var(--orange-d)">Who we are</span><h2>The group made up of groups</h2><p>{WHO}</p>{lga_chips()}<p class="btnrow"><a class="btn btn-primary" href="#about">Read about us</a></p></div>
<div>{video("video")}</div></div></section>

<section class="blk blk-navy"><div class="wrap"><span class="eyebrow" style="color:var(--yellow)">What we have achieved</span><h2>Five focus areas. One network.</h2>{pillars_list()}<div style="height:36px"></div>{stats()}
<p style="margin-top:36px"><b>Thanks to our partners</b></p>{partner_strip()}</div></section>

<section class="blk blk-yellow" id="home-gather"><div class="wrap"><span class="eyebrow">In focus</span><h2>Upcoming, projects and the R.A.C.K</h2>
<ul class="cards"><li class="gcard"><span class="gdate">{GATHER[0][0]}</span><h3>{GATHER[0][1]}</h3><p>{GATHER[0][2]}</p></li>
<li class="pcard" style="background:#fff"><h3>Projects</h3><p>Connected and Prepared, Resourcing Community Resilience and Learning Together.</p><p class="meta"><a href="#partners">See who funds them</a></p></li>
<li class="rcard"><h3>The R.A.C.K</h3><p>The online resource hub for Alliance groups.</p><p class="meta"><a href="#rack" style="color:#fff">Explore the R.A.C.K</a></p></li></ul></div></section>

<section class="blk"><div class="wrap"><span class="eyebrow" style="color:var(--teal-d)">Our partners</span><h2>Made possible together</h2>{partner_strip()}<p class="btnrow"><a class="btn btn-ghost" href="#partners">All our partners</a></p></div></section>
<section class="blk blk-teal"><div class="wrap"><h2>Get involved</h2><p style="font-size:1.25rem;max-width:56ch">Local experience. Shared learning. Wider impact. Join a network of groups who show up for their communities.</p>{cta_band()}</div></section>'''

    about = f'''<div class="pg-hero teal"><div class="wrap"><span class="eyebrow">About us</span><h1>Local experience. Shared learning. Wider impact.</h1><p>{WHO}</p></div></div>
<section class="blk"><div class="wrap bgrid" style="padding:0 0"><div class="blk-yellow"><h2>Vision</h2><p>{VISION}</p></div><div class="blk-navy"><h2>Purpose</h2><p>{PURPOSE}</p></div></div></section>
<section class="blk blk-cream"><div class="wrap"><h2>Our journey</h2>{journey()}</div></section>
<section class="blk blk-navy"><div class="wrap split"><div><h2>How we learn</h2><p>Monitoring, Evaluation, Accountability and Learning is our learning cycle.</p>{meal()}</div><div>{img("board", ALT["board"], "photo")}</div></div></section>
<section class="blk blk-orange"><div class="wrap"><blockquote>&ldquo;{QUOTE[0]}&rdquo;<cite>{QUOTE[1]}</cite></blockquote></div></section>
<section class="blk"><div class="wrap"><h2>Our structure</h2><p>Steering committee, embedded researchers from UCRH and the Network Lead, {CONTACT["name"]}. Names and roles to be supplied.</p><h2 style="margin-top:1.4em">Common questions</h2>{faq()}</div></section>'''

    partners = f'''<div class="pg-hero yellow"><div class="wrap"><span class="eyebrow">Impact</span><h1>The partners who make this work possible</h1><p>Funders, delivery partners and researchers standing behind community-led resilience.</p></div></div>
<section class="blk"><div class="wrap">{partner_groups()}</div></section>
<section class="blk blk-navy"><div class="wrap"><h2>Projects they support</h2><ul class="cards">{projects_cards()}</ul></div></section>
<section class="blk blk-teal"><div class="wrap"><h2>Partner with us</h2><p>Talk to the Network Lead about funding, research or delivery partnerships.</p><p class="btnrow"><a class="btn btn-primary" href="mailto:{CONTACT["email"]}">Email {CONTACT["name"]}</a></p></div></section>'''

    network = f'''<div class="pg-hero orange"><div class="wrap"><span class="eyebrow">Network</span><h1>60+ place-based groups across the Northern Rivers</h1><p>Find the resilience groups connected to the Alliance, by place and by focus.</p></div></div>
<section class="blk"><div class="wrap">{map_embed()}{lga_chips()}</div></section>
<section class="blk blk-cream"><div class="wrap"><h2>Five pillars</h2>{pillars_list()}</div></section>
<section class="blk"><div class="wrap split"><div><h2>All groups</h2>{directory()}</div><div>{contact_form()}</div></div></section>'''

    rack = f'''<div class="pg-hero rackhero"><div class="wrap split"><div><span class="eyebrow" style="color:var(--yellow)">Resources</span><h1>The R.A.C.K</h1><p>The online resource hub for the groups of the Alliance. Training, templates, funding and tools, in one place.</p>{rack_buttons()}</div><div>{img("workshop", ALT["table"], "photo")}</div></div></div>
<section class="blk blk-cream"><div class="wrap"><h2>What you will find inside</h2><ul class="cards">{rack_cards()}</ul>{gh_note()}</div></section>
<section class="blk blk-navy"><div class="wrap"><h2>Funding and grants</h2><ul class="cards"><li class="pcard"><h3>The HELP Fund</h3><p>NRMA Insurance's participatory grants program for the region.</p></li><li class="pcard"><h3>Establishment grants</h3><p>$3,000</p></li><li class="pcard"><h3>Resilience action grants</h3><p>Up to $10,000</p></li></ul></div></section>
<section class="blk blk-teal"><div class="wrap"><h2>Need help getting in?</h2><p>Access is for Alliance groups. Contact the Network Lead to get set up.</p><p class="btnrow"><a class="btn btn-primary" href="mailto:{CONTACT["email"]}">Contact the Network Lead</a></p></div></section>'''

    body = "".join([screen("home", "Home", home), screen("about", "About", about), screen("partners", "Partners", partners), screen("network", "Network", network), screen("rack", "R.A.C.K", rack)])
    return page_shell("NRCRA prototype 1: Colour blocks", CSS1, body, "v1")


# ================================================================ V2: Light background, rounded blocks
CSS2 = """
:root{--r:24px}
body{background:#f7fbfb}
.sec{padding:56px 0}.card{background:#fff;border-radius:var(--r);padding:32px;box-shadow:0 2px 0 var(--line),0 12px 32px -18px rgba(7,41,59,.25)}
.card.tint{background:var(--tint);box-shadow:none}.card.sun{background:var(--cream);box-shadow:none}.card.dark{background:var(--navy);color:#fff;box-shadow:none}.card.dark a:not(.btn){color:#fff}
.card.dark .btn-ghost{color:#fff;border-color:#fff}.card.dark .btn-ghost:hover{background:#fff;color:var(--navy)}.card.dark .lede-s,.card.dark .meta{color:#d5e3e8}
.btn{border-radius:99px;border-width:2px}.btn-cta{border-radius:99px}
.hero2{padding:40px 0 24px}.hero2 .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:28px;align-items:stretch}
.hero2 .lead{background:var(--navy);color:#fff;border-radius:32px;padding:48px 40px;display:flex;flex-direction:column;justify-content:center}
.hero2 .lead .btn-primary{border-color:var(--yellow)}.hero2 .lead .btn-ghost{color:#fff;border-color:#fff}.hero2 .lead .btn-ghost:hover{background:#fff;color:var(--navy)}
.mosaic{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:12px;min-height:420px}.mosaic img{border-radius:var(--r);width:100%;height:100%;object-fit:cover}.mosaic img:first-child{grid-row:1/3}
@media(max-width:860px){.hero2 .wrap{grid-template-columns:1fr}.hero2 .lead{padding:32px 24px}.mosaic{min-height:300px}}
.quick{margin-top:18px}.quick a{border-radius:18px;background:rgba(255,255,255,.1);color:#fff;border:2px solid rgba(255,255,255,.4)}.quick a:hover{background:var(--yellow);color:var(--navy);border-color:var(--yellow)}
.latest2{display:flex;flex-wrap:wrap;gap:12px;margin-top:16px}.latest2 span{background:var(--yellow);color:var(--navy);border-radius:99px;padding:.4em 1em;font-weight:700;font-size:.95rem}.latest2 a{color:var(--navy)}
.rounded{border-radius:var(--r);width:100%;height:100%;object-fit:cover}.video{border-radius:var(--r)}
.pillars li{background:#fff;border-radius:var(--r);box-shadow:0 2px 0 var(--line)}.pillars li::before{color:var(--teal-d)}
.card.dark .stats dt{color:var(--yellow)}.gcard,.pcard,.rcard{border-radius:var(--r);background:#fff;box-shadow:0 2px 0 var(--line)}.gdate{color:var(--orange-d)}
.rcard{color:var(--navy)}.rcard:nth-child(3n+1){background:var(--tint)}.rcard:nth-child(3n+2){background:var(--cream)}
.ptile a{border-radius:20px}.plogo{border-radius:14px}.strip a{border-radius:99px}
.chips li{background:var(--tint);border-color:transparent}
.pgroup{margin-bottom:40px}.pgroup h3{font-size:1.5rem}
.mapbox{border-radius:var(--r);overflow:hidden;border-width:0;box-shadow:0 2px 0 var(--line)}
select,input,textarea{border-radius:12px}.meal li{border-radius:16px}
.pg2{padding:56px 0 8px}.pg2 .pill{display:inline-block;background:var(--yellow);color:var(--navy);border-radius:99px;padding:.2em .9em;font-weight:800;margin-bottom:1em}.pg2 p{font-size:1.2rem;max-width:62ch;color:var(--muted)}
.stack>*+*{margin-top:24px}
"""


def v2():
    home = f'''<div class="hero2"><div class="wrap"><div class="lead"><span class="eyebrow" style="color:var(--yellow)">Northern Rivers Community Resilience Alliance</span>
<h1>{H1}</h1><ul class="tiles quick"><li><a href="#about">What we do<small>Focus and purpose</small></a></li><li><a href="#partners">Projects and HELP Fund<small>Who funds this</small></a></li><li><a href="#network">Our impact<small>60+ groups</small></a></li></ul>
<div class="latest2"><span>$800,000 HELP Fund announced</span><span>27 Nov: Alliance Gathering</span></div></div>
<div class="mosaic">{img("group-photo", ALT["group"], "", True)}{img("crowd", ALT["crowd"], "", True)}{img("circle", ALT["circle"], "", True)}</div></div></div>

<section class="sec"><div class="wrap split"><div class="card"><span class="eyebrow" style="color:var(--teal-d)">Who we are</span><h2>The group made up of groups</h2><p>{WHO}</p>{lga_chips()}<p class="btnrow"><a class="btn btn-primary" href="#about">About the Alliance</a></p></div>
<div>{video("video")}</div></div></section>

<section class="sec"><div class="wrap"><div class="card dark"><span class="eyebrow" style="color:var(--yellow)">What we have achieved</span><h2>Focus and impact</h2>{stats()}<p style="margin:28px 0 12px"><b>Thanks to our partners</b></p>{partner_strip()}</div>
<div style="height:20px"></div>{pillars_list()}</div></section>

<section class="sec"><div class="wrap"><span class="eyebrow" style="color:var(--teal-d)">In focus</span><h2>Upcoming, projects and the R.A.C.K</h2>
<ul class="cards"><li class="gcard"><span class="gdate">{GATHER[0][0]}</span><h3>{GATHER[0][1]}</h3><p>{GATHER[0][2]}</p></li><li class="pcard"><h3>Projects</h3><p>Three projects growing the Alliance, funding local ideas and learning together.</p><p class="meta"><a href="#partners">See partners</a></p></li><li class="rcard"><h3>The R.A.C.K</h3><p>Resources for Alliance groups.</p><p class="meta"><a href="#rack">Explore</a></p></li></ul></div></section>

<section class="sec"><div class="wrap"><div class="card tint"><h2>Our partners</h2>{partner_strip()}<p class="btnrow"><a class="btn btn-ghost" href="#partners">See all partners</a></p></div></div></section>
<section class="sec"><div class="wrap"><div class="card sun"><h2>Get involved</h2><p>Local experience. Shared learning. Wider impact.</p>{cta_band()}</div></div></section>'''

    about = f'''<div class="pg2"><div class="wrap"><span class="pill">About us</span><h1>Local experience. Shared learning. Wider impact.</h1><p>{WHO}</p></div></div>
<section class="sec"><div class="wrap stack"><div class="split"><div class="card tint"><h2>Vision</h2><p>{VISION}</p></div><div class="card sun"><h2>Purpose</h2><p>{PURPOSE}</p></div></div>
<div class="card"><h2>Our journey</h2>{journey()}</div>
<div class="split"><div class="card dark"><h2>How we learn</h2><p>Monitoring, Evaluation, Accountability and Learning.</p>{meal()}</div>{img("laughing", ALT["laugh"], "rounded")}</div>
<div class="card tint"><blockquote>&ldquo;{QUOTE[0]}&rdquo;<cite>{QUOTE[1]}</cite></blockquote></div>
<div class="card"><h2>Our structure</h2><p>Steering committee, UCRH embedded researchers and the Network Lead, {CONTACT["name"]}. Names to be supplied.</p><h3>Common questions</h3>{faq()}</div></div></section>'''

    partners = f'''<div class="pg2"><div class="wrap"><span class="pill">Impact</span><h1>Our partners</h1><p>The funders, delivery partners and researchers behind community-led resilience.</p></div></div>
<section class="sec"><div class="wrap">{partner_groups()}</div></section>
<section class="sec"><div class="wrap"><div class="card dark"><h2>Projects they support</h2><ul class="cards">{projects_cards()}</ul></div></div></section>'''

    network = f'''<div class="pg2"><div class="wrap"><span class="pill">Network</span><h1>Groups across the Northern Rivers</h1><p>60+ grassroots, place-based groups working across five pillars.</p></div></div>
<section class="sec"><div class="wrap stack">{map_embed()}{lga_chips()}<div class="card"><h2>All groups</h2>{directory()}</div>{pillars_list()}<div class="card tint">{contact_form()}</div></div></section>'''

    rack = f'''<div class="pg2"><div class="wrap"><span class="pill">Resources</span><h1>The R.A.C.K</h1><p>The online resource hub for the groups of the Alliance.</p>{rack_buttons()}</div></div>
<section class="sec"><div class="wrap stack"><div class="split"><div class="card sun"><h2>Who it is for</h2><p>Groups in the Alliance. To get access, contact the Network Lead.</p><p class="btnrow"><a class="btn btn-primary" href="mailto:{CONTACT["email"]}">Contact the Network Lead</a></p></div>{img("table", ALT["table"], "rounded")}</div>
<h2>What you will find inside</h2><ul class="cards">{rack_cards()}</ul>{gh_note()}
<div class="card dark"><h2>Funding and grants</h2><ul class="cards"><li class="pcard"><h3>The HELP Fund</h3><p>Participatory grants for local groups.</p></li><li class="pcard"><h3>Establishment grants</h3><p>$3,000</p></li><li class="pcard"><h3>Resilience action grants</h3><p>Up to $10,000</p></li></ul></div></div></section>'''

    body = "".join([screen("home", "Home", home), screen("about", "About", about), screen("partners", "Partners", partners), screen("network", "Network", network), screen("rack", "R.A.C.K", rack)])
    return page_shell("NRCRA prototype 2: Light and rounded", CSS2, body, "v2")


# ================================================================ V3: Heavy visuals
CSS3 = """
.hero3{position:relative;min-height:min(88vh,760px);display:flex;align-items:flex-end;color:#fff;background:var(--navy)}
.hero3>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.hero3::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,41,59,.6) 0%,rgba(7,41,59,.65) 50%,rgba(7,41,59,.92) 100%)}
.hero3 .wrap{position:relative;z-index:2;padding-bottom:56px;padding-top:120px}.hero3 h1{max-width:22ch;font-size:clamp(2.2rem,6vw,4.6rem)}
.hero3 .btn-primary{border-color:var(--yellow)}.hero3 .btn-ghost{color:#fff;border-color:#fff}.hero3 .btn-ghost:hover{background:#fff;color:var(--navy)}
.hero3 .tiles{margin-top:24px}.hero3 .tiles a{color:#fff;border-left:5px solid var(--yellow);background:rgba(7,41,59,.55)}.hero3 .tiles a:hover{background:var(--yellow);color:var(--navy)}
.full{position:relative;color:#fff;background:var(--navy);padding:96px 0;overflow:hidden}.full>img.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.full::after{content:"";position:absolute;inset:0;background:rgba(7,41,59,.78)}
.full .wrap{position:relative;z-index:2}.full a:not(.btn){color:#fff}.full .btn-primary{border-color:var(--yellow)}.full .btn-ghost{color:#fff;border-color:#fff}.full .btn-ghost:hover{background:#fff;color:var(--navy)}
.full .stats dt{color:var(--yellow)}.full .lede-s,.full .meta{color:#d5e3e8}
.light{padding:80px 0}.green{background:#0b3d2e;color:#fff}.green a:not(.btn){color:#fff}.green .btn-primary{border-color:var(--yellow)}
.bigvideo{position:relative}.bigvideo .video{aspect-ratio:21/9;min-height:360px}.bigvideo .video::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(7,41,59,.6),transparent);pointer-events:none}
.bigvideo .over{position:absolute;left:0;right:0;bottom:0;color:#fff;z-index:3;padding:0 0 32px;pointer-events:none}.bigvideo .over h2{max-width:18ch;font-size:clamp(1.8rem,4vw,3rem)}
.bigvideo .play{z-index:4}.bigvideo .vnote{background:var(--navy);margin:0;padding:8px 20px;text-align:right}.bigvideo .vnote a{color:#fff}
.photogrid{display:grid;grid-template-columns:repeat(3,1fr);gap:0}.photogrid figure{margin:0;position:relative;aspect-ratio:4/5;overflow:hidden;background:var(--navy)}
.photogrid img{width:100%;height:100%;object-fit:cover;transition:transform .5s}.photogrid figure:hover img{transform:scale(1.04)}
.photogrid figcaption{position:absolute;inset:auto 0 0 0;padding:70px 20px 20px;color:#fff;background:linear-gradient(transparent,rgba(7,41,59,.92))}.photogrid figcaption h3{margin:0 0 .2em;font-size:1.5rem}.photogrid figcaption p{margin:0}.photogrid a{color:#fff;font-weight:800}
@media(max-width:760px){.photogrid{grid-template-columns:1fr}.photogrid figure{aspect-ratio:4/3}}
.pillars{gap:2px;background:#fff2}.pillars li{background:rgba(255,255,255,.08);border-top:4px solid var(--yellow)}.pillars li::before{color:var(--yellow)}
.pillars.dk li{background:var(--navy);color:#fff}
.gcard,.pcard,.rcard{background:#fff;border-left:6px solid var(--yellow)}.gcard,.pcard,.rcard{color:var(--navy)}
.pg3{position:relative;min-height:420px;display:flex;align-items:flex-end;color:#fff;background:var(--navy)}.pg3>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.pg3::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,41,59,.55),rgba(7,41,59,.92))}
.pg3 .wrap{position:relative;z-index:2;padding-bottom:48px;padding-top:110px}.pg3 p{font-size:1.25rem;max-width:60ch}.pg3 .btn-primary{border-color:var(--yellow)}.pg3 .btn-ghost{color:#fff;border-color:#fff}
.pgroup h3{border-bottom:4px solid var(--yellow);display:inline-block;padding-bottom:.2em;font-size:1.6rem}
.ptile a{border-radius:0}
.mapfull .mapbox{border:0;aspect-ratio:21/9;min-height:420px}
.band{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:0}.band>*{margin:0}.band img{width:100%;height:340px;object-fit:cover}
"""


def hero3(img_name, alt, inner, cls="pg3"):
    return f'<div class="{cls}">{img(img_name, alt, "", True)}<div class="wrap">{inner}</div></div>'


def v3():
    home = f'''<div class="hero3">{img("aerial", ALT["aerial"], "", True)}<div class="wrap"><span class="eyebrow" style="color:var(--yellow)">Northern Rivers Community Resilience Alliance</span>
<h1>{H1}</h1><ul class="tiles"><li><a href="#about">What we do<small>Focus and purpose</small></a></li><li><a href="#partners">Projects and HELP Fund<small>Who funds this</small></a></li><li><a href="#network">Our impact<small>60+ groups</small></a></li></ul></div></div>

<section class="bigvideo"><div class="video" data-video="{VIMEO}">{img("crowd", "", "")}<div class="over"><div class="wrap"><span class="eyebrow" style="color:var(--yellow)">Watch</span><h2>The Alliance in action</h2></div></div><button class="play" aria-label="Play the Alliance sizzle reel video"><span aria-hidden="true">&#9654;</span></button></div><p class="vnote"><a href="{VIMEO_PAGE}">Watch on Vimeo</a></p></section>

<section class="light"><div class="wrap split"><div><span class="eyebrow" style="color:var(--teal-d)">Who we are</span><h2>The group made up of groups</h2><p>{WHO}</p>{lga_chips()}<p class="btnrow"><a class="btn btn-primary" href="#about">About the Alliance</a></p></div><div>{img("group-cheer", ALT["cheer"], "photo")}</div></div></section>

<section class="full">{img("cards", ALT["cards"], "bg")}<div class="wrap"><span class="eyebrow" style="color:var(--yellow)">What we have achieved</span><h2>Focus and impact</h2>{stats()}<div style="height:32px"></div>{pillars_list()}<p style="margin-top:32px"><b>Thanks to our partners</b></p>{partner_strip()}</div></section>

<section class="photogrid"><figure>{img("board", ALT["board"])}<figcaption><h3>Upcoming</h3><p>{GATHER[0][0]}: {GATHER[0][1]}</p><a href="#home">Gatherings</a></figcaption></figure>
<figure>{img("meeting", ALT["meeting"])}<figcaption><h3>Projects</h3><p>Three projects, funded by partners across government and philanthropy.</p><a href="#partners">See partners</a></figcaption></figure>
<figure>{img("workshop", ALT["table"])}<figcaption><h3>The R.A.C.K</h3><p>The resource hub for Alliance groups.</p><a href="#rack">Explore the R.A.C.K</a></figcaption></figure></section>

<section class="light"><div class="wrap"><span class="eyebrow" style="color:var(--teal-d)">Our partners</span><h2>Made possible together</h2>{partner_strip()}<p class="btnrow"><a class="btn btn-ghost" href="#partners">See all partners</a></p></div></section>
<section class="full">{img("hug", ALT["hug"], "bg")}<div class="wrap"><h2>Get involved</h2><p style="font-size:1.25rem;max-width:52ch">Local experience. Shared learning. Wider impact.</p>{cta_band()}</div></section>'''

    about = hero3("group-photo", ALT["group"], f'<span class="eyebrow" style="color:var(--yellow)">About us</span><h1>Local experience. Shared learning. Wider impact.</h1><p>{WHO}</p>') + f'''
<section class="light"><div class="wrap split"><div><h2>Vision</h2><p style="font-size:1.4rem;font-weight:700">{VISION}</p></div><div><h2>Purpose</h2><p>{PURPOSE}</p></div></div></section>
<section class="full">{img("line", ALT["line"], "bg")}<div class="wrap"><h2>Our journey</h2>{journey()}</div></section>
<section class="light"><div class="wrap split"><div><h2>How we learn</h2><p>Monitoring, Evaluation, Accountability and Learning.</p>{meal()}</div>{img("laughing", ALT["laugh"], "photo")}</div></section>
<section class="full green">{img("circle", ALT["circle"], "bg")}<div class="wrap"><blockquote>&ldquo;{QUOTE[0]}&rdquo;<cite>{QUOTE[1]}</cite></blockquote></div></section>
<section class="light"><div class="wrap"><h2>Our structure</h2><p>Steering committee, UCRH embedded researchers and the Network Lead, {CONTACT["name"]}. Names to be supplied.</p><h3>Common questions</h3>{faq()}</div></section>'''

    partners = hero3("speaker", ALT["speaker"], '<span class="eyebrow" style="color:var(--yellow)">Impact</span><h1>Our partners</h1><p>The funders, delivery partners and researchers behind community-led resilience.</p>') + f'''
<section class="light"><div class="wrap">{partner_groups()}</div></section>
<section class="full">{img("meeting", ALT["meeting"], "bg")}<div class="wrap"><h2>Projects they support</h2><ul class="cards">{projects_cards()}</ul></div></section>'''

    network = hero3("web", ALT["web"], '<span class="eyebrow" style="color:var(--yellow)">Network</span><h1>Groups across the Northern Rivers</h1><p>60+ grassroots, place-based groups working across five pillars.</p>') + f'''
<section class="mapfull">{map_embed()}</section>
<section class="light"><div class="wrap">{lga_chips()}<h2 style="margin-top:1.2em">Five pillars</h2>{pillars_list("pillars dk")}</div></section>
<section class="light" style="padding-top:0"><div class="wrap split"><div><h2>All groups</h2>{directory()}</div><div>{contact_form()}</div></div></section>'''

    rack = hero3("hall", ALT["pair"], f'<span class="eyebrow" style="color:var(--yellow)">Resources</span><h1>The R.A.C.K</h1><p>The online resource hub for the groups of the Alliance.</p>{rack_buttons()}') + f'''
<section class="light"><div class="wrap"><h2>What you will find inside</h2><ul class="cards">{rack_cards()}</ul>{gh_note()}</div></section>
<section class="full">{img("cards2", ALT["cards"], "bg")}<div class="wrap"><h2>Funding and grants</h2><ul class="cards"><li class="pcard"><h3>The HELP Fund</h3><p>Participatory grants for local groups.</p></li><li class="pcard"><h3>Establishment grants</h3><p>$3,000</p></li><li class="pcard"><h3>Resilience action grants</h3><p>Up to $10,000</p></li></ul>
<p style="margin-top:32px">Access is for Alliance groups. Need help getting in?</p><p class="btnrow"><a class="btn btn-primary" href="mailto:{CONTACT["email"]}">Contact the Network Lead</a></p></div></section>'''

    body = "".join([screen("home", "Home", home), screen("about", "About", about), screen("partners", "Partners", partners), screen("network", "Network", network), screen("rack", "R.A.C.K", rack)])
    return page_shell("NRCRA prototype 3: Heavy visuals", CSS3, body, "v3")


# ================================================================ dashboard
def dashboard():
    cards = [
        ("v1", "Prototype 1: Colour blocks", "Mood board 1. Bold navy, yellow, teal and orange blocks, big type, flat edges.", "swatch"),
        ("v2", "Prototype 2: Light and rounded", "Mood board 2. Light background, rounded content blocks, soft cards.", "rounded"),
        ("v3", "Prototype 3: Heavy visuals", "Mood board 3. Full-bleed photography, overlays, big video moment.", "photo"),
    ]
    out = ""
    for slug, t, d, _ in cards:
        links = "".join(f'<li><a href="{slug}/#{k}">{n}</a></li>' for k, n in PAGES)
        out += f'<article class="c"><h2><a href="{slug}/">{t}</a></h2><p>{d}</p><ul class="pl">{links}</ul></article>'
    return f'''<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NRCRA website prototypes</title><meta name="robots" content="noindex">{FONT}
<style>{TOKENS}body{{background:var(--tint)}}main{{max-width:1100px;margin:0 auto;padding:48px 20px}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px}}
.c{{background:#fff;padding:28px;border-top:8px solid var(--yellow)}}.c:nth-child(2){{border-color:var(--teal)}}.c:nth-child(3){{border-color:var(--orange)}}.c h2 a{{color:var(--navy);text-decoration:none}}
.pl{{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:8px}}.pl a{{display:block;padding:.4em .9em;border:2px solid var(--navy);color:var(--navy);text-decoration:none;font-weight:700}}.pl a:hover{{background:var(--navy);color:#fff}}</style></head>
<body><main><img src="assets/img/logo.png" alt="Northern Rivers Community Resilience Alliance" style="height:56px;margin-bottom:24px"><h1>Website prototypes</h1>
<p>Three directions for the five-page NRCRA website, one per mood board. Sample content only. Status: draft, for Round 1 direction review.</p><div class="grid">{out}</div>
<p class="vnote" style="margin-top:32px">Prototype of nrcra.org.au (Home, About, Partners, Network, R.A.C.K). Prepared by VeeMercado.com. client38.veemercado.com</p></main></body></html>'''


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
