# Excavation 011 — Multi-Head Attention

Ask one expert to interpret a sentence. The expert may follow reference, grammar, distance, or topic—but one attention distribution forces every relationship to compete in the same set of weights.

## Failed attempt: make one expert bigger

A wider query and key can hold more information, but one head still produces one distribution for each receiving token. A nearby adjective and a distant subject may both matter for different reasons. One compromise can blur both jobs.

## Your expert model

You supplied the better design:

> Each expert contributes what they do, related to their profession and domain of knowledge.

Imagine parallel specialists reading the same sentence:

- one notices who a pronoun refers to;
- one follows grammatical agreement;
- one notices nearby modifiers;
- one tracks the broader topic.

We do not assign those professions by hand. We give each specialist its own learned query, key, and value views, then let training reward useful specializations.

That is **multi-head attention**.

```text
same token representations
   ├── head 1: its own Q, K, V → result 1
   ├── head 2: its own Q, K, V → result 2
   └── head 3: its own Q, K, V → result 3
                         ↓
              preserve and recombine
```

## Why not average immediately?

Averaging would erase which expert supplied which coordinates before the model can use the distinction. Concatenation keeps their reports separate; a final learned transformation decides how to combine them.

Only now does the compact expression earn its place:

## The calculation hidden inside multi-head attention

In “The tiger that chased the deer was tired,” one reader follows grammar to discover what *was tired* describes, while another follows reference to keep tiger separate from deer. Averaging their notes too early destroys which evidence came from which question. Keeping the two notes side by side lets a later learned map decide how much grammar and reference the sentence needs.

### Naming what is already on the table

- **X** is the shared sequence of token representations.
- Each **headₕ** is an independent Q/K/V retrieval space, needed because relationships should not compete in one distribution.
- Concatenation preserves each report instead of averaging distinctions away.
- **H** counts the parallel heads.
- **W_O** is learned because the model must decide how the preserved reports should interact and return to the shared width.

Each head is the query–key–value mechanism from the previous excavation with independent learned projections.

The analogy has limits. Heads do not always become clean, human-readable professions. Some overlap; some are difficult to interpret. The architectural point is parallel relationship spaces, not a promise of tidy labels.

### Why the melody needs these exact notes

[Concatenation](../../MATHEMATICAL_MOVES.md#concatenation) keeps the grammar expert, reference expert, and distance expert side by side. Adding them immediately would erase which head supplied which evidence.
[Multiplication by the output matrix](../../MATHEMATICAL_MOVES.md#multiplication) lets the model learn how those preserved expert coordinates should interact; a fixed sum would impose the same mixture everywhere.

The symbols are about to change costume, but their work has appeared before: **the binding loom**—distinct pieces remain side by side instead of being blended away; and **the lock and key**—one influence matters through another, and either missing factor can close the path. This is how distant excavations begin to sound like variations of one melody.

The long cedar table already contains the complete multi-head attention mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
\mathrm{MultiHead}(X)
=\mathrm{Concat}(\text{head}_1,\ldots,\text{head}_H)W_O
$$

## Challenge

Give two different relationships needed to understand “The keys to the cabinet near the stairs are missing.” Explain why forcing both into one attention distribution could create a compromise.

## What the next excavation needs

The experts have exchanged information. Each token must now transform what it received into new internal knowledge.

[Next: Feed-Forward Networks](../012-feed-forward-networks/README.md)

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->
