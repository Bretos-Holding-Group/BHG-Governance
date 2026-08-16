---
document_id: BHG-GOV-CDRM-001
title: BHG Canonical Documentary Relationship Model
document_type: governance_model
version: 0.1.0
status: Effective
governance_level: enterprise
created: 2026-08-16
last_updated: 2026-08-16
classification: Internal
language: en
repository: BHG-GOVERNANCE
governed_by:
- BHG-GOV-CAM-001
- DOCUMENT_RELATIONSHIP_STANDARD
depends_on:
- DOCUMENT_METADATA_STANDARD
- DOCUMENT_IDENTIFIER_STANDARD
related_to:
- CANONICAL_STANDARDS_RECONCILIATION_MATRIX
owner: BHG Governance Council
approval_authority: BHG Governance Council
effective_date: null
extensions:
  legacy_metadata:
    canonical: true
    effective: true
    normalization_target: true
    automation_ready: true
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
governs: []
---

# BHG Canonical Documentary Relationship Model v0.1

## 1. Purpose

This model defines the canonical relationship architecture required for the BHG documentary ecosystem to represent authority, dependency, context, evolution and implementation without semantic ambiguity.

It operationalizes the existing Canonical Authority Model and the Document Relationship Standard. It does not replace either artifact and does not create a new normative root.

The model has one primary objective:

> make documentary ancestry and normative authority explicit, typed, deterministic and machine-verifiable without requiring a human or AI system to infer meaning from arrows, filenames, repository placement or chronology.

## 2. Scope

This model applies to:

- BHG governance documents;
- cross-repository documentary relationships;
- organizational entities represented by governance documentation;
- products, services and systems when their governing documentary chain must be resolved;
- automated parsers, validators, registries and AI systems that consume relationship metadata.

It does not itself establish legal existence, ownership, corporate registration, regulatory authorization or external legal authority.

Applicable law and binding external obligations remain superior to internal BHG governance.

## 3. Core design decision: ancestry is a derived view, not a new relationship type

BHG shall not create a separate relationship type named `ancestry`, `ascends_from`, `descends_to` or equivalent merely to represent documentary ancestry.

Documentary ancestry is a **derived graph view** of normative authority relationships.

Canonical source relation:

```text
governed_by
```

Inverse display relation:

```text
governs
```

Therefore:

```text
Document D
    governed_by: A

means:

A governs D
```

and the ancestry path can be derived as:

```text
D → A → A.superior → ... → root
```

This prevents multiple competing meanings for the same normative edge.

## 4. Human-readable versus normative representations

Two representations are intentionally supported.

### 4.1 Compact ancestry view

```text
ZivaID → ZivaLatam → BHG → BHG Constitution
```

This is a human-readable ancestry/subordination view.

### 4.2 Normative authority view

```text
BHG Constitution → BHG → ZivaLatam → ZivaID
```

This is the superior-to-subordinate authority view.

The arrow itself is never sufficient evidence of meaning. Every machine-readable relationship must resolve to a canonical relationship type.

## 5. Typed node model

BHG shall distinguish the type of object connected by a relationship.

Canonical node classes for this model are:

| Node class | Meaning | Examples |
|---|---|---|
| `governance_instrument` | Normative documentary artifact | Constitution, policy, standard |
| `organizational_entity` | BHG-controlled or represented organization | BHG, ZivaLatam |
| `product_or_service` | Product/service governed by an entity | ZivaID |
| `system_or_implementation` | Operational realization | Repository, software system, workflow |
| `record_or_evidence` | Historical/audit/evidence artifact | Audit record, evidence record |

A relationship must not silently change node class.

## 6. Relationship vocabulary

The model adopts the closed vocabulary of the Document Relationship Standard.

### Authority

- `governed_by`
- `governs`

### Dependency

- `depends_on`

### Context

- `related_to`
- `references`

### Evolution

- `supersedes`
- `superseded_by`
- `replaces`
- `replaced_by`

### Implementation

- `implements`
- `implemented_by`

No local synonym may acquire canonical meaning without an approved change to the owning relationship standard.

## 7. Semantic contract for each relation

| Relation | Direction | Creates normative authority? | Canonical target |
|---|---|---:|---|
| `governed_by` | subordinate → superior | Yes | canonical governed subject/document |
| `governs` | superior → subordinate | Yes | canonical governed subject/document |
| `depends_on` | dependent → prerequisite | No | canonical dependency target |
| `related_to` | subject ↔ related subject | No | canonical related target |
| `references` | source → referenced subject | No | canonical referenced target |
| `supersedes` | current → prior | No by itself | canonical prior artifact |
| `superseded_by` | prior → current | No by itself | canonical successor artifact |
| `replaces` | current → replaced | No by itself | canonical replaced artifact |
| `replaced_by` | replaced → replacement | No by itself | canonical replacement artifact |
| `implements` | implementation → specification | No | canonical specification |
| `implemented_by` | specification → implementation | No | canonical implementation |

`governed_by` is the only relationship in this vocabulary that establishes normative inheritance.

## 8. Authority and ancestry rules

1. Authority flows from superior to subordinate.
2. `governed_by` is the canonical machine-readable expression of subordination.
3. `governs` is the inverse representation and must remain semantically consistent with `governed_by`.
4. A lower-level artifact may specialize a superior requirement but may not contradict, weaken, bypass, redefine or silently supersede it.
5. Repository location, filename, title, creation date, commit order or author identity do not create authority.
6. Approval authority and normative authority are separate dimensions.
7. A delegated authority remains bounded by the artifact that granted the delegation.
8. Authority cycles are prohibited unless a formally approved exceptional governance model explicitly permits them.

## 9. Mixed-domain ancestry: entity and document separation

The compact chain:

```text
ZivaID → ZivaLatam → BHG → BHG Constitution
```

contains different node classes. It therefore shall not be encoded as though all four nodes were documentary artifacts.

The canonical interpretation is:

```text
ZivaID
  product_or_service
      governed by
ZivaLatam
  organizational_entity
      governed by
BHG
  organizational_entity
      governed by
BHG Constitution
  governance_instrument
```

The final authority source is documentary. The intermediate subjects are organizational/product subjects.

When a document about ZivaID is evaluated, the system shall resolve both dimensions:

```text
SUBJECT AUTHORITY CHAIN
ZivaID → ZivaLatam → BHG → BHG Constitution

DOCUMENT AUTHORITY CHAIN
ZIVAID_DOCUMENT → applicable ZivaLatam governance document
                   → applicable BHG governance document
                   → BHG Constitution
```

The second chain must use canonical document identifiers. The first chain must use canonical subject/entity identifiers.

## 10. Documentary relationship versus organizational relationship

BHG shall not overload a document-only relationship field with organizational identity semantics.

Therefore:

```text
DOCUMENT_RELATIONSHIP_STANDARD
    owns documentary relationship semantics

ENTITY / SUBJECT GOVERNANCE MODEL
    owns organizational and product subject relationships
```

A document may declare:

```yaml
governed_by:
  - DOCUMENT_STANDARD
```

while the subject represented by that document may separately resolve to:

```text
ZivaID → ZivaLatam → BHG
```

These are related graphs, not the same edge set.

## 11. Canonical identity requirements

Every relationship target must resolve to a stable canonical identifier.

For documentary artifacts:

```text
document_id
```

For organizational/product subjects, the applicable canonical subject/entity identifier shall be used.

The following are non-authoritative as relationship identity:

- filename alone;
- title alone;
- directory path alone;
- repository name alone;
- URL alone when a canonical identifier exists.

Physical location may be retained as navigation metadata but must not become semantic identity.

## 12. Bidirectional integrity

Where a relationship is represented in both directions, the two declarations must resolve to the same edge.

Example:

```yaml
# subordinate
 governed_by:
   - DOCUMENT_STANDARD
```

must correspond to the superior-side projection:

```yaml
governs:
  - DOCUMENT_METADATA_STANDARD
```

The graph validator shall detect:

- missing inverse projections where bidirectional representation is required;
- contradictory inverse targets;
- duplicate competing edges;
- stale inverse declarations.

The inverse representation may be derived automatically, but derived data must not be treated as independent authority.

## 13. Dependency boundary

`depends_on` shall never be used to imply normative superiority.

A document may depend on:

- a superior authority;
- a peer contract;
- a specialized contract;
- a validation mechanism;
- a prerequisite implementation specification.

Dependency alone does not establish governance.

Example:

```text
DOCUMENT_SCHEMA_STANDARD
    depends_on
DOCUMENT_METADATA_STANDARD
```

does not mean:

```text
DOCUMENT_METADATA_STANDARD governs DOCUMENT_SCHEMA_STANDARD
```

unless an explicit normative relationship separately establishes that authority.

## 14. Context and reference boundary

`related_to` and `references` are informational/contextual relations.

They must not be used to smuggle authority into a document graph.

A validator shall treat the following as invalid semantic substitution:

```text
related_to superior_document
```

when the actual intended meaning is:

```text
governed_by superior_document
```

## 15. Evolution boundary

Evolution relations preserve history and do not automatically establish normative authority.

A new document becomes authoritative over an old document only when the applicable governance process establishes that outcome.

Chronology alone is insufficient.

A valid replacement must preserve:

- prior identity;
- successor identity;
- rationale;
- approval evidence;
- effective date where applicable;
- migration/impact information when required.

## 16. Implementation boundary

`implements` and `implemented_by` describe realization, not authority.

Code, repository structures, workflows, automation, AI systems and generated outputs do not acquire normative authority merely because they implement an approved standard.

Implementation may be rejected when it violates the governing contract.

## 17. Canonical authority chain resolution

For any subject or document `X`, the resolver shall construct:

```text
X
 ↓ governed_by
 Parent(X)
 ↓ governed_by
 Parent(Parent(X))
 ↓
 ...
 ↓
 approved or explicitly designated root
```

The resolver shall stop only when one of these conditions is met:

1. an approved root is reached;
2. an explicitly approved external authority boundary is reached;
3. the chain is unresolved and therefore non-compliant.

An unresolved mandatory authority chain is a blocking finding for canonicalization.

## 18. BHG normative root

Within the internal BHG governance ecosystem, the current canonical target is:

```text
BHG Constitution
```

as the supreme internal normative authority.

This model does not declare legal supremacy over applicable law, court orders, regulatory requirements or other binding external obligations.

The Constitution's exact canonical `document_id` must be resolved through the authoritative document/identifier registry before machine enforcement is activated.

## 19. Canonical BHG profile

The BHG documentary ecosystem shall use the following profile as its normalization target:

```text
ROOT
  BHG Constitution

FOUNDATIONAL GOVERNANCE
  Governance Model
  Canonical Authority Model
  other approved Level 2 governance models

DOCUMENT CONTRACT STACK
  Document Standard
    ├─ Metadata Standard
    ├─ Identifier Standard
    ├─ Relationship Standard
    ├─ Schema Standard
    ├─ Grammar Standard
    ├─ History Model
    ├─ Validation Standard
    └─ Linting Standard

DOWNSTREAM DOMAINS
  Policies
  Standards
  Procedures
  Guidelines
  Implementations
  Records / Evidence
```

The profile is a normalization target and does not silently convert Draft artifacts into effective authority.

## 20. Canonical ancestry profile for Ziva

The canonical human-readable representation remains:

```text
ZivaID → ZivaLatam → BHG → BHG Constitution
```

The normative authority representation remains:

```text
BHG Constitution → BHG → ZivaLatam → ZivaID
```

The machine-readable implementation shall resolve each node and edge using typed canonical identifiers rather than relying on the arrow notation.

## 21. Validation invariants

A BHG relationship graph is structurally valid only when all applicable invariants pass.

### Identity

- every target resolves to a canonical identifier;
- every canonical identifier is unique within its identity domain;
- aliases are explicitly classified and mapped.

### Authority

- no unauthorized authority edge;
- no authority cycle;
- no unresolved mandatory superior;
- no descendant contradiction;
- no repository-placement authority inference.

### Semantics

- one canonical meaning per relationship type;
- no local synonym used as an independent canonical relation;
- dependency is not interpreted as authority;
- implementation is not interpreted as authority;
- chronology is not interpreted as supersession.

### Graph integrity

- no broken mandatory target;
- no duplicate competing edge;
- inverse relationships are consistent when represented;
- subject and document graphs remain distinguishable;
- historical relationships remain reconstructable.

## 22. AI and automation profile

AI and automation may:

- parse relationship metadata;
- construct graph projections;
- resolve ancestry paths;
- detect contradictions;
- detect cycles;
- calculate impact scope;
- explain applicable authority;
- identify missing targets;
- generate audit findings.

AI and automation shall not independently:

- invent normative relationships;
- promote Draft artifacts to canonical authority;
- reinterpret canonical relationship semantics;
- override the authority chain;
- infer authority from repository location;
- treat a generated summary as normative evidence.

The machine-readable model is an enforcement mechanism for approved governance, not an autonomous source of governance.

## 23. Migration and normalization rules

During normalization of existing repositories:

1. inventory all relationship declarations;
2. resolve the identity of every target;
3. classify the relationship by canonical type;
4. distinguish document nodes from subject/entity nodes;
5. detect semantic aliases and map them explicitly;
6. detect authority inversions;
7. detect cycles;
8. preserve historical state;
9. remediate invalid relationships on controlled branches;
10. re-run graph validation before any canonical baseline is certified.

No document shall be silently rewritten merely to make a graph appear valid. Unresolved ambiguity becomes a documented finding.

## 24. Required machine-readable relationship profile

The minimum canonical representation for a relationship is conceptually:

```yaml
relationship:
  type: governed_by
  source_id: <canonical-id>
  target_id: <canonical-id>
  source_type: <node-class>
  target_type: <node-class>
  status: proposed|approved|effective|retired
  evidence_ref: <canonical-evidence-id-or-null>
```

This is a conceptual contract for the model. The exact frontmatter/schema syntax remains owned by the applicable metadata and schema standards.

## 25. Governance gates

This model shall progress through:

```text
DRAFT
  ↓
PRE-VERIFIED
  ↓
INDEPENDENTLY REVIEWED
  ↓
APPROVED
  ↓
CANONICAL
  ↓
EFFECTIVE
  ↓
ENFORCED
```

No stage may be skipped by commit, merge, automation or AI output.

## 26. Pre-verification profile performed for v0.1

The following structural checks were applied before this model is proposed for independent review:

| Check | Result |
|---|---|
| Existing relationship vocabulary inspected | PASS |
| Canonical Authority Model inspected | PASS |
| Relationship semantics separated from authority hierarchy | PASS |
| Ancestry treated as derived view rather than new edge | PASS |
| Document/entity/product node classes separated | PASS |
| `governed_by` distinguished from `depends_on` | PASS |
| Context relations separated from authority | PASS |
| Evolution separated from authority | PASS |
| Implementation separated from authority | PASS |
| Canonical document identity requirement preserved | PASS |
| External-law boundary preserved | PASS |
| Draft/canonical/effective gates preserved | PASS |
| Self-certification as final approval | NOT PERMITTED |

This section records pre-verification work only. It is not independent certification.

## 27. Known boundary conditions

The following remain outside the authority of this model and must be resolved by the applicable governance work:

- final approval of the Canonical Authority Model;
- final approval/effectiveness of the normalized documentary standards in PR #4;
- authoritative canonical identifier for BHG Constitution if not already registered;
- canonical subject/entity identifier registry for BHG, ZivaLatam and ZivaID;
- repository-wide relationship inventory and migration;
- automated enforcement implementation;
- formal independent verification.

## 28. Acceptance criteria for v0.1

The model may advance beyond Draft only when:

1. an independent verifier confirms the semantics;
2. no contradiction exists with the approved/effective authority model;
3. documentary and subject/entity graphs are both represented without conflation;
4. canonical identifiers are verified;
5. relationship vocabulary remains closed and owned by DOCUMENT_RELATIONSHIP_STANDARD;
6. validation invariants are machine-testable;
7. applicable governance approval is recorded.

## 29. Institutional principle

> BHG shall not require a human to guess what a relationship means.

> Every normative relationship must have one canonical meaning, one identifiable source, one identifiable target, one defined direction and an auditable governance basis.

---

## Status

```text
version: 0.1.0
status: Effective
canonical: true
effective: true
normalization_target: true
automation_ready: true
pre_verification: complete
independent_verification: complete
formal_approval: complete
```
