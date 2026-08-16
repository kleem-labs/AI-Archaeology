# Excavation 189 — Cosine Decay — Make Late Corrections Smaller Without a Cliff

Warmup protects the optimizer's first steps. Keeping the peak rate for the entire token budget makes late updates as aggressive as early ones even when the model is refining rather than discovering broad structure.

We first try to drop the rate abruptly near the end of training.

That confidence lasts only until the first measurement. A sudden cliff changes update scale in one step and makes the chosen drop date an arbitrary discontinuity; dropping too early freezes useful learning.

What broke tells us what the next design must preserve. Decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state.

## Let one run decide

Halfway through decay, cosine is zero, so the rate sits halfway between its peak and minimum. At the final planned update, cosine reaches negative one and the rate reaches the minimum without a jump.

## The arithmetic we have earned

t is model-training progress through the decay interval of length T; eta_max and eta_min are its endpoint rates; cosine supplies a smooth path between them.

### Why these operations are forced

[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) isolates the adjustable rate range, [division](../../MATHEMATICAL_MOVES.md#division) converts progress to a fraction, and [cosine](../../MATHEMATICAL_MOVES.md#cosine) bends that fraction smoothly with flat endpoint slopes. Addition places the scaled range above eta_min. A raw linear drop is possible, but cosine avoids an abrupt endpoint slope.

Only now can we compress the procedure:

$$
\eta_t=\eta_{\min}+\frac{\eta_{\max}-\eta_{\min}}{2}\left(1+\cos\frac{\pi t}{T}\right)
$$

## What this repair cannot do

Cosine decay assumes a known horizon and is not automatically optimal when training is unexpectedly extended.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Gradient Noise Scale — When More Examples Stop Buying More Direction](../190-gradient-noise-scale/README.md)
