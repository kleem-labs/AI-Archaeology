# Excavation 105 — Selective Prediction

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Continual learning, reasoning, and research

Active learning spends human effort where it should teach the most. A deployed system still encounters cases where no available evidence justifies any answer, even after labels have been chosen carefully.

The previous discovery reaches the Hall of Possible Worlds carrying one unfinished problem. Beside the table of mirrored maps, the keeper of unfinished questions first tries to always return the highest-scoring answer.

There is good reason to begin this way. If we always return the highest-scoring answer, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: a forced answer converts uncertainty into confident-looking error.

This failure cannot be repaired by performing the instruction to always return the highest-scoring answer more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the table of mirrored maps; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to allow abstention and choose a coverage level whose retained answers meet a risk target. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Selective Prediction**. The name is simply a handle for the distinction already reconstructed.

## Understanding selective prediction

The system answers 80 of 100 cases and is correct on 78; the other 20 go to a human rather than becoming guesses.

## Where selective prediction runs out

Abstention shifts work and may fail unevenly across groups.

One unsolved mark remains on the table of mirrored maps. None of the responsibilities inside Selective Prediction can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the table of mirrored maps

Rebuild the selective prediction scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 106](../106-catastrophic-forgetting/README.md)
