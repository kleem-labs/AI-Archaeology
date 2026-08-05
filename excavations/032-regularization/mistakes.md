# Mistakes — 032

## Wrong Idea #1

Forbid complexity by making the model too small; it may lose real structure too. Stop training at an arbitrary time without observing unseen performance.

## Why it fails

When several explanations fit, prefer one that does not require extreme or brittle machinery.

## Correct idea

Add a cost for large weights, remove random paths during training, or stop when validation performance stops improving.
