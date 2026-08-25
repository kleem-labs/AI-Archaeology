# Excavation 200 — A Tiny Pretraining Factory — Close the Accountable Training Loop

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Data and pretraining operations

The training report can explain one finished run. We have now earned all the mechanisms needed to make the next run reconstructable from source documents to final artifact rather than relying on memory and scattered scripts.

At the Archive Foundry, the archivist-engineer meets the next case beside the chain-of-custody ledger. The nearest idea is also the most reasonable one: connect every tool into one automatic pipeline and trust any run that reaches the final stage.

The attraction of this attempt is easy to see. To connect every tool into one automatic pipeline and trust any run that reaches the final stage reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: automation can faithfully repeat a wrong manifest, destructive filter, contaminated validation set, incomplete checkpoint, or unauthorized release. Completion is not evidence of correctness.

The contradiction matters because it identifies a structural loss in the instruction to connect every tool into one automatic pipeline and trust any run that reaches the final stage, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The chain-of-custody ledger will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must assemble signed stage manifests, boundary-aware curation, audited mixtures, fixed budgets, measured schedules, distributed equivalence tests, atomic checkpoints, live validation, memorization probes, and human release gates into one reversible factory. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **A Tiny Pretraining Factory**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## Close the Accountable Training Loop

A tiny run begins from ten named documents, records every acceptance and removal, trains a reproducible model, survives an intentional interruption, reproduces its next updates, generates its report, and refuses release when the memorization gate fails.

## Where a tiny pretraining factory runs out

The factory is accountable, not omniscient. New sources, laws, hardware, attacks, and uses create new failures that must return to observation and the bounded research loop.

A final test reaches beyond the new instrument. It does not refute Tiny Pretraining Factory; it reveals the edge of what was constructed. The archivist-engineer carries that edge into the following room.

## The mandala returns to observation

The final artifact carries its documents, transformations, budgets, checkpoints, validation, audits, and release decision as evidence. The circle does not close by declaring perfection. It closes by returning every future change to the first law: observe what happened, let failure speak, and invent only what the world makes necessary.

```text
observation → need → mathematics → machine → consequence → observation
```

The trail called *the mandala returns to observation* is what remains when one necessity becomes another.

## Return to the chain-of-custody ledger

Rebuild the tiny pretraining factory scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
