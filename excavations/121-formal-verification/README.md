# Excavation 121 — Formal Verification

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Continual learning, reasoning, and research

Program synthesis turns examples into candidate procedures. Tests inspect selected cases; a safety-critical system may need proof that a property holds for every input permitted by the specification.

The previous discovery reaches the Hall of Possible Worlds carrying one unfinished problem. Beside the table of mirrored maps, the keeper of unfinished questions first tries to add more random tests and call the property proven.

There is good reason to begin this way. If we add more random tests and call the property proven, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: an untested edge case can remain.

This failure cannot be repaired by performing the instruction to add more random tests and call the property proven more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the table of mirrored maps; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to state assumptions and desired properties formally, then prove or mechanically check that every transition preserves them. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Formal Verification**. The name is simply a handle for the distinction already reconstructed.

## Understanding formal verification

Prove a refund state machine can issue at most one payment per idempotency key.

## Where formal verification runs out

Proof covers the formal model, which may omit real-world behavior.

The table of mirrored maps answers today's question and falls silent at the next. That silence is precise: Formal Verification was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the table of mirrored maps

Rebuild the formal verification scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 122](../122-differential-privacy/README.md)
