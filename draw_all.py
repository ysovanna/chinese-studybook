# -*- coding: utf-8 -*-
"""Flat 2D object SVGs for the three Chinese units. Hand-authored, no image model.
Run: python draw_all.py"""
import io
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
NAVY, INK, WHITE, LINE = '#1C2A4A', '#23262D', '#FFFFFF', '#C9CED8'
BLUE, GREEN, PURPLE, ORANGE, BROWN = '#0052A4', '#00A84D', '#996CAC', '#EF7C1C', '#CD7C2F'
YELLOW = '#F5B700'


def svg(unit, name, body, vb='0 0 160 100'):
    d = os.path.join(ROOT, unit, 'img')
    os.makedirs(d, exist_ok=True)
    io.open(os.path.join(d, name), 'w', encoding='utf-8', newline='\n').write(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{body}</svg>\n')


def contour(unit, name, path_d, color, label):
    """A tone contour drawn as a thick line with an arrow head over the syllable 'ma'."""
    nums = [float(v) for v in re.findall(r'-?\d+(?:\.\d+)?', path_d)]
    x1, y1 = nums[-2], nums[-1]
    svg(unit, name,
        f'<rect x="0" y="0" width="160" height="100" rx="14" fill="#F3F5F9"/>'
        f'<path d="{path_d}" fill="none" stroke="{color}" stroke-width="7" stroke-linecap="round"/>'
        f'<circle cx="{x1}" cy="{y1}" r="6.5" fill="{color}"/>'
        f'<text x="80" y="92" font-family="Noto Sans, Arial, sans-serif" font-size="24" font-weight="700" '
        f'fill="{NAVY}" text-anchor="middle">{label}</text>')


def bubble(x, y, w, h, fill=WHITE, stroke=LINE, tail='M'):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>'
            f'<path d="M{x + 14} {y + h} l-6 14 l18 -14Z" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>')


def person(x, color, flip=False):
    f = 'transform="scale(-1,1) translate(-160 0)"' if flip else ''
    return (f'<g {f}><circle cx="{x}" cy="30" r="14" fill="{color}"/>'
            f'<path d="M{x - 20} 92 q0 -34 20 -34 q20 0 20 34Z" fill="{color}"/></g>')


# ============ unit 1 · tones-first ============
U = 'tones-first'
svg(U, 'x-marks.svg',
    ''.join(f'<text x="{18 + i * 40}" y="52" font-family="Noto Sans, Arial, sans-serif" font-size="34" '
            f'font-weight="800" fill="{c}" text-anchor="middle">{t}</text>'
            for i, (t, c) in enumerate([('ā', BLUE), ('á', GREEN), ('ǎ', PURPLE), ('à', ORANGE)]))
    + '<rect x="10" y="64" width="140" height="5" rx="2.5" fill="#E4E8EF"/>')
contour(U, 't1-flat.svg', 'M30 34 L130 34', BLUE, 'mā')
contour(U, 't2-rise.svg', 'M35 62 L125 26', GREEN, 'má')
contour(U, 't3-dip.svg', 'M30 34 Q60 78 95 74 T132 44', PURPLE, 'mǎ')
contour(U, 't4-fall.svg', 'M35 26 L125 66', ORANGE, 'mà')
svg(U, 'x-neutral.svg',
    '<rect x="0" y="0" width="160" height="100" rx="14" fill="#F3F5F9"/>'
    '<path d="M40 46 Q80 40 120 46" fill="none" stroke="' + BROWN + '" stroke-width="4" stroke-dasharray="7 7" stroke-linecap="round"/>'
    '<path d="M96 22 q10 8 2 20 q-14 4 -18 -8Z" fill="' + BROWN + '" opacity=".85"/>'
    '<text x="80" y="90" font-family="Noto Sans, Arial, sans-serif" font-size="22" font-weight="700" fill="' + NAVY + '" text-anchor="middle">ma</text>')
svg(U, 'c1-ma.svg',
    ''.join(
        f'<rect x="{6 + i * 39}" y="8" width="34" height="52" rx="8" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
        f'<path d="{p}" fill="none" stroke="{c}" stroke-width="4.5" stroke-linecap="round"/>'
        f'<text x="{23 + i * 39}" y="76" font-family="Noto Sans, Arial, sans-serif" font-size="15" font-weight="800" fill="{NAVY}" text-anchor="middle">{lab}</text>'
        for i, (p, c, lab) in enumerate([
            ('M13 24 L33 24', BLUE, '妈'), ('M14 42 L32 22', GREEN, '麻'),
            ('M13 26 Q20 44 27 42 T34 32', PURPLE, '马'), ('M14 22 L32 42', ORANGE, '骂')]))
    + '<path d="M96 84 q-4 -14 8 -18 q-2 8 4 10 q10 -14 26 -8 q-8 4 -6 10 q10 2 8 14 l-6 0 q-2 -8 -8 -8 l-14 0 q-6 0 -6 6Z" fill="' + INK + '"/>'
    '<circle cx="134" cy="70" r="1.8" fill="' + INK + '"/>')
svg(U, 'c3-pairs.svg',
    f'<rect x="8" y="12" width="66" height="76" rx="10" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<path d="M18 40 Q30 62 42 58 T64 40" fill="none" stroke="{PURPLE}" stroke-width="4.5" stroke-linecap="round"/>'
    f'<path d="M22 74 L58 52" fill="none" stroke="{GREEN}" stroke-width="4.5" stroke-linecap="round"/>'
    f'<text x="41" y="30" font-family="Noto Sans, Arial, sans-serif" font-size="14" font-weight="800" fill="{NAVY}" text-anchor="middle">你好</text>'
    f'<path d="M82 50 h16 m-6 -7 l7 7 l-7 7" stroke="{INK}" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
    f'<rect x="104" y="12" width="48" height="76" rx="10" fill="{WHITE}" stroke="{GREEN}" stroke-width="2.5"/>'
    f'<path d="M112 66 L142 34" fill="none" stroke="{GREEN}" stroke-width="4.5" stroke-linecap="round"/>'
    f'<text x="128" y="28" font-family="Noto Sans, Arial, sans-serif" font-size="13" font-weight="800" fill="{NAVY}" text-anchor="middle">ní hǎo</text>')
svg(U, 'c4-zhchsh.svg',
    f'<path d="M28 78 Q20 40 52 22 Q96 2 122 26 Q138 40 128 58 Q120 72 100 70" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'
    f'<path d="M40 78 Q64 92 96 82 Q118 74 128 58" fill="#F3D9D2" stroke="{NAVY}" stroke-width="3"/>'
    f'<ellipse cx="86" cy="46" rx="20" ry="9" transform="rotate(-24 86 46)" fill="{PURPLE}" opacity=".9"/>'
    + ''.join(f'<text x="{16 + i * 37}" y="96" font-family="Noto Sans, Arial, sans-serif" font-size="15" font-weight="800" fill="{NAVY}">{s}</text>' for i, s in enumerate(['zh', 'ch', 'sh', 'r'])))
svg(U, 'c5-blocks.svg',
    f'<rect x="6" y="34" width="44" height="32" rx="7" fill="{BLUE}"/>'
    f'<rect x="58" y="34" width="44" height="32" rx="7" fill="{GREEN}"/>'
    f'<rect x="110" y="34" width="44" height="32" rx="7" fill="{ORANGE}"/>'
    + ''.join(f'<text x="{x}" y="55" font-family="Noto Sans, Arial, sans-serif" font-size="14" font-weight="800" fill="{WHITE}" text-anchor="middle">{w}</text>' for x, w in [(28, '我'), (80, '喜欢'), (132, '咖啡')])
    + '<path d="M52 50 h4 m-2 -3 l3 3 l-3 3" stroke="' + INK + '" stroke-width="2.5" fill="none"/>'
      '<path d="M104 50 h4 m-2 -3 l3 3 l-3 3" stroke="' + INK + '" stroke-width="2.5" fill="none"/>')
svg(U, 'c6-ma.svg',
    bubble(10, 18, 96, 46) +
    f'<rect x="22" y="32" width="52" height="7" rx="3.5" fill="{INK}"/>'
    f'<rect x="22" y="45" width="38" height="7" rx="3.5" fill="{LINE}"/>'
    f'<circle cx="126" cy="40" r="20" fill="{ORANGE}"/>'
    f'<text x="126" y="47" font-family="Noto Sans, Arial, sans-serif" font-size="19" font-weight="800" fill="{WHITE}" text-anchor="middle">吗?</text>')

# ============ unit 2 · greet-and-introduce ============
U = 'greet-and-introduce'
svg(U, 'x-hello.svg', person(46, BLUE) + person(114, GREEN, flip=True) + bubble(58, 6, 44, 30, fill=YELLOW, stroke=YELLOW))
svg(U, 'img-x-formal.svg', '')  # placeholder removed below
os.remove(os.path.join(ROOT, U, 'img', 'img-x-formal.svg'))
svg(U, 'x-formal.svg',
    f'<text x="80" y="52" font-family="Noto Sans SC, Noto Sans, sans-serif" font-size="46" font-weight="800" fill="{NAVY}" text-anchor="middle">您</text>'
    f'<path d="M80 92 c-10 -12 -22 -6 -18 4 c3 8 18 14 18 14 c0 0 15 -6 18 -14 c4 -10 -8 -16 -18 -4Z" fill="{ORANGE}"/>')
svg(U, 'x-tag.svg',
    f'<rect x="34" y="26" width="92" height="48" rx="8" fill="{WHITE}" stroke="{GREEN}" stroke-width="3"/>'
    f'<circle cx="46" cy="50" r="5" fill="none" stroke="{GREEN}" stroke-width="3"/>'
    f'<text x="92" y="57" font-family="Noto Sans SC, Noto Sans, sans-serif" font-size="21" font-weight="800" fill="{NAVY}" text-anchor="middle">我叫…</text>')
svg(U, 'x-handshake.svg',
    f'<path d="M6 46 h34 l22 14 q6 4 12 0 l10 -8" fill="none" stroke="{BLUE}" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M154 46 h-34 l-22 14 q-6 4 -12 0" fill="none" stroke="{GREEN}" stroke-width="9" stroke-linecap="round"/>'
    f'<rect x="62" y="48" width="36" height="20" rx="9" transform="rotate(-14 80 58)" fill="#F3D9D2" stroke="{NAVY}" stroke-width="2.5"/>'
    f'<path d="M80 22 c-7 -9 -16 -4 -13 3 c2 6 13 11 13 11 c0 0 11 -5 13 -11 c3 -7 -6 -12 -13 -3Z" fill="{ORANGE}"/>')
svg(U, 'x-wave.svg',
    f'<path d="M64 96 v-30 q0 -6 6 -6 t6 6 v-16 q0 -6 6 -6 t6 6 v-8 q0 -6 6 -6 t6 6 v10 q0 -6 6 -6 t6 6 v24 q0 18 -16 18Z" fill="#F3D9D2" stroke="{NAVY}" stroke-width="2.5"/>'
    + ''.join(f'<path d="M{m} {y} l{n} {-8 if n < 0 else 0}" stroke="{ORANGE}" stroke-width="3" stroke-linecap="round"/>' for m, y, n in [(46, 34, -10), (52, 20, -6), (122, 30, 10), (118, 16, 6)]))
svg(U, 'x-tea.svg',
    f'<path d="M40 40 h44 v22 q0 16 -22 16 t-22 -16Z" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'
    f'<path d="M84 44 h10 q10 0 10 9 t-10 9 h-8" fill="none" stroke="{NAVY}" stroke-width="3"/>'
    f'<path d="M52 26 q4 -6 0 -12 m12 12 q4 -6 0 -12" stroke="{LINE}" stroke-width="3" fill="none" stroke-linecap="round"/>'
    f'<text x="118" y="70" font-family="Noto Sans SC, Noto Sans, sans-serif" font-size="30" font-weight="800" fill="{BROWN}">请</text>')
svg(U, 'c1-hello.svg', person(42, BLUE) + person(118, GREEN, flip=True) + bubble(56, 4, 48, 30, fill=YELLOW, stroke=YELLOW))
svg(U, 'c2-how.svg',
    bubble(24, 16, 112, 52) +
    f'<path d="M52 52 L72 32" stroke="{GREEN}" stroke-width="6" stroke-linecap="round"/>'
    f'<circle cx="98" cy="42" r="10" fill="{ORANGE}"/>')
svg(U, 'c3-name.svg',
    f'<rect x="30" y="22" width="100" height="52" rx="8" fill="{WHITE}" stroke="{GREEN}" stroke-width="3"/>'
    f'<circle cx="44" cy="48" r="5" fill="none" stroke="{GREEN}" stroke-width="3"/>'
    f'<rect x="60" y="36" width="52" height="8" rx="4" fill="{INK}"/>'
    f'<rect x="60" y="52" width="36" height="7" rx="3.5" fill="{LINE}"/>')
svg(U, 'c4-ask.svg',
    bubble(28, 14, 104, 54) +
    f'<rect x="48" y="30" width="46" height="9" rx="4.5" fill="{LINE}"/>'
    f'<circle cx="112" cy="40" r="13" fill="{BLUE}"/>'
    f'<text x="112" y="46" font-family="Noto Sans, Arial, sans-serif" font-size="16" font-weight="800" fill="{WHITE}" text-anchor="middle">?</text>')
svg(U, 'c5-fine.svg',
    f'<circle cx="80" cy="52" r="34" fill="#F3F5F9" stroke="{LINE}" stroke-width="2"/>'
    f'<circle cx="68" cy="44" r="4" fill="{NAVY}"/><circle cx="92" cy="44" r="4" fill="{NAVY}"/>'
    f'<path d="M64 62 q16 14 32 0" stroke="{NAVY}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    f'<path d="M126 78 v-22 q0 -5 5 -5 t5 5 v-6 q0 -5 5 -5 t5 5 v18 q0 12 -11 12Z" fill="#F3D9D2" stroke="{NAVY}" stroke-width="2"/>')
svg(U, 'c6-meet.svg',
    f'<path d="M14 70 q22 -22 44 -8 l14 10" fill="none" stroke="{BLUE}" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M146 70 q-22 -22 -44 -8 l-10 7" fill="none" stroke="{GREEN}" stroke-width="9" stroke-linecap="round"/>'
    f'<rect x="58" y="52" width="44" height="22" rx="10" transform="rotate(-10 80 63)" fill="#F3D9D2" stroke="{NAVY}" stroke-width="2.5"/>'
    f'<path d="M80 18 c-8 -10 -18 -5 -15 4 c3 7 15 12 15 12 c0 0 12 -5 15 -12 c3 -9 -7 -14 -15 -4Z" fill="{ORANGE}"/>')
svg(U, 'c7-bye.svg', svg_wave := (
    f'<path d="M60 96 v-32 q0 -6 6 -6 t6 6 v-18 q0 -6 6 -6 t6 6 v-10 q0 -6 6 -6 t6 6 v12 q0 -6 6 -6 t6 6 v26 q0 18 -16 18Z" fill="#F3D9D2" stroke="{NAVY}" stroke-width="2.5"/>'
    + ''.join(f'<path d="M{m} {y} l{n} 0" stroke="{ORANGE}" stroke-width="3.5" stroke-linecap="round"/>' for m, y, n in [(42, 36, -12), (48, 22, -8), (126, 32, 12), (122, 18, 8)])))
svg(U, 'c8-please.svg',
    f'<path d="M30 36 h40 v20 q0 15 -20 15 t-20 -15Z" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'
    f'<path d="M70 40 h8 q9 0 9 8 t-9 8 h-6" fill="none" stroke="{NAVY}" stroke-width="3"/>'
    f'<path d="M40 24 q4 -6 0 -12 m11 12 q4 -6 0 -12" stroke="{LINE}" stroke-width="3" fill="none" stroke-linecap="round"/>'
    f'<text x="112" y="66" font-family="Noto Sans SC, Noto Sans, sans-serif" font-size="34" font-weight="800" fill="{BROWN}">请</text>')
svg(U, 'c9-thanks.svg',
    f'<path d="M70 84 q-16 -20 -14 -44 q1 -10 8 -10 q8 0 10 12 l4 20" fill="#F3D9D2" stroke="{NAVY}" stroke-width="2.5"/>'
    f'<path d="M90 84 q16 -20 14 -44 q-1 -10 -8 -10 q-8 0 -10 12 l-4 20" fill="#F3D9D2" stroke="{NAVY}" stroke-width="2.5"/>'
    f'<path d="M80 30 c-7 -9 -16 -4 -13 3 c2 6 13 11 13 11 c0 0 11 -5 13 -11 c3 -7 -6 -12 -13 -3Z" fill="{ORANGE}"/>')

# ============ unit 3 · numbers-survival ============
U = 'numbers-survival'
svg(U, 'x-count.svg',
    ''.join(f'<text x="{10 + i * 15.6}" y="58" font-family="Noto Sans SC, Noto Sans, sans-serif" font-size="24" '
            f'font-weight="800" fill="{NAVY if i % 2 == 0 else BLUE}">{c}</text>'
            for i, c in enumerate('一二三四五六七八九十')))
svg(U, 'x-ten1.svg',
    f'<rect x="10" y="30" width="46" height="40" rx="8" fill="{BLUE}"/>'
    f'<text x="33" y="57" font-family="Noto Sans SC, Noto Sans, sans-serif" font-size="22" font-weight="800" fill="{WHITE}" text-anchor="middle">十</text>'
    f'<text x="68" y="57" font-family="Arial" font-size="24" font-weight="800" fill="{INK}" text-anchor="middle">+</text>'
    f'<rect x="86" y="30" width="34" height="40" rx="8" fill="{GREEN}"/>'
    f'<text x="103" y="57" font-family="Noto Sans SC, Noto Sans, sans-serif" font-size="22" font-weight="800" fill="{WHITE}" text-anchor="middle">一</text>'
    f'<text x="140" y="57" font-family="Arial" font-size="22" font-weight="800" fill="{INK}" text-anchor="middle">=11</text>')
svg(U, 'x-twenty.svg',
    f'<rect x="12" y="30" width="40" height="40" rx="8" fill="{GREEN}"/>'
    f'<text x="32" y="57" font-family="Noto Sans SC, Noto Sans, sans-serif" font-size="22" font-weight="800" fill="{WHITE}" text-anchor="middle">二</text>'
    f'<rect x="60" y="30" width="40" height="40" rx="8" fill="{BLUE}"/>'
    f'<text x="80" y="57" font-family="Noto Sans SC, Noto Sans, sans-serif" font-size="22" font-weight="800" fill="{WHITE}" text-anchor="middle">十</text>'
    f'<text x="132" y="57" font-family="Arial" font-size="22" font-weight="800" fill="{INK}" text-anchor="middle">=20</text>')
svg(U, 'x-hand2.svg',
    f'<path d="M62 96 v-34 q0 -6 6 -6 t6 6 v-14 q0 -6 6 -6 t6 6 v28 q0 20 -16 20Z" fill="#F3D9D2" stroke="{NAVY}" stroke-width="2.5"/>'
    f'<text x="116" y="52" font-family="Noto Sans SC, Noto Sans, sans-serif" font-size="34" font-weight="800" fill="{BROWN}" text-anchor="middle">两</text>')
svg(U, 'x-coins.svg',
    f'<circle cx="46" cy="62" r="22" fill="{YELLOW}" stroke="{NAVY}" stroke-width="2.5"/>'
    f'<text x="46" y="70" font-family="Noto Sans SC, Noto Sans, sans-serif" font-size="18" font-weight="800" fill="{NAVY}" text-anchor="middle">块</text>'
    f'<rect x="82" y="34" width="64" height="38" rx="6" fill="#DDEBDD" stroke="{GREEN}" stroke-width="2.5"/>'
    f'<text x="114" y="59" font-family="Noto Sans SC, Noto Sans, sans-serif" font-size="18" font-weight="800" fill="{GREEN}" text-anchor="middle">元</text>')
svg(U, 'c1-nums.svg',
    ''.join(f'<rect x="{4 + (i % 5) * 32}" y="{6 if i < 5 else 52}" width="27" height="40" rx="6" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
            f'<text x="{17.5 + (i % 5) * 32}" y="{32 if i < 5 else 78}" font-family="Noto Sans SC, Noto Sans, sans-serif" '
            f'font-size="19" font-weight="800" fill="{NAVY}" text-anchor="middle">{c}</text>'
            for i, c in enumerate('一二三四五六七八九十')))
svg(U, 'c2-tag.svg',
    f'<path d="M40 14 h56 l30 30 -30 30 h-56 q-8 0 -8 -8 V22 q0 -8 8 -8Z" fill="{WHITE}" stroke="{ORANGE}" stroke-width="3"/>'
    f'<circle cx="44" cy="44" r="6" fill="none" stroke="{ORANGE}" stroke-width="3"/>'
    f'<text x="92" y="54" font-family="Noto Sans SC, Noto Sans, sans-serif" font-size="17" font-weight="800" fill="{NAVY}" text-anchor="middle">¥ ?</text>')
svg(U, 'c3-want.svg',
    f'<path d="M52 40 h44 v22 q0 16 -22 16 t-22 -16Z" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'
    f'<path d="M96 44 h8 q9 0 9 8 t-9 8 h-7" fill="none" stroke="{NAVY}" stroke-width="3"/>'
    f'<path d="M20 30 h24 m-5 -6 l6 6 l-6 6" stroke="{PURPLE}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    f'<text x="18" y="20" font-family="Noto Sans SC, Noto Sans, sans-serif" font-size="17" font-weight="800" fill="{PURPLE}">我要</text>')
svg(U, 'c4-toilet.svg',
    f'<rect x="52" y="8" width="56" height="84" rx="5" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'
    f'<circle cx="98" cy="52" r="4.5" fill="{NAVY}"/>'
    f'<rect x="60" y="18" width="40" height="22" rx="4" fill="{BLUE}"/>'
    f'<text x="80" y="34" font-family="Arial" font-size="14" font-weight="800" fill="{WHITE}" text-anchor="middle">WC</text>'
    f'<circle cx="126" cy="30" r="15" fill="{ORANGE}"/>'
    f'<text x="126" y="37" font-family="Arial" font-size="18" font-weight="800" fill="{WHITE}" text-anchor="middle">?</text>')
svg(U, 'c5-phone.svg',
    f'<rect x="56" y="4" width="48" height="92" rx="9" fill="{NAVY}"/>'
    f'<rect x="60" y="13" width="40" height="74" rx="3" fill="{WHITE}"/>'
    + ''.join(f'<rect x="{65 + (i % 2) * 20}" y="{20 + (i // 2) * 12}" width="14" height="7" rx="3.5" fill="{LINE if i > 3 else BLUE}"/>' for i in range(8))
    + f'<rect x="74" y="8" width="12" height="2.4" rx="1.2" fill="#3B4A6E"/>')
print('drawn all unit images')
