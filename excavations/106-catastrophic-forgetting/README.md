# Excavation 106 — Catastrophic Forgetting

Selective prediction gives the system permission to abstain. When an approved new task finally supplies more training data, learning it can overwrite skills that were reliable yesterday.

Using what we have, we fine-tune only on the newest data.

Yet updates useful for B overwrite weights carrying A.

So we rehearse old evidence, protect important parameters, or allocate new capacity.

## Let the case decide

Learning birds after mammals drops mammal accuracy; mixing a small mammal replay set preserves both.

## The boundary of the discovery

Memory, privacy, and capacity limit rehearsal.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 107](../107-continual-learning/README.md)
