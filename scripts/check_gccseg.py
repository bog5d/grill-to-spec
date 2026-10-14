#!/usr/bin/env python3
"""Dependency-free structural GCCSEG gate. Semantic evidence review is separate."""
import json
import pathlib
import sys

REQUIRED = ("goal", "context", "capability", "state", "evidence", "gate")
LEVELS = ("CLI_READY", "TASK_EXECUTED", "AUTONOMOUS_DISPATCHED", "FAILOVER_VERIFIED", "UNATTENDED_HANDOFF_VERIFIED")

def validate(d, require_v38=False):
    errors = []
    if not isinstance(d, dict):
        return ["root must be object"]
    for k in REQUIRED:
        if k not in d:
            errors.append(f"missing {k}")
    if errors:
        return errors
    if not isinstance(d["goal"], dict) or not d["goal"].get("success_criteria"):
        errors.append("goal.success_criteria required")
    if not isinstance(d["context"], dict) or not isinstance(d["context"].get("facts"), list):
        errors.append("context.facts must be array")
    else:
        for i, f in enumerate(d["context"]["facts"]):
            if not isinstance(f, dict) or not all(f.get(k) for k in ("claim", "source")) or f.get("classification") not in ("CURRENT", "HISTORICAL", "INFERRED", "UNKNOWN"):
                errors.append(f"context.facts[{i}] invalid")
    if not isinstance(d["capability"], dict) or not d["capability"].get("effective_config_ref"):
        errors.append("capability.effective_config_ref required")
    if not isinstance(d["state"], dict) or not d["state"].get("next_action"):
        errors.append("state.next_action required")
    if not isinstance(d["evidence"], list):
        errors.append("evidence must be array")
    else:
        for i, e in enumerate(d["evidence"]):
            if not isinstance(e, dict) or not all(e.get(k) for k in ("subject_id", "source", "event_at", "collected_at", "claim", "validation_result")):
                errors.append(f"evidence[{i}] missing fields")
    if not isinstance(d["gate"], dict) or d["gate"].get("level") not in LEVELS or not d["gate"].get("acceptance_criteria"):
        errors.append("gate.level and gate.acceptance_criteria required")
    # v3.8 semantic *structure* guard. Real execution still needs independent proof.
    if require_v38 or d.get("contract_version") == "3.8":
        if d.get("contract_version") != "3.8":
            errors.append("contract_version=3.8 required")
        if d.get("task_level") not in ("L1", "L2"):
            errors.append("task_level must be L1 or L2 for v3.8")
        g = d.get("goal_alignment")
        if not isinstance(g, dict):
            errors.append("goal_alignment object required for v3.8")
        else:
            if not isinstance(g.get("north_star"), str) or not g["north_star"].strip():
                errors.append("goal_alignment.north_star required")
            a = g.get("user_visible_acceptance")
            if not isinstance(a, list) or not a or any(not isinstance(x, str) or not x.strip() for x in a):
                errors.append("goal_alignment.user_visible_acceptance nonempty list required")
            baseline = g.get("baseline")
            if not isinstance(baseline, dict) or baseline.get("status") not in ("PASS", "FAIL", "PARTIAL", "UNKNOWN") or not baseline.get("evidence_ref"):
                errors.append("goal_alignment.baseline status and evidence_ref required")
            mapping = g.get("work_to_goal_map")
            if not isinstance(mapping, list) or not mapping or any(not isinstance(x, dict) or not all(x.get(k) for k in ("work_item_id", "goal_metric_id", "expected_change")) for x in mapping):
                errors.append("goal_alignment.work_to_goal_map invalid")
            if not isinstance(g.get("next_goal_gap"), str) or not g["next_goal_gap"].strip():
                errors.append("goal_alignment.next_goal_gap required")
            progress = g.get("progress")
            if not isinstance(progress, dict) or not all(k in progress for k in ("engineering_percent", "outcome_verified_points", "outcome_total_points")):
                errors.append("goal_alignment.progress dual measures required")
            else:
                for name in ("engineering_percent", "outcome_verified_points", "outcome_total_points"):
                    val = progress[name]
                    if val is not None and (isinstance(val, bool) or not isinstance(val, (int, float)) or not 0 <= val <= 100):
                        errors.append(f"goal_alignment.progress.{name} out of bounds")
            if d.get("task_level") == "L2":
                metrics, gates = g.get("outcome_metrics"), g.get("hard_gates")
                if not isinstance(metrics, list) or not metrics:
                    errors.append("L2 requires outcome_metrics")
                else:
                    names = []
                    weight_total = verified_total = 0
                    for i, m in enumerate(metrics):
                        if not isinstance(m, dict):
                            errors.append(f"metric[{i}] not object")
                            continue
                        name, status, weight, pts, refs = (m.get(k) for k in ("id", "status", "weight", "verified_points", "evidence_refs"))
                        if not isinstance(name, str) or not name.strip() or name in names:
                            errors.append(f"metric[{i}] missing/duplicate id")
                        names.append(name)
                        if isinstance(weight, bool) or not isinstance(weight, (int, float)) or not 0 < weight <= 100 or isinstance(pts, bool) or not isinstance(pts, (int, float)) or not 0 <= pts <= (weight if isinstance(weight, (int, float)) else 0):
                            errors.append(f"metric[{i}] invalid weight/points")
                            continue
                        weight_total += weight
                        verified_total += pts
                        if status not in ("UNKNOWN", "FAIL", "ISOLATED_PASS", "REAL_PASS") or not isinstance(refs, list):
                            errors.append(f"metric[{i}] invalid status/evidence_refs")
                        elif status in ("UNKNOWN", "FAIL") and pts != 0:
                            errors.append(f"metric[{i}] failed/unproven but awarded points")
                        elif status == "ISOLATED_PASS" and pts > weight * 0.5:
                            errors.append(f"metric[{i}] isolated pass overclaims points")
                        elif pts > 0 and not refs:
                            errors.append(f"metric[{i}] awarded points without evidence")
                    if abs(weight_total - 100) > 0.0001:
                        errors.append("L2 outcome_metrics weights must sum to 100")
                    if isinstance(progress, dict) and isinstance(progress.get("outcome_verified_points"), (int, float)) and abs(progress["outcome_verified_points"] - verified_total) > 0.0001:
                        errors.append("outcome_verified_points must equal evidenced metric sum")
                    if isinstance(progress, dict) and progress.get("outcome_total_points") != 100:
                        errors.append("L2 outcome_total_points must equal 100")
                    mapped_ids = {x.get("goal_metric_id") for x in mapping if isinstance(x, dict)} if isinstance(mapping, list) else set()
                    if not mapped_ids.intersection(set(names)):
                        errors.append("work_to_goal_map must reference outcome metric")
                goal_state = g.get("goal_state")
                if goal_state not in ("NOT_MET", "UNKNOWN", "VERIFIED"):
                    errors.append("L2 goal_state required (NOT_MET / UNKNOWN / VERIFIED)")
                total_claimed = progress.get("outcome_verified_points") if isinstance(progress, dict) else None
                if goal_state == "VERIFIED" or total_claimed == 100:
                    if not isinstance(gates, list) or not gates or any(not isinstance(h, dict) or h.get("status") != "PASS" for h in gates):
                        errors.append("100%/VERIFIED requires every hard gate PASS")
                    if total_claimed != 100:
                        errors.append("VERIFIED requires full outcome 100/100")
                if not isinstance(gates, list) or not gates:
                    errors.append("L2 requires hard_gates")
                else:
                    for i, gate in enumerate(gates):
                        if not isinstance(gate, dict) or not gate.get("id") or gate.get("status") not in ("PASS", "FAIL", "BLOCKED", "UNKNOWN") or not isinstance(gate.get("evidence_refs"), list):
                            errors.append(f"hard_gate[{i}] invalid")
                        elif gate["status"] == "PASS" and not gate["evidence_refs"]:
                            errors.append(f"hard_gate[{i}] PASS without evidence")
    return errors

def main():
    args = [a for a in sys.argv[1:] if a != "--require-v3-8"]
    if len(args) != 1:
        print("usage: python scripts/check_gccseg.py [--require-v3-8] path/to/task.json", file=sys.stderr)
        return 2
    try:
        data = json.loads(pathlib.Path(args[0]).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 2
    errors = validate(data, require_v38='--require-v3-8' in sys.argv)
    if errors:
        print("FAIL: " + "; ".join(errors))
        return 1
    print("PASS: GCCSEG structural + goal alignment contract (not semantic or real-world acceptance)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
