# Excavation 114 — Model-Based Planning

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Continual learning, reasoning, and research

Counterfactual reasoning compares unrealized alternatives for one case. Planning extends that question across a sequence, where each imagined action changes which choices and states can follow.

A new case arrives at the Hall of Possible Worlds. Nothing yet demands a new invention, so the keeper of unfinished questions uses the table of mirrored maps to commit to the first sequence imagined.

This is precisely the kind of shortcut a careful builder should try first. The instruction to commit to the first sequence imagined preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: one forecast may exploit model error or miss better branches.

The counterexample separates two questions that the attempt to commit to the first sequence imagined had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the table of mirrored maps fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now simulate multiple candidate sequences, score outcomes, act briefly, observe reality, and plan again. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Model-Based Planning**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Understanding model-based planning

A robot simulates left-right paths, takes one safe step, then updates after detecting an obstacle.

## Where model-based planning runs out

Planning cost grows with horizon and branching.

At the Hall of Possible Worlds, the keeper of unfinished questions leaves a blank beneath the new mark. Model-Based Planning has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the table of mirrored maps

Rebuild the model-based planning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 115](../115-tree-search/README.md)
