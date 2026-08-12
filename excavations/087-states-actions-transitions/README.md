# Excavation 087 — States, Actions, and Transitions

A reward says how an outcome turned out. To learn from it, the agent must preserve the situation it occupied, the action it chose, and the situation that followed.

At first we store only action and final reward.

The trouble appears immediately: the same action helps in one situation and harms in another.

We need to record current state, chosen action, reward, and resulting state.

## Let the case decide

“Move right” from left of the door succeeds; the same action beside a cliff fails because state differs.

## The boundary of the discovery

A state representation may omit information needed for future decisions.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 088](../088-value-functions/README.md)
