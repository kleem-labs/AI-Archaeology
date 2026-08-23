# Excavation 017 — Probability — Counting What We Do Not Know

<!-- book-prose-v2 -->

> **PART III — LEARNING FROM ERROR**
>
> The machine can move information. It still cannot admit uncertainty, measure a mistake, or use that mistake to change itself.

The Transformer has begun to infer hidden causes from the footprints of language. But inference without certainty is dangerous: the same rustle may have been made by a tiger, a deer, or only the wind.

A careful builder would first avoid adding machinery and choose the most common cause and declare certainty.

The shortcut appears to retain everything probability needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

The world supplies the one comparison the shortcut hoped never to face: this works until the rare tiger arrives. Refusing to decide is safer intellectually but useless when the camp must act.

The counterexample teaches probability. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: keep every plausible outcome and give each a share of belief. Count comparable past observations, then divide the count for one outcome by the total.

Now—and not earlier—we may introduce **Probability**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to choose the most common cause and declare certainty., and the case answers that this works until the rare tiger arrives. Refusing to decide is safer intellectually but useless when the camp must act. With the narrow repair—to keep every plausible outcome and give each a share of belief. Count comparable past observations, then divide the count for one outcome by the total—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Probability returns to the same counterexample, replaces the attempt to choose the most common cause and declare certainty. with the responsibility to keep every plausible outcome and give each a share of belief. Count comparable past observations, then divide the count for one outcome by the total, and must succeed where the shortcut failed.

## The calculation hidden inside probability

Before Probability receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

A tracker saw tigers after 2 of 10 comparable rustles. The raw count 2 means little without 10 opportunities. Dividing gives 0.2: under this evidence, two tenths of such rustles preceded a tiger.

### Names for pieces we have already used

**A** is the uncertain event we need to discuss.
The numerator counts observations where A occurred.
The denominator counts all comparable opportunities, because an isolated count has no scale.
Division turns the count into a share between zero and one.
**P(A)** names that evidence-dependent share, not a guarantee.

### Why no cheaper operation does the same job

[Division](../../MATHEMATICAL_MOVES.md#division) turns a tiger count into a share of comparable encounters. The count alone grows when we watch longer even if the underlying chance is unchanged.
[Probability](../../MATHEMATICAL_MOVES.md#probability) preserves several possible causes as parts of one whole instead of forcing certainty from incomplete evidence.

The notation is finally shorter than the story that created it:

$$
P(A)=\frac{\text{times }A\text{ occurred}}{\text{comparable observations}}
$$

## Probability beyond this one case

Probability is a weather forecast: not a promise, but an honest description of uncertainty that can still guide action.

## Where probability runs out

Probabilities depend on evidence and assumptions. When new evidence arrives, the shares must change.

The boundary can be predicted from the construction itself. Probability performs the repair to keep every plausible outcome and give each a share of belief. Count comparable past observations, then divide the count for one outcome by the total; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

## Take probability to the workbench

Move probability from imagination to evidence by making the shortcut fail under controlled inputs. Build the wrong idea first, break it, then use [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running probability, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the probability result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
