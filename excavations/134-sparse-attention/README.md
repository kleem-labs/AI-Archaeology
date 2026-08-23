# Excavation 134 — Sparse Attention — Looking Without Comparing Everything

<!-- book-prose-v2 -->

A mixture of experts activates only a few specialists for each token. Long-context attention still compares too many token pairs, making communication—not expert capacity—the next computational bottleneck.

Nothing yet appears to demand a new invention. We can keep full attention and buy more hardware.

There is a real principle behind this restraint: the complexity of sparse attention must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The decisive test is this: doubling length roughly quadruples pairwise comparisons.

That distinction is the hinge on which sparse attention turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: preserve a small pattern of local, global, or retrieved connections that matches the task's information paths.

We have earned the chapter's shorter name: **Sparse Attention**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that sparse attention is necessary rather than decorative. Delete its new responsibility and use the earlier plan to keep full attention and buy more hardware. Immediately, doubling length roughly quadruples pairwise comparisons. Reintroduce the single job to preserve a small pattern of local, global, or retrieved connections that matches the task's information paths. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can preserve a small pattern of local, global, or retrieved connections that matches the task's information paths. Because the old plan to keep full attention and buy more hardware is the only displaced piece, the reader can locate exactly where sparse attention changes the outcome.

## Looking Without Comparing Everything

A document token attends nearby sentences plus section headings instead of every word in the book.

The name sparse attention is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

## Where sparse attention runs out

A sparse pattern can hide the one distant clue the answer needs.

The weakness is not an accidental footnote. Every operation in sparse attention serves the narrower purpose to preserve a small pattern of local, global, or retrieved connections that matches the task's information paths; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take sparse attention to the workbench

Understanding sparse attention now means predicting its intermediate results before asking software for an answer. Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running sparse attention, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the sparse attention result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [The wrong ideas worth preserving](mistakes.md); [Diagram and dependency path](diagram.md); [Invention exercises](exercises.md); [References and reading trail](references.md); and [Visual asset brief](images/README.md).

[Next: External Memory — Remembering Beyond the Context Window](../135-external-memory/README.md)
