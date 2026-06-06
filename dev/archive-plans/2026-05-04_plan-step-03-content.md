# Step 03 &mdash; Content draft

Third implementation step. Goal: real Czech copy on every page, in vykání and warm-but-proper voice. Placeholders ("brzy doplníme") only where information is genuinely pending.

## Table of contents

- [Goal](#goal)
- [Inputs needed from the couple](#inputs-needed-from-the-couple)
- [Tasks](#tasks)
- [Voice and style](#voice-and-style)
- [Acceptance criteria](#acceptance-criteria)
- [What this step does NOT cover](#what-this-step-does-not-cover)

## Goal

Replace every Phase 2 placeholder with real Czech copy that matches the spec voice. Where information is genuinely pending (exact times, addresses, photos, IBAN), keep a clearly-flagged "brzy doplníme" placeholder rather than fabricating content.

## Inputs needed from the couple

| # | Page | What's needed |
|---|------|---------------|
| 1 | `location.html` | Exact street address of Vršovický zámeček, ceremony start time |
| 2 | `location.html` | Banquet at Vršovický zámeček itself, or a separate restaurant (with address)? |
| 3 | `program.html` | Day schedule &mdash; approximate times are fine |
| 4 | `about-us.html` | Where / when / how the couple met (paragraph or bullet points) |
| 5 | `contact.html` | Email address for the `mailto:` link |
| 6 | `gift.html` (Phase 4) | IBAN / account number &mdash; can be deferred to Phase 4 |

Anything not provided lands as "brzy doplníme" rather than a fabrication.

## Tasks

### 1. Hero (`index.html`)

Add a short welcoming line below the place &mdash; something like *"Těšíme se na vás."* &mdash; to soften the ceremonial feel of names + date + place.

### 2. Místo a čas (`location.html`)

Lead with a short prose paragraph framing the venue, followed by structured fields (address, ceremony time, banquet location). Keep Phase 2's section structure (Obřad · Hostina · Mapa).

### 3. Program (`program.html`)

Replace placeholder `00:00` rows with the real schedule, or keep them with a "brzy doplníme" intro if times aren't yet set. Keep the `<dl class="timeline">` markup.

### 4. Cesta a ubytování (`transit.html`)

Generic Prague-area intro is acceptable in this phase; specifics tighten once the venue is locked. Sections: Autem a parkování · Hromadná doprava · Ubytování.

### 5. O nás (`about-us.html`)

Write the meeting story in 1–2 short paragraphs, in vykání ("Potkali jsme se…"). Photos remain a Phase 5 placeholder.

### 6. Kontakt (`contact.html`)

Write the email-us copy with the actual address. The "Přidat do kalendáře" section remains a Phase 4 placeholder.

### 7. Dar (`gift.html`)

The lead paragraph from Phase 2 stays. The QR section remains a Phase 4 placeholder.

## Voice and style

- **Vykání** (V-form). "Milí hosté", "těšíme se na vás", "rádi bychom vás přivítali".
- **Warm but proper** &mdash; not stiff, not casual. The tone of a printed wedding invitation, not a product page.
- **Concise** &mdash; short paragraphs that scan well on mobile.
- **Diacritics correct** everywhere (á č ď é ě í ň ó ř š ť ú ů ý ž).
- **No marketing speak** ("zveme vás na nezapomenutelný zážitek" &mdash; no, thanks).

## Acceptance criteria

- [ ] No Phase 2 placeholder copy remains
- [ ] Every "brzy doplníme" maps to one of the 6 listed inputs (no orphan placeholders)
- [ ] Voice is consistent across pages (vykání, warm but proper)
- [ ] Diacritics correct everywhere
- [ ] Mobile read at 375px &mdash; paragraphs fit comfortably, no awkward breaks

## What this step does NOT cover

- Map iframe, `.ics` file, `mailto:` wiring, SPAYD QR (Phase 4)
- Real photos (Phase 5)
- Accessibility audit, cross-browser, validation (Phase 6)
- Domain and deploy (Phase 7)
