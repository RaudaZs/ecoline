#!/usr/bin/env python3
"""
assets/downlowds/output/ папкасындағы барлық PNG фотоларды WebP-ке конверттейді
Іске қосу: python optimize_assets.py
"""
import os
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("pip install Pillow деп орнат")
    sys.exit(1)

INPUT_DIR = Path(r"C:\Users\HP\Desktop\projects\ecoline\assets")
QUALITY = 80
MAX_WIDTH = 1920

exts = {'.jpg', '.jpeg', '.png'}
converted = 0
saved_bytes = 0

for img_path in INPUT_DIR.rglob("*"):
    if img_path.suffix.lower() not in exts:
        continue

    try:
        im = Image.open(img_path)
        orig_size = img_path.stat().st_size

        # Өлшемді кішірейт
        if im.width > MAX_WIDTH:
            ratio = MAX_WIDTH / im.width
            new_h = int(im.height * ratio)
            im = im.resize((MAX_WIDTH, new_h), Image.LANCZOS)

        # RGB-ке аудар
        if im.mode in ('RGBA', 'P'):
            im = im.convert('RGB')

        # WebP ретінде сақта
        out_path = img_path.with_suffix('.webp')
        im.save(out_path, 'WEBP', quality=QUALITY, method=6)

        new_size = out_path.stat().st_size
        saved = orig_size - new_size
        saved_bytes += saved

        # Ескі файлды өшір
        img_path.unlink()

        print(f"✓ {img_path.name} → {out_path.name} | {orig_size//1024}KB → {new_size//1024}KB")
        converted += 1

    except Exception as e:
        print(f"✗ {img_path.name}: {e}")

print(f"\n{'='*50}")
print(f"Барлығы: {converted} файл конвертталды")
print(f"Жалпы үнемдеу: {saved_bytes//1024//1024} MB")
