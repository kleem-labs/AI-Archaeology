# Excavation 110 — Self-Supervised Learning

[Previous: Excavation 109](../109-curriculum-learning/README.md)

How can enormous unlabeled data teach useful representations?

The first solution that suggests itself is this: Wait for humans to label every example.

The idea survives only until we test it against reality: Labels are expensive and discard most structure already inside observations.

The failure gives us a precise requirement: Hide or transform part of an observation and train the model to recover the missing relation.

## Now work a case you can see

Mask one image patch and predict it from neighbors; no human label is needed.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Pretext tasks may reward patterns unrelated to downstream needs.

The boundary follows from the mechanism itself. We designed it to hide or transform part of an observation and train the model to recover the missing relation. That operation solves the failure we had reached, but it contains no step that answers the additional problem above.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 111](../111-world-models/README.md)
