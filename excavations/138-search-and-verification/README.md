# Excavation 138 — Search and Verification — Separate Proposing from Checking

[Previous excavation](../137-test-time-compute/README.md)

The first proposed solution to a puzzle is plausible but wrong.

Before inheriting a technique, make the first decision yourself. Ask the same generator to confidently approve its own first answer.

For a moment, the idea appears sufficient. Then reality supplies the case it cannot explain: The error that shaped the proposal also shapes its self-justification.

The failure tells you what the repair must accomplish. Generate diverse candidates, check them with independent evidence, and keep only paths that survive.

Only now have you earned the chapter's name: **Search and Verification**.

## Follow one case all the way through

Propose five programs for a specification and run hidden tests before selecting one.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

A weak verifier rewards solutions that exploit its blind spots.

That limit is not a footnote. It is the pressure that forces the next excavation.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Process Supervision — Rewarding the Path, Not Only the Answer](../139-process-supervision/README.md)
