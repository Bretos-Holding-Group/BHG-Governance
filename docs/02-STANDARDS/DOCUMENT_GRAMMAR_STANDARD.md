---
title: Document Grammar Standard
document_id: DOCUMENT_GRAMMAR_STANDARD
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
related_to:
- DOCUMENT_LINTING_STANDARD
- DOCUMENT_VALIDATION_STANDARD
- DOCUMENT_RENDERING_STANDARD
extensions:
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
---

# Document Grammar Standard

## 1. Purpose

This standard defines the canonical textual and Markdown grammar used to represent official BHG documents. It owns representation and content-order conventions, not metadata semantics, structural schema semantics or governance authority.

## 2. Semantic boundary

- DOCUMENT_STANDARD owns the umbrella documentary contract.
- DOCUMENT_METADATA_STANDARD owns metadata meaning.
- DOCUMENT_SCHEMA_STANDARD owns structural representation.
- DOCUMENT_RELATIONSHIP_STANDARD owns relationship meaning.
- DOCUMENT_GRAMMAR_STANDARD owns textual representation, section grammar and deterministic document-body conventions.

Grammar rules shall not redefine fields, identifiers or authority relationships owned by other standards.

## 3. Document layers

The canonical textual representation consists of:

1. Front matter / metadata.
2. Document title and body.
3. Controlled sections.
4. Institutional conclusion where applicable.

Metadata remains structurally separate from body content even when serialized together in Markdown.

## 4. Canonical section order

Unless the document class explicitly defines another approved order, the preferred sequence is:

1. Purpose
2. Scope
3. Definitions
4. Principles
5. Requirements / Rules
6. Governance / Responsibilities
7. Procedures or Implementation
8. Validation / Compliance
9. Exceptions
10. References
11. Institutional Principle

A document class may omit non-applicable sections without inventing competing grammar.

## 5. Markdown requirements

Official Markdown documents shall use deterministic constructs:

- one primary H1 title;
- hierarchical H2/H3 headings;
- fenced code blocks for machine-readable examples;
- Markdown lists and tables where appropriate;
- no ambiguous pseudo-headings;
- no duplicated normative sections without explicit historical classification.

## 6. Metadata representation

Metadata shall be represented using the canonical field names and structure defined by DOCUMENT_METADATA_STANDARD and DOCUMENT_SCHEMA_STANDARD.

The grammar shall not introduce alternate field spellings such as `document-type` where the canonical field is `document_type`.

## 7. Relationship representation

Relationship fields shall use the canonical relationship vocabulary defined by DOCUMENT_RELATIONSHIP_STANDARD.

Legacy aliases such as `related-documents`, `dependencies`, `successors` or `predecessors` shall not be treated as canonical fields unless explicitly mapped by an approved migration rule.

## 8. Content grammar

Body content shall:

- express one coherent semantic purpose per section;
- avoid repeating normative definitions owned by another document;
- reference canonical authorities rather than reproduce competing definitions;
- use consistent terminology;
- distinguish normative requirements from explanatory material.

## 9. Machine readability

Documents shall use predictable headings, metadata, relationship fields and controlled terminology so parsers and validators can process them deterministically.

Grammar conformance does not grant normative authority.

## 10. Compatibility and evolution

Grammar revisions shall preserve backward compatibility where possible. Breaking changes require the applicable governance approval and migration guidance.

## 11. Validation

Grammar validation may verify:

- front matter presence;
- canonical field names;
- heading hierarchy;
- section order where mandatory;
- duplicate normative sections;
- prohibited aliases;
- code-block and table structure;
- canonical terminology.

Validation and linting enforce this standard but do not independently create authority.

## 12. AI and automation

AI and automation systems may generate, parse or validate documents only within the approved grammar. They shall not infer new normative semantics from formatting alone.

## 13. Institutional principle

> Grammar defines how governed knowledge is represented; it does not redefine what that knowledge means.
