"""Build a distraction-free reading edition from the excavation sources."""
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).parents[1]
BOOK = ROOT / "book"

VOLUMES = (
    ("VOLUME_I_WE_BUILD_A_MIND.md", 0, 45, "Volume I — We Build a Mind",
     "We begin with nothing but observations. By the final chapter, the same chain of necessities has produced a tiny language model that can learn and generate."),
    ("VOLUME_II_WE_ENTER_THE_WORLD.md", 46, 100, "Volume II — We Let the Mind Enter the World",
     "The model can speak. Now it must earn trust, use evidence and tools, survive deployment, gain new senses, act through consequences, and become an accountable system."),
    ("VOLUME_III_WE_KEEP_LEARNING.md", 101, 150, "Volume III — We Let the Mind Keep Learning",
     "The deployed system meets ignorance, change, causality, proof, privacy, attack, and finally the question of whether it may improve itself."),
    ("VOLUME_IV_WE_REBUILD_THE_ENGINE.md", 151, 175, "Volume IV — We Rebuild the Engine",
     "The research loop has earned the right to propose changes. We return to the tiny language model, freeze one honest baseline, and rebuild its engine one measured bottleneck at a time without surrendering a reference path."),
    ("VOLUME_V_WE_ACCOUNT_FOR_PRETRAINING.md", 176, 200, "Volume V — We Account for Pretraining",
     "The modern engine can run. We now build the accountable factory around it: traceable evidence, explicit curation, budgeted learning, coordinated workers, recoverable state, independent audits, and a report that remains attached to the final artifact."),
)

VOLUME_OVERTURES = {
    0: ("The book opens in a valley where mathematics has no names. Keep watch for one recurring transformation: an observation becomes a mark, the mark becomes a relationship, and the relationship becomes a machine. The tiger crossing the valley is not an example pasted onto a formula; its tracks are the pressure from which the formula will grow.",
        "tracks → marks → relationships → a mind begins"),
    46: ("The constructed mind enters halls where its words affect other lives. Listen for the mathematics of boundaries: probabilities become trust, retrieval becomes evidence, tools become consequences, and every powerful arrow must meet a gate that asks whether it is authorized.",
         "voice → evidence → action → consequence → proof"),
    101: ("The journey turns inward toward ignorance. Mirrored maps cover the Hall of Possible Worlds; some reflect missing knowledge, others irreducible chance. Here mathematics becomes the art of keeping alternatives alive long enough for evidence to separate them.",
          "ignorance → possible worlds → causes → tests → knowledge"),
    151: ("The brass reference machine hums in the Engine Cavern. Every optimization will be offered speed, memory, or scale, but the old machine remains beside it as a tuning fork. A faster path is accepted only when the mathematical responsibility sounds the same note.",
          "reference path ══ measured equivalence ══ optimized path"),
    176: ("The final volume enters the Archive Foundry, where documents become training experience. Nothing may disappear without a trace: sources, filters, mixtures, updates, checkpoints, and release decisions must remain connected by a recoverable chain of evidence.",
          "document → lineage → lesson → update → artifact → account"),
}

PARTS = {
    0: ("Part I — Measuring Reality",
        "A community in the valley can recognize danger but cannot yet compare one observation with another. Counting, features, vectors, distance, and matrices will not arrive as school subjects. Each will be invented because the previous description fails during the same attempt to understand the animals around the camp."),
    6: ("Part II — Inventing Meaning",
        "The community can now store measurements and transformations. Its records contain words, however, and a word changes its work from one sentence to another. The old measuring tools must be turned toward context until meaning, attention, and the Transformer emerge from the pressure."),
    17: ("Part III — Learning from Error",
         "The Transformer can construct a useful interpretation, but it cannot honestly pretend that every interpretation is certain. Footprints, words, and predictions all leave several possible stories alive. The expedition now needs a way to preserve uncertainty, price error, trace responsibility, and let error alter the machine."),
    36: ("Part IV — Building a Tiny GPT",
         "The learner can change its weights when examples are already numerical. Real language does not arrive that way. We now follow one sentence from raw characters to tokens, positions, honest prediction lessons, vocabulary probabilities, and finally generation."),
    46: ("Part V — Making Answers Useful",
         "Our tiny GPT speaks. That is an achievement, but it is not yet a reason to believe or use what it says. The assistant must be measured on unseen language, tested for the work people need, connected to evidence, and given carefully limited ways to reach beyond its memory."),
    56: ("Part VI — Trusting an Acting Machine",
         "A model that only writes can be wrong. A model with tools can make its mistake real. The story therefore moves from capability to authority: what the assistant may do, how hostile text is kept from becoming an instruction, and what evidence proves that a long task actually succeeded."),
    66: ("Part VII — Learning After Deployment",
         "The bounded assistant enters the world, and the world does not stand still. Its recommendations change behavior; seasons change data; updates change the model. To remain trustworthy, the system must detect these loops and then investigate which internal causes genuinely drive its decisions."),
    76: ("Part VIII — Seeing and Creating",
         "Language is only one trace of the valley. Cameras bring grids of colored light, and the assistant cannot understand them by pretending they are sentences. We begin again from the observation itself, then reuse the deeper principles already earned: locality, hierarchy, attention, compression, and gradual generation."),
    86: ("Part IX — Acting and Scaling",
         "The system can describe and create, but action supplies no correct next token. It supplies consequences. We follow that new kind of evidence from rewards and future value through multimodal alignment, efficient adaptation, large-scale training, live service, adversarial testing, and governance."),
    101: ("Part X — Learning What We Still Do Not Know",
          "A complete deployed system still faces two dangerous words: ‘I’m uncertain.’ Sometimes the world is genuinely ambiguous; sometimes the model simply has not learned enough. Separating those cases opens a longer journey through updating, continual learning, causal imagination, planning, proof, privacy, and robust research."),
    126: ("Part XI — Earning the Right to Improve",
          "The research system can now propose changes to itself. That power does not grant permission to deploy them. Every proposed improvement must become a falsifiable claim, survive controlled and reproducible tests, resist contaminated metrics and strategic gaming, and remain subject to human authority and rollback."),
    151: ("Part XII — Rebuilding the Engine Without Breaking the System",
          "The bounded loop gives us permission to improve—not permission to guess. We freeze the tiny language model, measure where its time and memory go, and replace one bottleneck at a time while the original path remains available to challenge every faster one."),
    176: ("Part XIII — A Pretraining Factory We Can Account For",
          "The model is modern but still empty of trustworthy experience. We follow one named corpus from its source documents through boundaries, curation, mixture decisions, compute budgets, distributed training, recovery, validation, memorization audits, and a reversible release."),
}

SUPPORT_HEADINGS = (
    "Enter the laboratory", "Implementation", "Test what you believe", "Exercises",
    "Challenge", "Before you leave the excavation", "Carry the discovery forward",
    "Connections", "What this discovery now makes possible", "Continue the dig",
)

SCAFFOLD_HEADINGS = (
    "From procedure to notation", "The arithmetic we have earned",
    "Only now do the symbols earn names", "Let the case decide",
    "The boundary of the discovery", "Carry the idea back into the world",
    "Next Need", "What the next excavation needs",
    "Let one run decide", "What this repair cannot do",
)


def chapter_for_book(path):
    text = path.read_text().strip()
    number = int(path.parent.name[:3])
    text = re.sub(r"^> \*\*PART .*?(?=\n\n)", "", text, flags=re.M | re.S)
    text = re.sub(r"^<!-- .*? -->\n*", "", text, flags=re.M)
    text = re.sub(r"^\[(?:Previous|Next)[^\n]*$", "", text, flags=re.M)
    for heading in SUPPORT_HEADINGS:
        text = re.sub(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", "", text, flags=re.M | re.S)
    # In the dig-site edition these labels help readers find a derivation or
    # limit quickly. In the continuous edition they expose the lesson template,
    # so the prose is allowed to flow without them.
    for heading in SCAFFOLD_HEADINGS:
        text = re.sub(rf"^##+ {re.escape(heading)}\n", "", text, flags=re.M)
    text = re.sub(
        r"^The equation is not the discovery\. It is the shortest record of the discovery already reconstructed above\.\n?",
        "",
        text,
        flags=re.M,
    )
    text = text.replace(
        "Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.\n",
        "",
    )
    text = text.replace(
        "That boundary is the opening condition of the next excavation.\n",
        "",
    )
    text = text.replace(
        "The standard name arrives only after the reader can point to the information the earlier design lost.\n",
        "",
    )
    text = text.replace(
        "That limit supplies the next excavation's opening condition.\n",
        "",
    )
    # Volume title (H1) → part (H2) → excavation (H3) → chapter sections.
    text = re.sub(r"^(#{1,4}) ", lambda m: "#" * (len(m.group(1)) + 2) + " ", text, flags=re.M)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    text = text.replace("../../MATHEMATICAL_MOVES.md", "../MATHEMATICAL_MOVES.md")
    text = text.replace("../../MATHEMATICS_ATLAS.md", "../MATHEMATICS_ATLAS.md")
    link = path.relative_to(ROOT).as_posix()
    return text + f"\n\n*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../{link}).*"


def build_volume(filename, start, end, title, introduction):
    volume_parts = [(number, value) for number, value in PARTS.items() if start <= number <= end]
    overture, overture_map = VOLUME_OVERTURES[start]
    out = [f"# {title}", "", introduction, "",
           "One discovery will create the need for the next; the object under construction never resets.", "",
           "## Overture", "", overture, "", "```text", overture_map, "```", "",
           "In this volume:", ""]
    out.extend(f"- [{part_title}](#{slug(part_title)})" for _, (part_title, _) in volume_parts)
    for path in sorted((ROOT / "excavations").glob("*/README.md")):
        number = int(path.parent.name[:3])
        if start <= number <= end:
            if number in PARTS:
                part_title, part_intro = PARTS[number]
                out.extend(["", "---", "", f"## {part_title}", "", part_intro])
            out.extend(["", "---", "", chapter_for_book(path)])
    return "\n".join(out).rstrip() + "\n"


def slug(title):
    return re.sub(r"[^a-z0-9 -]", "", title.lower()).replace(" ", "-")


def outputs():
    result = {}
    for args in VOLUMES:
        result[BOOK / args[0]] = build_volume(*args)
    result[BOOK / "README.md"] = """# Read AI Archaeology as a Book

The excavation folders are workshops. These five volumes are the uninterrupted
reading edition. Supporting code, diagrams, mistakes, exercises, and references
remain beside the chapter they belong to and are linked at the end of each
chapter.

1. [Volume I — We Build a Mind](VOLUME_I_WE_BUILD_A_MIND.md)
2. [Volume II — We Let the Mind Enter the World](VOLUME_II_WE_ENTER_THE_WORLD.md)
3. [Volume III — We Let the Mind Keep Learning](VOLUME_III_WE_KEEP_LEARNING.md)
4. [Volume IV — We Rebuild the Engine](VOLUME_IV_WE_REBUILD_THE_ENGINE.md)
5. [Volume V — We Account for Pretraining](VOLUME_V_WE_ACCOUNT_FOR_PRETRAINING.md)

For equation-focused review after deriving the ideas, use the
[Mathematical Gist](../MATHEMATICAL_GIST.md).

For a reusable understanding of why a formula adds, multiplies, divides,
squares, exponentiates, logs, maximizes, or differentiates, use
[Mathematical Moves](../MATHEMATICAL_MOVES.md).

To see every earned equation as one connected memory, enter the
[living Mathematical Mandala](../math-mandala/README.md).

To remember the recurring places and mathematical motions that bind the five
volumes into one imaginative journey, begin with
[The Living Mathematics](../THE_LIVING_MATHEMATICS.md).

To revisit the chapters as calculus, probability, linear algebra, information
theory, optimization, discrete mathematics, numerical analysis, and their
neighboring families, use the [Mathematics Atlas](../MATHEMATICS_ATLAS.md).
"""
    return result


parser = argparse.ArgumentParser()
parser.add_argument("--check", action="store_true")
args = parser.parse_args()
generated = outputs()

if args.check:
    stale = [str(path) for path, content in generated.items() if not path.exists() or path.read_text() != content]
    if stale:
        raise SystemExit("Continuous book is stale:\n" + "\n".join(stale))
    print("Continuous reading edition matches all excavation sources.")
else:
    BOOK.mkdir(exist_ok=True)
    for path, content in generated.items():
        path.write_text(content)
    print("Built the five-volume continuous reading edition.")
