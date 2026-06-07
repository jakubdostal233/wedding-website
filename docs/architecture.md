# Website Architecture

How the wedding website is built and how it works &mdash; the directory layout, the multi-page static structure, the asset and CSS organisation, the integrations, the offline generator tools, and how it is deployed. Self-contained reference; for the *deployment procedure* see [./deployment.md](./deployment.md), for *what* is being built see [../dev/SPEC.md](../dev/SPEC.md), and for *decisions* see [../dev/decisions.md](../dev/decisions.md).

## Table of contents

- [Abbreviations](#abbreviations)
- [1. Repository layout: deliverable versus meta-layer](#1-repository-layout-deliverable-versus-meta-layer)
- [2. The website: multi-page static architecture](#2-the-website-multi-page-static-architecture)
- [3. Assets and the CSS architecture](#3-assets-and-the-css-architecture)
- [4. Integrations](#4-integrations)
- [5. Offline generator tools](#5-offline-generator-tools)
- [6. Deployment](#6-deployment)
- [7. Privacy and access](#7-privacy-and-access)
- [8. Local development](#8-local-development)

## Abbreviations

| Abbreviation | Meaning |
|---|---|
| CDN | Content delivery network |
| CNAME | DNS record aliasing one domain to another (and the GitHub Pages file that binds a custom domain) |
| CSS | Cascading Style Sheets |
| DNS | Domain Name System |
| HTML | HyperText Markup Language |
| HTTPS | HTTP Secure (TLS-encrypted HTTP) |
| ICS | iCalendar file format (RFC 5545) |
| JS | JavaScript |
| OG | Open Graph (link-preview metadata) |
| SPAYD | Short Payment Descriptor &mdash; Czech QR payment standard |
| SVG | Scalable Vector Graphics |
| TLS | Transport Layer Security |
| WCAG | Web Content Accessibility Guidelines |

## 1. Repository layout: deliverable versus meta-layer

The repository separates **the deliverable** (the website itself, everything that is served) from **the meta-layer** (the planning, reference documentation, tooling, and scratch around it). This mirrors the `tyre-model` reference project, where the deliverable (`model/`) is isolated from `dev/`, `docs/`, and `tmp/`. The decision is recorded as [D-STRUCT](../dev/decisions.md#d-struct--repository-restructured-to-the-tyre-model-architecture).

```
wedding-website/
├── .claude/                 # agent context (CLAUDE.md) + Claude Code settings — meta
├── .github/workflows/
│   └── deploy.yml           # GitHub Actions: publish site/ to Pages — meta
├── .gitignore
├── README.md                # human-facing repo overview — meta
│
├── site/                    # THE DELIVERABLE — everything served (= the site root)
│   ├── index.html           # home / hero (page-width photo)
│   ├── program.html         # day timeline + maps (Místa) + add-to-calendar
│   ├── practical-info.html  # dress code, parking, menus, dar (thank-you), různé, kontakt
│   ├── photoshooting.html   # Focení — photo-shoot groups
│   ├── gift.html            # Dar + bank QR — unlisted (direct link /gift)
│   ├── favicon.svg
│   ├── CNAME                # binds the custom domain (tereza-jakub.cz)
│   ├── robots.txt           # disallow all crawlers
│   └── assets/
│       ├── css/main.css     # the single stylesheet
│       ├── img/             # og-card.png, qr-platba.svg
│       ├── js/              # reserved (currently empty)
│       └── wedding_tj.ics   # calendar download
│
├── dev/                     # steering — meta
│   ├── SPEC.md              # source of truth: what is being built
│   ├── roadmap.md           # phased plan + "where we are now" status
│   ├── plan.md              # live to-do list
│   ├── decisions.md         # decision log (D-/P-/O-)
│   ├── worklog.md           # transient log of state-changing work
│   ├── workflow-tracking.md # skill/hook/tooling feedback
│   ├── workflow-emojis-reference.md
│   └── archive-{plans,prompts,audits}/   # immutable dated snapshots
│
├── docs/                    # reference documentation — meta
│   ├── architecture.md      # this file
│   ├── deployment.md        # how to deploy / update / roll back
│   └── qa-checklist.md      # pre-launch functional checks
│
├── tools/                   # offline generators (produce tracked assets) — meta
│   ├── generate-og-card.py
│   └── generate-spayd-qr.py
│
└── tmp/                     # gitignored scratch (drafts, exports, design sources)
```

Only `site/` is served. Everything else is technically reachable on GitHub Pages but is excluded from the published artifact (the deploy workflow uploads `site/` alone) and discouraged from indexing by `robots.txt`.

## 2. The website: multi-page static architecture

The site is **vanilla HTML, CSS, and JavaScript with no build step and no Node toolchain** ([D-STACK](../dev/decisions.md#d-stack--vanilla-static-site-no-build-step)). Each page is a hand-authored `.html` file that the browser loads directly; there is no framework, no templating engine, and no compilation. The advantage for a small, roughly twelve-month-lifecycle informational site is that there is nothing in a build pipeline to break or maintain, and any text editor plus a browser is a complete toolchain.

There are four navigated pages plus one unlisted page, each a single Czech section of content (page filenames are English to keep paths stable; see [D-PAGES](../dev/decisions.md#d-pages--multi-page-english-filenames-czech-content) and the page-count reduction [D-IA4](../dev/decisions.md#d-ia4--site-reduced-to-four-pages)):

| File | Czech section | Purpose |
|---|---|---|
| `index.html` | Úvod | Hero: names, "10.07.2026, Praha", page-width photo |
| `program.html` | Program | Alternating timeline; "Vynecháváme"; add-to-calendar; 3 map embeds (Místa) |
| `practical-info.html` | Praktické informace | Dress code, parking, menus, children, Dar (thank-you), Různé, Kontakt |
| `photoshooting.html` | Focení | Photo-shoot groups |
| `gift.html` | (Dar) | Bank QR + IBAN &mdash; unlisted, direct link `/gift` |

**Shared header and footer.** Every page carries the same `<header class="site-header">` (the brand link plus the three-item nav &mdash; Program, Praktické informace, Focení) and `<footer class="site-footer">`; `gift.html` carries the same chrome but is itself absent from the nav (unlisted). Because there is no include mechanism, these blocks are **duplicated in each file and kept in sync manually** (with AI assistance). Pages cross-link with plain relative hrefs (`href="program.html"`, `href="index.html"`), so the whole nav works identically from any page. This manual-sync approach is comfortable at five pages; if the page count grew past roughly ten, a tiny build-time include or a small client-side fetch would be worth introducing.

## 3. Assets and the CSS architecture

`site/assets/` holds everything the HTML loads at runtime &mdash; it is part of the deliverable, not the meta-layer, which is why it lives inside `site/`:

- `css/main.css` &mdash; the **single stylesheet** for the entire site. It is mobile-first and organised as: a reset, a block of CSS custom properties (`--color-*` palette tokens, typography, spacing), base element styles, the shared header/footer, and then page-specific blocks (hero, timeline, map embeds, the QR block, buttons). Keeping all styles in one file is deliberate at this size; the custom-property tokens at the top are the single place a palette or type change is made.
- `img/` &mdash; `og-card.png` (the 1200&times;630 social preview) and `qr-platba.svg` (the SPAYD payment QR), both **generated offline** (see section 5); plus `hero.jpg` / `hero.webp`, the optimised home-page photo.
- `js/` &mdash; reserved for future JavaScript; currently empty (the site needs no runtime JS).
- `wedding_tj.ics` &mdash; the calendar event file offered for download.

The visual identity is a **blush-pink accent (`#ed9dbc`) on white** with **black/charcoal body text (`#2a2a2a`)**, typeset in **Playfair Display** (titles + all headings) and **Source Sans 3** (sans-serif body), both from the Google Fonts CDN. The palette comes from the printed wedding materials; the typography follows <https://www.jakubmares.cz>. See [D-DESIGN](../dev/decisions.md#d-design--visual-identity-refreshed-to-the-blush-pink-print-identity) and the [2026-06-07 restructure plan](../dev/archive-plans/2026-06-07_restructure-4pages-fonts-content.md). Because the palette and type live as custom properties in `main.css`, the identity is set in the token block rather than per page. The home page shows a page-width hero photo with the names above it; the Program page renders the day as an alternating centre-line timeline (pink times, black dots).

HTML references assets with **relative paths** (`href="assets/css/main.css"`, `src="assets/img/qr-platba.svg"`); since the pages and `assets/` sit together under `site/`, these resolve correctly both when served and when opened from disk. The Open Graph tags additionally use **absolute** URLs rooted at the domain (`https://tereza-jakub.cz/assets/img/og-card.png`), which remain correct because `site/` is served *as* the domain root (section 6).

## 4. Integrations

All "dynamic-feeling" features are static &mdash; no backend, no runtime third-party services ([D-NOSERVICES](../dev/decisions.md#d-noservices--no-third-party-services)):

- **Maps** &mdash; Google Maps iframe embeds on the **Program** page for the three venues (Vršovický zámeček, Havlíčkovy sady, La Farma), each with outbound links to Mapy.cz and Google Maps.
- **Calendar** &mdash; a static `wedding_tj.ics` file (iCalendar / RFC 5545) linked from the **Program** page with a `download` attribute; opening it adds the event to Apple Calendar, Google Calendar, or Outlook.
- **Email** &mdash; a `mailto:info@tereza-jakub.cz` link with a pre-filled subject; replies forward to the owner's Gmail via Seznam Email Profi.
- **Bank QR** &mdash; a Czech SPAYD QR code embedded as a static SVG on the unlisted **`gift.html`** page, with the IBAN and BIC printed beneath. The public Praktické informace page mentions the gift only as a thank-you (no payment details). No JavaScript runs; the QR is generated once, offline.
- **Open Graph cards** &mdash; every page carries OG and Twitter-card meta tags so that sharing a link in a chat app shows a preview card (`og-card.png`) with the names and date rather than a bare URL.

## 5. Offline generator tools

`tools/` holds two Python generators (plus `og-card.html`, the share-card source) that **produce tracked assets**; they are run rarely (only when their inputs change) and are not part of the served site:

- `generate-spayd-qr.py` &mdash; encodes the SPAYD string (account, variable symbol, message) and writes `site/assets/img/qr-platba.svg` (uses `segno`). Re-run only if the bank account, variable symbol, or message changes; re-scan the result with a banking app to confirm.
- `generate-og-card.py` &mdash; renders the share-card source `og-card.html` to `site/assets/img/og-card.png` at 1200&times;630 via **headless Chromium**, so the card uses the site's real web fonts (Playfair Display + Source Sans 3). Re-run (after editing `og-card.html`) only if the names, date, or place change.

Both hardcode their output path under `site/assets/img/`, and both are one-shot generators &mdash; the committed SVG and PNG are the artifacts the site actually uses.

## 6. Deployment

The site is hosted free on **GitHub Pages** behind the custom domain **`tereza-jakub.cz`** (registered at Wedos), with HTTPS auto-issued by Let's Encrypt ([D-HOST](../dev/decisions.md#d-host--github-pages--custom-domain)).

Publishing uses a **GitHub Actions** workflow ([../.github/workflows/deploy.yml](../.github/workflows/deploy.yml)) that, on every push to `main`, uploads the `site/` directory as the Pages artifact and deploys it ([D-DEPLOY](../dev/decisions.md#d-deploy--deploy-via-github-actions-serving-the-site-directory)). The uploaded folder is served *as the site root*, so:

- relative asset paths and the OG absolute URLs both stay correct;
- `CNAME` (inside `site/`) keeps the custom domain bound, and `robots.txt` is served from the root.

The site remains build-less: the workflow only copies static files, it does not compile anything. The full procedure, DNS records, rollback, renewal, and common issues are in [./deployment.md](./deployment.md).

## 7. Privacy and access

The site is **public but unlisted** ([D-PRIVACY](../dev/decisions.md#d-privacy--public-but-unlisted)): it is reachable by anyone with the URL but is kept out of search results. `site/robots.txt` returns `Disallow: /` for all crawlers, and every page includes `<meta name="robots" content="noindex,nofollow">`. The whole repository is technically reachable on the host, so no true secrets are committed to tracked files; bank details on the unlisted `gift.html` are intentionally public (the page is simply not linked from the nav).

## 8. Local development

Open any file in `site/` directly in a browser, or serve the directory for clean root-relative paths:

```bash
python3 -m http.server 8000 --directory site
```

Then open <http://localhost:8000>. Serving from `site/` reproduces the deployed root, so links and assets resolve exactly as they will in production.
