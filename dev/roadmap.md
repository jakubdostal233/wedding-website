# Wedding Website &mdash; Roadmap

Phased path from project init to live website, plus the current status. Phase names here are the canonical ones; the live to-do list is in `dev/plan.md` and completed detailed step-plans are archived in `dev/archive-plans/`; the spec ground-truth is in `dev/SPEC.md`.

## Table of contents

- [Where we are now](#where-we-are-now)
- [Phase 1 &mdash; Foundation](#phase-1--foundation)
- [Phase 2 &mdash; Page skeletons](#phase-2--page-skeletons)
- [Phase 3 &mdash; Content draft](#phase-3--content-draft)
- [Phase 4 &mdash; Integrations](#phase-4--integrations)
- [Phase 4.5 &mdash; Design refresh from print materials](#phase-45--design-refresh-from-print-materials)
- [Phase 5 &mdash; Photos](#phase-5--photos)
- [Phase 6 &mdash; Polish](#phase-6--polish)
- [Phase 7 &mdash; Domain and deploy](#phase-7--domain-and-deploy)
- [Symbols and abbreviations](#symbols-and-abbreviations)

## Where we are now

_Last updated: 2026-07-03._

✅ **The site is built and live** at <https://tereza-jakub.cz> &mdash; four navigated pages (Úvod, Program, Praktické informace, Focení) plus an unlisted `gift.html`, with a shared header/footer, real Czech content, and the integrations wired up (Google Maps embeds, the `.ics` calendar file, the `mailto:` link, and the SPAYD bank QR on the gift page), plus Open Graph share cards.

🧭 **Infrastructure restructure (2026-06-06).** The repository was reorganised to the tyre-model architecture: the website now lives in `site/`, deployment migrated from legacy branch-deploy to a GitHub Actions workflow, and `dev/` adopted the steering-document scheme. See `dev/decisions.md` ([D-STRUCT], [D-DEPLOY]) and `docs/architecture.md`.

🎨 **Design + IA refresh (2026-06-07).** The visual identity was set (blush-pink palette `#ED9DBC` on white + Playfair Display / Source Sans 3, matching jakubmares.cz) and the site reduced from seven pages to four navigated pages (O nás dropped, Focení added) plus an unlisted gift page, with an alternating Program timeline and a page-width hero photo. See `dev/decisions.md` ([D-DESIGN], [D-IA4]) and the restructure plan in `dev/archive-plans/2026-06-07_restructure-4pages-fonts-content.md`.

🎀 **Favicon + QA pass (2026-07-03).** The favicon was refreshed to the blush-pink identity (pink ground, Playfair monogram). A QA pass ran across all pages: HTML validation (all pass), internal-link resolution, IBAN checksum (valid), calendar and contrast checks, and a Czech copy read-through. Fixes shipped: the gift page's bank number no longer breaks mid-digit on mobile, the Program timeline **times** are charcoal for legibility (the pink is ~2.07:1 and fails WCAG AA), the font-link ampersands are escaped (HTML now validates), and Open Graph tags were added to `photoshooting.html`. See [decisions.md](./decisions.md) (D-DESIGN update).

📬 **The URL has been distributed to guests** (confirmed 2026-07-03).

📍 **Next:** owner-side real-device QA (phones/tablets, different banking apps for the QR) per [../docs/qa-checklist.md](../docs/qa-checklist.md); optionally a nicer hero photo (owner to provide). Wedding: 2026-07-10. The live task list is in `dev/plan.md`.

## Phase 1 &mdash; Foundation

**Goal.** Lay the technical foundation: site asset directories, base CSS (palette, typography, layout primitives), shared header/footer pattern, fonts loaded, and one working page (`index.html`) that proves everything renders correctly.

**Plan.**

- Decide and document the shared-header/footer strategy
- Create `assets/css/`, `assets/js/`, `assets/img/`
- Load fonts (Cormorant Garamond + Inter via Google Fonts)
- Write `assets/css/main.css` &mdash; reset, custom properties for palette/typography/spacing, base styles
- Implement `index.html` &mdash; hero with names/date/place, shared header/footer
- Verify locally (browser + `python3 -m http.server`)

**Deliverable.** `index.html` opens in a browser and matches the design mockup.

**Dependencies.** None.

**Detail.** `dev/plan-step-01-foundation.md`.

## Phase 2 &mdash; Page skeletons

**Goal.** Every page exists with shared header/footer and a stub for its content area. Navigation works between pages.

**Plan.**

- Create `location.html`, `program.html`, `transit.html`, `about-us.html`, `contact.html`, `gift.html`
- Apply the shared header/footer to each
- Stub each page's content area with placeholder Czech text and the section structure
- Verify nav links work both ways

**Deliverable.** Click any nav link on any page → land on a styled page with the right header/footer.

**Dependencies.** Phase 1.

## Phase 3 &mdash; Content draft

**Goal.** Real Czech copy on every page (placeholders where info is still pending).

**Plan.**

- Write hero copy for `index.html`
- Fill `location.html` with venue + restaurant info (placeholders if address is still pending)
- Fill `program.html` with the day timeline (placeholder times if not yet set)
- Fill `transit.html` with directions, parking, transit, and accommodation tips
- Write the meeting story for `about-us.html`
- Write contact + add-to-calendar copy for `contact.html`
- Write gift-section copy for `gift.html` (lead with "your presence is the gift")
- Voice: vykání, warm but proper

**Deliverable.** Pages read coherently in Czech.

**Dependencies.** Phase 2 + content from you (venue address, schedule, story).

## Phase 4 &mdash; Integrations

**Goal.** All dynamic-feeling features wired up.

**Plan.**

- Embed mapy.com iframe on `location.html` (and possibly `transit.html`) for the ceremony venue + restaurant
- Generate `wedding.ics`; link it from `contact.html`
- Add `mailto:` link with prefilled subject on `contact.html`
- Generate the SPAYD QR from your bank info (script in `tools/`; output saved to `site/assets/img/qr-platba.svg`)
- Embed the QR on `gift.html` with the IBAN/account number printed beneath

**Deliverable.** Every functional element works end-to-end.

**Dependencies.** Phase 3 + bank account info, venue addresses, finalised schedule.

## Phase 4.5 &mdash; Design refresh from print materials

**Goal.** Bring the website's visual identity in line with the printed wedding materials &mdash; the announcement (`tmp/style/svatebni-oznameni.pdf`) and the name badges (`tmp/style/jmenovky-design.pdf`). Tracked as [O-DESIGN] in `dev/decisions.md`.

**Plan.**

- Sample the exact palette (hex values) and identify the typefaces from the two PDFs &mdash; do not ship the eyeballed provisional values recorded in `dev/decisions.md`.
- Update `dev/SPEC.md` (Design section: palette + typography) and **re-confirm with the owner before applying anything** (project rule: design/palette/page-list changes go through the spec + sign-off).
- Replace the sage-green accent with the **blush/dusty-pink palette** on white, in the `--color-*` custom properties at the top of `site/assets/css/main.css`; align the heading typeface to the elegant high-contrast display serif; introduce the print motifs (rounded oval / arch shapes, thin charcoal hairlines, the stacked `10/07/26` date) where they fit.
- Re-check WCAG AA contrast with the new palette; regenerate `og-card.png` if the card design changes.

**Deliverable.** The site reads as the same identity as the printed announcement and badges.

**Dependencies.** The 2026-06-06 restructure (done); owner sign-off on the sampled palette/type via `dev/SPEC.md`.

## Phase 5 &mdash; Photos

**Goal.** Real photos in place of placeholders.

**Plan.**

- Source / shoot photos: hero (1) and "About us" (3–5)
- Crop, resize, compress (target ≤ 250 KB per image)
- Choose format(s): WebP with JPG fallback, or just optimised JPG
- Write descriptive `alt` text in Czech
- Test at multiple viewport sizes

**Deliverable.** Hero + "About us" look polished; total page weight is sane (~1 MB or less).

**Dependencies.** Phase 4 + photo selection.

## Phase 6 &mdash; Polish

**Goal.** Quality pass before going live.

**Status.** Largely done (2026-07-03). The automated + desktop side ran as a QA pass: HTML validation, internal-link resolution, IBAN checksum, contrast math (body 14.35:1 and muted grey 5.33:1 pass AA; the pink accent ~2.07:1 stays decorative, and the functional timeline times were darkened to charcoal), responsive layout on desktop and mobile (with a mobile fix for the gift-page number wrap), and a Czech copy read-through. Favicon done; `robots.txt` + per-page `noindex` in place. **Remaining is owner-side real-device testing** (phones/tablets, the QR in two banking apps) per [../docs/qa-checklist.md](../docs/qa-checklist.md), plus the optional nicer hero photo.

**Plan.**

- Mobile responsive testing on real devices (phone, tablet)
- Accessibility: `alt` text, semantic HTML, keyboard navigation, color contrast (WCAG AA)
- Performance: image optimisation, font-display strategy, no render-blocking JS
- Cross-browser: Chrome, Firefox, Safari, mobile Safari/Chrome
- Add `robots.txt` (disallow all) and `<meta name="robots" content="noindex">` to every page
- Favicon
- HTML validation (validator.w3.org), CSS validation
- Spell-check Czech content

**Deliverable.** Site is launch-ready.

**Dependencies.** Phase 5.

## Phase 7 &mdash; Domain and deploy

**Goal.** Site live at the custom domain.

**Status.** ✅ Largely done. The site is live at <https://tereza-jakub.cz>: the domain is registered at Wedos, DNS apex `A` records point at GitHub Pages, HTTPS (Let's Encrypt) is issued and enforced, and the `www` redirect works. As of 2026-06-06 deployment is **published via GitHub Actions** (`.github/workflows/deploy.yml`) serving `site/` as the root, replacing the original legacy branch-deploy. Full procedure and DNS records: `docs/deployment.md`.

**Remaining.** ✅ Done &mdash; the URL was distributed to guests (confirmed 2026-07-03).

**Dependencies.** Phase 6 (launch-quality pass) before broad distribution.

## Symbols and abbreviations

| Term          | Meaning                                                                            |
| ------------- | ---------------------------------------------------------------------------------- |
| SPAYD         | Short Payment Descriptor &mdash; Czech QR payment standard                         |
| WCAG AA       | Web Content Accessibility Guidelines, level AA &mdash; common accessibility target |
| FOUT          | Flash of Unstyled Text                                                             |
| WebP          | Modern image format with better compression than JPG                               |
| CNAME         | DNS record aliasing one domain to another                                          |
| `*.github.io` | Default URL pattern GitHub Pages serves before a custom domain is set              |
