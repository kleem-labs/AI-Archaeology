"""Require the reader to make and repair an attempt before any equation."""

from pathlib import Path

root = Path(__file__).parents[1]
required = (
    "## Take the First Step Yourself",
    "**Your problem:**",
    "**Try your first idea:**",
    "**Now try to break your idea:**",
    "Stop here.",
)
failures = []

for chapter in sorted((root / "excavations").glob("*/README.md")):
    text = chapter.read_text()
    for marker in required:
        if marker not in text:
            failures.append(f"{chapter}: missing {marker}")
    if "$$" in text and text.index("## Take the First Step Yourself") > text.index("$$"):
        failures.append(f"{chapter}: reader receives equation before making an attempt")

if failures:
    raise SystemExit("\n".join(failures))

print("Verified guided-discovery structure in every excavation.")
