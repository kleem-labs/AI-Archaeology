# Excavation 067 — Online Learning

<!-- book-prose-v2 -->

A feedback loop reveals that deployment is part of the data-generating process. When the world changes for legitimate reasons, a frozen model grows stale and needs a controlled way to learn online.

Before naming anything new, try to retrain immediately on every new labeled event.

Its appeal is not ignorance but economy. Online Learning should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Then a case arrives in which convenience and truth separate: the trouble appears immediately: one mislabeled transaction can move the model before anyone notices.

Notice what the counterexample has accomplished for online learning. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: we need to update from controlled batches with validation, rollback, and limits on how quickly behavior may change.

Humanity eventually gathered this problem and its repairs under the name **Online Learning**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace online learning with the old instruction to retrain immediately on every new labeled event. The result is again that the trouble appears immediately: one mislabeled transaction can move the model before anyone notices. Put back only the requirement to we need to update from controlled batches with validation, rollback, and limits on how quickly behavior may change. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when online learning is introduced. The same evidence that defeated the attempt to retrain immediately on every new labeled event is presented again. Only the ability to we need to update from controlled batches with validation, rollback, and limits on how quickly behavior may change changes, so the repaired conclusion cannot be credited to a conveniently different example.

## Understanding online learning

A new batch reduces recent fraud loss but doubles errors on the stable validation set; the update is rejected.

Run the online learning scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

## Where online learning runs out

Fast adaptation also creates fast corruption.

Why does that boundary remain? Online Learning was built for one responsibility: we need to update from controlled batches with validation, rollback, and limits on how quickly behavior may change. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take online learning to the workbench

The argument for online learning is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running online learning, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the online learning result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 068](../068-distribution-drift/README.md)
