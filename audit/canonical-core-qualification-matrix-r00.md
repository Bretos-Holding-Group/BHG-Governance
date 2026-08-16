# Canonical Core Qualification Matrix R00

Status: CANDIDATE / NON-NORMATIVE
Scope: 60 discovery candidates derived from the 485-document four-repository corpus.
Purpose: reproducibly separate discovery centrality from normative authority and qualify candidates for Canonical Core R00.

## Qualification contract

A candidate is NOT canonical merely because it has a high discovery score. Qualification requires independent evidence across:

1. centrality — structural importance in the corpus;
2. normative authority — authority supported by the existing normative hierarchy;
3. contractuality — defines reusable documentary/governance rules;
4. foundationality — required to construct or validate downstream layers;
5. ownership — belongs to the semantic owner of the domain it governs;
6. status — lifecycle state is recorded, never silently promoted;
7. conflict state — known normative conflicts are surfaced;
8. cycle state — participation in governed_by cycles is surfaced;
9. evidence — every qualification claim must be traceable to repository evidence.

## Decision classes

- CORE-CANDIDATE: strong structural/foundational evidence; still subject to normative validation.
- SUPPORTING-CANDIDATE: important dependency or contract but not independently foundational.
- HOLD: unresolved authority, ownership, conflict, identity, or lifecycle issue.
- EXCLUDE-FROM-CORE: insufficient core role despite high structural centrality.

## Anti-inference rules

- Centrality MUST NOT create authority.
- Draft status MUST NOT be promoted to Approved by automation.
- A governed_by cycle MUST NOT be broken automatically.
- File path/name MUST NOT establish ownership or authority.
- Approval authority MUST NOT be conflated with normative authority.
- Existing documents remain evidence even when not approved.

## Reproducibility

Input corpus: 485 documents.
Discovery set: top 60 candidates produced by Canonical Core Discovery R00.
Qualification is reproducible when each row is backed by: document identity, repository/path, discovery score, status, authority evidence, ownership evidence, conflict references, cycle references, and qualification rationale.

## Required row schema

| Rank | Document ID | Repository/path | Discovery score | Status | Authority evidence | Ownership | Contractuality | Foundationality | Conflict | Cycle | Decision | Rationale |
|---:|---|---|---:|---|---|---|---|---|---|---|---|---|

The populated 60-row machine-derived register is the authoritative working artifact for this phase; this matrix defines the qualification contract and must be evaluated against the complete corpus before any document is promoted to canonical status.

## Eight authority cycles

The following nodes remain protected from automatic edge deletion or rewriting until semantic authority is demonstrated:

- BHG-MIG-304657D4691E
- BHG-MIG-38F961165834
- BHG-MIG-4EF6926C68EA
- BHG-MIG-71A9F2A90F32
- BHG-MIG-83A30C7D861D
- BHG-MIG-AB1A5B8A9156
- BHG-MIG-D13DBA24B680
- BHG-MIG-D140A7A5674C

Cycle participation is a HOLD condition for automatic canonization, not an instruction to delete or alter the documents.

## Normative conflict gate

Known conflicts, including Constitution / Legal Hierarchy / Governance Approval Model and related authority-model conflicts, must be resolved or explicitly bounded before affected documents can receive unconditional CORE-CANDIDATE status.

## Expansion rule

Canonical Core R00 is intended as a minimal semantic foundation. The remaining corpus is not discarded or ignored. Each subsequent layer must inherit the Core contracts and preserve traceability back to the original repository evidence.
