---
title: Document Linting Standard
document_id: DOCUMENT_LINTING_STANDARD
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
- DOCUMENT_SCHEMA_STANDARD
- DOCUMENT_GRAMMAR_STANDARD
- DOCUMENT_RELATIONSHIP_STANDARD
- DOCUMENT_VALIDATION_STANDARD
related_to:
- DOCUMENT_AUTOMATION_STANDARD
- TRACEABILITY_STANDARD
extensions:
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
governs: []
---

# Document Linting Standard

## 1. Purpose

This standard defines static-analysis rules that detect documentary defects before or alongside formal validation. Linting is an enforcement mechanism over approved canonical contracts; it does not create normative authority.

## 2. Scope

Linting may inspect metadata, structure, grammar, identifiers, relationships, dependencies, naming, version consistency and traceability requirements defined by canonical standards.

## 3. Semantic boundary

Linting rules shall reference canonical standards rather than redefine them. A rule that detects a violation must identify the governing contract or rule source.

Lint output is evidence of technical conformance and shall not by itself approve, activate or canonicalize a document.

## 4. Principles

Linting shall be:

- automatic where feasible;
- deterministic;
- repeatable;
- non-destructive;
- machine-verifiable;
- traceable.

Linting shall not modify institutional content automatically unless a separately approved remediation mechanism explicitly authorizes such behavior.

## 5. Rule categories

### Metadata

Verify required fields, field names, field types, identifier presence and metadata consistency against DOCUMENT_METADATA_STANDARD.

### Structural

Verify schema conformance and required structural patterns against DOCUMENT_SCHEMA_STANDARD.

### Grammar

Verify headings, section grammar, prohibited aliases and representation rules against DOCUMENT_GRAMMAR_STANDARD.

### Identity

Verify identifier syntax and uniqueness against DOCUMENT_IDENTIFIER_STANDARD.

### Relationships

Verify canonical relationship vocabulary, target resolution, authority direction and cycle constraints against DOCUMENT_RELATIONSHIP_STANDARD.

### Lifecycle and history

Verify version syntax and historical continuity against DOCUMENT_HISTORY_MODEL and applicable versioning policy.

### Traceability

Verify required evidence and references where mandated by the applicable governance contract.

## 6. Severity

Every finding shall use one of:

- Info
- Warning
- Error
- Critical

Critical findings shall block the applicable governance gate when the referenced governing contract designates the condition as blocking.

The linting standard shall not invent blocking authority independently.

## 7. Rule identity and reports

Every lint rule shall have a stable rule identifier and declare its source contract.

A lint execution should record:

- rule identifier;
- governing standard reference;
- severity;
- location;
- description;
- recommendation;
- detection timestamp;
- execution/version identifier.

Reports shall be machine-readable and suitable for audit evidence.

## 8. Continuous execution

Linting may run before commits, pull requests, CI execution, publication and scheduled audits according to repository governance and automation policy.

Execution frequency does not change normative authority.

## 9. AI compatibility

AI systems may execute rules, classify findings and recommend remediation. They shall not independently approve governance compliance or change the canonical rule set.

## 10. Rule evolution

New lint rules require a documented source contract, stable rule identity and impact assessment. Rule changes shall preserve backward compatibility where feasible and shall be version-controlled.

## 11. Compliance

Linting conformance is a technical quality gate. A document may pass linting and still require governance review, approval or canonicalization.

## 12. Institutional principle

> Linting enforces canonical contracts; it does not become a canonical contract merely because software executes it.
