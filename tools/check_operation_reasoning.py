"""Ensure every displayed equation earns and links its mathematical moves."""
from pathlib import Path
import re

ROOT = Path(__file__).parents[1]
GUIDE = ROOT / "MATHEMATICAL_MOVES.md"
guide = GUIDE.read_text()
anchors = set(re.findall(r'<a id="([^"]+)"></a>', guide))
failures = []
equation_numbers = set()

for path in sorted((ROOT / "excavations").glob("*/README.md")):
    text = path.read_text()
    if "$$" not in text:
        continue
    number = int(path.parent.name[:3])
    equation_numbers.add(number)
    heading = "### Why no cheaper operation does the same job"
    if text.count(heading) != 1:
        failures.append(f"{path}: expected exactly one operation-reasoning section")
        continue
    if text.index(heading) > text.index("$$"):
        failures.append(f"{path}: operations are justified only after the equation")
    section = text[text.index(heading):text.index("$$")]
    linked = set(re.findall(r'MATHEMATICAL_MOVES\.md#([a-z-]+)', section))
    if not linked:
        failures.append(f"{path}: operation explanations do not link to the reusable guide")
    for anchor in linked:
        if anchor not in anchors:
            failures.append(f"{path}: links to missing Mathematical Moves anchor #{anchor}")
    alternatives = re.search(
        r"\b(?:would|without|rather than|instead|not |because|forced|omitted|removing|different|"
        r"prevent(?:s|ing|ed)?|but|cannot|avoids?)\b",
        section,
        re.I,
    )
    if not alternatives:
        failures.append(f"{path}: explains names but not why an alternative operation fails")

if failures:
    raise SystemExit("\n".join(failures))

print(f"Verified contextual operation choices and reusable links in {len(equation_numbers)} equation-bearing chapters.")
