# Excavation 088 — Value — Estimating Future Consequences

[Previous: Excavation 087](../087-states-actions-transitions/README.md)

Immediate reward cannot distinguish a step toward a distant goal from a dead end.

At first, the simplest answer is tempting: Choose the action with the largest reward right now.

But the simplicity has discarded something important: A small immediate treat can prevent reaching a larger later reward.

The missing information determines the next move: Estimate the future reward expected from a state or state-action pair.

## Now work a case you can see

One path gives 1 now; another gives 0 now and 10 next. Future value makes the second preferable.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

Value estimates inherit errors from limited experience.

The reason is visible in the procedure. It knows how to estimate the future reward expected from a state or state-action pair. The limitation above asks for another judgment, and no part of the procedure makes that judgment.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 089](../089-q-learning/README.md)
