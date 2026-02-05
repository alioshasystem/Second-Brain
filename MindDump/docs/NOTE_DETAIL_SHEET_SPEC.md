# NoteDetailSheet - Functionality Specification

## Overview
Modal sheet for displaying and editing note details with multi-state expansion and swipe-to-dismiss functionality.

---

## Visual Layout

```
┌─────────────────────────────────┐
│                                 │
│   Video Background (42%)        │  ← Looping video
│                                 │
│   [←]              [bookmark]   │  ← Header overlay
│                                 │
├─────────────────────────────────┤
│ ╭───────────────────────────╮   │
│ │                           │   │
│ │  Note Title               │   │
│ │  [tags]                   │   │
│ │  ─────────────────        │   │  ← Note Content Card
│ │                           │   │     (Beige background)
│ │  Note content...          │   │
│ │                           │   │
│ │                           │   │
│ │                      [+]  │   │  ← FAB button
│ ╰───────────────────────────╯   │
└─────────────────────────────────┘
```

---

## Intended Behavior

### 1. Initial Appearance
**Expected**: Sheet smoothly animates from bottom of screen to **60% collapsed position**

**Animation**:
- Duration: 0.4s
- Spring: response 0.4, damping 0.8
- Starts: Offscreen (dismissalProgress = 1.0)
- Ends: 60% position (dismissalProgress = 0.0, expansionProgress = 0.0)

**Visual State**:
- Video background visible at top (42% of screen)
- Header buttons overlay on video
- Note card appears at 60% screen height
- Card has rounded top corners
- Semi-transparent black overlay behind card

---

### 2. Collapsed State (60%)
**Card Position**: 40% from top of screen (60% height)
**Video Visible**: Yes
**Gestures Enabled**:
- ✅ Swipe up → Expand to 90%
- ✅ Swipe down (from top of scroll) → Dismiss
- ✅ Scroll within note content

**Threshold for Expansion**:
- Drag up > 100pt → Expand to 90%
- Drag up < 100pt → Spring back to 60%
- Fast swipe (velocity > 1000) → Expand immediately

---

### 3. Expanded State (90%)
**Card Position**: 10% from top of screen (90% height)
**Video Visible**: Partially (minimal)
**Gestures Enabled**:
- ✅ Scroll within note content
- ✅ Swipe down (when at scroll top) → Collapse or Dismiss

**Thresholds for Collapse/Dismiss**:
- Drag down > 100pt → **Collapse to 60%** (never dismiss directly from expanded)
- Drag down < 100pt → **Spring back to 90%**

---

### 4. Dismissal
**Trigger Conditions**:
- Swipe down > 150pt from collapsed state (60%)
- Tap on semi-transparent overlay
- Tap back arrow button

**Animation**:
- Card slides down offscreen
- Overlay fades out
- Video fades out
- Duration: 0.4s spring animation

**Auto-save**: All changes saved before dismissal

---

## Scrolling Behavior

### When Collapsed (60%)
- Content should scroll naturally within the card
- No visible bottom margin/empty space
- TextEditor should appear "infinitely long" downward
- Bounce at top when scrolled up
- Swipe down from scroll top triggers dismiss

### When Expanded (90%)
- Content scrolls within larger card space
- No visible bottom margin/empty space
- Swipe down from scroll top triggers collapse/dismiss logic
- Scroll indicator visible when content overflows

### Scroll Position Tracking
- `isScrollAtTop` tracked by ScrollableContentContainerView
- Used to determine if swipe-down gestures should trigger sheet actions
- Only allow sheet dismissal/collapse when scrolled to top

---

## Gesture Recognition Priority

### Pan Gesture Rules
1. **Upward drag when collapsed** → Sheet expansion (coordinator handles)
2. **Downward drag when expanded AND at top** → Sheet collapse/dismiss (coordinator handles)
3. **Downward drag when collapsed AND at top** → Sheet dismiss (coordinator handles)
4. **Scroll in middle of content** → Normal scrolling (ScrollView handles)

### Simultaneous Gestures
- Sheet pan gesture and ScrollView pan gesture can both evaluate
- Sheet gesture takes priority when at scroll top
- ScrollView waits for sheet gesture to fail when at top

---

## Component Architecture

### Files
- `NoteDetailSheet.swift` - Main sheet view with layout and state
- `NoteDetailViewModel.swift` - State management and business logic
- `NoteDetailSwipeDismissCoordinator.swift` - Gesture handling
- `NoteDetailContent.swift` - Note content (title, tags, text)
- `ScrollableContentContainerView.swift` - UIScrollView wrapper for tracking

### State Management
```swift
// Sheet states
enum SheetState {
    case collapsed   // 60% height
    case expanded    // 90% height
    case dismissing  // Animating out
}

// Progress values (0.0 - 1.0)
- expansionProgress: Interpolates between collapsed and expanded
- dismissalProgress: Tracks swipe-to-dismiss animation
```

### Height Calculations
```swift
// Screen height percentages
videoHeightRatio: 0.42      // Video background
collapsedHeightRatio: 0.60  // Collapsed card
expandedHeightRatio: 0.90   // Expanded card

// Card offset calculation
collapsedOffset = screenHeight × (1 - 0.60) = 40% from top
expandedOffset = screenHeight × (1 - 0.90) = 10% from top

// Interpolated based on expansionProgress
actualOffset = collapsedOffset - ((collapsedOffset - expandedOffset) × expansionProgress)
```

---

## Previous Fix Attempt Summary (V1)

**What was tried:**
- Replaced SwiftUI `TextEditor` with `ScrollableTextEditorView` (isScrollEnabled=false)
- Added Design System fonts/colors to ScrollableTextEditorView
- Changed `onAppear` to `.task` for better timing
- Added `contentInsetAdjustmentBehavior = .never` to ScrollableContentContainerView
- Added content height enforcement in `updateUIView`

**Result:** Scrolling while typing now works but other issues persist.

---

## Current Issues (Investigation V2)

### 🐛 Issue 1: Text Content Overflows Screen
**Root Cause:** `NoteDetailContent.swift:51` has **112pt total bottom padding**:
- `Spacing.lg` (24pt) on all sides (line 50)
- `Spacing.fabSize + Spacing.xl` (56pt + 32pt = 88pt) extra bottom (line 51)

The FAB padding was meant for the FAB button overlay, but it's inside the scroll content, pushing text up and leaving empty space below.

**Fix:** Remove the FAB bottom padding entirely.

---

### 🐛 Issue 2: 90% View Still Has Margin Below
**Root Cause:** `ScrollableContentContainerView.swift:65` forcibly sets `contentSize.height = minHeight`:
```swift
if minHeight > 0 && scrollView.contentSize.height < minHeight {
    scrollView.contentSize.height = minHeight  // Creates artificial empty space
}
```
This adds empty space when content is shorter than visible frame.

Additionally, UIHostingController inside the scroll view automatically adds safe area insets to content.

**Fix:** Remove the contentSize forcing code and disable UIHostingController's automatic safe area insets with `safeAreaRegions = []` (iOS 16.4+).

---

### 🐛 Issue 3: From 90%, Should Collapse to 60% Before Dismiss
**Root Cause:** In `NoteDetailSwipeDismissCoordinator.swift:131-145`, the logic exists:
```swift
if downwardDistance > dismissThreshold {           // 150+ pixels → DISMISS
    await viewModel.triggerDismissal()
} else if downwardDistance > expansionThreshold {  // 100-149 pixels → COLLAPSE
    viewModel.triggerCollapse()
}
```

The issue is that **150pt threshold is too easy to reach** - users expecting a two-step process (90%→60%→dismiss) are accidentally dismissing directly.

**Fix:** From expanded state (90%), ALWAYS collapse to 60% first - never dismiss directly. Only allow dismiss from collapsed state (60%).

---

## Testing Checklist

### Initial Appearance
- [ ] Sheet animates smoothly from bottom
- [ ] Lands at exactly 60% screen height
- [ ] Video background visible
- [ ] No flicker or height jump
- [ ] Overlay fades in smoothly

### Collapsed State (60%)
- [ ] Content scrolls normally
- [ ] No bottom margin visible
- [ ] Swipe up expands to 90%
- [ ] Swipe down dismisses
- [ ] Can scroll while typing

### Expanded State (90%)
- [ ] Content scrolls normally
- [ ] No bottom margin visible
- [ ] Swipe down 150pt+ dismisses
- [ ] Swipe down 100-149pt collapses to 60%
- [ ] Swipe down <100pt springs back
- [ ] Can scroll while typing

### Dismissal
- [ ] Tap overlay dismisses
- [ ] Back button dismisses
- [ ] Changes auto-saved
- [ ] Smooth animation out

### Edge Cases
- [ ] Very short notes (less than screen height)
- [ ] Very long notes (multiple screens)
- [ ] Rapid state transitions
- [ ] Interrupting animations
- [ ] Keyboard appearance/dismissal

---

## Design Tokens

### Colors
- Card Background: `Color.DS.noteCardBeige`
- Text: `Color.DS.primary`
- Overlay: `Color.black.opacity(0.5)`
- Shadow: `Color.DS.cardShadow`

### Spacing
- Card corners: `Spacing.noteCardRadius`
- Content padding: `Spacing.lg`
- Bottom padding: `Spacing.fabSize + Spacing.xl`
- Shadow radius: `Spacing.noteCardShadowRadius`

### Typography
- Title: `.font(.DS.title)` (Alice font)
- Body: `.font(.DS.body)` (Inter font)

### Animations
- State transitions: `.spring(response: 0.3, dampingFraction: 0.85)`
- Initial appearance: `.spring(response: 0.4, dampingFraction: 0.8)`
- Dismissal: `.spring(response: 0.4, dampingFraction: 0.8)`

---

## Future Enhancements

### Potential Improvements
- [ ] Haptic feedback on state transitions
- [ ] Keyboard-aware height adjustments
- [ ] Drag indicator visual affordance
- [ ] Smooth video fade during expansion
- [ ] Performance optimization for large notes
- [ ] Gesture conflict resolution improvements
- [ ] Accessibility improvements (VoiceOver support)
