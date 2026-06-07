# Wedding Website

Informational website for our wedding on **10 July 2026 in Prague**. Vanilla HTML, CSS, and JavaScript &mdash; no build step &mdash; hosted free on GitHub Pages at **[tereza-jakub.cz](https://tereza-jakub.cz)** (public but unlisted).

## Repository layout

The repo separates **the website** (everything served) from the **project meta-layer** around it.

```
wedding-website/
├── site/        # THE WEBSITE — everything served (the site root)
│   ├── *.html   #   the 4 pages (index, program, practical-info, about-us)
│   ├── assets/  #   css/main.css, img/ (og-card, payment QR), js/, wedding_tj.ics
│   ├── favicon.svg, CNAME, robots.txt
├── dev/         # steering: SPEC, roadmap, plan, decisions, worklog, archives
├── docs/        # reference docs: architecture, deployment, QA checklist
├── tools/       # offline generators (produce the tracked images in site/assets/img/)
├── tmp/         # scratch — gitignored
└── .github/workflows/deploy.yml   # GitHub Actions: publishes site/ to Pages
```

Only `site/` is published. See [docs/architecture.md](docs/architecture.md) for how it all fits together.

## Local preview

Open any file in `site/` directly in a browser, or serve the directory for clean root-relative paths:

```bash
python3 -m http.server 8000 --directory site
```

Then open <http://localhost:8000>.

## Stack

Vanilla HTML / CSS / JavaScript. No build step, no framework, no backend. Deployed via GitHub Actions to GitHub Pages, behind a custom domain with HTTPS.

## Status

**Live.** The site is four pages (Úvod, Program, Praktické informace, O nás) with Czech content and the integrations wired up (maps, calendar `.ics`, bank QR, `mailto:`, Open Graph cards). On 2026-06-06 the repository was restructured into `site/` with a GitHub Actions deploy; on 2026-06-07 the visual identity was set (blush-pink palette, Playfair Display + Source Sans 3) and the site was reduced from seven pages to four with a jakubmares.cz-style Program timeline. Up next: the hero / about-us photos and a final polish pass before the day.

## Pointers

- [dev/roadmap.md](dev/roadmap.md) &mdash; where the project is now and the phased plan.
- [dev/plan.md](dev/plan.md) &mdash; the current task list.
- [dev/SPEC.md](dev/SPEC.md) &mdash; the full specification (source of truth).
- [dev/decisions.md](dev/decisions.md) &mdash; decision log (decided / proposed / open).
- [docs/architecture.md](docs/architecture.md) &mdash; how the website is built and works.
- [docs/deployment.md](docs/deployment.md) &mdash; deploy, update, roll back; DNS and domain.
- [docs/qa-checklist.md](docs/qa-checklist.md) &mdash; pre-launch functional checks.
