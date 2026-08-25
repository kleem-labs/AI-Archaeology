# Excavation 084 — Diffusion — Learning by Destroying

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Calculus & Differential Change](../../MATHEMATICS_ATLAS.md#calculus) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

Autoregressive image generation chooses one piece after another, making an arbitrary generation order part of the model. Diffusion offers another route: destroy a complete image gradually so that generation can learn to reverse each small corruption.

At the Glass Menagerie, the maker of seeing-machines meets the next case beside the wall of illuminated tiles. The nearest idea is also the most reasonable one: map one random vector directly to a finished image in one jump.

The attraction of this attempt is easy to see. To map one random vector directly to a finished image in one jump reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: one enormous jump is difficult to learn and unstable across diverse images.

The contradiction matters because it identifies a structural loss in the instruction to map one random vector directly to a finished image in one jump, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The wall of illuminated tiles will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must gradually add noise to real images, then learn the smaller reverse step at every noise level. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Diffusion**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

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
