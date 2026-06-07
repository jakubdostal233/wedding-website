# Implementation plan

Living document &mdash; the current to-do list. Finished tasks are DELETED (not ticked); the file is reordered as priorities shift. Phase names are the canonical ones from [./roadmap.md](./roadmap.md); decision IDs (`D-`/`O-`) reference [./decisions.md](./decisions.md).

Current state: the site is **built and live** at <https://tereza-jakub.cz> (all seven pages, content, map/calendar/QR/mailto integrations, and Open Graph cards). The 2026-06-06 repository restructure ([D-STRUCT](./decisions.md#d-struct--repository-restructured-to-the-tyre-model-architecture)) and the migration to a GitHub Actions deploy ([D-DEPLOY](./decisions.md#d-deploy--deploy-via-github-actions-serving-the-site-directory)) are done. What remains before the wedding (2026-07-10):

## Immediate (no blockers)

1. 🧱 **Restructure to 4 pages + jakubmares.cz-style typography + new content.** Reduce the 7 pages to 4 (`index`, `program`, `practical-info`, `about-us`); swap to **Playfair Display + Source Sans 3** (replacing Bodoni Moda + Tangerine; palette unchanged); rebuild **Program** as an alternating vertical timeline like `jakubmares.cz/#program`; load the copy from `tmp/website-content.txt`; add + optimise the hero photo; regenerate `wedding_tj.ics`. **Full plan:** [./archive-plans/2026-06-07_restructure-4pages-fonts-content.md](./archive-plans/2026-06-07_restructure-4pages-fonts-content.md). This **supersedes** the earlier print-motifs direction (we now match jakubmares.cz, not the print materials' arch / date-block motifs) and the typography half of [D-DESIGN](./decisions.md#d-design--visual-identity-refreshed-to-the-blush-pink-print-identity).

## Mid-term (dependent)

- **Phase 5 &mdash; Photos.** The hero photo (`tmp/photos/tereza-jakub-1.jpg`) is added + optimised as part of the restructure above; about-us photos are dropped (O nás is title-only). Any further photos: optimise (target &le; 250 KB each, WebP + JPG fallback), write Czech `alt` text.
- **Phase 6 &mdash; Polish (remaining).** Finish the launch-quality pass: responsive testing on real devices, accessibility (semantic HTML, keyboard nav, WCAG AA contrast &mdash; note the new pink palette must still pass contrast), performance (image optimisation, font-display), cross-browser, HTML/CSS validation, Czech spell-check. Run [../docs/qa-checklist.md](../docs/qa-checklist.md) end to end. Dependency: Phase 4.5 (design) and Phase 5 (photos) settle the final look first.

## Long-term (not essential now)

- **English `/en/` mirror** (the Phase 2 language option; may be skipped entirely).
- **Self-host fonts** ([O-FONTS](./decisions.md#o-fonts--self-host-fonts-versus-google-fonts-cdn)) if privacy becomes a concern &mdash; bundle Playfair Display + Source Sans 3 into `site/assets/` instead of the Google Fonts CDN.

## Open questions

These are the OPEN items from [./decisions.md](./decisions.md); resolve with the owner:

1. **[O-FONTS](./decisions.md#o-fonts--self-host-fonts-versus-google-fonts-cdn)** &mdash; self-host fonts versus the Google Fonts CDN.

## Abbreviations

CDN &mdash; content delivery network; CSS &mdash; Cascading Style Sheets; OG &mdash; Open Graph; QR &mdash; quick-response code; SPAYD &mdash; Short Payment Descriptor (Czech QR payment standard); WCAG AA &mdash; Web Content Accessibility Guidelines, level AA.
