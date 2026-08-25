# Excavation 106 — Catastrophic Forgetting

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Continual learning, reasoning, and research

Selective prediction gives the system permission to abstain. When an approved new task finally supplies more training data, learning it can overwrite skills that were reliable yesterday.

A new case arrives at the Hall of Possible Worlds. Nothing yet demands a new invention, so the keeper of unfinished questions uses the table of mirrored maps to fine-tune only on the newest data.

This is precisely the kind of shortcut a careful builder should try first. The instruction to fine-tune only on the newest data preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: updates useful for B overwrite weights carrying A.

The counterexample separates two questions that the attempt to fine-tune only on the newest data had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the table of mirrored maps fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now rehearse old evidence, protect important parameters, or allocate new capacity. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Catastrophic Forgetting**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Understanding catastrophic forgetting

Learning birds after mammals drops mammal accuracy; mixing a small mammal replay set preserves both.

## Where catastrophic forgetting runs out

Memory, privacy, and capacity limit rehearsal.

The catastrophic forgetting repair holds, but the world asks for something it was never given. At the Hall of Possible Worlds, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the table of mirrored maps

Rebuild the catastrophic forgetting scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 107](../107-continual-learning/README.md)
