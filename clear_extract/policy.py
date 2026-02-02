from dataclasses import dataclass, field
from .enums import FieldStatus


@dataclass
class FieldPolicy:
    """
    Defines acceptance and review policies for a field.
    Extraction != acceptance; policies decide what is acceptable.
    """
    allow_inference: bool = False
    auto_accept_statuses: set[FieldStatus] = field(
        default_factory=lambda: {FieldStatus.EXPLICIT, FieldStatus.NORMALISED}
    )
    require_review_statuses: set[FieldStatus] = field(
        default_factory=lambda: {
            FieldStatus.INFERRED,
            FieldStatus.AMBIGUOUS,
            FieldStatus.CONFLICTING
        }
    )
    min_confidence: float | None = None
