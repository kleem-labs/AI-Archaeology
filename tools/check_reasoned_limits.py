"""Reject limitation sections that state a boundary without explaining why."""
from pathlib import Path
import re

root = Path(__file__).parents[1]
failures = []

for path in sorted((root / "excavations").glob("*/README.md")):
    text = path.read_text()
    match = re.search(r"^## (?:Limits|Where [^\n]*breaks)\n+(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not match:
        continue
    body = match.group(1).strip()
    sentences = len(re.findall(r"[.!?](?:\s|$)", body))
    causal = re.search(r"\b(because|since|the reason|follows from|repair is explicit|only knows|contains no|never|cannot infer|cannot prove|does not automatically)\b", body, re.I)
    if sentences < 2 or not causal:
        failures.append(f"{path}: limitation is asserted without a causal explanation")

if failures:
    raise SystemExit("\n".join(failures))

print("Verified causal explanations in every limitation section.")
