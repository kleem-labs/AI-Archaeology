# Excavation 085 — Denoising — Predicting What the Noise Hid

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

The forward diffusion process tells us exactly how clean image and noise combine at every step. Generation now depends on a network that can inspect the corrupted image and infer what the noise hid.

A new case arrives at the Glass Menagerie, but the maker of seeing-machines first reaches for the familiar wall of illuminated tiles. Its promise is simple: ask it to recreate the entire clean image directly from every noise level.

The rule survives the easy cases. The next case leaves a crack through the middle of it: the task changes dramatically across noise strengths. More confidence cannot repair information that never entered the rule.

*The maker of seeing-machines sketches the break before changing it:*

```text
OLD PATH:  request ──▶ ask it to recreate the entire clean… ──▶ the task changes dramatically across…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ tell the model the noise level and… ──▶ accountable result
```

Two trails now cross the wall of illuminated tiles. The pale trail bears the instruction “ask it to recreate the entire clean image directly from every noise level.” It disappears into the observed failure: the task changes dramatically across noise strengths. The darker trail carries one additional capacity—to tell the model the noise level and predict the added noise or equivalent clean direction. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed denoising mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the wall of illuminated tiles is altered in exactly one way: tell the model the noise level and predict the added noise or equivalent clean direction. Much later, people will call this territory **Denoising**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the wall of illuminated tiles. The failed path remains visible beneath the repair, because denoising is easier to remember when its scar remains attached to it. The scar reads, ‘the task changes dramatically across noise strengths’; the new line exists only to keep that loss from happening again.

## Predicting What the Noise Hid

If known noise [0.2,-0.1] was added, learning to estimate it lets subtraction move toward the clean sample.

## The calculation hidden inside denoising

The maker of seeing-machines carries the denoising scene to the wall of illuminated tiles. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Take one pixel from that corrupted tiger image. We know the random grain added to it was `+0.30`. The denoiser sees the corrupted image and the current noise step and predicts `+0.20`. Its error is `0.10`; squaring makes the contribution `0.01` and prevents a `-0.10` error elsewhere from cancelling it. Repeating this comparison across pixels and images teaches the network which part of a noisy observation should be removed.

xt is the noisy image already constructed in the example.
t tells the network how much corruption it faces.
The network predicts the exact noise ε that hid the clean image.
Squaring the pixel-by-pixel prediction error prevents cancellation; averaging trains across samples.

### Why the melody needs these exact notes

[Subtracting predicted noise from actual noise](../../MATHEMATICAL_MOVES.md#subtraction) isolates the denoiser's error rather than their combined amount.
[The squared norm](../../MATHEMATICAL_MOVES.md#norm) lets every pixel error contribute without opposite signs cancelling and penalizes large misses more strongly.
[Expectation](../../MATHEMATICAL_MOVES.md#expectation) averages that error over images, noise samples, and times according to how training encounters them.

Trace each operation by touch rather than by name: **the chisel**—what is shared is removed so the remaining change can be seen; and **the council of possible worlds**—each future speaks in proportion to how often it may arrive. Together they form the smallest mechanism that survives the counterexample.

The maker of seeing-machines reads the journey of denoising once more across the wall of illuminated tiles, then lets the words contract without losing their order:

$$
L=\mathbb{E}\left[\lVert\epsilon-\epsilon_\theta(x_t,t)\rVert^2\right]
$$

## Where denoising runs out

Prediction parameterization and schedule affect stability and quality.

The wall of illuminated tiles answers today's question and falls silent at the next. That silence is precise: Denoising was built to repair one failure, not to pretend every later boundary is already solved.

## Light learns a path home

Pixels became neighborhoods, neighborhoods became parts, parts became objects, and compressed coordinates became places from which images could be rebuilt. Diffusion completed the arc by turning destruction into a curriculum for creation.

```text
light → locality → hierarchy → latent space → noise → image
```

The trail called *light learns a path home* is what remains when one necessity becomes another.

## Return to the wall of illuminated tiles

Rebuild the denoising scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 086](../086-rewards/README.md)
