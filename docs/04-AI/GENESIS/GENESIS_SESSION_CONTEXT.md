---
title: Genesis Session Context
document_id: GEN-BHG-RUN-015
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
    category: Runtime Context
    parent_documents:
    - GENESIS_PROFILE.md
    - GENESIS_EXECUTION_CONTRACT.md
    - GENESIS_RUNTIME_BOOTSTRAP.md
    - GENESIS_RUNTIME_STATE_MACHINE.md
    related_documents:
    - GENESIS_EXECUTION_HISTORY_STANDARD.md
    - GENESIS_CONTEXT_ENGINE.md
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

# Genesis Session Context

## 1. Purpose

This document defines the runtime information maintained during every Genesis execution session.

The Session Context represents the complete operational state required for deterministic execution.

---

# 2. Session Principles

Every execution SHALL own one Session Context.

Session Context SHALL exist only during an active execution session.

Session Context SHALL never persist after session completion unless explicitly archived.

---

# 3. Mandatory Session Information

Every Session Context SHALL contain:

Session ID

Execution ID

Runtime ID

Repository ID

Repository Version

Repository Commit

Genesis Version

Execution Mode

Execution Timestamp

Current Runtime State

Current Engine

Current Command

Execution Objective

---

# 4. Repository Context

The session SHALL include:

Repository Structure

Architecture Map

Governance Documents

Policies

Standards

Engineering Documents

AI Documents

Automation Documents

Dependency Graph

Repository Metadata

Repository Health

---

# 5. Execution Context

Genesis SHALL maintain:

Loaded Engines

Active Findings

Execution Queue

Validation Status

Certification Status

Execution Progress

Execution Confidence

---

# 6. User Context

The session SHALL maintain:

Execution Request

Authorized Scope

Requested Output

Execution Restrictions

Language Configuration

Provider Information

---

# 7. Context Updates

Session Context SHALL be updated whenever:

Runtime State changes.

Repository changes.

Execution Phase changes.

New findings appear.

Validation completes.

Certification completes.

---

# 8. Context Integrity

Every update SHALL preserve:

Consistency

Traceability

Completeness

Determinism

No partial updates are allowed.

---

# 9. Session Termination

Upon completion Genesis SHALL:

Generate final reports.

Archive execution metadata.

Release runtime resources.

Destroy transient execution context.

Preserve only approved historical records.

---

# 10. Compliance

Every Genesis-compatible execution engine SHALL implement this Session Context specification.
