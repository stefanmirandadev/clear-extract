## Real-World Use Cases and Practical Value

This package is intended for situations where structured databases must be populated from unstructured or semi-structured documents, and where **correctness, transparency, and auditability matter more than raw extraction coverage**. Typical use cases include national registries, research infrastructure databases, and institutional data curation pipelines.

### 1. Scientific and Research Registries

In domains such as stem cell science, genomics, or animal model registries, source documents are often written by many independent groups using inconsistent terminology and structure. Naïve extraction systems can produce outputs that look plausible but are difficult to trust or defend.

This package supports these settings by:
- making it explicit whether a field value was directly stated, inferred, or ambiguous
- attaching structured provenance (document, location, snippet) to each field
- allowing conservative defaults for high-risk scientific fields

This enables partial automation without silently introducing incorrect scientific claims into curated datasets.

---

### 2. Incremental and Hybrid Curation Workflows

Many real systems operate in a hybrid mode, where automated extraction is combined with human review. The package is designed to support this directly by treating **uncertainty as data**, not as an error condition.

Practical benefits include:
- targeted human review of only ambiguous or inferred fields
- the ability to auto-accept low-risk fields while flagging high-risk ones
- clear separation between extraction and acceptance decisions

This reduces curator workload without requiring full trust in automated outputs.

---

### 3. Schema Evolution and Long-Lived Datasets

Structured datasets often evolve over time as schemas change or new fields are added. In many extraction systems, this leads to brittle pipelines or expensive reprocessing.

By making schema versions explicit and allowing fields to be marked as `NOT_EVALUATED` or `MISSING`, this package:
- supports gradual schema evolution
- avoids breaking existing records
- enables selective re-extraction of only affected fields

This is particularly valuable for long-running national or institutional data collections.

---

### 4. Auditing, Accountability, and Reproducibility

In academic and institutional contexts, it is often necessary to answer questions such as:
- “Where did this value come from?”
- “Was this explicitly stated or inferred?”
- “What evidence supports this entry?”

The package is designed to make such questions answerable by construction. Every extracted value can be traced back to specific source evidence, and the epistemic status of each field is recorded explicitly.

This supports reproducibility, downstream trust, and responsible use of automated extraction methods.

---

### 5. Model-Agnostic and Future-Proof Design

The package intentionally avoids coupling schemas and field semantics to any specific language model or provider. As models change, improve, or are replaced, the same schema definitions and field policies can be reused without modification.

This allows teams to focus effort on:
- defining what their data means
- deciding what level of uncertainty is acceptable
- improving extractors over time without rewriting schemas

---


### 6. Illustrative Example: Field-Level Uncertainty in Practice

Consider a laboratory report describing a mouse disease model. The report contains the sentence:

> “Mice carrying a homozygous deletion of *Trp53* were maintained at the Monash Animal Facility.”

Suppose the schema includes the fields `genotype` and `maintaining_institution`.

An extraction system using this package might produce the following results:

- **genotype**
  - value: `"Trp53 homozygous knockout"`
  - status: `NORMALISED`
  - evidence: direct citation of the sentence
  - confidence: high

- **maintaining_institution**
  - value: `"Monash University"`
  - status: `INFERRED`
  - evidence: citation of the facility mention
  - confidence: moderate

Although both fields are populated, they are treated differently by the system. The genotype is explicitly stated and normalised, while the institution is inferred from contextual information rather than directly named.

A downstream policy may therefore:
- automatically accept the genotype field
- flag the maintaining institution for human review

Importantly, the system does not claim that either value is correct or incorrect. Instead, it records *how* each value was obtained and allows acceptance decisions to be made explicitly and transparently.


### Summary

The primary value of this package is not higher extraction accuracy in isolation, but **making uncertainty, provenance, and risk explicit at the field level**. This enables structured extraction systems that are usable, inspectable, and defensible in real-world academic and institutional settings
