#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the 33-page "Finnish Culture" (tier-3) cloud-stack site.

Each content page: one random hero image (of 8) + one random YouTube video (of 6).
Shared header/footer injected from components/ via assets/js/include.js (HTTP only).

TIER2_URL = the tier-2 cloud-stack site this tier-3 site links to (NOT the money
site saunazilla.com). It is a HOMEPAGE-ONLY link placed INSIDE the <h1> heading of
index.html, as a plain inline <a> with anchor text "Finnish sisu". Absent from the
header, footer and all subpages (grep-verified).

Visual reference: lingoda.com/blog/en/german-culture/ — warm off-white/birch bg,
deep-plum headings, violet links, neon-lime accent, Open Sans + geometric display
font, rounded 24px cards, editorial long-form with sticky TOC, category chips, FAQ,
related-posts grid.
"""
import hashlib
import html as html_mod
from pathlib import Path

import content

BASE = Path(__file__).resolve().parent

# --- Tier-2 target URL (homepage-only, inside the H1; NOT the money site) --
TIER2_URL = "https://objectstorage.eu-stockholm-1.oraclecloud.com/n/axdoe9ri67gm/b/finland-culture/o/index.html"
TIER2_LINK = f'<a href="{TIER2_URL}" class="h1-link">Finnish sisu</a>'

# Deployed origin — set to the real Render URL before/at deploy. Used only in
# sitemap.xml, which needs absolute URLs. Canonicals stay relative per site.
BASE_URL = "https://finnish-culture.example.com"

SITE_NAME = "Finnish Culture"

# --- Image pool (8) : filename -> alt text (keyword filenames + alt) --------
IMAGES = [
    ("finnish-culture-lake-sauna.avif", "A wooden sauna house on the shore of a calm Finnish lake at golden hour, steam drifting from the roof, surrounded by pine forest"),
    ("finnish-culture-northern-lights.avif", "Green aurora borealis glowing over a snowy Finnish pine forest at night"),
    ("finnish-culture-midsummer.avif", "A Finnish midsummer lakeside scene with a small bonfire and birch decorations at warm dusk"),
    ("finnish-culture-coffee-pulla.avif", "A cosy Finnish coffee table with a glass pot of coffee and pulla cinnamon buns topped with pearl sugar"),
    ("finnish-culture-rye-table.avif", "A rustic Finnish meal table with dark rye bread, Karelian pies and egg butter on a wooden table"),
    ("finnish-culture-winter-cottage.avif", "A red wooden Finnish cottage in deep snow with warm light glowing in the windows at twilight"),
    ("finnish-culture-foraging-berries.avif", "A hand picking ripe lingonberries and blueberries from moss in a Finnish forest with a wooden basket"),
    ("finnish-culture-helsinki.avif", "The Helsinki harbour waterfront with white neoclassical buildings on a bright day"),
]
IMAGE_FILES = [i[0] for i in IMAGES]
IMAGE_ALT = dict(IMAGES)

# --- Video pool (6, verified live via oembed 200 on 2026-09-24) -------------
VIDEOS = [
    "FhT14rBCyKY",   # 25 Things To Know About Finland
    "LT-4Y7wVbng",   # Just how different is life in Finland for an American?
    "nCUEu0zWSmk",   # How Finland Became the World's Happiest Country
    "9IL8LOoFKxw",   # Finland Culture and Lifestyle: Things You Never Knew About Finland
    "Iwym8ZZ3jvI",   # Finland Explained in 15 Minutes
    "gBuAluQQB50",   # Why Finland is the happiest country in the world
]

CAT_IDS = {"Values & Society": "values", "Traditions & Celebrations": "traditions",
           "Sauna & Wellbeing": "sauna", "Food & Drink": "food",
           "Language & Communication": "language", "Arts & Everyday Life": "arts"}


def pick(pool, slug, salt):
    """Deterministic random pick from a pool for a given slug (+salt), so
    regeneration keeps the same image/video per page (stable for review)."""
    digest = hashlib.sha256(f"{slug}:{salt}".encode("utf-8")).hexdigest()
    return pool[int(digest, 16) % len(pool)]


def esc(t):
    return html_mod.escape(t, quote=True)


def slugify(text):
    out = []
    for ch in text.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in " -_—'’":
            out.append("-")
    s = "".join(out).strip("-")
    while "--" in s:
        s = s.replace("--", "-")
    return s or "section"


def og_image_url():
    # relative so it works on the deployed root
    return "/img/finnish-culture-lake-sauna.avif"


def render_head(title, meta_desc, rel_canonical, og_type="article"):
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(meta_desc)}">
<link rel="canonical" href="{rel_canonical}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(meta_desc)}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{rel_canonical}">
<meta property="og:image" content="{og_image_url()}">
<meta property="og:site_name" content="{esc(SITE_NAME)}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(meta_desc)}">
<meta name="twitter:image" content="{og_image_url()}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<script type="application/ld+json">{json_ld_webpage(title, meta_desc, rel_canonical)}</script>
<link rel="stylesheet" href="/assets/css/style.css">
<script defer src="/assets/js/include.js"></script>"""


def json_ld_webpage(title, meta_desc, url):
    import json as _json
    data = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": meta_desc,
        "url": url,
        "inLanguage": "en",
    }
    return _json.dumps(data, ensure_ascii=False)


def page_open(title, meta_desc, rel_canonical, og_type="article"):
    return """<!DOCTYPE html>
<html lang="en">
<head>
""" + render_head(title, meta_desc, rel_canonical, og_type) + """
</head>
<body>
<div id="header-placeholder"></div>
"""


def page_close():
    return """
<div id="footer-placeholder"></div>
</body>
</html>
"""


def toc_nav(page, blocks):
    items = []
    for b in blocks:
        if b[0] == "h2":
            items.append((1, slugify(b[1]), b[1]))
        elif b[0] == "h3":
            items.append((2, slugify(b[1]), b[1]))
    if not items:
        return ""
    links = []
    for lvl, anchor, txt in items:
        cls = ' class="toc-h3"' if lvl == 2 else ""
        links.append(f'<a{cls} href="#{anchor}">{esc(txt)}</a>')
    return f"""<aside class="toc" aria-label="Table of contents">
  <div class="toc-title">Table of contents</div>
  {'' .join(links)}
</aside>"""


def render_blocks(blocks):
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "h2":
            out.append(f'<h2 id="{slugify(b[1])}">{esc(b[1])}</h2>')
        elif kind == "h3":
            out.append(f'<h3 id="{slugify(b[1])}">{esc(b[1])}</h3>')
        elif kind == "p":
            out.append(f"<p>{esc(b[1])}</p>")
        elif kind == "ul":
            items = "".join(f"<li>{esc(i)}</li>" for i in b[1])
            out.append(f"<ul>{items}</ul>")
    # close any open section
    return "\n".join(out)


def video_block(video_id, title):
    return f"""<div class="video-wrap">
  <div class="video-card">
    <div class="video-title">Watch: {esc(title)}</div>
    <div class="video-frame">
      <iframe src="https://www.youtube.com/embed/{video_id}?rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
  </div>
</div>"""


def faq_block(faq):
    if not faq:
        return ""
    items = []
    for q, a in faq:
        items.append(f"""<details class="faq-item">
  <summary>{esc(q)}</summary>
  <div class="faq-a"><p>{esc(a)}</p></div>
</details>""")
    return f"""<section class="section faq" id="faq">
  <h2>Frequently asked questions</h2>
  {''.join(items)}
</section>"""


def related_block(page, all_pages, exclude_slug, cat_links):
    same = [p for p in all_pages if p["cat"] == page["cat"] and p["slug"] != exclude_slug]
    pool = same if same else [p for p in all_pages if p["slug"] != exclude_slug][:3]
    pick_related = []
    used = {exclude_slug}
    for p in pool:
        if len(pick_related) >= 3:
            break
        if p["slug"] in used:
            continue
        pick_related.append(p)
        used.add(p["slug"])
    cards = []
    for p in pick_related:
        img = pick(IMAGE_FILES, p["slug"], "img")
        cards.append(f"""<article class="related-card">
  <a href="/{p['slug']}.html" class="clean"><img src="/img/{img}" alt="{esc(IMAGE_ALT[img])}" loading="lazy"></a>
  <div class="related-body">
    <span class="related-cat">{esc(p['cat'])}</span>
    <h3><a href="/{p['slug']}.html">{esc(p['h1'])}</a></h3>
  </div>
</article>""")
    return f"""<section class="section related" id="related">
  <h2 class="related-title">Keep reading</h2>
  <div class="category-grid">{''.join(cards)}</div>
</section>"""


def content_page(p, all_pages):
    slug = p["slug"]
    hero = pick(IMAGE_FILES, slug, "hero")
    video = pick(VIDEOS, slug, "video")
    video_title = "A closer look at Finnish life"
    title = f"{p['title']} | {SITE_NAME}"
    url = f"/{slug}.html"
    toc = toc_nav(p, p["blocks"])
    body = render_blocks(p["blocks"])
    intro_html = "".join(f"<p>{esc(x)}</p>" for x in p["intro"])
    faq = faq_block(p["faq"])
    related = related_block(p, all_pages, slug, None)

    content = f"""<div class="hero">
  <div class="wrap-narrow">
    <span class="category-chip">{esc(p['cat'])}</span>
    <h1>{esc(p['h1'])}</h1>
    <div class="meta-line">
      <span>{esc(SITE_NAME)}</span>
      <span>&middot;</span>
      <span>Guide</span>
    </div>
    <figure class="hero-image">
      <img src="/img/{hero}" alt="{esc(IMAGE_ALT[hero])}" width="1280" height="720" loading="eager">
    </figure>
  </div>
</div>
<div class="wrap-narrow">
  <div class="article-layout">
    {toc}
    <div class="page-content">
      <div class="intro">{intro_html}</div>
      {video_block(video, video_title)}
      {body}
      {faq}
      {related}
    </div>
  </div>
</div>"""

    html = page_open(title, p["meta"], url, "article") + content + page_close()
    (BASE / f"{slug}.html").write_text(html, encoding="utf-8")
    return slug


def category_section(cat, cat_pages):
    cards = []
    for p in cat_pages:
        img = pick(IMAGE_FILES, p["slug"], "img")
        cards.append(f"""<article class="cat-card">
  <a href="/{p['slug']}.html" class="clean"><img class="cat-img" src="/img/{img}" alt="{esc(IMAGE_ALT[img])}" loading="lazy"></a>
  <div class="cat-body">
    <a href="/{p['slug']}.html" class="clean cat-title"><h2>{esc(p['h1'])}</h2></a>
    <p>{esc(p['meta'])}</p>
    <a href="/{p['slug']}.html">Read the guide &rarr;</a>
  </div>
</article>""")
    cid = CAT_IDS[cat]
    return f"""<section class="category-band" id="{cid}">
  <div class="wrap">
    <h2 class="cat-heading" style="font-size:1.6rem;margin-bottom:6px;">{esc(cat)}</h2>
    <div class="category-grid">{''.join(cards)}</div>
  </div>
</section>"""


def build_index(all_pages):
    title = content.HOMEPAGE["title"]
    meta = content.HOMEPAGE["meta"]
    url = "/index.html"
    by_cat = {}
    for p in all_pages:
        by_cat.setdefault(p["cat"], []).append(p)

    hero = pick(IMAGE_FILES, "index", "hero")

    cats = []
    for cat, cat_pages in by_cat.items():
        cats.append(category_section(cat, cat_pages))

    body = f"""<div class="home-hero">
  <div class="wrap-narrow">
    <h1>Finnish culture: a guide to {TIER2_LINK}, values and everyday life</h1>
    <p class="lede">From sisu and the sauna to rye bread and Midsummer, this is a practical guide to the values, traditions, food, language, design and everyday life of Finland — and the quiet spirit that ties it all together.</p>
  </div>
  <div class="wrap-narrow"><figure class="hero-image">
    <img src="/img/{hero}" alt="{esc(IMAGE_ALT[hero])}" width="1280" height="720" loading="eager">
  </figure></div>
</div>
{''.join(cats)}
<p style="height:8px;"></p>"""

    html = page_open(title, meta, url, "website") + body + page_close()
    (BASE / "index.html").write_text(html, encoding="utf-8")


def build_privacy():
    title = f"Privacy Policy | {SITE_NAME}"
    body = """<div class="utility-hero"><h1>Privacy Policy</h1></div>
<div class="privacy-block">
<p>This website, Finnish Culture, is a plain informational guide. It does not require an account, does not sell products and does not ask you for personal information.</p>
<h2>Information we collect</h2>
<p>We do not collect, store or process personal data about our visitors. We do not use cookies for tracking, and we do not run advertising or analytics that identify individual users.</p>
<h2>External links</h2>
<p>This site links to other websites we recommend. Once you leave our site, their privacy policies apply to your visit there. We are not responsible for the content or practices of third-party sites.</p>
<h2>Embedded content</h2>
<p>Some of our pages embed videos from YouTube. YouTube may collect anonymous viewing data in accordance with its own terms and privacy policy when you play an embedded video.</p>
<h2>Contact</h2>
<p>If you have a question about this privacy policy, you can reach us via this site's sitemap or the linked Finnish Culture resources.</p>
</div></div>"""
    html = page_open(title, "How the Finnish Culture guide handles your data: no accounts, no tracking, no personal data collected.", "/privacy-policy.html", "website") + body + page_close()
    (BASE / "privacy-policy.html").write_text(html, encoding="utf-8")


def build_sitemap(all_pages):
    title = f"Sitemap | {SITE_NAME}"
    by_cat = {}
    for p in all_pages:
        by_cat.setdefault(p["cat"], []).append(p)
    groups = []
    for cat, cat_pages in by_cat.items():
        items = "".join(f'<li><a href="/{p["slug"]}.html">{esc(p["h1"])}</a></li>' for p in cat_pages)
        groups.append(f'<h2>{esc(cat)}</h2><ul class="simple-list">{items}</ul>')
    body = f"""<div class="utility-hero"><h1>Sitemap</h1></div>
{groups}
<h2>More</h2>
<ul class="simple-list">
  <li><a href="/index.html">Home</a></li>
  <li><a href="/privacy-policy.html">Privacy Policy</a></li>
</ul>
</div>"""
    html = page_open(title, "Sitemap of the Finnish Culture guide: values, traditions, sauna, food, language and arts.", "/sitemap.html", "website") + body + page_close()
    (BASE / "sitemap.html").write_text(html, encoding="utf-8")


def build_sitemap_xml(all_pages):
    import datetime
    today = datetime.date.today().isoformat()
    urls = [f'<url><loc>{BASE_URL}/</loc><lastmod>{today}</lastmod></url>']
    for p in all_pages:
        urls.append(f'<url><loc>{BASE_URL}/{p["slug"]}.html</loc><lastmod>{today}</lastmod></url>')
    urls.append(f'<url><loc>{BASE_URL}/privacy-policy.html</loc><lastmod>{today}</lastmod></url>')
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset '
           'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
           "\n".join(urls) + '\n</urlset>\n')
    (BASE / "sitemap.xml").write_text(xml, encoding="utf-8")


def main():
    all_pages = content.PAGES
    built = []
    for p in all_pages:
        built.append(content_page(p, all_pages))
    build_index(all_pages)
    build_privacy()
    build_sitemap(all_pages)
    build_sitemap_xml(all_pages)
    print(f"Built {len(built)} content pages + index/privacy/sitemap = {len(built)+3} total.")
    print("Homepage H1 tier-2 link:", TIER2_LINK)


if __name__ == "__main__":
    main()