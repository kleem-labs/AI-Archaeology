"""Turn scaffolded attempt/failure/repair cards into continuous book prose.

This is intentionally a one-time editorial migration. It removes instructions
addressed to an author and preserves the chapter-specific intellectual content.
"""
from pathlib import Path
import re

ROOT = Path(__file__).parents[1]


def compact(text):
    text = re.sub(r"\n> ?", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def mistake_problem(folder):
    path = folder / "mistakes.md"
    if not path.exists():
        return ""
    text = path.read_text()
    match = re.search(r"\*\*Problem:\*\*\s*(.+?)(?=\n##|\Z)", text, re.S)
    return compact(match.group(1)) if match else ""


transitions = (
    ("The first solution that suggests itself is this:", "The idea survives only until we test it against reality:", "The failure gives us a precise requirement:"),
    ("A reasonable place to begin is:", "Now place that proposal under pressure:", "What broke tells us what the replacement must preserve:"),
    ("Without knowing the inherited method, we might try this:", "Its hidden assumption appears in the following case:", "Remove that assumption and the needed repair becomes clear:"),
    ("At first, the simplest answer is tempting:", "But the simplicity has discarded something important:", "The missing information determines the next move:"),
    ("Our first construction is deliberately modest:", "It works—right up to this boundary:", "Crossing that boundary requires one additional idea:"),
)

for path in sorted((ROOT / "excavations").glob("*/README.md")):
    number = int(path.parent.name[:3])
    if number < 17:
        continue
    text = path.read_text()
    a, f, r = transitions[number % len(transitions)]

    if "Pause here. You do not know the accepted method yet." in text:
        attempt_m = re.search(r"\*Your first move:\*\s*(.+?)\n\nIt sounds reasonable", text, re.S)
        failure_m = re.search(r"\*The case that breaks it:\*\s*(.+?)\n\nDo not reach for terminology", text, re.S)
        repair_m = re.search(r"\*Your repair:\*\s*(.+?)\n\nOnly after that reasoning may we give your discovery its inherited name\.", text, re.S)
        if not (attempt_m and failure_m and repair_m):
            continue
        attempt, failure, repair = map(lambda m: compact(m.group(1)), (attempt_m, failure_m, repair_m))
        if failure.startswith("Do not reject your idea because the book says it is wrong"):
            failure = mistake_problem(path.parent) or attempt
        replacement = f"{a} {attempt}\n\n{f} {failure}\n\n{r} {repair}"
        start = text.index("Pause here. You do not know the accepted method yet.")
        end_marker = "Only after that reasoning may we give your discovery its inherited name."
        end = text.index(end_marker, start) + len(end_marker)
        text = text[:start] + replacement + text[end:]

    elif "Before inheriting a technique, make the first decision yourself." in text:
        pattern = re.compile(
            r"Before inheriting a technique, make the first decision yourself\. (.+?)\n\n"
            r"For a moment, the idea appears sufficient\. Then reality supplies the case it cannot explain: (.+?)\n\n"
            r"The failure tells you what the repair must accomplish\. (.+?)\n\n"
            r"Only now have you earned the chapter's name: \*\*(.+?)\*\*\.", re.S)
        match = pattern.search(text)
        if not match:
            continue
        attempt, failure, repair, name = map(compact, match.groups())
        replacement = f"{a} {attempt}\n\n{f} {failure}\n\n{r} {repair}\n\nOnly here do we name the idea: **{name}**."
        text = text[:match.start()] + replacement + text[match.end():]

    path.write_text(text)

print("Removed template coaching voice from Excavations 017–150.")
