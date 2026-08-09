"""Report whether the repository meets the book-and-laboratory completion gate."""
from pathlib import Path

root = Path(__file__).parents[1]
chapters = sorted((root / "excavations").glob("*/README.md"))
required = ("diagram.md", "exercises.md", "mistakes.md", "references.md")
failures = []

for chapter in chapters:
    folder = chapter.parent
    number = int(folder.name[:3])
    for name in required:
        if not (folder / name).exists():
            failures.append(f"{folder}: missing {name}")
    text = chapter.read_text()
    invites_reader = (
        number < 17
        or
        "## Take the First Step Yourself" in text
        or ("Pause here." in text and "*Your first move:*" in text)
        or ("Suppose your first idea" in text and "What would a useful space have to do?" in text)
        or ("attempt" in text.lower() and "fail" in text.lower())
        or "Before inheriting a technique, make the first decision yourself." in text
    )
    if not invites_reader:
        failures.append(f"{chapter}: reader is not asked to propose the first move")

    # Concrete grounding is semantic: a word search cannot tell whether an
    # example lets a reader discover the idea. BOOK_AND_LAB_STANDARD.md keeps
    # that as an explicit human editorial gate instead of manufacturing a pass.

labs = sorted((root / "labs").glob("[0-9][0-9]_*.py"))
if len(labs) < 5:
    failures.append("laboratory: fewer than five runnable field labs")

if failures:
    raise SystemExit("\n".join(failures))

print(f"Book structure: {len(chapters)} chapters.")
print(f"Runnable field labs: {len(labs)}.")
print("Structural book/lab gate passed; manual depth review remains required.")
