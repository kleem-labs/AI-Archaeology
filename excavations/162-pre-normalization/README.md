# Excavation 162 — Pre-Normalization — Protect the Residual Highway

<!-- book-prose-v2 -->

The block is cheaper, but making it deeper reveals unstable early gradients when normalization follows each residual addition.

The obvious economy is to keep post-normalization because each block's output then looks standardized before the next block.

The proposal deserves a fair hearing. For pre-normalization, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Its hidden assumption becomes visible as soon as we observe that the supposedly clean output places normalization directly on the identity route every gradient must cross, making the long residual path harder to preserve.

The failure changes the question behind pre-normalization. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: normalize only the input to the changing branch and let the identity stream pass around it unchanged.

Only at this point does the inherited name **Pre-Normalization** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of pre-normalization by mentally removing the repair. We fall back to the proposal to keep post-normalization because each block's output then looks standardized before the next block; then the supposedly clean output places normalization directly on the identity route every gradient must cross, making the long residual path harder to preserve. Restore only the ability to normalize only the input to the changing branch and let the identity stream pass around it unchanged, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to keep post-normalization because each block's output then looks standardized before the next block to requiring the system to normalize only the input to the changing branch and let the identity stream pass around it unchanged. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to pre-normalization.

## Protect the Residual Highway

A block computes a normalized proposal F, then adds that proposal to the untouched x. If F initially contributes little, the block can behave almost like identity.

Put the old procedure beside pre-normalization. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## The calculation hidden inside pre-normalization

Do not read the coming Pre-Normalization line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Let the residual stream carry a useful tiger signal x. The new branch examines a normalized copy and proposes a correction F(...). At initialization that proposal may be almost zero. Adding it to the untouched x lets the block say 'change nothing yet'; replacing x with the proposal would destroy the signal. The layer indices merely distinguish the stream before and after this addition.

x_l is the residual stream entering layer l; RMSNorm prepares only the branch; F proposes a change; x_l+1 is the next stream.

### Why no cheaper operation does the same job

[Function application](../../MATHEMATICAL_MOVES.md#function-application) fixes the order: normalize, then transform. [Addition](../../MATHEMATICAL_MOVES.md#addition) preserves an untouched identity contribution beside the proposal. Replacing x with F would erase the gradient highway; normalizing the sum would place another transformation on that highway.

Every symbol in Pre-Normalization can now be read back into an action already performed. The whole procedure fits in one line:

$$
x_{\ell+1}=x_\ell+F(\mathrm{RMSNorm}(x_\ell))
$$

## Where pre-normalization runs out

Pre-normalization improves gradient behavior but changes representation scale and does not eliminate every deep-training instability.

The limit follows from the job assigned to pre-normalization. Its repair knows how to normalize only the input to the changing branch and let the identity stream pass around it unchanged. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take pre-normalization to the workbench

A claim about pre-normalization now exists on the page; the laboratory must be able to contradict it. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running pre-normalization, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the pre-normalization result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: SwiGLU — Let One Learned Path Gate Another](../163-swiglu/README.md)
