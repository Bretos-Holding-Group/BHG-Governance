---
title: Canonical Standards Reconciliation Matrix
document_id: CANONICAL_STANDARDS_RECONCILIATION_MATRIX
document_type: Governance Reconciliation Matrix
governance_level: Enterprise
version: 0.2.1
status: Draft
created: 2026-08-14
last_updated: 2026-08-14
effective_date: null
approval_authority: BHG Governance Council
governed_by:
- BHG-GOV-CAM-001
depends_on:
- BHG-AUD-NORM-001
- DOCUMENT_STANDARD
- DOCUMENT_METADATA_STANDARD
- DOCUMENT_IDENTIFIER_STANDARD
- DOCUMENT_RELATIONSHIP_STANDARD
- DOCUMENT_SCHEMA_STANDARD
- DOCUMENT_GRAMMAR_STANDARD
- DOCUMENT_VALIDATION_STANDARD
- DOCUMENT_LINTING_STANDARD
- DOCUMENT_HISTORY_MODEL
related_to: []
owner: BHG Governance Council
classification: Internal
language: en
repository: BHG-GOVERNANCE
extensions:
  legacy_metadata:
    canonical: false
    effective: false
    automation_ready: false
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
governs: []
---

# Canonical Standards Reconciliation Matrix

## 1. Purpose

This matrix is the controlled reconciliation layer for the documentary standards in `docs/02-STANDARDS`.

It establishes semantic ownership, authority direction, normalization state and the conditions required before documentary standards can become canonical and machine-enforceable.

It does not grant authority merely because a document exists, is approved, or occupies the standards directory.

## 2. Critical relationship rule

Only documents with a verified canonical identity may be used as canonical relationship targets in this matrix.

Existing standards that lack a verified `document_id` remain **PENDING IDENTITY RECONCILIATION**. They are not deleted, duplicated or promoted merely to satisfy this matrix.

Therefore, the pending adjacent standards previously listed in `related_to` have been removed from the relationship metadata until their identities are reconciled.

## 3. Core canonical stack

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

This is a semantic ownership target. It does not mean every dependency is an authority relationship.

## 4. Semantic ownership

| Semantic domain | Canonical owner | Boundary |
|---|---|---|
| Common documentary contract | DOCUMENT_STANDARD | Owns the global document contract |
| Metadata field meaning | DOCUMENT_METADATA_STANDARD | Owns metadata semantics |
| Permanent identity | DOCUMENT_IDENTIFIER_STANDARD | Owns permanent document identity |
| Relationship meaning | DOCUMENT_RELATIONSHIP_STANDARD | Owns relationship semantics |
| Structural schema | DOCUMENT_SCHEMA_STANDARD | Owns structural representation |
| Text/Markdown grammar | DOCUMENT_GRAMMAR_STANDARD | Owns textual representation |
| History/version semantics | DOCUMENT_HISTORY_MODEL | Owns evolution/history semantics |
| Validation semantics | DOCUMENT_VALIDATION_STANDARD | Enforces approved contracts |
| Lint enforcement | DOCUMENT_LINTING_STANDARD | Static enforcement only |

No downstream standard may silently redefine a semantic owned by another standard.

## 5. Standards inventory

The repository contains these adjacent standards, but their canonical identity has not yet been reconciled in the current normalization pass:

```text
DOCUMENT_AUTOMATION_STANDARD
DOCUMENT_CLASSIFICATION_STANDARD
DOCUMENT_COMPILER_STANDARD
DOCUMENT_DEPENDENCY_STANDARD
DOCUMENT_RENDERING_STANDARD
DOCUMENT_TEMPLATE_ENGINE_STANDARD
NAMING_STANDARD
QUALITY_STANDARD
REPOSITORY_STANDARD
TRACEABILITY_STANDARD
WRITING_STANDARD
```

Their existence is verified. Their **canonical metadata identity and semantic ownership remain pending** where the current documents do not expose the canonical `document_id` contract.

This is an identity/normalization gap, not a reason to create duplicate artifacts.

## 6. Normalization rules

1. One semantic owner per shared concept.
2. `governed_by` expresses normative subordination.
3. `depends_on` expresses prerequisite dependency and does not itself create authority.
4. `related_to` expresses association and must not be used to bypass unresolved identity.
5. Folder placement is not authority.
6. Approval status is not semantic ownership.
7. Historical chronology is not supersession.
8. Automation and AI enforce approved contracts; they do not create normative authority.

## 7. Current reconciliation status

### Core stack

The nine core standards targeted by PR #4 have been normalized toward one framework authority, canonical metadata vocabulary, canonical relationship semantics and explicit semantic boundaries.

They remain `Draft` pending independent validation and approval.

### Adjacent standards

Adjacent standards remain in the repository and are intentionally classified as pending reconciliation. The next normalization pass must establish their canonical identity, ownership and relationship targets before automated enforcement treats them as canonical.

## 8. Blocking classes

The following remain blocking until resolved:

- duplicate or conflicting normative definitions;
- authority inversion;
- metadata/schema semantic inversion;
- grammar/schema semantic inversion;
- incompatible relationship vocabulary;
- unresolved canonical identity for a document used as a normative relationship target;
- cross-repository authority ambiguity.

## 9. Automation gate

Automation may become enforceable only after:

1. mandatory metadata is present;
2. canonical `document_id` uniqueness is verified repository-wide;
3. relationship targets resolve deterministically;
4. authority graph cycles are absent;
5. adjacent standards are reconciled or explicitly classified as non-canonical/pending;
6. the applicable governance approval process is complete.

## 10. Status

```text
status: Draft
canonical: false
effective: false
automation_ready: false
```

This matrix is a normalization artifact and not an effective canonical authority until the applicable approval gate is passed.
