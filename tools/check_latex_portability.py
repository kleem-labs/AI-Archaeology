"""Reject LaTeX commands unsupported by the book's Markdown renderer."""
from pathlib import Path

root = Path(__file__).parents[1]
banned = (r"\operatorname", r"\operatorname*", r"\,", r"\;", r"\!", r"\qquad")
failures = []

for path in root.rglob("*.md"):
    text = path.read_text()
    for command in banned:
        if command in text:
            failures.append(f"{path}: unsupported LaTeX command {command}")

if failures:
    raise SystemExit("\n".join(failures))

print("Verified portable LaTeX commands in every Markdown file.")
