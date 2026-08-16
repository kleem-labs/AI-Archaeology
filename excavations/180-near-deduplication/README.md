# Excavation 180 — Near Deduplication — When a Copy Changes a Few Words

Exact deduplication removes byte-equivalent documents. The copied article with a new banner, reordered footer, or one edited sentence still survives as apparently new evidence.

Using what we have, we lowercase both documents and demand that every remaining word match.

The plan survives only until the evidence is counted. One inserted advertisement defeats the rule, while independently written short notices can match by accident. Exact sequence equality is too brittle for disguised copies.

The lost information tells us what must come next. Represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale.

## Let one run decide

The original report has ten shingles; its mirrored copy shares eight and introduces two. Their intersection has eight shingles and their union has twelve, giving similarity 8/12 rather than pretending the documents are either perfectly equal or wholly unrelated.

## The arithmetic we have earned

A and B are the shingle sets from the original tiger report and its edited mirror. Their intersection counts phrases both contain; their union counts every distinct phrase appearing in either; J is the shared fraction.

### Why these operations are forced

[Intersection](../../MATHEMATICAL_MOVES.md#intersection) keeps shared evidence and [union](../../MATHEMATICAL_MOVES.md#union) defines the total distinct evidence available. [Cardinality](../../MATHEMATICAL_MOVES.md#cardinality) turns each set into a count. [Division](../../MATHEMATICAL_MOVES.md#division) makes the overlap comparable across document lengths; a raw shared count would favor long documents.

Only now can we compress the procedure:

$$
J(A,B)=\frac{\lvert A\cap B\rvert}{\lvert A\cup B\rvert}
$$

## What this repair cannot do

Near-deduplication depends on shingle size and threshold; aggressive settings can erase legitimate quotations, templates, or independent accounts.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Quality Filtering — Remove Noise Without Defining Humanity Away](../181-quality-filtering/README.md)
