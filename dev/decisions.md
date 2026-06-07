# Decision log

Authoritative record of what is settled and what is not. Decided entries are listed oldest-first (new decisions appended at the end). Every entry is dated.

> This log was established on 2026-06-06 during the repository restructure ([D-STRUCT](#d-struct--repository-restructured-to-the-tyre-model-architecture)). Decisions that predate it were settled at the project's inception and recorded prose-style in [./SPEC.md](./SPEC.md); they are consolidated here and dated to the project's May 2026 start where known. [./SPEC.md](./SPEC.md) remains the fuller source of truth for *what* is being built; this file is the dated record of *decisions*.

Entry IDs encode status as a prefix &mdash; `D-` = Decided, `P-` = Proposed (pending owner sign-off), `O-` = Open &mdash; followed by a short topic mnemonic.

## Table of contents

- [Abbreviations](#abbreviations)
- [Decided](#decided)
- [Proposed - pending owner sign-off](#proposed---pending-owner-sign-off)
- [Open questions](#open-questions)

## Abbreviations

| Abbreviation | Meaning |
|---|---|
| CDN | Content delivery network |
| CNAME | DNS record aliasing one domain to another (and the GitHub Pages file that binds a custom domain) |
| CI | Continuous integration |
| DNS | Domain Name System |
| ICS | iCalendar file format (RFC 5545) |
| OG | Open Graph (link-preview metadata) |
| SPAYD | Short Payment Descriptor &mdash; Czech QR payment standard |
| SVG | Scalable Vector Graphics |

## Decided

Final. Implementation may proceed on these.

### D-STACK - Vanilla static site, no build step

- Date: 2026-05 (inception)
- Decision: The site is vanilla HTML / CSS / JavaScript with no framework, no build step, and no Node toolchain. A single stylesheet (`site/assets/css/main.css`), mobile-first.
- Why: lowest maintenance and lowest hosting cost for a small, ~12-month-lifecycle informational site; nothing to break in a build pipeline.

### D-PAGES - Multi-page, English filenames, Czech content

- Date: 2026-05 (inception)
- Decision: Multi-page architecture (seven pages) with a shared header/footer kept in sync manually (with AI assist). Page filenames are English (`location.html`, `about-us.html`); content is Czech (vykání, warm but proper). An English mirror under `/en/` is a possible later phase.
- Why: English filenames keep paths stable if an English mirror is ever added; Czech content matches the audience.

### D-HOST - GitHub Pages + custom domain

- Date: 2026-05 (inception)
- Decision: Hosted free on GitHub Pages, fronted by the custom domain `tereza-jakub.cz` (registered at Wedos), bound via a `CNAME` file. Email `info@tereza-jakub.cz` forwards via Seznam Email Profi (free tier). Total cost ~165 CZK + VAT / year (domain only).
- Why: free, reliable static hosting; the owner already controls the domain and email.
- See [../docs/deployment.md](../docs/deployment.md). Superseded in part by [D-DEPLOY](#d-deploy--deploy-via-github-actions-serving-the-site-directory) (the deploy *mechanism*; the host and domain are unchanged).

### D-PRIVACY - Public but unlisted

- Date: 2026-05 (inception)
- Decision: The site is public but unlisted &mdash; discoverable only via the URL given to guests. `robots.txt` disallows all crawlers and every page carries `<meta name="robots" content="noindex,nofollow">`. No true secrets live in tracked files (the whole repo is technically reachable).
- Why: a wedding site should not be search-indexed, but needs no authentication.

### D-NOSERVICES - No third-party services

- Date: 2026-05 (inception)
- Decision: No third-party runtime services &mdash; no analytics, no form backends (e.g. Formspree), no CDN beyond Google Fonts. Map embeds use `mapy.com` iframes; the bank QR is a static SPAYD SVG generated offline; contact is `mailto:` only; the calendar is a static `.ics` file.
- Why: privacy, simplicity, zero ongoing cost and zero runtime dependencies. Any new service requires an explicit decision logged here.

### D-STRUCT - Repository restructured to the tyre-model architecture

- Date: 2026-06-06
- Decision: The repository was reorganised to separate **the deliverable** from **the meta-layer**, mirroring the `tyre-model` reference project. The website (all HTML, `assets/`, `favicon.svg`, `CNAME`, `robots.txt`) now lives in a dedicated **`site/`** directory; `dev/` holds steering documents (this log, `plan.md`, `roadmap.md`, `worklog.md`, `workflow-tracking.md`, `workflow-emojis-reference.md`, and `archive-*/`); `docs/` holds reference documentation; `tools/` holds the offline generator scripts; `tmp/` (renamed from `temp/`) is gitignored scratch.
- Why: navigability and ease of development &mdash; a clean mental model of "what is served" versus "the process around it", and a consistent steering/reference convention.
- See [../README.md](../README.md), [../docs/architecture.md](../docs/architecture.md), and the archived restructure prompt at [./archive-prompts/2026-06-06_restructure-to-tyre-model.md](./archive-prompts/2026-06-06_restructure-to-tyre-model.md).

### D-DEPLOY - Deploy via GitHub Actions, serving the `site/` directory

- Date: 2026-06-06
- Decision: GitHub Pages publishes via a **GitHub Actions** static-upload workflow ([../.github/workflows/deploy.yml](../.github/workflows/deploy.yml)) that uploads the `site/` directory as the Pages artifact, replacing the previous legacy "deploy from a branch (root)" source. The `site/` folder is served *as the site root*, so the Open Graph absolute URLs (`https://tereza-jakub.cz/...`) are unchanged and `CNAME` / `robots.txt` ship inside `site/`. The site stays build-less &mdash; the workflow only uploads static files.
- Why: a dedicated `site/` directory ([D-STRUCT](#d-struct--repository-restructured-to-the-tyre-model-architecture)) is incompatible with legacy branch-deploy, which serves only `/` or `/docs`; the Actions path serves an arbitrary folder as root with no build step.
- See [../docs/deployment.md](../docs/deployment.md).

### D-DESIGN - Visual identity refreshed to the blush-pink print identity

- Date: 2026-06-07
- Decision: The site adopts the blush-pink identity of the printed wedding materials (`tmp/style/svatebni-oznameni.pdf`, `jmenovky-design.pdf`), replacing the inception ivory/charcoal/sage scheme. Resolves the former O-DESIGN open question.
  - **Palette** (sampled precisely from the print PDFs' CMYK fills, converted to sRGB &mdash; supersedes the eyeballed provisional values):
    - Accent &mdash; headings, the names, the `&`, links, dividers: **`#ED9DBC`** (rose pink)
    - Background / ground: **`#FFFFFF`** (white)
    - Body text: **`#2A2A2A`** (the existing charcoal, kept for readability &mdash; pink on white fails WCAG contrast for body copy)
    - Hairlines / rules: a light blush tint (`#F0DDE4`)
    - A very light blush (`#EBD3DC`, the jmenovky page field) is on hand as an optional future background tint.
  - **Typography** (all via Google Fonts; the print fonts themselves are NOT used &mdash; see below):
    - **Title + all headings: Bodoni Moda** &mdash; high-contrast didone, the closest Google-Fonts match to the print headline face (Agraham), which it replaces in both the title and the heading roles (in the print materials a single face served both).
    - **The `&` in the title: Tangerine** &mdash; calligraphic script replacing the print ampersand (terranika); set at ~0.92em of the names (`48px` against `52px` in the calibration render).
    - **Body: Bodoni Moda** (the same family as the headings) &mdash; at body sizes its `opsz` axis (`font-optical-sizing: auto`) serves a lower-contrast, readable cut, so it honours the print "Didot for body" intent (Bodoni and Didot are sibling didones) with a guaranteed, Czech-capable face. The original pick, Theano Didot, was dropped: it is no longer served by Google Fonts (returns "400: Font family not found"), so it would silently fall back to Georgia.
  - **Update 2026-06-07 (supersedes the three typography lines above):** the owner chose to match the typography of <https://www.jakubmares.cz> instead &mdash; **Playfair Display** (titles + headings) + **Source Sans 3** (sans-serif body), with a **plain Playfair `&`** in the title (Tangerine dropped). The palette above is unchanged. Bodoni Moda + Tangerine shipped only briefly. See the [restructure plan](./archive-plans/2026-06-07_restructure-4pages-fonts-content.md).
- Why the print fonts are not used directly: the print faces are `Agraham-PersonalUse` (no Czech diacritics &mdash; the announcement stamped the carons from a separate demo font), `terranika`, and `Didot` &mdash; none are available as the full font files an `@font-face` setup needs, and Agraham cannot set Czech text at all. The Google-Fonts equivalents avoid self-hosting, licensing, and `.woff2` work, and already cover Czech. This does not affect O-FONTS (CDN vs self-host) &mdash; the site still loads fonts from the Google Fonts CDN.
- See [./SPEC.md](./SPEC.md) (Design section); analysis renders were produced 2026-06-07.

### D-IA4 - Site reduced to four pages

- Date: 2026-06-07
- Decision: The seven-page structure is reduced to **four navigated pages** &mdash; `index.html` (Úvod), `program.html` (Program), `practical-info.html` (Praktické informace), `photoshooting.html` (Focení) &mdash; plus one **unlisted** page, `gift.html` (Dar + bank QR + IBAN), reachable only via `/gift`. The old `location.html`, `transit.html`, `contact.html`, and `about-us.html` (O nás) are removed. Content relocates: maps + add-to-calendar &rarr; Program; transport/parking, dress code, menus, children, Dar (thank-you), Různé, Kontakt &rarr; Praktické informace; the bank QR + IBAN live only on the unlisted `gift.html`; the photo-shoot groups go to `photoshooting.html`. Accommodation (ubytování) is dropped; O nás is dropped entirely.
- Why: simpler navigation for guests; payment details kept off the public nav; the supplied content fits cleanly. (Finalised over 2026-06-07: an initial pass kept O nás and Dar-in-Praktické-informace; then O nás was removed, Dar split out to the unlisted gift page, and Focení added to the nav.)
- Partially supersedes [D-PAGES](#d-pages--multi-page-english-filenames-czech-content) (the page *count* only &mdash; the multi-page architecture, English filenames, and Czech content all stand).
- See the [restructure plan](./archive-plans/2026-06-07_restructure-4pages-fonts-content.md).

## Proposed - pending owner sign-off

NOT decided. None may be implemented as a fixed choice until the owner signs off.

_None at present._

## Open questions

No decision yet. Tracked alongside the live plan in [./plan.md](./plan.md).

### O-FONTS - Self-host fonts versus Google Fonts CDN

- Decision needed: keep loading the web fonts (Playfair Display + Source Sans 3, per [D-DESIGN](#d-design--visual-identity-refreshed-to-the-blush-pink-print-identity)) from the Google Fonts CDN, or self-host them in `site/assets/`.
- Trade-off: the CDN is simplest but lets Google see a request on each page load (privacy / GDPR) and adds a third-party dependency ([D-NOSERVICES](#d-noservices--no-third-party-services) carves out the font CDN as the one exception); self-hosting removes that at the cost of bundling and updating the font files.
- Status: open. Default is the CDN; revisit if privacy becomes a concern. (The design refresh itself is now settled &mdash; see [D-DESIGN](#d-design--visual-identity-refreshed-to-the-blush-pink-print-identity).)
