# Excavation 108 — Meta-Learning

<!-- book-prose-v2 -->

Continual learning protects the past but may still require many examples for every genuinely new task. Experience across tasks could teach not only solutions, but a better procedure for adapting quickly.

The least expensive next move is to train one universal fixed solution.

The proposal deserves a fair hearing. For meta-learning, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The proposal breaks for a specific reason, not by authority: a new task with different labels requires many examples and broad retraining.

The failure changes the question behind meta-learning. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: optimize prior parameters or an update rule so a few new examples produce useful adaptation.

Only at this point does the inherited name **Meta-Learning** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of meta-learning by mentally removing the repair. We fall back to the proposal to train one universal fixed solution; then a new task with different labels requires many examples and broad retraining. Restore only the ability to optimize prior parameters or an update rule so a few new examples produce useful adaptation, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to train one universal fixed solution to requiring the system to optimize prior parameters or an update rule so a few new examples produce useful adaptation. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to meta-learning.

## Understanding meta-learning

After many two-class tasks, five labeled examples are enough to separate two unseen animal species.

Put the old procedure beside meta-learning. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## Where meta-learning runs out

Task distributions can be narrow and meta-learning can overfit them.

The limit follows from the job assigned to meta-learning. Its repair knows how to optimize prior parameters or an update rule so a few new examples produce useful adaptation. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take meta-learning to the workbench

A claim about meta-learning now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running meta-learning, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the meta-learning result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 109](../109-curriculum-learning/README.md)
