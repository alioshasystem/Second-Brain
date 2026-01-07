# MindDump Mock API Server

Mock backend for MindDump iOS app development. Provides all API endpoints with 50+ sample notes.

## Quick Start

```bash
# Create virtual environment
python -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload --port 8000
```

## API Documentation

Once running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Base URL

```
http://localhost:8000/api/v1
```

## Endpoints

### Notes
- `GET /api/v1/notes` - List notes (paginated, filterable)
- `POST /api/v1/notes` - Create note
- `GET /api/v1/notes/{id}` - Get note
- `PUT /api/v1/notes/{id}` - Update note
- `DELETE /api/v1/notes/{id}` - Delete note (soft delete)
- `POST /api/v1/notes/{id}/prioritize` - Change priority

### Folders
- `GET /api/v1/folders` - List folders
- `GET /api/v1/folders/tree` - Get folder tree
- `POST /api/v1/folders` - Create folder
- `GET /api/v1/folders/{id}` - Get folder
- `PUT /api/v1/folders/{id}` - Update folder
- `DELETE /api/v1/folders/{id}` - Delete folder

### Concepts
- `GET /api/v1/concepts` - List concepts
- `GET /api/v1/concepts/{id}` - Get concept with related notes

### User Settings
- `GET /api/v1/users/me/settings` - Get settings
- `POST /api/v1/users/me/settings` - Create settings
- `PUT /api/v1/users/me/settings` - Update settings
- `DELETE /api/v1/users/me/settings` - Delete settings

## Sample Data

The server includes:
- **52 notes** across categories (Work, Personal, Ideas, Learning, Tasks)
- **9 folders** in hierarchical structure
- **12 concepts** (Project Management, AI/ML, Design, etc.)
- **5 purposes** (work, personal, learning, ideas, tasks)
- **3 statuses** (active, archived, deleted)

## iOS Development

Configure your iOS app to use:
```
Base URL: http://localhost:8000/api/v1
```

Add to Info.plist for local development:
```xml
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsLocalNetworking</key>
    <true/>
</dict>
```
