# Excavation 150 — A Bounded Self-Improving System — Close the Research Loop

<!-- book-prose-v2 -->

Pre-deployment evaluation can reject a dangerous candidate before the world pays for the experiment. A measured improvement must still pass reproducibility, impact review, authorization, staged release, monitoring, and rollback before it may replace the system that proposed it.

The obvious economy is to let every measured gain replace the current system automatically.

The proposal deserves a fair hearing. For a bounded self-improving system, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The decisive test is this: contaminated tests, reward hacks, or one lucky run can promote a worse and less controllable successor.

The failure changes the question behind a bounded self-improving system. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: separate proposal, sandboxed experiment, reproducibility, independent evaluation, impact review, authorization, staged release, and rollback.

Only at this point does the inherited name **A Bounded Self-Improving System** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of a bounded self-improving system by mentally removing the repair. We fall back to the proposal to let every measured gain replace the current system automatically; then contaminated tests, reward hacks, or one lucky run can promote a worse and less controllable successor. Restore only the ability to separate proposal, sandboxed experiment, reproducibility, independent evaluation, impact review, authorization, staged release, and rollback, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to let every measured gain replace the current system automatically to requiring the system to separate proposal, sandboxed experiment, reproducibility, independent evaluation, impact review, authorization, staged release, and rollback. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to a bounded self-improving system.

## Close the Research Loop

A tokenizer change advances only after repeated clean tests, safety checks, signed approval, a small canary release, and monitored rollback criteria.

Put the old procedure beside a bounded self-improving system. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## Where a bounded self-improving system runs out

The loop remains only as wise as its objectives, evidence, boundaries, and accountable humans.

The limit follows from the job assigned to a bounded self-improving system. Its repair knows how to separate proposal, sandboxed experiment, reproducibility, independent evaluation, impact review, authorization, staged release, and rollback. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take a bounded self-improving system to the workbench

A claim about a bounded self-improving system now exists on the page; the laboratory must be able to contradict it. Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running a bounded self-improving system, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the a bounded self-improving system result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [The wrong ideas worth preserving](mistakes.md); [Diagram and dependency path](diagram.md); [Invention exercises](exercises.md); [References and reading trail](references.md); and [Visual asset brief](images/README.md).
