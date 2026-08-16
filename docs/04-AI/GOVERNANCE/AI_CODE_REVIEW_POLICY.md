---
title: AI Code Review Policy
document_id: BHG-MIG-2FB0C2D083A9
document_type: AI Document
version: 0.1.0
status: Draft
governance_level: AI
owner: BHG Governance Council
approval_authority: BHG Governance Council
created: '2026-07-06'
last_updated: '2026-07-06'
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
normalization_state: normalized
normalization_baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
normalization_date: '2026-08-16'
---

# AI Code Review Policy

Version: 1.0.0

Status: Active

Owner:
Ziva Engineering System (ZES)

---

# 1. Purpose

This policy defines the mandatory review process for every source code artifact generated, modified or suggested by Artificial Intelligence.

Its objective is to guarantee engineering quality, architectural consistency and security.

---

# 2. Scope

This policy applies to:

- AI generated code
- AI assisted code
- Refactoring
- Bug fixes
- Infrastructure as Code
- Configuration files
- Tests
- Scripts
- Documentation containing executable examples

---

# 3. Fundamental Principle

AI may generate code.

AI never approves code.

Approval belongs to the engineering review process.

---

# 4. Review Objectives

Every review shall verify:

- correctness
- readability
- maintainability
- security
- performance
- architectural consistency
- documentation consistency

---

# 5. Mandatory Verification

Every review must verify:

Architecture compliance

Documentation consistency

Coding Standard compliance

Security Standard compliance

Naming Standard compliance

API Standard compliance

Testing requirements

Backward compatibility

Dependency impact

Performance impact

---

# 6. AI Review Responsibilities

AI reviewers shall:

identify defects

identify duplicated logic

identify dead code

identify unnecessary complexity

identify security risks

identify missing documentation

identify architectural violations

recommend improvements

---

# 7. Human Responsibilities

Human reviewers shall:

validate business logic

approve architectural exceptions

approve security exceptions

approve production deployment

---

# 8. Automatic Review

Whenever possible automated review shall include:

Static Analysis

Linting

Formatting

Dependency Scan

Secret Detection

License Verification

Test Execution

Coverage Analysis

---

# 9. Security Review

Every code review shall verify:

input validation

authentication

authorization

secret handling

logging

error handling

dependency risks

OWASP compliance

---

# 10. Documentation Review

Every implementation must be checked against:

existing documentation

ADRs

Architecture documents

API documentation

Policies

---

# 11. AI Limitations

AI shall never:

approve its own code

ignore failing tests

remove security controls

bypass review

approve undocumented changes

introduce hidden functionality

---

# 12. Review Classification

Reviews shall be classified as:

Minor

Standard

Major

Critical

Critical reviews require senior approval.

---

# 13. Traceability

Every review shall record:

review date

reviewer

AI model (if applicable)

findings

decision

required changes

approval

---

# 14. Compliance

Code that does not pass review shall not be merged into the official repository.
