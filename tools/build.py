"""Static site generator for thermex.uz.

Usage:  python3 tools/build.py        (Python 3.8+, no dependencies)

Edit this file (texts, contacts, model list) or tools/data/*.json, run it, and
commit the regenerated HTML/JS together with the change. The generated files
carry a "do not edit by hand" comment; hand edits are lost on the next build.
"""
import json
import os
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA_DIR = os.path.join(HERE, 'data')
SITE = 'https://www.thermex.uz'   # must match the CNAME file (GitHub Pages redirects the other host here)
CATALOG_JS = ('/assets/js/catalog-data.js',)
# Warranty on the tank shown on the site, in months. Thermex quotes up to 84 for some
# series, but the warranty given in Uzbekistan is 5 years, so longer values are capped.
TANK_WARRANTY_CAP = 60
# Sales line (header, product enquiries, general forms)
PHONE = '+998 90 374-52-54'
PHONE_TEL = '+998903745254'
WA = 'https://wa.me/998903745254'
# Service centre line (repair, installation, warranty)
SVC = '+998 88 709-07-77'
SVC_TEL = '+998887090777'
SVC_WA = 'https://wa.me/998887090777'
TG = 'https://t.me/bobur_jq'
IG = 'https://www.instagram.com/sanneo.uz/'
FB = 'https://www.facebook.com/Sanneo.uz/'
EMAIL = 'info@thermex.uz'
ADDRESS = 'г. Ташкент, ул. Джами, 5'
PDF = '/files/thermex-Catalog1.pdf'
IMG = '/assets/img/'

ICONS = {
 'phone': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
 'pin': '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
 'clock': '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 'check': '<path d="M20 6 9 17l-5-5"/>',
 'arrow': '<path d="M5 12h14M12 5l7 7-7 7"/>',
 'arrow-ur': '<path d="M7 17 17 7M7 7h10v10"/>',
 'menu': '<path d="M4 6h16M4 12h16M4 18h16"/>',
 'x': '<path d="M18 6 6 18M6 6l12 12"/>',
 'shield': '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
 'wrench': '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
 'truck': '<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.62L18.3 9.38a1 1 0 0 0-.78-.38H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>',
 'award': '<circle cx="12" cy="8" r="6"/><path d="M15.48 12.89 17 22l-5-3-5 3 1.52-9.11"/>',
 'droplet': '<path d="M12 22a7 7 0 0 0 7-7c0-2-1-3.9-3-5.5s-3.5-4-4-6.5c-.5 2.5-2 4.9-4 6.5C6 11.1 5 13 5 15a7 7 0 0 0 7 7z"/>',
 'zap': '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
 'timer': '<path d="M10 2h4M12 14l3-3"/><circle cx="12" cy="14" r="8"/>',
 'box': '<path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5M12 22V12"/>',
 'thermo': '<path d="M14 4v10.54a4 4 0 1 1-4 0V4a2 2 0 0 1 4 0Z"/>',
 'users': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
 'home': '<path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
 'building': '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01M16 10h.01M16 14h.01M8 10h.01M8 14h.01"/>',
 'file-down': '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4M12 18v-6M9 15l3 3 3-3"/>',
 'file-check': '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4M9 15l2 2 4-4"/>',
 'headset': '<path d="M3 14h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a9 9 0 0 1 18 0v7a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3"/>',
 'tag': '<path d="M12.59 2.59A2 2 0 0 0 11.17 2H4a2 2 0 0 0-2 2v7.17a2 2 0 0 0 .59 1.42l8.7 8.7a2.43 2.43 0 0 0 3.42 0l6.58-6.58a2.43 2.43 0 0 0 0-3.42z"/><circle cx="7.5" cy="7.5" r="1"/>',
 'sliders': '<path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6"/>',
 'mail': '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 5L2 7"/>',
 'star': '<path d="m12 2 3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>',
 'globe': '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 4 10 15 15 0 0 1-4 10 15 15 0 0 1-4-10 15 15 0 0 1 4-10z"/>',
 'trees': '<path d="M10 10v.2A3 3 0 0 1 8.9 16H5a3 3 0 0 1-1-5.8V10a3 3 0 0 1 6 0Z"/><path d="M7 16v6M13 19v3"/><path d="M12 19h8.3a1 1 0 0 0 .7-1.7L18 14h.3a1 1 0 0 0 .7-1.7L16 9h.2a1 1 0 0 0 .8-1.7L13 3l-1.4 1.5"/>',
 'flame': '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.07-2.14-.22-4.05 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.15.43-2.29 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>',
 'layers': '<path d="m12 2 10 5-10 5L2 7l10-5z"/><path d="m2 17 10 5 10-5M2 12l10 5 10-5"/>',
 'play': '<path fill="currentColor" stroke="none" d="M6 4l14 8-14 8z"/>',
 'telegram': '<path fill="currentColor" stroke="none" d="M21.9 4.3 18.7 19.4c-.2 1-.9 1.3-1.8.8l-4.9-3.6-2.4 2.3c-.3.3-.5.5-1 .5l.3-5 9.1-8.2c.4-.4-.1-.6-.6-.2L6.2 13 1.4 11.5c-1-.3-1-1 .2-1.5L20.5 2.8c.9-.3 1.6.2 1.4 1.5z"/>',
 'instagram': '<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/>',
 'facebook': '<path fill="currentColor" stroke="none" d="M14 8h3V4h-3c-2.8 0-5 2.2-5 5v2H7v4h2v9h4v-9h3l1-4h-4V9c0-.6.4-1 1-1z"/>',
 'whatsapp': '<path fill="currentColor" stroke="none" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2.1 1-2.4c.3-.3.6-.3.8-.3h.6c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.3.5-.4.4c-.1.1-.3.3-.1.6.2.3.7 1.2 1.6 2 1.1 1 2 1.3 2.3 1.4.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.4z"/>',
}

def sprite():
    return ('<svg width="0" height="0" style="position:absolute" aria-hidden="true">' +
            ''.join(f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items()) + '</svg>')

def ic(name, cls='icon'):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'

NAV = [
    ('Каталог', '/catalog.html'),
    ('Водонагреватели', '/water-heaters.html'),
    ('Преимущества', '/advantages.html'),
    ('Сервис', '/service.html'),
    ('О компании', '/about.html'),
    ('Контакты', '/contacts.html'),
]

PRODUCTS = [
    # id, name, series, vol, power, heat, warranty, tags, image, new
    ('thermo-50v', 'Thermo 50 V', 'Thermo', 50, '2,5 кВт', '60 мин', 'бак 5 лет', '50', 'p-thermo-50v.webp', True),
    ('edisson-50v', 'Edisson ER 50 V', 'Edisson', 50, '1,5 кВт', 'IPX4', '220 В', '50', 'p-edisson-50v.webp', True),
    ('ers-80v', 'ERS 80 V Silverheat', 'Champion Silverheat', 80, '1,5 кВт', '170 мин', 'бак 5 лет', '80', 'p-ers-80v.webp', True),
    ('nobel-10u', 'Nobel 10 U', 'Nobel · под мойку', 10, '2 кВт', '16 мин', 'бак 5 лет', 'small', 'p-nobel-10u.webp', False),
    ('nobel-10o', 'Nobel 10 O', 'Nobel · над мойкой', 10, '2 кВт', '16 мин', 'бак 5 лет', 'small', 'p-nobel-10o.webp', False),
    ('nobel-15o', 'Nobel 15 O', 'Nobel · над мойкой', 15, '2 кВт', '28 мин', 'бак 5 лет', 'small', 'p-nobel-15o.webp', False),
]

def product_card(p):
    pid, name, series, vol, power, heat, war, tags, img, new = p
    second = ('timer', heat) if 'мин' in heat else ('shield', heat)
    third = ('award', war) if 'бак' in war else ('zap', war)
    return f'''
      <article class="product reveal" data-tags="b-thermex {vbucket(vol)}">
        <div class="product-media">
          <div class="tags">{'<span class="tag tag-new">New</span>' if new else ''}<span class="tag">{'Малолитражный' if vol <= 15 else 'Накопительный'}</span></div>
          <div class="product-vol">{vol}<small>литров</small></div>
          <img src="{IMG}{img}" alt="Водонагреватель Thermex {name}" loading="lazy" width="260" height="300">
        </div>
        <div class="product-body">
          <span class="product-series">{series}</span>
          <h3>Thermex {name}</h3>
          <ul class="specs-mini">
            <li>{ic('droplet')}{vol} л</li>
            <li>{ic('zap')}{power}</li>
            <li>{ic(second[0])}{second[1]}</li>
            <li>{ic(third[0])}{third[1]}</li>
          </ul>
          <div class="product-actions">
            <button type="button" class="btn btn-dark btn-sm" data-product="{pid}">Подробнее</button>
            <a class="btn btn-ghost btn-sm" href="{WA}?text={quote('Здравствуйте! Интересует Thermex ' + name + '. Подскажите цену.')}" target="_blank" rel="noopener">Узнать цену</a>
          </div>
        </div>
      </article>'''

from urllib.parse import quote

def products_grid(grid_id='products', filters=True):
    f = ''
    if filters:
        f = f'''<div class="filters" data-filters="{grid_id}" role="group" aria-label="Фильтр по объёму">
          <button type="button" class="chip is-active" data-filter="all" aria-pressed="true">Все модели</button>
          <button type="button" class="chip" data-filter="v-small" aria-pressed="false">10–15 л</button>
          <button type="button" class="chip" data-filter="v-50" aria-pressed="false">50 л</button>
          <button type="button" class="chip" data-filter="v-80" aria-pressed="false">80 л</button>
        </div>'''
    return f, f'<div class="products" id="{grid_id}">' + ''.join(product_card(p) for p in PRODUCTS) + '</div>'


def vbucket(v):
    return 'v-small' if v <= 15 else 'v-30' if v <= 30 else 'v-50' if v <= 50 else 'v-80' if v <= 80 else 'v-100'

BRANDS = {'thermex': 'Thermex', 'garanterm': 'Garanterm', 'etalon': 'Etalon'}
MOUNTS = {'V': 'вертикальный', 'H': 'горизонтальный', 'O': 'над мойкой', 'U': 'под мойку'}

# Full range from the price list (boilers excluded, prices never shown).
# (brand, model name, volume, mount V/H/O/U or None, made in China, kind, existing detailed id)
CATALOG = [
    ('thermex', 'Thermo 50 V', 50, 'V', False, None, 'thermo-50v'),
    ('thermex', 'Thermo 80 V', 80, 'V', False, None, None),
    ('thermex', 'Thermo 100', 100, None, False, None, None),
    ('thermex', 'Thermo 150', 150, None, False, None, None),
    ('thermex', 'Thermo ES 30', 30, None, False, None, None),
    ('thermex', 'Thermo ES 50', 50, None, False, None, None),
    ('thermex', 'Edisson ER 50 V', 50, 'V', False, None, 'edisson-50v'),
    ('thermex', 'Edisson ER 80 V', 80, 'V', False, None, None),
    ('thermex', 'ER 200', 200, None, False, 'floor', None),
    ('thermex', 'ER 300', 300, None, False, 'floor', None),
    ('thermex', 'ERS 50 V', 50, 'V', False, None, None),
    ('thermex', 'ERS 80 V Silverheat', 80, 'V', False, None, 'ers-80v'),
    ('thermex', 'ERS 80 H', 80, 'H', False, None, None),
    ('thermex', 'ERS 100 V', 100, 'V', False, None, None),
    ('thermex', 'ESS 30 V', 30, 'V', False, None, None),
    ('thermex', 'ESS 50 V', 50, 'V', False, None, None),
    ('thermex', 'ESS 80 V', 80, 'V', False, None, None),
    ('thermex', 'Titan 50 V', 50, 'V', False, None, None),
    ('thermex', 'Titan 80 V', 80, 'V', False, None, None),
    ('thermex', 'Titan 80 H', 80, 'H', False, None, None),
    ('thermex', 'Titan 100', 100, None, False, None, None),
    ('thermex', 'Titan 150 V', 150, 'V', False, None, None),
    ('thermex', 'Titan ESS 30 V', 30, 'V', False, None, None),
    ('thermex', 'Titan ESS 50 V', 50, 'V', False, None, None),
    ('thermex', 'Titan ESS 50 H', 50, 'H', False, None, None),
    ('thermex', 'Giro 50', 50, None, False, None, None),
    ('thermex', 'Giro 80', 80, None, False, None, None),
    ('thermex', 'Giro 100', 100, None, False, None, None),
    ('thermex', 'Nova 50', 50, None, False, None, None),
    ('thermex', 'Nova 100', 100, None, False, None, None),
    ('thermex', 'Nobel 10 O', 10, 'O', False, None, 'nobel-10o'),
    ('thermex', 'Nobel 10 U', 10, 'U', False, None, 'nobel-10u'),
    ('thermex', 'Nobel 15 O', 15, 'O', False, None, 'nobel-15o'),
    ('thermex', 'Nobel 15 U', 15, 'U', False, None, None),
    ('thermex', 'Combo 150 V L', 150, 'V', False, 'indirect', None),
    ('thermex', 'Combo 150 V R', 150, 'V', False, 'indirect', None),
    ('thermex', 'IF 80 Smart', 80, None, True, None, None),
    ('thermex', 'Neo 10 O', 10, 'O', True, None, None),
    ('thermex', 'Neo 15 O', 15, 'O', True, None, None),
    ('thermex', 'Zulu 10 O', 10, 'O', True, None, None),
    ('garanterm', 'ECO 80 V', 80, 'V', False, None, None),
    ('garanterm', 'Origin 50 V', 50, 'V', False, None, None),
    ('garanterm', 'Origin 80 V', 80, 'V', False, None, None),
    ('garanterm', 'Origin 80 H', 80, 'H', False, None, None),
    ('garanterm', 'Origin 100 V', 100, 'V', False, None, None),
    ('garanterm', 'Origin 150 V', 150, 'V', False, None, None),
    ('garanterm', 'Origin Slim 30 V', 30, 'V', False, None, None),
    ('garanterm', 'Origin Slim 50 V', 50, 'V', False, None, None),
    ('garanterm', 'Origin Slim 50 H', 50, 'H', False, None, None),
    ('garanterm', 'Origin Slim 80 V', 80, 'V', False, None, None),
    ('etalon', 'ER 50 V', 50, 'V', False, None, None),
    ('etalon', 'ER 80 V', 80, 'V', False, None, None),
    ('etalon', 'ER 80 H', 80, 'H', False, None, None),
    ('etalon', 'ER 100 V', 100, 'V', False, None, None),
]
DETAILED = {p[0]: p for p in PRODUCTS}

def slug(brand, name):
    import re
    return brand + '-' + re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

def placeholder(mount, vol, kind):
    if kind == 'floor':
        return 'ph-floor.svg'
    if mount == 'H':
        return 'ph-horizontal.svg'
    if vol <= 15:
        return 'ph-compact.svg'
    return 'ph-vertical.svg'


# Photos and specs fetched from thermex.ru (see tools/thermex_fetch.py in git history).
with open(os.path.join(DATA_DIR, 'thermex.json'), encoding='utf-8') as _f:
    FETCHED = json.load(_f)       # fetched from thermex.ru product pages
with open(os.path.join(DATA_DIR, 'featured.json'), encoding='utf-8') as _f:
    FEATURED = json.load(_f)      # the 6 models with hand-written specs and own photos
FETCHED.pop('thermex-ess-80-v', None)  # only an old ES 80 V page exists; not confirmed to be the same model
CARD_PHOTO = {'thermex-giro-50': 2}    # first photo shows the horizontal mounting variant

def cap_tank(months):
    return str(min(int(months), TANK_WARRANTY_CAP)) if months else months

def years(months):
    m = int(months)
    if m % 12:
        return f'{m} мес.'
    y = m // 12
    word = 'год' if y % 10 == 1 and y % 100 != 11 else 'года' if y % 10 in (2, 3, 4) and y % 100 not in (12, 13, 14) else 'лет'
    return f'{y} {word}'

def num(v):
    return v.replace('.', ',')

def curated_specs(specs):
    s = dict(specs)
    out = []
    def add(label, key, fmt=lambda v: v):
        if s.get(key):
            out.append([label, fmt(s[key])])
    add('Артикул', 'Артикул')
    add('Серия', 'Серия')
    add('Объём', 'Литраж, л', lambda v: v + ' л')
    power = s.get('Режимы мощности электрической, Вт') or s.get('Макс. мощность электрическая, Вт')
    if power:
        out.append(['Мощность', power.replace('/', ' / ') + ' Вт'])
    add('Мощность теплообменника', 'Мощность теплообменника, Вт', lambda v: v + ' Вт')
    add('Время нагрева (Δt 45°)', 'Время нагрева на ∆t 45° при макс. мощности, мин', lambda v: v + ' мин')
    add('Материал бака', 'Материал внутреннего бака')
    add('Нагревательный элемент', 'Материал нагревательного элемента')
    if s.get('Сухой ТЭН') == 'да':
        out.append(['Сухой ТЭН', 'да'])
    add('Форма', 'Форм-фактор', str.lower)
    add('Установка', 'Установка')
    add('Подводка', 'Подводка')
    add('Управление', 'Тип управления')
    add('Макс. температура', 'Макс. температура нагрева воды, °С', lambda v: v + ' °C')
    add('Макс. давление воды', 'Макс. давление воды, МПа', lambda v: num(v) + ' МПа')
    add('Класс защиты', 'Класс IP')
    h, w, d = s.get('Высота, мм'), s.get('Ширина, мм'), s.get('Глубина, мм')
    if h and w and d:
        out.append(['Размеры (В×Ш×Г)', f'{h} × {w} × {d} мм'])
    add('Вес', 'Вес, кг', lambda v: num(v) + ' кг')
    tank, prod = cap_tank(s.get('Гарантия на внутренний бак, мес')), s.get('Гарантия на изделие, мес')
    if tank or prod:
        parts = ([f'бак — {years(tank)}'] if tank else []) + ([f'изделие — {years(prod)}'] if prod else [])
        out.append(['Гарантия', ', '.join(parts)])
    add('Производство', 'Страна производитель', str.capitalize)
    return out

def fetched_photos(pid):
    info = FETCHED[pid]
    files = list(info['files'])
    first = CARD_PHOTO.get(pid, 1) - 1
    if 0 < first < len(files):
        files.insert(0, files.pop(first))
    return [f'{IMG}p/{f}' for f in files]

def catalog_data_js():
    data = dict(FEATURED)
    for brand, name, vol, mount, china, kind, detailed in CATALOG:
        pid = slug(brand, name)
        if detailed or pid not in FETCHED:
            continue
        info = FETCHED[pid]
        specs = curated_specs(info['specs'])
        data[pid] = {
            'title': f'{BRANDS[brand]} {name}',
            'label': info['title'],
            'volume': vol,
            'power': dict(specs).get('Мощность', ''),
            'desc': 'Характеристики по данным производителя (thermex.ru). Цену и наличие уточняйте у менеджера — ответим в течение 15 минут в рабочее время.',
            'images': fetched_photos(pid),
            'specs': specs,
        }
    return ('/* Generated by tools/build.py from tools/data/*.json — do not edit by hand. */\n'
            'window.THERMEX_CATALOG = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n')

def fetched_card(item):
    brand, name, vol, mount, china, kind, detailed = item
    pid = slug(brand, name)
    info = FETCHED[pid]
    s = dict(info['specs'])
    full = f'{BRANDS[brand]} {name}'
    country = s.get('Страна производитель', '').capitalize()
    is_cn = china or country == 'Китай'
    tag = 'Косвенного нагрева' if kind == 'indirect' else 'Малолитражный' if vol <= 15 else 'Накопительный'
    specs = [('droplet', f'{vol} л')]
    pw = s.get('Макс. мощность электрическая, Вт')
    if pw and pw.isdigit():
        specs.append(('zap', num(f'{int(pw) / 1000:g}') + ' кВт'))
    t = s.get('Время нагрева на ∆t 45° при макс. мощности, мин')
    if t:
        specs.append(('timer', f'{t} мин'))
    tank = cap_tank(s.get('Гарантия на внутренний бак, мес'))
    if tank:
        specs.append(('award', f'бак {years(tank)}'))
    wa_text = quote(f'Здравствуйте! Интересует водонагреватель {full}. Подскажите цену и наличие.')
    series = info['title'].replace('THERMEX ', '').replace('Edisson ', '')
    return f'''
      <article class="product reveal" data-tags="b-{brand} {vbucket(vol)}">
        <div class="product-media">
          <div class="tags"><span class="tag">{tag}</span>{'<span class="tag tag-cn">Китай</span>' if is_cn else ''}</div>
          <div class="product-vol">{vol}<small>литров</small></div>
          <img src="{fetched_photos(pid)[0]}" alt="Водонагреватель {full}" loading="lazy" width="260" height="300">
        </div>
        <div class="product-body">
          <span class="product-series">{series}</span>
          <h3>{full}</h3>
          <ul class="specs-mini">{''.join(spec_li(i, t) for i, t in specs)}</ul>
          <div class="product-actions">
            <button type="button" class="btn btn-dark btn-sm" data-product="{pid}">Подробнее</button>
            <a class="btn btn-ghost btn-sm" href="{WA}?text={wa_text}" target="_blank" rel="noopener">Узнать цену</a>
          </div>
        </div>
      </article>'''

def spec_li(icon, text):
    cls = ' class="full"' if 'запросу' in text else ''
    return f'<li{cls}>{ic(icon)}{text}</li>'

def catalog_card(item):
    brand, name, vol, mount, china, kind, detailed = item
    if detailed:
        return product_card(DETAILED[detailed])
    if slug(brand, name) in FETCHED:
        return fetched_card(item)
    bname = BRANDS[brand]
    full = f'{bname} {name}'
    pid = slug(brand, name)
    tag = 'Косвенного нагрева' if kind == 'indirect' else 'Малолитражный' if vol <= 15 else 'Накопительный'
    specs = [('droplet', f'{vol} л')]
    if mount:
        specs.append(('sliders', MOUNTS[mount]))
    if kind == 'indirect':
        specs.append(('flame', 'косвенный нагрев'))
    if china:
        specs.append(('globe', 'сделано в Китае'))
    specs.append(('headset', 'характеристики — по запросу'))
    attrs = f'data-name="{full}" data-brand="{bname}" data-vol="{vol}"'
    if mount:
        attrs += f' data-mount="{MOUNTS[mount]}"'
    if kind == 'indirect':
        attrs += ' data-kind="косвенного нагрева"'
    if china:
        attrs += ' data-origin="Китай"'
    wa_text = quote(f'Здравствуйте! Интересует водонагреватель {full}. Подскажите цену и наличие.')
    return f'''
      <article class="product reveal" data-tags="b-{brand} {vbucket(vol)}">
        <div class="product-media is-placeholder">
          <div class="tags"><span class="tag">{tag}</span>{'<span class="tag tag-cn">Китай</span>' if china else ''}</div>
          <div class="product-vol">{vol}<small>литров</small></div>
          <img src="{IMG}{placeholder(mount, vol, kind)}" alt="" loading="lazy" width="200" height="300">
          <span class="ph-note">Фото скоро появится</span>
        </div>
        <div class="product-body">
          <span class="product-series">{bname}</span>
          <h3>{full}</h3>
          <ul class="specs-mini">{''.join(spec_li(i, t) for i, t in specs)}</ul>
          <div class="product-actions">
            <button type="button" class="btn btn-dark btn-sm" data-product="{pid}" {attrs}>Подробнее</button>
            <a class="btn btn-ghost btn-sm" href="{WA}?text={wa_text}" target="_blank" rel="noopener">Узнать цену</a>
          </div>
        </div>
      </article>'''

def catalog_grid(grid_id='catalog-products'):
    def chip(val, label, count, active=False):
        return f'<button type="button" class="chip{" is-active" if active else ""}" data-filter="{val}" aria-pressed="{"true" if active else "false"}">{label} <span class="chip-count">{count}</span></button>'
    n = len(CATALOG)
    by_brand = {b: sum(1 for c in CATALOG if c[0] == b) for b in BRANDS}
    by_vol = {}
    for c in CATALOG:
        by_vol[vbucket(c[2])] = by_vol.get(vbucket(c[2]), 0) + 1
    vols = [('v-small', '10–15 л'), ('v-30', '30 л'), ('v-50', '50 л'), ('v-80', '80 л'), ('v-100', '100 л и больше')]
    filters = f'''
    <div class="filter-bar reveal">
      <div class="filters" data-filters="{grid_id}" role="group" aria-label="Бренд">
        {chip('all', 'Все бренды', n, True)}{''.join(chip('b-' + b, BRANDS[b], by_brand[b]) for b in BRANDS)}
      </div>
      <div class="filters" data-filters="{grid_id}" role="group" aria-label="Объём">
        {chip('all', 'Любой объём', n, True)}{''.join(chip(v, l, by_vol.get(v, 0)) for v, l in vols)}
      </div>
    </div>
    <p class="filter-empty" hidden>Нет моделей с такими параметрами — <a href="/contacts.html#request">напишите нам</a>, подберём под заказ.</p>'''
    return filters, f'<div class="products" id="{grid_id}">' + ''.join(catalog_card(c) for c in CATALOG) + '</div>'

def head(title, desc, path, og_image=IMG + 'og-cover.jpg', scripts=(), noindex=False):
    extra_scripts = ''.join(f'  <script src="{src}" defer></script>' + chr(10) for src in scripts)
    ld = {
        '@context': 'https://schema.org', '@type': 'LocalBusiness',
        'name': 'Thermex Uzbekistan — ООО «SAN-NEO»', 'url': SITE + '/',
        'logo': SITE + IMG + 'logo-thermex-uz.webp', 'image': SITE + og_image,
        'telephone': PHONE_TEL, 'email': EMAIL,
        'contactPoint': [
            {'@type': 'ContactPoint', 'telephone': PHONE_TEL, 'contactType': 'sales', 'areaServed': 'UZ', 'availableLanguage': ['ru', 'uz']},
            {'@type': 'ContactPoint', 'telephone': SVC_TEL, 'contactType': 'customer support', 'areaServed': 'UZ', 'availableLanguage': ['ru', 'uz']}],
        'address': {'@type': 'PostalAddress', 'streetAddress': 'ул. Джами, 5', 'addressLocality': 'Ташкент', 'addressCountry': 'UZ'},
        'openingHoursSpecification': [
            {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], 'opens': '09:00', 'closes': '18:00'}],
        'sameAs': [FB, IG, TG],
    }
    robots = '  <meta name="robots" content="noindex">' + chr(10) if noindex else ''
    return f'''<!DOCTYPE html>
<!-- Generated by tools/build.py. Edit the generator and run it; changes made here by hand are lost on the next build. -->
<html lang="ru" class="no-js">
<head>
  <meta charset="utf-8">
  <script>document.documentElement.className = 'js';</script>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
{robots}  <link rel="canonical" href="{SITE}{path}">
  <meta name="theme-color" content="#e30613">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="ru_RU">
  <meta property="og:site_name" content="Thermex Uzbekistan">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{SITE}{path}">
  <meta property="og:image" content="{SITE}{og_image}">
  <link rel="icon" type="image/png" href="/assets/img/favicon.png">
  <link rel="apple-touch-icon" href="/assets/img/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&amp;display=swap">
  <link rel="stylesheet" href="/assets/css/site.css">
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','GTM-5CR79S9Z');</script>
{extra_scripts}  <script src="/assets/js/site.js" defer></script>
</head>
<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5CR79S9Z" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
{sprite()}
'''

CUR = ' aria-current="page"'

def header(active):
    links = ''.join(f'<a href="{u}"{CUR if u == active else ""}>{t}</a>' for t, u in NAV)
    dlinks = ''.join(f'<a href="{u}"{CUR if u == active else ""}>{t}{ic("arrow")}</a>' for t, u in [('Главная', '/')] + NAV)
    return f'''<div class="topbar">
  <div class="container">
    <div class="topbar-info">
      <span>{ic('pin')}{ADDRESS}</span>
      <span>{ic('clock')}Пн–Пт 9:00–18:00, Сб–Вс выходной</span>
      <span>{ic('wrench')}Сервис:&nbsp;<a href="tel:{SVC_TEL}">{SVC}</a></span>
      <span>{ic('mail')}<a href="mailto:{EMAIL}">{EMAIL}</a></span>
    </div>
    <div class="topbar-social">
      <a href="{TG}" target="_blank" rel="noopener" aria-label="Telegram">{ic('telegram')}</a>
      <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{ic('instagram')}</a>
      <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{ic('facebook')}</a>
    </div>
  </div>
</div>
<header class="header">
  <div class="container">
    <a class="logo" href="/" aria-label="Thermex Узбекистан — на главную"><img src="{IMG}logo-thermex-uz.webp" alt="Thermex — официальный партнёр в Узбекистане" width="152" height="50"></a>
    <nav class="nav" aria-label="Основное меню">{links}</nav>
    <div class="header-cta">
      <a class="header-phone" href="tel:{PHONE_TEL}"><strong>{PHONE}</strong><small>Отдел продаж · WhatsApp / Telegram</small></a>
      <a class="btn btn-primary btn-sm" href="/contacts.html#request">Оставить заявку</a>
    </div>
    <button class="burger" type="button" data-open-drawer aria-label="Открыть меню" aria-controls="drawer">{ic('menu')}</button>
  </div>
</header>
<div class="drawer" id="drawer" aria-hidden="true">
  <div class="drawer-backdrop" data-close-drawer></div>
  <div class="drawer-panel" role="dialog" aria-modal="true" aria-label="Меню">
    <div class="drawer-head">
      <img src="{IMG}logo-thermex-uz.webp" alt="Thermex Узбекистан" width="128" height="42">
      <button class="burger" style="display:grid;margin:0" type="button" data-close-drawer data-autofocus aria-label="Закрыть меню">{ic('x')}</button>
    </div>
    <nav aria-label="Мобильное меню">{dlinks}</nav>
    <div class="drawer-contacts">
      <a class="btn btn-primary btn-block" href="tel:{PHONE_TEL}">{ic('phone')}Продажи: {PHONE}</a>
      <a class="btn btn-dark btn-block" href="tel:{SVC_TEL}">{ic('wrench')}Сервис: {SVC}</a>
      <a class="btn btn-ghost btn-block" href="{TG}" target="_blank" rel="noopener">{ic('telegram')}Написать в Telegram</a>
    </div>
  </div>
</div>
<main>
'''

def product_modal():
    return f'''
<div class="modal" id="product-modal" aria-hidden="true">
  <div class="modal-backdrop" data-close-modal></div>
  <div class="modal-dialog" role="dialog" aria-modal="true" aria-labelledby="modal-title">
    <button class="modal-close" type="button" data-close-modal data-autofocus aria-label="Закрыть">{ic('x')}</button>
    <div class="modal-gallery">
      <div class="modal-main"><img alt=""></div>
      <div class="thumbs"></div>
    </div>
    <div class="modal-info">
      <span class="product-series"></span>
      <h3 id="modal-title"></h3>
      <p class="desc"></p>
      <table class="spec-table"><tbody></tbody></table>
      <div class="modal-actions">
        <a class="btn btn-primary" data-wa href="{WA}" target="_blank" rel="noopener">{ic('whatsapp')}Узнать цену</a>
        <a class="btn btn-ghost" href="tel:{PHONE_TEL}">{ic('phone')}Позвонить</a>
      </div>
    </div>
  </div>
</div>'''

def cta_block(title='Поможем выбрать водонагреватель', text='Оставьте заявку — перезвоним в течение 15 минут в рабочее время, подберём модель, рассчитаем доставку и установку.', service=False):
    phone, tel = (SVC, SVC_TEL) if service else (PHONE, PHONE_TEL)
    return f'''
<section class="section" id="request">
  <div class="container">
    <div class="cta reveal">
      <div>
        <span class="eyebrow" style="color:#fff">Бесплатная консультация</span>
        <h2 class="h2">{title}</h2>
        <p class="lead">{text}</p>
        <div class="cta-contacts">
          <a href="tel:{tel}">{ic('phone')}{phone}</a>
          <a href="{TG}" target="_blank" rel="noopener">{ic('telegram')}Telegram</a>
          <a href="mailto:{EMAIL}">{ic('mail')}{EMAIL}</a>
        </div>
      </div>
      {lead_form(service=service)}
    </div>
  </div>
</section>'''

def lead_form(with_message=False, title='Оставить заявку', service=False):
    msg = '''
        <div class="field"><label for="lf-msg">Сообщение</label><textarea id="lf-msg" name="message" placeholder="Какая модель интересует, адрес доставки или установки"></textarea></div>''' if with_message else ''
    topic = '''
        <div class="field"><label for="lf-topic">Тема</label>
          <select id="lf-topic" name="topic">
            <option>Подбор и покупка водонагревателя</option>
            <option>Установка</option>
            <option>Гарантийный ремонт</option>
            <option>Постгарантийный ремонт / обслуживание</option>
            <option>Сотрудничество (оптовые поставки)</option>
          </select></div>''' if with_message else ''
    wa_attr = ' data-wa="998887090777"' if service else ''
    phone, tel = (SVC, SVC_TEL) if service else (PHONE, PHONE_TEL)
    return f'''<form class="form" data-lead{wa_attr} novalidate>
        <h3>{title}</h3>
        <p class="hint">Нажмите кнопку — откроется WhatsApp с готовым сообщением. Ответим в течение 15 минут в рабочее время.</p>
        <div class="field"><label for="lf-name">Имя</label><input id="lf-name" name="name" required autocomplete="name" placeholder="Ваше имя"></div>
        <div class="field"><label for="lf-phone">Телефон</label><input id="lf-phone" name="phone" type="tel" required autocomplete="tel" placeholder="+998 __ ___-__-__" pattern="[0-9+()\\s\\-]{{7,}}"></div>{topic}{msg}
        <div class="hp" aria-hidden="true"><label>Website<input name="website" tabindex="-1" autocomplete="off"></label></div>
        <label class="consent"><input type="checkbox" required checked> Согласен(на) на обработку персональных данных</label>
        <button class="btn btn-primary btn-block" type="submit" value="whatsapp">{ic('whatsapp')}Отправить в WhatsApp</button>
        <p class="form-wa" role="status">Отправьте сообщение в открывшемся WhatsApp — мы ответим в течение 15 минут в рабочее время.</p>
      </form>'''

def footer(service=False):
    cb_tel, cb_label = (SVC_TEL, 'Сервис') if service else (PHONE_TEL, 'Позвонить')
    return f'''</main>
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="footer-logo" href="/"><img src="{IMG}logo-thermex-uz.webp" alt="Thermex Узбекистан" width="134" height="44" loading="lazy"></a>
        <p>ООО «SAN-NEO» — официальный партнёр Thermex и дистрибьютор брендов Etalon и Garanterm в Узбекистане.</p>
        <div class="footer-social">
          <a href="{TG}" target="_blank" rel="noopener" aria-label="Telegram">{ic('telegram')}</a>
          <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{ic('instagram')}</a>
          <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{ic('facebook')}</a>
        </div>
      </div>
      <div>
        <h4>Навигация</h4>
        <ul>{''.join(f'<li><a href="{u}">{t}</a></li>' for t, u in [('Главная', '/')] + NAV)}</ul>
      </div>
      <div>
        <h4>Покупателям</h4>
        <ul>
          <li><a href="{PDF}" target="_blank" rel="noopener">Каталог PDF</a></li>
          <li><a href="/water-heaters.html#picker">Подбор объёма</a></li>
          <li><a href="/service.html">Гарантия и ремонт</a></li>
          <li><a href="/advantages.html#how">Как устроен водонагреватель</a></li>
        </ul>
      </div>
      <div>
        <h4>Контакты</h4>
        <ul>
          <li><small>Отдел продаж</small><br><a class="phone" href="tel:{PHONE_TEL}">{PHONE}</a></li>
          <li><small>Сервисный центр</small><br><a class="phone" href="tel:{SVC_TEL}">{SVC}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{ADDRESS}</li>
          <li>Пн–Пт 9:00–18:00, Сб–Вс выходной</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> ООО «SAN-NEO». Все права защищены. ИНН 305894063 · ОКЭД 46190</span>
      <span>Информация на сайте не является публичной офертой.</span>
    </div>
  </div>
</footer>
<div class="callbar">
  <a class="btn btn-primary" href="tel:{cb_tel}">{ic('phone')}{cb_label}</a>
  <a class="btn btn-dark" href="{TG}" target="_blank" rel="noopener">{ic('telegram')}Telegram</a>
</div>
'''

def page_hero(crumb, title, lead, extra=''):
    return f'''
<section class="page-hero">
  <div class="container">
    <nav class="crumbs" aria-label="Хлебные крошки"><a href="/">Главная</a><span>/</span><span>{crumb}</span></nav>
    <h1>{title}</h1>
    <p class="lead">{lead}</p>{extra}
  </div>
</section>'''

def picker():
    people = ''.join(f'<button type="button" value="{n}" class="{"is-active" if n == 2 else ""}" aria-pressed="{"true" if n == 2 else "false"}">{str(n) + ("+" if n == 6 else "")}</button>' for n in range(1, 7))
    return f'''
<section class="section" id="picker">
  <div class="container">
    <div class="picker reveal">
      <div class="picker-form">
        <span class="eyebrow">Калькулятор</span>
        <h2 class="h2">Подберите объём за 10 секунд</h2>
        <p>Рекомендации основаны на количестве людей и точках водоразбора: мойка, душ, ванна.</p>
        <span class="picker-label" id="pl-people">Сколько человек пользуются горячей водой?</span>
        <div class="seg" data-people role="group" aria-labelledby="pl-people">{people}</div>
        <span class="picker-label" id="pl-use">Для чего нужна горячая вода?</span>
        <div class="seg seg-text" data-use role="group" aria-labelledby="pl-use">
          <button type="button" value="full" class="is-active" aria-pressed="true">Душ, ванна и кухня</button>
          <button type="button" value="kitchen" aria-pressed="false">Только мойка / раковина</button>
        </div>
      </div>
      <div class="picker-result" aria-live="polite">
        <span class="label">Рекомендуемый объём</span>
        <div class="picker-big"><span data-rec>50</span><small>литров</small></div>
        <span class="picker-min">Минимально допустимый — <b data-min>30</b> л</span>
        <div class="picker-rec">
          <img src="{IMG}p-thermo-50v.webp" alt="" width="64" height="84">
          <div><strong>Thermex Thermo 50 V</strong><span data-note></span></div>
          <button type="button" class="btn btn-white btn-sm" data-product-link data-product="thermo-50v">Смотреть</button>
        </div>
      </div>
    </div>
  </div>
</section>'''

def video(yid, cover, label):
    return f'''<div class="video reveal" data-youtube="{yid}">
      <img src="{IMG}{cover}" alt="" loading="lazy" width="1400" height="933">
      <button class="video-play" type="button" aria-label="{label}"><span>{ic('play')}</span></button>
    </div>'''

def brands():
    return f'''
<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal">
      <div><span class="eyebrow">Наш статус</span><h2 class="h2">Официальный партнёр трёх брендов</h2>
      <p>Статус подтверждает соответствие требованиям производителей, стандартам качества и условиям гарантийного обслуживания.</p></div>
    </div>
    <div class="brands">
      <div class="brand reveal"><div class="brand-logo"><img src="{IMG}brand-thermex.webp" alt="Thermex" loading="lazy"></div><span class="role">Официальный партнёр в Узбекистане</span><p>Водонагреватели и отопительное оборудование — более 75 лет опыта и собственное производство.</p></div>
      <div class="brand reveal"><div class="brand-logo is-square"><img src="{IMG}brand-etalon.webp" alt="Etalon" loading="lazy"></div><span class="role">Официальный дистрибьютор</span><p>Оборудование Etalon с официальной гарантией и сервисной поддержкой.</p></div>
      <div class="brand reveal"><div class="brand-logo"><img src="{IMG}brand-garanterm.webp" alt="Garanterm" loading="lazy"></div><span class="role">Официальный дистрибьютор</span><p>Водонагреватели Garanterm — оригинальная продукция и комплектующие.</p></div>
    </div>
  </div>
</section>'''

WHY = [
    ('award', 'Официальный партнёр Thermex', 'Работаем напрямую с производителем — только оригинальная продукция.'),
    ('file-check', 'Сертифицированная продукция', 'Оригинальные комплектующие и документы на каждое изделие.'),
    ('shield', 'Гарантия до 5 лет на бак', 'Гарантийное и постгарантийное обслуживание в Узбекистане.'),
    ('wrench', 'Собственный сервисный центр', 'Опытные специалисты, установка и ремонт в Ташкенте и регионах.'),
    ('sliders', 'Профессиональный подбор', 'Подберём модель под ваш дом, семью и точки водоразбора.'),
    ('tag', 'Честные цены', 'Прозрачные условия сотрудничества для частных клиентов и организаций.'),
]

def features(items, cls='features'):
    return f'<div class="{cls}">' + ''.join(
        f'<div class="feature reveal"><div class="ic">{ic(i)}</div><h3>{t}</h3>' + (f'<p>{d}</p>' if d else '') + '</div>'
        for i, t, d in items) + '</div>'

def write(name, html):
    with open(os.path.join(ROOT, name), 'w', encoding='utf-8') as f:
        f.write(html)

# ------------------------------------------------------------------ Home
def home():
    f, grid = products_grid('home-products')
    cats = [
        ('Квартира', 'Стабильная горячая вода для семьи', '50–80 л', 'p-thermo-50v.webp', 'building'),
        ('Частный дом', 'Больше точек водоразбора — больше объём', '80–150 л', 'p-ers-80v.webp', 'home'),
        ('Дача', 'Там, где нет центрального ГВС', '30–50 л', 'p-edisson-50v.webp', 'trees'),
        ('Кухня и офис', 'Компактно — над или под мойку', '10–15 л', 'p-nobel-15o.webp', 'droplet'),
    ]
    cat_html = ''.join(f'''
      <a class="cat reveal" href="/catalog.html">
        <span class="arrow">{ic('arrow-ur')}</span>
        <h3>{t}</h3><p>{d}</p><span class="vol">{v}</span>
        <img src="{IMG}{img}" alt="" loading="lazy">
      </a>''' for t, d, v, img, _ in cats)
    body = f'''
<section class="hero">
  <div class="container">
    <div>
      <span class="badge"><b>{ic('check')}</b>Официальный партнёр Thermex в Узбекистане</span>
      <h1>Водонагреватели <span>Thermex</span> с гарантией и сервисом</h1>
      <p class="lead">Электрические накопительные водонагреватели для квартиры, дома и дачи. Подбор модели, доставка по Узбекистану, установка и официальное гарантийное обслуживание.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="/catalog.html">Смотреть каталог{ic('arrow')}</a>
        <a class="btn btn-ghost" href="/water-heaters.html#picker">Подобрать объём</a>
      </div>
      <ul class="hero-points">
        <li>{ic('shield')}Гарантия до 5 лет</li>
        <li>{ic('truck')}Доставка по Узбекистану</li>
        <li>{ic('wrench')}Установка и сервис</li>
      </ul>
    </div>
    <div class="hero-visual" aria-hidden="true">
      <img class="hv-left" src="{IMG}p-thermo-50v.webp" alt="" width="180" height="330">
      <img class="hv-main" src="{IMG}p-ers-80v.webp" alt="" width="290" height="470" fetchpriority="high">
      <img class="hv-right" src="{IMG}p-nobel-15o.webp" alt="" width="120" height="210">
      <div class="hero-card hc-1"><span class="ic">{ic('award')}</span><span><strong>75+ лет</strong>опыта Thermex</span></div>
      <div class="hero-card hc-2"><span class="ic">{ic('headset')}</span><span><strong>15 минут</strong>ответ на заявку</span></div>
    </div>
  </div>
</section>

<div class="container">
  <div class="stats reveal">
    <div class="stat"><strong>75<small>+</small></strong><span>лет опыта бренда Thermex</span></div>
    <div class="stat"><strong>5 <small>лет</small></strong><span>гарантия на внутренний бак</span></div>
    <div class="stat"><strong>15 <small>мин</small></strong><span>ответ на заявку в рабочее время</span></div>
    <div class="stat"><strong>3</strong><span>бренда: Thermex, Etalon, Garanterm</span></div>
  </div>
</div>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <div><span class="eyebrow">Выбор по задаче</span><h2 class="h2">Для какого помещения?</h2></div>
      <a class="btn btn-ghost" href="/water-heaters.html">Как выбрать{ic('arrow')}</a>
    </div>
    <div class="cats">{cat_html}</div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal">
      <div><span class="eyebrow">Модели в наличии</span><h2 class="h2">Популярные водонагреватели</h2></div>
      {f}
    </div>
    {grid}
    <div class="more-row reveal"><a class="btn btn-dark" href="/catalog.html">Весь каталог — {len(CATALOG)} моделей{ic('arrow')}</a></div>
  </div>
</section>

{picker()}

<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal">
      <div><span class="eyebrow">Почему нам доверяют</span><h2 class="h2">Покупайте у официального партнёра</h2>
      <p>ООО «SAN-NEO» обеспечивает поставку оборудования, сервисное обслуживание и гарантийную поддержку для частных клиентов и организаций.</p></div>
      <a class="btn btn-ghost" href="/about.html">О компании{ic('arrow')}</a>
    </div>
    {features(WHY)}
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="split-media reveal">
      <img src="{IMG}service-install.webp" alt="Мастер устанавливает водонагреватель Thermex" loading="lazy" width="1400" height="933">
      <div class="float"><span class="ic" style="display:grid;place-items:center;width:42px;height:42px;border-radius:12px;background:var(--red-50);color:var(--red)">{ic('shield')}</span><span><strong>2 года</strong>гарантия на монтаж</span></div>
    </div>
    <div class="reveal">
      <span class="eyebrow">Сервис Thermex</span>
      <h2 class="h2">Установка, ремонт и гарантийное обслуживание</h2>
      <ul class="checklist">
        <li><span class="tick">{ic('check')}</span><span>Бесплатное гарантийное обслуживание</span></li>
        <li><span class="tick">{ic('check')}</span><span>Быстрый монтаж в Ташкенте и регионах</span></li>
        <li><span class="tick">{ic('check')}</span><span>Постгарантийный ремонт и замена комплектующих</span></li>
        <li><span class="tick">{ic('check')}</span><span>Только оригинальные запчасти Thermex</span></li>
      </ul>
      <div class="hero-actions" style="margin-top:0">
        <a class="btn btn-primary" href="/service.html">Подробнее о сервисе{ic('arrow')}</a>
        <a class="btn btn-ghost" href="tel:{SVC_TEL}">{ic('phone')}Вызвать мастера</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal">
      <div><span class="eyebrow">Видеоинструкция</span><h2 class="h2">Как пользоваться водонагревателем Thermex</h2></div>
    </div>
    {video('QYPt5FqqHvM', 'video-cover.webp', 'Смотреть видеоинструкцию')}
  </div>
</section>

{brands()}
{cta_block()}
{product_modal()}
'''
    write('index.html', head('Водонагреватели Thermex в Узбекистане — официальный партнёр', 'Официальный партнёр Thermex в Узбекистане. Электрические водонагреватели для квартиры, дома и дачи. Гарантия до 5 лет, сервисный центр, доставка по Ташкенту и Узбекистану.', '/', scripts=CATALOG_JS) + header('/') + body + footer() + '</body>\n</html>\n')

# ------------------------------------------------------------------ Catalog
def catalog():
    f, grid = catalog_grid('catalog-products')
    extra = f'''
    <div class="hero-actions">
      <a class="btn btn-primary" href="{PDF}" target="_blank" rel="noopener">{ic('file-down')}Скачать каталог PDF</a>
      <a class="btn btn-ghost" href="/water-heaters.html#picker">Подобрать объём</a>
    </div>'''
    body = page_hero('Каталог', 'Каталог водонагревателей Thermex, Garanterm и Etalon', f'{len(CATALOG)} моделей от официального партнёра в Узбекистане. Выберите бренд и объём, нажмите «Подробнее» — и узнайте цену у менеджера.', extra) + f'''
<section class="section">
  <div class="container">
    <div class="section-head reveal" style="margin-bottom:24px">
      <div><span class="eyebrow">Весь модельный ряд</span><h2 class="h2">Выберите водонагреватель</h2></div>
    </div>
    {f}
    {grid}
  </div>
</section>
<section class="section-sm section-alt">
  <div class="container">
    {features([
        ('truck', 'Доставка по Узбекистану', 'Привезём водонагреватель в Ташкент и регионы.'),
        ('box', 'Полная комплектация', 'Монтажные крепления, инструкция и гарантийный талон.'),
        ('shield', 'Официальная гарантия', 'До 5 лет на внутренний бак, в зависимости от модели.'),
    ])}
  </div>
</section>
{cta_block('Не нашли нужную модель?', 'В каталоге Thermex более сотни моделей. Напишите нам — привезём нужный водонагреватель под заказ.')}
{product_modal()}
'''
    write('catalog.html', head('Каталог водонагревателей Thermex, Garanterm, Etalon — Ташкент', 'Каталог водонагревателей Thermex, Garanterm и Etalon в Узбекистане: Thermo, Edisson, ERS, ESS, Titan, Giro, Nova, Nobel, Origin и другие. Цены по запросу, доставка и установка.', '/catalog.html', scripts=CATALOG_JS) + header('/catalog.html') + body + footer() + '</body>\n</html>\n')

# ------------------------------------------------------------------ Water heaters (how to choose)
def heaters():
    f, grid = products_grid('wh-products')
    uses = [
        ('trees', 'Для дач и загородных участков', 'Идеальное решение там, где нет централизованного горячего водоснабжения. Электрические накопительные водонагреватели Thermex обеспечивают комфорт в любое время года.'),
        ('home', 'Для квартир и частных домов', 'Стабильная подача горячей воды для всей семьи. Надёжные и экономичные решения от официального партнёра Thermex.'),
        ('building', 'Для новостроек', 'Накопительные водонагреватели для новых жилых комплексов, коттеджей и таунхаусов — оптимальный выбор для современных инженерных систем.'),
    ]
    body = page_hero('Водонагреватели', 'Водонагреватели Thermex в Узбекистане', 'Электрический накопительный водонагреватель нагревает воду и автоматически поддерживает температуру. Постепенный нагрев снижает нагрузку на электросеть и позволяет подключать прибор к стандартной розетке.') + f'''
<section class="section">
  <div class="container split">
    <div class="split-media reveal"><img src="{IMG}homes.webp" alt="Дача, частный дом и новостройка" loading="lazy" width="1400" height="933"></div>
    <div class="reveal">
      <span class="eyebrow">Где применяются</span>
      <h2 class="h2">Решения для любого типа жилья</h2>
      <div class="anatomy-list" style="margin-top:28px">
        {''.join(f'<li style="list-style:none"><b style="background:var(--red)">{ic(i)}</b><div><strong>{t}</strong><span>{d}</span></div></li>' for i, t, d in uses)}
      </div>
    </div>
  </div>
</section>
{picker()}
<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal">
      <div><span class="eyebrow">Как выбрать</span><h2 class="h2">На что обратить внимание</h2>
      <p>При выборе модели важно учитывать объём бака и количество пользователей. Мы поможем с подбором бесплатно.</p></div>
    </div>
    {features([
        ('droplet', 'Объём бака', '10–15 л — для мойки; 30–50 л — для 1–2 человек; 80–150 л — для семьи и дома.'),
        ('zap', 'Мощность', '1,5–2,5 кВт — подключение к обычной розетке 220 В без отдельной линии.'),
        ('layers', 'Покрытие бака', 'Биостеклофарфор или нержавеющая сталь — защита от коррозии на годы.'),
        ('flame', 'Тип ТЭНа', 'Медный, нержавеющий или Silverheat с серебряным покрытием против накипи.'),
        ('sliders', 'Монтаж', 'Вертикальный, горизонтальный, над мойкой (O) или под мойку (U).'),
        ('shield', 'Гарантия', 'Проверяйте срок гарантии на бак — у Thermex до 5 лет.'),
    ])}
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <div><span class="eyebrow">Модельный ряд</span><h2 class="h2">Популярные модели Thermex</h2></div>
      {f}
    </div>
    {grid}
    <div class="more-row reveal"><a class="btn btn-dark" href="/catalog.html">Весь каталог — {len(CATALOG)} моделей{ic('arrow')}</a></div>
  </div>
</section>
{cta_block()}
{product_modal()}
'''
    write('water-heaters.html', head('Как выбрать водонагреватель Thermex — квартира, дом, дача', 'Водонагреватели Thermex для квартир, частных домов, дач и новостроек в Узбекистане. Калькулятор объёма, советы по выбору, модели в наличии.', '/water-heaters.html', scripts=CATALOG_JS) + header('/water-heaters.html') + body + footer() + '</body>\n</html>\n')

# ------------------------------------------------------------------ Advantages
def advantages():
    ten = [
        ('shield', '5 лет гарантии на бак', ''), ('globe', 'Итальянские технологии', ''),
        ('wrench', 'Гарантийный ремонт', ''), ('headset', 'Специализированный сервисный центр', ''),
        ('truck', 'Доставка по Узбекистану', ''), ('tag', 'Выгодные цены', ''),
        ('file-check', 'Лицензированная компания', ''), ('timer', 'Быстрая и простая установка', ''),
        ('star', 'Надёжное качество', ''), ('box', 'Аксессуары и запчасти', ''),
    ]
    parts = [
        ('Термометр', 'Внешний индикатор нагрева — видно температуру воды.'),
        ('Прочный корпус', 'Надёжный корпус защищает бак и теплоизоляцию.'),
        ('Биостеклофарфор', 'Внутреннее покрытие бака защищает от коррозии.'),
        ('Магниевый анод', 'Мощный анод продлевает срок службы бака.'),
        ('Теплоизоляция', 'Пенополиуретан высокой плотности снижает затраты на электроэнергию.'),
        ('Забор воды из нержавеющей стали', 'Чистая горячая вода без привкуса металла.'),
        ('Термостат с двойной защитой', 'Автоматически отключает прибор при перегреве.'),
    ]
    body = page_hero('Преимущества', 'Преимущества водонагревателей Thermex', 'Официальная гарантия, надёжность, энергоэффективность, сервисный центр и профессиональная установка. Thermex — проверенное качество для дома и квартиры.') + f'''
<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <div><span class="eyebrow">10 причин</span><h2 class="h2">Почему выбирают Thermex</h2></div>
    </div>
    {features(ten, 'features features-5')}
  </div>
</section>
<section class="section section-alt" id="how">
  <div class="container">
    <div class="section-head reveal">
      <div><span class="eyebrow">Внутри</span><h2 class="h2">Как устроен водонагреватель Thermex</h2></div>
    </div>
    <div class="anatomy">
      <div class="figure reveal"><img src="{IMG}tank-structure.webp" alt="Устройство водонагревателя Thermex в разрезе" loading="lazy" width="1400" height="876"></div>
      <ol class="anatomy-list reveal">
        {''.join(f'<li><b>{n}</b><div><strong>{t}</strong><span>{d}</span></div></li>' for n, (t, d) in enumerate(parts, 1))}
      </ol>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <div><span class="eyebrow">Видео</span><h2 class="h2">Устройство водонагревателя на видео</h2></div>
    </div>
    {video('YSIiaWQRmUA', 'choose.webp', 'Смотреть видео об устройстве водонагревателя')}
  </div>
</section>
{cta_block()}
'''
    write('advantages.html', head('Преимущества водонагревателей Thermex в Узбекистане', 'Преимущества водонагревателей Thermex в Узбекистане: официальная гарантия, надёжность, энергоэффективность, сервисный центр и профессиональная установка.', '/advantages.html') + header('/advantages.html') + body + footer() + '</body>\n</html>\n')

# ------------------------------------------------------------------ Service
def service():
    services = [
        ('wrench', 'Установка и подключение', 'Монтаж водонагревателя с гарантией 2 года на установочные работы.'),
        ('shield', 'Гарантийный ремонт', 'Бесплатное гарантийное обслуживание в официальном сервисе Thermex.'),
        ('sliders', 'Постгарантийный ремонт', 'Диагностика и ремонт водонагревателей после окончания гарантии.'),
        ('droplet', 'Техническое обслуживание', 'Чистка бака от накипи, проверка анода и ТЭНа.'),
        ('box', 'Оригинальные запчасти', 'ТЭНы, аноды, термостаты и комплектующие Thermex.'),
        ('headset', 'Консультация', 'Поможем разобраться с настройками и эксплуатацией прибора.'),
    ]
    steps = [
        ('Заявка', 'Позвоните или напишите в Telegram — ответим в течение 15 минут.'),
        ('Диагностика', 'Мастер определит причину неисправности и согласует стоимость.'),
        ('Ремонт или установка', 'Работаем с оригинальными комплектующими Thermex.'),
        ('Гарантия', 'Выдаём гарантию на выполненные работы.'),
    ]
    extra = f'''
    <div class="hero-actions">
      <a class="btn btn-primary" href="tel:{SVC_TEL}">{ic('phone')}Вызвать мастера</a>
      <a class="btn btn-ghost" href="#request">Оставить заявку</a>
    </div>'''
    body = page_hero('Сервис', 'Сервис и ремонт водонагревателей Thermex', 'Официальный сервис Thermex в Узбекистане: гарантийный и постгарантийный ремонт, установка и техническое обслуживание оборудования.', extra) + f'''
<section class="section">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow">Услуги</span><h2 class="h2">Что мы делаем</h2></div></div>
    {features(services)}
  </div>
</section>
<section class="section section-alt">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Гарантия</span>
      <h2 class="h2">Гарантийное и постгарантийное обслуживание</h2>
      <p class="lead" style="margin-top:18px">Водонагреватели Thermex — надёжная техника, требующая профессионального подхода к установке и обслуживанию. Правильный монтаж и регулярное обслуживание продлевают срок службы прибора на годы.</p>
      <ul class="checklist">
        <li><span class="tick">{ic('check')}</span><span>Официальный сервис Thermex в Узбекистане</span></li>
        <li><span class="tick">{ic('check')}</span><span>Опытные сертифицированные мастера</span></li>
        <li><span class="tick">{ic('check')}</span><span>Гарантия 2 года на установочные работы</span></li>
      </ul>
    </div>
    <div class="split-media reveal"><img src="{IMG}service-hands.webp" alt="Подключение водонагревателя" loading="lazy" width="1000" height="1000" style="aspect-ratio:4/3"></div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow">Как мы работаем</span><h2 class="h2">4 простых шага</h2></div></div>
    <div class="steps">{''.join(f'<div class="step reveal"><h3>{t}</h3><p>{d}</p></div>' for t, d in steps)}</div>
  </div>
</section>
{cta_block('Нужен ремонт или установка?', 'Опишите проблему — мастер свяжется с вами в течение 15 минут в рабочее время.', service=True)}
'''
    write('service.html', head('Сервис и ремонт водонагревателей Thermex в Узбекистане', 'Официальный сервис Thermex в Ташкенте: установка, гарантийный и постгарантийный ремонт, обслуживание водонагревателей, оригинальные запчасти.', '/service.html') + header('/service.html') + body + footer(service=True) + '</body>\n</html>\n')

# ------------------------------------------------------------------ About
def about():
    body = page_hero('О компании', 'О компании Thermex в Узбекистане', 'Thermex — один из ведущих производителей водонагревательного и отопительного оборудования, известный высоким качеством, надёжностью и современными технологиями.') + f'''
<section class="section">
  <div class="container split">
    <div class="split-media reveal"><img src="{IMG}team.webp" alt="Команда SAN-NEO — официальный партнёр Thermex" loading="lazy" width="1400" height="933"></div>
    <div class="reveal">
      <span class="eyebrow">Кто мы</span>
      <h2 class="h2">ООО «SAN-NEO»</h2>
      <p class="lead" style="margin-top:18px">Официальный дистрибьютор отопительного и водонагревательного оборудования в Узбекистане. Мы представляем продукцию Thermex, Etalon и Garanterm и обеспечиваем комплексный подход — от подбора оборудования до установки и сервисного обслуживания.</p>
      <p style="margin-top:16px;color:var(--muted)">Официальный статус позволяет нам предлагать клиентам оригинальную продукцию, профессиональный сервис, гарантийную поддержку и консультации на всех этапах эксплуатации оборудования.</p>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow">Почему нам доверяют</span><h2 class="h2">Наши принципы</h2></div></div>
    {features(WHY)}
  </div>
</section>
{brands()}
<section class="section">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow">Реквизиты</span><h2 class="h2">Юридическая информация</h2></div></div>
    <div class="req reveal">
      <div><small>Наименование</small><strong>ООО «SAN-NEO»</strong></div>
      <div><small>ИНН</small><strong>305894063</strong></div>
      <div><small>ОКЭД</small><strong>46190</strong></div>
      <div><small>Юридический адрес</small><strong>Fidoiylar MFY, Maxtumquli ko'chasi, 112-uy</strong></div>
      <div><small>Офис и склад</small><strong>{ADDRESS}</strong></div>
      <div><small>E-mail</small><strong><a href="mailto:{EMAIL}">{EMAIL}</a></strong></div>
    </div>
  </div>
</section>
{cta_block('Станьте нашим партнёром', 'Работаем с частными клиентами, строительными компаниями и магазинами. Предложим условия оптовых поставок.')}
'''
    write('about.html', head('О компании — официальный партнёр Thermex в Узбекистане', 'ООО «SAN-NEO» — официальный партнёр Thermex и дистрибьютор Etalon и Garanterm в Узбекистане. Поставка, установка, гарантийное и сервисное обслуживание.', '/about.html', IMG + 'og-cover.jpg') + header('/about.html') + body + footer() + '</body>\n</html>\n')

# ------------------------------------------------------------------ Contacts
def contacts():
    body = page_hero('Контакты', 'Свяжитесь с нами', 'Оставьте заявку — мы свяжемся с вами в течение 15 минут в рабочее время.') + f'''
<section class="section-sm">
  <div class="container">
    <div class="contact-cards">
      <div class="contact-card reveal"><div class="ic">{ic('phone')}</div><small>Отдел продаж</small><strong><a href="tel:{PHONE_TEL}">{PHONE}</a></strong><small>Покупка и подбор · WhatsApp / Telegram</small></div>
      <div class="contact-card reveal"><div class="ic">{ic('wrench')}</div><small>Сервисный центр</small><strong><a href="tel:{SVC_TEL}">{SVC}</a></strong><small>Установка, ремонт, гарантия</small></div>
      <div class="contact-card reveal"><div class="ic">{ic('mail')}</div><small>E-mail</small><strong><a href="mailto:{EMAIL}">{EMAIL}</a></strong><small>Для вопросов и заявок</small></div>
      <div class="contact-card reveal"><div class="ic">{ic('pin')}</div><small>Адрес</small><strong>{ADDRESS}</strong></div>
      <div class="contact-card reveal"><div class="ic">{ic('clock')}</div><small>Режим работы</small>
        <div class="hours"><div><span>Пн–Пт</span><b>9:00–18:00</b></div><div><span>Сб–Вс</span><b>выходной</b></div></div></div>
    </div>
  </div>
</section>
<section class="section" id="request" style="padding-top:24px">
  <div class="container split" style="align-items:stretch">
    <div class="reveal" style="display:grid">{lead_form(True, 'Напишите нам')}</div>
    <div class="map reveal">
      <iframe src="https://yandex.uz/map-widget/v1/?mode=search&amp;z=16&amp;text=%D0%A2%D0%B0%D1%88%D0%BA%D0%B5%D0%BD%D1%82%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%94%D0%B6%D0%B0%D0%BC%D0%B8%2C%205" title="Thermex Узбекистан на карте" loading="lazy"></iframe>
    </div>
  </div>
</section>
'''
    write('contacts.html', head('Контакты — Thermex Узбекистан', 'Контакты официального партнёра Thermex в Узбекистане: телефон, Telegram, e-mail, адрес в Ташкенте и режим работы.', '/contacts.html') + header('/contacts.html') + body + footer() + '</body>\n</html>\n')

# ------------------------------------------------------------------ 404 + legacy redirect
def not_found():
    extra = f'''
    <div class="hero-actions">
      <a class="btn btn-primary" href="/">На главную</a>
      <a class="btn btn-ghost" href="/catalog.html">Каталог</a>
      <a class="btn btn-ghost" href="/contacts.html">Контакты</a>
    </div>'''
    body = page_hero('Ошибка 404', 'Страница не найдена', 'Возможно, ссылка устарела или в адресе опечатка. Выберите нужный раздел ниже или позвоните нам.', extra)
    write('404.html', head('Страница не найдена — Thermex Узбекистан', 'Такой страницы на сайте нет.', '/404.html', noindex=True) + header('') + body + footer() + '</body>\n</html>\n')

# Old addresses (Cyrillic file names from the Nicepage export) redirect to the new ones.
LEGACY = [('Главная.html', '/')] + [(f'{ru}.html', f'/{en}.html') for ru, en in [('Каталог', 'catalog'), ('Водонагреватели', 'water-heaters'), ('Преимущества', 'advantages'), ('Сервис', 'service'), ('О-компании', 'about'), ('Контакты', 'contacts')]]

def legacy_redirect():
    for old, new in LEGACY:
        write(old, '<!DOCTYPE html>\n<html lang="ru"><head><meta charset="utf-8">'
              f'<meta http-equiv="refresh" content="0;url={new}"><link rel="canonical" href="{SITE}{new}">'
              f'<script>location.replace({json.dumps(new)} + location.hash);</script>'
              f'<title>Перенаправление</title></head><body><a href="{new}">{SITE}{new}</a></body></html>\n')

# ------------------------------------------------------------------ sitemap + robots
SITEMAP = [('/', '1.0'), ('/catalog.html', '0.9'), ('/water-heaters.html', '0.9'), ('/advantages.html', '0.7'),
           ('/service.html', '0.8'), ('/about.html', '0.6'), ('/contacts.html', '0.8')]

def sitemap():
    today = date.today().isoformat()
    rows = ''.join(f'  <url>\n    <loc>{SITE}{quote(path)}</loc>\n    <lastmod>{today}</lastmod>\n    <priority>{pr}</priority>\n  </url>\n' for path, pr in SITEMAP)
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + rows + '</urlset>\n')
    write('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')

def main():
    with open(os.path.join(ROOT, 'assets', 'js', 'catalog-data.js'), 'w', encoding='utf-8') as f:
        f.write(catalog_data_js())
    for fn in (home, catalog, heaters, advantages, service, about, contacts, not_found, legacy_redirect, sitemap):
        fn()
    fetched = sum(1 for c in CATALOG if not c[6] and slug(c[0], c[1]) in FETCHED)
    print(f'built 8 pages, sitemap, robots; catalog: {len(CATALOG)} models, {len(FEATURED)} featured + {fetched} with thermex.ru data')

if __name__ == '__main__':
    main()
