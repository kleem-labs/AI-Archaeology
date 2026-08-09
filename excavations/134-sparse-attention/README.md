# Excavation 134 — Sparse Attention — Looking Without Comparing Everything

[Previous excavation](../133-mixture-of-experts/README.md)

Long context makes every token compare with every other token.

Before inheriting a technique, make the first decision yourself. Keep full attention and buy more hardware.

For a moment, the idea appears sufficient. Then reality supplies the case it cannot explain: Doubling length roughly quadruples pairwise comparisons.

The failure tells you what the repair must accomplish. Preserve a small pattern of local, global, or retrieved connections that matches the task's information paths.

Only now have you earned the chapter's name: **Sparse Attention**.

## Follow one case all the way through

A document token attends nearby sentences plus section headings instead of every word in the book.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

A sparse pattern can hide the one distant clue the answer needs.

That limit is not a footnote. It is the pressure that forces the next excavation.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: External Memory — Remembering Beyond the Context Window](../135-external-memory/README.md)
