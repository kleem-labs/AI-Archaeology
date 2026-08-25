# Excavation 041 — Logits — Let Every Vocabulary Token Compete

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Language models and useful answers

Shifted inputs and targets create one lesson at every position. The Transformer answers each lesson with a contextual vector, but a vector is not yet a competition among words such as tiger, river, or sleeps.

The previous discovery reaches the Clockwork Scriptorium carrying one unfinished problem. Beside the sentence-wheel, the mechanist first tries to choose the nearest input embedding directly.

There is good reason to begin this way. If we choose the nearest input embedding directly, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: that restricts the scoring rule and hides how every vocabulary candidate should compete.

This failure cannot be repaired by performing the instruction to choose the nearest input embedding directly more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the sentence-wheel; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to use a learned linear map to produce one raw score for every vocabulary item. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Logits**. The name is simply a handle for the distinction already reconstructed.

## The calculation hidden inside logits

The mechanist carries the logits scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Logits have no standalone probability meaning and can shift together without changing the final distribution.

After reading “the striped animal is a,” the model holds one contextual description. Every vocabulary candidate now presents a learned question: how well does this description support *tiger*, *river*, *sleeping*, and so on? Matching the same context against each candidate produces one raw score per word. Those scores are logits; they are competitors, not probabilities yet.

### Naming what is already on the table

**h** is one contextual token vector containing what the Transformer currently knows.
**W_vocab** has one scoring direction per vocabulary candidate; multiplication compares h with all candidates at once.
**b** allows each token a learned baseline tendency.
**ℓ_i** is the resulting unconstrained logit for candidate i—not yet a probability.

### Why the melody needs these exact notes

[Multiplication by Wvocab](../../MATHEMATICAL_MOVES.md#multiplication) lets every contextual feature contribute a learned amount to every vocabulary candidate's score.
[The bias](../../MATHEMATICAL_MOVES.md#addition) gives each vocabulary token a learned baseline tendency even when the contextual vector is zero.
The index i selects one output candidate; it does not mean the token with the largest ID should win. See [indices](../../MATHEMATICAL_MOVES.md#indices).

The calculation borrows several gestures already encountered elsewhere: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the joining river**—separate contributions meet without losing where they came from. logits feels new because the objects are new; the gestures remain recognizably human.

The sentence-wheel already contains the complete logits mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
\ell_i=hW_{\text{vocab}}+b
$$

The equation arrives after every operation has a job.

## Logits beyond this one case

Judges first assign unconstrained scores to every contestant before those scores are converted into shares.

## Return to the sentence-wheel

Rebuild the logits scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 042](../042-vocabulary-probabilities/README.md)
