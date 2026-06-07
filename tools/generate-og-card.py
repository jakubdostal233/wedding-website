"""Generate the Open Graph preview card for the wedding website.

Output: ``site/assets/img/og-card.png`` (1200x630, the size Facebook / WhatsApp /
iMessage expect for link previews).

The card is authored as HTML (``tools/og-card.html``) and rendered with **headless
Chromium**, so it uses the site's real web fonts (Playfair Display + Source Sans 3,
from the Google Fonts CDN) and therefore matches the live pages exactly &mdash; no
font-substitution guesswork.

Usage::

    python tools/generate-og-card.py

Re-run if the names, date, or place change (edit ``og-card.html`` first). The PNG is
the tracked artefact under ``site/assets/img/``; this script is a one-shot generator.

Note: ``--ignore-certificate-errors`` is passed so the Google Fonts CDN loads even on
a TLS-inspecting corporate network (e.g. VUTS); it is harmless elsewhere.
"""

from __future__ import annotations

import glob
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "tools" / "og-card.html"
OUT = ROOT / "site" / "assets" / "img" / "og-card.png"
W, H = 1200, 630


def find_chromium() -> str:
    """Locate a Chromium/Chrome binary (Playwright build preferred, then system)."""
    pw = sorted(glob.glob(os.path.expanduser(
        "~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome")))
    if pw:
        return pw[-1]
    for name in ("google-chrome-stable", "google-chrome", "chromium", "chromium-browser"):
        path = shutil.which(name)
        if path:
            return path
    sys.exit("No Chromium/Chrome binary found.")


def main() -> None:
    chrome = find_chromium()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [chrome, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
         "--force-device-scale-factor=1", f"--window-size={W},{H}",
         "--ignore-certificate-errors", "--virtual-time-budget=8000",
         f"--screenshot={OUT}", HTML.as_uri()],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )

    # Re-save optimised (and confirm dimensions) via Pillow if available.
    try:
        from PIL import Image
        with Image.open(OUT) as im:
            assert im.size == (W, H), f"unexpected size {im.size}"
            im.convert("RGB").save(OUT, "PNG", optimize=True)
    except ImportError:
        pass

    print(f"Wrote {OUT} ({OUT.stat().st_size / 1024:.1f} KB, {W}x{H})")


if __name__ == "__main__":
    main()
