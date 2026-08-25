# Excavation 199 — The Training Report — Preserve the Decisions, Not Only the Weights

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Data and pretraining operations

Memorization auditing adds one essential limitation to the evaluation record. A released checkpoint still cannot explain its corpus, mixture, compute, interruptions, exclusions, intended uses, or known failures by inspecting weight tensors.

Inside the Archive Foundry, the old method is given an honest chance. The archivist-engineer places the evidence on the chain-of-custody ledger and tries to publish the final benchmark table and assume the configuration files explain the rest.

Nothing about this first move is careless. To publish the final benchmark table and assume the configuration files explain the rest is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: a score has no visible data lineage, uncertainty, subgroup behavior, energy or hardware context, incident history, or warning about uses the evaluation never tested.

The important discovery is not merely that trying to publish the final benchmark table and assume the configuration files explain the rest failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the chain-of-custody ledger, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to generate a training report from manifests and logs, then add human-reviewed explanations of intended use, out-of-scope use, limitations, incidents, provenance, evaluation conditions, and responsible release decisions. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **The Training Report**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## Preserve the Decisions, Not Only the Weights

The station's report names corpus and code versions, tokens seen, mixture shares, compute, checkpoint recoveries, per-domain validation, memorization probes, excluded sources, and the exact model artifact hash.

## Where the training report runs out

Documentation improves accountability but can be incomplete, outdated, misleading, or ignored; claims still require inspectable evidence.

The chain-of-custody ledger answers today's question and falls silent at the next. That silence is precise: Training Report was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the chain-of-custody ledger

Rebuild the training report scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: A Tiny Pretraining Factory — Close the Accountable Training Loop](../200-tiny-pretraining-factory/README.md)
