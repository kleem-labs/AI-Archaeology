# Excavation 114 — Model-Based Planning

<!-- book-prose-v2 -->

Counterfactual reasoning compares unrealized alternatives for one case. Planning extends that question across a sequence, where each imagined action changes which choices and states can follow.

The obvious economy is to commit to the first sequence imagined.

The proposal deserves a fair hearing. For model-based planning, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Its hidden assumption becomes visible as soon as we observe that one forecast may exploit model error or miss better branches.

The failure changes the question behind model-based planning. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: simulate multiple candidate sequences, score outcomes, act briefly, observe reality, and plan again.

Only at this point does the inherited name **Model-Based Planning** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of model-based planning by mentally removing the repair. We fall back to the proposal to commit to the first sequence imagined; then one forecast may exploit model error or miss better branches. Restore only the ability to simulate multiple candidate sequences, score outcomes, act briefly, observe reality, and plan again, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to commit to the first sequence imagined to requiring the system to simulate multiple candidate sequences, score outcomes, act briefly, observe reality, and plan again. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to model-based planning.

## Understanding model-based planning

A robot simulates left-right paths, takes one safe step, then updates after detecting an obstacle.

Put the old procedure beside model-based planning. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## Where model-based planning runs out

Planning cost grows with horizon and branching.

The limit follows from the job assigned to model-based planning. Its repair knows how to simulate multiple candidate sequences, score outcomes, act briefly, observe reality, and plan again. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take model-based planning to the workbench

A claim about model-based planning now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running model-based planning, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the model-based planning result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 115](../115-tree-search/README.md)
