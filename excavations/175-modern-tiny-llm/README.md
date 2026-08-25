# Excavation 175 — A Modern Tiny Language Model — Assemble the Measured Engine

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Model systems and engine optimization

Speculative decoding accelerates the final serial loop. We now have many locally useful repairs, but a pile of optimizations is not yet one reproducible model.

Inside the Engine Cavern, the old method is given an honest chance. The enginewright places the evidence on the brass reference machine and tries to enable every technique at once and celebrate if the program runs.

Nothing about this first move is careless. To enable every technique at once and celebrate if the program runs is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: when quality or speed changes, no one knows which mechanism caused it; masks, precision, sharding, and caches can disagree at their boundaries.

The important discovery is not merely that trying to enable every technique at once and celebrate if the program runs failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the brass reference machine, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to assemble the engine in dependency order, preserve a reference path, and test numerical or distributional equivalence at every boundary before accepting measured gains. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **A Modern Tiny Language Model**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## Assemble the Measured Engine

Train one tiny model with packed examples, RoPE, GQA, exact tiled attention, pre-RMSNorm, SwiGLU, tied embeddings, AdamW, clipping, mixed precision, accumulation, and checkpointing; then serve it with a KV cache and verified draft proposals.

## Where a modern tiny language model runs out

The engine is modern, not final. New hardware, data, and observations will create new bottlenecks, and every proposed repair must re-enter the bounded loop from Excavation 150.

The brass reference machine answers today's question and falls silent at the next. That silence is precise: Modern Tiny Language Model was built to repair one failure, not to pretend every later boundary is already solved.

## The old mind inside the new engine

The engine has changed its position system, cache, attention kernel, normalization, gate, optimizer, precision, memory plan, and distribution across machines. Yet the reference path remains beside it like a tuning fork: every faster mechanism must still produce the mathematical responsibility first derived in the valley.

```text
reference ──preserved meaning──▶ optimized engine
```

The trail called *the old mind inside the new engine* is what remains when one necessity becomes another.

## Return to the brass reference machine

Rebuild the modern tiny language model scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
