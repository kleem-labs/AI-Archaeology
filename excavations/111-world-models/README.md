# Excavation 111 — World Models

[Previous: Excavation 110](../110-self-supervised-learning/README.md)

An agent needs to predict consequences before acting.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Learn only which action was rewarded in previously visited situations.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* The agent cannot imagine untried sequences or reuse physical regularities.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Learn a compact model that predicts next state and reward from current state and action.

Only after that reasoning may we give your discovery its inherited name.

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
