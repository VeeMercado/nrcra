// Contrast audit for the prototypes. Paste into the browser console on a prototype page
// (or run with the browser tool). Visits every screen and lists text below WCAG 2.2 AA.
(async () => {
  const parse = (c) => { const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const p = m[1].split(/[ ,\/]+/).filter(Boolean).map(Number); return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 }; };
  const lin = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
  const L = (c) => 0.2126 * lin(c.r) + 0.7152 * lin(c.g) + 0.0722 * lin(c.b);
  const over = (top, under) => ({ r: top.r * top.a + under.r * (1 - top.a), g: top.g * top.a + under.g * (1 - top.a), b: top.b * top.a + under.b * (1 - top.a), a: 1 });
  function bgOf(el) {
    const stack = [];
    for (let e = el; e; e = e.parentElement) {
      const cs = getComputedStyle(e);
      if (cs.backgroundImage && cs.backgroundImage !== 'none' && !cs.backgroundImage.startsWith('linear-gradient(rgb(255')) return { image: true };
      if (e.querySelector(':scope > img[style], :scope > img') && getComputedStyle(e.querySelector(':scope > img')).position === 'absolute') return { image: true };
      for (const pseudo of ['::after', '::before']) { const ps = getComputedStyle(e, pseudo); if (ps.content !== 'none' && ps.position === 'absolute' && !(parseFloat(ps.width) < 200)) { const c = parse(ps.backgroundColor); if (c && c.a > 0) stack.push(c); } }
      const c = parse(cs.backgroundColor); if (c && c.a > 0) { stack.push(c); if (c.a >= 1) break; }
    }
    let col = { r: 255, g: 255, b: 255, a: 1 };
    for (let i = stack.length - 1; i >= 0; i--) col = over(stack[i], col);
    return { col };
  }
  const screens = [...document.querySelectorAll('[data-screen]')].map((s) => s.id);
  const fails = [];
  for (const id of screens) {
    location.hash = id; await new Promise((r) => setTimeout(r, 120));
    const page = document.getElementById(id);
    const els = [page, document.querySelector('.site-head'), document.querySelector('.site-foot'), document.querySelector('.protobar')].filter(Boolean).flatMap((root) => [...root.querySelectorAll('*')]);
    for (const el of els) {
      if (!el.offsetParent && getComputedStyle(el).position !== 'fixed') continue;
      const own = [...el.childNodes].filter((n) => n.nodeType === 3 && n.textContent.trim()).map((n) => n.textContent.trim()).join(' ');
      if (!own) continue;
      if (el.closest('.pc-n')) continue; // decorative ordinal, hidden from assistive tech (the list is already numbered)
      if (el.closest('.tagline')) continue; // brand lockup: logotype text has no contrast minimum (WCAG 1.4.3)
      const cs = getComputedStyle(el); const fg = parse(cs.color); const bg = bgOf(el);
      if (bg.image) continue;
      const f = over(fg, bg.col); const l1 = L(f), l2 = L(bg.col); const ratio = (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
      const size = parseFloat(cs.fontSize), bold = parseInt(cs.fontWeight) >= 700; const large = size >= 24 || (bold && size >= 18.66);
      const need = large ? 3 : 4.5;
      if (ratio < need) fails.push({ screen: id, text: own.slice(0, 40), ratio: +ratio.toFixed(2), need, fg: cs.color, bg: `rgb(${Math.round(bg.col.r)},${Math.round(bg.col.g)},${Math.round(bg.col.b)})`, cls: String(el.className).slice(0, 30), tag: el.tagName });
    }
  }
  location.hash = 'home';
  return fails;
})();
