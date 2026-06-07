# Implementation plan

Living document &mdash; the current to-do list. Finished tasks are DELETED (not ticked); the file is reordered as priorities shift. Phase names are the canonical ones from [./roadmap.md](./roadmap.md); decision IDs (`D-`/`O-`) reference [./decisions.md](./decisions.md).

Current state: the site is **built and live** at <https://tereza-jakub.cz>. Done: the 2026-06-06 restructure ([D-STRUCT](./decisions.md#d-struct--repository-restructured-to-the-tyre-model-architecture)) + Actions deploy ([D-DEPLOY](./decisions.md#d-deploy--deploy-via-github-actions-serving-the-site-directory)), the blush-pink design refresh ([D-DESIGN](./decisions.md#d-design--visual-identity-refreshed-to-the-blush-pink-print-identity)), and the reduction to four navigated pages + an unlisted `gift.html` ([D-IA4](./decisions.md#d-ia4--site-reduced-to-four-pages)), with the real Czech content in place. What remains before the wedding (2026-07-10):

## Immediate (no blockers)

1. 🎀 **Favicon refresh.** The browser-tab favicon (`site/favicon.svg`) is still the dark charcoal "T&J" &mdash; off-palette against the blush-pink identity. Regenerate it in the new identity (pink on white, Playfair).

## Mid-term (dependent)

- **Phase 5 &mdash; Photos.** The hero photo is in place + optimised (WebP + JPG, page-width); the O nás page was removed, so no further photos are required. Swap in a nicer hero later if desired (keep &le; 250 KB, Czech `alt`).
- **Phase 6 &mdash; Launch polish (now the main remaining work).** Run [../docs/qa-checklist.md](../docs/qa-checklist.md) end to end on real devices: WCAG AA contrast (the pink is decorative; body stays black), responsive / keyboard checks, performance, cross-browser, HTML/CSS validation, and a Czech spell-check of all copy.

## Long-term (not essential now)

- **English `/en/` mirror** (the Phase 2 language option; may be skipped entirely).
- **Self-host fonts** ([O-FONTS](./decisions.md#o-fonts--self-host-fonts-versus-google-fonts-cdn)) if privacy becomes a concern &mdash; bundle Playfair Display + Source Sans 3 into `site/assets/` instead of the Google Fonts CDN.

## Open questions

These are the OPEN items from [./decisions.md](./decisions.md); resolve with the owner:

1. **[O-FONTS](./decisions.md#o-fonts--self-host-fonts-versus-google-fonts-cdn)** &mdash; self-host fonts versus the Google Fonts CDN.

## Abbreviations

CDN &mdash; content delivery network; CSS &mdash; Cascading Style Sheets; OG &mdash; Open Graph; QR &mdash; quick-response code; SPAYD &mdash; Short Payment Descriptor (Czech QR payment standard); WCAG AA &mdash; Web Content Accessibility Guidelines, level AA.
