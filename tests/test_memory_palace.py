"""Behavior checks for the complete 226-chamber memory palace."""

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).parents[1]


class CompleteMemoryPalaceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "memory-palace" / "data.json").read_text())
        cls.films = [film for realm in cls.data["realms"] for film in realm["roots"]]

    def test_every_excavation_has_one_reachable_chamber(self):
        self.assertEqual(len(self.data["realms"]), 18)
        self.assertEqual([film["number"] for film in self.films], list(range(226)))
        for film in self.films:
            self.assertTrue((ROOT / "memory-palace" / film["path"]).resolve().exists())

    def test_every_film_has_five_recoverable_frames(self):
        for film in self.films:
            for field in ("question", "object", "failure_image", "transformation", "sentence"):
                self.assertTrue(film[field].strip(), (film["number"], field))
        self.assertEqual(len({film["object"] for film in self.films}), 226)
        self.assertEqual(len({film["sentence"] for film in self.films}), 226)

    def test_palace_exposes_navigation_and_chapter_doors(self):
        html = (ROOT / "memory-palace" / "index.html").read_text()
        self.assertIn("The 226-Chamber Memory Palace", html)
        self.assertIn("Open the complete excavation", html)
        self.assertIn("Eighteen memory realms", html)


if __name__ == "__main__":
    unittest.main()
