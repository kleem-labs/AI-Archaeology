# Excavation 165 — Adam — Give Each Parameter Its Own Step Scale

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

Weight tying concentrates more roles in shared parameters. During training, some coordinates receive frequent large gradients while rare-token coordinates receive sparse small ones.

A new case arrives at the Engine Cavern, but the enginewright first reaches for the familiar brass reference machine. Its promise is simple: use the same raw gradient step scale for every parameter.

Then the quiet test arrives: a rate safe for frequent large gradients barely moves sparse coordinates; a rate large enough for sparse coordinates makes noisy ones unstable. What looked like simplicity is revealed as a missing distinction.

*The enginewright sketches the break before changing it:*

```text
OLD PATH:  request ──▶ use the same raw gradient step scale… ──▶ a rate safe for frequent large…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ keep fading memories of gradient… ──▶ accountable result
```

The enginewright turns the brass reference machine toward the light. Through the old engraving, use the same raw gradient step scale for every parameter, the evidence ends in the same contradiction: a rate safe for frequent large gradients barely moves sparse coordinates; a rate large enough for sparse coordinates makes noisy ones unstable. A second engraving adds only the power to keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The enginewright circles the place where the two adam cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude. The enginewright writes **Adam** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The enginewright does not memorize adam. Instead, the enginewright memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude. The formal name merely lets that motion be shared.

<!-- memory-film-v1:start -->
> **Memory realm 12 of 18 — [Engine Cavern](../../MEMORY_PALACE.md#realm-12)**
>
> **The question carried into this chamber:** What fails if we use the same raw gradient step scale for every parameter?

## When the chamber changes

The Adam room does not ask you to memorize its name. It asks you to watch one object change.

First hold the failed picture still: The bridge follows the tempting path—use the same raw gradient step scale for every parameter. Then the evidence answers: a rate safe for frequent large gradients barely moves sparse coordinates; a rate large enough for sparse coordinates makes noisy ones unstable.

Now let the chamber move: The enginewright changes one moving part. The bridge can now keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude.

The object that should remain after the terminology disappears is **the adam bridge mounted on the brass reference machine**.

> **Memory seal — Adam**
>
> Adam keeps the missing power: keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude.

Give the idea a bodily path: Touch the adam bridge in imagination: tilt one hand as the broken rule and use the other to bring the necessary distinction back into balance.
<!-- memory-film-v1:end -->

## Give Each Parameter Its Own Step Scale

A frequently noisy weight builds a large second-moment estimate and receives a smaller normalized step; a consistently directed sparse weight can still move.

## The calculation hidden inside adam

The enginewright carries the adam scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Follow one weight that repeatedly receives gradients near 2 and another that usually receives gradients near 0.2. A single raw step scale makes their movement differ tenfold even if each signal is ordinary for its own weight. Remember each weight's recent direction in m and its recent squared size in v; compare direction with the square root of size, then let eta choose the common overall pace. Epsilon is the tiny floor that keeps a never-touched weight from asking us to divide by zero.

m-hat is bias-corrected directional memory, v-hat is bias-corrected squared-gradient memory, eta is global scale, and epsilon prevents division by zero.

### Why the melody needs these exact notes

[Division](../../MATHEMATICAL_MOVES.md#division) measures direction relative to recent gradient magnitude, giving each coordinate an adaptive scale. The [square root](../../MATHEMATICAL_MOVES.md#square-root) returns squared-gradient memory to gradient units. [Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) moves opposite estimated uphill direction; adding would increase loss locally.

Trace each operation by touch rather than by name: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; **the road home**—a squared construction returns to the scale of the world that created it; and **the chisel**—what is shared is removed so the remaining change can be seen. Together they form the smallest mechanism that survives the counterexample.

The story of adam has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
\theta_{t+1}=\theta_t-\eta\frac{\widehat m_t}{\sqrt{\widehat v_t}+\epsilon}
$$

## Where adam runs out

Adaptive scaling can generalize differently from SGD and introduces extra state for every parameter.

One unsolved mark remains on the brass reference machine. None of the responsibilities inside Adam can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the brass reference machine

Rebuild the adam scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: AdamW — Keep Shrinkage Separate from Adaptation](../166-adamw/README.md)
