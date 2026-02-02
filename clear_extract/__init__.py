"""
A schema-first Python library for extracting structured records from unstructured
documents while making field-level uncertainty, provenance, and decision policy explicit.
"""

from .enums import FieldStatus, EvidenceStrength
from .evidence import DocumentLocation, Evidence
from .guidance import ExtractionGuidance
from .policy import FieldPolicy
from .field import Field
from .result import FieldResult
from .schema import Schema
from .record import Record

__all__ = [
    "FieldStatus",
    "EvidenceStrength",
    "DocumentLocation",
    "Evidence",
    "ExtractionGuidance",
    "FieldPolicy",
    "Field",
    "FieldResult",
    "Schema",
    "Record",
]
