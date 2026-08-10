# Excavation 074 — Superposition

[Previous: Excavation 073](../073-attribution/README.md)

A network stores more useful features than it has individual neurons.

Our first construction is deliberately modest: Demand one feature per coordinate.

It works—right up to this boundary: Limited width forces useful patterns to share neurons, producing confusing mixed activations.

Crossing that boundary requires one additional idea: Represent features as directions that can overlap when they rarely need to be active together.

## Now work a case you can see

One two-dimensional space stores several sparse directions; collisions occur mainly when multiple stored features activate together.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

Separating superposed features is difficult and may not yield unique answers.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 075](../075-causal-interventions/README.md)
