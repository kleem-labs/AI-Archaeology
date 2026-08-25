"""Protect all 226 cinematic excavation films and their connected palace."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).parents[1]
START = "<!-- memory-film-v1:start -->"
END = "<!-- memory-film-v1:end -->"
failures: list[str] = []

data = json.loads((ROOT / "memory-palace" / "data.json").read_text())
realms = data.get("realms", [])
films = [film for realm in realms for film in realm.get("roots", [])]

if len(realms) != 18:
    failures.append(f"expected 18 memory realms, found {len(realms)}")
if [film.get("number") for film in films] != list(range(226)):
    failures.append("the palace must contain one ordered film for Excavations 000–225")

objects = set()
seals = set()
for film in films:
    number = film["number"]
    for field in ("question", "object", "failure_image", "transformation", "sentence", "gesture"):
        if not film.get(field, "").strip():
            failures.append(f"{number:03d}: missing {field}")
    if not film["question"].endswith("?"):
        failures.append(f"{number:03d}: memory question is not a question")
    if "we can we" in film["sentence"].lower() or "…" in film["sentence"]:
        failures.append(f"{number:03d}: memory seal is broken or truncated")
    if film["object"] in objects:
        failures.append(f"{number:03d}: memory object is not distinct")
    if film["sentence"] in seals:
        failures.append(f"{number:03d}: memory seal is not distinct")
    objects.add(film["object"])
    seals.add(film["sentence"])

    destination = (ROOT / "memory-palace" / film["path"]).resolve()
    if not destination.exists():
        failures.append(f"{number:03d}: palace door is broken")
        continue
    chapter = destination.read_text()
    if number <= 200:
        if START in chapter or END in chapter:
            failures.append(f"{number:03d}: recall instructions leaked into the reading narrative")
        folder = destination.parent
        for companion in (folder / "diagram.md", folder / "exercises.md", folder / "images" / "README.md"):
            text = companion.read_text()
            if text.count(START) != 1 or text.count(END) != 1:
                failures.append(f"{companion.relative_to(ROOT)}: memory film is absent or duplicated")

html = (ROOT / "memory-palace" / "index.html").read_text()
for label in ("Question", "Object", "Failure", "Transformation", "Memory seal"):
    if label not in html:
        failures.append(f"the living palace lost its {label} frame")
guide = (ROOT / "MEMORY_PALACE.md").read_text()
for realm in realms:
    if realm["name"] not in guide or realm["question"] not in guide:
        failures.append(f"the script-free guide lost {realm['name']}")

if failures:
    raise SystemExit("\n".join(failures))

print("Complete memory gate passed: 18 realms, 226 films, 1,130 frames.")
