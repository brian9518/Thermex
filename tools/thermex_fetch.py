"""Fetch product photos and specs from thermex.ru (runs in GitHub Actions).

Writes _scrape/data.json and _scrape/img/<id>-<n>.webp for every model in MODELS.
"""
import html
import io
import json
import os
import re
import time
import urllib.request

from PIL import Image

OUT = '_scrape'
BASE = 'https://thermex.ru/catalog/'
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'
MAX_IMAGES = 3

# Our catalog id -> product page on thermex.ru
MODELS = {
    'thermex-thermo-80-v': 'seriya-thermo/thermex-thermo-80-v/',
    'thermex-thermo-100': 'seriya-thermo/thermex-thermo-100-v/',
    'thermex-thermo-150': 'seriya-thermo/thermex-thermo-150-v/',
    'thermex-thermo-es-30': 'seriya-thermo/thermex-thermo-30-v-slim/',
    'thermex-thermo-es-50': 'seriya-thermo/thermex-thermo-50-v-slim/',
    'thermex-edisson-er-80-v': 'seriya-glasslined/edisson-er-80-v-/',
    'thermex-er-200': 'seriya-titaniumheat-floor/thermex-er-200-v/',
    'thermex-er-300': 'seriya-titaniumheat-floor/thermex-er-300-v/',
    'thermex-ers-50-v': 'seriya-champion-silverheat/thermex-ers-50-v-silverheat/',
    'thermex-ers-80-h': 'seriya-champion-silverheat/thermex-ers-80-h-silverheat/',
    'thermex-ers-100-v': 'seriya-champion-silverheat/thermex-ers-100-v-silverheat/',
    'thermex-ess-30-v': 'seriya-champion-silverheat/thermex-ess-30-v-silverheat/',
    'thermex-ess-50-v': 'seriya-champion-silverheat/thermex-ess-50-v-silverheat/',
    'thermex-ess-80-v': 'seriya-champion/thermex-es-80-v-silverheat/',
    'thermex-titan-50-v': 'seriya-champion-titaniumheat/thermex-titaniumheat-50-v/',
    'thermex-titan-80-v': 'seriya-champion-titaniumheat/thermex-titaniumheat-80-v/',
    'thermex-titan-80-h': 'seriya-champion-titaniumheat/thermex-titaniumheat-80-h/',
    'thermex-titan-100': 'seriya-champion-titaniumheat/thermex-titaniumheat-100-v/',
    'thermex-titan-150-v': 'seriya-champion-titaniumheat/thermex-titaniumheat-150-v/',
    'thermex-titan-ess-30-v': 'seriya-champion-titaniumheat/thermex-titaniumheat-30-v-slim/',
    'thermex-titan-ess-50-v': 'seriya-champion-titaniumheat/thermex-titaniumheat-50-v-slim/',
    'thermex-titan-ess-50-h': 'seriya-champion-titaniumheat/thermex-titaniumheat-50-h-slim/',
    'thermex-giro-50': 'seriya-giro/thermex-giro-50/',
    'thermex-giro-80': 'seriya-giro/thermex-giro-80/',
    'thermex-giro-100': 'seriya-giro/thermex-giro-100/',
    'thermex-nova-50': 'seriya-nova/thermex-nova-50-v/',
    'thermex-nova-100': 'seriya-nova/thermex-nova-100-v/',
    'thermex-nobel-15-u': 'seriya-nobel/thermex-n-15-u/',
    'thermex-combo-150-v-l': 'seriya-combi/thermex-er-150-v-combi/',
    'thermex-combo-150-v-r': 'seriya-combi/thermex-er-150-v-combi/',
    'garanterm-eco-80-v': 'seriya-eco/garanterm-eco-80-v/',
    'garanterm-origin-50-v': 'seriya-origin/garanterm-er-50-v/',
    'garanterm-origin-80-v': 'seriya-origin/garanterm-er-80-v/',
    'garanterm-origin-100-v': 'seriya-origin/garanterm-er-100-v/',
    'garanterm-origin-slim-30-v': 'seriya-origin/garanterm-es-30-v/',
    'garanterm-origin-slim-50-v': 'seriya-origin/garanterm-es-50-v/',
}


def get(url, binary=False):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'ru'})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    time.sleep(0.5)
    return data if binary else data.decode('utf-8', 'replace')


def text(fragment):
    fragment = re.sub(r'<i\b[^>]*>.*?</i>', '', fragment, flags=re.S)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', fragment))).strip()


def parse(page):
    title = re.search(r'<h1 class="catalog-good-title">(.*?)</h1>', page, re.S)
    desc = re.search(r'<div class="catalog-good-description">(.*?)</div>', page, re.S)
    images = []
    for href in re.findall(r'<a class="container-picture gallery-item[^"]*"[^>]*href="([^"]+)"', page):
        if href not in images:
            images.append(href)
    specs = []
    for row in re.findall(r'<div class="catalog-good-props-item">\s*(<span>.*?</span>)\s*(<span>.*?</span>)\s*</div>', page, re.S):
        key, value = text(row[0]), text(row[1])
        if key and value:
            specs.append([key, value])
    return {
        'title': text(title.group(1)) if title else '',
        'description': text(desc.group(1)) if desc else '',
        'images': images,
        'specs': specs,
    }


def to_webp(data, dest):
    im = Image.open(io.BytesIO(data))
    im = im.convert('RGBA') if im.mode in ('RGBA', 'LA', 'P') else im.convert('RGB')
    if im.mode == 'RGBA':
        bbox = im.getchannel('A').point(lambda v: 255 if v > 8 else 0).getbbox()
        if bbox:
            im = im.crop(bbox)
    im.thumbnail((700, 900), Image.LANCZOS)
    im.save(dest, 'WEBP', quality=82, method=6)


def main():
    os.makedirs(os.path.join(OUT, 'img'), exist_ok=True)
    data, cache = {}, {}
    for pid, path in MODELS.items():
        url = BASE + path
        try:
            if url not in cache:
                cache[url] = parse(get(url))
            info = dict(cache[url])
        except Exception as e:
            print('FAIL', pid, url, e)
            continue
        files = []
        for n, src in enumerate(info['images'][:MAX_IMAGES]):
            name = f'{pid}-{n + 1}.webp'
            try:
                to_webp(get('https://thermex.ru' + src, binary=True), os.path.join(OUT, 'img', name))
                files.append(name)
            except Exception as e:
                print('image fail', pid, src, e)
        info['url'] = url
        info['files'] = files
        data[pid] = info
        print(f'{pid}: {info["title"]} | {len(info["specs"])} specs | {len(files)} photos')
    with open(os.path.join(OUT, 'data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print('done', len(data), 'of', len(MODELS))


if __name__ == '__main__':
    main()
