# Excavation 131 — Synthetic Data — Letting a Model Write Lessons

[Previous excavation](../130-data-contamination/README.md)

Human examples are scarce. Can a model manufacture training data?

A reasonable place to begin is: Generate millions of answers and train on all of them.

Now place that proposal under pressure: Confident errors are copied, multiplied, and eventually treated as truth.

What broke tells us what the replacement must preserve: Generate candidates, verify what can be verified, preserve diversity, mix trusted data, and track ancestry.

Only here do we name the idea: **Synthetic Data**.

## Follow one case all the way through

Produce arithmetic problems, execute each answer, reject failures, and retain difficulty-balanced examples.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

Verification is weakest on the open-ended tasks where synthetic data is most tempting.

The repair is explicit: generate candidates, verify what can be verified, preserve diversity, mix trusted data, and track ancestry. Its power is also its boundary; anything not represented in those operations remains undecided.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Knowledge Distillation — Teaching a Smaller Student](../132-knowledge-distillation/README.md)
