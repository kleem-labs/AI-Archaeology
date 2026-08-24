# Excavation 180 — Near Deduplication — When a Copy Changes a Few Words

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Exact deduplication removes byte-equivalent documents. The copied article with a new banner, reordered footer, or one edited sentence still survives as apparently new evidence.

Inside the Archive Foundry, every old tool is given one honest chance. The archivist-engineer sets the chain-of-custody ledger between the evidence and the desired answer, then tries to lowercase both documents and demand that every remaining word match.

For a moment the mark looks complete. Then the evidence refuses to fit: one inserted advertisement defeats the rule, while independently written short notices can match by accident. Exact sequence equality is too brittle for disguised copies. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The archivist-engineer sketches the break before changing it:*

```text
observation
    │
    ▼
[lowercase both documents and demand…]
    │
    ╳  one inserted advertisement defeats…
    │
    ▼
[represent each document by…]
```

The archivist-engineer lays two translucent sheets over the chain-of-custody ledger. The first is inscribed, “lowercase both documents and demand that every remaining word match.” Its path ends where one inserted advertisement defeats the rule, while independently written short notices can match by accident. Exact sequence equality is too brittle for disguised copies. The second receives the same evidence but is allowed to represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale. Held to the light, the sheets separate at exactly one decision.

No one reaches for a near deduplication formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The archivist-engineer changes only that one responsibility: represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale. When the ink dries, the name **Near Deduplication** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The chain-of-custody ledger keeps both histories. Its older mark still says, ‘lowercase both documents and demand that every remaining word match’; beside it, the newer mark says, ‘represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale.’ The distance between those sentences is the exact shape of near deduplication: no larger than the failure required, and no smaller than reality permits.

## When a Copy Changes a Few Words

The original report has ten shingles; its mirrored copy shares eight and introduces two. Their intersection has eight shingles and their union has twelve, giving similarity 8/12 rather than pretending the documents are either perfectly equal or wholly unrelated.

## The calculation hidden inside near deduplication

The archivist-engineer carries the near deduplication scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A and B are the shingle sets from the original tiger report and its edited mirror. Their intersection counts phrases both contain; their union counts every distinct phrase appearing in either; J is the shared fraction.

### Why the melody needs these exact notes

[Intersection](../../MATHEMATICAL_MOVES.md#intersection) keeps shared evidence and [union](../../MATHEMATICAL_MOVES.md#union) defines the total distinct evidence available. [Cardinality](../../MATHEMATICAL_MOVES.md#cardinality) turns each set into a count. [Division](../../MATHEMATICAL_MOVES.md#division) makes the overlap comparable across document lengths; a raw shared count would favor long documents.

Inside near deduplication, familiar operations return with stricter duties: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Every mark needed for near deduplication is now visible on the chain-of-custody ledger. The symbols do not add an idea; they bind the discovered moves into one line:

$$
J(A,B)=\frac{\lvert A\cap B\rvert}{\lvert A\cup B\rvert}
$$

## Where near deduplication runs out

Near-deduplication depends on shingle size and threshold; aggressive settings can erase legitimate quotations, templates, or independent accounts.

At the Archive Foundry, the archivist-engineer leaves a blank beneath the new mark. Near Deduplication has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the chain-of-custody ledger

Rebuild the near deduplication scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Quality Filtering — Remove Noise Without Defining Humanity Away](../181-quality-filtering/README.md)
