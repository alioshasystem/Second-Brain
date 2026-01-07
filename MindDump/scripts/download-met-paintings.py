#!/usr/bin/env python3

"""
Download Impressionist paintings from The Met Museum API
Processes them to @2x and @3x sizes for iOS
"""

import os
import sys
import json
import urllib.request
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("❌ Pillow is not installed.")
    print("Install it with: pip3 install Pillow")
    sys.exit(1)

# The Met Museum API object IDs for Impressionist paintings
PAINTINGS = [
    {
        "id": 436532,  # Van Gogh - Wheat Field with Cypresses
        "name": "wheat-field-cypresses",
        "artist": "van-gogh"
    },
    {
        "id": 437980,  # Van Gogh - Irises
        "name": "irises",
        "artist": "van-gogh"
    },
    {
        "id": 436105,  # Monet - The Monet Family in Their Garden
        "name": "monet-garden",
        "artist": "monet"
    },
    {
        "id": 437009,  # Renoir - By the Seashore
        "name": "by-seashore",
        "artist": "renoir"
    },
    {
        "id": 435809,  # Cézanne - Still Life with Apples
        "name": "still-life-apples",
        "artist": "cezanne"
    },
    {
        "id": 437984,  # Van Gogh - Roses
        "name": "roses",
        "artist": "van-gogh"
    },
    {
        "id": 438817,  # Monet - Garden at Sainte-Adresse
        "name": "garden-sainte-adresse",
        "artist": "monet"
    },
    {
        "id": 437432,  # Renoir - A Waitress at Duval's Restaurant
        "name": "waitress",
        "artist": "renoir"
    },
    {
        "id": 436947,  # Cézanne - Madame Cézanne
        "name": "madame-cezanne",
        "artist": "cezanne"
    },
    {
        "id": 435882,  # Monet - Bridge Over a Pond of Water Lilies
        "name": "water-lilies-bridge",
        "artist": "monet"
    }
]

def download_painting(object_id, index, name, artist):
    """Download a painting from The Met Museum API"""
    api_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"

    print(f"\n📥 [{index}/10] Downloading {artist} - {name}...")

    try:
        # Get object data
        with urllib.request.urlopen(api_url) as response:
            data = json.loads(response.read())

        # Get primary image URL
        image_url = data.get("primaryImage")
        if not image_url:
            print(f"  ⚠️  No image available for object {object_id}")
            return None

        # Download image
        temp_file = f"temp_paintings/painting-{index:02d}-original.jpg"
        urllib.request.urlretrieve(image_url, temp_file)

        print(f"  ✅ Downloaded: {data.get('title', 'Unknown')}")
        return temp_file

    except Exception as e:
        print(f"  ❌ Error downloading: {e}")
        return None

def process_image(input_path, index, name):
    """Process image to @2x and @3x sizes"""
    print(f"  🖼️  Processing to @2x and @3x...")

    try:
        # Open image
        img = Image.open(input_path)

        # Convert to RGB if necessary
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # @2x version (828x1792)
        output_2x = f"temp_paintings/painting-{index:02d}@2x.jpg"
        img_2x = resize_and_crop(img, 828, 1792)
        img_2x.save(output_2x, 'JPEG', quality=85, optimize=True)

        # @3x version (1170x2532)
        output_3x = f"temp_paintings/painting-{index:02d}@3x.jpg"
        img_3x = resize_and_crop(img, 1170, 2532)
        img_3x.save(output_3x, 'JPEG', quality=85, optimize=True)

        print(f"  ✅ Created @2x (828x1792) and @3x (1170x2532)")

        return {
            "index": index,
            "name": name,
            "2x": output_2x,
            "3x": output_3x
        }

    except Exception as e:
        print(f"  ❌ Error processing: {e}")
        return None

def resize_and_crop(img, width, height):
    """Resize and crop image to exact dimensions"""
    # Calculate aspect ratios
    img_ratio = img.width / img.height
    target_ratio = width / height

    if img_ratio > target_ratio:
        # Image is wider, resize based on height
        new_height = height
        new_width = int(height * img_ratio)
    else:
        # Image is taller, resize based on width
        new_width = width
        new_height = int(width / img_ratio)

    # Resize
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Crop to exact size (center crop)
    left = (new_width - width) // 2
    top = (new_height - height) // 2
    right = left + width
    bottom = top + height

    return img.crop((left, top, right, bottom))

def create_asset_catalog_entries():
    """Create instructions for adding to Xcode"""
    print("\n" + "="*60)
    print("📋 NEXT STEPS: Add to Xcode Assets.xcassets")
    print("="*60)

    for i, painting in enumerate(PAINTINGS, 1):
        print(f"\n{i}. painting-{i:02d}-{painting['name']}")
        print(f"   Artist: {painting['artist'].title()}")
        print(f"   Files: painting-{i:02d}@2x.jpg, painting-{i:02d}@3x.jpg")

    print("\n" + "="*60)
    print("HOW TO ADD TO XCODE:")
    print("="*60)
    print("1. Open MindDump.xcodeproj in Xcode")
    print("2. Navigate to MindDump/Resources/Assets.xcassets")
    print("3. For each painting:")
    print("   a. Right-click → New Image Set")
    print("   b. Name: painting-XX-[description]")
    print("   c. Drag @2x image to 2x slot")
    print("   d. Drag @3x image to 3x slot")
    print("="*60)

def main():
    # Create temp directory
    os.makedirs("temp_paintings", exist_ok=True)

    print("🎨 Downloading and Processing Impressionist Paintings")
    print("="*60)

    processed = []

    # Download and process each painting
    for i, painting in enumerate(PAINTINGS, 1):
        original = download_painting(
            painting["id"],
            i,
            painting["name"],
            painting["artist"]
        )

        if original:
            result = process_image(original, i, painting["name"])
            if result:
                processed.append(result)

    print("\n" + "="*60)
    print(f"✅ Successfully processed {len(processed)}/10 paintings")
    print("="*60)

    create_asset_catalog_entries()

if __name__ == "__main__":
    main()
