from dataclasses import dataclass, field
from typing import Any
from .enums import FieldStatus
from .evidence import Evidence


@dataclass
class FieldResult:
    """
    The result of extracting a single field from documents.
    """
    value: Any | None
    status: FieldStatus
    confidence: float | None
    evidence: list[Evidence] = field(default_factory=list)
    notes: str | None = None
