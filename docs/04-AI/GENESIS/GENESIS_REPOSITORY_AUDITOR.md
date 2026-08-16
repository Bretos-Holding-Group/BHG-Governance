---
title: Genesis Repository Auditor
document_id: GENESIS-REPOSITORY-AUDITOR
version: 1.1.0
status: Approved
classification: Internal
created: 2026-07-11
last_updated: 2026-07-11
language: English
depends_on:
- GENESIS-PROFILE
- GENESIS-EXECUTION-CONTRACT
- GENESIS-COMMAND-PROTOCOL
- GENESIS-CONTEXT-ENGINE
- GENESIS-REPOSITORY-SCANNER
governs:
- GENESIS-HEALTH-MODEL
- GENESIS-PLANNING-ENGINE
document_type: AI Document
governance_level: AI
owner: BHG Governance Council
approval_authority: BHG Governance Council
effective_date: null
repository: BHG-GOVERNANCE
extensions:
  legacy_metadata:
    owners:
    - BHG Architecture Council
    - Genesis Engineering
    approvers:
    - BHG Governance Council
    namespace: Genesis
    applies_to:
    - All Genesis Execution Engines
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
    relationship_target_reconciliation:
      baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
      performed: '2026-08-16'
      mode: canonicalize_or_classify_external
    state: normalized
    date: '2026-08-16'
governed_by: []
related_to: []
---

# Genesis Repository Auditor

## Purpose

The Genesis Repository Auditor evaluates the repository against BHG governance, engineering standards and architectural rules.

Its objective is to determine the actual state of the repository and produce a deterministic audit report.

---

# Capability

Capability Name

Repository Audit

Capability Identifier

GEN-CAP-004

Description

Evaluate repository compliance, detect governance violations and produce actionable findings.

---

# Objectives

The Repository Auditor shall:

- Audit repository compliance.
- Detect governance violations.
- Detect architectural inconsistencies.
- Detect missing mandatory artifacts.
- Detect broken references.
- Detect dependency violations.
- Detect metadata inconsistencies.
- Detect repository risks.
- Generate deterministic findings.

---

# Audit Scope

The auditor shall evaluate:

Repository Structure

Repository Metadata

Governance Documents

Policies

Standards

Engineering Documents

AI Documents

Automation Documents

Architecture

Dependencies

Cross References

Naming Conventions

---

# Audit Categories

Governance Compliance

Documentation Compliance

Architecture Compliance

Metadata Compliance

Dependency Compliance

Repository Structure

Naming Compliance

Reference Integrity

Version Consistency

Repository Completeness

---

# Audit Pipeline

Load Repository Package

↓

Load Governance Rules

↓

Load Applicable Standards

↓

Execute Audit Rules

↓

Collect Findings

↓

Calculate Severity

↓

Generate Audit Report

↓

Return Certified Findings

---

# Finding Severity

Every finding shall be classified.

Supported levels:

Critical

High

Medium

Low

Informational

---

# Finding Structure

Each finding shall contain:

Identifier

Category

Severity

Title

Description

Affected Artifact

Applicable Standard

Evidence

Recommended Action

Certification Impact

---

# Audit Rules

The Repository Auditor shall verify:

Mandatory documents exist.

Document locations are valid.

Metadata is complete.

Naming conventions are respected.

Required dependencies exist.

References are valid.

Architecture matches repository structure.

Governance hierarchy is respected.

Repository integrity is preserved.

---

# Repository Risks

The auditor shall identify:

Missing documents

Duplicate artifacts

Broken references

Invalid metadata

Architecture drift

Policy conflicts

Dependency conflicts

Version conflicts

Repository inconsistencies

Unknown artifacts

---

# Audit Report

Every execution shall produce:

Repository Identifier

Audit Identifier

Execution Timestamp

Repository Version

Audited Scope

Compliance Summary

Finding Summary

Critical Findings

Recommendations

Next Actions

---

# Determinism

Equivalent repositories shall always generate equivalent audit findings.

---

# Failure Conditions

Auditing shall stop whenever:

Repository Package is unavailable.

Governance cannot be determined.

Applicable standards cannot be resolved.

Repository integrity cannot be verified.

---

# Output

The Repository Auditor shall produce:

Audit Report

Finding Inventory

Risk Summary

Compliance Summary

Repository Recommendations

Audit Identifier

---

# Compliance

Every Genesis-compatible execution engine shall execute the Repository Auditor before generating implementation plans or repository certifications.

Repository planning without a successful audit is prohibited.
