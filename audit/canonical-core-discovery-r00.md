# BHG Canonical Core Discovery R00

Status: CANDIDATE / READ-ONLY DISCOVERY
Authority effect: NONE
Normative modification: NONE

## 1. Purpose

This report establishes the first structured discovery pass for a BHG Canonical Core. It does not create normative authority, approve documents, alter existing authority relationships, or replace the BHG constitutional framework.

The objective is to identify a bounded foundational core (target range: approximately 40–60 documents) from the complete four-repository corpus, then expand normalization layer by layer until the full documentary corpus is reconciled.

## 2. Corpus principle

The four repositories are treated as the documentary reality set:

1. Bretos-Holding-Group/BHG-Governance
2. Bretos-Holding-Group/BHG-Ecosystem-Foundation
3. Bretos-Holding-Group/bhg-knowledge
4. Bretos-Holding-Group/ZivaLatam

A document being present in a repository establishes existence in the corpus. It does not by itself establish approval, normative authority, canonical status, or precedence.

Status and authority remain separate dimensions.

## 3. Existing evidence used

- BHG-Governance N1 inventory: 207 artifacts in the current audited branch, 206 with frontmatter, 1 without, 0 duplicate document IDs. The status distribution recorded by the inventory is Draft 82, Active 4, Approved 97, Review 21, Effective 2.
- BHG-Governance Authority/Dependency Reconciliation: 203 documents and 797 relationship edges in the current reconciliation scope; 785 resolved relationships, 12 missing-evidence findings, and 8 authority-cycle nodes.
- BHG-Ecosystem-Foundation current tree was inspected and contains foundational, identity, ecosystem, organization, repository, and integration documentation families.
- bhg-knowledge current tree was inspected and contains repository documentation plus placeholder engineering/standards artifacts.
- ZivaLatam current tree was inspected and contains an engineering charter plus architecture/ADR documentation, including engineering, trust, identity/privacy, evidence, API, system blueprint, MVP, repository, security and validation decisions.

The repository trees are evidence of the actual current corpus and are not being silently filtered out because of status.

## 4. Core selection rule

A document is a Core Candidate when it has demonstrated structural or semantic centrality to the ecosystem. Selection is based on evidence, not convenience or filename alone.

Primary signals:

1. Constitutional or foundational scope.
2. Definition of authority or hierarchy.
3. Definition of shared document contracts.
4. Definition of canonical identifiers or identity.
5. Definition of relationship semantics.
6. Definition of lifecycle, validation, schema, metadata, or dependency contracts.
7. Cross-repository governance/interoperability responsibility.
8. High dependency/reference centrality across the corpus.
9. Required bridge between BHG global governance and a domain repository.
10. Ability to constrain or explain a large downstream document population.

Exclusion signals:

- purely historical record;
- isolated implementation detail;
- domain-specific operational artifact with no cross-domain contract;
- duplicate or superseded artifact where canonical ownership is already demonstrated elsewhere.

Exclusion is a discovery classification only; excluded documents remain in the full corpus.

## 5. Initial Core Candidate families

The first discovery pass identifies the following families as mandatory candidates for deeper semantic scoring:

### C0 — Constitutional / institutional foundation

- BHG_CONSTITUTION.md
- BHG_FOUNDATION_BOOK.md
- BHG_GOVERNANCE_ROADMAP.md
- ECOSYSTEM_GOVERNANCE_MODEL.md
- ECOSYSTEM_MODEL.md

### C1 — Authority / hierarchy / governance

- AUTHORITY_MODEL.md
- AUTHORITY_MATRIX.md
- GOVERNANCE_MODEL.md
- LEGAL_HIERARCHY.md
- GOVERNANCE_APPROVAL_MODEL.md
- GOVERNANCE_INTEROPERABILITY_MODEL.md
- ECOSYSTEM_GOVERNANCE_MODEL.md

### C2 — Canonical document system

- DOCUMENT_STANDARD.md
- DOCUMENT_METADATA_STANDARD.md
- DOCUMENT_SCHEMA_STANDARD.md
- DOCUMENT_GRAMMAR_STANDARD.md
- DOCUMENT_RELATIONSHIP_STANDARD.md
- DOCUMENT_VALIDATION_STANDARD.md
- DOCUMENT_LIFECYCLE.md
- DOCUMENT_DEPENDENCY_STANDARD.md

### C3 — Repository / ecosystem architecture

- ARCHITECTURE_MAP.md
- REPOSITORY_STANDARD.md
- REPOSITORY_CLASSIFICATION.md
- REPOSITORY_DEPENDENCY_MODEL.md
- REPOSITORY_LIFECYCLE.md
- REPOSITORY_NAMING_STANDARD.md
- REPOSITORY_REGISTRY.md
- CROSS_REPOSITORY_MODEL.md
- ECOSYSTEM_ARCHITECTURE.md
- ECOSYSTEM_BOUNDARIES.md
- ECOSYSTEM_LAYERS.md

### C4 — Governance controls / change / audit

- F001_CHANGE_GOVERNANCE_VALIDATION.md
- NORMATIVE_CONFLICT_REGISTER.md
- relevant governance change/approval standards identified by the corpus scan
- authoritative audit/validation contracts required by the governance pipeline

### C5 — Cross-domain / Ziva bridge candidates

- ZivaLatam 00_ENGINEERING_CHARTER.md
- Ziva documentation-first / engineering-governance artifacts where present in the corpus
- Ziva ADRs only where they define a cross-domain contract rather than implementation detail
- cross-repository governance bridge artifacts

This list is a candidate family map, not a final canonical list. Duplicate conceptual ownership must be reconciled before any document is promoted to canonical status.

## 6. Critical semantic rule

The Core cannot be created by copying the most authoritative-looking 50 files into a new hierarchy.

Instead:

```text
Complete corpus
    ↓
Evidence extraction
    ↓
Candidate scoring
    ↓
Conflict analysis
    ↓
Authority / ownership mapping
    ↓
Core Candidate Set
    ↓
Human approval of unresolved normative semantics
    ↓
Canonical Core
```

The Canonical Core is therefore a derived architectural layer, not a new source of authority.

## 7. PR #22 integration

The eight BHG-MIG authority-cycle nodes remain unresolved. They must not be corrected by heuristic automation.

They are now treated as inputs to Core Discovery because they may identify documents whose authority/ownership must be settled before the core authority graph can become canonical.

The 12 missing-evidence relationships are handled separately through identifier/registry reconciliation and external/non-documentary classification.

## 8. Required next computation

The next machine-verifiable pass must produce a per-document Core Candidate Score across the four repositories, including:

- document_id;
- repository;
- path;
- status;
- document_type;
- governance_level;
- declared governed_by;
- declared governs;
- depends_on;
- related_to;
- inbound relationship count;
- outbound relationship count;
- cross-repository references;
- conflict-register references;
- authority-cycle participation;
- contract keywords/role indicators;
- candidate layer C0–C5;
- evidence basis;
- confidence;
- exclusion reason when not selected.

No source document should be edited during this scoring pass.

## 9. Expansion model

After Core R00 is validated, normalization proceeds in controlled layers:

```text
Canonical Core R00
      ↓
Core-dependent policies and standards
      ↓
Procedures / operational governance
      ↓
Repository/domain specialization
      ↓
Ziva and other domain layers
      ↓
Records / evidence / historical layer
      ↓
Full canonical corpus
```

Every downstream layer must reference and specialize the contracts owned by the layer above it rather than silently redefining them.

## 10. Acceptance criteria for Core R00

Core R00 is not complete until:

1. all four repositories have been inventoried;
2. no corpus document is silently omitted;
3. every candidate has an evidence basis;
4. authority, approval, dependency, and operational responsibility are separated;
5. duplicate conceptual ownership is explicitly recorded;
6. unresolved normative conflicts are preserved rather than guessed;
7. the candidate set is bounded and explainable;
8. the full corpus remains available for later layer expansion;
9. no source normative document is modified by discovery;
10. subsequent normalization can be performed deterministically from the resulting core contracts.

## 11. Current disposition

DISCOVERY IN PROGRESS.

This branch is intentionally isolated from main and does not certify the Core as canonical. The next step is automated corpus-wide scoring and generation of the detailed candidate register.
