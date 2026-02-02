from dataclasses import dataclass
from .enums import EvidenceStrength


@dataclass
class DocumentLocation:
    """
    Describes a specific location within a document.
    """
    document_id: str
    page: int | None = None
    section: str | None = None
    offset: tuple[int, int] | None = None


@dataclass
class Evidence:
    """
    Structured provenance for an extracted value.
    """
    document_id: str
    location: DocumentLocation
    snippet: str
    strength: EvidenceStrength
