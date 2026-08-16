# BHG Canonical Core Candidate Register R00

Status: CANDIDATE / NOT CANONICAL

This register records the first bounded candidate set. It does not establish authority. Scores are provisional until the corpus-wide machine pass computes relationship centrality and cross-repository evidence.

| Candidate | Repository | Layer | Core role | Initial basis | Authority status |
|---|---|---:|---|---|---|
| BHG_CONSTITUTION.md | BHG-Governance | C0 | constitutional authority | identified as governing constitutional framework | verify from source |
| BHG_FOUNDATION_BOOK.md | BHG-Governance | C0 | institutional doctrine | foundational scope across ecosystem | subordinate to Constitution |
| BHG_GOVERNANCE_ROADMAP.md | BHG-Governance | C0 | governance evolution | governance roadmap and lifecycle context | verify |
| AUTHORITY_MODEL.md | BHG-Governance | C1 | authority semantics | defines authority structure | unresolved against hierarchy artifacts |
| AUTHORITY_MATRIX.md | BHG-Governance | C1 | authority realization | operational authority mapping | distinguish from Authority Model |
| GOVERNANCE_MODEL.md | BHG-Governance | C1 | governance model | operationalizes constitutional governance | relationship requires reconciliation |
| LEGAL_HIERARCHY.md | BHG-Governance | C1 | hierarchy model | defines normative levels | conflict NORM-001/NORM-007 |
| GOVERNANCE_APPROVAL_MODEL.md | BHG-Governance | C1 | approval semantics | defines approval levels | separate approval from authority |
| GOVERNANCE_INTEROPERABILITY_MODEL.md | BHG-Governance | C1 | cross-domain governance | shared governance contracts | canonical ownership unresolved |
| DOCUMENT_STANDARD.md | BHG-Governance | C2 | document contract | global document structure/lifecycle | conflict register applies |
| DOCUMENT_METADATA_STANDARD.md | BHG-Governance | C2 | metadata contract | shared metadata semantics | BLOCKER reconciliation |
| DOCUMENT_SCHEMA_STANDARD.md | BHG-Governance | C2 | schema contract | structural metadata/schema | BLOCKER reconciliation |
| DOCUMENT_GRAMMAR_STANDARD.md | BHG-Governance | C2 | grammar contract | document grammar | BLOCKER reconciliation |
| DOCUMENT_RELATIONSHIP_STANDARD.md | BHG-Governance | C2 | relationship vocabulary | graph semantics | BLOCKER reconciliation |
| DOCUMENT_VALIDATION_STANDARD.md | BHG-Governance | C2 | validation contract | validation semantics | verify ownership |
| DOCUMENT_LIFECYCLE.md | BHG-Governance | C2 | lifecycle contract | status/evolution semantics | verify |
| DOCUMENT_DEPENDENCY_STANDARD.md | BHG-Governance | C2 | dependency semantics | dependency graph | distinguish from governed_by |
| ARCHITECTURE_MAP.md | BHG-Governance | C3 | repository architecture | repository/document architecture | candidate cross-layer bridge |
| REPOSITORY_STANDARD.md | bhg-knowledge | C3 | repository contract | repository rules | reconcile with Foundation repository standards |
| REPOSITORY_CLASSIFICATION.md | BHG-Ecosystem-Foundation | C3 | repository identity/classification | repository governance | candidate canonical owner |
| REPOSITORY_DEPENDENCY_MODEL.md | BHG-Ecosystem-Foundation | C3 | repository dependency | inter-repository dependencies | candidate canonical owner |
| REPOSITORY_LIFECYCLE.md | BHG-Ecosystem-Foundation | C3 | repository lifecycle | lifecycle semantics | candidate canonical owner |
| REPOSITORY_NAMING_STANDARD.md | BHG-Ecosystem-Foundation | C3 | repository naming | identity/naming contract | scope overlap known |
| REPOSITORY_REGISTRY.md | BHG-Ecosystem-Foundation | C3 | repository registry | authoritative repository inventory candidate | verify ownership |
| CROSS_REPOSITORY_MODEL.md | BHG-Ecosystem-Foundation | C3 | cross-repository contract | ecosystem integration | candidate bridge |
| ECOSYSTEM_ARCHITECTURE.md | BHG-Ecosystem-Foundation | C3 | ecosystem architecture | ecosystem structural model | candidate foundation bridge |
| ECOSYSTEM_BOUNDARIES.md | BHG-Ecosystem-Foundation | C3 | ecosystem boundaries | scope/boundary definition | candidate foundation bridge |
| ECOSYSTEM_LAYERS.md | BHG-Ecosystem-Foundation | C3 | ecosystem layers | layer model | candidate architecture input |
| F001_CHANGE_GOVERNANCE_VALIDATION.md | BHG-Governance | C4 | change validation | governance change controls | audit/validation role |
| NORMATIVE_CONFLICT_REGISTER.md | BHG-Governance | C4 | conflict evidence | records demonstrated normative conflicts | evidence, not authority |
| 00_ENGINEERING_CHARTER.md | ZivaLatam | C5 | domain governance bridge | explicit Ziva engineering governance entry point | must be subordinate/specialized under BHG |

## Notes

1. The current list is deliberately wider than the final 40–60 target so the machine pass can remove duplicates and low-centrality candidates.
2. BHG-Ecosystem-Foundation and bhg-knowledge contain repository/architecture artifacts that may overlap with BHG-Governance. This is an ownership question, not a reason to omit either repository.
3. Ziva ADRs are not automatically Core documents. They enter the Core only when they define a cross-domain contract or establish a required bridge to the BHG authority model.
4. Draft/Review documents remain corpus evidence. Their status does not cause silent deletion from analysis.
5. The eight authority-cycle nodes and 12 missing-evidence relationships remain unresolved inputs.
