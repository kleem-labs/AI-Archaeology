# Excavation 064 — Observability — Seeing Why an Agent Failed

<!-- book-prose-v2 -->

Multi-agent coordination divides work and introduces new boundaries, shared resources, and failure modes. When the result is wrong, the team needs enough trace to locate which assumption, handoff, or tool effect failed.

If the old idea can be stretched one step farther, we should log only the final response, or log every hidden detail without structure.

If the proposal works on every relevant case, observability is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

Now keep that rule fixed and let the difficult case enter: the first gives no diagnosis; the second creates an unreadable, expensive, privacy-sensitive transcript.

Nothing magical creates observability. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content.

This boundary between the failed rule and its repair is the subject later work calls **Observability**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize observability; try to break it by subtraction. Remove the part that knows how to record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content, leaving only the attempt to log only the final response, or log every hidden detail without structure. What returns is not a vague weakness but the original contradiction: the first gives no diagnosis; the second creates an unreadable, expensive, privacy-sensitive transcript. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to log only the final response, or log every hidden detail without structure receives the same test as the rule to record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content. Their different outcomes reveal what observability contributes without asking the reader to trust historical convention.

## Seeing Why an Agent Failed

A trace shows retrieval returned an outdated policy, the planner accepted it, and verification checked format but not date. The repair can now target the real failure.

Observability earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

Hold the setting, evidence, and desired outcome fixed while testing observability. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

## Where observability runs out

Logs describe what instrumentation captured. Missing fields, privacy limits, and misleading metrics still constrain diagnosis.

This is where observability runs out for a causal reason. We gave it enough structure to record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

## Take observability to the workbench

A mathematical story about observability earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running observability, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the observability result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 065](../065-bounded-autonomy/README.md)
