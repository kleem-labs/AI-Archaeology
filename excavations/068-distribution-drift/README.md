# Excavation 068 — Distribution Drift

<!-- book-prose-v2 -->

Online learning adapts quickly and can also absorb noise or attack just as quickly. The system must first distinguish ordinary variation from a genuine change in the source producing its inputs.

The first defensible move is to assume training accuracy remains valid forever.

There is a real principle behind this restraint: the complexity of distribution drift must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The proposal breaks for a specific reason, not by authority: a winter-trained demand model meets summer behavior and keeps reporting confident old patterns.

That distinction is the hinge on which distribution drift turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: monitor input, prediction, and outcome distributions; investigate meaningful shifts before retraining.

We have earned the chapter's shorter name: **Distribution Drift**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that distribution drift is necessary rather than decorative. Delete its new responsibility and use the earlier plan to assume training accuracy remains valid forever. Immediately, a winter-trained demand model meets summer behavior and keeps reporting confident old patterns. Reintroduce the single job to monitor input, prediction, and outcome distributions; investigate meaningful shifts before retraining. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can monitor input, prediction, and outcome distributions; investigate meaningful shifts before retraining. Because the old plan to assume training accuracy remains valid forever is the only displaced piece, the reader can locate exactly where distribution drift changes the outcome.

## Understanding distribution drift

Average order size moves from $40 to $75 while error doubles. The shift is evidence to inspect, not automatic permission to update.

The name distribution drift is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

## Where distribution drift runs out

Not every statistical shift changes the decision that matters.

The weakness is not an accidental footnote. Every operation in distribution drift serves the narrower purpose to monitor input, prediction, and outcome distributions; investigate meaningful shifts before retraining; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take distribution drift to the workbench

Understanding distribution drift now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running distribution drift, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the distribution drift result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 069](../069-controlled-experiments/README.md)
