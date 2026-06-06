# QA checklist

Functional checks to run on real devices after major changes &mdash; **especially** before sharing the site URL with guests, and after any deploy that touches integrations (map, calendar, QR, mailto).

The site looking right in your laptop browser is not enough; the integrations have to work on the **devices guests will actually use**.

## Table of contents

- [Test devices](#test-devices)
- [Pages render correctly](#pages-render-correctly)
- [Integrations &mdash; the things that must work](#integrations--the-things-that-must-work)
- [Sharing previews (Open Graph)](#sharing-previews-open-graph)
- [Performance / load](#performance--load)
- [Robots / privacy](#robots--privacy)
- [After any change to the bank info or schedule](#after-any-change-to-the-bank-info-or-schedule)
- [After a domain or DNS change](#after-a-domain-or-dns-change)
- [Abbreviations](#abbreviations)

## Abbreviations

| Abbreviation | Meaning |
|---|---|
| BIC | Bank Identifier Code (SWIFT) |
| DNS | Domain Name System |
| IBAN | International Bank Account Number |
| ICS | iCalendar file format (RFC 5545) |
| MX | Mail Exchange (DNS record type) |
| OG | Open Graph (link-preview metadata) |
| QR | Quick-response code |
| SPAYD | Short Payment Descriptor (Czech QR payment standard) |
| VS | Variable symbol (Czech payment reference) |
| WCAG AA | Web Content Accessibility Guidelines, level AA |

## Test devices

Run the relevant rows on at least:

- [ ] Your phone, **mobile data** (not work Wi-Fi &mdash; bypasses any corporate proxy)
- [ ] Your phone, home Wi-Fi
- [ ] A laptop or desktop browser
- [ ] (Bonus) Borrow a friend's phone (different OS / different banking app)

## Pages render correctly

For each page (`index`, `location`, `program`, `transit`, `about-us`, `contact`, `gift`):

- [ ] Page loads at `https://tereza-jakub.cz/<page>.html` (and `/` for index)
- [ ] HTTPS lock icon shows in browser, no cert warning
- [ ] Hero / page heading renders with the right serif typography
- [ ] Header nav: 6 links visible, active page underlined in sage
- [ ] Footer present, contact link works
- [ ] No layout breakage at narrow viewport (browser ~375px wide; phone in portrait)
- [ ] Browser tab shows the dark slate "T&J" favicon

## Integrations &mdash; the things that must work

### Maps (`location.html`)

- [ ] Both maps load (Vršovický zámeček + Restaurace La Farma)
- [ ] You can pan and zoom inside each iframe
- [ ] "Otevřít na Mapy.cz" link opens mapy.cz in a new tab, centered on the right venue
- [ ] "Otevřít v Google Maps" link opens Google Maps in a new tab, centered on the right venue
- [ ] On phone, opening the maps starts navigation cleanly

### Calendar (`contact.html`)

- [ ] "Přidat do kalendáře (.ics)" button downloads `wedding_tj.ics`
- [ ] Opening the file on **iOS / iPhone** &rarr; offered to add to Apple Calendar; event lands as "Svatba | Tereza a Jakub" on **10. 7. 2026, 11:00 local Prague**, ending 23:00
- [ ] Opening the file on **Android** &rarr; offered to add to Google Calendar (or whichever calendar app); same event details
- [ ] Opening the file on **desktop** with Outlook / Thunderbird / Google Calendar &rarr; same
- [ ] Event location shows "Vršovický zámeček, Praha"
- [ ] Event description has the full text and tap-able

### Email contact (`contact.html`)

- [ ] Tapping `info@tereza-jakub.cz` link opens the device's default email client
- [ ] Subject is pre-filled with **"Svatba 10.07.2026"**
- [ ] Send a real test email; arrives in your Gmail within ~1 minute
- [ ] Reply to the test email from Gmail &rarr; arrives at sender (forwarding works **both ways**? &mdash; if not, that's expected, replies-from-Gmail use Gmail's address, not the alias)

### Bank QR (`gift.html`)

Test with **at least 2 different Czech banking apps** to catch app-specific quirks:

- [ ] **Fio Banka app** &rarr; QR platba scanner &rarr; QR scans, app pre-fills:
  - Recipient account `2601802091/2010`
  - VS `10072026`
  - Message "Svatba Tereza a Jakub"
  - Amount blank (you enter)
- [ ] **Second banking app** (KB Mobilní banka / ČSOB Smart / Air Bank / Equa / your friend's app) &rarr; scans cleanly with same fields
- [ ] IBAN under the QR is correct: `CZ59 2010 0000 0026 0180 2091`
- [ ] BIC under the QR is correct: `FIOBCZPPXXX`

## Sharing previews (Open Graph)

- [ ] Send the URL `https://tereza-jakub.cz/` to yourself in **WhatsApp** &rarr; preview card appears with the names + date image, not just plain link
- [ ] Same in **Messenger / iMessage / Telegram / Slack / email**
- [ ] If a preview shows the wrong image: invalidate the cache via Facebook's Sharing Debugger (<https://developers.facebook.com/tools/debug/>) and Twitter's Card Validator (<https://cards-dev.twitter.com/validator>)

## Performance / load

- [ ] First page load on phone (mobile data) feels snappy (under ~3 s)
- [ ] No console errors in the browser DevTools (F12 &rarr; Console)
- [ ] No 404s in the Network tab (other than expected absence of any optional resources)

## Robots / privacy

- [ ] `https://tereza-jakub.cz/robots.txt` returns the `Disallow: /` rule
- [ ] Searching `site:tereza-jakub.cz` on Google returns no results (eventually, after Google re-crawls; immediately after deploy this just confirms the site isn't already indexed)

## After any change to the bank info or schedule

- [ ] Re-run `tools/generate-spayd-qr.py` (if SPAYD MSG / VS / IBAN changed)
- [ ] Re-scan the QR with your banking app to confirm new values
- [ ] Edit `site/assets/wedding_tj.ics` if the date or time changed; re-import on a phone to confirm the event updates

## After a domain or DNS change

- [ ] `dig tereza-jakub.cz +short` (or `host tereza-jakub.cz`) returns the four GitHub Pages IPs (`185.199.108-111.153`)
- [ ] Email forwarding still works (send a test to `info@tereza-jakub.cz`)
- [ ] HTTPS still works without cert warning
