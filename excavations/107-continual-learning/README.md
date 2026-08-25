# Excavation 107 — Continual Learning

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Continual learning, reasoning, and research

Catastrophic forgetting exposes competition inside shared parameters. Continual learning must absorb a stream of new tasks while preserving the old behavior that remains valid.

Inside the Hall of Possible Worlds, the old method is given an honest chance. The keeper of unfinished questions places the evidence on the table of mirrored maps and tries to periodically retrain from scratch on everything.

Nothing about this first move is careless. To periodically retrain from scratch on everything is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: the trouble appears immediately: storage and compute grow forever, and old raw data may be unavailable.

The important discovery is not merely that trying to periodically retrain from scratch on everything failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the table of mirrored maps, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to detect change, consolidate stable knowledge, adapt limited components, and evaluate past and present tasks together. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Continual Learning**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## Understanding continual learning

A seasonal model adapts its demand head while preserving reusable product representations.

## Where continual learning runs out

Stability and adaptability remain in tension.

Here the new path ends honestly. Continual Learning can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the table of mirrored maps

Rebuild the continual learning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 108](../108-meta-learning/README.md)
