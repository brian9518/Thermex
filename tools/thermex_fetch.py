"""Fetch product data from thermex.ru (runs in GitHub Actions)."""
import gzip
import os
import re
import time
import urllib.request

OUT = '_scrape'
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'


def get(url, binary=False):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'ru'})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
        if data[:2] == b'\x1f\x8b':
            data = gzip.decompress(data)
    time.sleep(0.5)
    return data if binary else data.decode('utf-8', 'replace')


def save(name, text):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(text)


def sitemap_urls(url, seen=None):
    seen = seen if seen is not None else set()
    if url in seen:
        return []
    seen.add(url)
    try:
        xml = get(url)
    except Exception as e:
        print('sitemap fail', url, e)
        return []
    locs = re.findall(r'<loc>\s*([^<\s]+)\s*</loc>', xml)
    if '<sitemapindex' in xml:
        out = []
        for loc in locs:
            out += sitemap_urls(loc, seen)
        return out
    return locs


def recon():
    for path in ['robots.txt']:
        try:
            save(path, get('https://thermex.ru/' + path))
        except Exception as e:
            print('fail', path, e)
    urls = sitemap_urls('https://thermex.ru/sitemap.xml')
    catalog = sorted(u for u in urls if '/catalog/' in u)
    save('catalog_urls.txt', '\n'.join(catalog))
    print('sitemap urls:', len(urls), 'catalog urls:', len(catalog))
    save('giro-100.html', get('https://thermex.ru/catalog/seriya-giro/thermex-giro-100/'))


if __name__ == '__main__':
    recon()
