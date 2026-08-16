---
title: Document Identifier Standard
document_id: DOCUMENT_IDENTIFIER_STANDARD
version: 1.2.1
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
- VERSIONING_POLICY
depends_on:
- DOCUMENT_METADATA_STANDARD
- GOVERNANCE_REGISTRY_MODEL
related_to:
- DOCUMENT_VALIDATION_STANDARD
- DOCUMENT_COMPILER_STANDARD
- TRACEABILITY_STANDARD
- REPOSITORY_STANDARD
extensions:
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
governs: []
---

# Document Identifier Standard

## 1. Purpose

This standard defines the canonical identity model for official BHG documents. The `document_id` is the permanent institutional identity of a documentary artifact and remains stable across versions, ownership changes, repository migrations and serialization changes.

## 2. Scope

The standard applies to official governance documents and any other documentary asset for which BHG governance requires a permanent identity.

## 3. Semantic ownership

DOCUMENT_IDENTIFIER_STANDARD is the canonical owner of identifier semantics. DOCUMENT_METADATA_STANDARD exposes the identifier as metadata, while DOCUMENT_STANDARD defines the umbrella documentary contract.

Identifier semantics shall not be redefined by metadata schemas, relationship standards, templates, linters, automation or repository placement.

## 4. Canonical identity field

Every governed document shall expose:

```yaml
document_id: <canonical identifier>
```

The identifier answers: **What document is this?**

The identifier shall not encode the current version, lifecycle state, date or repository location.

## 5. Identifier properties

Identifiers shall be:

- unique;
- permanent;
- immutable during normal lifecycle evolution;
- machine-readable;
- human-readable;
- repository-independent;
- technology-independent;
- deterministic.

## 6. Naming convention

The canonical identifier syntax is:

```text
UPPERCASE_WORDS_SEPARATED_BY_UNDERSCORES
```

Identifiers shall not contain spaces, version numbers, dates or repository names.

Example:

```text
DOCUMENT_IDENTIFIER_STANDARD
```

## 7. Assignment

An identifier shall be assigned when the documentary artifact is created. Before the artifact becomes official, uniqueness and registry compatibility shall be validated.

No official governance document may operate without a valid identifier.

## 8. Identity and version separation

`document_id` and `version` represent different semantics:

```text
document_id = permanent identity
version     = controlled evolution state
```

A new version does not create a new document identity.

## 9. Immutability

Once assigned, `document_id` shall not change as part of ordinary maintenance. Title, version, ownership, governance level, repository or serialization changes do not justify a new identifier.

Exceptional identity migration requires explicit governance approval, preservation of the previous identity evidence and impact analysis of all affected references.

## 10. Registry integration

The governance registry shall use `document_id` as the canonical reference key and maintain, as applicable:

- identifier;
- title;
- document type;
- current version;
- lifecycle status;
- repository location;
- ownership;
- governance relationships.

## 11. Relationship integration

Documentary relationships shall resolve to canonical document identities. Relationship semantics themselves are owned by DOCUMENT_RELATIONSHIP_STANDARD.

Filename, folder location or title shall never be treated as a sufficient substitute for `document_id` when canonical identity is required.

## 12. Validation

Identifier validation shall verify:

- field presence;
- syntax compliance;
- uniqueness;
- registry compatibility;
- metadata consistency;
- reference integrity.

Validation failures shall prevent certification where the applicable governance process requires certification.

## 13. Baseline and automation compatibility

Baseline systems and automation may use document identifiers for discovery, duplicate detection, dependency resolution and relationship mapping. Automation shall not create an official identifier without the required governance validation.

## 14. Duplication prevention

Multiple documents representing the same institutional concept shall be treated as a governance risk. Resolution shall determine consolidation, replacement, deprecation or explicit scope separation.

The identifier registry is the primary mechanism for detecting identity conflicts.

## 15. Audit and preservation

Identifier assignment, validation, migration and registry changes shall preserve sufficient evidence to reconstruct the documentary identity history.

Archived documents retain their original identifier.

## 16. Compliance

A document is not eligible for canonical baseline certification unless it has a valid unique identifier and satisfies the applicable registry and validation requirements.

## 17. Institutional principle

> Identity precedes traceability. A permanent document identity allows institutional knowledge to remain discoverable, verifiable and governable across generations.
