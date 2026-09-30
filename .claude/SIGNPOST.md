# Signpost - wedding-website

<!-- Full catalogue of where things live. Not auto-loaded - read it when you need a path
     not already in .claude/CLAUDE.md. One line each; keep current. -->

Wedding website: static site under `site/`, meta-layer (`dev/`, `docs/`, `tools/`, `tmp/`) around it.

## Steering docs (`dev/`)

- `dev/CONTEXT.md` - what the project is, why it exists, the principles it follows.
- `dev/ROADMAP.md` - phases, the active phase, the backlog.
- `dev/STATUS.md` - current state: last landed, in flight, what's blocked.
- `dev/DECISIONS.md` - decided and open, newest first, one `D-` id per entry.

## Working directories (`dev/`, `docs/`)

- `dev/audits/`, `dev/figures/`, `dev/plans/`, `dev/prompts/`, `dev/reviews/`, `dev/specs/` - empty,
  scaffolded for the canonical structure; populate as `pers:*` skills produce dated artefacts.
- `docs/figures/`, `docs/research/` - empty, same reason.
- `docs/evidence/D-DESIGN/` - checksum manifest for the two printed-material PDFs `DECISIONS.md`
  D-DESIGN cites (the PDFs themselves stay in `tmp/style/`, gitignored).

## Documentation (`docs/`)

- `docs/architecture.md` - how the site is built: layout, pages, CSS, integrations, generators, deploy.
- `docs/deployment.md` - how to deploy, update, roll back; DNS, domain, costs.
- `docs/qa-checklist.md` - functional checks to run on real devices before sharing the URL.

## The deliverable (`site/`)

- `site/index.html`, `program.html`, `practical-info.html`, `photoshooting.html` - the four navigated
  pages.
- `site/gift.html` - the unlisted Dar (bank QR) page, reachable only at `/gift`.
- `site/assets/css/main.css` - the single stylesheet (palette + typography tokens at the top).
- `site/assets/img/` - `og-card.png`, `qr-platba.svg`, the four `seating-*.svg` reception plans,
  `hero.{webp,jpg}`.
- `site/assets/wedding_tj.ics` - the calendar download.
- `site/favicon.svg`, `CNAME`, `robots.txt` - site-root files GitHub Pages serves as-is.
- `.github/workflows/deploy.yml` - the GitHub Actions publish workflow. **Currently missing from the
  working tree** (unstaged deletion) - see `dev/STATUS.md` § What's blocked before assuming it's gone
  for good.

## Tooling and scratch

- `tools/generate-og-card.py`, `generate-seating-schemes.py`, `generate-spayd-qr.py`, `og-card.html` -
  offline generators; write into `site/assets/img/` (and the seating generator also re-injects inline
  SVG into `practical-info.html`). Not served.
- `tmp/style/*.pdf` - the printed wedding materials D-DESIGN was sampled from; gitignored but kept
  intentionally (see `docs/evidence/D-DESIGN/manifest.md`), not scratch to be cleared.

## Entry docs

- `README.md` - human-facing overview.
- `.claude/CLAUDE.md` - agent entry doc.
- `.claude/MEMORY.md` - curated memory digest.
- `.claude/settings.json` - local permission allowlist (`python3 -m http.server`).

## Related / sibling repos

Full portfolio register -> core/jakub-hq/.claude/SIGNPOST.md (§ Portfolio). Paths below are
ROOT-relative (ROOT = /mnt/d/projects).

Claude infrastructure:

- core/jakub-hq - portfolio HQ: map, side-task routing, status dashboard (full register in its
  .claude/SIGNPOST.md).
- core/jd-plugins - jd / pers plugins (the skills + hooks this repo's workflow uses).
- core/claude-code-config - global CLAUDE.md + settings.json source (symlink-deployed).
