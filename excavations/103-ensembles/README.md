# Excavation 103 — Ensembles

[Previous: Excavation 102](../102-bayesian-updating/README.md)

One trained model gives a confident answer. Would another equally trained model agree?

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Trust one training run as the unique learned truth.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Different initialization and data order produce different boundaries.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Train several diverse models and combine predictions while inspecting disagreement.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

Five models vote tiger probabilities .9,.85,.88,.3,.25; the average is moderate and disagreement warns of model uncertainty.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

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
