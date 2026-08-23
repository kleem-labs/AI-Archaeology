# Excavation 041 — Logits — Let Every Vocabulary Token Compete

<!-- book-prose-v2 -->

Shifted inputs and targets create one lesson at every position. The Transformer answers each lesson with a contextual vector, but a vector is not yet a competition among words such as tiger, river, or sleeps.

A careful builder would first avoid adding machinery and choose the nearest input embedding directly.

The shortcut appears to retain everything logits needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

The world supplies the one comparison the shortcut hoped never to face: that restricts the scoring rule and hides how every vocabulary candidate should compete.

The counterexample teaches logits. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: use a learned linear map to produce one raw score for every vocabulary item.

Now—and not earlier—we may introduce **Logits**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to choose the nearest input embedding directly., and the case answers that that restricts the scoring rule and hides how every vocabulary candidate should compete. With the narrow repair—to use a learned linear map to produce one raw score for every vocabulary item—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Logits returns to the same counterexample, replaces the attempt to choose the nearest input embedding directly. with the responsibility to use a learned linear map to produce one raw score for every vocabulary item, and must succeed where the shortcut failed.

## The calculation hidden inside logits

Before Logits receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Logits have no standalone probability meaning and can shift together without changing the final distribution.

After reading “the striped animal is a,” the model holds one contextual description. Every vocabulary candidate now presents a learned question: how well does this description support *tiger*, *river*, *sleeping*, and so on? Matching the same context against each candidate produces one raw score per word. Those scores are logits; they are competitors, not probabilities yet.

### Names for pieces we have already used

**h** is one contextual token vector containing what the Transformer currently knows.
**W_vocab** has one scoring direction per vocabulary candidate; multiplication compares h with all candidates at once.
**b** allows each token a learned baseline tendency.
**ℓ_i** is the resulting unconstrained logit for candidate i—not yet a probability.

### Why no cheaper operation does the same job

[Multiplication by Wvocab](../../MATHEMATICAL_MOVES.md#multiplication) lets every contextual feature contribute a learned amount to every vocabulary candidate's score.
[The bias](../../MATHEMATICAL_MOVES.md#addition) gives each vocabulary token a learned baseline tendency even when the contextual vector is zero.
The index i selects one output candidate; it does not mean the token with the largest ID should win. See [indices](../../MATHEMATICAL_MOVES.md#indices).

The notation is finally shorter than the story that created it:

$$
\ell_i=hW_{\text{vocab}}+b
$$

The equation arrives after every operation has a job.

## Logits beyond this one case

Judges first assign unconstrained scores to every contestant before those scores are converted into shares.

## Take logits to the workbench

Move logits from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running logits, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the logits result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 042](../042-vocabulary-probabilities/README.md)
