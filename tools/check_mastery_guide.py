"""Keep one visible, complete mastery path across every reader entry point."""

from pathlib import Path


ROOT = Path(__file__).parents[1]
guide = ROOT / "HOW_TO_MASTER_THIS_BOOK.md"
ledger = ROOT / "MASTERY_LEDGER.md"
failures = []

required_sections = (
    "## The three passages through the book",
    "## The chapter ritual",
    "## The mastery ladder",
    "## The recall rhythm",
    "## When to leave a chapter",
    "## Checkpoints at the end of a part",
    "## Choose a sustainable pace",
    "## If you become stuck",
    "## The final test",
)

if not guide.exists() or not ledger.exists():
    failures.append("the mastery guide or ledger is missing")
else:
    text = guide.read_text()
    for section in required_sections:
        if section not in text:
            failures.append(f"mastery guide lost {section}")
    for level in range(6):
        if f"| {level}" not in text:
            failures.append(f"mastery guide lost level {level}")
    if ledger.read_text().count("| XIV —") != 1:
        failures.append("mastery ledger no longer spans all fourteen parts")

entry_points = (
    "README.md",
    "PARTS.md",
    "book/README.md",
    "LABORATORY.md",
    "MEMORY_PALACE.md",
    "memory-palace/README.md",
    "math-mandala/README.md",
    "MATHEMATICS_ATLAS.md",
    "MATHEMATICAL_GIST.md",
    "MATHEMATICAL_MOVES.md",
    "MATHEMATICAL_ROOTS.md",
    "mathematical-roots/README.md",
)
for name in entry_points:
    path = ROOT / name
    if "HOW_TO_MASTER_THIS_BOOK.md" not in path.read_text():
        failures.append(f"{name}: reader can no longer reach the mastery guide")

if failures:
    raise SystemExit("\n".join(failures))

print("Mastery path is complete and visible from 12 reader entry points.")
