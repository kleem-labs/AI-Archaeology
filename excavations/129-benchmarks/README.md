# Excavation 129 — Benchmarks — Building a Ruler Before Measuring Progress

[Previous excavation](../128-reproducibility/README.md)

Every team says its model is better, but each chooses different tasks.

Our first construction is deliberately modest: Let each model demonstrate its strongest example.

It works—right up to this boundary: A showcase cannot support comparison because difficulty and scoring move with the contestant.

Crossing that boundary requires one additional idea: Freeze representative tasks, inputs, metrics, and scoring rules before seeing results.

Only here do we name the idea: **Benchmarks**.

## Follow one case all the way through

Give three navigation agents the same maps, action budget, and success definition.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

A fixed ruler becomes stale when people optimize specifically for it.

That limit is not a footnote. It is the pressure that forces the next excavation.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Data Contamination — When the Test Was Secretly Homework](../130-data-contamination/README.md)
