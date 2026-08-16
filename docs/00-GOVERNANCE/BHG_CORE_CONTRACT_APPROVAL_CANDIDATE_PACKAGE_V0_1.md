---
document_id: BHG-GOV-ACP-001
title: BHG Core Contract Approval Candidate Package
document_type: governance_approval_package
governance_level: Enterprise
version: 0.1.0
status: Review
created: 2026-08-16
last_updated: 2026-08-16
approval_authority: BHG Governance Council
governed_by:
- BHG-MIG-5456F6E19A27
- BHG-GOV-N5-ARR-001
depends_on:
- BHG-GOV-N3-IDR-001
- BHG-GOV-N4-RNR-001
- BHG-GOV-N5-ARR-001
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
    normalization_phase: N5
    approval_readiness: CANDIDATE_PACKAGE_INCOMPLETE
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
    relationship_target_reconciliation:
      baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
      performed: '2026-08-16'
      mode: canonicalize_or_classify_external
governs: []
related_to: []
---

# BHG Core Contract Approval Candidate Package v0.1

## Purpose

Define the exact evidence package required before the six core documentary contracts may be submitted for formal approval.

## Contracts in scope

| Contract | Current state | Candidate gate |
|---|---|---|
| Canonical Authority Model | Draft | constitutional and approved-authority reconciliation |
| Document Standard | Draft | umbrella ownership and lifecycle reconciliation |
| Document Metadata Standard | Draft | field ownership and lifecycle reconciliation |
| Document Identifier Standard | Draft | permanent identity and registry closure |
| Document Schema Standard | Draft | structural/semantic boundary closure |
| Document Relationship Standard | Draft | vocabulary, graph and authority-boundary closure |

## Required evidence for every candidate

1. Stable `document_id`.
2. Current version and proposed version.
3. Exact semantic diff.
4. Normative owner.
5. Upstream authority.
6. All normative dependencies.
7. All observed conflicts.
8. Resolution decision for every conflict.
9. Migration impact.
10. Corpus validation result.
11. Backward-compatibility or breaking-change analysis.
12. Required implementation changes.
13. Required evidence/registry changes.
14. Authorized approval authority.
15. Approval event record.

## Candidate-state rule

`approval_candidate` is not an authority state. It means only that the technical and documentary package is assembled for human decision.

No automation may change `status: Draft` to `Approved` merely because the package exists or validation passes.

## Required approval sequence

```text
Draft
  ↓
Reconciled
  ↓
Evidence complete
  ↓
Approval candidate
  ↓
Authorized human approval event
  ↓
Approved
  ↓
Canonical (where designated)
  ↓
Effective (where designated)
```

## Current blockers

The package remains incomplete until N1 corpus evidence and N4/N5 graph evidence are actually generated from the in-scope repository state. The package must not claim PASS merely from the existence of these registers.

## Gate ownership

- Technical preparation: automation may assist.
- Evidence collection: automation may execute.
- Conflict detection: automation may execute.
- Resolution proposal: automation may prepare.
- Normative approval: authorized human governance authority only.
- Effective activation: authorized governance action plus recorded evidence.
