"""Reject displayed mathematics that appears before its explanation."""

from pathlib import Path

root = Path(__file__).parents[1]
derivation_headings = (
    "## Build Every Piece from the Concrete Example",
    "## Build each piece from what just happened",
)
failures = []
checked = 0

for chapter in sorted((root / "excavations").glob("*/README.md")):
    text = chapter.read_text()
    if "$$" not in text:
        continue
    checked += 1
    derivations = [text.index(item) for item in derivation_headings if item in text]
    if not derivations:
        failures.append(f"{chapter}: missing term-by-term derivation")
    elif min(derivations) > text.index("$$"):
        failures.append(f"{chapter}: equation appears before its derivation")
    if derivations and min(derivations) > text.index("$$"):
        failures.append(f"{chapter}: worked example appears after the equation")

if failures:
    raise SystemExit("\n".join(failures))

print(f"Verified {checked} equation-bearing chapters.")
