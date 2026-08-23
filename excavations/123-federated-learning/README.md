# Excavation 123 — Federated Learning

<!-- book-prose-v2 -->

Differential privacy limits the observable influence of one record. Hospitals and devices may be unwilling or legally unable to centralize their raw data even when collective learning would help everyone.

The machinery already in our hands suggests that we upload every user record to one server.

This is how federated learning ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Then a case arrives in which convenience and truth separate: central collection increases privacy and governance risk.

The wrong answer makes the need for federated learning inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: we need to send model updates to devices, train locally, aggregate protected updates, and return a shared model.

The usual name, **Federated Learning**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to upload every user record to one server produces the observed failure: central collection increases privacy and governance risk. Starting with the repaired demand to we need to send model updates to devices, train locally, aggregate protected updates, and return a shared model preserves the information the shortcut lost. The subject of federated learning lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to we need to send model updates to devices, train locally, aggregate protected updates, and return a shared model instead of merely trying to upload every user record to one server. That controlled contrast is what turns a plausible explanation of federated learning into an understandable derivation.

## Understanding federated learning

Phones compute keyboard gradients locally; the server receives an aggregate, not typed messages.

There are now two histories of this federated learning case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

## Where federated learning runs out

Updates can still leak information and devices are unreliable or biased.

Look back at what federated learning actually preserves: it can we need to send model updates to devices, train locally, aggregate protected updates, and return a shared model. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

## Take federated learning to the workbench

The reader has reconstructed federated learning in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running federated learning, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the federated learning result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 124](../124-adversarial-robustness/README.md)
