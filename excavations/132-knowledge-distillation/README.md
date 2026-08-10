# Excavation 132 — Knowledge Distillation — Teaching a Smaller Student

[Previous excavation](../131-synthetic-data/README.md)

A capable model is too expensive to deploy on a phone.

Without knowing the inherited method, we might try this: Train a small model only on the original hard labels.

Its hidden assumption appears in the following case: The labels reveal the winner but discard how the teacher distributed doubt among alternatives.

Remove that assumption and the needed repair becomes clear: Let the student imitate the teacher's probability pattern as well as the observed answer.

Only here do we name the idea: **Knowledge Distillation**.

## Follow one case all the way through

For an animal image, 0.55 tiger, 0.40 leopard, 0.05 car teaches similarity that the label tiger hides.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

The student also inherits the teacher's blind spots.

This is not an unrelated warning. The construction can let the student imitate the teacher's probability pattern as well as the observed answer. It cannot infer or control information that never enters that construction.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Mixture of Experts — Spending Computation Where It Helps](../133-mixture-of-experts/README.md)
