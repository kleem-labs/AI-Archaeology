# Excavation 143 — Uncertainty-Aware Planning — Choosing While Admitting Ignorance

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics)
>
> **Applied territory:** Scientific self-improvement and oversight

Corrigibility makes pause, inspection, correction, and handoff legitimate outcomes. A corrigible planner still has to choose when the most efficient route passes through a world it understands poorly.

Inside the Academy of Trials, the old method is given an honest chance. The experimentalist places the evidence on the sealed evidence ledger and tries to plan using only the single most likely world.

Nothing about this first move is careless. To plan using only the single most likely world is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: a small chance of bridge failure dominates the consequence but disappears from the chosen story.

The important discovery is not merely that trying to plan using only the single most likely world failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the sealed evidence ledger, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to carry multiple plausible worlds, weight their consequences, and seek information when uncertainty changes the decision. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Uncertainty-Aware Planning**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## Choosing While Admitting Ignorance

Compare detouring now with first sending a cheap inspection drone.

## Where uncertainty-aware planning runs out

Probabilities and consequence values may both be poorly estimated.

Here the new path ends honestly. Uncertainty-Aware Planning can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the sealed evidence ledger

Rebuild the uncertainty-aware planning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [The wrong ideas worth preserving](mistakes.md); [Diagram and dependency path](diagram.md); [Invention exercises](exercises.md); [References and reading trail](references.md); and [Visual asset brief](images/README.md).

[Next: Impact Measures — Notice What Changed Besides the Goal](../144-impact-measures/README.md)
