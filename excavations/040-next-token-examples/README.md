# Excavation 040 — Next-Token Examples — One Sentence Becomes Many Lessons

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Information Theory](../../MATHEMATICS_ATLAS.md#information) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Language models and useful answers

Causal masking prevents the learner from reading future answers. The model still needs to turn one sentence into all the honest prediction questions hidden inside it.

At the Clockwork Scriptorium, the mechanist returns to the sentence-wheel. Yesterday's instrument still lies open, so the first move asks for no new magic: treat an entire sentence as one training example with one answer.

The mechanist repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: most of its transitions provide no learning signal. The failure is stable enough to become evidence.

*The mechanist sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   treat an entire sentence as one… most of its transitions provide no…
            \        /
             \      /
              shift the sequence by one position so…
```

Across the sentence-wheel, the old path and the repaired path run side by side. One carries “treat an entire sentence as one training example with one answer”; the other knows how to shift the sequence by one position so every visible prefix predicts the token immediately following it. When the failure—most of its transitions provide no learning signal—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to next-token examples. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: shift the sequence by one position so every visible prefix predicts the token immediately following it. This problem and its repair will travel under the name **Next-Token Examples**, but the name carries no knowledge the scene has not earned.

What changed on the sentence-wheel can be said without symbols. Before, the method could only treat an entire sentence as one training example with one answer; now it can also shift the sequence by one position so every visible prefix predicts the token immediately following it. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

<!-- memory-film-v1:start -->
> **Memory realm 4 of 18 — [Clockwork Scriptorium](../../MEMORY_PALACE.md#realm-4)**
>
> **The question carried into this chamber:** What fails if we treat an entire sentence as one training example with one answer?

## When the chamber changes

The Next-Token Examples room does not ask you to memorize its name. It asks you to watch one object change.

First hold the failed picture still: The bell follows the tempting path—treat an entire sentence as one training example with one answer. Then the evidence answers: most of its transitions provide no learning signal.

Now let the chamber move: The mechanist changes one moving part. The bell can now shift the sequence by one position so every visible prefix predicts the token immediately following it.

The object that should remain after the terminology disappears is **the next-token examples bell mounted on the sentence-wheel**.

> **Memory seal — Next-Token Examples**
>
> Next-Token Examples keeps the missing power: shift the sequence by one position so every visible prefix predicts the token immediately following it.

Give the idea a bodily path: Touch the next-token examples bell in imagination: trace its outline with one finger, cover it with your palm, then uncover only the repaired path.
<!-- memory-film-v1:end -->

## The calculation hidden inside next-token examples

The mechanist carries the next-token examples scene to the sentence-wheel. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Padding and document boundaries can create false targets unless their losses are masked.

Tokens [the,cat,slept] become inputs [the,cat] and targets [cat,slept]. One forward pass therefore asks “after the?” and “after the cat?” at separate positions.

### Naming what is already on the table

**t₀…t_n** are consecutive tokens from one observed sequence.
Input x stops one token early because each position needs an answer to its right.
Target y starts one token later so y_i is exactly the next token after x_i.
The shared length lets one forward pass create a supervised lesson at every position.

### Why the melody needs these exact notes

[Parentheses](../../MATHEMATICAL_MOVES.md#brackets) keep each ordered token sequence intact; summing the tokens would destroy both identity and order.
[The shifted indices](../../MATHEMATICAL_MOVES.md#indices) remove the final token from inputs and the first token from targets, so target position i is exactly the next token after input position i.

Cover the prose about next-token examples and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
x=(t_0,\ldots,t_{n-1})
$$

$$
y=(t_1,\ldots,t_n)
$$

The equation arrives after every operation has a job.

## Next-Token Examples beyond this one case

A reading teacher pauses after every word, not only at the final period.

## Return to the sentence-wheel

Rebuild the next-token examples scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 041](../041-logits/README.md)
