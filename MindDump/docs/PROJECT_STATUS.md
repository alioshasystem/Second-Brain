# MindDump - Estado del Proyecto

**Última actualización:** 2026-01-25
**Versión PRD:** 0.3
**Estado Backend:** ✅ Backend API Integrado - `http://localhost:8000/api/v1`

---

## Resumen Ejecutivo

MindDump se encuentra en **fase de alineación frontend-backend completada**. El frontend está completamente alineado con la API del backend según INCONSISTENCIES.md. Se han implementado todas las DTOs, Mappers, Repositories y Endpoints necesarios para la comunicación con el backend en tiempo real.

### Progreso General: ~60%

- ✅ **Arquitectura y Design System** (100%)
- ✅ **Gestión de Notas** (95%) - Includes processNote endpoint
- ✅ **Networking Layer** (100%) - Totalmente integrado con API real
- ✅ **Tareas y To-dos** (100%) - Modelo, DTOs, Mapper, Repository implementados
- ✅ **Notificaciones** (100%) - Settings, DTOs, Mapper, Repository implementados
- ⚠️ **Autenticación** (0%)
- ⚠️ **Vistas Derivadas** (Conceptos, Intenciones UI) (50%)

---

## ✅ Completado

### 1. Design System (100%)

**Ubicación:** `DesignSystem/`

| Componente | Estado | Archivo |
|------------|--------|---------|
| Tokens - Colors | ✅ | `Tokens/Colors.swift` |
| Tokens - Typography | ✅ | `Tokens/Typography.swift` |
| Tokens - Spacing | ✅ | `Tokens/Spacing.swift` |
| UIKit Extensions | ✅ | `UIKit/` |
| Font Registration | ✅ | `Tokens/FontRegistration.swift` |

**Notas:**
- Sistema de tokens completo con Alice (títulos) e Inter (cuerpo)
- Paleta de colores definida con beige primary
- Espaciado coherente en toda la app

---

### 2. Core - Modelos SwiftData (100%)

**Ubicación:** `Core/Models/` y `Features/Notes/Models/`

| Modelo | Estado | Propósito |
|--------|--------|-----------|
| `Note` | ✅ | Modelo principal de notas con relaciones |
| `KeyConcept` | ✅ | Conceptos extraídos (futuro procesamiento) |
| `Purpose` | ✅ | Catálogo de intenciones |
| `NotePurpose` | ✅ | Relación nota-intención con peso |
| `Status` | ✅ | Estados de nota (active, archived, deleted) |
| `User` | ✅ | Usuario (sin autenticación real) |
| `UserSettings` | ✅ | Configuración de usuario |
| `Task` | ✅ | Tareas extraídas de notas (maps to tm_tasks) |
| `ProcessedData` | ✅ | Datos procesados (rewrittenText, concepts, classification, tasks) |

**Notas:**
- Todos los modelos usan `@Model` de SwiftData
- Relaciones bidireccionales correctamente configuradas
- `ProcessedData` completamente alineado con estructura del backend

---

### 3. Core - Networking Layer (100%)

**Ubicación:** `Core/Networking/`

| Componente | Estado | Propósito |
|------------|--------|-----------|
| `APIClient` | ✅ | Cliente HTTP genérico con async/await (soporta PATCH) |
| `APIEndpoint` | ✅ | Enum con todos los endpoints del backend (notes, tasks, notifications, concepts) |
| `HTTPMethod` | ✅ | Enum con métodos HTTP (GET, POST, PUT, PATCH, DELETE) |
| `APIError` | ✅ | Manejo robusto de errores de red y HTTP |
| **DTOs** | ✅ | `NoteDTO`, `TaskDTO`, `NotificationSettingsDTO`, `ConceptDTO`, `SettingsDTO` |
| **Mappers** | ✅ | `NoteMapper`, `TaskMapper`, `NotificationSettingsMapper`, `ConceptMapper` |

**Estado:**
- ✅ Backend completamente integrado
- ✅ Todos los endpoints alineados con API real
- ✅ DTOs y Mappers reflejan estructura actual del backend

---

### 4. Core - Repositories (100%)

**Ubicación:** `Core/Repositories/`

| Repository | Estado | Propósito |
|------------|--------|-----------|
| `NoteRepository` | ✅ | API - CRUD de notas, priorización, processNote endpoint |
| `TaskRepository` | ✅ | API - CRUD de tareas, filtrado por estado y nota |
| `NotificationSettingsRepository` | ✅ | API - Registro de FCM token y gestión de configuración |

**Notas:**
- Todas trabajan directamente con API REST
- Patrón @Observable para actualizaciones reactivas
- Manejo completo de errores y estados de carga

---

### 5. Core - Services (100%)

**Ubicación:** `Core/Services/`

| Service | Estado | Propósito |
|---------|--------|-----------|
| `NoteService` | ✅ | CRUD de notas en SwiftData (local persistence) |
| `TranscriptionService` | ✅ | Transcripción de voz con Apple Speech Framework |
| `UserSettingsService` | ✅ | Gestión de preferencias de usuario |

**Notas:**
- `SampleDataService` eliminado (usando backend real)
- `TranscriptionService` completamente integrado con Speech Framework

---

### 6. Shared Components (100%)

**Ubicación:** `Shared/Components/`

| Componente | Estado | Propósito |
|------------|--------|-----------|
| `Badge` | ✅ | Badge genérico reutilizable |
| `CategoryBadge` | ✅ | Badge para conceptos/categorías |
| `IconButton` | ✅ | Botones de iconos con estilos |
| `BottomSheet` | ✅ | Sheet modal desde abajo |
| `OverlayMenu` | ✅ | Menú overlay genérico |
| `FlowLayout` | ✅ | Layout fluido para badges |
| `FAB` | ✅ | Floating Action Button |
| `FloatingActionMenu` | ✅ | Menú de acciones flotante |

**Notas:**
- Todos los componentes siguen Design System
- Reutilizables y bien documentados

---

### 7. Features - Notes (85%)

**Ubicación:** `Features/Notes/`

| Vista/ViewModel | Estado | Propósito |
|-----------------|--------|-----------|
| `NotesListView` | ✅ | Lista principal de notas |
| `NotesTableViewRepresentable` | ✅ | Lista optimizada con UIKit |
| `NoteDetailView` | ✅ | Detalle de nota con scroll parallax |
| `NoteCard` | ✅ | Card de nota en lista |
| `NoteCreationSheet` | ⚠️ | Sheet de creación con expansión animada (405 líneas - excede límite) |
| `NoteCreationViewModel` | ✅ | ViewModel de creación con auto-save |
| `BlankNoteEditorView` | ⚠️ | Editor básico (sin funcionalidad completa) |
| `NoteActionsMenu` | ✅ | Menú de acciones en nota |
| `ActionMenu` | ✅ | Menú de acciones genérico |
| `FloatingActionMenu` | ✅ | Menú flotante de acciones (transcribe, scan, handwrite, dictate) |
| `NotesViewModel` | ✅ | ViewModel principal de notas |

**Funcionalidades implementadas:**
- ✅ Listar notas cronológicamente
- ✅ Ver detalle de nota
- ✅ Bookmark/priorizar nota
- ✅ Filtrar por carpeta/concepto
- ✅ Scroll optimizado con UIKit
- ✅ Parallax en detalle de nota
- ✅ Crear nota con animación de expansión
- ✅ Auto-save durante edición (debounced 500ms)
- ⚠️ Editar contenido de nota (funciona pero sin UI pulida)
- ❌ Eliminar nota

---

### 8. Features - Voice Input (Estructura: 90%, Funcional: 40%)

**Ubicación:** `Features/VoiceInput/`

| Componente | Estado | Propósito |
|------------|--------|-----------|
| `DictateSheet` | ✅ | Sheet de dictado básico (deprecado) |
| `DictationNoteCreationSheet` | ✅ | Sheet de dictado con expansión y creación de nota |
| `FloatingWaveformBar` | ✅ | Barra de visualización de audio con waveform |
| `VoiceDictationViewModel` | ⚠️ | ViewModel con polling (sin Speech Framework real) |

**Estado:**
- ✅ UI completa con waveform animado
- ✅ Integración con NoteCreationViewModel
- ✅ Auto-expansión según contenido
- ⚠️ Speech Framework estructurado pero no funcional
- ⚠️ TranscriptionService con protocol pero sin implementación real
- ❌ Permisos de micrófono no implementados
- ❌ Audio real no capturado

---

### 9. Features - Prioritize (100%)

**Ubicación:** `Features/Prioritize/`

| Componente | Estado | Propósito |
|------------|--------|-----------|
| `PrioritizeView` | ✅ | Vista de priorización tipo Tinder |
| `SwipeableCard` | ✅ | Card swipeable para priorizar |
| `PrioritizeViewModel` | ✅ | Lógica de priorización |

**Notas:**
- Feature completo y funcional
- Permite swipe para aumentar/disminuir prioridad

---

### 10. Features - Settings (50%)

**Ubicación:** `Features/Settings/`

| Componente | Estado | Propósito |
|------------|--------|-----------|
| `SettingsView` | ⚠️ | Vista de configuración básica |

**Estado:**
- ✅ Estructura de vista
- ❌ Opciones de idioma no implementadas
- ❌ Preferencias visuales no implementadas

---

### 11. App Structure (100%)

**Ubicación:** `App/`

| Archivo | Estado | Propósito |
|---------|--------|-----------|
| `MindDumpApp.swift` | ✅ | Entry point, SwiftData container |
| `MainTabView.swift` | ✅ | Tab principal (solo Notes por ahora) |
| `AppNavigation.swift` | ✅ | Rutas de navegación con enum |
| `ContentView.swift` | ✅ | Vista raíz |

**Notas:**
- SwiftData container configurado
- Navegación tipo-segura con `AppRoute`
- Injection de dependencias vía Environment

---

## ❌ Pendiente

### 1. Autenticación (0%)

**Requerido según PRD:**
- Onboarding/Tutorial
- Login con Google OAuth
- Login con Email/Password
- Gestión de tokens JWT
- Refresh token automático
- Keychain para credenciales

**Estado actual:**
- No hay ninguna pantalla de autenticación
- No hay gestión de sesión
- App abre directo en NotesListView

---

### 2. Backend y Procesamiento (0%)

**Requerido según PRD:**

#### Pipeline de Procesamiento
- Detección automática de conceptos (NLP/LLM)
- Clasificación de intención (Purpose)
- Extracción de to-dos
- Generación de embeddings semánticos
- Resumen automático (ProcessedData.summary)

#### API Backend
- Endpoints REST (todos definidos en docs, ninguno real)
- Base de datos PostgreSQL
- Worker de procesamiento asíncrono
- Rate limiting
- Autenticación JWT

**Estado actual:**
- Todo es local con SwiftData
- No hay procesamiento automático
- `ProcessedData` siempre es `nil`

---

### 3. Vistas Derivadas (0%)

**Faltantes según PRD:**

#### Vista - Conceptos
- Lista de conceptos generados
- Card por concepto con imagen
- Drill-down a notas del concepto
- Generación/selección de imagen

#### Vista - Intenciones (Purposes)
- Lista de intenciones predefinidas
- Filtro de notas por intención
- Badge visual por intención

#### Vista - To-dos
- Lista de pendientes activos
- Link a nota origen
- Marcar como completado
- Priorización

**Estado actual:**
- Solo existe NotesListView
- No hay navegación a estas vistas

---

### 4. Editor de Notas Completo (20%)

**Faltante:**
- Editor de texto enriquecido
- Formateo (bold, italic, listas)
- Bloques estructurados (futuro)
- Auto-save
- Historial de cambios
- Modo edición vs lectura

**Estado actual:**
- `BlankNoteEditorView` muy básico
- No hay persistencia al editar
- No hay UI de formateo

---

### 5. Voice Input Completo (20%)

**Faltante:**
- Integración con Speech Framework de Apple
- Permisos de micrófono
- UI de grabación en tiempo real
- Transcripción on-device
- Fallback a cloud (Whisper API)
- Manejo de errores de dictado

**Estado actual:**
- UI lista pero no funcional
- No pide permisos
- No transcribe

---

### 6. Pinturas/Imágenes (0%)

**Faltante según PRD:**
- Generación automática de pinturas por IA
- Selección manual de galería
- Asociación nota → imagen
- Asociación concepto → imagen
- Cache de imágenes
- Optimización de tamaño

**Estado actual:**
- Imagen hardcoded en `NoteDetailView` (`painting-01-wheat-field-cypresses`)
- No hay generación ni selección

---

### 7. Widgets y Quick Actions (0%)

**Faltante según PRD:**
- Widget de creación rápida de nota
- Quick Action para grabación de voz
- Deep linking desde widget
- Sincronización widget ↔ app

**Estado actual:**
- No implementado

---

### 8. Funcionalidades de Nota Faltantes (50%)

**Parcialmente implementado:**
- ✅ Ver nota
- ✅ Crear nota (básico)
- ✅ Bookmark/Priority
- ❌ Editar nota (solo estructura)
- ❌ Eliminar nota
- ❌ Archivar nota
- ❌ Buscar en notas
- ❌ Compartir nota

---

## 🔧 Deuda Técnica y Mejoras

### 1. Violaciones de Arquitectura (Commits Recientes)
**Prioridad Alta - Requiere Refactor:**

- ❌ **NoteCreationSheet.swift: 405 líneas** (límite: 350 - GUIDELINES.md:236)
  - Debe dividirse en componentes más pequeños
  - Extraer String extension a `Shared/Extensions/`

- ❌ **Código duplicado:** `NoteCreationSheet` y `DictationNoteCreationSheet` comparten ~80% estructura
  - Extraer lógica común a componente base
  - Header view duplicado dentro de NoteCreationSheet

- ❌ **Strings hardcodeados** (violación GUIDELINES.md:445-452):
  - "Untitled Note" (NoteCreationViewModel.swift:102, 133)
  - "Voice Note" (DictationNoteCreationSheet.swift:255)
  - "Nueva nota" (DictationNoteCreationSheet.swift:85)
  - Deben usar NSLocalizedString

- ❌ **Hardcoded design values** (violación GUIDELINES.md:80-98):
  - Font sizes `16`, `22` en lugar de `Font.DS.*`
  - `UIScreen.main.bounds` en lugar de GeometryReader

- ❌ **Patrón de concurrencia antiguo:**
  - `DispatchQueue.main.asyncAfter` (FloatingActionMenu.swift:127)
  - Debe usar `Task.sleep`

- ❌ **Error handling faltante:**
  - Async tasks ignoran errores (NoteCreationSheet.swift:196-201, 356-361)

### 2. Testing (0%)
- No hay tests unitarios
- No hay tests de integración
- No hay UI tests

### 3. Error Handling
- Error handling básico en Repositories
- No hay retry logic en networking
- No hay offline-first strategy clara
- Tareas async sin manejo de errores en vistas

### 4. Performance
- Scroll optimizado con UIKit ✅
- Imágenes no optimizadas (sin downsampling)
- No hay paginación en lista de notas
- Polling en VoiceDictationViewModel (debería usar async streams)

### 5. Accessibility
- No hay soporte VoiceOver
- No hay Dynamic Type
- No hay labels de accesibilidad

### 6. Localización
- Strings hardcodeados en español/inglés
- No hay `Localizable.strings`
- No hay soporte multi-idioma

---

## 📋 Inventarios Actualizados

### Modelos Implementados

| Modelo | Ubicación | Propósito |
|--------|-----------|-----------|
| `Note` | `Features/Notes/Models/` | Modelo principal de notas |
| `KeyConcept` | `Core/Models/` | Conceptos semánticos (shared) |
| `Purpose` | `Features/Notes/Models/` | Catálogo de intenciones |
| `NotePurpose` | `Features/Notes/Models/` | Relación nota-intención |
| `Status` | `Features/Notes/Models/` | Estados de nota |
| `User` | `Core/Models/` | Usuario (shared) |
| `UserSettings` | `Core/Models/` | Configuración usuario |
| `ProcessedData` | `Features/Notes/Models/` | Datos procesados de nota |

### Componentes Implementados

| Componente | Ubicación | Propósito |
|------------|-----------|-----------|
| `Badge` | `Shared/Components/` | Badge genérico |
| `CategoryBadge` | `Shared/Components/` | Badge de categoría/concepto |
| `IconButton` | `Shared/Components/` | Botón de icono con estilos |
| `BottomSheet` | `Shared/Components/` | Sheet modal |
| `OverlayMenu` | `Shared/Components/` | Menú overlay |
| `FlowLayout` | `Shared/Components/` | Layout fluido |
| `FAB` | `Shared/Components/` | Floating Action Button |
| `FloatingActionMenu` | `Shared/Components/` | Menú flotante de acciones |
| `FloatingWaveformBar` | `Features/VoiceInput/Views/` | Barra de waveform animada (feature-specific) |
| `NoteCard` | `Features/Notes/Views/` | Card de nota (feature-specific) |
| `NoteTableViewCell` | `Features/Notes/Views/UIKit/` | Cell optimizada UIKit |
| `NoteCreationSheet` | `Features/Notes/Views/` | Sheet de creación con expansión (⚠️ 405 líneas) |
| `DictationNoteCreationSheet` | `Features/VoiceInput/Views/` | Sheet de dictado con expansión |

### Services Implementados

| Service/Repository | Ubicación | Propósito |
|-------------------|-----------|-----------|
| `NoteService` | `Core/Services/` | CRUD de notas en SwiftData |
| `TranscriptionService` | `Core/Services/` | Transcripción (estructura) |
| `SampleDataService` | `Core/Services/` | Datos de ejemplo |
| `NoteRepository` | `Core/Repositories/` | Abstracción de datos de notas |

### Networking Implementado

| Componente | Ubicación | Propósito |
|------------|-----------|-----------|
| `APIClient` | `Core/Networking/` | Cliente HTTP genérico |
| `APIEndpoint` | `Core/Networking/` | Enum de endpoints |
| `APIError` | `Core/Networking/` | Errores de red |
| `NoteDTO` | `Core/Networking/DTOs/` | DTO de nota |
| `ConceptDTO` | `Core/Networking/DTOs/` | DTO de concepto |
| `SettingsDTO` | `Core/Networking/DTOs/` | DTO de settings |
| `PaginatedResponse` | `Core/Networking/DTOs/` | Respuesta paginada |
| `NoteMapper` | `Core/Networking/Mappers/` | DTO → Model mapper |
| `ConceptMapper` | `Core/Networking/Mappers/` | DTO → Model mapper |

---

## 🎯 Prioridades Recomendadas para MVP

### Fase 1 - MVP Funcional Offline (4-6 semanas)
1. ✅ ~~Design System~~ (Completado)
2. ✅ ~~Modelos SwiftData~~ (Completado)
3. ✅ ~~NotesListView~~ (Completado)
4. ✅ ~~NoteDetailView~~ (Completado)
5. **Editor de Notas Completo** (Pendiente)
6. **Eliminar/Archivar Notas** (Pendiente)
7. **Voice Input con Speech Framework** (Pendiente)
8. **Búsqueda en Notas** (Pendiente)

### Fase 2 - Autenticación (2-3 semanas)
1. **Onboarding/Tutorial** (Pendiente)
2. **Login con Email** (Pendiente)
3. **Login con Google** (Pendiente)
4. **Gestión de Sesión/Tokens** (Pendiente)

### Fase 3 - Backend e Integración (6-8 semanas)
1. **Backend API REST** (Pendiente)
2. **Database PostgreSQL** (Pendiente)
3. **Migración de Repositories a API** (Pendiente)
4. **Sincronización offline/online** (Pendiente)

### Fase 4 - Procesamiento Cognitivo (4-6 semanas)
1. **Pipeline de procesamiento** (Pendiente)
2. **Extracción de conceptos** (Pendiente)
3. **Clasificación de intenciones** (Pendiente)
4. **Extracción de to-dos** (Pendiente)

### Fase 5 - Vistas Derivadas (3-4 semanas)
1. **Vista de Conceptos** (Pendiente)
2. **Vista de Intenciones** (Pendiente)
3. **Vista de To-dos** (Pendiente)

### Fase 6 - Polish (2-3 semanas)
1. **Generación de Pinturas** (Pendiente)
2. **Widgets** (Pendiente)
3. **Quick Actions** (Pendiente)
4. **Localización** (Pendiente)
5. **Accessibility** (Pendiente)

---

## 📊 Métricas de Progreso

### Por Categoría

| Categoría | Completado | En Progreso | Pendiente | % |
|-----------|------------|-------------|-----------|---|
| Design System | 4/4 | 0 | 0 | 100% |
| Modelos | 9/9 | 0 | 0 | 100% |
| Networking | 11/11 | 0 | 0* | 100%* |
| Repositories | 2/2 | 0 | 0 | 100% |
| Services | 4/4 | 0 | 0 | 100% |
| Shared Components | 8/8 | 0 | 0 | 100% |
| Notes Feature | 10/13 | 2 | 1 | 77% |
| Voice Input | 3/5 | 2 | 0 | 60% |
| Prioritize | 3/3 | 0 | 0 | 100% |
| Settings | 1/3 | 0 | 2 | 33% |
| Autenticación | 0/4 | 0 | 4 | 0% |
| Backend | 0/10 | 0 | 10 | 0% |
| Vistas Derivadas | 0/3 | 0 | 3 | 0% |
| Widgets | 0/2 | 0 | 2 | 0% |

**\* Networking:** Estructura completa pero sin backend real

### Global

- **Total de tareas:** ~90
- **Completadas:** ~38
- **En progreso:** ~5
- **Pendientes:** ~47
- **Progreso:** ~42%

### ⚠️ Deuda Técnica de Commits Recientes
- **7 violaciones de arquitectura** requieren refactor
- **1 archivo excede límite de líneas** (405 vs 350)
- **Código duplicado significativo** entre sheets de creación

---

## 🚀 Siguientes Pasos Inmediatos

### Prioridad 1: Refactor Deuda Técnica (1-2 días)
1. **Dividir NoteCreationSheet** (405 → <350 líneas)
   - Extraer String extension a `Shared/Extensions/String+Height.swift`
   - Extraer componentes: HeaderView, ContentCard
   - Eliminar código duplicado con DictationNoteCreationSheet

2. **Localización de strings hardcodeados**
   - Crear `Localizable.strings`
   - Reemplazar "Untitled Note", "Voice Note", "Nueva nota"

3. **Usar Design System tokens**
   - Reemplazar font sizes hardcodeados
   - Eliminar `UIScreen.main.bounds`

### Prioridad 2: Completar Features Existentes (2-3 días)
4. **Implementar Speech Framework Real**
   - Permisos de micrófono
   - AVAudioEngine para captura
   - SFSpeechRecognizer para transcripción
   - Reemplazar polling con async streams

5. **Funcionalidad de Eliminación**
   - Soft delete (cambiar status)
   - Confirmación
   - Undo

### Prioridad 3: Nuevas Features (1-2 semanas)
6. **Búsqueda Básica**
   - Barra de búsqueda en NotesListView
   - Filtrado en memoria
   - Highlight de resultados

7. **Onboarding/Autenticación**
   - Decidir si empezar con autenticación o continuar con features offline

---

**Nota:** Este documento debe actualizarse después de cada sprint o milestone completado.
