"""
Concepts API routes.
Implements read operations for concepts.
"""

from typing import Optional
from fastapi import APIRouter, HTTPException, Query

from src.models.schemas import (
    ConceptResponse,
    PaginatedResponse,
    PaginationInfo,
)
from src.data.sample_data import concepts, notes, get_concept_by_id

router = APIRouter(prefix="/concepts", tags=["Concepts"])


def iso_now() -> str:
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")


@router.get("", response_model=PaginatedResponse[ConceptResponse])
async def list_concepts(
    page: int = Query(1, ge=1),
    limit: int = Query(50, ge=1, le=200),
    min_weight: Optional[float] = None,
    search: Optional[str] = None,
):
    """List all concepts with pagination and filtering."""
    filtered = concepts.copy()

    # Filter by minimum weight
    if min_weight is not None:
        filtered = [c for c in filtered if c.get("weight", 0.0) >= min_weight]

    # Search in concept text
    if search:
        search_lower = search.lower()
        filtered = [
            c for c in filtered
            if search_lower in c.get("concept_text", "").lower()
            or search_lower in c.get("normalized_name", "").lower()
        ]

    # Sort by weight descending
    filtered.sort(key=lambda c: c.get("weight", 0.0), reverse=True)

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


@router.get("/{concept_id}", response_model=ConceptResponse)
async def get_concept(concept_id: str):
    """Get a single concept by ID with related notes."""
    concept = get_concept_by_id(concept_id)
    if not concept:
        raise HTTPException(status_code=404, detail={
            "code": "CONCEPT_NOT_FOUND",
            "message": f"Concept with ID {concept_id} not found",
            "details": {"concept_id": concept_id},
            "timestamp": iso_now(),
        })

    # Find related notes
    related_notes = []
    for note in notes:
        note_concepts = note.get("concepts") or []
        if any(c.get("id") == concept_id for c in note_concepts):
            related_notes.append({
                "id": note["id"],
                "title": note["title"],
            })

    concept_copy = concept.copy()
    concept_copy["related_notes"] = related_notes[:10]  # Limit to 10

    return concept_copy
