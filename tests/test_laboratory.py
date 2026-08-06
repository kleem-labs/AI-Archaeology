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

if __name__ == "__main__":
    unittest.main()
