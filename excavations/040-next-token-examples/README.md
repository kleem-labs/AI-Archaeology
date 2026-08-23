# Excavation 040 — Next-Token Examples — One Sentence Becomes Many Lessons

<!-- book-prose-v2 -->

Causal masking prevents the learner from reading future answers. The model still needs to turn one sentence into all the honest prediction questions hidden inside it.

If the old idea can be stretched one step farther, we should treat an entire sentence as one training example with one answer.

If the proposal works on every relevant case, next-token examples is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

Now keep that rule fixed and let the difficult case enter: most of its transitions provide no learning signal.

Nothing magical creates next-token examples. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: shift the sequence by one position so every visible prefix predicts the token immediately following it.

This boundary between the failed rule and its repair is the subject later work calls **Next-Token Examples**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize next-token examples; try to break it by subtraction. Remove the part that knows how to shift the sequence by one position so every visible prefix predicts the token immediately following it, leaving only the attempt to treat an entire sentence as one training example with one answer.. What returns is not a vague weakness but the original contradiction: most of its transitions provide no learning signal. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to treat an entire sentence as one training example with one answer. receives the same test as the rule to shift the sequence by one position so every visible prefix predicts the token immediately following it. Their different outcomes reveal what next-token examples contributes without asking the reader to trust historical convention.

## The calculation hidden inside next-token examples

Do not read the coming Next-Token Examples line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Padding and document boundaries can create false targets unless their losses are masked.

Tokens [the,cat,slept] become inputs [the,cat] and targets [cat,slept]. One forward pass therefore asks “after the?” and “after the cat?” at separate positions.

### Names for pieces we have already used

**t₀…t_n** are consecutive tokens from one observed sequence.
Input x stops one token early because each position needs an answer to its right.
Target y starts one token later so y_i is exactly the next token after x_i.
The shared length lets one forward pass create a supervised lesson at every position.

### Why no cheaper operation does the same job

[Parentheses](../../MATHEMATICAL_MOVES.md#brackets) keep each ordered token sequence intact; summing the tokens would destroy both identity and order.
[The shifted indices](../../MATHEMATICAL_MOVES.md#indices) remove the final token from inputs and the first token from targets, so target position i is exactly the next token after input position i.

The notation is finally shorter than the story that created it:

$$
x=(t_0,\ldots,t_{n-1})
$$

$$
y=(t_1,\ldots,t_n)
$$

The equation arrives after every operation has a job.

## Next-Token Examples beyond this one case

A reading teacher pauses after every word, not only at the final period.

## Take next-token examples to the workbench

A mathematical story about next-token examples earns trust only when the failed and repaired paths can both be reproduced. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running next-token examples, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the next-token examples result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 041](../041-logits/README.md)
