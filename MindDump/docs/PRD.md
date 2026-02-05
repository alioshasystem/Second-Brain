# Product Requirements Document (PRD)
## MindDump - Notetaking App

**Version:** 1.0 MVP
**Platform:** iOS (Swift)
**Target Device:** iPhone 11 and newer

---

## 1. Overview

### 1.1 Purpose
MindDump is a minimalist notetaking application designed for rapid capture and organization of thoughts. The app emphasizes quick note creation through multiple input methods (typing, voice dictation) and provides a simple tag-based organization system.

### 1.2 Core Value Proposition
- Fast note capture with minimal friction
- Voice-to-text transcription for hands-free note creation
- Simple tag-based organization
- Swipe-based note prioritization for quick triage

### 1.3 Target User
Individuals who need to quickly capture thoughts, ideas, or information throughout their day without complex organizational overhead. Users who prefer a clean, distraction-free interface.

---

## 2. Features (MVP Scope)

### 2.1 Core Features (Fully Functional)

#### P0 - Note Management

| Feature | Description | User Story |
|---------|-------------|------------|
| **View Notes List** | Display all notes as glassmorphism cards with title and preview text | As a user, I can see all my notes in a scrollable list to quickly find what I need |
| **View Note Detail** | Display full note content with title, last modified date, tags, and content | As a user, I can tap a note to see its full content |
| **Create Note (Voice)** | Create notes via voice dictation with automatic transcription | As a user, I can speak my thoughts and have them saved as a note |
| **Top Navigation Menu** | Access settings and filters via expandable menu from header | As a user, I can access app settings and navigation options |

#### P1 - Voice Input

| Feature | Description | User Story |
|---------|-------------|------------|
| **Voice Dictation** | Record voice and create note from transcription | As a user, I can speak my thoughts and have them saved as a note |

#### P3 - Settings & Navigation

| Feature | Description | User Story |
|---------|-------------|------------|
| **Settings Screen** | View list of settings options and access prioritization | As a user, I can access app settings |
| **Navigate Back** | Return to previous screen via back button | As a user, I can navigate back from any detail view |

---

### 2.2 Intentionally Non-Functional Features (MVP)

The following features are visible in the UI but are **intentionally non-functional placeholders** in the MVP. They display an alert or perform no action when tapped.

| Feature | UI Element | MVP Behavior |
|---------|-----------|--------------|
| **Scan (Camera)** | Action Menu - Camera icon | Displays "Camera scan feature coming soon!" alert |
| **Transcribe (Link)** | Action Menu - Link icon | Same behavior as Dictate (placeholder) |
| **Show Original** | Note Actions Menu - Eye icon | Displays placeholder alert |
| **Make To-Do's** | Note Actions Menu - CheckSquare icon | Displays placeholder alert |
| **Find Related Notes** | Note Actions Menu - Search icon | Displays placeholder alert |
| **Remind Me** | Note Actions Menu - Bell icon | Displays placeholder alert |
| **Search** | Header - Search icon | No action (button present but non-functional) |
| **Account** | Settings - User icon | No action |
| **Personalize** | Settings - Palette icon | No action |
| **Privacy** | Settings - Lock icon | No action |
| **Terms of Services** | Settings - FileText icon | No action |
| **About** | Settings - Info icon | No action |
| **Feedback** | Settings - MessageSquare icon | No action |
| **Sign out** | Settings - LogOut icon | No action |
| **Get Pro** | Settings - Upgrade card | No action |

---

## 3. UI / UX Requirements

### 3.1 Navigation Structure

```
Notes List (Home)
├── Note Detail
│   └── Note Actions Menu (overlay)
├── Blank Note Editor
├── Top Navigation Menu (expandable from header)
│   ├── All Notes
│   └── Settings
├── Dictate Sheet
└── Settings
```

**Single-Page Navigation:** The app focuses on a single notes list view with an expandable top menu for navigation to settings and filters.

### 3.2 Layout Specifications

#### 3.2.1 Notes List View
- **Background:** Warm beige tone (#F5F3ED - rgb(0.96, 0.95, 0.93))
- **Header:**
  - Title "NOTAS" in Alice font (24pt)
  - Menu button (hamburger icon) on the right that toggles to X when menu is open
  - Background: Same warm beige as page background
  - Shadow: Subtle shadow (black 10% opacity, 8pt radius, 0x 4y offset) to separate from content
- **Top Navigation Menu (Expandable):**
  - Grows downward from header when menu button is pressed
  - Contains menu options in Alice font (20pt):
    - "Todas las notas"
    - "Configuración"
  - Each option separated by thin divider line (primary color 10% opacity)
  - Same beige background as header
  - Overlay darkens notes below by 10% when open
  - Notes do not move/reflow when menu expands
- **Content:** Vertically scrolling list of note cards with glassmorphism styling
- **FAB:** Black circular button (60pt diameter) with note icon, bottom-right corner (20pt right, 24pt bottom)

#### 3.2.2 Note Card (Glassmorphism)
- **Background:** Liquid glass effect
  - Semi-transparent white (70% opacity)
  - Ultra-thin material backdrop blur
  - White border (50% opacity, 1pt width)
  - Shadow: black 8% opacity, 16pt radius, 0x 4y offset
  - Rounded corners: 16pt radius
- **Padding:** 20pt all sides
- **Top row:**
  - Bookmark icon (filled, 16pt, primary color) on left
  - Options menu icon (ellipsis, 16pt, primary color) on right
- **Title:** Alice font, 16pt, primary color, max 2 lines
- **Preview text:** System font, 14pt, muted foreground color, max 3 lines
- **Spacing:** 12pt between elements (vertical)
- **Animations:**
  - Press: Scale to 0.98 with spring animation
  - List entry: Staggered fade-in with scale (0.95 to 1.0), 50ms delay per card
  - Smooth spring transitions (0.3s response, 0.8 damping)

#### 3.2.3 Note Detail View
- **Header:** Back button, "All Notes" label, Search icon, Settings icon
- **Content:** Title (24pt bold), Last Modified date, Tags with chevron, Full content
- **Promote Button:** Circular toggle button (40pt diameter) with arrow-up icon
- **FAB:** Black circular button with Origami icon, opens Note Actions Menu

#### 3.2.4 Settings View
- **Header:** Back button, "Settings" title
- **Content:**
  - Upgrade card (white, rounded, contains "Get Pro" button)
  - Options list (white, rounded, icon + label rows)
- **Options:** Account, Personalize, Privacy, Terms of Services, About, Feedback, Sign out

#### 3.2.5 Blank Note Editor
- **Header:** Back button, "New Note" label, Check (save) button
- **Content:** Title input (24pt, no border), Content textarea (full height)

#### 3.2.6 Action Menu (Overlay)
- Dark overlay (50% opacity)
- Vertical stack of action buttons (56pt circles, white) with labels (black pill badges)
- Actions: Transcribe (Link), Dictate (Mic), Scan (Camera), Write (PenLine)
- Close button replaces FAB (black circle with X)

#### 3.2.7 Note Actions Menu (Overlay)
- Same structure as Action Menu
- Actions: Show Original (Eye), Make To-Do's (CheckSquare), Find Related Notes (Search), Remind Me (Bell)

#### 3.2.8 Dictate Sheet (Bottom Sheet)
- Drag handle bar
- Title "Voice Dictation" with close button
- Large microphone button (80pt, toggles red when recording)
- Status text ("Tap to start recording" / "Recording...")
- Transcription display area (gray background)
- Cancel and Save Note buttons

#### 3.2.9 Tags Drawer (Bottom Sheet)
- Drag handle bar
- Title "Filter by Tag" with close button
- Scrollable list of tag buttons
- "All Notes" option at top
- Selected tag highlighted (black background, white text)

### 3.3 Color System

| Token | Value | Usage |
|-------|-------|-------|
| Primary | `#030213` (near-black) | Primary buttons, FAB, text |
| Background | `#FFFFFF` | Cards, sheets (with glassmorphism overlay) |
| Background Secondary | `#F5F3ED` (warm beige) | Main screen background |
| Muted | `#ECECF0` | Secondary backgrounds |
| Muted Foreground | `#717182` | Secondary text |
| Border | `rgba(0,0,0,0.1)` | Subtle borders |
| Destructive | `#D4183D` | Recording state, errors |

### 3.4 Typography

**Primary Font:** Alice (Google Fonts)
- Used for: Main headings ("NOTAS"), note titles, menu options
- Sizes: 24pt (main header), 20pt (menu options), 16pt (note titles)

**System Font:** San Francisco (iOS default)
- Used for: Body text, preview text, secondary content
- Base font size: 16px
- Font weights: Normal (400), Medium (500)
- Body text: 16pt normal weight
- Caption text: 14pt normal weight
- Label text: 12pt normal weight

### 3.5 Iconography

Uses Lucide icon set:
- Plus, X, ArrowLeft, ArrowUp
- Search, Settings, MoreVertical, ChevronDown, ChevronRight
- Mic, MicOff, Camera, PenLine, Link
- User, Palette, Lock, FileText, Info, MessageSquare, LogOut, ListOrdered
- CheckSquare, Bell, Eye, Origami, Heart

### 3.6 Animations & Transitions

- **Top menu expansion:** Grows from header with spring animation (0.3s response, 0.8 damping), height animates from 0 to auto
- **Menu button transition:** Smooth rotation between hamburger and X icon
- **Note cards:**
  - Entry: Staggered fade-in with scale effect (0.95 to 1.0), 50ms delay between cards
  - Press: Scale to 0.98 with spring animation (0.3s response, 0.7 damping)
  - Removal: Scale and fade out
- **Dark overlay:** Fades in/out with menu (0.2s ease-in-out) to 10% opacity
- **Bottom sheets:** Slide in from bottom (300ms spring animation)
- **FAB:** Smooth shadow and scale transitions on press

### 3.7 Gestures

| Gesture | Location | Action |
|---------|----------|--------|
| Tap | Note card | Open note detail |
| Tap | Menu button (header) | Toggle top navigation menu |
| Tap | Top menu option | Navigate and close menu |
| Tap outside | Overlay/Sheet | Dismiss |
| Tap | FAB | Open dictate sheet |

---

## 4. Technical Requirements

### 4.1 Platform & Compatibility

- **Language:** Swift (latest stable version)
- **Minimum iOS:** Version compatible with iPhone 11
- **Target Devices:** iPhone 11 and newer
- **Orientation:** Portrait only

### 4.2 Development Approach

- Follow standard Apple-recommended patterns and Human Interface Guidelines
- Use native iOS components where available (UIKit or SwiftUI based on team preference)
- Local data persistence (no backend required for MVP)
- Use concrete class dependency injection (avoid protocol boilerplate)
- Implement design tokens FIRST before any UI work

### 4.3 Permissions Required

| Permission | Purpose |
|------------|---------|
| Microphone | Voice dictation feature |


### 4.5 Local Storage

- Notes persisted locally on device
- No cloud sync required for MVP
- No authentication required for MVP

### 4.6 Voice Transcription

- Use iOS Speech framework for speech-to-text
- Real-time transcription display during recording
- Save transcription as note content

### 4.7 AI Integration Points (Future Reference)

The mockup suggests potential AI integration in these areas (not implemented in MVP):
- **Show Original:** Implies notes may have AI-processed versions
- **Make To-Do's:** Suggests AI extraction of action items from note content
- **Find Related Notes:** Semantic search/similarity matching
- **Transcribe (Link):** Possibly AI-powered URL content extraction

These are noted for future consideration only. No AI dependencies or implementation in MVP.

### 4.8 Design System Setup

Create `DesignSystem/Tokens/` (Colors.swift, Spacing.swift, Typography.swift) using values from Section 3.3-3.4 as first development task. Create `Preview_DesignSystem.swift` to visualize tokens during development. Never hard-code colors/spacing/fonts in views—only reference tokens.
---

## 5. Non-Goals

### 5.1 Scope Boundaries
- No feature additions beyond what is visible in the mockup
- No cloud sync or backend services
- No user authentication or account management
- No AI or machine learning features
- No multi-device sync
- No collaboration features
- No rich text editing or formatting
- No image or file attachments (except via future Scan feature)
- No export functionality
- No widget support

### 5.2 Design Constraints
- No redesign or UX reinterpretation of the mockup
- No additional color schemes or themes beyond light mode
- No accessibility features beyond iOS system defaults
- No localization (English only)

### 5.3 Technical Constraints
- No premature optimization
- No complex architecture patterns beyond what is necessary
- No third-party dependencies unless strictly required

---

## 6. Future Suggestions

The following are observations and potential improvements for future versions, clearly separated from MVP scope:

### 6.1 Feature Completion
- Implement camera scanning for document/text capture
- Implement reminder functionality with iOS notifications
- Implement semantic search for "Find Related Notes"
- Implement AI-powered to-do extraction from notes
- Implement settings options (Account, Personalize, Privacy, etc.)
- Implement search functionality

### 6.2 Enhancements
- Dark mode support (design tokens already defined in mockup)
- Note editing (currently notes appear read-only after creation)
- Note deletion
- Tag management (create, rename, delete tags)
- Note sorting options (date, title, priority)
- iCloud sync for multi-device access
- Rich text or markdown support
- Share sheet integration

### 6.3 Platform Expansion
- iPad optimization
- macOS app via Catalyst or native SwiftUI
- watchOS companion for quick capture
- Widgets for home screen note preview

### 6.4 AI Integration
- Voice transcription improvements with speaker identification
- Automatic tagging based on content
- Smart note summarization
- Content-aware duplicate detection

---

## Appendix A: Screen Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         NOTES LIST                               │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  NOTAS                              [☰] ←── tap ──→ [✕]  │   │
│  │                                              ↓            │   │
│  │                              ┌───────────────────────┐   │   │
│  │                              │ Todas las notas       │   │   │
│  │                              │ ───────────────────── │   │   │
│  │                              │ Configuración         │   │   │
│  │                              └───────────────────────┘   │   │
│  │                                (TOP NAVIGATION MENU)     │   │
│  │                                                          │   │
│  │  ┌────────────────────────────────────────────────────┐ │   │
│  │  │ [🔖] Glassmorphism Card 1            [⋯]         │ │   │
│  │  │ Voice note onboarding flow                        │ │   │
│  │  │ I think the onboarding should be...              │ │   │
│  │  │                                                    │ │   │
│  │  │ [🔖] Glassmorphism Card 2            [⋯]         │ │   │
│  │  │ Monetization ideas                                │ │   │
│  │  │ So I was thinking about how we...                │ │   │
│  │  │ ...                                                │ │   │
│  │  └────────────────────────────────────────────────────┘ │   │
│  │             │ (tap)                                     │   │
│  │             ↓                                           │   │
│  │        NOTE DETAIL ──→ [Note Actions Menu]            │   │
│  │                                                          │   │
│  │  [+ FAB] ──→ DICTATE SHEET                            │   │
│  │                                                          │   │
│  │  [Menu] ──→ SETTINGS VIEW                             │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

**Navigation Flow:**
- Single-page app focused on notes list
- Top menu expands from header for settings and filters
- FAB opens voice dictation directly
- Tap cards to view note detail

---

## Appendix B: Component Inventory

| Component | Type | Instances |
|-----------|------|-----------|
| Header with Expandable Menu | Navigation | Notes List |
| Glassmorphism Note Card | List Item | Notes List |
| Top Navigation Menu | Expandable Navigation | Header |
| FAB | Button | Notes List, Note Detail |
| Bottom Sheet | Modal | Tags Drawer, Dictate Sheet |
| Overlay Menu | Modal | Note Actions Menu |
| Text Input | Form | Blank Note Editor |
| Text Area | Form | Blank Note Editor |
| Icon Button | Button | Headers, Cards, Menus |
| Settings Row | List Item | Settings View |
| Dark Overlay | Visual Effect | Menu expansion |

---

*Document generated from Figma mockup analysis. Implementation should strictly follow mockup specifications.*
