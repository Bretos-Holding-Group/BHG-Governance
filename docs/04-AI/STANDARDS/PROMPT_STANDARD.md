---
title: Prompt Standard
document_id: BHG-MIG-F86E17B1CAA4
document_type: AI Document
version: 0.1.0
status: Draft
governance_level: AI
owner: BHG Governance Council
approval_authority: BHG Governance Council
created: '2026-07-07'
last_updated: '2026-07-07'
effective_date: null
classification: Internal
language: en
repository: BHG-GOVERNANCE
extensions:
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
governed_by: []
governs: []
depends_on: []
related_to: []
---

# Prompt Standard

Version: 1.0.0

Status: Active

Owner:
Breto's Holding Group

---

# 1. Purpose

Define the engineering standard for designing prompts across the BHG ecosystem.

Every prompt shall follow a consistent structure that maximizes clarity, determinism, maintainability and reuse.

---

# 2. Design Principles

Every prompt shall be:

Simple

Modular

Predictable

Explicit

Auditable

Reusable

Maintainable

Traceable

Secure

Scalable

---

# 3. Prompt Architecture

Every prompt shall contain the following sections whenever applicable.

Purpose

Context

Role

Objectives

Constraints

Inputs

Expected Outputs

Rules

Workflow

Failure Handling

Examples

Metadata

---

# 4. Prompt Length

Prompts shall contain only the information required.

Avoid unnecessary verbosity.

Prefer modular composition over extremely large prompts.

---

# 5. Context

Context shall include only relevant information.

Avoid duplicated instructions.

Avoid conflicting information.

Context shall be deterministic.

---

# 6. Role Definition

Every prompt shall clearly define:

Who the AI is.

What responsibilities it has.

What responsibilities it does NOT have.

Authority boundaries.

Decision boundaries.

---

# 7. Objectives

Objectives shall be:

Specific

Measurable

Ordered

Non-conflicting

Business-oriented

---

# 8. Constraints

Every prompt shall explicitly define:

Forbidden actions

Required behaviour

Security limitations

Legal limitations

Privacy rules

Governance rules

---

# 9. Inputs

Input requirements shall specify:

Mandatory inputs

Optional inputs

Accepted formats

Validation rules

Expected quality

---

# 10. Outputs

Expected outputs shall define:

Structure

Formatting

Completeness

Language

Precision

Traceability

Confidence when applicable

---

# 11. Prompt Modularity

Large prompts shall be divided into reusable components.

Examples:

Context Modules

Knowledge Modules

Role Modules

Policy Modules

Output Modules

Validation Modules

---

# 12. Reusability

Prompts shall avoid project-specific assumptions whenever possible.

Reusable components are preferred.

---

# 13. Determinism

Prompts shall minimize ambiguity.

Expected behaviour shall remain stable across executions.

---

# 14. Error Handling

Every prompt shall define behaviour for:

Missing information

Contradictory inputs

Invalid requests

Security violations

Insufficient confidence

---

# 15. Examples

Complex prompts should include examples illustrating expected behaviour.

Examples shall remain synchronized with the current version.

---

# 16. Documentation

Every prompt shall include metadata.

Minimum:

Prompt ID

Version

Owner

Status

Dependencies

Last Review

Security Level

Department

---

# 17. Maintainability

Prompts shall be easy to modify.

Avoid duplicated logic.

Avoid hidden dependencies.

Prefer composition over repetition.

---

# 18. Human Oversight

Prompt outputs are recommendations.

Final decisions belong to authorized human personnel.

No prompt may override corporate governance.

---

# 19. Continuous Improvement

Prompts shall evolve using:

Operational metrics

Audit reports

Peer review

User feedback

Incident analysis

Governance updates
