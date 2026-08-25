# Excavation 081 — Autoencoders — Compressing and Rebuilding

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Vision and generative models

Vision Transformers let distant patches attend to one another. Classification uses the representation once; reconstruction asks whether a smaller internal code can preserve enough of the image to rebuild it.

The previous discovery reaches the Glass Menagerie carrying one unfinished problem. Beside the wall of illuminated tiles, the maker of seeing-machines first tries to copy the input through an unrestricted hidden layer.

There is good reason to begin this way. If we copy the input through an unrestricted hidden layer, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: a wide hidden layer learns identity without compression.

This failure cannot be repaired by performing the instruction to copy the input through an unrestricted hidden layer more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the wall of illuminated tiles; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to force information through a bottleneck and train reconstruction. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Autoencoders**. The name is simply a handle for the distinction already reconstructed.

## Compressing and Rebuilding

Four correlated measurements compress to two codes that still rebuild the originals approximately.

## Where autoencoders runs out

Good reconstruction may preserve details irrelevant to downstream meaning.

One unsolved mark remains on the wall of illuminated tiles. None of the responsibilities inside Autoencoders can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the wall of illuminated tiles

Rebuild the autoencoders scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 082](../082-latent-space/README.md)
