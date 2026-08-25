# Excavation 134 — Sparse Attention — Looking Without Comparing Everything

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Scientific self-improvement and oversight

A mixture of experts activates only a few specialists for each token. Long-context attention still compares too many token pairs, making communication—not expert capacity—the next computational bottleneck.

A new case arrives at the Academy of Trials. Nothing yet demands a new invention, so the experimentalist uses the sealed evidence ledger to keep full attention and buy more hardware.

This is precisely the kind of shortcut a careful builder should try first. The instruction to keep full attention and buy more hardware preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: doubling length roughly quadruples pairwise comparisons.

The counterexample separates two questions that the attempt to keep full attention and buy more hardware had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the sealed evidence ledger fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now preserve a small pattern of local, global, or retrieved connections that matches the task's information paths. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Sparse Attention**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Looking Without Comparing Everything

A document token attends nearby sentences plus section headings instead of every word in the book.

## Where sparse attention runs out

A sparse pattern can hide the one distant clue the answer needs.

A final test reaches beyond the new instrument. It does not refute Sparse Attention; it reveals the edge of what was constructed. The experimentalist carries that edge into the following room.

## Return to the sealed evidence ledger

Rebuild the sparse attention scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [The wrong ideas worth preserving](mistakes.md); [Diagram and dependency path](diagram.md); [Invention exercises](exercises.md); [References and reading trail](references.md); and [Visual asset brief](images/README.md).

[Next: External Memory — Remembering Beyond the Context Window](../135-external-memory/README.md)
