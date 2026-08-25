"""Protect the five-realm memory journey beneath Excavations 201–225."""

from __future__ import annotations

import json
from pathlib import Path

from build_excavations_201_225 import REALMS, ROOT_MEMORY, ROWS, concept, realm_for


ROOT = Path(__file__).parents[1]
REQUIRED_MEMORY_FIELDS = (
    "question",
    "object",
    "failure_image",
    "transformation",
    "sentence",
    "gesture",
)
failures: list[str] = []


if len(REALMS) != 5:
    failures.append(f"expected five realms, found {len(REALMS)}")

numbers = [row.number for row in ROWS]
if numbers != list(range(201, 226)):
    failures.append("the root journey must remain continuous from 201 through 225")

if set(ROOT_MEMORY) != set(numbers):
    failures.append("ROOT_MEMORY must contain exactly one film for every root")

sentences: set[str] = set()
objects: set[str] = set()
for row in ROWS:
    memory = ROOT_MEMORY[row.number]
    realm = realm_for(row.number)
    chapter = ROOT / "excavations" / f"{row.number:03d}-{row.slug}" / "README.md"
    text = chapter.read_text() if chapter.exists() else ""
    companions = "\n".join(
        (chapter.parent / relative).read_text()
        for relative in ("diagram.md", "exercises.md", "images/README.md")
    )

    for field in REQUIRED_MEMORY_FIELDS:
        value = memory.get(field, "").strip()
        if not value:
            failures.append(f"{row.number}: empty memory field {field}")
        elif value not in companions:
            failures.append(f"{row.number}: memory companions lost {field}")

    if memory["sentence"] in sentences:
        failures.append(f"{row.number}: memory seal is not unique")
    sentences.add(memory["sentence"])
    if memory["object"] in objects:
        failures.append(f"{row.number}: physical memory object is not unique")
    objects.add(memory["object"])

    if "## When the chamber changes" in text or "Memory seal" in text:
        failures.append(f"{row.number}: recall scaffolding leaked into the reading narrative")
    for required in (concept(row), memory["object"], memory["question"]):
        if required not in text:
            failures.append(f"{row.number}: chapter lost concrete context {required!r}")

guide = (ROOT / "MATHEMATICAL_ROOTS.md").read_text()
for realm in REALMS:
    if realm["name"] not in guide or realm["question"] not in guide:
        failures.append(f"roots guide lost {realm['name']}")
for row in ROWS:
    memory = ROOT_MEMORY[row.number]
    if memory["sentence"] not in guide:
        failures.append(f"roots guide lost the seal for {row.number}")

data_path = ROOT / "mathematical-roots" / "data.json"
data = json.loads(data_path.read_text())
roots = [item for realm in data.get("realms", []) for item in realm.get("roots", [])]
if len(data.get("realms", [])) != 5 or len(roots) != 25:
    failures.append("the living Undercroft must expose five realms and 25 roots")

html = (ROOT / "mathematical-roots" / "index.html").read_text()
for label in ("Question", "Object", "Failure", "Transformation", "Memory seal"):
    if label not in html:
        failures.append(f"the living Undercroft lost its {label} frame")
for row in ROWS:
    path = f"../excavations/{row.number:03d}-{row.slug}/README.md"
    if path not in html:
        failures.append(f"the living Undercroft lost the door to {row.number}")

if failures:
    raise SystemExit("\n".join(failures))

print("Mathematical-root memory gate passed: 5 realms, 25 films, 125 frames.")
