---
document_id: BHG-GOV-CSR-001
title: BHG Canonical Status Registry
document_type: governance_record
version: 1.0.1
status: Effective
governance_level: Enterprise
created: 2026-08-16
last_updated: 2026-08-16
classification: Internal
language: en
repository: BHG-GOVERNANCE
governed_by:
- BHG-MIG-5456F6E19A27
- BHG-GOV-CDRM-001
owner: BHG Governance Council
approval_authority: BHG Governance Council
effective_date: null
extensions:
  legacy_metadata:
    canonical: true
    effective: true
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
depends_on: []
related_to: []
---

# BHG Canonical Status Registry

## Purpose

This registry records the approved operational status of canonical BHG governance artifacts. It is an execution-control record and does not replace the governed artifact itself.

## Current status

| Document ID | Artifact | Version | Canonical | Effective | Execution state |
|---|---|---:|---:|---:|---|
| `BHG-GOV-CDRM-001` | BHG Canonical Documentary Relationship Model | 0.1.0 | true | true | Enabled for governance validation |

## Authority rule

The registered status applies only after the corresponding controlled change is merged into the authoritative branch. A registry entry cannot by itself create authority where the underlying artifact has not been approved through the applicable governance process.

## Enforcement boundary

The relationship model governs the semantics of documentary relationships. Automation may validate compliance with the model, but may not invent normative relationships, promote unapproved artifacts, or override BHG governance.

## Transition record

- Prior state: Draft / non-canonical / non-effective.
- Approval event: repository owner approval recorded on 2026-08-16.
- Controlled integration: PR #5 merged into the PR #4 integration branch.
- Main-branch integration: PR #4 merged into `main` on 2026-08-16.
- Status-synchronization gate: PR #6 merged into `main` on 2026-08-16.

## Status

```text
registry_status: Effective
model_status_authorized: Canonical + Effective
execution_mode: governance-validation-enabled
main_branch_activation: complete
```
