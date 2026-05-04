# Wedding Website

Informational website for our wedding on **10 July 2026 in Prague**. Built from scratch with vanilla HTML, CSS, and JavaScript; hosted free on GitHub Pages.

## Repository layout

| Path | What's there |
|------|--------------|
| `index.html`, `*.html`, `assets/` | The public site (added during Phase 1+) |
| `dev/` | Specification, roadmap, and active step plans |
| `docs/` | Long-form documentation (see below) |
| `.claude/` | Project context for [Claude Code](https://claude.com/claude-code) |
| `temp/` | Scratch &mdash; gitignored |

### Planned documentation

Files added to `docs/` as the project grows:

- `deployment.md` &mdash; GitHub Pages setup, DNS configuration, domain renewal notes
- `content-workflow.md` &mdash; how to add a page, how to swap a photo, how to update copy
- `assets-pipeline.md` &mdash; image optimisation, font handling, SPAYD QR regeneration

## Local preview

Open any `.html` file directly in a browser, or run a local web server for clean root-relative paths:

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

## Stack

Vanilla HTML / CSS / JavaScript. No build step, no framework, no backend.

## Status

In development. See `dev/roadmap.md` for the phased plan and `dev/SPEC.md` for the full specification.
