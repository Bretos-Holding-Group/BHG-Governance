---
title: BHG Governance Architecture Map
document_id: BHG_GOVERNANCE_ARCHITECTURE_MAP
document_type: Repository Architecture Map
governance_level: Enterprise
version: 2.0.0
status: Draft
owner: BHG Governance Council
approval_authority: BHG Governance Council
created: 2026-08-14
last_updated: 2026-08-14
effective_date: null
classification: Internal
language: en
repository: BHG-Governance
governed_by:
- BHG-GOV-CAM-001
depends_on:
- BHG_REPOSITORY_AUTHORITY_SEQUENCE
related_to:
- BHG_CONSTITUTION
- CANONICAL_STANDARDS_RECONCILIATION_MATRIX
extensions:
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
governs: []
---

# BHG Governance Architecture Map

## 1. Purpose

This document defines the structural architecture of the BHG-Governance repository.

It is subordinate to the applicable BHG constitutional and governance authority. Repository placement, filename and historical creation order do not create normative authority.

## 2. Authority position

BHG-Governance is the repository for the BHG governance system. Its scope includes governance models, policies, documentary standards, engineering governance, AI governance, automation governance and audit/validation artifacts.

It does not become an independent constitutional root and does not supersede the BHG Constitution or the approved cross-repository authority model.

## 3. Domain sequence

The repository is organized by functional governance layer:

```text
00-FOUNDATION
    ↓
00-GOVERNANCE
    ↓
01-POLICIES
    ↓
02-STANDARDS
    ↓
03-ENGINEERING
    ↓
04-AI
    ↓
05-AUTOMATION
    ↓
06-AUDIT
    ↓
99-HISTORY
```

This is a repository organization sequence, not a claim that every lower directory is normatively superior to every document in a higher directory. Normative authority is determined by the approved authority model and explicit relationships.

## 4. Domain responsibilities

### 00-FOUNDATION

Contains constitutional and foundational governance artifacts used by the governance repository.

### 00-GOVERNANCE

Contains canonical governance models, authority models and controlled reconciliation artifacts.

### 01-POLICIES

Contains enterprise and domain policy contracts subordinate to applicable governance authority.

### 02-STANDARDS

Contains controlled documentary, repository and implementation standards. Shared semantic contracts require one canonical owner.

### 03-ENGINEERING

Contains engineering policies, standards, ADRs and implementation governance subordinate to applicable policies and standards.

### 04-AI

Contains AI governance, standards and Genesis documentation. AI systems may analyze and enforce approved contracts but do not create normative authority.

### 05-AUTOMATION

Contains automation governance and operational contracts. Automation implements approved rules and must not invent authority.

### 06-AUDIT

Contains validation, conflict registers, audit reports and readiness assessments. Audit artifacts record evidence; they do not become normative authority merely by detecting a finding.

### 99-HISTORY

Contains immutable historical records and evidence. Historical artifacts do not redefine current authority.

## 5. Authority versus placement

The following rule is mandatory:

```text
folder != authority
filename != authority
creation_order != authority
approval_level != normative_level
```

Authority is resolved from the approved hierarchy and explicit normative relationships.

## 6. Document creation sequence

Every new normative or architectural document in this repository must follow:

```text
Identify subject
    ↓
Resolve canonical owner
    ↓
Resolve superior authority
    ↓
Select canonical document_id
    ↓
Select document_type and lifecycle state
    ↓
Declare governed_by / depends_on / related_to
    ↓
Assess cross-repository impact
    ↓
Create on non-main branch
    ↓
Validate metadata and authority graph
    ↓
Independent review
    ↓
Approval / merge according to governance
```

No document should be created merely because a directory appears to need another document.

## 7. Core documentary authority

The documentary standards form a contract stack:

```text
DOCUMENT_STANDARD
    ├── DOCUMENT_METADATA_STANDARD
    ├── DOCUMENT_IDENTIFIER_STANDARD
    ├── DOCUMENT_RELATIONSHIP_STANDARD
    ├── DOCUMENT_SCHEMA_STANDARD
    ├── DOCUMENT_GRAMMAR_STANDARD
    ├── DOCUMENT_HISTORY_MODEL
    └── DOCUMENT_VALIDATION_STANDARD
             └── DOCUMENT_LINTING_STANDARD
```

The stack separates semantic ownership from dependency. A subordinate standard may specialize a contract but may not silently redefine the contract owned by another standard.

## 8. Audit boundary

Audit findings are evidence for remediation.

An audit report does not itself grant authority to create, delete, rename or supersede normative documents. Remediation must be evaluated against the applicable canonical contract and recorded through controlled change.

## 9. Cross-repository boundary

BHG-Governance participates in the four-repository BHG normalization scope together with:

- BHG-Ecosystem-Foundation;
- bhg-knowledge;
- ZivaLatam.

Cross-repository authority follows `BHG_REPOSITORY_AUTHORITY_SEQUENCE`.

The governance repository does not acquire ownership of institutional architecture merely because it governs governance processes.

## 10. Baseline status

```text
status: Draft
canonical: false
effective: false
automation_ready: false
```

This version intentionally remains Draft until the applicable authority model and repository-wide normalization have passed independent validation.
