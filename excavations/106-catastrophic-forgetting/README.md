# Excavation 106 — Catastrophic Forgetting

[Previous: Excavation 105](../105-selective-prediction/README.md)

After learning task B, the model suddenly fails task A.

A reasonable place to begin is: Fine-tune only on the newest data.

Now place that proposal under pressure: Updates useful for B overwrite weights carrying A.

What broke tells us what the replacement must preserve: Rehearse old evidence, protect important parameters, or allocate new capacity.

## Now work a case you can see

Learning birds after mammals drops mammal accuracy; mixing a small mammal replay set preserves both.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

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
