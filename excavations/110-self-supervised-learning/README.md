# Excavation 110 — Self-Supervised Learning

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Continual learning, reasoning, and research

Curriculum learning controls the order of experience. The supply of human labels still limits every curriculum, while raw text, images, and audio contain countless prediction problems whose answers are present in the data itself.

A new case arrives at the Hall of Possible Worlds. Nothing yet demands a new invention, so the keeper of unfinished questions uses the table of mirrored maps to wait for humans to label every example.

This is precisely the kind of shortcut a careful builder should try first. The instruction to wait for humans to label every example preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: labels are expensive and discard most structure already inside observations.

The counterexample separates two questions that the attempt to wait for humans to label every example had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the table of mirrored maps fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now hide or transform part of an observation and train the model to recover the missing relation. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Self-Supervised Learning**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Understanding self-supervised learning

Mask one image patch and predict it from neighbors; no human label is needed.

## Where self-supervised learning runs out

Pretext tasks may reward patterns unrelated to downstream needs.

A final test reaches beyond the new instrument. It does not refute Self-Supervised Learning; it reveals the edge of what was constructed. The keeper of unfinished questions carries that edge into the following room.

## Return to the table of mirrored maps

Rebuild the self-supervised learning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 111](../111-world-models/README.md)
