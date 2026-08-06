# Excavation 117 — Neuro-Symbolic Systems

[Previous: Excavation 116](../116-reasoning-and-verification/README.md)

## Take the First Step Yourself

> **Your problem:** Neural models handle perception; symbolic rules handle exact constraints. Must one system do both?

> **Try your first idea:** Force fuzzy perception into rigid rules or exact rules into learned approximation.

> **Now try to break your idea:** The first breaks on noisy inputs; the second can violate guaranteed constraints.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Neural models handle perception; symbolic rules handle exact constraints. Must one system do both?

## Your First Attempt

Force fuzzy perception into rigid rules or exact rules into learned approximation.

## Break Your First Attempt

The first breaks on noisy inputs; the second can violate guaranteed constraints.

## Repair Your Attempt

Let neural components propose symbols or scores and symbolic components enforce explicit relations.

## What You Have Just Invented

**Let neural components propose symbols or scores and symbolic components enforce explicit relations.**

## Rebuild the Discovery with a Concrete Case

Vision detects board pieces; a chess engine enforces legal moves.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Real-World Limit

Errors at the interface can still corrupt the combined result.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 118](../118-knowledge-graphs/README.md)
