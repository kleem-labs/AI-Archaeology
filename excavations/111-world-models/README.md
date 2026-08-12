# Excavation 111 — World Models

Self-supervision extracts lessons from unlabeled observations. An acting system needs more than representations: before choosing, it must imagine how the world may change after each possible action.

At first we learn only which action was rewarded in previously visited situations.

Yet the agent cannot imagine untried sequences or reuse physical regularities.

We need to learn a compact model that predicts next state and reward from current state and action.

## Let the case decide

From ball position and push direction, predict where the ball will move before choosing the push.

## The boundary of the discovery

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
