---
title: Document Metadata Standard
document_id: DOCUMENT_METADATA_STANDARD
version: 1.3.0
status: Draft
document_type: Standard
governance_level: Enterprise
owner: BHG Governance Council
approval_authority: BHG Governance Council
created: 2026-07-20
last_updated: 2026-08-14
effective_date: null
classification: Internal
language: en
repository: BHG-GOVERNANCE
governed_by:
- DOCUMENT_STANDARD
- BHG-POL-002
- BHG-POL-VERSIONING
depends_on:
- DOCUMENT_IDENTIFIER_STANDARD
- DOCUMENT_HISTORY_MODEL
related_to:
- BHG-MIG-49D1A6CF8892
- BHG-MIG-8327291A8F30
- BHG-MIG-D42CF4B63138
- BHG-MIG-52D57B6334D2
extensions:
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
    relationship_target_reconciliation:
      baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
      performed: '2026-08-16'
      mode: canonicalize_or_classify_external
    state: normalized
    date: '2026-08-16'
governs: []
---

# Document Metadata Standard

## 1. Purpose

This standard defines the canonical metadata contract for official BHG documents. Metadata provides the deterministic structural layer required for governance, validation, auditing, indexing, relationship analysis and long-term preservation.

## 2. Scope

The contract applies to official governance documents and to other BHG-controlled documentary assets when the applicable document class requires the standard metadata model.

## 3. Semantic ownership

This document is the canonical owner of metadata field meaning. DOCUMENT_STANDARD defines the umbrella documentary contract; DOCUMENT_SCHEMA_STANDARD defines structural representation; DOCUMENT_IDENTIFIER_STANDARD owns identifier semantics; DOCUMENT_RELATIONSHIP_STANDARD owns relationship semantics; DOCUMENT_HISTORY_MODEL owns version/history semantics.

No peer standard, template, linter, workflow or automation implementation may silently redefine the meaning of a metadata field.

## 4. Canonical metadata domains

### 4.1 Documentary identity

Mandatory fields:

- `title`
- `document_id`
- `document_type`
- `version`

`document_id` is the permanent identity of the document and remains stable across versions. Identifier syntax and uniqueness rules are owned by DOCUMENT_IDENTIFIER_STANDARD.

### 4.1.1 Canonical document type values

For the documentary classes governed by this normalization scope, `document_type` shall use one of the following canonical values:

- `Standard`
- `Governance Model`
- `Governance Reconciliation Matrix`

Values are case-sensitive. Legacy aliases or alternate casing are non-canonical and shall not be used in normalized documents.

### 4.2 Governance authority

Mandatory fields:

- `governance_level`
- `owner`
- `approval_authority`

These fields identify governance position and institutional responsibility. They do not independently establish authority; authority is resolved through the canonical governance hierarchy and relationship model.

### 4.3 Lifecycle

Mandatory fields:

- `status`
- `created`
- `last_updated`
- `effective_date`

Official lifecycle values are:

- Concept
- Draft
- Review
- Approved
- Active
- Deprecated
- Archived

Lifecycle transition semantics are governed by the applicable governance process and DOCUMENT_HISTORY_MODEL.

### 4.4 Classification and language

Mandatory fields:

- `classification`
- `language`

Classification semantics follow DOCUMENT_CLASSIFICATION_STANDARD. Language follows LANGUAGE_POLICY. These fields shall not be inferred when an explicit value is required.

### 4.5 Repository identity

Mandatory field:

- `repository`

The repository field identifies the authorized source location of the canonical document and shall remain consistent with repository governance.

### 4.6 Documentary relationships

The metadata contract exposes:

- `governed_by`
- `governs`
- `depends_on`
- `related_to`

Their meanings are owned by DOCUMENT_RELATIONSHIP_STANDARD. Metadata stores the relationships; it does not redefine their authority semantics.

## 5. Canonical field contract

| Field | Required | Semantic owner | Core meaning |
|---|---|---|---|
| title | yes | DOCUMENT_METADATA_STANDARD | Official human-readable document name |
| document_id | yes | DOCUMENT_IDENTIFIER_STANDARD | Permanent machine identity |
| document_type | yes | DOCUMENT_METADATA_STANDARD | Normative documentary category |
| version | yes | DOCUMENT_HISTORY_MODEL | Current version state |
| status | yes | DOCUMENT_METADATA_STANDARD / lifecycle policy | Governance lifecycle state |
| governance_level | yes | DOCUMENT_METADATA_STANDARD / authority model | Position in governance hierarchy |
| owner | yes | DOCUMENT_METADATA_STANDARD | Responsible institutional owner |
| approval_authority | yes | DOCUMENT_METADATA_STANDARD / authority model | Authority responsible for approval |
| created | yes | DOCUMENT_HISTORY_MODEL | Immutable origin date |
| last_updated | yes | DOCUMENT_HISTORY_MODEL | Latest controlled modification date |
| effective_date | conditional | DOCUMENT_HISTORY_MODEL | Applicability date of current version |
| classification | yes | DOCUMENT_CLASSIFICATION_STANDARD | Information handling category |
| language | yes | LANGUAGE_POLICY | Canonical document language |
| repository | yes | DOCUMENT_METADATA_STANDARD / repository governance | Authorized source repository |
| governed_by | conditional | DOCUMENT_RELATIONSHIP_STANDARD | Superior authority relationships |
| governs | conditional | DOCUMENT_RELATIONSHIP_STANDARD | Downstream authority relationships |
| depends_on | conditional | DOCUMENT_RELATIONSHIP_STANDARD | Interpretive/implementation prerequisites |
| related_to | conditional | DOCUMENT_RELATIONSHIP_STANDARD | Non-authoritative contextual relationships |

## 6. Metadata invariants

The following invariants are mandatory:

1. `document_id` shall be unique and shall not be reused.
2. `document_id` shall remain stable across versions.
3. `created` shall preserve the original creation date.
4. `repository` shall identify the authorized source of truth.
5. `status` shall represent lifecycle, not technical validation.
6. `effective_date` shall not be interpreted as approval evidence by itself.
7. Relationship fields shall use only canonical relationship vocabulary.
8. Metadata shall not encode authority that conflicts with the Canonical Authority Model.
9. `document_type` shall use the canonical controlled vocabulary defined in §4.1.1.

## 7. Metadata immutability and controlled change

Permanent identity fields are:

- `document_id`
- `created`

Repository identity may change only through an approved repository migration process.

Controlled fields may change through governed modification, including:

- `title`
- `owner`
- `approval_authority`
- `governance_level`
- relationship fields
- lifecycle fields

Every controlled change shall preserve version history, rationale and approval evidence.

## 8. Validation requirements

Metadata shall be validated before approval, publication, baseline inclusion or repository certification.

Validation shall verify:

- required fields;
- schema conformance;
- identifier uniqueness;
- canonical relationship vocabulary;
- authority consistency;
- dependency integrity;
- lifecycle consistency;
- version compatibility;
- canonical `document_type` value.

A technical validation state shall never replace the official lifecycle `status`.

## 9. Schema evolution

New metadata fields require governance approval, documentation, validation rules and impact assessment. Breaking changes require a major metadata-contract version increment and a migration strategy.

## 10. Automation and AI

Automation and AI systems may read, validate, index and analyze metadata. They may not independently change authority, ownership, approval or lifecycle semantics.

Linting and automation are enforcement mechanisms over approved canonical contracts and do not create normative authority by implementation alone.

## 11. Audit and preservation

Metadata changes shall preserve sufficient evidence to reconstruct the previous state, modified fields, reason, approving authority and effective date.

The metadata contract shall remain interpretable across changes in storage systems, automation platforms and document formats.

## 12. Normalization rule

This standard supersedes duplicated or competing metadata definitions once formally approved. During normalization, duplicate internal definitions shall be consolidated into this single field contract, while historical material is preserved through version history rather than repeated normative sections.

## 13. Compliance

Official documents without valid required metadata are non-compliant and shall not be certified as part of a canonical baseline until remediated or formally excepted.

## 14. Institutional principle

Metadata transforms documents into governed institutional assets by providing deterministic identity, lifecycle, authority context and relationship data without replacing the superior governance model.
