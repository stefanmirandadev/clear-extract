from dataclasses import dataclass, field


@dataclass
class ExtractionGuidance:
    """
    Provides structured guidance for extracting a specific field.
    """
    definition: str
    counterexamples: list[str] = field(default_factory=list)
    precedence_rules: list[str] = field(default_factory=list)
    allowed_entity_types: list[str] | None = None
    notes: str | None = None
