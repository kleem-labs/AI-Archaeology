# Excavation 117 — Neuro-Symbolic Systems

[Previous: Excavation 116](../116-reasoning-and-verification/README.md)

Neural models handle perception; symbolic rules handle exact constraints. Must one system do both?

Without knowing the inherited method, we might try this: Force fuzzy perception into rigid rules or exact rules into learned approximation.

Its hidden assumption appears in the following case: The first breaks on noisy inputs; the second can violate guaranteed constraints.

Remove that assumption and the needed repair becomes clear: Let neural components propose symbols or scores and symbolic components enforce explicit relations.

## Now work a case you can see

Vision detects board pieces; a chess engine enforces legal moves.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Errors at the interface can still corrupt the combined result.

This is not an unrelated warning. The construction can let neural components propose symbols or scores and symbolic components enforce explicit relations. It cannot infer or control information that never enters that construction.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 118](../118-knowledge-graphs/README.md)
