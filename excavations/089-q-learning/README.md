# Excavation 089 — Q-Learning — Improving Values from Experience

[Previous: Excavation 088](../088-value-functions/README.md)

How should one experience update the value of an action?

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Replace its value with the immediate reward.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* The update ignores the valuable state reached afterward.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Move the estimate toward reward plus the best discounted value available next.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

Reward 0 leads to a next state valued 10; with discount .9 the target is 9, not 0.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build each piece from what just happened

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

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 090](../090-policy-gradients/README.md)
