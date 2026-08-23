# Excavation 106 — Catastrophic Forgetting

<!-- book-prose-v2 -->

Selective prediction gives the system permission to abstain. When an approved new task finally supplies more training data, learning it can overwrite skills that were reliable yesterday.

We can postpone invention if we simply fine-tune only on the newest data.

If the proposal works on every relevant case, catastrophic forgetting is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

Its hidden assumption becomes visible as soon as we observe that updates useful for B overwrite weights carrying A.

Nothing magical creates catastrophic forgetting. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: rehearse old evidence, protect important parameters, or allocate new capacity.

This boundary between the failed rule and its repair is the subject later work calls **Catastrophic Forgetting**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize catastrophic forgetting; try to break it by subtraction. Remove the part that knows how to rehearse old evidence, protect important parameters, or allocate new capacity, leaving only the attempt to fine-tune only on the newest data. What returns is not a vague weakness but the original contradiction: updates useful for B overwrite weights carrying A. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to fine-tune only on the newest data receives the same test as the rule to rehearse old evidence, protect important parameters, or allocate new capacity. Their different outcomes reveal what catastrophic forgetting contributes without asking the reader to trust historical convention.

## Understanding catastrophic forgetting

Learning birds after mammals drops mammal accuracy; mixing a small mammal replay set preserves both.

Hold the setting, evidence, and desired outcome fixed while testing catastrophic forgetting. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

## Where catastrophic forgetting runs out

Memory, privacy, and capacity limit rehearsal.

This is where catastrophic forgetting runs out for a causal reason. We gave it enough structure to rehearse old evidence, protect important parameters, or allocate new capacity, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

## Take catastrophic forgetting to the workbench

A mathematical story about catastrophic forgetting earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running catastrophic forgetting, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the catastrophic forgetting result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 107](../107-continual-learning/README.md)
