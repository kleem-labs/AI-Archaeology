# Excavation 128 — Reproducibility — Can the Discovery Survive Another Run?

<!-- book-prose-v2 -->

Experimental design isolates one suspected cause and provides a control. A single successful run can still be a favorable random seed rather than a discovery that will survive repetition.

The first defensible move is to keep the best checkpoint and report its score.

There is a real principle behind this restraint: the complexity of reproducibility must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Now keep that rule fixed and let the difficult case enter: changing only the random seed makes the gain disappear.

That distinction is the hinge on which reproducibility turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: record code, data, configuration, environment, seeds, and variation across repeated runs.

We have earned the chapter's shorter name: **Reproducibility**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that reproducibility is necessary rather than decorative. Delete its new responsibility and use the earlier plan to keep the best checkpoint and report its score. Immediately, changing only the random seed makes the gain disappear. Reintroduce the single job to record code, data, configuration, environment, seeds, and variation across repeated runs. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can record code, data, configuration, environment, seeds, and variation across repeated runs. Because the old plan to keep the best checkpoint and report its score is the only displaced piece, the reader can locate exactly where reproducibility changes the outcome.

## Can the Discovery Survive Another Run

Run five seeds; compare the distribution of gains rather than celebrating the luckiest one.

The name reproducibility is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

## Where reproducibility runs out

Repeated agreement does not remove a shared bias in all runs.

The weakness is not an accidental footnote. Every operation in reproducibility serves the narrower purpose to record code, data, configuration, environment, seeds, and variation across repeated runs; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take reproducibility to the workbench

Understanding reproducibility now means predicting its intermediate results before asking software for an answer. Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running reproducibility, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the reproducibility result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [The wrong ideas worth preserving](mistakes.md); [Diagram and dependency path](diagram.md); [Invention exercises](exercises.md); [References and reading trail](references.md); and [Visual asset brief](images/README.md).

[Next: Benchmarks — Building a Ruler Before Measuring Progress](../129-benchmarks/README.md)
