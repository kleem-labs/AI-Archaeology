# Excavation 120 — Program Synthesis

<!-- book-prose-v2 -->

Graph neural networks propagate learned messages through relational structure. Some tasks demand more than one answer: they demand a reusable procedure that maps every allowed input to an output.

The least expensive next move is to memorize the provided input-output pairs.

The proposal deserves a fair hearing. For program synthesis, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Now keep that rule fixed and let the difficult case enter: a new input exposes the absence of an underlying algorithm.

The failure changes the question behind program synthesis. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: search or generate candidate programs, execute them, and keep those satisfying examples and constraints.

Only at this point does the inherited name **Program Synthesis** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of program synthesis by mentally removing the repair. We fall back to the proposal to memorize the provided input-output pairs; then a new input exposes the absence of an underlying algorithm. Restore only the ability to search or generate candidate programs, execute them, and keep those satisfying examples and constraints, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to memorize the provided input-output pairs to requiring the system to search or generate candidate programs, execute them, and keep those satisfying examples and constraints. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to program synthesis.

## Understanding program synthesis

Examples 2→4 and 3→6 suggest multiply by two; testing 5 distinguishes it from memorized lookup.

Put the old procedure beside program synthesis. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## Where program synthesis runs out

Finite examples rarely identify one unique intended program.

The limit follows from the job assigned to program synthesis. Its repair knows how to search or generate candidate programs, execute them, and keep those satisfying examples and constraints. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take program synthesis to the workbench

A claim about program synthesis now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running program synthesis, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the program synthesis result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 121](../121-formal-verification/README.md)
