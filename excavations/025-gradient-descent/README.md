# Excavation 025 — Gradient Descent — Teaching a Tiny Network

[Previous excavation](../024-backpropagation/README.md)

## Problem

We can now assign blame to every weight. The network still needs a disciplined way to turn those sensitivities into repeated improvement.

## Naive Attempt

Jump directly opposite the gradient with no step control; the model may overshoot and diverge. Take microscopic steps; learning may take forever. Trust one example; its noisy advice can undo another.

## Why It Fails

The attempt either throws away uncertainty, measures the wrong thing, or repeats work that the next step must preserve. We need a procedure whose parts answer the failure directly.

## Better Attempt

Move every parameter a controlled distance opposite its gradient, repeat on batches of examples, and watch loss rather than assuming progress.

## Why It Still Fails

The verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.

## Key Insight

**Move every parameter a controlled distance opposite its gradient, repeat on batches of examples, and watch loss rather than assuming progress.**

## Mathematics Emerges

## Build Every Piece from the Concrete Example

Forget θ for a moment. Our tiny model has one adjustable weight, currently **8**. We want it to become **3**, so its mistake is (weight − 3)². At weight 8, the mistake is 25.

A tiny upward nudge shows a local sensitivity of 10. In ordinary language: increasing the weight a little makes the mistake rise about ten times as much. Ten therefore points uphill. To reduce the mistake, we move the other way. That creates the minus sign.

Should we move the entire ten units?

~~~text
8 - 10 = -2
mistake at -2 = (-2 - 3)² = 25
~~~

We jumped across the valley and learned nothing. So direction is not enough. We need a knob controlling how much of the proposed movement we trust.

Try taking one tenth:

~~~text
suggested uphill direction = 10
reverse it                 = -10
take one tenth             = -1
new weight                 = 8 - 1 = 7
new mistake                = (7 - 3)² = 16
~~~

The mistake fell from 25 to 16. That one tenth is the **learning rate**, later written η. It is simply a caution knob:

- η = 1 takes the entire proposed movement;
- η = 0.1 takes one tenth;
- η = 0.01 takes one hundredth.

Too large can jump over the valley. Too small moves safely but slowly.

### Give Short Names Only After We Know the Pieces

- **θ_t** packages the current weights; our tiny example has only 8.
- **L** is the mistake measure; here it is (weight − 3)².
- **∇_θL** packages local sensitivities; our example has only 10.
- The minus sign reverses the uphill direction.
- **η** is the chosen fraction of the correction; here it is 0.1.
- **t** means before this correction; **t+1** means after it.

Substitute real values before compact symbols:

~~~text
next weight = current weight - learning rate × uphill sensitivity
            = 8              - 0.1           × 10
            = 7
~~~

Only now can we compress the same procedure:

$$
\theta_{t+1}=\theta_t-\eta\nabla_\theta L
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

## Real-World Analogy

Descending in fog requires frequent local slope readings and careful steps. Momentum and adaptive methods are better walking strategies, not different destinations.

## Limits

Gradient descent finds a reachable low region, not necessarily the unique best explanation. Data, initialization, scale, and step size all shape the journey.

## Implementation

Build the wrong idea first, break it, then use [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises

Use the [invention exercises](exercises.md), not as a quiz but as a request to rediscover the idea.

## Connections

- [Mistakes and failed ideas](mistakes.md)
- [Mermaid and ASCII diagram](diagram.md)
- [References](references.md)
- [Visual asset brief](images/README.md)

The limitation in this excavation creates the need for the next one.
