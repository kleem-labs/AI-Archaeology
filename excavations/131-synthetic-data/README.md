# Excavation 131 — Synthetic Data — Letting a Model Write Lessons

Contamination turns the test into disguised homework. Fresh human-written data is expensive, tempting the model to manufacture far more lessons for itself.

An obvious shortcut is to generate millions of answers and train on all of them.

Yet confident errors are copied, multiplied, and eventually treated as truth.

We need to generate candidates, verify what can be verified, preserve diversity, mix trusted data, and track ancestry.

## Let the case decide

Produce arithmetic problems, execute each answer, reject failures, and retain difficulty-balanced examples.

## The boundary of the discovery

Verification is weakest on the open-ended tasks where synthetic data is most tempting.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Knowledge Distillation — Teaching a Smaller Student](../132-knowledge-distillation/README.md)
