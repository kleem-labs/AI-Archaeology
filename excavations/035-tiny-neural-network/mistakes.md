# Mistakes — 035

## Wrong Idea #1

Hide everything behind a framework call. The code runs, but the causal chain disappears. Hand-tune outputs without gradients; every new example breaks the tuning.

## Why it fails

Understanding becomes operational only when one example can travel forward, create loss, send blame backward, and update the same weights.

## Correct idea

Build a two-layer network, cache its intermediate values, backpropagate every derivative, update on batches, and evaluate on unseen data.
