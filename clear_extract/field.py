from dataclasses import dataclass, field
from .guidance import ExtractionGuidance
from .policy import FieldPolicy


@dataclass
class Field:
    """
    Defines a field in an extraction schema.
    """
    name: str
    type: type
    nullable: bool = True
    guidance: ExtractionGuidance | None = None
    policy: FieldPolicy = field(default_factory=FieldPolicy)
