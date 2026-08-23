"""Build the living mathematical mandala from the excavation sources.

Displayed equations become clickable nodes. Links to MATHEMATICAL_MOVES decide
which conceptual neighborhood surrounds each node, so future equations extend
the mandala without a hand-maintained graph.
"""
from __future__ import annotations

import argparse
import html
import json
import math
import re
from pathlib import Path


ROOT = Path(__file__).parents[1]
OUTPUT = ROOT / "math-mandala"
GITHUB_ROOT = "https://github.com/kleem-labs/AI-Archaeology/blob/main"
MANDALA_URL = "https://kleem-labs.github.io/AI-Archaeology/math-mandala/"
RAW_MANDALA_URL = "https://raw.githubusercontent.com/kleem-labs/AI-Archaeology/main/math-mandala/math-mandala.svg"
EQUATION = re.compile(r"\$\$(.*?)\$\$", re.S)
MOVE_LINK = re.compile(r"MATHEMATICAL_MOVES\.md#([a-z0-9-]+)")

FAMILIES = (
    {
        "id": "organize", "name": "Name & Organize", "color": "#8bd3dd",
        "question": "What kind of thing is this, and how do its pieces stay addressable?",
        "moves": ("equals", "brackets", "indices", "symbol-decorations",
                  "cardinality", "membership", "arrows",
                  "function-application", "tuples", "tables"),
    },
    {
        "id": "compare", "name": "Compare & Measure", "color": "#a9def9",
        "question": "What changed, how far apart are two observations, and what direction survives?",
        "moves": ("subtraction", "absolute-value", "powers", "square-root",
                  "difference-and-delta", "inequalities", "approximation"),
    },
    {
        "id": "combine", "name": "Combine Evidence", "color": "#cdb4db",
        "question": "Which contributions belong in one answer, and which relationships must interact?",
        "moves": ("addition", "summation", "multiplication", "dot-product",
                  "concatenation", "function-composition"),
    },
    {
        "id": "share", "name": "Share & Normalize", "color": "#ffd6a5",
        "question": "How do totals become fair shares, averages, or comparable scales?",
        "moves": ("division", "mean", "normalization", "norm", "proportionality"),
    },
    {
        "id": "reshape", "name": "Reshape Scale", "color": "#ffadad",
        "question": "How can scale change without discarding the relationship we care about?",
        "moves": ("exponential", "logarithm", "negative-sign", "cosine", "rounding"),
    },
    {
        "id": "choose", "name": "Choose & Constrain", "color": "#fdffb6",
        "question": "Which candidate wins, and which possibilities remain allowed?",
        "moves": ("maximum", "minimum", "arg-max", "cases", "union",
                  "intersection", "replacement", "logical-and"),
    },
    {
        "id": "sensitivity", "name": "Describe Sensitivity", "color": "#bde0fe",
        "question": "If this changes slightly, what moves downstream and by how much?",
        "moves": ("limit", "derivative", "partial-derivative", "gradient"),
    },
    {
        "id": "uncertainty", "name": "Reason Under Uncertainty", "color": "#caffbf",
        "question": "Which possibilities remain alive, and how strongly should each count?",
        "moves": ("probability", "conditional-bar", "expectation", "variance",
                  "covariance", "trace"),
    },
)

FAMILY_BY_MOVE = {
    move: family["id"] for family in FAMILIES for move in family["moves"]
}
FAMILY_LOOKUP = {family["id"]: family for family in FAMILIES}
MOVE_PRIORITY = {
    move: family_index * 100 + move_index
    for family_index, family in enumerate(FAMILIES)
    for move_index, move in enumerate(family["moves"])
}


def display_move(anchor: str) -> str:
    return {"arg-max": "arg max", "logical-and": "logical and"}.get(
        anchor, anchor.replace("-", " ")
    )


def family_label_lines(name: str) -> tuple[str, str]:
    lines = {
        "Name & Organize": ("Name &", "Organize"),
        "Compare & Measure": ("Compare &", "Measure"),
        "Combine Evidence": ("Combine", "Evidence"),
        "Share & Normalize": ("Share &", "Normalize"),
        "Reshape Scale": ("Reshape", "Scale"),
        "Choose & Constrain": ("Choose &", "Constrain"),
        "Describe Sensitivity": ("Describe", "Sensitivity"),
        "Reason Under Uncertainty": ("Reason Under", "Uncertainty"),
    }
    return lines[name]


def compact_equation(source: str, limit: int = 180) -> str:
    text = re.sub(r"\s+", " ", source.strip())
    return text if len(text) <= limit else text[: limit - 1] + "…"


def family_for(title: str, moves: list[str], frequencies: dict[str, int]) -> str:
    lower = title.lower()
    overrides = (
        ("uncertainty", ("probability", "likelihood", "information", "entropy",
                         "perplexity", "calibration", "bayesian", "uncertainty",
                         "covariance")),
        ("sensitivity", ("derivative", "chain rule", "backprop", "gradient",
                         "learning rate", "momentum", "adam")),
        ("compare", ("distance", "similarity", "geometry", "vectors as change")),
    )
    for family, words in overrides:
        if any(word in lower for word in words):
            return family
    present = [move for move in moves if move in FAMILY_BY_MOVE]
    if not present:
        return "organize"
    chosen = min(
        present,
        key=lambda move: (frequencies.get(move, 0), -MOVE_PRIORITY[move]),
    )
    return FAMILY_BY_MOVE[chosen]


def collect() -> dict:
    sources = []
    frequencies = {}
    for path in sorted((ROOT / "excavations").glob("*/README.md")):
        text = path.read_text()
        moves = list(dict.fromkeys(MOVE_LINK.findall(text)))
        for move in set(moves):
            frequencies[move] = frequencies.get(move, 0) + 1
        sources.append((path, text, moves))

    chapters = []
    equations = []
    used_moves = set()
    for path, text, linked_moves in sources:
        blocks = EQUATION.findall(text)
        if not blocks:
            continue
        number = int(path.parent.name[:3])
        title_match = re.search(r"^# (.+)$", text, re.M)
        title = title_match.group(1) if title_match else path.parent.name
        moves = [move for move in linked_moves if move in FAMILY_BY_MOVE]
        used_moves.update(moves)
        family = family_for(title, moves, frequencies)
        relative = path.relative_to(ROOT).as_posix()
        chapters.append({
            "number": number, "title": title, "path": relative,
            "family": family, "moves": moves, "equation_count": len(blocks),
        })
        for index, block in enumerate(blocks, 1):
            equations.append({
                "id": f"equation-{number:03d}-{index}",
                "number": number,
                "index": index,
                "label": f"{number:03d}" if len(blocks) == 1 else f"{number:03d}.{index}",
                "title": title,
                "equation": compact_equation(block),
                "path": relative,
                "family": family,
                "moves": moves,
            })

    operations = []
    for family in FAMILIES:
        for move in family["moves"]:
            if move in used_moves:
                operations.append({
                    "id": f"move-{move}",
                    "anchor": move,
                    "name": display_move(move),
                    "family": family["id"],
                    "path": f"MATHEMATICAL_MOVES.md#{move}",
                })
    return {
        "version": 1,
        "families": [dict(family) for family in FAMILIES],
        "operations": operations,
        "chapters": chapters,
        "equations": equations,
        "counts": {
            "chapters": len(chapters),
            "equations": len(equations),
            "operations": len(operations),
        },
    }


def polar(radius: float, angle: float) -> tuple[float, float]:
    radians = math.radians(angle)
    return 1100 + radius * math.cos(radians), 1100 + radius * math.sin(radians)


def positions(data: dict) -> dict:
    sector = 360 / len(FAMILIES)
    result = {"families": {}, "operations": {}, "equations": {}}
    for family_index, family in enumerate(FAMILIES):
        centre = -90 + family_index * sector
        start, end = centre - sector / 2 + 5, centre + sector / 2 - 5
        result["families"][family["id"]] = (*polar(245, centre), centre)

        moves = [m for m in data["operations"] if m["family"] == family["id"]]
        for index, move in enumerate(moves):
            per_ring = 3
            ring = index // per_ring
            batch = moves[ring * per_ring : (ring + 1) * per_ring]
            within = index % per_ring
            angle = start + (within + 0.5) / len(batch) * (end - start)
            result["operations"][move["anchor"]] = (
                *polar(360 + ring * 78, angle), angle
            )

        nodes = [n for n in data["equations"] if n["family"] == family["id"]]
        per_ring = 13
        for index, node in enumerate(nodes):
            ring = index // per_ring
            batch = nodes[ring * per_ring : (ring + 1) * per_ring]
            within = index % per_ring
            angle = start + (within + 0.5) / len(batch) * (end - start)
            result["equations"][node["id"]] = (
                *polar(680 + ring * 115, angle), angle
            )
    return result


def curve(start: tuple[float, float], end: tuple[float, float], bend=.48) -> str:
    x1, y1 = start
    x2, y2 = end
    cx = 1100 + ((x1 + x2) / 2 - 1100) * bend
    cy = 1100 + ((y1 + y2) / 2 - 1100) * bend
    return f"M {x1:.1f},{y1:.1f} Q {cx:.1f},{cy:.1f} {x2:.1f},{y2:.1f}"


def svg_document(data: dict) -> str:
    pos = positions(data)
    out = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2200 2200" role="img" aria-labelledby="mandala-title mandala-description">',
        '<title id="mandala-title">AI Archaeology Mathematical Mandala</title>',
        f'<desc id="mandala-description">A clickable map of {data["counts"]["equations"]} equations grouped by the human needs that forced them to exist.</desc>',
        '<style>',
        '.bg{fill:#090d20}.ring{fill:none;stroke:#d8c27a;stroke-opacity:.14;stroke-width:2}.spoke{fill:none;stroke:#dbe7ff;stroke-opacity:.12;stroke-width:1.5}.thread{fill:none;stroke:#f4cf75;stroke-opacity:.18;stroke-width:1.7;stroke-dasharray:3 7}.family-edge{stroke-width:2.3;stroke-opacity:.3}.family-node{stroke:#fff8df;stroke-width:2.5}.move-node{fill:#111936;stroke-width:2}.equation-node{stroke:#fff;stroke-opacity:.82;stroke-width:1.2}.node:hover{stroke:#fff;stroke-width:4;filter:url(#glow)}.family-label{fill:#f8f3e6;font:600 18px ui-sans-serif,system-ui;text-anchor:middle}.move-label{fill:#eef3ff;font:500 12px ui-sans-serif,system-ui;text-anchor:middle}.eq-label{fill:#091020;font:700 9px ui-monospace,monospace;text-anchor:middle;dominant-baseline:central}.title{fill:#fff8df;font:700 32px ui-serif,Georgia,serif;text-anchor:middle;letter-spacing:1px}.subtitle{fill:#b8c5e2;font:400 15px ui-sans-serif,system-ui;text-anchor:middle}.heart{fill:#f4cf75;font:700 38px ui-serif,Georgia,serif;text-anchor:middle}.legend{fill:#bdc9e5;font:400 14px ui-sans-serif,system-ui}.legend-strong{fill:#fff8df;font:600 15px ui-sans-serif,system-ui}',
        '</style>',
        '<defs><filter id="glow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>',
        '<rect class="bg" width="2200" height="2200" rx="28"/>',
    ]
    for radius in (155, 245, 360, 438, 516, 594, 680, 795, 910, 1025):
        out.append(f'<circle class="ring" cx="1100" cy="1100" r="{radius}"/>')

    ordered = sorted(data["equations"], key=lambda item: (item["number"], item["index"]))
    for previous, following in zip(ordered, ordered[1:]):
        a = pos["equations"][previous["id"]][:2]
        b = pos["equations"][following["id"]][:2]
        out.append(f'<path class="thread" d="{curve(a, b, .72)}"/>')

    for family in FAMILIES:
        fx, fy, _ = pos["families"][family["id"]]
        for move in [m for m in data["operations"] if m["family"] == family["id"]]:
            mx, my, _ = pos["operations"][move["anchor"]]
            out.append(
                f'<path class="spoke family-edge" stroke="{family["color"]}" '
                f'd="{curve((fx, fy), (mx, my))}"/>'
            )

    frequencies = {
        move["anchor"]: sum(move["anchor"] in item["moves"] for item in data["chapters"])
        for move in data["operations"]
    }
    for node in data["equations"]:
        available = [move for move in node["moves"] if move in pos["operations"]]
        if not available:
            continue
        primary = min(
            available,
            key=lambda move: (frequencies[move], -MOVE_PRIORITY[move]),
        )
        mx, my, _ = pos["operations"][primary]
        ex, ey, _ = pos["equations"][node["id"]]
        color = FAMILY_LOOKUP[node["family"]]["color"]
        out.append(
            f'<path class="spoke" stroke="{color}" '
            f'd="{curve((mx, my), (ex, ey), .58)}"/>'
        )

    out.extend([
        f'<a href="{GITHUB_ROOT}/MATHEMATICAL_GIST.md">',
        '<circle class="node family-node" cx="1100" cy="1100" r="122" fill="#111936"/><title>Open the Mathematical Gist</title>',
        '<text class="heart" x="1100" y="1067">♥</text>',
        '<text class="title" x="1100" y="1109">OBSERVATION</text>',
        '<text class="subtitle" x="1100" y="1138">need → move → equation</text>',
        '</a>',
    ])

    for family in FAMILIES:
        x, y, _ = pos["families"][family["id"]]
        count = sum(n["family"] == family["id"] for n in data["equations"])
        first_line, second_line = family_label_lines(family["name"])
        out.append(
            f'<a href="{GITHUB_ROOT}/MATHEMATICAL_MOVES.md#map-of-the-moves">'
            f'<circle class="node family-node" cx="{x:.1f}" cy="{y:.1f}" r="70" '
            f'fill="{family["color"]}" fill-opacity=".14"/>'
            f'<title>{html.escape(family["question"])}</title>'
            f'<text class="family-label" x="{x:.1f}" y="{y - 11:.1f}">'
            f'{html.escape(first_line)}</text>'
            f'<text class="family-label" x="{x:.1f}" y="{y + 10:.1f}">'
            f'{html.escape(second_line)}</text>'
            f'<text class="subtitle" x="{x:.1f}" y="{y + 34:.1f}">{count} equations</text></a>'
        )

    for move in data["operations"]:
        x, y, _ = pos["operations"][move["anchor"]]
        color = FAMILY_LOOKUP[move["family"]]["color"]
        width = max(68, len(move["name"]) * 7 + 20)
        out.append(
            f'<a href="{GITHUB_ROOT}/{move["path"]}"><rect class="node move-node" '
            f'x="{x - width / 2:.1f}" y="{y - 15:.1f}" width="{width:.1f}" '
            f'height="30" rx="15" stroke="{color}"/>'
            f'<title>Open the {html.escape(move["name"])} mental model</title>'
            f'<text class="move-label" x="{x:.1f}" y="{y + 4:.1f}">'
            f'{html.escape(move["name"])}</text></a>'
        )

    for node in data["equations"]:
        x, y, _ = pos["equations"][node["id"]]
        color = FAMILY_LOOKUP[node["family"]]["color"]
        moves = ", ".join(display_move(move) for move in node["moves"]) or "notation"
        tooltip = f'{node["title"]} — {node["equation"]} — moves: {moves}'
        out.append(
            f'<a href="{GITHUB_ROOT}/{node["path"]}"><circle class="node equation-node" '
            f'cx="{x:.1f}" cy="{y:.1f}" r="16" fill="{color}"/>'
            f'<title>{html.escape(tooltip)}</title>'
            f'<text class="eq-label" x="{x:.1f}" y="{y:.1f}">'
            f'{html.escape(node["label"])}</text></a>'
        )

    out.extend([
        '<g transform="translate(70 2055)">',
        '<text class="legend-strong" x="0" y="0">How to read the mandala</text>',
        '<text class="legend" x="0" y="25">centre: lived observation · inner petals: mathematical jobs · middle petals: reusable moves · outer petals: equations</text>',
        '<text class="legend" x="0" y="48">colored spokes: an equation uses this move · faint gold thread: the next equation in discovery order · every node is a link</text>',
        f'<text class="legend" x="0" y="71">{data["counts"]["equations"]} equations · {data["counts"]["chapters"]} excavations · {data["counts"]["operations"]} reusable moves · generated from the chapters</text>',
        '</g>',
        '</svg>',
    ])
    return "\n".join(out) + "\n"


def markdown_page(data: dict) -> str:
    return f"""# The Living Mathematical Mandala

This is not a poster placed on top of the mathematics. It is a memory of how
the mathematics grew.

[**Open the living, clickable mandala →**]({MANDALA_URL})

[![The AI Archaeology Mathematical Mandala](math-mandala.svg)]({MANDALA_URL})

GitHub displays an SVG inside Markdown as one image. That preview cannot pass a
click through to an individual node. The link above opens the living mandala,
where every node has its own destination. If GitHub Pages has not finished its
first deployment, use the [direct clickable SVG]({RAW_MANDALA_URL}).

- the **heart** opens the [Mathematical Gist](../MATHEMATICAL_GIST.md), where the equations remain in discovery order;
- a **mathematical job** opens the map of [Mathematical Moves](../MATHEMATICAL_MOVES.md#map-of-the-moves);
- a **move** such as subtraction, summation, or logarithm opens its reusable mental model;
- a **numbered equation** opens the excavation in which the reader was forced to invent it.

## Read the rings from the heart outward

    observation
        ↓ creates a need
    mathematical job
        ↓ chooses a relationship-preserving move
    operation
        ↓ compresses the discovered reasoning
    equation

Equations that answer the same kind of human need stay in the same part of the
mandala, even when they were discovered many chapters apart. The faint gold
thread preserves the chronological path from one equation to the next.

- **Where does this equation belong?** Follow its color and spoke inward.
- **What did we discover next?** Follow the gold thread.

The current mandala contains **{data["counts"]["equations"]} equations from
{data["counts"]["chapters"]} excavations**, connected through
**{data["counts"]["operations"]} reusable mathematical moves**.

## It grows with the book

The mandala has no hand-maintained equation list. Its builder reads every
displayed equation and every Mathematical Moves link from the excavation
sources. When a future chapter earns a new equation, explain the required
operations in that chapter and link them to <code>MATHEMATICAL_MOVES.md</code>.
Then run <code>python tools/build_math_mandala.py</code>. The new equation will
enter the right conceptual neighborhood, and the next outer ring will appear
when it is needed.
"""


def interactive_fragment(data: dict) -> str:
    """Return the in-conversation explorer as an embeddable fragment."""
    template = """
<div id="ai-archaeology-math-mandala">
  <style>
    #ai-archaeology-math-mandala{--ink:#f8f3e6;--muted:#aebbd7;--gold:#f4cf75;min-height:760px;padding:20px;border-radius:24px;color:var(--ink);background:radial-gradient(circle at 44% 43%,#19244c 0,#0c122a 46%,#080c1d 100%);font-family:Inter,ui-sans-serif,system-ui,sans-serif;box-sizing:border-box}
    #ai-archaeology-math-mandala *{box-sizing:border-box}
    #ai-archaeology-math-mandala .mm-head{display:flex;align-items:flex-end;justify-content:space-between;gap:18px;margin:0 auto 10px;max-width:1180px}
    #ai-archaeology-math-mandala h2{margin:0;font:700 clamp(24px,3vw,38px) Georgia,serif;letter-spacing:.02em}
    #ai-archaeology-math-mandala .mm-kicker{color:var(--gold);font-size:12px;letter-spacing:.16em;text-transform:uppercase;margin-bottom:5px}
    #ai-archaeology-math-mandala .mm-count{color:var(--muted);font-size:13px;white-space:nowrap}
    #ai-archaeology-math-mandala .mm-tools{max-width:1180px;margin:0 auto 8px;display:flex;gap:10px;align-items:center}
    #ai-archaeology-math-mandala input{width:min(390px,100%);border:1px solid #34426b;border-radius:999px;background:#0d1430;color:var(--ink);padding:10px 15px;outline:none}
    #ai-archaeology-math-mandala input:focus{border-color:var(--gold);box-shadow:0 0 0 3px #f4cf7526}
    #ai-archaeology-math-mandala .mm-stage{display:grid;grid-template-columns:minmax(0,1fr) 290px;gap:14px;max-width:1180px;margin:auto}
    #ai-archaeology-math-mandala svg{width:100%;min-height:640px;border:1px solid #253158;border-radius:20px;background:#090e22aa}
    #ai-archaeology-math-mandala .mm-card{align-self:start;min-height:255px;padding:18px;border:1px solid #2d3962;border-radius:18px;background:#0d1430e8;box-shadow:0 18px 45px #0005}
    #ai-archaeology-math-mandala .mm-card h3{margin:0 0 8px;font:700 21px Georgia,serif}
    #ai-archaeology-math-mandala .mm-card p{color:var(--muted);line-height:1.48;font-size:13px;overflow-wrap:anywhere}
    #ai-archaeology-math-mandala .mm-formula{margin:13px 0;padding:12px;border-left:3px solid var(--gold);background:#080d21;color:#fff8df;font:13px ui-monospace,monospace;white-space:pre-wrap;overflow-wrap:anywhere}
    #ai-archaeology-math-mandala .mm-links{display:flex;flex-wrap:wrap;gap:7px}
    #ai-archaeology-math-mandala .mm-links a{color:#091020;background:var(--gold);border-radius:999px;padding:7px 10px;text-decoration:none;font-size:12px;font-weight:700}
    #ai-archaeology-math-mandala .ring{fill:none;stroke:#d8c27a;stroke-opacity:.13}
    #ai-archaeology-math-mandala .edge{fill:none;stroke:#cbd8f0;stroke-opacity:.09}
    #ai-archaeology-math-mandala .thread{fill:none;stroke:var(--gold);stroke-opacity:.12;stroke-dasharray:2 6}
    #ai-archaeology-math-mandala .node{cursor:pointer}
    #ai-archaeology-math-mandala .family-text{fill:#f8f3e6;font-size:10px;font-weight:700;text-anchor:middle;pointer-events:none}
    #ai-archaeology-math-mandala .move-text{fill:#e9efff;font-size:7px;text-anchor:middle;pointer-events:none}
    #ai-archaeology-math-mandala .eq-text{fill:#081020;font-size:5.4px;font-weight:800;text-anchor:middle;dominant-baseline:central;pointer-events:none}
    #ai-archaeology-math-mandala .dim{opacity:.06!important}
    #ai-archaeology-math-mandala .lit{opacity:1!important;stroke-opacity:.95!important;filter:drop-shadow(0 0 5px currentColor)}
    #ai-archaeology-math-mandala .mm-help{max-width:1180px;margin:10px auto 0;color:var(--muted);font-size:12px;text-align:center}
    @media(max-width:850px){#ai-archaeology-math-mandala .mm-stage{grid-template-columns:1fr}#ai-archaeology-math-mandala .mm-card{min-height:auto}#ai-archaeology-math-mandala .mm-head{align-items:flex-start;flex-direction:column}#ai-archaeology-math-mandala .mm-count{white-space:normal}}
  </style>
  <div class="mm-head">
    <div><div class="mm-kicker">A living memory of mathematical necessity</div><h2>The Mathematical Mandala</h2></div>
    <div class="mm-count"></div>
  </div>
  <div class="mm-tools"><input aria-label="Find an excavation or mathematical move" placeholder="Find distance, softmax, gradient, logarithm…"></div>
  <div class="mm-stage"><svg viewBox="0 0 900 900" aria-label="Interactive mathematical mandala"></svg><aside class="mm-card" aria-live="polite"></aside></div>
  <div class="mm-help">Begin at the heart. Hover to reveal relationships; click a node to open its excavation or mathematical explanation. The gold thread preserves discovery order.</div>
  <script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js"></script>
  <script>
  (function(){
    var root=document.getElementById("ai-archaeology-math-mandala");
    var data=__DATA__;
    var github="__GITHUB__";
    root.querySelector(".mm-count").textContent=data.counts.equations+" equations · "+data.counts.chapters+" excavations · "+data.counts.operations+" moves";
    var svg=d3.select(root).select("svg"), card=root.querySelector(".mm-card"), input=root.querySelector("input");
    var cx=450,cy=450,sector=360/data.families.length;
    var familyById=new Map(data.families.map(function(d){return [d.id,d]}));
    var familyPos=new Map(),movePos=new Map(),equationPos=new Map();
    function polar(r,a){var rad=a*Math.PI/180;return [cx+r*Math.cos(rad),cy+r*Math.sin(rad)]}
    data.families.forEach(function(f,fi){
      var mid=-90+fi*sector,start=mid-sector/2+5,end=mid+sector/2-5;
      familyPos.set(f.id,polar(103,mid));
      var moves=data.operations.filter(function(d){return d.family===f.id}),movePerRing=3;
      moves.forEach(function(m,i){
        var ring=Math.floor(i/movePerRing),batch=moves.slice(ring*movePerRing,(ring+1)*movePerRing),within=i%movePerRing;
        movePos.set(m.anchor,polar(152+ring*32,start+(within+.5)/batch.length*(end-start)));
      });
      var nodes=data.equations.filter(function(d){return d.family===f.id}),per=13;
      nodes.forEach(function(n,i){
        var ring=Math.floor(i/per),batch=nodes.slice(ring*per,(ring+1)*per),within=i%per;
        equationPos.set(n.id,polar(285+ring*48,start+(within+.5)/batch.length*(end-start)));
      });
    });
    [65,103,152,184,216,248,285,333,381,429].forEach(function(r){svg.append("circle").attr("class","ring").attr("cx",cx).attr("cy",cy).attr("r",r)});
    function curve(a,b,bend){
      var qx=cx+((a[0]+b[0])/2-cx)*bend,qy=cy+((a[1]+b[1])/2-cy)*bend;
      return "M"+a[0]+","+a[1]+" Q"+qx+","+qy+" "+b[0]+","+b[1];
    }
    var ordered=data.equations.slice().sort(function(a,b){return a.number-b.number||a.index-b.index});
    ordered.slice(1).forEach(function(n,i){
      svg.append("path").datum({kind:"thread",a:ordered[i].id,b:n.id}).attr("class","thread relation").attr("stroke-width",.7).attr("d",curve(equationPos.get(ordered[i].id),equationPos.get(n.id),.72));
    });
    data.families.forEach(function(f){
      data.operations.filter(function(m){return m.family===f.id}).forEach(function(m){
        svg.append("path").datum({kind:"family-move",family:f.id,move:m.anchor}).attr("class","edge relation").attr("stroke",f.color).attr("stroke-width",1.1).attr("d",curve(familyPos.get(f.id),movePos.get(m.anchor),.48));
      });
    });
    data.equations.forEach(function(n){
      n.moves.filter(function(m){return movePos.has(m)}).forEach(function(m){
        svg.append("path").datum({kind:"move-equation",move:m,equation:n.id}).attr("class","edge relation").attr("stroke",familyById.get(n.family).color).attr("stroke-width",.55).attr("d",curve(movePos.get(m),equationPos.get(n.id),.6));
      });
    });
    var centre=svg.append("g").attr("class","node centre").attr("transform","translate("+cx+","+cy+")");
    centre.append("circle").attr("r",52).attr("fill","#111936").attr("stroke","#f4cf75").attr("stroke-width",2);
    centre.append("text").attr("text-anchor","middle").attr("y",-12).attr("fill","#f4cf75").attr("font-size",24).text("♥");
    centre.append("text").attr("text-anchor","middle").attr("y",9).attr("fill","#fff8df").attr("font-family","Georgia,serif").attr("font-size",13).attr("font-weight",700).text("OBSERVATION");
    centre.append("text").attr("text-anchor","middle").attr("y",27).attr("fill","#aebbd7").attr("font-size",7).text("need → move → equation");
    var families=svg.selectAll(".family").data(data.families).enter().append("g").attr("class","node family").attr("transform",function(d){return "translate("+familyPos.get(d.id)+")"});
    families.append("circle").attr("r",29).attr("fill",function(d){return d.color}).attr("fill-opacity",.14).attr("stroke",function(d){return d.color}).attr("stroke-width",1.4);
    families.append("text").attr("class","family-text").attr("y",-6).each(function(d){
      var labels={"Name & Organize":["Name &","Organize"],"Compare & Measure":["Compare &","Measure"],"Combine Evidence":["Combine","Evidence"],"Share & Normalize":["Share &","Normalize"],"Reshape Scale":["Reshape","Scale"],"Choose & Constrain":["Choose &","Constrain"],"Describe Sensitivity":["Describe","Sensitivity"],"Reason Under Uncertainty":["Reason Under","Uncertainty"]};
      var words=labels[d.name],text=d3.select(this);text.append("tspan").attr("x",0).text(words[0]);text.append("tspan").attr("x",0).attr("dy",11).text(words[1]);
    });
    var moves=svg.selectAll(".move").data(data.operations).enter().append("g").attr("class","node move").attr("transform",function(d){return "translate("+movePos.get(d.anchor)+")"});
    moves.append("rect").attr("x",function(d){return -Math.max(20,d.name.length*3.3)}).attr("y",-7).attr("width",function(d){return Math.max(40,d.name.length*6.6)}).attr("height",14).attr("rx",7).attr("fill","#111936").attr("stroke",function(d){return familyById.get(d.family).color}).attr("stroke-width",1);
    moves.append("text").attr("class","move-text").attr("y",2.5).text(function(d){return d.name});
    var equations=svg.selectAll(".equation").data(data.equations).enter().append("g").attr("class","node equation").attr("transform",function(d){return "translate("+equationPos.get(d.id)+")"});
    equations.append("circle").attr("r",7).attr("fill",function(d){return familyById.get(d.family).color}).attr("stroke","#fff").attr("stroke-opacity",.75).attr("stroke-width",.7);
    equations.append("text").attr("class","eq-text").text(function(d){return d.label});
    function safe(value){var div=document.createElement("div");div.textContent=value;return div.innerHTML}
    function show(d,type){
      if(type==="equation"){
        var linked=d.moves.map(function(anchor){return data.operations.find(function(x){return x.anchor===anchor})}).filter(Boolean);
        card.innerHTML='<div class="mm-kicker">Excavation '+String(d.number).padStart(3,"0")+'</div><h3>'+safe(d.title)+'</h3><div class="mm-formula">'+safe(d.equation)+'</div><p>This equation lives here because it uses '+safe(linked.map(function(m){return m.name}).join(", ")||"named structure")+'. Follow a move inward to remember the human job performed by its sign.</p><div class="mm-links"><a target="_blank" href="'+github+"/"+d.path+'">Open excavation</a>'+linked.slice(0,3).map(function(m){return '<a target="_blank" href="'+github+'/MATHEMATICAL_MOVES.md#'+m.anchor+'">'+safe(m.name)+'</a>'}).join("")+'</div>';
      }else if(type==="move"){
        var f=familyById.get(d.family),count=data.equations.filter(function(n){return n.moves.includes(d.anchor)}).length;
        card.innerHTML='<div class="mm-kicker">Reusable mathematical move</div><h3>'+safe(d.name)+'</h3><p><strong>'+count+' equations</strong> call on this move. Its neighborhood is “'+safe(f.name)+'” because it answers: '+safe(f.question)+'</p><div class="mm-links"><a target="_blank" href="'+github+'/MATHEMATICAL_MOVES.md#'+d.anchor+'">Open mental model</a></div>';
      }else if(type==="family"){
        var count=data.equations.filter(function(n){return n.family===d.id}).length;
        card.innerHTML='<div class="mm-kicker">Mathematical job</div><h3>'+safe(d.name)+'</h3><p>'+safe(d.question)+'</p><p><strong>'+count+' equations</strong> gather in this sector. Their symbols differ, but their human need is related.</p><div class="mm-links"><a target="_blank" href="'+github+'/MATHEMATICAL_MOVES.md#map-of-the-moves">Open the moves map</a></div>';
      }else{
        card.innerHTML='<div class="mm-kicker">Begin at the heart</div><h3>Observation creates need</h3><p>Reality gives us a problem. A failed attempt reveals the relationship that must survive. A mathematical move preserves it. Only then does an equation become the shortest memory of the discovery.</p><div class="mm-links"><a target="_blank" href="'+github+'/MATHEMATICAL_GIST.md">Open the Mathematical Gist</a></div>';
      }
    }
    function reset(){root.querySelectorAll(".node,.relation").forEach(function(el){el.classList.remove("dim","lit")})}
    function highlight(d,type){
      var light=new Set();
      if(type==="equation"){light.add(d.id);d.moves.forEach(function(m){light.add(m)});light.add(d.family)}
      if(type==="move"){light.add(d.anchor);light.add(d.family);data.equations.filter(function(n){return n.moves.includes(d.anchor)}).forEach(function(n){light.add(n.id)})}
      if(type==="family"){light.add(d.id);data.operations.filter(function(m){return m.family===d.id}).forEach(function(m){light.add(m.anchor)});data.equations.filter(function(n){return n.family===d.id}).forEach(function(n){light.add(n.id)})}
      svg.selectAll(".family").classed("dim",function(n){return !light.has(n.id)}).classed("lit",function(n){return light.has(n.id)});
      svg.selectAll(".move").classed("dim",function(n){return !light.has(n.anchor)}).classed("lit",function(n){return light.has(n.anchor)});
      svg.selectAll(".equation").classed("dim",function(n){return !light.has(n.id)}).classed("lit",function(n){return light.has(n.id)});
      svg.selectAll(".relation").classed("dim",function(r){return !((r.family&&light.has(r.family))||(r.move&&light.has(r.move))||(r.equation&&light.has(r.equation))||(r.a&&light.has(r.a))||(r.b&&light.has(r.b)))}).classed("lit",function(r){return (r.family&&light.has(r.family))||(r.move&&light.has(r.move))||(r.equation&&light.has(r.equation))});
    }
    function openPage(path){window.open(path,"_blank","noopener,noreferrer")}
    families.on("mouseenter",function(event,d){highlight(d,"family");show(d,"family")}).on("click",function(event,d){event.stopPropagation();openPage(github+"/MATHEMATICAL_MOVES.md#map-of-the-moves")});
    moves.on("mouseenter",function(event,d){highlight(d,"move");show(d,"move")}).on("click",function(event,d){event.stopPropagation();openPage(github+"/MATHEMATICAL_MOVES.md#"+d.anchor)});
    equations.on("mouseenter",function(event,d){highlight(d,"equation");show(d,"equation")}).on("click",function(event,d){event.stopPropagation();openPage(github+"/"+d.path)});
    centre.on("click",function(event){event.stopPropagation();openPage(github+"/MATHEMATICAL_GIST.md")});
    svg.on("click",function(){reset();show(null,"centre")});
    input.addEventListener("input",function(){
      var q=input.value.trim().toLowerCase();if(!q){reset();return}
      var eq=data.equations.find(function(n){return n.title.toLowerCase().includes(q)||n.equation.toLowerCase().includes(q)||n.label===q});
      var move=data.operations.find(function(n){return n.name.includes(q)||n.anchor.includes(q)});
      if(eq){highlight(eq,"equation");show(eq,"equation")}else if(move){highlight(move,"move");show(move,"move")}
    });
    show(null,"centre");
  })();
  </script>
</div>
"""
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return template.replace("__DATA__", payload).replace(
        "__GITHUB__", GITHUB_ROOT
    )


def standalone_document(data: dict) -> str:
    """Wrap the explorer for GitHub Pages."""
    return """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="The living mathematical memory map of AI Archaeology">
  <title>AI Archaeology — Mathematical Mandala</title>
  <style>
    html,body{margin:0;min-height:100%;background:#080c1d}
    body{padding:clamp(8px,2vw,24px)}
  </style>
</head>
<body>
""" + interactive_fragment(data) + """
</body>
</html>
"""


def generated_files(data: dict) -> dict[Path, str]:
    return {
        OUTPUT / "data.json": json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        OUTPUT / "math-mandala.svg": svg_document(data),
        OUTPUT / "README.md": markdown_page(data),
        OUTPUT / "index.html": standalone_document(data),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument(
        "--interactive",
        type=Path,
        help="also write an interactive in-conversation visualization fragment",
    )
    args = parser.parse_args()
    data = collect()
    files = generated_files(data)
    if args.check:
        stale = [
            path for path, content in files.items()
            if not path.exists() or path.read_text() != content
        ]
        if stale:
            raise SystemExit(
                "Mathematical mandala is stale:\n"
                + "\n".join(str(path) for path in stale)
            )
        print(f'Mathematical mandala matches {data["counts"]["equations"]} equations.')
        return
    OUTPUT.mkdir(exist_ok=True)
    for path, content in files.items():
        path.write_text(content)
    if args.interactive:
        args.interactive.parent.mkdir(parents=True, exist_ok=True)
        args.interactive.write_text(interactive_fragment(data))
    print(
        "Built the living mathematical mandala: "
        f'{data["counts"]["equations"]} equations, '
        f'{data["counts"]["chapters"]} excavations, '
        f'{data["counts"]["operations"]} moves.'
    )


if __name__ == "__main__":
    main()
