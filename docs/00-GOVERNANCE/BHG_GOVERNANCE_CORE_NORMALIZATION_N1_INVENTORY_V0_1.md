---
document_id: BHG-GOV-N1-001
title: BHG Governance Core Normalization N1 Inventory and Classification Register
version: 0.1.0
status: Review
document_type: normalization_control_register
governance_level: Enterprise
owner: BHG Governance Council
approval_authority: BHG Governance Council
created: 2026-08-16
last_updated: 2026-08-16
classification: Internal
language: en
repository: BHG-GOVERNANCE
effective_date: null
extensions:
  legacy_metadata:
    canonical: false
    effective: false
    approval_readiness: NOT_YET_APPROVAL_READY
    normalization_phase: N1
    scope: BHG-Governance core
    baseline_branch: main
    baseline_commit: d3abf0044655021fe671e513740491143f5a3f81
    baseline_tree: bf3e319509c05cfdeb215bc665085d12b30cfae7
    n0_control: BHG-GOV-N0-001
    n1_mode: inventory_and_classification_only
    source_modification_permitted: false
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

# BHG Governance Core Normalization — N1 Inventory and Classification Register v0.1

## 1. Purpose

N1 establishes the documentary inventory and classification control layer for the BHG Governance core.

N1 is intentionally non-destructive. It records what exists, how it is physically organized, what class of artifact it appears to represent, what normative role it may have, and which questions must be resolved before source-document modification.

N1 does not approve, canonicalize, make effective, rewrite, rename, move, merge, delete or otherwise alter source governance artifacts.

## 2. Entry decision

N1 may be prepared before formal approval of N0 because it is an observational and classification phase and does not exercise normative authority over source documents.

The N0 control record remains `Review / READY_PENDING_FORMAL_APPROVAL`. N1 therefore inherits the frozen baseline as an **observational baseline**, not as an implicit approval of N0.

This distinction permits forward progress while preserving the constitutional approval gate.

## 3. Authoritative inventory source

The authoritative physical inventory source is the complete recursive Git tree of the frozen baseline commit:

```text
repository: Bretos-Holding-Group/BHG-Governance
branch: main
commit: d3abf0044655021fe671e513740491143f5a3f81
tree: bf3e319509c05cfdeb215bc665085d12b30cfae7
```

The exact verified N0 baseline is authoritative; N1 must not create a competing baseline.

## 4. N1 operating rule

The repository tree answers:

> What exists physically?

Document content answers:

> What does each artifact mean?

Governance metadata answers:

> What authority, lifecycle and relationship does the artifact claim?

N1 therefore keeps these three evidence layers separate:

```text
PHYSICAL INVENTORY
      ↓
CONTENT / DOCUMENT PROFILE
      ↓
GOVERNANCE PROFILE
```

No classification may use directory location as proof of authority.

## 5. Classification taxonomy

Every in-scope artifact shall receive a provisional node class and documentary class.

### Node classes

- `governance_instrument`
- `organizational_entity`
- `product_or_service`
- `system_or_implementation`
- `record_or_evidence`
- `unknown_pending_review`

### Documentary classes

- `constitution`
- `governance_model`
- `policy`
- `standard`
- `procedure`
- `guideline`
- `template`
- `architecture_or_design`
- `engineering_artifact`
- `ai_governance_artifact`
- `automation_artifact`
- `audit_artifact`
- `history_record`
- `registry`
- `roadmap_or_plan`
- `reference_or_glossary`
- `readme_or_navigation`
- `evidence_or_record`
- `unknown_pending_review`

Classification is descriptive until authority and lifecycle are independently resolved.

## 6. Physical domain inventory

The frozen repository contains the following major domains, verified from the complete recursive tree:

| Physical domain | Provisional functional class | N1 treatment |
|---|---|---|
| `.github/workflows` | automation_artifact | inventory + implementation classification |
| repository root | reference_or_navigation / governance support | individual classification |
| `docs/00-FOUNDATION` | governance_instrument candidates | priority normative review |
| `docs/00-GOVERNANCE` | governance_instrument candidates | priority normative review |
| `docs/01-POLICIES` | policy candidates | priority normative review |
| `docs/02-STANDARDS` | standard candidates | priority normative review |
| `docs/03-ENGINEERING` | system_or_implementation candidates | relationship review |
| `docs/04-AI` | ai_governance_artifact / implementation candidates | authority boundary review |
| `docs/05-AUTOMATION` | automation_artifact candidates | implementation and delegation review |
| `docs/06-AUDIT` | audit_artifact / record_or_evidence candidates | boundary review |
| `docs/99-HISTORY` | history_record candidates | immutable historical review |

This table is a classification hypothesis, not an authority declaration.

## 7. Priority inventory zones

N1 shall process the repository in this order:

```text
P0 — Constitutional and authority roots
P1 — Governance models and control registries
P2 — Documentary standards and contracts
P3 — Policies
P4 — Foundation models
P5 — Engineering / AI / Automation implementations
P6 — Audit records and historical records
```

The priority order exists to resolve semantic dependencies before downstream artifacts are interpreted.

## 8. P0/P1 control anchors observed

The baseline contains, at minimum, these critical anchors:

| Artifact | Current observed state | N1 role |
|---|---|---|
| `docs/00-FOUNDATION/BHG_CONSTITUTION.md` | Approved / Supreme | normative root |
| `docs/00-GOVERNANCE/CANONICAL_AUTHORITY_MODEL.md` | Draft | authority-model candidate; approval dependency |
| `docs/00-GOVERNANCE/BHG_CANONICAL_DOCUMENT_RELATIONSHIP_MODEL_V0_1.md` | Canonical / Effective | relationship semantics |
| `docs/00-GOVERNANCE/BHG_CANONICAL_STATUS_REGISTRY.md` | Effective | lifecycle/status registry |
| `docs/00-GOVERNANCE/CANONICAL_STANDARDS_RECONCILIATION_MATRIX.md` | governance control artifact | standards reconciliation |
| `docs/00-GOVERNANCE/BHG_REPOSITORY_AUTHORITY_SEQUENCE.md` | governance sequence artifact | repository authority interpretation |

The exact lifecycle status of every other artifact must be resolved from its content and applicable status registry rather than inferred from location.

## 9. P2 documentary contract inventory

The following standards are explicitly identified as a dependency cluster requiring resolution in later normalization work:

| Contract | Version | Current observed state | N1 disposition |
|---|---:|---|---|
| `DOCUMENT_STANDARD.md` | current baseline | Draft | dependency candidate |
| `DOCUMENT_METADATA_STANDARD.md` | 1.3.0 | Draft | dependency candidate |
| `DOCUMENT_IDENTIFIER_STANDARD.md` | 1.2.1 | Draft | dependency candidate |
| `DOCUMENT_SCHEMA_STANDARD.md` | 1.2.0 | Draft | dependency candidate |
| `DOCUMENT_RELATIONSHIP_STANDARD.md` | 1.3.0 | Draft | dependency candidate |
| `DOCUMENT_CLASSIFICATION_STANDARD.md` | present | state to resolve | classification contract candidate |
| `DOCUMENT_VALIDATION_STANDARD.md` | present | state to resolve | validation contract candidate |
| `DOCUMENT_LINTING_STANDARD.md` | present | state to resolve | enforcement contract candidate |
| `DOCUMENT_HISTORY_MODEL.md` | present | state to resolve | historical integrity candidate |
| `DOCUMENT_DEPENDENCY_STANDARD.md` | present | state to resolve | dependency semantics candidate |
| `NAMING_STANDARD.md` | present | state to resolve | naming normalization candidate |
| `TRACEABILITY_STANDARD.md` | present | state to resolve | traceability candidate |
| `QUALITY_STANDARD.md` | present | state to resolve | quality gate candidate |
| `REPOSITORY_STANDARD.md` | present | state to resolve | repository contract candidate |

N1 does not promote any of these artifacts.

## 10. Metadata inspection model

For each Markdown artifact, N1 shall capture, where present:

```text
document_id
title
document_type
version
status
canonical
effective
governance_level
owner
approval_authority
effective_date
classification
language
repository
path
governed_by
depends_on
related_to
references
supersedes
superseded_by
replaces
replaced_by
implements
implemented_by
```

Fields absent from a document are recorded as `missing`, not inferred.

Unknown fields are recorded separately and must not be silently deleted during N1.

## 11. Identity classification

Every artifact must eventually receive one of:

```text
IDENTITY_VERIFIED
IDENTITY_PRESENT_BUT_NONCONFORMING
IDENTITY_MISSING
IDENTITY_DUPLICATE
IDENTITY_CONFLICT
IDENTITY_PENDING
```

Filename similarity is not sufficient to establish identity.

## 12. Lifecycle classification

Every artifact must eventually receive one of:

```text
Draft
Review
Proposed
Approved
Canonical
Effective
Deprecated
Retired
Historical
Unknown
```

`Canonical` and `Effective` are distinct dimensions and must not be collapsed into one status string.

A document whose content says `Approved` but whose authoritative registry says `Draft` is a conflict requiring resolution.

## 13. Relationship classification

Declared relationships shall be normalized into the effective CDRM vocabulary:

```text
governed_by
governs
depends_on
related_to
references
supersedes
superseded_by
replaces
replaced_by
implements
implemented_by
```

N1 records raw declarations before mapping them. This preserves evidence and prevents accidental semantic rewriting.

## 14. Authority classification

Each artifact receives an authority posture:

```text
SUPREME
NORMATIVE
DELEGATED_NORMATIVE
IMPLEMENTATION
REFERENCE
AUDIT_EVIDENCE
HISTORICAL
NON_NORMATIVE
UNKNOWN_PENDING_REVIEW
```

The posture is provisional until resolved against the Canonical Authority Model and Constitution.

## 15. Duplicate and collision classes

N1 must identify:

- exact-content duplicates;
- near-duplicate documents;
- same-title different-ID collisions;
- same-ID different-content collisions;
- supersession candidates;
- replacement candidates;
- obsolete copies;
- historical copies that must not be deleted;
- documents whose role is duplicated by another document.

No duplicate may be deleted during N1.

## 16. Cross-domain boundary controls

N1 shall flag any artifact where:

- an implementation appears to declare normative authority;
- an audit record appears to establish policy;
- a history record appears to supersede current governance;
- a template is treated as an effective policy;
- a repository location is used as authority evidence;
- a README is treated as a normative source without explicit authority;
- an AI or automation document appears to grant itself approval authority;
- an entity relationship is encoded as a documentary relationship without typed semantics.

## 17. Special attention: `docs/06-AUDIT`

The audit domain requires explicit boundary classification because earlier normalization work identified an ownership/boundary concern around audit intelligence material.

N1 shall therefore distinguish:

```text
BHG governance audit records
        ≠
external/product engineering governance
        ≠
implementation intelligence
```

The physical presence of an audit artifact in BHG-Governance is not proof that BHG owns the normative subject described by that artifact.

## 18. Special attention: Genesis ecosystem

The repository contains substantial Genesis-related engineering, AI and automation material.

N1 shall not classify Genesis implementation documentation as normative merely because the material describes governance automation.

The following distinction is mandatory:

```text
Governance rule
      ≠
Governance implementation
      ≠
AI execution protocol
      ≠
Audit evidence
```

This boundary will be essential for later automation enforcement.

## 19. N1 evidence model

Each classification assertion should ultimately carry:

```yaml
source_path: <repository path>
source_sha: <blob sha>
classification: <value>
classification_confidence: high|medium|low
status_observed: <value|null>
identity_observed: <value|null>
relationship_observed: <value|null>
evidence_basis: content|metadata|registry|constitution|tree|history
review_state: pending|verified|conflict
```

N1 is evidence collection; it is not authority creation.

## 20. N1 findings register — initial structural findings

### N1-F001 — Upstream approval dependency cluster

**Severity:** HIGH

The authority model and core documentary contracts remain Draft while the CDRM is Effective/Canonical.

**Treatment:** carry forward to standards reconciliation/approval work.

### N1-F002 — Repository contains multiple documentary layers

**Severity:** MEDIUM

Foundation, Governance, Policies, Standards, Engineering, AI, Automation, Audit and History coexist in one repository.

**Treatment:** classify by semantic role rather than directory authority.

### N1-F003 — Potential authority/implementation boundary complexity

**Severity:** HIGH

Engineering, AI and Automation contain governance-adjacent artifacts that may describe or implement authority.

**Treatment:** typed node classification and explicit `implements`/`governed_by` separation.

### N1-F004 — Audit boundary requires explicit ownership classification

**Severity:** HIGH

The audit domain requires distinction between BHG-owned governance evidence and implementation/product audit intelligence.

**Treatment:** content-level ownership and authority review.

### N1-F005 — Historical material must remain reconstructable

**Severity:** MEDIUM

`99-HISTORY` must not be normalized as if it were current normative content.

**Treatment:** historical classification and immutable evidence preservation.

## 21. N1 non-destructive rule

No source document may be changed, renamed, moved, merged, deleted or status-promoted solely as a result of N1.

N1 outputs classification evidence and findings. Remediation belongs to later controlled phases.

## 22. N1 exit criteria

N1 is complete only when:

1. every in-scope artifact has an inventory record;
2. every artifact has a provisional node class;
3. every artifact has a documentary class or `unknown_pending_review`;
4. lifecycle state is recorded where observable;
5. identity state is recorded;
6. raw relationships are captured;
7. authority posture is recorded;
8. duplicates/collisions are registered;
9. cross-domain boundary findings are registered;
10. every assertion has evidence provenance;
11. no source artifact was modified by N1;
12. unresolved cases are explicitly enumerated.

## 23. N1 status

```text
PHASE: N1
MODE: Inventory + Classification
SOURCE MODIFICATION: PROHIBITED
N0 FORMAL APPROVAL: PENDING
N1 DISCOVERY: STARTED
N1 CONTROL REGISTER: CREATED
N1 STRUCTURAL INVENTORY SOURCE: VERIFIED
N1 CONTENT-LEVEL INVENTORY: IN PROGRESS
N1 CLASSIFICATION: IN PROGRESS
N1 EXIT: NOT YET REACHED
```

## 24. Next micro-step

The next controlled operation is **N1-M2 — Content-Level Metadata and Relationship Extraction**.

It shall read the actual Markdown content of every in-scope artifact and populate the inventory with observed frontmatter, identity, lifecycle and relationship declarations. It shall not modify the source files.

## 25. Institutional principle

> N1 records what each artifact is before BHG decides what each artifact should become.

> Classification is evidence. Authority is governance. Normalization is remediation. These operations must remain separate.
