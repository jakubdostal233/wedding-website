# Workflow tracking

> 📋 **What this file is for &mdash; read before adding anything.** A running record of how the owner's *setup* (Claude Code skills, hooks, tooling, and this project's architecture) helps or hinders the work, with concrete, verified observations. Every entry is grounded in a specific in-session moment. Improvement suggestions target the **`jd`** / **`jd-pers`** plugins; each is a *candidate* needing per-item owner approval &mdash; never bundle, never self-apply. Verify any hook/skill claim by reading it before writing it here.

Abbreviations: CI (continuous integration), CDN (content delivery network), PR (pull request).

Related: [./worklog.md](./worklog.md) records state-changing work; this file records how the *process* is going.

## What works

> ⭐ Record only wins attributable to the owner's deliberate setup &mdash; a specific skill, hook, or this project's architecture/convention. Name the element responsible.

- 🔁 2026-06-06 &mdash; **The `jd:refine` + paste-back loop turned a vague, mixed (commands + questions) prompt into an executable spec with explicit sign-off gates.** The raw request bundled an architecture goal, two open questions (`assets/` location, "does a dedicated dir make sense?"), and a deferred design task; refining it first produced a single coherent prompt that resolved each with grounded recommendations. *Thanks to:* the `jd:refine` skill and the refine-in-place workflow.
- 🧵 2026-06-06 &mdash; **Parallel exploration produced a grounded plan instead of guesses.** Two read-only `Explore` agents (one mapping `tyre-model`'s architecture, one inventorying this repo with a path-breakage analysis) surfaced the decisive constraint &mdash; the site is served from the repo root and GitHub Pages branch-deploy only allows `/` or `/docs` &mdash; which is what made the `site/` + Actions decision correct rather than a coin-flip. *Thanks to:* the `Workflow` tool fan-out with `Explore` agents.
- 🙋 2026-06-06 &mdash; **The pre-move sign-off gate caught a live-site risk before any irreversible change.** The plan paused for approval of the directory tree and deploy-cutover handling; a cheap `gh api .../pages` check at that point revealed the site was *already live* (the project docs said deployment was still "planned"). *Thanks to:* the restructure prompt's built-in "present tree + wait" gate plus `AskUserQuestion`.
- 🔒 2026-06-06 &mdash; **`git mv` preserved history across a large move.** All 14 site files and 4 step-plans moved as tracked renames, not delete+add. *Thanks to:* the prompt's "never drop data / use `git mv`" guardrail (the owner's global rule).

## What does not work / friction

> ⚠️ Each entry records a friction caused by a skill / hook / tool / setup gap AND proposes a concrete fix.

- 🗺️ 2026-06-06 &mdash; **Project docs lagged reality: deployment status was wrong.** `.claude/CLAUDE.md` and `roadmap.md` both framed deployment as "Phase 7 (planned)", but the site was already built and live on the custom domain with HTTPS. Only a `gh api repos/{owner}/{repo}/pages` call exposed this; trusting the docs would have mis-sequenced the cutover. *Fix (done this session):* corrected the docs, and the restructure adds a `roadmap.md` "Where we are now" status block that must track reality. *General fix:* any deploy/restructure work should verify live state (`gh api .../pages`) before trusting prose docs.
- 🧩 2026-06-06 &mdash; **`git mv` does not apply to the gitignored scratch dir.** Renaming `temp/` → `tmp/` had to be a plain `mv` because `temp/` is gitignored (no tracked files for `git mv` to move). Minor, handled; noted so the next person doesn't reach for `git mv` and get a confusing error.
- 🧱 2026-06-07 &mdash; **`jd-pers:look` cannot render live HTTPS URLs on the VUTS network, nor JS-only (SPA) sections &mdash; but a one-line workaround fixes both.** Rendering `https://tereza-jakub.cz` and `https://www.jakubmares.cz` returned Chrome's "Your connection is not private": the VUTS Palo&nbsp;Alto firewall MITMs TLS (the served cert is reissued by `O = "VUTS, a.s.", CN = Palo Alto`) and look's bundled Chromium does not trust that root (`curl` / `wget` do, via the system store). A static `wget` mirror dodged the cert but showed only the hero &mdash; jakubmares.cz builds its sections client-side (Next.js). **The render *does* work** if you call the same Chromium binary look resolves and add two flags &mdash; `--ignore-certificate-errors` (defeats the MITM cert) and `--virtual-time-budget=<ms>` (lets the SPA hydrate before capture):

  ```bash
  "$(ls -d $HOME/.cache/ms-playwright/chromium-*/chrome-linux64/chrome | tail -1)" \
    --headless=new --no-sandbox --disable-gpu --hide-scrollbars \
    --window-size=1440,5400 --ignore-certificate-errors --virtual-time-budget=15000 \
    --screenshot=/tmp/out.png "<url>"
  ```

  Verified this session &mdash; it produced a complete render of both sites. The cert AIA `-301` errors printed to stderr are non-fatal. Then downscale/crop the PNG with PIL to read it (a tall capture exceeds the 2000&nbsp;px image-read limit).

## Improvement ideas (jd / jd-pers plugins, new skills, new tools/guides)

> 💡 Each idea cites the in-session moment that motivates it and is a *candidate* requiring owner approval; verify the target skill's current scope before proposing.

- 🚀 2026-06-06 &mdash; **A "GitHub Pages: branch-deploy → Actions migration" guide/checklist (candidate).** This session worked out the safe cutover from memory: verify `pages` state, write the `upload-pages-artifact` / `deploy-pages` workflow with the right `permissions` + `environment`, switch `build_type` to `workflow` via `gh api`, push, verify the live domain, and keep a revert-plus-`build_type=legacy` rollback. A short guide shipped with a web/deploy skill (e.g. `ok:web`, or a `jd` web skill if one exists) would make this repeatable. *Verify first:* whether an existing skill already covers Pages deployment before adding it.
- 🎨 2026-06-06 &mdash; **A reusable "extract a palette/type spec from print PDFs" helper (candidate).** Pre-extracting the design tokens from `tmp/style/*.pdf` was done by eye (provisional hexes). A small tool that samples dominant colors and lists embedded font names from a PDF would make design-from-print handoffs precise rather than eyeballed. Could attach to `jd:doc` or a design skill.
- 🔓 2026-06-07 &mdash; **`jd-pers:look`: add an opt-in `--insecure` flag and a documented `--wait <ms>` (candidate).** The friction above (cert wall + SPA hydration) was only solvable by dropping to the raw Chromium binary. Reading `resources/tools/look`, the `chromium)` branch already assembles the args and already maps an internal `wait` to `--virtual-time-budget` (around line 159) &mdash; it just lacks (a) any `--ignore-certificate-errors` path and (b) a CLI flag to set `wait`. Proposal: an opt-in `--insecure` → `--ignore-certificate-errors` (for TLS-inspecting corporate networks such as VUTS) and a documented `--wait <ms>` → `--virtual-time-budget` (for JS-rendered pages). Both are small, safe, opt-in additions to the existing arg array. *Verified:* read the `chromium)` branch before proposing; no cert-ignore flag exists today. Owner approval required before touching the skill.
