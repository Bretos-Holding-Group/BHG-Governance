---
document_id: BHG-UFCG-F4-EXP-001
title: BHG F4 Controlled Governance Experiment
version: 0.1.0
status: Proposed
document_type: controlled_experiment
governance_level: repository
owner: BHG Governance
approval_authority: BHG Governance review
---

# BHG F4 Controlled Governance Experiment v0.1

**Status:** Proposed experiment
**Governance state:** Not adopted
**Operational authority:** None
**Lifecycle stage:** F4 — Closed controlled test
**Parent model:** BHG Upward Feedback & Change Governance F0–F9

## 1. Purpose

Test whether the proposed F0–F9 feedback lifecycle can process a synthetic improvement proposal through controlled governance gates without modifying production systems or creating institutional authority.

## 2. Test subject

Synthetic proposal: **Document Lifecycle Reconciliation Engine**.

The proposal is intentionally derived from the problem that originated the F0–F9 model: declared document status may diverge from traceable governance history.

The experiment tests the governance mechanism, not the production implementation of a document engine.

## 3. Isolation boundary

- Synthetic identifiers only: `F4-BBX-###`.
- No production documents are promoted.
- No production repository policy is changed.
- No real employee or customer data is used.
- No F9 authority is created.
- No proposal may bypass the defined gates.

## 4. Controlled input

The synthetic proposal package must contain:

1. problem statement;
2. evidence summary;
3. proposed solution;
4. expected benefit;
5. estimated cost;
6. risks;
7. blast radius;
8. reversibility;
9. success metrics;
10. failure criteria.

## 5. Controlled execution

The experiment must simulate, in order:

`F0 → F1 → F2 → F3 → F4`

For each transition the evaluator records:

- required evidence present/absent;
- gate decision;
- authority required;
- authority exercised;
- transition validity;
- traceability identifier;
- rejection/hold reason where applicable.

The experiment must also inject invalid transitions, including attempts to move directly from F1 to F7 and F3 to F9.

Expected result: invalid transitions are rejected and do not alter the lifecycle state.

## 6. Adversarial controls

The controlled test must include:

- duplicate proposal;
- proposal with insufficient evidence;
- proposal with unsupported claimed impact;
- governance-bypass attempt;
- scope-creep attempt;
- repeated unsupported proposal;
- failed experiment result;
- good-faith failed proposal.

The system/model must distinguish a failed experiment from misconduct.

## 7. Success criteria

F4 passes only if:

1. every valid transition is recognized;
2. every prohibited transition is blocked;
3. evidence requirements are explicit;
4. governance authority is explicit;
5. rejected/failed proposals remain traceable;
6. good-faith failure is not treated as misconduct;
7. duplicate/noise proposals do not bypass triage;
8. the experiment produces no production change;
9. the same test package can be replayed with the same expected decision;
10. unresolved ambiguity is recorded rather than silently decided.

## 8. Failure criteria

F4 fails if any of the following occurs:

- an invalid transition is accepted;
- a proposal gains authority solely from its originator;
- evidence requirements are ambiguous enough to permit arbitrary promotion;
- a governance bypass succeeds;
- test activity modifies production governance;
- a failed good-faith experiment is classified as misconduct without an explicit rule;
- results cannot be reproduced from the recorded package.

## 9. Exit decision

Allowed outcomes:

- `F4_PASS` → eligible for F5 design;
- `F4_CONDITIONAL` → redesign and repeat F4;
- `F4_FAIL` → return to F3 or abandon the model component.

`F4_PASS` does not authorize F5. A separate F5 gate is mandatory.
