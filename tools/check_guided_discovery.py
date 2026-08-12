"""Protect reader-led prose without forcing a repeated lesson template."""
from pathlib import Path
from rebuild_narrative_continuity import ATTEMPT_LEADS, CARRY

root = Path(__file__).parents[1]
banned = (
    "Pause here. You do not know the accepted method yet.",
    "It sounds reasonable. Now make it face the smallest case that refuses to cooperate.",
    "Do not reach for terminology. Say—in ordinary language—",
    "Before inheriting a technique, make the first decision yourself.",
    "Do not reject your idea because the book says it is wrong.",
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
    if number >= 17 and not any(opening in text for opening in ATTEMPT_LEADS):
        failures.append(f"{chapter}: attempted idea is not integrated into narrative prose")
    if "The repair is explicit:" in text or "What information did the attempt lose?" in text:
        failures.append(f"{chapter}: exposes editorial scaffolding to the reader")

if failures:
    raise SystemExit("\n".join(failures))

print("Verified narrative discovery flow without template coaching prose.")
