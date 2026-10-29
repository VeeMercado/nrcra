"""Teal-led exploration: Home, About, Impact (blank) and Network on the designer's Layout Design wireframe
(content and layout only), styled from Prototype 1, with teal as the main driver instead of navy.

  teal-a  solid teal for short lines (hero, header button, strips, footer), light teal for paragraphs
  teal-b  teal as accents and tints only (highlights, buttons, borders, tinted panels), navy kept for the footer

White text never sits on teal (2.99:1). Navy text on teal is 5.05:1.
Imported by build.py, which owns the shared helpers and base CSS.
"""
import build as B
from build import E, img, logo, screen, icon, BASE, MOBILE, JS, FONT, CSS1, VIMEO, CONTACT

SIGN_IN = "https://rack.nrcra.org.au"  # the R.A.C.K address NRCRA gave us (not live yet)
MENU = [("home", "Home"), ("about", "About"), ("impact", "Impact"), ("network", "Network")]
OTHER = {"teal-a": "teal-b", "teal-b": "teal-a"}
NAMES = {"teal-a": "Teal A", "teal-b": "Teal B"}


def nav3():
    links = "".join(f'<a href="#{k}" data-nav="{k}">{t}</a>' for k, t in MENU)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap head-in"><a href="#home" class="brand" aria-label="NRCRA home">{logo()}</a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav id="nav" aria-label="Main">{links}<a class="btn btn-cta" href="{SIGN_IN}" target="_blank" rel="noopener">Sign In</a></nav></div></header>'''


def protobar3(cur):
    o = OTHER[cur]
    return f'''<div class="protobar" role="region" aria-label="Prototype controls"><div class="pb-in">
<p class="pb-label"><b>MOCKUP &amp; PROTOTYPE ONLY</b> by <a href="https://veemercado.com">veemercado.com</a><span class="pb-cur"> &middot; viewing {NAMES[cur]}</span></p>
<nav class="pb-nav" aria-label="Teal versions"><a class="pb-btn pb-all" href="../#round-2">All prototypes</a><a class="pb-btn" data-proto="{o}" href="../{o}/" aria-label="{NAMES[o]}"><span class="pb-short" aria-hidden="true">{NAMES[o][-1]}</span><span class="pb-long">{NAMES[o]}</span></a><a class="pb-btn" data-proto="v1" href="../v1/" aria-label="Prototype 1, the navy version"><span class="pb-short" aria-hidden="true">P1</span><span class="pb-long">Prototype 1</span></a></nav>
<button type="button" class="pb-top" aria-label="Back to top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})"><span class="pb-long">Back to top&nbsp;</span><span aria-hidden="true">&uarr;</span></button></div></div>'''


def hl(t):
    return f'<span class="hl">{E(t)}</span>'


def steps():
    st = [("people", "Join the network", "Bring your group into the Alliance.", "#network", "Find out how"), ("cal", "Come to a gathering", f"{B.GATHER[0]}: {B.GATHER[1]}.", "#home", "Upcoming"),
          ("share", "Share knowledge", "Add what works to the R.A.C.K.", SIGN_IN, "The R.A.C.K"), ("hand", "Partner with us", "Fund or research community-led resilience.", "#impact", "Impact")]
    return '<ol class="steps">' + "".join(f'<li><span class="ci">{icon(i)}</span><b>{E(t)}</b><p>{E(d)}</p><a href="{h}">{E(l)}</a></li>' for i, t, d, h, l in st) + "</ol>"


def part_band():
    return f'<section class="partband"><div class="wrap"><h2>How you can be part of it</h2>{steps()}</div></section>'


# ---------------------------------------------------------------- Home
def home_body():
    lgas = "".join(f"<li>{E(n)} LGA</li>" for n in ["Tweed", "Byron", "Ballina", "Lismore", "Kyogle", "Clarence", "Richmond"])
    partners = B.v1_partners().replace('href="#partners"', 'href="#impact"')
    return f'''<div class="hero1"><div class="wrap"><div class="h1-panel tpanel"><span class="eyebrow">Northern Rivers Community Resilience Alliance</span>
<h1>When disaster strikes, local people are always first to respond.</h1><p class="lede">{B.H1}.</p>
<p class="btnrow"><a class="btn btn-primary" href="#about">Learn more</a><a class="btn btn-ghost" href="mailto:{CONTACT["email"]}">Contact us</a></p></div>
<div class="h1-photo hvid" data-video="{VIMEO}">{img("speaker", eager=True, alt="")}<button class="play" aria-label="Play the Alliance sizzle reel video, full screen"><span aria-hidden="true">&#9654;</span></button><span class="vtag">Watch the sizzle reel</span></div></div></div>

<section class="sec"><div class="wrap"><div class="card wwa surface"><div><span class="eyebrow">Who we are</span><h2>{hl("The group made up of groups")}</h2><p>{B.WHO}</p><h3>We&rsquo;re a network of 7 Local Government Areas (LGA)</h3><ul class="lgapills">{lgas}</ul>
<p class="btnrow"><a class="btn btn-ghost" href="#network">Explore our network</a></p></div><div class="wwa-map">{B.places_map()}</div></div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap statrow"><div class="statcard"><span class="eyebrow">What we have achieved</span>{B.stats()}</div><div class="framed">{img("cheer")}</div></div></section>

<section class="sec" style="padding-top:0" id="focus"><div class="wrap"><span class="eyebrow">In focus</span><h2 class="sechead">{hl("Upcoming, projects and the R.A.C.K")}</h2>
<ul class="kb"><li>{img("crowd")}<h3>{B.GATHER[0]}: {B.GATHER[1]}</h3><p>{B.GATHER[2]}.</p></li><li>{img("meeting")}<h3>Projects</h3><p>Connected and Prepared, Resourcing Community Resilience and Learning Together. <a href="#impact">Impact</a></p></li>
<li>{img("board")}<h3>The R.A.C.K</h3><p>{B.RACK_LINE} <a href="{SIGN_IN}">Sign In</a></p></li></ul></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><div class="card pcard2 surface">{partners}</div></div></section>
{part_band()}'''


# ---------------------------------------------------------------- About
MEAL6 = [("Includes Everyone", "People feel respected and able to participate.", "people"), ("Builds Trust", "Relationships and cooperation grow over time.", "connect"),
         ("Shares Power", "Groups influence priorities, leadership and decisions.", "share"), ("Builds Capability", "Groups gain skills, resources and confidence.", "grow"),
         ("Learns and Adapts", "Feedback leads to practical changes.", "improve"), ("Creates Collective Value", "Groups gain what they couldn’t achieve alone.", "strengthen")]


def journey_h():
    out = '<ol class="htl">'
    for y, t in B.JOURNEY:
        out += f'<li><span class="hstop">{E(y)}</span><div class="hcard"><p>{E(t)}</p></div></li>'
    return out + "</ol>"


def team():
    roles = ["Network Lead", "Steering committee", "Steering committee", "UCRH researcher", "UCRH researcher", "UCRH researcher"]
    return '<ul class="team2">' + "".join(f'<li><span class="tc" aria-hidden="true">Photo</span><b>Name</b><span>{r}</span></li>' for r in roles) + '</ul><p class="vnote">Sample placeholders. Names and photos to come.</p>'


def about_body():
    return f'''<div class="wrap"><div class="splith rev"><div class="ph">{img("line", eager=True)}</div><div><span class="eyebrow">About us</span><h1>We&rsquo;re changing the Northern Rivers&rsquo; resilience culture</h1><p class="lede">{B.MORE}</p></div></div></div>
<section class="sec"><div class="wrap"><div class="card vp-wrap surface"><div><span class="script">Our goal</span><h2>Vision</h2><p>{B.VISION}</p><span class="script" style="margin-top:28px">Our why</span><h2>Purpose</h2><p>{B.PURPOSE}</p></div>
<div class="cluster">{img("circle", "c1", alt="")}{img("house", "c2", alt="")}{img("talk", "c3", alt="")}<i class="b1" aria-hidden="true"></i><i class="b2" aria-hidden="true"></i></div></div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><span class="script">How we take action</span><h2 class="sechead">{hl("We have a MEAL plan")}</h2><p class="lede">Monitoring, Evaluation, Accountability and Learning. A healthy Resilience Alliance isn&rsquo;t just one that delivers projects. It&rsquo;s one where people feel included, power is shared, groups gain real value, and we can learn and adapt together.</p>
{B.meal()}<ul class="mealgrid">{"".join(f'<li>{icon(k)}<h3>{E(t)}</h3><p>{E(d)}</p></li>' for t, d, k in MEAL6)}</ul></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="card surface"><span class="script">Progress so far</span><h2 class="sechead">Our journey</h2>{journey_h()}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="card surface"><h2 class="sechead">Meet the team</h2>{team()}</div></div></section>
{part_band()}'''


# ---------------------------------------------------------------- Network
def pillar_cards():
    return '<ol class="pillcards">' + "".join(f'<li><span class="pi">{icon(k)}</span><span class="pn">{i:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p></li>' for i, (t, d, k) in enumerate(B.PILLARS, 1)) + "</ol>"


def group_cards():
    ph = ["crowd", "laughing", "listening", "cards", "table", "pair", "talk", "house"]
    n = 0
    items = ""
    for p, gs in B.PILLAR_GROUPS.items():
        for name, area, lga in gs:
            items += f'<li data-lga="{lga}" data-pillar="{E(p)}"><span class="gph">{img(ph[n % len(ph)], alt="")}<span class="gdot" aria-hidden="true">{name[-1]}</span></span><b>{E(name)}</b><span>{area}, {lga}</span><em>{E(p)}</em><small>Group description to come.</small></li>'
            n += 1
    lopts = "".join(f"<option>{l}</option>" for l in B.LGAS)
    popts = "".join(f"<option>{E(p[0])}</option>" for p in B.PILLARS)
    return f'''<div class="dir"><div class="filters"><label>Location <select data-f="lga"><option value="">All locations</option>{lopts}</select></label>
<label>Pillar <select data-f="pillar"><option value="">All pillars</option>{popts}</select></label><label class="dq">Search <input type="search" data-f="q" placeholder="Group name or town"></label></div>
<ul class="gdir gdir-c">{items}</ul><p class="empty" hidden>No groups match those filters.</p><p class="vnote">Sample groups. Real names and areas come from the Alliance member list.</p></div>'''


def network_body():
    return f'''<div class="wrap"><div class="splith"><div><span class="eyebrow">Network</span><h1>{B.NET_H1}</h1><p class="lede">7 council areas across the Northern Rivers region of New South Wales, Australia.</p></div><div class="ph">{B.map_embed()}</div></div></div>
<section class="sec"><div class="wrap"><span class="eyebrow">Our focus</span><h2 class="sechead">{hl("Five pillars")}</h2><p class="lede">{B.CALLOUT} We connect them using these five key pillars.</p>{pillar_cards()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="card surface"><h2 class="sechead">All groups</h2>{group_cards()}</div></div></section>
{part_band()}'''


def impact_body():
    return '<div class="wrap"><div class="pg-head"><h1>Impact</h1></div></div>'


# ---------------------------------------------------------------- CSS
CSS_T = """
body.teal{--bg:#f3f6f7}
.teal .sechead{margin-bottom:28px}
.hl{background:linear-gradient(transparent 56%,var(--teal) 56%,var(--teal) 94%,transparent 94%);padding:0 .12em;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.teal .card{border-radius:var(--r);padding:36px}
.wwa{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center}.wwa>*{min-width:0}.wwa-map{max-width:420px;justify-self:center;width:100%}
.lgapills{list-style:none;margin:0 0 6px;padding:0;display:flex;flex-wrap:wrap;gap:8px}.lgapills li{border:2px solid var(--navy);border-radius:99px;padding:.2em .8em;font-weight:700;font-size:.95rem;background:#fff}
.statrow{display:grid;grid-template-columns:1.1fr .9fr;gap:24px;align-items:center}.statrow>*{min-width:0}.statcard{border-radius:var(--r);padding:36px}.statcard .stats dt{color:var(--navy)}
.framed{border-radius:36px;padding:14px;background:var(--fr,var(--teal))}.framed img{border-radius:24px;width:100%;aspect-ratio:4/3;object-fit:cover}
.pcard2 .p3{align-items:center}
.partband{padding:56px 0 52px;text-align:center}.partband h2{margin-bottom:24px}
.steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,1fr);gap:20px}.steps li{display:grid;justify-items:center;gap:8px}.steps .ci{width:76px;height:76px;border-radius:50%;background:#fff;border:3px solid var(--ci);display:grid;place-items:center;color:var(--navy)}.steps .ci .ico{width:34px;height:34px}.steps a{font-weight:800;color:var(--navy)}.steps p{margin:0;font-size:.95rem}
.steps li:nth-child(1){--ci:var(--orange)}.steps li:nth-child(2){--ci:var(--navy)}.steps li:nth-child(3){--ci:var(--navy)}.steps li:nth-child(4){--ci:var(--orange)}
@media(max-width:860px){.wwa,.statrow{grid-template-columns:1fr}.steps{grid-template-columns:1fr 1fr}.teal .card{padding:26px 20px}}
.teal .kb li{border-top:10px solid var(--kc)}.kb li:nth-child(1){--kc:var(--teal)}.kb li:nth-child(2){--kc:var(--yellow)}.kb li:nth-child(3){--kc:var(--orange)}
.splith{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;padding:36px 0 12px}.splith>*{min-width:0}.splith .ph img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:32px}.splith .ph .mapbox{height:380px;border-radius:32px}.splith.rev .ph{order:-1}
@media(max-width:860px){.splith{grid-template-columns:1fr}.splith.rev .ph{order:0}}
.script{font:700 1.5rem Caveat,cursive;color:var(--orange-d);display:block;margin-bottom:2px}
.vp-wrap{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}.vp-wrap>*{min-width:0}@media(max-width:860px){.vp-wrap{grid-template-columns:1fr}}
.cluster{position:relative;aspect-ratio:1;max-width:460px;margin:0 auto;width:100%}.cluster img,.cluster i{position:absolute;border-radius:50%;object-fit:cover}.cluster .c1{width:62%;height:62%;left:0;top:6%;border:6px solid #fff}.cluster .c2{width:42%;height:42%;right:0;top:0;border:6px solid #fff}.cluster .c3{width:38%;height:38%;left:30%;bottom:0;border:6px solid #fff}
.cluster .b1{width:30%;height:30%;right:4%;bottom:6%;background:var(--teal)}.cluster .b2{width:12%;height:12%;left:58%;top:52%;background:var(--yellow)}
.meal{margin:18px 0 22px}.mealgrid{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(6,1fr);gap:12px}.mealgrid li{background:var(--grey-6);border-radius:18px;padding:18px 14px}.mealgrid .ico{width:34px;height:34px;color:var(--navy);margin-bottom:8px}.mealgrid h3{font-size:1rem;margin:0 0 .3em}.mealgrid p{margin:0;font-size:.9rem}
@media(max-width:1000px){.mealgrid{grid-template-columns:repeat(3,1fr)}}@media(max-width:560px){.mealgrid{grid-template-columns:1fr 1fr}}
.htl{list-style:none;margin:30px 0 0;padding:0;display:grid;grid-template-columns:repeat(5,1fr);gap:18px;position:relative}.htl::before{content:"";position:absolute;left:10%;right:10%;top:36px;border-top:4px dotted rgba(7,41,59,.55)}
.htl li{position:relative;display:flex;flex-direction:column;align-items:center;gap:14px}.hstop{position:relative;z-index:2;width:76px;height:76px;border-radius:50%;display:grid;place-items:center;background:#fff;border:6px solid var(--bc);font-weight:900;text-align:center;font-size:.95rem;line-height:1.05}
.htl li:nth-child(1){--bc:var(--teal)}.htl li:nth-child(2){--bc:var(--yellow)}.htl li:nth-child(3){--bc:var(--orange)}.htl li:nth-child(4){--bc:var(--navy)}.htl li:nth-child(5){--bc:var(--teal)}
.hcard{background:#fff;border-radius:18px;padding:16px;width:100%;height:100%}.hcard p{margin:0;font-size:.95rem}
@media(max-width:1000px){.htl{grid-template-columns:repeat(3,1fr);row-gap:28px}.htl::before{display:none}}@media(max-width:640px){.htl{grid-template-columns:1fr}}
.team2{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;justify-content:center;gap:24px}.team2 li{width:150px;text-align:center;display:grid;justify-items:center;gap:4px}.team2 .tc{width:96px;height:96px;border-radius:50%;background:var(--teal-25);display:grid;place-items:center;font-weight:800;font-size:.9rem}.team2 li span:not(.tc){font-size:.9rem;color:var(--muted)}
.pillcards{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:16px;justify-content:center}.pillcards li{flex:1 1 200px;max-width:230px;background:#fff;border-radius:18px 18px 22px 22px;padding:0 18px 22px;text-align:center;border-top:14px solid var(--pc)}
.pillcards li:nth-child(1){--pc:var(--teal)}.pillcards li:nth-child(2){--pc:var(--yellow)}.pillcards li:nth-child(3){--pc:var(--orange)}.pillcards li:nth-child(4){--pc:var(--navy)}.pillcards li:nth-child(5){--pc:#9fb0b8}
.pillcards .pi{width:52px;height:52px;border-radius:50%;background:var(--grey-6);display:grid;place-items:center;margin:-26px auto 6px;color:var(--navy)}.pillcards .pi .ico{width:28px;height:28px}.pillcards .pn{font-weight:900;font-size:.85rem;letter-spacing:.1em}.pillcards h3{margin:.3em 0}.pillcards p{margin:0;font-size:.95rem}
.gdir-c{grid-template-columns:repeat(auto-fill,minmax(220px,1fr))!important;gap:16px!important}.gdir-c li{padding:0 0 16px!important;background:#fff!important;border:1px solid var(--line);border-radius:20px!important;overflow:hidden}.gdir-c .gph{display:block;position:relative;margin-bottom:34px}.gdir-c .gph img{width:100%;height:100px;object-fit:cover}
.gdir-c .gdot{position:absolute;left:14px;bottom:-24px;width:48px;height:48px;border-radius:50%;background:var(--teal);color:var(--navy);border:3px solid #fff;display:grid;place-items:center;font-weight:900}.gdir-c b,.gdir-c span:not(.gph):not(.gdot),.gdir-c em,.gdir-c small{margin:0 16px}.gdir-c small{color:var(--muted);margin-top:6px}
.pg-head{padding:48px 0 40px}.pg-head h1{margin:0}
/* brand colour dos and don'ts (see brand-contrast): pins keep a 3px white gap from teal lines, solid colours only behind short lines */
.teal .pmap .dot circle{stroke-width:3}
"""

CSS_A = """
/* A: solid teal for short lines, light teal for paragraphs */
.ta .h1-panel{background:var(--teal);color:var(--navy)}.ta .h1-panel h1,.ta .h1-panel .eyebrow{color:var(--navy)}.ta .h1-panel .btn-ghost{color:var(--navy);border-color:var(--navy)}.ta .h1-panel .btn-ghost:hover{background:var(--navy);color:#fff}
.ta .btn-cta{background:var(--teal);color:var(--navy);border-color:var(--navy)}.ta .btn-cta:hover{background:var(--navy);color:#fff}
.ta .site-head{border-bottom:6px solid var(--teal)}.ta #nav a[aria-current=page]{background:var(--teal-25)}
.ta :is(.h1-panel,.partband,.ticker,.site-foot) :focus-visible{outline-color:var(--navy)}
.ta .surface{background:var(--teal-12);border-top:10px solid var(--teal)}.ta .statcard{background:var(--teal-25);border-top:10px solid var(--teal)}.ta .framed{--fr:var(--teal)}
.ta .kb li{background:var(--teal-12)}.ta .kb li:nth-child(2){background:var(--yellow-20)}.ta .kb li:nth-child(3){background:var(--orange-12)}.ta .kb a{color:var(--navy);font-weight:800}
.ta .pcard2 .p3-logos li{background:#fff}.ta .mealgrid li{background:#fff}.ta .meal li{background:#fff}
.ta .partband{background:var(--teal);color:var(--navy)}.ta .steps li{--ci:var(--navy)!important}.ta .h1-panel .btn-primary{border-color:var(--navy)}
.ta .site-foot .ack{background:var(--teal-12);border-radius:18px;padding:18px 20px;border-top:8px solid var(--navy)}
.ta .ticker{background:var(--yellow);color:var(--navy)}.ta .tk-in .tkd{color:var(--navy)}
.ta .site-foot{--foot:var(--teal);--foot-ink:var(--navy);--foot-h:var(--navy);--foot-line:rgba(7,41,59,.4)}.ta .site-foot a{text-decoration:underline}
.ta .pmap{--land:#fff;--sea:var(--teal-25);--coast:var(--teal);--river:var(--teal)}
"""

CSS_B = """
/* B: teal as accents and tints only, navy kept for the footer */
.tb .h1-panel{background:var(--teal-25);color:var(--navy);border:4px solid var(--teal)}.tb .h1-panel h1,.tb .h1-panel .eyebrow{color:var(--navy)}.tb .h1-panel .btn-ghost{color:var(--navy);border-color:var(--navy)}.tb .h1-panel .btn-ghost:hover{background:var(--navy);color:#fff}
.tb .btn-primary,.tb .btn-cta{background:var(--teal);color:var(--navy);border-color:var(--teal)}.tb .btn-primary:hover,.tb .btn-cta:hover{background:var(--navy);color:#fff;border-color:var(--navy)}
.tb .btn-cta{border-color:var(--navy)}.tb #nav a[aria-current=page]{background:var(--teal-25)}
.tb .surface{background:#fff;border-top:10px solid var(--teal)}.tb .statcard{background:#fff;border-left:10px solid var(--teal)}.tb .framed{--fr:var(--teal-25);outline:4px solid var(--teal);outline-offset:-4px}
.tb .kb li{background:#fff}.tb .kb a{color:var(--teal-d);font-weight:800}
.tb .partband{background:var(--teal-12);border-top:6px solid var(--teal);border-bottom:6px solid var(--teal)}
.tb .ticker{background:var(--navy);color:var(--teal)}.tb .tk-in .tkd{color:var(--teal-25)}
.tb .site-foot{--foot-h:var(--teal)}
.tb .pmap{--land:#fff;--sea:var(--teal-12);--coast:var(--teal);--river:var(--teal)}
"""


def page(v):
    css = CSS_A if v == "teal-a" else CSS_B
    cls = "ta" if v == "teal-a" else "tb"
    body = "".join([screen("home", "Home", home_body()), screen("about", "About", about_body()), screen("impact", "Impact", impact_body()), screen("network", "Network", network_body())])
    return f'''<!doctype html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>NRCRA teal-led {NAMES[v]}</title><meta name="robots" content="noindex">
<meta name="description" content="Teal-led exploration of the NRCRA website. Sample content only.">
{FONT}<style>{BASE}{CSS1}{CSS_T}{css}{MOBILE}</style></head><body class="v1 teal {cls}">
{nav3()}<main id="main">{body}</main>{B.TICKER}{B.footer(True, boxed=True)}{protobar3(v)}<script>{JS}</script></body></html>'''


def main():
    B.write("teal-a/index.html", page("teal-a"))
    B.write("teal-b/index.html", page("teal-b"))
