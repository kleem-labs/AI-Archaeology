"""Remove the repeated course-template opening from Excavations 017–125.

The source material is preserved, but the reader now moves through one scene:
observation -> personal proposal -> counterexample -> requirement -> name.
"""
from pathlib import Path
import re

ROOT = Path(__file__).parents[1]

SECTION = re.compile(r"^## (.+?)\n(.*?)(?=^## |\Z)", re.M | re.S)


def body(sections, name):
    return sections.get(name, "").strip()


def unquote(text):
    lines = []
    for line in text.splitlines():
        line = re.sub(r"^> ?", "", line)
        line = re.sub(r"^\*\*(?:Your problem|Try your first idea|Now try to break your idea):\*\* ?", "", line)
        lines.append(line)
    return "\n".join(lines).strip()


for path in sorted((ROOT / "excavations").glob("*/README.md")):
    number = int(path.parent.name[:3])
    if number < 17:
        continue

    text = path.read_text()
    matches = list(SECTION.finditer(text))
    sections = {match.group(1): match.group(2) for match in matches}
    observation_name = "The Observation" if "The Observation" in sections else "Problem"
    needed = (observation_name, "Your First Attempt", "Break Your First Attempt", "Repair Your Attempt")
    if not all(name in sections for name in needed):
        continue

    first = matches[0].start()
    prefix = text[:first].rstrip()
    # Remove the duplicated coaching box. Its actual ideas are reconstructed
    # below as a continuous encounter, not discarded.
    observation = body(sections, observation_name)
    attempt = body(sections, "Your First Attempt")
    failure = body(sections, "Break Your First Attempt")
    repair = body(sections, "Repair Your Attempt")
    invention = body(sections, "What You Have Just Invented")

    opening = f"""

{observation}

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* {attempt}

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* {failure}

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* {repair}
""".rstrip()

    if invention:
        cleaned = invention.strip()
        if cleaned.strip("* ") != repair.strip("* "):
            opening += f"\n\nOnly after that reasoning may we give your discovery its inherited name.\n\n{cleaned}"
        else:
            opening += "\n\nOnly after that reasoning may we give your discovery its inherited name."

    consumed = {
        "Take the First Step Yourself", observation_name, "Your First Attempt",
        "Break Your First Attempt", "Repair Your Attempt", "What You Have Just Invented",
    }
    remainder = []
    replacements = {
        "Rebuild the Discovery with a Concrete Case": "Now work a case you can see",
        "Build Every Piece from the Concrete Example": "Build each piece from what just happened",
        "Only Now Give the Discovery a Mathematical Name": "Compress your discovery into mathematics",
        "Real-World Limit": "Where your new idea still breaks",
        "Real-World Analogy": "Carry the idea back into the world",
        "Implementation": "Enter the laboratory",
        "Exercises and Connections": "Carry the discovery forward",
        "Exercises": "Test what you believe",
        "Connections": "What this discovery now makes possible",
    }
    for match in matches:
        name, content = match.group(1), match.group(2).rstrip()
        if name in consumed:
            continue
        remainder.append(f"## {replacements.get(name, name)}\n{content}")

    new_text = prefix + opening + "\n\n" + "\n\n".join(remainder).rstrip() + "\n"
    path.write_text(new_text)

print("Editorialized Excavations 017–125 into continuous reader-led scenes.")
