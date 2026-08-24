# Excavation 063 — Multi-Agent Coordination — When Should Work Be Divided?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Idempotent retries make repetition safe. A large goal can nevertheless overwhelm one agent's context and tools, raising the question of when division of work reduces risk rather than multiplying it.

Nothing in the Gatehouse of Consequences yet bears today's mathematical name. There is only the gatekeeper, the iron threshold, and one plausible action: create many agents for every problem and let them freely edit shared state.

Then the quiet test arrives: they duplicate searches, contradict one another, overwrite files, and consume more time coordinating than solving. What looked like simplicity is revealed as a missing distinction.

*The gatekeeper sketches the break before changing it:*

```text
OLD PATH:  request ──▶ create many agents for every problem… ──▶ they duplicate searches, contradict…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ we need to delegate only separable… ──▶ accountable result
```

The gatekeeper turns the iron threshold toward the light. Through the old engraving, create many agents for every problem and let them freely edit shared state, the evidence ends in the same contradiction: they duplicate searches, contradict one another, overwrite files, and consume more time coordinating than solving. A second engraving adds only the power to delegate only separable work with explicit ownership, inputs, outputs, and merge rules. Keep one accountable coordinator for the final result. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The gatekeeper circles the place where the two multi-agent coordination cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: we need to delegate only separable work with explicit ownership, inputs, outputs, and merge rules. Keep one accountable coordinator for the final result. The gatekeeper writes **Multi-Agent Coordination** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The gatekeeper places a finger over the new distinction. At once the two cases collapse and they duplicate searches, contradict one another, overwrite files, and consume more time coordinating than solving. Lifting the finger restores only this capacity: delegate only separable work with explicit ownership, inputs, outputs, and merge rules. Keep one accountable coordinator for the final result. That tiny reversible motion is the chapter's proof of necessity.

## When Should Work Be Divided

Three agents receive distinct questions and return evidence in the same schema. The coordinator resolves conflicts and alone edits the final report.

Multi-Agent Coordination earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

## Where multi-agent coordination runs out

Parallel agents amplify both capability and error. Shared resources, authority, and termination require careful control.

One unsolved mark remains on the iron threshold. None of the responsibilities inside Multi-Agent Coordination can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the iron threshold

Rebuild the multi-agent coordination scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 064](../064-observability/README.md)
