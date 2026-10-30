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
    return f'''<section class="blk"><h2>Does teal work with red?</h2>
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
    return f'''<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Brand colours: navy, teal, orange, yellow</title><meta name="robots" content="noindex">{FONT}
<style>{BASE}html{{scroll-padding-top:84px}}body{{background:#f3f6f7;padding-top:64px}}.topnav{{position:fixed;top:0;left:0;right:0;z-index:50;background:#fff;border-bottom:1px solid var(--line)}}.topnav ul{{list-style:none;margin:0 auto;padding:10px 20px;max-width:1240px;display:flex;flex-wrap:wrap;gap:8px}}:root{{--btn-r:12px}}.topnav a{{display:inline-flex;align-items:center;min-height:44px;padding:0 1.1em;border:2px solid var(--navy);border-radius:12px;color:var(--navy);font-weight:800;text-decoration:none}}.topnav a:hover{{background:var(--navy);color:#fff}}.topnav .n-y{{background:var(--yellow)}}.topnav .n-r{{background:var(--orange);font-size:1.2rem}}.topnav .n-t{{background:#00857c;color:#fff}}.topnav .n-d{{background:var(--navy);color:#fff}}.topnav .n-y:hover,.topnav .n-r:hover,.topnav .n-t:hover,.topnav .n-d:hover{{background:#fff;color:var(--navy)}}.topnav .back{{margin-left:auto}}@media(max-width:900px){{.topnav a{{min-height:40px;padding:0 .8em;font-size:.9rem}}.topnav .bl{{display:none}}}}@media(max-width:560px){{body{{padding-top:112px}}html{{scroll-padding-top:132px}}}}main{{max-width:1240px;margin:0 auto;padding:36px 20px 56px}}
.flag{{display:inline-block;background:#111;color:#ffcb2a;font-weight:900;letter-spacing:.06em;border-radius:99px;padding:.35em 1em;font-size:.85rem;margin-bottom:14px}}.flag a{{color:#fff}}
.rule{{background:#fff;border-left:10px solid var(--orange);border-radius:20px;padding:22px 26px;margin:22px 0}}.rule p{{margin:0}}
.blk,.card2{{background:#fff;border-radius:28px;padding:28px;margin:0 0 22px}}table{{width:100%;border-collapse:collapse;font-size:.95rem}}th,td{{text-align:left;padding:10px 8px;border-bottom:1px solid var(--line)}}th{{font-size:.8rem;text-transform:uppercase;letter-spacing:.06em}}
.chip{{display:inline-grid;place-items:center;width:44px;height:32px;border-radius:8px;font-weight:900;vertical-align:middle;border:1px solid rgba(7,41,59,.25)}}.pass{{color:#1f6b35;font-weight:800}}.fail{{color:#a3201a;font-weight:800}}code{{font-size:.85em;background:var(--grey-6);padding:.1em .4em;border-radius:6px}}
.demo{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}}.demo>div{{border-radius:20px;padding:22px;border:2px solid var(--line)}}.demo h3{{margin-top:0}}.dont{{border-color:#a3201a!important}}.do{{border-color:#1f6b35!important}}
.big{{border-radius:16px;padding:18px;margin:0 0 10px}}.by{{background:var(--yellow);color:#fff}}.br{{background:var(--orange);color:#fff}}.bt{{background:var(--teal);color:#fff}}
.hl{{background:linear-gradient(transparent 56%,var(--yellow) 56%,var(--yellow) 94%,transparent 94%);padding:0 .12em}}.pill{{display:inline-block;background:var(--orange);color:#fff;font-weight:800;font-size:1.2rem;border-radius:99px;padding:.3em 1em}}
.pill2{{display:inline-block;background:var(--navy);color:var(--yellow);font-weight:800;font-size:1.2rem;border-radius:99px;padding:.3em 1em}}.lt{{border-radius:16px;padding:18px;margin:0 0 12px;color:var(--navy);font-weight:600}}.lt span{{display:block}}.lt small{{display:block;margin-top:8px;font-weight:800;font-size:.8rem}}.l-w{{background:#fff;border:2px solid var(--line)}}.l-g{{background:#f3f6f7;border:2px solid var(--line)}}.tint{{border-radius:16px;padding:18px;margin:0 0 12px;color:var(--navy);font-weight:600}}.tint span{{display:block}}.tint small{{display:block;margin-top:8px;font-weight:800;font-size:.8rem;color:var(--navy)}}.t-y{{background:#ffeaaa;border-top:8px solid var(--yellow)}}.t-r{{background:#fbd6c9;border-bottom:8px solid var(--orange)}}.t-t{{background:#beddda;border-top:8px solid var(--teal)}}.opt{{margin:0 0 12px}}.opt small{{display:block;font-weight:800;color:var(--muted);font-size:.8rem;text-transform:uppercase;letter-spacing:.06em}}.hlt{{background:linear-gradient(transparent 56%,var(--teal) 56%,var(--teal) 94%,transparent 94%)}}.hlr{{background:linear-gradient(transparent 56%,var(--orange) 56%,var(--orange) 94%,transparent 94%)}}.pill4{{display:inline-block;background:#00857c;color:#fff;font-weight:800;font-size:1.2rem;border-radius:99px;padding:.3em 1em}}.pill3{{display:inline-block;background:var(--teal);color:var(--navy);font-weight:800;font-size:1.2rem;border-radius:99px;padding:.3em 1em}}.pairs{{display:flex;flex-wrap:wrap;gap:18px}}.pairs figure{{margin:0}}.pair{{display:flex;width:160px;height:70px;border-radius:12px;overflow:hidden}}.pair span{{flex:1}}.pairs figcaption{{font-size:.85rem;margin-top:6px;max-width:160px}}.bar{{height:12px;border-radius:99px;background:var(--orange);margin:10px 0 16px;max-width:200px}}.ex>*{{margin-bottom:14px}}
{BTN_CSS}
.topnav .n-b{{border-style:dashed}}.sw{{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin:14px 0}}.sw>div{{border-radius:20px;padding:22px;font-weight:800}}.sw b{{display:block;font-size:2rem}}.sw small{{display:block;font-weight:700;margin-top:6px}}.sw code{{background:#fff;color:#07293b}}.yn{{display:inline-block;font-size:.68rem;font-weight:900;letter-spacing:.08em;line-height:1;padding:.4em .75em;border-radius:6px;border:1px solid rgba(7,41,59,.3);vertical-align:middle;margin-left:4px}}.warn{{color:#8a5a00;font-weight:800}}.sr{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}.vfail{{background:#a3201a;color:#fff;padding:.15em .6em;border-radius:6px;box-decoration-break:clone;-webkit-box-decoration-break:clone}}.vpass{{text-decoration:underline;text-decoration-color:#07293b;text-decoration-thickness:4px;text-underline-offset:5px}}.swatch{{display:inline-block;width:34px;height:24px;border-radius:6px;border:1px solid rgba(7,41,59,.3);vertical-align:middle}}@media(max-width:700px){{.sw{{grid-template-columns:1fr}}}}
@media(max-width:1150px){{.demo{{grid-template-columns:1fr 1fr}}}}@media(max-width:700px){{.demo{{grid-template-columns:1fr}}}}@media(max-width:760px){{table{{font-size:.85rem}}}}</style></head>
<body><nav class="topnav" aria-label="On this page"><ul><li><a class="n-d" href="#colours">Brand colours</a></li><li><a class="n-t" href="#teal-adjust">Teal adjustment</a></li><li><a class="n-t" href="#teal">Teal</a></li><li><a class="n-d" href="#lightteal">Light teal</a></li><li><a class="n-r" href="#red">Red</a></li><li><a class="n-y" href="#yellow">Yellow</a></li><li><a class="n-d" href="#dos">Do&rsquo;s and Don&rsquo;ts</a></li><li><a class="n-d" href="#text">Text colours</a></li><li><a class="n-t n-b" href="#teal-buttons">Teal buttons</a></li><li><a class="n-y n-b" href="#yellow-buttons">Yellow buttons</a></li><li class="back"><a href="../">&larr; <span class="bl">Back to </span>prototypes</a></li></ul></nav><svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><filter id="f-grey" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0.2126 0.7152 0.0722 0 0 0.2126 0.7152 0.0722 0 0 0.2126 0.7152 0.0722 0 0 0 0 0 1 0"/></filter><filter id="f-prot" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0.567 0.433 0 0 0 0.558 0.442 0 0 0 0 0.242 0.758 0 0 0 0 0 1 0"/></filter><filter id="f-deut" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0.625 0.375 0 0 0 0.7 0.3 0 0 0 0 0.3 0.7 0 0 0 0 0 1 0"/></filter><filter id="f-trit" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0.95 0.05 0 0 0 0 0.433 0.567 0 0 0 0.475 0.525 0 0 0 0 0 1 0"/></filter></defs></svg><main><span class="flag">MOCKUP &amp; PROTOTYPE ONLY &middot; by <a href="https://veemercado.com">veemercado.com</a></span>
<h1>Using the brand colours navy, teal, orange, yellow</h1>
<p class="lede">Contrast ratios for the brand orange (<code>{RED.upper()}</code>), yellow (<code>{YEL.upper()}</code>) and teal (<code>{TEAL.upper()}</code>) against white, navy and black text. Ratios use the WCAG formula, the same one the <a href="https://webaim.org/resources/contrastchecker/">WebAIM Contrast Checker</a> uses, and each row links to WebAIM with the colours filled in.</p>
<div class="rule"><p><b>Red &amp; teal elements.</b> To maintain readability, red and teal shouldn&rsquo;t be used as background colours for large chunks of text, as standard text colours (white, navy or black) won&rsquo;t pass contrast requirements. They work well for smaller accents, like title backgrounds. For teal backgrounds, <a href="#teal-adjust">see the recommended colour adjustments</a>.</p></div>
{brand_colours()}
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
<script data-cfasync="false">(function(){{var n=document.querySelector(".topnav");function f(){{var h=n.offsetHeight;document.body.style.paddingTop=h+"px";document.documentElement.style.scrollPaddingTop=(h+16)+"px"}}f();addEventListener("resize",f)}})()</script>
</main></body></html>'''




# ---------------------------------------------------------------- button, link and text colour sets (review page)
NAVY_, WHITE_, GREY_, LIGHT_ = "#07293b", "#ffffff", "#5e747d", "#f3f6f7"
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
    nav = (f'<div class="mnav" style="background:{bg};color:{fg}"><span style="{nav_cur}">Home</span><span>Network</span><span>About</span><span>Impact</span>'
           f'<span class="push">{_b("Sign In", K["Primary"], None, big)}</span></div>')
    return f'''<div class="set {"dark" if dark else "light"}" style="background:{bg};color:{fg}"><h3 style="color:{fg}">{name} on {"navy" if dark else "white"}</h3>{rows}{nav}</div>'''


def light_teal():
    import colorsys
    def hue(h):
        r, g, b = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        a, l, sat = colorsys.rgb_to_hls(r, g, b)
        return f"hue {round(a * 360)}, saturation {round(sat * 100)}%"
    pale, mid = "#f3f9f8", "#beddda"
    demo = f'''<div class="lteal"><h3>In Prototype A and B</h3>
<div class="mnav" style="background:#fff;color:{NAVY_}"><span style="background:{mid};color:{NAVY_}">Home</span><span>Network</span><span>About</span><span>Impact</span></div>
<div class="ltcard" style="background:{pale};border-bottom:10px solid #00a79d"><b>Pale teal <code>{pale.upper()}</code></b><br>{hue(pale)}. Navy text {_ratio(NAVY_, pale):.2f}:1</div>
<div class="ltcard" style="background:{mid};border-bottom:10px solid #00a79d"><b>Light teal <code>{mid.upper()}</code></b><br>{hue(mid)}. Navy text {_ratio(NAVY_, mid):.2f}:1</div></div>'''
    return f'''<section class="blk" id="lightteal"><h2>Light teal and pale teal</h2><p>The three project PDFs use two light teals. <b>Pale teal</b>, <code>#F3F9F8</code>, is for large pale panels and for hover on the menu and links. <b>Light teal</b>, <code>#BEDDDA</code>, is for the selected menu item, pressed buttons and tinted panels. Both are soft, slightly grey greens, so they sit comfortably next to yellow and red.</p>{demo}</section>'''


def text_colours():
    texts = [(NAVY_, WHITE_, "Navy on white", "default text"), (GREY_, WHITE_, "#5e747d on white", "quiet text, where it matters"), (GREY_, LIGHT_, "#5e747d on #f3f6f7", "quiet text on light grey"),
             (WHITE_, NAVY_, "White on navy", "text on dark"), (LIGHT_, NAVY_, "#f3f6f7 on navy", "text on dark"), (WHITE_, "#00857c", "White on adjusted teal", "text on teal"), (LIGHT_, "#00857c", "#f3f6f7 on adjusted teal", "text on teal")]
    rows = "".join(f'<tr><td><span class="chip" style="color:{f};background:{b}">Aa</span> {l}</td><td>{n}</td><td><b>{_ratio(f, b):.2f}:1</b></td><td class="{"pass" if _ratio(f, b) >= 4.5 else "fail"}">{"Pass" if _ratio(f, b) >= 4.5 else "Fail"}</td></tr>' for f, b, l, n in texts)
    return f'''<section class="blk" id="text"><h2>Text colours</h2><p>Navy for text. <code>#5e747d</code> for quiet text on white where it matters. White and <code>#f3f6f7</code> on darker backgrounds.</p>
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
    others = [("Adjusted teal", "#00857c", "Buttons and any area with white text"), ("Quiet text", GREY_, "Small supporting text on white, light grey and pale teal"),
              ("White", WHITE_, "Cards and page"), ("Light grey", LIGHT_, "Page background"),
              ("Pale teal", "#f3f9f8", "Large pale panels, from the PDFs"), ("Light teal", "#beddda", "Selected menu item, hover, tinted panels, from the PDFs"),
              ("Light yellow", "#ffeaaa", "Tint for large text blocks (guidance examples)"), ("Light red", "#fbd6c9", "Tint for large text blocks (guidance examples)")]
    return f'''<section class="blk" id="colours"><h2>Brand colours</h2>
<h3>Main 4 brand colours</h3>{_hex_table(main4)}
<p class="vnote"><b class="fail">&#10007; NO</b> for navy on teal: it reaches {_ratio(NAVY_, "#00a79d"):.2f}:1, but navy and this teal are hard to tell apart for some people with colour blindness, so we do not recommend the pairing.</p>
<h3 style="margin-top:30px">Adjusted teal, quiet text, white and the light colours</h3>{_hex_table(others)}</section>'''


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
            intro = "<p>Primary, secondary, tertiary, link and menu item, for teal and yellow, each on white and on navy. The primary button is the colour with a navy outline, as the Sign In button is in Prototype A and B. A red or green chip says whether the text passes AA. Each shows default, hover and active: hover fills with navy (or the colour, for navy buttons), active takes the lighter tint with navy text. Menu and links work the same way: hover underlines on pale teal #F3F9F8 (links also turn navy, the menu stays navy), and active takes light teal #BEDDDA.</p>"
        secs += f'<section class="blk" id="{sid}"><h2>{name} buttons <code>{c.upper()}</code></h2>{intro}<p>{note}</p><div class="bpair">{_set(name, c, tx, tint, link, note, False)}{_set(name, c, tx, tint, link, note, True)}</div><p class="vnote">Selected menu item: the lighter version of {name.lower()} (<code>{tint.upper()}</code>) as the background, navy text.</p></section>'
    return secs


def button_sets():
    return '''<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><title>Moved: brand colour contrast</title><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url=../brand-contrast/#teal-buttons"><script data-cfasync="false">location.replace("../brand-contrast/#teal-buttons")</script></head><body style="font-family:sans-serif;padding:24px"><p>The button sets now live on the <a href="../brand-contrast/#teal-buttons">Brand colour contrast</a> page.</p></body></html>'''


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
    B.write("brand-contrast/index.html", _link_terms(_orange(brand_contrast())).replace("#6c8590", "#5e747d").replace("#e0f4f3", "#f3f9f8").replace("#bfe9e7", "#beddda"))
    B.write("button-sets/index.html", button_sets())
