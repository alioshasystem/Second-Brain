#!/usr/bin/env python3

"""
Automatically create image sets in Assets.xcassets for the paintings
"""

import os
import json
import shutil
from pathlib import Path

# Painting names from the download script
PAINTINGS = [
    {"index": 1, "name": "wheat-field-cypresses", "artist": "van-gogh"},
    {"index": 2, "name": "irises", "artist": "van-gogh"},
    {"index": 3, "name": "monet-garden", "artist": "monet"},
    {"index": 4, "name": "by-seashore", "artist": "renoir"},
    {"index": 5, "name": "still-life-apples", "artist": "cezanne"},
    {"index": 6, "name": "roses", "artist": "van-gogh"},
    {"index": 7, "name": "garden-sainte-adresse", "artist": "monet"},
    {"index": 8, "name": "waitress", "artist": "renoir"},
    {"index": 9, "name": "madame-cezanne", "artist": "cezanne"},
    {"index": 10, "name": "water-lilies-bridge", "artist": "monet"}
]

def create_image_set(assets_dir, painting):
    """Create an image set in Assets.xcassets"""
    index = painting["index"]
    name = painting["name"]

    # Create imageset directory
    imageset_name = f"painting-{index:02d}-{name}"
    imageset_path = os.path.join(assets_dir, f"{imageset_name}.imageset")

    print(f"  Creating {imageset_name}...")

    # Create directory
    os.makedirs(imageset_path, exist_ok=True)

    # Check if image files exist
    img_2x = f"temp_paintings/painting-{index:02d}@2x.jpg"
    img_3x = f"temp_paintings/painting-{index:02d}@3x.jpg"

    if not os.path.exists(img_2x) or not os.path.exists(img_3x):
        print(f"    ⚠️  Warning: Images not found for painting {index:02d}")
        return False

    # Copy images to imageset
    shutil.copy(img_2x, os.path.join(imageset_path, f"{imageset_name}@2x.jpg"))
    shutil.copy(img_3x, os.path.join(imageset_path, f"{imageset_name}@3x.jpg"))

    # Create Contents.json
    contents = {
        "images": [
            {
                "filename": f"{imageset_name}@2x.jpg",
                "idiom": "universal",
                "scale": "2x"
            },
            {
                "filename": f"{imageset_name}@3x.jpg",
                "idiom": "universal",
                "scale": "3x"
            }
        ],
        "info": {
            "author": "xcode",
            "version": 1
        }
    }

    contents_path = os.path.join(imageset_path, "Contents.json")
    with open(contents_path, 'w') as f:
        json.dump(contents, f, indent=2)

    print(f"    ✅ Created successfully")
    return True

def main():
    # Get paths
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent
    assets_dir = project_dir / "MindDump" / "Resources" / "Assets.xcassets"

    print("🎨 Setting up Assets.xcassets image sets")
    print("="*60)

    # Check if assets directory exists
    if not assets_dir.exists():
        print(f"❌ Assets directory not found: {assets_dir}")
        return

    # Check if temp_paintings exists
    temp_dir = project_dir / "temp_paintings"
    if not temp_dir.exists():
        print(f"❌ Temp paintings directory not found: {temp_dir}")
        print("   Please run download-met-paintings.py first")
        return

    print(f"Assets directory: {assets_dir}")
    print(f"Temp directory: {temp_dir}")
    print()

    # Change to project directory
    os.chdir(project_dir)

    # Create image sets
    created = 0
    for painting in PAINTINGS:
        if create_image_set(str(assets_dir), painting):
            created += 1

    print()
    print("="*60)
    print(f"✅ Successfully created {created}/{len(PAINTINGS)} image sets")
    print("="*60)
    print()
    print("📋 Image sets created:")
    for painting in PAINTINGS:
        print(f"  • painting-{painting['index']:02d}-{painting['name']}")
    print()
    print("You can now use these in SwiftUI:")
    print('  Image("painting-01-wheat-field-cypresses")')
    print('  Image("painting-02-irises")')
    print("  etc.")

if __name__ == "__main__":
    main()
