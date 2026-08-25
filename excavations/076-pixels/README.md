# Excavation 076 — Pixels — Turning Light into Numbers

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

> **PART VIII — SEEING AND CREATING**
>
> Language was only one trace of reality. Light, space, sound, and noise demand new forms of the discoveries you already made.

Causal interventions turn interpretation into an experiment. The field system can now inspect language reasoning, but its users also need it to understand the camera's raw grid of colored light.

At the Glass Menagerie, the maker of seeing-machines meets the next case beside the wall of illuminated tiles. The nearest idea is also the most reasonable one: assign one label to the entire raw byte sequence.

The attraction of this attempt is easy to see. To assign one label to the entire raw byte sequence reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: a one-pixel shift changes thousands of byte positions although the same tiger remains.

The contradiction matters because it identifies a structural loss in the instruction to assign one label to the entire raw byte sequence, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The wall of illuminated tiles will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must preserve local spatial arrangement and compare nearby color measurements. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Pixels**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## Turning Light into Numbers

A 2×2 grayscale patch becomes four intensities with explicit row and column positions.

## Where pixels runs out

Pixels depend on lighting, sensor, scale, and viewpoint.

The pixels repair holds, but the world asks for something it was never given. At the Glass Menagerie, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the wall of illuminated tiles

Rebuild the pixels scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 077](../077-convolution/README.md)
