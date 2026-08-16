---
title: Document Relationship Standard
document_id: DOCUMENT_RELATIONSHIP_STANDARD
version: 1.3.0
status: Draft
document_type: Standard
governance_level: Enterprise
owner: BHG Governance Council
approval_authority: BHG Governance Council
created: 2026-07-21
last_updated: 2026-08-14
effective_date: null
classification: Internal
language: en
repository: BHG-GOVERNANCE
governed_by:
- DOCUMENT_STANDARD
depends_on:
- DOCUMENT_METADATA_STANDARD
- DOCUMENT_IDENTIFIER_STANDARD
related_to:
- BHG-MIG-8327291A8F30
- DOCUMENT_HISTORY_MODEL
- DOCUMENT_VALIDATION_STANDARD
- BHG-MIG-D42CF4B63138
extensions:
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
    relationship_target_reconciliation:
      baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
      performed: '2026-08-16'
      mode: canonicalize_or_classify_external
governs: []
---

# Document Relationship Standard

## 1. Purpose

This standard defines the canonical semantics and validation rules for relationships between BHG documentary artifacts. It is the sole semantic owner of the official documentary relationship vocabulary.

## 2. Scope

The standard applies to relationships declared by official BHG documents and to systems that parse, validate, index or resolve those relationships.

## 3. Semantic ownership

DOCUMENT_RELATIONSHIP_STANDARD owns relationship meaning. DOCUMENT_METADATA_STANDARD stores relationship fields; DOCUMENT_IDENTIFIER_STANDARD owns document identity; DOCUMENT_SCHEMA_STANDARD owns structural representation.

No metadata schema, template, linter, workflow or automation implementation may redefine relationship meaning.

## 4. Canonical relationship vocabulary

The canonical relationship types are:

### Authority

- `governed_by` — superior authority from which the current document derives legitimacy.
- `governs` — downstream artifact or scope receiving authority from the current document.

### Dependency

- `depends_on` — prerequisite required for interpretation, implementation, validation or operation without necessarily establishing superior authority.

### Context

- `related_to` — contextual association without authority inheritance.
- `references` — informational reference without authority inheritance.

### Evolution

- `supersedes` — current artifact replaces a prior artifact or version.
- `superseded_by` — current artifact has been replaced.
- `replaces` — controlled replacement of an artifact.
- `replaced_by` — current artifact has been replaced by another artifact.

### Implementation

- `implements` — artifact provides an implementation or operational realization of another artifact.
- `implemented_by` — artifacts or systems implementing the current artifact.

## 5. Authority rules

Authority flows from superior to subordinate documents. A lower-level document shall not override a superior authority.

Authority relationships shall be acyclic unless an explicitly approved governance model defines an exceptional case.

Repository placement, chronology, filename, title or approval timestamp shall not be interpreted as authority.

## 6. Dependency rules

`depends_on` identifies prerequisites and shall not be used as a substitute for `governed_by`.

A document may depend on a superior, peer or specialized contract when required for correct interpretation or implementation. Such dependency does not change the authority hierarchy.

## 7. Context and implementation rules

`related_to` and `references` do not create authority or mandatory inheritance.

`implements` and `implemented_by` describe realization relationships and do not change normative ownership.

## 8. Evolution rules

Evolution relationships shall preserve historical identity and decision evidence. They shall not be used to silently overwrite prior versions.

A replacement relationship requires the applicable governance approval and migration/impact analysis.

## 9. Relationship target rules

Every relationship target shall resolve to a canonical `document_id` whenever the target is a governed documentary artifact.

Filenames and paths may be used as repository navigation aids, but are not authoritative identity references.

Every target shall exist or be explicitly classified as an approved external reference under the applicable schema.

## 10. Integrity invariants

The following conditions are mandatory:

1. No authority cycle.
2. No relationship that contradicts the Canonical Authority Model.
3. No unresolved mandatory target.
4. No duplicate competing relationship semantics.
5. No use of `depends_on` to encode normative superiority.
6. No use of `related_to` or `references` to create hidden authority.
7. No relationship target identified only by filename when canonical identity is required.

## 11. Relationship graph

The governance relationship graph consists of documentary nodes and typed edges. It shall support:

- authority resolution;
- dependency analysis;
- impact analysis;
- baseline validation;
- lifecycle analysis;
- governed knowledge retrieval.

## 12. Validation

Relationship validation shall verify:

- vocabulary validity;
- target existence;
- identifier validity;
- authority direction;
- dependency integrity;
- cycle detection;
- registry consistency;
- compatibility with the Canonical Authority Model.

Validation is an enforcement mechanism and does not itself create normative authority.

## 13. Automation and AI

Automation and AI may parse, validate, visualize and analyze relationships. They shall not independently create, delete or reinterpret normative relationships without authorized governance change.

## 14. Repository independence

Relationship meaning shall survive repository migration, folder changes, storage-system changes and documentation-platform changes. Canonical identity, not physical location, is the authoritative reference point.

## 15. Audit and preservation

Relationship changes shall preserve previous state, changed relationship, rationale, responsible authority, approval evidence and effective date where applicable.

Historical relationships shall remain reconstructable.

## 16. Compliance

Documents containing invalid authority relationships, unresolved mandatory dependencies, unauthorized authority chains or non-canonical relationship terms are non-compliant and shall not enter a canonical baseline until remediated or formally excepted.

## 17. Institutional principle

> Explicit relationships transform isolated documents into a governed institutional knowledge graph.
