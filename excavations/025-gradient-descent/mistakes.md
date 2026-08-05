# Mistakes — 025

## Wrong Idea #1

Jump directly opposite the gradient with no step control; the model may overshoot and diverge. Take microscopic steps; learning may take forever. Trust one example; its noisy advice can undo another.

**Problem:** Gradient descent finds a reachable low region, not necessarily the unique best explanation. Data, initialization, scale, and step size all shape the journey.

## Correct Idea

Move every parameter a controlled distance opposite its gradient, repeat on batches of examples, and watch loss rather than assuming progress.
