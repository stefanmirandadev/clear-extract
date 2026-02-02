from dataclasses import dataclass
from .field import Field


@dataclass
class Schema:
    """
    Defines an extraction schema with versioning.
    """
    name: str
    version: str
    fields: list[Field]
