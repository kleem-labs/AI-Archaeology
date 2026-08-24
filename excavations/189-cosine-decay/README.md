# Excavation 189 — Cosine Decay — Make Late Corrections Smaller Without a Cliff

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Data and pretraining operations

Warmup protects the optimizer's first steps. Keeping the peak rate for the entire token budget makes late updates as aggressive as early ones even when the model is refining rather than discovering broad structure.

A new case arrives at the Archive Foundry, but the archivist-engineer first reaches for the familiar chain-of-custody ledger. Its promise is simple: drop the rate abruptly near the end of training.

Then the quiet test arrives: a sudden cliff changes update scale in one step and makes the chosen drop date an arbitrary discontinuity; dropping too early freezes useful learning. What looked like simplicity is revealed as a missing distinction.

*The archivist-engineer sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ drop the rate abruptly near the end… ──▶ blurred: a sudden cliff changes update scale…
      │
      └── new lens ──▶ decay smoothly from the peak toward a… ──▶ distinction survives
```

The archivist-engineer turns the chain-of-custody ledger toward the light. Through the old engraving, drop the rate abruptly near the end of training, the evidence ends in the same contradiction: a sudden cliff changes update scale in one step and makes the chosen drop date an arbitrary discontinuity; dropping too early freezes useful learning. A second engraving adds only the power to decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The archivist-engineer circles the place where the two cosine decay cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state. The archivist-engineer writes **Cosine Decay** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The archivist-engineer does not memorize cosine decay. Instead, the archivist-engineer memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state. The formal name merely lets that motion be shared.

<!-- memory-film-v1:start -->
> **Memory realm 13 of 18 — [Archive Foundry](../../MEMORY_PALACE.md#realm-13)**
>
> **The question carried into this chamber:** What fails if we drop the rate abruptly near the end of training?

## When the chamber changes

The mathematical name Cosine Decay can now rest. What matters is whether its transformation remains visible.

First hold the failed picture still: The scale follows the tempting path—drop the rate abruptly near the end of training. Then the evidence answers: a sudden cliff changes update scale in one step and makes the chosen drop date an arbitrary discontinuity; dropping too early freezes useful learning.

Now let the chamber move: The archivist-engineer changes one moving part. The scale can now decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state.

The object that should remain after the terminology disappears is **the cosine decay scale mounted on the chain-of-custody ledger**.

> **Memory seal — Cosine Decay**
>
> Cosine Decay keeps the missing power: decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state.

Give the idea a bodily path: Touch the cosine decay scale in imagination: tilt one hand as the broken rule and use the other to bring the necessary distinction back into balance.
<!-- memory-film-v1:end -->

## Make Late Corrections Smaller Without a Cliff

Halfway through decay, cosine is zero, so the rate sits halfway between its peak and minimum. At the final planned update, cosine reaches negative one and the rate reaches the minimum without a jump.

## The calculation hidden inside cosine decay

The archivist-engineer carries the cosine decay scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

t is model-training progress through the decay interval of length T; eta_max and eta_min are its endpoint rates; cosine supplies a smooth path between them.

### Why the melody needs these exact notes

[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) isolates the adjustable rate range, [division](../../MATHEMATICAL_MOVES.md#division) converts progress to a fraction, and [cosine](../../MATHEMATICAL_MOVES.md#cosine) bends that fraction smoothly with flat endpoint slopes. Addition places the scaled range above eta_min. A raw linear drop is possible, but cosine avoids an abrupt endpoint slope.

Trace each operation by touch rather than by name: **the chisel**—what is shared is removed so the remaining change can be seen; **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; and **the returning tide**—movement bends smoothly and reaches its shore without a cliff. Together they form the smallest mechanism that survives the counterexample.

The story of cosine decay has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
\eta_t=\eta_{\min}+\frac{\eta_{\max}-\eta_{\min}}{2}\left(1+\cos\frac{\pi t}{T}\right)
$$

## Where cosine decay runs out

Cosine decay assumes a known horizon and is not automatically optimal when training is unexpectedly extended.

One unsolved mark remains on the chain-of-custody ledger. None of the responsibilities inside Cosine Decay can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the chain-of-custody ledger

Rebuild the cosine decay scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Gradient Noise Scale — When More Examples Stop Buying More Direction](../190-gradient-noise-scale/README.md)
