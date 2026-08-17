import json
from pathlib import Path

ROOT = Path(__file__).parent
fixtures = json.loads((ROOT / "fixtures.json").read_text())

allowed = {
    ("F0", "F1"), ("F1", "F2"), ("F2", "F3"), ("F3", "F4"),
    ("F4", "F5"), ("F4", "F3")
}

def evaluate(s):
    pair = (s["from"], s["to"])
    evidence = s["evidence"]
    if evidence == "duplicate":
        return "DUPLICATE"
    if evidence == "good_faith_failure":
        return "RETURN_WITH_LEARNING"
    if pair not in allowed:
        return "REJECT"
    if evidence in {"missing_impact", "scope_creep", "governance_bypass", "experiment_failed", "missing_rollback"}:
        return "REJECT"
    if pair == ("F4", "F5") and "limited_scope" not in evidence:
        return "REJECT"
    return "PASS"

results = []
for scenario in fixtures["scenarios"]:
    observed = evaluate(scenario)
    expected = scenario["expected"]
    results.append({"id": scenario["id"], "expected": expected, "observed": observed, "pass": observed == expected})

# Deterministic replay
replay = []
for scenario in fixtures["scenarios"]:
    replay.append(evaluate(scenario))
first = [r["observed"] for r in results]

summary = {
    "fixture_set": fixtures["fixture_set"],
    "scenario_count": len(results),
    "scenario_pass_count": sum(r["pass"] for r in results),
    "all_expected_results_match": all(r["pass"] for r in results),
    "deterministic_replay": replay == first,
    "production_write_allowed": fixtures["production_write_allowed"],
    "results": results,
}
print(json.dumps(summary, indent=2, sort_keys=True))
if not (summary["all_expected_results_match"] and summary["deterministic_replay"] and not summary["production_write_allowed"]):
    raise SystemExit(1)
