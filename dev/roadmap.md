# Wedding Website &mdash; Roadmap

Phased path from project init to live website. Each phase has a brief description, a plan, deliverables, and dependencies. Detail for the *current* phase lives in `dev/plan-step-NN-*.md`; the spec ground-truth is in `dev/SPEC.md`.

## Table of contents

- [Phase 1 &mdash; Foundation](#phase-1--foundation)
- [Phase 2 &mdash; Page skeletons](#phase-2--page-skeletons)
- [Phase 3 &mdash; Content draft](#phase-3--content-draft)
- [Phase 4 &mdash; Integrations](#phase-4--integrations)
- [Phase 5 &mdash; Photos](#phase-5--photos)
- [Phase 6 &mdash; Polish](#phase-6--polish)
- [Phase 7 &mdash; Domain and deploy](#phase-7--domain-and-deploy)
- [Symbols and abbreviations](#symbols-and-abbreviations)

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
- Generate the SPAYD QR from your bank info (script in `temp/`; output saved to `assets/img/qr-platba.svg`)
- Embed the QR on `gift.html` with the IBAN/account number printed beneath

**Deliverable.** Every functional element works end-to-end.

**Dependencies.** Phase 3 + bank account info, venue addresses, finalised schedule.

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

**Plan.**
- Push the repo to GitHub
- Enable GitHub Pages (Settings → Pages → deploy from `main` branch, root)
- Verify the default `*.github.io` URL works
- Buy a domain at a Czech registrar (forpsi.cz, websupport.cz, domena.cz, etc.)
- Configure DNS at the registrar (apex `A` records to GitHub Pages IPs + `www` `CNAME`)
- Add a `CNAME` file in the repo with the domain name
- Wait for DNS propagation (minutes to hours)
- Confirm HTTPS works (GitHub auto-issues Let's Encrypt)
- Test the live URL on multiple devices
- Distribute the URL to guests

**Deliverable.** Guests can reach the site at the custom domain.

**Dependencies.** Phase 6 + a chosen domain name.

## Symbols and abbreviations

| Term | Meaning |
|------|---------|
| SPAYD | Short Payment Descriptor &mdash; Czech QR payment standard |
| WCAG AA | Web Content Accessibility Guidelines, level AA &mdash; common accessibility target |
| FOUT | Flash of Unstyled Text |
| WebP | Modern image format with better compression than JPG |
| CNAME | DNS record aliasing one domain to another |
| `*.github.io` | Default URL pattern GitHub Pages serves before a custom domain is set |
