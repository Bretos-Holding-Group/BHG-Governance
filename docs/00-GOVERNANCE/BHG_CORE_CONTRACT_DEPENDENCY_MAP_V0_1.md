---
document_id: BHG-GOV-N2-CDM-001
title: BHG Core Contract Dependency Map
document_type: Governance Reconciliation Matrix
governance_level: Enterprise
version: 0.1.0
status: Review
created: 2026-08-16
last_updated: 2026-08-16
approval_authority: BHG Governance Council
governed_by:
- BHG-GOV-CAM-001
related_to:
- BHG-GOV-N2-CCR-001
owner: BHG Governance Council
effective_date: null
classification: Internal
language: en
repository: BHG-GOVERNANCE
extensions:
  legacy_metadata:
    canonical: false
    effective: false
    automation_ready: false
    normalization_phase: N2
    approval_readiness: SUPPORTING_ARTIFACT
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
governs: []
depends_on: []
normalization_state: normalized
normalization_baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
normalization_date: '2026-08-16'
---

# BHG Core Contract Dependency Map v0.1

## 1. Purpose

This map defines the semantic ownership and dependency boundaries required to reconcile the core documentary contracts without conflating authority, dependency, implementation and representation.

## 2. Contract ownership

| Contract | Owns | Must not own |
|---|---|---|
| BHG Constitution | Supreme governance | Lower documentary implementation semantics |
| Authority Model | Authority semantics and institutional authority concepts | Document metadata mechanics |
| Canonical Authority Model | Canonical reconciliation target for authority | Independent constitutional authority |
| Document Standard | Umbrella documentary contract | Specialized field/identity/relationship meanings |
| Metadata Standard | Metadata field semantics | Structural serialization or authority decisions |
| Identifier Standard | Permanent document identity | Metadata field meaning outside identity |
| Schema Standard | Structural representation | Semantic redefinition of fields/relations |
| Relationship Standard | Relationship vocabulary and semantics | Identity assignment or approval authority |
| Grammar Standard | Textual/Markdown representation | Schema or metadata semantics |
| History/Lifecycle Model | Evolution and transition semantics | Approval authority itself |
| Validation Standard | Conformance evaluation | Normative rule creation |
| Linting Standard | Static enforcement mechanics | Normative rule creation |

## 3. Required dependency direction

```text
Constitution
   ↓
Authority Model
   ↓
Canonical Authority Model
   ↓
Document Standard
   ↓
+-------------------------------+
| Metadata                       |
| Identifier                     |
| Schema                         |
| Relationship                   |
| Grammar                        |
| History / Lifecycle            |
+-------------------------------+
   ↓
Validation / Linting / Automation
```

The arrows above describe dependency and semantic precedence for normalization. They do not replace explicit `governed_by` relationships.

## 4. Non-substitutability rules

- A folder cannot substitute for `governed_by`.
- `depends_on` cannot substitute for normative authority.
- A schema cannot substitute for metadata semantics.
- A metadata field cannot substitute for an approval event.
- A linter cannot substitute for governance approval.
- A version number cannot substitute for supersession evidence.
- A repository cannot substitute for a governance level.

## 5. CDRM compatibility

The Canonical Documentary Relationship Model is the current effective owner of documentary relationship-model semantics. Its effective state does not automatically make every dependency effective. This map therefore treats the six core contracts as reconciliation inputs until their own approval gates are satisfied.

## 6. Approval-package requirement

Before a contract is presented for approval, its package must identify:

```text
current identity
current version
proposed version
semantic owner
upstream authority
normative dependencies
observed conflicts
resolution decisions
migration impact
validation evidence
approval authority
```

## 7. Current gate

```text
dependency map: COMPLETE FOR N2
semantic ownership: DEFINED
approval candidates: NOT YET GENERATED
normative promotions: 0
```
