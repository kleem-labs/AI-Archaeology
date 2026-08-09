"""Every Part XI Pure Python experiment must visibly reject and repair."""
from pathlib import Path
import importlib.util
import unittest


class PartXITests(unittest.TestCase):
    def test_every_experiment_has_a_working_gate(self):
        root = Path(__file__).parents[1] / "excavations"
        paths = sorted(root.glob("1[2-5][0-9]-*/implementation/pure_python.py"))
        paths = [path for path in paths if 126 <= int(path.parents[1].name[:3]) <= 150]
        self.assertEqual(len(paths), 25)
        for path in paths:
            spec = importlib.util.spec_from_file_location(path.parents[1].name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            weak = {"evidence": True, "failure_test": False, "approved": True}
            repaired = {"evidence": True, "failure_test": True, "approved": True}
            self.assertFalse(module.accept(weak), path)
            self.assertTrue(module.accept(repaired), path)


if __name__ == "__main__":
    unittest.main()
