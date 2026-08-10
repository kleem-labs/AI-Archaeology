# Excavation 069 — Controlled Experiments

[Previous: Excavation 068](../068-distribution-drift/README.md)

A new model performs better after launch, but traffic and season also changed.

Our first construction is deliberately modest: Compare this week with last week.

It works—right up to this boundary: A holiday raises sales for both systems and receives credit as a model improvement.

Crossing that boundary requires one additional idea: Randomly assign comparable cases to old and new behavior and compare predefined outcomes.

## Now work a case you can see

Split 10,000 simultaneous visitors evenly; conversion is 5% for control and 5.5% for treatment under the same week.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

Experiments require sufficient samples, ethical limits, and careful metrics.

Why does the boundary remain? Our new machinery only knows how to randomly assign comparable cases to old and new behavior and compare predefined outcomes. Solving that problem does not automatically solve every decision built on top of it.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 070](../070-bandits/README.md)
