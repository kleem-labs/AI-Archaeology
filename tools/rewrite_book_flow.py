"""Replace editorial teaching prompts with continuous causal prose.

The first woven edition stored each chapter's attempt, failure, and repair in
ornate templates.  This migration preserves those facts in a small source file
and rewrites the chapter opening as a scene a reader can simply inhabit.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from build_memory_palace import NARRATIVE_SOURCE, action_phrase, concise, derived_source
from deepen_chapter_prose import title_parts
from rebuild_narrative_continuity import CARRY
from weave_mathematical_world import world_for


ROOT = Path(__file__).parents[1]
MARKER = "<!-- flow-prose-v1 -->"


SCENES = (
    "At {place}, the {keeper} meets the next case beside the {object}. The nearest idea is also the most reasonable one: {attempt}.",
    "The previous discovery reaches {place} carrying one unfinished problem. Beside the {object}, the {keeper} first tries to {attempt}.",
    "A new case arrives at {place}. Nothing yet demands a new invention, so the {keeper} uses the {object} to {attempt}.",
    "Inside {place}, the old method is given an honest chance. The {keeper} places the evidence on the {object} and tries to {attempt}.",
)

FAILURES = (
    "The easy case appears to confirm the rule. Then a harder observation exposes its limit: {failure}.",
    "That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: {failure}.",
    "For a moment the answer looks complete. The next observation shows what the method could not preserve: {failure}.",
    "The attempt reaches a boundary that greater confidence cannot cross: {failure}.",
)

WHY_ATTEMPTS = (
    "The attraction of this attempt is easy to see. To {attempt} reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.",
    "There is good reason to begin this way. If we {attempt}, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.",
    "This is precisely the kind of shortcut a careful builder should try first. The instruction to {attempt} preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.",
    "Nothing about this first move is careless. To {attempt} is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.",
)

WHAT_FAILURES = (
    "The contradiction matters because it identifies a structural loss in the instruction to {attempt}, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The {object} will remain beside both versions so that the added capacity can be traced to the observation that demanded it.",
    "This failure cannot be repaired by performing the instruction to {attempt} more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the {object}; otherwise a changed answer could be mistaken for an explanation.",
    "The counterexample separates two questions that the attempt to {attempt} had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the {object} fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.",
    "The important discovery is not merely that trying to {attempt} failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the {object}, so success cannot be manufactured by quietly replacing the original question.",
)

REPAIRS = (
    "The repair can now be kept narrow. The new method must {repair} This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.",
    "The evidence has earned one extension and no more. We need to {repair} The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.",
    "Only the broken responsibility needs to change. The method must now {repair} With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.",
    "The old construction is therefore not discarded. It is widened just enough to {repair} The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.",
)

REVEALS = (
    "A construction that performs this newly earned job is **{concept}**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.",
    "Once this responsibility becomes part of the method, we have built what is called **{concept}**. The name is simply a handle for the distinction already reconstructed.",
    "This repaired capacity is the idea named **{concept}**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.",
    "The necessary extension now has a name: **{concept}**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.",
)


def chapter_path(number: int) -> Path:
    return next((ROOT / "excavations").glob(f"{number:03d}-*/README.md"))


def preserve_sources() -> dict[str, dict[str, str]]:
    if NARRATIVE_SOURCE.exists():
        return json.loads(NARRATIVE_SOURCE.read_text())
    sources = {str(number): derived_source(number) for number in range(17, 201)}
    NARRATIVE_SOURCE.parent.mkdir(exist_ok=True)
    NARRATIVE_SOURCE.write_text(json.dumps(sources, ensure_ascii=False, indent=2) + "\n")
    return sources


def lower_action(value: str) -> str:
    value = action_phrase(value)
    value = re.sub(r"^(?:to\s+)", "", value, flags=re.I)
    return value


def rewrite(number: int, source: dict[str, str]) -> None:
    path = chapter_path(number)
    raw_text = path.read_text()
    had_flow_marker = MARKER in raw_text
    text = text_without_marker = raw_text.replace(MARKER + "\n\n", "")
    title, concept, _subtitle = title_parts(text)
    place, keeper, object_name = world_for(number)
    carry = CARRY[number]
    first_heading = text.find("\n## ")
    if first_heading < 0:
        raise ValueError(f"missing first section in {path}")
    start = text.find(carry)
    if start < 0:
        if not had_flow_marker:
            raise ValueError(f"missing carry paragraph in {path}")
        opening_blocks = text[:first_heading].rstrip().split("\n\n")
        if len(opening_blocks) < 4:
            raise ValueError(f"cannot recover rewritten opening in {path}")
        prefix = "\n\n".join(opening_blocks[:-4]).rstrip()
    else:
        prefix = text_without_marker[:start].rstrip()

    attempt = lower_action(source["attempt"]).rstrip(". ")
    failure = concise(source["failure"])
    repair = lower_action(source["repair"])
    if not repair.endswith((".", "?", "!")):
        repair += "."
    values = {
        "place": place,
        "keeper": keeper,
        "object": object_name,
        "attempt": attempt,
        "failure": failure,
        "repair": repair,
        "concept": concept,
    }
    scene = SCENES[number % len(SCENES)].format(**values)
    why_attempt = WHY_ATTEMPTS[number % len(WHY_ATTEMPTS)].format(**values)
    fracture = FAILURES[number % len(FAILURES)].format(**values)
    what_failure = WHAT_FAILURES[number % len(WHAT_FAILURES)].format(**values)
    resolution = REPAIRS[number % len(REPAIRS)].format(**values)
    reveal = REVEALS[number % len(REVEALS)].format(**values)
    opening = "\n\n".join((carry, scene, why_attempt, fracture, what_failure, resolution, reveal))

    if "<!-- mathematical-world-v1 -->" in prefix:
        prefix = prefix.replace(
            "<!-- mathematical-world-v1 -->",
            "<!-- mathematical-world-v1 -->\n\n" + MARKER,
        )
    else:
        prefix += "\n\n" + MARKER
    rewritten = prefix + "\n\n" + opening + "\n" + text_without_marker[first_heading:]
    rewritten = re.sub(r"\n{3,}", "\n\n", rewritten).rstrip() + "\n"
    path.write_text(rewritten)


def remove_editorial_asides() -> None:
    """Keep derivation prose inside the mathematical scene."""
    for path in sorted((ROOT / "excavations").glob("*/README.md")):
        text = path.read_text()
        _title, concept, _subtitle = title_parts(text)
        text = re.sub(
            r"Cover the prose about [^.]+ and each mark can still be recovered from the case\. "
            r"Only now is the compressed form safe to write:",
            f"Every mark in the coming {concept.lower()} equation now belongs to a visible part of the case. The compressed form is:",
            text,
        )
        text = text.replace(
            "Every mark in the coming line now belongs to a visible part of the case. The compressed form is:",
            f"Every mark in the coming {concept.lower()} equation now belongs to a visible part of the case. The compressed form is:",
        )
        text = re.sub(
            r"Before the line is compressed, notice its recurring motions: (.*?) "
            r"They are the handholds by which the reader can later climb back from notation to meaning\.",
            r"The calculation reuses familiar motions: \1 Together they keep the path from the concrete case to notation intact.",
            text,
        )
        text = text.replace(
            "The reader can see the growth by drawing the square table:",
            "The growth becomes visible when we draw the square table:",
        )
        text = text.replace(
            "neither the reader nor the loss can treat them as comparable beliefs yet.",
            "they cannot yet serve as comparable beliefs or a stable training target.",
        )
        path.write_text(text)


def main() -> None:
    sources = preserve_sources()
    for number in range(17, 201):
        rewrite(number, sources[str(number)])
    remove_editorial_asides()
    print("Rewrote Excavations 017–200 as one causal reading journey.")


if __name__ == "__main__":
    main()
