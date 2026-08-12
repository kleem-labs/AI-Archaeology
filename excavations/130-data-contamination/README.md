# Excavation 130 — Data Contamination — When the Test Was Secretly Homework

Benchmarks freeze tasks and metrics before results are known. A model may score well because those supposedly unseen questions, or close paraphrases, appeared in its training data.

Using what we have, we assume held-out files guarantee unseen knowledge.

But the same questions appeared online in training data with small formatting changes.

So we track provenance, search for semantic overlap, use time-separated tests, and create private fresh evaluations.

## Let the case decide

A supposedly unseen riddle shares its distinctive answer phrase with a training document; remove the overlap and retest.

## The boundary of the discovery

No detector can prove absence from an unknown corpus.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Synthetic Data — Letting a Model Write Lessons](../131-synthetic-data/README.md)
