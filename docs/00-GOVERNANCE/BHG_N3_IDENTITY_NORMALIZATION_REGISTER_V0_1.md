---
document_id: BHG-GOV-N3-IDR-001
title: BHG N3 Identity Normalization Register
document_type: governance_normalization_register
governance_level: Enterprise
version: 0.1.0
status: Review
created: 2026-08-16
last_updated: 2026-08-16
approval_authority: BHG Governance Council
governed_by:
- BHG-MIG-5456F6E19A27
- BHG-GOV-CAM-001
depends_on:
- DOCUMENT_IDENTIFIER_STANDARD
- DOCUMENT_METADATA_STANDARD
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
    normalization_phase: N3
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

# BHG N3 Identity Normalization Register v0.1

## Purpose

Establish the canonical identity rules and the evidence required to normalize document identity without changing source documents in this phase.

## Canonical rules

1. `document_id` is the permanent identity of a documentary artifact.
2. Version identifies an evolution of the same identity and does not create a new identity by itself.
3. Filename and repository path are locators, not identities.
4. A missing identifier is a normalization finding; it is not silently invented from a filename.
5. A duplicate identifier is a blocking integrity finding until resolved by evidence.
6. Historical documents retain identity and history; they are not rewritten merely to satisfy current conventions.
7. Any migration mapping must preserve source identity, destination identity, reason, evidence and effective date.

## Required N3 evidence

| Check | Required evidence | Gate |
|---|---|---|
| Identifier presence | Inventory record for every in-scope document | PASS/FAIL |
| Identifier uniqueness | Repository-wide uniqueness result | PASS/FAIL |
| Identifier stability | No identity derived solely from path/name | PASS/FAIL |
| Version separation | Identity/version distinction verified | PASS/FAIL |
| Registry coverage | Registry entry or explicit migration finding | PASS/FAIL |
| Historical preservation | Historical identity retained | PASS/FAIL |

## Approval consequence

This register does not approve the Identifier Standard. It prepares evidence for the approval candidate. Any identifier-standard change must be represented as a semantic delta against the current Draft version and verified before human approval.

## Exit condition

N3 may close when the inventory contains complete identity coverage, duplicate detection has been executed, unresolved identity conflicts are registered, and every proposed migration mapping has evidence.
