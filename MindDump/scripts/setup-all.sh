#!/bin/bash

# Master setup script for MindDump assets and fonts
# This script runs all setup tasks in the correct order

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "🎨 MindDump - Assets & Fonts Setup"
echo "="*60
echo ""

# Check dependencies
echo "📋 Checking dependencies..."

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    echo "Install it with: brew install python3"
    exit 1
fi
echo "  ✅ Python 3 found"

# Check for Pillow
if ! python3 -c "import PIL" &> /dev/null 2>&1; then
    echo "  ⚠️  Pillow (PIL) not found, installing..."
    pip3 install Pillow
fi
echo "  ✅ Pillow (PIL) found"

# Check for curl
if ! command -v curl &> /dev/null; then
    echo "❌ curl is not installed"
    exit 1
fi
echo "  ✅ curl found"

# Check for unzip
if ! command -v unzip &> /dev/null; then
    echo "❌ unzip is not installed"
    exit 1
fi
echo "  ✅ unzip found"

echo ""
echo "="*60
echo "Step 1/3: Downloading and processing paintings"
echo "="*60
echo ""

cd "$PROJECT_DIR"
python3 scripts/download-met-paintings.py

echo ""
echo "="*60
echo "Step 2/3: Setting up Assets.xcassets"
echo "="*60
echo ""

python3 scripts/setup-asset-catalog.py

echo ""
echo "="*60
echo "Step 3/3: Downloading Inter font"
echo "="*60
echo ""

bash scripts/download-inter-font.sh

echo ""
echo "="*60
echo "✅ ALL TASKS COMPLETED!"
echo "="*60
echo ""
echo "📋 Summary:"
echo "  ✅ Downloaded and processed 10 Impressionist paintings"
echo "  ✅ Created image sets in Assets.xcassets"
echo "  ✅ Downloaded Inter-Regular.ttf font"
echo "  ✅ Created Info.plist with font configuration"
echo ""
echo "🔧 IMPORTANT: Final steps in Xcode"
echo "="*60
echo "1. Open MindDump.xcodeproj in Xcode"
echo ""
echo "2. Verify fonts in Project Navigator:"
echo "   • MindDump/Resources/Fonts/Alice-Regular.ttf"
echo "   • MindDump/Resources/Fonts/Inter-Regular.ttf"
echo "   For each font:"
echo "     - Select the file"
echo "     - In File Inspector (right panel)"
echo "     - ✅ Ensure 'MindDump' is checked under Target Membership"
echo ""
echo "3. Verify Info.plist:"
echo "   • MindDump/Info.plist should be visible"
echo "   • It should contain UIAppFonts array with both fonts"
echo ""
echo "4. Build and test the app:"
echo "   • CMD+B to build"
echo "   • Fix any signing/provisioning issues if needed"
echo ""
echo "5. To use the assets in SwiftUI:"
echo '   • Images: Image("painting-01-wheat-field-cypresses")'
echo '   • Fonts: .font(.custom("Inter", size: 16))'
echo ""
echo "="*60

# Cleanup temp directories
echo ""
read -p "🗑️  Clean up temporary files? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Cleaning up..."
    rm -rf "$PROJECT_DIR/temp_paintings"
    rm -rf "$PROJECT_DIR/temp_fonts"
    echo "✅ Cleanup complete"
fi

echo ""
echo "🎉 Setup complete! Happy coding!"
