---
title: Approval Candidate Package Specification
document_id: APPROVAL_CANDIDATE_PACKAGE_SPECIFICATION
version: 1.0.2
status: Draft
document_type: Standard
governance_level: Enterprise
owner: BHG Governance Council
approval_authority: BHG Governance Council
created: 2026-08-16
last_updated: 2026-08-16
effective_date: null
classification: Internal
language: en
repository: BHG-GOVERNANCE
governed_by:
- DOCUMENT_STANDARD
- DOCUMENT_METADATA_STANDARD
- DOCUMENT_IDENTIFIER_STANDARD
- DOCUMENT_HISTORY_MODEL
- DOCUMENT_RELATIONSHIP_STANDARD
depends_on:
- DOCUMENT_SCHEMA_STANDARD
- DOCUMENT_LINTING_STANDARD
related_to: []
extensions: {}
governs: []
---

# Approval Candidate Package Specification

## 1. Purpose

This standard defines the canonical structure, evidence requirements, lifecycle, reproducibility requirements, and authority boundaries for BHG Approval Candidate Packages (AC Packages).

An AC Package is an evidence-bearing candidate for independent verification. It is not an approval instrument and cannot itself confer normative authority.

## 2. Scope

The initial candidate set is:

| Package ID | Package type | Purpose |
|---|---|---|
| AC-01 | Remediation Candidate | Evidence that the remediation baseline was integrated. |
| AC-02 | Validation Execution Candidate | Evidence that post-remediation validation executed against the intended revision. |
| AC-03 | N3 Candidate | Documentary identity and metadata evidence. |
| AC-04 | N4 Candidate | Documentary relationship evidence. |
| AC-05 | N5 Candidate | Post-remediation structural output evidence. |
| AC-06 | Consolidated Candidate | Reconciliation of AC-01 through AC-05 into one custody chain. |

## 3. Authority boundary

AC Packages may record evidence, validation results, candidate conclusions, exceptions, and verification requirements. They MUST NOT:

- declare a normative artifact approved;
- canonicalize or activate an artifact merely by packaging evidence;
- substitute automated validation for authorized human approval;
- modify the authority of the BHG Constitution or any superior governance instrument;
- infer approval from a successful workflow, merge, artifact, or candidate state.

The required process boundary is:

```text
Evidence
  ↓
Validated
  ↓
Approval Candidate
  ↓
Independent Verification
  ↓
Approved / Rejected / Returned
```

AC Package lifecycle states are distinct from the lifecycle states of governed documents.

## 4. Canonical package fields

Every AC Package MUST expose these exact fields:

| Field | Required | Meaning |
|---|---|---|
| `package_id` | Yes | Stable identifier AC-01 through AC-06. |
| `package_type` | Yes | Canonical package classification. |
| `status` | Yes | AC lifecycle state; construction/automation may assign only `DRAFT` or `CANDIDATE`. |
| `claim` | Yes | Precise bounded assertion proposed for independent verification. |
| `source_pr` | Conditional | PR directly producing or representing the evidence. |
| `base_sha` | Conditional | Exact base revision where a boundary exists. |
| `head_sha` | Conditional | Exact resulting revision where one exists. |
| `evidence_ids` | Yes | Ordered references to evidence records. |
| `artifact_sha256` | Conditional | SHA-256 digest of a referenced evidence artifact. |
| `dependencies` | Yes | Explicit package/document/workflow/revision/evidence dependencies. |
| `acceptance_criteria` | Yes | Testable criteria for the claim. |
| `validation_result` | Yes | Observed validation result: `PASS`, `FAIL`, `PENDING`, or `NOT_APPLICABLE`. |
| `scope` | Yes | Exact bounded subject of the claim. |
| `non_authority_statement` | Yes | Explicit statement that the package is not approval, canonicalization, activation, or authorization. |
| `independent_verification_requirement` | Yes | Requirement for authorized independent verification. |
| `verification_record` | Conditional | Required once independent verification occurs; absent before then. |

`document_id` identifies this specification. `package_id` identifies a package instance. They MUST NOT be conflated.

No alternate field names may silently replace these canonical names.

## 5. Evidence record contract

Each referenced evidence record MUST contain, where applicable:

| Field | Required | Meaning |
|---|---|---|
| `evidence_id` | Yes | Stable unique evidence identifier. |
| `evidence_type` | Yes | Commit, workflow run, job, artifact, report, inventory, verification record, or equivalent. |
| `source` | Yes | Authoritative source system. |
| `subject` | Yes | Exact object, corpus, revision, execution, or event evidenced. |
| `reference` | Yes | Immutable or directly resolvable evidence reference. |
| `sha256` | Conditional | Digest where applicable. |
| `timestamp` | Conditional | Creation/execution time where applicable. |
| `result` | Conditional | Observed result for execution/validation evidence. |
| `scope` | Yes | Exact bounded scope. |

Evidence MUST distinguish observed facts from interpretation and candidate conclusions.

## 6. Reproducibility

Where technically applicable, each package MUST record:

- repository identifier;
- exact revision SHA(s);
- workflow name;
- workflow run ID;
- relevant job ID(s);
- execution result;
- artifact identifier;
- artifact SHA-256;
- validation scope;
- validation method/rule set;
- execution timestamp;
- package generation timestamp.

A human-readable `PASS` or `SUCCESS` statement is insufficient when machine-verifiable evidence exists.

## 7. Validation versus verification

`validation_result` records an observed result from an automated or procedural validation process.

`verification_record` records an independent assessment. One MUST NOT overwrite or substitute for the other.

The verification record MUST contain:

| Field | Required |
|---|---|
| `verification_id` | Yes |
| `verifier` | Yes |
| `verification_timestamp` | Yes |
| `verification_scope` | Yes |
| `verification_result` | Yes: `PASS`, `REJECTED`, or `RETURNED` |
| `verification_evidence` | Yes |
| `exceptions` | Yes, including an explicit empty set when none exist |
| `authority_reference` | Yes |

## 8. AC-01 through AC-06 requirements

### AC-01
Must establish `PR #14 → merged revision → remediated corpus`, including exact merge SHA, affected scope, remediation categories, acceptance criteria, and the link to the validation input.

### AC-02
Must establish that post-remediation validation executed against the intended revision, including PR, base/head SHA, workflow, run, jobs, result, artifact and digest where applicable, exact scope, and observational/non-authoritative nature.

### AC-03 — N3
Must isolate evidence for frontmatter completeness, required metadata completeness, document identifier uniqueness, permitted metadata keys, and lifecycle/status validity. Counts MUST be reproduced from the actual evidence artifact.

### AC-04 — N4
Must identify the relationship validation workflow, exact revision, relevant jobs, relationship rules, canonical schema compatibility, supported legacy metadata extension handling, result, and acceptance criteria. Validation MUST use the applicable canonical documentary model rather than obsolete metadata assumptions.

### AC-05 — N5
Must establish post-remediation structural output integrity, including corpus, revision, evidence inventory, validation execution, acceptance criteria, and known blockers/exceptions.

### AC-06
Must reconcile AC-01 through AC-05 without introducing a new substantive gate. It MUST include immutable references/digests, dependency and revision correspondence, workflow/artifact correspondence, acceptance-criteria reconciliation, blockers/exceptions, scope, authority boundary, and independent-verification requirement.

The canonical chain is:

```text
AC-01
 ↓
PR #14 remediation
 ↓
AC-02
 ↓
PR #15 validation execution
 ↓
AC-03 — N3
 ↓
AC-04 — N4
 ↓
AC-05 — N5
 ↓
AC-06 — consolidated candidate
```

## 9. Candidate lifecycle

```text
DRAFT
  ↓
CANDIDATE
  ↓
INDEPENDENT_VERIFICATION
  ├── APPROVED
  ├── REJECTED
  └── RETURNED
```

Only an authorized independent approval process may assign `APPROVED`. Automated validation MUST NOT assign it.

## 10. Completeness criteria

A candidate is structurally complete only when all required fields exist; the claim and scope are explicit; identifiers are stable and unique; evidence resolves; revisions are exact; acceptance criteria are testable; validation is traceable; dependencies and exceptions are disclosed; the non-authority statement is present; independent verification is required; and, once performed, the verification record is complete and distinct from validation evidence.

Failure of a mandatory criterion prevents the package from being treated as complete.

## 11. Consolidated reconciliation matrix

AC-06 SHOULD use:

| Requirement | Evidence source | Result | Verification state |
|---|---|---|---|
| Remediation integrated | AC-01 | Actual evidence result | Pending independent verification |
| Validation executed | AC-02 | Actual evidence result | Pending independent verification |
| N3 | AC-03 | Actual evidence result | Pending independent verification |
| N4 | AC-04 | Actual evidence result | Pending independent verification |
| N5 | AC-05 | Actual evidence result | Pending independent verification |
| Chain integrity | AC-06 | Actual evidence result | Pending independent verification |
| Human independent approval | Authorized verifier | PENDING | Required |

Results MUST reflect evidence and MUST NOT be fabricated to satisfy the matrix.

## 12. Evidence integrity

SHA-256 is the canonical artifact digest unless a superior BHG standard requires another algorithm. A changed artifact is new evidence and requires a new digest and corresponding reconciliation.

## 13. Independence

The process that constructs or automatically validates a candidate MUST NOT silently self-authorize its final approval. Independent verification MUST examine package completeness, evidence authenticity/correspondence, revision correspondence, claim accuracy and scope, acceptance criteria, exceptions, authority boundaries, and reproducibility where applicable.

## 14. Change control

Changes to this specification MUST follow the BHG governed documentation lifecycle and applicable human approval process. A change MUST NOT retroactively alter previously issued evidence without explicit versioned reconciliation.

## 15. Non-authority statement

Every generated AC Package MUST include or canonically reference:

> This Approval Candidate Package is an evidence and verification candidate only. It does not constitute normative approval, canonicalization, activation, or authorization. Final approval requires the applicable independent verification and authorized approval process.

## 16. Current adoption target

The initial target chain is:

```text
AC-01 → PR #14 Remediation
AC-02 → PR #15 Validation Execution
AC-03 → N3
AC-04 → N4
AC-05 → N5
AC-06 → Consolidated Candidate
```

This specification remains `Draft` until the applicable human governance process adopts it.
