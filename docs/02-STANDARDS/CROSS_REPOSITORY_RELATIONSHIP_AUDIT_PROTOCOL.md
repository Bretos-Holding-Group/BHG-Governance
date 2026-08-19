---
title: Cross-Repository Relationship Audit Protocol
document_id: BHG_CROSS_REPOSITORY_RELATIONSHIP_AUDIT_PROTOCOL
version: 1.0.0
status: Draft
document_type: Standard
governance_level: Enterprise
owner: BHG Governance Council
approval_authority: BHG Governance Council
created: 2026-08-19
last_updated: 2026-08-19
effective_date: null
classification: Internal
language: en
repository: BHG-Governance

governed_by:
  - BHG_CONSTITUTION

depends_on:
  - BHG_CANONICAL_DOCUMENT_RELATIONSHIP_MODEL_V0_1
  - BHG_CANONICAL_AUTHORITY_MODEL
related_to:
  - REPOSITORY_IDENTITY_REGISTER
  - REPOSITORY_NAMING_STANDARD
---

# Cross-Repository Relationship Audit Protocol

## 1. Purpose

Define a reproducible, non-authoritative method for auditing documentary relationships and dependencies across the BHG repository ecosystem.

This protocol does not create, elevate, transfer, or replace governance authority. BHG-Governance remains the governance authority for the ecosystem subject to the BHG Constitution.

## 2. Scope

The initial audit scope includes:

1. `Bretos-Holding-Group/BHG-Governance`
2. `Bretos-Holding-Group/BHG-Ecosystem-Foundation`
3. `Bretos-Holding-Group/bhg-knowledge`
4. `Bretos-Holding-Group/ZivaLatam`

`Legalbreto` is excluded because it is an independent project outside current BHG institutional scope.

## 3. Authority hierarchy

The audit must preserve the applicable direction of authority:

```text
BHG Constitution
      ↓
BHG Governance
      ↓
BHG Ecosystem Foundation / BHG Knowledge / applicable entity governance
      ↓
Repository-local governance and implementation artifacts
```

A lower-level repository may define internal rules within its delegated scope, but those rules must not assert authority over superior BHG authority.

## 4. Relationship vocabulary

Detected or declared cross-repository relationships must be classified using the canonical relationship semantics established by BHG Governance.

At minimum, the audit distinguishes:

- `governed_by`
- `governs`
- `depends_on`
- `related_to`
- `references`
- `implements`
- `supersedes`
- `superseded_by`
- `replaces`
- `replaced_by`

No new relationship type is introduced by this protocol.

## 5. Evidence matrix

Every material cross-repository relationship should be represented as:

| Field | Required meaning |
|---|---|
| source_repository | Repository containing the source artifact |
| source_document_id | Canonical identity of the source artifact |
| relationship_type | Existing canonical relationship semantic |
| target_repository | Repository containing the target artifact |
| target_document_id | Canonical identity of the target artifact |
| authority_basis | Document establishing why the relationship is valid |
| evidence_location | Exact file/section supporting the relationship |
| direction_check | Whether relationship direction is valid |
| contradiction_check | Whether any higher authority contradicts it |
| result | `VALID`, `INVALID`, `MISSING_EVIDENCE`, or `CONTRADICTION` |

## 6. Audit rules

1. Do not infer authority from physical repository location alone.
2. Do not infer dependency from naming alone.
3. A relationship is not validated merely because two documents mention each other.
4. `governed_by` direction must respect the authority hierarchy.
5. Repository-local governance must not become upstream authority merely through reciprocal references.
6. Duplicate or reciprocal declarations must be reconciled against canonical relationship semantics.
7. Authority-bearing cycles must be investigated before normalization is considered complete.
8. Missing evidence is distinct from contradiction.
9. Historical relationships must not be rewritten as current authority without explicit evidence.
10. The audit produces evidence; it does not approve normative changes.
11. Institutional identity state must be distinguished from repository hosting, technical compatibility, and future integration intent.

## 7. Output

A completed audit should produce:

- cross-repository relationship matrix;
- dependency graph;
- authority-direction findings;
- missing-evidence register;
- contradiction register;
- normalization candidates;
- unresolved questions requiring human authority.

## 8. Change boundary

This protocol is observational. Its execution must not modify the audited repositories.

Corrections identified by the audit must be implemented through separately traceable changes in the affected repository and independently verified before merge.

## 9. Approval boundary

A successful audit means only that the examined relationships satisfy the defined verification criteria or that exceptions are explicitly recorded.

It does not mean:

- normative approval;
- canonicalization;
- activation;
- authorization to bypass BHG Governance;
- approval of any underlying document.

## 10. Traceability

The audit must record:

- repository names;
- branch/ref;
- commit SHA;
- source document IDs;
- target document IDs;
- evidence locations;
- validator/version;
- execution timestamp;
- result;
- unresolved exceptions.

This requirement exists so that the relationship graph can be reconstructed without relying on personal memory or undocumented knowledge.
