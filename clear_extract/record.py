from dataclasses import dataclass
from .result import FieldResult


@dataclass
class Record:
    """
    A structured record extracted from documents.
    Links back to schema name and version for traceability.
    """
    schema_name: str
    schema_version: str
    fields: dict[str, FieldResult]
