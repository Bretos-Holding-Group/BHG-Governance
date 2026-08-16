---
title: Architecture Decision Record Template
document_id: ADR_TEMPLATE
version: 1.0.0
status: Draft
document_type: Template
governance_level: Enterprise
owner: BHG Governance Council
approval_authority: BHG Governance Council
created: 2026-08-06
last_updated: 2026-08-06
effective_date: 2026-08-06
classification: Internal
language: en
repository: BHG-GOVERNANCE
governed_by:
- ADR_STANDARD.md
- ENGINEERING_GOVERNANCE_MODEL.md
governs:
- Future ADR Documents
depends_on:
- ADR_STANDARD.md
- DOCUMENT_METADATA_STANDARD.md
- VERSIONING_POLICY.md
related_to:
- GOVERNANCE_CHANGE_REQUEST_STANDARD.md
- GOVERNANCE_IMPLEMENTATION_WORKFLOW.md
extensions:
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
---

# Architecture Decision Record Template

> Official template for documenting architectural decisions across the Breto's Holding Group ecosystem.

---

# ADR Metadata

Every ADR shall begin with the official BHG metadata contract.

Example:

```yaml
---
title:

document_id:

version:

status:

document_type: ADR

governance_level:

owner:

approval_authority:

created:

last_updated:

effective_date:

classification:

language:

repository:

governed_by:

governs:

depends_on:

related_to:

# Decision Identification
ADR Number
Unique sequential identifier.
Example:
ADR-0001

# Decision Title
A concise description of the architectural decision.
Example:
Dependency Relationship Semantics

# Status
Current ADR lifecycle state.
Allowed values:
Draft
Review
Approved
Accepted
Superseded
Deprecated

# Context
Describe the situation that requires a decision.
Include:
current state;
business context;
technical context;
governance context.

# Problem Statement
Define the problem or uncertainty requiring resolution.
The problem statement should explain:
what needs to be solved;
why it matters;
consequences of not deciding.

# Decision
Describe the approved solution.
Include:
selected approach;
architectural principles applied;
constraints considered.

# Alternatives Considered
Document evaluated alternatives.
For each alternative include:
description;
advantages;
disadvantages;
reason for acceptance or rejection.
Example:
## Alternative 1

Description:

Advantages:

Disadvantages:

Decision:

# Consequences
Document the impact of the decision.
Include:
Positive Consequences
Expected benefits.
Negative Consequences
Trade-offs or limitations.
Operational Impact
Effects on processes, teams or systems.

# Implementation Impact
Define affected areas.
Example:
affected_repositories:

- repository-name

affected_documents:

- document-name.md

affected_systems:

- system-name

# rDependencies
Document required dependencies.
Example:
depends_on:

- DOCUMENT_NAME.md

# Related Decisions
Reference connected ADRs.
Example:
related_adrs:

- ADR-0001

# Governance Change Request
If implementation is required, reference the associated GCR.
Example:
related_gcr:

- GCR-0001

# Migration Strategy
Required when replacing an existing architecture.
Include:
migration steps;
compatibility requirements;
transition risks.

# Validation Criteria
Define how the decision will be validated.
Examples:
architecture compliance;
implementation verification;
automated validation;
governance review.

# Supersession Information
Required when replacing another ADR.
Example:
supersedes:

- ADR-0000

# Approval Record
Example:
approval:

status:

approved_by:

approval_date:

# Historical Record
Document significant lifecycle events.
Example:
## History

YYYY-MM-DD

Created ADR.

YYYY-MM-DD

Approved decision.

# Institutional Principle
An ADR preserves not only what was decided, but why the decision was necessary.

---