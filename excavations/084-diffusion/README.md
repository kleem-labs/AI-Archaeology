# Excavation 084 — Diffusion — Learning by Destroying

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Calculus & Differential Change](../../MATHEMATICS_ATLAS.md#calculus) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

Autoregressive image generation chooses one piece after another, making an arbitrary generation order part of the model. Diffusion offers another route: destroy a complete image gradually so that generation can learn to reverse each small corruption.

Inside the Glass Menagerie, every old tool is given one honest chance. The maker of seeing-machines sets the wall of illuminated tiles between the evidence and the desired answer, then tries to map one random vector directly to a finished image in one jump.

For a moment the mark looks complete. Then the evidence refuses to fit: one enormous jump is difficult to learn and unstable across diverse images. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The maker of seeing-machines sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   map one random vector directly to a… one enormous jump is difficult to…
            \        /
             \      /
              gradually add noise to real images,…
```

The maker of seeing-machines lays two translucent sheets over the wall of illuminated tiles. The first is inscribed, “map one random vector directly to a finished image in one jump.” Its path ends where one enormous jump is difficult to learn and unstable across diverse images. The second receives the same evidence but is allowed to gradually add noise to real images, then learn the smaller reverse step at every noise level. Held to the light, the sheets separate at exactly one decision.

No one reaches for a diffusion formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The maker of seeing-machines changes only that one responsibility: gradually add noise to real images, then learn the smaller reverse step at every noise level. When the ink dries, the name **Diffusion** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The wall of illuminated tiles keeps both histories. Its older mark still says, ‘map one random vector directly to a finished image in one jump’; beside it, the newer mark says, ‘gradually add noise to real images, then learn the smaller reverse step at every noise level.’ The distance between those sentences is the exact shape of diffusion: no larger than the failure required, and no smaller than reality permits.

## Learning by Destroying

A tiger image becomes slightly grainy, then more noisy, then nearly random; training learns each local cleanup.

## The calculation hidden inside diffusion

The maker of seeing-machines carries the diffusion scene to the wall of illuminated tiles. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Print a clean tiger photograph on transparent film. At the first step, keep almost all of the photograph and mix in a faint sheet of random grain. At later steps, keep less tiger and add more grain until the animal is nearly lost. The two mixing amounts must be coordinated: increasing noise while keeping all the original image would make total intensity grow without bound. The square-root factors preserve a controlled overall scale while transferring influence from image to noise.

The clean image is the named tiger image x0.
Noise ε is the random corruption added during the forward process.
The retained clean fraction and noise fraction change with step t.
Square roots scale amplitudes so their variances combine as intended.

### Why the melody needs these exact notes

[The two multiplications](../../MATHEMATICAL_MOVES.md#multiplication) scale how much clean image and fresh noise survive at time t.
[Addition](../../MATHEMATICAL_MOVES.md#addition) overlays those two same-shaped image contributions. Concatenation would produce two images side by side rather than one corrupted image.
[Square roots of the variance shares](../../MATHEMATICAL_MOVES.md#square-root) convert variance allocation into amplitude scaling; the two squared amplitudes then sum to one total variance.

Inside diffusion, familiar operations return with stricter duties: **the lock and key**—one influence matters through another, and either missing factor can close the path; **the joining river**—separate contributions meet without losing where they came from; and **the road home**—a squared construction returns to the scale of the world that created it. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Every mark needed for diffusion is now visible on the wall of illuminated tiles. The symbols do not add an idea; they bind the discovered moves into one line:

$$
x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon
$$

## Where diffusion runs out

Many denoising steps make sampling expensive.

At the Glass Menagerie, the maker of seeing-machines leaves a blank beneath the new mark. Diffusion has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the wall of illuminated tiles

Rebuild the diffusion scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 085](../085-denoising/README.md)
