# Excavation 087 — States, Actions, and Transitions

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

A reward says how an outcome turned out. To learn from it, the agent must preserve the situation it occupied, the action it chose, and the situation that followed.

Nothing in the Road of Consequences yet bears today's mathematical name. There is only the expedition leader, the map of branching journeys, and one plausible action: store only action and final reward.

Then the quiet test arrives: the trouble appears immediately: the same action helps in one situation and harms in another. What looked like simplicity is revealed as a missing distinction.

*The expedition leader sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: store only action and final reward
                         │
                         └── mismatch: the trouble appears immediately: the…

reference evidence ──▶ measured repair: we need to record current state,…
```

The expedition leader turns the map of branching journeys toward the light. Through the old engraving, store only action and final reward, the evidence ends in the same contradiction: the trouble appears immediately: the same action helps in one situation and harms in another. A second engraving adds only the power to record current state, chosen action, reward, and resulting state. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The expedition leader circles the place where the two states, actions, and transitions cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: we need to record current state, chosen action, reward, and resulting state. The expedition leader writes **States, Actions, and Transitions** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The expedition leader places a finger over the new distinction. At once the two cases collapse and the trouble appears immediately: the same action helps in one situation and harms in another. Lifting the finger restores only this capacity: record current state, chosen action, reward, and resulting state. That tiny reversible motion is the chapter's proof of necessity.

## Understanding states, actions, and transitions

“Move right” from left of the door succeeds; the same action beside a cliff fails because state differs.

## Where states, actions, and transitions runs out

A state representation may omit information needed for future decisions.

One unsolved mark remains on the map of branching journeys. None of the responsibilities inside States, Actions, and Transitions can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the map of branching journeys

Rebuild the states, actions, and transitions scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 088](../088-value-functions/README.md)
