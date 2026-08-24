# Excavation 027 — Learning Rate — How Large Should the Next Step Be?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Learning from uncertainty and error

A mini-batch replaces one noisy witness with the average advice of a small council. The council can point downhill, but its vote still says nothing about how far the network should move.

Night gathers around the Lantern Observatory. Under the light of the ring of glass lanterns, the keeper of uncertain stories refuses to invent prematurely and begins with the plain rule: always take a huge step: leap across the valley and oscillate.

Then the quiet test arrives: always take a microscopic step: improve so slowly that the expedition ends first. What looked like simplicity is revealed as a missing distinction.

*The keeper of uncertain stories sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: always take a huge step: leap across…
                         │
                         └── mismatch: always take a microscopic step:…

reference evidence ──▶ measured repair: we need to multiply the gradient by a…
```

The keeper of uncertain stories turns the ring of glass lanterns toward the light. Through the old engraving, always take a huge step: leap across the valley and oscillate, the evidence ends in the same contradiction: always take a microscopic step: improve so slowly that the expedition ends first. A second engraving adds only the power to multiply the gradient by a learning rate, observe whether loss descends, and adjust the rate over time. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The keeper of uncertain stories circles the place where the two learning rate cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: we need to multiply the gradient by a learning rate, observe whether loss descends, and adjust the rate over time. The keeper of uncertain stories writes **Learning Rate** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The keeper of uncertain stories places a finger over the new distinction. At once the two cases collapse and always take a microscopic step: improve so slowly that the expedition ends first. Lifting the finger restores only this capacity: multiply the gradient by a learning rate, observe whether loss descends, and adjust the rate over time. That tiny reversible motion is the chapter's proof of necessity.

<!-- memory-film-v1:start -->
> **Memory realm 3 of 18 — [Lantern Observatory](../../MEMORY_PALACE.md#realm-3)**
>
> **The question carried into this chamber:** How Large Should the Next Step Be?

## When the chamber changes

The Learning Rate chamber leaves one scene behind so the idea can be recovered after its symbols fade.

First hold the failed picture still: The wheel follows the tempting path—always take a huge step: leap across the valley and oscillate. Then the evidence answers: always take a microscopic step: improve so slowly that the expedition ends first.

Now let the chamber move: The keeper of uncertain stories changes one moving part. The wheel can now multiply the gradient by a learning rate, observe whether loss descends, and adjust the rate over time.

The object that should remain after the terminology disappears is **the learning rate wheel mounted on the ring of glass lanterns**.

> **Memory seal — Learning Rate**
>
> Learning Rate keeps the missing power: multiply the gradient by a learning rate, observe whether loss descends, and adjust the rate over time.

Give the idea a bodily path: Touch the learning rate wheel in imagination: close one fist around the lost information, then open it as the repair restores that information.
<!-- memory-film-v1:end -->

## The calculation hidden inside learning rate

The keeper of uncertain stories carries the learning rate scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but no single learning rate is best throughout training. Scale, curvature, batch noise, and parameter units all matter.

The tiger alarm's stripe dial is again 8, and the local uphill sensitivity is 10. Moving opposite the entire suggestion sends the dial to −2 and jumps across the best setting. Trusting one tenth moves it to 7; trusting one hundredth moves it to 7.9. All three moves use the same downhill direction. The learning rate answers the separate human question: how much of that local advice should we trust now?

### Naming what is already on the table

**g_t** is the downhill evidence measured at step t.
**η_t** converts direction into a chosen travel distance and may change with time.
The minus sign moves against increasing loss.
**θ_t** and **θ_{t+1}** distinguish the old and updated parameter states.

### Why the melody needs these exact notes

[gₜ](../../MATHEMATICAL_MOVES.md#gradient) gives direction but not distance.
[Multiplying by ηₜ](../../MATHEMATICAL_MOVES.md#multiplication) turns the direction into a controllable step for this time t; adding η would shift every coordinate regardless of the gradient's direction.
[Subtraction](../../MATHEMATICAL_MOVES.md#negative-sign) moves opposite the locally uphill gradient rather than making loss rise faster.

The symbols are about to change costume, but their work has appeared before: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the turning wind**—an uphill quantity is made to point downhill, or surprise is made to count as cost. This is how distant excavations begin to sound like variations of one melody.

The story of learning rate has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
\theta_{t+1}=\theta_t-\eta_t g_t
$$

## Learning Rate beyond this one case

A mountain guide chooses shorter steps on steep or uncertain ground and can walk farther on a smooth open slope.

## Return to the ring of glass lanterns

Rebuild the learning rate scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Excavation 028](../028-momentum/README.md)
