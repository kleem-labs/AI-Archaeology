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
    boilerplate = re.search(r"\b(our new machinery only knows|solving that problem does not automatically|the boundary follows from the mechanism itself|that operation solves the failure)\b", body, re.I)
    explanatory = re.search(r"\b(because|since|depend|depends|not|can|may|cannot|does not|doesn't|but|while|unless|without|only|rather than|reveals|loses|ignores|require|requires|affect|affects|shape|shapes)\b", body, re.I)
    if sentences < 1 or len(body.split()) < 8 or not explanatory or boilerplate:
        failures.append(f"{path}: limitation lacks a specific causal explanation or uses boilerplate")

if failures:
    raise SystemExit("\n".join(failures))

print("Verified causal explanations in every limitation section.")
