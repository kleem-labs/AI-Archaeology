# Excavation 134 — Sparse Attention — Looking Without Comparing Everything

A mixture of experts activates only a few specialists for each token. Long-context attention still compares too many token pairs, making communication—not expert capacity—the next computational bottleneck.

One tempting answer is to keep full attention and buy more hardware.

The world refuses to cooperate: doubling length roughly quadruples pairwise comparisons.

So we preserve a small pattern of local, global, or retrieved connections that matches the task's information paths.

## Let the case decide

A document token attends nearby sentences plus section headings instead of every word in the book.

## The boundary of the discovery

A sparse pattern can hide the one distant clue the answer needs.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: External Memory — Remembering Beyond the Context Window](../135-external-memory/README.md)
