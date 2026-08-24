# Excavation 103 — Ensembles

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Continual learning, reasoning, and research

Bayesian updating combines prior plausibility with the likelihood of new evidence. One trained model can still be confidently wrong about its own uncertainty, so we ask whether independently trained models agree.

Nothing in the Hall of Possible Worlds yet bears today's mathematical name. There is only the keeper of unfinished questions, the table of mirrored maps, and one plausible action: trust one training run as the unique learned truth.

The rule survives the easy cases. The next case leaves a crack through the middle of it: different initialization and data order produce different boundaries. More confidence cannot repair information that never entered the rule.

*The keeper of unfinished questions sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: trust one training run as the unique…
possible road B ─┘              └── loses: different initialization and data…

same roads ──▶ repaired map ──▶ we need to train several diverse…
```

Two trails now cross the table of mirrored maps. The pale trail bears the instruction “trust one training run as the unique learned truth.” It disappears into the observed failure: different initialization and data order produce different boundaries. The darker trail carries one additional capacity—to train several diverse models and combine predictions while inspecting disagreement. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed ensembles mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the table of mirrored maps is altered in exactly one way: we need to train several diverse models and combine predictions while inspecting disagreement. Much later, people will call this territory **Ensembles**. Here the name is only a memory of the failure it can survive.

The table of mirrored maps has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and ensembles looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

## Understanding ensembles

Five models vote tiger probabilities .9,.85,.88,.3,.25; the average is moderate and disagreement warns of model uncertainty.

## Where ensembles runs out

Ensembles cost more and shared data can produce shared mistakes.

The table of mirrored maps answers today's question and falls silent at the next. That silence is precise: Ensembles was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the table of mirrored maps

Rebuild the ensembles scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 104](../104-active-learning/README.md)
