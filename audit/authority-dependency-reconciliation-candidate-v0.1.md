# BHG Authority & Dependency Reconciliation — Remediation Candidate v0.1

Status: CANDIDATE  
Authority effect: NONE  
Purpose: evidence-driven remediation planning only; no normative status or authority is established by this report.

## Summary

- Documents scanned: 203
- Relationship edges scanned: 797
- Resolved relationships: 785
- Missing-evidence findings: 12
- Authority-cycle findings: 8

## Required remediation

### A. Authority-cycle findings — HUMAN SEMANTIC DECISION REQUIRED

The eight reported cycle nodes form a mutually circular `governed_by` graph. Automation must not choose which authority edge to remove or reinterpret.

- `BHG-MIG-304657D4691E`
- `BHG-MIG-38F961165834`
- `BHG-MIG-4EF6926C68EA`
- `BHG-MIG-71A9F2A90F32`
- `BHG-MIG-83A30C7D861D`
- `BHG-MIG-AB1A5B8A9156`
- `BHG-MIG-D13DBA24B680`
- `BHG-MIG-D140A7A5674C`

Required human decision: identify the legitimate superior edge(s) and classify erroneous/redundant edges before any automated correction.

### B. Unresolved relationship targets — EVIDENCE / IDENTITY RECONCILIATION

- `BHG-FDN-001` — `governed_by` → `BHG_GOVERNANCE_ARCHITECTURE_MAP` — `docs/00-FOUNDATION/BHG_FOUNDATION_BOOK.md`
- `BHG-GOV-ROADMAP` — `related_to` → `CHANGELOG` — `docs/00-FOUNDATION/BHG_GOVERNANCE_ROADMAP.md`
- `BHG-FDN-002` — `governed_by` → `BHG_GOVERNANCE_ARCHITECTURE_MAP` — `docs/00-FOUNDATION/GLOSSARY.md`
- `GOVERNANCE_MODEL` — `depends_on` → `BHG_GOVERNANCE_ARCHITECTURE_MAP` — `docs/00-FOUNDATION/GOVERNANCE_MODEL.md`
- `GOVERNANCE_MODEL` — `governed_by` → `BHG_GOVERNANCE_ARCHITECTURE_MAP` — `docs/00-FOUNDATION/GOVERNANCE_MODEL.md`
- `BHG-GOV-002` — `governed_by` → `BHG_GOVERNANCE_ARCHITECTURE_MAP` — `docs/00-FOUNDATION/GOVERNANCE_PIPELINE.md`
- `BHG-POL-002` — `governed_by` → `BHG_GOVERNANCE_ARCHITECTURE_MAP` — `docs/01-POLICIES/DOCUMENT_POLICY.md`
- `F001_CHANGE_GOVERNANCE_VALIDATION` — `related_to` → `BHG_GOVERNANCE_ARCHITECTURE_MAP` — `docs/06-AUDIT/F001_CHANGE_GOVERNANCE_VALIDATION.md`
- `GENESIS-BOOTSTRAP-CERTIFICATION` — `related_to` → `BHG_GOVERNANCE_ARCHITECTURE_MAP` — `docs/06-AUDIT/GENESIS_BOOTSTRAP_CERTIFICATION.md`
- `GENESIS-BOOTSTRAP-CERTIFICATION` — `related_to` → `CHANGELOG` — `docs/06-AUDIT/GENESIS_BOOTSTRAP_CERTIFICATION.md`
- `GENESIS-BOOTSTRAP-CLOSURE-REVIEW` — `depends_on` → `BHG_GOVERNANCE_ARCHITECTURE_MAP` — `docs/06-AUDIT/GENESIS_BOOTSTRAP_CLOSURE_REVIEW.md`
- `GENESIS-BOOTSTRAP-CLOSURE-REVIEW` — `related_to` → `CHANGELOG` — `docs/06-AUDIT/GENESIS_BOOTSTRAP_CLOSURE_REVIEW.md`

Required action: resolve each target against the authoritative document/identifier registry or explicitly classify it as external/non-documentary. Do not infer authority from filenames.

## Approval boundary

No source document is modified by this candidate. Human approval is required before any semantic correction of `governed_by` edges or promotion of unresolved targets to canonical identifiers.
