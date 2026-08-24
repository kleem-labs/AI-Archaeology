# Excavation 104 — Active Learning

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Continual learning, reasoning, and research

An ensemble turns disagreement into evidence about model uncertainty. When labels are expensive, that disagreement can guide which unlabeled case deserves a human answer next.

At the Hall of Possible Worlds, the keeper of unfinished questions returns to the table of mirrored maps. Yesterday's instrument still lies open, so the first move asks for no new magic: label random examples forever.

Reality answers without terminology: thousands of easy repeated cases consume effort while the decision boundary remains unclear. The table of mirrored maps now holds two situations the old rule cannot keep apart.

*The keeper of unfinished questions sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: label random examples forever
                         │
                         └── mismatch: thousands of easy repeated cases…

reference evidence ──▶ measured repair: ask for labels where the model is…
```

The table of mirrored maps is divided down the middle. Left side: “label random examples forever.” Its final mark records thousands of easy repeated cases consume effort while the decision boundary remains unclear. Right side: the same starting evidence, now allowed to ask for labels where the model is uncertain or where examples add new coverage. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given active learning a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: ask for labels where the model is uncertain or where examples add new coverage. The name **Active Learning** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to label random examples forever; on the other lies the observed fact that thousands of easy repeated cases consume effort while the decision boundary remains unclear. The bridge called active learning has exactly the planks needed to ask for labels where the model is uncertain or where examples add new coverage.

<!-- memory-film-v1:start -->
> **Memory realm 10 of 18 — [Hall of Possible Worlds](../../MEMORY_PALACE.md#realm-10)**
>
> **The question carried into this chamber:** What fails if we label random examples forever?

## When the chamber changes

The mathematical name Active Learning can now rest. What matters is whether its transformation remains visible.

First hold the failed picture still: The bell follows the tempting path—label random examples forever. Then the evidence answers: thousands of easy repeated cases consume effort while the decision boundary remains unclear.

Now let the chamber move: The keeper of unfinished questions changes one moving part. The bell can now ask for labels where the model is uncertain or where examples add new coverage.

The object that should remain after the terminology disappears is **the active learning bell mounted on the table of mirrored maps**.

> **Memory seal — Active Learning**
>
> Active Learning keeps the missing power: ask for labels where the model is uncertain or where examples add new coverage.

Give the idea a bodily path: Touch the active learning bell in imagination: trace its outline with one finger, cover it with your palm, then uncover only the repaired path.
<!-- memory-film-v1:end -->

## Understanding active learning

The model knows obvious cats and dogs but splits 50–50 on one fox-like animal; labeling it teaches more than another obvious cat.

## Where active learning runs out

Uncertainty sampling can chase noise or outliers.

A final test reaches beyond the new instrument. It does not refute Active Learning; it reveals the edge of what was constructed. The keeper of unfinished questions carries that edge into the following room.

## Return to the table of mirrored maps

Rebuild the active learning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 105](../105-selective-prediction/README.md)
