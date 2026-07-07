# Wedding Website &mdash; Project Context

Static informational website for **Tereza & Jakub**'s wedding on **10 July 2026 in Prague** (Vršovický zámeček). Public but unlisted, hosted free on GitHub Pages, single-author, ~12-month lifecycle. **Live at <https://tereza-jakub.cz>.**

The repository separates **the deliverable** (the website, in `site/`) from **the meta-layer** (planning in `dev/`, reference docs in `docs/`, generators in `tools/`, scratch in `tmp/`) &mdash; the same split as the `~/git/tyre-model/` reference project.

## Where things live

Entry points (read first; keep current whenever anything that affects them changes):

- [./CLAUDE.md](./CLAUDE.md) (this file) &mdash; agent-facing, lean; signposts to everything below.
- [../README.md](../README.md) &mdash; human-facing repo overview: what it is, the layout, how to preview, current status.

The deliverable:

- [../site/](../site/) &mdash; **everything that is served** (the site root): the five `*.html` pages (`index`, `program`, `practical-info`, `photoshooting` &mdash; plus the unlisted `gift`, not in the nav), `favicon.svg`, `CNAME`, `robots.txt`, and `assets/` (`css/main.css`, `img/`, `js/`, `wedding_tj.ics`). This is the only directory GitHub Pages publishes.

Steering (`dev/`, operational):

- [../dev/SPEC.md](../dev/SPEC.md) &mdash; the source of truth: what we're building, scope, open items.
- [../dev/roadmap.md](../dev/roadmap.md) &mdash; phased plan **and** the "where we are now" status (the canonical phase names).
- [../dev/plan.md](../dev/plan.md) &mdash; the live to-do list; finished tasks are deleted, not ticked.
- [../dev/decisions.md](../dev/decisions.md) &mdash; decision log (`D-` decided / `P-` proposed / `O-` open).
- [../dev/worklog.md](../dev/worklog.md) &mdash; transient, newest-first log of state-changing work; promote settled facts to the right doc, then delete here.
- [../dev/workflow-tracking.md](../dev/workflow-tracking.md) &mdash; skill/hook/tooling feedback (what helps, what hinders, improvement ideas).
- [../dev/workflow-emojis-reference.md](../dev/workflow-emojis-reference.md) &mdash; the emoji vocabulary for `dev/` markdown and chat.
- [../dev/archive-plans/](../dev/archive-plans/), [../dev/archive-prompts/](../dev/archive-prompts/), [../dev/archive-audits/](../dev/archive-audits/) &mdash; immutable dated snapshots (`YYYY-MM-DD_slug.md`); not transient.

Documentation (`docs/`, reference, ToC + Abbreviations at top, no emojis):

- [../docs/architecture.md](../docs/architecture.md) &mdash; how the website works: layout, the multi-page static structure, assets/CSS, integrations, generators, deployment.
- [../docs/deployment.md](../docs/deployment.md) &mdash; how to deploy / update / roll back; DNS, domain, costs.
- [../docs/qa-checklist.md](../docs/qa-checklist.md) &mdash; functional checks to run on real devices before sharing the URL.

Tooling and scratch:

- [../tools/](../tools/) &mdash; offline generators that produce tracked assets (`generate-og-card.py`, `generate-spayd-qr.py`, `generate-seating-schemes.py`); they write into `site/assets/img/`, and the seating generator additionally re-injects the inline plans into `practical-info.html` between its `seating-plans` markers. Not served.
- [../tmp/](../tmp/) &mdash; gitignored scratch (drafts, exports, the design-source PDFs in `tmp/style/`). Don't reference `tmp/` from tracked files.

## Stack

Vanilla HTML / CSS / JavaScript, no build step, no Node toolchain. Multi-page architecture with a shared header/footer kept in sync manually (with AI assist).

## Project conventions

- **Page filenames in English** (`program.html`, `practical-info.html`), **content in Czech** (vykání, warm but proper). English mirror under `/en/` is a possible later phase.
- **Em dashes use the entity `&mdash;`, not the Unicode character.** User preference &mdash; entities are explicit in source and don't get confused with hyphens or en dashes at a glance. Applies everywhere: HTML, Markdown, CSS, and config files. In Markdown the entity still renders as a proper em dash through the inline-HTML pass.
- **CSS:** single `site/assets/css/main.css`, mobile-first; palette/type live as `--color-*` and typography custom properties at the top of the file (the one place a palette/type change is made). Current identity: blush-pink accent (`#ed9dbc`) for titles + headings on white, black/charcoal body text; **Playfair Display** (titles + headings) + **Source Sans 3** (sans-serif body) via Google Fonts &mdash; typography matches jakubmares.cz, palette from the print materials (see [../dev/decisions.md](../dev/decisions.md) `D-DESIGN` and the [restructure plan](../dev/archive-plans/2026-06-07_restructure-4pages-fonts-content.md)). Program is an alternating timeline; the home page is a page-width hero photo. Nav: Program · Praktické informace · Focení (`gift.html` is not in the nav and no page links it &mdash; reachable only directly at `/gift`).
- **Emojis:** welcome in `dev/` markdown and in chat (they help navigation; vocabulary in [../dev/workflow-emojis-reference.md](../dev/workflow-emojis-reference.md)). NOT in `docs/` or config files; avoid them in the website source too &mdash; **except** the occasional intentional content emoji the owner asks for (e.g. the 🙂 on a few content lines &mdash; the Program intro and "Vynecháváme", the Praktické informace "Kontakt", and the gift page).
- **No third-party services** (no Formspree, no analytics, no CDN beyond Google Fonts) unless added with an explicit decision logged in [../dev/decisions.md](../dev/decisions.md).
- **Photos:** the home-page hero is a real, optimized couple photo &mdash; `site/assets/img/hero.webp` + `hero.jpg` (1800&times;1350 4:3; WebP served first via `<picture>`, JPG fallback). For any swap: keep &le; 250 KB, EXIF-stripped, Czech `alt`, and match the frame's `width`/`height` in `index.html`. No other photos on the site.

## Local development

Open any file in `site/` directly in a browser, or serve the directory for clean root-relative paths:

```bash
python3 -m http.server 8000 --directory site
```

Then open <http://localhost:8000>. Serving from `site/` reproduces the deployed root exactly.

## Deployment

Live on GitHub Pages, **published via GitHub Actions** ([../.github/workflows/deploy.yml](../.github/workflows/deploy.yml)): every push to `main` uploads `site/` as the Pages artifact and serves it as the site root. Custom domain `tereza-jakub.cz` is bound via the repo Pages settings/API (the `site/CNAME` file alone does not bind it under the Actions source). Full procedure: [../docs/deployment.md](../docs/deployment.md).

## Scratch / private notes

- `tmp/` is gitignored &mdash; use freely for drafts, exports, generator runs, design sources. Don't reference `tmp/` from tracked files. Throwaway specs are named `spec_YYYY-MM-DD_slug.md`.

## When the owner says "update project docs" (or similar)

This phrase means: run the following audit. It is the canonical meaning of the request.

1. **`tmp/` (drafts and scratch specs first).** For each draft / spec file: if all its tasks are done, remove the file (prefer a recoverable delete, e.g. `gio trash`). If partly done, delete the done entries and move the not-yet-done tasks into [../dev/plan.md](../dev/plan.md).
2. **`dev/`.**
   - [../dev/SPEC.md](../dev/SPEC.md) and [../dev/decisions.md](../dev/decisions.md) &mdash; do they still match reality? Is everything still valid as written?
   - [../dev/plan.md](../dev/plan.md) &mdash; delete executed tasks; check the ordering is still optimal; can anything move from mid-term to immediate? Is everything in `tmp/` and in the roadmap reflected here? If not, update it.
   - [../dev/roadmap.md](../dev/roadmap.md) &mdash; do "Where we are now" and the phase statuses still match reality?
   - [../dev/workflow-tracking.md](../dev/workflow-tracking.md) &mdash; is every skill/hook issue and improvement idea from recent work captured (per that file's own section rules)?
   - [../dev/worklog.md](../dev/worklog.md) &mdash; anything worth preserving: promote it to the right durable doc (`decisions.md`, `SPEC.md`, or a `docs/` file), then delete it here; anything already documented elsewhere or now stale: delete it.
3. **`docs/`.** Make sure everything is up to date &mdash; especially [../docs/architecture.md](../docs/architecture.md) and [../docs/deployment.md](../docs/deployment.md), which drift most easily; update them to reflect reality.
4. **Entry docs ([./CLAUDE.md](./CLAUDE.md), [../README.md](../README.md)).** Update both to reflect the current state &mdash; the signposts and conventions in `CLAUDE.md`, and the project summary, file structure, and status in `README.md`. They are what a fresh agent and a newcomer read first, so they must not lag the rest.

## Workflow notes for Claude

- Follow the global workflow (`jd:audit` → `jd:plan` → implement → `jd:verify` → `jd:git`) for non-trivial changes. Skip steps when the spec already settles the question.
- The user is a beginner with web frontend (deep with Python/CFD per global CLAUDE.md). Brief teaching comments in HTML/CSS/JS files are welcome where they explain a foundational concept; otherwise keep code clean per global rules.
- **Before changing the visual design, palette, or page list, update [../dev/SPEC.md](../dev/SPEC.md) and re-confirm with the user.**
