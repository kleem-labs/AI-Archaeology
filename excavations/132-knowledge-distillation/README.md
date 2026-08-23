# Excavation 132 — Knowledge Distillation — Teaching a Smaller Student

<!-- book-prose-v2 -->

Synthetic data can expand training only when errors are verified instead of multiplied. The capable teacher generating or checking those lessons may be too large and costly for deployment.

The least expensive next move is to train a small model only on the original hard labels.

The proposal deserves a fair hearing. For knowledge distillation, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The proposal breaks for a specific reason, not by authority: the trouble appears immediately: the labels reveal the winner but discard how the teacher distributed doubt among alternatives.

The failure changes the question behind knowledge distillation. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: let the student imitate the teacher's probability pattern as well as the observed answer.

Only at this point does the inherited name **Knowledge Distillation** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of knowledge distillation by mentally removing the repair. We fall back to the proposal to train a small model only on the original hard labels; then the trouble appears immediately: the labels reveal the winner but discard how the teacher distributed doubt among alternatives. Restore only the ability to let the student imitate the teacher's probability pattern as well as the observed answer, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to train a small model only on the original hard labels to requiring the system to let the student imitate the teacher's probability pattern as well as the observed answer. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to knowledge distillation.

## Teaching a Smaller Student

For an animal image, 0.55 tiger, 0.40 leopard, 0.05 car teaches similarity that the label tiger hides.

Put the old procedure beside knowledge distillation. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## Where knowledge distillation runs out

The student also inherits the teacher's blind spots.

The limit follows from the job assigned to knowledge distillation. Its repair knows how to let the student imitate the teacher's probability pattern as well as the observed answer. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take knowledge distillation to the workbench

A claim about knowledge distillation now exists on the page; the laboratory must be able to contradict it. Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running knowledge distillation, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the knowledge distillation result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [The wrong ideas worth preserving](mistakes.md); [Diagram and dependency path](diagram.md); [Invention exercises](exercises.md); [References and reading trail](references.md); and [Visual asset brief](images/README.md).

[Next: Mixture of Experts — Spending Computation Where It Helps](../133-mixture-of-experts/README.md)
