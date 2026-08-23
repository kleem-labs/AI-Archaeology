# Excavation 084 — Diffusion — Learning by Destroying

<!-- book-prose-v2 -->

Autoregressive image generation chooses one piece after another, making an arbitrary generation order part of the model. Diffusion offers another route: destroy a complete image gradually so that generation can learn to reverse each small corruption.

The least expensive next move is to map one random vector directly to a finished image in one jump.

The proposal deserves a fair hearing. For diffusion, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The proposal breaks for a specific reason, not by authority: one enormous jump is difficult to learn and unstable across diverse images.

The failure changes the question behind diffusion. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: gradually add noise to real images, then learn the smaller reverse step at every noise level.

Only at this point does the inherited name **Diffusion** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of diffusion by mentally removing the repair. We fall back to the proposal to map one random vector directly to a finished image in one jump; then one enormous jump is difficult to learn and unstable across diverse images. Restore only the ability to gradually add noise to real images, then learn the smaller reverse step at every noise level, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to map one random vector directly to a finished image in one jump to requiring the system to gradually add noise to real images, then learn the smaller reverse step at every noise level. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to diffusion.

## Learning by Destroying

A tiger image becomes slightly grainy, then more noisy, then nearly random; training learns each local cleanup.

Put the old procedure beside diffusion. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## The calculation hidden inside diffusion

Do not read the coming Diffusion line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Print a clean tiger photograph on transparent film. At the first step, keep almost all of the photograph and mix in a faint sheet of random grain. At later steps, keep less tiger and add more grain until the animal is nearly lost. The two mixing amounts must be coordinated: increasing noise while keeping all the original image would make total intensity grow without bound. The square-root factors preserve a controlled overall scale while transferring influence from image to noise.

The clean image is the named tiger image x0.
Noise ε is the random corruption added during the forward process.
The retained clean fraction and noise fraction change with step t.
Square roots scale amplitudes so their variances combine as intended.

### Why no cheaper operation does the same job

[The two multiplications](../../MATHEMATICAL_MOVES.md#multiplication) scale how much clean image and fresh noise survive at time t.
[Addition](../../MATHEMATICAL_MOVES.md#addition) overlays those two same-shaped image contributions. Concatenation would produce two images side by side rather than one corrupted image.
[Square roots of the variance shares](../../MATHEMATICAL_MOVES.md#square-root) convert variance allocation into amplitude scaling; the two squared amplitudes then sum to one total variance.

Every symbol in Diffusion can now be read back into an action already performed. The whole procedure fits in one line:

$$
x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon
$$

## Where diffusion runs out

Many denoising steps make sampling expensive.

The limit follows from the job assigned to diffusion. Its repair knows how to gradually add noise to real images, then learn the smaller reverse step at every noise level. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take diffusion to the workbench

A claim about diffusion now exists on the page; the laboratory must be able to contradict it. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running diffusion, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the diffusion result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 085](../085-denoising/README.md)
