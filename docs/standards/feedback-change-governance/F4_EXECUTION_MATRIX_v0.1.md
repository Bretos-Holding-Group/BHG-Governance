---
document_id: BHG-UFCG-F4-MAT-001
title: F4 Execution Matrix
version: 0.1.0
status: Proposed
document_type: execution_matrix
governance_level: repository
owner: BHG Governance
approval_authority: BHG Governance review
---

# F4 Execution Matrix v0.1

| Test | Input | Expected | Evidence |
|---|---|---|---|
| F4-001 | Valid F0→F1 | Accept | transition record |
| F4-002 | Valid F1→F2 | Accept | evidence checklist |
| F4-003 | Valid F2→F3 | Accept | experiment authorization |
| F4-004 | Valid F3→F4 | Accept | controlled-test record |
| F4-005 | F1→F7 bypass | Reject | gate violation |
| F4-006 | F3→F9 bypass | Reject | gate violation |
| F4-007 | Missing evidence | Hold/Reject | deficiency record |
| F4-008 | Duplicate proposal | Triage/Link | duplicate record |
| F4-009 | Unsupported impact claim | Hold | evidence deficiency |
| F4-010 | Scope creep | Reject/Redirect | scope record |
| F4-011 | Governance bypass | Reject/Escalate | governance record |
| F4-012 | Repeated unsupported proposal | Deprioritize/Close | noise record |
| F4-013 | Failed experiment | Return/Abandon | failure record |
| F4-014 | Good-faith failed proposal | Preserve learning | non-misconduct record |
| F4-015 | Replay identical case | Same decision | replay record |
| F4-016 | Production isolation | Zero changes | repository check |
