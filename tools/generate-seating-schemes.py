"""Generate the reception seating schemes (inside + terrace) as SVG, in two variants.

Output (all tracked artefacts under ``site/assets/img/``):

- ``seating-inside.svg`` / ``seating-outside.svg`` &mdash; seats carry **numbers** 1&ndash;45;
- ``seating-inside-names.svg`` / ``seating-outside-names.svg`` &mdash; the same floor
  plans with **guest names** on larger chips (long names wrap to two lines).

This script is the single source of truth for all four files: the floor plans are
authored parametrically (palette constants, primitive helpers, scene functions,
per-variant chip geometry), so a seat, name, or wall changes by editing this file
and re-running &mdash; never by hand-editing the emitted SVGs.

Usage::

    python tools/generate-seating-schemes.py

Styled with the site identity (blush ``#ed9dbc`` accent, Playfair Display titles +
Source Sans 3 chip text, fonts via the Google Fonts CDN inside the SVG ``<style>``).
Note for embedding: an SVG referenced through ``<img>`` does not load external
fonts (browser image mode) &mdash; inline the SVG into the HTML when the real fonts
must apply. Standard library only.
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
INK = "#3a3a3a"           # charcoal - body text, chip text (not pure black)
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

SEAT = 42  # numbered seat chip side length

# --- guest names (seat number -> name); the names variant renders these ----
NAMES = {
    1: "Nevěsta", 2: "Ženich", 3: "Maminka ženicha", 4: "Tatínek ženicha",
    5: "Tomášek", 6: "Sestra ženicha", 7: "Tomáš H.", 8: "Babička nevěsty",
    9: "Dědeček nevěsty", 10: "Martin", 11: "Maminka nevěsty", 12: "Michal P.",
    13: "Šárka P.", 14: "Teta Stáňa", 15: "Babička ženicha", 16: "Bratr nevěsty",
    17: "Terka", 18: "Daniel", 19: "Strejda Jára", 20: "Žanet",
    21: "Martina S.", 22: "Marek S.", 23: "Vítek", 24: "Martin K.",
    25: "Lea K.", 26: "Bára", 27: "Jirka", 28: "Ondra",
    29: "Martina D.", 30: "Tatínek nevěsty", 31: "Pavel Š.", 32: "Adam B.",
    33: "Dominik", 34: "Martin P.", 35: "André", 36: "Valda",
    37: "Michal Z.", 38: "Amálka", 39: "Monča", 40: "Míša",
    41: "Klára", 42: "Eliška", 43: "Ester", 44: "Anet B.", 45: "Magda Š.",
}

# --- variants: chip geometry + outside-terrace fit --------------------------
# names chips are wider/taller to fit two-line names; the terrace room widens
# accordingly so the chips keep a margin to its walls.
MODES = {
    "numbers": {"suffix": "", "names": False, "w": SEAT, "h": SEAT,
                "out_room": (140, 300), "rail_x": 95},
    "names": {"suffix": "-names", "names": True, "w": 80, "h": 46,
              "out_room": (130, 350), "rail_x": 85},
}


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


def seat(cx, cy, n, m) -> str:
    """One seat chip: the number (numbers mode) or the guest name (names mode,
    wrapping names longer than 10 chars at the first space)."""
    w, h = m["w"], m["h"]
    chip = (
        f'<rect x="{cx - w / 2:.1f}" y="{cy - h / 2:.1f}" width="{w}" height="{h}" '
        f'rx="9" ry="9" fill="{SEAT_FILL}" stroke="#c9c9c9" stroke-width="1.6"/>'
    )
    if not m["names"]:
        return chip + text(cx, cy, n, size=w * 0.42, weight=600)
    name = NAMES[n]
    if len(name) > 10 and " " in name:
        l1, l2 = name.split(" ", 1)
        return (chip + text(cx, cy - 8.5, l1, size=13, weight=600)
                + text(cx, cy + 8.5, l2, size=13, weight=600))
    return chip + text(cx, cy, name, size=13, weight=600)


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


def banquet_run(x, y, w, h, left, right, m, foot=None) -> str:
    """A long banquet table: seats down the left and right long edges,
    an optional seat at the foot. left/right are seat-number lists (top -> bottom)."""
    parts = [table(x, y, w, h)]
    n = len(left)
    top, bot = y + 40, y + h - 40
    ys = [top + (bot - top) * i / (n - 1) for i in range(n)]
    dx = 7 + m["w"] / 2
    for num, cy in zip(left, ys):
        parts.append(seat(x - dx, cy, num, m))
    for num, cy in zip(right, ys):
        parts.append(seat(x + w + dx, cy, num, m))
    if foot:
        parts.append(seat(x + w / 2, y + h + 9 + m["h"] / 2, foot, m))
    return "".join(parts)


def cluster4(cx, cy, left, right, m) -> str:
    """Table for four, two seats on each long side. left/right = (top, bottom)."""
    parts = [table(cx - 40, cy - 50, 80, 100)]
    dx = 46 + m["w"] / 2
    for num, oy in zip(left, (-24, 24)):
        parts.append(seat(cx - dx, cy + oy, num, m))
    for num, oy in zip(right, (-24, 24)):
        parts.append(seat(cx + dx, cy + oy, num, m))
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
def build_inside(m) -> str:
    W, H = 920, 1240
    p = [title(W / 2, 60, "Uvnitř")]
    p.append(room(45, 100, 830, 1095))

    # head table: guests along both long edges, seat 5 at the left end
    tx, ty, tw, th = 185, 185, 560, 84
    cy_top = ty - 6 - m["h"] / 2
    cy_bot = ty + th + 6 + m["h"] / 2
    p.append(table(tx, ty, tw, th))
    # both edges share one 6-slot grid; bottom slots 2+3 (across from the
    # couple 2+1) stay empty, so 6-9 sit exactly across from 4, 3, 11, 10
    def slot_x(i):
        return tx + tw * (i + 0.5) / 6
    for i, num in enumerate([4, 3, 2, 1, 11, 10]):
        p.append(seat(slot_x(i), cy_top, num, m))
    for i, num in zip((0, 1, 4, 5), (6, 7, 8, 9)):
        p.append(seat(slot_x(i), cy_bot, num, m))
    p.append(seat(tx - 6 - m["w"] / 2, ty + th / 2, 5, m))  # left end

    # low walls (spanning to the room side walls) + stairs between them
    p.append(wall(45, 345, 355, 24))
    p.append(wall(530, 345, 345, 24))
    p.append(text(222, 388, "zídka", size=14, fill=INK_SOFT, weight=600))
    p.append(text(702, 388, "zídka", size=14, fill=INK_SOFT, weight=600))
    p.append(stairs(400, 333, 130, 48))

    # left cluster (12-15) and right banquet run (16-30 + 23)
    p.append(cluster4(250, 560, left=(15, 14), right=(12, 13), m=m))
    p.append(banquet_run(560, 470, 150, 560,
                         left=[30, 29, 28, 27, 26, 25, 24],
                         right=[16, 17, 18, 19, 20, 21, 22],
                         m=m, foot=23))

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
def build_outside(m) -> str:
    W, H = 560, 820
    room_x, room_w = m["out_room"]
    rail_x = m["rail_x"]
    p = [title(W / 2, 60, "Venku")]
    # terrace outline (sized to the table run) + a light railing line down the left
    p.append(room(room_x, 125, room_w, 590))
    p.append(
        f'<path d="M{rail_x},135 L{rail_x},725 L150,725" fill="none" stroke="{WALL}" '
        'stroke-width="2" stroke-linejoin="round"/>'
    )
    p.append(banquet_run(250, 170, 110, 430,
                         left=[45, 44, 43, 42, 41, 40, 39],
                         right=[31, 32, 33, 34, 35, 36, 37],
                         m=m, foot=38))
    # entrance bottom-left - arrow pointing left, label below (same pattern as inside)
    head_x = rail_x - 15
    p.append(arrow(room_x, 755, head_x, 755))
    p.append(text((room_x + head_x) / 2, 783, "Vchod", size=18, fill=INK, weight=600))
    return document(W, H, "".join(p))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for m in MODES.values():
        for stem, build in [("seating-inside", build_inside),
                            ("seating-outside", build_outside)]:
            out = OUT_DIR / f"{stem}{m['suffix']}.svg"
            out.write_text(build(m), encoding="utf-8")
            print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
