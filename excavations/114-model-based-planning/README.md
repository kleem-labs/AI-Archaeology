# Excavation 114 — Model-Based Planning

[Previous: Excavation 113](../113-counterfactuals/README.md)

A world model can predict one step. How should the agent choose a long action sequence?

Our first construction is deliberately modest: Commit to the first sequence imagined.

It works—right up to this boundary: One forecast may exploit model error or miss better branches.

Crossing that boundary requires one additional idea: Simulate multiple candidate sequences, score outcomes, act briefly, observe reality, and plan again.

## Now work a case you can see

A robot simulates left-right paths, takes one safe step, then updates after detecting an obstacle.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Planning cost grows with horizon and branching.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 115](../115-tree-search/README.md)
