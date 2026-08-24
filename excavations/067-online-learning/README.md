# Excavation 067 — Online Learning

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

A feedback loop reveals that deployment is part of the data-generating process. When the world changes for legitimate reasons, a frozen model grows stale and needs a controlled way to learn online.

Night gathers around the Living Watchgarden. Under the light of the weathered observation slate, the field naturalist refuses to invent prematurely and begins with the plain rule: retrain immediately on every new labeled event.

The rule survives the easy cases. The next case leaves a crack through the middle of it: the trouble appears immediately: one mislabeled transaction can move the model before anyone notices. More confidence cannot repair information that never entered the rule.

*The field naturalist sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   retrain immediately on every new… the trouble appears immediately: one…
            \        /
             \      /
              we need to update from controlled…
```

Two trails now cross the weathered observation slate. The pale trail bears the instruction “retrain immediately on every new labeled event.” It disappears into the observed failure: the trouble appears immediately: one mislabeled transaction can move the model before anyone notices. The darker trail carries one additional capacity—to update from controlled batches with validation, rollback, and limits on how quickly behavior may change. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed online learning mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the weathered observation slate is altered in exactly one way: we need to update from controlled batches with validation, rollback, and limits on how quickly behavior may change. Much later, people will call this territory **Online Learning**. Here the name is only a memory of the failure it can survive.

The weathered observation slate has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and online learning looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

## Understanding online learning

A new batch reduces recent fraud loss but doubles errors on the stable validation set; the update is rejected.

## Where online learning runs out

Fast adaptation also creates fast corruption.

The weathered observation slate answers today's question and falls silent at the next. That silence is precise: Online Learning was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the weathered observation slate

Rebuild the online learning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 068](../068-distribution-drift/README.md)
