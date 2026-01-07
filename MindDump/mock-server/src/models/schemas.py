"""
Pydantic schemas for API request/response models.
Matches the API_ENDPOINTS.md specification.
"""

from datetime import datetime
from typing import Optional, Generic, TypeVar, Any
from pydantic import BaseModel, Field

T = TypeVar("T")


# ============================================================================
# Base Response Models
# ============================================================================


class StatusResponse(BaseModel):
    id: str
    name: str


class PurposeResponse(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    weight: int


class ProcessedDataResponse(BaseModel):
    summary: Optional[str] = None
    key_points: Optional[list[str]] = None
    sentiment: Optional[str] = None


class ConceptResponse(BaseModel):
    id: str
    concept_text: str
    normalized_name: Optional[str] = None
    weight: float
    creation_date: Optional[str] = None
    last_update: Optional[str] = None
    notes_count: Optional[int] = None
    related_notes: Optional[list[dict]] = None


class ConceptBrief(BaseModel):
    """Brief concept info for embedding in other responses"""
    id: str
    concept_text: str
    weight: float


# ============================================================================
# Pagination
# ============================================================================


class PaginationInfo(BaseModel):
    total: int
    page: int
    limit: int
    pages: int
    has_next: bool = False
    has_prev: bool = False


class PaginatedResponse(BaseModel, Generic[T]):
    items: list[T]
    pagination: PaginationInfo


# ============================================================================
# Notes
# ============================================================================


class NoteResponse(BaseModel):
    id: str
    user_id: Optional[str] = None
    title: str
    creation_date: str
    last_update: str
    last_open: Optional[str] = None
    original_text: str
    processed_data: Optional[ProcessedDataResponse] = None
    language: str
    priority: int
    status: Optional[StatusResponse] = None
    word_count: int
    concepts: Optional[list[ConceptBrief]] = None
    purposes: Optional[list[PurposeResponse]] = None
    folder_id: Optional[str] = None


class NoteCreate(BaseModel):
    title: str
    original_text: str
    language: str = "en"
    priority: int = 0
    status_id: Optional[str] = None
    concept_ids: Optional[list[str]] = None
    purpose_ids: Optional[list[dict]] = None  # [{purpose_id, weight}]


class NoteUpdate(BaseModel):
    title: Optional[str] = None
    original_text: Optional[str] = None
    priority: Optional[int] = None
    status_id: Optional[str] = None


class PrioritizeRequest(BaseModel):
    action: str  # "increase", "decrease", "set"
    value: int = 1


class PrioritizeResponse(BaseModel):
    id: str
    priority: int
    previous_priority: int
    last_update: str


# ============================================================================
# Folders
# ============================================================================


class FolderResponse(BaseModel):
    id: str
    user_id: Optional[str] = None
    parent_folder_id: Optional[str] = None
    category_level: int
    concept: Optional[ConceptBrief] = None
    percentage: float
    creation_date: str
    last_update: str
    children_count: Optional[int] = None
    children: Optional[list["FolderResponse"]] = None
    notes_count: Optional[int] = None


class FolderCreate(BaseModel):
    parent_folder_id: Optional[str] = None
    concept_id: str
    category_level: int = 1


class FolderUpdate(BaseModel):
    parent_folder_id: Optional[str] = None
    concept_id: Optional[str] = None
    percentage: Optional[float] = None


class FolderTreeNode(BaseModel):
    id: str
    parent_folder_id: Optional[str] = None
    category_level: int
    concept: Optional[ConceptBrief] = None
    children: list["FolderTreeNode"] = []


class FolderTreeResponse(BaseModel):
    folders: list[FolderTreeNode]


# ============================================================================
# User Settings
# ============================================================================


class UserSettingsResponse(BaseModel):
    id: str
    user_id: str
    language: str
    auto_structure_note: bool
    creation_date: str
    last_update: str


class UserSettingsCreate(BaseModel):
    language: str = "en"
    auto_structure_note: bool = True


class UserSettingsUpdate(BaseModel):
    language: Optional[str] = None
    auto_structure_note: Optional[bool] = None


# ============================================================================
# Errors
# ============================================================================


class ErrorDetail(BaseModel):
    code: str
    message: str
    details: Optional[dict[str, Any]] = None
    timestamp: str


class ErrorResponse(BaseModel):
    error: ErrorDetail


# Rebuild models for forward references
FolderResponse.model_rebuild()
FolderTreeNode.model_rebuild()
