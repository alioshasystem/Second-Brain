# Note Creation Sheet - Implementation & Animation System

**Version:** 1.0
**Date:** 2026-01-10
**Status:** ✅ Implemented & Working

---

## Overview

Sistema de creación de notas con sheet modal que se expande dinámicamente basado en el contenido del texto. El sheet crece orgánicamente desde 30% de la pantalla hasta fullscreen, con animaciones fluidas y sin scrolling interno.

## Core Philosophy

**No Scrolling Inside Card**
- ❌ El contenido NUNCA scrollea dentro del card
- ✅ El TextEditor crece con el contenido
- ✅ El sheet se expande automáticamente cuando el contenido excede el espacio disponible

**Content-Driven Expansion**
- La altura del sheet está **controlada por el contenido**, no por scrolling
- Expansión smooth y continua (no abrupta)
- Painting background solo aparece al 100% de expansión

---

## Technical Architecture

### Component Structure

```
NoteCreationSheet.swift
├── ZStack (Overlay System)
│   ├── Color.black.opacity(0.3) - Dismiss overlay
│   ├── Painting Background + Header (conditional)
│   └── Content Card (VStack)
│       ├── TextField (Title)
│       ├── Text (Date)
│       ├── Divider
│       └── TextEditor (Content) - Dynamic height
│
NoteCreationViewModel.swift
├── SheetState enum
├── Expansion Progress Calculator
├── Auto-Save System
└── Note Creation Logic

String Extension
└── height(withConstrainedWidth:font:lineSpacing:) - Text measurement
```

### Key Files

| File | Purpose |
|------|---------|
| `NoteCreationSheet.swift` | UI & Animation orchestration |
| `NoteCreationViewModel.swift` | Business logic & state management |
| `String+Height.swift` (extension) | Text height calculation for dynamic sizing |

---

## Animation System

### 1. Sheet Expansion States

```swift
enum SheetState {
    case collapsed      // 30% of screen height
    case expanding      // Animated transition
    case expanded       // 100% of screen (fullscreen)
    case navigating     // Transitioning to NoteDetailView
}
```

### 2. Expansion Progress (0.0 → 1.0)

**Formula:**
```swift
func expansionProgress() -> CGFloat {
    let overflow = max(0, contentHeight - availableHeight)
    guard overflow > 0 else { return 0 }

    // Expand gradually over 300pt of overflow
    let progress = min(1.0, overflow / 300.0)
    return progress
}
```

**Key Points:**
- `progress = 0.0`: Content fits in collapsed sheet (30%)
- `progress = 0.0 → 1.0`: Content is overflowing, sheet expanding
- `progress = 1.0`: Triggers full expansion to fullscreen

### 3. Card Offset Calculation

```swift
private func cardOffsetY(geometry: GeometryProxy) -> CGFloat {
    let collapsedOffset = geometry.size.height * (1 - 0.3)  // 70% from top
    let expandedOffset = geometry.size.height * 0.42 - 24    // At 42% - 24pt

    // Smoothly interpolate based on expansion progress
    return collapsedOffset - (collapsedOffset - expandedOffset) * expansionProgress
}
```

**Visual:**
```
Collapsed (30%):
┌─────────────────┐
│                 │ } 70% (collapsedOffset)
│                 │
│                 │
│                 │
│┏━━━━━━━━━━━━━━┓│
││   Content    ││ } 30%
││     Card     ││
│┗━━━━━━━━━━━━━━┛│
└─────────────────┘

Expanded (100%):
┌─────────────────┐
│   🎨 Painting   │ } 42%
│                 │
├─────────────────┤ ← cardOffset (42% - 24pt)
│┏━━━━━━━━━━━━━━┓│
││   Content    ││
││     Card     ││ } 58% + 24pt
││              ││
││              ││
│┗━━━━━━━━━━━━━━┛│
└─────────────────┘
```

---

## Dynamic Text Height System

### Problem Solved

**Challenge:** SwiftUI's TextEditor doesn't provide content size natively. Need to calculate exact text height to:
1. Know when content overflows available space
2. Grow the TextEditor frame accordingly
3. Trigger sheet expansion at the right time

### Solution: UIKit Text Measurement

```swift
extension String {
    func height(withConstrainedWidth width: CGFloat,
                font: UIFont,
                lineSpacing: CGFloat = 6) -> CGFloat {

        let paragraphStyle = NSMutableParagraphStyle()
        paragraphStyle.lineSpacing = lineSpacing

        let constraintRect = CGSize(width: width, height: .greatestFiniteMagnitude)
        let boundingBox = self.boundingRect(
            with: constraintRect,
            options: [.usesLineFragmentOrigin, .usesFontLeading],
            attributes: [
                .font: font,
                .paragraphStyle: paragraphStyle
            ],
            context: nil
        )

        return ceil(boundingBox.height)
    }
}
```

### Height Update Flow

```swift
private func updateTextHeight(for text: String, width: CGFloat) {
    let font = UIFont.systemFont(ofSize: 16, weight: .regular)
    let textWidth = width - (Spacing.lg * 2)

    // Calculate ACTUAL text height
    let actualTextHeight = text.isEmpty ? 0 : text.height(
        withConstrainedWidth: textWidth,
        font: font,
        lineSpacing: 6
    )

    let calculatedHeight = actualTextHeight + 40  // Cursor padding

    // For UI: minimum 200pt for TextEditor
    textContentHeight = max(200, calculatedHeight)

    // For expansion: report ACTUAL height (prevents early expansion)
    viewModel?.updateContentHeight(calculatedHeight)
}
```

**Critical Distinction:**
- `textContentHeight` (UI): Minimum 200pt para que el TextEditor se vea bien
- `calculatedHeight` (Logic): Altura real del texto para determinar overflow

---

## Painting Background Behavior

### Visibility Rules

```swift
private var shouldShowPainting: Bool {
    // Only show when fully expanded
    isExpandedState
}

private var paintingOpacity: Double {
    isExpandedState ? 1.0 : 0.0
}
```

**Design Decision:**
- ❌ No gradual fade-in durante expansión
- ✅ Aparece instantáneamente al llegar a `sheetState = .expanded`
- Painting solo visible cuando `expansionProgress >= 1.0` y se dispara `triggerExpansion()`

**Why?**
- Evita distracciones visuales durante typing
- Transición clara entre "note creation" y "detail view mode"
- Mantiene foco en el contenido mientras escribes

---

## Animation Specifications

### Spring Animations

```swift
// Card offset animation
.animation(.spring(response: 0.3, dampingFraction: 0.85), value: expansionProgress)

// State transition animation
.animation(.spring(response: 0.4, dampingFraction: 0.8), value: viewModel?.sheetState)

// Painting fade-in
.animation(.easeInOut(duration: 0.3), value: paintingOpacity)
```

### Timing Parameters

| Element | Duration | Curve | Damping |
|---------|----------|-------|---------|
| Card offset | 300ms | Spring | 0.85 |
| State transition | 400ms | Spring | 0.8 |
| Painting fade | 300ms | EaseInOut | N/A |

**Spring Response:**
- `0.3s`: Quick, snappy feel para card movement
- `0.4s`: Slightly slower para state changes (more deliberate)

**Damping Fraction:**
- `0.85`: Minimal bounce en card offset (feels tight)
- `0.8`: Slight bounce en state transitions (feels organic)

---

## Available Height Calculation

### On Appear Setup

```swift
.onAppear {
    // Calculate available height in collapsed state (30% of screen)
    let screenHeight = UIScreen.main.bounds.height
    let collapsedSheetHeight = screenHeight * 0.3

    // Subtract fixed UI elements
    // Title (40pt) + Date (20pt) + Divider (30pt) + Padding (48pt) = 138pt
    let fixedUIHeight: CGFloat = 138
    let availableForContent = collapsedSheetHeight - fixedUIHeight

    viewModel?.availableHeight = availableForContent
}
```

**Example (iPhone 14 Pro):**
```
Screen height: 852pt
Collapsed sheet: 852 * 0.3 = 255.6pt
Fixed UI: 138pt
Available for content: 117.6pt
```

**Overflow Trigger:**
- Si `textContentHeight > 117.6pt` → `overflow > 0` → expansión comienza

---

## Auto-Expansion Trigger

### ViewModel Logic

```swift
func updateContentHeight(_ height: CGFloat) {
    contentHeight = height

    // Trigger full expansion when overflow reaches 100%
    if sheetState == .collapsed && expansionProgress() >= 1.0 {
        triggerExpansion()
    }
}

func triggerExpansion() {
    guard sheetState == .collapsed else { return }

    withAnimation(.spring(response: 0.4, dampingFraction: 0.8)) {
        sheetState = .expanding
    }

    Task {
        try? await Task.sleep(for: .milliseconds(400))
        sheetState = .expanded
        await createNote()
    }
}
```

**Flow:**
1. Usuario escribe texto
2. `updateTextHeight()` calcula altura actual
3. `updateContentHeight()` actualiza ViewModel
4. `expansionProgress()` calcula overflow ratio
5. Cuando `progress >= 1.0` → `triggerExpansion()`
6. Animación a fullscreen + crear nota en SwiftData

---

## Edge Cases & Solutions

### 1. Early Expansion (Fixed)

**Problem:** Card movía desde la primera palabra
**Cause:** Reportábamos `textContentHeight = max(200, ...)` al ViewModel
**Solution:**
```swift
// UI usa 200pt minimum
textContentHeight = max(200, calculatedHeight)

// Logic usa altura real
viewModel?.updateContentHeight(calculatedHeight)
```

### 2. Painting Shows Too Early (Fixed)

**Problem:** Background aparecía durante expansión gradual
**Cause:** `shouldShowPainting` usaba `expansionProgress > 0.5`
**Solution:**
```swift
private var shouldShowPainting: Bool {
    isExpandedState  // Solo cuando sheetState == .expanded
}
```

### 3. Internal Scrolling Conflict (Fixed)

**Problem:** Gestures conflictivos entre scroll y sheet drag
**Solution:**
```swift
TextEditor(...)
    .scrollDisabled(true)  // Nunca scrollea internamente
    .frame(height: max(200, textContentHeight))  // Crece dinámicamente
```

---

## User Interactions

### Gestures Supported

| Gesture | Action | State Requirement |
|---------|--------|-------------------|
| Tap overlay | Dismiss sheet (saves if content exists) | Any |
| Tap on card | Focus TextEditor | Any |
| Type text | Trigger auto-expansion when overflow | collapsed |
| Drag up (card) | Manual expansion (future) | collapsed |
| Drag down (card) | Dismiss sheet (future) | Any |

### Keyboard Behavior

```swift
@FocusState private var isTitleFocused: Bool

.onAppear {
    isTitleFocused = true  // Auto-focus title on appear
}
```

**Keyboard Avoidance:**
- SwiftUI maneja automáticamente con `.ignoresSafeArea(edges: .bottom)`
- Card offset ajusta para mantener contenido visible

---

## Performance Considerations

### Text Height Calculation

**Cost:** O(n) donde n = caracteres en texto
**Frequency:** Cada keystroke (onChange)
**Optimization:**
- Usa `UIFont.boundingRect()` nativo (muy rápido)
- No hay debounce necesario (< 1ms en devices modernos)

### Animation Performance

**60 FPS Target:**
- ✅ Spring animations son GPU-aceleradas
- ✅ Offset calculations son simples (linear interpolation)
- ✅ No re-renders innecesarios (usa `@Observable`)

### Memory

**Sheet Lifecycle:**
```swift
.onAppear { setupViewModel() }
.onDisappear { viewModel?.cleanup() }
```

`cleanup()` cancela:
- Auto-save tasks
- Ongoing animations
- Prevents memory leaks

---

## Integration with Note Detail View

### Visual Continuity

**Matching Elements:**
| Element | Creation Sheet | Detail View |
|---------|----------------|-------------|
| Painting height | 42% | 42% |
| Card offset | `height * 0.42 - 24pt` | `height * 0.42 - 24pt` |
| Corner radius | `Spacing.noteCardRadius` | `Spacing.noteCardRadius` |
| Shadow | Same specs | Same specs |
| Background | `Color.DS.noteCardBeige` | `Color.DS.noteCardBeige` |

**Seamless Transition:**
```swift
.onChange(of: viewModel?.createdNote) { _, newNote in
    if let note = newNote, viewModel?.sheetState == .expanded {
        Task {
            try? await Task.sleep(for: .milliseconds(100))
            onNoteCreated(note.id)  // Navigate
            dismissSheet()
        }
    }
}
```

Cuando expanded, el sheet es **visualmente idéntico** a NoteDetailView, permitiendo transición sin salto visual.

---

## Testing Checklist

- [x] Sheet aparece al tocar botón Handwrite
- [x] TextEditor crece con contenido (no scrolling interno)
- [x] Sheet permanece en 30% hasta que contenido excede espacio
- [x] Expansión smooth cuando contenido overflows
- [x] Painting solo aparece en fullscreen (no durante expansión)
- [x] Auto-save funciona correctamente (500ms debounce)
- [x] Nota se crea en SwiftData al expandir completamente
- [x] Navegación correcta a NoteDetailView
- [x] Dismiss al tap overlay (guarda si hay contenido)
- [x] Keyboard auto-focus en title
- [x] No memory leaks (cleanup on disappear)

---

## Future Enhancements

### Planned Features

1. **Manual Drag Gestures**
   ```swift
   .gesture(
       DragGesture()
           .onChanged { value in
               // Drag up → expand
               // Drag down → dismiss
           }
   )
   ```

2. **Haptic Feedback**
   - Light impact al empezar expansión
   - Medium impact al alcanzar fullscreen

3. **Expansion Threshold Configuration**
   ```swift
   private let expansionThreshold: CGFloat = 300  // Configurable
   ```

4. **Custom Transition Curves**
   - Diferentes spring curves por estado
   - Ease-in-out personalizado

5. **Content Preview During Expansion**
   - Mini-preview del painting emergiendo gradualmente
   - Parallax effect en header buttons

---

## Code Examples

### Minimal Implementation

```swift
// 1. Text height tracking
@State private var textContentHeight: CGFloat = 200

// 2. Dynamic TextEditor
TextEditor(text: $content)
    .scrollDisabled(true)
    .frame(height: max(200, textContentHeight))
    .onChange(of: content) { _, newValue in
        updateTextHeight(for: newValue)
    }

// 3. Sheet offset animation
.offset(y: cardOffsetY())
.animation(.spring(response: 0.3, dampingFraction: 0.85),
           value: expansionProgress)

// 4. Height calculation
private func updateTextHeight(for text: String) {
    let font = UIFont.systemFont(ofSize: 16)
    let actualHeight = text.height(withConstrainedWidth: width, font: font)
    textContentHeight = max(200, actualHeight + 40)
    viewModel?.updateContentHeight(actualHeight + 40)
}
```

### Key Modifier Chain

```swift
VStack { /* content */ }
    .padding(Spacing.lg)
    .background(Color.DS.noteCardBeige)
    .clipShape(.rect(topLeadingRadius: radius, topTrailingRadius: radius))
    .shadow(color: Color.DS.cardShadow, radius: shadowRadius, x: 0, y: 4)
    .offset(y: cardOffsetY)
    .animation(.spring(response: 0.3, dampingFraction: 0.85), value: progress)
    .animation(.spring(response: 0.4, dampingFraction: 0.8), value: state)
```

---

## Debugging Tips

### Common Issues

**Issue:** Card moves immediately when typing
**Check:**
- `updateContentHeight()` receiving actual height, not UI minimum?
- `availableHeight` calculated correctly in `onAppear`?

**Issue:** Painting shows during expansion
**Check:**
- `shouldShowPainting` only checks `isExpandedState`?
- Not using `expansionProgress` for visibility?

**Issue:** Jerky animations
**Check:**
- Using `.animation()` modifier, not `withAnimation {}` in body?
- Spring damping values reasonable (0.7-0.9)?

### Debug Overlays

```swift
// Add to card VStack
.overlay(alignment: .topTrailing) {
    VStack(alignment: .trailing, spacing: 4) {
        Text("Content: \(Int(textContentHeight))pt")
        Text("Available: \(Int(viewModel?.availableHeight ?? 0))pt")
        Text("Progress: \(Int(expansionProgress * 100))%")
        Text("State: \(String(describing: viewModel?.sheetState))")
    }
    .font(.system(size: 10, weight: .bold))
    .foregroundStyle(.red)
    .padding(8)
}
```

---

## References

### Related Files
- `NoteDetailView.swift` - Target visual state
- `NoteCreationViewModel.swift` - Business logic
- `NoteService.swift` - SwiftData persistence
- `FEATURE_NOTE_CREATION.md` - Original PRD

### Design System
- `Color.DS.*` - Design system colors
- `Spacing.*` - Design system spacing
- `.DS.title`, `.DS.body` - Typography

### Apple Documentation
- [UIFont boundingRect](https://developer.apple.com/documentation/uikit/uifont/1619955-boundingrect)
- [SwiftUI Spring Animations](https://developer.apple.com/documentation/swiftui/animation/spring(response:dampingfraction:blendDuration:))
- [TextEditor](https://developer.apple.com/documentation/swiftui/texteditor)

---

**Author:** Claude Sonnet 4.5
**Last Updated:** 2026-01-10
**Status:** Production Ready ✅
