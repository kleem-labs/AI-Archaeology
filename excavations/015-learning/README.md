# Excavation 015 — How a Dead Brain Learns

[Previous: Layer Normalization](../014-layer-normalization/README.md)

Build a complete Transformer with embeddings, attention, feed-forward networks, residual paths, and normalization. Ask it a question.

It answers nonsense.

The instrument exists; the skill does not. Every learned weight began as an arbitrary number.

## Memorization fails

Show it:

```text
cat eats fish
```

It can store that sequence, but “dog eats ___” exposes the limitation. We need a process that improves on examples and generalizes beyond exact memories.

Prediction provides a relentless exercise. Pause after “The cat sat on the ___.” To succeed consistently, the model must use grammar, context, relationships, and facts. Prediction is not proof of complete understanding, but it puts pressure on useful internal structure.

## “Wrong” is not precise enough

An arrow landing ten centimeters from a target is different from one landing ten meters away. Learning needs a number saying how bad the current prediction is. We call that number **loss**.

Now imagine loss as height in an enormous landscape. Every model weight is one direction in that landscape. Training wants to move downhill.

## Random wiggling fails

Change one weight, run the model again, and keep the change if loss improves. With billions of weights, trying directions one at a time is hopeless.

Instead ask, for each weight:

> If I move this number a tiny amount, how does the loss change?

That question—not a symbol—is the derivative. It measures sensitivity. All those sensitivities together form the gradient, a local direction of steepest increase. To reduce loss, move a small step the other way.

Only now does the update rule earn its place:

## Why Every Term Must Exist Before the Equation

- **θ** is the current collection of learnable weights.
- **L** is the measured prediction failure.
- **∇L** collects how increasing each weight would increase loss.
- The minus sign reverses that uphill direction.
- **η** controls step size because direction alone does not say how far to move.
- The arrow means replace the old weights with the improved ones.


$\theta$ is the current state of the weights, $\nabla L$ is a vector of advised change, and $\eta$ controls how large a step to take.

Only now can we compress that reasoning:

$$
\theta\leftarrow\theta-\eta\nabla L
$$


## How does blame reach billions of weights?

Trace the prediction backward through the operations. Ask how much each intermediate result contributed to the error, then how much each earlier result contributed to that. Backpropagation is organized blame assignment through the chain of computations.

Each training step is therefore:

```text
predict → measure loss → trace responsibility backward → nudge weights
```

Repeated over enormous amounts of text, small corrections reshape the entire web.

## Challenge

Explain derivative, gradient, and backpropagation without using their formulas: sensitivity, direction, and blame assignment should remain distinct.

## What the next excavation needs

Why should next-token prediction produce grammar, facts, abstraction, or reasoning at all? The answer lies behind the visible words.

[Next: Emergence](../016-emergence/README.md)
