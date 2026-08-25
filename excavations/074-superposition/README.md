# Excavation 074 — Superposition

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Information Theory](../../MATHEMATICS_ATLAS.md#information)
>
> **Applied territory:** Learning in the world and interpretability

Attribution assigns influence to inputs or internal components. The investigation soon finds that one neuron can participate in many features and one feature can be distributed across many neurons.

A new case arrives at the Living Watchgarden. Nothing yet demands a new invention, so the field naturalist uses the weathered observation slate to demand one feature per coordinate.

This is precisely the kind of shortcut a careful builder should try first. The instruction to demand one feature per coordinate preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: limited width forces useful patterns to share neurons, producing confusing mixed activations.

The counterexample separates two questions that the attempt to demand one feature per coordinate had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the weathered observation slate fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now represent features as directions that can overlap when they rarely need to be active together. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Superposition**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Understanding superposition

One two-dimensional space stores several sparse directions; collisions occur mainly when multiple stored features activate together.

## Where superposition runs out

Separating superposed features is difficult and may not yield unique answers.

A final test reaches beyond the new instrument. It does not refute Superposition; it reveals the edge of what was constructed. The field naturalist carries that edge into the following room.

## Return to the weathered observation slate

Rebuild the superposition scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 075](../075-causal-interventions/README.md)
