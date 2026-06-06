# Deployment

How to deploy and update the wedding website at <https://tereza-jakub.cz>. Self-contained &mdash; no need to dig through chat history or PRs.

## Table of contents

- [Stack](#stack)
- [Initial deployment (one-time)](#initial-deployment-one-time)
- [Updating the site](#updating-the-site)
- [Rollback](#rollback)
- [Domain renewal](#domain-renewal)
- [Costs](#costs)
- [Common issues](#common-issues)

## Stack

Static site &mdash; vanilla HTML/CSS/JS, no build step &mdash; hosted on GitHub Pages, fronted by a custom domain.

| Where | What |
|-------|------|
| Repository | <https://github.com/jakubdostal233/wedding-website> (branch `main`) |
| Hosting | GitHub Pages (free), publishes the `site/` directory via GitHub Actions (`.github/workflows/deploy.yml`) |
| Domain | `tereza-jakub.cz` at Wedos (registered May 2026, 1-year term) |
| Email | `info@tereza-jakub.cz` at Seznam Email Profi (free tier) &mdash; forwards to personal Gmail |

## Initial deployment (one-time)

Steps 1&ndash;7. Skip steps already done; the order matters because step 5 (DNS at Wedos) needs steps 2 and 3 to be live first.

### 1. Push the repo to GitHub

```bash
git push -u origin main
```

Verify with `git status -sb` &mdash; should show `## main...origin/main` with no `[ahead]` marker.

### 2. Enable GitHub Pages (GitHub Actions source)

The repo deploys via the workflow at `.github/workflows/deploy.yml`, which uploads the `site/` directory as the Pages artifact and serves it as the site root.

In the repo on GitHub: **Settings &rarr; Pages &rarr; Build and deployment**.

| Field | Value |
|-------|-------|
| Source | **GitHub Actions** |

(Equivalently from the CLI: `gh api repos/jakubdostal233/wedding-website/pages -X PUT -F build_type=workflow`.)

A push to `main` then triggers the workflow &mdash; visible in the **Actions** tab. After a minute or two the deploy finishes and the site is live. If it doesn't deploy, check the Actions tab for the workflow run's error.

> Migration note: the project originally used the legacy "Deploy from a branch" source (`main` / root). It moved to the GitHub Actions source on 2026-06-06 when the site files were relocated into `site/` (GitHub Pages branch-deploy can only serve `/` or `/docs`, not an arbitrary folder).

### 3. Bind the custom domain

Under the **GitHub Actions** source, the custom domain is bound through the repo's Pages settings (not by a `CNAME` file alone): in **Settings &rarr; Pages &rarr; Custom domain**, enter `tereza-jakub.cz` and save (or via the CLI: `gh api repos/jakubdostal233/wedding-website/pages -X PUT -F cname=tereza-jakub.cz`).

A `CNAME` file is also kept at `site/CNAME` (containing `tereza-jakub.cz`) so it ships inside the served artifact at the root &mdash; conventional and portable, but the authoritative binding is the Pages setting above. The Pages settings page shows "Custom domain: tereza-jakub.cz" with a green check once DNS (step 4) resolves.

### 4. Configure DNS at Wedos

Open <https://client.wedos.com> &rarr; DNS for `tereza-jakub.cz`.

#### Delete

The current parking-page records:

| název | typ | data | Why delete |
|-------|-----|------|------------|
| (empty) | A | `185.8.237.22` | Wedos parking IP, replaced |
| (empty) | AAAA | `2a0e:acc0::d22` | Wedos parking IPv6, replaced |
| `*` | A | `185.8.237.22` | Wildcard parking; not needed |
| `*` | AAAA | `2a0e:acc0::d22` | Wildcard parking; not needed |

#### Keep

The Seznam Email Profi MX records &mdash; they handle email and are independent of the web records:

| název | typ | data |
|-------|-----|------|
| (empty) | MX | `10 5259e2d39345ffbf.mx2.emailprofi.seznam.cz.` |
| (empty) | MX | `20 5259e2d39345ffbf.mx1.emailprofi.seznam.cz.` |

Do **not** touch the MX records, otherwise email forwarding stops.

#### Add &mdash; four A records (apex, IPv4)

These are GitHub Pages' anycast IPs for custom apex domains. Documented at <https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site>.

| název | TTL | typ | data |
|-------|-----|-----|------|
| (empty) | 300 | A | `185.199.108.153` |
| (empty) | 300 | A | `185.199.109.153` |
| (empty) | 300 | A | `185.199.110.153` |
| (empty) | 300 | A | `185.199.111.153` |

#### Add &mdash; `www` CNAME (optional but recommended)

So that `www.tereza-jakub.cz` also works (GitHub redirects it to the apex automatically):

| název | TTL | typ | data |
|-------|-----|-----|------|
| `www` | 300 | CNAME | `jakubdostal233.github.io.` |

(Note the trailing dot.)

#### Apply

Click **aplikovat změny** (apply changes) at the top of the DNS panel.

### 5. Wait for DNS propagation

Usually under an hour, occasionally up to a few hours. From any terminal:

```bash
dig tereza-jakub.cz +short
```

Expected output once propagated:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

When you see those four IPs (in any order), DNS is live worldwide.

### 6. HTTPS verification

GitHub Pages auto-issues a Let's Encrypt certificate as soon as DNS resolves to its IPs. In the repo **Settings &rarr; Pages**:

1. Wait until "Custom domain" shows a green checkmark next to `tereza-jakub.cz`.
2. Tick **"Enforce HTTPS"** &mdash; this makes GitHub redirect any `http://` request to `https://`.

This usually takes a few minutes after DNS propagates. If the checkmark doesn't appear after an hour, click "Check again" or remove + re-add the custom domain in the Pages settings.

### 7. Test the live site

- Open <https://tereza-jakub.cz> on a phone over **mobile data** (not your home Wi-Fi &mdash; that may use a stale DNS cache)
- Click through every page; check the maps load, the QR renders, the ICS download works
- Send a test email to `info@tereza-jakub.cz` from another account; verify it arrives in your Gmail (MX records weren't touched, but worth confirming)
- Ask one trusted person to load the URL and report back before broadcasting it to all guests

## Updating the site

After initial deployment, every update is a single command:

```bash
git push
```

A push to `main` triggers the `deploy.yml` workflow, which uploads `site/` and deploys it. The new content is live within a minute or two (watch the **Actions** tab). No DNS or hosting touch needed.

The workflow uploads only `site/`, so edits outside it (`README.md`, `docs/`, `dev/`, `tools/`) still trigger a run but produce an identical artifact &mdash; no harm. Only changes under `site/` actually alter the published site.

## Rollback

If a deploy breaks something:

```bash
git revert HEAD
git push
```

Reverts the most recent commit and pushes; the `deploy.yml` workflow redeploys within ~1 minute. You can also re-run the last good deployment from the **Actions** tab (re-run the previous successful workflow run) without a new commit.

For broader rollback (multiple commits to undo), `git revert <oldercommit>..HEAD` and push. Avoid `git reset --hard` on `main` since the branch is shared with GitHub.

If the **deploy workflow itself** is broken (the site stops updating), check the Actions tab for the failing step and fix `.github/workflows/deploy.yml`; the workflow is a small static-upload (`upload-pages-artifact` with `path: site` → `deploy-pages`), so failures are usually a path or permissions typo.

For severe issues (e.g., the site shows wrong content on the wrong domain due to a CNAME / DNS misconfiguration), point the apex A records at Wedos back to the parking IPs (`185.8.237.22`) to take the site offline while you debug.

## Domain renewal

Wedos sends an email reminder ~30 days before the domain expires. To renew:

1. Log into <https://client.wedos.com>
2. **Domény &rarr; tereza-jakub.cz &rarr; Prodloužit / Renew**
3. Choose 1 year (or longer)
4. Pay (~120 CZK + VAT for `.cz`, 1-year term)

If you forget to renew, there's a grace period (~30&ndash;45 days for `.cz`) during which you can still recover the domain at higher cost. After that, the domain is released back to public registration and anyone can grab it.

After the wedding (2026-07-10), if you don't plan to keep the site online long-term, just let the domain lapse at the next renewal. The repo and content remain on GitHub indefinitely; only the custom domain disappears, and the site becomes reachable at `jakubdostal233.github.io/wedding-website/` again.

## Costs

| Item | Provider | Annual cost |
|------|----------|-------------|
| Domain `tereza-jakub.cz` | Wedos | ~120 CZK + VAT |
| Email forwarding | Seznam Email Profi (free tier) | 0 |
| Static hosting | GitHub Pages (free) | 0 |
| TLS certificate | Let's Encrypt (auto, via GitHub) | 0 |
| **Total** | | **~165 CZK + VAT / year** |

## Common issues

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `tereza-jakub.cz` shows the parking page | DNS hasn't propagated yet, or the apex A records still point at parking IPs | Wait, then verify with `dig tereza-jakub.cz +short` |
| `tereza-jakub.cz` loads but `*.github.io` doesn't | Expected after CNAME is set; GitHub redirects to the custom domain | Not a problem |
| HTTPS warning in browser | Cert not yet issued by Let's Encrypt | Wait 5&ndash;15 min after DNS resolves; check Pages settings for green check |
| Email stops working after DNS changes | MX records accidentally deleted | Re-add the two Seznam MX records (see [step 4 &mdash; Keep](#keep)) |
| Pages build fails | Syntax error or unsupported file in repo | Check Actions tab for the error message |
| Site updates aren't showing | Browser cache; GitHub CDN cache | Hard refresh (Ctrl+Shift+R); wait 5 min for CDN |
| Wedos DNS panel rejects an MX/CNAME with trailing dot | Some panels add the dot themselves | Try the value without the trailing dot |
