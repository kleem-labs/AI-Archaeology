# Excavation 104 — Active Learning

<!-- book-prose-v2 -->

An ensemble turns disagreement into evidence about model uncertainty. When labels are expensive, that disagreement can guide which unlabeled case deserves a human answer next.

The first defensible move is to label random examples forever.

There is a real principle behind this restraint: the complexity of active learning must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Now keep that rule fixed and let the difficult case enter: thousands of easy repeated cases consume effort while the decision boundary remains unclear.

That distinction is the hinge on which active learning turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: ask for labels where the model is uncertain or where examples add new coverage.

We have earned the chapter's shorter name: **Active Learning**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that active learning is necessary rather than decorative. Delete its new responsibility and use the earlier plan to label random examples forever. Immediately, thousands of easy repeated cases consume effort while the decision boundary remains unclear. Reintroduce the single job to ask for labels where the model is uncertain or where examples add new coverage. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can ask for labels where the model is uncertain or where examples add new coverage. Because the old plan to label random examples forever is the only displaced piece, the reader can locate exactly where active learning changes the outcome.

## Understanding active learning

The model knows obvious cats and dogs but splits 50–50 on one fox-like animal; labeling it teaches more than another obvious cat.

The name active learning is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

## Where active learning runs out

Uncertainty sampling can chase noise or outliers.

The weakness is not an accidental footnote. Every operation in active learning serves the narrower purpose to ask for labels where the model is uncertain or where examples add new coverage; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take active learning to the workbench

Understanding active learning now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running active learning, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the active learning result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 105](../105-selective-prediction/README.md)
