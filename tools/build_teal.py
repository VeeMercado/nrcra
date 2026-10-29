"""Teal-led exploration (teal as accents and tints only): Home, About, Impact (blank) and Network on the designer's Layout Design wireframe
(content and layout only), styled from Prototype 1, with teal as the main driver instead of navy.

  prototype-b  teal as accents and tints only (highlights, buttons, borders, tinted panels), navy kept for the footer

White text never sits on teal (2.99:1). Navy text on teal is 5.05:1.
Imported by build.py, which owns the shared helpers and base CSS.
"""
import re
import build as B
from build import E, img, logo, screen, icon, BASE, MOBILE, JS, FONT, CSS1, VIMEO, CONTACT

SIGN_IN = "https://rack.nrcra.org.au"  # the R.A.C.K address NRCRA gave us (not live yet)
MENU = [("home", "Home"), ("network", "Network"), ("about", "About"), ("impact", "Impact")]
NAMES = {"prototype-a": "Prototype A", "prototype-b": "Prototype B"}
SHORT = {"prototype-a": "A", "prototype-b": "B"}


def nav3():
    links = "".join(f'<a href="#{k}" data-nav="{k}">{t}</a>' for k, t in MENU)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap head-in"><a href="#home" class="brand" aria-label="NRCRA home">{logo()}</a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav id="nav" aria-label="Main">{links}<a class="btn btn-cta" href="{SIGN_IN}" target="_blank" rel="noopener">Sign In</a></nav></div></header>'''


def protobar3(cur):
    others = "".join(f'<a class="pb-btn" data-proto="{k}" href="../{k}/" aria-label="{NAMES[k]}"><span class="pb-short" aria-hidden="true">{SHORT[k]}</span><span class="pb-long">{NAMES[k]}</span></a>' for k in NAMES if k != cur)
    return f'''<div class="protobar" role="region" aria-label="Prototype controls"><div class="pb-in">
<p class="pb-label"><b>MOCKUP &amp; PROTOTYPE ONLY</b> by <a href="https://veemercado.com">veemercado.com</a><span class="pb-cur"> &middot; viewing Round 2: {NAMES[cur]}</span></p>
<nav class="pb-nav" aria-label="Round 2 designs"><a class="pb-btn pb-all" href="../#round-2">All prototypes</a>{others}</nav>
<button type="button" class="pb-top" aria-label="Back to top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})"><span class="pb-long">Back to top&nbsp;</span><span aria-hidden="true">&uarr;</span></button></div></div>'''


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
    lgas = "".join(f"<li>{E(n)} LGA</li>" for n in ["Tweed", "Byron", "Ballina", "Lismore", "Kyogle", "Clarence", "Richmond"])
    partners = B.v1_partners().replace('href="#partners"', 'href="#impact"')
    return f'''<div class="hero1 herobg"><div class="wrap"><div class="h1-panel tpanel"><span class="eyebrow">Northern Rivers Community Resilience Alliance</span>
<h1>We believe when climate disasters hit, it&rsquo;s the <span class="mark">community{B.SQUIGGLE}</span> that steps up first.</h1><p class="lede">We are a network of grassroots, community-led groups working together to build disaster resilience across the Northern Rivers.</p>
<p class="btnrow"><a class="btn btn-primary" href="#about">Learn more</a></p></div>
<div class="h1-photo" data-video="{VIMEO}">{img("cheer", eager=True, alt="")}<button class="play" aria-label="Play the Alliance sizzle reel video, full screen"><span aria-hidden="true">&#9654;</span></button></div></div></div>

<section class="sec"><div class="wrap"><div class="card wwa surface"><div><span class="eyebrow">Who we are</span><h2>{hl("The group made up of groups")}</h2><p>{B.WHO}</p><h3>We&rsquo;re a network of 7 Local Government Areas (LGA)</h3><ul class="lgapills">{lgas}</ul>
<p class="btnrow"><a class="btn btn-ghost" href="#network">Explore our network</a></p></div><div class="wwa-map">{B.places_map()}</div></div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><div class="statcard"><span class="eyebrow">What we have achieved</span>{B.stats()}</div></div></section>

<section class="sec" style="padding-top:0" id="focus"><div class="wrap"><span class="eyebrow">In focus</span><h2 class="sechead">{hl("Upcoming, projects and the R.A.C.K")}</h2>
<ul class="kb"><li>{img("crowd")}<h3>{B.GATHER[0]}: {B.GATHER[1]}</h3><p>{B.GATHER[2]}.</p></li><li>{img("meeting")}<h3>Projects</h3><p>Connected and Prepared, Resourcing Community Resilience and Learning Together. <a href="#impact">Impact</a></p></li>
<li>{img("board")}<h3>The R.A.C.K</h3><p>{B.RACK_LINE} <a href="{SIGN_IN}">Sign In</a></p></li></ul></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><div class="card pcard2 surface">{partners}</div></div></section>
{part_band()}'''


# ---------------------------------------------------------------- About
MEAL6 = [("Includes Everyone", "People feel respected and able to participate.", "people"), ("Builds Trust", "Relationships and cooperation grow over time.", "connect"),
         ("Shares Power", "Groups influence priorities, leadership and decisions.", "share"), ("Builds Capability", "Groups gain skills, resources and confidence.", "grow"),
         ("Learns and Adapts", "Feedback leads to practical changes.", "improve"), ("Creates Collective Value", "Groups gain what they couldn’t achieve alone.", "strengthen")]


def team():
    roles = ["Network Lead", "Steering committee", "Steering committee", "UCRH researcher", "UCRH researcher", "UCRH researcher"]
    return '<ul class="team2">' + "".join(f'<li><span class="tc" aria-hidden="true">Photo</span><b>Name</b><span>{r}</span></li>' for r in roles) + '</ul><p class="vnote">Sample placeholders. Names and photos to come.</p>'


def about_body():
    return f'''<div class="wrap"><div class="splith rev"><div class="ph">{img("line", eager=True)}</div><div><span class="eyebrow">About us</span><h1>We&rsquo;re changing the Northern Rivers&rsquo; resilience culture</h1><p class="lede">{B.MORE}</p></div></div></div>
<section class="sec"><div class="wrap"><div class="card vp-wrap surface"><div><span class="script">Our goal</span><h2>Vision</h2><p>{B.VISION}</p><span class="script" style="margin-top:28px">Our why</span><h2>Purpose</h2><p>{B.PURPOSE}</p></div>
<div class="circles">{B.deco("rings", "")}{img("laughing", alt="")}{img("talk", alt="")}{img("circle", alt="")}<span class="blob" aria-hidden="true"></span></div></div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><span class="script">How we take action</span><h2 class="sechead">{hl("We have a MEAL plan")}</h2><p class="lede">Monitoring, Evaluation, Accountability and Learning. A healthy Resilience Alliance isn&rsquo;t just one that delivers projects. It&rsquo;s one where people feel included, power is shared, groups gain real value, and we can learn and adapt together.</p>
{B.meal()}<ul class="mealgrid">{"".join(f'<li>{icon(k)}<h3>{E(t)}</h3><p>{E(d)}</p></li>' for t, d, k in MEAL6)}</ul></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="card surface"><span class="script">Progress so far</span><h2 class="sechead">Our journey</h2>{B.journey("river")}</div></div></section>
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
.steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.steps li{display:grid;justify-items:center;gap:8px}.steps .ci{width:76px;height:76px;border-radius:50%;background:#fff;border:3px solid var(--ci);display:grid;place-items:center;color:var(--navy)}.steps .ci .ico{width:34px;height:34px}.steps a{font-weight:800}.steps p{margin:0;font-size:.95rem}
.steps li:nth-child(1){--ci:var(--orange)}.steps li:nth-child(2){--ci:var(--navy)}.steps li:nth-child(3){--ci:var(--navy)}.steps li:nth-child(4){--ci:var(--orange)}
@media(max-width:860px){.wwa,.statrow{grid-template-columns:1fr}.steps{grid-template-columns:1fr 1fr}.teal .card{padding:26px 20px}}
.teal .kb li{border-bottom:10px solid var(--kc)}.kb li:nth-child(1){--kc:var(--teal)}.kb li:nth-child(2){--kc:var(--yellow)}.kb li:nth-child(3){--kc:var(--orange)}
.splith{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;padding:36px 0 12px}.splith>*{min-width:0}.splith .ph img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:32px}.splith .ph .mapbox{height:380px;border-radius:32px}.splith.rev .ph{order:-1}
@media(max-width:860px){.splith{grid-template-columns:1fr}.splith.rev .ph{order:0}}
.script{font:700 1.5rem Caveat,cursive;color:var(--orange-d);display:block;margin-bottom:2px}
.vp-wrap{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}.vp-wrap>*{min-width:0}@media(max-width:860px){.vp-wrap{grid-template-columns:1fr}}
.circles{position:relative;height:440px}.circles img{position:absolute;border-radius:50%;object-fit:cover;border:8px solid #fff}
.circles img:nth-of-type(1){width:300px;height:300px;left:0;top:0}.circles img:nth-of-type(2){width:220px;height:220px;right:0;top:40px}.circles img:nth-of-type(3){width:200px;height:200px;left:150px;bottom:0}
.circles .blob{position:absolute;right:30px;bottom:30px;width:150px;height:150px;background:var(--yellow);border-radius:62% 38% 55% 45%/48% 60% 40% 52%}
.deco{position:absolute;pointer-events:none;width:150px;height:150px}.circles .deco-rings{z-index:0;width:190px;height:190px;left:40%;top:30%}
@media(max-width:760px){.circles{height:360px}.circles img:nth-of-type(1){width:220px;height:220px}.circles img:nth-of-type(2){width:160px;height:160px}.circles img:nth-of-type(3){width:150px;height:150px;left:90px}}
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
ol.river{position:relative;list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(5,1fr);gap:16px}
ol.river::before{content:"";position:absolute;left:0;right:0;top:26px;height:12px;border-radius:99px;background:var(--teal-25)}
ol.river li{position:relative;padding-top:64px;display:block}ol.river b{position:absolute;top:0;left:0;background:#fff;border:3px solid var(--teal);border-radius:99px;padding:.35em .9em;font-weight:900;color:var(--teal-d);font-size:1rem}
ol.river p{margin:0;font-size:.95rem}@media(max-width:860px){ol.river{grid-template-columns:1fr}ol.river::before{left:24px;right:auto;width:10px;top:0;bottom:0;height:auto}ol.river li{padding:0 0 0 70px;min-height:60px}ol.river b{left:0}}

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
.herobg{padding:0!important}
.herobg>.wrap:first-child{display:flex;align-items:center;max-width:none;padding:0;position:relative;min-height:640px}
.herobg .h1-photo{position:absolute;inset:0;border-radius:0;min-height:0}
.herobg .h1-panel{position:relative;z-index:2;max-width:580px;margin:56px 0 56px max(20px,calc((100vw - var(--wrap))/2 + 20px))}
.herobg .h1-photo .play{inset:auto;margin:0;z-index:3;top:50%;left:calc((max(20px,(100vw - var(--wrap))/2 + 20px) + 580px + 100%)/2);transform:translate(-50%,-50%)}

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
.mark{position:relative;display:inline-block}.mark .squig{position:absolute;left:0;right:0;bottom:-.25em;width:100%;height:.4em}
@media(min-width:601px){.herobg .h1-panel{padding:52px 44px}}
@media(max-width:600px){.tb .herobg>.wrap:first-child{display:flex;align-items:flex-start;min-height:calc(100vh - var(--hh,65px));min-height:calc(100svh - var(--hh,65px));padding:0}.tb .herobg .h1-panel{margin:0;padding:28px 20px 40px;max-width:none}.tb .herobg .h1-photo::after{background:linear-gradient(180deg,rgba(0,97,90,.94) 0%,rgba(0,97,90,.88) 30%,rgba(0,97,90,.5) 48%,rgba(0,97,90,0) 62%)}.herobg .h1-photo .play{inset:auto;left:50%;top:75%;transform:translate(-50%,-50%)}.herobg .h1-panel h1{font-size:1.75rem;line-height:1.15}.herobg .h1-panel .lede{font-size:1rem}.herobg .h1-panel .eyebrow{font-size:.72rem}}
.tb .h1-panel{background:var(--teal-25);color:var(--navy);border:4px solid var(--teal)}.tb .h1-panel h1,.tb .h1-panel .eyebrow{color:var(--navy)}.tb .h1-panel .btn-ghost{color:var(--navy);border-color:var(--navy);background:#fff}.tb .h1-panel .btn-ghost:hover{background:var(--navy);color:#fff}
.tb #nav a[aria-current=page]{background:var(--teal-25)}
.tb .surface{background:#fff;border-bottom:10px solid var(--teal)}.tb .statcard{background:#fff;border-bottom:10px solid var(--teal)}.tb .framed{--fr:var(--teal-25);outline:4px solid var(--teal);outline-offset:-4px}
.tb .kb li{background:#fff}.tb .kb a{color:var(--teal-d);font-weight:800}
.tb .partband{background:var(--teal-12);border-bottom:6px solid var(--teal)}.partband a:not(.btn):hover{background:var(--teal-25)}
.tb .ticker{background:var(--navy);color:var(--teal)}.tb .tk-in .tkd{color:var(--teal-25)}
.tb .site-foot{--foot-h:var(--teal)}
.tb .pmap{--land:#fff;--sea:var(--teal-12);--coast:var(--teal);--river:var(--teal)}
"""


def page(v):
    css, cls = CSS_B, "tb"
    body = "".join([screen("home", "Home", home_body()), screen("about", "About", about_body()), screen("impact", "Impact", impact_body()), screen("network", "Network", network_body())])
    return f'''<!doctype html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>NRCRA teal-led {NAMES[v]}</title><meta name="robots" content="noindex">
<meta name="description" content="Teal-led exploration of the NRCRA website. Sample content only.">
{FONT}<style>{BASE}{CSS1}{CSS_T}{css}{MOBILE}</style></head><body class="v1 teal {cls}">
{nav3()}<main id="main">{body}</main>{B.TICKER}{re.sub(r'<span class="foot-tag"><span class="tagline">.*?</span></span>', "", B.footer(True, boxed=True), flags=re.S)}{protobar3(v)}<script>{JS}</script></body></html>'''


# prototype-a/index.html is a frozen, hand-kept file (Prototype A). It is not built from build.py, so changes to Round 1 never reach it.
def main():
    B.write("prototype-b/index.html", page("prototype-b"))
