"""Build the ordered mathematical spine from equation-bearing excavations."""
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).parents[1]
OUTPUT = ROOT / "MATHEMATICAL_GIST.md"
# Split only at H2 boundaries. H3 term-by-term explanations belong to their
# parent derivation and must remain beside the concrete example.
SECTION = re.compile(r"(^## .+?\n.*?)(?=^## |\Z)", re.M | re.S)


def clean_section(section):
    """Keep derivation prose and math while removing chapter-navigation noise."""
    lines = section.strip().splitlines()
    if lines and lines[0].startswith("## "):
        lines = lines[1:]
    text = "\n".join(lines).strip()
    return text.replace("../../MATHEMATICAL_MOVES.md", "MATHEMATICAL_MOVES.md")


def build():
    entries = []
    equation_count = 0
    for path in sorted((ROOT / "excavations").glob("*/README.md")):
        text = path.read_text()
        # The complete book's cinematic recall film belongs to the chapter,
        # not to the equation-only spine. In the earliest excavations an
        # equation precedes the first H2, so remove the film before finding
        # that prefix as well as before collecting equation sections.
        text = re.sub(
            r"\n?<!-- memory-film-v1:start -->.*?<!-- memory-film-v1:end -->\n?",
            "\n",
            text,
            flags=re.S,
        )
        if "$$" not in text:
            continue
        title_match = re.search(r"^# (.+)$", text, re.M)
        title = title_match.group(1) if title_match else path.parent.name
        sections = [clean_section(match.group(1)) for match in SECTION.finditer(text) if "$$" in match.group(1)]
        # A few early chapters place mathematics before their first H2. Keep
        # that material rather than silently omitting it.
        first_h2 = text.find("\n## ")
        prefix = text[:first_h2] if first_h2 >= 0 else text
        if "$$" in prefix:
            sections.insert(0, prefix.split("\n", 1)[-1].strip())
        equation_count += sum(section.count("$$") // 2 for section in sections)
        relative = path.relative_to(ROOT).as_posix()
        entries.append((title, relative, sections))

    out = [
        "# The Mathematical Gist of AI Archaeology",
        "",
        "This is the book's mathematical spine in discovery order. It is not a",
        "formula sheet. Every entry keeps the concrete work and the explanation",
        "of each term before allowing notation to compress the idea.",
        "",
        "Use it after reading an excavation, or to revisit the chain of",
        "mathematical inventions without rereading the entire narrative.",
        "For the reusable meaning of an operation, follow its link into the",
        "[Mathematical Moves guide](MATHEMATICAL_MOVES.md).",
        "To remember where an equation belongs and what it connects to, enter",
        "the [living Mathematical Mandala](math-mandala/README.md).",
        "",
        f"**{len(entries)} equation-bearing excavations · {equation_count} displayed equations**",
        "",
        "## Map",
        "",
    ]
    for title, relative, _ in entries:
        anchor = re.sub(r"[^a-z0-9 -]", "", title.lower()).replace(" ", "-")
        anchor = re.sub(r"-+", "-", anchor).strip("-")
        out.append(f"- [{title}](#{anchor})")

    for title, relative, sections in entries:
        out.extend(["", "---", "", f"## {title}", ""])
        for index, section in enumerate(sections):
            if index:
                out.extend(["", "### The next compression in this excavation", ""])
            out.append(section)
        out.extend(["", f"[Return to the full excavation]({relative})"])

    return "\n".join(out).rstrip() + "\n"


parser = argparse.ArgumentParser()
parser.add_argument("--check", action="store_true", help="fail if the generated gist is stale")
args = parser.parse_args()
generated = build()

if args.check:
    if not OUTPUT.exists() or OUTPUT.read_text() != generated:
        raise SystemExit("MATHEMATICAL_GIST.md is stale; rebuild it with tools/build_mathematical_gist.py")
    print("Mathematical gist matches the excavation sources.")
else:
    OUTPUT.write_text(generated)
    print("Built MATHEMATICAL_GIST.md from the ordered excavation sources.")
