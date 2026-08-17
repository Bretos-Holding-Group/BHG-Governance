---
document_id: BHG-UFCG-MOD-001
title: BHG Upward Feedback & Change Governance — F0-F9 Lifecycle Model
version: 0.1.0
status: proposed
maturity: model
document_type: conceptual_model
owner: BHG Governance
operational_use: prohibited
---

# F0–F9 Lifecycle

## State definitions

| State | Name | Meaning | Required evidence | Maximum blast radius |
|---|---|---|---|---|
| F0 | Observation | Problem, risk, inefficiency or opportunity identified | Observation record | None |
| F1 | Proposal | Candidate solution expressed | Proposal identity and rationale | None |
| F2 | Fundamented Proposal | Proposal supported by evidence, impact and reasoning | Evidence, impact, risks, cost, scope | None |
| F3 | Experiment Candidate | Authorized candidate for controlled testing | Hypothesis, metrics, success/failure criteria, rollback | Controlled |
| F4 | Closed Controlled Test | Tested in sandbox/lab/isolated environment | Reproducible test results | Controlled |
| F5 | Limited Real-World Deployment | Small real environment, local entity or subsidiary | Pilot evidence, monitoring, rollback | Limited |
| F6 | Local/Subsidiary Scale | Full adoption within validated local scope | Operational evidence and incident record | Local |
| F7 | Validated Local Change | Positive local result formally demonstrated | Validation package | Local |
| F8 | BHG Standard Candidate | Demonstrated potential for cross-entity reuse | Cross-entity applicability evidence | Candidate cross-entity |
| F9 | Institutional Standard | BHG formally adopts the change | Standardization decision, normative documentation and controls | BHG-wide as declared |

## Non-success states

`REJECTED`, `FAILED`, `ABANDONED`, `PAUSED`, `REVOKED`, and `SUPERSEDED` are lifecycle outcomes or conditions, not substitutes for evidence of success.

## Promotion rule

No state promotion is automatic. Every transition requires a defined gate, evidence package and authorized decision.

## Critical rule

F1/F2/F3 documentation cannot be represented as operationally validated. F4–F7 require actual controlled or real-world evidence. F8 requires evidence that the capability generalizes beyond its originating context. F9 requires formal institutional adoption.
