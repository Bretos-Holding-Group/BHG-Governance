---
document_id: BHG-GOV-N4-RNR-001
title: BHG N4 Relationship Normalization Register
document_type: governance_normalization_register
governance_level: Enterprise
version: 0.1.0
status: Review
created: 2026-08-16
last_updated: 2026-08-16
approval_authority: BHG Governance Council
governed_by:
- BHG-MIG-5456F6E19A27
- BHG-GOV-CDRM-001
depends_on:
- DOCUMENT_RELATIONSHIP_STANDARD
- DOCUMENT_IDENTIFIER_STANDARD
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
    normalization_phase: N4
    approval_readiness: EVIDENCE_READY
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

# BHG N4 Relationship Normalization Register v0.1

## Purpose

Define the evidence and transformation rules for normalizing documentary relationships against the effective Canonical Documentary Relationship Model.

## Canonical relationship vocabulary

The normalization process recognizes only explicitly defined relationship semantics. Current controlled categories include:

- `governed_by`
- `governs`
- `depends_on`
- `related_to`
- `references`
- `supersedes`
- `superseded_by`
- `replaces`
- `replaced_by`
- `implements`
- `implemented_by`

A relation must not be inferred from folder placement, filename, chronology, visual arrows or document proximity alone.

## N4 checks

| Check | Requirement | Gate |
|---|---|---|
| Vocabulary | Every declared relation maps to the controlled vocabulary | PASS/FAIL |
| Target resolution | Every target resolves to a canonical identity | PASS/FAIL |
| Authority separation | `governed_by` is not substituted by `depends_on` | PASS/FAIL |
| Inverse integrity | Required inverse relations are consistent | PASS/FAIL |
| Cycle detection | No prohibited authority cycles | PASS/FAIL |
| Directionality | Relationship direction is explicitly defined | PASS/FAIL |
| Historical relations | Supersession/replacement claims have evidence | PASS/FAIL |

## Ascendancy rule

Documentary ascendancy is a derived view of the authority graph. The canonical machine-readable relation remains `governed_by`. The compact human representation may show:

```text
ZivaID → ZivaLatam → BHG → BHG Constitution
```

The normative authority representation is:

```text
BHG Constitution → BHG → ZivaLatam → ZivaID
```

The arrow direction in these views is explanatory and never substitutes for explicit relation semantics.

## Exit condition

N4 may close when all in-scope relationships are classified, all targets are resolvable or explicitly registered as findings, authority cycles are tested, and migration mappings exist for every relation requiring normalization.

## Approval consequence

This register does not promote the Relationship Standard. It produces evidence against which the candidate version of that standard can be verified and later approved by the authorized human authority.
