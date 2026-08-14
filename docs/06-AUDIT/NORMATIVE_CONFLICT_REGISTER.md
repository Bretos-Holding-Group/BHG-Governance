---
document_id: BHG-AUD-NORM-001
document_type: audit
governance_level: enterprise
version: 0.1.0
status: draft
created: 2026-08-14
last_updated: 2026-08-14
effective_date: null
approval_authority: pending
governed_by:
  - BHG_CONSTITUTION.md
  - AUTHORITY_MODEL.md
  - AUTHORITY_MATRIX.md
depends_on:
  - LEGAL_HIERARCHY.md
  - POLICY_HIERARCHY.md
  - DOCUMENT_STANDARD.md
  - DOCUMENT_METADATA_STANDARD.md
  - DOCUMENT_SCHEMA_STANDARD.md
  - DOCUMENT_GRAMMAR_STANDARD.md
  - DOCUMENT_RELATIONSHIP_STANDARD.md
  - DOCUMENT_VALIDATION_STANDARD.md
related_to:
  - F001_CHANGE_GOVERNANCE_VALIDATION.md
  - RAI-001_REPOSITORY_INTEGRITY.md
  - RAI-002_DOCUMENTATION_INTEGRITY.md
  - RAI-003_ARCHITECTURE_ALIGNMENT.md
---

# Normative Conflict Register

## 1. Purpose

This is a working audit register for the normalization phase of the BHG documentation system. It records detected or suspected conflicts, overlaps, authority ambiguities, and hierarchy discrepancies across the four repositories currently under normalization.

This register does **not** itself establish canonical authority. It records evidence that must be resolved before canonicalization.

## 2. Governing principle

A descendant normative document may specialize, operationalize, or constrain a superior rule within the superior's declared scope, but it must not contradict, weaken, redefine, supersede, or bypass the superior authority unless the governing hierarchy explicitly authorizes that relationship.

For a normative relation `A governs B`:

`authority(A) > authority(B)`

and every rule introduced by `B` must be compatible with the applicable rules of `A`.

## 3. Scope

Repositories in scope:

1. `Bretos-Holding-Group/BHG-Governance`
2. `Bretos-Holding-Group/BHG-Ecosystem-Foundation`
3. `Bretos-Holding-Group/bhg-knowledge`
4. `Bretos-Holding-Group/ZivaLatam`

The register covers explicit standards and normative-adjacent artifacts including governance models, constitutions, authority models, policies, hierarchies, schemas, templates, registries, ADRs with normative force, and engineering rules.

## 4. Status model

- `CONFIRMED`: conflict is demonstrated directly by source documents.
- `SUSPECTED`: evidence indicates a likely conflict, but semantic reconciliation is still required.
- `OVERLAP`: responsibilities appear duplicated or broader than the artifact's stated scope.
- `GAP`: required authority or relationship is not explicitly defined.
- `RESOLVED`: formally reconciled and approved; not used during this initial pass.

## 5. Initial conflict register

| ID | Source | Target / comparator | Type | Severity | Finding | Required resolution |
|---|---|---|---|---|---|---|
| NORM-001 | `BHG_CONSTITUTION.md` | `LEGAL_HIERARCHY.md` | hierarchy divergence | BLOCKER | The Constitution presents one normative level sequence while Legal Hierarchy introduces a different sequence, including explicit Guidelines and Records/Evidence levels and a different treatment of Authority Models. | Establish one canonical hierarchy and define whether Legal Hierarchy is a refinement or conflicting authority. |
| NORM-002 | `GOVERNANCE_MODEL.md` | `AUTHORITY_MODEL.md` | authority relationship ambiguity | HIGH | Governance Model operationalizes constitutional governance while Authority Model defines authority structure, but their exact parent/child relationship is not represented consistently as one canonical chain. | Define the authority relationship and precedence explicitly. |
| NORM-003 | `BHG_CONSTITUTION.md` | Foundation artifacts | cross-repository authority gap | BLOCKER | Foundation artifacts declare their own superior foundational documents, but their exact placement beneath the BHG constitutional hierarchy is not uniformly demonstrated. | Establish the cross-repository authority bridge. |
| NORM-004 | `REPOSITORY_NAMING_STANDARD.md` | repository classification/lifecycle/registry artifacts | scope overlap | HIGH | Repository Naming Standard contains naming plus identity, classification, registry, lifecycle, validation, automation and security responsibilities. | Separate owned rules from delegated/reference rules and define governing standards. |
| NORM-005 | Ziva `00_ENGINEERING_CHARTER` / `DOCUMENTATION_FIRST_POLICY.md` | BHG global hierarchy | cross-repository authority gap | BLOCKER | Ziva's engineering chain is explicit internally but its normative position relative to the BHG global hierarchy is not yet formally reconciled. | Define whether Ziva rules are specialization of BHG rules and identify the governing superior documents. |
| NORM-006 | `bhg-knowledge/.github/standards/DOCUMENT_ENGINEERING_STANDARD.md` | BHG document standards | normative artifact gap | HIGH | The artifact exists but currently contains no substantive specification, so it cannot safely act as a governing standard. | Classify as placeholder, deprecated artifact, or complete it only after canonical authority is established. |
| NORM-007 | `LEGAL_HIERARCHY.md` | `BHG_CONSTITUTION.md` | hierarchy extension | HIGH | Legal Hierarchy introduces Guidelines and Records/Evidence as explicit lower levels not represented identically in the Constitution's hierarchy. | Determine whether these are legitimate descendants or an independent classification dimension. |
| NORM-008 | `AUTHORITY_MATRIX.md` | `AUTHORITY_MODEL.md` | model vs operational matrix | MEDIUM | The two artifacts cover related authority concerns but their normative boundary is not yet formally expressed. | Define Authority Model as model and Authority Matrix as operational realization, or otherwise reconcile. |
| NORM-009 | `DOCUMENT_METADATA_STANDARD.md` | `DOCUMENT_SCHEMA_STANDARD.md` | schema/metadata mismatch | BLOCKER | The metadata standard and schema standard use different field naming conventions for equivalent concepts (`document_id` vs `document-type` patterns, etc.). | Establish one canonical metadata contract before automated validation. |
| NORM-010 | `DOCUMENT_METADATA_STANDARD.md` | `DOCUMENT_GRAMMAR_STANDARD.md` | schema/grammar mismatch | BLOCKER | Equivalent metadata concepts are represented with different naming conventions and structures. | Canonicalize field names and semantic definitions. |
| NORM-011 | `DOCUMENT_SCHEMA_STANDARD.md` | `DOCUMENT_GRAMMAR_STANDARD.md` | structural model divergence | BLOCKER | Schema defines six structural objects while Grammar defines five layers with different conceptual names. | Define a canonical structural model and explicit mapping if the concepts are equivalent. |
| NORM-012 | `DOCUMENT_RELATIONSHIP_STANDARD.md` | `DOCUMENT_GRAMMAR_STANDARD.md` | relationship vocabulary divergence | BLOCKER | Relationship Standard defines canonical snake_case relationships while Grammar uses alternate names such as `dependencies`, `successors`, `predecessors`, and `related-documents`. | Establish canonical relationship vocabulary and semantic equivalence rules. |
| NORM-013 | `DOCUMENT_STANDARD.md` | `DOCUMENT_METADATA_STANDARD.md` | contract dependency ambiguity | HIGH | The general Document Standard and Metadata Standard overlap in defining document structure and metadata requirements. | Assign responsibility: document lifecycle/structure vs metadata contract. |
| NORM-014 | `DOCUMENT_STANDARD.md` | itself | internal duplication/version ambiguity | BLOCKER | The current document contains multiple normative sections/version indicators, creating more than one apparent specification inside the same standard. | Consolidate into one authoritative specification before declaring canonical. |
| NORM-015 | `DOCUMENT_SCHEMA_STANDARD.md` | `DOCUMENT_METADATA_STANDARD.md` | self-compliance inconsistency | BLOCKER | The schema artifact does not consistently express its own metadata using the metadata vocabulary declared as standard. | Normalize the schema document to the eventual canonical metadata contract. |
| NORM-016 | `DOCUMENT_SCHEMA_STANDARD.md` | `DOCUMENT_LIFECYCLE.md` / `DOCUMENT_METADATA_STANDARD.md` | lifecycle overlap | HIGH | Lifecycle concepts appear both as metadata fields and as a structural/lifecycle object. | Define metadata representation versus lifecycle model semantics. |
| NORM-017 | `DOCUMENT_RELATIONSHIP_STANDARD.md` | repository/domain-specific standards | relationship authority ambiguity | HIGH | Multiple domains may define relationships locally while a global relationship standard exists. | Require local relationship rules to reference and specialize the canonical global vocabulary. |
| NORM-018 | Ziva `ZES_ENGINEERING_RULES_v1.0.md` | Ziva `DOCUMENTATION_FIRST_POLICY.md` | specialization chain | SUSPECTED | ZES explicitly positions Documentation First Policy upstream of engineering rules; the chain appears coherent but must be reconciled with global BHG authority. | Validate the chain and register its BHG superior. |
| NORM-019 | `BHG-Ecosystem-Foundation` repository standards | BHG-Governance repository/document standards | cross-repository duplication | SUSPECTED | Repository naming, identity, registry and lifecycle concepts are distributed across repositories. | Build one canonical ownership map for repository-related concepts. |
| NORM-020 | All four repositories | global metadata/document contract | normalization gap | GAP | Documents were created manually and no automated canonical contract has yet enforced uniform metadata, content structure, or authority relationships. | Establish canonical document contract first; automation follows only after normalization. |

## 6. Preliminary authority hypotheses

These are hypotheses only and must not be treated as approved authority:

```text
BHG Constitution
  -> Governance Model / Foundational Governance
  -> Authority Model
  -> Policies
  -> Standards
  -> Procedures / Guidelines
  -> Implementations
  -> Records / Evidence
```

The following cross-repository relationships require explicit reconciliation before they can enter the canonical graph:

- BHG-Governance ↔ BHG-Ecosystem-Foundation
- BHG-Governance ↔ bhg-knowledge
- BHG-Governance ↔ ZivaLatam
- Foundation identity/repository authority ↔ global governance authority
- Ziva engineering authority ↔ global governance authority

## 7. Resolution rules for subsequent normalization

1. A lower-level document cannot override a higher-level rule merely by declaring a different value.
2. A domain-specific standard may specialize a global standard only within its declared scope.
3. A policy cannot redefine the authority of the governance model that governs it.
4. A standard cannot silently redefine metadata, identifiers, relationships, lifecycle, or validation semantics owned by a superior standard.
5. A local vocabulary must either use the canonical vocabulary or explicitly declare a valid mapping.
6. A document may depend on another document without being normatively subordinate to it; `depends_on` and `governed_by` are distinct relations.
7. No automation should be implemented against unresolved normative semantics.

## 8. Next required analysis

Before any normative document is edited, the following must be completed:

1. Resolve the global hierarchy conflict (`NORM-001`).
2. Resolve cross-repository authority (`NORM-003`, `NORM-005`).
3. Reconcile the canonical metadata contract (`NORM-009`, `NORM-010`, `NORM-015`).
4. Reconcile structural grammar/schema (`NORM-011`).
5. Reconcile relationship vocabulary (`NORM-012`).
6. Define ownership boundaries for repository and lifecycle concepts (`NORM-004`, `NORM-016`, `NORM-019`).
7. Produce the Canonical Authority Model.
8. Only then begin document-by-document normalization.

## 9. Important limitation

This is the **initial conflict register**, not a claim that every normative conflict in the four repositories has been exhaustively discovered. It records the conflicts and gaps demonstrated during the current authority-mapping pass. Exhaustive closure requires completing the semantic comparison of all identified standards and normative-adjacent artifacts against the canonical authority model once that model is approved.
