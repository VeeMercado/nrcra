# NRCRA website prototypes

Prototypes for the nrcra.org.au website. Sample content only. Preview URL: https://client38.veemercado.com/

**Round 1** (three directions, one per mood board; the client chose Prototype 1)
- `v1/` colour block sections, `v2/` light and fresh, `v3/` illustrated visuals; `v1.2/` and `v3.2/` are archived variants (each page is an anchor: `#home`, `#about`, `#partners`, `#network`, `#rack`)

**Round 2**
- `prototype-a/` Prototype A, Teal Accents (the existing navy style) (menu and pages match Prototype B). A separate, hand-kept file: `build.py` does not write it, so Round 1 changes never reach it
- `prototype-b/` Prototype B, Teal hero (teal as accents and tints)
- `brand-contrast/` guidance on using the brand red, yellow and teal with accessible text

**Other**
- `index.html` dashboard with Round 2 and Round 1 tabs
- `tools/build.py` regenerates every page from one content source: `python3 tools/build.py` (Round 2 lives in `tools/build_r2.py`)
- `tools/contrast-audit.js` paste into the browser console on a prototype to list text below AA
- `assets/img/` photos from nrcra.org.au; `assets/funders/` funder logos supplied by NRCRA; brand: Nunito Sans, navy #07293b, teal #00a79d, orange #f05a28, yellow #ffcb2a
