# Excavation 138 — Search and Verification — Separate Proposing from Checking

Test-time compute lets hard problems receive more attempts. More attempts also produce more plausible mistakes, so proposing candidate paths must be separated from checking them.

Perhaps we ask the same generator to confidently approve its own first answer.

That confidence lasts only until the error that shaped the proposal also shapes its self-justification.

So we generate diverse candidates, check them with independent evidence, and keep only paths that survive.

## Let the case decide

Propose five programs for a specification and run hidden tests before selecting one.

## The boundary of the discovery

A weak verifier rewards solutions that exploit its blind spots.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Process Supervision — Rewarding the Path, Not Only the Answer](../139-process-supervision/README.md)
