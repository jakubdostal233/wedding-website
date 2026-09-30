# Context &mdash; wedding-website

## Purpose

Static informational website for Tereza & Jakub's wedding on 10 July 2026 in Prague (Vršovický
zámeček). It tells guests when and where, how to get there, and what the day looks like; offers a
contact channel, an add-to-calendar file, and an optional bank QR for financial gifts (kept off the
public nav, reachable only via a direct link shared personally).

## What success looks like

The site is live at <https://tereza-jakub.cz>, the URL has been sent to every guest, and every
integration (maps, calendar file, `mailto:`, bank QR) works on the phones and banking apps guests
actually use &mdash; confirmed by the owner running [docs/qa-checklist.md](../docs/qa-checklist.md) on
real devices. After the wedding (2026-07-10) the site can be left live or the domain allowed to lapse;
either way the repository and its content remain on GitHub.

## Audience

Tereza & Jakub (owners) and their wedding guests (readers). Single-author, AI-assisted maintenance;
no other contributors.

## Principles

- **Free, low-effort, ~12-month lifecycle.** Vanilla HTML/CSS/JavaScript, no framework, no build step,
  no Node toolchain, no backend, no database &mdash; nothing in a pipeline to break or maintain. See
  `DECISIONS.md` D-STACK.
- **No third-party runtime services** beyond the Google Fonts CDN &mdash; no analytics, no form
  backends, no CDN for anything else &mdash; unless a new one is added with an explicit decision logged
  in `DECISIONS.md`. See D-NOSERVICES.
- **Public but unlisted**, never search-indexed: `robots.txt` disallows all crawlers and every page
  carries `<meta name="robots" content="noindex,nofollow">`. No true secrets live in tracked files,
  since the whole repository is technically reachable on the host. See D-PRIVACY.
- **No RSVP handling, no photo gallery beyond a few shots, no forms beyond `mailto:`.** Guest contact is
  a plain email link; RSVPs happen by email or phone, outside the site.
- **The deliverable and the meta-layer stay separated.** Everything served lives under `site/`
  (the only directory GitHub Pages publishes); planning, reference docs, generators and scratch live
  outside it in `dev/`, `docs/`, `tools/`, `tmp/`. See D-STRUCT.
- **Never drop data when restructuring.** A file move is `git mv`, not delete-and-recreate, so history
  survives.

## Relation to other work

Standalone. The deliverable/meta-layer split mirrors the `personal/tyre-model` reference project
(D-STRUCT); no other repo depends on this one.
