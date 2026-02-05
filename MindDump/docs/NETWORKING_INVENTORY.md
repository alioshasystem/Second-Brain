# Networking Inventory

**Purpose:** Track all networking components, endpoints, and API clients to avoid duplication and maintain consistency.

After implementing networking code, document it here with a concise description.

---

| Component | Location | Purpose |
|-----------|----------|---------|
| **Core Networking** | | |
| `APIClient` | `Core/Networking/` | Cliente HTTP genérico con async/await usando URLSession (soporta GET, POST, PUT, PATCH, DELETE) |
| `APIEndpoint` | `Core/Networking/` | Enum con todos los endpoints del backend (notes, tasks, concepts, notifications, settings) |
| `APIError` | `Core/Networking/` | Enum de errores de red con LocalizedError y manejo de HTTP status codes |
| `HTTPMethod` | `Core/Networking/` | Enum con métodos HTTP (GET, POST, PUT, PATCH, DELETE) |
| **DTOs (Data Transfer Objects)** | | |
| `NoteDTO` | `Core/Networking/DTOs/` | DTO para notas con ProcessedData actualizado (rewrittenText, concepts, classification, tasks) |
| `TaskDTO` | `Core/Networking/DTOs/` | DTO para tareas extraídas (TaskResponseDTO, TaskCreateDTO, TaskUpdateDTO) |
| `NotificationSettingsDTO` | `Core/Networking/DTOs/` | DTO para configuración de notificaciones (NotificationSettingsResponseDTO, RegisterTokenDTO) |
| `ConceptDTO` | `Core/Networking/DTOs/` | DTO para conceptos clave |
| `SettingsDTO` | `Core/Networking/DTOs/` | DTO para configuración de usuario |
| **Mappers** | | |
| `NoteMapper` | `Core/Networking/Mappers/` | Convierte NoteDTO ↔ NoteModel (incluye ProcessedDataModel actualizado) |
| `TaskMapper` | `Core/Networking/Mappers/` | Convierte TaskDTO ↔ TaskModel |
| `NotificationSettingsMapper` | `Core/Networking/Mappers/` | Convierte NotificationSettingsDTO ↔ NotificationSettingsModel |
| `ConceptMapper` | `Core/Networking/Mappers/` | Convierte ConceptDTO ↔ ConceptModel |
| **Repositories** | | |
| `NoteRepository` | `Core/Repositories/` | API - Operaciones CRUD de notas, priorización, y re-procesamiento (processNote) |
| `TaskRepository` | `Core/Repositories/` | API - CRUD de tareas, filtrado por estado y nota |
| `NotificationSettingsRepository` | `Core/Repositories/` | API - Registro de FCM token, fetch y actualización de configuración |

**Nota:** Backend completamente integrado. Todos los datos proceden de API REST en `http://localhost:8000/api/v1`

---

## Notes

- **When to add**: After completing implementation of API clients, endpoints, or networking utilities
- **Location**: All networking code lives in `Core/Networking/`
- **How to describe**: One concise sentence explaining what endpoint/client it handles (not how)
- **Why track**: Avoid duplicate endpoints, maintain consistent API patterns, and identify networking layer responsibilities
