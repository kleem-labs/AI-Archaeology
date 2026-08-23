# Excavation 085 — Denoising — Predicting What the Noise Hid

<!-- book-prose-v2 -->

The forward diffusion process tells us exactly how clean image and noise combine at every step. Generation now depends on a network that can inspect the corrupted image and infer what the noise hid.

For a moment, remain loyal to the simplest proposal: ask it to recreate the entire clean image directly from every noise level.

Its appeal is not ignorance but economy. Denoising should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Reality now asks a question the retained information cannot answer: the task changes dramatically across noise strengths.

Notice what the counterexample has accomplished for denoising. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: tell the model the noise level and predict the added noise or equivalent clean direction.

Humanity eventually gathered this problem and its repairs under the name **Denoising**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace denoising with the old instruction to ask it to recreate the entire clean image directly from every noise level. The result is again that the task changes dramatically across noise strengths. Put back only the requirement to tell the model the noise level and predict the added noise or equivalent clean direction. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when denoising is introduced. The same evidence that defeated the attempt to ask it to recreate the entire clean image directly from every noise level is presented again. Only the ability to tell the model the noise level and predict the added noise or equivalent clean direction changes, so the repaired conclusion cannot be credited to a conveniently different example.

## Predicting What the Noise Hid

If known noise [0.2,-0.1] was added, learning to estimate it lets subtraction move toward the clean sample.

Run the denoising scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

## The calculation hidden inside denoising

Before Denoising receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Take one pixel from that corrupted tiger image. We know the random grain added to it was `+0.30`. The denoiser sees the corrupted image and the current noise step and predicts `+0.20`. Its error is `0.10`; squaring makes the contribution `0.01` and prevents a `-0.10` error elsewhere from cancelling it. Repeating this comparison across pixels and images teaches the network which part of a noisy observation should be removed.

xt is the noisy image already constructed in the example.
t tells the network how much corruption it faces.
The network predicts the exact noise ε that hid the clean image.
Squaring the pixel-by-pixel prediction error prevents cancellation; averaging trains across samples.

### Why no cheaper operation does the same job

[Subtracting predicted noise from actual noise](../../MATHEMATICAL_MOVES.md#subtraction) isolates the denoiser's error rather than their combined amount.
[The squared norm](../../MATHEMATICAL_MOVES.md#norm) lets every pixel error contribute without opposite signs cancelling and penalizes large misses more strongly.
[Expectation](../../MATHEMATICAL_MOVES.md#expectation) averages that error over images, noise samples, and times according to how training encounters them.

Every symbol in Denoising can now be read back into an action already performed. The whole procedure fits in one line:

$$
L=\mathbb{E}\left[\lVert\epsilon-\epsilon_\theta(x_t,t)\rVert^2\right]
$$

## Where denoising runs out

Prediction parameterization and schedule affect stability and quality.

Why does that boundary remain? Denoising was built for one responsibility: tell the model the noise level and predict the added noise or equivalent clean direction. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take denoising to the workbench

The argument for denoising is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running denoising, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the denoising result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 086](../086-rewards/README.md)
