"""Require a lived or named domain example before displayed mathematics."""
from pathlib import Path
import re

root = Path(__file__).parents[1]
named_objects = re.compile(
    r"\b(tiger|animal|ranger|tracker|village|camp|coin|bag|message|word|token|"
    r"sentence|model|alarm|detector|photograph|image|microphone|map|cartographer|"
    r"librarian|book|oven|bread|dough|robot|hiker|policy|caption|clinic|patient|"
    r"cave|sensor|device|weight|dataset|prediction|story|event|language|text|"
    r"examples?|future|training|river|node|tree|hospital|router|words?|tokens?|"
    r"predictions?|models?)\b", re.I)
banned_openings = (
    "Three examples propose gradients [",
    "Let q=[",
    "Suppose one head returns [",
    "Let the first map turn [",
    "A layer receives [",
    "Successive gradients are [",
)
failures = []

for path in sorted((root / "excavations").glob("*/README.md")):
    text = path.read_text()
    if "$$" not in text:
        continue
    before_equation = text[:text.index("$$")]
    section = before_equation[before_equation.rfind("\n## "):]
    if not named_objects.search(section):
        failures.append(f"{path}: equation is not preceded by a named human or domain example")
    for phrase in banned_openings:
        if phrase in section:
            failures.append(f"{path}: anonymous-number derivation remains: {phrase}")

if failures:
    raise SystemExit("\n".join(failures))

print("Verified human-readable derivations before every displayed equation.")
