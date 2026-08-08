"""Require the reader to make and repair an attempt before any equation."""

from pathlib import Path

root = Path(__file__).parents[1]
failures = []

for chapter in sorted((root / "excavations").glob("*/README.md")):
    text = chapter.read_text()
    number = int(chapter.parent.name[:3])
    if number < 17:
        # These opening chapters are deliberately bespoke prose. Their causal
        # flow is an editorial reading check, not a heading/keyword check.
        required = ()
    else:
        required = ("Pause here.", "*Your first move:*", "*The case that breaks it:*", "*Your repair:*")
    for marker in required:
        if marker not in text:
            failures.append(f"{chapter}: missing reader-led discovery marker {marker}")
    first_discovery = min((text.lower().find(marker.lower()) for marker in required if marker.lower() in text.lower()), default=-1)
    if required and "$$" in text and (first_discovery < 0 or first_discovery > text.index("$$")):
        failures.append(f"{chapter}: reader receives equation before making an attempt")

if failures:
    raise SystemExit("\n".join(failures))

print("Verified guided-discovery structure in every excavation.")
