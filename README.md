# NRCRA website prototypes

Prototypes for the nrcra.org.au website. Sample content only. Preview URL: https://client38.veemercado.com/

**Round 1** (three directions, one per mood board; the client chose Prototype 1)
- `v1/` colour block sections, `v2/` light and fresh, `v3/` illustrated visuals; `v1.2/` and `v3.2/` are archived variants (each page is an anchor: `#home`, `#about`, `#partners`, `#network`, `#rack`)

**Round 2**
- `prototype-c/` Prototype C, the only published Round 2 prototype. Built by `tools/build_teal.py`. Feedback needed is for finalising the content
- Prototypes A (two cards) and B (one green card) are archived: not built or published. Their Home headers are kept as variants in `build_teal.py` (`HEROES`), and snapshots (plus the original A and B) are in the git-ignored `_archive-*` folders on the working machine. The original A and B are also in git history
- `brand-contrast/` brand guidelines: colours, type, spacing and corner rules, and contrast with accessible text

**Other**
- `index.html` dashboard with Round 2 and Round 1 tabs (Round 1 has CHOSEN above an ARCHIVE line)
- `tools/build.py` regenerates every page from one content source: `python3 tools/build.py` (Round 2 lives in `tools/build_r2.py`)
- `tools/contrast-audit.js` paste into the browser console on a prototype to list text below AA
- `assets/img/` photos from nrcra.org.au; `assets/funders/` funder logos supplied by NRCRA; brand: Nunito Sans, navy #07293b, teal #00a79d, orange #f05a28, yellow #ffcb2a
