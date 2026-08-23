# Excavation 110 — Self-Supervised Learning

<!-- book-prose-v2 -->

Curriculum learning controls the order of experience. The supply of human labels still limits every curriculum, while raw text, images, and audio contain countless prediction problems whose answers are present in the data itself.

Nothing yet appears to demand a new invention. We can wait for humans to label every example.

There is a real principle behind this restraint: the complexity of self-supervised learning must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The decisive test is this: labels are expensive and discard most structure already inside observations.

That distinction is the hinge on which self-supervised learning turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: hide or transform part of an observation and train the model to recover the missing relation.

We have earned the chapter's shorter name: **Self-Supervised Learning**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that self-supervised learning is necessary rather than decorative. Delete its new responsibility and use the earlier plan to wait for humans to label every example. Immediately, labels are expensive and discard most structure already inside observations. Reintroduce the single job to hide or transform part of an observation and train the model to recover the missing relation. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can hide or transform part of an observation and train the model to recover the missing relation. Because the old plan to wait for humans to label every example is the only displaced piece, the reader can locate exactly where self-supervised learning changes the outcome.

## Understanding self-supervised learning

Mask one image patch and predict it from neighbors; no human label is needed.

The name self-supervised learning is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

## Where self-supervised learning runs out

Pretext tasks may reward patterns unrelated to downstream needs.

The weakness is not an accidental footnote. Every operation in self-supervised learning serves the narrower purpose to hide or transform part of an observation and train the model to recover the missing relation; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take self-supervised learning to the workbench

Understanding self-supervised learning now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running self-supervised learning, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the self-supervised learning result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 111](../111-world-models/README.md)
