# F4 Controlled Governance Execution Harness

This harness defines a deterministic, synthetic-only execution layer for the F4 controlled governance experiment.

## Rules

- No production repositories, records, participants, or evidence are mutated.
- Fixtures use synthetic identifiers only.
- Every transition is evaluated against the F0-F9 model and gate rules.
- Illegal promotion attempts must be rejected.
- Failed experiments must not be promoted.
- Good-faith failure is distinct from misconduct.
- Replay of the same fixture and ruleset must produce the same result.

## Execution contract

Each scenario supplies:

1. current lifecycle state;
2. requested transition;
3. evidence profile;
4. governance conditions;
5. expected result.

The execution record must contain observed result, rule outcome, and deterministic replay result.
