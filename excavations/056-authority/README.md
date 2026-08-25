# Excavation 056 — Authority — What Is the Agent Allowed to Do?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Agents and reliable action

> **PART VI — TRUSTING AN ACTING MACHINE**
>
> The model no longer merely answers. Its words can cause actions, and every action creates questions of authority and proof.

Tools let language cause external effects. The moment an answer can act, capability must be separated from permission: what may this agent do without asking again?

At the Gatehouse of Consequences, the gatekeeper meets the next case beside the iron threshold. The nearest idea is also the most reasonable one: give every available tool to the model and treat user intent as unlimited permission.

The attraction of this attempt is easy to see. To give every available tool to the model and treat user intent as unlimited permission reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: ask for an itinerary and watch the agent buy a nonrefundable ticket. The plan was requested; the purchase was not.

The contradiction matters because it identifies a structural loss in the instruction to give every available tool to the model and treat user intent as unlimited permission, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The iron threshold will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must separate capability from authority. Give the smallest permissions needed, attach scope and limits, and require confirmation before consequential actions. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Authority**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## What Is the Agent Allowed to Do

The agent may search flights and hold a draft itinerary. Purchasing requires a new explicit approval containing price, destination, and dates.

Authority earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

## Where authority runs out

Permission checks do not prove the chosen action is wise. They bound what can happen while judgment and verification remain separate.

A final test reaches beyond the new instrument. It does not refute Authority; it reveals the edge of what was constructed. The gatekeeper carries that edge into the following room.

## Return to the iron threshold

Rebuild the authority scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 057](../057-prompt-injection/README.md)
