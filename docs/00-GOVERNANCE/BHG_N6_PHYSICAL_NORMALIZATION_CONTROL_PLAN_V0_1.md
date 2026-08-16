---
document_id: BHG-GOV-N6-PNC-001
title: BHG N6 Physical Normalization Control Plan
document_type: governance_normalization_control_plan
governance_level: Enterprise
version: 0.1.0
status: Review
created: 2026-08-16
last_updated: 2026-08-16
approval_authority: BHG Governance Council
governed_by:
- BHG_CONSTITUTION
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
    normalization_phase: N6
    approval_readiness: BLOCKED_PENDING_N3_N5
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
---

# BHG N6 Physical Normalization Control Plan v0.1

## Rule

Physical changes are downstream of semantic normalization. No document is moved, renamed, merged, split, deleted, or reclassified as canonical solely because of its path or filename.

## Required preconditions

- N3 identity conflicts resolved or explicitly mapped.
- N4 relationship mappings complete.
- N5 authority reconciliation complete.
- Approval-candidate packages prepared for affected normative standards.
- Historical evidence preserved.
- Migration mapping reviewed.

## Controlled operations

1. Rename with identity preservation.
2. Move with reference reconciliation.
3. Merge only with explicit supersession history.
4. Split only with explicit identity mapping.
5. Archive without destroying evidence.
6. Remove only after duplicate/obsolescence evidence and authorization.

## Gate

N6 is currently **BLOCKED_PENDING_N3_N5**. This is intentional. The plan is ready; execution against source documents must wait until the semantic and authority gates are closed.
