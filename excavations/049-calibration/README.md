# Excavation 049 — Calibration — Does 80% Confidence Mean Eight Out of Ten?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Language models and useful answers

Grounding exposes unsupported claims, but the assistant also reports confidence. If “80% certain” is wrong half the time, users cannot use that number to decide when to trust or verify it.

The previous discovery reaches the Hall of Voices carrying one unfinished problem. Beside the listening table, the public archivist first tries to treat the largest softmax probability as honest confidence.

There is good reason to begin this way. If we treat the largest softmax probability as honest confidence, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability.

This failure cannot be repaired by performing the instruction to treat the largest softmax probability as honest confidence more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the listening table; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to group predictions with similar confidence and compare their average stated confidence with the fraction actually correct. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Calibration**. The name is simply a handle for the distinction already reconstructed.

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
