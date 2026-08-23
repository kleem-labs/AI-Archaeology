# Excavation 049 — Calibration — Does 80% Confidence Mean Eight Out of Ten?

<!-- book-prose-v2 -->

Grounding exposes unsupported claims, but the assistant also reports confidence. If “80% certain” is wrong half the time, users cannot use that number to decide when to trust or verify it.

For a moment, remain loyal to the simplest proposal: treat the largest softmax probability as honest confidence.

Its appeal is not ignorance but economy. Calibration should not be added until an observation exposes the exact thing the older procedure cannot preserve.

The world supplies the one comparison the shortcut hoped never to face: collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability.

Notice what the counterexample has accomplished for calibration. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: group predictions with similar confidence and compare their average stated confidence with the fraction actually correct.

Humanity eventually gathered this problem and its repairs under the name **Calibration**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace calibration with the old instruction to treat the largest softmax probability as honest confidence. The result is again that collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability. Put back only the requirement to group predictions with similar confidence and compare their average stated confidence with the fraction actually correct. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when calibration is introduced. The same evidence that defeated the attempt to treat the largest softmax probability as honest confidence is presented again. Only the ability to group predictions with similar confidence and compare their average stated confidence with the fraction actually correct changes, so the repaired conclusion cannot be credited to a conveniently different example.

## The calculation hidden inside calibration

Before Calibration receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Five predictions report 0.8 confidence. Exactly four are correct. Accuracy is 4/5=0.8, so this group is calibrated. If only two are correct, accuracy is 0.4 and the confidence gap is 0.4.

### Names for pieces we have already used

Each group contains predictions with similar confidence. Accuracy counts how many were correct. The absolute difference measures the reliability gap; weighting by group size prevents tiny groups dominating.

### Why no cheaper operation does the same job

[Confidence minus accuracy](../../MATHEMATICAL_MOVES.md#subtraction) finds each bin's reliability gap; adding them would measure overall level rather than disagreement.
[Absolute value](../../MATHEMATICAL_MOVES.md#absolute-value) makes overconfidence and underconfidence both count as error when this metric asks for magnitude rather than direction.
[Multiplying by |Bᵦ|/n](../../MATHEMATICAL_MOVES.md#multiplication) gives a large bin proportionally more influence, and [the sum](../../MATHEMATICAL_MOVES.md#summation) combines all bin contributions. An unweighted mean would let a tiny bin count as much as a common one.

Every symbol in Calibration can now be read back into an action already performed. The whole procedure fits in one line:

$$
\mathrm{ECE}=\sum_b\frac{|B_b|}{n}\left|\mathrm{accuracy}(B_b)-\mathrm{confidence}(B_b)\right|
$$

## Where calibration runs out

Calibration depends on task and population. A model calibrated overall can be unreliable for an important subgroup.

Why does that boundary remain? Calibration was built for one responsibility: group predictions with similar confidence and compare their average stated confidence with the fraction actually correct. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take calibration to the workbench

The argument for calibration is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running calibration, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the calibration result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 050](../050-data-quality/README.md)
