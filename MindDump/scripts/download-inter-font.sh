#!/bin/bash

# Script to download Inter font for MindDump

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
FONTS_DIR="$PROJECT_DIR/MindDump/Resources/Fonts"
TEMP_DIR="$PROJECT_DIR/temp_fonts"

echo "📥 Downloading Inter font..."

# Create temp directory
mkdir -p "$TEMP_DIR"

# Download Inter font from GitHub
INTER_URL="https://github.com/rsms/inter/releases/download/v4.0/Inter-4.0.zip"

echo "  Downloading from: $INTER_URL"
curl -L "$INTER_URL" -o "$TEMP_DIR/Inter.zip"

# Extract
echo "  Extracting..."
unzip -q "$TEMP_DIR/Inter.zip" -d "$TEMP_DIR"

# Find and copy Inter-Regular.ttf
if [ -f "$TEMP_DIR/Inter Desktop/Inter-Regular.ttf" ]; then
    echo "  Copying Inter-Regular.ttf to $FONTS_DIR/"
    cp "$TEMP_DIR/Inter Desktop/Inter-Regular.ttf" "$FONTS_DIR/"
    echo "  ✅ Inter-Regular.ttf installed!"
elif [ -f "$TEMP_DIR/Inter-Regular.ttf" ]; then
    echo "  Copying Inter-Regular.ttf to $FONTS_DIR/"
    cp "$TEMP_DIR/Inter-Regular.ttf" "$FONTS_DIR/"
    echo "  ✅ Inter-Regular.ttf installed!"
else
    echo "  ❌ Could not find Inter-Regular.ttf in the downloaded archive"
    echo "  Trying alternative download method..."

    # Alternative: Download directly from Google Fonts
    echo "  Downloading from Google Fonts..."
    GFONTS_URL="https://fonts.google.com/download?family=Inter"
    curl -L "$GFONTS_URL" -o "$TEMP_DIR/Inter-GFonts.zip"
    unzip -q "$TEMP_DIR/Inter-GFonts.zip" -d "$TEMP_DIR/Inter-GFonts"

    # Look for static or variable fonts
    REGULAR_FONT=$(find "$TEMP_DIR/Inter-GFonts" -name "*Regular.ttf" | head -1)

    if [ -n "$REGULAR_FONT" ]; then
        echo "  Found: $REGULAR_FONT"
        cp "$REGULAR_FONT" "$FONTS_DIR/Inter-Regular.ttf"
        echo "  ✅ Inter-Regular.ttf installed!"
    else
        echo "  ❌ Could not find Inter-Regular.ttf"
        exit 1
    fi
fi

# Clean up
echo "  Cleaning up temp files..."
rm -rf "$TEMP_DIR"

echo ""
echo "✅ Inter font successfully downloaded to:"
echo "   $FONTS_DIR/Inter-Regular.ttf"
echo ""
echo "📋 Next steps:"
echo "1. Open Xcode project"
echo "2. Verify Inter-Regular.ttf is in the project navigator"
echo "3. Select the font file and check:"
echo "   ✅ Target Membership: MindDump"
echo "4. The Info.plist will be created automatically by the setup script"
