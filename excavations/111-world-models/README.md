# Excavation 111 — World Models

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Continual learning, reasoning, and research

Self-supervision extracts lessons from unlabeled observations. An acting system needs more than representations: before choosing, it must imagine how the world may change after each possible action.

Inside the Hall of Possible Worlds, the old method is given an honest chance. The keeper of unfinished questions places the evidence on the table of mirrored maps and tries to learn only which action was rewarded in previously visited situations.

Nothing about this first move is careless. To learn only which action was rewarded in previously visited situations is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: the agent cannot imagine untried sequences or reuse physical regularities.

The important discovery is not merely that trying to learn only which action was rewarded in previously visited situations failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the table of mirrored maps, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to learn a compact model that predicts next state and reward from current state and action. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **World Models**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## Understanding world models

From ball position and push direction, predict where the ball will move before choosing the push.

## Where world models runs out

Model errors compound during long imagined rollouts.

One unsolved mark remains on the table of mirrored maps. None of the responsibilities inside World Models can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the table of mirrored maps

Rebuild the world models scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 112](../112-causal-inference/README.md)
