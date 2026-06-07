# Specification: Wedding Website

## Table of contents

- [Objective](#objective)
- [Stack and architecture](#stack-and-architecture)
- [Languages](#languages)
- [Access](#access)
- [Design](#design)
- [Pages](#pages)
- [Integrations](#integrations)
- [Deployment](#deployment)
- [Out of scope](#out-of-scope)
- [Pending content](#pending-content)
- [Open questions](#open-questions)
- [Risks and assumptions](#risks-and-assumptions)
- [Symbols and abbreviations](#symbols-and-abbreviations)

## Objective

Static informational website for **Tereza & Jakub**'s wedding on **10 July 2026 in Prague** (Vršovický zámeček). Tells guests when and where, how to get there, and what the day looks like; offers a contact channel, an "add to calendar" file, and an optional bank QR for financial gifts. Free hosting; low-effort to maintain; ~12-month lifecycle.

## Stack and architecture

- **Vanilla HTML / CSS / JavaScript** &mdash; no framework, no build step, no Node toolchain
- **Multi-page** architecture with shared header/footer (kept in sync manually with AI assistance)
- **Site files live in a dedicated `site/` directory** (`site/index.html`, `site/assets/…`, `site/CNAME`, `site/robots.txt`) &mdash; separated from the project meta-layer (`dev/`, `docs/`, `tools/`, `tmp/`). See `docs/architecture.md`.
- **Hosted on GitHub Pages**, free tier, **published via a GitHub Actions workflow** (`.github/workflows/deploy.yml`) that serves `site/` as the site root
- **Custom domain** `tereza-jakub.cz` (~200 CZK/yr), bound via the repo Pages settings/API and a `CNAME` file in `site/`
- **No backend, no database, no third-party services** (no analytics, no form services, no CDN beyond Google Fonts)

## Languages

- **Phase 1: Czech only.** Voice: vykání ("Milí přátelé, …"), warm but proper.
- **Phase 2 (optional, late):** English mirror under `/en/`.

Page filenames are in English regardless of content language to keep paths stable across phases.

## Access

- **Public but unlisted.** Discoverable only by the URL distributed to guests.
- `robots.txt` disallows all crawlers.
- Each HTML page includes `<meta name="robots" content="noindex">`.

## Design

- **Style:** modern minimalist &mdash; high-contrast serif headings, serif body, generous whitespace, a single blush-pink accent on white, photo-led. Refreshed from the printed wedding materials &mdash; see [decisions.md](./decisions.md#d-design--visual-identity-refreshed-to-the-blush-pink-print-identity) (D-DESIGN).
- **Palette:** white ground (`#FFFFFF`) · charcoal body text (`#2A2A2A`) · blush-pink accent (`#ED9DBC` &mdash; headings, names, links, dividers); blush hairlines (`#F0DDE4`)
- **Typography** (via Google Fonts): **Bodoni Moda** (title, all headings, and body &mdash; its `opsz` axis serves a high-contrast cut at display sizes and a readable, lower-contrast cut at body sizes) · **Tangerine** (the calligraphic `&` in the title)
- **Mobile-first** responsive layout

## Pages

| File | Czech section name | Purpose |
|------|--------------------|---------|
| `index.html` | Úvod | Hero &mdash; names, date, place, hero photo |
| `location.html` | Místo a čas | Ceremony venue + restaurant + time, map embeds |
| `program.html` | Program | Day timeline |
| `transit.html` | Cesta a ubytování | Directions, parking, transit, accommodation |
| `about-us.html` | O nás | Meeting story + photos |
| `contact.html` | Kontakt | Mailto, add-to-calendar, map links |
| `gift.html` | Dar | Bank QR for optional gifts (low priority) |

All pages share a single header (site nav) and footer.

## Integrations

- **Map:** `mapy.com` iframe embed (one for the ceremony venue, one for the restaurant)
- **Calendar:** single static `.ics` file in the repo; download button labelled "Přidat do kalendáře"
- **Email:** `mailto:` link with prefilled subject `Svatba 10.07.2026`
- **Bank QR:** Czech **SPAYD** format, generated from your account info, embedded as a static SVG/PNG in the repo (no JavaScript at runtime)

## Deployment

Live at <https://tereza-jakub.cz> (public but unlisted). Full procedure, DNS records, rollback, and renewal: `docs/deployment.md`.

- Develop locally: open `site/*.html` directly, or run `python3 -m http.server 8000 --directory site`
- Hosted on GitHub Pages, **published via GitHub Actions** (`.github/workflows/deploy.yml`): every push to `main` uploads `site/` as the Pages artifact and serves it as the site root
- Domain: `tereza-jakub.cz` registered at Wedos (~120 CZK/yr); bound via the repo Pages settings/API (a `CNAME` file in `site/` does not bind the domain on its own under the Actions source) with apex A records pointing at GitHub Pages
- Email: `info@tereza-jakub.cz` forwards to personal Gmail via Seznam Email Profi (free tier)
- HTTPS auto-issued by Let's Encrypt (enforced)

Total annual cost: ~200 CZK (domain only).

## Out of scope

- **RSVP** &mdash; handled outside the site (email/phone)
- **Photo gallery** beyond a few "About us" shots
- **English translation** &mdash; Phase 2 only, may be skipped entirely
- **Backend** of any kind
- **Forms** &mdash; guest contact is via `mailto:` only
- **Analytics** &mdash; none

## Pending content

These can be filled in over time; none block scaffolding or the foundation step:

- Photos (hero, "About us")

## Open questions

| # | Question | Why it matters | Resolution path |
|---|----------|----------------|-----------------|
| 1 | Self-host fonts vs. Google Fonts CDN | Privacy (Google sees a request when each page loads), GDPR, performance | Default: Google Fonts CDN; switch to self-hosted in Phase 6 if privacy becomes a concern |

## Risks and assumptions

| Item | Risk | Mitigation |
|------|------|------------|
| GitHub Pages serves all repo files | `dev/SPEC.md` etc. publicly accessible if URL is guessed | Low for a wedding site; `robots.txt` discourages crawlers; never put true secrets in tracked files |
| Multi-page header/footer drift | 7 pages = 7 copies of header HTML | AI-assisted sync; convert to a tiny include script if it becomes painful past ~10 pages |
| Mapy.com iframe stability | Embed format could change | Low risk; format is stable. Fall back to a static screenshot + outbound link if needed |
| SPAYD QR correctness | Wrong data → guests' payments fail or land elsewhere | Generate once, scan with two banking apps to verify before launch |
| Domain DNS propagation delay | Site unreachable for hours after a DNS change | Switch DNS ≥ 1 week before guests are invited |

All risks above are **low** unless flagged otherwise.

## Symbols and abbreviations

| Term | Meaning |
|------|---------|
| SPAYD | Short Payment Descriptor &mdash; Czech QR payment standard |
| EPC QR | European Payments Council QR &mdash; international QR payment standard |
| FOUT | Flash of Unstyled Text &mdash; brief moment before a custom font loads |
| CNAME | DNS record type for aliasing one domain to another |
| ToC | Table of Contents |
| iframe | Inline frame &mdash; embedded HTML document inside another page |
| WCAG | Web Content Accessibility Guidelines |
