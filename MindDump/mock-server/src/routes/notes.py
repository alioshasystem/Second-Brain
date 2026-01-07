"""
Notes API routes.
Implements CRUD operations and prioritization for notes.
"""

from datetime import datetime
from typing import Optional
from fastapi import APIRouter, HTTPException, Query
import uuid

from src.models.schemas import (
    NoteResponse,
    NoteCreate,
    NoteUpdate,
    PrioritizeRequest,
    PrioritizeResponse,
    PaginatedResponse,
    PaginationInfo,
)
from src.data.sample_data import notes, get_note_by_id, get_status_by_id, statuses

router = APIRouter(prefix="/notes", tags=["Notes"])


def iso_now() -> str:
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")


@router.get("", response_model=PaginatedResponse[NoteResponse])
async def list_notes(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    status: Optional[str] = None,
    priority_min: Optional[int] = None,
    priority_max: Optional[int] = None,
    search: Optional[str] = None,
    sort_by: str = Query("last_update", regex="^(creation_date|last_update|priority|title)$"),
    order: str = Query("desc", regex="^(asc|desc)$"),
):
    """List all notes with pagination and filtering."""
    filtered = notes.copy()

    # Filter by status
    if status:
        filtered = [n for n in filtered if n.get("status", {}).get("name") == status]

    # Filter by priority range
    if priority_min is not None:
        filtered = [n for n in filtered if n.get("priority", 0) >= priority_min]
    if priority_max is not None:
        filtered = [n for n in filtered if n.get("priority", 0) <= priority_max]

    # Search in title and content
    if search:
        search_lower = search.lower()
        filtered = [
            n for n in filtered
            if search_lower in n.get("title", "").lower()
            or search_lower in n.get("original_text", "").lower()
        ]

    # Sort
    reverse = order == "desc"
    if sort_by == "priority":
        filtered.sort(key=lambda n: n.get("priority", 0), reverse=reverse)
    elif sort_by == "title":
        filtered.sort(key=lambda n: n.get("title", "").lower(), reverse=reverse)
    elif sort_by == "creation_date":
        filtered.sort(key=lambda n: n.get("creation_date", ""), reverse=reverse)
    else:  # last_update
        filtered.sort(key=lambda n: n.get("last_update", ""), reverse=reverse)

    # Pagination
    total = len(filtered)
    start = (page - 1) * limit
    end = start + limit
    items = filtered[start:end]

    pages = (total + limit - 1) // limit if total > 0 else 1

    return PaginatedResponse(
        items=items,
        pagination=PaginationInfo(
            total=total,
            page=page,
            limit=limit,
            pages=pages,
            has_next=page < pages,
            has_prev=page > 1,
        ),
    )


@router.post("", response_model=NoteResponse, status_code=201)
async def create_note(note_data: NoteCreate):
    """Create a new note."""
    note_id = str(uuid.uuid4())
    now = iso_now()

    # Get status if provided
    status = None
    if note_data.status_id:
        status_obj = get_status_by_id(note_data.status_id)
        if status_obj:
            status = {"id": status_obj["id"], "name": status_obj["name"]}
    else:
        # Default to active
        active_status = next((s for s in statuses if s["name"] == "active"), None)
        if active_status:
            status = {"id": active_status["id"], "name": active_status["name"]}

    word_count = len(note_data.original_text.split())

    new_note = {
        "id": note_id,
        "user_id": "user-1",
        "title": note_data.title,
        "creation_date": now,
        "last_update": now,
        "last_open": None,
        "original_text": note_data.original_text,
        "processed_data": None,
        "language": note_data.language,
        "priority": note_data.priority,
        "status": status,
        "word_count": word_count,
        "concepts": None,
        "purposes": None,
        "folder_id": None,
    }

    notes.insert(0, new_note)
    return new_note


@router.get("/{note_id}", response_model=NoteResponse)
async def get_note(note_id: str):
    """Get a single note by ID."""
    note = get_note_by_id(note_id)
    if not note:
        raise HTTPException(status_code=404, detail={
            "code": "NOTE_NOT_FOUND",
            "message": f"Note with ID {note_id} not found",
            "details": {"note_id": note_id},
            "timestamp": iso_now(),
        })

    # Update last_open
    note["last_open"] = iso_now()
    return note


@router.put("/{note_id}", response_model=NoteResponse)
async def update_note(note_id: str, note_data: NoteUpdate):
    """Update an existing note."""
    note = get_note_by_id(note_id)
    if not note:
        raise HTTPException(status_code=404, detail={
            "code": "NOTE_NOT_FOUND",
            "message": f"Note with ID {note_id} not found",
            "details": {"note_id": note_id},
            "timestamp": iso_now(),
        })

    if note_data.title is not None:
        note["title"] = note_data.title

    if note_data.original_text is not None:
        note["original_text"] = note_data.original_text
        note["word_count"] = len(note_data.original_text.split())

    if note_data.priority is not None:
        note["priority"] = max(0, min(4, note_data.priority))

    if note_data.status_id is not None:
        status_obj = get_status_by_id(note_data.status_id)
        if status_obj:
            note["status"] = {"id": status_obj["id"], "name": status_obj["name"]}

    note["last_update"] = iso_now()
    return note


@router.delete("/{note_id}", status_code=204)
async def delete_note(note_id: str):
    """Soft delete a note (set status to deleted)."""
    note = get_note_by_id(note_id)
    if not note:
        raise HTTPException(status_code=404, detail={
            "code": "NOTE_NOT_FOUND",
            "message": f"Note with ID {note_id} not found",
            "details": {"note_id": note_id},
            "timestamp": iso_now(),
        })

    # Soft delete - change status to deleted
    deleted_status = next((s for s in statuses if s["name"] == "deleted"), None)
    if deleted_status:
        note["status"] = {"id": deleted_status["id"], "name": deleted_status["name"]}
    note["last_update"] = iso_now()

    return None


@router.post("/{note_id}/prioritize", response_model=PrioritizeResponse)
async def prioritize_note(note_id: str, request: PrioritizeRequest):
    """Change note priority."""
    note = get_note_by_id(note_id)
    if not note:
        raise HTTPException(status_code=404, detail={
            "code": "NOTE_NOT_FOUND",
            "message": f"Note with ID {note_id} not found",
            "details": {"note_id": note_id},
            "timestamp": iso_now(),
        })

    previous_priority = note.get("priority", 0)
    new_priority = previous_priority

    if request.action == "increase":
        new_priority = min(4, previous_priority + request.value)
    elif request.action == "decrease":
        new_priority = max(0, previous_priority - request.value)
    elif request.action == "set":
        new_priority = max(0, min(4, request.value))
    else:
        raise HTTPException(status_code=400, detail={
            "code": "INVALID_ACTION",
            "message": f"Invalid action: {request.action}. Use 'increase', 'decrease', or 'set'",
            "details": {"action": request.action},
            "timestamp": iso_now(),
        })

    note["priority"] = new_priority
    note["last_update"] = iso_now()

    return PrioritizeResponse(
        id=note_id,
        priority=new_priority,
        previous_priority=previous_priority,
        last_update=note["last_update"],
    )
