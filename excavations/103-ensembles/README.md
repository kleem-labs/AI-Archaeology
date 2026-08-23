# Excavation 103 — Ensembles

<!-- book-prose-v2 -->

Bayesian updating combines prior plausibility with the likelihood of new evidence. One trained model can still be confidently wrong about its own uncertainty, so we ask whether independently trained models agree.

Before naming anything new, try to trust one training run as the unique learned truth.

Its appeal is not ignorance but economy. Ensembles should not be added until an observation exposes the exact thing the older procedure cannot preserve.

One counterexample is enough to expose the missing job: different initialization and data order produce different boundaries.

Notice what the counterexample has accomplished for ensembles. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: we need to train several diverse models and combine predictions while inspecting disagreement.

Humanity eventually gathered this problem and its repairs under the name **Ensembles**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace ensembles with the old instruction to trust one training run as the unique learned truth. The result is again that different initialization and data order produce different boundaries. Put back only the requirement to we need to train several diverse models and combine predictions while inspecting disagreement. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when ensembles is introduced. The same evidence that defeated the attempt to trust one training run as the unique learned truth is presented again. Only the ability to we need to train several diverse models and combine predictions while inspecting disagreement changes, so the repaired conclusion cannot be credited to a conveniently different example.

## Understanding ensembles

Five models vote tiger probabilities .9,.85,.88,.3,.25; the average is moderate and disagreement warns of model uncertainty.

Run the ensembles scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

## Where ensembles runs out

Ensembles cost more and shared data can produce shared mistakes.

Why does that boundary remain? Ensembles was built for one responsibility: we need to train several diverse models and combine predictions while inspecting disagreement. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take ensembles to the workbench

The argument for ensembles is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running ensembles, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the ensembles result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 104](../104-active-learning/README.md)
