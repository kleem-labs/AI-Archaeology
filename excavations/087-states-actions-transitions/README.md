# Excavation 087 — States, Actions, and Transitions

[Previous: Excavation 086](../086-rewards/README.md)

To learn from reward, what must one experience record?

Without knowing the inherited method, we might try this: Store only action and final reward.

Its hidden assumption appears in the following case: The same action helps in one situation and harms in another.

Remove that assumption and the needed repair becomes clear: Record current state, chosen action, reward, and resulting state.

## Now work a case you can see

“Move right” from left of the door succeeds; the same action beside a cliff fails because state differs.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

A state representation may omit information needed for future decisions.

This is not an unrelated warning. The construction can record current state, chosen action, reward, and resulting state. It cannot infer or control information that never enters that construction.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 088](../088-value-functions/README.md)
