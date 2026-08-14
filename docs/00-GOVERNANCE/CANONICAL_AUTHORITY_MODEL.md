---
document_id: BHG-GOV-CAM-001
document_type: governance_model
governance_level: enterprise
version: 0.1.0
status: draft
created: 2026-08-14
last_updated: 2026-08-14
effective_date: null
approval_authority: pending
governed_by:
  - BHG_CONSTITUTION.md
  - GOVERNANCE_MODEL.md
  - AUTHORITY_MODEL.md
  - AUTHORITY_MATRIX.md
depends_on:
  - docs/06-AUDIT/NORMATIVE_CONFLICT_REGISTER.md
  - LEGAL_HIERARCHY.md
  - POLICY_HIERARCHY.md
  - GOVERNANCE_APPROVAL_MODEL.md
related_to:
  - GOVERNANCE_INTEROPERABILITY_MODEL.md
  - DOCUMENT_STANDARD.md
  - DOCUMENT_METADATA_STANDARD.md
  - DOCUMENT_SCHEMA_STANDARD.md
  - DOCUMENT_GRAMMAR_STANDARD.md
  - DOCUMENT_RELATIONSHIP_STANDARD.md
---

# Canonical Authority Model

## 1. Purpose

This document defines the proposed canonical model for normative authority across the BHG documentation ecosystem and its connected repositories.

It is a **draft normalization artifact**. It does not supersede the BHG Constitution, Governance Model, Authority Model, Authority Matrix, Legal Hierarchy, Policy Hierarchy, or any approved standard until formally reviewed and approved under the applicable governance process.

Its purpose is to establish one explicit authority model that can later be used to reconcile existing documents, prevent downward contradiction, and serve as the normative foundation for automated validation.

## 2. Governing principle

A normative document at a lower authority level may specialize, operationalize, or constrain a superior rule within the superior rule's declared scope. It must not contradict, weaken, redefine, bypass, or silently supersede the superior authority.

For a normative relationship `A governs B`:

```text
authority(A) > authority(B)
```

and:

```text
rules(B) must be compatible with applicable rules(A)
```

A downstream document may be more specific without becoming more authoritative.

## 3. Core distinction

The following concepts are independent and must not be conflated:

```text
normative authority
approval authority
delegated authority
operational responsibility
ownership
```

Approval of a lower-level artifact does not elevate that artifact above its governing authority.

Delegation grants authority within a defined scope and does not permit contradiction of the superior rule that created the delegation.

## 4. Proposed canonical hierarchy

The following hierarchy is the canonicalization target proposed by this draft:

```text
LEVEL 1 — SUPREME GOVERNANCE
    BHG Constitution

LEVEL 2 — FOUNDATIONAL GOVERNANCE
    Governance Model
    Authority Model
    Foundational governance models

LEVEL 3 — GOVERNANCE POLICIES
    Enterprise policies
    Domain policies
    Company policies
    Product policies
    Operational policies

LEVEL 4 — STANDARDS
    Enterprise standards
    Domain standards
    Company standards
    Product standards
    Engineering standards
    AI standards
    Repository standards
    Document standards

LEVEL 5 — PROCEDURES
    Approved procedures implementing policies and standards

LEVEL 6 — GUIDELINES
    Non-binding or advisory guidance explicitly subordinate to applicable policies,
    standards, and procedures

LEVEL 7 — IMPLEMENTATIONS
    Code, configurations, repository structures, workflows, services, and other
    operational implementations

LEVEL 8 — RECORDS AND EVIDENCE
    Audit records, execution records, evidence, reports, logs, and other historical
    or evidentiary artifacts
```

This hierarchy reconciles the need for a single normative ordering with the more detailed levels identified in `LEGAL_HIERARCHY.md`. It remains subject to formal approval because existing governing artifacts currently express the hierarchy differently.

## 5. Authority ordering

For normative documents:

```text
Level 1 > Level 2 > Level 3 > Level 4 > Level 5 > Level 6 > Level 7 > Level 8
```

Within a level, authority is determined by declared scope and specificity, subject to the applicable governance and approval rules.

A more specific document at the same level may constrain a broader document only when the broader document permits specialization and the scopes do not conflict.

A later version does not automatically acquire authority over a different document merely because it is newer. Supersession must be explicit and governed.

## 6. Relationship semantics

The following relations must remain distinct:

### 6.1 `governed_by`

Normative subordination.

```text
A governed_by B
=> B has normative authority over A
```

### 6.2 `governs`

Inverse of `governed_by`.

```text
B governs A
=> authority(B) > authority(A)
```

### 6.3 `depends_on`

Technical, semantic, procedural, or informational dependency. It does **not** by itself establish normative authority.

### 6.4 `related_to`

Association without authority implication.

### 6.5 `implements`

A lower-level artifact realizes a rule or requirement established elsewhere. Implementation does not acquire the authority of the artifact it implements.

### 6.6 `supersedes`

Explicit replacement of an earlier artifact under approved change governance. It must never be inferred solely from version or date.

## 7. Cross-repository authority

The four repositories are treated as one connected normative ecosystem for purposes of authority consistency:

```text
BHG-Governance
BHG-Ecosystem-Foundation
bhg-knowledge
ZivaLatam
```

A repository boundary does not create independent normative sovereignty.

A repository-specific policy or standard may specialize a global BHG rule only when:

1. its scope is explicitly declared;
2. its superior authority is identified;
3. it does not contradict the superior rule;
4. any specialization is within the superior rule's permitted scope; and
5. its approval authority is valid for that scope.

## 8. Cross-repository bridge model

The target model is:

```text
                         BHG CONSTITUTION
                                |
                                v
                     FOUNDATIONAL GOVERNANCE
                                |
              +-----------------+-----------------+
              |                 |                 |
              v                 v                 v
       BHG-Governance   Ecosystem Foundation   Shared Contracts
              |                 |                 |
              +-----------------+-----------------+
                                |
                                v
                         Policies / Standards
                                |
                +---------------+---------------+
                |                               |
                v                               v
          bhg-knowledge                       ZivaLatam
          specialization                     specialization
                |                               |
                +---------------+---------------+
                                v
                    Procedures / Implementations
                                |
                                v
                       Records / Evidence
```

This diagram represents the intended authority relationship, not an assertion that every current repository document already complies with it.

## 9. Shared canonical contracts

The following concepts require one canonical semantic owner before automated validation is implemented:

- document identity;
- document metadata;
- document schema;
- document grammar;
- document relationships;
- document lifecycle;
- repository identity;
- repository classification;
- repository lifecycle;
- governance authority;
- approval authority;
- dependency semantics.

Domain repositories may reference and specialize these contracts, but must not silently fork their meaning.

## 10. Document authority model

The canonical document-system target is:

```text
DOCUMENT STANDARD
        |
        +--> METADATA STANDARD
        |
        +--> IDENTIFIER STANDARD
        |
        +--> SCHEMA STANDARD
        |
        +--> GRAMMAR STANDARD
        |
        +--> RELATIONSHIP STANDARD
        |
        +--> LIFECYCLE MODEL
        |
        +--> VALIDATION STANDARD
        |
        +--> LINTING / AUTOMATION / COMPILER
```

The exact parent-child relationships among these artifacts remain subject to the conflict register. This model establishes that specialized document standards cannot independently redefine shared semantics owned by the canonical document system.

## 11. Downward consistency rule

Every normative descendant must satisfy all applicable superior rules.

The minimum validation condition is:

```text
For every document D:

  for every normative ancestor A of D:
      D must be compatible with A
```

A contradiction includes, at minimum:

- assigning a different meaning to a superior-defined term;
- redefining a canonical field;
- replacing a canonical relationship with an incompatible one;
- lowering a mandatory requirement without authorization;
- creating an incompatible hierarchy;
- declaring independent authority where only delegated authority exists;
- bypassing a mandatory approval or governance control;
- silently superseding an existing rule.

## 12. Specialization rule

A descendant may add specificity.

Example:

```text
Global standard:
    Every controlled document has a permanent document_id.

Domain standard:
    Every audit document has a permanent document_id and an audit_record_id.
```

This is compatible if `audit_record_id` is a distinct domain identifier and does not redefine `document_id`.

The following would be incompatible:

```text
Global standard:
    document_id is permanent.

Domain standard:
    document_id changes with every version.
```

## 13. Approval and delegation

Approval authority is a governance mechanism, not an independent normative hierarchy.

Therefore:

```text
approval authority != normative authority
```

A delegated organization, company, product team, or domain may approve an artifact within its delegated scope while remaining subordinate to the rules that define that scope.

No approval record may be interpreted as authority to contradict a superior rule unless the superior governance mechanism explicitly grants such authority.

## 14. Canonical ownership rule

Every shared normative concept must have exactly one canonical semantic owner.

Other documents must either:

1. reference the owner;
2. specialize the owner's rule within scope; or
3. operationalize the owner's rule.

They must not create an independent competing definition without an explicit approved supersession or delegation relationship.

## 15. Conflict-resolution precedence

When two normative artifacts appear to conflict, resolution must proceed in this order:

1. higher authority level prevails;
2. explicit `governed_by` relationship prevails over inferred folder location;
3. narrower valid scope may specialize a broader scope without contradicting it;
4. explicit approved supersession prevails over simple chronology;
5. approval authority is considered only within its delegated scope;
6. if authority remains ambiguous, the conflict is BLOCKING and must not be resolved by implementation convention.

## 16. Repository placement is not authority

A document's directory, filename, repository, commit history, or creation order does not independently establish normative authority.

Those attributes may provide evidence, but authority must be derived from the declared and approved governance model.

This is particularly important during the current normalization phase because the existing repositories were populated manually and contain historical placement decisions that may not represent the final canonical structure.

## 17. Normalization consequences

Once this model is approved, normalization shall proceed in this order:

```text
1. establish canonical authority
2. establish canonical metadata
3. establish canonical vocabulary
4. establish canonical relationships
5. establish canonical document structure
6. normalize existing normative documents
7. normalize downstream documents
8. validate the four repository baselines
9. implement automated enforcement
```

No automated validator should be treated as authoritative until the underlying normative semantics are approved.

## 18. Required canonicalization decisions

The following decisions remain open and must be resolved before this model can become effective:

- final relationship between Constitution and Foundation Manifesto;
- exact placement of Foundation models within Level 2;
- final hierarchy representation used by `LEGAL_HIERARCHY.md`;
- relationship between normative levels and approval levels;
- canonical owner of repository identity, classification, lifecycle, and registry semantics;
- canonical owner of document metadata;
- canonical mapping between Schema and Grammar;
- canonical relationship vocabulary;
- canonical lifecycle model;
- exact normative position of Ziva engineering governance;
- status and treatment of empty or placeholder normative artifacts in `bhg-knowledge`.

These decisions correspond to unresolved findings in `NORMATIVE_CONFLICT_REGISTER.md` and must not be silently assumed to be resolved by this draft.

## 19. Canonicalization acceptance criteria

This model may become `approved` only when:

- every Level 1-8 authority is assigned a single semantic definition;
- every normative document has a declared superior or is explicitly designated as a root;
- all cross-repository normative bridges are documented;
- no approved descendant contradicts an approved ancestor;
- shared contracts have one canonical owner;
- approval authority and normative authority are explicitly separated;
- the conflict register contains no unresolved BLOCKER affecting the authority model;
- the model has passed the applicable governance approval process.

## 20. Current status

```text
status: DRAFT
canonical: false
effective: false
automation_ready: false
```

This document is the proposed authority target for the normalization phase. It must be reviewed against the complete conflict register before any existing standard is declared canonical.
