# MindDump API Endpoints

Reference documentation for iOS developers to understand how the app will fetch and send data to the backend.

**Base URL**: `https://api.minddump.app/api/v1`

**Authentication**: JWT Bearer token in Authorization header

---

## Authentication

### Register User
```http
POST /auth/register
```

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response** (201 Created):
```json
{
  "access_token": "jwt_token_here",
  "token_type": "bearer",
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "created_at": "2025-12-31T10:00:00Z"
  }
}
```

**Errors**:
- `400` - Validation error (invalid email, weak password)
- `409` - Email already exists

---

### Login
```http
POST /auth/login
```

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response** (200 OK):
```json
{
  "access_token": "jwt_token_here",
  "token_type": "bearer",
  "user": {
    "id": "uuid",
    "email": "user@example.com"
  }
}
```

**Errors**:
- `401` - Invalid credentials
- `429` - Too many login attempts

---

### Google OAuth Login
```http
POST /auth/oauth/google
```

**Request Body**:
```json
{
  "id_token": "google_id_token_here"
}
```

**Response** (200 OK):
```json
{
  "access_token": "jwt_token_here",
  "token_type": "bearer",
  "user": {
    "id": "uuid",
    "email": "user@example.com"
  }
}
```

**Errors**:
- `400` - Invalid Google token
- `401` - Google authentication failed

---

### Apple OAuth Login
```http
POST /auth/oauth/apple
```

**Request Body**:
```json
{
  "id_token": "apple_id_token_here",
  "user_data": {
    "email": "user@privaterelay.appleid.com",
    "name": "John Doe"
  }
}
```

**Response** (200 OK):
```json
{
  "access_token": "jwt_token_here",
  "token_type": "bearer",
  "user": {
    "id": "uuid",
    "email": "user@example.com"
  }
}
```

**Errors**:
- `400` - Invalid Apple token
- `401` - Apple authentication failed

---

### Get Current User
```http
GET /auth/me
```

**Request Headers**:
```
Authorization: Bearer {access_token}
```

**Response** (200 OK):
```json
{
  "id": "uuid",
  "email": "user@example.com",
  "created_at": "2025-12-31T10:00:00Z"
}
```

**Errors**:
- `401` - Unauthorized

---

## Notes

### List Notes
```http
GET /notes
```

**Query Parameters**:
- `page` (int, default: 1) - Page number
- `limit` (int, default: 20, max: 100) - Items per page
- `status` (string) - Filter by status: "active", "archived", "deleted"
- `priority_min` (int) - Minimum priority level
- `priority_max` (int) - Maximum priority level
- `search` (string) - Search in title and content

**Response** (200 OK):
```json
{
  "items": [
    {
      "id": "uuid",
      "user_id": "uuid",
      "title": "Meeting Notes",
      "creation_date": "2025-12-31T10:00:00Z",
      "last_update": "2025-12-31T12:00:00Z",
      "last_open": "2025-12-31T11:30:00Z",
      "original_text": "Discussed project timeline...",
      "processed_data": {
        "rewritten_text": "During our meeting, we discussed...",
        "raw_concepts": "project management\nteam expansion\ndeadline",
        "classification": "Plan",
        "raw_tasks": "- Prepare Q1 presentation\n- Send timeline to team"
      },
      "language": "en",
      "priority": 3,
      "status_id": "uuid",
      "note_type_id": "uuid",
      "word_count": 150,
      "audio_url": null,
      "concepts": [
        {
          "id": "uuid",
          "concept_text": "Project Management",
          "normalized_name": "project_management",
          "weight": 0.85
        }
      ],
      "tasks": [
        {
          "id": "uuid",
          "task_description": "Prepare Q1 presentation",
          "is_completed": false,
          "date": "2025-12-31",
          "time": "14:00"
        }
      ]
    }
  ],
  "pagination": {
    "total": 156,
    "page": 1,
    "limit": 20
  }
}
```

---

### Create Note (Text or Voice)
```http
POST /notes
```

**Request Body** (Text note):
```json
{
  "title": "My Note",
  "original_text": "This is the note content",
  "note_type": "text",
  "language": "en",
  "priority": 1,
  "auto_process": true,
  "current_date": "2025-12-31"
}
```

**Request Body** (Voice note - audio_base64):
```json
{
  "title": "Voice Note",
  "audio_base64": "data:audio/wav;base64,UklGR...",
  "note_type": "voice",
  "language": "en",
  "priority": 1,
  "auto_process": true,
  "current_date": "2025-12-31"
}
```

**Response** (201 Created):
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "title": "My Note",
  "creation_date": "2025-12-31T10:00:00Z",
  "last_update": "2025-12-31T10:00:00Z",
  "last_open": null,
  "original_text": "This is the note content",
  "processed_data": {
    "rewritten_text": "This is the improved note content...",
    "raw_concepts": "note\ncontent",
    "classification": "Record",
    "raw_tasks": ""
  },
  "language": "en",
  "priority": 1,
  "status_id": "uuid",
  "note_type_id": "uuid",
  "word_count": 5,
  "audio_url": null,
  "concepts": [],
  "tasks": []
}
```

**Errors**:
- `400` - Validation error (missing required fields)
- `401` - Unauthorized

**Note**: If `auto_process=true`, the note will be processed with AI to extract concepts, classify purpose, and detect tasks. Processing happens asynchronously after the note is created.

---

### Get Note
```http
GET /notes/{id}
```

**Response** (200 OK):
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "title": "Meeting Notes",
  "creation_date": "2025-12-31T10:00:00Z",
  "last_update": "2025-12-31T12:00:00Z",
  "last_open": "2025-12-31T11:30:00Z",
  "original_text": "Discussed project timeline...",
  "processed_data": {
    "rewritten_text": "During our meeting, we discussed...",
    "raw_concepts": "project management\nteam expansion",
    "classification": "Plan",
    "raw_tasks": "- Prepare presentation\n- Send timeline"
  },
  "language": "en",
  "priority": 3,
  "status_id": "uuid",
  "note_type_id": "uuid",
  "word_count": 150,
  "audio_url": null,
  "concepts": [
    {
      "id": "uuid",
      "concept_text": "Project Management",
      "normalized_name": "project_management",
      "weight": 0.85
    }
  ],
  "tasks": [
    {
      "id": "uuid",
      "task_description": "Prepare Q1 presentation",
      "is_completed": false,
      "date": "2025-12-31",
      "time": "14:00",
      "priority": 2,
      "created_at": "2025-12-31T10:00:00Z",
      "completed_at": null
    }
  ]
}
```

**Errors**:
- `404` - Note not found
- `401` - Unauthorized

---

### Update Note
```http
PATCH /notes/{id}
```

**Request Body**:
```json
{
  "title": "Updated Title",
  "original_text": "Updated content",
  "rewritten_text": "Updated improved content",
  "priority": 2,
  "language": "en",
  "current_date": "2025-12-31"
}
```

**Response** (200 OK):
```json
{
  "id": "uuid",
  "title": "Updated Title",
  "original_text": "Updated content",
  "last_update": "2025-12-31T13:00:00Z",
  "priority": 2,
  "status_id": "uuid",
  "note_type_id": "uuid"
}
```

**Errors**:
- `404` - Note not found
- `400` - Validation error
- `401` - Unauthorized

**Note**: When updating the original_text, the note will be re-processed with AI if `current_date` is provided.

---

### Process Note
```http
POST /notes/{id}/process
```

Manually trigger AI processing of the note to:
- Rewrite and improve text
- Extract concepts
- Classify purpose (Do, Plan, Record, Learn)
- Detect tasks/pendientes

**Request Body**:
```json
{
  "current_date": "2025-12-31"
}
```

**Response** (200 OK):
```json
{
  "id": "uuid",
  "title": "Note Title",
  "original_text": "Note content",
  "processed_data": {
    "rewritten_text": "Improved content...",
    "raw_concepts": "concept1\nconcept2",
    "classification": "Do",
    "raw_tasks": "- Task 1\n- Task 2"
  },
  "language": "en",
  "priority": 1,
  "status_id": "uuid",
  "note_type_id": "uuid",
  "word_count": 25,
  "audio_url": null,
  "concepts": [
    {
      "id": "uuid",
      "concept_text": "concept1",
      "normalized_name": "concept1",
      "weight": 0.95
    }
  ],
  "tasks": [
    {
      "id": "uuid",
      "task_description": "Task 1",
      "is_completed": false
    }
  ]
}
```

**Errors**:
- `404` - Note not found
- `400` - Validation error
- `401` - Unauthorized

---

### Delete Note
```http
DELETE /notes/{id}
```

**Response** (204 No Content)

**Errors**:
- `404` - Note not found
- `401` - Unauthorized

**Note**: This is a soft delete. The note status is set to "deleted" but remains in the database.

---

## Concepts

### List User Concepts
```http
GET /concepts
```

**Query Parameters**:
- `page` (int, default: 1)
- `limit` (int, default: 50, max: 200)

**Response** (200 OK):
```json
{
  "concepts": [
    {
      "id": "uuid",
      "user_id": "uuid",
      "concept_text": "Project Management",
      "normalized_name": "project_management",
      "weight": 25.5,
      "creation_date": "2025-12-31T10:00:00Z",
      "last_update": "2025-12-31T10:00:00Z",
      "note_count": 12
    }
  ],
  "pagination": {
    "total": 45,
    "page": 1,
    "limit": 50
  }
}
```

---

### Get Top Concepts
```http
GET /concepts/top
```

**Query Parameters**:
- `limit` (int, default: 10) - Number of top concepts to return

**Response** (200 OK):
```json
{
  "concepts": [
    {
      "id": "uuid",
      "concept_text": "Project Management",
      "weight": 25.5,
      "note_count": 12
    }
  ]
}
```

---

## Purposes

### List Purposes
```http
GET /purposes
```

**Query Parameters**:
- `page` (int, default: 1)
- `limit` (int, default: 20)

**Response** (200 OK):
```json
{
  "items": [
    {
      "id": "uuid",
      "name": "Do",
      "description": "Action items and tasks to do",
      "notes_count": 45
    },
    {
      "id": "uuid",
      "name": "Plan",
      "description": "Planning and strategy notes",
      "notes_count": 38
    },
    {
      "id": "uuid",
      "name": "Record",
      "description": "Recording information and facts",
      "notes_count": 29
    },
    {
      "id": "uuid",
      "name": "Learn",
      "description": "Learning and educational notes",
      "notes_count": 22
    }
  ],
  "pagination": {
    "total": 4,
    "page": 1,
    "limit": 20
  }
}
```

**Note**: Purposes are system-defined and cannot be created/modified by users. Standard purposes are: Do, Plan, Record, Learn.

---

### Get Purpose
```http
GET /purposes/{id}
```

**Response** (200 OK):
```json
{
  "id": "uuid",
  "name": "Plan",
  "description": "Planning and strategy notes",
  "notes_count": 29
}
```

**Errors**:
- `404` - Purpose not found
- `401` - Unauthorized

---

## Tasks

### List Tasks
```http
GET /tasks
```

**Query Parameters**:
- `is_completed` (bool, optional) - Filter by completion status (true/false)
- `date_from` (ISO date, optional) - Filter tasks from this date
- `date_to` (ISO date, optional) - Filter tasks until this date
- `limit` (int, default: 50) - Items per page
- `offset` (int, default: 0) - Pagination offset

**Response** (200 OK):
```json
{
  "items": [
    {
      "id": "uuid",
      "user_id": "uuid",
      "note_id": "uuid",
      "task_description": "Prepare Q1 presentation",
      "is_completed": false,
      "date": "2025-12-31",
      "time": "14:00",
      "priority": 2,
      "reminder_sent": 0,
      "created_at": "2025-12-31T10:00:00Z",
      "completed_at": null
    }
  ],
  "pagination": {
    "total": 34,
    "limit": 50,
    "offset": 0
  }
}
```

---

### Get Task
```http
GET /tasks/{id}
```

**Response** (200 OK):
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "note_id": "uuid",
  "task_description": "Prepare Q1 presentation",
  "is_completed": false,
  "date": "2025-12-31",
  "time": "14:00",
  "priority": 2,
  "reminder_sent": 0,
  "created_at": "2025-12-31T10:00:00Z",
  "completed_at": null
}
```

**Errors**:
- `404` - Task not found
- `401` - Unauthorized

---

### Update Task
```http
PATCH /tasks/{id}
```

**Request Body**:
```json
{
  "is_completed": true,
  "task_description": "Updated task description",
  "date": "2026-01-10",
  "time": "15:30",
  "priority": 3
}
```

**Response** (200 OK):
```json
{
  "id": "uuid",
  "task_description": "Updated task description",
  "is_completed": true,
  "date": "2026-01-10",
  "time": "15:30",
  "priority": 3,
  "completed_at": "2026-01-06T14:00:00Z"
}
```

**Errors**:
- `404` - Task not found
- `400` - Validation error
- `401` - Unauthorized

---

### Delete Task
```http
DELETE /tasks/{id}
```

**Response** (204 No Content)

**Errors**:
- `404` - Task not found
- `401` - Unauthorized

---

## Settings

### Get User Settings
```http
GET /settings
```

**Response** (200 OK):
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "language": "en",
  "auto_structure_note": true,
  "creation_date": "2025-12-31T10:00:00Z",
  "last_update": "2025-12-31T10:00:00Z"
}
```

**Errors**:
- `404` - Settings not found
- `401` - Unauthorized

---

### Update User Settings
```http
PATCH /settings
```

**Request Body**:
```json
{
  "language": "es",
  "auto_structure_note": false
}
```

**Response** (200 OK):
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "language": "es",
  "auto_structure_note": false,
  "last_update": "2025-12-31T13:00:00Z"
}
```

**Errors**:
- `404` - Settings not found
- `400` - Validation error
- `401` - Unauthorized

---

## Notifications

### Register FCM Token
```http
POST /notifications/register-token
```

Register device token for push notifications.

**Request Body**:
```json
{
  "fcm_token": "eSyFj8K3Qn2..."
}
```

**Response** (200 OK):
```json
{
  "success": true,
  "message": "Token registered successfully"
}
```

**Errors**:
- `400` - Validation error
- `401` - Unauthorized

---

### Get Notification Settings
```http
GET /notifications/settings
```

**Response** (200 OK):
```json
{
  "notifications_enabled": true,
  "notify_15_min_before": true,
  "notify_morning_9am": true,
  "custom_minutes_before": null,
  "quiet_hours_start": "22:00",
  "quiet_hours_end": "08:00"
}
```

**Errors**:
- `404` - Settings not found
- `401` - Unauthorized

---

### Update Notification Settings
```http
PATCH /notifications/settings
```

**Request Body**:
```json
{
  "notifications_enabled": true,
  "notify_15_min_before": false,
  "custom_minutes_before": 30,
  "quiet_hours_start": "23:00",
  "quiet_hours_end": "07:00"
}
```

**Response** (200 OK):
```json
{
  "notifications_enabled": true,
  "notify_15_min_before": false,
  "notify_morning_9am": true,
  "custom_minutes_before": 30,
  "quiet_hours_start": "23:00",
  "quiet_hours_end": "07:00"
}
```

**Errors**:
- `404` - Settings not found
- `400` - Validation error
- `401` - Unauthorized

---

### Send Test Notification
```http
POST /notifications/test
```

Send a test push notification to verify configuration.

**Response** (200 OK):
```json
{
  "success": true,
  "message": "Test notification sent"
}
```

**Errors**:
- `400` - No FCM token registered
- `401` - Unauthorized

---

## Error Response Format

All errors follow this format:

```json
{
  "error": {
    "code": "NOTE_NOT_FOUND",
    "message": "Note with ID {id} not found",
    "details": {
      "note_id": "uuid-here"
    },
    "timestamp": "2025-12-31T10:30:00Z"
  }
}
```

### Common Error Codes

- `VALIDATION_ERROR` - Invalid request data
- `UNAUTHORIZED` - Missing or invalid authentication token
- `FORBIDDEN` - Valid token but insufficient permissions
- `NOT_FOUND` - Resource not found
- `CONFLICT` - Resource already exists or constraint violation
- `INTERNAL_ERROR` - Server error
- `RATE_LIMIT_EXCEEDED` - Too many requests
- `PROCESSING_ERROR` - Error during async processing
- `STORAGE_LIMIT_EXCEEDED` - User storage quota exceeded

---

## Rate Limiting

- **Authenticated requests**: 100 requests per minute
- **Authentication endpoints**: 10 requests per minute
- **Upload endpoints**: 20 requests per hour
- **AI generation endpoints**: 10 requests per hour

Rate limit headers:
- `X-RateLimit-Limit`: Request limit
- `X-RateLimit-Remaining`: Remaining requests
- `X-RateLimit-Reset`: Timestamp when limit resets

**429 Too Many Requests** response when limit exceeded.

---

## Pagination

List endpoints that support pagination use these query parameters:
- `page` (int, default: 1) - Page number (1-indexed)
- `limit` (int) - Items per page (default varies by endpoint)
- `offset` (int) - Alternative pagination method (instead of page)

Response format includes:
```json
{
  "items": [...],
  "pagination": {
    "total": 156,
    "page": 1,
    "limit": 20
  }
}
```

---

## Error Handling

### Error Response Format

All errors return appropriate HTTP status codes with this response format:

```json
{
  "detail": "Error message describing what went wrong"
}
```

Or for validation errors:

```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "invalid email format",
      "type": "value_error.email"
    }
  ]
}
```

### Common HTTP Status Codes

- `200` - Success
- `201` - Created
- `204` - No Content (success with no body)
- `400` - Bad Request (validation error)
- `401` - Unauthorized (missing/invalid token)
- `404` - Not Found
- `409` - Conflict (e.g., email already exists)
- `429` - Too Many Requests (rate limit exceeded)
- `500` - Internal Server Error

---

## Rate Limiting

Rate limits apply to all endpoints:
- **Default**: 60 requests per minute per user
- **Authentication endpoints**: 10 requests per minute
- **Broadcast limits**: May be lower for resource-intensive operations

Rate limit information is included in response headers:
- `X-RateLimit-Limit` - Request limit
- `X-RateLimit-Remaining` - Remaining requests
- `X-RateLimit-Reset` - Timestamp when limit resets (Unix time)

When rate limit is exceeded, the API returns `429 Too Many Requests`.

---

## Versioning

The API version is included in the base URL: `/api/v1`

Breaking changes will result in a new version (`/api/v2`), while backward-compatible changes will be added to the current version.

---

## Notes on Processing

### Automatic Note Processing

When creating or updating a note with `auto_process=true`:
1. **Synchronous**: Note is saved immediately and returned to client
2. **Asynchronous**: Backend processes the note in the background:
   - Transcribes voice (if applicable)
   - Rewrites and improves text
   - Extracts key concepts
   - Classifies purpose (Do, Plan, Record, Learn)
   - Detects and extracts tasks

The `processed_data` field is populated asynchronously after creation. Poll the note endpoint to see updates.

### Voice Audio Format

Voice notes should be sent as base64-encoded audio:
- Formats supported: WAV, MP3, M4A
- Maximum size: 25 MB (base64 encoded)
- Should include the MIME type prefix: `data:audio/wav;base64,<content>`

---

**Last Updated**: 2026-01-25
