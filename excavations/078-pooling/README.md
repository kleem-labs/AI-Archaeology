# Excavation 078 — Pooling — Keeping Evidence While Shrinking the Map

<!-- book-prose-v2 -->

Convolution slides one local detector across the whole image. The resulting activation maps preserve every detected location and quickly become too large for deeper processing.

The obvious economy is to keep every activation at full resolution through every layer.

The proposal deserves a fair hearing. For pooling, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The decisive test is this: memory explodes and tiny shifts move evidence to neighboring cells.

The failure changes the question behind pooling. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: summarize small neighborhoods while retaining the strongest or average evidence.

Only at this point does the inherited name **Pooling** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of pooling by mentally removing the repair. We fall back to the proposal to keep every activation at full resolution through every layer; then memory explodes and tiny shifts move evidence to neighboring cells. Restore only the ability to summarize small neighborhoods while retaining the strongest or average evidence, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to keep every activation at full resolution through every layer to requiring the system to summarize small neighborhoods while retaining the strongest or average evidence. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to pooling.

## Keeping Evidence While Shrinking the Map

Max pooling [1,7,2,3] keeps 7: an edge existed somewhere in that patch.

Put the old procedure beside pooling. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## Where pooling runs out

Pooling discards exact location and can erase subtle patterns.

The limit follows from the job assigned to pooling. Its repair knows how to summarize small neighborhoods while retaining the strongest or average evidence. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take pooling to the workbench

A claim about pooling now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running pooling, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the pooling result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 079](../079-cnn-hierarchy/README.md)
