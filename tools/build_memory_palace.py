"""Give every excavation a concrete five-frame memory film and one connected palace."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from build_excavations_201_225 import REALMS as ROOT_REALMS
from build_excavations_201_225 import ROOT_MEMORY
from build_mathematical_roots_palace import html_page
from deepen_chapter_prose import title_parts
from rebuild_narrative_continuity import CARRY
from weave_mathematical_world import BREAKS, REVEALS, SCENES, WORLDS, world_for


ROOT = Path(__file__).parents[1]
OUTPUT = ROOT / "memory-palace"
NARRATIVE_SOURCE = OUTPUT / "narrative_sources.json"
START = "<!-- memory-film-v1:start -->"
END = "<!-- memory-film-v1:end -->"


FOUNDATION_MEMORY = {
0: ("How can one observation survive after every witness has gone?", "a fresh tiger track beside the tribe's first charcoal mark", "Wind softens the track while two witnesses remember different animals.", "A hand traces the track into clay; the animal can leave, but the shared mark remains.", "Mathematics begins when an observation receives a form that can outlive its observer.", "Press one finger into your palm, then lift it while imagining the mark remaining."),
1: ("Which parts of an animal must we preserve to judge whether it threatens the camp?", "five carved tiger tokens: weight, speed, teeth, stripes, and direction", "A zebra passes the stripe test, while a three-legged tiger fails the four-leg test.", "The tokens separate, and only observations relevant to the danger decision remain on the table.", "A feature is a chosen observation that preserves a distinction needed by a question.", "Touch five fingertips in turn, naming one observable property with each touch."),
2: ("How can many comparable features travel as one object without losing which is which?", "an ordered leather satchel with one pocket for each tiger feature", "Loose measurement stones spill together; weight can no longer be distinguished from speed.", "The stones slide into named pockets whose order remains fixed for every animal.", "A vector lets several measurements travel together while their positions preserve meaning.", "Sweep scattered fingers together, then hold them in a fixed row."),
3: ("How can the tribe turn many feature disagreements into one honest separation?", "two tiger silhouettes joined by feature-length measuring cords", "Positive and negative disagreements pull opposite ways and cancel, making different animals appear identical.", "Every cord's disagreement becomes nonnegative before the cords combine into one path between the animals.", "Distance is the single separation left after every comparable disagreement has been allowed to count.", "Stretch both hands apart, briefly cross them to show cancellation, then separate them again."),
4: ("How can a vector describe not only what exists, but what changed?", "an arrow laid from yesterday's tiger position to today's", "Two isolated position stones reveal locations but hide the movement connecting them.", "The stones remain while a directed arrow grows from the earlier position to the later one.", "A change vector remembers both how far the world moved and in which direction.", "Point to one place, then sweep the same finger toward a second place."),
5: ("How can many output judgments reuse the same collection of input features?", "a brass grid whose rows are judges and columns are tiger features", "Separate handwritten rules repeatedly fetch the same features and silently change their ordering.", "The rules lock into one grid; each row combines the same ordered input into one named output.", "A matrix is a reusable arrangement of transformations that lets inputs interact consistently.", "Hold one hand as vertical rows and cross it with the other as horizontal columns."),
6: ("If a dictionary cannot contain every use of a word, where does meaning come from?", "the word tiger suspended in a web of neighboring word-threads", "Cutting tiger from its sentences leaves a label whose living uses have disappeared.", "Threads reconnect it to hunt, stripes, jungle, fear, and many contrasting contexts.", "Meaning is not hidden inside a word; it is constrained by the relationships in which the word participates.", "Pinch an imaginary word, then open both hands outward into a web."),
7: ("How can a machine give that web of meaning a place where relationships can move?", "a constellation in which tiger and lion stars can drift nearer while tiger and bicycle drift apart", "Private one-hot pedestals keep every word equally far from every other word.", "The pedestals dissolve and training moves stars through a shared geometric sky.", "An embedding is a learned place where useful relationships become available as geometry.", "Hold three fingers far apart, then bring two together while leaving the third away."),
8: ("When a word is surrounded by many others, how can it retrieve only what matters now?", "a movable lantern above a sentence carved around a circular table", "One fixed summary blends river, animal, and action until the word bank cannot choose its active meaning.", "The lantern sends a different beam from each word toward the contextual clues relevant to this occurrence.", "Attention lets each occurrence gather the evidence that matters to its present question.", "Shade your eyes, then point a narrow beam from one imagined word to another."),
9: ("How can raw relevance scores become shares that are positive and together form one whole?", "three attention bowls receiving water from scored channels", "Raw scores include negatives and arbitrary scales, so they cannot say how much of the single vessel each clue receives.", "Every channel becomes positive, then the common vessel divides the water into comparable shares summing to one.", "Softmax turns competing scores into a conserved distribution of attention.", "Raise three fingers at different heights, then lower them into one balanced open palm."),
10: ("Why must asking, matching, and contributing be three different jobs?", "three masks labeled query, key, and value hanging above one word", "Using one description for every job confuses what is sought, how relevance is tested, and what information is finally carried.", "The word passes through three masks: one asks, one advertises, and one contributes.", "Query, key, and value separate the question, the match, and the knowledge that travels.", "Point toward yourself, touch two fingertips together, then offer an open palm."),
11: ("What if understanding one word requires several kinds of relevance at once?", "a many-windowed observatory aimed at the same sentence", "One attention beam must choose between syntax, identity, position, and reference, flattening different relationships into one compromise.", "Several windows open; each follows one kind of relationship before their views reunite.", "Multi-head attention lets several relational questions be asked in parallel before their answers meet.", "Fan your fingers like separate rays, then close them into one hand."),
12: ("After words exchange information, how can each position privately transform what it learned?", "a small two-gate loom standing at every word position", "Attention moves information between positions but cannot by itself perform every nonlinear transformation inside each position.", "Each word enters its own loom, expands through the first gate, bends, and contracts through the second.", "A feed-forward network gives every position a private nonlinear workshop after communication.", "Open both hands wide, bend the fingers, then bring the hands close again."),
13: ("How can a deep stack learn a change without erasing the useful state it already has?", "a stone bridge with an old road running beneath a newly built arch", "Every new layer replaces the whole state, so a poor transformation can destroy information and gradients struggle to return.", "The old road remains open while the new branch contributes only its proposed change.", "A residual connection preserves the old state while allowing a layer to add a correction.", "Hold one hand steady while the other makes a small motion and joins it."),
14: ("How can differently scaled hidden states enter the next layer on comparable footing?", "a balancing fountain whose columns begin at wildly different heights", "One enormous activation dominates the chamber while tiny signals become almost invisible.", "The fountain recenters its columns and adjusts their spread without destroying their relative pattern.", "Layer normalization gives each token a stable local scale from which learning can continue.", "Raise one hand high and one low, then bring them to a balanced middle level."),
15: ("How can a machine use an error to change the internal decisions that produced it?", "a clay brain beside a prediction stone and an error chisel", "The machine can measure that its answer was wrong but the judgment leaves no mark on its internal weights.", "The error chisel travels backward, assigning each adjustable surface a small responsibility and reshaping it.", "Learning begins when observed error can alter the decisions that created it.", "Tap your forehead lightly, trace backward through the air, then make a tiny turning motion."),
16: ("How can countless small learned relationships become abilities nobody wrote as rules?", "a dark word-constellation whose hidden figure appears only when all stars glow", "Inspecting one star or one rule reveals almost nothing resembling the complete ability.", "Connections brighten across many layers until a larger structure becomes visible between them.", "Emergence is the visible capability formed by many distributed relationships acting together.", "Wiggle separate fingertips like stars, then draw a wide circle around the whole pattern."),
}


REALM_QUESTIONS = (
    "How can observation become a form we can compare and transform?",
    "How can relationships between words become a geometry that listens?",
    "How can uncertainty become information, blame, and learning?",
    "How does raw language become an honest next-token prediction?",
    "What must fluent answers acquire before they become useful?",
    "How can a machine act without confusing capability with permission?",
    "How can a deployed system learn while remaining inside the world it changes?",
    "How can a grid of light become objects and imagined images?",
    "How can consequences teach action and still remain governable at scale?",
    "How can a system preserve ignorance long enough to investigate it?",
    "How does a proposed improvement earn the right to be believed?",
    "How can an engine change its route while preserving its mathematical promise?",
    "How can every training artifact remain attached to accountable evidence?",
)

ARTIFACTS = ("seal", "lens", "key", "lantern", "compass", "bridge", "thread", "mirror", "bell", "vessel", "gate", "wheel", "map", "scale", "gear", "prism")
GESTURES = (
    "trace its outline with one finger, cover it with your palm, then uncover only the repaired path",
    "hold both hands as the two failed alternatives, then move one hand through the repaired route",
    "draw the old path in the air, stop sharply at its failure, and finish with the new motion",
    "close one fist around the lost information, then open it as the repair restores that information",
    "point backward to the failed attempt, touch the present object, then point forward through the repair",
    "tilt one hand as the broken rule and use the other to bring the necessary distinction back into balance",
    "make a narrow gate with both hands, block the old path, then open only the route the evidence permits",
    "tap five fingertips in order—question, object, failure, transformation, seal—without saying the formal name",
)

FOUNDATION_LABELS = (
    "Observation", "Features", "Vectors", "Distance", "Change Vectors", "Matrices",
    "Meaning", "Embeddings", "Attention", "Softmax", "Query, Key, and Value",
    "Multi-Head Attention", "Feed-Forward Networks", "Residual Connections",
    "Layer Normalization", "Learning", "Emergence",
)


def chapter_path(number: int) -> Path:
    return next((ROOT / "excavations").glob(f"{number:03d}-*/README.md"))


def fill(template: str, paragraph: str, values: dict[str, str], field: str) -> str:
    marker = "<<<MEMORY_VALUE>>>"
    rendered = template.replace("{" + field + "}", marker)
    for key, value in values.items():
        rendered = rendered.replace("{" + key + "}", value)
    before, after = rendered.split(marker)
    if not paragraph.startswith(before) or (after and not paragraph.endswith(after)):
        raise ValueError(f"cannot recover {field} from {paragraph[:90]!r}")
    stop = len(paragraph) - len(after) if after else None
    return paragraph[len(before):stop]


def concise(value: str) -> str:
    value = re.sub(r"\s+", " ", value).strip().rstrip(". ")
    return value


def question_from(subtitle: str, attempt: str) -> str:
    if re.match(r"^(Why|How|What|When|Where|Which|Who)\b", subtitle):
        return subtitle + "?"
    return f"What fails if we {attempt.rstrip('.')}?"


def action_phrase(value: str) -> str:
    value = concise(value)
    patterns = (
        r"^we need to\s+", r"^we need\s+", r"^need to\s+",
        r"^(?:the method|the system|the model|the agent) (?:must|should|needs to)\s+",
    )
    for pattern in patterns:
        value = re.sub(pattern, "", value, flags=re.I)
    return value[0].lower() + value[1:] if value else value


def derived_source(number: int) -> dict[str, str]:
    path = chapter_path(number)
    text = path.read_text()
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    index = paragraphs.index(CARRY[number])
    place, keeper, base_object = world_for(number)
    _title, concept, subtitle = title_parts(text)
    values = {"place": place, "keeper": keeper, "object": base_object, "concept": concept}
    attempt = fill(SCENES[number % len(SCENES)], paragraphs[index + 1], values, "attempt")
    failure = fill(BREAKS[number % len(BREAKS)], paragraphs[index + 2], values, "failure")
    reveal = next(p for p in paragraphs[index + 1:index + 14] if f"**{concept}**" in p)
    repair = fill(REVEALS[number % len(REVEALS)], reveal, values, "repair")
    return {"attempt": attempt, "failure": failure, "repair": repair}


def derived_memory(number: int) -> dict[str, str]:
    path = chapter_path(number)
    text = path.read_text()
    place, keeper, base_object = world_for(number)
    _title, concept, subtitle = title_parts(text)
    if NARRATIVE_SOURCE.exists():
        source = json.loads(NARRATIVE_SOURCE.read_text())[str(number)]
    else:
        source = derived_source(number)
    attempt = source["attempt"]
    failure = source["failure"]
    repair = source["repair"]
    repair = action_phrase(repair)
    inline_concept = re.sub(r"^(?:A|An|The)\s+", "", concept).strip()
    artifact_kind = ARTIFACTS[number % len(ARTIFACTS)]
    artifact = f"the {inline_concept.lower()} {artifact_kind} mounted on the {base_object}"
    return {
        "question": question_from(subtitle, attempt),
        "object": artifact,
        "failure_image": f"The {artifact_kind} follows the tempting path—{concise(attempt)}. Then the evidence answers: {concise(failure)}.",
        "transformation": f"The {keeper} changes one moving part. The {artifact_kind} can now {repair}.",
        "sentence": f"{concept} keeps the missing power: {repair}.",
        "gesture": f"Touch the {inline_concept.lower()} {artifact_kind} in imagination: {GESTURES[number % len(GESTURES)]}.",
    }


def all_memory() -> dict[int, dict[str, str]]:
    memories = {}
    for number, values in FOUNDATION_MEMORY.items():
        memories[number] = dict(zip(("question", "object", "failure_image", "transformation", "sentence", "gesture"), values))
    for number in range(17, 201):
        memories[number] = derived_memory(number)
    memories.update(ROOT_MEMORY)
    return memories


def realms() -> list[dict]:
    result = []
    for index, ((start, end, place, keeper, base_object), question) in enumerate(zip(WORLDS[:-1], REALM_QUESTIONS), 1):
        result.append({
            "number": index,
            "name": " ".join(word if word in {"of"} else word.title() for word in place.removeprefix("the ").split()),
            "start": start,
            "end": end,
            "question": question,
            "threshold": f"The {keeper} waits beside the {base_object}.",
            "path": f"{base_object} → failed path → recovered power",
        })
    earlier_realm_count = len(result)
    for realm in ROOT_REALMS:
        result.append({**realm, "number": realm["number"] + earlier_realm_count})
    return result


def realm_for(number: int, journey: list[dict]) -> dict:
    return next(realm for realm in journey if realm["start"] <= number <= realm["end"])


def memory_section(number: int, concept: str, memory: dict, realm: dict) -> str:
    variants = (
        "The {concept} room does not ask you to memorize its name. It asks you to watch one object change.",
        "Keep the formal name {concept} covered for another moment. The surviving image is enough to rebuild it.",
        "The {concept} chamber leaves one scene behind so the idea can be recovered after its symbols fade.",
        "Before leaving {concept}, replay the discovery as motion rather than as a definition.",
        "The mathematical name {concept} can now rest. What matters is whether its transformation remains visible.",
    )
    return f"""{START}
> **Memory realm {realm['number']} of 18 — [{realm['name']}](../../MEMORY_PALACE.md#realm-{realm['number']})**
>
> **The question carried into this chamber:** {memory['question']}

## When the chamber changes

{variants[number % len(variants)].format(concept=concept)}

First hold the failed picture still: {memory['failure_image']}

Now let the chamber move: {memory['transformation']}

The object that should remain after the terminology disappears is **{memory['object']}**.

> **Memory seal — {concept}**
>
> {memory['sentence']}

Give the idea a bodily path: {memory['gesture']}
{END}"""


def insert_section(text: str, number: int, section: str) -> str:
    text = re.sub(rf"\n?{re.escape(START)}.*?{re.escape(END)}\n?", "\n", text, flags=re.S)
    if number >= 17:
        position = text.find("\n## ")
    else:
        positions = [text.find("\n" + heading) for heading in (
            "## A serious limitation", "## Where ", "## Challenge", "## What the next excavation needs", "## Next Need"
        ) if text.find("\n" + heading) >= 0]
        position = min(positions) if positions else -1
    if position < 0:
        navigation = text.rfind("\n[Next:")
        position = navigation if navigation >= 0 else len(text)
    return text[:position].rstrip() + "\n\n" + section + "\n\n" + text[position:].lstrip()


def companion_block(number: int, memory: dict) -> str:
    return f"""{START}
## Five-frame memory film

```text
QUESTION       {memory['question']}
     ↓
OBJECT         {memory['object']}
     ↓
VISIBLE BREAK  {memory['failure_image']}
     ↓
TRANSFORMATION {memory['transformation']}
     ↓
MEMORY SEAL    {memory['sentence']}
```
{END}"""


def replace_or_append(text: str, block: str) -> str:
    text = re.sub(rf"\n?{re.escape(START)}.*?{re.escape(END)}\n?", "\n", text, flags=re.S)
    return text.rstrip() + "\n\n" + block + "\n"


def write_chapters(memories: dict, journey: list[dict]) -> None:
    # The book and the recall palace are two reading modes. The prose must flow
    # without commands to cover names, freeze frames, or perform gestures; the
    # explicit five-frame ritual remains in the palace and companions.
    for number in range(201):
        path = chapter_path(number)
        text = path.read_text()
        _title, concept, _subtitle = title_parts(text)
        if number < len(FOUNDATION_LABELS):
            concept = FOUNDATION_LABELS[number]
        memory = memories[number]
        text = re.sub(rf"\n?{re.escape(START)}.*?{re.escape(END)}\n?", "\n", text, flags=re.S)
        path.write_text(re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n")
        folder = path.parent
        diagram = folder / "diagram.md"
        diagram.write_text(replace_or_append(diagram.read_text(), companion_block(number, memory)))
        exercises = folder / "exercises.md"
        exercise = f"""{START}
## Close-book memory test

Close every file. Reconstruct the five frames beginning only from **{memory['object']}**. Explain the failure before naming the accepted idea; perform this gesture while recovering the repair: {memory['gesture']} If the formal name arrives before the necessity, replay the scene more slowly.
{END}"""
        exercises.write_text(replace_or_append(exercises.read_text(), exercise))
        visual = folder / "images" / "README.md"
        visual.parent.mkdir(exist_ok=True)
        current = visual.read_text() if visual.exists() else f"# Visual Brief — {concept}\n"
        brief = f"""{START}
## Cinematic continuity sequence

Create one continuous five-frame scene—not five unrelated illustrations:

1. **Question:** {memory['question']}
2. **Object:** {memory['object']}
3. **Failure:** {memory['failure_image']}
4. **Transformation:** {memory['transformation']}
5. **Seal:** {memory['sentence']}

Keep the same object, lighting, camera direction, and landmarks in every frame. The final frame may reveal notation faintly, but no equation may appear before the physical transformation has made every operation necessary.
{END}"""
        visual.write_text(replace_or_append(current, brief))


def collect(memories: dict, journey: list[dict]) -> dict:
    data_realms = []
    for realm in journey:
        roots = []
        for number in range(realm["start"], realm["end"] + 1):
            path = chapter_path(number)
            _title, concept, _subtitle = title_parts(path.read_text())
            if number < len(FOUNDATION_LABELS):
                concept = FOUNDATION_LABELS[number]
            roots.append({
                "number": number,
                "name": concept,
                "title": path.read_text().splitlines()[0].removeprefix("# "),
                "path": f"../{path.relative_to(ROOT).as_posix()}",
                **memories[number],
            })
        data_realms.append({**realm, "roots": roots})
    return {"version": 1, "realms": data_realms, "root_count": 226}


def guide(data: dict) -> str:
    lines = [
        "# The 226-Chamber Memory Palace",
        "",
        "This is the cinematic index to the complete AI Archaeology journey. It does not replace the chapters. It gives every chapter a retrievable place in imagination.",
        "",
        "Use it during the retrieval passage described in [How to Master AI Archaeology](HOW_TO_MASTER_THIS_BOOK.md), after first reconstructing the chapter's discovery.",
        "",
        "[**Enter the living, clickable Memory Palace →**](https://kleem-labs.github.io/AI-Archaeology/memory-palace/)",
        "",
        "Every chamber preserves the same causal film:",
        "",
        "```text",
        "human question → physical object → visible failure → transformation → memory seal",
        "```",
        "",
        "Walk forward when learning. Walk backward when remembering: seal → transformation → failure → question.",
        "",
    ]
    for realm in data["realms"]:
        lines.extend([
            f"## Realm {realm['number']} — {realm['name']}", "", realm["question"], "",
            "| Excavation | Memory object | Memory seal |", "|---:|---|---|",
        ])
        for item in realm["roots"]:
            lines.append(f"| [{item['number']:03d} — {item['name']}]({item['path'].removeprefix('../')}) | {item['object']} | {item['sentence']} |")
        lines.append("")
    return "\n".join(lines)


def palace_html(data: dict) -> str:
    return (html_page(data)
        .replace("AI Archaeology — The Mathematical Undercroft", "AI Archaeology — The 226-Chamber Memory Palace")
        .replace("AI Archaeology · Volume VI", "AI Archaeology · The Complete Journey")
        .replace("The Undercroft of Mathematical Roots", "The 226-Chamber Memory Palace")
        .replace("Walk five realms. In every chamber, an ordinary object fails, transforms, and leaves behind a mathematical promise you can recover without memorizing a definition.", "Walk eighteen realms and 226 chambers. In each one, an ordinary object fails, transforms, and leaves a promise you can reconstruct instead of memorize.")
        .replace("Five mathematical realms", "Eighteen memory realms")
        .replace("Root chambers in the selected realm", "Excavation chambers in the selected realm")
        .replace("Volume VI", "the complete book"))


def outputs(data: dict) -> dict[Path, str]:
    return {
        ROOT / "MEMORY_PALACE.md": guide(data),
        OUTPUT / "data.json": json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        OUTPUT / "README.md": "# The Living 226-Chamber Memory Palace\n\n[Enter the complete clickable journey.](https://kleem-labs.github.io/AI-Archaeology/memory-palace/)\n\nUse the palace during the retrieval passage in [How to Master AI Archaeology](../HOW_TO_MASTER_THIS_BOOK.md). For the script-free index, use [MEMORY_PALACE.md](../MEMORY_PALACE.md).\n",
        OUTPUT / "index.html": palace_html(data),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    memories = all_memory()
    journey = realms()
    data = collect(memories, journey)
    generated = outputs(data)
    if args.check:
        stale = [str(path) for path, content in generated.items() if not path.exists() or path.read_text() != content]
        for number in range(201):
            text = chapter_path(number).read_text()
            if START in text or END in text:
                stale.append(str(chapter_path(number)))
        if stale:
            raise SystemExit("Memory palace is stale:\n" + "\n".join(stale))
        print("Memory palace matches all 226 excavation films.")
        return
    write_chapters(memories, journey)
    data = collect(memories, journey)
    generated = outputs(data)
    OUTPUT.mkdir(exist_ok=True)
    for path, content in generated.items():
        path.write_text(content)
    print("Built 226 chapter films across 18 connected memory realms.")


if __name__ == "__main__":
    main()
