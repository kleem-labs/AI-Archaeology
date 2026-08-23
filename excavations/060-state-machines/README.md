# Excavation 060 — State Machines — Knowing What Has Actually Happened

<!-- book-prose-v2 -->

Memory carries chosen information across contexts. Remembering that an email was intended does not establish that it was sent; real workflows need an authoritative account of which events actually changed state.

The least expensive next move is to let the conversation prose serve as the workflow state.

The proposal deserves a fair hearing. For state machines, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The proposal breaks for a specific reason, not by authority: the model says “refund completed” after merely drafting it, or issues it twice after losing track of an earlier tool result.

The failure changes the question behind state machines. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system.

Only at this point does the inherited name **State Machines** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of state machines by mentally removing the repair. We fall back to the proposal to let the conversation prose serve as the workflow state; then the model says “refund completed” after merely drafting it, or issues it twice after losing track of an earlier tool result. Restore only the ability to represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to let the conversation prose serve as the workflow state to requiring the system to represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to state machines.

## Knowing What Has Actually Happened

A refund moves requested → approved only with an approval record, then approved → issued only with a payment transaction ID. A sentence alone changes nothing.

State Machines earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

Put the old procedure beside state machines. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## Where state machines runs out

Real workflows have exceptions and concurrent events. State machines need recovery paths and authoritative external records.

The limit follows from the job assigned to state machines. Its repair knows how to represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take state machines to the workbench

A claim about state machines now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running state machines, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the state machines result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 061](../061-verification/README.md)
