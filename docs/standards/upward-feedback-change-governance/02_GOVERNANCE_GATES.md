---
document_id: BHG-UFCG-GATE-001
title: BHG Upward Feedback & Change Governance — Gate Model
version: 0.1.0
status: Proposed
governance_level: repository
document_type: governance_model
owner: BHG Governance
approval_authority: BHG Governance review
maturity: design
operational_use: prohibited
---

# Governance Gates

| Transition | Gate | Minimum decision evidence |
|---|---|---|
| F0 → F1 | Proposal Intake Gate | Clear problem and proposed direction |
| F1 → F2 | Evidence Gate | Evidence, impact, reasoning, risks and scope |
| F2 → F3 | Experiment Authorization Gate | Hypothesis, metrics, test design, rollback and resource justification |
| F3 → F4 | Controlled Test Gate | Isolated test environment and safety controls |
| F4 → F5 | Limited Deployment Gate | Passing controlled results, monitoring and rollback |
| F5 → F6 | Local Scale Gate | Pilot evidence, operational stability and acceptable incidents |
| F6 → F7 | Local Validation Gate | Reproducible local outcome and documented limitations |
| F7 → F8 | Cross-Entity Applicability Gate | Evidence from multiple contexts or strong generalization case |
| F8 → F9 | BHG Standardization Gate | Institutional authority, normative documentation, ownership and lifecycle controls |

## Gate invariants

1. No gate may infer evidence that has not been collected.
2. A failed experiment may return to an earlier state or be abandoned; failure is not automatically misconduct.
3. Contradictory evidence must remain visible.
4. A proposal cannot alter the governed system merely by entering the feedback channel.
5. Escalation increases required evidence and authority.
6. Rollback must be defined before material real-world exposure.
7. F9 standards require a defined revocation and supersession mechanism.

## Decision separation

The person proposing a change may participate in evaluation, but proposal authorship alone does not constitute approval authority. Separation of proposal, evidence review, authorization and institutional adoption should be used where risk warrants it.
