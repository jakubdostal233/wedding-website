# Implementation plan

Living document &mdash; the current to-do list. Finished tasks are DELETED (not ticked); the file is reordered as priorities shift. Phase names are the canonical ones from [./roadmap.md](./roadmap.md); decision IDs (`D-`/`O-`) reference [./decisions.md](./decisions.md).

Current state: the site is **built and live** at <https://tereza-jakub.cz> (all seven pages, content, map/calendar/QR/mailto integrations, and Open Graph cards). The 2026-06-06 repository restructure ([D-STRUCT](./decisions.md#d-struct--repository-restructured-to-the-tyre-model-architecture)) and the migration to a GitHub Actions deploy ([D-DEPLOY](./decisions.md#d-deploy--deploy-via-github-actions-serving-the-site-directory)) are done. What remains before the wedding (2026-07-10):

## Immediate (no blockers)

1. 📍 **Phase 4.5 &mdash; Visual design refresh from the print materials ([O-DESIGN](./decisions.md#o-design--visual-design-refresh-from-the-print-materials)).** Update the site's identity to match `tmp/style/svatebni-oznameni.pdf` + `tmp/style/jmenovky-design.pdf`: swap the **sage-green accent for the blush/dusty-pink palette**, align the typography to the elegant high-contrast display serif, and introduce the print motifs (rounded oval / arch shapes, thin charcoal hairlines, the stacked `10/07/26` date) &mdash; primarily in `site/assets/css/main.css` (custom properties / tokens) plus any per-page touches. Provisional palette and typography are captured in [O-DESIGN](./decisions.md#o-design--visual-design-refresh-from-the-print-materials).
   - First: **sample the exact hex values** from the two PDFs (don't ship the eyeballed estimates).
   - Gate (project rule): update [./SPEC.md](./SPEC.md) Design section and **re-confirm with the owner** before applying any visual change.

## Mid-term (dependent)

- **Phase 5 &mdash; Photos.** Source / shoot the hero photo and the about-us photos, optimise (target &le; 250 KB each, WebP + JPG fallback), write Czech `alt` text, and replace the placeholder blocks. Dependency: photo selection.
- **Phase 6 &mdash; Polish (remaining).** Finish the launch-quality pass: responsive testing on real devices, accessibility (semantic HTML, keyboard nav, WCAG AA contrast &mdash; note the new pink palette must still pass contrast), performance (image optimisation, font-display), cross-browser, HTML/CSS validation, Czech spell-check. Run [../docs/qa-checklist.md](../docs/qa-checklist.md) end to end. Dependency: Phase 4.5 (design) and Phase 5 (photos) settle the final look first.

## Long-term (not essential now)

- **English `/en/` mirror** (the Phase 2 language option; may be skipped entirely).
- **Self-host fonts** ([O-FONTS](./decisions.md#o-fonts--self-host-fonts-versus-google-fonts-cdn)) if privacy becomes a concern &mdash; bundle Cormorant Garamond + Inter (or the redesign's chosen faces) into `site/assets/` instead of the Google Fonts CDN.

## Open questions

These are the OPEN items from [./decisions.md](./decisions.md); resolve with the owner:

1. **[O-DESIGN](./decisions.md#o-design--visual-design-refresh-from-the-print-materials)** &mdash; the design refresh palette / typography (provisional inputs captured; needs exact sampling + SPEC update + sign-off).
2. **[O-FONTS](./decisions.md#o-fonts--self-host-fonts-versus-google-fonts-cdn)** &mdash; self-host fonts versus the Google Fonts CDN.

## Abbreviations

CDN &mdash; content delivery network; CSS &mdash; Cascading Style Sheets; OG &mdash; Open Graph; QR &mdash; quick-response code; SPAYD &mdash; Short Payment Descriptor (Czech QR payment standard); WCAG AA &mdash; Web Content Accessibility Guidelines, level AA.
