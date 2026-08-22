"""The mathematical mandala must remain a complete view of earned notation."""
from pathlib import Path
import importlib.util
import json
import re
import unittest


ROOT = Path(__file__).parents[1]


def load_builder():
    path = ROOT / "tools" / "build_math_mandala.py"
    spec = importlib.util.spec_from_file_location("build_math_mandala", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class MathematicalMandalaTests(unittest.TestCase):
    def test_every_displayed_equation_is_a_node(self):
        builder = load_builder()
        data = builder.collect()
        expected = 0
        for path in (ROOT / "excavations").glob("*/README.md"):
            expected += len(re.findall(r"\$\$(.*?)\$\$", path.read_text(), re.S))
        self.assertEqual(len(data["equations"]), expected)
        self.assertEqual(len({node["id"] for node in data["equations"]}), expected)

    def test_links_and_generated_data_are_valid(self):
        data = json.loads((ROOT / "math-mandala" / "data.json").read_text())
        for node in data["equations"]:
            self.assertTrue((ROOT / node["path"]).exists(), node["path"])
        move_source = (ROOT / "MATHEMATICAL_MOVES.md").read_text()
        for move in data["operations"]:
            self.assertIn(f'<a id="{move["anchor"]}"></a>', move_source)


if __name__ == "__main__":
    unittest.main()
