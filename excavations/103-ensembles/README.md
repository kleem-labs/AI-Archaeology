# Excavation 103 — Ensembles

[Previous: Excavation 102](../102-bayesian-updating/README.md)

One trained model gives a confident answer. Would another equally trained model agree?

At first, the simplest answer is tempting: Trust one training run as the unique learned truth.

But the simplicity has discarded something important: Different initialization and data order produce different boundaries.

The missing information determines the next move: Train several diverse models and combine predictions while inspecting disagreement.

## Now work a case you can see

Five models vote tiger probabilities .9,.85,.88,.3,.25; the average is moderate and disagreement warns of model uncertainty.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Ensembles cost more and shared data can produce shared mistakes.

The reason is visible in the procedure. It knows how to train several diverse models and combine predictions while inspecting disagreement. The limitation above asks for another judgment, and no part of the procedure makes that judgment.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 104](../104-active-learning/README.md)
