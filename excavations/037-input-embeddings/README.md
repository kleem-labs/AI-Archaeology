# Excavation 037 — Input Embeddings: Giving Tokens Learnable Coordinates

[Previous: Tokenization](../036-tokenization/README.md)

## Problem

The tokenizer returns IDs:

~~~text
tiger → 417
lion  → 92
river → 801
~~~

A neural network needs numbers, so perhaps the problem appears solved. But what does 417 mean?

Nothing except “look in slot 417.”

## Naive Attempt

Feed token IDs directly into the network. Since 417 is larger than 92, arithmetic treats tiger as greater than lion. The distance from tiger to lion becomes 325, while the distance from tiger to token 418 is one.

## Why It Fails

Tokenizer IDs are addresses, not measurements. Their order is accidental. Renumbering the vocabulary must not change language, yet direct arithmetic changes every relationship.

## Better Attempt

Give every vocabulary item a one-hot vector: one coordinate is one and all others are zero.

~~~text
lion  → [1, 0, 0, 0]
tiger → [0, 1, 0, 0]
river → [0, 0, 1, 0]
~~~

Now IDs no longer pretend to contain magnitude.

## Why It Still Fails

A vocabulary of 50,000 tokens produces 50,000-dimensional vectors containing 49,999 zeros. Every distinct pair is equally distant. We preserved identity but learned no relationship.

The network needs a compact set of coordinates whose positions can change when prediction errors reveal useful relationships.

## Key Insight

Create a table with one learnable vector per token. A token ID selects a row. Training moves that row whenever changing the token's representation would reduce prediction loss.

~~~text
token ID → choose one row → dense vector
~~~

The ID remains an address. The selected row becomes the representation.

## Mathematics Emerges

Let the embedding table contain one row for each vocabulary item:

## Walk It Once with Concrete Values

With four tokens and width two, the table might have rows [0.1,0.8], [-0.2,0.4], [0.7,-0.1], [0.3,0.2]. Token ID 2 selects [0.7,-0.1]; the number 2 is only the shelf address.

## Why Every Term Must Exist Before the Equation

- **V** is the vocabulary and **|V|** its number of token addresses.
- **d** is the compact representation width chosen for the model.
- **E** therefore needs one row per token and d learnable coordinates per row.
- **i** is a token ID used only to select row E[i]; **x_i** is the retrieved meaning-bearing vector.
- **e_i** is the one-hot selector. Multiplying e_i by E produces the same row, explaining why direct lookup is valid and cheaper.


Multiplying by a one-hot vector merely selects one row, so an implementation can perform the lookup directly.

Only now can we compress that reasoning:

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


## Real-World Analogy

A library call number is not the book's meaning. It is an address used to retrieve the book. Token IDs are call numbers; embedding rows are the learnable content retrieved from the shelf.

## How Learning Changes the Table

Suppose tiger repeatedly appears where danger, stripes, and hunting matter. Prediction errors send corrections into its row. Lion receives some similar corrections and some different ones. Their vectors may become nearby—not because their IDs were nearby, but because useful predictions demanded shared structure.

This reconnects to Excavation 007. There we needed geometry for meaning. Here we have finally installed that geometry as a trainable component inside the language model.

## Limits

The same token initially retrieves the same row in every sentence. Bank beside river and bank beside money start from one vector. Attention will later contextualize it.

Worse, the embedding table contains no order. Swapping dog bites man with man bites dog selects the same three rows in a different sequence, but self-attention alone has no built-in idea that one row arrived first.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

## Next Need

Tokens now have learnable coordinates, but no position. Excavation 038 must make order visible without confusing position with meaning.

[Next: Position](../038-position/README.md)
