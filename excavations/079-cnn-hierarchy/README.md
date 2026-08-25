# Excavation 079 — CNN Hierarchies

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Vision and generative models

Pooling keeps strong local evidence while shrinking the map. Edges and spots are still not eyes, stripes, or tigers; later detectors must compose simple evidence into larger structures.

Inside the Glass Menagerie, the old method is given an honest chance. The maker of seeing-machines places the evidence on the wall of illuminated tiles and tries to classify directly from isolated edge responses.

Nothing about this first move is careless. To classify directly from isolated edge responses is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: one edge has no object-level meaning.

The important discovery is not merely that trying to classify directly from isolated edge responses failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the wall of illuminated tiles, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to stack local detectors so later layers combine earlier patterns over wider regions. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **CNN Hierarchies**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## Understanding cnn hierarchies

Edges form corners; corners and textures form stripes; repeated stripes plus shape support tiger.

## Where cnn hierarchies runs out

The hierarchy is learned, not guaranteed to match human parts.

The wall of illuminated tiles answers today's question and falls silent at the next. That silence is precise: CNN Hierarchies was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the wall of illuminated tiles

Rebuild the cnn hierarchies scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 080](../080-vision-transformers/README.md)
