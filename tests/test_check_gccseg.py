import unittest
from scripts.check_gccseg import validate

class TestGCCSEG(unittest.TestCase):
    def test_missing(self):
        self.assertIn("missing goal", validate({}))
    def test_valid(self):
        d = {"goal": {"success_criteria": ["done"]}, "context": {"facts": []}, "capability": {"effective_config_ref": "config/live.json"}, "state": {"status": "READY", "next_action": "dispatch"}, "evidence": [], "gate": {"level": "CLI_READY", "acceptance_criteria": ["exit 0"]}}
        self.assertEqual(validate(d), [])
    def test_unverified_claim(self):
        d = {"goal": {"success_criteria": ["done"]}, "context": {"facts": [{"claim": "crashed", "source": "old log", "classification": "INVALID"}]}, "capability": {"effective_config_ref": "config/live.json"}, "state": {"status": "READY", "next_action": "dispatch"}, "evidence": [], "gate": {"level": "CLI_READY", "acceptance_criteria": ["exit 0"]}}
        self.assertTrue(validate(d))


    def test_v38_outcome_contract(self):
        import json
        from pathlib import Path
        d = json.loads(Path("examples/gccseg/v38-goal-aligned.json").read_text(encoding="utf-8"))
        self.assertEqual(validate(d, require_v38=True), [])

    def test_heartbeat_only_cannot_claim_autonomous_100(self):
        import json
        from pathlib import Path
        d = json.loads(Path("examples/gccseg/v38-heartbeat-false-pass.json").read_text(encoding="utf-8"))
        errors = validate(d, require_v38=True)
        self.assertTrue(errors)
        self.assertTrue(any("failed/unproven" in e for e in errors), errors)

    def test_legacy_contract_blocked_when_v38_enforced(self):
        d = {"goal": {"success_criteria": ["done"]}, "context": {"facts": []}, "capability": {"effective_config_ref": "config/live.json"}, "state": {"status": "READY", "next_action": "dispatch"}, "evidence": [], "gate": {"level": "CLI_READY", "acceptance_criteria": ["exit 0"]}}
        self.assertEqual(validate(d), [])  # historical compatibility
        self.assertIn("contract_version=3.8 required", validate(d, require_v38=True))

    def test_missing_target_link_rejected(self):
        import json
        from pathlib import Path
        d = json.loads(Path("examples/gccseg/v38-goal-aligned.json").read_text(encoding="utf-8"))
        d["goal_alignment"]["work_to_goal_map"][0]["goal_metric_id"] = "UNRELATED"
        self.assertTrue(any("reference outcome metric" in e for e in validate(d, require_v38=True)))

if __name__ == "__main__":
    unittest.main()
