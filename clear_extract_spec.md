# Schema-First Field-Level Extraction Package — Specification

## 1. Purpose

This package defines a **schema-first extraction framework** for converting unstructured documents into structured records **while making field-level uncertainty, provenance, and decision policy explicit**.

The package does NOT perform LLM calls, prompt engineering, document parsing, or API integrations.  
It defines the **data model and contracts** that extraction implementations must conform to.

The package is designed to be:
- reusable across projects
- model-agnostic
- auditable
- conservative by default
- compatible with batch extraction

---

## 2. Core Design Principles

1. **Schema-first**  
   Extraction is driven by an explicit schema, not by documents.

2. **Field-level epistemics**  
   Every field has an explicit status describing *how* the value was obtained.

3. **Provenance is first-class**  
   Evidence for extracted values is structured, not free text.

4. **Extraction ≠ acceptance**  
   Extractors emit results; policies decide what is acceptable.

5. **Minimal surface area**  
   No UI, no orchestration, no analytics, no LLM SDKs.

---

## 3. Package Layout

```
schema_extractor/
  pyproject.toml
  schema_extractor/
    __init__.py
    schema.py
    field.py
    guidance.py
    policy.py
    result.py
    evidence.py
    record.py
    enums.py
```

---

## 4. Enumerations (`enums.py`)

### 4.1 FieldStatus

A CLOSED enum. Do not allow extension.

```python
class FieldStatus(Enum):
    EXPLICIT
    NORMALISED
    INFERRED
    AMBIGUOUS
    CONFLICTING
    MISSING
    NOT_EVALUATED
```

---

### 4.2 EvidenceStrength

```python
class EvidenceStrength(Enum):
    STRONG
    MEDIUM
    WEAK
```

---

## 5. Evidence (`evidence.py`)

```python
@dataclass
class DocumentLocation:
    document_id: str
    page: int | None = None
    section: str | None = None
    offset: tuple[int, int] | None = None
```

```python
@dataclass
class Evidence:
    document_id: str
    location: DocumentLocation
    snippet: str
    strength: EvidenceStrength
```

---

## 6. Extraction Guidance (`guidance.py`)

```python
@dataclass
class ExtractionGuidance:
    definition: str
    counterexamples: list[str] = field(default_factory=list)
    precedence_rules: list[str] = field(default_factory=list)
    allowed_entity_types: list[str] | None = None
    notes: str | None = None
```

---

## 7. Field Policy (`policy.py`)

```python
@dataclass
class FieldPolicy:
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
```

---

## 8. Field Definition (`field.py`)

```python
@dataclass
class Field:
    name: str
    type: type
    nullable: bool = True
    guidance: ExtractionGuidance | None = None
    policy: FieldPolicy = field(default_factory=FieldPolicy)
```

---

## 9. Field Result (`result.py`)

```python
@dataclass
class FieldResult:
    value: Any | None
    status: FieldStatus
    confidence: float | None
    evidence: list[Evidence] = field(default_factory=list)
    notes: str | None = None
```

---

## 10. Schema (`schema.py`)

```python
@dataclass
class Schema:
    name: str
    version: str
    fields: list[Field]
```

---

## 11. Record (`record.py`)

```python
@dataclass
class Record:
    schema_name: str
    schema_version: str
    fields: dict[str, FieldResult]
```

---

## 12. Extractor Interface (Documentation Only)

```python
class Extractor(Protocol):
    def extract(
        self,
        documents: list[Any],
        fields: list[Field],
        schema: Schema
    ) -> dict[str, FieldResult]:
        ...
```

---

## 13. Minimal Usage Example

```python
MouseModel = Schema(
    name="MouseDiseaseModel",
    version="1.0",
    fields=[...]
)
```

---

## 14. Explicit Non-Goals

- No LLM calls
- No prompt definitions
- No UI
- No analytics
- No orchestration

---

## 15. One-Sentence Definition

A schema-first Python library for extracting structured records from unstructured documents while making field-level uncertainty, provenance, and decision policy explicit.
