"""Executable checks for the mathematical roots in Part XIV."""

from pathlib import Path
import importlib.util
import unittest


ROOT = Path(__file__).parents[1]


def load(path):
    spec = importlib.util.spec_from_file_location(path.parents[1].name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PartXIVTests(unittest.TestCase):
    def test_every_pure_python_discovery_runs(self):
        paths = [
            next((ROOT / "excavations").glob(f"{number:03d}-*/implementation/pure_python.py"))
            for number in range(201, 226)
        ]
        self.assertEqual(len(paths), 25)
        for path in paths:
            self.assertIsNotNone(load(path).demo(), path)

    def test_all_three_stages_are_chapter_specific_and_compile(self):
        bodies = set()
        for number in range(201, 226):
            folder = next((ROOT / "excavations").glob(f"{number:03d}-*")) / "implementation"
            for name in ("pure_python.py", "numpy.py", "pytorch.py"):
                text = (folder / name).read_text()
                self.assertIn(f"Excavation {number:03d}", text)
                compile(text, str(folder / name), "exec")
            body = (folder / "pure_python.py").read_text()
            self.assertNotIn(body, bodies, folder)
            bodies.add(body)

    def test_foundation_invariants_survive(self):
        sets = load(ROOT / "excavations/201-sets/implementation/pure_python.py")
        projection = load(ROOT / "excavations/207-orthogonality-projection/implementation/pure_python.py")
        bayes = load(ROOT / "excavations/217-conditional-probability-bayes/implementation/pure_python.py")
        stable = load(ROOT / "excavations/225-numerical-stability/implementation/pure_python.py")
        self.assertEqual(sets.overlap({"tiger", "otter"}, {"tiger", "frog"}), {"tiger"})
        self.assertEqual(projection.project((3, 2), (1, 0)), [3, 0])
        posterior = bayes.bayes({"tiger": .1, "deer": .9}, {"tiger": .8, "deer": .1})
        self.assertAlmostEqual(sum(posterior.values()), 1)
        self.assertTrue(stable.math.isfinite(stable.logsumexp([1000, 999, 998])))


if __name__ == "__main__":
    unittest.main()
