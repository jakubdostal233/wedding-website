"""Generate the SPAYD payment QR code for the wedding bank account.

Output: ``site/assets/img/qr-platba.svg``

SPAYD (Short Payment Descriptor) is the Czech standard for QR payments.
Every Czech mobile-banking app can scan this format and pre-fill a payment.

Usage::

    uv run --with segno python tools/generate-spayd-qr.py

Re-run only when the account info or variable symbol changes; the SVG is
the tracked artefact under ``site/assets/img/``.
"""

from __future__ import annotations

from pathlib import Path

import segno

# SPAYD spec: https://qr-platba.cz/pro-vyvojare/specifikace-formatu/
# Fields are separated by `*`; each is `KEY:VALUE`.
SPAYD = (
    "SPD*1.0"
    "*ACC:CZ5920100000002601802091+FIOBCZPPXXX"
    "*X-VS:10072026"
    "*MSG:Svatba Tereza a Jakub"
)

OUT = Path(__file__).resolve().parent.parent / "site" / "assets" / "img" / "qr-platba.svg"


def main() -> None:
    print("Encoding SPAYD:")
    print(f"  {SPAYD}\n")

    OUT.parent.mkdir(parents=True, exist_ok=True)

    qr = segno.make(SPAYD, error="m")
    qr.save(str(OUT), scale=10, border=2)

    size_kb = OUT.stat().st_size / 1024
    print(f"Wrote {OUT} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
