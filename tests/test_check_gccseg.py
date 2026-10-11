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

if __name__ == "__main__":
    unittest.main()
