# Excavation 177 — Document Boundaries — Keep One Story from Leaking into Another

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Data and pretraining operations

The manifest fixes which source documents belong to the run. Tokenization can still concatenate them into a stream where the ending of one document predicts the beginning of an unrelated one.

Morning reaches the Archive Foundry before anyone has a name for today's difficulty. Beside the chain-of-custody ledger, the archivist-engineer tries the smallest continuation of what already works: join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width.

Then the quiet test arrives: a ranger report ending with “tiger tracks near” is trained to predict the first word of an unrelated software license. The model receives a relationship that never existed in either document. What looked like simplicity is revealed as a missing distinction.

*The archivist-engineer sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ join every token sequence end to end… ──▶ blurred: a ranger report ending with “tiger…
      │
      └── new lens ──▶ mark document ends, reset position… ──▶ distinction survives
```

The archivist-engineer turns the chain-of-custody ledger toward the light. Through the old engraving, join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width, the evidence ends in the same contradiction: a ranger report ending with “tiger tracks near” is trained to predict the first word of an unrelated software license. The model receives a relationship that never existed in either document. A second engraving adds only the power to mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The archivist-engineer circles the place where the two document boundaries cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended. The archivist-engineer writes **Document Boundaries** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The archivist-engineer does not memorize document boundaries. Instead, the archivist-engineer memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended. The formal name merely lets that motion be shared.

<!-- memory-film-v1:start -->
> **Memory realm 13 of 18 — [Archive Foundry](../../MEMORY_PALACE.md#realm-13)**
>
> **The question carried into this chamber:** What fails if we join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width?

## When the chamber changes

The Document Boundaries chamber leaves one scene behind so the idea can be recovered after its symbols fade.

First hold the failed picture still: The lens follows the tempting path—join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width. Then the evidence answers: a ranger report ending with “tiger tracks near” is trained to predict the first word of an unrelated software license. The model receives a relationship that never existed in either document.

Now let the chamber move: The archivist-engineer changes one moving part. The lens can now mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended.

The object that should remain after the terminology disappears is **the document boundaries lens mounted on the chain-of-custody ledger**.

> **Memory seal — Document Boundaries**
>
> Document Boundaries keeps the missing power: mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended.

Give the idea a bodily path: Touch the document boundaries lens in imagination: hold both hands as the two failed alternatives, then move one hand through the repaired route.
<!-- memory-film-v1:end -->

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
