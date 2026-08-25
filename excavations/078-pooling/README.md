# Excavation 078 — Pooling — Keeping Evidence While Shrinking the Map

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

Convolution slides one local detector across the whole image. The resulting activation maps preserve every detected location and quickly become too large for deeper processing.

A new case arrives at the Glass Menagerie. Nothing yet demands a new invention, so the maker of seeing-machines uses the wall of illuminated tiles to keep every activation at full resolution through every layer.

This is precisely the kind of shortcut a careful builder should try first. The instruction to keep every activation at full resolution through every layer preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: memory explodes and tiny shifts move evidence to neighboring cells.

The counterexample separates two questions that the attempt to keep every activation at full resolution through every layer had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the wall of illuminated tiles fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now summarize small neighborhoods while retaining the strongest or average evidence. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Pooling**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Keeping Evidence While Shrinking the Map

Max pooling [1,7,2,3] keeps 7: an edge existed somewhere in that patch.

## Where pooling runs out

Pooling discards exact location and can erase subtle patterns.

At the Glass Menagerie, the maker of seeing-machines leaves a blank beneath the new mark. Pooling has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the wall of illuminated tiles

Rebuild the pooling scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 079](../079-cnn-hierarchy/README.md)
