---
document_id: BHG-GOV-N0-001
title: BHG Governance Core Normalization N0 Baseline
version: 0.1.0
status: Review
canonical: false
effective: false
approval_readiness: READY_PENDING_FORMAL_APPROVAL
document_type: Governance Reconciliation Matrix
governance_level: Enterprise
owner: BHG Governance Council
approval_authority: BHG Governance Council
created: 2026-08-16
last_updated: 2026-08-16
effective_date: null
classification: Internal
language: en
repository: BHG-GOVERNANCE
normalization_phase: N0
scope: BHG-Governance core
baseline_branch: main
baseline_commit: d3abf0044655021fe671e513740491143f5a3f81
baseline_tree: bf3e319509c05cfdeb215bc665085d12b30cfae7

# BHG Governance Core Normalization — N0 Baseline v0.1

## 1. Purpose

This control record freezes the documentary, normative and automation baseline from which normalization of the BHG Governance core shall proceed.

N0 does not normalize source documents. It establishes the exact starting state, scope, control references, dependencies, validation gates and approval-readiness conditions required before N1 inventory and classification begin.

## 2. Baseline identity

| Control | Value |
|---|---|
| Repository | `Bretos-Holding-Group/BHG-Governance` |
| Authoritative branch | `main` |
| Baseline commit | `d3abf0044655021fe671e513740491143f5a3f81` |
| Baseline tree | `bf3e319509c05cfdeb215bc665085d12b30cfae7` |
| N0 working branch | `normalization/N0-governance-core-baseline-v0.1` |
| Baseline date | 2026-08-16 |
| Scope | BHG Governance core |
| Main-branch changes during N0 | None |

The recursive repository tree at the baseline commit is complete (`truncated: false`) and includes the Foundation, Governance, Policies, Standards, Engineering, AI, Automation, Audit and History areas. The baseline therefore freezes the repository before any N1 normalization changes.

## 3. Normative root

The current constitutional root is:

```text
BHG Constitution v1.1.0
status: Approved
governance-level: Supreme
effective-date: 2026-01-01
blob_sha: a509e7cf589a5a954f8b4f8088458007fd17a5fd
```

The Constitution states that lower-level governance artifacts shall never contradict higher-level artifacts and that only authorized human governance bodies may approve, reject or modify official governance artifacts.

Therefore this N0 record may prepare, reconcile and verify the baseline, but it shall not self-promote a governance artifact to Approved.

## 4. Canonical control stack at N0

The current control stack is:

```text
BHG Constitution
        ↓
Canonical Authority Model
        ↓
Document Standard
        ↓
Metadata / Identifier / Schema / Relationship contracts
        ↓
N0 Baseline
        ↓
N1 Inventory and Classification
```

The following documents are the primary control anchors for N0.

| Artifact | Version | Current status | SHA |
|---|---:|---|---|
| BHG Constitution | 1.1.0 | Approved | `a509e7cf589a5a954f8b4f8088458007fd17a5fd` |
| Canonical Authority Model | 0.2.1 | Draft | `691957619b073319cd336a70bbd6a9f73eb6259c` |
| Canonical Documentary Relationship Model | 0.1.0 | Effective / Canonical | `84ea142037f1babc52a51a56c561337f8ea67882` |
| Canonical Status Registry | 1.0.1 | Effective | `f3f44a64e89ad5f4e729ca5e68ac83188985a21e` |
| Document Standard | current baseline | Draft | `b37eb1050d087ea29c4401960d6edd9d7e9d2cb9` |
| Document Metadata Standard | 1.3.0 | Draft | `028b68d381a213275ec22a5c74c8013ca4e3ed9e` |
| Document Identifier Standard | 1.2.1 | Draft | `6be53b6fa5a27d5252bfac3f137a1886e244e8f5` |
| Document Schema Standard | 1.2.0 | Draft | `88c010a97f4f7bae327c07dc2492c44ed707e323` |
| Document Relationship Standard | 1.3.0 | Draft | `d707bbc31c62597c97fe79bc2ca58ddd575ba230` |

## 5. Critical N0 finding

The Canonical Documentary Relationship Model is already Canonical + Effective, but several upstream documentary contracts remain Draft. This is not a reason to invalidate N0; it is a controlled dependency that must be resolved before those contracts are used as fully effective authority over the entire normalized corpus.

In particular:

1. `CANONICAL_AUTHORITY_MODEL.md` remains Draft.
2. `DOCUMENT_METADATA_STANDARD.md` remains Draft.
3. `DOCUMENT_IDENTIFIER_STANDARD.md` remains Draft.
4. `DOCUMENT_SCHEMA_STANDARD.md` remains Draft.
5. `DOCUMENT_RELATIONSHIP_STANDARD.md` remains Draft.

The current CDRM therefore supplies effective relationship semantics while these source contracts remain the subject of the preceding canonical-standards approval path. N0 records this explicitly rather than silently treating Draft artifacts as Effective.

## 6. Scope definition

N0 scope is the **BHG-Governance core repository** only.

Included documentary domains:

- Foundation
- Governance
- Policies
- Standards
- Engineering
- AI
- Automation
- Audit
- History
- repository-level governance artifacts
- governance automation workflows

Excluded from normalization modification during N0:

- BHG-Ecosystem-Foundation
- bhg-knowledge
- ZivaLatam
- external repositories or external legal records

Those repositories may be referenced as cross-repository context but are not altered by N0.

## 7. Scope boundaries inside BHG-Governance

N0 distinguishes three classes:

### A. Normative core

Constitution, governance models, policies, standards, approved procedures and other artifacts that can carry normative force.

### B. Operational/supporting documentation

Engineering, AI, automation and implementation documentation that may implement or specialize approved governance but cannot acquire authority merely from location or implementation.

### C. Records/history/evidence

Audit reports, evidence, logs, historical material and certification records. These preserve institutional state and evidence but do not become normative roots through their existence.

## 8. Immutable baseline controls

The following are frozen for N0:

- baseline commit SHA;
- baseline tree SHA;
- constitutional root SHA;
- canonical relationship model SHA;
- status registry SHA;
- primary document-contract SHAs;
- repository scope;
- normalization phase;
- branch separation from `main`.

Any change to the authoritative baseline requires a new controlled baseline and must not silently mutate this record.

## 9. N0 verification matrix

| Verification | Result | Evidence |
|---|---|---|
| Repository exists and is accessible | PASS | GitHub repository metadata |
| Authoritative branch identified | PASS | `main` |
| Baseline commit resolved | PASS | `d3abf0044655021fe671e513740491143f5a3f81` |
| Recursive tree resolved | PASS | complete tree, not truncated |
| Constitution located | PASS | `BHG_CONSTITUTION.md` |
| Constitution status verified | PASS | Approved |
| CDRM located | PASS | `BHG_CANONICAL_DOCUMENT_RELATIONSHIP_MODEL_V0_1.md` |
| CDRM status verified | PASS | Canonical + Effective |
| Status Registry located | PASS | `BHG_CANONICAL_STATUS_REGISTRY.md` |
| Status Registry verified | PASS | Effective |
| Metadata contract located | PASS | Draft |
| Identifier contract located | PASS | Draft |
| Schema contract located | PASS | Draft |
| Relationship contract located | PASS | Draft |
| N0 working branch isolated from main | PASS | dedicated branch |
| Main modified during N0 | NO | control preserved |
| Constitutional human-authority rule preserved | PASS | Constitution |
| Draft artifacts silently promoted | NO | prohibited |

## 10. Repository structure observed

The baseline contains, at minimum, these major documentary domains:

```text
00-FOUNDATION
00-GOVERNANCE
01-POLICIES
02-STANDARDS
03-ENGINEERING
04-AI
05-AUTOMATION
06-AUDIT
99-HISTORY
```

The repository also contains root-level architecture, changelog, bootstrap and README artifacts plus GitHub workflow automation.

N0 does not infer authority from these directory names. Directory placement is recorded as physical evidence only.

## 11. Canonical ancestry control

The effective relationship model requires ancestry to be derived from typed normative relationships rather than inferred from arrows or physical placement.

Human-readable subject ancestry remains:

```text
ZivaID → ZivaLatam → BHG → BHG Constitution
```

Normative authority remains:

```text
BHG Constitution → BHG → ZivaLatam → ZivaID
```

Machine resolution must use canonical identifiers and typed `governed_by` relationships.

For BHG-Governance N0, the equivalent documentary principle is:

```text
Document
  ↓ governed_by
Superior governance artifact
  ↓ governed_by
Higher governance artifact
  ↓
BHG Constitution
```

## 12. Baseline integrity rules

During N0 and all subsequent normalization phases:

1. `main` is not modified directly.
2. All normalization work occurs on controlled branches.
3. Every proposed change is reviewable through a controlled PR.
4. Draft artifacts are not treated as Effective authority.
5. Repository location does not create authority.
6. Filename does not create identity.
7. Chronology does not create supersession.
8. `depends_on` does not create authority.
9. AI/automation does not approve governance.
10. Historical evidence is preserved.
11. New baselines are created whenever the authoritative baseline changes.

## 13. N0 approval-readiness criteria

N0 is considered **READY_PENDING_FORMAL_APPROVAL** when all of the following are true:

- exact authoritative baseline is frozen;
- scope is explicit;
- constitutional root is verified;
- effective CDRM is verified;
- dependency standards are identified with their real statuses;
- no hidden Draft → Effective promotion has occurred;
- branch isolation is established;
- N1 entry conditions are explicit;
- approval packet is complete;
- remaining approval decision is limited to the authorized human governance authority.

All technical/preparatory conditions are satisfied by this baseline.

## 14. Formal approval gate

The only remaining gate for this N0 control record is formal approval by the authorized human governance authority under the applicable BHG approval process.

This record deliberately does not set:

```text
status: Approved
canonical: true
effective: true
```

Those values would constitute a governance decision and cannot be generated merely by technical automation or by the preparatory work recorded here.

## 15. N1 entry condition

Once N0 receives the applicable formal approval, N1 may begin against this exact baseline:

```text
N1 — Documentary Inventory and Classification
```

N1 shall inventory every in-scope documentary artifact, classify its node/document type, resolve identity, capture lifecycle state, record metadata completeness and identify every declared relationship before modifying source documents.

## 16. Approval packet summary

```text
CONTROL: BHG-GOV-N0-001
PHASE: N0
SCOPE: BHG-Governance core
BASELINE: d3abf0044655021fe671e513740491143f5a3f81
TREE: bf3e319509c05cfdeb215bc665085d12b30cfae7
STATUS: Review
APPROVAL_READINESS: READY_PENDING_FORMAL_APPROVAL
TECHNICAL_PRECONDITIONS: PASS
MAIN_PROTECTED: YES
DRAFT_PROMOTION: NONE
N1_READY: YES, AFTER FORMAL APPROVAL
```

## 17. Institutional principle

> Normalization begins with a frozen truth. No document is normalized against a moving target.

> The baseline records what exists; the subsequent phases determine what must change.
