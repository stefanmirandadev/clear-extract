from enum import Enum


class FieldStatus(Enum):
    """
    A CLOSED enum describing how a field value was obtained.
    Do not allow extension.
    """
    EXPLICIT = "explicit"
    NORMALISED = "normalised"
    INFERRED = "inferred"
    AMBIGUOUS = "ambiguous"
    CONFLICTING = "conflicting"
    MISSING = "missing"
    NOT_EVALUATED = "not_evaluated"


class EvidenceStrength(Enum):
    """
    Describes the quality or reliability of a piece of evidence.
    """
    STRONG = "strong"
    MEDIUM = "medium"
    WEAK = "weak"
