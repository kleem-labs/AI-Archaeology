# Excavation 107 — Continual Learning

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Continual learning, reasoning, and research

Catastrophic forgetting exposes competition inside shared parameters. Continual learning must absorb a stream of new tasks while preserving the old behavior that remains valid.

Night gathers around the Hall of Possible Worlds. Under the light of the table of mirrored maps, the keeper of unfinished questions refuses to invent prematurely and begins with the plain rule: periodically retrain from scratch on everything.

At the edge of the table of mirrored maps, the shortcut produces its consequence: the trouble appears immediately: storage and compute grow forever, and old raw data may be unavailable. That consequence, not a textbook, earns the next move.

*The keeper of unfinished questions sketches the break before changing it:*

```text
OLD PATH:  request ──▶ periodically retrain from scratch on… ──▶ the trouble appears immediately:…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ we need to detect change, consolidate… ──▶ accountable result
```

The keeper of unfinished questions covers the new mark and the old contradiction returns: the trouble appears immediately: storage and compute grow forever, and old raw data may be unavailable. The cover is lifted, restoring the ability to detect change, consolidate stable knowledge, adapt limited components, and evaluate past and present tasks together, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason continual learning exists.

What must change for continual learning is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: we need to detect change, consolidate stable knowledge, adapt limited components, and evaluate past and present tasks together. That threshold is where **Continual Learning** enters the story.

The marks on the table of mirrored maps form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. continual learning is not any single point. It is the path connecting them in the only order that makes the last point necessary.


Before leaving the table of mirrored maps, the keeper of unfinished questions tests the new idea backward. Remove the ability to detect change, consolidate stable knowledge, adapt limited components, and evaluate past and present tasks together, and the method falls back to this tempting instruction: periodically retrain from scratch on everything. The old consequence returns—the trouble appears immediately: storage and compute grow forever, and old raw data may be unavailable. Restore the missing ability and that particular contradiction disappears. This reversible test is why continual learning belongs to the growing structure rather than to a list of facts to memorize.

## Understanding continual learning

A seasonal model adapts its demand head while preserving reusable product representations.

## Where continual learning runs out

Stability and adaptability remain in tension.

Here the new path ends honestly. Continual Learning can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the table of mirrored maps

Rebuild the continual learning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 108](../108-meta-learning/README.md)
