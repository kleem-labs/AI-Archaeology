# Excavation 199 — The Training Report — Preserve the Decisions, Not Only the Weights

Memorization auditing adds one essential limitation to the evaluation record. A released checkpoint still cannot explain its corpus, mixture, compute, interruptions, exclusions, intended uses, or known failures by inspecting weight tensors.

An obvious shortcut is to publish the final benchmark table and assume the configuration files explain the rest.

Then the hidden cost becomes visible. A score has no visible data lineage, uncertainty, subgroup behavior, energy or hardware context, incident history, or warning about uses the evaluation never tested.

Crossing that boundary requires one additional guarantee. Generate a training report from manifests and logs, then add human-reviewed explanations of intended use, out-of-scope use, limitations, incidents, provenance, evaluation conditions, and responsible release decisions.

## Let one run decide

The station's report names corpus and code versions, tokens seen, mixture shares, compute, checkpoint recoveries, per-domain validation, memorization probes, excluded sources, and the exact model artifact hash.

## What this repair cannot do

Documentation improves accountability but can be incomplete, outdated, misleading, or ignored; claims still require inspectable evidence.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: A Tiny Pretraining Factory — Close the Accountable Training Loop](../200-tiny-pretraining-factory/README.md)
