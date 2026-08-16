---
title: Document Schema Standard
document_id: DOCUMENT_SCHEMA_STANDARD
version: 1.2.0
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
- DOCUMENT_RELATIONSHIP_STANDARD
related_to:
- DOCUMENT_GRAMMAR_STANDARD
- DOCUMENT_VALIDATION_STANDARD
- BHG-MIG-DF2BC2DF9A4A
- BHG-MIG-9783A5418C4A
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

# Document Schema Standard

## 1. Purpose

This standard defines the canonical structural schema used to represent official BHG documents as deterministic data. It owns structural representation, not the meaning of metadata fields, identifiers or documentary relationships.

## 2. Semantic boundaries

- DOCUMENT_STANDARD owns the umbrella documentary contract.
- DOCUMENT_METADATA_STANDARD owns metadata field semantics.
- DOCUMENT_IDENTIFIER_STANDARD owns identifier semantics.
- DOCUMENT_RELATIONSHIP_STANDARD owns relationship semantics.
- DOCUMENT_SCHEMA_STANDARD owns structural representation and field arrangement.
- DOCUMENT_GRAMMAR_STANDARD owns textual/Markdown representation rules.
- DOCUMENT_VALIDATION_STANDARD and DOCUMENT_LINTING_STANDARD enforce approved contracts.

A schema shall not silently redefine the semantic meaning owned by another standard.

## 3. Canonical document object

The canonical document representation consists of:

```text
Document
├── metadata
├── content
└── relationships
```

Automation and validation data may be represented as controlled extension fields, but shall not alter normative meaning.

## 4. Metadata object

The metadata object shall use the canonical field names defined by DOCUMENT_METADATA_STANDARD, including where applicable:

- `title`
- `document_id`
- `document_type`
- `version`
- `status`
- `governance_level`
- `owner`
- `approval_authority`
- `created`
- `last_updated`
- `effective_date`
- `classification`
- `language`
- `repository`
- `governed_by`
- `governs`
- `depends_on`
- `related_to`

The schema defines where these fields appear and their structural constraints. Their semantic meanings remain owned by their canonical standards.

## 5. Content object

The content object contains the controlled document body, including sections such as purpose, scope, principles, definitions, requirements, procedures, responsibilities, exceptions and institutional principles when applicable to the document class.

DOCUMENT_GRAMMAR_STANDARD defines representation and formatting constraints for the content.

## 6. Relationship object

Relationships shall use the canonical vocabulary defined by DOCUMENT_RELATIONSHIP_STANDARD and shall resolve to canonical document identities where the target is a governed documentary artifact.

## 7. Structural invariants

A conforming schema shall ensure:

1. required metadata fields are structurally present;
2. field names are deterministic;
3. field types are valid;
4. identifier and relationship references are structurally valid;
5. content is separable from metadata;
6. extensions do not override canonical semantics;
7. unknown fields are handled according to the approved schema policy rather than silently interpreted.

## 8. Serialization

The canonical schema is representation-independent. Approved serializations may include YAML front matter, JSON and other governed representations.

Serialization syntax shall not change the underlying semantic model.

## 9. Schema evolution

Schema revisions shall declare:

- schema/document version;
- compatibility impact;
- migration requirements when applicable.

Breaking structural changes require the applicable governance approval and migration plan.

## 10. Validation compatibility

Schema validation shall verify structural conformance before approval, publication or baseline certification where required.

Structural validation does not create normative authority; it enforces the contracts defined by the canonical standards.

## 11. Automation and AI

Automation and AI systems may parse and validate the schema, resolve dependencies and inspect structure. They shall not modify governance authority or semantic ownership through schema interpretation.

## 12. Institutional principle

> The schema defines how governed document data is structured; it does not redefine what that data means.
