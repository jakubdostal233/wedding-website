# Step 01 — Foundation

First implementation step. Goal: a working `index.html` that proves the technical foundation is sound — directory structure, fonts, palette, base CSS, and the shared header/footer pattern.

## Table of contents

- [Goal](#goal)
- [Tasks](#tasks)
- [Acceptance criteria](#acceptance-criteria)
- [Decisions to make in this step](#decisions-to-make-in-this-step)
- [Risks](#risks)
- [Estimated effort](#estimated-effort)
- [What this step does NOT cover](#what-this-step-does-not-cover)

## Goal

By the end of this step, opening `index.html` in a browser shows a styled hero matching the design mockup: serif "Jakub & [J]" name, sans-serif date "10 · 7 · 2026", "Praha" subtitle, ivory background, charcoal text, sage accent. The site nav (header) and footer are present and link to placeholder URLs for the other pages (404 is fine — those pages don't exist yet).

## Tasks

### 1. Create asset directories

```
assets/
  css/
  js/
  img/
```

(No `fonts/` directory unless we self-host; default this step is Google Fonts CDN.)

### 2. Decide the shared-header/footer strategy

Three viable options for vanilla multi-page:

| Option | How | Pros | Cons |
|--------|-----|------|------|
| **A. Copy-paste** | Same HTML in every page | Zero magic, what-you-see-is-what-runs | Manual sync (or AI-assisted) on every change |
| **B. JS include at runtime** | Empty `<div id="header"></div>`, JS does `fetch('partials/header.html')` and injects | Single source of truth | Header pops in after page load (FOUC); bad for print/SEO; fails without JS |
| **C. Build step** | Tiny script (Python or `cat`) assembles HTML from partials at edit time | Single source of truth, no runtime cost | Adds a build step we explicitly chose to avoid |

**Recommendation: Option A.** With AI assist, "update the nav on every page" is one instruction. Reconsider only if the page count exceeds ~10.

### 3. Set up font loading

Add to the `<head>` of every page:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Inter:wght@400;500&display=swap">
```

`display=swap` shows fallback text immediately, swaps in the custom font once loaded — better than invisible-text-while-loading.

### 4. Write `assets/css/main.css`

Sections, in order:

1. **Reset** — minimal modern reset (`*, *::before, *::after { box-sizing: border-box; }`, `body { margin: 0; }`, etc.)
2. **Custom properties** — palette, type tokens, spacing scale, max-width tokens

   ```css
   :root {
     --color-bg:     #faf8f3;  /* ivory */
     --color-text:   #2a2a2a;  /* charcoal */
     --color-accent: #8a9a7b;  /* sage green */
     --color-muted:  #6b6b6b;

     --font-display: 'Cormorant Garamond', Georgia, serif;
     --font-body:    'Inter', system-ui, sans-serif;

     --space-xs: 0.5rem;
     --space-sm: 1rem;
     --space-md: 2rem;
     --space-lg: 4rem;
     --space-xl: 8rem;

     --max-width: 60rem;
   }
   ```

3. **Base typography** — `body`, `h1`–`h3`, `p`, `a`
4. **Layout primitives** — centered container, header bar, footer bar
5. **Hero block** — for the index page

### 5. Build `index.html`

- `<head>`: title, meta (charset, viewport, robots noindex, description), font links, CSS link
- `<header>`: site name + nav with all 7 page links
- `<main>`: hero block (names, date, place, optional hero image area)
- `<footer>`: copyright + minimal links

Names placeholder: "Jakub & [J]" until partner's name is locked in.

### 6. Test locally

- Open `index.html` directly in a browser → renders correctly
- Run `python3 -m http.server 8000` from the repo root → open <http://localhost:8000> → root-relative paths resolve
- Resize to ~375px wide → layout adapts cleanly
- Browser dev tools → no console errors, no failed network requests (other than 404s for unimplemented pages, which are fine)

### 7. Commit

After acceptance criteria pass, commit with a descriptive message. Use the `jd:git` skill for help grouping changes if needed.

## Acceptance criteria

- [ ] `index.html` renders with the modern minimalist look — ivory bg, charcoal text, sage accent, Cormorant Garamond for display, Inter for body
- [ ] Site header shows nav with all 7 pages (other links 404 for now — fine)
- [ ] Site footer present
- [ ] Mobile layout works (375px viewport — resize in browser)
- [ ] No console errors
- [ ] HTML validates as HTML5 (paste source into validator.w3.org)
- [ ] Works in Chrome and Firefox

## Decisions to make in this step

- **Shared-header/footer strategy.** Option A (copy-paste) recommended above. Confirm before writing the second page in Phase 2.
- **Fonts: CDN vs self-hosted.** Default is Google Fonts CDN. Switch to self-hosted later (Phase 6) if privacy matters.
- **Hero image.** Real photo not available yet. Use a solid sage band, a soft gradient, or a light-grey placeholder block until a photo is chosen.

## Risks

- **FOUT (flash of unstyled text)** — brief moment of fallback font before Cormorant/Inter loads. `display=swap` is the right tradeoff for a wedding site; users see something readable immediately.
- **Color contrast** — charcoal `#2a2a2a` on ivory `#faf8f3` is ~14:1 (well above WCAG AAA 7:1). Sage `#8a9a7b` on ivory has lower contrast — only use sage for non-essential accent text or large display headings, never body copy.
- **Path conventions** — relative paths like `assets/css/main.css` work from `index.html` at root. Sub-paths (e.g. `/en/index.html` in Phase 2) need `../assets/...` or root-relative `/assets/...`. Decide convention now: **root-relative `/`** is simpler at any depth.

## Estimated effort

2–4 hours focused work for someone new to HTML/CSS. Most of the time goes to the CSS and getting the hero typography to *feel* right.

## What this step does NOT cover

- Other pages (Phase 2)
- Real Czech content (Phase 3)
- Map, calendar, mailto, QR (Phase 4)
- Real photos (Phase 5)
- Polish, accessibility audit, performance (Phase 6)
- Domain and deploy (Phase 7)
