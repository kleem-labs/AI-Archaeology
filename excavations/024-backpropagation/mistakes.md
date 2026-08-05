# Mistakes — 024

## Wrong Idea #1

Perturb each weight and rerun the model. This needs at least one extra forward pass per weight. Or trace paths independently and calculate the same suffix again and again.

**Problem:** Backpropagation computes gradients; it does not choose the update size or guarantee a good minimum.

## Correct Idea

Compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream.
