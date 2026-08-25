# Excavation 103 — Ensembles

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Continual learning, reasoning, and research

Bayesian updating combines prior plausibility with the likelihood of new evidence. One trained model can still be confidently wrong about its own uncertainty, so we ask whether independently trained models agree.

Inside the Hall of Possible Worlds, the old method is given an honest chance. The keeper of unfinished questions places the evidence on the table of mirrored maps and tries to trust one training run as the unique learned truth.

Nothing about this first move is careless. To trust one training run as the unique learned truth is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: different initialization and data order produce different boundaries.

The important discovery is not merely that trying to trust one training run as the unique learned truth failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the table of mirrored maps, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to train several diverse models and combine predictions while inspecting disagreement. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Ensembles**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## Understanding ensembles

Five models vote tiger probabilities .9,.85,.88,.3,.25; the average is moderate and disagreement warns of model uncertainty.

## Where ensembles runs out

Ensembles cost more and shared data can produce shared mistakes.

The table of mirrored maps answers today's question and falls silent at the next. That silence is precise: Ensembles was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the table of mirrored maps

Rebuild the ensembles scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 104](../104-active-learning/README.md)
