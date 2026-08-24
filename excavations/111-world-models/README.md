# Excavation 111 — World Models

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Self-supervision extracts lessons from unlabeled observations. An acting system needs more than representations: before choosing, it must imagine how the world may change after each possible action.

Nothing in the Hall of Possible Worlds yet bears today's mathematical name. There is only the keeper of unfinished questions, the table of mirrored maps, and one plausible action: learn only which action was rewarded in previously visited situations.

Then the quiet test arrives: the agent cannot imagine untried sequences or reuse physical regularities. What looked like simplicity is revealed as a missing distinction.

*The keeper of unfinished questions sketches the break before changing it:*

```text
observation
    │
    ▼
[learn only which action was rewarded…]
    │
    ╳  the agent cannot imagine untried…
    │
    ▼
[we need to learn a compact model that…]
```

The keeper of unfinished questions turns the table of mirrored maps toward the light. Through the old engraving, learn only which action was rewarded in previously visited situations, the evidence ends in the same contradiction: the agent cannot imagine untried sequences or reuse physical regularities. A second engraving adds only the power to learn a compact model that predicts next state and reward from current state and action. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The keeper of unfinished questions circles the place where the two world models cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: we need to learn a compact model that predicts next state and reward from current state and action. The keeper of unfinished questions writes **World Models** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The keeper of unfinished questions places a finger over the new distinction. At once the two cases collapse and the agent cannot imagine untried sequences or reuse physical regularities. Lifting the finger restores only this capacity: learn a compact model that predicts next state and reward from current state and action. That tiny reversible motion is the chapter's proof of necessity.

## Understanding world models

From ball position and push direction, predict where the ball will move before choosing the push.

## Where world models runs out

Model errors compound during long imagined rollouts.

One unsolved mark remains on the table of mirrored maps. None of the responsibilities inside World Models can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the table of mirrored maps

Rebuild the world models scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 112](../112-causal-inference/README.md)
