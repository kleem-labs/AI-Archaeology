# Excavation 105 — Selective Prediction

Active learning spends human effort where it should teach the most. A deployed system still encounters cases where no available evidence justifies any answer, even after labels have been chosen carefully.

At first we always return the highest-scoring answer.

But a forced answer converts uncertainty into confident-looking error.

That failure tells us to allow abstention and choose a coverage level whose retained answers meet a risk target.

## Let the case decide

The system answers 80 of 100 cases and is correct on 78; the other 20 go to a human rather than becoming guesses.

## The boundary of the discovery

Abstention shifts work and may fail unevenly across groups.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 106](../106-catastrophic-forgetting/README.md)
