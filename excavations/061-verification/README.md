# Excavation 061 — Verification — How Does the Agent Know It Succeeded?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

A state machine records what transitions are allowed and which events occurred. Reaching a state named `done` is still only a claim unless observable evidence proves the requested outcome in the outside world.

A new case arrives at the Gatehouse of Consequences, but the gatekeeper first reaches for the familiar iron threshold. Its promise is simple: trust the absence of an error message or the model’s own description of its work.

The rule survives the easy cases. The next case leaves a crack through the middle of it: the changed code compiles but breaks another case. Confidence is not evidence of the requested outcome. More confidence cannot repair information that never entered the rule.

*The gatekeeper sketches the break before changing it:*

```text
observation
    │
    ▼
[trust the absence of an error message…]
    │
    ╳  the changed code compiles but breaks…
    │
    ▼
[define success before acting, then…]
```

Two trails now cross the iron threshold. The pale trail bears the instruction “trust the absence of an error message or the model’s own description of its work.” It disappears into the observed failure: the changed code compiles but breaks another case. Confidence is not evidence of the requested outcome. The darker trail carries one additional capacity—to define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed verification mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the iron threshold is altered in exactly one way: define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state. Much later, people will call this territory **Verification**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the iron threshold. The failed path remains visible beneath the repair, because verification is easier to remember when its scar remains attached to it. The scar reads, ‘the changed code compiles but breaks another case. Confidence is not evidence of the requested outcome’; the new line exists only to keep that loss from happening again.

## How Does the Agent Know It Succeeded

For “fix CSV import,” success requires the original failing file to load, existing import tests to remain green, and malformed rows to produce the agreed error.

Verification earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

## Where verification runs out

Verification can test only stated properties. A passing check suite may omit the most important behavior.

The iron threshold answers today's question and falls silent at the next. That silence is precise: Verification was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the iron threshold

Rebuild the verification scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 062](../062-retries-idempotency/README.md)
