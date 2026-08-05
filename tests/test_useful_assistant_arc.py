import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1] / "excavations"

def load(number):
    path = next(ROOT.glob(number + "-*/implementation/pure_python.py"))
    spec = importlib.util.spec_from_file_location("excavation_" + number, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class UsefulAssistantArcTests(unittest.TestCase):
    def test_perplexity(self):
        self.assertAlmostEqual(load("046").perplexity([.5,.5,.5]),2)
    def test_calibration(self):
        self.assertAlmostEqual(load("049").calibration_gap([.8]*5,[1,1,1,1,0]),0)
    def test_preference(self):
        self.assertGreater(load("053").preference_probability(2,1),.5)
    def test_retrieval(self):
        result=load("054").retrieve("tiger",["river","tiger stripes"],lambda q,d:int(q in d))
        self.assertEqual(result,"tiger stripes")
    def test_tool_permission(self):
        module=load("055")
        with self.assertRaises(PermissionError):
            module.act("weather",{},allowed={})

if __name__ == "__main__":
    unittest.main()
