# Excavation 067 — Online Learning

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality)
>
> **Applied territory:** Learning in the world and interpretability

A feedback loop reveals that deployment is part of the data-generating process. When the world changes for legitimate reasons, a frozen model grows stale and needs a controlled way to learn online.

Inside the Living Watchgarden, the old method is given an honest chance. The field naturalist places the evidence on the weathered observation slate and tries to retrain immediately on every new labeled event.

Nothing about this first move is careless. To retrain immediately on every new labeled event is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: the trouble appears immediately: one mislabeled transaction can move the model before anyone notices.

The important discovery is not merely that trying to retrain immediately on every new labeled event failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the weathered observation slate, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to update from controlled batches with validation, rollback, and limits on how quickly behavior may change. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Online Learning**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## Understanding online learning

A new batch reduces recent fraud loss but doubles errors on the stable validation set; the update is rejected.

## Where online learning runs out

Fast adaptation also creates fast corruption.

The weathered observation slate answers today's question and falls silent at the next. That silence is precise: Online Learning was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the weathered observation slate

Rebuild the online learning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 068](../068-distribution-drift/README.md)
