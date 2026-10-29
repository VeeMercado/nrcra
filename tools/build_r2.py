"""Brand red, yellow and teal contrast guidance: one standalone page.
Imported by build.py, which owns the shared helpers and base CSS."""
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


def _row(fg, bg, fgname, bgname):
    r = _ratio(fg, bg)
    url = f"https://webaim.org/resources/contrastchecker/?fcolor={fg[1:].upper()}&bcolor={bg[1:].upper()}"
    n = "pass" if r >= 4.5 else "fail"
    l = "pass" if r >= 3 else "fail"
    return (f'<tr><td><span class="chip" style="color:{fg};background:{bg}">Aa</span> {fgname} on {bgname}</td><td><b>{r:.2f}:1</b></td>'
            f'<td class="{n}">{n.title()}</td><td class="{l}">{l.title()}</td><td><a href="{url}">Check in WebAIM</a></td></tr>')


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


def brand_contrast():
    NAVY, WHITE, BLACK, RED, YEL, TEAL = "#07293b", "#ffffff", "#000000", "#f05a28", "#ffcb2a", "#00a79d"
    def block(name, bg):
        rows = "".join(_row(fg, bg, n, name) for fg, n in [(WHITE, "White text"), (NAVY, "Navy text"), (BLACK, "Black text")])
        rows += "".join(_row(bg, b, name + " text", n) for b, n in [(WHITE, "white")])
        return f'<section class="blk"><h2>Brand {name} <code>{bg.upper()}</code></h2><table><thead><tr><th>Pairing</th><th>Ratio</th><th>Body text (4.5:1)</th><th>Large text (3:1)</th><th>WebAIM</th></tr></thead><tbody>{rows}</tbody></table></section>'
    para = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    return f'''<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Brand red, yellow and teal contrast</title><meta name="robots" content="noindex">{FONT}
<style>{BASE}body{{background:#f3f6f7}}main{{max-width:1240px;margin:0 auto;padding:36px 20px 56px}}
.flag{{display:inline-block;background:#111;color:#ffcb2a;font-weight:900;letter-spacing:.06em;border-radius:99px;padding:.35em 1em;font-size:.85rem;margin-bottom:14px}}.flag a{{color:#fff}}
.rule{{background:#fff;border-left:10px solid var(--orange);border-radius:20px;padding:22px 26px;margin:22px 0}}.rule p{{margin:0}}
.blk,.card2{{background:#fff;border-radius:28px;padding:28px;margin:0 0 22px}}table{{width:100%;border-collapse:collapse;font-size:.95rem}}th,td{{text-align:left;padding:10px 8px;border-bottom:1px solid var(--line)}}th{{font-size:.8rem;text-transform:uppercase;letter-spacing:.06em}}
.chip{{display:inline-grid;place-items:center;width:44px;height:32px;border-radius:8px;font-weight:900;vertical-align:middle;border:1px solid rgba(7,41,59,.25)}}.pass{{color:#1f6b35;font-weight:800}}.fail{{color:#a3201a;font-weight:800}}code{{font-size:.85em;background:var(--grey-6);padding:.1em .4em;border-radius:6px}}
.demo{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}}.demo>div{{border-radius:20px;padding:22px;border:2px solid var(--line)}}.demo h3{{margin-top:0}}.dont{{border-color:#a3201a!important}}.do{{border-color:#1f6b35!important}}
.big{{border-radius:16px;padding:18px;margin:0 0 10px}}.by{{background:var(--yellow);color:#fff}}.br{{background:var(--orange);color:#fff}}.bt{{background:var(--teal);color:#fff}}
.hl{{background:linear-gradient(transparent 56%,var(--yellow) 56%,var(--yellow) 94%,transparent 94%);padding:0 .12em}}.pill{{display:inline-block;background:var(--orange);color:#fff;font-weight:800;font-size:1.2rem;border-radius:99px;padding:.3em 1em}}
.pill2{{display:inline-block;background:var(--navy);color:var(--yellow);font-weight:800;font-size:1.2rem;border-radius:99px;padding:.3em 1em}}.lt{{border-radius:16px;padding:18px;margin:0 0 12px;color:var(--navy);font-weight:600}}.lt span{{display:block}}.lt small{{display:block;margin-top:8px;font-weight:800;font-size:.8rem}}.l-w{{background:#fff;border:2px solid var(--line)}}.l-g{{background:#f3f6f7;border:2px solid var(--line)}}.tint{{border-radius:16px;padding:18px;margin:0 0 12px;color:var(--navy);font-weight:600}}.tint span{{display:block}}.tint small{{display:block;margin-top:8px;font-weight:800;font-size:.8rem;color:var(--navy)}}.t-y{{background:#ffeaaa;border-top:8px solid var(--yellow)}}.t-r{{background:#fbd6c9;border-bottom:8px solid var(--orange)}}.t-t{{background:#bfe9e7;border-top:8px solid var(--teal)}}.opt{{margin:0 0 12px}}.opt small{{display:block;font-weight:800;color:var(--muted);font-size:.8rem;text-transform:uppercase;letter-spacing:.06em}}.hlt{{background:linear-gradient(transparent 56%,var(--teal) 56%,var(--teal) 94%,transparent 94%)}}.hlr{{background:linear-gradient(transparent 56%,var(--orange) 56%,var(--orange) 94%,transparent 94%)}}.pill3{{display:inline-block;background:var(--teal);color:var(--navy);font-weight:800;font-size:1.2rem;border-radius:99px;padding:.3em 1em}}.pairs{{display:flex;flex-wrap:wrap;gap:18px}}.pairs figure{{margin:0}}.pair{{display:flex;width:160px;height:70px;border-radius:12px;overflow:hidden}}.pair span{{flex:1}}.pairs figcaption{{font-size:.85rem;margin-top:6px;max-width:160px}}.bar{{height:12px;border-radius:99px;background:var(--orange);margin:10px 0 16px;max-width:200px}}.ex>*{{margin-bottom:14px}}
@media(max-width:1150px){{.demo{{grid-template-columns:1fr 1fr}}}}@media(max-width:700px){{.demo{{grid-template-columns:1fr}}}}@media(max-width:760px){{table{{font-size:.85rem}}}}</style></head>
<body><svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><filter id="f-grey" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0.2126 0.7152 0.0722 0 0 0.2126 0.7152 0.0722 0 0 0.2126 0.7152 0.0722 0 0 0 0 0 1 0"/></filter><filter id="f-prot" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0.567 0.433 0 0 0 0.558 0.442 0 0 0 0 0.242 0.758 0 0 0 0 0 1 0"/></filter><filter id="f-deut" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0.625 0.375 0 0 0 0.7 0.3 0 0 0 0 0.3 0.7 0 0 0 0 0 1 0"/></filter><filter id="f-trit" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0.95 0.05 0 0 0 0 0.433 0.567 0 0 0 0.475 0.525 0 0 0 0 0 1 0"/></filter></defs></svg><main><span class="flag">MOCKUP &amp; PROTOTYPE ONLY &middot; by <a href="https://veemercado.com">veemercado.com</a></span>
<h1>Using the brand red, yellow and teal</h1>
<p class="lede">Contrast ratios for the brand red (orange, <code>{RED.upper()}</code>) yellow (<code>{YEL.upper()}</code>) and teal (<code>{TEAL.upper()}</code>) against white, navy and black text. Ratios use the WCAG formula, the same one the <a href="https://webaim.org/resources/contrastchecker/">WebAIM Contrast Checker</a> uses, and each row links to WebAIM with the colours filled in.</p>
<div class="rule"><p><b>Red, yellow &amp; teal elements.</b> To maintain readability, red, yellow and teal shouldn&rsquo;t be used as background colours for large chunks of text, as standard text colours (white, navy or black) won&rsquo;t pass contrast requirements. They work well for smaller accents, like title backgrounds or buttons (for example yellow or teal paired with navy).</p></div>
{block("yellow", YEL)}{block("red", RED)}{block("teal", TEAL)}{combo(RED, TEAL, NAVY, WHITE, YEL)}
<section class="card2"><h2>What this means</h2><ul><li><b>Yellow:</b> white text fails everywhere ({_ratio(WHITE, YEL):.2f}:1). Navy passes comfortably ({_ratio(NAVY, YEL):.2f}:1), so yellow is safe for buttons and title backgrounds with navy text.</li>
<li><b>Red:</b> white fails for body text ({_ratio(WHITE, RED):.2f}:1) and only passes as large text. Navy is {_ratio(NAVY, RED):.2f}:1, just under 4.5:1, so it only passes when the text is large (24px, or bold from about 19px). Black does pass ({_ratio(BLACK, RED):.2f}:1) but is off brand.</li>
<li><b>Teal:</b> white text is {_ratio(WHITE, TEAL):.2f}:1, which fails even as large text (it needs 3:1). Navy is {_ratio(NAVY, TEAL):.2f}:1 and passes for body text. Black passes ({_ratio(BLACK, TEAL):.2f}:1) but is off brand.</li>
<li><b>As text colour:</b> red on white is {_ratio(RED, WHITE):.2f}:1, yellow on white is {_ratio(YEL, WHITE):.2f}:1 and teal on white is {_ratio(TEAL, WHITE):.2f}:1, so none of them works for words on a white page.</li></ul></section>
<section class="card2"><h2>Don&rsquo;t and do</h2><div class="demo"><div class="dont"><h3>Don&rsquo;t: large blocks of text</h3><p class="big by">{para}</p><p class="big br">{para}</p><p class="big bt">{para}</p></div>
<div class="do tints"><h3>Do: large blocks of text</h3><p class="tint t-y"><span>{para}</span><small>Navy on light yellow: {_ratio(NAVY, "#ffeaaa"):.2f}:1</small></p><p class="tint t-r"><span>{para}</span><small>Navy on light red: {_ratio(NAVY, "#fbd6c9"):.2f}:1</small></p><p class="tint t-t"><span>{para}</span><small>Navy on light teal: {_ratio(NAVY, "#bfe9e7"):.2f}:1</small></p><p class="vnote">Lighter tint of the brand colour as the background, navy text, and the solid brand colour as a top or bottom border.</p></div>
<div class="do ex"><h3>Do: small accents</h3><p class="opt"><small>Option 1</small><span class="hl" style="font-weight:900;font-size:1.5rem">Navy title with a yellow highlight</span></p><p class="opt"><small>Option 2</small><span class="hl hlt" style="font-weight:900;font-size:1.5rem">Navy title with a teal highlight</span></p><p class="opt"><small>Option 3</small><span class="hl hlr" style="font-weight:900;font-size:1.5rem">Navy title with a red highlight</span></p><p><a class="btn btn-primary" href="#">Yellow button, navy text</a></p><p><span class="pill">Red pill, white bold large text</span></p><p><span class="pill2">Navy background, yellow text</span></p><div class="bar" aria-hidden="true"></div><p style="margin:0">Body copy stays navy on white or on a light tint. Red and yellow stay as the accent.</p></div>
<div class="do lights"><h3>Do: large blocks of text on a light background</h3><p class="lt l-w"><span>{para}</span><small>Navy on white <code>#FFFFFF</code>: {_ratio(NAVY, "#ffffff"):.2f}:1</small></p><p class="lt l-g"><span>{para}</span><small>Navy on light grey <code>#F3F6F7</code>: {_ratio(NAVY, "#f3f6f7"):.2f}:1</small></p><p class="vnote">The white and light grey used for the page and cards in Prototype 1. Navy body text, and the brand colours only as small accents.</p></div></div></section>
</main></body></html>'''


def main():
    B.write("brand-contrast/index.html", brand_contrast())
