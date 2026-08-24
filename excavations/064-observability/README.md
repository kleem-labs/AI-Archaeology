# Excavation 064 — Observability — Seeing Why an Agent Failed

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Multi-agent coordination divides work and introduces new boundaries, shared resources, and failure modes. When the result is wrong, the team needs enough trace to locate which assumption, handoff, or tool effect failed.

At the Gatehouse of Consequences, the gatekeeper returns to the iron threshold. Yesterday's instrument still lies open, so the first move asks for no new magic: log only the final response, or log every hidden detail without structure.

The gatekeeper repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: the first gives no diagnosis; the second creates an unreadable, expensive, privacy-sensitive transcript. The failure is stable enough to become evidence.

*The gatekeeper sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ log only the final response, or log… ──▶ blurred: the first gives no diagnosis; the…
      │
      └── new lens ──▶ record structured events for… ──▶ distinction survives
```

Across the iron threshold, the old path and the repaired path run side by side. One carries “log only the final response, or log every hidden detail without structure”; the other knows how to record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content. When the failure—the first gives no diagnosis; the second creates an unreadable, expensive, privacy-sensitive transcript—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to observability. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content. This problem and its repair will travel under the name **Observability**, but the name carries no knowledge the scene has not earned.

What changed on the iron threshold can be said without symbols. Before, the method could only log only the final response, or log every hidden detail without structure; now it can also record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

## Seeing Why an Agent Failed

A trace shows retrieval returned an outdated policy, the planner accepted it, and verification checked format but not date. The repair can now target the real failure.

Observability earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

## Where observability runs out

Logs describe what instrumentation captured. Missing fields, privacy limits, and misleading metrics still constrain diagnosis.

The observability repair holds, but the world asks for something it was never given. At the Gatehouse of Consequences, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the iron threshold

Rebuild the observability scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 065](../065-bounded-autonomy/README.md)
