"""Reject displayed mathematics that appears before its explanation."""

from pathlib import Path

root = Path(__file__).parents[1]
heading = "## Why Every Term Must Exist Before the Equation"
example_headings = (
    "## Walk It Once with Concrete Values",
    "## Build the Update from One Real Number",
)
failures = []
checked = 0

for chapter in sorted((root / "excavations").glob("*/README.md")):
    text = chapter.read_text()
    if "$$" not in text:
        continue
    checked += 1
    if heading not in text:
        failures.append(f"{chapter}: missing term-by-term derivation")
    elif text.index(heading) > text.index("$$"):
        failures.append(f"{chapter}: equation appears before its derivation")
    examples = [text.index(item) for item in example_headings if item in text]
    if not examples:
        failures.append(f"{chapter}: missing a concrete worked example")
    elif min(examples) > text.index("$$"):
        failures.append(f"{chapter}: worked example appears after the equation")

if failures:
    raise SystemExit("\n".join(failures))

print(f"Verified {checked} equation-bearing chapters.")
