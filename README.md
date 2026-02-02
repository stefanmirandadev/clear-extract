# clear_extract

A schema-first Python library for extracting structured records from unstructured documents while making field-level uncertainty, provenance, and decision policy explicit.

---

## Overview

This package provides a lightweight framework for building **structured extraction systems** in settings where correctness, transparency, and auditability matter. It is designed for use cases such as scientific registries, institutional databases, and research infrastructure projects, where unstructured documents must be converted into structured records without silently introducing errors.

The package does not perform extraction itself. Instead, it defines the **data model and contracts** that extraction implementations must follow, allowing teams to combine automated extraction (e.g. via large language models) with explicit handling of uncertainty and human review.

---

## Motivation

Many existing extraction pipelines focus on producing complete structured outputs, often obscuring how individual values were obtained or how reliable they are. In practice, this makes downstream validation difficult and increases the risk of propagating subtle errors.

This package addresses that problem by:
- treating uncertainty as a first-class outcome rather than a failure
- recording provenance and evidence at the level of individual fields
- separating extraction from acceptance and decision-making
- supporting partial, incremental, and hybrid (human-in-the-loop) workflows

The goal is not maximal automation, but **responsible automation**.

---

## Core Concepts

### Schema-first design

Extraction is driven by an explicit schema that defines:
- which fields exist
- what each field means
- how uncertainty should be handled for each field

Schemas are versioned and independent of any particular extraction method or model.

---

### Field-level epistemic status

Every extracted field includes an explicit status describing *how* the value was obtained, such as:
- explicitly stated
- normalised from explicit text
- inferred from context
- ambiguous or conflicting
- missing or not evaluated

This makes it possible to reason about extracted data without assuming correctness.

---

### Provenance as structured data

Extracted values may include structured evidence describing:
- the source document
- the location within the document
- the supporting text snippet
- the strength of the evidence

This supports auditing, review, and reproducibility.

---

### Separation of concerns

The package deliberately separates:
- **schemas and field semantics**
- **extraction implementations**
- **acceptance and review policies**

This allows extraction methods to evolve over time without rewriting schemas or downstream logic.

---

## What This Package Does *Not* Do

This package intentionally does **not**:
- call LLM or other model APIs
- define prompts or prompt templates
- parse PDFs, perform OCR, or chunk documents
- provide user interfaces or dashboards
- implement review workflows or analytics

These concerns are expected to be handled by project-specific code built on top of the package.

---

## Typical Use Cases

- National or institutional scientific registries
- Research data curation pipelines
- Hybrid automated/manual extraction workflows
- Long-lived datasets with evolving schemas
- Settings where auditability and transparency are required

---

## Minimal Example

```python
from schema_extractor import Schema, Field, FieldPolicy
from schema_extractor.guidance import ExtractionGuidance

MouseModel = Schema(
    name="MouseDiseaseModel",
    version="1.0",
    fields=[
        Field(
            name="genotype",
            type=str,
            guidance=ExtractionGuidance(
                definition="Genetic modification of the mouse model",
                counterexamples=["Phenotype description"]
            ),
            policy=FieldPolicy(allow_inference=False)
        ),
        Field(
            name="phenotype",
            type=str,
            guidance=ExtractionGuidance(
                definition="Observable traits resulting from the genotype"
            ),
            policy=FieldPolicy(allow_inference=True)
        )
    ]
)
```

An external extractor implementation can then populate field results while adhering to the package’s contracts.

## Design Philosophy
This package is designed to support systems that:
- acknowledge and make visible uncertainty rather than hide it
- allow partial automation without loss of control
- remain usable as models, schemas and requirements evolve

It is intended to be small, explicit and stable.



