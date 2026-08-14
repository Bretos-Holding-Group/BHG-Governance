---
document_id: BHG-GOV-CSTRM-001
document_type: governance_reconciliation_matrix
governance_level: enterprise
version: 0.2.0
status: draft
created: 2026-08-14
last_updated: 2026-08-14
effective_date: null
approval_authority: pending
canonical: false
effective: false
automation_ready: false

governed_by:
  - docs/00-GOVERNANCE/CANONICAL_AUTHORITY_MODEL.md

depends_on:
  - docs/06-AUDIT/NORMATIVE_CONFLICT_REGISTER.md
  - docs/02-STANDARDS/DOCUMENT_STANDARD.md
  - docs/02-STANDARDS/DOCUMENT_METADATA_STANDARD.md
  - docs/02-STANDARDS/DOCUMENT_IDENTIFIER_STANDARD.md
  - docs/02-STANDARDS/DOCUMENT_RELATIONSHIP_STANDARD.md
  - docs/02-STANDARDS/DOCUMENT_SCHEMA_STANDARD.md
  - docs/02-STANDARDS/DOCUMENT_GRAMMAR_STANDARD.md
  - docs/02-STANDARDS/DOCUMENT_VALIDATION_STANDARD.md
  - docs/02-STANDARDS/DOCUMENT_LINTING_STANDARD.md
  - docs/02-STANDARDS/DOCUMENT_HISTORY_MODEL.md

related_to:
  - docs/02-STANDARDS/DOCUMENT_AUTOMATION_STANDARD.md
  - docs/02-STANDARDS/DOCUMENT_CLASSIFICATION_STANDARD.md
  - docs/02-STANDARDS/DOCUMENT_DEPENDENCY_STANDARD.md
  - docs/02-STANDARDS/DOCUMENT_RENDERING_STANDARD.md
  - docs/02-STANDARDS/NAMING_STANDARD.md
  - docs/02-STANDARDS/QUALITY_STANDARD.md
  - docs/02-STANDARDS/REPOSITORY_STANDARD.md
  - docs/02-STANDARDS/TRACEABILITY_STANDARD.md
  - docs/02-STANDARDS/WRITING_STANDARD.md
---

# Canonical Standards Reconciliation Matrix

## 1. Purpose

This matrix is the controlled reconciliation layer for the documentary standards in `docs/02-STANDARDS`. It establishes semantic ownership, normative relationships, overlap risks and normalization state before any standard is accepted as canonical.

The matrix does not grant authority merely because a document exists, is marked Approved, or occupies the standards directory.

## 2. Governing model

The matrix is subordinate to `CANONICAL_AUTHORITY_MODEL.md`. The canonical authority model establishes the authority hierarchy; this matrix operationalizes that hierarchy for the documentary standards layer.

The following distinctions are mandatory:

```text
repository placement != normative authority
approval status != semantic ownership
depends_on != governed_by
chronology != supersession
implementation != authority
validation != approval
```

## 3. Reconciliation principles

1. Every shared semantic has one canonical owner.
2. The framework standard governs the common documentary contract but delegates specialized semantics.
3. Metadata, identity, relationships, schema, grammar, history and validation are distinct domains.
4. Specialized standards may constrain implementation but may not redefine a superior semantic owner.
5. Duplicate internal definitions are normalization defects.
6. Existing `Approved` status does not prevent remediation of contradictions through governed change.
7. Automation and AI enforce or interpret approved contracts but do not create normative authority.
8. Unresolved contradictions remain blocking findings until dispositioned.

## 4. Complete standards inventory

The repository currently contains the following documentary standards in `docs/02-STANDARDS`:

| ID | Standard | Semantic domain | Target role | Current phase disposition |
|---|---|---|---|---|
| STD-001 | DOCUMENT_STANDARD.md | Umbrella document contract | Framework standard | NORMALIZED-CANDIDATE |
| STD-002 | DOCUMENT_METADATA_STANDARD.md | Metadata semantics | Canonical metadata contract | NORMALIZED-CANDIDATE |
| STD-003 | DOCUMENT_IDENTIFIER_STANDARD.md | Permanent document identity | Canonical identity contract | NORMALIZED-CANDIDATE |
| STD-004 | DOCUMENT_RELATIONSHIP_STANDARD.md | Relationship vocabulary and semantics | Canonical relationship contract | NORMALIZED-CANDIDATE |
| STD-005 | DOCUMENT_SCHEMA_STANDARD.md | Structural representation | Canonical schema contract | NORMALIZED-CANDIDATE |
| STD-006 | DOCUMENT_GRAMMAR_STANDARD.md | Text/Markdown grammar | Canonical grammar contract | NORMALIZED-CANDIDATE |
| STD-007 | DOCUMENT_VALIDATION_STANDARD.md | Conformance validation | Canonical validation contract | NORMALIZED-CANDIDATE |
| STD-008 | DOCUMENT_LINTING_STANDARD.md | Static linting | Enforcement specialization | NORMALIZED-CANDIDATE |
| STD-009 | DOCUMENT_HISTORY_MODEL.md | Version/history semantics | Canonical history contract | NORMALIZED-CANDIDATE |
| STD-010 | DOCUMENT_DEPENDENCY_STANDARD.md | Dependency semantics | Adjacent specialized contract | PENDING RECONCILIATION |
| STD-011 | DOCUMENT_CLASSIFICATION_STANDARD.md | Information classification | Adjacent specialized contract | PENDING RECONCILIATION |
| STD-012 | DOCUMENT_AUTOMATION_STANDARD.md | Documentary automation | Adjacent enforcement/automation contract | PENDING RECONCILIATION |
| STD-013 | DOCUMENT_COMPILER_STANDARD.md | Document compilation | Adjacent implementation contract | PENDING RECONCILIATION |
| STD-014 | DOCUMENT_RENDERING_STANDARD.md | Rendering/presentation | Adjacent representation contract | PENDING RECONCILIATION |
| STD-015 | DOCUMENT_TEMPLATE_ENGINE_STANDARD.md | Template generation | Adjacent implementation contract | PENDING RECONCILIATION |
| STD-016 | NAMING_STANDARD.md | Naming conventions | Cross-cutting naming contract | PENDING RECONCILIATION |
| STD-017 | QUALITY_STANDARD.md | Documentation quality | Cross-cutting quality contract | PENDING RECONCILIATION |
| STD-018 | REPOSITORY_STANDARD.md | Repository documentary environment | Repository contract | PENDING RECONCILIATION |
| STD-019 | TRACEABILITY_STANDARD.md | Traceability | Cross-cutting evidence contract | PENDING RECONCILIATION |
| STD-020 | WRITING_STANDARD.md | Writing style and language | Representation/style contract | PENDING RECONCILIATION |

This inventory deliberately distinguishes the **core canonical documentary stack** from adjacent standards. Adjacent standards cannot be treated as canonical documentary foundations until their ownership and dependencies are reconciled.

## 5. Core canonical stack

The target dependency and ownership model is:

```text
DOCUMENT_STANDARD
    |
    +-- DOCUMENT_METADATA_STANDARD
    |       |
    |       +-- DOCUMENT_IDENTIFIER_STANDARD
    |       +-- DOCUMENT_RELATIONSHIP_STANDARD
    |
    +-- DOCUMENT_SCHEMA_STANDARD
    +-- DOCUMENT_GRAMMAR_STANDARD
    +-- DOCUMENT_HISTORY_MODEL
    +-- DOCUMENT_VALIDATION_STANDARD
            |
            +-- DOCUMENT_LINTING_STANDARD
```

This is a semantic ownership target. It does not imply that every dependency is an authority relationship.

## 6. Semantic ownership matrix

| Semantic domain | Canonical owner | Other standards may | Other standards may not |
|---|---|---|---|
| Common documentary contract | DOCUMENT_STANDARD | specialize within delegated domains | redefine the global contract |
| Metadata field meaning | DOCUMENT_METADATA_STANDARD | consume fields | redefine field semantics |
| Permanent identity | DOCUMENT_IDENTIFIER_STANDARD | reference document_id | create competing identity semantics |
| Relationship meaning | DOCUMENT_RELATIONSHIP_STANDARD | declare relationships | redefine relationship types |
| Structural schema | DOCUMENT_SCHEMA_STANDARD | instantiate schema | redefine metadata/identity meaning |
| Text/Markdown grammar | DOCUMENT_GRAMMAR_STANDARD | constrain representation | redefine schema or authority |
| History/version semantics | DOCUMENT_HISTORY_MODEL | record evolution | redefine permanent identity |
| Validation semantics | DOCUMENT_VALIDATION_STANDARD | execute checks | create normative authority |
| Lint enforcement | DOCUMENT_LINTING_STANDARD | implement validation rules | become normative authority by code alone |

## 7. Current reconciliation results

### 7.1 DOCUMENT_STANDARD

Observed defects included duplicate internal normative definitions and competing metadata/relationship requirements. Normalization consolidated the document into one umbrella contract, delegated specialized semantics, removed subordinate standards from `depends_on`, and moved the document to Draft pending approval.

### 7.2 DOCUMENT_METADATA_STANDARD

Observed defects included duplicate internal definitions and peer standards incorrectly listed as superior authorities. Normalization consolidated the metadata contract, established one field vocabulary and separated metadata semantics from schema, identity and relationship semantics.

### 7.3 DOCUMENT_IDENTIFIER_STANDARD

Observed defect: peer/subordinate standards were declared as superior authority. Normalization makes DOCUMENT_STANDARD the framework authority, preserves identifier specialization and separates permanent identity from version/history.

### 7.4 DOCUMENT_RELATIONSHIP_STANDARD

Observed defect: metadata, identifier, classification and schema peers were declared as governing authorities. Normalization makes DOCUMENT_STANDARD the superior framework and establishes relationship semantics as a specialized owner.

### 7.5 DOCUMENT_SCHEMA_STANDARD

Observed defects: alternate hyphenated field vocabulary, grammar treated as superior authority and implementation systems treated as governed artifacts. Normalization aligns field names with the metadata contract and confines schema to structural representation.

### 7.6 DOCUMENT_GRAMMAR_STANDARD

Observed defects: alternate relationship field names and broad authority claims. Normalization confines grammar to textual representation and explicitly delegates metadata, schema and relationship semantics.

### 7.7 DOCUMENT_HISTORY_MODEL

Observed defect: multiple peer standards were declared as superior authority. Normalization separates permanent identity, version/history and relationship evolution semantics.

### 7.8 DOCUMENT_VALIDATION_STANDARD

Observed defect: grammar, schema and compiler were treated as superior authorities without a clear semantic boundary. Normalization makes validation an enforcement contract subordinate to the documentary framework while consuming the canonical structural and semantic contracts as dependencies.

### 7.9 DOCUMENT_LINTING_STANDARD

Observed defect: implementation systems were treated as governed outputs and linting could be interpreted as normative authority. Normalization explicitly makes linting an enforcement layer over approved canonical contracts.

## 8. Blocking normalization classes

### NRM-STD-001 — Internal duplicate definitions

A standard containing repeated or conflicting normative definitions is BLOCKING until one authoritative internal definition remains.

### NRM-STD-002 — Cross-standard semantic duplication

The same semantic defined by multiple standards is BLOCKING when meanings differ and HIGH when ownership is ambiguous.

### NRM-STD-003 — Authority inversion

A lower-level or peer standard must not be declared as superior authority without explicit delegation from the canonical authority model. BLOCKING.

### NRM-STD-004 — Metadata/schema inversion

Schema may structure metadata but may not redefine metadata field meaning. BLOCKING when definitions conflict.

### NRM-STD-005 — Grammar/schema inversion

Grammar controls representation; schema controls structure. BLOCKING when their definitions conflict.

### NRM-STD-006 — Validation/linting authority inversion

Validation and linting enforce approved contracts; implementation cannot independently create normative authority. HIGH/BLOCKING where implementation contradicts an approved contract.

## 9. Canonical vocabulary requirement

The documentary system shall maintain one controlled vocabulary for:

- metadata fields;
- identifiers;
- relationship types;
- lifecycle states;
- version semantics;
- structural sections;
- validation states.

Legacy aliases may exist only when explicitly mapped to canonical terms and classified as non-canonical.

## 10. Normalization states

```text
EXISTING
  ↓
INVENTORIED
  ↓
RECONCILED
  ↓
NORMALIZED
  ↓
CANONICAL-CANDIDATE
  ↓
APPROVED
  ↓
CANONICAL
  ↓
ENFORCED
```

No existing Approved label automatically skips reconciliation.

## 11. Current gate assessment

```text
Canonical Authority Model              MERGED / DRAFT
Complete standards inventory           ESTABLISHED
Core semantic ownership model          ESTABLISHED
Core reconciliation matrix             DRAFT
Core standards normalized              CANDIDATE / PENDING REVIEW
Adjacent standards reconciled          NOT YET
Cross-standard validation              NOT YET
Canonical standards baseline           NOT READY
Automated enforcement                  NOT READY
```

## 12. Controlled next operations

The next operations after independent review of this branch are:

1. Reconcile the remaining adjacent standards in dependency order.
2. Re-run cross-standard contradiction analysis.
3. Resolve remaining legacy aliases and metadata vocabulary drift.
4. Produce the canonical document-standard baseline.
5. Establish automated validation rules against the approved contracts.
6. Only then normalize downstream governance documents.

No downstream document shall establish a competing metadata, identity or relationship vocabulary while the canonical documentary contracts remain pending.

## 13. Status

```text
status: draft
canonical: false
effective: false
automation_ready: false
```

This matrix records reconciliation state and normalization decisions. It does not itself replace any standard or grant canonical authority.
