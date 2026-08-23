# Excavation 096 — Distributed Training

<!-- book-prose-v2 -->

Quantization reduces the precision and footprint of those weights. Training the largest systems still exceeds the memory and computation of one machine, forcing the work and state to be divided.

The least expensive next move is to let many machines train independent copies and combine them occasionally.

The proposal deserves a fair hearing. For distributed training, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Now keep that rule fixed and let the difficult case enter: their parameters drift and duplicated work wastes computation.

The failure changes the question behind distributed training. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: partition data or model work, synchronize required results, and preserve one coherent update.

Only at this point does the inherited name **Distributed Training** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of distributed training by mentally removing the repair. We fall back to the proposal to let many machines train independent copies and combine them occasionally; then their parameters drift and duplicated work wastes computation. Restore only the ability to partition data or model work, synchronize required results, and preserve one coherent update, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to let many machines train independent copies and combine them occasionally to requiring the system to partition data or model work, synchronize required results, and preserve one coherent update. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to distributed training.

## Understanding distributed training

Two workers compute gradients on different batches, average them, then apply the same update.

Put the old procedure beside distributed training. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## Where distributed training runs out

Communication, failure recovery, and numerical nondeterminism become bottlenecks.

The limit follows from the job assigned to distributed training. Its repair knows how to partition data or model work, synchronize required results, and preserve one coherent update. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take distributed training to the workbench

A claim about distributed training now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running distributed training, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the distributed training result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 097](../097-inference-serving/README.md)
