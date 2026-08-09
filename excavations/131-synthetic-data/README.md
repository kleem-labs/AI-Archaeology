# Excavation 131 — Synthetic Data — Letting a Model Write Lessons

[Previous excavation](../130-data-contamination/README.md)

Human examples are scarce. Can a model manufacture training data?

Before inheriting a technique, make the first decision yourself. Generate millions of answers and train on all of them.

For a moment, the idea appears sufficient. Then reality supplies the case it cannot explain: Confident errors are copied, multiplied, and eventually treated as truth.

The failure tells you what the repair must accomplish. Generate candidates, verify what can be verified, preserve diversity, mix trusted data, and track ancestry.

Only now have you earned the chapter's name: **Synthetic Data**.

## Follow one case all the way through

Produce arithmetic problems, execute each answer, reject failures, and retain difficulty-balanced examples.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

Verification is weakest on the open-ended tasks where synthetic data is most tempting.

That limit is not a footnote. It is the pressure that forces the next excavation.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Knowledge Distillation — Teaching a Smaller Student](../132-knowledge-distillation/README.md)
