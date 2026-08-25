"""Weave the logical excavations into one visual, mathematical world.

The earlier editorial pass established necessity. This pass supplies the layer
that a book needs after correctness: recurring places, visual transformations,
mathematical motifs, silence before names, and milestone revelations. It
replaces meta-pedagogy; it does not decorate or alter the mathematics.
"""

from __future__ import annotations

from pathlib import Path
import argparse
import re
import subprocess
import sys

from deepen_chapter_prose import OPENINGS, PRESSURE, REPAIRS, compact, title_parts


ROOT = Path(__file__).parents[1]
MARKER = "<!-- mathematical-world-v1 -->"


# start, end, place, keeper, physical object used to think
WORLDS = (
    (0, 5, "the Valley of First Measures", "cartographer", "dust-map"),
    (6, 16, "the Scriptorium of Echoes", "keeper of words", "long cedar table"),
    (17, 35, "the Lantern Observatory", "keeper of uncertain stories", "ring of glass lanterns"),
    (36, 45, "the Clockwork Scriptorium", "mechanist", "sentence-wheel"),
    (46, 55, "the Hall of Voices", "public archivist", "listening table"),
    (56, 65, "the Gatehouse of Consequences", "gatekeeper", "iron threshold"),
    (66, 75, "the Living Watchgarden", "field naturalist", "weathered observation slate"),
    (76, 85, "the Glass Menagerie", "maker of seeing-machines", "wall of illuminated tiles"),
    (86, 100, "the Road of Consequences", "expedition leader", "map of branching journeys"),
    (101, 125, "the Hall of Possible Worlds", "keeper of unfinished questions", "table of mirrored maps"),
    (126, 150, "the Academy of Trials", "experimentalist", "sealed evidence ledger"),
    (151, 175, "the Engine Cavern", "enginewright", "brass reference machine"),
    (176, 200, "the Archive Foundry", "archivist-engineer", "chain-of-custody ledger"),
    (201, 225, "the Undercroft of First Principles", "mathematical archaeologist", "stone workbench"),
)

REALM_ECHOES = (
    "Beneath {concept}, the valley's first instruments are still present: marks preserve observations, comparisons preserve differences, and arrows preserve change. The object has grown richer, but the mathematical need is descended from those first tracks in the dust.",
    "The Scriptorium has not abandoned geometry. Inside {concept}, nearness still means shared structure, direction still means agreement, and addition still lets several voices contribute without becoming the same voice. Meaning is geometry taught to listen.",
    "Every lantern in {concept} remembers an older operation. Probability keeps several stories lit; logarithms turn compounded uncertainty into steps; summation lets separate surprises form one account. Learning begins when those lights can alter the machine that reads them.",
    "The sentence-wheel turns with machinery earned long before language: indices retrieve, vectors carry features, dot products compare directions, and weighted sums gather context. {concept} changes what travels through the machine, not why those operations exist.",
    "In the Hall of Voices, {concept} inherits the mathematics of honest comparison: measure on the same evidence, separate memory from observation, and preserve uncertainty until a source can resolve it. Fluent words do not repeal those older obligations.",
    "The Gatehouse gives ancient arrows a moral weight. In {concept}, an arrow no longer means only ‘becomes’; it may cross from language into irreversible state. Sets describe what is permitted, boundaries describe where permission ends, and evidence must prove which transition truly occurred.",
    "The Living Watchgarden studies change itself. Under {concept}, a remembered baseline makes movement visible, probability keeps untried futures alive, and causal comparison asks which action—not merely which coincidence—bent the world. The observer now stands inside the loop being measured.",
    "The Glass Menagerie returns to the valley's geometry at a finer scale. {concept} asks which nearby lights belong together, how small patterns compose into larger ones, and which transformations preserve identity while appearance changes. Seeing is measurement arranged across space.",
    "Along the Road of Consequences, {concept} combines two old languages: probability for futures that may occur and value for consequences that matter if they do. An action is therefore not a label; it is an arrow cast into a branching world.",
    "The mirrored maps beneath {concept} preserve a discipline learned from distance: compare like with like and keep the relevant difference visible. Here the compared objects are possible worlds, causes, proofs, memories, or programs rather than animal measurements.",
    "At the Academy of Trials, {concept} is built from controlled differences. Hold the surrounding world still, change one claimed cause, and measure what survives. Subtraction becomes intellectual honesty: remove the baseline before calling the remainder an improvement.",
    "The Engine Cavern lets {concept} change speed, memory, or scale while the brass reference machine guards meaning. Equality here is not decoration; it is a promise that the optimized path performs the same mathematical responsibility by another physical route.",
    "In the Archive Foundry, {concept} joins mathematics to memory. Sets identify what must be present, hashes preserve identity, counts bound exposure, and arrows keep every transformation attached to its source. A model may forget its documents internally; the factory must not forget them externally.",
    "In the Undercroft, {concept} is recovered beneath the machine that had already been using it. Concrete objects remain visible until every symbol has a human job, and each operation stays connected to the failure that made it necessary.",
)


WORLD_MEMORY = (
    "The {object} keeps both histories. Its older mark still says, ‘{attempt}’; beside it, the newer mark says, ‘{repair}.’ The distance between those sentences is the exact shape of {concept}: no larger than the failure required, and no smaller than reality permits.",
    "Nothing is erased from the {object}. The failed path remains visible beneath the repair, because {concept} is easier to remember when its scar remains attached to it. The scar reads, ‘{failure}’; the new line exists only to keep that loss from happening again.",
    "A thread now runs backward from {concept} through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and {failure}. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction.",
    "The {keeper} places a finger over the new distinction. At once the two cases collapse and {failure}. Lifting the finger restores only this capacity: {repair}. That tiny reversible motion is the chapter's proof of necessity.",
    "What changed on the {object} can be said without symbols. Before, the method could only {attempt}; now it can also {repair}. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.",
    "The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In {concept}, that memory takes a precise form: whenever {failure}, preserve enough structure to {repair}.",
    "The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because {failure}, while the other can {repair}. That fork—not the vocabulary—is where {concept} lives.",
    "The {object} has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and {concept} looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.",
    "One boundary in the room is now sharper. On one side lies the promise to {attempt}; on the other lies the observed fact that {failure}. The bridge called {concept} has exactly the planks needed to {repair}.",
    "The {keeper} does not memorize {concept}. Instead, the {keeper} memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can {repair}. The formal name merely lets that motion be shared.",
    "Under the latest ink, the first question is still legible: what if we followed the tempting rule—{attempt}? The answer remains {failure}. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.",
    "The marks on the {object} form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. {concept} is not any single point. It is the path connecting them in the only order that makes the last point necessary.",
)


SCENES = (
    "At {place}, the {keeper} returns to the {object}. Yesterday's instrument still lies open, so the first move asks for no new magic: {attempt}.",
    "Morning reaches {place} before anyone has a name for today's difficulty. Beside the {object}, the {keeper} tries the smallest continuation of what already works: {attempt}.",
    "The {object} at {place} still carries the marks of the previous discovery. The {keeper} follows them as far as they seem willing to go: {attempt}.",
    "Night gathers around {place}. Under the light of the {object}, the {keeper} refuses to invent prematurely and begins with the plain rule: {attempt}.",
    "Inside {place}, every old tool is given one honest chance. The {keeper} sets the {object} between the evidence and the desired answer, then tries to {attempt}.",
    "A new case arrives at {place}, but the {keeper} first reaches for the familiar {object}. Its promise is simple: {attempt}.",
    "The doors of {place} close against the wind. On the {object}, the {keeper} writes the cheapest rule that might still be true: {attempt}.",
    "Nothing in {place} yet bears today's mathematical name. There is only the {keeper}, the {object}, and one plausible action: {attempt}.",
)

BREAKS = (
    "For a moment the mark looks complete. Then the evidence refuses to fit: {failure}. The old line has not become false everywhere; it has reached the precise place where it can no longer see.",
    "The rule survives the easy cases. The next case leaves a crack through the middle of it: {failure}. More confidence cannot repair information that never entered the rule.",
    "Reality answers without terminology: {failure}. The {object} now holds two situations the old rule cannot keep apart.",
    "Then the quiet test arrives: {failure}. What looked like simplicity is revealed as a missing distinction.",
    "The {keeper} repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: {failure}. The failure is stable enough to become evidence.",
    "At the edge of the {object}, the shortcut produces its consequence: {failure}. That consequence, not a textbook, earns the next move.",
)

QUESTIONS = (
    "No one reaches for a {concept} formula. The only useful question is smaller: what did the first path lose that the second path must carry?",
    "The room becomes quiet around the failed {concept} mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.",
    "The broken rule has given {concept} a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.",
    "The {keeper} circles the place where the two {concept} cases collapsed together. The repair must open that circle and preserve the difference inside it.",
    "The failure is no longer an embarrassment to {concept}. It is a compass: it points directly toward the information the next construction must retain.",
    "What must change for {concept} is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.",
)

OVERLAYS = (
    "The {keeper} lays two translucent sheets over the {object}. The first is inscribed, “{attempt}.” Its path ends where {failure}. The second receives the same evidence but is allowed to {repair}. Held to the light, the sheets separate at exactly one decision.",
    "Two trails now cross the {object}. The pale trail bears the instruction “{attempt}.” It disappears into the observed failure: {failure}. The darker trail carries one additional capacity—to {repair}. Nothing else in the scene moves, so the new branch cannot hide where its power came from.",
    "The {object} is divided down the middle. Left side: “{attempt}.” Its final mark records {failure}. Right side: the same starting evidence, now allowed to {repair}. The difference is narrow enough to see and important enough to change the ending.",
    "The {keeper} turns the {object} toward the light. Through the old engraving, {attempt}, the evidence ends in the same contradiction: {failure}. A second engraving adds only the power to {repair}. Superimposed, the two paths share every stroke until the precise place where the old one breaks.",
    "Across the {object}, the old path and the repaired path run side by side. One carries “{attempt}”; the other knows how to {repair}. When the failure—{failure}—arrives, only one path still possesses a place to record the missing distinction.",
    "The {keeper} covers the new mark and the old contradiction returns: {failure}. The cover is lifted, restoring the ability to {repair}, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason {concept} exists.",
)

REVEALS = (
        "The {keeper} changes only that one responsibility: {repair}. When the ink dries, the name **{concept}** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.",
        "So the {object} is altered in exactly one way: {repair}. Much later, people will call this territory **{concept}**. Here the name is only a memory of the failure it can survive.",
        "The repair can now be stated without mystery: {repair}. The name **{concept}** arrives afterward, like a title given to a path whose stones are already underfoot.",
        "Only the missing distinction is restored: {repair}. The {keeper} writes **{concept}** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.",
    "The evidence permits one narrow invention: {repair}. This problem and its repair will travel under the name **{concept}**, but the name carries no knowledge the scene has not earned.",
    "The old instrument is not discarded; it is given the one capacity the counterexample demanded: {repair}. That threshold is where **{concept}** enters the story.",
)


MOTIFS = {
    "addition": ("the joining river", "separate contributions meet without losing where they came from"),
    "summation": ("the chorus", "many witnesses contribute to one answer without one silence erasing the rest"),
    "subtraction": ("the chisel", "what is shared is removed so the remaining change can be seen"),
    "multiplication": ("the lock and key", "one influence matters through another, and either missing factor can close the path"),
    "division": ("the fair cup", "a total is judged per person, per step, or per unit rather than admired for being large"),
    "logarithm": ("the spiral stair", "compounded chances become steps that can be accumulated"),
    "exponential": ("the rising flame", "a small score difference becomes positive relative evidence"),
    "negative-sign": ("the turning wind", "an uphill quantity is made to point downhill, or surprise is made to count as cost"),
    "powers": ("the echoing chamber", "large departures return with greater force while opposite signs stop cancelling"),
    "square-root": ("the road home", "a squared construction returns to the scale of the world that created it"),
    "dot-product": ("the meeting of arrows", "matching directions reinforce while opposing directions resist"),
    "partial-derivative": ("the whispered question", "one decision is asked what would change if only it moved"),
    "derivative": ("the whispered question", "the present slope answers how a tiny movement would alter the outcome"),
    "expectation": ("the council of possible worlds", "each future speaks in proportion to how often it may arrive"),
    "maximum": ("the highest lantern", "the strongest surviving possibility sets the visible ceiling"),
    "minimum": ("the narrow gate", "the smaller allowance prevents a promise from exceeding its boundary"),
    "concatenation": ("the binding loom", "distinct pieces remain side by side instead of being blended away"),
    "cosine": ("the returning tide", "movement bends smoothly and reaches its shore without a cliff"),
    "covariance": ("the paired dance", "two quantities reveal whether their departures move together"),
}


CODAS = {
    5: (
        "The first constellation",
        "The valley began with unnamed observations. A feature kept one distinction; a vector kept several; distance turned disagreement into separation; a matrix turned several judgments into one reusable machine. None was a separate school subject. Each was the shape left behind when the earlier tool broke.",
        "observation → feature → vector → distance → transformation",
    ),
    16: (
        "When measurements learned to listen",
        "The instruments of Part I have changed character. Vectors no longer describe only bodies; they hold fragments of meaning. A dot product is no longer only geometry; it becomes relevance. Weighted sums become attention, and layered corrections become a Transformer. The old mathematics did not disappear. It learned a new song.",
        "geometry → relevance → attention → context → emergence",
    ),
    35: (
        "The circle that teaches itself",
        "Uncertainty became information; information became loss; loss became local sensitivity; sensitivities flowed backward; and a chosen step changed the machine. The circle is closed only because every arrow can be walked in ordinary language.",
        "prediction → surprise → loss → blame → update → new prediction",
    ),
    45: (
        "A sentence enters; a future leaves",
        "Characters became tokens, tokens found coordinates, positions supplied order, masks protected honesty, and logits opened a competition among possible next words. The tiny GPT is not one invention. It is a procession of necessities moving through a sentence.",
        "text → tokens → positions → context → probabilities → next token",
    ),
    65: (
        "The mind reaches the gate",
        "Speech became evidence-seeking action, and action demanded authority, state, verification, safe repetition, coordination, and an operating boundary. Intelligence crossed into the world only by learning that capability and permission are different quantities.",
        "answer → evidence → tool → authority → state → proof → boundary",
    ),
    75: (
        "The garden looks back at the watcher",
        "Deployment changed the data that trained the system. Experiments separated cause from coincidence; probes found readable traces; interventions asked which traces actually mattered. The observer has entered the observed world.",
        "action ↺ world → data → representation → intervention → evidence",
    ),
    85: (
        "Light learns a path home",
        "Pixels became neighborhoods, neighborhoods became parts, parts became objects, and compressed coordinates became places from which images could be rebuilt. Diffusion completed the arc by turning destruction into a curriculum for creation.",
        "light → locality → hierarchy → latent space → noise → image",
    ),
    100: (
        "One system, many kinds of consequence",
        "Words, images, rewards, tools, servers, attacks, and institutions now meet in one machine. The equations remain necessary, but none can decide alone what the complete system should be allowed to do.",
        "representation + learning + action + evidence + authority",
    ),
    125: (
        "The hall of worlds opens",
        "Ignorance split into kinds; beliefs learned to update; causes separated from correlations; possible futures became searchable; claims became provable or refutable. The system can now ask a new question without pretending it has already earned the answer.",
        "uncertainty → alternatives → causes → plans → proofs → research",
    ),
    150: (
        "Improvement enters a circle of gates",
        "A proposed change must now survive a hypothesis, experiment, reproduction, adversary, impact review, human authority, staged release, and rollback. Progress is no longer a larger score. It is a claim that remains standing after every relevant way of being wrong has spoken.",
        "proposal → test → opposition → authority → release → reversal",
    ),
    175: (
        "The old mind inside the new engine",
        "The engine has changed its position system, cache, attention kernel, normalization, gate, optimizer, precision, memory plan, and distribution across machines. Yet the reference path remains beside it like a tuning fork: every faster mechanism must still produce the mathematical responsibility first derived in the valley.",
        "reference ──preserved meaning──▶ optimized engine",
    ),
    200: (
        "The mandala returns to observation",
        "The final artifact carries its documents, transformations, budgets, checkpoints, validation, audits, and release decision as evidence. The circle does not close by declaring perfection. It closes by returning every future change to the first law: observe what happened, let failure speak, and invent only what the world makes necessary.",
        "observation → need → mathematics → machine → consequence → observation",
    ),
    225: (
        "The roots return to the living mandala",
        "Sets, spaces, change, uncertainty, evidence, decisions, optimization, and stable computation now form one connected memory. No equation arrived as authority: each became the shortest record of a human repair already reconstructed.",
        "observation → failed idea → necessity → mathematics → machine → observation",
    ),
}


def world_for(number: int) -> tuple[str, str, str]:
    for start, end, place, keeper, object_name in WORLDS:
        if start <= number <= end:
            return place, keeper, object_name
    raise ValueError(number)


def extract_field(paragraph: str, templates: tuple[str, ...], field: str) -> str:
    for template in templates:
        before, after = template.split("{" + field + "}")
        if paragraph.startswith(before) and (not after or paragraph.endswith(after)):
            value = paragraph[len(before):]
            if after:
                value = value[:-len(after)]
            return value.rstrip(". ")
    raise ValueError(f"Cannot recover {field} from: {paragraph}")


def clean_label(value: str, width: int = 38) -> str:
    value = re.sub(r"[`*_]", "", value)
    value = re.sub(r"\[[^\]]+\]\([^\)]+\)", "", value)
    value = compact(value).rstrip(".")
    if len(value) > width:
        value = value[:width].rsplit(" ", 1)[0] + "…"
    return value


def action_phrase(value: str) -> str:
    """Turn a full repair sentence into a phrase that can follow 'to' or 'can'."""
    value = value.strip().rstrip(". ")
    value = re.sub(
        r"^(?:(?:we|the method|the system|the model|the agent)\s+)?(?:now\s+)?need(?:s)?\s+to\s+",
        "",
        value,
        flags=re.I,
    )
    return value


def field_sketch(number: int, attempt: str, failure: str, repair: str) -> str:
    a, f, r = map(clean_label, (attempt, failure, repair))
    realm = next(i for i, (start, end, *_rest) in enumerate(WORLDS) if start <= number <= end)
    style = (realm + number) % 6
    if style == 0:
        drawing = f"""observation
    │
    ▼
[{a}]
    │
    ╳  {f}
    │
    ▼
[{r}]"""
    elif style == 1:
        drawing = f"""             evidence
            /        \\
   old lantern      hidden distinction
   {a:<26} {f}
            \\        /
             \\      /
              {r}"""
    elif style == 2:
        drawing = f"""OLD PATH:  request ──▶ {a} ──▶ {f}
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ {r} ──▶ accountable result"""
    elif style == 3:
        drawing = f"""light / evidence
      │
      ├── old lens ──▶ {a} ──▶ blurred: {f}
      │
      └── new lens ──▶ {r} ──▶ distinction survives"""
    elif style == 4:
        drawing = f"""possible road A ─┐
                 ├── old map: {a}
possible road B ─┘              └── loses: {f}

same roads ──▶ repaired map ──▶ {r}"""
    else:
        drawing = f"""reference evidence ──▶ shortcut: {a}
                         │
                         └── mismatch: {f}

reference evidence ──▶ measured repair: {r}"""
    return f"""*The {keeper_word(number)} sketches the break before changing it:*

```text
{drawing}
```"""


def keeper_word(number: int) -> str:
    return world_for(number)[1]


MOTIF_FRAMES = (
    "Listen beneath {concept}: {motifs}. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.",
    "The calculation borrows several gestures already encountered elsewhere: {motifs}. {concept} feels new because the objects are new; the gestures remain recognizably human.",
    "Three old motions cast new shadows here: {motifs}. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.",
    "The symbols are about to change costume, but their work has appeared before: {motifs}. This is how distant excavations begin to sound like variations of one melody.",
    "Inside {concept}, familiar operations return with stricter duties: {motifs}. The metaphor is useful only as long as it predicts what the operation will do in the worked case.",
    "Trace each operation by touch rather than by name: {motifs}. Together they form the smallest mechanism that survives the counterexample.",
    "The mandala has curved back upon itself. In this chamber we meet {motifs}. What seemed like a new formula is older mathematical instinct arranged around a new need.",
    "The calculation reuses familiar motions: {motifs}. Together they keep the path from the concrete case to notation intact.",
)


def motif_paragraph(text: str, concept: str, number: int) -> str:
    first_equation = text.find("$$")
    if first_equation < 0:
        return text
    before = text[:first_equation]
    anchors = []
    for anchor in re.findall(r"MATHEMATICAL_MOVES\.md#([a-z-]+)", before):
        if anchor in MOTIFS and anchor not in anchors:
            anchors.append(anchor)
    if not anchors:
        return text
    phrases = [f"**{MOTIFS[a][0]}**—{MOTIFS[a][1]}" for a in anchors[:3]]
    if len(phrases) == 1:
        joined = phrases[0]
    else:
        joined = "; ".join(phrases[:-1]) + "; and " + phrases[-1]
    paragraph = MOTIF_FRAMES[number % len(MOTIF_FRAMES)].format(
        concept=concept.lower(), motifs=joined
    )
    insertion_points = (
        "Every symbol in ",
        "The notation is finally shorter than the story that created it:",
        "Every symbol now names an action already performed.",
    )
    positions = [text.find(point) for point in insertion_points if text.find(point) >= 0]
    if not positions:
        return text
    pos = min(positions)
    return text[:pos] + paragraph + "\n\n" + text[pos:]


def add_coda(text: str, number: int) -> str:
    if number not in CODAS:
        return text
    title, prose, chain = CODAS[number]
    coda = f"""## {title}

{prose}

```text
{chain}
```

The trail called *{title.lower()}* is what remains when one necessity becomes another."""
    marker = "\n## Take "
    pos = text.find(marker)
    if pos < 0:
        return text + "\n\n" + coda
    return text[:pos] + "\n\n" + coda + "\n\n" + text[pos:].lstrip()


def polish(text: str, number: int, concept: str) -> str:
    """Remove the last visible lesson scaffolds from a woven chapter."""
    place, keeper, object_name = world_for(number)
    inline_concept = re.sub(r"^(?:A|An|The)\s+", "", concept).strip()

    # The worked case should stand on its own. These paragraphs once explained
    # how to read it; the scene and counterexample now perform that job.
    c = re.escape(concept.lower())
    case_bridge = re.compile(
        rf"\n\n(?:Put the old procedure beside {c}\..*?|Run the {c} scene twice in your head\..*?|"
        rf"The name {c} is still unimportant\..*?|There are now two histories of this {c} case:.*?|"
        rf"Hold the setting, evidence, and desired outcome fixed while testing {c}\..*?|"
        rf"A formula for {c} is not yet needed\..*?)(?=\n\n## )",
        re.S,
    )
    text = case_bridge.sub("", text)

    # Replace commentary about notation with a physical transition from the
    # worked scene into arithmetic.
    math_entry = (
        f"The {keeper} carries the {inline_concept.lower()} scene to the {object_name}. Every quantity already has "
        "a visible owner and every operation already has a job; the symbols will only keep those "
        "moves precise when the calculation is repeated."
    )
    text = re.sub(
        r"(?:Before .*? receives symbols, its procedure must be possible in ordinary language\. "
        r"Notation is useful here only because it lets us repeat that same reasoning without ambiguity\.|"
        r"Do not read the coming .*? line as an instruction dropped from above\. "
        r"Read it from left to right as a compressed record of the concrete decisions already made\.)",
        math_entry,
        text,
    )
    text = text.replace("### Names for pieces we have already used", "### Naming what is already on the table")
    text = text.replace("### Why no cheaper operation does the same job", "### Why the melody needs these exact notes")

    equation_reveals = (
        f"Every mark needed for {inline_concept.lower()} is now visible on the {object_name}. The symbols do not add an idea; they bind the discovered moves into one line:",
        f"The {keeper} reads the journey of {inline_concept.lower()} once more across the {object_name}, then lets the words contract without losing their order:",
        f"Nothing remains unnamed in the {inline_concept.lower()} case on the {object_name}. We can finally trade the long route for its compact map:",
        f"The story of {inline_concept.lower()} has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:",
        f"Every mark in the coming {inline_concept.lower()} equation now belongs to a visible part of the case. The compressed form is:",
        f"The {object_name} already contains the complete {inline_concept.lower()} mechanism. Mathematics gives that mechanism a form small enough to carry:",
    )
    equation_reveal = equation_reveals[number % len(equation_reveals)]
    text = re.sub(
        r"(?:Every symbol in .*? can now be read back into an action already performed\. The whole procedure fits in one line:|"
        r"The notation is finally shorter than the story that created it:|"
        r"Every symbol now names an action already performed\. The whole procedure fits in one line:)",
        equation_reveal,
        text,
    )

    # Keep every genuine limitation paragraph, remove the generic explanation,
    # then let the world's physical blank carry the causal transition forward.
    boundary_pattern = re.compile(r"(^## Where [^\n]+\n\n)(.*?)(?=^## |\Z)", re.M | re.S)
    match = boundary_pattern.search(text)
    if match:
        paragraphs = [p.strip() for p in match.group(2).split("\n\n") if p.strip()]
        old_leads = (
            "The limit follows from",
            "Why does that boundary remain?",
            "The weakness is not an accidental footnote.",
            "Look back at what",
            "This is where",
            "The boundary can be predicted",
        )
        if paragraphs and paragraphs[-1].startswith(old_leads):
            paragraphs.pop()
        closures = (
            f"At {place}, the {keeper} leaves a blank beneath the new mark. {inline_concept} has no operation that can answer it, so the blank—not a promised solution—travels onward.",
            f"The {object_name} answers today's question and falls silent at the next. That silence is precise: {inline_concept} was built to repair one failure, not to pretend every later boundary is already solved.",
            f"A final test reaches beyond the new instrument. It does not refute {inline_concept}; it reveals the edge of what was constructed. The {keeper} carries that edge into the following room.",
            f"One unsolved mark remains on the {object_name}. None of the responsibilities inside {inline_concept} can move it, and so it becomes the observation from which the next excavation must begin.",
            f"The {inline_concept.lower()} repair holds, but the world asks for something it was never given. At {place}, that unmet need is preserved rather than hidden behind a stronger claim.",
            f"Here the new path ends honestly. {inline_concept} can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.",
        )
        closure = closures[number % len(closures)]
        body = "\n\n".join(paragraphs + [closure])
        text = text[:match.start()] + match.group(1) + body + "\n\n" + text[match.end():]

    # The workbench is a change of medium, not another lecture about method.
    workbench_pattern = re.compile(
        r"^## Take [^\n]+ to the workbench\n\n(.*?)(?=^\[Next:|\Z)", re.M | re.S
    )
    match = workbench_pattern.search(text)
    if match:
        paragraphs = [p.strip() for p in match.group(1).split("\n\n") if p.strip()]
        resources = next((p for p in paragraphs if "(mistakes.md)" in p), "")
        lab = (
            f"## Return to the {object_name}\n\n"
            f"Rebuild the {inline_concept.lower()} scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). "
            "Run the tempting rule first and predict its failure on paper. Then change only the responsibility "
            "earned in this excavation and compare every intermediate value. If the repaired path surprises you, "
            "the surprise belongs in the margin before the code is changed."
        )
        if resources:
            lab += "\n\n" + resources
        text = text[:match.start()] + lab + "\n\n" + text[match.end():]

    return re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"


def weave(path: Path) -> bool:
    text = path.read_text()
    if MARKER in text:
        number = int(path.parent.name[:3])
        _title, concept, _subtitle = title_parts(text)
        polished = polish(text, number, concept)
        if polished != text:
            path.write_text(polished)
            return True
        return False
    number = int(path.parent.name[:3])
    _title, concept, _subtitle = title_parts(text)
    inline_concept = re.sub(r"^(?:A|An|The)\s+", "", concept).strip().lower()

    # The foundational chapters already use individually written scenes. Give
    # them returning motifs and milestone codas without replacing their voice.
    if number < 17:
        text = text.replace("<!-- book-prose-v2 -->", "<!-- book-prose-v2 -->\n" + MARKER)
        text = motif_paragraph(text, concept, number)
        text = add_coda(text, number)
        path.write_text(polish(text, number, concept))
        return True

    first_h2 = text.find("\n## ")
    if first_h2 < 0:
        raise ValueError(f"{path}: no chapter body")
    remainder = text[first_h2:].lstrip()
    prefix = text[:first_h2]
    title_line = text.splitlines()[0]
    part_match = re.search(r"(?m)^> \*\*PART .*?(?=\n\n(?!>)|\Z)", prefix, re.S)
    part = part_match.group(0).strip() if part_match else ""

    stripped = re.sub(r"(?m)^# .*\n?", "", prefix, count=1)
    stripped = re.sub(r"<!--.*?-->", "", stripped)
    stripped = re.sub(r"(?m)^>.*\n?", "", stripped)
    paragraphs = [compact(p) for p in stripped.split("\n\n") if compact(p)]
    if len(paragraphs) != 9:
        raise ValueError(f"{path}: expected nine v2 opening paragraphs, found {len(paragraphs)}")

    carry = paragraphs[0]
    attempt = extract_field(paragraphs[1], OPENINGS, "attempt")
    failure = extract_field(paragraphs[3], PRESSURE, "failure")
    repair = extract_field(paragraphs[5], REPAIRS, "repair")
    place, keeper, object_name = world_for(number)
    realm = next(i for i, (start, end, *_rest) in enumerate(WORLDS) if start <= number <= end)

    scene = SCENES[number % len(SCENES)].format(
        place=place,
        keeper=keeper,
        object=object_name,
        attempt=attempt,
    )
    breaking = BREAKS[number % len(BREAKS)].format(
        failure=failure,
        object=object_name,
        keeper=keeper,
    )
    question = QUESTIONS[number % len(QUESTIONS)].format(keeper=keeper, concept=inline_concept)
    overlay = OVERLAYS[number % len(OVERLAYS)].format(
        keeper=keeper,
        object=object_name,
        concept=inline_concept,
        attempt=attempt,
        failure=failure,
        repair=action_phrase(repair),
    )
    reveal = REVEALS[number % len(REVEALS)].format(
        keeper=keeper,
        object=object_name,
        repair=repair,
        concept=concept,
    )
    realm_echo = WORLD_MEMORY[number % len(WORLD_MEMORY)].format(
        object=object_name,
        keeper=keeper,
        concept=inline_concept,
        attempt=attempt,
        failure=failure,
        repair=action_phrase(repair),
    )
    if number == next(start for start, _end, *_rest in WORLDS if start <= number <= _end):
        realm_echo += " " + REALM_ECHOES[realm].format(concept=inline_concept)
    opening = [title_line, "<!-- book-prose-v2 -->", MARKER]
    if part:
        opening.append(part)
    opening.extend([
        carry,
        scene,
        breaking,
        field_sketch(number, attempt, failure, repair),
        overlay,
        question,
        reveal,
        realm_echo,
    ])
    woven = "\n\n".join(opening) + "\n\n" + remainder
    woven = motif_paragraph(woven, concept, number)
    woven = add_coda(woven, number)
    finished = polish(woven, number, concept)
    # Some non-equation chapters have deliberately compact source cases. Give
    # those scenes enough room to make the necessity reversible without
    # inflating every chapter with the same editorial paragraph.
    if len(re.findall(r"\b[\w’-]+\b", finished)) < 500:
        residue = (
            f"Before leaving the {object_name}, the {keeper} tests the new idea backward. Remove the ability to "
            f"{action_phrase(repair)}, and the method falls back to this tempting instruction: {attempt}. "
            f"The old consequence returns—{failure}. Restore the missing ability and that particular contradiction "
            f"disappears. This reversible test is why {inline_concept} belongs to the growing structure rather than "
            "to a list of facts to memorize."
        )
        first_h2 = finished.find("\n## ")
        finished = finished[:first_h2] + "\n\n" + residue + "\n" + finished[first_h2:]
    path.write_text(finished)
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--from-head",
        action="store_true",
        help="rebuild the generated literary layer from the checked-in chapter sources",
    )
    args = parser.parse_args()
    changed = 0
    for path in sorted((ROOT / "excavations").glob("*/README.md")):
        if args.from_head:
            relative = path.relative_to(ROOT).as_posix()
            source = subprocess.run(
                ["git", "show", f"HEAD:{relative}"],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            ).stdout
            path.write_text(source)
        changed += weave(path)
    print(f"Wove mathematical world, visual journey, and returning motifs into {changed} chapters.")
    atlas_builder = ROOT / "tools" / "build_mathematics_atlas.py"
    if atlas_builder.exists():
        subprocess.run([sys.executable, str(atlas_builder)], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
