# Excavation 114 — Model-Based Planning

[Previous: Excavation 113](../113-counterfactuals/README.md)

A world model can predict one step. How should the agent choose a long action sequence?

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Commit to the first sequence imagined.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* One forecast may exploit model error or miss better branches.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Simulate multiple candidate sequences, score outcomes, act briefly, observe reality, and plan again.

Only after that reasoning may we give your discovery its inherited name.

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
