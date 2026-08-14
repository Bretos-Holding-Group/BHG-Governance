---
document_id: BHG-GOV-CAM-001
document_type: governance_model
governance_level: enterprise
version: 0.2.0
status: draft
created: 2026-08-14
last_updated: 2026-08-14
effective_date: null
approval_authority: pending
governed_by:
  - BHG_CONSTITUTION.md
  - GOVERNANCE_MODEL.md
  - AUTHORITY_MODEL.md
depends_on:
  - docs/06-AUDIT/NORMATIVE_CONFLICT_REGISTER.md
  - LEGAL_HIERARCHY.md
  - POLICY_HIERARCHY.md
  - GOVERNANCE_APPROVAL_MODEL.md
  - GOVERNANCE_INTEROPERABILITY_MODEL.md
related_to:
  - AUTHORITY_MATRIX.md
  - DOCUMENT_STANDARD.md
  - DOCUMENT_METADATA_STANDARD.md
  - DOCUMENT_SCHEMA_STANDARD.md
  - DOCUMENT_GRAMMAR_STANDARD.md
  - DOCUMENT_RELATIONSHIP_STANDARD.md
---

# Canonical Authority Model

## 1. Purpose

This document defines the proposed canonical normative-authority model for the BHG documentation ecosystem and its four connected repositories.

It is a **draft normalization artifact**. It does not itself supersede any approved governing artifact. Its purpose is to establish the authority rules that will be used to reconcile the existing manually-created documentation before canonicalization and automated enforcement.

## 2. Foundational rule

The authority of a normative artifact is determined by its approved governance position, scope, and explicit normative relationships—not by filename, directory, repository location, creation order, commit history, or the identity of the person who created it.

For a normative relationship:

```text
A governs B
=> authority(A) > authority(B)
=> B must remain compatible with A
```

A descendant may specialize, operationalize, or add stricter requirements within the superior's permitted scope. It may not contradict, weaken, redefine, bypass, or silently supersede the superior.

## 3. Authority dimensions

The following concepts are independent:

```text
normative authority
approval authority
delegated authority
operational responsibility
ownership
scope
```

Approval of a lower-level artifact does not elevate its normative authority. Delegation grants authority only within the delegated scope and does not authorize contradiction of the rule that created the delegation.

## 4. Canonical normative hierarchy

The normalization target is the following single normative hierarchy:

```text
LEVEL 1 — SUPREME GOVERNANCE
    BHG Constitution

LEVEL 2 — FOUNDATIONAL GOVERNANCE
    Governance Model
    Authority Model
    Foundational governance models

LEVEL 3 — POLICIES
    Enterprise
    Domain
    Company
    Product
    Operational

LEVEL 4 — STANDARDS
    Enterprise
    Domain
    Company
    Product
    Engineering
    AI
    Repository
    Document

LEVEL 5 — PROCEDURES
    Approved procedures implementing policies and standards

LEVEL 6 — GUIDELINES
    Explicitly subordinate guidance; non-binding unless a superior artifact
    explicitly gives it normative force

LEVEL 7 — IMPLEMENTATIONS
    Code, configuration, repository structures, workflows, services, and other
    operational realizations

LEVEL 8 — RECORDS AND EVIDENCE
    Audit records, execution records, evidence, reports, logs, and historical
    artifacts
```

The ordering is:

```text
L1 > L2 > L3 > L4 > L5 > L6 > L7 > L8
```

### 4.1 Resolution of the hierarchy conflict

`LEGAL_HIERARCHY.md` is treated as the detailed hierarchy specification for the same eight-level authority model. Where the Constitution expresses the hierarchy more compactly, the detailed hierarchy is a refinement and must not introduce a competing authority system.

`AUTHORITY_MODEL.md` and other Level 2 models are members of Foundational Governance; they are not independent roots above the Constitution.

This is a **draft reconciliation decision** and requires formal approval before becoming effective.

## 5. Authority versus approval hierarchy

Normative level and approval level are separate dimensions.

```text
NORMATIVE LEVEL
    answers: "How authoritative is this rule?"

APPROVAL LEVEL
    answers: "Who may approve this artifact within its delegated scope?"
```

`GOVERNANCE_APPROVAL_MODEL.md` therefore cannot redefine the normative hierarchy merely by assigning an approval level.

A lower-level artifact may be approved by a delegated authority while remaining normatively subordinate to its governing artifact.

## 6. Core authority graph

The canonical target graph is:

```text
BHG CONSTITUTION (L1)
        |
        v
FOUNDATIONAL GOVERNANCE (L2)
        |
        +-- Governance Model
        +-- Authority Model
        +-- other approved Foundation models
        |
        v
POLICIES (L3)
        |
        v
STANDARDS (L4)
        |
        v
PROCEDURES (L5)
        |
        v
GUIDELINES (L6)
        |
        v
IMPLEMENTATIONS (L7)
        |
        v
RECORDS / EVIDENCE (L8)
```

This graph is normative. A relationship such as `depends_on`, `related_to`, or `references` does not automatically create a position in this hierarchy.

## 7. Cross-repository authority

The following repositories are one normative ecosystem:

```text
BHG-Governance
BHG-Ecosystem-Foundation
bhg-knowledge
ZivaLatam
```

Repository boundaries do not create independent normative sovereignty.

The cross-repository target is:

```text
                    BHG CONSTITUTION
                           |
                           v
                FOUNDATIONAL GOVERNANCE
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
       BHG-Governance  Ecosystem     Shared Contracts
                       Foundation
             |             |             |
             +-------------+-------------+
                           |
                           v
                    Policies / Standards
                           |
              +------------+------------+
              |                         |
              v                         v
        bhg-knowledge               ZivaLatam
        specialization             specialization
              |                         |
              +------------+------------+
                           v
                 Procedures / Implementations
                           |
                           v
                    Records / Evidence
```

A repository-specific normative artifact is valid only if its superior authority, scope, and specialization are explicit.

## 8. Ziva authority bridge

Ziva's engineering governance is treated as a **domain specialization of the BHG hierarchy**, not as an independent constitutional root.

The working chain is:

```text
BHG Constitution
    -> BHG foundational governance
    -> applicable BHG policies / standards
    -> Ziva engineering governance
    -> Ziva implementation rules
```

`00_ENGINEERING_CHARTER`, `DOCUMENTATION_FIRST_POLICY`, and `ZES_ENGINEERING_RULES` may introduce Ziva-specific requirements only inside that delegated/domain scope.

## 9. Foundation authority bridge

Foundation artifacts are treated as Level 2 Foundational Governance unless their approved content is explicitly classified at another level.

`FOUNDATION_MANIFESTO`, identity/ecosystem models, and related Foundation artifacts therefore do not acquire authority above the BHG Constitution merely because they are stored in the Foundation repository.

Where a Foundation artifact defines an enterprise-wide principle, its relationship to the Constitution and Governance Model must be explicit rather than inferred from repository placement.

## 10. Canonical semantic ownership

Every shared normative concept must have exactly one canonical semantic owner.

Initial ownership targets for normalization are:

| Concept | Canonical owner target | Downstream rule |
|---|---|---|
| Constitutional authority | BHG Constitution | No descendant may contradict it |
| Governance structure | Governance Model | Domain governance specializes it |
| Authority semantics | Authority Model | Matrices operationalize it |
| Approval mechanics | Governance Approval Model | Approval does not elevate normative authority |
| Policy hierarchy | Policy Hierarchy | Lower policies cannot contradict higher policies |
| Document identity | Document Identifier Standard | Domain IDs must remain distinct |
| Document metadata | Document Metadata Standard | Schema/Grammar must conform |
| Document structure | Document Schema Standard | Grammar maps to the canonical schema |
| Document grammar | Document Grammar Standard | Must not redefine metadata semantics |
| Document relationships | Document Relationship Standard | Local vocabularies map to canonical relations |
| Document lifecycle | Document Lifecycle model | Metadata represents lifecycle state; model owns semantics |
| Repository semantics | Repository standards after ownership reconciliation | Local rules reference canonical repository contracts |
| Engineering specialization | Domain engineering governance | Must remain under BHG authority |

These are **normalization targets**, not yet approved canonical ownership assignments.

## 11. Document-system authority model

The document standards are organized as a contract stack rather than competing authorities:

```text
DOCUMENT STANDARD
    |
    +-- METADATA CONTRACT
    |      -> DOCUMENT_METADATA_STANDARD
    |
    +-- IDENTITY CONTRACT
    |      -> DOCUMENT_IDENTIFIER_STANDARD
    |
    +-- STRUCTURE CONTRACT
    |      -> DOCUMENT_SCHEMA_STANDARD
    |
    +-- GRAMMAR CONTRACT
    |      -> DOCUMENT_GRAMMAR_STANDARD
    |
    +-- RELATIONSHIP CONTRACT
    |      -> DOCUMENT_RELATIONSHIP_STANDARD
    |
    +-- LIFECYCLE CONTRACT
    |      -> DOCUMENT_LIFECYCLE
    |
    +-- VALIDATION CONTRACT
           -> DOCUMENT_VALIDATION_STANDARD
```

The contracts are complementary. They must not independently redefine the same semantic field, relation, lifecycle state, or identity rule.

## 12. Metadata normalization rule

`DOCUMENT_METADATA_STANDARD` is the target owner of shared document metadata semantics.

The normalization target is one canonical vocabulary, with `snake_case` field names unless a future approved standard explicitly establishes another convention.

Equivalent aliases such as:

```text
document-type

document_type
```

must not coexist as independent canonical meanings.

Schema, Grammar, templates, validators, and domain documents must reference the canonical metadata contract.

## 13. Relationship normalization rule

`DOCUMENT_RELATIONSHIP_STANDARD` is the target owner of shared relationship semantics.

The normalization target is the canonical vocabulary declared there, including:

```text
governed_by
governs
depends_on
related_to
supersedes
superseded_by
references
implements
implemented_by
replaces
replaced_by
```

Terms such as `dependencies`, `successors`, `predecessors`, and `related-documents` must either be retired or explicitly mapped as non-canonical aliases during normalization.

## 14. Relationship semantics

These relations are not interchangeable:

```text
governed_by  = normative subordination
governs       = inverse normative relation
depends_on    = dependency without inherent authority
related_to    = association without authority
implements    = realization of another rule
supersedes    = approved replacement
```

A dependency must never be interpreted as governance merely because one artifact depends on another.

## 15. Downward consistency rule

For every normative document `D`, every applicable normative ancestor `A` must remain compatible with `D`:

```text
for every D:
    for every normative ancestor A:
        compatible(D, A) = true
```

A contradiction includes:

- redefining a superior term;
- changing the meaning of a canonical field;
- replacing a canonical relation with an incompatible relation;
- lowering a mandatory requirement without authorization;
- creating an incompatible hierarchy;
- claiming independent authority where only delegation exists;
- bypassing mandatory governance or approval controls;
- silently superseding a superior or peer rule.

## 16. Specialization rule

A descendant may add specificity without changing the superior semantic contract.

Valid:

```text
Global: every controlled document has permanent document_id.
Domain: every audit document also has audit_record_id.
```

Invalid:

```text
Global: document_id is permanent.
Domain: document_id changes on every version.
```

The second rule changes the superior meaning and is therefore a contradiction.

## 17. Conflict-resolution precedence

When two normative artifacts appear to conflict:

1. higher normative authority prevails;
2. explicit `governed_by` prevails over folder location;
3. valid narrower scope may specialize broader scope;
4. explicit approved `supersedes` prevails over chronology;
5. approval authority is considered only within delegated scope;
6. unresolved authority is BLOCKING and must not be resolved by implementation convention.

## 18. Repository placement is not authority

Directory, filename, repository, creation order, and historical manual placement are evidence, not authority.

This rule is mandatory for the current normalization phase because the four repositories were populated manually and were not created through an automated canonical-document pipeline.

## 19. Normalization sequence

The approved target sequence is:

```text
1. Canonical Authority Model
2. Canonical semantic ownership
3. Canonical metadata contract
4. Canonical vocabulary
5. Canonical relationship semantics
6. Canonical document structure
7. Normalize existing normative documents
8. Normalize downstream documents
9. Establish four-repository canonical baselines
10. Implement automated validation and enforcement
```

Automation must enforce an approved semantic model; it must not invent or decide normative authority.

## 20. Conflict disposition matrix

The current draft resolves the authority question as follows:

| Conflict | Draft disposition |
|---|---|
| NORM-001 | Resolve as one 8-level normative hierarchy; Legal Hierarchy is a refinement |
| NORM-002 | Governance Model and Authority Model are distinct Level 2 artifacts with explicit model relationships |
| NORM-003 | Foundation is subordinate to the Constitution; repository location does not create sovereignty |
| NORM-004 | Repository Naming Standard must surrender unrelated semantic ownership to canonical repository contracts |
| NORM-005 | Ziva engineering governance is domain specialization under BHG authority |
| NORM-006 | Empty engineering standard cannot act as authority until classified or completed |
| NORM-007 | Guidelines and Records/Evidence are valid lower levels, not competing hierarchy roots |
| NORM-008 | Authority Model defines semantics; Authority Matrix operationalizes authority assignments |
| NORM-009 | Metadata Standard owns metadata semantics; Schema consumes them |
| NORM-010 | Metadata Standard owns field semantics; Grammar consumes them |
| NORM-011 | Schema owns structural object model; Grammar must map to it explicitly |
| NORM-012 | Relationship Standard owns relationship semantics |
| NORM-013 | Document Standard owns overall document contract; Metadata Standard owns metadata contract |
| NORM-014 | Duplicate internal normative sections must be consolidated during document normalization |
| NORM-015 | Schema must conform to the canonical metadata contract |
| NORM-016 | Lifecycle model owns lifecycle semantics; metadata carries state representation |
| NORM-017 | Domain relationship rules must reference canonical relationship semantics |
| NORM-018 | ZES chain is valid only as Ziva specialization under BHG authority |
| NORM-019 | Repository identity/classification/lifecycle/registry require one canonical ownership map |
| NORM-020 | Manual historical state is baseline evidence, not a normative exception |
| NORM-021 | Approval levels are separate from normative levels |
| NORM-022 | Delegated approval cannot elevate normative authority |
| NORM-023 | Interoperability defines cross-domain requirements; concrete contracts retain single semantic owners |
| NORM-024 | Interoperability principles must not duplicate concrete dependency/schema/repository ownership |

## 21. Acceptance criteria for canonical status

This model may become `approved`, `canonical: true`, and `effective: true` only when:

- the authority hierarchy has been formally approved;
- all Level 1-8 semantics are defined;
- every normative document has a superior or an explicitly approved root status;
- all four-repository bridges are documented;
- shared contracts have one semantic owner;
- no approved descendant contradicts an approved ancestor;
- approval and normative authority are explicitly separated;
- no unresolved BLOCKER remains in the authority model;
- the applicable governance approval process has been completed.

## 22. Current status

```text
status: DRAFT
canonical: false
effective: false
automation_ready: false
normalization_target: true
```

This version is a reconciliation draft produced from the current Conflict Register. It is intended to govern the next normalization analysis; it is not yet an effective governing instrument.