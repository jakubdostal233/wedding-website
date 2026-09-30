# Roadmap &mdash; wedding-website

## Goal

Guests informed and able to attend: a live, guest-tested site with every integration working, ready
before the wedding on 2026-07-10 (mirrors `dev/CONTEXT.md`).

## Active

- 🔄 **Phase 6 &mdash; Polish** &mdash; the desktop/automated QA pass is done (2026-07-03); the one
  remaining item is owner-side real-device testing. ▸ Run
  [docs/qa-checklist.md](../docs/qa-checklist.md) on real phones/tablets, including the bank QR in two
  banking apps.

## Phases

### Phase 1 &mdash; Foundation ✅

Directory scaffold, base CSS custom properties, shared header/footer, fonts loaded, a working
`index.html`.

### Phase 2 &mdash; Page skeletons ✅

Every page created with the shared header/footer; nav links work both ways.

### Phase 3 &mdash; Content draft ✅

Real Czech copy on every page.

### Phase 4 &mdash; Integrations ✅

Maps, the `.ics` calendar, `mailto:`, and the SPAYD bank QR all wired and working end-to-end.

### Phase 4.5 &mdash; Design refresh from print materials ✅

The blush-pink identity was sampled from the printed wedding materials and shipped. See
[DECISIONS.md](./DECISIONS.md) D-DESIGN.

### Phase 5 &mdash; Photos ✅

Hero photo in place (`hero.webp` + `hero.jpg`, optimised, Czech `alt` text). A nicer replacement is an
optional backlog item, not a blocker.

### Phase 6 &mdash; Polish 🔄

Desktop + automated QA passed 2026-07-03 (HTML validation, contrast math, link checks, a mobile fix for
the gift-page number wrap, Open Graph tags on every page). Owner-side real-device QA is the one item
outstanding &mdash; see **Active** above.

### Phase 7 &mdash; Domain and deploy ✅

Live at <https://tereza-jakub.cz>, HTTPS enforced, URL distributed to guests (confirmed 2026-07-03). See
[DECISIONS.md](./DECISIONS.md) D-HOST and D-DEPLOY.

## Acceptance / success criteria

- [x] Site live at the custom domain with HTTPS
- [x] URL distributed to guests
- [ ] Owner-side real-device QA run and passed ([docs/qa-checklist.md](../docs/qa-checklist.md))

## Backlog

- Nicer hero photo swap (optional, owner to provide) &mdash; keep &le;250 KB, Czech `alt`, matching the
  frame's `width`/`height` in `index.html`.
- English `/en/` mirror (optional, may be skipped entirely).
- Self-host fonts instead of the Google Fonts CDN &mdash; see [DECISIONS.md](./DECISIONS.md) D-FONTS.
