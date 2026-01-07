#!/bin/bash

# Script to download and process Impressionist paintings for MindDump
# This script downloads 10 paintings and processes them to @2x and @3x sizes

set -e

# Create directories
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
TEMP_DIR="$PROJECT_DIR/temp_paintings"
ASSETS_DIR="$PROJECT_DIR/MindDump/Resources/Assets.xcassets"

mkdir -p "$TEMP_DIR"

echo "📥 Downloading 10 Impressionist paintings..."
echo "⚠️  Note: You'll need to manually download these from the sources provided:"
echo "   - The Met Museum API"
echo "   - Rawpixel"
echo "   - National Gallery of Art"
echo "   - PICRYL"
echo ""
echo "Suggested paintings (public domain):"
echo "1. Van Gogh - Wheat Field with Cypresses"
echo "2. Monet - Water Lilies"
echo "3. Renoir - Girl with a Watering Can"
echo "4. Cézanne - Mont Sainte-Victoire"
echo "5. Van Gogh - Starry Night Over the Rhone"
echo "6. Monet - The Artist's Garden at Giverny"
echo "7. Renoir - On the Terrace"
echo "8. Van Gogh - Almond Blossoms"
echo "9. Monet - Impression Sunrise"
echo "10. Cézanne - The Card Players"
echo ""
echo "📍 Please download these images to: $TEMP_DIR"
echo "   Name them: painting-01.jpg, painting-02.jpg, etc."
echo ""
read -p "Press Enter when you've downloaded the paintings to $TEMP_DIR..."

# Check if ImageMagick is installed
if ! command -v magick &> /dev/null && ! command -v convert &> /dev/null; then
    echo "❌ ImageMagick is not installed."
    echo "Install it with: brew install imagemagick"
    exit 1
fi

# Determine which command to use
if command -v magick &> /dev/null; then
    CONVERT_CMD="magick"
else
    CONVERT_CMD="convert"
fi

echo ""
echo "🖼️  Processing images..."

# Process each painting
for i in {01..10}; do
    INPUT="$TEMP_DIR/painting-$i.jpg"

    if [ ! -f "$INPUT" ]; then
        echo "⚠️  Warning: painting-$i.jpg not found, skipping..."
        continue
    fi

    echo "Processing painting-$i..."

    # @2x version (828x1792)
    OUTPUT_2X="$TEMP_DIR/painting-${i}@2x.jpg"
    $CONVERT_CMD "$INPUT" -resize 828x1792^ -gravity center -extent 828x1792 -quality 85 "$OUTPUT_2X"

    # @3x version (1170x2532)
    OUTPUT_3X="$TEMP_DIR/painting-${i}@3x.jpg"
    $CONVERT_CMD "$INPUT" -resize 1170x2532^ -gravity center -extent 1170x2532 -quality 85 "$OUTPUT_3X"

    echo "  ✅ Created @2x and @3x versions"
done

echo ""
echo "✅ Image processing complete!"
echo ""
echo "📋 Next steps:"
echo "1. Open Xcode and navigate to $ASSETS_DIR"
echo "2. For each painting (01-10):"
echo "   a. Right-click in Assets.xcassets → New Image Set"
echo "   b. Name it 'painting-XX-[description]' (e.g., painting-01-wheat-field)"
echo "   c. Drag the @2x image to the 2x slot"
echo "   d. Drag the @3x image to the 3x slot"
echo ""
echo "Processed images are in: $TEMP_DIR"
