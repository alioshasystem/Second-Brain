"""
MindDump Mock API Server

FastAPI server that provides mock endpoints for iOS app development.
Implements all endpoints from API_ENDPOINTS.md with sample data.

Usage:
    uvicorn main:app --reload --port 8000

API Documentation:
    http://localhost:8000/docs (Swagger UI)
    http://localhost:8000/redoc (ReDoc)
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import notes_router, folders_router, concepts_router, settings_router

app = FastAPI(
    title="MindDump Mock API",
    description="Mock backend for MindDump iOS app development",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS middleware for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers with /api/v1 prefix
API_PREFIX = "/api/v1"

app.include_router(notes_router, prefix=API_PREFIX)
app.include_router(folders_router, prefix=API_PREFIX)
app.include_router(concepts_router, prefix=API_PREFIX)
app.include_router(settings_router, prefix=API_PREFIX)


@app.get("/")
async def root():
    """Root endpoint with API info."""
    return {
        "name": "MindDump Mock API",
        "version": "1.0.0",
        "docs": "/docs",
        "api_base": "/api/v1",
        "endpoints": {
            "notes": "/api/v1/notes",
            "folders": "/api/v1/folders",
            "concepts": "/api/v1/concepts",
            "settings": "/api/v1/users/me/settings",
        },
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
