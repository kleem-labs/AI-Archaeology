"""Remove duplicated coaching cards from the bespoke opening excavations."""
from pathlib import Path
import re

ROOT = Path(__file__).parents[1]
pattern = re.compile(r"\n## Take the First Step Yourself\n.*?(?=\n(?!(?:>.*|\s*)$))", re.S | re.M)

for path in sorted((ROOT / "excavations").glob("0??-*/README.md")):
    number = int(path.parent.name[:3])
    if number >= 17 or number == 7:
        continue
    text = path.read_text()
    start = text.find("\n## Take the First Step Yourself\n")
    if start < 0:
        continue
    tail = text[start + 1:].splitlines()
    end_line = None
    for index in range(1, len(tail)):
        line = tail[index]
        if line and not line.startswith(">") and index > 1:
            end_line = index
            break
    if end_line is None:
        continue
    replacement_tail = "\n".join(tail[end_line:])
    path.write_text(text[:start].rstrip() + "\n\n" + replacement_tail.lstrip() + "\n")

print("Removed duplicated coaching cards from Excavations 000–016.")
