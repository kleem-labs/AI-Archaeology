# Excavation 138 — Search and Verification — Separate Proposing from Checking

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Scientific self-improvement and oversight

Test-time compute lets hard problems receive more attempts. More attempts also produce more plausible mistakes, so proposing candidate paths must be separated from checking them.

A new case arrives at the Academy of Trials. Nothing yet demands a new invention, so the experimentalist uses the sealed evidence ledger to ask the same generator to confidently approve its own first answer.

This is precisely the kind of shortcut a careful builder should try first. The instruction to ask the same generator to confidently approve its own first answer preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: the error that shaped the proposal also shapes its self-justification.

The counterexample separates two questions that the attempt to ask the same generator to confidently approve its own first answer had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the sealed evidence ledger fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now generate diverse candidates, check them with independent evidence, and keep only paths that survive. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Search and Verification**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Separate Proposing from Checking

Propose five programs for a specification and run hidden tests before selecting one.

## Where search and verification runs out

A weak verifier rewards solutions that exploit its blind spots.

At the Academy of Trials, the experimentalist leaves a blank beneath the new mark. Search and Verification has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the sealed evidence ledger

Rebuild the search and verification scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [The wrong ideas worth preserving](mistakes.md); [Diagram and dependency path](diagram.md); [Invention exercises](exercises.md); [References and reading trail](references.md); and [Visual asset brief](images/README.md).

[Next: Process Supervision — Rewarding the Path, Not Only the Answer](../139-process-supervision/README.md)
