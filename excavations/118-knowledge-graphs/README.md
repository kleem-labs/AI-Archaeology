# Excavation 118 — Knowledge Graphs

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Graphs & Relational Structures](../../MATHEMATICS_ATLAS.md#graphs) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Continual learning, reasoning, and research

A neuro-symbolic system gives learned perception and exact rules distinct jobs. Those rules need facts stored with explicit entities and relationships rather than buried inside one paragraph or vector.

A new case arrives at the Hall of Possible Worlds. Nothing yet demands a new invention, so the keeper of unfinished questions uses the table of mirrored maps to store every fact as an isolated sentence.

This is precisely the kind of shortcut a careful builder should try first. The instruction to store every fact as an isolated sentence preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: repeated entities, reverse links, and multi-hop questions become difficult to traverse.

The counterexample separates two questions that the attempt to store every fact as an isolated sentence had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the table of mirrored maps fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now represent entities as nodes and named relations as edges. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Knowledge Graphs**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Understanding knowledge graphs

Tiger —is_a→ cat and cat —is_a→ mammal support a two-hop ancestry query.

## Where knowledge graphs runs out

Graphs can be incomplete, stale, and uncertain.

The knowledge graphs repair holds, but the world asks for something it was never given. At the Hall of Possible Worlds, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the table of mirrored maps

Rebuild the knowledge graphs scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 119](../119-graph-neural-networks/README.md)
