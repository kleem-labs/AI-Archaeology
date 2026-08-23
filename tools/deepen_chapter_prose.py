"""Turn the excavation catalogue into continuous mathematical book prose.

This pass deliberately works from the chapter-specific intellectual material
already present in every excavation: the carried problem, tempting attempt,
counterexample, repair, worked case, earned arithmetic, limitation, and field
work.  It removes the repeated course-template voice without discarding any of
those ideas.

The marker makes the migration idempotent.  If an older part-builder is run
again, its output loses the marker and can be editorialized again.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).parents[1]
MARKER = "<!-- book-prose-v2 -->"

SECTION = re.compile(r"^## ([^\n]+)\n(.*?)(?=^## |\Z)", re.M | re.S)

CASE_HEADINGS = {
    "Let the case decide",
    "Let one run decide",
    "Now work a case you can see",
    "Follow one case all the way through",
    "Rebuild the Discovery with a Concrete Case",
    "Build Every Piece from the Concrete Example",
}
MATH_HEADINGS = {
    "The arithmetic we have earned",
    "From procedure to notation",
    "Compress your discovery into mathematics",
    "Only Now Give the Discovery a Mathematical Name",
}
BOUNDARY_HEADINGS = {
    "The boundary of the discovery",
    "What this repair cannot do",
    "Where your new idea still breaks",
    "Where the discovery still breaks",
    "Limits",
}
LAB_HEADINGS = {"Enter the laboratory", "Implementation"}
LINK_HEADINGS = {
    "Carry the discovery forward",
    "Continue the dig",
    "Test what you believe",
    "What this discovery now makes possible",
    "Exercises and Connections",
    "Exercises",
    "Connections",
}

LEADS = (
    "The first solution that suggests itself is this:",
    "A reasonable place to begin is:",
    "Without knowing the inherited method, we might try this:",
    "At first, the simplest answer is tempting:",
    "Our first construction is deliberately modest:",
    "Perhaps we",
    "We first try to",
    "One tempting answer is to",
    "At first we",
    "Using what we have, we",
    "An obvious shortcut is to",
    "It survives until the measured run answers back.",
    "The idea survives only until we test it against reality:",
    "Now place that proposal under pressure:",
    "Its hidden assumption appears in the following case:",
    "But the simplicity has discarded something important:",
    "It works—right up to this boundary:",
    "Yet",
    "But the run answers back.",
    "That confidence lasts only until the first measurement.",
    "The shortcut reaches its first real document and breaks.",
    "Reality objects.",
    "The plan survives only until the evidence is counted.",
    "Then the hidden cost becomes visible.",
    "The failure gives us a precise requirement:",
    "What broke tells us what the replacement must preserve:",
    "Remove that assumption and the needed repair becomes clear:",
    "The missing information determines the next move:",
    "Crossing that boundary requires one additional idea:",
    "The cost of that attempt points to the missing operation:",
    "The failure leaves one precise requirement.",
    "What broke tells us what the next design must preserve.",
    "Now the missing job can be stated plainly.",
    "That evidence forces a repair.",
    "The lost information tells us what must come next.",
    "Crossing that boundary requires one additional guarantee.",
    "Now the missing requirement is concrete.",
    "That failure tells us to",
    "Now we can see what is missing: we must",
    "The failure tells us to",
    "That confidence lasts only until",
    "The world refuses to cooperate:",
    "But",
    "So we",
)

OPENINGS = (
    "The least expensive next move is to {attempt}",
    "For a moment, remain loyal to the simplest proposal: {attempt}",
    "Nothing yet appears to demand a new invention. We can {attempt}",
    "The machinery already in our hands suggests that we {attempt}",
    "If the old idea can be stretched one step farther, we should {attempt}",
    "A careful builder would first avoid adding machinery and {attempt}",
    "The obvious economy is to {attempt}",
    "Before naming anything new, try to {attempt}",
    "The first defensible move is to {attempt}",
    "At this point the shortest path seems to be to {attempt}",
    "We can postpone invention if we simply {attempt}",
    "The previous discovery seems almost sufficient: we could {attempt}",
)

ATTRACTIONS = (
    "The proposal deserves a fair hearing. For {concept}, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.",
    "Its appeal is not ignorance but economy. {Concept} should not be added until an observation exposes the exact thing the older procedure cannot preserve.",
    "There is a real principle behind this restraint: the complexity of {concept} must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.",
    "This is how {concept} ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.",
    "If the proposal works on every relevant case, {concept} is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.",
    "The shortcut appears to retain everything {concept} needs. The next observation must test that belief, not merely assert that a textbook prefers another method.",
)

PRESSURE = (
    "Now keep that rule fixed and let the difficult case enter: {failure}",
    "The world supplies the one comparison the shortcut hoped never to face: {failure}",
    "Its hidden assumption becomes visible as soon as we observe that {failure}",
    "Then a case arrives in which convenience and truth separate: {failure}",
    "The proposal breaks for a specific reason, not by authority: {failure}",
    "Reality now asks a question the retained information cannot answer: {failure}",
    "The decisive test is this: {failure}",
    "One counterexample is enough to expose the missing job: {failure}",
)

HINGES = (
    "The failure changes the question behind {concept}. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.",
    "Notice what the counterexample has accomplished for {concept}. It has not handed us a standard technique. It has told us the property any successful repair must preserve.",
    "That distinction is the hinge on which {concept} turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.",
    "The wrong answer makes the need for {concept} inspectable. We can state the new job in ordinary language before allowing symbols to hide it.",
    "Nothing magical creates {concept}. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.",
    "The counterexample teaches {concept}. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.",
)

REPAIRS = (
    "The required repair is now narrow enough to state: {repair}",
    "So the new mechanism must do one additional job: {repair}",
    "What survives the counterexample is this requirement: {repair}",
    "We can now repair the procedure without guessing: {repair}",
    "The lost distinction tells us what to build: {repair}",
    "Only one extra responsibility has been earned: {repair}",
)

CASE_BRIDGES = (
    "Put the old procedure beside {concept}. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.",
    "Run the {concept} scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.",
    "The name {concept} is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.",
    "There are now two histories of this {concept} case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.",
    "Hold the setting, evidence, and desired outcome fixed while testing {concept}. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.",
    "A formula for {concept} is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.",
)

NAME_BRIDGES = (
    "Only at this point does the inherited name **{concept}** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.",
    "Humanity eventually gathered this problem and its repairs under the name **{concept}**. The name comes after the need; it must never conceal the observation that gave it meaning.",
    "We have earned the chapter's shorter name: **{concept}**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.",
    "The usual name, **{concept}**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.",
    "This boundary between the failed rule and its repair is the subject later work calls **{concept}**. Naming it adds nothing; the discovery happened when the lost information became visible.",
    "Now—and not earlier—we may introduce **{concept}**. The words label the problem-and-repair pair whose necessity the reader can already test.",
)

RECONSTRUCTIONS = (
    "Test the necessity of {concept} by mentally removing the repair. We fall back to the proposal to {attempt}; then {failure}. Restore only the ability to {repair}, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.",
    "Now perform a small thought experiment. Keep the whole situation fixed but replace {concept} with the old instruction to {attempt}. The result is again that {failure}. Put back only the requirement to {repair}. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.",
    "A reader can check that {concept} is necessary rather than decorative. Delete its new responsibility and use the earlier plan to {attempt}. Immediately, {failure}. Reintroduce the single job to {repair}. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.",
    "We can audit the discovery from both directions. Starting with the shortcut to {attempt} produces the observed failure: {failure}. Starting with the repaired demand to {repair} preserves the information the shortcut lost. The subject of {concept} lives in the difference between those two causal stories.",
    "Do not memorize {concept}; try to break it by subtraction. Remove the part that knows how to {repair}, leaving only the attempt to {attempt}. What returns is not a vague weakness but the original contradiction: {failure}. The removed responsibility therefore has an observable job.",
    "The invention can now defend itself. Without it, our best available move is to {attempt}, and the case answers that {failure}. With the narrow repair—to {repair}—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.",
)

ATTRIBUTION_CHECKS = (
    "Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to {attempt} to requiring the system to {repair}. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to {concept}.",
    "The comparison has one invariant: the world does not become kinder when {concept} is introduced. The same evidence that defeated the attempt to {attempt} is presented again. Only the ability to {repair} changes, so the repaired conclusion cannot be credited to a conveniently different example.",
    "This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can {repair}. Because the old plan to {attempt} is the only displaced piece, the reader can locate exactly where {concept} changes the outcome.",
    "Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to {repair} instead of merely trying to {attempt}. That controlled contrast is what turns a plausible explanation of {concept} into an understandable derivation.",
    "A name can make an invention feel inevitable, but this control removes that illusion. The rule to {attempt} receives the same test as the rule to {repair}. Their different outcomes reveal what {concept} contributes without asking the reader to trust historical convention.",
    "The logic would be weaker if the repaired method were tested on an easier scene. It is not. {Concept} returns to the same counterexample, replaces the attempt to {attempt} with the responsibility to {repair}, and must succeed where the shortcut failed.",
)

BOUNDARY_BRIDGES = (
    "The limit follows from the job assigned to {concept}. Its repair knows how to {repair}. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.",
    "Why does that boundary remain? {Concept} was built for one responsibility: {repair}. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.",
    "The weakness is not an accidental footnote. Every operation in {concept} serves the narrower purpose to {repair}; none was designed to answer the new question. We have reached the honest edge of the invention.",
    "Look back at what {concept} actually preserves: it can {repair}. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.",
    "This is where {concept} runs out for a causal reason. We gave it enough structure to {repair}, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.",
    "The boundary can be predicted from the construction itself. {Concept} performs the repair to {repair}; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.",
)

FIELDWORK_OPENINGS = (
    "A claim about {concept} now exists on the page; the laboratory must be able to contradict it.",
    "The argument for {concept} is still provisional until a runnable case can make it fail.",
    "Understanding {concept} now means predicting its intermediate results before asking software for an answer.",
    "The reader has reconstructed {concept} in words; the workbench tests whether those words specify a real procedure.",
    "A mathematical story about {concept} earns trust only when the failed and repaired paths can both be reproduced.",
    "Move {concept} from imagination to evidence by making the shortcut fail under controlled inputs.",
)


def compact(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def clean_sentence(value: str) -> str:
    value = compact(value)
    changed = True
    while changed:
        changed = False
        for lead in sorted(LEADS, key=len, reverse=True):
            if value.lower().startswith(lead.lower()):
                value = value[len(lead):].strip(" :")
                changed = True
                break
    return value.rstrip(". ")


def lower_first(value: str) -> str:
    value = value.strip()
    if not value:
        return value
    return value[0].lower() + value[1:]


def finish(value: str) -> str:
    value = value.strip()
    if value and value[-1] not in ".!?:":
        value += "."
    return value


def title_parts(text: str) -> tuple[str, str, str]:
    first = text.splitlines()[0].removeprefix("# ").strip()
    parts = [part.strip() for part in first.split(" — ")]
    concept = parts[1] if len(parts) > 1 else first
    subtitle = " — ".join(parts[2:]) if len(parts) > 2 else f"Understanding {concept.lower()}"
    if len(parts) == 2 and ":" in concept:
        concept, subtitle = [piece.strip() for piece in concept.split(":", 1)]
    return first, concept, subtitle.rstrip("?")


def part_block(text: str) -> str:
    match = re.search(r"(?m)^> \*\*PART .*?(?=\n\n(?!>)|\Z)", text, re.S)
    return match.group(0).strip() if match else ""


def opening_paragraphs(text: str) -> list[str]:
    first_h2 = text.find("\n## ")
    prefix = text if first_h2 < 0 else text[:first_h2]
    prefix = re.sub(r"(?m)^# .*\n?", "", prefix, count=1)
    prefix = re.sub(r"(?m)^>.*\n?", "", prefix)
    paragraphs = []
    for paragraph in prefix.split("\n\n"):
        value = compact(paragraph)
        if not value or value.startswith("[Previous") or value == MARKER:
            continue
        paragraphs.append(value)
    return paragraphs


def section_map(text: str) -> list[tuple[str, str]]:
    return [(m.group(1).strip(), m.group(2).strip()) for m in SECTION.finditer(text)]


def pick(sections: list[tuple[str, str]], names: set[str]) -> str:
    for name, body in sections:
        if name in names or any(name.startswith(prefix) for prefix in names):
            return body.strip()
    return ""


def pick_all(sections: list[tuple[str, str]], names: set[str]) -> str:
    bodies = []
    generic = (
        "The procedure now works in ordinary language. To repeat it consistently and "
        "implement it at scale, we give precise names to operations the concrete example has already earned."
    )
    for name, body in sections:
        if name in names or any(name.startswith(prefix) for prefix in names):
            if compact(body) != generic:
                bodies.append(body.strip())
    return "\n\n".join(bodies)


def remaining_sections(sections: list[tuple[str, str]]) -> list[tuple[str, str]]:
    consumed = CASE_HEADINGS | MATH_HEADINGS | BOUNDARY_HEADINGS | LAB_HEADINGS | LINK_HEADINGS
    return [(name, body) for name, body in sections if name not in consumed]


def prose_math(body: str, concept: str, number: int) -> str:
    if not body:
        return ""
    body = body.strip()
    body = body.replace("### Only now do the symbols earn names", "### Names for pieces we have already used")
    body = body.replace("### Give Short Names Only After We Know the Pieces", "### Names for pieces we have already used")
    body = body.replace("### Why these operations are forced", "### Why no cheaper operation does the same job")
    body = body.replace("### Why Every Term Must Exist Before the Equation", "### Why every term has to be present")
    # Term dictionaries and operation checklists were the strongest remaining
    # source of a notes-like rhythm. Their sentences now form prose while the
    # links and bold symbol names remain visible.
    body = re.sub(r"(?m)^- ", "", body)
    body = body.replace(
        "Only now can we compress the exact procedure:",
        f"Every symbol in {concept} can now be read back into an action already performed. The whole procedure fits in one line:",
    )
    body = body.replace(
        "Only now can we compress the procedure:",
        f"Every symbol in {concept} can now be read back into an action already performed. The whole procedure fits in one line:",
    )
    body = body.replace(
        "Only now can we compress that reasoning:",
        "The notation is finally shorter than the story that created it:",
    )
    body = body.replace(
        "Only now should notation compress it:",
        "The notation is finally shorter than the story that created it:",
    )
    body = body.replace(
        "No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would create decoration, not understanding.",
        f"{concept} earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.",
    )
    body = re.sub(r"\n{3,}", "\n\n", body)
    intro = (
        f"Do not read the coming {concept} line as an instruction dropped from above. "
        "Read it from left to right as a compressed record of the concrete decisions already made."
        if number % 2 == 0
        else
        f"Before {concept} receives symbols, its procedure must be possible in ordinary language. "
        "Notation is useful here only because it lets us repeat that same reasoning without ambiguity."
    )
    return f"## The calculation hidden inside {concept.lower()}\n\n{intro}\n\n{body}"


def fieldwork(concept: str, lab: str, links: str, number: int) -> str:
    lab = compact(lab) if lab else "Reproduce the failed rule first, predict the repaired result, and only then run the three implementations."
    items = []
    for line in links.splitlines():
        line = line.strip()
        if line.startswith("- ["):
            items.append(line[2:])
    if not items:
        items = [
            "[Mistakes worth preserving](mistakes.md)",
            "[The chapter diagram](diagram.md)",
            "[Invention exercises](exercises.md)",
            "[Primary research trail](references.md)",
            "[Visual brief](images/README.md)",
        ]
    companions = "; ".join(items[:-1]) + (f"; and {items[-1]}" if items else "")
    return (
        f"## Take {concept.lower()} to the workbench\n\n"
        f"{FIELDWORK_OPENINGS[number % len(FIELDWORK_OPENINGS)].format(concept=concept.lower(), Concept=concept)} "
        f"{finish(lab)} "
        "Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. "
        f"Before running {concept.lower()}, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.\n\n"
        f"Explain the {concept.lower()} result once without terminology, then once with the precise symbols or state transitions the implementation used.\n\n"
        f"The rest of the evidence remains beside this excavation: {companions}."
    )


def editorialize(path: Path) -> bool:
    text = path.read_text()
    if MARKER in text:
        return False
    number = int(path.parent.name[:3])
    title, concept, subtitle = title_parts(text)
    part = part_block(text)
    sections = section_map(text)

    # The first sixteen excavations were written individually and already have
    # richer openings. Preserve them, but remove the catalogue-like ending and
    # improve the repeated mathematical scaffolding where present.
    if number < 17:
        out = text
        out = out.replace("## Enter the laboratory", f"## Take {concept.lower()} to the workbench")
        out = out.replace("## Carry the discovery forward", f"## Follow {concept.lower()} into the next discovery")
        out = out.replace("## Continue the dig", f"## Follow {concept.lower()} into the next discovery")
        out = out.replace("## The arithmetic we have earned", f"## The calculation hidden inside {concept.lower()}")
        out = out.replace("### Only now do the symbols earn names", "### Names for pieces we have already used")
        out = out.replace("### Why these operations are forced", "### Why no cheaper operation does the same job")
        out = re.sub(r"(?m)^- (?=\[[^\]]+\]\()", "", out)
        out = out.replace("Only now can we compress that reasoning:", "The notation is finally shorter than the story that created it:")
        out = out.replace("Only now can we compress the exact procedure:", "Every symbol now names an action already performed. The whole procedure fits in one line:")
        out = out.rstrip() + f"\n\n{MARKER}\n"
        path.write_text(out)
        return True

    paragraphs = opening_paragraphs(text)
    if len(paragraphs) < 3:
        raise ValueError(f"{path}: cannot recover observation/attempt/failure/repair")

    carry = paragraphs[0]
    raw_attempt = clean_sentence(paragraphs[1])
    if len(paragraphs) >= 4:
        attempt = raw_attempt
        failure = clean_sentence(paragraphs[2])
        repair = clean_sentence(paragraphs[3])
    else:
        sentences = re.split(r"(?<=[.!?])\s+", raw_attempt, maxsplit=1)
        attempt = sentences[0]
        failure = sentences[1] if len(sentences) > 1 else raw_attempt
        repair = clean_sentence(paragraphs[2])

    case = pick(sections, CASE_HEADINGS)
    math = pick_all(sections, MATH_HEADINGS)
    boundary = pick(sections, BOUNDARY_HEADINGS)
    lab = pick(sections, LAB_HEADINGS)
    links = pick(sections, LINK_HEADINGS)

    # Some early chapters carry the worked case directly inside the arithmetic
    # section. Do not manufacture a second one; the opening counterexample is
    # already concrete and the arithmetic will continue it.
    case_text = ""
    if case:
        cleaned_case = re.sub(
            r"\n\nNothing in that case was introduced because.*?(?=\n\n|\Z)",
            "",
            case,
            flags=re.S,
        ).strip()
        case_paragraphs = [p.strip() for p in cleaned_case.split("\n\n") if p.strip()]
        case_body = "\n\n".join(case_paragraphs)
        case_text = (
            f"## {subtitle}\n\n"
            f"{case_body}\n\n"
            f"{CASE_BRIDGES[number % len(CASE_BRIDGES)].format(concept=concept.lower(), Concept=concept)}"
        )

    opening = [f"# {title}", MARKER]
    if part:
        opening.append(part)
    opening.extend(
        [
            carry,
            finish(OPENINGS[number % len(OPENINGS)].format(attempt=lower_first(attempt))),
            ATTRACTIONS[number % len(ATTRACTIONS)].format(concept=concept.lower(), Concept=concept),
            finish(PRESSURE[number % len(PRESSURE)].format(failure=lower_first(failure))),
            HINGES[number % len(HINGES)].format(concept=concept.lower(), Concept=concept),
            finish(REPAIRS[number % len(REPAIRS)].format(repair=lower_first(repair))),
            NAME_BRIDGES[number % len(NAME_BRIDGES)].format(concept=concept),
            RECONSTRUCTIONS[number % len(RECONSTRUCTIONS)].format(
                concept=concept.lower(),
                Concept=concept,
                attempt=lower_first(attempt),
                failure=lower_first(failure),
                repair=lower_first(repair),
            ),
            ATTRIBUTION_CHECKS[number % len(ATTRIBUTION_CHECKS)].format(
                concept=concept.lower(),
                Concept=concept,
                attempt=lower_first(attempt),
                repair=lower_first(repair),
            ),
        ]
    )

    pieces = ["\n\n".join(opening)]
    if case_text:
        pieces.append(case_text)
    math_text = prose_math(math, concept, number)
    if math_text:
        pieces.append(math_text)

    for name, body in remaining_sections(sections):
        # Preserve genuinely chapter-specific material not consumed above.
        if name in {"Real-World Analogy", "Carry the idea back into the world"}:
            pieces.append(f"## {concept} beyond this one case\n\n{body}")
        elif name not in {"Next Need", "What the next excavation needs"}:
            pieces.append(f"## {name}\n\n{body}")

    if boundary:
        boundary = re.sub(r"\n\nThat boundary is the opening condition.*", "", boundary, flags=re.S).strip()
        causal = BOUNDARY_BRIDGES[number % len(BOUNDARY_BRIDGES)].format(
            concept=concept.lower(), Concept=concept, repair=lower_first(repair)
        )
        pieces.append(f"## Where {concept.lower()} runs out\n\n{boundary}\n\n{causal}")

    pieces.append(fieldwork(concept, lab, links, number))

    # Keep forward navigation or the final closing sentence, but never allow it
    # to interrupt the chapter opening.
    tail = text[text.rfind("\n## ") :] if "\n## " in text else text
    next_match = re.search(r"(?m)^\[Next:[^\n]+", text)
    if next_match:
        pieces.append(next_match.group(0))
    elif number == 200:
        final_line = text.rstrip().splitlines()[-1]
        if final_line and not final_line.startswith("-") and not final_line.startswith("##"):
            pieces.append(final_line)

    final = "\n\n".join(piece.strip() for piece in pieces if piece.strip())
    final = re.sub(
        r"No new equation is needed\. The invention is a boundary, procedure, or system contract\. "
        r"Adding symbols would (?:create decoration, not understanding|not make it more rigorous)\.",
        f"{concept} earns a boundary, procedure, or system contract rather than a new equation. "
        "Symbols here would decorate the decision instead of clarifying it.",
        final,
    )
    path.write_text(final + "\n")
    return True


def main() -> None:
    changed = 0
    for path in sorted((ROOT / "excavations").glob("*/README.md")):
        changed += editorialize(path)
    print(f"Deepened {changed} excavation chapters into continuous book prose.")


if __name__ == "__main__":
    main()
