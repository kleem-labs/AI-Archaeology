# Excavation 023 — The Chain Rule — Following One Change Through Many Machines

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Calculus & Differential Change](../../MATHEMATICS_ATLAS.md#calculus) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Learning from uncertainty and error

A derivative can question one weight when its effect on loss is direct. Inside the network, that weight first changes a hidden signal, then a score, then a probability, and only then the loss.

Nothing in the Lantern Observatory yet bears today's mathematical name. There is only the keeper of uncertain stories, the ring of glass lanterns, and one plausible action: measure only the first effect or only the final effect.

At the edge of the ring of glass lanterns, the shortcut produces its consequence: either breaks the causal path. Recompute the whole network separately for every weight; that repeats enormous amounts of work. That consequence, not a textbook, earns the next move.

*The keeper of uncertain stories sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   measure only the first effect or only… either breaks the causal path.…
            \        /
             \      /
              we need to multiply local…
```

The keeper of uncertain stories covers the new mark and the old contradiction returns: either breaks the causal path. Recompute the whole network separately for every weight; that repeats enormous amounts of work. The cover is lifted, restoring the ability to multiply local sensitivities along the causal path. Each stage tells how strongly it passes a small change onward, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason chain rule exists.

What must change for chain rule is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: we need to multiply local sensitivities along the causal path. Each stage tells how strongly it passes a small change onward. That threshold is where **The Chain Rule** enters the story.

The marks on the ring of glass lanterns form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. chain rule is not any single point. It is the path connecting them in the only order that makes the last point necessary.

<!-- memory-film-v1:start -->
> **Memory realm 3 of 18 — [Lantern Observatory](../../MEMORY_PALACE.md#realm-3)**
>
> **The question carried into this chamber:** What fails if we measure only the first effect or only the final effect?

## When the chamber changes

Before leaving The Chain Rule, replay the discovery as motion rather than as a definition.

First hold the failed picture still: The mirror follows the tempting path—measure only the first effect or only the final effect. Then the evidence answers: either breaks the causal path. Recompute the whole network separately for every weight; that repeats enormous amounts of work.

Now let the chamber move: The keeper of uncertain stories changes one moving part. The mirror can now multiply local sensitivities along the causal path. Each stage tells how strongly it passes a small change onward.

The object that should remain after the terminology disappears is **the chain rule mirror mounted on the ring of glass lanterns**.

> **Memory seal — The Chain Rule**
>
> The Chain Rule keeps the missing power: multiply local sensitivities along the causal path. Each stage tells how strongly it passes a small change onward.

Give the idea a bodily path: Touch the chain rule mirror in imagination: tap five fingertips in order—question, object, failure, transformation, seal—without saying the formal name.
<!-- memory-film-v1:end -->

## The calculation hidden inside the chain rule

The keeper of uncertain stories carries the chain rule scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Turn an oven knob slightly. The first mechanism doubles that movement into a fuel change; the next triples the fuel change into temperature; the bread-loss rule magnifies the temperature error fourfold. A one-unit knob change therefore becomes 2, then 6, then 24 units of final sensitivity. Each machine contributes one local multiplier, and the whole causal path requires all of them.

### Naming what is already on the table

**w→x→y→L** is the causal path through successive machines.
Each fraction is one local sensitivity: how its output changes when its input changes.
Multiplication is forced because a change is scaled at every link it traverses.
The product gives the effect of w on L without pretending they touch directly.

### Why the melody needs these exact notes

Each [derivative](../../MATHEMATICAL_MOVES.md#derivative) is a local conversion rate: loss per y, y per x, and x per weight.
[Multiplying the rates](../../MATHEMATICAL_MOVES.md#multiplication) is forced because one unit of weight change produces dx/dw units of x, each produces dy/dx units of y, and each of those produces dL/dy loss. Adding would mix rates with incompatible units.

Before the line is compressed, notice its recurring motions: **the whispered question**—the present slope answers how a tiny movement would alter the outcome; and **the lock and key**—one influence matters through another, and either missing factor can close the path. They are the handholds by which the reader can later climb back from notation to meaning.

The ring of glass lanterns already contains the complete chain rule mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
\frac{dL}{dw}=\frac{dL}{dy}\frac{dy}{dx}\frac{dx}{dw}
$$

## The Chain Rule beyond this one case

A line of gears passes motion onward. To know the final turn from the first gear, combine the ratio contributed by every contact.

## Where the chain rule runs out

Branches require sensitivities from every downstream path to be added, not merely one chain followed.

Here the new path ends honestly. Chain Rule can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the ring of glass lanterns

Rebuild the chain rule scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
