"""Label every excavation by mathematical lineage and build the Mathematics Atlas."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import argparse
import re


ROOT = Path(__file__).parents[1]
ATLAS = ROOT / "MATHEMATICS_ATLAS.md"
MARKER = "<!-- mathematical-lineage-v1 -->"


FAMILIES = {
    "foundations": (
        "Mathematical Foundations & Measurement",
        "What counts as an object, distinction, comparison, or trustworthy measurement?",
    ),
    "linear-algebra": (
        "Linear Algebra & Geometry",
        "Vectors, spaces, transformations, projections, similarity, and learned coordinates.",
    ),
    "calculus": (
        "Calculus & Differential Change",
        "Local sensitivity, gradients, composition, curvature, and accumulated change.",
    ),
    "probability": (
        "Probability & Statistics",
        "Uncertainty, distributions, sampling, estimation, variation, and evidence from data.",
    ),
    "information": (
        "Information Theory",
        "Surprise, entropy, compression, prediction cost, and the value of distinctions.",
    ),
    "optimization": (
        "Optimization",
        "Turning measured error into a controlled search for better parameters or decisions.",
    ),
    "discrete": (
        "Discrete Mathematics, Logic & Algorithms",
        "Sets, rules, masks, states, search, proofs, programs, and finite procedures.",
    ),
    "graphs": (
        "Graphs & Relational Structures",
        "Nodes, edges, paths, message passing, dependency, and coordinated relationships.",
    ),
    "numerical": (
        "Numerical Analysis & Scientific Computing",
        "How finite machines approximate, store, rearrange, and accelerate mathematical work.",
    ),
    "dynamics": (
        "Dynamical Systems, Control & Decision Theory",
        "States changing through time, feedback, planning, action, stability, and consequence.",
    ),
    "causality": (
        "Causality & Experimental Design",
        "Separating causes from coincidences through interventions, controls, and counterfactuals.",
    ),
}


# These defaults express the mathematical atmosphere of each causal arc. Title
# rules below bring the most chapter-specific roots to the front.
ARC_ROOTS = (
    (0, 5, ("foundations", "linear-algebra")),
    (6, 16, ("linear-algebra", "information")),
    (17, 21, ("probability", "information")),
    (22, 25, ("calculus", "optimization")),
    (26, 35, ("optimization", "probability", "calculus")),
    (36, 45, ("discrete", "linear-algebra", "probability")),
    (46, 55, ("probability", "information", "foundations")),
    (56, 65, ("discrete", "foundations", "graphs")),
    (66, 75, ("causality", "dynamics", "probability")),
    (76, 85, ("linear-algebra", "numerical", "probability")),
    (86, 90, ("dynamics", "probability", "optimization")),
    (91, 100, ("linear-algebra", "numerical", "foundations")),
    (101, 110, ("probability", "optimization", "information")),
    (111, 125, ("discrete", "causality", "probability")),
    (126, 150, ("foundations", "causality", "probability")),
    (151, 175, ("numerical", "linear-algebra", "optimization")),
    (176, 200, ("foundations", "probability", "numerical")),
    (201, 225, ("foundations", "linear-algebra", "calculus", "probability", "discrete", "dynamics", "optimization", "numerical")),
)


TERRITORIES = (
    (0, 16, "Foundations and representation"),
    (17, 35, "Learning from uncertainty and error"),
    (36, 55, "Language models and useful answers"),
    (56, 65, "Agents and reliable action"),
    (66, 75, "Learning in the world and interpretability"),
    (76, 85, "Vision and generative models"),
    (86, 100, "Decision-making, scaling, and accountable systems"),
    (101, 125, "Continual learning, reasoning, and research"),
    (126, 150, "Scientific self-improvement and oversight"),
    (151, 175, "Model systems and engine optimization"),
    (176, 200, "Data and pretraining operations"),
    (201, 225, "Mathematical roots beneath the machine"),
)


TITLE_RULES = (
    ("graphs", r"graph|multi-agent|knowledge graph|dependency"),
    ("causality", r"causal|counterfactual|experiment|intervention|attribution|hypoth|contamination|benchmark|reproduc|validation|evaluation|red team|audit|oversight|debate"),
    ("dynamics", r"feedback|online learning|state|transition|planning|world model|tree search|reward|value|q-learning|policy gradient|bandit|control|retries|resume|loss spike"),
    ("calculus", r"derivative|chain rule|backprop|gradient|activation|jacobian|hessian|differential"),
    ("optimization", r"gradient descent|learning rate|momentum|initialization|regularization|adam|warmup|decay|clipping|training|compute-optimal|self-improv|pre-normal|swiglu"),
    ("information", r"meaning|entropy|cross-entropy|information|perplexity|compression|autoencoder|latent|retrieval|token|memorization|deduplication|quality filtering|distillation"),
    ("probability", r"probability|likelihood|sampling|uncertainty|calibration|ensemble|bayesian|distribution|mini-batch|mixture|noise|diffusion|denoising|preference|selective|privacy|language identification"),
    ("linear-algebra", r"feature|vector|distance|matri|embedding|attention|query|key|value|logit|linear|convolution|pooling|pixel|vision|multimodal|low-rank|lora|rotary|position|norm|weight tying|tensor"),
    ("numerical", r"quantization|precision|scaling|profil|pipeline|packing|cache|flash|checkpoint|shard|parallel|serving|accumulation|sequence|compute|factory"),
    ("discrete", r"tokenization|mask|context window|tool|authority|injection|memory|state machine|verification|idempot|coordination|bounded|search|logic|symbolic|program|formal|sparse|manifest|boundar|provenance|report|governance"),
    ("foundations", r"before mathematics|measurement|feature|generalization|data quality|evaluation|observability|governance|impact|human|constitutional|report|provenance|quality|baseline"),
)


# A few titles use general words whose chapter has a more precise mathematical
# home than keyword matching alone can express.
EXACT = {
    3: ("linear-algebra", "foundations"),
    9: ("probability", "information", "linear-algebra"),
    13: ("numerical", "linear-algebra", "optimization"),
    14: ("probability", "numerical", "linear-algebra"),
    18: ("probability", "causality"),
    19: ("information", "probability"),
    20: ("information", "probability"),
    21: ("information", "probability", "optimization"),
    24: ("calculus", "graphs", "optimization"),
    31: ("probability", "optimization", "foundations"),
    33: ("causality", "probability", "foundations"),
    34: ("probability", "foundations"),
    43: ("probability", "information", "discrete"),
    46: ("information", "probability"),
    49: ("probability", "foundations"),
    51: ("probability", "optimization", "foundations"),
    53: ("probability", "optimization", "information"),
    66: ("dynamics", "causality"),
    68: ("probability", "causality", "foundations"),
    70: ("probability", "dynamics", "optimization"),
    74: ("linear-algebra", "information"),
    84: ("probability", "calculus", "numerical"),
    85: ("probability", "information", "numerical"),
    88: ("dynamics", "probability"),
    89: ("dynamics", "optimization", "probability"),
    90: ("probability", "calculus", "optimization"),
    92: ("information", "linear-algebra", "probability"),
    95: ("numerical", "linear-algebra"),
    101: ("probability", "information"),
    102: ("probability", "causality"),
    112: ("causality", "probability"),
    113: ("causality", "probability", "dynamics"),
    118: ("graphs", "discrete"),
    119: ("graphs", "linear-algebra", "optimization"),
    121: ("discrete", "foundations"),
    122: ("probability", "information", "optimization"),
    127: ("causality", "probability", "foundations"),
    133: ("probability", "discrete", "optimization"),
    140: ("dynamics", "optimization", "foundations"),
    143: ("probability", "dynamics"),
    144: ("dynamics", "foundations"),
    155: ("linear-algebra", "dynamics", "numerical"),
    156: ("linear-algebra", "numerical"),
    160: ("numerical", "linear-algebra", "discrete"),
    165: ("optimization", "probability", "numerical"),
    166: ("optimization", "numerical"),
    167: ("optimization", "numerical", "calculus"),
    187: ("optimization", "numerical", "probability"),
    190: ("probability", "optimization", "numerical"),
    198: ("information", "probability", "causality"),
    201: ("discrete", "foundations"),
    202: ("discrete", "graphs", "foundations"),
    203: ("foundations", "discrete"),
    204: ("linear-algebra", "foundations"),
    205: ("linear-algebra", "foundations"),
    206: ("linear-algebra", "dynamics"),
    207: ("linear-algebra", "foundations"),
    208: ("linear-algebra", "numerical"),
    209: ("calculus", "foundations"),
    210: ("calculus", "optimization"),
    211: ("calculus", "linear-algebra"),
    212: ("calculus", "optimization"),
    213: ("calculus", "numerical"),
    214: ("calculus", "foundations"),
    215: ("linear-algebra", "numerical"),
    216: ("probability", "foundations"),
    217: ("probability", "foundations"),
    218: ("probability", "linear-algebra"),
    219: ("probability", "foundations"),
    220: ("probability", "foundations"),
    221: ("probability", "causality"),
    222: ("probability", "dynamics"),
    223: ("dynamics", "optimization", "discrete"),
    224: ("optimization", "foundations"),
    225: ("numerical", "foundations"),
}


def title_of(text: str) -> str:
    return text.splitlines()[0].removeprefix("# ").strip()


def arc_roots(number: int) -> tuple[str, ...]:
    return next(roots for start, end, roots in ARC_ROOTS if start <= number <= end)


def territory(number: int) -> str:
    return next(name for start, end, name in TERRITORIES if start <= number <= end)


def classify(number: int, title: str) -> tuple[str, ...]:
    if number in EXACT:
        return EXACT[number]
    lowered = title.lower()
    ordered = []
    for family, pattern in TITLE_RULES:
        if re.search(pattern, lowered) and family not in ordered:
            ordered.append(family)
    if len(ordered) >= 2:
        return tuple(ordered[:3])
    for family in arc_roots(number):
        if family not in ordered:
            ordered.append(family)
    return tuple(ordered[:2] if len(ordered) > 1 else ordered)


def label_line(number: int, families: tuple[str, ...]) -> str:
    links = " · ".join(
        f"[{FAMILIES[key][0]}](../../MATHEMATICS_ATLAS.md#{key})" for key in families
    )
    return (
        f"{MARKER}\n"
        f"> **Mathematical roots:** {links}\n"
        f">\n"
        f"> **Applied territory:** {territory(number)}"
    )


def labelled(text: str, number: int, families: tuple[str, ...]) -> str:
    text = re.sub(
        rf"\n+{re.escape(MARKER)}\n> \*\*Mathematical roots:\*\*[^\n]*\n(?:>\n)?> \*\*Applied territory:\*\*[^\n]*",
        "",
        text,
    )
    anchor = "<!-- mathematical-world-v1 -->"
    if anchor not in text:
        raise ValueError(f"Chapter {number:03d} has no mathematical-world marker")
    return text.replace(anchor, anchor + "\n\n" + label_line(number, families), 1)


def atlas(chapters: list[tuple[int, str, Path, tuple[str, ...]]]) -> str:
    clustered = defaultdict(list)
    for chapter in chapters:
        for family in chapter[3]:
            clustered[family].append(chapter)

    out = [
        "# Mathematics Atlas",
        "",
        "The book order answers **why did the next idea become necessary?** This atlas answers a different question: **which mathematical family am I learning?** Keep the excavation order for discovery; use these clusters for revision, comparison, and building a traditional mathematics map in your mind.",
        "",
        "A chapter may appear in several families because real AI does not respect classroom walls. Attention is simultaneously geometry, probability, and information; backpropagation is calculus moving through a computational graph; diffusion joins probability, differential change, and numerical approximation.",
        "",
        "## The families at a glance",
        "",
        "| Mathematical family | Chapters using it | Question it teaches us to ask |",
        "|---|---:|---|",
    ]
    for key, (name, description) in FAMILIES.items():
        out.append(f"| [{name}](#{key}) | {len(clustered[key])} | {description} |")

    for key, (name, description) in FAMILIES.items():
        out.extend(["", f"<a id=\"{key}\"></a>", f"## {name}", "", description, ""])
        for number, title, path, roots in clustered[key]:
            relative = path.relative_to(ROOT).as_posix()
            other = [FAMILIES[root][0] for root in roots if root != key]
            suffix = f" — *also: {', '.join(other)}*" if other else ""
            out.append(f"- **{number:03d}** [{title.replace(f'Excavation {number:03d} — ', '')}]({relative}){suffix}")

    out.extend([
        "",
        "## Chronological lineage index",
        "",
        "This table keeps the causal reading order while exposing the mathematical threads crossing it.",
        "",
        "| # | Excavation | Mathematical roots | Applied territory |",
        "|---:|---|---|---|",
    ])
    for number, title, path, roots in chapters:
        relative = path.relative_to(ROOT).as_posix()
        names = " · ".join(FAMILIES[root][0] for root in roots)
        short = title.replace(f"Excavation {number:03d} — ", "")
        out.append(f"| {number:03d} | [{short}]({relative}) | {names} | {territory(number)} |")
    return "\n".join(out).rstrip() + "\n"


def outputs() -> tuple[dict[Path, str], list[tuple[int, str, Path, tuple[str, ...]]]]:
    generated = {}
    chapters = []
    for path in sorted((ROOT / "excavations").glob("*/README.md")):
        number = int(path.parent.name[:3])
        text = path.read_text()
        title = title_of(text)
        families = classify(number, title)
        chapters.append((number, title, path, families))
        generated[path] = labelled(text, number, families)
    if [number for number, *_ in chapters] != list(range(226)):
        raise ValueError("Expected one continuous sequence from Excavation 000 through 225")
    generated[ATLAS] = atlas(chapters)
    return generated, chapters


parser = argparse.ArgumentParser()
parser.add_argument("--check", action="store_true")
args = parser.parse_args()
generated, chapters = outputs()

if args.check:
    stale = [str(path) for path, content in generated.items() if not path.exists() or path.read_text() != content]
    if stale:
        raise SystemExit("Mathematics Atlas is stale:\n" + "\n".join(stale))
    print(f"Verified mathematical lineage labels across {len(chapters)} excavations.")
else:
    for path, content in generated.items():
        path.write_text(content)
    print(f"Labelled {len(chapters)} excavations and built MATHEMATICS_ATLAS.md.")
