# Excavation 087 — States, Actions, and Transitions

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

A reward says how an outcome turned out. To learn from it, the agent must preserve the situation it occupied, the action it chose, and the situation that followed.

Inside the Road of Consequences, the old method is given an honest chance. The expedition leader places the evidence on the map of branching journeys and tries to store only action and final reward.

Nothing about this first move is careless. To store only action and final reward is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: the trouble appears immediately: the same action helps in one situation and harms in another.

The important discovery is not merely that trying to store only action and final reward failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the map of branching journeys, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to record current state, chosen action, reward, and resulting state. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **States, Actions, and Transitions**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## Understanding states, actions, and transitions

“Move right” from left of the door succeeds; the same action beside a cliff fails because state differs.

## Where states, actions, and transitions runs out

A state representation may omit information needed for future decisions.

One unsolved mark remains on the map of branching journeys. None of the responsibilities inside States, Actions, and Transitions can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the map of branching journeys

Rebuild the states, actions, and transitions scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 088](../088-value-functions/README.md)
