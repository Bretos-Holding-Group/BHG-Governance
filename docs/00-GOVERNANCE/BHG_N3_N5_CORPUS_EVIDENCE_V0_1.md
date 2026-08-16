---
document_id: BHG-GOV-N3N5-EVD-001
title: BHG N3-N5 Corpus Evidence Report
document_type: governance_evidence_report
governance_level: Enterprise
version: 0.1.0
status: Review
created: 2026-08-16
last_updated: 2026-08-16
approval_authority: BHG Governance Council
governed_by:
- BHG-MIG-5456F6E19A27
depends_on:
- BHG-GOV-N3-IDR-001
- BHG-GOV-N4-RNR-001
- BHG-GOV-N5-ARR-001
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
    normalization_phase: N3-N5
    approval_readiness: CONDITIONAL
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

# BHG N3-N5 Corpus Evidence Report v0.1

## Evidence source

The evidence below is derived from the read-only BHG Normalization Audit executed against commit `4a3b091de9d2657e1611565800f73d33c60c5d6e` (the merge commit of PR #12).

Workflow run: `31958863494` — BHG Normalization Audit.
Artifact: `bhg-n1-normalization-evidence`.
Artifact SHA-256: `78bcde03eb96e025538cb9a6da1a446ed766d101917707df7e6b711456e470ae`.

A second independent workflow on the same commit, `31958863501`, completed successfully for BHG Documentary Relationship Validation.

## Corpus measurements

| Measure | Result |
|---|---:|
| Markdown artifacts inventoried | 203 |
| Frontmatter present | 146 |
| Frontmatter absent | 57 |
| Documents with required-metadata gaps | 158 |
| Distinct frontmatter keysets | 35 |
| Duplicate document IDs | 2 IDs |

Duplicate IDs:

- `BHG-POL-001`
- `GEN-BHG-ENG-013`

## Status distribution observed

| Status | Count |
|---|---:|
| Approved | 97 |
| Official | 7 |
| Active | 4 |
| Effective | 2 |
| Review | 12 |
| Draft | 22 |
| draft | 2 |

The mixed `Draft` / `draft` representation is an observed lifecycle-normalization finding. It is not interpreted as equivalent authority without normalization rules.

## N3 — Identity evidence

N3 is **not closed**.

Blocking evidence findings are:

1. Two duplicate document IDs exist.
2. 57 Markdown artifacts have no frontmatter.
3. 158 artifacts have at least one required metadata field missing.
4. 35 frontmatter keysets demonstrate active schema fragmentation.

No identity is silently reassigned by this report. Identity migration requires explicit mapping and evidence.

## N4 — Relationship evidence

The relationship-validation workflow on the same commit completed successfully. This validates the currently effective CDRM and status-registry gate, but it does **not** mean that every legacy relationship in the corpus has been semantically normalized.

N4 therefore remains conditionally open pending corpus-wide classification of observed relations, target resolution, inverse consistency, and historical/supersession evidence.

The canonical ascendancy interpretation remains:

```text
ZivaID → ZivaLatam → BHG → BHG Constitution
```

as a compact human view, while machine-readable normative authority remains represented through explicit relationship semantics such as `governed_by`.

## N5 — Authority evidence

The inventory's contract dependency cluster reports all six core documentary contracts as `draft`:

- Canonical Authority Model
- Document Standard
- Document Metadata Standard
- Document Identifier Standard
- Document Schema Standard
- Document Relationship Standard

This is a material N5 finding. No automated process may promote these contracts based on the existence of validation or evidence alone.

The Constitution and currently approved authority instruments remain the operative normative sources until authorized human approval establishes otherwise.

## Approval consequence

The evidence package is **not an approval event** and does not change any governance status.

Current conclusion:

```text
N3  CONDITIONAL — identity normalization findings remain
N4  CONDITIONAL — corpus relationship normalization remains
N5  CONDITIONAL — core contracts remain Draft pending reconciliation and human approval
```

## Next required actions

1. Resolve or explicitly map the two duplicate IDs.
2. Establish the migration policy for the 57 frontmatter-less documents.
3. Resolve the 158 required-metadata gaps according to the canonical metadata contract.
4. Reconcile the 35 observed keysets into the canonical metadata/schema model.
5. Execute full relation-target and authority-graph analysis.
6. Produce six approval-candidate semantic diffs.
7. Only then present the approval package for independent verification and authorized human approval.

## Integrity rule

This report records observed evidence. It does not infer approval, canonicality, effectiveness, or authority from repository location, workflow success, status text, or automation output.
