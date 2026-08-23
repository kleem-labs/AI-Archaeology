# Excavation 037 — Input Embeddings: Giving Tokens Learnable Coordinates

<!-- book-prose-v2 -->

Tokenization gives the machine repeatable pieces and assigns each piece an address. An address distinguishes tokens but says nothing about how their meanings should begin.

For a moment, remain loyal to the simplest proposal: feed token IDs directly into the network.

Its appeal is not ignorance but economy. Input Embeddings should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Reality now asks a question the retained information cannot answer: since 417 is larger than 92, arithmetic treats tiger as greater than lion. The distance from tiger to lion becomes 325, while the distance from tiger to token 418 is one.

Notice what the counterexample has accomplished for input embeddings. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: give every vocabulary item a one-hot vector: one coordinate is one and all others are zero. `lion → [1, 0, 0, 0]`, `tiger → [0, 1, 0, 0]`, and `river → [0, 0, 1, 0]`. Now IDs no longer pretend to contain magnitude.

Humanity eventually gathered this problem and its repairs under the name **Input Embeddings**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace input embeddings with the old instruction to feed token IDs directly into the network.. The result is again that since 417 is larger than 92, arithmetic treats tiger as greater than lion. The distance from tiger to lion becomes 325, while the distance from tiger to token 418 is one. Put back only the requirement to give every vocabulary item a one-hot vector: one coordinate is one and all others are zero. `lion → [1, 0, 0, 0]`, `tiger → [0, 1, 0, 0]`, and `river → [0, 0, 1, 0]`. Now IDs no longer pretend to contain magnitude. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when input embeddings is introduced. The same evidence that defeated the attempt to feed token IDs directly into the network. is presented again. Only the ability to give every vocabulary item a one-hot vector: one coordinate is one and all others are zero. `lion → [1, 0, 0, 0]`, `tiger → [0, 1, 0, 0]`, and `river → [0, 0, 1, 0]`. Now IDs no longer pretend to contain magnitude changes, so the repaired conclusion cannot be credited to a conveniently different example.

## The calculation hidden inside input embeddings

Before Input Embeddings receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

A vocabulary of 50,000 tokens produces 50,000-dimensional vectors containing 49,999 zeros. Every distinct pair is equally distant. We preserved identity but learned no relationship.

The network needs a compact set of coordinates whose positions can change when prediction errors reveal useful relationships.

Let the embedding table contain one row for each vocabulary item:

The tokenizer assigns shelf address 2 to *tiger*. Looking up address 2 retrieves a small card of adjustable coordinates learned from tiger's usage. The address itself says nothing about meaning; moving the tiger card to shelf 7 would not change its learned contents. The table is therefore a collection of learned starting descriptions, while the token ID is merely the address used to fetch one.

### Names for pieces we have already used

**V** is the vocabulary and **|V|** its number of token addresses.
**d** is the compact representation width chosen for the model.
**E** therefore needs one row per token and d learnable coordinates per row.
**i** is a token ID used only to select row E[i]; **x_i** is the retrieved meaning-bearing vector.
**e_i** is the one-hot selector. Multiplying e_i by E produces the same row, explaining why direct lookup is valid and cheaper.

Multiplying by a one-hot vector merely selects one row, so an implementation can perform the lookup directly.

### Why no cheaper operation does the same job

[E ∈ ℝ](../../MATHEMATICAL_MOVES.md#membership) states the embedding table's allowed shape: one row per vocabulary token and d real coordinates per row.
[E[i]](../../MATHEMATICAL_MOVES.md#indices) treats token ID i as a shelf address. It retrieves one row rather than using the ID as a meaningful magnitude.
[One-hot multiplication](../../MATHEMATICAL_MOVES.md#multiplication) gives the same lookup because every zero row contribution vanishes and the single one-valued row survives; addition then combines the row contributions.

The notation is finally shorter than the story that created it:

$$
E\in\mathbb{R}^{|V|\times d}
$$

For token ID $i$, retrieve:

$$
\mathbf{x}_i=E[i]
$$

The one-hot view gives the same result:

$$
\mathbf{x}_i=\mathbf{e}_iE
$$

## Input Embeddings beyond this one case

A library call number is not the book's meaning. It is an address used to retrieve the book. Token IDs are call numbers; embedding rows are the learnable content retrieved from the shelf.

## How Learning Changes the Table

Suppose tiger repeatedly appears where danger, stripes, and hunting matter. Prediction errors send corrections into its row. Lion receives some similar corrections and some different ones. Their vectors may become nearby—not because their IDs were nearby, but because useful predictions demanded shared structure.

This reconnects to Excavation 007. There we needed geometry for meaning. Here we have finally installed that geometry as a trainable component inside the language model.

## Where input embeddings runs out

The same token initially retrieves the same row in every sentence. Bank beside river and bank beside money start from one vector. Attention will later contextualize it.

Worse, the embedding table contains no order. Swapping dog bites man with man bites dog selects the same three rows in a different sequence, but self-attention alone has no built-in idea that one row arrived first.

Why does that boundary remain? Input Embeddings was built for one responsibility: give every vocabulary item a one-hot vector: one coordinate is one and all others are zero. `lion → [1, 0, 0, 0]`, `tiger → [0, 1, 0, 0]`, and `river → [0, 0, 1, 0]`. Now IDs no longer pretend to contain magnitude. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take input embeddings to the workbench

The argument for input embeddings is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running input embeddings, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the input embeddings result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Position](../038-position/README.md)
