# Excavation 138 — Search and Verification — Separate Proposing from Checking

<!-- book-prose-v2 -->

Test-time compute lets hard problems receive more attempts. More attempts also produce more plausible mistakes, so proposing candidate paths must be separated from checking them.

The obvious economy is to ask the same generator to confidently approve its own first answer.

The proposal deserves a fair hearing. For search and verification, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Its hidden assumption becomes visible as soon as we observe that the error that shaped the proposal also shapes its self-justification.

The failure changes the question behind search and verification. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: generate diverse candidates, check them with independent evidence, and keep only paths that survive.

Only at this point does the inherited name **Search and Verification** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of search and verification by mentally removing the repair. We fall back to the proposal to ask the same generator to confidently approve its own first answer; then the error that shaped the proposal also shapes its self-justification. Restore only the ability to generate diverse candidates, check them with independent evidence, and keep only paths that survive, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to ask the same generator to confidently approve its own first answer to requiring the system to generate diverse candidates, check them with independent evidence, and keep only paths that survive. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to search and verification.

## Separate Proposing from Checking

Propose five programs for a specification and run hidden tests before selecting one.

Put the old procedure beside search and verification. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## Where search and verification runs out

A weak verifier rewards solutions that exploit its blind spots.

The limit follows from the job assigned to search and verification. Its repair knows how to generate diverse candidates, check them with independent evidence, and keep only paths that survive. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take search and verification to the workbench

A claim about search and verification now exists on the page; the laboratory must be able to contradict it. Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running search and verification, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the search and verification result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [The wrong ideas worth preserving](mistakes.md); [Diagram and dependency path](diagram.md); [Invention exercises](exercises.md); [References and reading trail](references.md); and [Visual asset brief](images/README.md).

[Next: Process Supervision — Rewarding the Path, Not Only the Answer](../139-process-supervision/README.md)
