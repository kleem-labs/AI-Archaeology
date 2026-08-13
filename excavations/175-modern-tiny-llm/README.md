# Excavation 175 — A Modern Tiny Language Model — Assemble the Measured Engine

Speculative decoding accelerates the final serial loop. We now have many locally useful repairs, but a pile of optimizations is not yet one reproducible model.

Perhaps we enable every technique at once and celebrate if the program runs.

It survives until the measured run answers back. When quality or speed changes, no one knows which mechanism caused it; masks, precision, sharding, and caches can disagree at their boundaries.

Now the missing requirement is concrete. Assemble the engine in dependency order, preserve a reference path, and test numerical or distributional equivalence at every boundary before accepting measured gains.

## Let one run decide

Train one tiny model with packed examples, RoPE, GQA, exact tiled attention, pre-RMSNorm, SwiGLU, tied embeddings, AdamW, clipping, mixed precision, accumulation, and checkpointing; then serve it with a KV cache and verified draft proposals.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## What this repair cannot do

The engine is modern, not final. New hardware, data, and observations will create new bottlenecks, and every proposed repair must re-enter the bounded loop from Excavation 150.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

The engine returns to the bounded research loop: observe, propose, test, verify, authorize, release gradually, and remain able to reverse.
