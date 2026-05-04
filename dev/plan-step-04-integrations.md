# Step 04 &mdash; Integrations

Fourth implementation step. Goal: wire up the dynamic-feeling features &mdash; embedded maps, calendar download, payment QR, and contact mailto.

## Table of contents

- [Goal](#goal)
- [Scope of this commit](#scope-of-this-commit)
- [Tasks](#tasks)
- [Conventions used](#conventions-used)
- [Acceptance criteria](#acceptance-criteria)
- [What this step does NOT cover](#what-this-step-does-not-cover)

## Goal

Replace the Phase 3 placeholders with working integrations:

- Mapy.com iframes on `location.html` for both venues
- Downloadable `.ics` calendar file linked from `contact.html`
- SPAYD QR code and bank account block on `gift.html`
- `mailto:` link on `contact.html` &mdash; **deferred** until domain + email forwarding is set up

## Scope of this commit

The `mailto:` piece is deferred &mdash; the domain (e.g. `tereza-jakub.cz`) is being registered separately, and once email forwarding is live a follow-up commit will land the mailto link. The other three integrations ship now.

## Tasks

### 1. Map iframes (`location.html`)

Embed two Google Maps iframes (one per venue), built from the place coordinates:

| Section | Embed URL |
|---------|-----------|
| Obřad &mdash; Vršovický zámeček | `https://maps.google.com/maps?q=50.0698224,14.4522475&z=17&output=embed` |
| Hostina &mdash; Restaurace La Farma | `https://maps.google.com/maps?q=50.0761213,14.4599892&z=17&output=embed` |

Google Maps' `?q=<lat>,<lng>&output=embed` pattern works in iframes without an API key. We attempted `mapy.com/s/<id>?frame=1` first but mapy.com's modern embed flow needs auth tokens that the share dialog provides &mdash; reverting to plain Google Maps is simpler and reliable. Mapy.com outbound links (the "Otevřít na Mapy.cz" links under each venue) stay so guests can still use mapy.cz directly.

Iframes use `loading="lazy"` so they don't block initial render.

CSS: `.map-embed` &mdash; absolute-positioned iframe inside an aspect-ratio'd wrapper for responsive sizing.

The Phase 3 standalone "Mapa" section is removed; each venue carries its own embed inline.

### 2. Calendar `.ics` (`contact.html`)

Write `assets/wedding_tj.ics`:

- `DTSTART:20260710T090000Z` (= 11:00 Prague CEST)
- `DTEND:20260710T210000Z` (= 23:00 Prague)
- UTC times so calendar apps convert to whatever local timezone the guest is in
- `SUMMARY` / `DESCRIPTION` / `LOCATION` in Czech
- `UID` stable across regenerations: `tereza-jakub-svatba-20260710@tereza-jakub.cz`

Add a styled download button labelled "Přidat do kalendáře (.ics)" to `contact.html`.

### 3. SPAYD QR (`gift.html`)

Generate `assets/img/qr-platba.svg` from this SPAYD string:

```
SPD*1.0*ACC:CZ5920100000002601802091+FIOBCZPPXXX*X-VS:10072026*MSG:Svatba Tereza a Jakub
```

Generator script lives at `tools/generate-spayd-qr.py` (tracked in git so the SVG is reproducible). Run:

```bash
uv run --with segno python tools/generate-spayd-qr.py
```

Embed the SVG on `gift.html` inside a `.qr-block` card with the bank info underneath:

| Field | Value |
|-------|-------|
| Číslo účtu | 2601802091/2010 |
| IBAN | CZ59 2010 0000 0026 0180 2091 |
| BIC/SWIFT | FIOBCZPPXXX |
| Variabilní symbol | 10072026 |

### 4. CSS additions (`main.css`)

- `.map-embed` &mdash; aspect-ratio wrapper for responsive iframes
- `.button` &mdash; ghost outline button (used for the ICS download; reusable later)
- `.qr-block` &mdash; centered card around QR + bank info

## Conventions used

- **Map iframes.** Google Maps `?q=<lat>,<lng>&output=embed` pattern (no API key needed); `loading="lazy"`; responsive aspect-ratio wrapper.
- **ICS file.** UTC times so the event renders correctly in any guest's local timezone. Single `.ics`, downloaded by guests.
- **QR generator.** Python script in `tools/` (tracked, single-purpose). Output SVG is the tracked artefact under `assets/img/`. Re-run only when account info changes.

## Acceptance criteria

- [ ] Both Google Maps load and are zoomable in iframes on `location.html`
- [ ] Mobile at 375px: iframes scale cleanly, QR renders sharp, ICS button is readable and tappable
- [ ] Clicking "Přidat do kalendáře" downloads `wedding_tj.ics`; opening in any calendar app shows the event "Svatba | Tereza a Jakub" on 10. 7. 2026, 11:00 local
- [ ] Scanning the QR with **two** banking apps both show: Fio account `2601802091/2010`, VS `10072026`, message "Svatba Tereza a Jakub", amount blank (guest enters)
- [ ] No console errors

## What this step does NOT cover

- `mailto:` link &mdash; deferred to a follow-up once domain + email forwarding are set up
- Real photos (Phase 5)
- Accessibility audit, HTML/CSS validation, performance, cross-browser (Phase 6)
- Domain registration and deploy (Phase 7)
