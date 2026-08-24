# Excavation 105 — Selective Prediction

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Continual learning, reasoning, and research

Active learning spends human effort where it should teach the most. A deployed system still encounters cases where no available evidence justifies any answer, even after labels have been chosen carefully.

Morning reaches the Hall of Possible Worlds before anyone has a name for today's difficulty. Beside the table of mirrored maps, the keeper of unfinished questions tries the smallest continuation of what already works: always return the highest-scoring answer.

Then the quiet test arrives: a forced answer converts uncertainty into confident-looking error. What looked like simplicity is revealed as a missing distinction.

*The keeper of unfinished questions sketches the break before changing it:*

```text
observation
    │
    ▼
[always return the highest-scoring…]
    │
    ╳  a forced answer converts uncertainty…
    │
    ▼
[allow abstention and choose a…]
```

The keeper of unfinished questions turns the table of mirrored maps toward the light. Through the old engraving, always return the highest-scoring answer, the evidence ends in the same contradiction: a forced answer converts uncertainty into confident-looking error. A second engraving adds only the power to allow abstention and choose a coverage level whose retained answers meet a risk target. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The keeper of unfinished questions circles the place where the two selective prediction cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: allow abstention and choose a coverage level whose retained answers meet a risk target. The keeper of unfinished questions writes **Selective Prediction** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The keeper of unfinished questions does not memorize selective prediction. Instead, the keeper of unfinished questions memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can allow abstention and choose a coverage level whose retained answers meet a risk target. The formal name merely lets that motion be shared.

## Understanding selective prediction

The system answers 80 of 100 cases and is correct on 78; the other 20 go to a human rather than becoming guesses.

## Where selective prediction runs out

Abstention shifts work and may fail unevenly across groups.

One unsolved mark remains on the table of mirrored maps. None of the responsibilities inside Selective Prediction can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the table of mirrored maps

Rebuild the selective prediction scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 106](../106-catastrophic-forgetting/README.md)
