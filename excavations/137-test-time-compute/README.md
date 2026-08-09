# Excavation 137 — Test-Time Compute — Thinking Longer on Harder Problems

[Previous excavation](../136-long-context-retrieval/README.md)

One fixed forward pass treats an easy lookup and a hard proof as equal work.

Before inheriting a technique, make the first decision yourself. Make every model response extremely long.

For a moment, the idea appears sufficient. Then reality supplies the case it cannot explain: Easy tasks waste computation while long fluent mistakes become more convincing.

The failure tells you what the repair must accomplish. Allocate extra attempts or steps only when uncertainty and verification justify their cost.

Only now have you earned the chapter's name: **Test-Time Compute**.

## Follow one case all the way through

Answer 2+2 immediately, but generate and check several candidate routes for a scheduling puzzle.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

More computation amplifies a bad objective or unreliable verifier.

That limit is not a footnote. It is the pressure that forces the next excavation.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Search and Verification — Separate Proposing from Checking](../138-search-and-verification/README.md)
