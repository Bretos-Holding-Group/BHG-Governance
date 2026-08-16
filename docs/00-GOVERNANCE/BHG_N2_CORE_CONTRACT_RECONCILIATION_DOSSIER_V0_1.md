---
document_id: BHG-GOV-N2-CCR-001
title: BHG Core Contract Reconciliation Dossier
document_type: Governance Reconciliation Matrix
governance_level: Enterprise
version: 0.1.0
status: Review
canonical: false
effective: false
automation_ready: false
normalization_phase: N2
approval_readiness: NOT_YET_READY
created: 2026-08-16
last_updated: 2026-08-16
approval_authority: BHG Governance Council
governed_by:
  - BHG_CONSTITUTION
  - BHG-GOV-CAM-001
depends_on:
  - DOCUMENT_STANDARD
  - DOCUMENT_METADATA_STANDARD
  - DOCUMENT_IDENTIFIER_STANDARD
  - DOCUMENT_SCHEMA_STANDARD
  - DOCUMENT_RELATIONSHIP_STANDARD
  - DOCUMENT_GRAMMAR_STANDARD
  - DOCUMENT_HISTORY_MODEL
  - DOCUMENT_VALIDATION_STANDARD
related_to:
  - CANONICAL_STANDARDS_RECONCILIATION_MATRIX
---

# BHG Core Contract Reconciliation Dossier v0.1

## 1. Purpose

This dossier records the N2 reconciliation of the core documentary contracts before any of them can be presented as an approval candidate. It separates observed facts, normative target decisions, unresolved dependencies and approval gates.

N2 is not an approval action. It prepares the contracts so that a later authorized approval can be based on evidence rather than metadata promotion.

## 2. Scope

The core contract stack under reconciliation is:

1. `BHG-GOV-CAM-001` — Canonical Authority Model
2. `DOCUMENT_STANDARD`
3. `DOCUMENT_METADATA_STANDARD`
4. `DOCUMENT_IDENTIFIER_STANDARD`
5. `DOCUMENT_SCHEMA_STANDARD`
6. `DOCUMENT_RELATIONSHIP_STANDARD`

Supporting contracts are considered dependencies, not silently promoted by this dossier.

## 3. Current observed state

| Contract | Current version | Current state | N2 disposition |
|---|---:|---|---|
| Canonical Authority Model | 0.2.1 | Draft | Reconcile against Constitution + approved Authority Model |
| Document Standard | 1.2.0 | Draft | Reconcile umbrella ownership and lifecycle boundaries |
| Document Metadata Standard | 1.3.0 | Draft | Reconcile field ownership and lifecycle representation |
| Document Identifier Standard | 1.2.1 | Draft | Reconcile permanent identity and registry dependencies |
| Document Schema Standard | 1.2.0 | Draft | Reconcile structural ownership with metadata/relationship semantics |
| Document Relationship Standard | 1.3.0 | Draft | Reconcile relationship vocabulary and authority graph semantics |

No contract is promoted by this dossier.

## 4. Canonical dependency architecture

The target architecture is:

```text
BHG Constitution
       |
       v
Approved Authority Model
       |
       v
Canonical Authority Model
       |
       v
DOCUMENT_STANDARD
       |
       +----------------------+-----------------------+
       |                      |                       |
       v                      v                       v
METADATA_STANDARD       IDENTIFIER_STANDARD    SCHEMA_STANDARD
       |                      |                       |
       +----------------------+-----------------------+
                              |
                              v
                  RELATIONSHIP_STANDARD
                              |
                              v
                       VALIDATION / LINT
```

This diagram is a dependency/semantic architecture, not an assertion that every downward edge is `governed_by`. Normative authority and implementation/dependency edges remain distinct.

## 5. Reconciliation rules

### R1 — Constitution is the supreme authority

No candidate contract may define authority above or independently of the BHG Constitution.

### R2 — Approved authority precedes canonical authority

The Canonical Authority Model must be demonstrably derived from the approved Authority Model and Constitution. Its reconciliation decisions may not become effective merely because they are documented.

### R3 — Umbrella ownership

`DOCUMENT_STANDARD` owns the common documentary contract but delegates field, identity, structure, relationship and lifecycle semantics to their designated owners.

### R4 — Single semantic owner

Each shared concept must have one canonical semantic owner. Other contracts may consume, constrain implementation within scope, or reference it, but may not redefine its meaning.

### R5 — Identity precedes relationship resolution

Relationship targets require canonical document identity. Relationship normalization cannot be certified while identity collisions or unresolved canonical targets remain in the governed corpus.

### R6 — Schema consumes semantics

The schema defines representation and structural constraints. It cannot redefine metadata, identity or relationship meaning.

### R7 — Lifecycle semantics remain distinct from status representation

Metadata may carry lifecycle state, but the lifecycle model/process owns transition semantics. A status field alone does not constitute approval authority or evidence of an approval event.

### R8 — Automation is downstream

Validation, linting and synchronization may enforce approved contracts but cannot promote Draft contracts to Approved, Canonical or Effective without an authorized approval event.

## 6. Resolved N2 boundaries

The following boundaries are now explicit:

| Boundary | Resolution |
|---|---|
| Authority vs approval | Separate dimensions |
| Authority vs dependency | `governed_by` is not `depends_on` |
| Identity vs version | `document_id` remains permanent; `version` evolves |
| Metadata vs schema | Metadata owns meaning; schema owns representation |
| Relationship vs metadata | Relationship Standard owns relation meaning; Metadata Standard stores it |
| Grammar vs schema | Grammar serializes content; Schema owns structural representation |
| Lifecycle vs metadata | Lifecycle/process owns transitions; metadata represents state |
| Repository placement vs authority | Location is evidence, not authority |
| Automation vs governance | Automation validates/enforces approved rules; humans approve normative authority |

## 7. Remaining blockers before approval candidates

### B1 — Authority chain closure

The Canonical Authority Model still requires formal reconciliation against the currently approved authority instruments. Its eight-level hierarchy must be demonstrably compatible rather than merely asserted.

### B2 — Contract status consistency

The CDRM is already Canonical + Effective, while its upstream documentary contracts remain Draft. This is not automatically invalid, but the dependency graph must explicitly explain why the effective relationship model can operate without granting effective status to its upstream drafts.

### B3 — Metadata lifecycle precision

The metadata contract lists lifecycle values, while transition semantics are delegated. The approval candidate must explicitly distinguish representational values from approval/activation authority and define the allowed transition evidence.

### B4 — Identifier registry closure

The identifier standard depends on a registry model. N2 requires the registry relationship and uniqueness boundary to be explicit before identity normalization is certified.

### B5 — Schema/metadata exactness

The schema currently enumerates metadata fields but the exact field-level structural contract must be reconciled with the complete metadata standard before approval.

### B6 — Relationship graph closure

The relationship standard defines the vocabulary, but N1 corpus evidence must establish target resolvability, inverse consistency, authority-cycle absence and canonical identity coverage.

### B7 — Supporting contract disposition

Grammar, history, validation and linting contracts must either be confirmed as approved dependencies, reconciled as approval candidates, or explicitly classified as downstream/non-blocking for this approval package.

## 8. Approval-candidate gate

A core contract may enter `approval_candidate` only when:

- its semantic owner is unique;
- its upstream authority is explicit and valid;
- all normative dependencies are identified;
- all blocking conflicts are resolved or formally dispositioned;
- its relationship targets are canonicalizable;
- its lifecycle/status semantics are unambiguous;
- its version change is justified by the reconciliation delta;
- its approval package contains evidence and a change summary;
- no automation is being used as a substitute for approval.

## 9. N2 conclusion

N2 has resolved the architecture and semantic boundaries, but the six contracts are **not yet approval candidates** because B1-B7 require evidence or explicit disposition.

Therefore the correct state remains:

```text
N2: IN PROGRESS
approval_candidates: NOT_READY
contracts_promoted: 0
normative_status_changes: 0
```

This is intentional. N2 must close the remaining evidence gaps before an approval request can truthfully state that the contracts are internally coherent and executable.

## 10. Next execution block

1. Execute N1-M2/M3/M4 against the full BHG-Governance corpus.
2. Resolve identifier and relationship evidence.
3. Inspect supporting lifecycle/validation/grammar contracts.
4. Reconcile the Canonical Authority Model against approved authority.
5. Produce versioned approval-candidate drafts only after the blockers are closed.
