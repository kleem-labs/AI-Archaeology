# Excavation 189 — Cosine Decay — Make Late Corrections Smaller Without a Cliff

<!-- book-prose-v2 -->

Warmup protects the optimizer's first steps. Keeping the peak rate for the entire token budget makes late updates as aggressive as early ones even when the model is refining rather than discovering broad structure.

At this point the shortest path seems to be to drop the rate abruptly near the end of training.

This is how cosine decay ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Reality now asks a question the retained information cannot answer: a sudden cliff changes update scale in one step and makes the chosen drop date an arbitrary discontinuity; dropping too early freezes useful learning.

The wrong answer makes the need for cosine decay inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state.

The usual name, **Cosine Decay**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to drop the rate abruptly near the end of training produces the observed failure: a sudden cliff changes update scale in one step and makes the chosen drop date an arbitrary discontinuity; dropping too early freezes useful learning. Starting with the repaired demand to decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state preserves the information the shortcut lost. The subject of cosine decay lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state instead of merely trying to drop the rate abruptly near the end of training. That controlled contrast is what turns a plausible explanation of cosine decay into an understandable derivation.

## Make Late Corrections Smaller Without a Cliff

Halfway through decay, cosine is zero, so the rate sits halfway between its peak and minimum. At the final planned update, cosine reaches negative one and the rate reaches the minimum without a jump.

There are now two histories of this cosine decay case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

## The calculation hidden inside cosine decay

Before Cosine Decay receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

t is model-training progress through the decay interval of length T; eta_max and eta_min are its endpoint rates; cosine supplies a smooth path between them.

### Why no cheaper operation does the same job

[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) isolates the adjustable rate range, [division](../../MATHEMATICAL_MOVES.md#division) converts progress to a fraction, and [cosine](../../MATHEMATICAL_MOVES.md#cosine) bends that fraction smoothly with flat endpoint slopes. Addition places the scaled range above eta_min. A raw linear drop is possible, but cosine avoids an abrupt endpoint slope.

Every symbol in Cosine Decay can now be read back into an action already performed. The whole procedure fits in one line:

$$
\eta_t=\eta_{\min}+\frac{\eta_{\max}-\eta_{\min}}{2}\left(1+\cos\frac{\pi t}{T}\right)
$$

## Where cosine decay runs out

Cosine decay assumes a known horizon and is not automatically optimal when training is unexpectedly extended.

Look back at what cosine decay actually preserves: it can decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

## Take cosine decay to the workbench

The reader has reconstructed cosine decay in words; the workbench tests whether those words specify a real procedure. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running cosine decay, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the cosine decay result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Gradient Noise Scale — When More Examples Stop Buying More Direction](../190-gradient-noise-scale/README.md)
