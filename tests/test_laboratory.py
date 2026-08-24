import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]

def load(name):
    path = ROOT / "labs" / name
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class LaboratoryTests(unittest.TestCase):
    def test_distance_lab(self):
        self.assertGreater(load("01_distance_lab.py").run(), 0)
    def test_softmax_lab(self):
        load("02_softmax_lab.py").run()
    def test_attention_lab(self):
        self.assertIn("output", load("03_attention_lab.py").run())
    def test_gradient_lab(self):
        load("04_gradient_lab.py").run()
    def test_generation_lab(self):
        self.assertEqual(len(load("05_generation_lab.py").run()), 4)
    def test_engine_rebuild_lab(self):
        result = load("06_engine_rebuild_lab.py").run_lab()
        self.assertEqual(result["quality_authority"], "frozen target model")
        self.assertEqual(result["kv_cache_reduction"], 4)
    def test_pretraining_factory_lab(self):
        result = load("07_pretraining_factory_lab.py").run_lab()
        self.assertEqual(result["raw_documents"], 4)
        self.assertEqual(result["unique_documents"], 3)
        self.assertTrue(result["release"])
    def test_mathematical_roots_lab(self):
        result = load("08_mathematical_roots_lab.py").run_lab()
        self.assertEqual(result["set overlap"], {"tiger", "otter"})
        self.assertEqual(result["best bridge action"], "cross")
        self.assertTrue(result["stable log total"] > 1000)

if __name__ == "__main__":
    unittest.main()
