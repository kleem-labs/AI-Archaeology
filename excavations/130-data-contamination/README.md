# Excavation 130 — Data Contamination — When the Test Was Secretly Homework

[Previous excavation](../129-benchmarks/README.md)

A model scores perfectly on a benchmark. Did it generalize?

The first solution that suggests itself is this: Assume held-out files guarantee unseen knowledge.

The idea survives only until we test it against reality: The same questions appeared online in training data with small formatting changes.

The failure gives us a precise requirement: Track provenance, search for semantic overlap, use time-separated tests, and create private fresh evaluations.

Only here do we name the idea: **Data Contamination**.

## Follow one case all the way through

A supposedly unseen riddle shares its distinctive answer phrase with a training document; remove the overlap and retest.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

No detector can prove absence from an unknown corpus.

The boundary follows from the mechanism itself. We designed it to track provenance, search for semantic overlap, use time-separated tests, and create private fresh evaluations. That operation solves the failure we had reached, but it contains no step that answers the additional problem above.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Synthetic Data — Letting a Model Write Lessons](../131-synthetic-data/README.md)
