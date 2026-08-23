# Excavation 177 — Document Boundaries — Keep One Story from Leaking into Another

<!-- book-prose-v2 -->

The manifest fixes which source documents belong to the run. Tokenization can still concatenate them into a stream where the ending of one document predicts the beginning of an unrelated one.

At this point the shortest path seems to be to join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width.

This is how document boundaries ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

The world supplies the one comparison the shortcut hoped never to face: a ranger report ending with “tiger tracks near” is trained to predict the first word of an unrelated software license. The model receives a relationship that never existed in either document.

The wrong answer makes the need for document boundaries inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended.

The usual name, **Document Boundaries**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width produces the observed failure: a ranger report ending with “tiger tracks near” is trained to predict the first word of an unrelated software license. The model receives a relationship that never existed in either document. Starting with the repaired demand to mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended preserves the information the shortcut lost. The subject of document boundaries lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended instead of merely trying to join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width. That controlled contrast is what turns a plausible explanation of document boundaries into an understandable derivation.

## Keep One Story from Leaking into Another

Two short documents share one packed row, but a boundary mask lets each token read only tokens from its own document. The empty hardware space is saved without inventing a false continuation.

There are now two histories of this document boundaries case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

## The calculation hidden inside document boundaries

Before Document Boundaries receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

A_ij answers one concrete yes-or-no question for token positions i and j: may information cross between them? One means the pair shares a document; zero means the boundary forbids the connection.

### Why no cheaper operation does the same job

[Cases](../../MATHEMATICAL_MOVES.md#cases) are forced because same-document and cross-document pairs obey different rules. [Equality](../../MATHEMATICAL_MOVES.md#equals) assigns an exact permission bit. A distance score would blur a categorical boundary, while addition would invent partial permission.

Every symbol in Document Boundaries can now be read back into an action already performed. The whole procedure fits in one line:

$$
A_{ij}=\begin{cases}1&\text{tokens }i,j\text{ share a document}\\0&\text{otherwise}\end{cases}
$$

## Where document boundaries runs out

Boundary isolation prevents accidental cross-document lessons; it cannot decide whether two paragraphs really belong to the same source document.

Look back at what document boundaries actually preserves: it can mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

## Take document boundaries to the workbench

The reader has reconstructed document boundaries in words; the workbench tests whether those words specify a real procedure. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running document boundaries, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the document boundaries result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Language Identification — Do Not Confuse Familiar Script with Familiar Language](../178-language-identification/README.md)
