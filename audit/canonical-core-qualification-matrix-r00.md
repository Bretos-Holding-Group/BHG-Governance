# Canonical Core Qualification Matrix R00

Status: CANDIDATE / NON-NORMATIVE
Scope: 60 discovery candidates derived from the four-repository corpus.

## Qualification contract

Centrality is discovery evidence only. It does not create normative authority. A candidate is qualified only through independent evidence of centrality, authority, contractuality, foundationality, ownership, lifecycle status, conflicts, cycles, and traceability.

### Decision rules used in this machine pass

- `CORE-CANDIDATE`: Approved + strong foundational/contract evidence + no automatic disqualifier detected in the discovery record. This remains a candidate, not canonical authority.
- `HOLD`: Draft/Review status, unresolved authority/ownership, known conflict class, or protected cycle involvement.
- `SUPPORTING-CANDIDATE`: structurally useful but not independently foundational.
- `EXCLUDE-FROM-CORE`: not assigned automatically in R00; absence from Core must be justified by evidence rather than score alone.

### Anti-inference rules

- Centrality MUST NOT create authority.
- Draft/Review MUST NOT be promoted to Approved.
- A `governed_by` cycle MUST NOT be broken automatically.
- Filename/path MUST NOT establish ownership.
- Approval authority MUST NOT be treated as normative authority.
- Existing documents remain corpus evidence regardless of status.

## Populated 60-row machine qualification register

| Rank | Document ID | Repository | Score | Status | Authority evidence | Ownership | Contractuality | Foundationality | Conflict/cycle gate | Decision | Rationale |
|---:|---|---|---:|---|---|---|---|---|---|---|---|
|1|BHG-MIG-2F763FF54F97|BHG-Governance|93|Approved|constitutional/supreme signal|BHG|strong|strong|review required|CORE-CANDIDATE|Highest structural signal; constitutional evidence requires hierarchy verification.|
|2|BHG-MIG-5456F6E19A27|BHG-Governance|84|Approved|constitutional/supreme signal|BHG|strong|strong|review required|CORE-CANDIDATE|Constitutional/foundational signal.|
|3|BHG-LH-001|BHG-Governance|75|Approved|foundational governance level|BHG|strong|strong|Legal Hierarchy conflict class|HOLD|High-value authority model but affected by hierarchy reconciliation.|
|4|BHG-MIG-54D9BFC94609|BHG-Governance|70|Approved|foundational governance level|BHG|strong|strong|authority reconciliation|CORE-CANDIDATE|Governance matrix with strong foundational/contract evidence.|
|5|BHG-MIG-C43A05E01439|BHG-Governance|70|Approved|foundational governance level|BHG|strong|strong|authority reconciliation|CORE-CANDIDATE|Governance model with strong foundational/contract evidence.|
|6|BHG-GOV-CAM-001|BHG-Governance|69|Draft|foundational governance level|BHG|strong|strong|Draft|HOLD|High-value candidate but lifecycle status prevents promotion.|
|7|BHG-GOV-002|BHG-Governance|67|Approved|foundational governance level|BHG|strong|strong|review required|CORE-CANDIDATE|Governance process is structurally foundational.|
|8|BHG-GPS-001|BHG-Governance|65|Approved|foundational governance level|BHG|strong|strong|review required|CORE-CANDIDATE|Standard with strong contract/foundation signal.|
|9|BHG-POL-002|BHG-Governance|59|Approved|contract indicators|BHG|strong|medium|review required|CORE-CANDIDATE|High inbound centrality and reusable policy contract.|
|10|GOVERNANCE-APPROVAL-MODEL|BHG-Governance|57|Approved|governance model|BHG|strong|strong|approval-vs-authority conflict class|HOLD|Core contract candidate but approval authority must remain distinct from normative authority.|
|11|BHG-POL-VERSIONING|BHG-Governance|57|Approved|contract indicators|BHG|strong|medium|review required|CORE-CANDIDATE|High inbound centrality and versioning contract.|
|12|BHG-GOV-009|BHG-Governance|54|Approved|foundational governance level|BHG|strong|strong|review required|CORE-CANDIDATE|Governance process with foundational evidence.|
|13|BHG-MIG-DA57580E8D90|BHG-Governance|54|Approved|contract indicators|BHG|strong|medium|review required|CORE-CANDIDATE|Reusable corporate policy contract.|
|14|GOVERNANCE_INTEROPERABILITY_MODEL|BHG-Governance|53|Approved|foundational governance level|BHG|strong|strong|ownership/authority review|HOLD|Cross-domain governance contract requires ownership confirmation.|
|15|GOVERNANCE_REGISTRY_MODEL|BHG-Governance|52|Approved|foundational governance level|BHG|strong|strong|review required|CORE-CANDIDATE|Registry model with strong contract/foundation signal.|
|16|BHG-MIG-9783A5418C4A|BHG-Governance|52|Approved|foundational governance level|BHG|strong|strong|review required|CORE-CANDIDATE|Standard with strong foundational signal.|
|17|ECOSYSTEM_ARCHITECTURE|BHG-Governance|50|Approved|foundational governance level|BHG|strong|strong|cross-layer review|CORE-CANDIDATE|Architecture bridge is foundational.|
|18|BHG-FDN-001|BHG-Governance|49|Approved|foundational governance level|BHG|strong|strong|constitutional subordination review|CORE-CANDIDATE|Institutional foundation candidate; subordinate to Constitution.|
|19|BHG-FDN-002|BHG-Governance|49|Approved|foundational governance level|BHG|strong|strong|review required|CORE-CANDIDATE|Foundation reference with broad scope.|
|20|GOVERNANCE_AUTONOMY_MODEL|BHG-Governance|49|Approved|foundational governance level|BHG|strong|strong|authority delegation review|HOLD|Autonomy must not elevate delegated authority.|
|21|GOVERNANCE_DELEGATION_MODEL|BHG-Governance|49|Approved|foundational governance level|BHG|strong|strong|authority delegation review|HOLD|Delegation semantics require authority boundary verification.|
|22|GOVERNANCE_EVOLUTION_MODEL|BHG-Governance|49|Approved|foundational governance level|BHG|strong|strong|review required|CORE-CANDIDATE|Governance evolution contract.|
|23|GOVERNANCE_MODEL|BHG-Governance|49|Approved|foundational governance level|BHG|strong|strong|authority reconciliation|HOLD|Central governance model requires hierarchy reconciliation.|
|24|BHG-GOV-CDRM-001|BHG-Governance|49|Effective|foundational governance level|BHG|strong|strong|status/evidence review|CORE-CANDIDATE|Effective governance model with strong foundational signal.|
|25|BHG-POL-001|BHG-Governance|49|Approved|contract indicators|BHG|strong|medium|review required|CORE-CANDIDATE|Reusable policy contract with inbound centrality.|
|26|ECOSYSTEM_MODEL|BHG-Governance|48|Approved|foundational governance level|BHG|strong|strong|cross-layer review|CORE-CANDIDATE|Ecosystem structural model.|
|27|ORGANIZATION_MODEL|BHG-Governance|48|Approved|foundational governance level|BHG|strong|strong|scope review|CORE-CANDIDATE|Organization architecture contract.|
|28|GROWTH_MODEL|BHG-Governance|48|Draft|foundational governance level|BHG|strong|strong|Draft|HOLD|Structural value is high but status prevents promotion.|
|29|BHG-MIG-6F1F2862B6EF|BHG-Governance|48|Approved|foundational governance level|BHG|strong|strong|review required|CORE-CANDIDATE|Governance model candidate.|
|30|BHG-MIG-B417AA972D08|BHG-Governance|48|Draft|foundational governance level|BHG|strong|strong|Draft|HOLD|High structural signal but lifecycle unresolved.|
|31|ECOSYSTEM_PRINCIPLES|BHG-Governance|47|Approved|foundational governance level|BHG|strong|strong|review required|CORE-CANDIDATE|Ecosystem principles provide foundational contract.|
|32|REPOSITORY_LIFECYCLE|BHG-Governance|47|Approved|foundational governance level|BHG|strong|strong|repository ownership review|HOLD|Repository contract overlaps Foundation domain; ownership must be resolved.|
|33|REPOSITORY_REGISTRY|BHG-Governance|47|Approved|foundational governance level|BHG|strong|strong|registry ownership review|HOLD|Registry authority requires cross-repository ownership verification.|
|34|BHG-MIG-B6F5272CD7D6|BHG-Governance|47|Review|foundational governance level|BHG|strong|strong|Review status|HOLD|Lifecycle status unresolved.|
|35|ARCHITECTURE_MAP|BHG-Governance|46|Draft|foundational governance level|BHG|strong|strong|Draft + cross-layer ownership|HOLD|Important architecture candidate but not approved.|
|36|ECOSYSTEM_BOUNDARIES|BHG-Governance|46|Approved|foundational governance level|BHG|strong|strong|boundary review|CORE-CANDIDATE|Defines ecosystem scope/boundaries.|
|37|ECOSYSTEM_LAYERS|BHG-Governance|46|Approved|foundational governance level|BHG|strong|strong|layer authority review|CORE-CANDIDATE|Layer model is foundational.|
|38|BUSINESS_CAPABILITY_MODEL|BHG-Governance|46|Approved|foundational governance level|BHG|strong|strong|scope review|CORE-CANDIDATE|Capability model supports organization architecture.|
|39|REPOSITORY_CLASSIFICATION|BHG-Governance|46|Approved|foundational governance level|BHG|strong|strong|cross-repository ownership|HOLD|Repository classification overlaps Foundation ownership.|
|40|REPOSITORY_DEPENDENCY_MODEL|BHG-Governance|46|Approved|foundational governance level|BHG|strong|strong|cross-repository ownership|HOLD|Dependency contract needs canonical owner.|
|41|REPOSITORY_NAMING_STANDARD|BHG-Governance|46|Approved|foundational governance level|BHG|strong|strong|scope overlap|HOLD|Naming contract needs canonical owner and scope.|
|42|CROSS_REPOSITORY_MODEL|BHG-Governance|46|Approved|foundational governance level|BHG|strong|strong|cross-repository ownership|HOLD|Cross-repository bridge requires ownership confirmation.|
|43|MATURITY_MODEL|BHG-Governance|46|Draft|foundational governance level|BHG|strong|medium|Draft|HOLD|Draft lifecycle prevents promotion.|
|44|BHG-MIG-375CFA146C47|BHG-Governance|46|Review|foundational governance level|BHG|strong|strong|Review status|HOLD|Lifecycle unresolved.|
|45|BHG-MIG-49D1A6CF8892|BHG-Governance|46|Approved|contract indicators|BHG|strong|medium|review required|CORE-CANDIDATE|Standard with contract signal.|
|46|BHG-AUD-NORM-001|BHG-Governance|46|Draft|audit|BHG|medium|medium|Draft|HOLD|Audit evidence is valuable but not a normative core authority.|
|47|BUSINESS_DOMAIN_MODEL|BHG-Governance|45|Approved|foundational governance level|BHG|strong|strong|scope review|CORE-CANDIDATE|Domain model supports organization architecture.|
|48|ECOSYSTEM_SYNCHRONIZATION|BHG-Governance|45|Approved|foundational governance level|BHG|strong|strong|cross-layer review|CORE-CANDIDATE|Synchronization contract supports ecosystem coherence.|
|49|SOURCE_OF_TRUTH_MODEL|BHG-Governance|45|Approved|foundational governance level|BHG|strong|strong|authority/source review|HOLD|Source-of-truth semantics must not create circular authority.|
|50|EVOLUTION_MODEL|BHG-Governance|45|Approved|foundational governance level|BHG|strong|strong|review required|CORE-CANDIDATE|Ecosystem evolution model.|
|51|DOCUMENT_STANDARD|BHG-Governance|45|Draft|contract indicators|BHG|strong|strong|Draft + metadata/schema fragmentation|HOLD|Potential core contract but explicitly blocked pending standard reconciliation.|
|52|BHG-MIG-8327291A8F30|BHG-Governance|45|Draft|contract indicators|BHG|strong|medium|Draft|HOLD|High inbound centrality but lifecycle unresolved.|
|53|IDENTITY_MODEL|BHG-Governance|44|Draft|foundational governance level|BHG|strong|strong|Draft + identity reconciliation|HOLD|Identity is core-relevant but cannot be promoted automatically.|
|54|HOLDING_MODEL|BHG-Governance|44|Approved|foundational governance level|BHG|strong|strong|review required|CORE-CANDIDATE|Holding architecture contract.|
|55|SHARED_ASSET_MODEL|BHG-Governance|44|Approved|foundational governance level|BHG|strong|strong|cross-domain ownership review|HOLD|Shared-asset authority boundary requires verification.|
|56|ROADMAP_MODEL|BHG-Governance|44|Approved|foundational governance level|BHG|strong|medium|review required|SUPPORTING-CANDIDATE|Useful governance planning contract but not independently foundational.|
|57|HISTORY_ARCHIVE_README|BHG-Governance|44|Draft|historical guide|BHG|weak|weak|Draft + historical role|HOLD|Important evidence but not a core normative contract.|
|58|FOUNDATION_NORMALIZATION_ROADMAP|BHG-Ecosystem-Foundation|43|Draft|foundational governance level|Foundation|strong|strong|Draft + cross-repository authority|HOLD|Foundation-layer roadmap cannot be promoted until BHG/Foundation authority boundary is explicit.|
|59|BHG_GOVERNANCE_ARCHITECTURE_MAP|BHG-Governance|43|Draft|contract indicators|BHG|strong|strong|Draft + 12 missing-evidence references|HOLD|High-value architecture evidence but unresolved references remain.|
|60|BRAND_ARCHITECTURE|BHG-Governance|43|Approved|foundation identity model|BHG|medium|medium|scope review|SUPPORTING-CANDIDATE|Relevant identity model but not independently foundational to governance core.|

## Cycle cross-check

The eight protected cycle nodes are `BHG-MIG-304657D4691E`, `BHG-MIG-38F961165834`, `BHG-MIG-4EF6926C68EA`, `BHG-MIG-71A9F2A90F32`, `BHG-MIG-83A30C7D861D`, `BHG-MIG-AB1A5B8A9156`, `BHG-MIG-D13DBA24B680`, and `BHG-MIG-D140A7A5674C`. No automated edge removal or authority reassignment is performed by this matrix. Any candidate proven to participate in one of these cycles remains HOLD until semantic authority is resolved.

## Normative conflict cross-check

Known conflict classes are treated as gates, not as automatic corrections: Constitution vs Legal Hierarchy; Governance Approval Model vs normative authority; Foundation vs constitutional authority; BHG vs Ziva/domain ownership; metadata/schema/grammar/relationship fragmentation; repository ownership/delegation ambiguity. A candidate affected by one of these unresolved classes cannot receive unconditional canonical status.

## Result

This matrix is a qualification artifact, not a canonization decision. The current machine disposition is deliberately conservative: candidates with unresolved lifecycle, authority, ownership, cycle, or conflict conditions remain HOLD. The final Canonical Core R00 requires governance approval after CI verifies the reproducibility of this register against the complete corpus.
