"""Generate the reception seating schemes (inside + terrace) as SVG.

Output: ``site/assets/img/seating-inside.svg`` (restaurant, "Uvnitř") and
``site/assets/img/seating-outside.svg`` (terrace, "Venku") &mdash; the tracked
artefacts. This script is their single source of truth: the floor plans are
authored parametrically here (palette constants, primitive helpers, scene
functions), so a seat, label, or wall moves by editing a coordinate and
re-running &mdash; never by hand-editing the emitted SVG.

Usage::

    python tools/generate-seating-schemes.py

Styled with the site identity (blush ``#ed9dbc`` accent, Playfair Display
titles + Source Sans 3 numbers, fonts via the Google Fonts CDN inside the
SVG ``<style>``). Note for embedding: an SVG referenced through ``<img>``
does not load external fonts (browser image mode) &mdash; inline the SVG into
the HTML when the real fonts must apply. Standard library only.
"""

from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "site" / "assets" / "img"

# --- palette (from the wedding site: blush accent on white) ----------------
ACCENT = "#ed9dbc"        # blush pink - titles, accents
ACCENT_DARK = "#c76a8d"   # deeper blush - key labels
TABLE_FILL = "#f9e7ef"    # soft blush tint - table tops
TABLE_STROKE = "#dbaabf"  # table outline
ZONE_FILL = "#f3ece2"     # warm neutral - bar / toilets / service zones
INK = "#3a3a3a"           # charcoal - body text, seat numbers (not pure black)
INK_SOFT = "#7a7a7a"      # muted - secondary labels, arrows
WALL = "#9a9a9a"          # room outline / low walls
SEAT_FILL = "#ffffff"     # seat fill
PAGE_BG = "#ffffff"       # the site background is white

FONT_TITLE = "'Playfair Display', Georgia, 'Times New Roman', serif"
FONT_BODY = "'Source Sans 3', 'Segoe UI', system-ui, sans-serif"
FONT_IMPORT = (
    "@import url('https://fonts.googleapis.com/css2?"
    "family=Playfair+Display:wght@500;600;700&"
    "family=Source+Sans+3:wght@400;600;700&display=swap');"
)

SEAT = 42  # seat chip side length


# --- low-level SVG helpers -------------------------------------------------
def esc(s) -> str:
    return html.escape(str(s), quote=True)


def text(x, y, s, size=18, fill=INK, font=None, weight=400,
         anchor="middle", baseline="central", spacing=None) -> str:
    font = font or FONT_BODY
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="{font}" font-size="{size}" '
        f'fill="{fill}" font-weight="{weight}" text-anchor="{anchor}" '
        f'dominant-baseline="{baseline}"{ls}>{esc(s)}</text>'
    )


def seat(cx, cy, label, size=SEAT) -> str:
    half = size / 2
    fill, stroke, num, sw = SEAT_FILL, "#c9c9c9", INK, 1.6
    return (
        f'<rect x="{cx - half:.1f}" y="{cy - half:.1f}" width="{size}" height="{size}" '
        f'rx="9" ry="9" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
        + text(cx, cy, label, size=size * 0.42, fill=num, weight=600)
    )


def table(x, y, w, h, rx=16) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" ry="{rx}" '
        f'fill="{TABLE_FILL}" stroke="{TABLE_STROKE}" stroke-width="2"/>'
    )


def room(x, y, w, h) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" '
        f'fill="none" stroke="{WALL}" stroke-width="2.5"/>'
    )


def wall(x, y, w, h) -> str:
    """Hatched low wall (zidka)."""
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#hatch)" '
        f'stroke="{WALL}" stroke-width="1.5"/>'
    )


def stairs(x, y, w, h, label="Schody") -> str:
    parts = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" '
        f'fill="#f0f0f0" stroke="{WALL}" stroke-width="1.5"/>'
    ]
    for i in range(1, 4):
        yy = y + h * i / 4
        parts.append(
            f'<line x1="{x}" y1="{yy:.1f}" x2="{x + w}" y2="{yy:.1f}" '
            f'stroke="{WALL}" stroke-width="1.2"/>'
        )
    parts.append(text(x + w / 2, y + h + 15, label, size=15, fill=INK_SOFT, weight=600))
    return "".join(parts)


def zone(x, y, w, h, label="", fill=ZONE_FILL, size=22, font=None, weight=600) -> str:
    font = font or FONT_TITLE
    rect = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" '
        f'stroke="{TABLE_STROKE}" stroke-width="1.6"/>'
    )
    if not label:
        return rect
    return rect + text(x + w / 2, y + h / 2, label, size=size, fill=INK, font=font,
                       weight=weight, spacing="1")


def arrow(x1, y1, x2, y2) -> str:
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK_SOFT}" '
        f'stroke-width="2.5" marker-end="url(#arrow)"/>'
    )


def banquet_run(x, y, w, h, left, right, foot=None) -> str:
    """A long banquet table: seats down the left and right long edges,
    an optional seat at the foot. left/right are label lists (top -> bottom)."""
    parts = [table(x, y, w, h)]
    n = len(left)
    top, bot = y + 40, y + h - 40
    ys = [top + (bot - top) * i / (n - 1) for i in range(n)]
    for lbl, cy in zip(left, ys):
        parts.append(seat(x - 28, cy, lbl))
    for lbl, cy in zip(right, ys):
        parts.append(seat(x + w + 28, cy, lbl))
    if foot:
        parts.append(seat(x + w / 2, y + h + 30, foot))
    return "".join(parts)


def cluster4(cx, cy, left, right) -> str:
    """Table for four, two seats on each long side. left/right = (top, bottom)."""
    parts = [table(cx - 40, cy - 50, 80, 100)]
    for lbl, oy in zip(left, (-24, 24)):
        parts.append(seat(cx - 67, cy + oy, lbl))
    for lbl, oy in zip(right, (-24, 24)):
        parts.append(seat(cx + 67, cy + oy, lbl))
    return "".join(parts)


def title(cx, y, s, size=44) -> str:
    return (
        text(cx, y, s, size=size, fill=ACCENT, font=FONT_TITLE, weight=600, spacing="3")
        + f'<line x1="{cx - 70}" y1="{y + size * 0.55:.1f}" x2="{cx + 70}" '
        f'y2="{y + size * 0.55:.1f}" stroke="{ACCENT}" stroke-width="2.5" '
        'stroke-linecap="round"/>'
    )


DEFS = (
    "<defs>"
    '<pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" '
    f'patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="8" '
    f'stroke="{WALL}" stroke-width="2"/></pattern>'
    '<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" '
    'markerHeight="7" orient="auto-start-reverse">'
    f'<path d="M0,0 L10,5 L0,10 z" fill="{INK_SOFT}"/></marker>'
    "</defs>"
)


def document(w, h, body) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="{w}" height="{h}" font-family="{FONT_BODY}">'
        f"<style><![CDATA[{FONT_IMPORT}]]></style>{DEFS}"
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="{PAGE_BG}"/>'
        f"{body}</svg>"
    )


# --- scene: inside (UVNITR) ------------------------------------------------
def build_inside() -> str:
    W, H = 920, 1240
    p = [title(W / 2, 60, "Uvnitř")]
    p.append(room(45, 100, 830, 1095))

    # head table: guests along both long edges, seat 5 at the left end
    tx, ty, tw, th = 185, 185, 560, 84
    cy_top = ty - 6 - SEAT / 2
    cy_bot = ty + th + 6 + SEAT / 2
    p.append(table(tx, ty, tw, th))
    # both edges share one 6-slot grid; bottom slots 2+3 (across from the
    # couple 2+1) stay empty, so 6-9 sit exactly across from 4, 3, 11, 10
    def slot_x(i):
        return tx + tw * (i + 0.5) / 6
    for i, lbl in enumerate(["4", "3", "2", "1", "11", "10"]):
        p.append(seat(slot_x(i), cy_top, lbl))
    for i, lbl in zip((0, 1, 4, 5), ("6", "7", "8", "9")):
        p.append(seat(slot_x(i), cy_bot, lbl))
    p.append(seat(tx - 6 - SEAT / 2, ty + th / 2, "5"))  # left end

    # low walls (spanning to the room side walls) + stairs between them
    p.append(wall(45, 345, 355, 24))
    p.append(wall(530, 345, 345, 24))
    p.append(text(222, 388, "zídka", size=14, fill=INK_SOFT, weight=600))
    p.append(text(702, 388, "zídka", size=14, fill=INK_SOFT, weight=600))
    p.append(stairs(400, 333, 130, 48))

    # left cluster (12-15) and right banquet run (16-30 + 23)
    p.append(cluster4(250, 560, left=("15", "14"), right=("12", "13")))
    p.append(banquet_run(560, 470, 150, 560,
                         left=["30", "29", "28", "27", "26", "25", "24"],
                         right=["16", "17", "18", "19", "20", "21", "22"],
                         foot="23"))

    # toilets alcove between the cluster and the bar - centred arrow, label below it
    p.append(zone(45, 800, 110, 90))
    p.append(arrow(130, 835, 70, 835))
    p.append(text(100, 864, "Toalety", size=15, weight=600))

    # bar (attached to the left and bottom walls) and entrance (bottom-right)
    p.append(zone(45, 1060, 390, 135, "Bar", size=30))
    p.append(arrow(805, 1130, 745, 1130))
    p.append(text(775, 1158, "Vchod", size=18, fill=INK, weight=600))

    return document(W, H, "".join(p))


# --- scene: outside / terrace (VENKU) --------------------------------------
def build_outside() -> str:
    W, H = 560, 820
    p = [title(W / 2, 60, "Venku")]
    # terrace outline (sized to the table run) + a light railing line down the left
    p.append(room(140, 125, 300, 590))
    p.append(
        f'<path d="M95,135 L95,725 L150,725" fill="none" stroke="{WALL}" '
        'stroke-width="2" stroke-linejoin="round"/>'
    )
    p.append(banquet_run(250, 170, 110, 430,
                         left=["45", "44", "43", "42", "41", "40", "39"],
                         right=["31", "32", "33", "34", "35", "36", "37"],
                         foot="38"))
    # entrance bottom-left - arrow pointing left, label below (same pattern as inside)
    p.append(arrow(140, 755, 80, 755))
    p.append(text(110, 783, "Vchod", size=18, fill=INK, weight=600))
    return document(W, H, "".join(p))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, build in [("seating-inside.svg", build_inside),
                        ("seating-outside.svg", build_outside)]:
        out = OUT_DIR / name
        out.write_text(build(), encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
