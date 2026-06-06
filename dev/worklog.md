# Worklog

Agent scratch log: state-changing work and decisions, newest first. Once a fact is settled it is PROMOTED to the proper doc (`decisions.md`, `SPEC.md`, `roadmap.md`, `docs/`) and DELETED from here. This file is not a permanent record.

Abbreviations: CI (continuous integration), CDN (content delivery network), OG (Open Graph), QR (quick-response code), SPAYD (Short Payment Descriptor &mdash; Czech QR payment standard).

## 2026-06-06 — Repository restructured to the tyre-model architecture

🧭 Reorganised the repo to separate the deliverable from the meta-layer, adopting the `~/git/tyre-model/` reference architecture. Driven by the refined prompt now archived at [./archive-prompts/2026-06-06_restructure-to-tyre-model.md](./archive-prompts/2026-06-06_restructure-to-tyre-model.md). New decisions: [D-STRUCT](./decisions.md#d-struct--repository-restructured-to-the-tyre-model-architecture) (the restructure) and [D-DEPLOY](./decisions.md#d-deploy--deploy-via-github-actions-serving-the-site-directory) (Actions deploy).

- 📦 **`site/` created** &mdash; all served files (`git mv`'d, history preserved): the 7 HTML pages, `favicon.svg`, `CNAME`, `robots.txt`, and `assets/` (css / img / js / `wedding_tj.ics`). They moved together so every relative path still resolves; the OG absolute URLs (`https://tereza-jakub.cz/...`) are unchanged because the folder is served as the site root.
- ⚙️ **Generator scripts** in `tools/` repointed to `site/assets/img/` (`generate-og-card.py`, `generate-spayd-qr.py`); re-ran both &mdash; they reproduce the QR SVG and OG PNG at the new path (minor byte change from re-encoding; identical design and SPAYD payload). Also fixed a stale `temp/...` usage line in the QR script.
- 🗂️ **`dev/` adopted the tyre-model steering scheme** &mdash; new `decisions.md`, `plan.md`, `worklog.md`, `workflow-tracking.md`, `workflow-emojis-reference.md`; new `archive-plans/` (the four completed `plan-step-NN` files moved in with their first-commit date prefix), `archive-prompts/` (seeded with the restructure prompt), `archive-audits/` (empty, `.gitkeep`). `SPEC.md` kept as source of truth; `roadmap.md` kept and now also carries the "where we are now" status (no separate `notebook.md`).
- 🧹 **`temp/` → `tmp/`** (gitignored scratch; plain `mv`); `.gitignore` updated.
- 📝 **`docs/architecture.md`** written (how the site works). `docs/deployment.md` + `SPEC.md` updated for the Actions deploy and the `site/` layout. `.claude/CLAUDE.md` + `README.md` rewritten to the new layout; emoji-usage rule added to `CLAUDE.md` (welcome in `dev/` + chat, never in `docs/`/code/config).
- 🚀 **Deploy cutover (live site):** the site was already live via legacy branch-deploy (`main` / root). Switched the Pages source to GitHub Actions and pushed; the workflow uploads `site/` and serves it at the root with the custom domain + HTTPS intact. Rollback path: revert + switch the Pages source back to `legacy` (branch / root).

🎯 **Next:** Phase 4.5 &mdash; the visual design refresh from `tmp/style/*.pdf` ([O-DESIGN](./decisions.md#o-design--visual-design-refresh-from-the-print-materials)). The dominant print identity is **blush/dusty pink on white** (not the current sage green); provisional palette/typography captured in `decisions.md`. Apply nothing until `SPEC.md` is updated and the owner signs off.
