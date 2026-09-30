# Wedding Website

Informational website for our wedding on **10 July 2026 in Prague**. Vanilla HTML, CSS, and JavaScript &mdash; no build step &mdash; hosted free on GitHub Pages at **[tereza-jakub.cz](https://tereza-jakub.cz)** (public but unlisted).

## Repository layout

The repo separates **the website** (everything served) from the **project meta-layer** around it.

```
wedding-website/
├── site/        # THE WEBSITE - everything served (the site root)
│   ├── *.html   #   index, program, practical-info, photoshooting (+ unlisted gift)
│   ├── assets/  #   css/main.css, img/ (og-card, payment QR), js/, wedding_tj.ics
│   ├── favicon.svg, CNAME, robots.txt
├── dev/         # steering: CONTEXT, ROADMAP, STATUS, DECISIONS
├── docs/        # reference docs: architecture, deployment, QA checklist, evidence
├── tools/       # offline generators (produce the tracked images in site/assets/img/)
├── tmp/         # scratch - gitignored
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

**Live** at <https://tereza-jakub.cz>. Four navigated pages (Úvod, Program, Praktické informace,
Focení) plus an unlisted gift page, Czech content, every integration wired up (maps, calendar `.ics`,
bank QR, `mailto:`, Open Graph cards), and the URL already sent to guests. The one item remaining
before the wedding (2026-07-10) is owner-side real-device testing; see
[dev/STATUS.md](dev/STATUS.md) for the current state and [dev/DECISIONS.md](dev/DECISIONS.md) for how
the design and structure got here.

## Pointers

- [dev/CONTEXT.md](dev/CONTEXT.md) &mdash; what this project is, why it exists, the principles it
  follows.
- [dev/ROADMAP.md](dev/ROADMAP.md) &mdash; where the project is now and the phased plan.
- [dev/STATUS.md](dev/STATUS.md) &mdash; current state: what landed last, what is in flight.
- [dev/DECISIONS.md](dev/DECISIONS.md) &mdash; decision log (decided / open).
- [docs/architecture.md](docs/architecture.md) &mdash; how the website is built and works.
- [docs/deployment.md](docs/deployment.md) &mdash; deploy, update, roll back; DNS and domain.
- [docs/qa-checklist.md](docs/qa-checklist.md) &mdash; pre-launch functional checks.
