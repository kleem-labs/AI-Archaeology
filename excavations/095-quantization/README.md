# Excavation 095 — Quantization

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Low-rank adaptation learns a small correction while preserving the base model. The unchanged base weights still consume memory and arithmetic every time the adapted model answers.

Nothing in the Road of Consequences yet bears today's mathematical name. There is only the expedition leader, the map of branching journeys, and one plausible action: round every weight aggressively without measuring effect.

At the edge of the map of branching journeys, the shortcut produces its consequence: small but important distinctions disappear and outputs degrade. That consequence, not a textbook, earns the next move.

*The expedition leader sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   round every weight aggressively… small but important distinctions…
            \        /
             \      /
              we need to map values to a limited…
```

The expedition leader covers the new mark and the old contradiction returns: small but important distinctions disappear and outputs degrade. The cover is lifted, restoring the ability to map values to a limited set of levels using calibrated scale and test sensitive layers, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason quantization exists.

What must change for quantization is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: we need to map values to a limited set of levels using calibrated scale and test sensitive layers. That threshold is where **Quantization** enters the story.

The marks on the map of branching journeys form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. quantization is not any single point. It is the path connecting them in the only order that makes the last point necessary.

<!-- memory-film-v1:start -->
> **Memory realm 9 of 18 — [Road of Consequences](../../MEMORY_PALACE.md#realm-9)**
>
> **The question carried into this chamber:** What fails if we round every weight aggressively without measuring effect?

## When the chamber changes

The Quantization room does not ask you to memorize its name. It asks you to watch one object change.

First hold the failed picture still: The prism follows the tempting path—round every weight aggressively without measuring effect. Then the evidence answers: small but important distinctions disappear and outputs degrade.

Now let the chamber move: The expedition leader changes one moving part. The prism can now map values to a limited set of levels using calibrated scale and test sensitive layers.

The object that should remain after the terminology disappears is **the quantization prism mounted on the map of branching journeys**.

> **Memory seal — Quantization**
>
> Quantization keeps the missing power: map values to a limited set of levels using calibrated scale and test sensitive layers.

Give the idea a bodily path: Touch the quantization prism in imagination: tap five fingertips in order—question, object, failure, transformation, seal—without saying the formal name.
<!-- memory-film-v1:end -->

## Understanding quantization

Weights from -1 to 1 become 256 integer levels; a stored integer plus scale approximately reconstructs each value.

## The calculation hidden inside quantization

The expedition leader carries the quantization scene to the map of branching journeys. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Suppose one learned weight is `0.73`, but the device can store only integer steps of size `0.10`. Dividing by the step size says the weight is 7.3 steps; rounding stores integer 7. During computation, multiplying 7 by `0.10` reconstructs `0.70`. The device has traded an error of `0.03` for cheaper storage and arithmetic. The scale decides which real differences survive.

Real weight w is divided by scale s to express it in integer-sized steps.
Rounding chooses the nearest allowed integer q.
Multiplying q by s reconstructs the approximate weight used in computation.
The scale is calibrated so important values fit the available integer range.

### Why the melody needs these exact notes

[Dividing by scale s](../../MATHEMATICAL_MOVES.md#division) expresses a real weight in units of one quantization step.
[Rounding](../../MATHEMATICAL_MOVES.md#rounding) chooses the nearest integer level because storage permits only discrete codes; this is the deliberate lossy step.
[Multiplying q by s](../../MATHEMATICAL_MOVES.md#multiplication) converts the stored step count back to the weight's approximate real scale. [The hat on w](../../MATHEMATICAL_MOVES.md#symbol-decorations) marks this reconstructed approximation; addition would shift levels rather than restore their unit size.

Before the line is compressed, notice its recurring motions: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; and **the lock and key**—one influence matters through another, and either missing factor can close the path. They are the handholds by which the reader can later climb back from notation to meaning.

The map of branching journeys already contains the complete quantization mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
q=\mathrm{round}(w/s)
$$

$$
\widehat w=sq
$$

## Where quantization runs out

Lower precision trades accuracy for efficiency and hardware support varies.

Here the new path ends honestly. Quantization can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the map of branching journeys

Rebuild the quantization scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 096](../096-distributed-training/README.md)
