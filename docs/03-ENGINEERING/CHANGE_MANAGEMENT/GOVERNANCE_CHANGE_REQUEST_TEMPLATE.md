---
title: Governance Change Request Template
document_id: GOVERNANCE_CHANGE_REQUEST_TEMPLATE
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
- GOVERNANCE_CHANGE_REQUEST_STANDARD
governs: []
depends_on:
- DOCUMENT_METADATA_STANDARD
- BHG-POL-VERSIONING
related_to:
- ADR_STANDARD
extensions:
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
    relationship_target_reconciliation:
      baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
      performed: '2026-08-16'
      mode: canonicalize_or_classify_external
  legacy_relationships:
  - relationship: governed_by
    target: CHANGE_MANAGEMENT_README.md
    classification: missing_document_target
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
  - relationship: governs
    target: Future Governance Change Requests
    classification: external_scope
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
  - relationship: related_to
    target: CHANGELOG_POLICY.md
    classification: missing_document_target
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
---

# Governance Change Request Template

> Official template for creating controlled Governance Change Requests across the Breto's Holding Group ecosystem.

---

# Document Metadata

Every GCR shall contain the official BHG metadata structure.

Example:

---
title: 

document_id:

version:

status:

document_type: Governance Change Request

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

Change Identification
Change ID

Unique identifier for the change request.

Example:

GCR-0001
# Change Title

Short description of the requested change.

Example:

Introduce ADR Dependency Relationship Semantics
# Related Architecture Decision Record

Every GCR shall reference the approved ADR that authorizes the change.

Example:

related_adr:

- ADR-0001-DEPENDENCY-RELATIONSHIP-SEMANTICS.md
# Change Objective

Describe the expected result.

Example:

Define the official interpretation of depends_on relationships within BHG governance documents.
# Change Reason

Explain why the change is required.

Include:

business reason;
governance reason;
technical reason.
# Scope

Define the boundaries of the implementation.

# Included

List all authorized changes.

# Excluded

List changes that are explicitly outside the scope.

# Affected Repositories

List every repository impacted.

Example:

affected_repositories:

- BHG-GOVERNANCE
- BHG-Ecosystem-Foundation
# Affected Files

List exact files.

Example:

affected_files:

- docs/03-ENGINEERING/ADR/ADR_STANDARD.md
- docs/CHANGELOG.md
# Implementation Plan

Describe the required execution steps.

Example:

1. Update metadata standard.
2. Create ADR standard.
3. Validate references.
4. Execute repository review.
# Version Impact

Define expected version changes.

Example:

version_changes:

BHG-GOVERNANCE:
  before: 1.0.0
  after: 1.1.0
# Validation Criteria

Define how success will be verified.

Examples:

metadata validation passes;
repository structure remains compliant;
references are valid;
documentation builds successfully.
# Rollback Strategy

Define how the change can be reverted.

Example:

Restore previous document versions and revert associated commits.
# Implementation Evidence

Completed after execution.

Include:

commit hashes;
pull requests;
validation reports;
approval evidence.

# Approval Record

Example:

approval:

status:

approved_by:

approval_date:
# Completion Status

Example:

completion:

status:

completed_date:

validated_by:
# Institutional Principle

A Governance Change Request transforms approved decisions into controlled, traceable and verifiable implementation.

---
