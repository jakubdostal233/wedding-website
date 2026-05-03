# Wedding Website — Project Context

Static informational website for Jakub & [partner]'s wedding on **10 July 2026 in Prague**. Public but unlisted, hosted free on GitHub Pages, single-author, ~12-month lifecycle.

## Where to find what

- **Spec (source of truth):** `dev/SPEC.md` — what we're building, decisions made, open items
- **Roadmap:** `dev/roadmap.md` — phased path from now to launch
- **Active plan:** `dev/plan-step-NN-*.md` — tasks for the current phase
- **Documentation:** `docs/` — long-form guides (deployment, content workflow, etc.)
- **Public README:** `README.md` — repo overview for any reader

## Stack

Vanilla HTML / CSS / JavaScript, no build step, no Node toolchain. Multi-page architecture with shared header/footer kept in sync manually (with AI assist).

## Project conventions

- **Page filenames in English** (`location.html`, `about-us.html`), **content in Czech** (vykání, warm but proper). English mirror under `/en/` is a possible Phase 2.
- **CSS:** single `assets/css/main.css`, mobile-first; palette ivory · charcoal · sage; type Cormorant Garamond + Inter.
- **No third-party services** (no Formspree, no analytics, no CDN beyond Google Fonts) unless added with explicit decision logged in `dev/SPEC.md`.
- **Photos:** placeholders (e.g. solid sage block or `assets/img/placeholder-*.jpg`) until real photos are available.
- **Site files live at the repo root** (`index.html`, `assets/`, …) alongside project files (`dev/`, `docs/`). GitHub Pages serves the root, so anything in the repo is technically reachable — `robots.txt` disallows crawlers, but don't put secrets in tracked files.

## Local development

Open any `.html` directly in a browser, or run a local server for clean root-relative paths:

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000 .

## Deployment (planned, Phase 7)

GitHub Pages, deploy from `main` branch root. Custom domain via `CNAME` file at launch.

## Scratch / private notes

- `temp/` is gitignored — use freely for drafts, exports, generator scripts (e.g. SPAYD QR generation). Don't reference `temp/` from tracked files.

## Workflow notes for Claude

- Follow the user's global workflow (`jd:audit` → `jd:plan` → implement → `jd:verify` → `jd:git`) for non-trivial changes. Skip steps when the spec already settles the question.
- The user is a beginner with web frontend (deep with Python/CFD per global CLAUDE.md). Brief teaching comments in HTML/CSS/JS files are welcome where they explain a foundational concept; otherwise keep code clean per global rules.
- Before changing the visual design, palette, or page list, update `dev/SPEC.md` and re-confirm with the user.
