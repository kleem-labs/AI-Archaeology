# Excavation 069 — Controlled Experiments

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality) · [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics)
>
> **Applied territory:** Learning in the world and interpretability

Drift detection says that the input or outcome distribution moved. It does not say whether a new model, a holiday, a policy change, or chance caused the observed performance difference.

The previous discovery reaches the Living Watchgarden carrying one unfinished problem. Beside the weathered observation slate, the field naturalist first tries to compare this week with last week.

There is good reason to begin this way. If we compare this week with last week, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: a holiday raises sales for both systems and receives credit as a model improvement.

This failure cannot be repaired by performing the instruction to compare this week with last week more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the weathered observation slate; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to randomly assign comparable cases to old and new behavior and compare predefined outcomes. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Controlled Experiments**. The name is simply a handle for the distinction already reconstructed.

## Understanding controlled experiments

Split 10,000 simultaneous visitors evenly; conversion is 5% for control and 5.5% for treatment under the same week.

## Where controlled experiments runs out

Experiments require sufficient samples, ethical limits, and careful metrics.

One unsolved mark remains on the weathered observation slate. None of the responsibilities inside Controlled Experiments can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the weathered observation slate

Rebuild the controlled experiments scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 070](../070-bandits/README.md)
