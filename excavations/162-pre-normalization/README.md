# Excavation 162 — Pre-Normalization — Protect the Residual Highway

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Model systems and engine optimization

The block is cheaper, but making it deeper reveals unstable early gradients when normalization follows each residual addition.

The brass reference machine at the Engine Cavern still carries the marks of the previous discovery. The enginewright follows them as far as they seem willing to go: keep post-normalization because each block's output then looks standardized before the next block.

For a moment the mark looks complete. Then the evidence refuses to fit: the supposedly clean output places normalization directly on the identity route every gradient must cross, making the long residual path harder to preserve. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The enginewright sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: keep post-normalization because each…
                         │
                         └── mismatch: the supposedly clean output places…

reference evidence ──▶ measured repair: normalize only the input to the…
```

The enginewright lays two translucent sheets over the brass reference machine. The first is inscribed, “keep post-normalization because each block's output then looks standardized before the next block.” Its path ends where the supposedly clean output places normalization directly on the identity route every gradient must cross, making the long residual path harder to preserve. The second receives the same evidence but is allowed to normalize only the input to the changing branch and let the identity stream pass around it unchanged. Held to the light, the sheets separate at exactly one decision.

No one reaches for a pre-normalization formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The enginewright changes only that one responsibility: normalize only the input to the changing branch and let the identity stream pass around it unchanged. When the ink dries, the name **Pre-Normalization** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because the supposedly clean output places normalization directly on the identity route every gradient must cross, making the long residual path harder to preserve, while the other can normalize only the input to the changing branch and let the identity stream pass around it unchanged. That fork—not the vocabulary—is where pre-normalization lives.

<!-- memory-film-v1:start -->
> **Memory realm 12 of 18 — [Engine Cavern](../../MEMORY_PALACE.md#realm-12)**
>
> **The question carried into this chamber:** What fails if we keep post-normalization because each block's output then looks standardized before the next block?

## When the chamber changes

The Pre-Normalization chamber leaves one scene behind so the idea can be recovered after its symbols fade.

First hold the failed picture still: The key follows the tempting path—keep post-normalization because each block's output then looks standardized before the next block. Then the evidence answers: the supposedly clean output places normalization directly on the identity route every gradient must cross, making the long residual path harder to preserve.

Now let the chamber move: The enginewright changes one moving part. The key can now normalize only the input to the changing branch and let the identity stream pass around it unchanged.

The object that should remain after the terminology disappears is **the pre-normalization key mounted on the brass reference machine**.

> **Memory seal — Pre-Normalization**
>
> Pre-Normalization keeps the missing power: normalize only the input to the changing branch and let the identity stream pass around it unchanged.

Give the idea a bodily path: Touch the pre-normalization key in imagination: draw the old path in the air, stop sharply at its failure, and finish with the new motion.
<!-- memory-film-v1:end -->

## Protect the Residual Highway

A block computes a normalized proposal F, then adds that proposal to the untouched x. If F initially contributes little, the block can behave almost like identity.

## The calculation hidden inside pre-normalization

The enginewright carries the pre-normalization scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Let the residual stream carry a useful tiger signal x. The new branch examines a normalized copy and proposes a correction F(...). At initialization that proposal may be almost zero. Adding it to the untouched x lets the block say 'change nothing yet'; replacing x with the proposal would destroy the signal. The layer indices merely distinguish the stream before and after this addition.

x_l is the residual stream entering layer l; RMSNorm prepares only the branch; F proposes a change; x_l+1 is the next stream.

### Why the melody needs these exact notes

[Function application](../../MATHEMATICAL_MOVES.md#function-application) fixes the order: normalize, then transform. [Addition](../../MATHEMATICAL_MOVES.md#addition) preserves an untouched identity contribution beside the proposal. Replacing x with F would erase the gradient highway; normalizing the sum would place another transformation on that highway.

Three old motions cast new shadows here: **the joining river**—separate contributions meet without losing where they came from. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Every mark needed for pre-normalization is now visible on the brass reference machine. The symbols do not add an idea; they bind the discovered moves into one line:

$$
x_{\ell+1}=x_\ell+F(\mathrm{RMSNorm}(x_\ell))
$$

## Where pre-normalization runs out

Pre-normalization improves gradient behavior but changes representation scale and does not eliminate every deep-training instability.

At the Engine Cavern, the enginewright leaves a blank beneath the new mark. Pre-Normalization has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the brass reference machine

Rebuild the pre-normalization scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: SwiGLU — Let One Learned Path Gate Another](../163-swiglu/README.md)
