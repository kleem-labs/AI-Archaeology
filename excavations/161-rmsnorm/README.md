# Excavation 161 — RMSNorm — Do We Need to Subtract the Centre?

FlashAttention removes one systems bottleneck, making smaller repeated operations visible. Layer normalization calculates both a mean and a spread at every token and layer.

Perhaps we delete normalization because each individual operation appears cheap.

It survives until the measured run answers back. Deep residual streams drift in scale and training destabilizes; the repeated control was doing essential work.

Now the missing requirement is concrete. Keep rescaling invariance by dividing by root-mean-square magnitude, while testing whether explicit recentering is dispensable.

## Let one run decide

Vectors [3,4] and [30,40] become the same relative pattern after division by their RMS, although neither has its mean subtracted.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

Take the model feature pair [3,4]. Adding the raw values would let a negative feature cancel a positive one, so first turn their sizes into 9 and 16. Together they contribute 25; shared across two features that is 12.5 per feature. Its square root, about 3.54, returns to the features' ordinary units. Only now do we call this typical magnitude RMS(x) and the feature count d.

d is feature width; each x_i is one feature; RMS(x) is the vector's typical magnitude before a learned scale is applied.

### Why these operations are forced

[Squaring](../../MATHEMATICAL_MOVES.md#powers) keeps negative and positive feature magnitudes from cancelling. [Summation](../../MATHEMATICAL_MOVES.md#summation) gathers every feature's contribution, [division](../../MATHEMATICAL_MOVES.md#division) makes the magnitude per feature, and the [square root](../../MATHEMATICAL_MOVES.md#square-root) returns to the original scale. Omitting division would make wider vectors appear larger merely for having more coordinates.

Only now can we compress the procedure:

$$
\mathrm{RMS}(x)=\sqrt{\frac1d\sum_{i=1}^{d}x_i^2}
$$

## What this repair cannot do

RMSNorm does not guarantee that recentering is unimportant for every architecture or task.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Pre-Normalization — Protect the Residual Highway](../162-pre-normalization/README.md)
