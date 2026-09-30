# wedding-website

Static informational website for Tereza & Jakub's wedding on 10 July 2026 in Prague (Vršovický
zámeček). Public but unlisted, hosted free on GitHub Pages, single-author, ~12-month lifecycle. Live at
<https://tereza-jakub.cz>. The repository separates **the deliverable** (the website, in `site/`) from
**the meta-layer** (`dev/`, `docs/`, `tools/`, `tmp/`) &mdash; see `dev/CONTEXT.md`.

## How to work here

- Only `site/` is served (the only directory GitHub Pages publishes); everything else is meta.
- **Em dashes use the entity `&mdash;`, not the Unicode character** &mdash; a repo-local override of
  the portfolio default, applying everywhere: HTML, Markdown, CSS, config files. In Markdown the entity
  still renders as a proper em dash through the inline-HTML pass.
- **CSS:** single `site/assets/css/main.css`, mobile-first; palette/type live as `--color-*` and
  typography custom properties at the top (the one place a palette/type change is made). Current
  identity: blush-pink accent (`#ed9dbc`) on white, charcoal body text, Playfair Display (headings) +
  Source Sans 3 (body) &mdash; see `dev/DECISIONS.md` D-DESIGN.
- **Page filenames stay English, content stays Czech** (vykání, warm but proper) &mdash; see
  `dev/DECISIONS.md` D-PAGES. `gift.html` is deliberately unlisted: not in the nav, not linked from any
  page, reachable only at the direct `/gift` URL.
- Avoid emojis in the website source (HTML/CSS/JS) and in `docs/` &mdash; the occasional
  owner-requested content emoji (e.g. 🙂 on a few content lines) is the one exception.
- A new third-party service needs an explicit decision logged in `dev/DECISIONS.md` first &mdash; see
  D-NOSERVICES.
- Before changing the visual design, palette, or page list: log the change in `dev/DECISIONS.md` and
  confirm with the owner first.
- Hero photo swap: `site/assets/img/hero.{webp,jpg}` &mdash; keep &le; 250 KB, EXIF-stripped, Czech
  `alt`, matching the frame's `width`/`height` in `index.html`.
- Local preview: `python3 -m http.server 8000 --directory site` (serves from `site/`, reproducing the
  deployed root exactly).
- Deploy: a push to `main` triggers `.github/workflows/deploy.yml`, which uploads `site/` to GitHub
  Pages. Full procedure: `docs/deployment.md`.
- The owner is a beginner with web frontend (deep with Python/CFD per the global CLAUDE.md) &mdash;
  brief teaching comments in HTML/CSS/JS are welcome where they explain a foundational concept.

## Steering docs

Read the one a task needs; the global CLAUDE.md § Documentation says what each holds and how it is kept.

- `dev/CONTEXT.md` &mdash; what this project is, why it exists, and the principles it follows.
- `dev/ROADMAP.md` &mdash; what comes next, in phases, with the backlog beneath.
- `dev/STATUS.md` &mdash; where things stand now: what landed last, what is in flight.
- `dev/DECISIONS.md` &mdash; what was decided, with rejected alternatives; cited by its `D-` id.
- `docs/architecture.md`, `docs/deployment.md`, `docs/qa-checklist.md` &mdash; reference documentation.

Every state change lands in `dev/` before the turn ends.

@MEMORY.md
