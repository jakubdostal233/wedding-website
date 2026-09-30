# Status &mdash; wedding-website

Last updated: 2026-09-30

## Summary

The site is built and live at <https://tereza-jakub.cz>. Every planned integration works; the one item
outstanding before the wedding (2026-07-10) is the owner's real-device QA pass.

## Last landed

- 2026-07-07 &mdash; seating plans embedded inline in Praktické informace; `gift.html` unlinked from
  every page (reachable only at the direct `/gift` URL); Gröbovka parking links added.
- 2026-07-07 &mdash; four reception seating-scheme SVGs (numbered and named-guest variants) generated as
  tracked assets.
- 2026-07-03 &mdash; site-wide QA pass (HTML validation, contrast, link checks, favicon refresh); URL
  distributed to guests.

## In flight

- Owner-side real-device QA &mdash; see [ROADMAP.md](./ROADMAP.md) § Active and
  [docs/qa-checklist.md](../docs/qa-checklist.md).

## What works

- [x] All five pages (four navigated + the unlisted gift page) built, styled, and live &mdash;
      [docs/architecture.md](../docs/architecture.md).
- [x] Every integration (maps, calendar file, `mailto:`, bank QR, Open Graph cards) wired and working
      &mdash; docs/architecture.md § 4.
- [x] Deployed via GitHub Actions to the custom domain with HTTPS enforced &mdash;
      [docs/deployment.md](../docs/deployment.md).

## What's blocked

<!-- nothing blocked -->
