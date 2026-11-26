"""Basic structural tests; these do not require Ollama or model downloads."""
import unittest

from agents.multi_agent import WORKER_TOOL_MAP, WORKER_PROMPTS, SUPERVISOR_PROMPT

class MultiAgentStructureTests(unittest.TestCase):
    def test_four_specialists_are_defined(self):
        self.assertEqual(len(WORKER_TOOL_MAP), 4)
        self.assertEqual(set(WORKER_TOOL_MAP), set(WORKER_PROMPTS))

    def test_each_worker_has_tools(self):
        for tools in WORKER_TOOL_MAP.values():
            self.assertTrue(tools)

    def test_safety_prompts(self):
        self.assertIn("NOT proof", WORKER_PROMPTS["anomaly_investigator"])
        self.assertIn("never execute", SUPERVISOR_PROMPT.lower())

if __name__ == "__main__":
    unittest.main()
