# Excavation 103 — Ensembles

Bayesian updating combines prior plausibility with the likelihood of new evidence. One trained model can still be confidently wrong about its own uncertainty, so we ask whether independently trained models agree.

We first try to trust one training run as the unique learned truth.

That confidence lasts only until different initialization and data order produce different boundaries.

We need to train several diverse models and combine predictions while inspecting disagreement.

## Let the case decide

Five models vote tiger probabilities .9,.85,.88,.3,.25; the average is moderate and disagreement warns of model uncertainty.

## The boundary of the discovery

Ensembles cost more and shared data can produce shared mistakes.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 104](../104-active-learning/README.md)
