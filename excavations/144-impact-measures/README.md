# Excavation 144 — Impact Measures — Notice What Changed Besides the Goal

[Previous excavation](../143-uncertainty-aware-planning/README.md)

A cleaning robot succeeds but rearranges the entire house.

Our first construction is deliberately modest: Score only the requested final condition.

It works—right up to this boundary: Unnecessary irreversible changes remain invisible to the goal score.

Crossing that boundary requires one additional idea: Compare the resulting world with a reasonable baseline and penalize avoidable side effects.

Only here do we name the idea: **Impact Measures**.

## Follow one case all the way through

Cleaning the spill changes one patch of floor; moving every chair and deleting files changes unrelated state.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

A baseline can punish beneficial change or preserve an unjust status quo.

That limit is not a footnote. It is the pressure that forces the next excavation.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Human Oversight — Put Judgment at the Irreversible Edge](../145-human-oversight/README.md)
