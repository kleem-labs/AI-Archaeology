# Excavation 066 — Feedback Loops

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality)
>
> **Applied territory:** Learning in the world and interpretability

> **PART VII — LEARNING AFTER DEPLOYMENT**
>
> The laboratory door opens onto a changing world. Now the system influences the very evidence from which it learns.

The field assistant is now bounded, observable, and deployed. Its recommendations change what people see and choose, so today's behavior alters the data that will be treated as evidence tomorrow.

The weathered observation slate at the Living Watchgarden still carries the marks of the previous discovery. The field naturalist follows them as far as they seem willing to go: treat every click as independent evidence of natural preference.

For a moment the mark looks complete. Then the evidence refuses to fit: show one song repeatedly; its extra clicks now appear to prove it deserved repetition. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The field naturalist sketches the break before changing it:*

```text
observation
    │
    ▼
[treat every click as independent…]
    │
    ╳  show one song repeatedly; its extra…
    │
    ▼
[record how the system influenced each…]
```

The field naturalist lays two translucent sheets over the weathered observation slate. The first is inscribed, “treat every click as independent evidence of natural preference.” Its path ends where show one song repeatedly; its extra clicks now appear to prove it deserved repetition. The second receives the same evidence but is allowed to record how the system influenced each observation and evaluate outcomes against a control or exploration policy. Held to the light, the sheets separate at exactly one decision.

No one reaches for a feedback loops formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The field naturalist changes only that one responsibility: record how the system influenced each observation and evaluate outcomes against a control or exploration policy. When the ink dries, the name **Feedback Loops** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because show one song repeatedly; its extra clicks now appear to prove it deserved repetition, while the other can record how the system influenced each observation and evaluate outcomes against a control or exploration policy. That fork—not the vocabulary—is where feedback loops lives. The Living Watchgarden studies change itself. Under feedback loops, a remembered baseline makes movement visible, probability keeps untried futures alive, and causal comparison asks which action—not merely which coincidence—bent the world. The observer now stands inside the loop being measured.

## Understanding feedback loops

Two equal songs begin with ten listeners each. The agent promotes A to ninety more people; A receives more clicks because it received more chances, not necessarily because it was better.

## Where feedback loops runs out

Feedback can create self-fulfilling popularity and erase unexposed alternatives.

At the Living Watchgarden, the field naturalist leaves a blank beneath the new mark. Feedback Loops has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the weathered observation slate

Rebuild the feedback loops scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 067](../067-online-learning/README.md)
