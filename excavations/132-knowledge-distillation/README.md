# Excavation 132 — Knowledge Distillation — Teaching a Smaller Student

[Previous excavation](../131-synthetic-data/README.md)

A capable model is too expensive to deploy on a phone.

Before inheriting a technique, make the first decision yourself. Train a small model only on the original hard labels.

For a moment, the idea appears sufficient. Then reality supplies the case it cannot explain: The labels reveal the winner but discard how the teacher distributed doubt among alternatives.

The failure tells you what the repair must accomplish. Let the student imitate the teacher's probability pattern as well as the observed answer.

Only now have you earned the chapter's name: **Knowledge Distillation**.

## Follow one case all the way through

For an animal image, 0.55 tiger, 0.40 leopard, 0.05 car teaches similarity that the label tiger hides.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

The student also inherits the teacher's blind spots.

That limit is not a footnote. It is the pressure that forces the next excavation.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Mixture of Experts — Spending Computation Where It Helps](../133-mixture-of-experts/README.md)
