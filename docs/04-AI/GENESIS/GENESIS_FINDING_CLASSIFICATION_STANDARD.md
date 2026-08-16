---
title: Genesis Finding Classification Standard
document_id: GEN-BHG-STD-010
version: 1.1.0
status: Approved
owner: BHG Architecture Council
effective_date: TBD
classification: Internal
document_type: AI Document
governance_level: AI
approval_authority: BHG Governance Council
created: '2026-07-11'
last_updated: '2026-07-11'
language: en
repository: BHG-GOVERNANCE
extensions:
  legacy_metadata:
    review_authority: BHG Governance Council
    category: Audit Standard
    parent_documents:
    - GENESIS_PROFILE.md
    - GENESIS_EXECUTION_CONTRACT.md
    - GENESIS_REPOSITORY_AUDITOR.md
    - GENESIS_HEALTH_CALCULATION_STANDARD.md
    related_documents:
    - GENESIS_EXECUTION_REPORT_STANDARD.md
    - GENESIS_CERTIFICATION_ENGINE.md
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
---

# Genesis Finding Classification Standard

## 1. Purpose

This standard defines the official classification model used by Genesis to identify, categorize, prioritize and report repository findings.

Every finding SHALL follow a deterministic classification process.

---

# 2. Finding Definition

A Finding is any verified condition detected by Genesis that affects repository quality, governance, integrity, compliance or certification.

Findings SHALL be supported by repository evidence.

---

# 3. Finding Categories

Genesis SHALL classify findings into one of the following categories:

- Governance
- Documentation
- Architecture
- Engineering
- AI
- Automation
- Security
- Compliance
- Repository Integrity
- Traceability
- Dependencies

A finding SHALL belong to one primary category.

---

# 4. Severity Levels

Every finding SHALL receive one severity level.

| Level | Meaning |
|--------|---------|
| INFO | Informational only |
| LOW | Minor improvement recommended |
| MEDIUM | Moderate issue requiring correction |
| HIGH | Significant issue affecting repository quality |
| CRITICAL | Blocks certification or execution |

Severity SHALL be determined using objective repository evidence.

---

# 5. Finding Status

Every finding SHALL contain one lifecycle state.

- Open
- In Progress
- Mitigated
- Resolved
- Accepted Risk

---

# 6. Evidence Requirement

Every finding SHALL include:

- Finding ID
- Category
- Severity
- Description
- Repository Evidence
- Affected Documents
- Recommended Action

Findings without evidence SHALL NOT be reported.

---

# 7. Certification Impact

Certification impact SHALL be classified as:

- None
- Minor
- Moderate
- Major
- Blocking

Blocking findings SHALL prevent repository certification.

---

# 8. Priority Calculation

Genesis SHALL prioritize findings using:

1. Severity
2. Certification Impact
3. Number of affected documents
4. Dependency impact

No subjective prioritization is permitted.

---

# 9. Reporting

Every Repository Report SHALL summarize findings by:

- Category
- Severity
- Certification Impact
- Status

---

# 10. Compliance

Every Genesis Engine producing repository findings SHALL implement this standard.

Alternative finding classification models are prohibited.
