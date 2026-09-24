#!/usr/bin/env python3
"""Generate 8 x 1280x720 Finnish-culture images via xAI Imagine
(grok-imagine-image, resolution "1k" = 1280x720 horizontal, cheapest tier),
download and optimize to .avif in the tier-3 work folder img/ dir.
Modest quality on purpose to keep token use low."""
import json
import os
import time
import urllib.request
from pathlib import Path

PROFILE_ENV = Path(os.environ.get("LOCALAPPDATA", "")) / "hermes" / "profiles" / "dev" / ".env"
OUT_DIR = Path(r"C:\Users\porne\Documents\Marskibrain\projects\saunazilla\cloud-stacks\finnish-culture-tier-3\img")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def get_key():
    if "XAI_API_KEY" in os.environ and os.environ["XAI_API_KEY"].startswith("xai-"):
        return os.environ["XAI_API_KEY"]
    for line in PROFILE_ENV.read_text(encoding="utf-8", errors="ignore").splitlines():
        if line.startswith("XAI_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("XAI_API_KEY not found in profile .env")


KEY = get_key()

# filename -> prompt  (8 images, horizontal 16:9, finnish-culture themed)
IMAGES = {
    "finnish-culture-lake-sauna": (
        "A grey wooden sauna house on the shore of a calm Finnish lake surrounded by pine forest "
        "and birch trees, soft steam drifting from the roof, early evening golden light, tranquil "
        "and serene Nordic mood, high quality editorial photography, horizontal 16:9. No text, no people."
    ),
    "finnish-culture-northern-lights": (
        "Green northern lights aurora borealis glowing over a snowy Finnish forest of pine trees at "
        "night, a few stars, peaceful arctic landscape, deep blues and greens, high quality editorial "
        "photography, horizontal 16:9. No text, no people, no buildings."
    ),
    "finnish-culture-midsummer": (
        "A traditional Finnish midsummer celebration at a lakeside: a small bonfire and folded wooden "
        "chairs near the water, birch branches as decoration, warm orange dusk light over a calm lake, "
        "festive but serene mood, high quality editorial photography, horizontal 16:9. No text, no people."
    ),
    "finnish-culture-coffee-pulla": (
        "A cosy Finnish coffee table with a glass pot of strong coffee and a plate of pulla cinnamon "
        "buns topped with pearl sugar, linen tablecloth and a candle, warm inviting Nordic home "
        "ambience, high quality editorial photography, horizontal 16:9. No text, no people."
    ),
    "finnish-culture-rye-table": (
        "A rustic Finnish meal table with dark rye bread, Karelian rice pies with egg butter, butter "
        "and salmon, on a wooden table with simple ceramics, warm natural light, traditional and "
        "appetizing Nordic food mood, high quality editorial photography, horizontal 16:9. No text, no people."
    ),
    "finnish-culture-winter-cottage": (
        "A classic red wooden Finnish cottage in deep snow, warm light glowing in small windows, "
        "snow-covered spruce trees around, soft blue twilight, cozy and still winter scene, high "
        "quality editorial photography, horizontal 16:9. No text, no people."
    ),
    "finnish-culture-foraging-berries": (
        "A close-up of a hand picking ripe lingonberries and blueberries from moss and low shrubs in "
        "a Finnish forest, soft dappled light, wooden basket partly visible, rewarding nature mood, "
        "high quality editorial photography, horizontal 16:9. No text no signage."
    ),
    "finnish-culture-helsinki": (
        "The Helsinki harbour waterfront on a bright day with white Neoclassical buildings, a ferry "
        "on the water, clean and modern Nordic city, clear sky, calm and airy mood, high quality "
        "editorial photography, horizontal 16:9. No text."
    ),
}

URL = "https://api.x.ai/v1/images/generations"


def generate(prompt):
    payload = {
        "model": "grok-imagine-image",
        "prompt": prompt,
        "n": 1,
        "response_format": "url",
        # modest quality to save tokens; "1k" alone yields 1280x720 horizontal
        "resolution": "1k",
    }
    req = urllib.request.Request(
        URL, data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=240) as resp:
        return json.loads(resp.read().decode("utf-8"))


def download(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "hermes-tier3"})
    with urllib.request.urlopen(req, timeout=240) as resp, open(dest, "wb") as f:
        f.write(resp.read())


def to_avif(src, dest):
    try:
        import PIL.Image
        im = PIL.Image.open(src).convert("RGB")
        if im.width > 1340:
            h = int(im.height * 1340 / im.width)
            im = im.resize((1340, h), PIL.Image.LANCZOS)
        im.save(dest, "AVIF", quality=52)
        return True
    except Exception as e:
        print(f"  avif conversion failed ({e}); leaving source")
        return False


def main():
    results = {}
    for name, prompt in IMAGES.items():
        src = OUT_DIR / f"{name}.tmp.jpg"
        avif = OUT_DIR / f"{name}.avif"
        if avif.exists():
            print(f"[skip] {name}.avif already present", flush=True)
            results[name] = "cached"
            continue
        print(f"[gen ] {name} ...", flush=True)
        ok = False
        for attempt in range(3):
            try:
                data = generate(prompt)
                if "error" in data:
                    raise RuntimeError(data["error"])
                url = data["data"][0]["url"]
                download(url, src)
                ok = True
                break
            except Exception as e:
                print(f"  attempt {attempt+1} failed: {e}", flush=True)
                time.sleep(4)
        if not ok:
            results[name] = "ERROR"
            continue
        if to_avif(src, avif):
            results[name] = "ok"
            src.unlink(missing_ok=True)
        else:
            jpg = OUT_DIR / f"{name}.jpg"
            src.replace(jpg)
            results[name] = "ok-jpg"
        print(f"  -> {avif.name} ({avif.stat().st_size if avif.exists() else jpg.stat().st_size} bytes)", flush=True)
    print("\n=== SUMMARY ===")
    for k, v in results.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()