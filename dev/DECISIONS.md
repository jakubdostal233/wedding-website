# Decisions &mdash; wedding-website

Every entry carries a fixed id &mdash; `D-` plus a short upper-case topic mnemonic, unique here and
never renamed; the id is the one way to cite it anywhere. The **State** line, not the id, says whether
an entry is decided or still open. All decisions are approved by the owner.

## Table of contents

- [Abbreviations](#abbreviations)
- [Decided](#decided)
- [Open](#open)

## Abbreviations

| Abbreviation | Meaning                                                                                          |
| ------------ | ------------------------------------------------------------------------------------------------ |
| CDN          | Content delivery network                                                                         |
| CNAME        | DNS record aliasing one domain to another (and the GitHub Pages file that binds a custom domain) |
| DNS          | Domain Name System                                                                               |
| SPAYD        | Short Payment Descriptor &mdash; Czech QR payment standard                                       |

## Decided

### D-DESIGN &mdash; Visual identity refreshed to the blush-pink print identity

**State:** ✅ DECIDED · 2026-06-07 (typography updated 2026-06-07, times-color updated 2026-07-03)

**Decision:** The site adopts the blush-pink identity of the printed wedding materials
(`tmp/style/svatebni-oznameni.pdf`, `jmenovky-design.pdf` &mdash; checksums in
[docs/evidence/D-DESIGN/manifest.md](../docs/evidence/D-DESIGN/manifest.md)), replacing the inception
ivory/charcoal/sage scheme. Palette: accent `#ED9DBC` (rose pink, sampled from the print CMYK fills) for
headings/names/links/dividers, white ground `#FFFFFF`, charcoal body text `#2A2A2A`, blush hairlines
`#F0DDE4`. Typography (all via Google Fonts, matching <https://www.jakubmares.cz>): **Playfair Display**
for titles and all headings, **Source Sans 3** for body text, a plain Playfair `&` in the title. The
Program timeline's **times** are charcoal, not the accent pink &mdash; the pink measures ~2.07:1 on
white and fails WCAG AA even at large text, so the pink stays for decorative display only (titles,
headings, names, links) while functional schedule text takes the readable charcoal.

**Why:** The print faces (`Agraham-PersonalUse`, `terranika`, `Didot`) are not available as usable
`@font-face` files and `Agraham` cannot set Czech diacritics at all; the Google Fonts equivalents avoid
self-hosting and licensing work and already cover Czech. An earlier Bodoni Moda + Tangerine pairing
(closer to the print faces) shipped briefly on 2026-06-07 before the owner chose to match
jakubmares.cz's Playfair Display + Source Sans 3 pairing instead; the sampled palette was unchanged by
that switch.

**Revisit when:** -

### D-IA4 &mdash; Site reduced to four pages

**State:** ✅ DECIDED · 2026-06-07

**Decision:** The seven-page structure is reduced to four navigated pages &mdash; `index.html` (Úvod),
`program.html` (Program), `practical-info.html` (Praktické informace), `photoshooting.html` (Focení)
&mdash; plus one page kept out of the nav, `gift.html` (Dar + bank QR + IBAN), reachable only directly
at `/gift`. `location.html`, `transit.html`, `contact.html` and `about-us.html` (O nás) are removed;
their content relocates into the four remaining pages (maps + calendar → Program; transport, dress code,
menus, children, Dar thank-you, Různé, Kontakt → Praktické informace; photo-shoot groups →
Photoshooting). Accommodation (ubytování) is dropped; O nás is dropped entirely.

**Why:** Simpler navigation for guests, payment details kept off the public nav, and the supplied
content fit cleanly into four pages. Partially supersedes D-PAGES (the page count only &mdash; the
multi-page architecture, English filenames and Czech content all stand).

**Revisit when:** -

### D-DEPLOY &mdash; Deploy via GitHub Actions, serving the `site/` directory

**State:** ✅ DECIDED · 2026-06-06

**Decision:** GitHub Pages publishes via a GitHub Actions static-upload workflow
(`.github/workflows/deploy.yml`) that uploads the `site/` directory as the Pages artifact, replacing the
previous legacy "deploy from a branch (root)" source. `site/` is served as the site root, so the Open
Graph absolute URLs stay correct and `CNAME` / `robots.txt` ship inside `site/`. The site stays
build-less &mdash; the workflow only uploads static files.

**Why:** A dedicated `site/` directory (D-STRUCT) is incompatible with legacy branch-deploy, which
serves only `/` or `/docs`; the Actions path serves an arbitrary folder as root with no build step. Full
procedure: [docs/deployment.md](../docs/deployment.md).

**Revisit when:** -

### D-STRUCT &mdash; Repository restructured to the tyre-model architecture

**State:** ✅ DECIDED · 2026-06-06

**Decision:** The repository separates the deliverable from the meta-layer, mirroring the `tyre-model`
reference project. The website (all HTML, `assets/`, `favicon.svg`, `CNAME`, `robots.txt`) lives in
`site/`; `dev/` holds steering documents; `docs/` holds reference documentation; `tools/` holds the
offline generator scripts; `tmp/` is gitignored scratch.

**Why:** Navigability and ease of development &mdash; a clean mental model of "what is served" versus
"the process around it". See [docs/architecture.md](../docs/architecture.md).

**Revisit when:** -

### D-NOSERVICES &mdash; No third-party services

**State:** ✅ DECIDED · 2026-05 (inception)

**Decision:** No third-party runtime services &mdash; no analytics, no form backends (e.g. Formspree),
no CDN beyond Google Fonts. Map embeds use Google Maps iframes; the bank QR is a static SPAYD SVG
generated offline; contact is `mailto:` only; the calendar is a static `.ics` file.

**Why:** Privacy, simplicity, zero ongoing cost and zero runtime dependencies.

**Revisit when:** Adding a new integration that would need one &mdash; log the new decision here first.

### D-PRIVACY &mdash; Public but unlisted

**State:** ✅ DECIDED · 2026-05 (inception)

**Decision:** The site is public but unlisted &mdash; discoverable only via the URL given to guests.
`robots.txt` disallows all crawlers and every page carries
`<meta name="robots" content="noindex,nofollow">`. No true secrets live in tracked files, since the
whole repository is technically reachable.

**Why:** A wedding site should not be search-indexed, but needs no authentication.

**Revisit when:** -

### D-HOST &mdash; GitHub Pages + custom domain

**State:** ✅ DECIDED · 2026-05 (inception)

**Decision:** Hosted free on GitHub Pages, fronted by the custom domain `tereza-jakub.cz` (registered at
Wedos), bound via the repo's Pages settings. Email `info@tereza-jakub.cz` forwards via Seznam Email
Profi (free tier). Total cost ~165 CZK + VAT / year (domain only).

**Why:** Free, reliable static hosting; the owner already controls the domain and email. The deploy
_mechanism_ is superseded by D-DEPLOY; the host and domain are unchanged. See
[docs/deployment.md](../docs/deployment.md).

**Revisit when:** -

### D-PAGES &mdash; Multi-page, English filenames, Czech content

**State:** ✅ DECIDED · 2026-05 (inception)

**Decision:** Multi-page architecture with a shared header/footer kept in sync manually (with AI
assistance). Page filenames are English; content is Czech (vykání, warm but proper). An English mirror
under `/en/` is a possible later phase.

**Why:** English filenames keep paths stable if an English mirror is ever added; Czech content matches
the audience. The page _count_ was later reduced by D-IA4; the architecture, filenames and content
language stand.

**Revisit when:** -

### D-STACK &mdash; Vanilla static site, no build step

**State:** ✅ DECIDED · 2026-05 (inception)

**Decision:** The site is vanilla HTML / CSS / JavaScript with no framework, no build step, and no Node
toolchain. A single stylesheet (`site/assets/css/main.css`), mobile-first.

**Why:** Lowest maintenance and lowest hosting cost for a small, ~12-month-lifecycle informational site;
nothing to break in a build pipeline.

**Revisit when:** -

## Open

### D-FONTS &mdash; Self-host fonts versus Google Fonts CDN

**State:** ❓ OPEN · 2026-06-07

**Question:** Keep loading Playfair Display + Source Sans 3 (D-DESIGN) from the Google Fonts CDN, or
self-host them in `site/assets/`?

**Blocks:** Nothing &mdash; can wait.

**Options:** a) Keep the Google Fonts CDN (current default) &mdash; simplest, but Google sees a request
on each page load (privacy/GDPR), and it is the one exception D-NOSERVICES carves out for a third-party
dependency. b) Self-host the two font families in `site/assets/` &mdash; removes that dependency, at the
cost of bundling and updating the font files by hand.
