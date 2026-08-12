# Excavation 114 — Model-Based Planning

Counterfactual reasoning compares unrealized alternatives for one case. Planning extends that question across a sequence, where each imagined action changes which choices and states can follow.

Perhaps we commit to the first sequence imagined.

The world refuses to cooperate: one forecast may exploit model error or miss better branches.

So we simulate multiple candidate sequences, score outcomes, act briefly, observe reality, and plan again.

## Let the case decide

A robot simulates left-right paths, takes one safe step, then updates after detecting an obstacle.

## The boundary of the discovery

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
