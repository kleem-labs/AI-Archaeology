"""Guard the reading edition against editorial instructions and private context."""

from pathlib import Path
import re


ROOT = Path(__file__).parents[1]
BOOK = ROOT / "book"
FORBIDDEN = (
    "When the chamber changes",
    "Memory seal",
    "Give the idea a bodily path",
    "Do not take the answer",
    "Keep the formal name",
    "First hold the failed picture",
    "That consequence, not a textbook",
    "does not memorize",
    "Cover the prose",
    "Much later, people will call",
    "Mathematical roots:",
    "Applied territory:",
    "Continue at the dig site",
    "your original excavation",
    "The user's discovery",
    "The user’s discovery",
)


failures = []
volumes = sorted(BOOK.glob("VOLUME_*.md"))
combined = "\n".join(path.read_text() for path in volumes)

for phrase in FORBIDDEN:
    if phrase.lower() in combined.lower():
        failures.append(f"reading edition contains editorial residue: {phrase}")

for number in range(226):
    pattern = rf"^### Excavation {number:03d}\b"
    count = len(re.findall(pattern, combined, flags=re.M))
    if count != 1:
        failures.append(f"Excavation {number:03d} appears {count} times in the six volumes")

if failures:
    raise SystemExit("\n".join(failures))

print("Verified uninterrupted reader-facing prose across all six volumes.")
