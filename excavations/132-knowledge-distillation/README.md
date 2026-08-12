# Excavation 132 — Knowledge Distillation — Teaching a Smaller Student

Synthetic data can expand training only when errors are verified instead of multiplied. The capable teacher generating or checking those lessons may be too large and costly for deployment.

Perhaps we train a small model only on the original hard labels.

The trouble appears immediately: the labels reveal the winner but discard how the teacher distributed doubt among alternatives.

Now we can see what is missing: we must let the student imitate the teacher's probability pattern as well as the observed answer.

## Let the case decide

For an animal image, 0.55 tiger, 0.40 leopard, 0.05 car teaches similarity that the label tiger hides.

## The boundary of the discovery

The student also inherits the teacher's blind spots.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Mixture of Experts — Spending Computation Where It Helps](../133-mixture-of-experts/README.md)
