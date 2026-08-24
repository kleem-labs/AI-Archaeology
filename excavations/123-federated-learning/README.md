# Excavation 123 — Federated Learning

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality)
>
> **Applied territory:** Continual learning, reasoning, and research

Differential privacy limits the observable influence of one record. Hospitals and devices may be unwilling or legally unable to centralize their raw data even when collective learning would help everyone.

Night gathers around the Hall of Possible Worlds. Under the light of the table of mirrored maps, the keeper of unfinished questions refuses to invent prematurely and begins with the plain rule: upload every user record to one server.

Then the quiet test arrives: central collection increases privacy and governance risk. What looked like simplicity is revealed as a missing distinction.

*The keeper of unfinished questions sketches the break before changing it:*

```text
observation
    │
    ▼
[upload every user record to one server]
    │
    ╳  central collection increases privacy…
    │
    ▼
[we need to send model updates to…]
```

The keeper of unfinished questions turns the table of mirrored maps toward the light. Through the old engraving, upload every user record to one server, the evidence ends in the same contradiction: central collection increases privacy and governance risk. A second engraving adds only the power to send model updates to devices, train locally, aggregate protected updates, and return a shared model. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The keeper of unfinished questions circles the place where the two federated learning cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: we need to send model updates to devices, train locally, aggregate protected updates, and return a shared model. The keeper of unfinished questions writes **Federated Learning** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The keeper of unfinished questions places a finger over the new distinction. At once the two cases collapse and central collection increases privacy and governance risk. Lifting the finger restores only this capacity: send model updates to devices, train locally, aggregate protected updates, and return a shared model. That tiny reversible motion is the chapter's proof of necessity.

<!-- memory-film-v1:start -->
> **Memory realm 10 of 18 — [Hall of Possible Worlds](../../MEMORY_PALACE.md#realm-10)**
>
> **The question carried into this chamber:** What fails if we upload every user record to one server?

## When the chamber changes

Before leaving Federated Learning, replay the discovery as motion rather than as a definition.

First hold the failed picture still: The wheel follows the tempting path—upload every user record to one server. Then the evidence answers: central collection increases privacy and governance risk.

Now let the chamber move: The keeper of unfinished questions changes one moving part. The wheel can now send model updates to devices, train locally, aggregate protected updates, and return a shared model.

The object that should remain after the terminology disappears is **the federated learning wheel mounted on the table of mirrored maps**.

> **Memory seal — Federated Learning**
>
> Federated Learning keeps the missing power: send model updates to devices, train locally, aggregate protected updates, and return a shared model.

Give the idea a bodily path: Touch the federated learning wheel in imagination: close one fist around the lost information, then open it as the repair restores that information.
<!-- memory-film-v1:end -->

## Understanding federated learning

Phones compute keyboard gradients locally; the server receives an aggregate, not typed messages.

## Where federated learning runs out

Updates can still leak information and devices are unreliable or biased.

One unsolved mark remains on the table of mirrored maps. None of the responsibilities inside Federated Learning can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the table of mirrored maps

Rebuild the federated learning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 124](../124-adversarial-robustness/README.md)
