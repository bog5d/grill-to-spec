#!/usr/bin/env python3
"""Dependency-free structural GCCSEG gate. Semantic evidence review is separate."""
import json
import pathlib
import sys

REQUIRED = ("goal", "context", "capability", "state", "evidence", "gate")
LEVELS = ("CLI_READY", "TASK_EXECUTED", "AUTONOMOUS_DISPATCHED", "FAILOVER_VERIFIED", "UNATTENDED_HANDOFF_VERIFIED")

def validate(d):
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
    return errors

def main():
    if len(sys.argv) != 2:
        print("usage: python scripts/check_gccseg.py path/to/task.json", file=sys.stderr)
        return 2
    try:
        data = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 2
    errors = validate(data)
    if errors:
        print("FAIL: " + "; ".join(errors))
        return 1
    print("PASS: GCCSEG structural contract (not semantic acceptance)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
