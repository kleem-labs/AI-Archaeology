# Excavation 180 — Near Deduplication — When a Copy Changes a Few Words

<!-- book-prose-v2 -->

Exact deduplication removes byte-equivalent documents. The copied article with a new banner, reordered footer, or one edited sentence still survives as apparently new evidence.

The least expensive next move is to lowercase both documents and demand that every remaining word match.

The proposal deserves a fair hearing. For near deduplication, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The proposal breaks for a specific reason, not by authority: one inserted advertisement defeats the rule, while independently written short notices can match by accident. Exact sequence equality is too brittle for disguised copies.

The failure changes the question behind near deduplication. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale.

Only at this point does the inherited name **Near Deduplication** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of near deduplication by mentally removing the repair. We fall back to the proposal to lowercase both documents and demand that every remaining word match; then one inserted advertisement defeats the rule, while independently written short notices can match by accident. Exact sequence equality is too brittle for disguised copies. Restore only the ability to represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to lowercase both documents and demand that every remaining word match to requiring the system to represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to near deduplication.

## When a Copy Changes a Few Words

The original report has ten shingles; its mirrored copy shares eight and introduces two. Their intersection has eight shingles and their union has twelve, giving similarity 8/12 rather than pretending the documents are either perfectly equal or wholly unrelated.

Put the old procedure beside near deduplication. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## The calculation hidden inside near deduplication

Do not read the coming Near Deduplication line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

A and B are the shingle sets from the original tiger report and its edited mirror. Their intersection counts phrases both contain; their union counts every distinct phrase appearing in either; J is the shared fraction.

### Why no cheaper operation does the same job

[Intersection](../../MATHEMATICAL_MOVES.md#intersection) keeps shared evidence and [union](../../MATHEMATICAL_MOVES.md#union) defines the total distinct evidence available. [Cardinality](../../MATHEMATICAL_MOVES.md#cardinality) turns each set into a count. [Division](../../MATHEMATICAL_MOVES.md#division) makes the overlap comparable across document lengths; a raw shared count would favor long documents.

Every symbol in Near Deduplication can now be read back into an action already performed. The whole procedure fits in one line:

$$
J(A,B)=\frac{\lvert A\cap B\rvert}{\lvert A\cup B\rvert}
$$

## Where near deduplication runs out

Near-deduplication depends on shingle size and threshold; aggressive settings can erase legitimate quotations, templates, or independent accounts.

The limit follows from the job assigned to near deduplication. Its repair knows how to represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take near deduplication to the workbench

A claim about near deduplication now exists on the page; the laboratory must be able to contradict it. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running near deduplication, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the near deduplication result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Quality Filtering — Remove Noise Without Defining Humanity Away](../181-quality-filtering/README.md)
