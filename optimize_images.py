#!/usr/bin/env python3
"""
Ecoline images/  папкасындағы барлық суреттерді WebP-ке конверттейді
Іске қосу: python optimize_images.py
"""
import os
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("pip install Pillow деп орнат")
    sys.exit(1)

INPUT_DIR = Path(r"C:\Users\HP\Desktop\projects\ecoline\images")
OUTPUT_DIR = Path(r"C:\Users\HP\Desktop\projects\ecoline\images")
QUALITY = 82
MAX_WIDTH = 1920

exts = {'.jpg', '.jpeg', '.png', '.webp'}
converted = 0
saved_bytes = 0

for img_path in INPUT_DIR.rglob("*"):
    if img_path.suffix.lower() not in exts:
        continue
    if img_path.stem.endswith("_orig"):
        continue

    try:
        im = Image.open(img_path)
        orig_size = img_path.stat().st_size

        # Өлшемді кішірейт (егер MAX_WIDTH-тан үлкен болса)
        if im.width > MAX_WIDTH:
            ratio = MAX_WIDTH / im.width
            new_h = int(im.height * ratio)
            im = im.resize((MAX_WIDTH, new_h), Image.LANCZOS)

        # RGB-ке аудар (RGBA болса)
        if im.mode in ('RGBA', 'P'):
            im = im.convert('RGB')

        # WebP ретінде сақта
        out_path = img_path.with_suffix('.webp')
        im.save(out_path, 'WEBP', quality=QUALITY, method=6)

        new_size = out_path.stat().st_size
        saved = orig_size - new_size
        saved_bytes += saved

        # Ескі файлды өшір (тек .jpg/.jpeg/.png болса)
        if img_path.suffix.lower() in {'.jpg', '.jpeg', '.png'} and out_path != img_path:
            img_path.unlink()

        print(f"✓ {img_path.name} → {out_path.name} | {orig_size//1024}KB → {new_size//1024}KB (үнемдеу: {saved//1024}KB)")
        converted += 1

    except Exception as e:
        print(f"✗ {img_path.name}: {e}")

print(f"\n{'='*50}")
print(f"Барлығы: {converted} файл конвертталды")
print(f"Жалпы үнемдеу: {saved_bytes//1024//1024} MB")
