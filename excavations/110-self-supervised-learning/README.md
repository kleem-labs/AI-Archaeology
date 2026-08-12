# Excavation 110 — Self-Supervised Learning

Curriculum learning controls the order of experience. The supply of human labels still limits every curriculum, while raw text, images, and audio contain countless prediction problems whose answers are present in the data itself.

One tempting answer is to wait for humans to label every example.

But labels are expensive and discard most structure already inside observations.

So we hide or transform part of an observation and train the model to recover the missing relation.

## Let the case decide

Mask one image patch and predict it from neighbors; no human label is needed.

## The boundary of the discovery

Pretext tasks may reward patterns unrelated to downstream needs.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 111](../111-world-models/README.md)
