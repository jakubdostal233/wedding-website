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

## Proposed - pending owner sign-off

NOT decided. None may be implemented as a fixed choice until the owner signs off.

_None at present._

## Open questions

No decision yet. Tracked alongside the live plan in [./plan.md](./plan.md).

### O-FONTS - Self-host fonts versus Google Fonts CDN

- Decision needed: keep loading Cormorant Garamond + Inter from the Google Fonts CDN, or self-host them in `site/assets/`.
- Trade-off: the CDN is simplest but lets Google see a request on each page load (privacy / GDPR) and adds a third-party dependency ([D-NOSERVICES](#d-noservices--no-third-party-services) carves out the font CDN as the one exception); self-hosting removes that at the cost of bundling and updating the font files.
- Status: open. Default is the CDN; revisit if privacy becomes a concern or during the design refresh ([O-DESIGN](#o-design--visual-design-refresh-from-the-print-materials)).

### O-DESIGN - Visual design refresh from the print materials

- Decision needed: update the site's visual identity (palette, typography, motifs) to match the printed wedding materials. This is the **next phase** after the restructure (roadmap Phase 4.5); nothing is applied yet, and it requires updating [./SPEC.md](./SPEC.md) (Design section) and owner sign-off before implementation.
- Design source of truth: the two PDFs in `tmp/style/` &mdash; `svatebni-oznameni.pdf` (the final wedding announcement) and `jmenovky-design.pdf` (the name badges).
- **Provisional palette** (eyeballed from the PDFs on 2026-06-06 &mdash; NOT yet sampled precisely; sample exact hex values from the PDFs during the design phase):
  - Blush-pink tint (light background / surfaces): ~`#F3D9DE`
  - Rose pink (primary accent / headings / large letters): ~`#E7A6B7`
  - White (`#FFFFFF`) for cards / grounds
  - Charcoal hairline (`#2A2A2A`, the existing charcoal) for thin outlines and dividers
  - This **replaces the current sage-green accent** &mdash; the dominant identity in the print materials is blush/dusty pink on white, not ivory/charcoal/sage.
- **Provisional typography & motifs:** an elegant high-contrast display serif for the names/headings (evaluate keeping Cormorant Garamond as the free web stand-in versus a closer match); a refined serif for body; recurring motifs are rounded oval / arch shapes, thin charcoal hairline frames, vertical hairline dividers, and a stacked date block (`10` / `07` / `26`).
- Status: open. Provisional inputs captured so the design-refresh phase is ready to execute.
