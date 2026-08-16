# Excavation 177 — Document Boundaries — Keep One Story from Leaking into Another

The manifest fixes which source documents belong to the run. Tokenization can still concatenate them into a stream where the ending of one document predicts the beginning of an unrelated one.

We first try to join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width.

That confidence lasts only until the first measurement. A ranger report ending with “tiger tracks near” is trained to predict the first word of an unrelated software license. The model receives a relationship that never existed in either document.

What broke tells us what the next design must preserve. Mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended.

## Let one run decide

Two short documents share one packed row, but a boundary mask lets each token read only tokens from its own document. The empty hardware space is saved without inventing a false continuation.

## The arithmetic we have earned

A_ij answers one concrete yes-or-no question for token positions i and j: may information cross between them? One means the pair shares a document; zero means the boundary forbids the connection.

### Why these operations are forced

[Cases](../../MATHEMATICAL_MOVES.md#cases) are forced because same-document and cross-document pairs obey different rules. [Equality](../../MATHEMATICAL_MOVES.md#equals) assigns an exact permission bit. A distance score would blur a categorical boundary, while addition would invent partial permission.

Only now can we compress the procedure:

$$
A_{ij}=\begin{cases}1&\text{tokens }i,j\text{ share a document}\\0&\text{otherwise}\end{cases}
$$

## What this repair cannot do

Boundary isolation prevents accidental cross-document lessons; it cannot decide whether two paragraphs really belong to the same source document.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Language Identification — Do Not Confuse Familiar Script with Familiar Language](../178-language-identification/README.md)
