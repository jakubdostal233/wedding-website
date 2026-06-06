---
source: user prompt
date: 2026-06-06
intent: Restructure the wedding-website project to adopt the tyre-model architecture (dedicated site directory, dev/ steering-file scheme, docs/ reference style, emoji vocabulary, tmp/ rename), write website architecture documentation, and plan&mdash;but not yet execute&mdash;the next-phase design refresh from the style PDFs.
---

# Restructure wedding-website to adopt the tyre-model architecture

## Role and single task

You are restructuring the `wedding-website` project (`/home/jakub/git/wedding-website/`) so its layout, project-context files, and documentation follow the same architecture as the reference project `tyre-model` (`/home/jakub/git/tyre-model/`). The goal is a repo that is easy to navigate and easy to develop: a clean separation between **the deliverable (the website)** and **the meta-layer around it (planning, reference docs, tooling, scratch)**, mirroring how tyre-model separates `model/` from `dev/`, `docs/`, `.claude/`, and `tmp/`.

This is **one coherent restructuring task** with several enumerated deliverables (§3). It is **not** a freehand redesign &mdash; adopt tyre-model's *patterns and purpose*, adapted to a small, single-author, ~12-month static site. The deployment approach, the site directory name, and the `dev/` steering set are already decided (§4, §7); the remaining open call is how existing `dev/` content maps onto the scheme.

Treat the website's visual design (palette, fonts, page list) as **out of scope for this pass** &mdash; that is the *next* phase (§9), planned but not executed now.

## Workflow and guardrails (follow these throughout)

- Follow the project workflow: **`jd:audit` (current state) &rarr; `jd:plan` &rarr; confirm the target structure with me &rarr; implement &rarr; `jd:verify` &rarr; `jd:git`.** Skip a step only if it is genuinely settled.
- **Get my sign-off before moving any files:** present the proposed final directory tree and the `dev/` file mapping (the deployment approach and the `site/` name are already decided &mdash; §4, §7), then wait. The project rule "re-confirm before changing the page list / structure" applies.
- **Never drop or orphan data.** Move tracked files with `git mv` so history is preserved. After every move, confirm nothing was lost and every reference still resolves (§6).
- **Automate the repetitive parts.** Updating dozens of cross-references (OG URLs, internal links, doc paths) by hand invites drift &mdash; write a small script or use a single well-tested search-replace pass, then verify.
- **Report honestly.** Distinguish "moved and verified the site still renders" from "moved, not yet checked." Use `jd:verify` to actually open/serve the site and confirm, don't assume.
- **Commit via `jd:git`** in logical groups once verification passes.
- **Conventions for files you create or edit:** em dashes as the entity `&mdash;` (everywhere &mdash; HTML, Markdown, CSS, config); one line per paragraph in Markdown (no hard-wrapping); English filenames, Czech site content.

## 3. Deliverables

1. **Dedicated website directory** holding everything the site needs to run (HTML, CSS, images, JS, `.ics`, favicon, and the deploy-control files `CNAME`/`robots.txt`), per §4. Name (decided): **`site/`** (the repo is already `wedding-website`, so `website/` would read as `wedding-website/website/`). **Plus** a minimal `.github/workflows/deploy.yml` that publishes `site/` via GitHub Actions (§4).
2. **tmp/ rename:** rename `temp/` &rarr; `tmp/`, adopting tyre-model's scratch convention (gitignored; throwaway specs named `spec_<YYYY-MM-DD>_<slug>.md`).
3. **`tools/` confirmed in place** as a meta-layer directory, with the two generator scripts' hardcoded output paths updated to the new asset location (§6).
4. **`dev/` adopted to the tyre-model steering scheme**, adapted to this project's scale (§7), including an emoji-vocabulary file and `archive-*/` convention.
5. **`docs/architecture.md`**: new long-form reference documenting how the website itself works, in tyre-model `docs/` style (§8).
6. **Emoji adoption** (§ the emoji vocabulary file + usage rule) consistent with tyre-model.
7. **Updated project-context + entry files** so they describe the new structure accurately: `.claude/CLAUDE.md`, `README.md`, `dev/SPEC.md`, `docs/deployment.md`, `.gitignore`, and `robots.txt`/`CNAME` placement.
8. **A plan/roadmap that includes the next-phase design refresh** from the style PDFs (§9) &mdash; written, not executed.

## 4. Deployment approach (DECIDED: Option A &mdash; `site/` + GitHub Actions)

The site moves into a dedicated **`site/`** directory, deployed via a **GitHub Actions static-upload workflow** (not branch-deploy). This is settled; the notes below are the rationale and the constraints to honor.

**Why this approach is necessary:** today the site is served from the **repo root**, and GitHub Pages "Deploy from a branch" only serves `/` (root) or `/docs` &mdash; never an arbitrarily named subfolder like `site/`. The Actions path uploads the `site/` folder as the artifact, which is served *as the site root*. Consequences:

- **OG absolute URLs stay unchanged** (`https://tereza-jakub.cz/`, `.../about-us.html`, `.../assets/img/og-card.png`) &mdash; the folder *is* the served root, not a `/site/` sub-path.
- **`CNAME`, `robots.txt`, and `favicon.svg` live inside `site/`** so they ship in the served artifact at the root.
- The site itself **stays build-less**; the workflow only uploads static files (no compilation step).

**Do:**

- Add a minimal `.github/workflows/deploy.yml` using the official Pages actions (`actions/upload-pages-artifact` with `path: site`, then `actions/deploy-pages`), triggered on push to `main`. Keep it as small as possible.
- **Verify the actual current deployment status first** (per project docs, launch deployment is "Phase 7 (planned)"; confirm whether the site is already live). If not yet live, this is the ideal, low-risk moment to restructure.
- **Verify the current GitHub Pages + custom-domain + CNAME-in-artifact behavior against official docs** (use `jd:howto`) before committing the workflow, since this is outward-facing.
- The Pages **source** must be switched from "branch" to "GitHub Actions" in repo settings &mdash; if that can't be done from the CLI, flag it to me as a manual step.
- Update `docs/deployment.md` and `dev/SPEC.md` to describe the Actions-based deploy and the `site/` layout.

(Rejected alternatives, for the record: **B** = keep serving from root, which would not give a dedicated directory; **C** = serve from `/docs`, which collides with the `docs/` reference guides.)

## 5. Direct answers to the questions embedded in the original request

Bake these resolutions into the plan (still subject to the §4 sign-off):

- **"Website content in a dedicated directory &mdash; does that make sense?"** Yes &mdash; it cleanly separates the deliverable from the meta-layer, exactly as tyre-model isolates `model/`. The *only* real obstacle is the GitHub Pages serving constraint, which the §4 GitHub Actions deploy resolves.
- **"What is `assets/` for, and where should it live?"** `assets/` holds everything the public HTML loads at runtime: `css/main.css` (the single stylesheet), `img/` (`og-card.png`, `qr-platba.svg`), `js/` (currently empty, reserved), and `wedding_tj.ics` (calendar download). These are *part of the website*, not meta-layer &mdash; so `assets/` **moves into the dedicated site directory** (`site/assets/`), alongside the HTML. `favicon.svg` (currently at root, referenced as `favicon.svg`) must move *with* the HTML into `site/`.
- **"Tools stay in `tools/`?"** Yes. `tools/` is meta-layer (generator scripts that *produce* tracked assets), analogous to tyre-model's `tools/`. Keep it at the repo root, outside the site directory. Only their hardcoded output paths change (§6).
- **"Rename `temp/` &rarr; `tmp/`?"** Yes &mdash; do it, and update every reference to it (§6).

## 6. Mechanical changes and path-breakage checklist (verify each)

When the site files move into `site/`:

- **Generator output paths** in `tools/generate-spayd-qr.py` and `tools/generate-og-card.py`: currently `Path(__file__).resolve().parent.parent / "assets" / "img" / ...`. Update to target `site/assets/img/...`. Re-run both scripts and confirm the regenerated `qr-platba.svg` and `og-card.png` are byte-reasonable and land in the new path.
- **HTML relative references** (`href="assets/css/main.css"`, `src="assets/img/qr-platba.svg"`, `href="assets/wedding_tj.ics"`, cross-page links like `href="index.html"`, `href="favicon.svg"`): these keep working *as long as the HTML, `assets/`, and `favicon.svg` all move together* into `site/`. Confirm by serving locally.
- **OG absolute URLs** (`<meta property="og:image" content="https://tereza-jakub.cz/assets/img/og-card.png">`, `og:url` per page): **unchanged** (the `site/` folder is served as root). Confirm none need editing across all 7 pages.
- **`CNAME`** (`tereza-jakub.cz`): place it in `site/` so it ships in the served artifact at the root. Confirm GitHub picks it up.
- **`robots.txt`** (`Disallow: /`): move into `site/` so it is served from the site root.
- **`.gitignore`:** change the `temp/` entry to `tmp/`; add any new ignores the chosen deployment introduces (e.g. nothing for static Actions).
- **`temp/` &rarr; `tmp/` references:** update `.claude/CLAUDE.md` ("Scratch / private notes"), `README.md` (repo-layout table), and any other tracked mention. Move all current `temp/` contents (`style/`, `mailclient/`, screenshots, the prompt drafts) into `tmp/`.
- **Docs referencing the old layout:** `docs/deployment.md` (serving folder, "test the live site" URLs), `README.md` (layout table + planned-docs list), `.claude/CLAUDE.md` (the "Site files live at the repo root" convention line &mdash; rewrite it to describe `site/`), `dev/SPEC.md` (deployment section).
- **Local-dev command:** `python3 -m http.server 8000` must now be run from inside `site/` (or document the new path). Update `.claude/CLAUDE.md` and `README.md` accordingly, and confirm the allow-rule in `.claude/settings.json` still fits.

## 7. dev/ adoption (adapt, do not copy wholesale)

tyre-model's `dev/` is a steering system: `purpose.md`, `context.md`, `philosophy.md`, `decisions.md` (DECIDED/PROPOSED/OPEN, newest-first), `plan.md` (live to-do; finished tasks deleted, not ticked), `notebook.md` (human-facing phase status; canonical phase names), `worklog.md` (transient agent log), `workflow-tracking.md`, `workflow-emojis-reference.md`, and `archive-audits/` `archive-plans/` `archive-prompts/` (immutable, date-prefixed: `YYYY-MM-DD_slug.md`, or a `YYYY-MM-DD_slug/` directory with `00_consolidated-*.md` for fan-out work).

This project currently has `dev/SPEC.md`, `dev/roadmap.md`, and `dev/plan-step-01..04-*.md`. Propose a mapping onto the tyre-model scheme that fits a small site &mdash; e.g.:

- Keep **`SPEC.md`** as the source of truth (it already absorbs purpose/context/philosophy/decisions for a project this size). Decide whether to split out a lean **`decisions.md`** (the spec already records "decisions made") &mdash; recommended, since the restructure and the upcoming design refresh will generate decisions worth logging.
- Map **`roadmap.md`** &rarr; the `notebook.md` role (phase status, the canonical phase names) and/or keep it as the phased plan.
- Map the **`plan-step-NN-*.md`** files &rarr; a live **`plan.md`** for current work, with completed step-plans moved to **`dev/archive-plans/`** (`YYYY-MM-DD_plan-step-NN-*.md`).
- Add **`dev/archive-prompts/`** and seed it with this very prompt once execution starts (`2026-06-06_restructure-to-tyre-model.md`).
- Add **`workflow-emojis-reference.md`** (§ emoji adoption).
- Include **`worklog.md`** (transient, chronological agent log of state-changing work; settled facts get promoted to the right durable doc, then deleted here) and **`workflow-tracking.md`** (skill/hook wins, frictions + fixes, plugin-improvement ideas) &mdash; both decided in, mirroring tyre-model. Seed `workflow-tracking.md` with observations from this restructuring session.

Present the proposed `dev/` file set and mapping for sign-off before creating/moving anything. Do not silently discard content from existing `dev/` files &mdash; migrate it.

## 8. Documentation deliverable: docs/architecture.md

Write a long-form **`docs/architecture.md`** describing how the website itself works, in tyre-model `docs/` style: start with a **Table of Contents**, then an **Abbreviations** section (alphabetical &mdash; CNAME, CSS, DNS, ICS, OG, QR, SPAYD, SVG, …; a Symbols section is optional/likely unneeded for a website), then long-form reference prose. **No emojis in `docs/`** (per the convention). Cover at least:

- The multi-page static architecture (the 7 pages and their purpose) and the **no-build / vanilla HTML-CSS-JS** philosophy.
- The shared header/footer kept in sync manually, and how pages cross-link.
- The `assets/` layout and the **single-stylesheet** CSS architecture (mobile-first; palette ivory · charcoal · sage; type Cormorant Garamond + Inter from Google Fonts).
- How Open Graph cards work and where `og-card.png` comes from.
- The generator tools (`tools/generate-*.py`) and what tracked assets they produce.
- How deployment works (cross-link `docs/deployment.md`; don't duplicate it).
- The directory layout after the restructure (deliverable vs meta-layer), so a newcomer can navigate.

The existing `docs/deployment.md` and `docs/qa-checklist.md` already fit the `docs/` = reference-guides model; align their headers to the ToC + Abbreviations convention if cheap, otherwise leave them.

## 9. Emoji adoption

Adopt tyre-model's convention: copy/adapt `tyre-model/dev/workflow-emojis-reference.md` into this project's **`dev/workflow-emojis-reference.md`** (the single source of truth for emoji meanings), and add the usage rule to `.claude/CLAUDE.md`: **emojis are welcome in `dev/` markdown and in chat, but NOT in `docs/`, HTML, CSS, JS, or config files.** This parallels the project's existing clean-source discipline (e.g. the `&mdash;` entity rule).

## 10. Next phase &mdash; design refresh from the style PDFs (PLAN ONLY, do not execute)

`tmp/style/` (after the rename) contains the canonical design template:
- `jmenovky-design.pdf` &mdash; the name badges (jmenovky)
- `svatebni-oznameni.pdf` &mdash; the final wedding announcement (svatební oznámení)

These define the real wedding identity (color palette, typography, motifs). The plan/roadmap you produce must include a **distinct, well-scoped next phase** that updates the website's design (palette and fonts in `assets/css/main.css`, and any related tokens) to match these PDFs. In this restructuring pass:

- **Do not change any visual design.** No edits to the palette, fonts, or page layout in this pass.
- **Recommended (optional):** read the two PDFs now and *pre-extract* the palette (hex values) and typography into a `dev/` design note (or an OPEN item in `decisions.md`), naming the two PDFs as the design source of truth, so the next phase is ready to execute. Apply nothing.
- Per the project rule, the actual design change will require updating `dev/SPEC.md` (palette/type are specified there) and my re-confirmation before implementation &mdash; note this gate in the plan.

## 11. Acceptance criteria

- Site files (HTML, `assets/`, `favicon.svg`, `CNAME`, `robots.txt`) live in `site/`; `git mv` preserved history; the site renders correctly when served locally from `site/` (verified, not assumed).
- `.github/workflows/deploy.yml` exists, publishes `site/` via GitHub Actions, and is documented in `docs/deployment.md`; the Pages-source switch is either done or flagged to me as a manual step.
- `temp/` is gone; `tmp/` holds its former contents; no tracked reference to `temp/` remains.
- `tools/` scripts run and emit assets to the new path; regenerated assets verified.
- `dev/` reflects the agreed tyre-model-style scheme &mdash; including `worklog.md`, `workflow-tracking.md`, and `archive-*/` &mdash; with no prior content lost.
- `dev/workflow-emojis-reference.md` exists; the emoji usage rule is in `.claude/CLAUDE.md`.
- `docs/architecture.md` exists and accurately describes the post-restructure site, with no emojis and a ToC + Abbreviations header.
- `.claude/CLAUDE.md`, `README.md`, `dev/SPEC.md`, `docs/deployment.md`, `.gitignore` all describe the new structure correctly; their "where things live" pointers match reality.
- The plan/roadmap includes the next-phase design refresh referencing the two PDFs.
- All cross-references resolve (links, OG URLs, asset paths, generator paths); the §6 checklist is fully green.
- Changes committed via `jd:git` in logical groups.

## 12. Out of scope for this pass

- Any visual/design change (palette, fonts, layout) &mdash; that is §10, next phase.
- Adding pages, content, or third-party services.
- An English `/en/` mirror.

---

## Appendix A &mdash; tyre-model architecture (grounding; verify against the live repo, it may have evolved)

Analyze `/home/jakub/git/tyre-model/` yourself; this is a head-start summary.

- **Bipartite entry files.** `.claude/CLAUDE.md` = agent-facing, lean; its **"Where things live"** section lists every major file/dir with its one-line role (Entry points / Steering `dev/` / Documentation `docs/` / Code & assets), plus collraboration rules, a "when the owner says 'update project docs'" procedure, and all conventions in one place. `README.md` = human-facing narrative: Why, Status, Project layout (ASCII tree), Setup, Tech stack, Pointers, Acronyms.
- **`dev/` = steering** (lean/transient + durable): `purpose.md`, `context.md`, `philosophy.md`, `decisions.md` (D-LABEL items; DECIDED/PROPOSED/OPEN; newest-first), `plan.md` (live to-do, finished tasks deleted), `notebook.md` (human phase status; canonical phase names), `worklog.md` (transient), `workflow-tracking.md`, `workflow-emojis-reference.md`.
- **`dev/archive-*/`** = immutable, date-prefixed snapshots: `archive-audits/`, `archive-plans/`, `archive-prompts/`. Single-agent &rarr; one file `YYYY-MM-DD_slug.md`; multi-agent fan-out &rarr; a `YYYY-MM-DD_slug/` directory with `NN_aspect.md` per agent + `00_consolidated-*.md`.
- **`docs/` = reference documentation**: every file opens with **ToC + Symbols + Abbreviations (all alphabetical)**, then long-form prose. `docs/reports/` holds dated, immutable state snapshots `YYYY-MM-DD_topic.md`. **No emojis in `docs/`.**
- **Deliverable vs meta-layer.** The thing being built (`model/`) is isolated from the meta-layer (`dev/`, `docs/`, `.claude/`, `README.md`) and from scratch/read-only dirs (`tmp/`, `results/`, `data/`). `tmp/` is gitignored scratch; throwaway specs named `spec_YYYY-MM-DD_slug.md`.
- **Emoji vocabulary.** `dev/workflow-emojis-reference.md` is the single source of truth (categories: Status/Workflow, Progress & State, Priority, Communication, Technical & Data, AI-Agent, Useful Combinations). Welcome in `dev/` + chat; never in `docs/`, code, or configs.
- **Naming.** Sequential, legible phase names (`phase-1`, `phase-1.1`, `phase-2`), never opaque codes.

## Appendix B &mdash; wedding-website current state (pre-restructure)

- **Root site files:** `index.html`, `about-us.html`, `location.html`, `program.html`, `transit.html`, `contact.html`, `gift.html`; `favicon.svg`; `CNAME` (`tereza-jakub.cz`); `robots.txt` (`Disallow: /`).
- **`assets/`:** `css/main.css` (single stylesheet, ~392 lines, mobile-first, palette ivory/charcoal/sage, Cormorant Garamond + Inter); `img/og-card.png` (1200×630 OG card), `img/qr-platba.svg` (SPAYD payment QR); `js/` (empty); `wedding_tj.ics` (calendar). Referenced from HTML via relative paths; OG tags use absolute `https://tereza-jakub.cz/...` URLs.
- **`tools/`:** `generate-spayd-qr.py` (segno &rarr; `assets/img/qr-platba.svg`), `generate-og-card.py` (Pillow &rarr; `assets/img/og-card.png`); both hardcode `parent.parent/"assets"/"img"/...`.
- **`dev/`:** `SPEC.md` (source of truth), `roadmap.md`, `plan-step-01-foundation.md` … `plan-step-04-integrations.md`.
- **`docs/`:** `deployment.md` (GitHub Pages, DNS, Wedos domain, costs), `qa-checklist.md`, `.gitkeep`.
- **`.claude/`:** `CLAUDE.md` (48 lines; states "Site files live at the repo root … GitHub Pages serves the root"), `settings.json` (allows `python3 -m http.server *`).
- **`temp/` (gitignored):** `style/jmenovky-design.pdf`, `style/svatebni-oznameni.pdf`, `mailclient/*.PNG`, `github-pages.PNG`, prompt drafts.
- **Deployment:** GitHub Pages from `main` root; per docs, launch deployment is "Phase 7 (planned)" &mdash; confirm whether it is already live before restructuring.
