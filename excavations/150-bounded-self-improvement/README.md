# Excavation 150 — A Bounded Self-Improving System — Close the Research Loop

[Previous excavation](../149-predeployment-evaluations/README.md)

Can a system improve its own components without quietly expanding its power or rewriting success?

The first solution that suggests itself is this: Let every measured gain replace the current system automatically.

The idea survives only until we test it against reality: Contaminated tests, reward hacks, or one lucky run can promote a worse and less controllable successor.

The failure gives us a precise requirement: Separate proposal, sandboxed experiment, reproducibility, independent evaluation, impact review, authorization, staged release, and rollback.

Only here do we name the idea: **A Bounded Self-Improving System**.

## Follow one case all the way through

A tokenizer change advances only after repeated clean tests, safety checks, signed approval, a small canary release, and monitored rollback criteria.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

The loop remains only as wise as its objectives, evidence, boundaries, and accountable humans.

The boundary follows from the mechanism itself. We designed it to separate proposal, sandboxed experiment, reproducibility, independent evaluation, impact review, authorization, staged release, and rollback. That operation solves the failure we had reached, but it contains no step that answers the additional problem above.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

The circle is closed, but not finished: every future discovery must pass through the same bounded loop.
