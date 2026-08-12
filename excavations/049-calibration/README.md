# Excavation 049 — Calibration — Does 80% Confidence Mean Eight Out of Ten?

Grounding exposes unsupported claims, but the assistant also reports confidence. If “80% certain” is wrong half the time, users cannot use that number to decide when to trust or verify it.

We first try to treat the largest softmax probability as honest confidence.

The world refuses to cooperate: collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability.

That failure tells us to group predictions with similar confidence and compare their average stated confidence with the fraction actually correct.

## The arithmetic we have earned

Five predictions report 0.8 confidence. Exactly four are correct. Accuracy is 4/5=0.8, so this group is calibrated. If only two are correct, accuracy is 0.4 and the confidence gap is 0.4.

### Only now do the symbols earn names

Each group contains predictions with similar confidence. Accuracy counts how many were correct. The absolute difference measures the reliability gap; weighting by group size prevents tiny groups dominating.

### Why these operations are forced

- [Confidence minus accuracy](../../MATHEMATICAL_MOVES.md#subtraction) finds each bin's reliability gap; adding them would measure overall level rather than disagreement.
- [Absolute value](../../MATHEMATICAL_MOVES.md#absolute-value) makes overconfidence and underconfidence both count as error when this metric asks for magnitude rather than direction.
- [Multiplying by |Bᵦ|/n](../../MATHEMATICAL_MOVES.md#multiplication) gives a large bin proportionally more influence, and [the sum](../../MATHEMATICAL_MOVES.md#summation) combines all bin contributions. An unweighted mean would let a tiny bin count as much as a common one.

Only now can we compress the exact procedure:

$$
\mathrm{ECE}=\sum_b\frac{|B_b|}{n}\left|\mathrm{accuracy}(B_b)-\mathrm{confidence}(B_b)\right|
$$

## The boundary of the discovery

Calibration depends on task and population. A model calibrated overall can be unreliable for an important subgroup.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 050](../050-data-quality/README.md)
