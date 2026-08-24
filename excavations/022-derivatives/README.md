# Excavation 022 — Derivatives — Asking One Weight What It Changed

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Calculus & Differential Change](../../MATHEMATICS_ATLAS.md#calculus) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Learning from uncertainty and error

Cross-entropy turns the model's misplaced confidence into one loss. One number can announce that the whole machine is wrong, but it cannot yet tell any particular weight whether moving up or down would help.

The doors of the Lantern Observatory close against the wind. On the ring of glass lanterns, the keeper of uncertain stories writes the cheapest rule that might still be true: try a large jump and keep it if loss falls.

The keeper of uncertain stories repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: large jumps can leap over improvements. Try every possible value; there are infinitely many. The failure is stable enough to become evidence.

*The keeper of uncertain stories sketches the break before changing it:*

```text
observation
    │
    ▼
[try a large jump and keep it if loss…]
    │
    ╳  large jumps can leap over…
    │
    ▼
[nudge the weight by a tiny amount,…]
```

Across the ring of glass lanterns, the old path and the repaired path run side by side. One carries “try a large jump and keep it if loss falls”; the other knows how to nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero. When the failure—large jumps can leap over improvements. Try every possible value; there are infinitely many—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to derivatives. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero. This problem and its repair will travel under the name **Derivatives**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—try a large jump and keep it if loss falls? The answer remains large jumps can leap over improvements. Try every possible value; there are infinitely many. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

<!-- memory-film-v1:start -->
> **Memory realm 3 of 18 — [Lantern Observatory](../../MEMORY_PALACE.md#realm-3)**
>
> **The question carried into this chamber:** What fails if we try a large jump and keep it if loss falls?

## When the chamber changes

The Derivatives chamber leaves one scene behind so the idea can be recovered after its symbols fade.

First hold the failed picture still: The thread follows the tempting path—try a large jump and keep it if loss falls. Then the evidence answers: large jumps can leap over improvements. Try every possible value; there are infinitely many.

Now let the chamber move: The keeper of uncertain stories changes one moving part. The thread can now nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero.

The object that should remain after the terminology disappears is **the derivatives thread mounted on the ring of glass lanterns**.

> **Memory seal — Derivatives**
>
> Derivatives keeps the missing power: nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero.

Give the idea a bodily path: Touch the derivatives thread in imagination: make a narrow gate with both hands, block the old path, then open only the route the evidence permits.
<!-- memory-film-v1:end -->

## The calculation hidden inside derivatives

The keeper of uncertain stories carries the derivatives scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A village adjusts one alarm dial controlling how much smoke is needed before ringing a bell. At setting 3 the false-alarm cost is 9. Raising the dial by only 0.001 changes the cost to about 9.006001. The extra cost divided by the tiny dial movement is about 6. Repeating with ever smaller movements reveals the local sensitivity at the current setting rather than the effect of one arbitrary jump.

### Naming what is already on the table

**w** is the one weight whose responsibility we are probing.
**ε** is a small experimental nudge.
**L(w+ε)−L(w)** measures the loss change caused by that nudge.
Dividing by ε turns total change into change per unit of weight.
The limit shrinks the nudge so the answer becomes local rather than dependent on an arbitrary test step.
**dL/dw** names that local sensitivity.

### Why the melody needs these exact notes

[The numerator subtracts](../../MATHEMATICAL_MOVES.md#subtraction) old loss from nudged loss to isolate what the nudge changed; adding them would mix level with change.
[Division by the weight nudge](../../MATHEMATICAL_MOVES.md#division) converts raw loss change into loss change **per unit of weight change**, making different probe sizes comparable.
[The limit](../../MATHEMATICAL_MOVES.md#limit) lets the probe approach zero so curvature across a large jump does not disguise the local slope; setting ε equal to zero directly would divide by zero.

The mandala has curved back upon itself. In this chamber we meet **the chisel**—what is shared is removed so the remaining change can be seen; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. What seemed like a new formula is older mathematical instinct arranged around a new need.

Cover the prose about derivatives and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
\frac{dL}{dw}=\lim_{\epsilon\to0}\frac{L(w+\epsilon)-L(w)}{\epsilon}
$$

## Derivatives beyond this one case

A derivative is a local slope on a mountain trail: it says which direction rises and how sharply, only near the current step.

## Where derivatives runs out

A derivative is local advice. Curved landscapes can change direction, flatten, or hide better valleys elsewhere.

The derivatives repair holds, but the world asks for something it was never given. At the Lantern Observatory, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the ring of glass lanterns

Rebuild the derivatives scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
