"""
Folders API routes.
Implements CRUD operations and tree structure for folders.
"""

from datetime import datetime
from typing import Optional
from fastapi import APIRouter, HTTPException, Query
import uuid

from src.models.schemas import (
    FolderResponse,
    FolderCreate,
    FolderUpdate,
    FolderTreeResponse,
    FolderTreeNode,
    PaginatedResponse,
    PaginationInfo,
    ConceptBrief,
)
from src.data.sample_data import folders, concepts, get_folder_by_id, get_concept_by_id

router = APIRouter(prefix="/folders", tags=["Folders"])


def iso_now() -> str:
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")


def build_tree(parent_id: Optional[str] = None) -> list[FolderTreeNode]:
    """Recursively build folder tree structure."""
    children = [f for f in folders if f.get("parent_folder_id") == parent_id]
    result = []

    for folder in children:
        concept_data = folder.get("concept")
        concept = None
        if concept_data:
            concept = ConceptBrief(
                id=concept_data["id"],
                concept_text=concept_data["concept_text"],
                weight=concept_data.get("weight", 0.0),
            )

        node = FolderTreeNode(
            id=folder["id"],
            parent_folder_id=folder.get("parent_folder_id"),
            category_level=folder.get("category_level", 1),
            concept=concept,
            children=build_tree(folder["id"]),
        )
        result.append(node)

    return result


@router.get("", response_model=PaginatedResponse[FolderResponse])
async def list_folders(
    parent_id: Optional[str] = None,
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
):
    """List folders, optionally filtered by parent folder."""
    filtered = folders.copy()

    # Filter by parent_id (None means root folders)
    if parent_id is not None:
        if parent_id == "null" or parent_id == "":
            filtered = [f for f in filtered if f.get("parent_folder_id") is None]
        else:
            filtered = [f for f in filtered if f.get("parent_folder_id") == parent_id]
    else:
        # If no parent_id specified, return root folders by default
        filtered = [f for f in filtered if f.get("parent_folder_id") is None]

    # Sort by creation_date
    filtered.sort(key=lambda f: f.get("creation_date", ""), reverse=True)

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


@router.get("/tree", response_model=FolderTreeResponse)
async def get_folder_tree():
    """Get complete folder tree structure."""
    tree = build_tree(None)
    return FolderTreeResponse(folders=tree)


@router.post("", response_model=FolderResponse, status_code=201)
async def create_folder(folder_data: FolderCreate):
    """Create a new folder."""
    folder_id = str(uuid.uuid4())
    now = iso_now()

    # Get concept
    concept_obj = get_concept_by_id(folder_data.concept_id)
    if not concept_obj:
        raise HTTPException(status_code=404, detail={
            "code": "CONCEPT_NOT_FOUND",
            "message": f"Concept with ID {folder_data.concept_id} not found",
            "details": {"concept_id": folder_data.concept_id},
            "timestamp": iso_now(),
        })

    # Validate parent folder if provided
    if folder_data.parent_folder_id:
        parent = get_folder_by_id(folder_data.parent_folder_id)
        if not parent:
            raise HTTPException(status_code=404, detail={
                "code": "FOLDER_NOT_FOUND",
                "message": f"Parent folder with ID {folder_data.parent_folder_id} not found",
                "details": {"folder_id": folder_data.parent_folder_id},
                "timestamp": iso_now(),
            })

    new_folder = {
        "id": folder_id,
        "user_id": "user-1",
        "parent_folder_id": folder_data.parent_folder_id,
        "category_level": folder_data.category_level,
        "concept": {
            "id": concept_obj["id"],
            "concept_text": concept_obj["concept_text"],
            "weight": concept_obj.get("weight", 0.0),
        },
        "percentage": 0.0,
        "creation_date": now,
        "last_update": now,
        "children_count": 0,
    }

    folders.append(new_folder)

    # Update parent's children_count
    if folder_data.parent_folder_id:
        parent = get_folder_by_id(folder_data.parent_folder_id)
        if parent:
            parent["children_count"] = parent.get("children_count", 0) + 1

    return new_folder


@router.get("/{folder_id}", response_model=FolderResponse)
async def get_folder(folder_id: str):
    """Get a single folder by ID."""
    folder = get_folder_by_id(folder_id)
    if not folder:
        raise HTTPException(status_code=404, detail={
            "code": "FOLDER_NOT_FOUND",
            "message": f"Folder with ID {folder_id} not found",
            "details": {"folder_id": folder_id},
            "timestamp": iso_now(),
        })

    # Add children list
    children = [f for f in folders if f.get("parent_folder_id") == folder_id]
    folder_copy = folder.copy()
    folder_copy["children"] = children
    folder_copy["notes_count"] = 0  # Mock value

    return folder_copy


@router.put("/{folder_id}", response_model=FolderResponse)
async def update_folder(folder_id: str, folder_data: FolderUpdate):
    """Update an existing folder."""
    folder = get_folder_by_id(folder_id)
    if not folder:
        raise HTTPException(status_code=404, detail={
            "code": "FOLDER_NOT_FOUND",
            "message": f"Folder with ID {folder_id} not found",
            "details": {"folder_id": folder_id},
            "timestamp": iso_now(),
        })

    # Validate new parent (check for circular reference)
    if folder_data.parent_folder_id is not None:
        if folder_data.parent_folder_id == folder_id:
            raise HTTPException(status_code=400, detail={
                "code": "CIRCULAR_REFERENCE",
                "message": "A folder cannot be its own parent",
                "details": {"folder_id": folder_id},
                "timestamp": iso_now(),
            })

        # Check if new parent exists
        if folder_data.parent_folder_id != "":
            new_parent = get_folder_by_id(folder_data.parent_folder_id)
            if not new_parent:
                raise HTTPException(status_code=404, detail={
                    "code": "FOLDER_NOT_FOUND",
                    "message": f"Parent folder with ID {folder_data.parent_folder_id} not found",
                    "details": {"folder_id": folder_data.parent_folder_id},
                    "timestamp": iso_now(),
                })

        folder["parent_folder_id"] = folder_data.parent_folder_id if folder_data.parent_folder_id else None

    if folder_data.concept_id is not None:
        concept_obj = get_concept_by_id(folder_data.concept_id)
        if concept_obj:
            folder["concept"] = {
                "id": concept_obj["id"],
                "concept_text": concept_obj["concept_text"],
                "weight": concept_obj.get("weight", 0.0),
            }

    if folder_data.percentage is not None:
        folder["percentage"] = max(0.0, min(1.0, folder_data.percentage))

    folder["last_update"] = iso_now()
    return folder


@router.delete("/{folder_id}", status_code=204)
async def delete_folder(folder_id: str):
    """Delete a folder (must be empty)."""
    folder = get_folder_by_id(folder_id)
    if not folder:
        raise HTTPException(status_code=404, detail={
            "code": "FOLDER_NOT_FOUND",
            "message": f"Folder with ID {folder_id} not found",
            "details": {"folder_id": folder_id},
            "timestamp": iso_now(),
        })

    # Check if folder has children
    children = [f for f in folders if f.get("parent_folder_id") == folder_id]
    if children:
        raise HTTPException(status_code=400, detail={
            "code": "FOLDER_NOT_EMPTY",
            "message": "Cannot delete folder with children. Remove children first.",
            "details": {"folder_id": folder_id, "children_count": len(children)},
            "timestamp": iso_now(),
        })

    # Remove from list
    folders.remove(folder)

    # Update parent's children_count
    if folder.get("parent_folder_id"):
        parent = get_folder_by_id(folder["parent_folder_id"])
        if parent:
            parent["children_count"] = max(0, parent.get("children_count", 1) - 1)

    return None
