---
title: Cross-Repository Relationship Audit Protocol
document_id: BHG_CROSS_REPOSITORY_RELATIONSHIP_AUDIT_PROTOCOL
version: 1.0.0
status: Draft
document_type: Standard
governance_level: Enterprise
owner: BHG Governance Council
approval_authority: BHG Governance Council
created: 2026-08-16
last_updated: 2026-08-16
effective_date: null
classification: Internal
---

# Cross-Repository Relationship Audit Protocol

## 1. Purpose

Define a reproducible, non-authoritative method for auditing documentary relationships and dependencies across the BHG repository ecosystem.

This protocol does not create, elevate, transfer, or replace governance authority. BHG-Governance remains the repository of highest governance authority for the ecosystem, subject to the BHG Constitution.

## 2. Scope

The initial audit scope is:

1. `Bretos-Holding-Group/BHG-Governance`
2. `Bretos-Holding-Group/BHG-Ecosystem-Foundation`
3. `Bretos-Holding-Group/bhg-knowledge`
4. `Bretos-Holding-Group/ZivaLatam`

The audit evaluates relationships and dependencies only. Document lifecycle status is not itself an audit failure unless it changes the semantics of a declared relationship.

## 3. Authority hierarchy

The audit must preserve the following direction:

```text
BHG Constitution
      ↓
BHG Governance
      ↓
Ecosystem Foundation / Knowledge / ZivaLatam
      ↓
Repository-local governance and implementation artifacts
```

A lower-level repository may define internal rules where permitted, but an internal rule must not assert authority over BHG Governance or the BHG Constitution.

## 4. Relationship vocabulary

Each detected or declared cross-repository relationship must be classified using the canonical relationship semantics already defined by BHG Governance.

At minimum, the audit distinguishes:

- `governed_by`
- `governs`
- `depends_on`
- `derived_from`
- `references`
- `implements`
- `supersedes`
- `extends`

No new relationship type is introduced by this protocol.

## 5. Evidence matrix

Every cross-repository relationship must be represented as:

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
3. A relationship is not considered validated merely because two documents mention each other.
4. `governed_by` direction must respect the authority hierarchy.
5. A repository-local governance document must not become an upstream authority merely by being referenced by another repository.
6. Duplicate or reciprocal declarations must be reconciled against canonical relationship semantics.
7. Cycles involving authority-bearing relationships must be investigated and resolved before normalization is considered complete.
8. Missing evidence is distinct from contradiction.
9. Historical relationships must not be rewritten as current authority without explicit evidence.
10. The audit produces evidence; it does not approve normative changes.

## 7. Output

The audit must produce:

- cross-repository relationship matrix;
- dependency graph;
- authority-direction findings;
- missing-evidence register;
- contradiction register;
- normalization candidates;
- unresolved questions requiring human authority.

## 8. Change boundary

This protocol is observational. Its execution must not modify documents in the audited repositories.

Corrections identified by the audit must be implemented through separately traceable changes in the affected repository and verified independently before merge.

## 9. Approval boundary

A successful audit result means only that the examined relationships satisfy the defined verification criteria or that all exceptions are explicitly recorded.

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
