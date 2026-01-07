# MindDump Setup Scripts

Automated scripts to download and configure assets and fonts for the MindDump iOS app.

## Quick Start

Run the master setup script to complete all tasks:

```bash
./scripts/setup-all.sh
```

This will:
1. Download 10 Impressionist paintings from The Met Museum API
2. Process images to @2x (828x1792) and @3x (1170x2532) sizes
3. Create image sets in Assets.xcassets
4. Download Inter-Regular.ttf font
5. Set up Info.plist with font configuration

## Individual Scripts

### `setup-all.sh`
Master script that runs all setup tasks in sequence.

**Usage:**
```bash
./scripts/setup-all.sh
```

### `download-met-paintings.py`
Downloads 10 Impressionist paintings from The Met Museum API and processes them to the correct sizes.

**Requirements:**
- Python 3
- Pillow (PIL) - installed automatically if missing

**Usage:**
```bash
python3 scripts/download-met-paintings.py
```

**Output:**
- `temp_paintings/painting-XX@2x.jpg` (828x1792, 85% quality)
- `temp_paintings/painting-XX@3x.jpg` (1170x2532, 85% quality)

**Paintings included:**
1. Van Gogh - Wheat Field with Cypresses
2. Van Gogh - Irises
3. Monet - The Monet Family in Their Garden
4. Renoir - By the Seashore
5. Cézanne - Still Life with Apples
6. Van Gogh - Roses
7. Monet - Garden at Sainte-Adresse
8. Renoir - A Waitress at Duval's Restaurant
9. Cézanne - Madame Cézanne
10. Monet - Bridge Over a Pond of Water Lilies

### `setup-asset-catalog.py`
Creates image sets in Assets.xcassets and copies the processed paintings.

**Requirements:**
- Python 3
- Processed paintings in `temp_paintings/`

**Usage:**
```bash
python3 scripts/setup-asset-catalog.py
```

**Output:**
- Creates `.imageset` directories in `MindDump/Resources/Assets.xcassets/`
- Copies images and creates Contents.json for each painting

### `download-inter-font.sh`
Downloads Inter-Regular.ttf font from the official repository.

**Usage:**
```bash
./scripts/download-inter-font.sh
```

**Output:**
- `MindDump/Resources/Fonts/Inter-Regular.ttf`

### `download-paintings.sh`
Alternative manual script with step-by-step guidance for downloading paintings.

**Usage:**
```bash
./scripts/download-paintings.sh
```

## Post-Setup Steps in Xcode

After running the scripts, complete these steps in Xcode:

### 1. Verify Font Target Membership

1. Open `MindDump.xcodeproj` in Xcode
2. In the Project Navigator, navigate to `MindDump/Resources/Fonts/`
3. Select `Inter-Regular.ttf`
4. In the File Inspector (right panel), ensure **MindDump** is checked under "Target Membership"
5. Repeat for `Alice-Regular.ttf`

### 2. Verify Info.plist

1. Select `MindDump/Info.plist` in the Project Navigator
2. Verify it contains:
   ```xml
   <key>UIAppFonts</key>
   <array>
       <string>Alice-Regular.ttf</string>
       <string>Inter-Regular.ttf</string>
   </array>
   ```

### 3. Build and Test

1. Press **CMD+B** to build
2. Fix any signing/provisioning issues if needed
3. Run the app to verify everything works

## Using the Assets in SwiftUI

### Images

```swift
// Use any of the 10 paintings
Image("painting-01-wheat-field-cypresses")
    .resizable()
    .aspectRatio(contentMode: .fill)

Image("painting-02-irises")
    .resizable()
    .aspectRatio(contentMode: .fit)
```

### Fonts

```swift
// Inter font
Text("Hello World")
    .font(.custom("Inter", size: 16))

// Alice font (already configured)
Text("Hello World")
    .font(.custom("Alice", size: 16))
```

## Troubleshooting

### Pillow not found
```bash
pip3 install Pillow
```

### ImageMagick not found (for manual script)
```bash
brew install imagemagick
```

### Font not appearing in app
1. Verify the font file is in `MindDump/Resources/Fonts/`
2. Check Target Membership in Xcode
3. Clean build folder (CMD+Shift+K) and rebuild
4. Verify Info.plist has correct font names

### Images not showing
1. Verify image sets are in `Assets.xcassets`
2. Check that Contents.json exists in each `.imageset`
3. Clean build folder and rebuild

## File Structure

```
MindDump/
├── MindDump/
│   ├── Resources/
│   │   ├── Assets.xcassets/
│   │   │   ├── painting-01-wheat-field-cypresses.imageset/
│   │   │   ├── painting-02-irises.imageset/
│   │   │   └── ... (10 total)
│   │   └── Fonts/
│   │       ├── Alice-Regular.ttf
│   │       └── Inter-Regular.ttf
│   └── Info.plist
└── scripts/
    ├── setup-all.sh
    ├── download-met-paintings.py
    ├── setup-asset-catalog.py
    ├── download-inter-font.sh
    └── download-paintings.sh
```

## Credits

- Paintings: The Metropolitan Museum of Art (public domain)
- Inter Font: Rasmus Andersson (Open Font License)
- Alice Font: Ksenia Erulevich (Open Font License)
