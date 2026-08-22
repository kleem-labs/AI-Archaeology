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

    def test_published_view_has_individual_chapter_links(self):
        page = (ROOT / "math-mandala" / "index.html").read_text()
        self.assertIn("https://github.com/kleem-labs/AI-Archaeology/blob/main", page)
        self.assertIn("Open excavation", page)
        self.assertIn('openPage(github+"/"+d.path)', page)
        self.assertIn('openPage(github+"/MATHEMATICAL_MOVES.md#"+d.anchor)', page)
        self.assertNotIn("github.com/deep2810", page)

    def test_readme_offers_live_and_script_free_clickable_views(self):
        readme = (ROOT / "README.md").read_text()
        self.assertIn("https://kleem-labs.github.io/AI-Archaeology/", readme)
        self.assertIn(
            "https://raw.githubusercontent.com/kleem-labs/AI-Archaeology/main/"
            "math-mandala/math-mandala.svg",
            readme,
        )


if __name__ == "__main__":
    unittest.main()
