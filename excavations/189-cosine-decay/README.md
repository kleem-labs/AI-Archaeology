# Excavation 189 — Cosine Decay — Make Late Corrections Smaller Without a Cliff

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Data and pretraining operations

Warmup protects the optimizer's first steps. Keeping the peak rate for the entire token budget makes late updates as aggressive as early ones even when the model is refining rather than discovering broad structure.

The previous discovery reaches the Archive Foundry carrying one unfinished problem. Beside the chain-of-custody ledger, the archivist-engineer first tries to drop the rate abruptly near the end of training.

There is good reason to begin this way. If we drop the rate abruptly near the end of training, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: a sudden cliff changes update scale in one step and makes the chosen drop date an arbitrary discontinuity; dropping too early freezes useful learning.

This failure cannot be repaired by performing the instruction to drop the rate abruptly near the end of training more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the chain-of-custody ledger; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Cosine Decay**. The name is simply a handle for the distinction already reconstructed.

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
