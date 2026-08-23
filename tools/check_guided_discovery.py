"""Protect reader-led prose without preserving the old lesson template."""
from pathlib import Path
from rebuild_narrative_continuity import CARRY

root = Path(__file__).parents[1]
banned = (
    "Pause here. You do not know the accepted method yet.",
    "It sounds reasonable. Now make it face the smallest case that refuses to cooperate.",
    "Do not reach for terminology. Say—in ordinary language—",
    "Before inheriting a technique, make the first decision yourself.",
    "Do not reject your idea because the book says it is wrong.",
    "## Let the case decide",
    "## Let one run decide",
    "## Enter the laboratory",
    "## The arithmetic we have earned",
    "### Only now do the symbols earn names",
    "### Why these operations are forced",
)
failures = []

for chapter in sorted((root / "excavations").glob("*/README.md")):
    text = chapter.read_text()
    number = int(chapter.parent.name[:3])
    for phrase in banned:
        if phrase in text:
            failures.append(f"{chapter}: contains template coaching prose: {phrase}")
    if number >= 17 and CARRY[number] not in text:
        failures.append(f"{chapter}: does not carry forward the preceding discovery")
    if number >= 17 and "<!-- book-prose-v2 -->" not in text:
        failures.append(f"{chapter}: has not passed the continuous-prose editorial migration")
    if number >= 17 and "repair" not in text.lower():
        failures.append(f"{chapter}: never tests or names the repaired responsibility")
    if "The repair is explicit:" in text or "What information did the attempt lose?" in text:
        failures.append(f"{chapter}: exposes editorial scaffolding to the reader")

if failures:
    raise SystemExit("\n".join(failures))

print("Verified narrative discovery flow without template coaching prose.")
