# Excavation 080 — Vision Transformers

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

A convolutional hierarchy builds local parts into objects. Some decisions depend on distant regions that a fixed local pathway connects only after many layers, inviting the image patches to communicate directly.

At the Glass Menagerie, the maker of seeing-machines meets the next case beside the wall of illuminated tiles. The nearest idea is also the most reasonable one: treat every pixel as a token.

The attraction of this attempt is easy to see. To treat every pixel as a token reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: the sequence becomes enormous and individual pixels carry little stable structure.

The contradiction matters because it identifies a structural loss in the instruction to treat every pixel as a token, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The wall of illuminated tiles will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must group pixels into patches, embed them as tokens, add position, and apply attention. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Vision Transformers**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## Understanding vision transformers

A 224×224 image with 16×16 patches becomes 196 tokens instead of 50,176 pixel tokens.

## Where vision transformers runs out

Patch size trades detail for cost and needs substantial data.

A final test reaches beyond the new instrument. It does not refute Vision Transformers; it reveals the edge of what was constructed. The maker of seeing-machines carries that edge into the following room.

## Return to the wall of illuminated tiles

Rebuild the vision transformers scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 081](../081-autoencoders/README.md)
