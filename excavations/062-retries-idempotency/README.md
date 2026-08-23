# Excavation 062 — Retries and Idempotency — Trying Again Without Doing It Twice

<!-- book-prose-v2 -->

Verification compares the intended effect with reality. When the evidence is absent because a request timed out, trying again may repeat an action that actually succeeded the first time.

Nothing yet appears to demand a new invention. We can retry the action whenever a response is missing.

There is a real principle behind this restraint: the complexity of retries and idempotency must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The decisive test is this: the trouble appears immediately: the first payment succeeded and the retry charges the customer twice.

That distinction is the hinge on which retries and idempotency turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect.

We have earned the chapter's shorter name: **Retries and Idempotency**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that retries and idempotency is necessary rather than decorative. Delete its new responsibility and use the earlier plan to retry the action whenever a response is missing. Immediately, the trouble appears immediately: the first payment succeeded and the retry charges the customer twice. Reintroduce the single job to give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect. Because the old plan to retry the action whenever a response is missing is the only displaced piece, the reader can locate exactly where retries and idempotency changes the outcome.

## Trying Again Without Doing It Twice

Both payment attempts carry order-417. The server records that key with the first charge; the retry retrieves the same receipt rather than creating another charge.

Retries and Idempotency earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

The name retries and idempotency is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

## Where retries and idempotency runs out

Not every external operation supports idempotency. Agents need reconciliation and human escalation when outcome is ambiguous.

The weakness is not an accidental footnote. Every operation in retries and idempotency serves the narrower purpose to give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take retries and idempotency to the workbench

Understanding retries and idempotency now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running retries and idempotency, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the retries and idempotency result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 063](../063-multi-agent-coordination/README.md)
