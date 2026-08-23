# Excavation 126 — Hypotheses — Turning Curiosity into a Testable Claim

<!-- book-prose-v2 -->

> **PART XI — EARNING THE RIGHT TO IMPROVE**
>
> Discovery is no longer enough. Every proposed improvement must survive evidence, opposition, authority, and the possibility of reversal.

A bounded research system can propose and test changes without deploying them automatically. Its first obligation is to turn curiosity into a claim precise enough that an observation could prove it wrong.

The obvious economy is to ask whether more context makes the model better.

The proposal deserves a fair hearing. For hypotheses, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The decisive test is this: better at what, on which examples, compared with what baseline? Any result can be declared a success after the fact.

The failure changes the question behind hypotheses. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: state one predicted change, one intervention, one measurement, and one observation that would count against the claim.

Only at this point does the inherited name **Hypotheses** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of hypotheses by mentally removing the repair. We fall back to the proposal to ask whether more context makes the model better; then better at what, on which examples, compared with what baseline? Any result can be declared a success after the fact. Restore only the ability to state one predicted change, one intervention, one measurement, and one observation that would count against the claim, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to ask whether more context makes the model better to requiring the system to state one predicted change, one intervention, one measurement, and one observation that would count against the claim. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to hypotheses.

## Turning Curiosity into a Testable Claim

Predict that raising context from 128 to 256 tokens reduces held-out loss on long-reference stories but not shuffled stories.

Put the old procedure beside hypotheses. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## Where hypotheses runs out

A clean hypothesis can still test the wrong measurement.

The limit follows from the job assigned to hypotheses. Its repair knows how to state one predicted change, one intervention, one measurement, and one observation that would count against the claim. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take hypotheses to the workbench

A claim about hypotheses now exists on the page; the laboratory must be able to contradict it. Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running hypotheses, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the hypotheses result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [The wrong ideas worth preserving](mistakes.md); [Diagram and dependency path](diagram.md); [Invention exercises](exercises.md); [References and reading trail](references.md); and [Visual asset brief](images/README.md).

[Next: Experimental Design — Changing One Cause at a Time](../127-experimental-design/README.md)
