# Excavation 041 — Logits — Let Every Vocabulary Token Compete

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Shifted inputs and targets create one lesson at every position. The Transformer answers each lesson with a contextual vector, but a vector is not yet a competition among words such as tiger, river, or sleeps.

Morning reaches the Clockwork Scriptorium before anyone has a name for today's difficulty. Beside the sentence-wheel, the mechanist tries the smallest continuation of what already works: choose the nearest input embedding directly.

At the edge of the sentence-wheel, the shortcut produces its consequence: that restricts the scoring rule and hides how every vocabulary candidate should compete. That consequence, not a textbook, earns the next move.

*The mechanist sketches the break before changing it:*

```text
OLD PATH:  request ──▶ choose the nearest input embedding… ──▶ that restricts the scoring rule and…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ use a learned linear map to produce… ──▶ accountable result
```

The mechanist covers the new mark and the old contradiction returns: that restricts the scoring rule and hides how every vocabulary candidate should compete. The cover is lifted, restoring the ability to use a learned linear map to produce one raw score for every vocabulary item, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason logits exists.

What must change for logits is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: use a learned linear map to produce one raw score for every vocabulary item. That threshold is where **Logits** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In logits, that memory takes a precise form: whenever that restricts the scoring rule and hides how every vocabulary candidate should compete, preserve enough structure to use a learned linear map to produce one raw score for every vocabulary item.

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
