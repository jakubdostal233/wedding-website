# Plan &mdash; restructure to 4 pages, jakubmares.cz-style typography, new content

- **Date:** 2026-06-07
- **Status:** approach locked with the owner; execution pending the GO.
- **Supersedes:** the typography half of [D-DESIGN](../decisions.md#d-design--visual-identity-refreshed-to-the-blush-pink-print-identity) (Bodoni Moda + Tangerine) &mdash; replaced by Playfair Display + Source Sans 3. The **palette is unchanged**.

## 🎯 Goal

Reduce the seven pages to four, adopt the font pairing of <https://www.jakubmares.cz> (Playfair Display + Source Sans 3) while keeping our blush-pink palette, replace the site copy from `tmp/website-content.txt`, and rebuild **Program** as an alternating vertical timeline like `jakubmares.cz/#program`.

## ✅ Decisions (locked with owner 2026-06-07)

- **Multi-page** (4 pages), English filenames, Czech content.
- **Fonts:** Playfair Display (titles + headings) + Source Sans 3 (body). Drop Bodoni Moda + Tangerine. Plain Playfair `&` in the title (no calligraphic ampersand).
- **Palette preserved:** pink `#ED9DBC` for **titles and main/heading text**; **black / charcoal `#2A2A2A` for body text and high-contrast structural bits** (e.g. timeline dots) &mdash; "the way it is now". Black is fine wherever contrast needs it. White `#FFFFFF` ground.
- **Keep** the bank QR + IBAN (under Dar). **Drop** accommodation (ubytování).
- New filename **`practical-info.html`**. Nav = brand (→ home) + **Program · Praktické informace · O nás**. **Regenerate `wedding_tj.ics`** to the new timeline times.
- **Maps:** keep the interactive `mapy.com` embeds + "Otevřít na Mapy.cz / Google Maps" buttons (our current "Místo a čas" style), for **three** places; the embed cards/buttons may be restyled to echo the reference (rounded, dark button).

## 🔍 Reference design (jakubmares.cz &mdash; `tmp/style/program.PNG`, `tmp/style/fonts.PNG`, + live render)

- **Hero:** full-bleed photo, the names centred in Playfair, the date flanked by short dashed rules.
- **Program "dne":** an **alternating vertical centre timeline** &mdash; a thin centre line with a solid **dot** at each event; events **zig-zag left/right**; the **time range is bold**, the label sits **below** it (uppercase + letter-spaced + muted in the reference). Collapses to a single left-aligned column on mobile.
- **Type:** Playfair bold headings; Source Sans 3 body in grey.
- **Venue blocks (ref):** rounded photo card + dark "Otevřít v Google Maps" button.

### Adaptations to us
1. **Colour:** centre line + **dots in black/charcoal** (per owner, for contrast); time in bold charcoal; label below in grey; only the section **heading is pink**. Add a pink touch only if a render looks flat. Verify with renders.
2. **Longer labels:** our timeline rows are full sentences with **clickable map links** (not terse uppercase), so labels stay **normal case** for readability while keeping the zig-zag structure.
3. **Maps:** keep interactive embeds (not the ref's static photo card), but may borrow the rounded-card + dark-button styling.
4. **Hero:** match the reference's full-bleed photo with the name overlaid (a change from the current centred hero + placeholder block) &mdash; confirm at render time.

## 🗂️ Pages: 7 → 4

| Page | Nav label | Content |
|---|---|---|
| `index.html` | (brand → home) | Hero: full-bleed photo + names / date / place |
| `program.html` | Program | Alternating timeline + "Vynecháváme" + add-to-calendar + 3 map blocks |
| `practical-info.html` *(new)* | Praktické informace | Dress code, hostina menu, raut, doprava & parkování, program pro děti, Dar (QR + IBAN), Kontakt |
| `about-us.html` | O nás | Title only |

**Delete:** `location.html`, `transit.html`, `contact.html`, `gift.html` (content relocates per the table; accommodation dropped). The `qr-platba.svg`, `wedding_tj.ics` (regenerated), and `og-card.png` assets are retained.

## 🛠️ Implementation steps

> 👁️ **Verification rule (owner-mandated): render every implemented unit with `jd-pers:look` and read the PNG back before moving on** &mdash; each page, the font swap, the hero, the timeline, every map block and section. Local files render directly; for any live check use the `--ignore-certificate-errors` + `--virtual-time-budget` Chromium technique (see [workflow-tracking.md](../workflow-tracking.md)). Fix what the render reveals before proceeding.

1. **Docs / re-confirm gate.** Update [SPEC.md](../SPEC.md) (Pages table → 4; Design → Playfair Display + Source Sans 3, palette unchanged), [decisions.md](../decisions.md) (amend D-DESIGN typography → Playfair/Source Sans 3 + plain `&`; record the 7→4 page-list change), [roadmap.md](../roadmap.md) "where we are now". This plan is referenced from [plan.md](../plan.md).
2. **Structure.** Create `practical-info.html`; rewrite the shared header/footer (4-item nav) across `index` / `program` / `practical-info` / `about-us`; remove `location.html`, `transit.html`, `contact.html`, `gift.html`; fix all internal links. Manual header/footer sync (4 copies).
3. **Fonts.** Swap the Google Fonts `<link>` on all 4 pages → Playfair Display (ital,wght 400–700) + Source Sans 3 (wght 300–700); remove Bodoni Moda + Tangerine. In `main.css`: `--font-display: 'Playfair Display'`, `--font-body: 'Source Sans 3'`, remove `--font-script`, simplify `.hero__amp` to a plain Playfair `&`. Palette tokens unchanged; use black where contrast needs it.
4. **Content** (from `tmp/website-content.txt`, Czech):
   - **index** &mdash; optimise `tmp/photos/tereza-jakub-1.jpg` (**11.4 MB** → ≤ 250 KB, ~1600–2000 px, WebP + JPG fallback), move to `site/assets/img/`, full-bleed hero with overlaid name.
   - **program** &mdash; alternating-timeline CSS + 8 rows (10:30→16:00) with inline links (Vršovický zámeček, Havlíčkovy sady/Gröbovka → mapy.com; La Farma → lafarma.cz); the "Vynecháváme" list; add-to-calendar (regenerate `wedding_tj.ics`); 3 map blocks (reuse the 2 existing embeds + add Havlíčkovy sady).
   - **practical-info** &mdash; dress code; hostina menu (soup + 3 mains); raut menu + sides + drinks note; doprava & parkování (EasyPark / zones / Flora, with links); program pro děti (playground link); Dar (thank-you + QR + IBAN); Kontakt (`mailto:info@tereza-jakub.cz`).
   - **about-us** &mdash; heading "O nás" only.
5. **Verify.** Render each page (local file renders; for any live check use the `--ignore-certificate-errors` + `--virtual-time-budget` Chromium technique &mdash; see [workflow-tracking.md](../workflow-tracking.md)). Check Czech diacritics, the mobile timeline collapse, and contrast (pink decorative, black body).
6. **Docs refresh.** [architecture.md](../../docs/architecture.md) (pages, fonts, timeline), [qa-checklist.md](../../docs/qa-checklist.md) (nav 6→3, section list), [CLAUDE.md](../../.claude/CLAUDE.md) (identity + page list), [README.md](../../README.md).
7. **Commit** via `jd:git` in logical groups, then push (deploys via Actions).

## ⚠️ Risks / notes

- Hero photo is **11.4 MB** &mdash; must be optimised before shipping (perf).
- Header/footer are duplicated across 4 pages and kept in manual sync.
- `.ics` correctness &mdash; re-verify the regenerated event against the new timeline.
- Inspect `location.html`'s actual map-embed mechanism (iframe host) before reusing it for the 3 blocks.
- Contrast: pink on white is decorative only; body text stays black for WCAG AA.
