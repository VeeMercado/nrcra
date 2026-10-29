# NRCRA website prototypes

Prototypes for the nrcra.org.au website. Sample content only. Preview URL: https://client38.veemercado.com/

**Round 1** (three directions, one per mood board; the client chose Prototype 1)
- `v1/` colour block sections, `v2/` light and fresh, `v3/` illustrated visuals; `v1.2/` and `v3.2/` are archived variants (each page is an anchor: `#home`, `#about`, `#partners`, `#network`, `#rack`)

**Round 2** (compared with each other, not with Round 1)
- `client/` Prototype 1 rebuilt from the client's feedback document (Home, Network, About, Impact; Sign In goes to the R.A.C.K)
- `recommended/` the same client content on the designer's audited wireframes (Layout Design.pdf): Home, About, Impact, Network, R.A.C.K
- `accessibility/` notes on where the requested design does not meet WCAG 2.2 AA, with measured contrast ratios

**Other**
- `index.html` dashboard with Round 1 and Round 2 tabs
- `tools/build.py` regenerates every page from one content source: `python3 tools/build.py` (Round 2 lives in `tools/build_r2.py`)
- `tools/contrast-audit.js` paste into the browser console on a prototype to list text below AA
- `assets/img/` photos from nrcra.org.au; `assets/funders/` funder logos supplied by NRCRA; brand: Nunito Sans, navy #07293b, teal #00a79d, orange #f05a28, yellow #ffcb2a
