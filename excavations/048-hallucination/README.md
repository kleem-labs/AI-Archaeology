# Excavation 048 — Hallucination — When Fluent Prediction Outruns Evidence

<!-- book-prose-v2 -->

Evaluation therefore begins with the job the system is supposed to perform. On that job, a disturbing failure remains: the model can produce a beautifully fluent answer even when no evidence supports it.

The least expensive next move is to trust fluent language because uncertainty should sound hesitant.

The proposal deserves a fair hearing. For hallucination, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Now keep that rule fixed and let the difficult case enter: training rewards plausible continuations. A fabricated citation can match the shape of real citations and therefore sound more natural than “I do not know.”.

The failure changes the question behind hallucination. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source.

Only at this point does the inherited name **Hallucination** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of hallucination by mentally removing the repair. We fall back to the proposal to trust fluent language because uncertainty should sound hesitant; then training rewards plausible continuations. A fabricated citation can match the shape of real citations and therefore sound more natural than “I do not know.”. Restore only the ability to separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to trust fluent language because uncertainty should sound hesitant to requiring the system to separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to hallucination.

## When Fluent Prediction Outruns Evidence

The prompt asks for the 2018 paper “Tiger Attention Networks.” Search returns no matching source. A supported system must say no source was found instead of completing the familiar citation pattern.

Put the old procedure beside hallucination. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## Where hallucination runs out

Evidence reduces unsupported claims but sources can be wrong, stale, conflicting, or misread.

The limit follows from the job assigned to hallucination. Its repair knows how to separate linguistic plausibility from supported knowledge. Require evidence, permit abstention, and test whether claims can be traced to an available source. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take hallucination to the workbench

A claim about hallucination now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running hallucination, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the hallucination result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 049](../049-calibration/README.md)
