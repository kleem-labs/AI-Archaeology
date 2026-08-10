# Excavation 136 — Long-Context Retrieval — Finding the One Clue That Matters

[Previous excavation](../135-external-memory/README.md)

A million-token archive fits, but the model still overlooks one decisive sentence.

A reasonable place to begin is: Assume information inside the window will automatically influence the answer.

Now place that proposal under pressure: Availability is not retrieval; distracting passages dominate the relevant line.

What broke tells us what the replacement must preserve: Test whether the clue can be located, ranked, and used, then combine retrieval with focused reasoning.

Only here do we name the idea: **Long-Context Retrieval**.

## Follow one case all the way through

Hide a changed contract date among repeated boilerplate and trace whether the model selects the exact clause.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

Retrieval success does not guarantee correct reasoning over what was retrieved.

That limit is not a footnote. It is the pressure that forces the next excavation.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Test-Time Compute — Thinking Longer on Harder Problems](../137-test-time-compute/README.md)
