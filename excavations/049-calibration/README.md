# Excavation 049 — Calibration — Does 80% Confidence Mean Eight Out of Ten?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Language models and useful answers

Grounding exposes unsupported claims, but the assistant also reports confidence. If “80% certain” is wrong half the time, users cannot use that number to decide when to trust or verify it.

Morning reaches the Hall of Voices before anyone has a name for today's difficulty. Beside the listening table, the public archivist tries the smallest continuation of what already works: treat the largest softmax probability as honest confidence.

The rule survives the easy cases. The next case leaves a crack through the middle of it: collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability. More confidence cannot repair information that never entered the rule.

*The public archivist sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: treat the largest softmax probability…
                         │
                         └── mismatch: collect ten answers each reported…

reference evidence ──▶ measured repair: group predictions with similar…
```

Two trails now cross the listening table. The pale trail bears the instruction “treat the largest softmax probability as honest confidence.” It disappears into the observed failure: collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability. The darker trail carries one additional capacity—to group predictions with similar confidence and compare their average stated confidence with the fraction actually correct. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed calibration mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the listening table is altered in exactly one way: group predictions with similar confidence and compare their average stated confidence with the fraction actually correct. Much later, people will call this territory **Calibration**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the listening table. The failed path remains visible beneath the repair, because calibration is easier to remember when its scar remains attached to it. The scar reads, ‘collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability’; the new line exists only to keep that loss from happening again.

<!-- memory-film-v1:start -->
> **Memory realm 5 of 18 — [Hall of Voices](../../MEMORY_PALACE.md#realm-5)**
>
> **The question carried into this chamber:** What fails if we treat the largest softmax probability as honest confidence?

## When the chamber changes

The mathematical name Calibration can now rest. What matters is whether its transformation remains visible.

First hold the failed picture still: The lens follows the tempting path—treat the largest softmax probability as honest confidence. Then the evidence answers: collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability.

Now let the chamber move: The public archivist changes one moving part. The lens can now group predictions with similar confidence and compare their average stated confidence with the fraction actually correct.

The object that should remain after the terminology disappears is **the calibration lens mounted on the listening table**.

> **Memory seal — Calibration**
>
> Calibration keeps the missing power: group predictions with similar confidence and compare their average stated confidence with the fraction actually correct.

Give the idea a bodily path: Touch the calibration lens in imagination: hold both hands as the two failed alternatives, then move one hand through the repaired route.
<!-- memory-film-v1:end -->

## The calculation hidden inside calibration

The public archivist carries the calibration scene to the listening table. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Five predictions report 0.8 confidence. Exactly four are correct. Accuracy is 4/5=0.8, so this group is calibrated. If only two are correct, accuracy is 0.4 and the confidence gap is 0.4.

### Naming what is already on the table

Each group contains predictions with similar confidence. Accuracy counts how many were correct. The absolute difference measures the reliability gap; weighting by group size prevents tiny groups dominating.

### Why the melody needs these exact notes

[Confidence minus accuracy](../../MATHEMATICAL_MOVES.md#subtraction) finds each bin's reliability gap; adding them would measure overall level rather than disagreement.
[Absolute value](../../MATHEMATICAL_MOVES.md#absolute-value) makes overconfidence and underconfidence both count as error when this metric asks for magnitude rather than direction.
[Multiplying by |Bᵦ|/n](../../MATHEMATICAL_MOVES.md#multiplication) gives a large bin proportionally more influence, and [the sum](../../MATHEMATICAL_MOVES.md#summation) combines all bin contributions. An unweighted mean would let a tiny bin count as much as a common one.

The calculation borrows several gestures already encountered elsewhere: **the chisel**—what is shared is removed so the remaining change can be seen; **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. calibration feels new because the objects are new; the gestures remain recognizably human.

The public archivist reads the journey of calibration once more across the listening table, then lets the words contract without losing their order:

$$
\mathrm{ECE}=\sum_b\frac{|B_b|}{n}\left|\mathrm{accuracy}(B_b)-\mathrm{confidence}(B_b)\right|
$$

## Where calibration runs out

Calibration depends on task and population. A model calibrated overall can be unreliable for an important subgroup.

The listening table answers today's question and falls silent at the next. That silence is precise: Calibration was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the listening table

Rebuild the calibration scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 050](../050-data-quality/README.md)
