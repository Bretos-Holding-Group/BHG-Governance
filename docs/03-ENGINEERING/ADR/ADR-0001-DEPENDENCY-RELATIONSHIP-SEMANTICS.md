---
title: Adr 0001 Dependency Relationship Semantics
document_id: BHG-MIG-B1D0077270AD
document_type: Engineering Standard
version: 0.1.0
status: Draft
governance_level: Engineering
owner: BHG Governance Council
approval_authority: BHG Governance Council
created: '2026-08-07'
last_updated: '2026-08-07'
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

ADR-0001 — Dependency Relationship Semantics

«Defines the canonical semantic model for the "depends_on" relationship across the Breto's Holding Group governance ecosystem.»

---

1. Decision Status

Status: Draft

This ADR is submitted for governance review.

It shall not authorize implementation until it reaches the required approval state defined by "ADR_STANDARD.md" and the corresponding Change Management workflow.

---

2. Context

The BHG governance architecture defines "depends_on" as a relationship identifying documents required for the correct interpretation, implementation, validation or operation of another document.

The existing governance standards do not explicitly define whether "depends_on" shall represent:

1. only the immediate dependencies of a document; or
2. the complete transitive dependency chain.

This semantic gap was identified during the Cross-Document Relationship & Dependency Coherence Audit conducted on 2026-08-07.

The audit identified an actual inconsistency within BHG-Ecosystem-Foundation.

The Foundation dependency chain currently contains both behaviors:

FOUNDATION_MANIFESTO
        │
        ▼
FOUNDATION_VISION
        │
        ▼
FOUNDATION_MISSION
        │
        ▼
FOUNDATION_VALUES
        │
        ▼
FOUNDATION_PRINCIPLES
        │
        ▼
FOUNDATION_PHILOSOPHY

"FOUNDATION_VALUES" declares multiple ancestors in "depends_on", while "FOUNDATION_PRINCIPLES" and "FOUNDATION_PHILOSOPHY" declare only their immediate dependencies.

As a result, the same relationship type currently has two different interpretations within the same governance chain.

This prevents deterministic dependency analysis and creates uncertainty for future Genesis automation.

---

3. Problem Statement

Without an explicit dependency semantic model, BHG systems cannot reliably determine:

- the direct dependency of a document;
- the complete dependency ancestry;
- dependency impact;
- change propagation;
- dependency cycles;
- affected documents;
- validation order;
- implementation order.

The ambiguity is particularly important because BHG intends to support automated governance, validation and dependency analysis through Genesis systems.

The dependency declaration itself therefore requires a deterministic semantic definition.

---

4. Considered Models

Model A — Transitive Declaration

Under this model, each document declares both:

- its immediate dependencies; and
- all dependencies inherited through the dependency chain.

Example:

A
│
▼
B
│
▼
C

"C" would declare:

depends_on:
  - B
  - A

Advantages

- Complete ancestry is visible directly in metadata.
- A document can expose its complete dependency context without graph traversal.

Disadvantages

- Creates duplicated relationship data.
- Requires repeated updates when an upstream dependency changes.
- Increases metadata maintenance.
- Creates greater risk of inconsistent declarations.
- Makes it harder to distinguish direct dependency from inherited dependency.
- Can produce unnecessary relationship duplication across large repositories.

---

Model B — Direct Dependency Declaration

Under this model, each document declares only the dependencies immediately required by that document.

Example:

A
│
▼
B
│
▼
C

"C" declares:

depends_on:
  - B

The complete dependency ancestry is calculated by traversing the graph:

C → B → A

Therefore:

Direct dependency:
C → B

Transitive dependency:
C → B → A

---

5. Decision

BHG adopts Model B — Direct Dependency Declaration.

The "depends_on" metadata field shall represent direct dependencies only.

A document shall list a target in "depends_on" only when that target is directly required for the correct interpretation, implementation, validation or operation of the source document.

Transitive dependencies shall not be duplicated in the source document's metadata.

Instead, authorized governance and automation systems shall derive transitive dependencies through graph traversal.

---

6. Canonical Semantic Rule

The canonical interpretation of "depends_on" is:

«"depends_on" identifies the immediate documentary dependencies required by the source document.»

Therefore:

A → B → C

means:

B depends_on A
C depends_on B

It does not require:

C depends_on A

unless C directly requires A independently of B.

---

7. Direct vs. Transitive Dependency

BHG shall distinguish between two analytical concepts.

Direct Dependency

A dependency explicitly declared in:

depends_on:

Example:

depends_on:
  - DOCUMENT_RELATIONSHIP_STANDARD.md

This represents a direct dependency.

---

Transitive Dependency

A dependency discovered by traversing one or more direct dependency relationships.

Example:

DOCUMENT_A
    │
    ▼
DOCUMENT_B
    │
    ▼
DOCUMENT_C

If:

A depends_on B
B depends_on C

then:

A

has:

- direct dependency: "B"
- transitive dependency: "C"

"C" does not need to be repeated in A's "depends_on" metadata unless A independently depends directly on C.

---

8. Dependency Graph Principle

The BHG dependency graph shall be treated as a directed graph.

The relationship:

A depends_on B

shall be represented as:

A → B

Graph traversal may then calculate:

- direct dependencies;
- transitive dependencies;
- dependency depth;
- dependency chains;
- affected documents;
- dependency cycles;
- change propagation.

The metadata declaration and the derived graph shall remain conceptually separate.

---

9. Metadata Integrity

The adoption of direct dependency semantics creates a single source of truth for dependency declarations.

Each direct dependency shall be declared once at the appropriate source document.

Automation shall calculate derived dependency information rather than requiring authors to manually duplicate transitive relationships.

This reduces:

- relationship duplication;
- metadata drift;
- inconsistent ancestry;
- maintenance overhead;
- ambiguity during audits.

---

10. Dependency Resolution

A valid dependency shall:

1. identify an existing governed artifact;
2. resolve to its canonical document identity;
3. be directly required by the source document;
4. comply with the applicable relationship and metadata standards;
5. not create a prohibited circular dependency.

Dependency resolution shall occur before approval where required by the applicable governance standards.

---

11. Circular Dependency Handling

Direct dependency semantics do not permit circular dependencies merely because dependencies are declared locally.

For example:

A → B
B → C
C → A

shall be detected as a circular dependency through graph analysis.

The declaration of only direct dependencies does not weaken BHG's existing prohibition against circular governance dependencies.

---

12. Impact Analysis

Under this decision, change-impact analysis shall distinguish:

Direct Impact

Documents that directly depend on the changed document.

Transitive Impact

Documents that depend on the changed document through one or more intermediate dependencies.

Example:

A → B → C

If C changes:

Direct dependent:
B

Transitive dependent:
A

This distinction shall be preserved by future governance automation.

---

13. Genesis Compatibility

Genesis dependency and validation systems shall interpret:

depends_on:

as the canonical declaration of direct dependencies.

Genesis systems may derive:

- transitive dependency graphs;
- dependency ancestry;
- dependency depth;
- impact propagation;
- affected-document sets;
- dependency cycles.

Genesis systems shall not require authors to manually declare transitive dependencies when those dependencies are already derivable through the direct dependency graph.

---

14. Foundation Application

This decision establishes the semantic rule that shall govern the remediation of AUD-004.

The Foundation documents shall not be manually corrected by assuming a semantic interpretation before this ADR reaches the required approval state.

Once this ADR is approved, the corresponding Governance Change Request shall define the controlled remediation of affected Foundation documents.

The remediation shall evaluate each existing "depends_on" declaration and determine whether the relationship is:

- direct;
- redundant/transitive;
- missing;
- invalid.

No implementation change is authorized by this ADR alone.

---

15. Relationship with "governed_by"

This ADR establishes semantics specifically for:

depends_on:

It does not, by itself, establish the direct-versus-transitive semantic model for:

governed_by:

The authority semantics of "governed_by" and "governs" remain subject to their applicable governance standards and any future ADR or governance decision required to resolve their own semantic ambiguity.

This separation prevents dependency semantics from being incorrectly applied to authority relationships.

---

16. Consequences

Positive Consequences

The decision:

- establishes deterministic dependency declarations;
- eliminates mixed dependency semantics;
- reduces metadata duplication;
- improves maintainability;
- supports automated graph traversal;
- simplifies validation;
- improves change-impact analysis;
- supports scalable governance across multiple repositories;
- creates a clearer contract for human developers and AI systems.

Negative Consequences

The decision requires:

- remediation of existing inconsistent metadata;
- graph traversal for transitive analysis;
- future automation to distinguish direct and transitive dependencies;
- controlled migration of existing Foundation relationships.

These consequences are accepted as part of establishing a deterministic governance model.

---

17. Implementation Boundary

This ADR defines the governance decision.

Implementation shall occur through the official Change Management process.

The implementation sequence shall be:

ADR
 │
 ▼
Governance Review
 │
 ▼
ADR Approval
 │
 ▼
Governance Change Request
 │
 ▼
Implementation
 │
 ▼
Validation
 │
 ▼
Audit
 │
 ▼
Closure

No repository modification is authorized solely by the existence of this ADR.

---

18. Validation Criteria

After implementation, validation shall confirm:

- "depends_on" represents direct dependencies only;
- transitive dependencies are derived through graph traversal;
- affected documents no longer mix direct and transitive declaration models;
- dependency targets resolve correctly;
- prohibited cycles are detected;
- dependency impact can be calculated deterministically;
- metadata remains compliant with the applicable BHG standards.

---

19. Decision Outcome

If approved, this ADR becomes the authoritative architectural decision for the semantics of "depends_on" across the BHG governance ecosystem.

All future governance documents shall follow the direct-dependency model unless a subsequent approved ADR explicitly supersedes this decision.

---

20. Institutional Principle

«Declare dependencies directly. Derive dependency ancestry through the graph.»

This principle establishes a deterministic separation between documentary declaration and automated dependency analysis.
