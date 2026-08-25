# Excavation 120 — Program Synthesis

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality)
>
> **Applied territory:** Continual learning, reasoning, and research

Graph neural networks propagate learned messages through relational structure. Some tasks demand more than one answer: they demand a reusable procedure that maps every allowed input to an output.

At the Hall of Possible Worlds, the keeper of unfinished questions meets the next case beside the table of mirrored maps. The nearest idea is also the most reasonable one: memorize the provided input-output pairs.

The attraction of this attempt is easy to see. To memorize the provided input-output pairs reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: a new input exposes the absence of an underlying algorithm.

The contradiction matters because it identifies a structural loss in the instruction to memorize the provided input-output pairs, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The table of mirrored maps will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must search or generate candidate programs, execute them, and keep those satisfying examples and constraints. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Program Synthesis**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## Understanding program synthesis

Examples 2→4 and 3→6 suggest multiply by two; testing 5 distinguishes it from memorized lookup.

## Where program synthesis runs out

Finite examples rarely identify one unique intended program.

At the Hall of Possible Worlds, the keeper of unfinished questions leaves a blank beneath the new mark. Program Synthesis has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the table of mirrored maps

Rebuild the program synthesis scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 121](../121-formal-verification/README.md)
