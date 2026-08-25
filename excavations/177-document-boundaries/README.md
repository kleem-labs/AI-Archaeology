# Excavation 177 — Document Boundaries — Keep One Story from Leaking into Another

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Data and pretraining operations

The manifest fixes which source documents belong to the run. Tokenization can still concatenate them into a stream where the ending of one document predicts the beginning of an unrelated one.

The previous discovery reaches the Archive Foundry carrying one unfinished problem. Beside the chain-of-custody ledger, the archivist-engineer first tries to join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width.

There is good reason to begin this way. If we join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: a ranger report ending with “tiger tracks near” is trained to predict the first word of an unrelated software license. The model receives a relationship that never existed in either document.

This failure cannot be repaired by performing the instruction to join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the chain-of-custody ledger; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Document Boundaries**. The name is simply a handle for the distinction already reconstructed.

## Keep One Story from Leaking into Another

Two short documents share one packed row, but a boundary mask lets each token read only tokens from its own document. The empty hardware space is saved without inventing a false continuation.

## The calculation hidden inside document boundaries

The archivist-engineer carries the document boundaries scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A_ij answers one concrete yes-or-no question for token positions i and j: may information cross between them? One means the pair shares a document; zero means the boundary forbids the connection.

### Why the melody needs these exact notes

[Cases](../../MATHEMATICAL_MOVES.md#cases) are forced because same-document and cross-document pairs obey different rules. [Equality](../../MATHEMATICAL_MOVES.md#equals) assigns an exact permission bit. A distance score would blur a categorical boundary, while addition would invent partial permission.

The story of document boundaries has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
A_{ij}=\begin{cases}1&\text{tokens }i,j\text{ share a document}\\0&\text{otherwise}\end{cases}
$$

## Where document boundaries runs out

Boundary isolation prevents accidental cross-document lessons; it cannot decide whether two paragraphs really belong to the same source document.

One unsolved mark remains on the chain-of-custody ledger. None of the responsibilities inside Document Boundaries can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the chain-of-custody ledger

Rebuild the document boundaries scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Language Identification — Do Not Confuse Familiar Script with Familiar Language](../178-language-identification/README.md)
