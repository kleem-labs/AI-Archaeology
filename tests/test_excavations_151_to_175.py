"""Executable checks for the measured engine rebuilt in Part XII."""
from pathlib import Path
import importlib.util
import unittest


ROOT = Path(__file__).parents[1]


def load(path):
    spec = importlib.util.spec_from_file_location(path.parents[1].name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PartXIITests(unittest.TestCase):
    def test_every_pure_python_excavation_runs_its_evidence(self):
        paths = sorted((ROOT / "excavations").glob("1[5-7][0-9]-*/implementation/pure_python.py"))
        paths = [path for path in paths if 151 <= int(path.parents[1].name[:3]) <= 175]
        self.assertEqual(len(paths), 25)
        for path in paths:
            result = load(path).demo()
            self.assertIsInstance(result, dict, path)
            self.assertTrue(result, path)

    def test_optimizations_preserve_the_claim_they_make(self):
        rope = load(ROOT / "excavations/155-rotary-position/implementation/pure_python.py")
        cache = load(ROOT / "excavations/157-kv-cache/implementation/pure_python.py")
        flash = load(ROOT / "excavations/160-flash-attention/implementation/pure_python.py")
        clip = load(ROOT / "excavations/167-gradient-clipping/implementation/pure_python.py")
        tensor = load(ROOT / "excavations/173-tensor-parallelism/implementation/pure_python.py")

        self.assertAlmostEqual(sum(v * v for v in rope.rotate([3, 4], .7)), 25)
        self.assertEqual(cache.projection_counts(100), {"without_cache": 5050, "with_cache": 100})
        self.assertAlmostEqual(flash.online_softmax([1, 2, 3, 4]), 2.4926527345857696)
        self.assertEqual(clip.clip([12, 16], 5), [3, 4])

        x = [2, 3]
        weights = [[1, 0, 2, 0], [0, 1, 0, 2]]
        joined = sum((tensor.matmul(x, block) for block in tensor.split_columns(weights, 2)), [])
        self.assertEqual(joined, tensor.matmul(x, weights))

    def test_all_three_stages_are_chapter_specific(self):
        for number in range(151, 176):
            folder = next((ROOT / "excavations").glob(f"{number:03d}-*")) / "implementation"
            for name in ("pure_python.py", "numpy.py", "pytorch.py"):
                text = (folder / name).read_text()
                self.assertNotIn("def compare(reference, repaired)", text)
                compile(text, str(folder / name), "exec")


if __name__ == "__main__":
    unittest.main()
