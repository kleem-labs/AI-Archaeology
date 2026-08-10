# Excavation 089 — Q-Learning — Improving Values from Experience

[Previous: Excavation 088](../088-value-functions/README.md)

How should one experience update the value of an action?

Our first construction is deliberately modest: Replace its value with the immediate reward.

It works—right up to this boundary: The update ignores the valuable state reached afterward.

Crossing that boundary requires one additional idea: Move the estimate toward reward plus the best discounted value available next.

## Now work a case you can see

Reward 0 leads to a next state valued 10; with discount .9 the target is 9, not 0.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build each piece from what just happened


A rescue robot reaches a fork. Moving left finds one injured hiker now, worth immediate reward 1, and leads to a state whose best known continuation is worth 5. If future reward is discounted by 0.9, the experience proposes `1 + 0.9×5 = 5.5` as the new target value for choosing left. The robot is not claiming certainty; it is joining what happened now with its best current estimate of what can follow.

- The immediate reward is what happened now.
- The largest next-state Q value represents the best continuation currently known.
- Discount γ reduces distant evidence and keeps unending sums bounded.
- Adding immediate and discounted future reward creates the target the old estimate moves toward.

Only now can we compress the procedure:

$$
\text{target}=r+\gamma\max_{a^\prime}Q(s^\prime,a^\prime)
$$

## Where your new idea still breaks

Maximization can overestimate noisy actions and offline data limits safe exploration.

Why does the boundary remain? Our new machinery only knows how to move the estimate toward reward plus the best discounted value available next. Solving that problem does not automatically solve every decision built on top of it.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 090](../090-policy-gradients/README.md)
