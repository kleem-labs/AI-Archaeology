"""Reject the measurable fingerprints of catalogue notes and lesson templates."""

from collections import Counter
from pathlib import Path
import re


ROOT = Path(__file__).parents[1]
chapters = sorted((ROOT / "excavations").glob("*/README.md"))
failures = []

banned_headings = (
    "## Problem",
    "## Naive Attempt",
    "## Why It Fails",
    "## Better Attempt",
    "## Key Insight",
    "## Mathematics Emerges",
    "## Let the case decide",
    "## Let one run decide",
    "## Enter the laboratory",
    "## Continue the dig",
    "## The arithmetic we have earned",
)

paragraph_owners = {}
for chapter in chapters:
    text = chapter.read_text()
    number = int(chapter.parent.name[:3])
    words = len(re.findall(r"\b[\w’-]+\b", text))
    minimum = 500 if number >= 17 else 430
    if words < minimum:
        failures.append(f"{chapter}: only {words} words; the causal case is underdeveloped")
    for heading in banned_headings:
        if heading in text:
            failures.append(f"{chapter}: exposes catalogue heading {heading}")
    for paragraph in re.split(r"\n\n+", text):
        normalized = re.sub(r"\s+", " ", paragraph).strip()
        if (
            len(normalized.split()) >= 16
            and "(mistakes.md)" not in normalized
            and not normalized.startswith(("#", "-", "[", "<!--", ">"))
        ):
            paragraph_owners.setdefault(normalized, []).append(chapter)

for paragraph, owners in paragraph_owners.items():
    if len(owners) > 3:
        failures.append(
            f"repeated prose paragraph appears in {len(owners)} chapters: {paragraph[:100]}..."
        )

if failures:
    raise SystemExit("\n".join(failures))

print(f"Verified book-like prose depth and non-template rhythm across {len(chapters)} chapters.")
