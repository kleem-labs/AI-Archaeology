# Excavation 037 — Input Embeddings: Giving Tokens Learnable Coordinates

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Language models and useful answers

Tokenization gives the machine repeatable pieces and assigns each piece an address. An address distinguishes tokens but says nothing about how their meanings should begin.

A new case arrives at the Clockwork Scriptorium, but the mechanist first reaches for the familiar sentence-wheel. Its promise is simple: feed token IDs directly into the network.

The rule survives the easy cases. The next case leaves a crack through the middle of it: since 417 is larger than 92, arithmetic treats tiger as greater than lion. The distance from tiger to lion becomes 325, while the distance from tiger to token 418 is one. More confidence cannot repair information that never entered the rule.

*The mechanist sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: feed token IDs directly into the…
possible road B ─┘              └── loses: since 417 is larger than 92,…

same roads ──▶ repaired map ──▶ give every vocabulary item a one-hot…
```

Two trails now cross the sentence-wheel. The pale trail bears the instruction “feed token IDs directly into the network.” It disappears into the observed failure: since 417 is larger than 92, arithmetic treats tiger as greater than lion. The distance from tiger to lion becomes 325, while the distance from tiger to token 418 is one. The darker trail carries one additional capacity—to give every vocabulary item a one-hot vector: one coordinate is one and all others are zero. `lion → [1, 0, 0, 0]`, `tiger → [0, 1, 0, 0]`, and `river → [0, 0, 1, 0]`. Now IDs no longer pretend to contain magnitude. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed input embeddings mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the sentence-wheel is altered in exactly one way: give every vocabulary item a one-hot vector: one coordinate is one and all others are zero. `lion → [1, 0, 0, 0]`, `tiger → [0, 1, 0, 0]`, and `river → [0, 0, 1, 0]`. Now IDs no longer pretend to contain magnitude. Much later, people will call this territory **Input Embeddings**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the sentence-wheel. The failed path remains visible beneath the repair, because input embeddings is easier to remember when its scar remains attached to it. The scar reads, ‘since 417 is larger than 92, arithmetic treats tiger as greater than lion. The distance from tiger to lion becomes 325, while the distance from tiger to token 418 is one’; the new line exists only to keep that loss from happening again.

<!-- memory-film-v1:start -->
> **Memory realm 4 of 18 — [Clockwork Scriptorium](../../MEMORY_PALACE.md#realm-4)**
>
> **The question carried into this chamber:** What fails if we feed token IDs directly into the network?

## When the chamber changes

The Input Embeddings chamber leaves one scene behind so the idea can be recovered after its symbols fade.

First hold the failed picture still: The bridge follows the tempting path—feed token IDs directly into the network. Then the evidence answers: since 417 is larger than 92, arithmetic treats tiger as greater than lion. The distance from tiger to lion becomes 325, while the distance from tiger to token 418 is one.

Now let the chamber move: The mechanist changes one moving part. The bridge can now give every vocabulary item a one-hot vector: one coordinate is one and all others are zero. `lion → [1, 0, 0, 0]`, `tiger → [0, 1, 0, 0]`, and `river → [0, 0, 1, 0]`. Now IDs no longer pretend to contain magnitude.

The object that should remain after the terminology disappears is **the input embeddings bridge mounted on the sentence-wheel**.

> **Memory seal — Input Embeddings**
>
> Input Embeddings keeps the missing power: give every vocabulary item a one-hot vector: one coordinate is one and all others are zero. `lion → [1, 0, 0, 0]`, `tiger → [0, 1, 0, 0]`, and `river → [0, 0, 1, 0]`. Now IDs no longer pretend to contain magnitude.

Give the idea a bodily path: Touch the input embeddings bridge in imagination: tilt one hand as the broken rule and use the other to bring the necessary distinction back into balance.
<!-- memory-film-v1:end -->

## The calculation hidden inside input embeddings

The mechanist carries the input embeddings scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A vocabulary of 50,000 tokens produces 50,000-dimensional vectors containing 49,999 zeros. Every distinct pair is equally distant. We preserved identity but learned no relationship.

The network needs a compact set of coordinates whose positions can change when prediction errors reveal useful relationships.

Let the embedding table contain one row for each vocabulary item:

The tokenizer assigns shelf address 2 to *tiger*. Looking up address 2 retrieves a small card of adjustable coordinates learned from tiger's usage. The address itself says nothing about meaning; moving the tiger card to shelf 7 would not change its learned contents. The table is therefore a collection of learned starting descriptions, while the token ID is merely the address used to fetch one.

### Naming what is already on the table

**V** is the vocabulary and **|V|** its number of token addresses.
**d** is the compact representation width chosen for the model.
**E** therefore needs one row per token and d learnable coordinates per row.
**i** is a token ID used only to select row E[i]; **x_i** is the retrieved meaning-bearing vector.
**e_i** is the one-hot selector. Multiplying e_i by E produces the same row, explaining why direct lookup is valid and cheaper.

Multiplying by a one-hot vector merely selects one row, so an implementation can perform the lookup directly.

### Why the melody needs these exact notes

[E ∈ ℝ](../../MATHEMATICAL_MOVES.md#membership) states the embedding table's allowed shape: one row per vocabulary token and d real coordinates per row.
[E[i]](../../MATHEMATICAL_MOVES.md#indices) treats token ID i as a shelf address. It retrieves one row rather than using the ID as a meaningful magnitude.
[One-hot multiplication](../../MATHEMATICAL_MOVES.md#multiplication) gives the same lookup because every zero row contribution vanishes and the single one-valued row survives; addition then combines the row contributions.

Trace each operation by touch rather than by name: **the lock and key**—one influence matters through another, and either missing factor can close the path. Together they form the smallest mechanism that survives the counterexample.

The mechanist reads the journey of input embeddings once more across the sentence-wheel, then lets the words contract without losing their order:

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

The sentence-wheel answers today's question and falls silent at the next. That silence is precise: Input Embeddings was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the sentence-wheel

Rebuild the input embeddings scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Position](../038-position/README.md)
