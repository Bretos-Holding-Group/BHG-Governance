---
title: BHG Repository Authority Sequence
document_id: BHG_REPOSITORY_AUTHORITY_SEQUENCE
document_type: Governance Architecture
governance_level: Enterprise
version: 0.1.0
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
- CANONICAL_STANDARDS_RECONCILIATION_MATRIX
- BHG-AUD-NORM-001
related_to:
- BHG-Ecosystem-Foundation
- bhg-knowledge
- ZivaLatam
extensions:
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
---

# BHG Repository Authority Sequence

## 1. Purpose

This document defines the cross-repository authority and implementation sequence for the four repositories currently included in the BHG normalization scope.

It is an implementation bridge for the draft Canonical Authority Model. It does not create authority above that model, the BHG Constitution, or any approved superior governance artifact.

## 2. Core rule

Repository location does not create normative authority.

A repository may own a domain of knowledge or implementation without becoming an independent constitutional root.

Cross-repository relationships shall distinguish normative authority, semantic ownership, dependency, specialization, implementation and evidence.

## 3. Authority graph

```text
LEVEL 1 — SUPREME
BHG CONSTITUTION
        │
        ▼
LEVEL 2 — FOUNDATIONAL GOVERNANCE
        │
        ├── BHG-Ecosystem-Foundation
        │     institutional / ecosystem architecture
        │
        └── BHG-Governance
              governance, policies and standards
                    │
                    ▼
LEVEL 3/4 — DOMAIN SPECIALIZATION
        │
        ├── bhg-knowledge
        │     knowledge-system specialization
        │
        └── ZivaLatam
              product / engineering specialization
                    │
                    ▼
LEVEL 5–7 — PROCEDURES / IMPLEMENTATION
                    │
                    ▼
LEVEL 8 — RECORDS / EVIDENCE
```

The two Level-2 repositories are peer domains under the constitutional hierarchy. BHG-Ecosystem-Foundation does not govern BHG-Governance, and BHG-Governance does not govern the institutional architecture owned by the Foundation repository.

## 4. Domain ownership

| Repository | Primary responsibility | Must not become authority for |
|---|---|---|
| BHG-Ecosystem-Foundation | institutional and ecosystem architecture | governance procedures, product implementation |
| BHG-Governance | governance models, policies, standards, validation | product-specific architecture or business implementation |
| bhg-knowledge | organizational knowledge system and knowledge operations | constitutional authority or enterprise governance |
| ZivaLatam | Ziva product, architecture and engineering specialization | BHG-wide governance or constitutional authority |

Shared concepts require one canonical semantic owner. A downstream repository may specialize a shared contract but must not silently redefine it.

## 5. Consumption sequence

```text
1. BHG Constitution
2. BHG-Ecosystem-Foundation — applicable institutional/ecosystem architecture
3. BHG-Governance — applicable governance, policy and standards
4. Repository-local architecture and domain contracts
5. Repository-local implementation documentation
6. Code / configuration / workflows
7. Audit records and evidence
```

The sequence is a resolution order: when a new document is created, its applicable superior authority must be identified before its local scope is defined.

## 6. Future document creation gate

A new normative or architecture document shall not be created until the author or agent has:

1. identified the repository and domain;
2. identified the applicable superior authority;
3. verified that an existing document does not already own the semantic subject;
4. selected a canonical `document_id`;
5. selected the canonical document type and lifecycle state;
6. declared `governed_by`, `depends_on` and `related_to` according to their distinct semantics;
7. checked cross-repository impact;
8. created the change on a non-main branch;
9. validated metadata, relationships and authority direction;
10. preserved an auditable change record.

## 7. Relationship rules

`governed_by` means normative subordination.

`depends_on` means prerequisite dependency and does not by itself establish authority.

`related_to` means association and does not establish authority.

`implements` means realization of an existing rule.

Repository relationships shall never use `depends_on` or `related_to` as an implicit substitute for `governed_by`.

## 8. Cross-repository specialization

BHG-Ecosystem-Foundation owns institutional and ecosystem architecture inside its approved scope.

BHG-Governance owns the governance system, including governance models, policies, documentary standards and compliance mechanisms inside its approved scope.

bhg-knowledge consumes applicable Foundation and Governance contracts and may specialize knowledge taxonomy, workflows and services.

ZivaLatam consumes applicable Foundation and Governance contracts. Its Engineering Charter, ZES rules, ADRs and implementation contracts are local specializations and must not redefine enterprise governance semantics.

## 9. Change sequencing

Cross-repository changes shall be executed in dependency order:

```text
Foundation / constitutional impact
        ↓
Governance contract impact
        ↓
Shared contract normalization
        ↓
Knowledge / product specialization
        ↓
Implementation
        ↓
Validation and audit
```

A downstream repository must not be normalized against an unresolved upstream contract when the downstream change depends on that unresolved meaning.

## 10. Baseline status

```text
status: Draft
canonical: false
effective: false
automation_ready: false
```
