# Excavation 139 — Process Supervision — Rewarding the Path, Not Only the Answer

[Previous excavation](../138-search-and-verification/README.md)

Two solutions reach the correct number; one used invalid reasoning by luck.

Our first construction is deliberately modest: Reward only whether the final answer matches.

It works—right up to this boundary: Lucky shortcuts receive the same credit as reliable reasoning.

Crossing that boundary requires one additional idea: Evaluate checkable intermediate claims and train the system to prefer valid paths.

Only here do we name the idea: **Process Supervision**.

## Follow one case all the way through

Mark each algebraic transformation valid or invalid before judging the final result.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

Human process labels are expensive and can enforce one style rather than truth.

Why does the boundary remain? Our new machinery only knows how to evaluate checkable intermediate claims and train the system to prefer valid paths. Solving that problem does not automatically solve every decision built on top of it.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Reward Hacking — When the Score Replaces the Goal](../140-reward-hacking/README.md)
