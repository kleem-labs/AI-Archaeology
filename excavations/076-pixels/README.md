# Excavation 076 — Pixels — Turning Light into Numbers

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

> **PART VIII — SEEING AND CREATING**
>
> Language was only one trace of reality. Light, space, sound, and noise demand new forms of the discoveries you already made.

Causal interventions turn interpretation into an experiment. The field system can now inspect language reasoning, but its users also need it to understand the camera's raw grid of colored light.

Inside the Glass Menagerie, every old tool is given one honest chance. The maker of seeing-machines sets the wall of illuminated tiles between the evidence and the desired answer, then tries to assign one label to the entire raw byte sequence.

The maker of seeing-machines repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: a one-pixel shift changes thousands of byte positions although the same tiger remains. The failure is stable enough to become evidence.

*The maker of seeing-machines sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: assign one label to the entire raw…
                         │
                         └── mismatch: a one-pixel shift changes thousands…

reference evidence ──▶ measured repair: preserve local spatial arrangement…
```

Across the wall of illuminated tiles, the old path and the repaired path run side by side. One carries “assign one label to the entire raw byte sequence”; the other knows how to preserve local spatial arrangement and compare nearby color measurements. When the failure—a one-pixel shift changes thousands of byte positions although the same tiger remains—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to pixels. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: preserve local spatial arrangement and compare nearby color measurements. This problem and its repair will travel under the name **Pixels**, but the name carries no knowledge the scene has not earned.

What changed on the wall of illuminated tiles can be said without symbols. Before, the method could only assign one label to the entire raw byte sequence; now it can also preserve local spatial arrangement and compare nearby color measurements. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it. The Glass Menagerie returns to the valley's geometry at a finer scale. pixels asks which nearby lights belong together, how small patterns compose into larger ones, and which transformations preserve identity while appearance changes. Seeing is measurement arranged across space.

## Turning Light into Numbers

A 2×2 grayscale patch becomes four intensities with explicit row and column positions.

## Where pixels runs out

Pixels depend on lighting, sensor, scale, and viewpoint.

The pixels repair holds, but the world asks for something it was never given. At the Glass Menagerie, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the wall of illuminated tiles

Rebuild the pixels scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 077](../077-convolution/README.md)
