# Excavation 105 — Selective Prediction

[Previous: Excavation 104](../104-active-learning/README.md)

Must the model answer every question, even when evidence is weak?

The first solution that suggests itself is this: Always return the highest-scoring answer.

The idea survives only until we test it against reality: A forced answer converts uncertainty into confident-looking error.

The failure gives us a precise requirement: Allow abstention and choose a coverage level whose retained answers meet a risk target.

## Now work a case you can see

The system answers 80 of 100 cases and is correct on 78; the other 20 go to a human rather than becoming guesses.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Abstention shifts work and may fail unevenly across groups.

The boundary follows from the mechanism itself. We designed it to Allow abstention and choose a coverage level whose retained answers meet a risk target. That operation solves the failure we had reached, but it contains no step that answers the additional problem above.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 106](../106-catastrophic-forgetting/README.md)
