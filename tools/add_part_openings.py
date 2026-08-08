"""Give each major act a distinct narrative threshold."""
from pathlib import Path

ROOT = Path(__file__).parents[1]
OPENINGS = {
    0: ("PART I — MEASURING REALITY", "You begin with no mathematics—only tracks, weather, animals, memory, and a world that refuses to repeat itself exactly."),
    6: ("PART II — INVENTING MEANING", "Measurements can describe a tiger. They cannot yet explain why the same word changes meaning when its neighbors change."),
    17: ("PART III — LEARNING FROM ERROR", "The machine can move information. It still cannot admit uncertainty, measure a mistake, or use that mistake to change itself."),
    36: ("PART IV — BUILDING A TINY GPT", "You have built a learner. Now place language in its hands and discover every mechanism required to make one token predict another."),
    46: ("PART V — MAKING ANSWERS USEFUL", "A machine that speaks is not necessarily a machine that knows, helps, or deserves belief."),
    56: ("PART VI — TRUSTING AN ACTING MACHINE", "The model no longer merely answers. Its words can cause actions, and every action creates questions of authority and proof."),
    66: ("PART VII — LEARNING AFTER DEPLOYMENT", "The laboratory door opens onto a changing world. Now the system influences the very evidence from which it learns."),
    76: ("PART VIII — SEEING AND CREATING", "Language was only one trace of reality. Light, space, sound, and noise demand new forms of the discoveries you already made."),
    86: ("PART IX — ACTING AND SCALING", "Correct answers disappear. The learner must act, wait for consequences, share machines, and remain accountable at scale."),
    101: ("PART X — LEARNING WHAT WE STILL DO NOT KNOW", "The complete system now meets the frontier: ignorance, changing tasks, causal questions, proofs, attacks, and open-ended research."),
}

for number, (title, scene) in OPENINGS.items():
    path = next((ROOT / "excavations").glob(f"{number:03d}-*/README.md"))
    text = path.read_text()
    marker = f"> **{title}**"
    if marker in text:
        continue
    lines = text.splitlines()
    insert_at = 1
    block = ["", marker, ">", f"> {scene}", ""]
    lines[insert_at:insert_at] = block
    path.write_text("\n".join(lines) + "\n")

print("Added ten distinct part openings.")
