# Excavation 161 — RMSNorm — Do We Need to Subtract the Centre?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

FlashAttention removes one systems bottleneck, making smaller repeated operations visible. Layer normalization calculates both a mean and a spread at every token and layer.

Morning reaches the Engine Cavern before anyone has a name for today's difficulty. Beside the brass reference machine, the enginewright tries the smallest continuation of what already works: delete normalization because each individual operation appears cheap.

At the edge of the brass reference machine, the shortcut produces its consequence: deep residual streams drift in scale and training destabilizes; the repeated control was doing essential work. That consequence, not a textbook, earns the next move.

*The enginewright sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: delete normalization because each…
possible road B ─┘              └── loses: deep residual streams drift in scale…

same roads ──▶ repaired map ──▶ keep rescaling invariance by dividing…
```

The enginewright covers the new mark and the old contradiction returns: deep residual streams drift in scale and training destabilizes; the repeated control was doing essential work. The cover is lifted, restoring the ability to keep rescaling invariance by dividing by root-mean-square magnitude, while testing whether explicit recentering is dispensable, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason rmsnorm exists.

What must change for rmsnorm is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: keep rescaling invariance by dividing by root-mean-square magnitude, while testing whether explicit recentering is dispensable. That threshold is where **RMSNorm** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In rmsnorm, that memory takes a precise form: whenever deep residual streams drift in scale and training destabilizes; the repeated control was doing essential work, preserve enough structure to keep rescaling invariance by dividing by root-mean-square magnitude, while testing whether explicit recentering is dispensable.

## Do We Need to Subtract the Centre

Vectors [3,4] and [30,40] become the same relative pattern after division by their RMS, although neither has its mean subtracted.

## The calculation hidden inside rmsnorm

The enginewright carries the rmsnorm scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Take the model feature pair [3,4]. Adding the raw values would let a negative feature cancel a positive one, so first turn their sizes into 9 and 16. Together they contribute 25; shared across two features that is 12.5 per feature. Its square root, about 3.54, returns to the features' ordinary units. Only now do we call this typical magnitude RMS(x) and the feature count d.

d is feature width; each x_i is one feature; RMS(x) is the vector's typical magnitude before a learned scale is applied.

### Why the melody needs these exact notes

[Squaring](../../MATHEMATICAL_MOVES.md#powers) keeps negative and positive feature magnitudes from cancelling. [Summation](../../MATHEMATICAL_MOVES.md#summation) gathers every feature's contribution, [division](../../MATHEMATICAL_MOVES.md#division) makes the magnitude per feature, and the [square root](../../MATHEMATICAL_MOVES.md#square-root) returns to the original scale. Omitting division would make wider vectors appear larger merely for having more coordinates.

The calculation borrows several gestures already encountered elsewhere: **the echoing chamber**—large departures return with greater force while opposite signs stop cancelling; **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. rmsnorm feels new because the objects are new; the gestures remain recognizably human.

The brass reference machine already contains the complete rmsnorm mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
\mathrm{RMS}(x)=\sqrt{\frac1d\sum_{i=1}^{d}x_i^2}
$$

## Where rmsnorm runs out

RMSNorm does not guarantee that recentering is unimportant for every architecture or task.

Here the new path ends honestly. RMSNorm can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the brass reference machine

Rebuild the rmsnorm scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Pre-Normalization — Protect the Residual Highway](../162-pre-normalization/README.md)
