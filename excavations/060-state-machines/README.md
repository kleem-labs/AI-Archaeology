# Excavation 060 — State Machines — Knowing What Has Actually Happened

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Agents and reliable action

Memory carries chosen information across contexts. Remembering that an email was intended does not establish that it was sent; real workflows need an authoritative account of which events actually changed state.

At the Gatehouse of Consequences, the gatekeeper meets the next case beside the iron threshold. The nearest idea is also the most reasonable one: let the conversation prose serve as the workflow state.

The attraction of this attempt is easy to see. To let the conversation prose serve as the workflow state reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: the model says “refund completed” after merely drafting it, or issues it twice after losing track of an earlier tool result.

The contradiction matters because it identifies a structural loss in the instruction to let the conversation prose serve as the workflow state, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The iron threshold will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **State Machines**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## Knowing What Has Actually Happened

A refund moves requested → approved only with an approval record, then approved → issued only with a payment transaction ID. A sentence alone changes nothing.

State Machines earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

## Where state machines runs out

Real workflows have exceptions and concurrent events. State machines need recovery paths and authoritative external records.

At the Gatehouse of Consequences, the gatekeeper leaves a blank beneath the new mark. State Machines has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the iron threshold

Rebuild the state machines scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 061](../061-verification/README.md)
