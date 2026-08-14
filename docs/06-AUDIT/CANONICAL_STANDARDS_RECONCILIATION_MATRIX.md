---
document_id: BHG-AUD-CSTRM-001
document_type: audit_reconciliation_matrix
governance_level: enterprise
version: 0.1.0
status: draft
created: 2026-08-14
last_updated: 2026-08-14
effective_date: null
approval_authority: pending
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
  - docs/02-STANDARDS/DOCUMENT_LINTING_STANDARD.md
  - docs/02-STANDARDS/DOCUMENT_HISTORY_MODEL.md
related_to:
  - docs/00-GOVERNANCE/CANONICAL_AUTHORITY_MODEL.md
---

# Canonical Standards Reconciliation Matrix

## 1. Purpose

This matrix establishes the first controlled reconciliation layer for the existing document standards in BHG-Governance.

It does not declare any existing standard canonical merely because it exists, has an Approved status, or occupies the `02-STANDARDS` directory. Authority is determined by the Canonical Authority Model, semantic ownership, explicit relationships, and approved scope.

The matrix is a normalization instrument. Its purpose is to identify semantic ownership, overlaps, contradictions, dependencies, and required normalization actions before any standard is treated as the canonical contract for future documents.

## 2. Governing authority

The matrix is subordinate to `docs/00-GOVERNANCE/CANONICAL_AUTHORITY_MODEL.md`.

The current Canonical Authority Model establishes Level 4 as the Standards layer and distinguishes normative governance from dependency, relationship, approval, and repository placement.

Accordingly:

```text
repository placement != normative authority
depends_on != governed_by
approval status != semantic ownership
chronology != supersession
```

## 3. Reconciliation principles

1. Every shared semantic must have one canonical owner.
2. A framework standard may govern specialized contracts without absorbing their complete semantics.
3. Metadata, identity, structure, grammar, relationships, lifecycle, and validation are distinct semantic domains.
4. Specialized standards may add constraints but may not redefine a superior canonical meaning.
5. Duplicate internal definitions within one document are treated as normalization defects.
6. An `Approved` status does not prevent normalization when the document contains internal contradictions or conflicts with a superior standard.
7. No automation rule becomes authoritative merely because it exists in code.
8. Unresolved normative conflicts remain blocking findings until formally dispositioned.

## 4. Primary standards inventory

| ID | Standard | Primary semantic domain | Target canonical role | Current disposition |
|---|---|---|---|---|
| STD-001 | DOCUMENT_STANDARD.md | Overall document contract | Framework / umbrella standard | RECONCILE |
| STD-002 | DOCUMENT_METADATA_STANDARD.md | Metadata fields and metadata semantics | Canonical metadata contract | RECONCILE |
| STD-003 | DOCUMENT_IDENTIFIER_STANDARD.md | Document identity and identifiers | Canonical identity contract | RECONCILE |
| STD-004 | DOCUMENT_RELATIONSHIP_STANDARD.md | Inter-document relationship semantics | Canonical relationship contract | RECONCILE |
| STD-005 | DOCUMENT_SCHEMA_STANDARD.md | Structural document schema | Canonical structure contract | RECONCILE |
| STD-006 | DOCUMENT_GRAMMAR_STANDARD.md | Markdown/content grammar | Canonical grammar contract | RECONCILE |
| STD-007 | DOCUMENT_LINTING_STANDARD.md | Static document linting rules | Validation/lint specialization | RECONCILE |
| STD-008 | DOCUMENT_HISTORY_MODEL.md | Document history/version semantics | Lifecycle/history specialization | RECONCILE |

## 5. Semantic ownership target

The target contract stack is:

```text
DOCUMENT_STANDARD
    |
    +-- DOCUMENT_METADATA_STANDARD
    +-- DOCUMENT_IDENTIFIER_STANDARD
    +-- DOCUMENT_RELATIONSHIP_STANDARD
    +-- DOCUMENT_SCHEMA_STANDARD
    +-- DOCUMENT_GRAMMAR_STANDARD
    +-- DOCUMENT_HISTORY_MODEL
    +-- DOCUMENT_VALIDATION / LINTING
```

This is a target ownership model, not an assertion that the current documents already implement it correctly.

### 5.1 Ownership rules

| Semantic | Target owner | Other standards may | Other standards may not |
|---|---|---|---|
| Document contract | DOCUMENT_STANDARD | reference and specialize | redefine the global contract |
| Metadata field meaning | DOCUMENT_METADATA_STANDARD | consume metadata | redefine field semantics |
| Document identity | DOCUMENT_IDENTIFIER_STANDARD | reference IDs | create incompatible ID semantics |
| Relationship meaning | DOCUMENT_RELATIONSHIP_STANDARD | use canonical relations | create competing relation meanings |
| Structural schema | DOCUMENT_SCHEMA_STANDARD | instantiate schema | redefine metadata semantics |
| Content grammar | DOCUMENT_GRAMMAR_STANDARD | constrain representation | redefine schema ownership |
| History/version semantics | DOCUMENT_HISTORY_MODEL | represent history | redefine identity or authority |
| Linting rules | DOCUMENT_LINTING_STANDARD | validate canonical contracts | become normative authority by implementation alone |

## 6. Reconciliation matrix

| Standard | Superior authority target | Main overlap risk | Current normalization action | Priority |
|---|---|---|---|---|
| DOCUMENT_STANDARD | Canonical Authority Model + applicable governance/policy layer | May duplicate metadata, schema, grammar, and validation requirements | Reduce to umbrella document contract; delegate semantic ownership explicitly | BLOCKING |
| DOCUMENT_METADATA_STANDARD | DOCUMENT_STANDARD | Duplicate metadata definitions and possible version/field conflicts | Consolidate to one canonical metadata vocabulary and one internal definition | BLOCKING |
| DOCUMENT_IDENTIFIER_STANDARD | DOCUMENT_STANDARD + metadata contract | Identity rules can overlap metadata and naming rules | Make identifier semantics authoritative; metadata consumes the identifier | HIGH |
| DOCUMENT_RELATIONSHIP_STANDARD | DOCUMENT_STANDARD | Relation names may be duplicated elsewhere | Make relationship vocabulary canonical and map aliases explicitly | BLOCKING |
| DOCUMENT_SCHEMA_STANDARD | DOCUMENT_STANDARD + metadata contract | Schema can redefine metadata fields | Make schema structural and consume canonical metadata semantics | BLOCKING |
| DOCUMENT_GRAMMAR_STANDARD | DOCUMENT_STANDARD + schema contract | Grammar can duplicate structural rules | Restrict to representation/content grammar and map to schema | HIGH |
| DOCUMENT_HISTORY_MODEL | DOCUMENT_STANDARD + identifier contract | Version/history semantics can conflict with identity | Separate immutable identity from mutable version/history | HIGH |
| DOCUMENT_LINTING_STANDARD | DOCUMENT_VALIDATION contract | Executable lint rules can silently become normative | Make linting an enforcement layer over approved standards | HIGH |

## 7. Known normalization classes

### NRM-STD-001 — Internal duplicate definitions

A standard may contain more than one metadata or normative definition inside the same file, including different versions or repeated sections.

Disposition:

```text
BLOCKING until one authoritative internal definition remains.
```

### NRM-STD-002 — Cross-standard semantic duplication

The same field, relationship, lifecycle state, or structural rule may be defined in multiple standards without an explicit ownership relationship.

Disposition:

```text
BLOCKING when meanings differ.
HIGH when meanings are identical but ownership is ambiguous.
```

### NRM-STD-003 — Authority inversion

A lower-level standard must not govern or redefine the semantic contract of a superior standard without explicit delegated authority.

Disposition:

```text
BLOCKING.
```

### NRM-STD-004 — Metadata/schema inversion

Schema may consume metadata semantics, but it must not silently redefine the canonical meaning of metadata fields.

Disposition:

```text
BLOCKING.
```

### NRM-STD-005 — Grammar/schema inversion

Grammar controls representation; schema controls structural validity. Neither may silently absorb the other's semantic ownership.

Disposition:

```text
HIGH; BLOCKING when definitions conflict.
```

### NRM-STD-006 — Validation becoming authority

A linter, script, workflow, or validator can enforce a rule but cannot create normative authority by implementation alone.

Disposition:

```text
HIGH until enforcement rules reference approved canonical contracts.
```

## 8. Canonical vocabulary requirement

The future canonical documentation system must maintain one controlled vocabulary for:

- document identity;
- metadata fields;
- governance relationships;
- lifecycle states;
- version semantics;
- structural sections;
- validation states.

Aliases may exist only when explicitly mapped to the canonical term and classified as legacy/non-canonical.

## 9. Normalization gates

A standard may progress through these states:

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

No existing `Approved` label automatically skips reconciliation or normalization.

## 10. Current gate assessment

```text
Canonical Authority Model             MERGED / DRAFT
Standards inventory                   ESTABLISHED
Semantic ownership target             ESTABLISHED
Reconciliation matrix                 DRAFT
Existing standards normalized         NOT YET
Canonical standards                   NOT YET
Automated enforcement                 NOT READY
```

## 11. Next controlled operations

The next normalization work must proceed in dependency order:

1. Reconcile `DOCUMENT_STANDARD`.
2. Reconcile `DOCUMENT_METADATA_STANDARD`.
3. Reconcile `DOCUMENT_IDENTIFIER_STANDARD`.
4. Reconcile `DOCUMENT_RELATIONSHIP_STANDARD`.
5. Reconcile `DOCUMENT_SCHEMA_STANDARD`.
6. Reconcile `DOCUMENT_GRAMMAR_STANDARD`.
7. Reconcile `DOCUMENT_HISTORY_MODEL`.
8. Reconcile `DOCUMENT_LINTING_STANDARD` against the canonical contracts.
9. Re-run cross-standard contradiction analysis.
10. Produce the canonical document-standard baseline.

No downstream document normalization should establish a conflicting local metadata or relationship vocabulary while these contracts remain unresolved.

## 12. Status

```text
status: DRAFT
canonical: false
effective: false
automation_ready: false
```

This matrix is a controlled reconciliation artifact. It records normalization targets and findings; it does not itself replace any existing standard.
