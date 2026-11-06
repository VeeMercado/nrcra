"""Brand red, yellow and teal contrast guidance: one standalone page.
Imported by build.py, which owns the shared helpers and base CSS."""
import re
import build as B
from build import BASE, FONT

# ---------------------------------------------------------------- brand red and yellow: contrast guidance (single page)
def _lum(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])


def _ratio(a, b):
    la, lb = _lum(a), _lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


# pairings that pass the ratio but are marked NO: navy on brand teal is hard to tell apart for some people with colour blindness
CB_NO = {("#07293b", "#00a79d")}
# pairings shown as "LARGE only": they pass 3:1 but not 4.5:1
LARGE_ONLY = {("#ffffff", "#f05a28")}
# pairings that pass the ratio but use black, which is off brand
OFF_BRAND = {("#000000", "#f05a28")}


def _row(fg, bg, fgname, bgname):
    r = _ratio(fg, bg)
    url = f"https://webaim.org/resources/contrastchecker/?fcolor={fg[1:].upper()}&bcolor={bg[1:].upper()}"
    n = "pass" if r >= 4.5 else "fail"
    l = "pass" if r >= 3 else "fail"
    nt, lt = n.title(), l.title()
    key = (fg.lower(), bg.lower())
    extra = ""
    if key in CB_NO or key in OFF_BRAND:
        n = l = "fail"
        nt = lt = "Not recommended"
        extra = "<br><small>off brand</small>" if key in OFF_BRAND else ""
    return (f'<tr><td><span class="chip" style="color:{fg};background:{bg}">Aa</span> {fgname} on {bgname}</td><td><b>{r:.2f}:1</b>{extra}</td>'
            f'<td class="{n}">{nt}</td><td class="{l}">{lt}</td><td><a href="{url}">Check in WebAIM</a></td></tr>')


def combo(RED, TEAL, NAVY, WHITE, YEL):
    r = _ratio(RED, TEAL)
    rows = _row(RED, TEAL, "Red text", "teal") + _row(TEAL, RED, "Teal text", "red") + _row(NAVY, TEAL, "Navy text", "teal") + _row(NAVY, RED, "Navy text", "red")
    sim = "".join(f'<figure><div class="pair" style="filter:{f}"><span style="background:{RED}"></span><span style="background:{TEAL}"></span></div><figcaption>{n}</figcaption></figure>' for n, f in [("Normal vision", "none"), ("Greyscale", "url(#f-grey)"), ("Protanopia (no red cones)", "url(#f-prot)"), ("Deuteranopia (no green cones)", "url(#f-deut)"), ("Tritanopia (no blue cones)", "url(#f-trit)")])
    return f'''<section class="blk" id="teal-orange"><h2>Does teal work with red?</h2>
<p>Not side by side. Red <code>{RED.upper()}</code> and teal <code>{TEAL.upper()}</code> are opposite hues, but they are almost the same lightness, so the contrast between them is only <b>{r:.2f}:1</b>. Anything that needs 3:1 against its neighbour (text, icons, chart segments, button edges) fails when one sits on the other.</p>
<table><thead><tr><th>Pairing</th><th>Ratio</th><th>Body text (4.5:1)</th><th>Large text (3:1)</th><th>WebAIM</th></tr></thead><tbody>{rows}</tbody></table>
<h3 style="margin-top:22px">Seen by different eyes</h3><div class="pairs">{sim}</div>
<p class="vnote">Simulated with standard colour-matrix filters. In greyscale the two squares become nearly the same grey, so red and teal depend on hue alone to tell them apart.</p>
<ul><li><b>Never:</b> red text on teal, teal text on red, or a red shape touching a teal shape with no gap that carries meaning (for example a two-colour chart or status).</li>
<li><b>Fine:</b> red and teal as separate blocks with their own navy text, as in the Connect, Share, Care band, where each colour has yellow or a gap between it and the next. Navy text works on both.</li>
<li><b>If they must touch:</b> separate them with a navy or white line, at least 3px wide.</li></ul></section>'''


BTN_CSS = r""".bpair{display:grid;grid-template-columns:1fr 1fr;gap:18px}.set{border-radius:20px;padding:22px;border:2px solid var(--line)}.set h3{margin-top:0}.row{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin:0 0 14px}
.mbtn{display:inline-flex;align-items:center;justify-content:center;font:800 1rem var(--font);padding:.7em 1.3em;border-radius:12px;min-height:44px}.mbtn{background:var(--bg);color:var(--fg);border:2px solid var(--bd);cursor:pointer}.mbtn:hover,.mbtn.is-hover{background:var(--hbg);color:var(--hfg);border-color:var(--hbd)}.mbtn:active,.mbtn.is-active{background:var(--abg);color:var(--afg);border-color:var(--abd)}.mbtn:focus-visible{outline:3px solid var(--orange-d);outline-offset:3px}.krow{display:grid;gap:6px;margin:0 0 16px}.kl{font-weight:800;font-size:.9rem;display:flex;gap:10px;align-items:center;flex-wrap:wrap}.sts{display:flex;gap:14px;flex-wrap:wrap}.st{display:grid;justify-items:start;gap:4px}.st small{font-size:.75rem;font-weight:700;opacity:.85}.lk{color:var(--lc);text-decoration:underline;text-decoration-color:var(--ld);text-underline-offset:4px;text-decoration-thickness:2px;font-weight:700;padding:.1em .3em;border-radius:6px}.lk:hover,.lk.is-hover{color:var(--lh);text-decoration-thickness:4px}.lk:active,.lk.is-active{background:var(--lt);color:#07293b}.mnav .push{margin-left:auto;padding:0}.mn{color:var(--mc);text-decoration:none;font-weight:700;padding:.45em .9em;border-radius:12px;display:inline-block}.mn:hover,.mn.is-hover{background:#f3f9f8;color:#07293b;text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:6px}.mn:active,.mn.is-active{background:var(--mt);color:#07293b}.mnav{display:flex;flex-wrap:wrap;gap:6px;align-items:center;border-radius:14px;padding:8px;margin-top:6px;font-weight:700}.mnav>span{padding:.45em .9em;border-radius:12px}.mnav .mbtn{padding:.45em 1em;min-height:0}.lteal{border:2px solid var(--line);border-radius:20px;padding:20px;background:#fff}.lteal h3{margin-top:0}.ltcard{border-radius:16px;padding:16px 18px;margin-top:12px;color:#07293b}
.rt{font-size:.8rem;font-weight:800;border-radius:99px;padding:.15em .7em;background:#fff;border:2px solid}.rt.ok{color:#1f6b35;border-color:#1f6b35}.rt.bad{color:#a3201a;border-color:#a3201a}
"""

def brand_contrast():
    NAVY, WHITE, BLACK, RED, YEL, TEAL = "#07293b", "#ffffff", "#000000", "#f05a28", "#ffcb2a", "#00a79d"
    def block(name, bg):
        rows = "".join(_row(fg, bg, n, name) for fg, n in [(WHITE, "White text"), (NAVY, "Navy text"), (BLACK, "Black text")])
        rows += "".join(_row(bg, b, name + " text", n) for b, n in [(WHITE, "white")])
        return f'<section class="blk" id="{name}"><h2>Brand {name} <code>{bg.upper()}</code></h2><table><thead><tr><th>Pairing</th><th>Ratio</th><th>Body text (4.5:1)</th><th>Large text (3:1)</th><th>WebAIM</th></tr></thead><tbody>{rows}</tbody></table></section>'
    para = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    return f'''<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Brand guidelines</title><meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noai, noimageai">{FONT}
<style>{BASE}html{{scroll-padding-top:84px}}body{{background:#f3f6f7;padding-top:64px}}.topnav{{position:fixed;top:0;left:0;right:0;z-index:50;background:#fff;border-bottom:1px solid var(--line)}}.topnav>ul{{list-style:none;margin:0 auto;padding:10px 20px;max-width:1240px;display:flex;flex-wrap:wrap;gap:8px}}:root{{--btn-r:12px}}.topnav>ul>li>a,.topnav .cat{{display:inline-flex;align-items:center;gap:.45em;min-height:44px;padding:0 1.1em;border:2px solid var(--navy);border-radius:12px;color:var(--navy);font:inherit;font-weight:800;text-decoration:none;cursor:pointer;background:#fff}}.topnav>ul>li>a:hover,.topnav .cat:hover{{background:var(--navy);color:#fff}}.topnav .cat:focus-visible,.topnav .menu a:focus-visible{{outline:3px solid #07293b;outline-offset:2px}}.topnav .n-y{{background:var(--yellow)}}.topnav .n-r{{background:var(--orange);color:#fff;font-size:1.2rem}}.topnav .n-t{{background:#00857c;color:#fff}}.topnav .n-d{{background:var(--navy);color:#fff}}.topnav .n-y:hover,.topnav .n-r:hover,.topnav .n-t:hover,.topnav .n-d:hover{{background:#fff;color:var(--navy)}}.topnav .back{{margin-left:auto}}@media(max-width:900px){{.topnav>ul>li>a,.topnav .cat{{min-height:40px;padding:0 .8em;font-size:.9rem}}.topnav .bl{{display:none}}}}@media(max-width:560px){{body{{padding-top:112px}}html{{scroll-padding-top:132px}}}}main{{max-width:1240px;margin:0 auto;padding:36px 20px 56px}}
.flag{{display:inline-block;background:#111;color:#ffcb2a;font-weight:900;letter-spacing:.06em;border-radius:99px;padding:.35em 1em;font-size:.85rem;margin-bottom:14px}}.flag a{{color:#fff}}
#colours table{{table-layout:fixed}}#colours th:nth-child(1){{width:21%}}#colours th:nth-child(2){{width:13%}}#colours th:nth-child(4),#colours th:nth-child(5){{width:13%}}#colours th:nth-child(3){{width:auto}}.logodemo{{display:flex;flex-wrap:wrap;align-items:flex-end;gap:18px 32px;margin:18px 0 0}}.logodemo .cs small,.csrow .cs small{{font-size:.8rem;color:var(--muted)}}.csrow{{display:flex;flex-wrap:wrap;gap:18px;margin:18px 0 0}}.cs{{display:grid;gap:8px;justify-items:center;font-size:.85rem}}.cs span{{display:block;width:84px;height:84px;background:var(--teal);border-radius:12px}}.pagesec{{font-size:clamp(1.9rem,4vw,2.4rem);margin:40px 0 12px}}.rule{{background:#fff;border-left:10px solid var(--orange);border-radius:20px;padding:22px 26px;margin:22px 0}}.rule p{{margin:0}}
.blk,.card2{{background:#fff;border-radius:28px;padding:28px;margin:0 0 22px}}.blk{{overflow-x:auto;position:relative}}table{{width:100%;border-collapse:collapse;font-size:.95rem}}th,td{{text-align:left;padding:10px 8px;border-bottom:1px solid var(--line)}}th{{font-size:.8rem;text-transform:uppercase;letter-spacing:.06em}}
.chip{{display:inline-grid;place-items:center;width:44px;height:32px;border-radius:8px;font-weight:900;vertical-align:middle;border:1px solid rgba(7,41,59,.25)}}.pass{{color:#1f6b35;font-weight:800}}.fail{{color:#a3201a;font-weight:800}}code{{font-size:.85em;background:var(--grey-6);padding:.1em .4em;border-radius:6px}}
.demo{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}}.demo>div{{border-radius:20px;padding:22px;border:2px solid var(--line)}}.demo h3{{margin-top:0}}.dont{{border-color:#a3201a!important}}.do{{border-color:#1f6b35!important}}
.big{{border-radius:16px;padding:18px;margin:0 0 10px}}.by{{background:var(--yellow);color:#fff}}.br{{background:var(--orange);color:#fff}}.bt{{background:var(--teal);color:#fff}}
.hl{{background:linear-gradient(transparent 56%,var(--yellow) 56%,var(--yellow) 94%,transparent 94%);padding:0 .12em}}.pill{{display:inline-block;background:var(--orange);color:#fff;font-weight:800;font-size:1.2rem;border-radius:99px;padding:.3em 1em}}
.pill2{{display:inline-block;background:var(--navy);color:var(--yellow);font-weight:800;font-size:1.2rem;border-radius:99px;padding:.3em 1em}}.lt{{border-radius:16px;padding:18px;margin:0 0 12px;color:var(--navy);font-weight:600}}.lt span{{display:block}}.lt small{{display:block;margin-top:8px;font-weight:800;font-size:.8rem}}.l-w{{background:#fff;border:2px solid var(--line)}}.l-g{{background:#f3f6f7;border:2px solid var(--line)}}.tint{{border-radius:16px;padding:18px;margin:0 0 12px;color:var(--navy);font-weight:600}}.tint span{{display:block}}.tint small{{display:block;margin-top:8px;font-weight:800;font-size:.8rem;color:var(--navy)}}.t-y{{background:#ffeaaa;border-top:8px solid var(--yellow)}}.t-r{{background:#fbd6c9;border-bottom:8px solid var(--orange)}}.t-t{{background:#beddda;border-top:8px solid var(--teal)}}.opt{{margin:0 0 12px}}.opt small{{display:block;font-weight:800;color:var(--muted);font-size:.8rem;text-transform:uppercase;letter-spacing:.06em}}.hlt{{background:linear-gradient(transparent 56%,var(--teal) 56%,var(--teal) 94%,transparent 94%)}}.hlr{{background:linear-gradient(transparent 56%,var(--orange) 56%,var(--orange) 94%,transparent 94%)}}.pill4{{display:inline-block;background:#00857c;color:#fff;font-weight:800;font-size:1.2rem;border-radius:99px;padding:.3em 1em}}.pill3{{display:inline-block;background:var(--teal);color:var(--navy);font-weight:800;font-size:1.2rem;border-radius:99px;padding:.3em 1em}}.pairs{{display:flex;flex-wrap:wrap;gap:18px}}.pairs figure{{margin:0}}.pair{{display:flex;width:160px;height:70px;border-radius:12px;overflow:hidden}}.pair span{{flex:1}}.pairs figcaption{{font-size:.85rem;margin-top:6px;max-width:160px}}.bar{{height:12px;border-radius:99px;background:var(--orange);margin:10px 0 16px;max-width:200px}}.ex>*{{margin-bottom:14px}}
{BTN_CSS}
.topnav .n-b{{border-style:dashed}}
.topnav .dd{{position:relative}}.topnav .cat .car{{font-size:.75em}}.topnav .menu{{display:none;position:absolute;top:100%;left:0;margin:6px 0 0;padding:6px;min-width:280px;max-width:calc(100vw - 24px);list-style:none;flex-direction:column;gap:2px;background:#fff;border:2px solid var(--navy);border-radius:12px;box-shadow:0 10px 28px rgba(7,41,59,.22);z-index:60}}.topnav .menu::before{{content:"";position:absolute;left:0;right:0;top:-10px;height:10px}}.topnav .dd.open .menu{{display:flex}}@media(hover:hover){{.topnav .dd:hover .menu{{display:flex}}}}.topnav .menu a{{display:flex;align-items:center;min-height:44px;padding:0 .9em;border-radius:8px;color:var(--navy);font-weight:700;text-decoration:none}}.topnav .menu a:hover{{background:#f3f9f8;text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:5px}}.sw{{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin:14px 0}}.sw>div{{border-radius:20px;padding:22px;font-weight:800}}.sw b{{display:block;font-size:2rem}}.sw small{{display:block;font-weight:700;margin-top:6px}}.sw code{{background:#fff;color:#07293b}}.yn{{display:inline-block;font-size:.68rem;font-weight:900;letter-spacing:.08em;line-height:1;padding:.4em .75em;border-radius:6px;border:1px solid rgba(7,41,59,.3);vertical-align:middle;margin-left:4px}}.warn{{color:#8a5a00;font-weight:800}}.sr{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}.vfail{{background:#a3201a;color:#fff;padding:.15em .6em;border-radius:6px;box-decoration-break:clone;-webkit-box-decoration-break:clone}}.vpass{{text-decoration:underline;text-decoration-color:#07293b;text-decoration-thickness:4px;text-underline-offset:5px}}.swatch{{display:inline-block;width:34px;height:24px;border-radius:6px;border:1px solid rgba(7,41,59,.3);vertical-align:middle}}@media(max-width:700px){{.sw{{grid-template-columns:1fr}}}}
@media(max-width:1150px){{.demo{{grid-template-columns:1fr 1fr}}}}@media(max-width:700px){{.demo{{grid-template-columns:1fr}}}}@media(max-width:760px){{table{{font-size:.85rem}}}}
/* text follows the brand type scale: 56, 38, 24, 20, 16 and 12 (labels only); weights 400 and 800 */
h1{{font-size:clamp(2.375rem,5vw,3.5rem);font-weight:800}}h2,h2.pagesec{{font-size:clamp(1.875rem,4vw,2.375rem);font-weight:800}}h3{{font-size:1.25rem;font-weight:800}}
.lede{{font-size:1.25rem}}p,td,li,table code,p code,.vnote,.kl,.vpass,.vfail,table small,.blk p,.topnav .menu a{{font-size:1rem}}
th,.yn,.flag,.topnav .cat .car,td small,table small{{font-size:.75rem;font-weight:800}}
.topnav .cat,.topnav a,.btn,b,.kl,.vpass,.vfail,.flag,.chip{{font-weight:800}}.topnav .cat{{font-size:1rem}}
small,figcaption,.pill,.pill2,.pill3,.pill4,.pill5{{font-size:.75rem!important;font-weight:800}}nav a,nav span,header a{{font-weight:800}}.cs b{{font-size:1rem}}.ltcard,.ltcard *{{font-size:1rem}}.demo span[class^=lo],.demo p span{{font-weight:400}}
small,span.rt,.mnav span,.mnav a,.topnav .menu a{{font-weight:800!important}}span.rt{{font-size:.75rem!important}}.mnav span{{font-size:1rem!important}}
@media(max-width:760px){{table{{font-size:1rem}}}}</style></head>
<body><nav class="topnav" aria-label="On this page"><ul><li class="dd"><button type="button" class="cat n-d" aria-expanded="false" aria-controls="m-brand">Brand Colours <span class="car" aria-hidden="true">&#9662;</span></button><ul class="menu" id="m-brand"><li><a href="#colours">Brand colours</a></li><li><a href="#text">Text colours</a></li><li><a href="#contrast">Brand colour contrast</a></li></ul></li><li class="dd"><button type="button" class="cat n-d" aria-expanded="false" aria-controls="m-dos">Do&rsquo;s and Don&rsquo;ts <span class="car" aria-hidden="true">&#9662;</span></button><ul class="menu" id="m-dos"><li><a href="#dos">Do&rsquo;s and Don&rsquo;ts</a></li><li><a href="#guidelines">Type, spacing, corners</a></li></ul></li><li class="dd"><button type="button" class="cat n-t" aria-expanded="false" aria-controls="m-teal">Teal <span class="car" aria-hidden="true">&#9662;</span></button><ul class="menu" id="m-teal"><li><a href="#teal-adjust">Teal adjustment</a></li><li><a href="#teal">Teal contrast</a></li><li><a href="#lightteal">Light teal and pale teal</a></li><li><a href="#teal-orange">Does teal work with orange?</a></li><li><a href="#teal-buttons">Teal buttons</a></li></ul></li><li class="dd"><button type="button" class="cat n-r" aria-expanded="false" aria-controls="m-orange">Orange <span class="car" aria-hidden="true">&#9662;</span></button><ul class="menu" id="m-orange"><li><a href="#red">Orange contrast</a></li><li><a href="#teal-orange">Does teal work with orange?</a></li></ul></li><li class="dd"><button type="button" class="cat n-y" aria-expanded="false" aria-controls="m-yellow">Yellow <span class="car" aria-hidden="true">&#9662;</span></button><ul class="menu" id="m-yellow"><li><a href="#yellow">Yellow contrast</a></li><li><a href="#yellow-buttons">Yellow buttons</a></li></ul></li><li class="back"><a href="../">&larr; <span class="bl">Back to </span>prototypes</a></li></ul></nav><svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><filter id="f-grey" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0.2126 0.7152 0.0722 0 0 0.2126 0.7152 0.0722 0 0 0.2126 0.7152 0.0722 0 0 0 0 0 1 0"/></filter><filter id="f-prot" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0.567 0.433 0 0 0 0.558 0.442 0 0 0 0 0.242 0.758 0 0 0 0 0 1 0"/></filter><filter id="f-deut" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0.625 0.375 0 0 0 0.7 0.3 0 0 0 0 0.3 0.7 0 0 0 0 0 1 0"/></filter><filter id="f-trit" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0.95 0.05 0 0 0 0 0.433 0.567 0 0 0 0.475 0.525 0 0 0 0 0 1 0"/></filter></defs></svg><main><span class="flag">MOCKUP &amp; PROTOTYPE ONLY &middot; by <a href="https://veemercado.com">veemercado.com</a></span>
<h1>Brand guidelines</h1>
{brand_colours()}
<h2 class="pagesec" id="contrast">Brand colour contrast</h2>
<p class="lede">Contrast ratios for the brand orange (<code>{RED.upper()}</code>), yellow (<code>{YEL.upper()}</code>) and teal (<code>{TEAL.upper()}</code>) against white, navy and black text. Ratios use the WCAG formula, the same one the <a href="https://webaim.org/resources/contrastchecker/">WebAIM Contrast Checker</a> uses, and each row links to WebAIM with the colours filled in.</p>
<div class="rule"><p><b>Red &amp; teal elements.</b> To maintain readability, red and teal shouldn&rsquo;t be used as background colours for large chunks of text, as standard text colours (white, navy or black) won&rsquo;t pass contrast requirements. They work well for smaller accents, like title backgrounds. For teal backgrounds, <a href="#teal-adjust">see the recommended colour adjustments</a>.</p></div>
{teal_adjust()}
{block("teal", TEAL)}
{light_teal()}
{block("red", RED)}{block("yellow", YEL)}{combo(RED, TEAL, NAVY, WHITE, YEL)}
<section class="card2"><h2>What this means</h2><ul><li><b>Yellow:</b> white text fails everywhere ({_ratio(WHITE, YEL):.2f}:1). Navy passes comfortably ({_ratio(NAVY, YEL):.2f}:1), so yellow is safe for buttons and title backgrounds with navy text.</li>
<li><b>Red:</b> white fails for body text ({_ratio(WHITE, RED):.2f}:1) and only passes as large text. Navy is {_ratio(NAVY, RED):.2f}:1, just under 4.5:1, so it only passes when the text is large (24px, or bold from about 19px). Black does pass ({_ratio(BLACK, RED):.2f}:1) but is off brand.</li>
<li><b>Teal:</b> white text is {_ratio(WHITE, TEAL):.2f}:1, which fails even as large text (it needs 3:1). Navy is {_ratio(NAVY, TEAL):.2f}:1, which passes the ratio, but it is not recommended: navy and this teal are hard to tell apart for some people with colour blindness. Black passes ({_ratio(BLACK, TEAL):.2f}:1) but is off brand.</li>
<li><b>As text colour:</b> red on white is {_ratio(RED, WHITE):.2f}:1, yellow on white is {_ratio(YEL, WHITE):.2f}:1 and teal on white is {_ratio(TEAL, WHITE):.2f}:1, so none of them works for words on a white page.</li>
<li><b>Adjusted teal:</b> because brand teal fails with white text, the prototypes use a slightly darker teal, <code>#00857C</code> (white text {_ratio(WHITE, "#00857c"):.2f}:1), for buttons and any area with white text. Brand teal stays for borders, dots and text on navy. See <a href="#teal-adjust">Recommended colour adjustments</a>.</li></ul></section>
<section class="card2" id="dos"><h2>Don&rsquo;t and do</h2><div class="demo"><div class="dont"><h3>Don&rsquo;t: large blocks of text</h3><p class="big by">{para}</p><p class="big br">{para}</p><p class="big bt">{para}</p></div>
<div class="do tints"><h3>Do: large blocks of text</h3><p class="tint t-y"><span>{para}</span><small>Navy on light yellow: {_ratio(NAVY, "#ffeaaa"):.2f}:1</small></p><p class="tint t-r"><span>{para}</span><small>Navy on light red: {_ratio(NAVY, "#fbd6c9"):.2f}:1</small></p><p class="tint t-t"><span>{para}</span><small>Navy on light teal: {_ratio(NAVY, "#beddda"):.2f}:1</small></p><p class="vnote">Lighter tint of the brand colour as the background, navy text, and the solid brand colour as a top or bottom border.</p></div>
<div class="do ex"><h3>Do: small accents</h3><p class="opt"><small>Option 1</small><span class="hl" style="font-weight:900;font-size:1.5rem">Navy title with a yellow highlight</span></p><p class="opt"><small>Option 2</small><span class="hl hlt" style="font-weight:900;font-size:1.5rem">Navy title with a teal highlight</span></p><p class="opt"><small>Option 3</small><span class="hl hlr" style="font-weight:900;font-size:1.5rem">Navy title with a red highlight</span></p><p><a class="btn btn-primary" href="#">Yellow button, navy text</a></p><p><span class="pill">Red pill, white bold large text</span></p><p><span class="pill2">Navy background, yellow text</span></p><p><span class="pill4">Darker teal background, white text</span><small class="vnote" style="display:block">Darker teal #00857C, white text {_ratio("#ffffff", "#00857c"):.2f}:1</small></p><div class="bar" aria-hidden="true"></div><p style="margin:0">Body copy stays navy on white or on a light tint. Red and yellow stay as the accent.</p></div>
<div class="do lights"><h3>Do: large blocks of text on a light background</h3><p class="lt l-w"><span>{para}</span><small>Navy on white <code>#FFFFFF</code>: {_ratio(NAVY, "#ffffff"):.2f}:1</small></p><p class="lt l-g"><span>{para}</span><small>Navy on light grey <code>#F3F6F7</code>: {_ratio(NAVY, "#f3f6f7"):.2f}:1</small></p><p class="vnote">The white and light grey used for the page and cards in Prototype 1. Navy body text, and the brand colours only as small accents.</p></div></div></section>
{text_colours()}
{button_sections()}
{guidelines()}
<script data-cfasync="false">(function(){{var n=document.querySelector(".topnav");function f(){{var h=n.offsetHeight;document.body.style.paddingTop=h+"px";document.documentElement.style.scrollPaddingTop=(h+16)+"px"}}f();addEventListener("resize",f);
var dds=[].slice.call(document.querySelectorAll(".topnav .dd"));
function closeAll(x){{dds.forEach(function(d){{if(d!==x){{d.classList.remove("open");d.querySelector(".cat").setAttribute("aria-expanded","false")}}}})}}
dds.forEach(function(d){{var b=d.querySelector(".cat"),m=d.querySelector(".menu");
b.addEventListener("click",function(e){{e.stopPropagation();var o=!d.classList.contains("open");closeAll(d);d.classList.toggle("open",o);b.setAttribute("aria-expanded",o?"true":"false");if(o){{m.style.left="";var r=m.getBoundingClientRect();if(r.right>innerWidth-8)m.style.left=(innerWidth-8-r.right)+"px"}}}});
m.addEventListener("click",function(e){{if(e.target.closest("a"))closeAll()}})}});
document.addEventListener("click",function(){{closeAll()}});
document.addEventListener("keydown",function(e){{if(e.key==="Escape"){{var o=dds.filter(function(d){{return d.classList.contains("open")}})[0];closeAll();if(o)o.querySelector(".cat").focus()}}}})}})()</script>
</main></body></html>'''




# ---------------------------------------------------------------- button, link and text colour sets (review page)
NAVY_, WHITE_, GREY_, LIGHT_ = "#07293b", "#ffffff", "#586c74", "#f3f6f7"
FAMILIES = [
    # name, colour, text on colour, light tint (selected menu item), link colour on white, note
    ("Teal", "#00857c", WHITE_, "#beddda", "#00857c", "The adjusted teal. Darker than brand teal (#00a79d) so white text passes."),
    ("Yellow", "#ffcb2a", NAVY_, "#ffeaaa", NAVY_, "Brand yellow. Navy text; yellow itself never carries text on white."),
]


def _chip(fg, bg, big=False):
    r = _ratio(fg, bg)
    need = 3 if big else 4.5
    ok = r >= need
    return f'<span class="rt {"ok" if ok else "bad"}">{r:.2f}:1 {"pass" if ok else "fail"}{" (large)" if big and ok and r < 4.5 else ""}</span>'


def _kinds(name, c, tx, tint, dark):
    navy, white = NAVY_, "#ffffff"
    sec_bd = c if name != "Yellow" else navy
    if not dark:
        return {"Primary": [(c, tx, navy), (navy, white, navy), (tint, navy, navy)],
                "Secondary": [(white, c if name == "Teal" else navy, sec_bd), (navy, white, navy), (tint, navy, navy)],
                "Tertiary": [(navy, white, navy), (c, tx, navy), (tint, navy, navy)]}
    return {"Primary": [(c, tx, white), (white, navy, white), (tint, navy, white)],
            "Secondary": [(white, navy, white), (c, tx, white), (tint, navy, white)],
            "Tertiary": [("transparent", white, white), (white, navy, white), (tint, navy, white)]}


def _b(label, trip, state, big):
    d, h, a = trip
    st = (f"--bg:{d[0]};--fg:{d[1]};--bd:{d[2]};--hbg:{h[0]};--hfg:{h[1]};--hbd:{h[2]};--abg:{a[0]};--afg:{a[1]};--abd:{a[2]};" + ("font-size:1.2rem;" if big else ""))
    cls = "mbtn" + (" is-hover" if state == 1 else " is-active" if state == 2 else "")
    return f'<span class="{cls}" tabindex="0" style="{st}">{label}</span>'


def _lk(label, lc, lh, ld, tint, state):
    cls = "lk" + (" is-hover" if state == 1 else " is-active" if state == 2 else "")
    return f'<a href="#" onclick="return false" class="{cls}" style="--lc:{lc};--lh:{lh};--ld:{ld};--lt:{tint}">{label}</a>'


def _set(name, c, tx, tint, link, note, dark):
    bg = NAVY_ if dark else WHITE_
    fg = "#fff" if dark else NAVY_
    big = name == "Red"  # red labels only pass as large bold text
    K = _kinds(name, c, tx, tint, dark)
    rows = ""
    for kind in ("Primary", "Secondary", "Tertiary"):
        chip = _chip(K[kind][0][1], K[kind][0][0], big) if K[kind][0][0] != "transparent" else ""
        rows += f'<div class="krow"><span class="kl">{kind} {chip}</span><div class="sts">' + "".join(f'<div class="st">{_b(kind, K[kind], i, big)}<small>{n}</small></div>' for i, n in enumerate(("Default", "Hover", "Active"))) + "</div></div>"
    lc = "#ffffff" if dark else link
    lh = tint if dark else NAVY_
    ld = c if (name == "Yellow" and not dark) else "currentColor"
    rows += f'<div class="krow"><span class="kl">Link {_chip(lc, bg)}</span><div class="sts">' + "".join(f'<div class="st">{_lk("Link text", lc, lh, ld, tint, i)}<small>{n}</small></div>' for i, n in enumerate(("Default", "Hover", "Active"))) + "</div></div>"
    mfg = "#ffffff" if dark else NAVY_
    rows += f'<div class="krow"><span class="kl">Menu item {_chip(mfg, bg)}</span><div class="sts">' + "".join(f'<div class="st"><a href="#" onclick="return false" class="mn{" is-hover" if i == 1 else " is-active" if i == 2 else ""}" style="--mc:{mfg};--mt:{tint}">Network</a><small>{n}</small></div>' for i, n in enumerate(("Default", "Hover", "Active"))) + "</div></div>"
    nav_cur = f"background:{tint};color:{NAVY_}"
    nav = (f'<div class="mnav" style="background:{bg};color:{fg}"><span style="{nav_cur}">Home</span><span>Network</span><span>About</span><span>Progress</span>'
           f'<span class="push">{_b("Sign In", K["Primary"], None, big)}</span></div>')
    return f'''<div class="set {"dark" if dark else "light"}" style="background:{bg};color:{fg}"><h3 style="color:{fg}">{name} on {"navy" if dark else "white"}</h3>{rows}{nav}</div>'''


def light_teal():
    import colorsys
    def hue(h):
        r, g, b = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        a, l, sat = colorsys.rgb_to_hls(r, g, b)
        return f"hue {round(a * 360)}, saturation {round(sat * 100)}%"
    pale, mid = "#f3f9f8", "#beddda"
    demo = f'''<div class="lteal"><h3>In the NRCRA Prototype</h3>
<div class="mnav" style="background:#fff;color:{NAVY_}"><span style="background:{mid};color:{NAVY_}">Home</span><span>Network</span><span>About</span><span>Progress</span></div>
<div class="ltcard" style="background:{pale};border-bottom:10px solid #00a79d"><b>Pale teal <code>{pale.upper()}</code></b><br>{hue(pale)}. Navy text {_ratio(NAVY_, pale):.2f}:1</div>
<div class="ltcard" style="background:{mid};border-bottom:10px solid #00a79d"><b>Light teal <code>{mid.upper()}</code></b><br>{hue(mid)}. Navy text {_ratio(NAVY_, mid):.2f}:1</div></div>'''
    return f'''<section class="blk" id="lightteal"><h2>Light teal and pale teal</h2><p>The three project PDFs use two light teals. <b>Pale teal</b>, <code>#F3F9F8</code>, is for large pale panels and for hover on the menu and links. <b>Light teal</b>, <code>#BEDDDA</code>, is for the selected menu item, pressed buttons and tinted panels. Both are soft, slightly grey greens, so they sit comfortably next to yellow and red.</p>{demo}</section>'''


def text_colours():
    texts = [(NAVY_, WHITE_, "Navy on white", "default text"), (GREY_, WHITE_, "#586c74 on white", "quiet text, where it matters"), (GREY_, LIGHT_, "#586c74 on #f3f6f7", "quiet text on light grey"),
             (WHITE_, NAVY_, "White on navy", "text on dark"), (LIGHT_, NAVY_, "#f3f6f7 on navy", "text on dark"), (WHITE_, "#00857c", "White on adjusted teal", "text on teal"), (LIGHT_, "#00857c", "#f3f6f7 on adjusted teal", "text on teal")]
    rows = "".join(f'<tr><td><span class="chip" style="color:{f};background:{b}">Aa</span> {l}</td><td>{n}</td><td><b>{_ratio(f, b):.2f}:1</b></td><td class="{"pass" if _ratio(f, b) >= 4.5 else "fail"}">{"Pass" if _ratio(f, b) >= 4.5 else "Fail"}</td></tr>' for f, b, l, n in texts)
    return f'''<section class="blk" id="text"><h2>Text colours</h2><p>Navy for text. <code>#586c74</code> for quiet text on white where it matters. White and <code>#f3f6f7</code> on darker backgrounds.</p>
<table><thead><tr><th>Pairing</th><th>Use</th><th>Ratio</th><th>Body text (4.5:1)</th></tr></thead><tbody>{rows}</tbody></table></section>'''


def _tick(fg, bg):
    r = _ratio(fg, bg)
    key = (fg.lower(), bg.lower())
    cb = key in CB_NO
    large = key in LARGE_ONLY
    ok = r >= 4.5 and not cb and not large
    cls = "pass" if ok else "warn" if large else "fail"
    sym = "&#10003;" if ok else "~" if large else "&#10007;"
    word = "YES" if ok else "LARGE only" if large else "NO"
    note = ", passes the ratio but not recommended for colour blindness" if cb else ", passes as large text only (3:1)" if large else ""
    spoken = "recommended" if ok else "recommended for large text only" if large else "not recommended" + (" for colour blindness" if cb else "")
    return (f'<td class="{cls}" title="{r:.2f}:1{note}"><span aria-hidden="true">{sym}</span> '
            f'<span class="yn" style="background:{bg};color:{fg}">{word}</span><span class="sr"> {spoken}, {r:.2f} to 1</span></td>')


def _hex_table(rows):
    body = "".join(f'<tr><td><span class="swatch" style="background:{h}"></span> {n}</td><td><code>{h.upper()}</code></td><td>{u}</td>{_tick(NAVY_, h)}{_tick(WHITE_, h)}</tr>' for n, h, u in rows)
    return f'<table><thead><tr><th>Colour</th><th>Hex</th><th>Used for</th><th>Navy text</th><th>White text</th></tr></thead><tbody>{body}</tbody></table><p class="vnote"><b class="pass">&#10003; YES</b> recommended: the text colour shown on this background passes AA for body text (4.5:1 or more). <b class="warn">~ LARGE only</b> passes only for large text (24px, or bold from about 19px; 3:1 or more). <b class="fail">&#10007; NO</b> not recommended: it falls short. Hover a cell for the exact ratio.</p>'


def brand_colours():
    main4 = [("Yellow", "#ffcb2a", "Highlights and small accents, with navy text"), ("Navy", NAVY_, "Text, footer, dark backgrounds"),
             ("Orange", "#f05a28", "Small accents"), ("Teal", "#00a79d", "Borders, dots and accents; text on navy only")]
    others = [("Adjusted teal", "#00857c", "Buttons and any area with white text"), ("Darker yellow", "#B38C00", "The word Share on Home and the yellow circles in the MEAL cycle. Use where brand yellow is too light to read on a light background"), ("Quiet text", GREY_, "Small supporting text on white, light grey, pale teal and light yellow. Also the arrows in the MEAL cycle."),
              ("White", WHITE_, "Cards and page"), ("Light grey", LIGHT_, "Page background"),
              ("Pale teal", "#f3f9f8", "Large pale panels, from the PDFs"), ("Light teal", "#beddda", "Selected menu item, hover, tinted panels, from the PDFs"),
              ("Light yellow", "#ffeaaa", "Tint for large text blocks (guidance examples)"), ("Light red", "#fbd6c9", "Tint for large text blocks (guidance examples)")]
    return f'''<section class="blk" id="colours"><h2>Brand colours</h2>
<h3>Main 4 brand colours</h3>{_hex_table(main4)}
<p class="vnote"><b class="fail">&#10007; NO</b> for navy on teal: it reaches {_ratio(NAVY_, "#00a79d"):.2f}:1, but navy and this teal are hard to tell apart for some people with colour blindness, so we do not recommend the pairing.</p>
<h3 style="margin-top:30px">Adjusted teal, darker yellow, quiet text, white and the light colours</h3>{_hex_table(others)}</section>'''


def _gl_table(head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


def guidelines():
    type_rows = [
        ("Page title (H1)", "56 (3.5rem)", "38 (2.375rem)", "800", "1.12", "-0.01em", "clamp(2.375rem, 5vw, 3.5rem)", "One per page, under the pill above it"),
        ("Section title (H2)", "38 (2.375rem)", "30 (1.875rem)", "800", "1.12", "-0.01em", "clamp(1.875rem, 4vw, 2.375rem)", "Opens each band of a page"),
        ("Card title and list item title (H3)", "24 (1.5rem)", "22 (1.375rem)", "800", "1.12", "-0.01em", "clamp(1.375rem, 2.4vw, 1.5rem)", "Titles inside cards and in long lists, such as the Privacy Policy"),
        ("Small title", "20 (1.25rem)", "20 (1.25rem)", "800", "1.3", "normal", "fixed", "RACK cards, small tiles. Same size as the lead paragraph, but bold."),
        ("Lead paragraph", "20 (1.25rem)", "20 (1.25rem)", "400", "1.6", "normal", "fixed", "Under a page title. Not bold."),
        ("Body text", "16 (1rem)", "16 (1rem)", "400", "1.6", "normal", "fixed", "All paragraphs. Same size as button text."),
        ("Button text", "16 (1rem)", "16 (1rem)", "800", "normal (about 1.4)", "normal", "fixed", "Buttons, menu items, footer links and links styled as buttons, everywhere on the site. Sentence case: capital first letter on the first word only, and on names such as RACK. Examples: Learn about us, Find out more, Back to top, Sign in, Our network, Privacy policy. Exceptions: the small buttons inside charts (View score, View rating), which follow the chart, and the small buttons Back to top and Visit page, which are 11px and 38px high."),
        ("Pill tag above titles (smallest text)", "12 (0.75rem)", "12 (0.75rem)", "800", "1.3", "normal", "fixed, uppercase", "The only text between 12 and 16px, also used for the Thanks to our funders line and the funder chip names. Capitals on the pills, no extra letter spacing, always centred in the pill. The Draft tags on the Privacy Policy stay at 16px."),
        ("Footer base line", "11 (0.6875rem)", "11 (0.6875rem)", "400 (Back to Top 800)", "1.6", "normal", "fixed", "The copyright and Privacy Policy line and the Back to Top button at the very bottom of the footer. The smallest text on the site, the steering committee names under their logos, the country names on the Network cards, and the text of the small buttons (Back to top, Visit page)."),
    ]
    pad_rows = [
        ("Section (band)", "0 top, 60px bottom (96px on Network and Home partners, 130px on About and the pages above the footer)", "Same", "Space below a band is its bottom padding. Content sits on the 980px wide column."),
        ("Content card (cards, chart cards, tiles)", "26px top and bottom, 20px left and right", "Same", "28px corners. About story cards 18px sides, 24px bottom."),
        ("Home header text card", "60px", "31px top, 40px bottom", "Matches the section gap"),
        ("Square card (steering committee)", "20px", "20px", "16px corners"),
        ("Button", "8px top and bottom, 17.6px left and right", "Same", "12px corners, 16px text"),
        ("Pill tag above titles", "3.2px top and bottom, 12.8px right, 10.4px left", "Same", "28px high, fully round, 12px uppercase text"),
        ("Funder chip (Thanks to our funders)", "0 top and bottom, about 16px left and right", "Same", "40px high (36px at 1100px wide and below), fully round, white fill, Light teal #BEDDDA border, Pale teal #F3F9F8 on hover"),
        ("Header menu bar", "0 (height set by the 50px logo and the buttons)", "Same", "Sticks to the top"),
        ("Footer", "52px top, 32px bottom", "Same", "Teal band"),
    ]
    margin_rows = [
        ("Page title (H1) to text below", "19px bottom", "19px bottom", "Fluid with the title size"),
        ("Section title (H2) to text below", "15px bottom", "15px bottom", ""),
        ("Card title (H3) to text below", "11px bottom", "11px bottom", ""),
        ("Paragraph to next paragraph", "20px bottom (lead), 14px top (Privacy Policy)", "Same", "Body paragraphs are spaced by this bottom margin, not by empty lines"),
        ("Note under the map or intro", "16px top", "16px top", "Same as the card gap"),
    ]
    special_rows = [
        ("Line spacing", "Titles 1.12, small titles and tags 1.3, lead and body text 1.6", "Set as a multiple of the font size, never in px. Each style's value is in the Title and text sizes table."),
        ("Letter spacing", "Page, section and card titles are tightened by 0.01em. All other text is normal.", "Uppercase pill tags have none"),
        ("Quotes", "Italic, 400, 20px", "Italic is used only for quotes. Quote marks are curly: &ldquo; and &rdquo;"),
        ("Apostrophes and dashes", "Curly apostrophe (&rsquo;). No long dashes: use a full stop, comma or the word to.", "Applies to all copy"),
        ("Special characters", "Arrows in buttons and menus and the bullets are drawn icons, not typed characters.", "Do not type arrow or bullet characters"),
        ("Numbers and dates", "Dates written 28 November 2026. Percentages with the % sign and no space: 75%.", "Australian English"),
    ]
    corner_rows = [
        ("Buttons, menu items, drop-downs, social icon buttons, the Aboriginal flag in the footer", "12px", "Every clickable control is a rounded square. The menu highlight covers the label and its arrow. The footer flag (60 x 40) uses the same 12px."),
        ("Hero cards, cards, chart cards, tiles, header photos, the map and the Draft policy box", "28px", "One shared radius for every large surface, on desktop, tablet and phone"),
        ("Pictures inside a padded card, steering committee tiles, dropdown menus", "16px", "Smaller surfaces nested inside a card or on the page"),
        ("Funder logo chips under the timeline entries", "20px", "Small white boxes, 40px high (36px at 1100px wide and below), one logo each"),
        ("Pills", "Fully round (99px)", "Only the tag above a page title, the Draft tags and the colour bars. Never for buttons."),
        ("Round photos and initial circles", "50%", "See Circle photo sizes"),
        ("Chart bars and squares", "4px", "Inside charts only. The chart's View score and View rating button group has 6px corners."),
    ]
    space_rows = [
        ("Site content width", "980px, centred (Wix Classic maximum)", "The menu, every page and the footer sit inside one 980px column. On screens narrower than 1020px the column keeps a 20px gutter each side. Coloured bands and backgrounds run the full width of the screen behind it. Full width sections: the page headers, Our timeline (About), Thanks to our funders (Home), the team (About), the five RACK cards and Our stories (Network). Their content stretches across the screen with a gutter of 20 to 56px each side."),
        ("Between sections", "60px", "Top and bottom of every band, on every page. Same as the Home header text card padding."),
        ("Large bands", "96px", "White bands on About and Network, and the space under Our Focus on Home"),
        ("Partners band on Home", "96px above, 115px below", "The Thanks to our funders band"),
        ("Large spacing", "130px", "The big gap used around the green divider lines on About, between sections on About, above the footer on About, Network, RACK, Progress and the group pages, and on Progress above each section title and between the header and the white band. Use this whenever a large space is needed."),
        ("Gap between cards, tiles and buttons", "16px", "Always 16px: grids and lists of cards, tiles and rows of buttons, and the chart cards on Progress"),
        ("Gap between text and picture", "48px", "Two column rows"),
    ]
    circle_rows = [
        ("Mini", "56", "56", "Initial circle for a committee group or a number badge when there is no logo or photo"),
        ("Small", "160", "85", "Our Focus photos on Home and the Meet our researchers circles on About"),
        ("Medium", "190", "150", "Meet the team initials and photos on About"),
        ("Extra large", "370", "300", "Home header photo circles (they overlap, so the real size follows the card width up to this limit: 305 and 278 at 1280px wide)"),
    ]
    logo_rows = [
        ("Small", "20", "Funder logos under each timeline entry on About and in the two funding cards on About (the funder strip under the menu is archived and not on any page)"),
        ("Medium", "50", "Steering committee tiles (limited to 100px wide)."),
        ("NRCRA logo (SVG)", "232 wide", "The header menu logo (horizontal navy, about 44px high) and the footer logo (vertical white, about 125px high) are the same 232px width. Four files: horizontal navy, horizontal white, vertical navy, vertical white. The header uses horizontal navy on the light page. The footer uses the vertical (stacked) white logo straight on the navy footer, with no white box. On desktop it sits in the left column. On phones it is centred across the footer on its own row and never more than 200px high. On narrow screens the logo shrinks to fit."),
        ("Large", "84", "Lead partner logo on Home (NEMA). Shrinks only when the column is too narrow for the logo: 64px at 1280px wide. FRRR and UCRH beside it are 45% of that height (29px). The NSW Proudly co-funded by logo (an SVG, interim version made from the public NSW Government logo until NSW supplies the approved file) is taller, up to 135px."),
    ]
    header_photo_rows = [
        ("Size 1: Network (map), Progress, RACK", "546 x 517", "350 x 461", "Cropped to fill. The Google map on Network is the same size."),
        ("Size 2: About and Home", "469 wide", "350 x 263", "About is 469 x 529 and sticks out 80px above and below the text beside it. The Home video card is the same 469px width but keeps its near-square shape (11 : 10, 469 x 426). On iPad and phone the Home video is full width and centred in a 4 : 3 shape."),
        ("Privacy Policy", "none", "none", "Text only"),
    ]
    photo_rows = header_photo_rows + [
        ("Story photos (Network)", "331 x 248", "312 x 234", "Shape 4 : 3, 16px corners, inside a 28px card"),
        ("Steering committee tiles (About)", "160 x 160", "111 x 111", "16px corners, logo 50px high"),
        ("Acknowledgement flag (footer)", "60 x 40", "60 x 40", "A picture, not an icon"),
    ]
    icon_rows = [
        ("Small", "16", "16", "Menu arrows, the Draft flag in each Draft tag, the yellow ring in the Network note"),
        ("Default", "22", "22", "Menu (hamburger) icon on phones. The button shows the icon only, with no word Menu, in a 48px square teal button."),
        ("Large", "44", "44", "The tap area for icon buttons: social icon buttons in the footer (12px corners, white button, navy icon 28px) and the menu arrow button on phones"),
        ("Giant", "92", "92", "Watch (play) button on the Home video and on the Network story photos"),
    ]
    circle_demo = "".join(f'<div class="cs"><span style="border-radius:50%;width:{round(d*.4)}px;height:{round(d*.4)}px"></span><b>{n}</b><small>{d}px</small></div>' for n, d in [("Mini", 56), ("Small", 160), ("Medium", 190), ("Extra large", 370)])
    logo_demo = "".join(f'<div class="cs"><img src="../assets/funders/nsw.png" alt="" style="height:{h}px;width:auto"><b>{n}</b><small>{h}px</small></div>' for n, h in [("Small", 20), ("Medium", 50), ("Large", 84)])
    swatches = "".join(f'<div class="cs"><span style="border-radius:{r}"></span><b>{n}</b></div>' for n, r in [("12px", "12px"), ("16px", "16px"), ("20px", "20px"), ("28px", "28px"), ("Pill", "99px")])
    return f'''<section class="blk" id="guidelines"><h2>Type, spacing and corner rules</h2>
<p class="vnote">Use these values when setting the site up in Wix. Sizes are in px with the rem value in brackets. Desktop is 1000px and wider; phone is 390px. Only two font weights are used: 400 and 800. Checked against the NRCRA prototype on 4 November 2026, at 1280px wide and 390px wide.</p>
<h2 id="gl-text" style="margin-top:30px">1. Text</h2>
<h3 id="gl-type">Title and text sizes</h3>{_gl_table(["Style", "Desktop (px)", "Phone (px)", "Weight", "Line spacing", "Letter spacing", "Fluid rule", "Use"], type_rows)}
<h3 id="gl-special" style="margin-top:30px">Line spacing, letter spacing and special characters</h3>{_gl_table(["Rule", "Value", "Notes"], special_rows)}
<h2 id="gl-visuals" style="margin-top:44px">2. Visuals</h2>
<h3 id="gl-photos">Photos</h3><p class="vnote">There are only two header photo sizes. Header photos have 28px corners, sit beside the page title on desktop, and go full width under the title on phones.</p>{_gl_table(["Picture", "Desktop (px)", "Phone (px)", "Notes"], photo_rows)}
<h3 id="gl-circles" style="margin-top:30px">Circle photos</h3>
<p class="vnote">Round photos and initial circles use one of four named sizes. The diameter is the same on both axes, the photo is cropped to fill the circle (centre crop unless a focal point is set), and there is no border. Pick the size by name; do not invent in-between sizes.</p>
{_gl_table(["Size", "Desktop (px)", "Phone (px)", "Used for"], circle_rows)}<p class="vnote">Shown at 40% of real size.</p><div class="csrow" style="align-items:flex-end">{circle_demo}</div>
<h3 id="gl-logos" style="margin-top:30px">Logos</h3>
<p class="vnote">Header, footer, partner, funder and committee logos use one of three sizes (Small, Medium and Large), set by height, with the width following the logo&rsquo;s own shape (never stretched or cropped). Logos have no border and no background box. Pick the size by name.</p>
{_gl_table(["Size", "Height (px)", "Used for"], logo_rows)}<div class="logodemo">{logo_demo}</div>
<h3 id="gl-icons" style="margin-top:30px">Icons</h3><p class="vnote">Four icon sizes, set by height and width together, used across the whole site. Charts and infographics keep their own sizes. The Acknowledgement flag in the footer (60 x 40) is a picture, not an icon.</p>{_gl_table(["Size", "Desktop (px)", "Phone (px)", "Used for"], icon_rows)}
<h3 id="gl-corners" style="margin-top:30px">Corners</h3>{_gl_table(["Element", "Corner radius", "Use"], corner_rows)}<div class="csrow">{swatches}</div>
<h2 id="gl-spacing" style="margin-top:44px">3. Spacing</h2><p class="vnote">Read from the outside in: the space between sections, the margin and gap between elements, then the padding inside each element.</p>
<h3 id="gl-space">Between sections</h3>{_gl_table(["Where", "Value", "Use"], space_rows)}
<h3 id="gl-margin" style="margin-top:30px">Margin and gap (space outside an element)</h3><p class="vnote">Margin and gap are the empty space between elements. Nothing is painted in it.</p>{_gl_table(["Between", "Desktop", "Phone", "Notes"], margin_rows)}
<h3 id="gl-pad" style="margin-top:30px">Padding (space inside an element)</h3><p class="vnote">Padding is the space between an element&rsquo;s edge and what is inside it, such as the edge of a card and its text. The background colour fills the padding.</p>{_gl_table(["Element", "Desktop", "Phone", "Notes"], pad_rows)}</section>'''


def teal_adjust():
    return f'''<section class="blk" id="teal-adjust"><h2>Recommended colour adjustments for using teal as backgrounds</h2>
<p>The brand teal <code>#00A79D</code> gives white text only {_ratio(WHITE_, "#00a79d"):.2f}:1, which fails AA. So the prototypes use an <b>adjusted teal</b>, <code>#00857C</code>, wherever white text sits on teal (every button, including Sign In). It is a little darker, and white on it reaches {_ratio(WHITE_, "#00857c"):.2f}:1. Brand teal is kept for borders, dots and text on navy, where it passes. The adjusted teal is a new colour and needs the client&rsquo;s yes.</p>
<div class="sw"><div style="background:#00a79d;color:#fff"><b>Aa White text</b>Brand teal <code>#00A79D</code><small><span class="vfail">White on it {_ratio(WHITE_, "#00a79d"):.2f}:1, fails</span></small></div><div style="background:#00857c;color:#fff"><b>Aa White text</b>Adjusted teal <code>#00857C</code><small><span class="vpass">White on it {_ratio(WHITE_, "#00857c"):.2f}:1, passes</span></small></div></div></section>'''


def button_sections():
    secs = ""
    for name, c, tx, tint, link, note in FAMILIES:
        sid = name.lower() + "-buttons"
        intro = ""
        if name == "Teal":
            intro = "<p>Primary, secondary, tertiary, link and menu item, for teal and yellow, each on white and on navy. The primary button is the colour with a navy outline, as the Sign In button is in Prototype C. A red or green chip says whether the text passes AA. Each shows default, hover and active: hover fills with navy (or the colour, for navy buttons), active takes the lighter tint with navy text. Menu and links work the same way: hover underlines on pale teal #F3F9F8 (links also turn navy, the menu stays navy), and active takes light teal #BEDDDA.</p>"
        secs += f'<section class="blk" id="{sid}"><h2>{name} buttons <code>{c.upper()}</code></h2>{intro}<p>{note}</p><div class="bpair">{_set(name, c, tx, tint, link, note, False)}{_set(name, c, tx, tint, link, note, True)}</div><p class="vnote">Selected menu item: the lighter version of {name.lower()} (<code>{tint.upper()}</code>) as the background, navy text.</p></section>'
    return secs


def button_sets():
    return '''<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><title>Moved: brand colour contrast</title><meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noai, noimageai"><meta http-equiv="refresh" content="0;url=../brand-contrast/#teal-buttons"><script data-cfasync="false">location.replace("../brand-contrast/#teal-buttons")</script></head><body style="font-family:sans-serif;padding:24px"><p>The button sets now live on the <a href="../brand-contrast/#teal-buttons">Brand colour contrast</a> page.</p></body></html>'''


HR_URL = "https://humanrights.gov.au/resource-hub/by-resource-type/guidelines-and-standards/guides-and-standards-disability-rights/chapter-3-standards-and-guidelines-digital-accessibility"
WCAG_URL = "https://www.wcag.com/"


def _link_terms(html):
    """Link the words that mean accessibility, standards and readability to the digital accessibility guide, and WCAG to wcag.com.
    Visible text only: skips existing links, buttons, code, the menu, headings and the head."""
    skip_open = ("a", "button", "code", "nav", "head", "style", "script", "title", "h1", "h2", "h3")
    hr = re.compile(r"\b(contrast requirements|readability|readable|accessibility|accessible|AA)\b")
    wc = re.compile(r"\bWCAG\b")
    def link(url, text):
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{text}<span class="sr"> (opens in a new tab)</span></a>'
    out, depth = [], 0
    for part in re.split(r"(<[^>]+>)", html):
        if part.startswith("<"):
            m = re.match(r"<(/?)([a-zA-Z0-9]+)", part)
            if m and m.group(2).lower() in skip_open and not part.endswith("/>"):
                depth = depth + 1 if not m.group(1) else max(0, depth - 1)
            out.append(part)
            continue
        if depth == 0 and part.strip():
            part = hr.sub(lambda m: link(HR_URL, m.group(1)), part)
            part = wc.sub(lambda m: link(WCAG_URL, m.group(0)), part)
        out.append(part)
    return "".join(out)


def _orange(html):
    """Rename the brand red to orange in visible text only (not tags, styles or scripts). Keeps 'red cones' and the red/green chip wording."""
    keep = [("red cones", "\x00A"), ("red or green chip", "\x00B")]
    parts = re.split(r"(<style.*?</style>|<script.*?</script>|<[^>]+>)", html, flags=re.S)
    out = []
    for part in parts:
        if part.startswith("<"):
            out.append(part)
            continue
        for a, b in keep:
            part = part.replace(a, b)
        part = re.sub(r"\bRed\b", "Orange", part)
        part = re.sub(r"\bred\b", "orange", part)
        for a, b in keep:
            part = part.replace(b, a)
        out.append(part)
    return "".join(out)


def main():
    B.write("brand-contrast/index.html", _link_terms(_orange(brand_contrast())).replace("#6c8590", "#586c74").replace("#e0f4f3", "#f3f9f8").replace("#bfe9e7", "#beddda"))
    B.write("button-sets/index.html", button_sets())
