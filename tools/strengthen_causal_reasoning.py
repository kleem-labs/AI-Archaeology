"""Repair misplaced limitations and explain terse boundaries from mechanism."""
from pathlib import Path
import re

ROOT = Path(__file__).parents[1]
attempts = (
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
    "The cost of that attempt points to the missing operation:",
)
explanations = (
    "The boundary follows from the mechanism itself. We designed it to {repair} That operation solves the failure we had reached, but it contains no step that answers the additional problem above.",
    "The repair is explicit: {repair_lower} Its power is also its boundary; anything not represented in those operations remains undecided.",
    "This is not an unrelated warning. The construction can {repair_lower} It cannot infer or control information that never enters that construction.",
    "The reason is visible in the procedure. It knows how to {repair_lower} The limitation above asks for another judgment, and no part of the procedure makes that judgment.",
    "Why does the boundary remain? Our new machinery only knows how to {repair_lower} Solving that problem does not automatically solve every decision built on top of it.",
)


def compact(value):
    return re.sub(r"\s+", " ", value).strip()


for path in sorted((ROOT / "excavations").glob("*/README.md")):
    number = int(path.parent.name[:3])
    text = path.read_text()
    text = text.replace("Look back at what the repair actually does: it ", "The repair is explicit: ")
    # Imperative repair sentences were sometimes inserted after infinitives
    # with their original capital letter. Lowercase only that first word.
    text = re.sub(r"(We designed it to )([A-Z])", lambda m: m.group(1) + m.group(2).lower(), text)
    text = re.sub(r"(only knows how to )([A-Z])", lambda m: m.group(1) + m.group(2).lower(), text)

    # In 017–045 the old migration inserted the completed method's later limit
    # where the naive counterexample belonged. The attempted paragraph already
    # states its concrete failure, so remove the false causal bridge.
    if 17 <= number <= 45:
        text = text.replace("Crossing that boundary requires one additional idea:", "The cost of that attempt points to the missing operation:")
        text = text.replace("## Why It Still Fails", "## From procedure to notation")
        text = text.replace("\n## Compress your discovery into mathematics\n", "\n")
        text = text.replace("## Why It Still Fails\n\nThe verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.\n\n## Compress your discovery into mathematics\n\n\n", "## From procedure to notation\n\nThe procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.\n\n")
        repair_positions = [(text.find(marker), marker) for marker in repairs if marker in text]
        break_positions = [(text.find(marker), marker) for marker in breaks if marker in text]
        if repair_positions and break_positions:
            bpos, _ = min(break_positions)
            rpos, _ = min(repair_positions)
            if bpos < rpos:
                text = text[:bpos].rstrip() + "\n\n" + text[rpos:]

    if number == 24:
        old = "Backpropagation computes gradients; it does not choose the update size or guarantee a good minimum."
        new = ("Backpropagation returns a local sensitivity for each weight: which infinitesimal direction would raise the loss, and how strongly. "
               "That information contains no instruction saying whether to take the whole suggested movement, one tenth of it, or one thousandth; choosing that fraction is a separate optimization decision. "
               "Nor does a local slope reveal the entire loss landscape. A downward direction from the present point cannot prove that a deeper valley does not exist elsewhere, so backpropagation alone cannot guarantee the best minimum.")
        text = text.replace(old, new)

    # Find the chapter's actual repair, which supplies the causal scope needed
    # to explain why a later limitation remains.
    repair = ""
    for marker in repairs:
        match = re.search(re.escape(marker) + r"\s*(.+?)(?=\n\n)", text, re.S)
        if match:
            repair = compact(match.group(1))
            break
    if not repair:
        path.write_text(text)
        continue

    section = re.search(r"(^## (?:Limits|Where [^\n]*breaks)\n+)(.*?)(?=^## |\Z)", text, re.M | re.S)
    if section and number != 24:
        body = section.group(2).strip()
        sentence_count = len(re.findall(r"[.!?](?:\s|$)", body))
        causal = re.search(r"\b(because|since|this follows|the reason|only knows|contains no|never)\b", body, re.I)
        if sentence_count < 3 or not causal:
            short_repair = repair[:260].rstrip()
            if len(repair) > 260:
                short_repair = short_repair.rsplit(" ", 1)[0] + "."
            if not short_repair.endswith((".", "!", "?")):
                short_repair += "."
            repair_lower = short_repair[0].lower() + short_repair[1:]
            why = explanations[number % len(explanations)].format(repair=short_repair, repair_lower=repair_lower)
            # Remove the old generic bridge used by Part XI before adding the
            # mechanism-specific explanation.
            body = body.replace("\n\nThat limit is not a footnote. It is the pressure that forces the next excavation.", "")
            replacement = section.group(1) + body.rstrip() + "\n\n" + why + "\n\n"
            text = text[:section.start()] + replacement + text[section.end():]

    # Idempotence: an editorial tool must not duplicate prose when rerun.
    paragraphs = text.split("\n\n")
    deduplicated = []
    for paragraph in paragraphs:
        if not deduplicated or paragraph.strip() != deduplicated[-1].strip():
            deduplicated.append(paragraph)
    path.write_text("\n\n".join(deduplicated))

print("Strengthened causal reasoning and repaired Excavations 017–045 ordering.")
