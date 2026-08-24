# Excavation 080 — Vision Transformers

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

A convolutional hierarchy builds local parts into objects. Some decisions depend on distant regions that a fixed local pathway connects only after many layers, inviting the image patches to communicate directly.

At the Glass Menagerie, the maker of seeing-machines returns to the wall of illuminated tiles. Yesterday's instrument still lies open, so the first move asks for no new magic: treat every pixel as a token.

Reality answers without terminology: the sequence becomes enormous and individual pixels carry little stable structure. The wall of illuminated tiles now holds two situations the old rule cannot keep apart.

*The maker of seeing-machines sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ treat every pixel as a token ──▶ blurred: the sequence becomes enormous and…
      │
      └── new lens ──▶ group pixels into patches, embed them… ──▶ distinction survives
```

The wall of illuminated tiles is divided down the middle. Left side: “treat every pixel as a token.” Its final mark records the sequence becomes enormous and individual pixels carry little stable structure. Right side: the same starting evidence, now allowed to group pixels into patches, embed them as tokens, add position, and apply attention. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given vision transformers a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: group pixels into patches, embed them as tokens, add position, and apply attention. The name **Vision Transformers** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to treat every pixel as a token; on the other lies the observed fact that the sequence becomes enormous and individual pixels carry little stable structure. The bridge called vision transformers has exactly the planks needed to group pixels into patches, embed them as tokens, add position, and apply attention.

## Understanding vision transformers

A 224×224 image with 16×16 patches becomes 196 tokens instead of 50,176 pixel tokens.

## Where vision transformers runs out

Patch size trades detail for cost and needs substantial data.

A final test reaches beyond the new instrument. It does not refute Vision Transformers; it reveals the edge of what was constructed. The maker of seeing-machines carries that edge into the following room.

## Return to the wall of illuminated tiles

Rebuild the vision transformers scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 081](../081-autoencoders/README.md)
