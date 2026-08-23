# Excavation 144 — Impact Measures — Notice What Changed Besides the Goal

<!-- book-prose-v2 -->

Uncertainty-aware planning carries several plausible worlds and may seek information before acting. Even a plan that succeeds in all of them can alter unrelated parts of the world unnecessarily.

The least expensive next move is to score only the requested final condition.

The proposal deserves a fair hearing. For impact measures, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Now keep that rule fixed and let the difficult case enter: unnecessary irreversible changes remain invisible to the goal score.

The failure changes the question behind impact measures. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: compare the resulting world with a reasonable baseline and penalize avoidable side effects.

Only at this point does the inherited name **Impact Measures** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of impact measures by mentally removing the repair. We fall back to the proposal to score only the requested final condition; then unnecessary irreversible changes remain invisible to the goal score. Restore only the ability to compare the resulting world with a reasonable baseline and penalize avoidable side effects, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to score only the requested final condition to requiring the system to compare the resulting world with a reasonable baseline and penalize avoidable side effects. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to impact measures.

## Notice What Changed Besides the Goal

Cleaning the spill changes one patch of floor; moving every chair and deleting files changes unrelated state.

Put the old procedure beside impact measures. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## Where impact measures runs out

A baseline can punish beneficial change or preserve an unjust status quo.

The limit follows from the job assigned to impact measures. Its repair knows how to compare the resulting world with a reasonable baseline and penalize avoidable side effects. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take impact measures to the workbench

A claim about impact measures now exists on the page; the laboratory must be able to contradict it. Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running impact measures, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the impact measures result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [The wrong ideas worth preserving](mistakes.md); [Diagram and dependency path](diagram.md); [Invention exercises](exercises.md); [References and reading trail](references.md); and [Visual asset brief](images/README.md).

[Next: Human Oversight — Put Judgment at the Irreversible Edge](../145-human-oversight/README.md)
