# Implementation plan

Living document &mdash; the current to-do list. Finished tasks are DELETED (not ticked); the file is reordered as priorities shift. Phase names are the canonical ones from [./roadmap.md](./roadmap.md); decision IDs (`D-`/`O-`) reference [./decisions.md](./decisions.md).

Current state: the site is **built and live** at <https://tereza-jakub.cz> (all seven pages, content, map/calendar/QR/mailto integrations, and Open Graph cards). The 2026-06-06 repository restructure ([D-STRUCT](./decisions.md#d-struct--repository-restructured-to-the-tyre-model-architecture)) and the migration to a GitHub Actions deploy ([D-DEPLOY](./decisions.md#d-deploy--deploy-via-github-actions-serving-the-site-directory)) are done. What remains before the wedding (2026-07-10):

## Immediate (no blockers)

1. 🎨 **Phase 4.5 &mdash; print motifs (palette + typography are done; see [D-DESIGN](./decisions.md#d-design--visual-identity-refreshed-to-the-blush-pink-print-identity)).** The blush-pink palette (`#ED9DBC` accent on `#FFFFFF`) and the typography (Bodoni Moda for title / headings / body, Tangerine for the title `&`) are applied. Still to bring over from `tmp/style/svatebni-oznameni.pdf` + `jmenovky-design.pdf`: the recurring **motifs** &mdash; rounded oval / arch shapes, thin hairline frames, vertical hairline dividers, and the stacked `10 / 07 / 26` date block. Primarily `site/assets/css/main.css` plus any per-page touches.

## Mid-term (dependent)

- **Phase 5 &mdash; Photos.** Source / shoot the hero photo and the about-us photos, optimise (target &le; 250 KB each, WebP + JPG fallback), write Czech `alt` text, and replace the placeholder blocks. Dependency: photo selection.
- **Phase 6 &mdash; Polish (remaining).** Finish the launch-quality pass: responsive testing on real devices, accessibility (semantic HTML, keyboard nav, WCAG AA contrast &mdash; note the new pink palette must still pass contrast), performance (image optimisation, font-display), cross-browser, HTML/CSS validation, Czech spell-check. Run [../docs/qa-checklist.md](../docs/qa-checklist.md) end to end. Dependency: Phase 4.5 (design) and Phase 5 (photos) settle the final look first.

## Long-term (not essential now)

- **English `/en/` mirror** (the Phase 2 language option; may be skipped entirely).
- **Self-host fonts** ([O-FONTS](./decisions.md#o-fonts--self-host-fonts-versus-google-fonts-cdn)) if privacy becomes a concern &mdash; bundle Bodoni Moda + Tangerine into `site/assets/` instead of the Google Fonts CDN.

## Open questions

These are the OPEN items from [./decisions.md](./decisions.md); resolve with the owner:

1. **[O-FONTS](./decisions.md#o-fonts--self-host-fonts-versus-google-fonts-cdn)** &mdash; self-host fonts versus the Google Fonts CDN.

## Abbreviations

CDN &mdash; content delivery network; CSS &mdash; Cascading Style Sheets; OG &mdash; Open Graph; QR &mdash; quick-response code; SPAYD &mdash; Short Payment Descriptor (Czech QR payment standard); WCAG AA &mdash; Web Content Accessibility Guidelines, level AA.
