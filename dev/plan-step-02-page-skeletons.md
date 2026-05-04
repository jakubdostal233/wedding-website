# Step 02 &mdash; Page skeletons

Second implementation step. Goal: every page exists with shared header/footer and a stub content area; navigation works in both directions.

## Table of contents

- [Goal](#goal)
- [Tasks](#tasks)
- [Acceptance criteria](#acceptance-criteria)
- [Decisions confirmed in this step](#decisions-confirmed-in-this-step)
- [Conventions used](#conventions-used)
- [What this step does NOT cover](#what-this-step-does-not-cover)

## Goal

After this step, the site has all 7 pages (`index.html` from Step 01 plus 6 new). Each non-index page renders the shared header/footer and a stub content area with section structure plus minimal Czech placeholder text. Clicking any nav link from any page lands on the right page; the active page is indicated with `aria-current="page"`.

## Tasks

### 1. Confirm header/footer pattern

Step 01 settled on **Option A &mdash; copy-paste**. Each page carries identical header and footer markup; the only difference between pages is the `aria-current="page"` attribute on the matching nav link. Sync across pages stays manual (AI-assisted).

### 2. Add `.page` and `.timeline` styles to `assets/css/main.css`

- `.page` &mdash; vertical-rhythm wrapper for content pages (where `.hero` is the wrapper on the index page)
- `.timeline` &mdash; grid layout for `<dl>` time–event pairs on `program.html`

### 3. Create the 6 pages

| File | `<h1>` | Sections (stub) |
|------|--------|-----------------|
| `location.html` | Místo a čas | Obřad · Hostina · Mapa |
| `program.html` | Program | (timeline placeholder) |
| `transit.html` | Cesta a ubytování | Autem a parkování · Hromadná doprava · Ubytování |
| `about-us.html` | O nás | Náš příběh · Fotky |
| `contact.html` | Kontakt | Napište nám · Přidat do kalendáře |
| `gift.html` | Dar | (lead copy + QR placeholder) |

Each page:
- Same `<head>` as `index.html` &mdash; meta, fonts, CSS link
- Page-specific `<title>` in the form `Page name · Tereza & Jakub`
- Header copy-pasted from `index.html`, with `aria-current="page"` on the matching nav link
- `<main class="page container">` wrapping page-specific content
- Footer copy-pasted from `index.html`
- HTML comments (`<!-- TODO Phase X: ... -->`) marking what later phases will fill in (map, calendar, mailto, QR, photos)

### 4. Verify

- Click each nav link from each page &mdash; all 200 OK
- `python3 -m http.server` running, paths resolve
- 375px wide &mdash; header nav wraps, content readable
- DevTools console &mdash; no errors

## Acceptance criteria

- [ ] All 6 new pages exist and render
- [ ] Header (brand + nav) and footer are byte-identical across all 7 pages, except for the `aria-current="page"` attribute on the active nav item
- [ ] Each page's `<title>` is page-specific
- [ ] Each page has at least an `h1` and one section stub
- [ ] Mobile layout works at 375px
- [ ] No console errors

## Decisions confirmed in this step

- **Header/footer pattern.** Copy-paste (Option A from Step 01). Reconsider single-source-of-truth strategies (build script, JS injection) only if the page count exceeds ~10.
- **Title format.** `Page name · Tereza & Jakub` &mdash; page-specific part first so the meaningful bit is visible even when the browser truncates the tab title.
- **Active-page indicator.** `aria-current="page"` on the matching nav link. Styling already lives in `main.css` from Step 01 (sage underline).

## Conventions used

- **Phase markers in HTML comments.** `<!-- TODO Phase 4: mailto link -->`. Easy to grep when starting a later phase, and they document intent inline.
- **Czech placeholder copy.** Minimal, in vykání, clearly worded so it cannot accidentally ship as real content. Phase 3 replaces it.
- **`em` italics on placeholder lines** &mdash; e.g. `<em>Mapa bude vložena ve fázi 4.</em>` &mdash; visually flags content that's not the final copy.

## What this step does NOT cover

- Real Czech content (Phase 3)
- Map iframes, `.ics` download, `mailto:` link, SPAYD QR (Phase 4)
- Real photos (Phase 5)
- Accessibility audit, color-contrast verification, cross-browser checks, HTML validation (Phase 6)
- Domain and deploy (Phase 7)
