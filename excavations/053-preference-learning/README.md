# Excavation 053 — Preference Learning — When Several Answers Are Correct but Not Equally Helpful

<!-- book-prose-v2 -->

Instruction tuning turns continuation into cooperation on demonstrated tasks. Several answers can obey the same instruction while differing sharply in clarity, honesty, safety, and usefulness.

A careful builder would first avoid adding machinery and write one perfect target response for every prompt and train only to imitate it.

The shortcut appears to retain everything preference learning needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

Reality now asks a question the retained information cannot answer: many answers can be valid. A single target penalizes harmless alternatives and cannot express that answer A is preferred to B without being the only possible answer.

The counterexample teaches preference learning. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy.

Now—and not earlier—we may introduce **Preference Learning**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to write one perfect target response for every prompt and train only to imitate it, and the case answers that many answers can be valid. A single target penalizes harmless alternatives and cannot express that answer A is preferred to B without being the only possible answer. With the narrow repair—to collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Preference Learning returns to the same counterexample, replaces the attempt to write one perfect target response for every prompt and train only to imitate it with the responsibility to collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy, and must succeed where the shortcut failed.

## The calculation hidden inside preference learning

Before Preference Learning receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

For “How do I reset my router?”, answer A gives three safe ordered steps; answer B gives twenty vague paragraphs. A reviewer chooses A. Repeated comparisons teach concision and usefulness without declaring one exact sentence mandatory.

### Names for pieces we have already used

The reward scores two responses to the same prompt. Their difference matters, not the absolute score. The logistic function turns that difference into a preference probability; larger positive differences favor the chosen answer.

### Why no cheaper operation does the same job

[rA−rB](../../MATHEMATICAL_MOVES.md#subtraction) discards any common reward offset and keeps only which answer reviewers prefer and by how much.
[The inner negative](../../MATHEMATICAL_MOVES.md#negative-sign) makes larger preference gaps reduce the exponential term, so A's probability rises rather than falls.
[Exponentiation](../../MATHEMATICAL_MOVES.md#exponential) turns an unbounded reward gap into positive odds; adding one and [taking the reciprocal](../../MATHEMATICAL_MOVES.md#division) squeeze the result between zero and one without changing order.

Every symbol in Preference Learning can now be read back into an action already performed. The whole procedure fits in one line:

$$
P(A\succ B)=\frac{1}{1+\exp(-(r_A-r_B))}
$$

## Where preference learning runs out

Human preferences conflict, annotators make mistakes, and optimizing a learned reward can exploit its blind spots.

The boundary can be predicted from the construction itself. Preference Learning performs the repair to collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

## Take preference learning to the workbench

Move preference learning from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running preference learning, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the preference learning result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 054](../054-retrieval-augmented-generation/README.md)
