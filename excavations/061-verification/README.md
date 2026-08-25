# Excavation 061 — Verification — How Does the Agent Know It Succeeded?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Agents and reliable action

A state machine records what transitions are allowed and which events occurred. Reaching a state named `done` is still only a claim unless observable evidence proves the requested outcome in the outside world.

The previous discovery reaches the Gatehouse of Consequences carrying one unfinished problem. Beside the iron threshold, the gatekeeper first tries to trust the absence of an error message or the model’s own description of its work.

There is good reason to begin this way. If we trust the absence of an error message or the model’s own description of its work, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: the changed code compiles but breaks another case. Confidence is not evidence of the requested outcome.

This failure cannot be repaired by performing the instruction to trust the absence of an error message or the model’s own description of its work more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the iron threshold; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Verification**. The name is simply a handle for the distinction already reconstructed.

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
