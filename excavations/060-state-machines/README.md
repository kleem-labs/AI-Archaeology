# Excavation 060 — State Machines — Knowing What Has Actually Happened

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Memory carries chosen information across contexts. Remembering that an email was intended does not establish that it was sent; real workflows need an authoritative account of which events actually changed state.

Inside the Gatehouse of Consequences, every old tool is given one honest chance. The gatekeeper sets the iron threshold between the evidence and the desired answer, then tries to let the conversation prose serve as the workflow state.

For a moment the mark looks complete. Then the evidence refuses to fit: the model says “refund completed” after merely drafting it, or issues it twice after losing track of an earlier tool result. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The gatekeeper sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: let the conversation prose serve as…
                         │
                         └── mismatch: the model says “refund completed”…

reference evidence ──▶ measured repair: represent allowed states and…
```

The gatekeeper lays two translucent sheets over the iron threshold. The first is inscribed, “let the conversation prose serve as the workflow state.” Its path ends where the model says “refund completed” after merely drafting it, or issues it twice after losing track of an earlier tool result. The second receives the same evidence but is allowed to represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system. Held to the light, the sheets separate at exactly one decision.

No one reaches for a state machines formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The gatekeeper changes only that one responsibility: represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system. When the ink dries, the name **State Machines** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The iron threshold keeps both histories. Its older mark still says, ‘let the conversation prose serve as the workflow state’; beside it, the newer mark says, ‘represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system.’ The distance between those sentences is the exact shape of state machines: no larger than the failure required, and no smaller than reality permits.

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
