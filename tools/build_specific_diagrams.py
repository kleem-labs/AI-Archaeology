"""Replace generic diagrams with the actual argument made by each chapter."""
from pathlib import Path
import re

ROOT = Path(__file__).parents[1]


def compact(value, limit=92):
    value = re.sub(r"[*_`#>]", "", value)
    value = re.sub(r"\s+", " ", value).strip().replace('"', "'")
    if len(value) > limit:
        value = value[:limit].rsplit(" ", 1)[0] + "…"
    return value


starts = (
    "The first solution that suggests itself is this:",
    "A reasonable place to begin is:",
    "Without knowing the inherited method, we might try this:",
    "At first, the simplest answer is tempting:",
    "Our first construction is deliberately modest:",
)
breaks = (
    "The idea survives only until we test it against reality:",
    "Now place that proposal under pressure:",
    "Its hidden assumption appears in the following case:",
    "But the simplicity has discarded something important:",
    "It works—right up to this boundary:",
)
repairs = (
    "The failure gives us a precise requirement:",
    "What broke tells us what the replacement must preserve:",
    "Remove that assumption and the needed repair becomes clear:",
    "The missing information determines the next move:",
    "Crossing that boundary requires one additional idea:",
)

for readme in sorted((ROOT / "excavations").glob("*/README.md")):
    number = int(readme.parent.name[:3])
    text = readme.read_text()
    title = compact(re.search(r"^# (.+)$", text, re.M).group(1), 120)
    if number < 17:
        mistakes = (readme.parent / "mistakes.md").read_text()
        am = re.search(r"^## (Wrong idea[^\n]*)$", mistakes, re.M)
        fm = re.search(r"\*\*Why it fails:\*\*\s*(.+?)(?=\n\n)", mistakes, re.S)
        rm = re.search(r"## Discovery\s*(.+?)(?=\n##|\Z)", mistakes, re.S)
        if not (am and fm and rm):
            continue
        attempt_heading = am.group(1)
        if "—" in attempt_heading:
            attempt_heading = attempt_heading.split("—", 1)[1]
        else:
            attempt_heading = re.sub(r"^Wrong idea\s*\d*\s*[-:]?\s*", "", attempt_heading, flags=re.I)
        attempt, failure, repair = compact(attempt_heading), compact(fm.group(1)), compact(rm.group(1))
    else:
        sm = next((re.search(re.escape(s) + r"\s*(.+?)(?=\n\n)", text, re.S) for s in starts if s in text), None)
        fm = next((re.search(re.escape(s) + r"\s*(.+?)(?=\n\n)", text, re.S) for s in breaks if s in text), None)
        rm = next((re.search(re.escape(s) + r"\s*(.+?)(?=\n\n|\Z)", text, re.S) for s in repairs if s in text), None)
        if not (sm and fm and rm):
            continue
        attempt, failure, repair = compact(sm.group(1)), compact(fm.group(1)), compact(rm.group(1))

    layouts = (
        f'''flowchart LR\n    A["{attempt}"] -->|"test"| B["{failure}"]\n    B -->|"forces"| C["{repair}"]''',
        f'''flowchart TD\n    A["{attempt}"] --> B["Reality: {failure}"]\n    B -. "missing requirement" .-> C["{repair}"]''',
        f'''flowchart LR\n    B["{failure}"] --> A["Reject: {attempt}"]\n    B --> C["Keep: {repair}"]''',
        f'''flowchart TD\n    A["Question"] --> B["Try: {attempt}"]\n    A --> C["Observe: {failure}"]\n    B --> D["Repair: {repair}"]\n    C --> D''',
    )
    visual = layouts[number % len(layouts)]
    diagram = f'''# Diagram — {title}\n\nThe picture carries this excavation's particular counterexample and repair.\n\n```mermaid\n{visual}\n```\n\n```text\nTRY     {attempt}\nBREAK   {failure}\nREPAIR  {repair}\n```\n'''
    (readme.parent / "diagram.md").write_text(diagram)

print("Built chapter-specific diagrams for Excavations 000–150.")
