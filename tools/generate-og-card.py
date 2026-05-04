"""Generate the Open Graph preview card for the wedding website.

Output: ``assets/img/og-card.png`` (1200x630, the size Facebook/WhatsApp/iMessage
expect for link previews).

Uses **EB Garamond** from the system fonts &mdash; a very close cousin of the site's
Cormorant Garamond (both are 16th-century Garamond revivals), so the share-card
visually matches the hero block.

Usage::

    uv run --with pillow python tools/generate-og-card.py

Re-run if the names, date, or place change. The PNG is the tracked artefact
under ``assets/img/`` &mdash; this script is a one-shot generator.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# Canvas
W, H = 1200, 630

# Palette (matches the site's --color-* tokens in main.css)
BG = (250, 248, 243)       # ivory
TEXT = (42, 42, 42)        # charcoal
ACCENT = (138, 154, 123)   # sage
MUTED = (107, 107, 107)

# Font files (system-installed)
EBG = Path("/usr/share/fonts/truetype/ebgaramond")
SANS = Path("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf")

FONT_REGULAR = EBG / "EBGaramond12-Regular.ttf"
FONT_BOLD = EBG / "EBGaramond12-Bold.ttf"
FONT_ITALIC = EBG / "EBGaramond12-Italic.ttf"

OUT = Path(__file__).resolve().parent.parent / "assets" / "img" / "og-card.png"


def draw_centered(draw: ImageDraw.ImageDraw, text: str, y: int,
                  font: ImageFont.FreeTypeFont, fill: tuple[int, int, int]) -> None:
    """Draw `text` horizontally centered at vertical position `y`."""
    w = draw.textlength(text, font=font)
    draw.text(((W - w) / 2, y), text, fill=fill, font=font)


def main() -> None:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # --- Date row (sans, slightly tracked, muted) ----------------------
    date_font = ImageFont.truetype(str(SANS), size=32)
    draw_centered(draw, "10.07.2026", 100, date_font, MUTED)

    # --- Names (large serif, with sage bold ampersand) ----------------
    name_font = ImageFont.truetype(str(FONT_REGULAR), size=140)
    amp_font = ImageFont.truetype(str(FONT_BOLD), size=140)

    parts: list[tuple[str, ImageFont.FreeTypeFont, tuple[int, int, int]]] = [
        ("Tereza ", name_font, TEXT),
        ("& ", amp_font, ACCENT),
        ("Jakub", name_font, TEXT),
    ]
    total_w = sum(draw.textlength(s, font=f) for s, f, _ in parts)
    x = (W - total_w) / 2
    y_names = 180
    for s, f, color in parts:
        draw.text((x, y_names), s, fill=color, font=f)
        x += draw.textlength(s, font=f)

    # --- Sage divider --------------------------------------------------
    div_y = 400
    div_half = 60
    draw.rectangle(
        [(W // 2 - div_half, div_y), (W // 2 + div_half, div_y + 2)],
        fill=ACCENT,
    )

    # --- Place (italic serif) -----------------------------------------
    place_font = ImageFont.truetype(str(FONT_ITALIC), size=46)
    draw_centered(draw, "Praha, Vršovický zámeček", 430, place_font, TEXT)

    # --- Welcome line (smaller italic muted) ---------------------------
    welcome_font = ImageFont.truetype(str(FONT_ITALIC), size=32)
    draw_centered(draw, "Těšíme se na vás.", 530, welcome_font, MUTED)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG", optimize=True)

    size_kb = OUT.stat().st_size / 1024
    print(f"Wrote {OUT} ({size_kb:.1f} KB, {W}x{H})")


if __name__ == "__main__":
    main()
