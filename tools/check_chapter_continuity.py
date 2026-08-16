"""Reject chapter boundaries that behave like an unrelated syllabus."""
from pathlib import Path
import re

from rebuild_narrative_continuity import CARRY

ROOT = Path(__file__).parents[1]
failures = []
chapters = sorted((ROOT / "excavations").glob("*/README.md"))

if len(chapters) != 201:
    failures.append(f"expected Excavations 000–200, found {len(chapters)}")

for path in chapters:
    number = int(path.parent.name[:3])
    text = path.read_text()
    first_section = text.find("\n## ")
    opening = text[:first_section] if first_section >= 0 else text
    if re.search(r"^\[Previous", opening, re.M):
        failures.append(f"{path}: file navigation interrupts the opening scene")
    if number >= 17 and CARRY.get(number) not in opening:
        failures.append(f"{path}: opening does not inherit the previous capability")
    for phrase in (
        "What information did the attempt lose?",
        "Name the missing guarantee before continuing.",
        "The repair is explicit:",
        "Solving that problem does not automatically solve",
        "The boundary follows from the mechanism itself.",
    ):
        if phrase in text:
            failures.append(f"{path}: exposes authoring scaffold: {phrase}")

if failures:
    raise SystemExit("\n".join(failures))

print("Verified one causal opening chain across Excavations 000–200.")
