# Excavation 054 — Retrieval-Augmented Generation — Let the Model Look Before It Speaks

<!-- book-prose-v2 -->

Preference learning lets reviewers distinguish answers that are all technically possible. Even the preferred answer may rely on stale memory when the question asks about a document or fact that changed after training.

The obvious economy is to retrain the whole model whenever one document changes.

The proposal deserves a fair hearing. For retrieval-augmented generation, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The decisive test is this: a price changes today, a policy changes tomorrow, and private documents cannot all be baked into public weights. Retraining is slow and still hides the source.

The failure changes the question behind retrieval-augmented generation. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved.

Only at this point does the inherited name **Retrieval-Augmented Generation** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of retrieval-augmented generation by mentally removing the repair. We fall back to the proposal to retrain the whole model whenever one document changes; then a price changes today, a policy changes tomorrow, and private documents cannot all be baked into public weights. Retraining is slow and still hides the source. Restore only the ability to search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to retrain the whole model whenever one document changes to requiring the system to search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to retrieval-augmented generation.

## Let the Model Look Before It Speaks

The user asks for today’s return policy. Retrieval selects the current policy document, not an old blog post. The answer quotes the 30-day rule and links it to that document.

Put the old procedure beside retrieval-augmented generation. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## Where retrieval-augmented generation runs out

Retrieval can miss the right document or return misleading text. Generation must distinguish evidence from instructions embedded inside evidence.

The limit follows from the job assigned to retrieval-augmented generation. Its repair knows how to search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take retrieval-augmented generation to the workbench

A claim about retrieval-augmented generation now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running retrieval-augmented generation, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the retrieval-augmented generation result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 055](../055-tool-using-agents/README.md)
