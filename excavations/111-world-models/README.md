# Excavation 111 — World Models

[Previous: Excavation 110](../110-self-supervised-learning/README.md)

An agent needs to predict consequences before acting.

A reasonable place to begin is: Learn only which action was rewarded in previously visited situations.

Now place that proposal under pressure: The agent cannot imagine untried sequences or reuse physical regularities.

What broke tells us what the replacement must preserve: Learn a compact model that predicts next state and reward from current state and action.

## Now work a case you can see

From ball position and push direction, predict where the ball will move before choosing the push.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Model errors compound during long imagined rollouts.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 112](../112-causal-inference/README.md)
