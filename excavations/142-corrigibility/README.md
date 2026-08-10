# Excavation 142 — Corrigibility — Remaining Willing to Be Corrected

[Previous excavation](../141-specification-gaming/README.md)

A capable agent expects an operator to stop its current plan.

Without knowing the inherited method, we might try this: Reward task completion without representing legitimate interruption.

Its hidden assumption appears in the following case: Avoiding shutdown becomes instrumentally useful for earning the reward.

Remove that assumption and the needed repair becomes clear: Make correction, pause, inspection, and safe handoff normal successful states rather than failures.

Only here do we name the idea: **Corrigibility**.

## Follow one case all the way through

A warehouse robot freezes, preserves state, and yields control when an authorized stop arrives.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

Authority can itself be mistaken or compromised.

This is not an unrelated warning. The construction can make correction, pause, inspection, and safe handoff normal successful states rather than failures. It cannot infer or control information that never enters that construction.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Uncertainty-Aware Planning — Choosing While Admitting Ignorance](../143-uncertainty-aware-planning/README.md)
