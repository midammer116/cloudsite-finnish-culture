# Finnish Culture — Tier-3 Cloud Stack Website Plan

## Build notes
- Work folder : projects/saunazilla/cloud-stacks/finnish-culture-tier-3
- Tier        : 3 (topical-authority guide site). Does NOT link to the money site
  (saunazilla.com). External link target: tier-2 cloud-stack website **Finland Culture**
  (https://objectstorage.eu-stockholm-1.oraclecloud.com/n/axdoe9ri67gm/b/finland-culture/o/index.html).
  Purpose: build topical authority toward that tier-2 site.
- Link rule  : the tier-2 link is a HOMEPAGE-ONLY link, placed INSIDE the <h1> heading, as a
  plain inline <a> with anchor text **"Finnish sisu"**. NOT in the header, NOT in the footer,
  NOT on content/subpages. Grep-verified per standing rule.
- Deploy     : Render (static site). NOT auto-deployed — awaiting user visual review first.
  Render needs a PUBLIC GitHub repo; live URL must contain NO "tier" (service/repo name = clean
  keyword, e.g. `finnish-culture` → https://finnish-culture.onrender.com).
- Footer     : NO Saunazilla social-media icons. Clean grouped link grid + privacy + sitemap.
- Visual     : Mimics lingoda.com/blog/en/german-culture/ — warm off-white/birch background
  (#fbf9f9/#fff, blush cards #f4e9ea), deep-plum headings (#1b0338/#350359), violet-magenta
  links (#9100d4/#ae00ff), one neon-lime accent (#d5fd44), Open Sans body + geometric-sans
  display headings, rounded cards (radius 8/24px), editorial long-form with sticky TOC,
  category chips, meta line, FAQ, related-posts grid.
- Images     : 8 x 1280x720 horizontal, xAI Imagine (`grok-imagine-image`, `resolution "1k"` =
  1280x720, cheapest tier), one random hero image per content page + homepage, stored in `img/`
  as optimized `.avif` (~30–60 KB each), keyword filenames + keyword alt text.
- Videos     : 6 supplied YouTube videos (all live, all Finland-themed — verified 2026-09-24 via
  oembed HTTP 200), one random per page (main content column). IDs:
  FhT14rBCyKY / LT-4Y7wVbng / nCUEu0zWSmk / 9IL8LOoFKxw / Iwym8ZZ3jvI / gBuAluQQB50
- Layout     : homepage (category grid linking all pages) + 30 content pages + privacy + sitemap.
  Article = two-column (content + sticky TOC sidebar): hero image, category chip, H1, meta line,
  TOC (#anchor links), H2 sections with paragraphs and H3 subsections, one embedded video, FAQ,
  related-posts grid. Shared header/footer via assets/js/include.js (HTTP deploy env).

## Site structure — 33 pages

Nav categories (6):
- Values & Society
- Traditions & Celebrations
- Sauna & Wellbeing
- Food & Drink
- Language & Communication
- Arts & Everyday Life

### Utilities
1. index.html — Finnish Culture — H1 "Finnish Culture: The Spirit of Finnish Sisu"
   (tier-2 link "Finnish sisu" placed INSIDE the H1)
2. privacy-policy.html — Privacy Policy
3. sitemap.html — Sitemap

### Values & Society
4.  sisu.html — Finnish Sisu — "Sisu: Finland's Spirit of Resilience"
    H2: What "sisu" really means; Sisu in everyday life; Sisu and wellbeing; Sisu vs. resilience
5.  honesty-trust.html — Honesty & Social Trust — "Honesty and Social Trust in Finland"
    H2: Why honesty matters; The high-trust society; Everyday honesty; Trust and institutions
6.  equality.html — Equality — "Equality and the Finnish Social Model"
    H2: Equality as a value; Gender balance; Consensus and the welfare model; Everyday equality
7.  personal-space.html — Personal Space & Silence — "Personal Space and the Comfort of Silence"
    H2: The value of silence; Personal space in daily life; Talking about feelings; Reading the room
8.  punctuality.html — Punctuality & Time — "Punctuality and the Respect for Time"
    H2: Being on time; Time as a promise; Seasonal time; Time at work

### Traditions & Celebrations
9.  juhannus.html — Juhannus (Midsummer) — "Juhannus: Finnish Midsummer"
    H2: The summer solstice; Lakeside rituals; Midsummer food; Midsummer today
10. vappu.html — Vappu (May Day) — "Vappu: Finland's May Day Celebration"
    H2: Welcome to spring; Student celebrations; The picnic tradition; Sima and tippaleipä
11. joulu.html — Joulu (Christmas) — "Joulu: Finnish Christmas Traditions"
    H2: The Christmas peace; Food and traditions; Sauna on Christmas Eve; Gifts and the day itself
12. independence-day.html — Independence Day — "How Finland Celebrates Independence Day"
    H2: A quiet national day; The presidential reception; Candlelight at the graves; Education angle
13. seasonal-rhythm.html — Seasonal Rhythm — "The Seasonal Rhythm of Finnish Life"
    H2: Four very different seasons; The midnight sun and kaamos; Nature's calendar; What flows from it

### Sauna & Wellbeing
14. sauna-culture.html — Sauna Culture — "Sauna: The Soul of Finnish Culture"
    H2: More than a room; A social equaliser; The sauna ritual; Types of sauna
15. sauna-etiquette.html — Sauna Etiquette — "Sauna Etiquette: The Unwritten Rules"
    H2: Nudity is normal; How to behave; The löyly rule; After the sauna
16. loyly.html — Löyly — "Löyly: The Art of Sauna Steam"
    H2: What löyly means; Throwing the water; Managing the heat; Why it matters
17. ice-swimming.html — Ice Swimming — "Avanto: Ice Swimming and Winter Wellness"
    H2: The winter tradition; How it is done; Health benefits; Safety
18. wellbeing-nature.html — Nature & Wellbeing — "Nature, Silence and Finnish Wellbeing"
    H2: The forest as a reset; Silence as therapy; Everyday wellbeing; The happy-country clue

### Food & Drink
19. finnish-cuisine.html — Finnish Cuisine — "Finnish Cuisine: Simple, Honest and Fresh"
    H2: From forest to table; Staple ingredients; Everyday meals; Seasonal eating
20. rye-bread.html — Rye Bread — "Rye Bread: The Staff of Finnish Life"
    H2: Why rye rules; The sourdough tradition; How it is eaten; Modern rye
21. karelian-pies.html — Karelian Pies — "Karelian Pies and Savoury Classics"
    H2: The shape of home; Making the pie; Egg butter; Where to find them
22. coffee-culture.html — Coffee Culture — "Coffee Culture: The World's Caffeine Kings"
    H2: The world's heaviest coffee drinkers; The proper coffee break; Fika without the name;
        What Finns drink today
23. foraging-berries.html — Foraging & Berries — "Foraging, Berries and the Forest Pantry"
    H2: Everyman's right to the forest; The berry calendar; Mushrooms and edibles; Preserving the harvest

### Language & Communication
24. finnish-language.html — The Finnish Language — "The Finnish Language: What to Know"
    H2: A non-Indo-European language; Grammar at a glance; Loanwords and adaptation; Learning tips
25. finnish-humour.html — Finnish Humour — "Finnish Humour: Dry, Deadpan and Honest"
    H2: Understatement as comedy; Self-deprecation; Timing and silence; Where to hear it
26. how-finns-communicate.html — How Finns Communicate — "How Finns Communicate: Direct and Quiet"
    H2: Say what you mean; The joy of small talk (or not); Written vs. spoken; Being a good listener
27. dialects.html — Dialects — "Finnish Dialects and Regional Identity"
    H2: A language of many voices; East vs. West; Standard vs. colloquial; Dialect pride
28. colloquial-finnish.html — Colloquial Finnish — "Colloquial Finnish: How Finns Actually Talk"
    H2: Puhekieli vs. kirjakieli; Dropping and shortening; Everyday words; Meeting it in the wild

### Arts & Everyday Life
29. finnish-design.html — Finnish Design — "Finnish Design: Function, Light and Simplicity"
    H2: Form follows honesty; The golden age; Design icons; Design in daily life
30. nature-everymans-right.html — Everyman's Rights — "Everyman's Rights: Free Access to Nature"
    H2: What the right means; Where you may go; What to respect; Teaching at school
31. summer-cottage.html — The Summer Cottage — "The Summer Cottage: A National Obsession"
    H2: A second home in nature; The simple rhythm; Lakeside living; What it means
32. music-and-arts.html — Music & Arts — "Music, Film and the Arts in Finland"
    H2: A sound identity; From sauna metal to classical; Film and literature; Festivals and venues
33. everyday-social-life.html — Everyday Social Life — "Everyday Social Life in Finland"
    H2: Work and social life; Invitations and hosting; Sports and clubs; Guest etiquette

## Images (8, 1280x720, finnish-culture themed)
1. finnish-culture-lake-sauna.avif — wooden sauna house on a Finnish lake at golden hour
2. finnish-culture-northern-lights.avif — green aurora over snowy pine forest
3. finnish-culture-midsummer.avif — midsummer lakeside bonfire and birch decor at dusk
4. finnish-culture-coffee-pulla.avif — coffee pot and pulla cinnamon buns on a linen table
5. finnish-culture-rye-table.avif — rye bread, Karelian pies and egg butter table spread
6. finnish-culture-winter-cottage.avif — red wooden cottage in deep snow with warm windows
7. finnish-culture-foraging-berries.avif — hand picking lingonberries/blueberries in moss
8. finnish-culture-helsinki.avif — Helsinki harbour with white neoclassical buildings

## Deliverables
- 33 .html pages (index + 30 content + privacy + sitemap) + sitemap.xml + robots.txt + favicon.svg
- assets/css/style.css + assets/js/include.js + components/header.html + components/footer.html
- img/ with 8 optimized .avif images (40–76 KB, 1280x720)
- generate-pages.py + gen_images.py + content.py + SITE-PLAN.md
- Awaiting user visual review before any deploy to Render (no auto-deploy). BASE_URL
  placeholder (sitemap.xml) to be set to the real Render URL at deploy.