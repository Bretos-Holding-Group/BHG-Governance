---
title: Genesis Health Calculation Standard
document_id: GEN-BHG-STD-009
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
    category: Health Standard
    parent_documents:
    - GENESIS_PROFILE.md
    - GENESIS_EXECUTION_CONTRACT.md
    - GENESIS_HEALTH_MODEL.md
    - GENESIS_REPOSITORY_DISCOVERY_PROTOCOL.md
    related_documents:
    - GENESIS_FINDING_CLASSIFICATION_STANDARD.md
    - GENESIS_EXECUTION_REPORT_STANDARD.md
    - GENESIS_CERTIFICATION_ENGINE.md
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
governed_by: []
governs: []
depends_on: []
related_to: []
---

# Genesis Health Calculation Standard

## 1. Purpose

This standard defines the official methodology used by Genesis to calculate Repository Health.

Every Health Score SHALL be deterministic, reproducible and evidence-based.

Estimated scores are strictly prohibited.

---

# 2. Health Calculation Principles

Genesis SHALL:

- Calculate only measurable metrics.
- Ignore subjective opinions.
- Use repository evidence only.
- Produce identical results for identical repositories.

---

# 3. Health Dimensions

Repository Health SHALL be calculated using the following dimensions.

| Dimension | Weight |
|------------|-------:|
| Governance | 20% |
| Documentation | 20% |
| Architecture | 15% |
| Engineering | 15% |
| AI | 10% |
| Automation | 10% |
| Repository Integrity | 10% |

Total Weight SHALL equal 100%.

---

# 4. Dimension Rules

Every dimension SHALL receive a score between:

- 0
- 25
- 50
- 75
- 100

Intermediate arbitrary values SHALL NOT be generated.

---

# 5. Repository Health Formula

Overall Repository Health SHALL be calculated as:

Σ (Dimension Score × Weight)

No alternative formula is permitted.

---

# 6. Health Levels

| Score | Status |
|---------|------------|
| 95–100 | Excellent |
| 85–94 | Very Good |
| 75–84 | Good |
| 60–74 | Acceptable |
| 40–59 | Needs Improvement |
| 20–39 | Critical |
| 0–19 | Repository Failure |

---

# 7. Evidence Requirement

Every dimension SHALL reference:

- evaluated documents
- evaluated standards
- evaluated policies
- detected violations

Dimensions without evidence SHALL receive zero points.

---

# 8. Confidence

Genesis SHALL publish:

- Health Score
- Confidence Level

Confidence values:

- COMPLETE
- HIGH
- MEDIUM
- LOW
- FAILED

Health scores with LOW or FAILED confidence SHALL NOT be eligible for certification.

---

# 9. Health Report

Every Repository Health Report SHALL contain:

- Overall Score
- Dimension Scores
- Evidence
- Violations
- Recommendations
- Confidence

---

# 10. Compliance

No Genesis Engine may calculate Repository Health using alternative methodologies.

Violation of this standard invalidates Repository Certification.
