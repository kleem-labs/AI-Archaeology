# Excavation 162 — Pre-Normalization — Protect the Residual Highway

The block is cheaper, but making it deeper reveals unstable early gradients when normalization follows each residual addition.

Perhaps we keep post-normalization because each block's output then looks standardized before the next block.

It survives until the measured run answers back. The supposedly clean output places normalization directly on the identity route every gradient must cross, making the long residual path harder to preserve.

Now the missing requirement is concrete. Normalize only the input to the changing branch and let the identity stream pass around it unchanged.

## Let one run decide

A block computes a normalized proposal F, then adds that proposal to the untouched x. If F initially contributes little, the block can behave almost like identity.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

Let the residual stream carry a useful tiger signal x. The new branch examines a normalized copy and proposes a correction F(...). At initialization that proposal may be almost zero. Adding it to the untouched x lets the block say 'change nothing yet'; replacing x with the proposal would destroy the signal. The layer indices merely distinguish the stream before and after this addition.

x_l is the residual stream entering layer l; RMSNorm prepares only the branch; F proposes a change; x_l+1 is the next stream.

### Why these operations are forced

[Function application](../../MATHEMATICAL_MOVES.md#function-application) fixes the order: normalize, then transform. [Addition](../../MATHEMATICAL_MOVES.md#addition) preserves an untouched identity contribution beside the proposal. Replacing x with F would erase the gradient highway; normalizing the sum would place another transformation on that highway.

Only now can we compress the procedure:

$$
x_{\ell+1}=x_\ell+F(\mathrm{RMSNorm}(x_\ell))
$$

## What this repair cannot do

Pre-normalization improves gradient behavior but changes representation scale and does not eliminate every deep-training instability.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: SwiGLU — Let One Learned Path Gate Another](../163-swiglu/README.md)
