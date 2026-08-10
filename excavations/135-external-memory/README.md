# Excavation 135 — External Memory — Remembering Beyond the Context Window

[Previous excavation](../134-sparse-attention/README.md)

An agent must remember a project after the current prompt disappears.

The first solution that suggests itself is this: Append every past event to every future prompt.

The idea survives only until we test it against reality: Cost grows forever and important facts drown in irrelevant history.

The failure gives us a precise requirement: Write selected facts to addressed storage, retrieve by present need, and preserve provenance and update rules.

Only here do we name the idea: **External Memory**.

## Follow one case all the way through

Store the user's chosen unit system once, retrieve it for calculations, and retain when and why it was recorded.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

Bad memories can persist longer than the conversations that created them.

That limit is not a footnote. It is the pressure that forces the next excavation.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Long-Context Retrieval — Finding the One Clue That Matters](../136-long-context-retrieval/README.md)
