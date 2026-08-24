"""Behavior checks for the living Mathematical Roots Undercroft."""

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).parents[1]


class MathematicalRootsMemoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(
            (ROOT / "mathematical-roots" / "data.json").read_text()
        )
        cls.roots = [
            root
            for realm in cls.data["realms"]
            for root in realm["roots"]
        ]

    def test_every_root_is_reachable_from_the_palace(self):
        self.assertEqual(len(self.data["realms"]), 5)
        self.assertEqual([root["number"] for root in self.roots], list(range(201, 226)))
        for root in self.roots:
            destination = (ROOT / "mathematical-roots" / root["path"]).resolve()
            self.assertTrue(destination.exists(), destination)

    def test_every_chamber_has_a_distinct_object_and_seal(self):
        self.assertEqual(len({root["object"] for root in self.roots}), 25)
        self.assertEqual(len({root["sentence"] for root in self.roots}), 25)
        for root in self.roots:
            for key in (
                "question",
                "object",
                "failure_image",
                "transformation",
                "sentence",
                "gesture",
            ):
                self.assertTrue(root[key].strip(), (root["number"], key))

    def test_interface_preserves_the_five_frame_journey(self):
        html = (ROOT / "mathematical-roots" / "index.html").read_text()
        for label in ("Question", "Object", "Failure", "Transformation", "Memory seal"):
            self.assertIn(label, html)
        self.assertIn("Open the complete excavation", html)


if __name__ == "__main__":
    unittest.main()
