# Part XII Plan — Rebuilding the Engine Without Breaking the System

Excavation 150 closes the authority loop: a proposed improvement may replace
the current system only after controlled evidence, review, staged release, and
rollback planning. That ending creates a new kind of freedom. We may return to
the tiny GPT and improve its engine—but now every change must expose the
bottleneck it solves and the trade it introduces.

## The single experiment

A ranger station wants to train and serve a stronger language model on limited
hardware. We freeze one reproducible baseline, measure where its time and memory
go, and alter one mechanism at a time. The object under construction never
resets.

| Movement | Excavations | Necessity |
|---|---:|---|
| Establish honest evidence | 151–154 | Freeze a baseline, profile it, keep devices fed, and stop paying for padding. |
| Repair attention for modern decoding | 155–160 | Encode useful relative position, stop recomputing the past, reduce KV traffic, and make exact attention respect memory hierarchy. |
| Stabilize the block | 161–164 | Simplify normalization, preserve the residual highway, gate private computation, and reuse learned word geometry. |
| Make optimization survive scale | 165–171 | Adapt steps, separate decay, stop gradient explosions, use reduced precision safely, assemble larger effective batches, and trade recomputation for memory. |
| Cross the device boundary and serve | 172–175 | Shard redundant state, split large matrices, verify cheap drafts with the real model, and assemble the modern tiny language model. |

## Boundary rule

Every chapter must open with the exact capability earned by its predecessor and
the next measured failure. No optimization is introduced because modern models
use it. It appears only after the baseline makes its cost visible.

## Mathematical rule

Every displayed equation must explain:

1. the concrete quantities entering each operation;
2. why the chosen operation preserves the required relationship;
3. why the nearest alternative—sum, product, raw count, max, or replacement—
   answers the wrong question;
4. where that move can be reused through `MATHEMATICAL_MOVES.md`.

## Primary research trail

- [RoFormer / RoPE](https://arxiv.org/abs/2104.09864)
- [ALiBi](https://arxiv.org/abs/2108.12409)
- [Multi-query attention](https://arxiv.org/abs/1911.02150)
- [Grouped-query attention](https://arxiv.org/abs/2305.13245)
- [FlashAttention](https://arxiv.org/abs/2205.14135)
- [RMSNorm](https://arxiv.org/abs/1910.07467)
- [Pre-LN analysis](https://proceedings.mlr.press/v119/xiong20b.html)
- [GLU variants / SwiGLU](https://arxiv.org/abs/2002.05202)
- [Adam](https://arxiv.org/abs/1412.6980)
- [AdamW](https://openreview.net/forum?id=Bkg6RiCqY7)
- [Mixed-precision training](https://arxiv.org/abs/1710.03740)
- [Activation checkpointing](https://arxiv.org/abs/1604.06174)
- [ZeRO](https://arxiv.org/abs/1910.02054)
- [Megatron-LM](https://arxiv.org/abs/1909.08053)
- [Speculative decoding](https://proceedings.mlr.press/v202/leviathan23a.html)
