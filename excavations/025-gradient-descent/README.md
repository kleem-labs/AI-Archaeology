# Excavation 025 — Gradient Descent — Teaching a Tiny Network

[Previous excavation](../024-backpropagation/README.md)

We can now assign blame to every weight. The network still needs a disciplined way to turn those sensitivities into repeated improvement.

The first solution that suggests itself is this: Jump directly opposite the gradient with no step control; the model may overshoot and diverge. Take microscopic steps; learning may take forever. Trust one example; its noisy advice can undo another.

The failure gives us a precise requirement: Move every parameter a controlled distance opposite its gradient, repeat on batches of examples, and watch loss rather than assuming progress.

## From procedure to notation

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

## Build each piece from what just happened

Return to the tiger alarm's stripe dial. It is 8; verified encounters suggest 3; the squared mistake is 25; and the local uphill sensitivity is 10. Moving the full ten units lands at −2, equally far from the target on the other side. Direction alone has not taught us distance. Taking one tenth of the proposed correction moves the dial to 7 and lowers the mistake to 16. That chosen fraction is the learning rate.

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

## Carry the idea back into the world

Descending in fog requires frequent local slope readings and careful steps. Momentum and adaptive methods are better walking strategies, not different destinations.

## Limits

Gradient descent finds a reachable low region, not necessarily the unique best explanation. Data, initialization, scale, and step size all shape the journey.

The boundary follows from the mechanism itself. We designed it to move every parameter a controlled distance opposite its gradient, repeat on batches of examples, and watch loss rather than assuming progress. That operation solves the failure we had reached, but it contains no step that answers the additional problem above.

## Enter the laboratory

Build the wrong idea first, break it, then use [Pure Python → NumPy → PyTorch](implementation/README.md).

The [Gradient Step-Size Field Lab](../../labs/04_gradient_lab.py) lets you watch a cautious step learn, a useful step learn faster, and an oversized step bounce forever.

## Test what you believe

Use the [invention exercises](exercises.md), not as a quiz but as a request to rediscover the idea.

## What this discovery now makes possible

- [Mistakes and failed ideas](mistakes.md)
- [Mermaid and ASCII diagram](diagram.md)
- [References](references.md)
- [Visual asset brief](images/README.md)

The limitation in this excavation creates the need for the next one.
