---
title: Genesis Context Engine
document_id: GENESIS-CONTEXT-ENGINE
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
governs:
- GENESIS-REPOSITORY-SCANNER
- GENESIS-REPOSITORY-AUDITOR
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
governed_by: []
related_to: []
normalization_state: normalized
normalization_baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
normalization_date: '2026-08-16'
---

# Genesis Context Engine

## Purpose

The Genesis Context Engine is responsible for determining, collecting, validating and maintaining every piece of contextual information required before any execution begins.

No Genesis-compatible execution engine shall execute any operation without first establishing a valid operational context.

---

# Capability

Capability Name

Context Resolution

Capability Identifier

GEN-CAP-002

Description

Build a complete operational context for every execution.

---

# Objectives

The Context Engine shall:

- Understand the current repository.
- Identify applicable governance.
- Determine execution scope.
- Load required documents.
- Resolve dependencies.
- Eliminate missing context.
- Produce deterministic executions.

---

# Context Layers

Genesis organizes context into independent layers.

## Layer 1

Execution Context

Contains:

- Current Intent
- Execution Mode
- Active Session

---

## Layer 2

Repository Context

Contains:

- Repository Structure
- Repository Metadata
- Repository Health

---

## Layer 3

Governance Context

Contains:

- Constitution
- Policies
- Standards
- Engineering Rules
- AI Rules
- Automation Rules

---

## Layer 4

Document Context

Contains:

- Active Document
- Dependencies
- References
- Metadata

---

## Layer 5

Architecture Context

Contains:

- Repository Architecture
- Component Relationships
- Dependency Graph

---

## Layer 6

Project Context

Contains:

- Current Phase
- Current Roadmap
- Pending Tasks
- Active Milestones

---

# Context Loading Pipeline

Execution Request

↓

Load Execution Context

↓

Load Repository Context

↓

Load Governance Context

↓

Load Document Context

↓

Load Architecture Context

↓

Load Project Context

↓

Validate Context

↓

Execute Intent

---

# Context Validation

Genesis shall verify:

- Repository availability.
- Required documents.
- Dependency integrity.
- Metadata consistency.
- Governance applicability.
- Architecture consistency.
- Version compatibility.

---

# Context Sources

The Context Engine may obtain information from:

- Repository files.
- Governance documents.
- Metadata headers.
- Repository structure.
- Architecture map.
- Roadmaps.
- Approved standards.

No external information shall be treated as authoritative unless explicitly approved.

---

# Context Cache

Execution engines may temporarily cache validated context.

Cached context shall be discarded whenever:

- Repository changes.
- Governance changes.
- Active branch changes.
- Requested scope changes.
- Context expiration occurs.

---

# Failure Conditions

Context resolution shall fail whenever:

- Repository cannot be analyzed.
- Required governance is missing.
- Mandatory documents are unavailable.
- Metadata is invalid.
- Dependency graph cannot be resolved.
- Architecture integrity cannot be verified.

---

# Output

The Context Engine shall produce a Context Package containing:

- Execution Scope
- Repository Snapshot
- Applicable Governance
- Loaded Documents
- Dependency Graph
- Architecture Summary
- Validation Status
- Context Identifier

---

# Determinism

Equivalent repositories and equivalent requests shall always generate equivalent Context Packages.

---

# Compliance

Every Genesis execution engine shall invoke the Context Engine before executing any operational intent.

Executing without a validated Context Package is prohibited.
