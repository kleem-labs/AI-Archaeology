# Excavation 150 — A Bounded Self-Improving System — Close the Research Loop

[Previous excavation](../149-predeployment-evaluations/README.md)

Can a system improve its own components without quietly expanding its power or rewriting success?

Before inheriting a technique, make the first decision yourself. Let every measured gain replace the current system automatically.

For a moment, the idea appears sufficient. Then reality supplies the case it cannot explain: Contaminated tests, reward hacks, or one lucky run can promote a worse and less controllable successor.

The failure tells you what the repair must accomplish. Separate proposal, sandboxed experiment, reproducibility, independent evaluation, impact review, authorization, staged release, and rollback.

Only now have you earned the chapter's name: **A Bounded Self-Improving System**.

## Follow one case all the way through

A tokenizer change advances only after repeated clean tests, safety checks, signed approval, a small canary release, and monitored rollback criteria.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

The loop remains only as wise as its objectives, evidence, boundaries, and accountable humans.

That limit is not a footnote. It is the pressure that forces the next excavation.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

The circle is closed, but not finished: every future discovery must pass through the same bounded loop.
