"""
User Settings API routes.
Implements CRUD operations for user settings.
"""

from datetime import datetime
from fastapi import APIRouter, HTTPException
import uuid

from src.models.schemas import (
    UserSettingsResponse,
    UserSettingsCreate,
    UserSettingsUpdate,
)
from src.data.sample_data import user_settings

router = APIRouter(prefix="/users/me/settings", tags=["User Settings"])


def iso_now() -> str:
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")


# Store settings as mutable global (for mock purposes)
_settings: dict | None = user_settings.copy()


@router.get("", response_model=UserSettingsResponse)
async def get_settings():
    """Get current user settings."""
    global _settings
    if not _settings:
        raise HTTPException(status_code=404, detail={
            "code": "SETTINGS_NOT_FOUND",
            "message": "User settings not found",
            "details": {},
            "timestamp": iso_now(),
        })
    return _settings


@router.post("", response_model=UserSettingsResponse, status_code=201)
async def create_settings(settings_data: UserSettingsCreate):
    """Create user settings."""
    global _settings
    if _settings:
        raise HTTPException(status_code=409, detail={
            "code": "SETTINGS_ALREADY_EXIST",
            "message": "User settings already exist. Use PUT to update.",
            "details": {},
            "timestamp": iso_now(),
        })

    now = iso_now()
    _settings = {
        "id": str(uuid.uuid4()),
        "user_id": "user-1",
        "language": settings_data.language,
        "auto_structure_note": settings_data.auto_structure_note,
        "creation_date": now,
        "last_update": now,
    }

    return _settings


@router.put("", response_model=UserSettingsResponse)
async def update_settings(settings_data: UserSettingsUpdate):
    """Update user settings."""
    global _settings
    if not _settings:
        raise HTTPException(status_code=404, detail={
            "code": "SETTINGS_NOT_FOUND",
            "message": "User settings not found. Use POST to create.",
            "details": {},
            "timestamp": iso_now(),
        })

    if settings_data.language is not None:
        _settings["language"] = settings_data.language

    if settings_data.auto_structure_note is not None:
        _settings["auto_structure_note"] = settings_data.auto_structure_note

    _settings["last_update"] = iso_now()

    return _settings


@router.delete("", status_code=204)
async def delete_settings():
    """Delete user settings."""
    global _settings
    if not _settings:
        raise HTTPException(status_code=404, detail={
            "code": "SETTINGS_NOT_FOUND",
            "message": "User settings not found",
            "details": {},
            "timestamp": iso_now(),
        })

    _settings = None
    return None
