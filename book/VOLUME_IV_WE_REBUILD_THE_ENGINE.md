# Volume IV — We Rebuild the Engine

The research loop has earned the right to propose changes. We return to the tiny language model, freeze one honest baseline, and rebuild its engine one measured bottleneck at a time without surrendering a reference path.

One discovery will create the need for the next; the object under construction never resets.

In this volume:

- [Part XII — Rebuilding the Engine Without Breaking the System](#part-xii--rebuilding-the-engine-without-breaking-the-system)

---

## Part XII — Rebuilding the Engine Without Breaking the System

The bounded loop gives us permission to improve—not permission to guess. We freeze the tiny language model, measure where its time and memory go, and replace one bottleneck at a time while the original path remains available to challenge every faster one.

---

### Excavation 151 — A Reproducible Baseline — Improve Something That Actually Exists

<!-- book-prose-v2 -->

The bounded loop can approve a candidate, but approval is meaningless if nobody can reconstruct the system it is supposed to improve.

Before naming anything new, try to keep the final score and the model file; those should be enough to compare the next idea.

Its appeal is not ignorance but economy. A Reproducible Baseline should not be added until an observation exposes the exact thing the older procedure cannot preserve.

One counterexample is enough to expose the missing job: a rerun changes the data order, random seed, tokenizer revision, and library behavior. Its score moves even though the proposed improvement was never applied.

Notice what the counterexample has accomplished for a reproducible baseline. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline.

Humanity eventually gathered this problem and its repairs under the name **A Reproducible Baseline**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace a reproducible baseline with the old instruction to keep the final score and the model file; those should be enough to compare the next idea. The result is again that a rerun changes the data order, random seed, tokenizer revision, and library behavior. Its score moves even though the proposed improvement was never applied. Put back only the requirement to freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when a reproducible baseline is introduced. The same evidence that defeated the attempt to keep the final score and the model file; those should be enough to compare the next idea is presented again. Only the ability to freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### Improve Something That Actually Exists

Run the same tiny tiger-language model twice from the recorded seed. Only after its loss curve and held-out score agree do we permit one component to change.

Run the a reproducible baseline scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

#### The calculation hidden inside a reproducible baseline

Before A Reproducible Baseline receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

The frozen run scores 2.4 and the candidate scores 2.1 on the same loss test. Looking at 2.1 alone cannot tell you whether anything improved. Remove the old 2.4 from the new 2.1: the remaining −0.3 is the candidate's change. We call the old measurement m_baseline, the new one m_candidate, and the remainder delta m only after doing that comparison.

m_baseline is the frozen model's measurement; m_candidate is measured by the same procedure; delta m names only the change between them.

##### Why no cheaper operation does the same job

[Subtraction](../MATHEMATICAL_MOVES.md#subtraction) removes the common baseline and isolates the candidate's change. Addition would make two large scores look impressive even when they are identical. The order fixes the sign: positive means the candidate raised this metric.

Every symbol in A Reproducible Baseline can now be read back into an action already performed. The whole procedure fits in one line:

$$
\Delta m=m_{\text{candidate}}-m_{\text{baseline}}
$$

#### Where a reproducible baseline runs out

Reproducibility makes differences attributable; it does not tell us which component is worth changing.

Why does that boundary remain? A Reproducible Baseline was built for one responsibility: freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take a reproducible baseline to the workbench

The argument for a reproducible baseline is still provisional until a runnable case can make it fail. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running a reproducible baseline, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the a reproducible baseline result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/151-reproducible-baseline/README.md).*

---

### Excavation 152 — Profiling — Measure Where the Time Went

<!-- book-prose-v2 -->

A reproducible baseline gives us a trustworthy before-state. Its first run is too slow for the ranger station, but a total runtime does not identify the guilty stage.

The first defensible move is to optimize the largest-looking matrix because attention is famous for being expensive.

There is a real principle behind this restraint: the complexity of profiling must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Now keep that rule fixed and let the difficult case enter: the device spends much of the run waiting for data and moving tensors. Making one matrix faster barely changes the wall clock.

That distinction is the hinge on which profiling turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: measure data loading, computation, communication, and idle time separately before choosing a repair.

We have earned the chapter's shorter name: **Profiling**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that profiling is necessary rather than decorative. Delete its new responsibility and use the earlier plan to optimize the largest-looking matrix because attention is famous for being expensive. Immediately, the device spends much of the run waiting for data and moving tensors. Making one matrix faster barely changes the wall clock. Reintroduce the single job to measure data loading, computation, communication, and idle time separately before choosing a repair. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can measure data loading, computation, communication, and idle time separately before choosing a repair. Because the old plan to optimize the largest-looking matrix because attention is famous for being expensive is the only displaced piece, the reader can locate exactly where profiling changes the outcome.

#### Measure Where the Time Went

A 100 ms step contains 35 ms of loading, 45 ms of compute, 10 ms of communication, and 10 ms idle. The first engineering question is now visible in numbers.

The name profiling is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### The calculation hidden inside profiling

Do not read the coming Profiling line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Start a stopwatch with one training step. Loading ends at 35 ms; computation then carries the clock to 80; communication to 90; idle synchronization to 100. These are consecutive pieces of one elapsed interval, so you join them end to end. The name T_step is simply the final reading after T_data, T_compute, T_communication, and T_idle have all contributed.

Each T names elapsed time assigned to one non-overlapping stage of the same training step.

##### Why no cheaper operation does the same job

[Addition](../MATHEMATICAL_MOVES.md#addition) is forced because these non-overlapping durations occur along one wall-clock path and accumulate into total time. Multiplication would claim that doubling one stage scales every other stage. The equality is valid only when the measured categories cover the step without overlap.

Every symbol in Profiling can now be read back into an action already performed. The whole procedure fits in one line:

$$
T_{\text{step}}=T_{\text{data}}+T_{\text{compute}}+T_{\text{communication}}+T_{\text{idle}}
$$

#### Where profiling runs out

A profile describes this workload on this hardware; changing sequence length or batch size can move the bottleneck.

The weakness is not an accidental footnote. Every operation in profiling serves the narrower purpose to measure data loading, computation, communication, and idle time separately before choosing a repair; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take profiling to the workbench

Understanding profiling now means predicting its intermediate results before asking software for an answer. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running profiling, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the profiling result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/152-profiling/README.md).*

---

### Excavation 153 — The Input Pipeline — Stop Making the Accelerator Wait

<!-- book-prose-v2 -->

Profiling reveals that the accelerator repeatedly waits for the next token batch. The model is ready, but its evidence is still being read and prepared.

At this point the shortest path seems to be to load a batch, wait until loading finishes, compute it, and only then begin loading the next one.

This is how the input pipeline ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

The world supplies the one comparison the shortcut hoped never to face: data time and compute time are paid sequentially on every step, leaving expensive compute hardware idle.

The wrong answer makes the need for the input pipeline inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering.

The usual name, **The Input Pipeline**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to load a batch, wait until loading finishes, compute it, and only then begin loading the next one produces the observed failure: data time and compute time are paid sequentially on every step, leaving expensive compute hardware idle. Starting with the repaired demand to prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering preserves the information the shortcut lost. The subject of the input pipeline lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering instead of merely trying to load a batch, wait until loading finishes, compute it, and only then begin loading the next one. That controlled contrast is what turns a plausible explanation of the input pipeline into an understandable derivation.

#### Stop Making the Accelerator Wait

If loading takes 35 ms and compute 45 ms, serial work costs 80 ms. Once overlapped, a steady-state step is governed mainly by the slower 45 ms stage.

There are now two histories of this the input pipeline case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

#### The calculation hidden inside the input pipeline

Before The Input Pipeline receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Now give the ranger station's data loader and accelerator separate workers and start both together. Loading finishes after 35 ms, but the next step is still waiting for computation at 45 ms. The pair is ready when the slower worker finishes—not after 35+45 ms. That finishing time is what T_overlapped records; the approximation sign leaves room for pipeline startup and coordination.

The two times describe stages allowed to run concurrently after the pipeline is filled.

##### Why no cheaper operation does the same job

[Maximum](../MATHEMATICAL_MOVES.md#maximum) appears because concurrent stages finish when the slower one finishes. Adding would describe serial execution—the failed design. [Approximation](../MATHEMATICAL_MOVES.md#approximation) admits startup, synchronization, and overhead that prevent perfect overlap.

Every symbol in The Input Pipeline can now be read back into an action already performed. The whole procedure fits in one line:

$$
T_{\text{overlapped}}\approx\max(T_{\text{data}},T_{\text{compute}})
$$

#### Where the input pipeline runs out

Prefetching can hide latency, not unlimited data cost; workers, memory, or storage bandwidth can become the next limit.

Look back at what the input pipeline actually preserves: it can prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

#### Take the input pipeline to the workbench

The reader has reconstructed the input pipeline in words; the workbench tests whether those words specify a real procedure. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running the input pipeline, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the the input pipeline result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/153-input-pipeline/README.md).*

---

### Excavation 154 — Sequence Packing — Stop Training on Empty Space

<!-- book-prose-v2 -->

The input pipeline now keeps the device busy. Inspection shows that many of the tokens occupying each fixed rectangle are padding rather than language.

We can postpone invention if we simply pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste.

If the proposal works on every relevant case, sequence packing is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

Its hidden assumption becomes visible as soon as we observe that the loss ignores padding, but attention and matrix multiplication still spend time and memory carrying those empty positions.

Nothing magical creates sequence packing. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: pack several short examples into each fixed-length row and mask their boundaries so examples cannot read one another.

This boundary between the failed rule and its repair is the subject later work calls **Sequence Packing**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize sequence packing; try to break it by subtraction. Remove the part that knows how to pack several short examples into each fixed-length row and mask their boundaries so examples cannot read one another, leaving only the attempt to pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste. What returns is not a vague weakness but the original contradiction: the loss ignores padding, but attention and matrix multiplication still spend time and memory carrying those empty positions. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste receives the same test as the rule to pack several short examples into each fixed-length row and mask their boundaries so examples cannot read one another. Their different outcomes reveal what sequence packing contributes without asking the reader to trust historical convention.

#### Stop Training on Empty Space

Lengths 6, 5, 3, and 2 fill two rows of length 8 exactly. Padding falls from 16 allocated positions with 6 empty to 16 positions with none empty.

Hold the setting, evidence, and desired outcome fixed while testing sequence packing. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

#### The calculation hidden inside sequence packing

Do not read the coming Sequence Packing line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Draw two rows with eight boxes each: sixteen paid positions. Place sequences of lengths 6 and 2 in the first row, then 5 and 3 in the second. All sixteen boxes now contain real tokens. To ask what share of the paid space teaches the model, put useful boxes over paid boxes: 16/16. Eta_pack is only a short name for that useful fraction.

The numerator counts language tokens that create lessons; the denominator counts every position for which hardware reserves work.

##### Why no cheaper operation does the same job

[Division](../MATHEMATICAL_MOVES.md#division) forms the useful share per allocated position, making batches of different sizes comparable. A raw token count would reward larger batches even if their wasted fraction were worse. The ratio stays between zero and one because real tokens cannot exceed allocated positions.

Every symbol in Sequence Packing can now be read back into an action already performed. The whole procedure fits in one line:

$$
\eta_{\text{pack}}=\frac{N_{\text{real tokens}}}{N_{\text{allocated positions}}}
$$

#### Where sequence packing runs out

Packing improves utilization only if masks and position resets prevent cross-example contamination.

This is where sequence packing runs out for a causal reason. We gave it enough structure to pack several short examples into each fixed-length row and mask their boundaries so examples cannot read one another, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take sequence packing to the workbench

A mathematical story about sequence packing earns trust only when the failed and repaired paths can both be reproduced. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running sequence packing, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the sequence packing result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/154-sequence-packing/README.md).*

---

### Excavation 155 — Rotary Position Embeddings — Let Distance Enter the Match

<!-- book-prose-v2 -->

Packed training supplies dense sequences, but the learned absolute position cards from our first GPT bind each slot to a private identity rather than making relative displacement part of the query-key match.

The previous discovery seems almost sufficient: we could learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples.

The shortcut appears to retain everything rotary position embeddings needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

Then a case arrives in which convenience and truth separate: moving the same phrase from positions 10–12 to 110–112 changes every position vector although the internal distances are unchanged.

The counterexample teaches rotary position embeddings. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference.

Now—and not earlier—we may introduce **Rotary Position Embeddings**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples, and the case answers that moving the same phrase from positions 10–12 to 110–112 changes every position vector although the internal distances are unchanged. With the narrow repair—to rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Rotary Position Embeddings returns to the same counterexample, replaces the attempt to learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples with the responsibility to rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference, and must succeed where the shortcut failed.

#### Let Distance Enter the Match

Rotate the two coordinates of tiger by angle mθ and river by nθ. Their match depends on (m−n)θ, so shifting both tokens together preserves their separation signal.

A formula for rotary position embeddings is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

#### The calculation hidden inside rotary position embeddings

Before Rotary Position Embeddings receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Imagine the pair of coordinates as a clock hand beginning at [1,0]. At position one, a quarter-turn sends it to [0,1]; at position two, another quarter-turn sends it to [−1,0]. The hand's length never changes—only its angle does. Multiplying position p by the chosen turn theta tells us the total angle; the four cosine-and-sine entries record how any starting pair must contribute to its two rotated coordinates.

p is token position, theta is one rotation frequency, and R rotates one coordinate pair without changing its length.

##### Why no cheaper operation does the same job

[Function application](../MATHEMATICAL_MOVES.md#function-application) applies the same rotation rule at each position. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) mixes the two coordinates according to cosine and sine; [addition](../MATHEMATICAL_MOVES.md#addition) combines their signed contributions. Squaring or adding p would change magnitude instead of encoding position as an angle whose differences survive a shared shift.

Every symbol in Rotary Position Embeddings can now be read back into an action already performed. The whole procedure fits in one line:

$$
R(p\theta)=\begin{bmatrix}\cos(p\theta)&-\sin(p\theta)\\\sin(p\theta)&\cos(p\theta)\end{bmatrix}
$$

#### Where rotary position embeddings runs out

RoPE supplies structured relative position, but distances far beyond training still produce unfamiliar phases.

The boundary can be predicted from the construction itself. Rotary Position Embeddings performs the repair to rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

#### Take rotary position embeddings to the workbench

Move rotary position embeddings from imagination to evidence by making the shortcut fail under controlled inputs. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running rotary position embeddings, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the rotary position embeddings result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/155-rotary-position/README.md).*

---

### Excavation 156 — Relative Position Bias — What Should Happen Beyond the Seen Window?

<!-- book-prose-v2 -->

Rotary position makes displacement visible inside the attention match. When the station tests much longer sequences, the model must rank relationships at separations absent from training.

The least expensive next move is to trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there.

The proposal deserves a fair hearing. For relative position bias, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The proposal breaks for a specific reason, not by authority: a mathematically defined position is not necessarily a learned behavior; attention can become erratic at unfamiliar separations.

The failure changes the question behind relative position bias. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation.

Only at this point does the inherited name **Relative Position Bias** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of relative position bias by mentally removing the repair. We fall back to the proposal to trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there; then a mathematically defined position is not necessarily a learned behavior; attention can become erratic at unfamiliar separations. Restore only the ability to add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there to requiring the system to add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to relative position bias.

#### What Should Happen Beyond the Seen Window

For one head with slope 0.1, a key 2 places back receives −0.2 while a key 20 places back receives −2.0 before softmax. Content can overcome the penalty, but distance has a predictable cost.

Put the old procedure beside relative position bias. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

#### The calculation hidden inside relative position bias

Do not read the coming Relative Position Bias line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Suppose tiger matches one key with content score 3.0. The key is two places away, and we decide that each place should cost 0.1, so distance contributes 2×0.1=0.2. Removing that cost leaves 2.8. A key twenty places away pays 20×0.1=2.0 and keeps 1.0. We now name the original content score s_ij, the price per place m, and the adjusted result s-prime.

s_ij is the content match, |i−j| is token separation, m is this head's nonnegative distance slope, and s-prime is the adjusted score.

##### Why no cheaper operation does the same job

[Subtraction](../MATHEMATICAL_MOVES.md#subtraction) lowers rather than raises distant matches. [Absolute value](../MATHEMATICAL_MOVES.md#absolute-value) keeps separation size while discarding left-versus-right direction in this bias. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) lets slope m control the price per position; adding a fixed m would not make farther tokens cost more.

Every symbol in Relative Position Bias can now be read back into an action already performed. The whole procedure fits in one line:

$$
s_{ij}^{\prime}=s_{ij}-m\lvert i-j\rvert
$$

#### Where relative position bias runs out

A fixed distance preference can suppress a decisive remote clue and is an architectural bias, not universal truth.

The limit follows from the job assigned to relative position bias. Its repair knows how to add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

#### Take relative position bias to the workbench

A claim about relative position bias now exists on the page; the laboratory must be able to contradict it. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running relative position bias, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the relative position bias result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/156-relative-position-bias/README.md).*

---

### Excavation 157 — The KV Cache — Stop Re-reading the Entire Past

<!-- book-prose-v2 -->

Relative position now behaves predictably, but autoregressive generation still reruns the Transformer over the full prefix after appending each token.

For a moment, remain loyal to the simplest proposal: at step t, recompute keys and values for positions 1 through t because the prefix is presented again.

Its appeal is not ignorance but economy. The KV Cache should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Reality now asks a question the retained information cannot answer: past token representations are unchanged in causal decoding, so the same projections are calculated repeatedly while one new token is added.

Notice what the counterexample has accomplished for the kv cache. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache.

Humanity eventually gathered this problem and its repairs under the name **The KV Cache**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace the kv cache with the old instruction to at step t, recompute keys and values for positions 1 through t because the prefix is presented again. The result is again that past token representations are unchanged in causal decoding, so the same projections are calculated repeatedly while one new token is added. Put back only the requirement to store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when the kv cache is introduced. The same evidence that defeated the attempt to at step t, recompute keys and values for positions 1 through t because the prefix is presented again is presented again. Only the ability to store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### Stop Re-reading the Entire Past

Generating token 101 computes one new key and value, then reads the 100 cached pairs. It does not rebuild pairs 1 through 100.

Run the the kv cache scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

#### The calculation hidden inside the kv cache

Before The KV Cache receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

At token 101, write the hundred old keys on cards and compute one new card. Nothing on the old cards has changed, so combining must mean placing card 101 after cards 1 through 100—not adding their numbers together. K_1:t−1 names the ordered stack already present, k_t the one new card, and K_1:t the longer stack after appending.

K_1:t−1 is the unchanged past cache, k_t is the newly computed key, and K_1:t is the cache available to the current query.

##### Why no cheaper operation does the same job

[Function application](../MATHEMATICAL_MOVES.md#function-application) names one append operation. Appending preserves order and old values; [addition](../MATHEMATICAL_MOVES.md#addition) would numerically blend keys and destroy which token produced each one. The indices show that only position t is new.

Every symbol in The KV Cache can now be read back into an action already performed. The whole procedure fits in one line:

$$
K_{1:t}=\mathrm{append}(K_{1:t-1},k_t)
$$

#### Where the kv cache runs out

Because every past key and value must remain available, saved computation becomes growing memory and memory-bandwidth cost, especially for long contexts and many users.

Why does that boundary remain? The KV Cache was built for one responsibility: store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take the kv cache to the workbench

The argument for the kv cache is still provisional until a runnable case can make it fail. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running the kv cache, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the the kv cache result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/157-kv-cache/README.md).*

---

### Excavation 158 — Multi-Query Attention — Why Cache Separate Copies for Every Head?

<!-- book-prose-v2 -->

Caching turns repeated arithmetic into memory reads. Profiling now shows decoding limited by loading separate key and value histories for every attention head.

Nothing yet appears to demand a new invention. We can preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections.

There is a real principle behind this restraint: the complexity of multi-query attention must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The decisive test is this: the caches grow with both sequence length and head count, and loading them dominates the arithmetic for one new token.

That distinction is the hinge on which multi-query attention turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: keep many query heads but share one key head and one value head across them.

We have earned the chapter's shorter name: **Multi-Query Attention**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that multi-query attention is necessary rather than decorative. Delete its new responsibility and use the earlier plan to preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections. Immediately, the caches grow with both sequence length and head count, and loading them dominates the arithmetic for one new token. Reintroduce the single job to keep many query heads but share one key head and one value head across them. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can keep many query heads but share one key head and one value head across them. Because the old plan to preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections is the only displaced piece, the reader can locate exactly where multi-query attention changes the outcome.

#### Why Cache Separate Copies for Every Head

Eight query experts ask eight different questions of the same cached catalog. Cache entries fall from eight key-value pairs per token to one pair per token.

The name multi-query attention is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### The calculation hidden inside multi-query attention

Do not read the coming Multi-Query Attention line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Take one layer with 100 remembered tokens. If each KV head stores 64 coordinates, one head needs 100×64 coordinate slots for keys and the same again for values. Eight heads need eight copies of those slots. The three counts—tokens L, KV heads H_KV, and width d_h—multiply because every choice from one count is paired with every choice from the others.

L is cached sequence length, H_KV is the number of key-value heads, and d_h is the width stored per head.

##### Why no cheaper operation does the same job

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) appears because every token stores every KV head's coordinates: doubling any factor doubles memory. [Proportionality](../MATHEMATICAL_MOVES.md#proportionality) omits fixed factors such as both K and V, bytes per number, layers, and batch size while preserving the scaling argument.

Every symbol in Multi-Query Attention can now be read back into an action already performed. The whole procedure fits in one line:

$$
M_{\text{KV}}\propto L H_{\text{KV}} d_h
$$

#### Where multi-query attention runs out

A single shared catalog can remove distinctions that genuinely need different key-value spaces.

The weakness is not an accidental footnote. Every operation in multi-query attention serves the narrower purpose to keep many query heads but share one key head and one value head across them; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take multi-query attention to the workbench

Understanding multi-query attention now means predicting its intermediate results before asking software for an answer. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running multi-query attention, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the multi-query attention result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/158-multi-query-attention/README.md).*

---

### Excavation 159 — Grouped-Query Attention — Recover Some Specialist Memory

<!-- book-prose-v2 -->

One shared KV head makes decoding light enough for the station, but evaluation finds a quality loss on relationships that benefited from distinct catalogs.

The machinery already in our hands suggests that we return immediately to one KV head per query head.

This is how grouped-query attention ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

One counterexample is enough to expose the missing job: quality recovers, but so does the full cache and bandwidth cost that forced sharing.

The wrong answer makes the need for grouped-query attention inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: partition query heads into groups; queries remain distinct while each group shares one key-value head.

The usual name, **Grouped-Query Attention**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to return immediately to one KV head per query head produces the observed failure: quality recovers, but so does the full cache and bandwidth cost that forced sharing. Starting with the repaired demand to partition query heads into groups; queries remain distinct while each group shares one key-value head preserves the information the shortcut lost. The subject of grouped-query attention lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to partition query heads into groups; queries remain distinct while each group shares one key-value head instead of merely trying to return immediately to one KV head per query head. That controlled contrast is what turns a plausible explanation of grouped-query attention into an understandable derivation.

#### Recover Some Specialist Memory

Eight query heads arranged into two KV groups preserve two catalogs. The cache is twice MQA's size but one quarter of ordinary eight-head KV storage.

There are now two histories of this grouped-query attention case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

#### The calculation hidden inside grouped-query attention

Before Grouped-Query Attention receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Line up the model's eight query heads and two KV catalogs. Four consecutive query heads must point to catalog 0 and the next four to catalog 1. Scaling head number h from the eight-head range into the two-catalog range gives h×2/8; rounding down turns positions 0 through 3 into address 0 and positions 4 through 7 into address 1. The name g(h) records that address-making rule.

h is a query-head index, H_Q counts query heads, H_KV counts shared KV groups, and g(h) selects the group serving head h.

##### Why no cheaper operation does the same job

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) spreads the KV group range across query-head indices; [division](../MATHEMATICAL_MOVES.md#division) converts one query index into its proportional group location. The floor deliberately [rounds](../MATHEMATICAL_MOVES.md#rounding) down so every head receives one valid discrete group rather than a fractional address.

Every symbol in Grouped-Query Attention can now be read back into an action already performed. The whole procedure fits in one line:

$$
g(h)=\left\lfloor\frac{hH_{\text{KV}}}{H_Q}\right\rfloor
$$

#### Where grouped-query attention runs out

Because sharing deliberately removes independent KV views, the number and assignment of groups remain empirical design choices whose quality must be measured.

Look back at what grouped-query attention actually preserves: it can partition query heads into groups; queries remain distinct while each group shares one key-value head. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

#### Take grouped-query attention to the workbench

The reader has reconstructed grouped-query attention in words; the workbench tests whether those words specify a real procedure. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running grouped-query attention, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the grouped-query attention result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/159-grouped-query-attention/README.md).*

---

### Excavation 160 — FlashAttention — The Arithmetic Was Not the Bottleneck

<!-- book-prose-v2 -->

Grouped-query attention makes generation economical, yet training long packed sequences still materializes a large attention-score matrix in slow device memory.

If the old idea can be stretched one step farther, we should reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost.

If the proposal works on every relevant case, flashattention is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

Now keep that rule fixed and let the difficult case enter: approximation changes the model, while profiling shows much of the time is spent writing and rereading exact intermediate scores rather than multiplying them.

Nothing magical creates flashattention. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once.

This boundary between the failed rule and its repair is the subject later work calls **FlashAttention**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize flashattention; try to break it by subtraction. Remove the part that knows how to tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once, leaving only the attempt to reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost. What returns is not a vague weakness but the original contradiction: approximation changes the model, while profiling shows much of the time is spent writing and rereading exact intermediate scores rather than multiplying them. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost receives the same test as the rule to tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once. Their different outcomes reveal what flashattention contributes without asking the reader to trust historical convention.

#### The Arithmetic Was Not the Bottleneck

Process two score tiles. Carry only the running maximum, normalized denominator, and weighted value total into the next tile; the final answer matches ordinary softmax attention.

Hold the setting, evidence, and desired outcome fixed while testing flashattention. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

#### The calculation hidden inside flashattention

Do not read the coming FlashAttention line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

The model's first attention tile contains scores 1 and 4, so 4 becomes the remembered safety ceiling. The next tile contains 3 and 2; neither exceeds 4, so the ceiling remains 4. If a later tile contained 7, the ceiling would become 7 and the earlier exponential totals would be rescaled. Thus m is the largest score already processed, the s_j values are the arriving tile, and m-prime is the one maximum covering both histories.

m is the largest score already seen, s_j are scores in the new tile, and m-prime is the safe maximum for the combined tiles.

##### Why no cheaper operation does the same job

[Maximum](../MATHEMATICAL_MOVES.md#maximum) preserves the one value needed to stabilize exponentials across both old and new tiles. Addition would invent a score that never occurred; averaging could be lower than the true maximum and allow overflow. The prime marks the updated running version; see [symbol decorations](../MATHEMATICAL_MOVES.md#symbol-decorations).

Every symbol in FlashAttention can now be read back into an action already performed. The whole procedure fits in one line:

$$
m^{\prime}=\max(m,\max_j s_j)
$$

#### Where flashattention runs out

FlashAttention removes avoidable memory traffic, not quadratic pairwise arithmetic itself.

This is where flashattention runs out for a causal reason. We gave it enough structure to tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take flashattention to the workbench

A mathematical story about flashattention earns trust only when the failed and repaired paths can both be reproduced. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running flashattention, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the flashattention result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/160-flash-attention/README.md).*

---

### Excavation 161 — RMSNorm — Do We Need to Subtract the Centre?

<!-- book-prose-v2 -->

FlashAttention removes one systems bottleneck, making smaller repeated operations visible. Layer normalization calculates both a mean and a spread at every token and layer.

A careful builder would first avoid adding machinery and delete normalization because each individual operation appears cheap.

The shortcut appears to retain everything rmsnorm needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

The world supplies the one comparison the shortcut hoped never to face: deep residual streams drift in scale and training destabilizes; the repeated control was doing essential work.

The counterexample teaches rmsnorm. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: keep rescaling invariance by dividing by root-mean-square magnitude, while testing whether explicit recentering is dispensable.

Now—and not earlier—we may introduce **RMSNorm**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to delete normalization because each individual operation appears cheap, and the case answers that deep residual streams drift in scale and training destabilizes; the repeated control was doing essential work. With the narrow repair—to keep rescaling invariance by dividing by root-mean-square magnitude, while testing whether explicit recentering is dispensable—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. RMSNorm returns to the same counterexample, replaces the attempt to delete normalization because each individual operation appears cheap with the responsibility to keep rescaling invariance by dividing by root-mean-square magnitude, while testing whether explicit recentering is dispensable, and must succeed where the shortcut failed.

#### Do We Need to Subtract the Centre

Vectors [3,4] and [30,40] become the same relative pattern after division by their RMS, although neither has its mean subtracted.

A formula for rmsnorm is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

#### The calculation hidden inside rmsnorm

Before RMSNorm receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Take the model feature pair [3,4]. Adding the raw values would let a negative feature cancel a positive one, so first turn their sizes into 9 and 16. Together they contribute 25; shared across two features that is 12.5 per feature. Its square root, about 3.54, returns to the features' ordinary units. Only now do we call this typical magnitude RMS(x) and the feature count d.

d is feature width; each x_i is one feature; RMS(x) is the vector's typical magnitude before a learned scale is applied.

##### Why no cheaper operation does the same job

[Squaring](../MATHEMATICAL_MOVES.md#powers) keeps negative and positive feature magnitudes from cancelling. [Summation](../MATHEMATICAL_MOVES.md#summation) gathers every feature's contribution, [division](../MATHEMATICAL_MOVES.md#division) makes the magnitude per feature, and the [square root](../MATHEMATICAL_MOVES.md#square-root) returns to the original scale. Omitting division would make wider vectors appear larger merely for having more coordinates.

Every symbol in RMSNorm can now be read back into an action already performed. The whole procedure fits in one line:

$$
\mathrm{RMS}(x)=\sqrt{\frac1d\sum_{i=1}^{d}x_i^2}
$$

#### Where rmsnorm runs out

RMSNorm does not guarantee that recentering is unimportant for every architecture or task.

The boundary can be predicted from the construction itself. RMSNorm performs the repair to keep rescaling invariance by dividing by root-mean-square magnitude, while testing whether explicit recentering is dispensable; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

#### Take rmsnorm to the workbench

Move rmsnorm from imagination to evidence by making the shortcut fail under controlled inputs. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running rmsnorm, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the rmsnorm result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/161-rmsnorm/README.md).*

---

### Excavation 162 — Pre-Normalization — Protect the Residual Highway

<!-- book-prose-v2 -->

The block is cheaper, but making it deeper reveals unstable early gradients when normalization follows each residual addition.

The obvious economy is to keep post-normalization because each block's output then looks standardized before the next block.

The proposal deserves a fair hearing. For pre-normalization, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Its hidden assumption becomes visible as soon as we observe that the supposedly clean output places normalization directly on the identity route every gradient must cross, making the long residual path harder to preserve.

The failure changes the question behind pre-normalization. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: normalize only the input to the changing branch and let the identity stream pass around it unchanged.

Only at this point does the inherited name **Pre-Normalization** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of pre-normalization by mentally removing the repair. We fall back to the proposal to keep post-normalization because each block's output then looks standardized before the next block; then the supposedly clean output places normalization directly on the identity route every gradient must cross, making the long residual path harder to preserve. Restore only the ability to normalize only the input to the changing branch and let the identity stream pass around it unchanged, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to keep post-normalization because each block's output then looks standardized before the next block to requiring the system to normalize only the input to the changing branch and let the identity stream pass around it unchanged. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to pre-normalization.

#### Protect the Residual Highway

A block computes a normalized proposal F, then adds that proposal to the untouched x. If F initially contributes little, the block can behave almost like identity.

Put the old procedure beside pre-normalization. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

#### The calculation hidden inside pre-normalization

Do not read the coming Pre-Normalization line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Let the residual stream carry a useful tiger signal x. The new branch examines a normalized copy and proposes a correction F(...). At initialization that proposal may be almost zero. Adding it to the untouched x lets the block say 'change nothing yet'; replacing x with the proposal would destroy the signal. The layer indices merely distinguish the stream before and after this addition.

x_l is the residual stream entering layer l; RMSNorm prepares only the branch; F proposes a change; x_l+1 is the next stream.

##### Why no cheaper operation does the same job

[Function application](../MATHEMATICAL_MOVES.md#function-application) fixes the order: normalize, then transform. [Addition](../MATHEMATICAL_MOVES.md#addition) preserves an untouched identity contribution beside the proposal. Replacing x with F would erase the gradient highway; normalizing the sum would place another transformation on that highway.

Every symbol in Pre-Normalization can now be read back into an action already performed. The whole procedure fits in one line:

$$
x_{\ell+1}=x_\ell+F(\mathrm{RMSNorm}(x_\ell))
$$

#### Where pre-normalization runs out

Pre-normalization improves gradient behavior but changes representation scale and does not eliminate every deep-training instability.

The limit follows from the job assigned to pre-normalization. Its repair knows how to normalize only the input to the changing branch and let the identity stream pass around it unchanged. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

#### Take pre-normalization to the workbench

A claim about pre-normalization now exists on the page; the laboratory must be able to contradict it. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running pre-normalization, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the pre-normalization result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/162-pre-normalization/README.md).*

---

### Excavation 163 — SwiGLU — Let One Learned Path Gate Another

<!-- book-prose-v2 -->

Pre-normalization lets gradients reach deep blocks, but the ordinary feed-forward network applies one fixed activation independently to one projection.

Before naming anything new, try to make the hidden layer merely wider and trust more coordinates to express every conditional interaction.

Its appeal is not ignorance but economy. SwiGLU should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Then a case arrives in which convenience and truth separate: width adds capacity but still asks one projection both to create content and decide when that content matters.

Notice what the counterexample has accomplished for swiglu. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: create one content projection and one gate projection; use the smooth gate to scale content feature by feature.

Humanity eventually gathered this problem and its repairs under the name **SwiGLU**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace swiglu with the old instruction to make the hidden layer merely wider and trust more coordinates to express every conditional interaction. The result is again that width adds capacity but still asks one projection both to create content and decide when that content matters. Put back only the requirement to create one content projection and one gate projection; use the smooth gate to scale content feature by feature. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when swiglu is introduced. The same evidence that defeated the attempt to make the hidden layer merely wider and trust more coordinates to express every conditional interaction is presented again. Only the ability to create one content projection and one gate projection; use the smooth gate to scale content feature by feature changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### Let One Learned Path Gate Another

For a token describing a river bank, one path proposes financial features while the gate suppresses them; in a money context the same content path can be opened.

Run the swiglu scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

#### The calculation hidden inside swiglu

Before SwiGLU receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Picture one candidate feature saying 'river-bank meaning: 5.' A separate learned gate examines this occurrence of bank. Near the river it may open close to 1, allowing almost all 5 through; near money it may close near 0, silencing that feature. This demands multiplication: zero times content must become zero. W_v creates the candidate, W_g creates gate evidence, SiLU shapes that evidence, and the circled product pairs each gate with its own feature.

W_g creates gate evidence, SiLU bends it smoothly, W_v creates candidate content, and the circled product combines matching hidden coordinates.

##### Why no cheaper operation does the same job

[Function application](../MATHEMATICAL_MOVES.md#function-application) makes the gate depend on this token. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) is forced because a zero gate must silence its matching content and a partial gate must scale it. Addition would let closed content leak through. The elementwise mark means aligned coordinates interact rather than forming every pair.

Every symbol in SwiGLU can now be read back into an action already performed. The whole procedure fits in one line:

$$
\mathrm{SwiGLU}(x)=\mathrm{SiLU}(xW_g)\odot(xW_v)
$$

#### Where swiglu runs out

Gating improves useful capacity but increases projection parameters and does not explain what every hidden feature means.

Why does that boundary remain? SwiGLU was built for one responsibility: create one content projection and one gate projection; use the smooth gate to scale content feature by feature. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take swiglu to the workbench

The argument for swiglu is still provisional until a runnable case can make it fail. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running swiglu, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the swiglu result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/163-swiglu/README.md).*

---

### Excavation 164 — Weight Tying — Use One Word Geometry Twice

<!-- book-prose-v2 -->

SwiGLU improves the block, but the model stores one large table for input embeddings and another large matrix for scoring the same vocabulary at output.

The first defensible move is to let both matrices learn independently because reading a token and predicting it are different jobs.

There is a real principle behind this restraint: the complexity of weight tying must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The proposal breaks for a specific reason, not by authority: the model spends parameters learning two unrelated geometries for the same set of word identities, and rare tokens receive weak evidence in both places.

That distinction is the hinge on which weight tying turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias.

We have earned the chapter's shorter name: **Weight Tying**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that weight tying is necessary rather than decorative. Delete its new responsibility and use the earlier plan to let both matrices learn independently because reading a token and predicting it are different jobs. Immediately, the model spends parameters learning two unrelated geometries for the same set of word identities, and rare tokens receive weak evidence in both places. Reintroduce the single job to reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias. Because the old plan to let both matrices learn independently because reading a token and predicting it are different jobs is the only displaced piece, the reader can locate exactly where weight tying changes the outcome.

#### Use One Word Geometry Twice

The tiger vector used to enter the model also becomes the direction a final hidden state must align with to predict tiger.

The name weight tying is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### The calculation hidden inside weight tying

Do not read the coming Weight Tying line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

The input table already contains a row pointing in the learned direction of tiger. At the output, predicting tiger means asking how strongly the final hidden state points along that same direction. Turning table rows into scoring columns changes only their orientation. E names the existing table, T marks that turn, and equality says W_out is the very same learned values—not a second copy trained to resemble them.

E stores one embedding row per token; transpose turns those rows into output-scoring columns without changing their values.

##### Why no cheaper operation does the same job

[Equality](../MATHEMATICAL_MOVES.md#equals) imposes shared parameters rather than merely similar initialization. Transposition changes orientation so matrix shapes fit; it does not relearn or numerically transform the coordinates. Using addition would combine two matrices instead of making one geometry perform both roles.

Every symbol in Weight Tying can now be read back into an action already performed. The whole procedure fits in one line:

$$
W_{\text{out}}=E^{\mathsf T}
$$

#### Where weight tying runs out

Tying reduces parameters and imposes a useful constraint, but separate input and output roles may sometimes benefit from extra freedom.

The weakness is not an accidental footnote. Every operation in weight tying serves the narrower purpose to reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take weight tying to the workbench

Understanding weight tying now means predicting its intermediate results before asking software for an answer. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running weight tying, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the weight tying result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/164-weight-tying/README.md).*

---

### Excavation 165 — Adam — Give Each Parameter Its Own Step Scale

<!-- book-prose-v2 -->

Weight tying concentrates more roles in shared parameters. During training, some coordinates receive frequent large gradients while rare-token coordinates receive sparse small ones.

At this point the shortest path seems to be to use the same raw gradient step scale for every parameter.

This is how adam ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Reality now asks a question the retained information cannot answer: a rate safe for frequent large gradients barely moves sparse coordinates; a rate large enough for sparse coordinates makes noisy ones unstable.

The wrong answer makes the need for adam inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude.

The usual name, **Adam**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to use the same raw gradient step scale for every parameter produces the observed failure: a rate safe for frequent large gradients barely moves sparse coordinates; a rate large enough for sparse coordinates makes noisy ones unstable. Starting with the repaired demand to keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude preserves the information the shortcut lost. The subject of adam lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude instead of merely trying to use the same raw gradient step scale for every parameter. That controlled contrast is what turns a plausible explanation of adam into an understandable derivation.

#### Give Each Parameter Its Own Step Scale

A frequently noisy weight builds a large second-moment estimate and receives a smaller normalized step; a consistently directed sparse weight can still move.

There are now two histories of this adam case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

#### The calculation hidden inside adam

Before Adam receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Follow one weight that repeatedly receives gradients near 2 and another that usually receives gradients near 0.2. A single raw step scale makes their movement differ tenfold even if each signal is ordinary for its own weight. Remember each weight's recent direction in m and its recent squared size in v; compare direction with the square root of size, then let eta choose the common overall pace. Epsilon is the tiny floor that keeps a never-touched weight from asking us to divide by zero.

m-hat is bias-corrected directional memory, v-hat is bias-corrected squared-gradient memory, eta is global scale, and epsilon prevents division by zero.

##### Why no cheaper operation does the same job

[Division](../MATHEMATICAL_MOVES.md#division) measures direction relative to recent gradient magnitude, giving each coordinate an adaptive scale. The [square root](../MATHEMATICAL_MOVES.md#square-root) returns squared-gradient memory to gradient units. [Subtraction](../MATHEMATICAL_MOVES.md#subtraction) moves opposite estimated uphill direction; adding would increase loss locally.

Every symbol in Adam can now be read back into an action already performed. The whole procedure fits in one line:

$$
\theta_{t+1}=\theta_t-\eta\frac{\widehat m_t}{\sqrt{\widehat v_t}+\epsilon}
$$

#### Where adam runs out

Adaptive scaling can generalize differently from SGD and introduces extra state for every parameter.

Look back at what adam actually preserves: it can keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

#### Take adam to the workbench

The reader has reconstructed adam in words; the workbench tests whether those words specify a real procedure. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running adam, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the adam result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/165-adam/README.md).*

---

### Excavation 166 — AdamW — Keep Shrinkage Separate from Adaptation

<!-- book-prose-v2 -->

Adam trains the block, but adding an L2 penalty to the loss sends shrinkage through the optimizer's coordinate-wise rescaling.

We can postpone invention if we simply treat penalty gradients and data gradients identically because both appear in one total loss.

If the proposal works on every relevant case, adamw is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The decisive test is this: coordinates with different gradient histories receive different effective shrinkage even when the intended rule was to decay all selected weights at one rate.

Nothing magical creates adamw. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: apply Adam's adaptive data update and parameter decay as separate operations.

This boundary between the failed rule and its repair is the subject later work calls **AdamW**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize adamw; try to break it by subtraction. Remove the part that knows how to apply Adam's adaptive data update and parameter decay as separate operations, leaving only the attempt to treat penalty gradients and data gradients identically because both appear in one total loss. What returns is not a vague weakness but the original contradiction: coordinates with different gradient histories receive different effective shrinkage even when the intended rule was to decay all selected weights at one rate. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to treat penalty gradients and data gradients identically because both appear in one total loss receives the same test as the rule to apply Adam's adaptive data update and parameter decay as separate operations. Their different outcomes reveal what adamw contributes without asking the reader to trust historical convention.

#### Keep Shrinkage Separate from Adaptation

Two equal weights with different gradient histories receive different Adam steps but the same proportional decay.

Hold the setting, evidence, and desired outcome fixed while testing adamw. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

#### The calculation hidden inside adamw

Do not read the coming AdamW line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Suppose two weights both equal 2, although their gradient histories differ. If decay means 'remove one tenth of one percent of the present weight this step,' both should lose the same proportion before their evidence-driven Adam movements differ. Multiplying theta by 1−eta lambda performs that direct shrink. The separate subtraction then applies Adam's learned direction, preventing gradient history from secretly changing the intended decay rule.

lambda is decay strength; the first term shrinks the old parameter directly; the second is Adam's data-driven update.

##### Why no cheaper operation does the same job

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) by 1−eta lambda makes decay proportional to current parameter size: a zero weight stays zero and doubling a weight doubles shrinkage. [Subtraction](../MATHEMATICAL_MOVES.md#subtraction) then applies the independently adapted loss step. Hiding decay inside m and v would mix two jobs the formula deliberately separates.

Every symbol in AdamW can now be read back into an action already performed. The whole procedure fits in one line:

$$
\theta_{t+1}=(1-\eta\lambda)\theta_t-\eta\frac{\widehat m_t}{\sqrt{\widehat v_t}+\epsilon}
$$

#### Where adamw runs out

Decoupled decay still requires choosing which parameters to decay and how strongly.

This is where adamw runs out for a causal reason. We gave it enough structure to apply Adam's adaptive data update and parameter decay as separate operations, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take adamw to the workbench

A mathematical story about adamw earns trust only when the failed and repaired paths can both be reproduced. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running adamw, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the adamw result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/166-adamw/README.md).*

---

### Excavation 167 — Gradient Clipping — Stop One Shock from Becoming a Catastrophe

<!-- book-prose-v2 -->

Most steps are stable, but a rare batch produces an enormous global gradient norm and overwhelms Adam's still-developing moment estimates.

The previous discovery seems almost sufficient: we could discard the entire batch whenever any gradient coordinate looks large.

The shortcut appears to retain everything gradient clipping needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

One counterexample is enough to expose the missing job: useful directional evidence is lost, and one arbitrary coordinate threshold ignores the size of the full update vector.

The counterexample teaches gradient clipping. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: preserve the gradient's direction but scale its whole norm down only when it exceeds a chosen ceiling.

Now—and not earlier—we may introduce **Gradient Clipping**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to discard the entire batch whenever any gradient coordinate looks large, and the case answers that useful directional evidence is lost, and one arbitrary coordinate threshold ignores the size of the full update vector. With the narrow repair—to preserve the gradient's direction but scale its whole norm down only when it exceeds a chosen ceiling—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Gradient Clipping returns to the same counterexample, replaces the attempt to discard the entire batch whenever any gradient coordinate looks large with the responsibility to preserve the gradient's direction but scale its whole norm down only when it exceeds a chosen ceiling, and must succeed where the shortcut failed.

#### Stop One Shock from Becoming a Catastrophe

A gradient of length 20 with ceiling 5 is multiplied by one quarter. A gradient of length 3 passes unchanged.

A formula for gradient clipping is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

#### The calculation hidden inside gradient clipping

Before Gradient Clipping receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

The model's current gradient points in a useful direction but has length 20, while this run permits length 5. The required scale is 5/20, or one quarter, so every component shrinks by one quarter and direction survives. If the next gradient has length 3, the fraction 5/3 would enlarge it—exactly what we do not want—so we cap the multiplier at 1. We call the ceiling c, the original advice g, and the safe advice g-prime.

g is the original gradient vector, c is the allowed norm ceiling, and g-prime is the gradient actually given to the optimizer.

##### Why no cheaper operation does the same job

[Division](../MATHEMATICAL_MOVES.md#division) computes the fraction needed to bring the current norm down to c. [Minimum](../MATHEMATICAL_MOVES.md#minimum) chooses at most one, so small gradients are never enlarged. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) scales every coordinate equally, preserving direction; clipping coordinates separately would rotate the update.

Every symbol in Gradient Clipping can now be read back into an action already performed. The whole procedure fits in one line:

$$
g^{\prime}=g\min\left(1,\frac{c}{\lVert g\rVert}\right)
$$

#### Where gradient clipping runs out

Clipping limits damage; it can hide a broken loss, corrupt data, or an unsuitable learning rate if used without diagnosis.

The boundary can be predicted from the construction itself. Gradient Clipping performs the repair to preserve the gradient's direction but scale its whole norm down only when it exceeds a chosen ceiling; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

#### Take gradient clipping to the workbench

Move gradient clipping from imagination to evidence by making the shortcut fail under controlled inputs. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running gradient clipping, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the gradient clipping result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/167-gradient-clipping/README.md).*

---

### Excavation 168 — Mixed Precision — Stop Storing Every Number with Unneeded Detail

<!-- book-prose-v2 -->

Stable gradients now expose the physical bill: weights, activations, and gradients are stored and moved as wide numbers even when many operations tolerate fewer bits.

The least expensive next move is to convert every value and every update permanently to half precision.

The proposal deserves a fair hearing. For mixed precision, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Now keep that rule fixed and let the difficult case enter: small updates disappear when rounded into large weights, and some intermediate values overflow or underflow the smaller numeric range.

The failure changes the question behind mixed precision. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision.

Only at this point does the inherited name **Mixed Precision** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of mixed precision by mentally removing the repair. We fall back to the proposal to convert every value and every update permanently to half precision; then small updates disappear when rounded into large weights, and some intermediate values overflow or underflow the smaller numeric range. Restore only the ability to use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to convert every value and every update permanently to half precision to requiring the system to use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to mixed precision.

#### Stop Storing Every Number with Unneeded Detail

A million activation values require roughly two megabytes at 16 bits instead of four at 32 bits, while a 32-bit master weight accumulates tiny updates safely.

Put the old procedure beside mixed precision. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

#### The calculation hidden inside mixed precision

Do not read the coming Mixed Precision line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Place one million model activation numbers in memory. At 32 bits each they occupy 32 million bits; at 16 bits each, 16 million bits. Hardware reports bytes, with eight bits in each byte, so divide either total by eight: four megabytes versus two. N counts the values, b is the chosen bits per value, and M is the resulting payload in bytes.

N is the number of stored scalar values, b is bits per value, and division by eight converts bits into bytes.

##### Why no cheaper operation does the same job

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) is forced because every one of N values consumes b bits. [Division](../MATHEMATICAL_MOVES.md#division) converts units using eight bits per byte; adding eight would not perform a unit conversion. The equality describes payload memory and intentionally omits allocator overhead.

Every symbol in Mixed Precision can now be read back into an action already performed. The whole procedure fits in one line:

$$
M=\frac{N b}{8}\ \text{bytes}
$$

#### Where mixed precision runs out

Mixed precision reduces representation cost, but numeric range—not only bit count—still threatens small gradients.

The limit follows from the job assigned to mixed precision. Its repair knows how to use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

#### Take mixed precision to the workbench

A claim about mixed precision now exists on the page; the laboratory must be able to contradict it. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running mixed precision, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the mixed precision result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/168-mixed-precision/README.md).*

---

### Excavation 169 — Loss Scaling — Rescue Gradients Too Small to Represent

<!-- book-prose-v2 -->

The forward pass looks correct, but some half-precision gradients round to zero before the optimizer can use them.

For a moment, remain loyal to the simplest proposal: increase the learning rate so small updates become visible.

Its appeal is not ignorance but economy. Loss Scaling should not be added until an observation exposes the exact thing the older procedure cannot preserve.

The world supplies the one comparison the shortcut hoped never to face: the learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update.

Notice what the counterexample has accomplished for loss scaling. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating.

Humanity eventually gathered this problem and its repairs under the name **Loss Scaling**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace loss scaling with the old instruction to increase the learning rate so small updates become visible. The result is again that the learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update. Put back only the requirement to multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when loss scaling is introduced. The same evidence that defeated the attempt to increase the learning rate so small updates become visible is presented again. Only the ability to multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### Rescue Gradients Too Small to Represent

A gradient 0.000001 becomes 0.001 when loss scale is 1000, survives backpropagation, and returns to 0.000001 after unscaling.

Run the loss scaling scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

#### The calculation hidden inside loss scaling

Before Loss Scaling receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

A true gradient of 0.000001 may vanish in half precision. Before differentiation, make the loss one thousand times larger; every loss-derived gradient becomes 0.001 and survives. Before updating the weight, divide by the same thousand and recover 0.000001. S names this temporary magnifier, L the original loss, and g the restored gradient—the model has not been told to learn a thousand times faster.

L is original loss, S is a temporary positive scale, and g is the recovered gradient in the loss's original units.

##### Why no cheaper operation does the same job

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) by S enlarges every loss-derived gradient before narrow arithmetic can erase it. [Division](../MATHEMATICAL_MOVES.md#division) by the same S reverses that temporary unit change before the optimizer. Adding S would not proportionally enlarge tiny sensitivities and could not be undone uniformly.

Every symbol in Loss Scaling can now be read back into an action already performed. The whole procedure fits in one line:

$$
g=\frac{1}{S}\nabla_\theta(SL)
$$

#### Where loss scaling runs out

A scale large enough to prevent underflow can cause overflow, so practical systems adjust it dynamically.

Why does that boundary remain? Loss Scaling was built for one responsibility: multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take loss scaling to the workbench

The argument for loss scaling is still provisional until a runnable case can make it fail. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running loss scaling, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the loss scaling result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/169-loss-scaling/README.md).*

---

### Excavation 170 — Gradient Accumulation — Build a Large Batch That Does Not Fit

<!-- book-prose-v2 -->

The optimizer needs a less noisy effective batch, but all its examples and activations cannot coexist on one device.

Nothing yet appears to demand a new invention. We can reduce the batch until it fits and change nothing else.

There is a real principle behind this restraint: the complexity of gradient accumulation must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Its hidden assumption becomes visible as soon as we observe that the gradient becomes noisier and the training regime changes; increasing the learning rate cannot recreate evidence never averaged together.

That distinction is the hinge on which gradient accumulation turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step.

We have earned the chapter's shorter name: **Gradient Accumulation**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that gradient accumulation is necessary rather than decorative. Delete its new responsibility and use the earlier plan to reduce the batch until it fits and change nothing else. Immediately, the gradient becomes noisier and the training regime changes; increasing the learning rate cannot recreate evidence never averaged together. Reintroduce the single job to run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step. Because the old plan to reduce the batch until it fits and change nothing else is the only displaced piece, the reader can locate exactly where gradient accumulation changes the outcome.

#### Build a Large Batch That Does Not Fit

Four micro-batches of eight examples create one effective batch of thirty-two while only eight examples' activations are resident at a time.

The name gradient accumulation is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### The calculation hidden inside gradient accumulation

Do not read the coming Gradient Accumulation line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Imagine four small tables of eight examples arriving one after another. Each table gives its own average advice about the weights, but none is allowed to update yet. Add the four pieces of advice into one pending total, then share that total across the four witnesses. K counts those witnesses, g_k names one witness's advice, and g_effective is what the single optimizer step hears.

K is the number of micro-batches and g_k is the gradient average produced by micro-batch k of equal size.

##### Why no cheaper operation does the same job

[Summation](../MATHEMATICAL_MOVES.md#summation) lets every micro-batch contribute to the same pending update. [Division](../MATHEMATICAL_MOVES.md#division) returns advice per micro-batch so increasing K does not enlarge the step by itself. Multiplication would let a zero coordinate in one micro-batch erase all others.

Every symbol in Gradient Accumulation can now be read back into an action already performed. The whole procedure fits in one line:

$$
g_{\text{effective}}=\frac1K\sum_{k=1}^{K}g_k
$$

#### Where gradient accumulation runs out

Accumulation lowers activation memory but adds serial work and does not reduce parameter or optimizer-state memory.

The weakness is not an accidental footnote. Every operation in gradient accumulation serves the narrower purpose to run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take gradient accumulation to the workbench

Understanding gradient accumulation now means predicting its intermediate results before asking software for an answer. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running gradient accumulation, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the gradient accumulation result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/170-gradient-accumulation/README.md).*

---

### Excavation 171 — Activation Checkpointing — Remember Less, Recompute Exactly

<!-- book-prose-v2 -->

Only one micro-batch is resident, yet backpropagation retains every layer's intermediate values until their gradients are computed.

The machinery already in our hands suggests that we delete all activations after the forward pass.

This is how activation checkpointing ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Then a case arrives in which convenience and truth separate: backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly.

The wrong answer makes the need for activation checkpointing inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: keep selected checkpoint activations and recompute the missing segments once when backward reaches them.

The usual name, **Activation Checkpointing**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to delete all activations after the forward pass produces the observed failure: backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly. Starting with the repaired demand to keep selected checkpoint activations and recompute the missing segments once when backward reaches them preserves the information the shortcut lost. The subject of activation checkpointing lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to keep selected checkpoint activations and recompute the missing segments once when backward reaches them instead of merely trying to delete all activations after the forward pass. That controlled contrast is what turns a plausible explanation of activation checkpointing into an understandable derivation.

#### Remember Less, Recompute Exactly

In a nine-layer chain, retain boundaries around three-layer segments. Backward rebuilds one segment at a time instead of storing all nine layers.

There are now two histories of this activation checkpointing case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

#### The calculation hidden inside activation checkpointing

Before Activation Checkpointing receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

In a model chain of nine layers, keeping every activation costs nine stored boundaries. Keep only layers 0, 3, and 6; during backward work, rebuild the three missing operations inside the needed segment. For a much longer chain, choosing about the square root of L boundaries creates segments of about the same length, balancing stored checkpoints against recomputation. Big-O records this growth pattern, not an exact byte count.

L is the number of sequential layers and the expression records the memory-growth order under a balanced basic checkpoint scheme.

##### Why no cheaper operation does the same job

[Square root](../MATHEMATICAL_MOVES.md#square-root) appears because balancing roughly sqrt(L) stored boundaries with sqrt(L)-sized recomputed segments minimizes the larger side of the trade. [Proportionality](../MATHEMATICAL_MOVES.md#proportionality) is implicit in big-O: exact bytes depend on activation shapes and implementation.

Every symbol in Activation Checkpointing can now be read back into an action already performed. The whole procedure fits in one line:

$$
M_{\text{activations}}=O(\sqrt{L})
$$

#### Where activation checkpointing runs out

Checkpointing buys memory with extra computation; a poor partition can save little or recompute too much.

Look back at what activation checkpointing actually preserves: it can keep selected checkpoint activations and recompute the missing segments once when backward reaches them. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

#### Take activation checkpointing to the workbench

The reader has reconstructed activation checkpointing in words; the workbench tests whether those words specify a real procedure. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running activation checkpointing, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the activation checkpointing result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/171-activation-checkpointing/README.md).*

---

### Excavation 172 — ZeRO — Stop Replicating the Same Training State

<!-- book-prose-v2 -->

Recomputation makes the forward graph fit, but AdamW stores parameters, gradients, first moments, and second moments. Ordinary data parallelism copies all of them onto every device.

If the old idea can be stretched one step farther, we should add devices and replicate the full training state on each one.

If the proposal works on every relevant case, zero is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The proposal breaks for a specific reason, not by authority: compute capacity grows while per-device model-state memory remains almost unchanged, so the same memory wall returns.

Nothing magical creates zero. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them.

This boundary between the failed rule and its repair is the subject later work calls **ZeRO**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize zero; try to break it by subtraction. Remove the part that knows how to partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them, leaving only the attempt to add devices and replicate the full training state on each one. What returns is not a vague weakness but the original contradiction: compute capacity grows while per-device model-state memory remains almost unchanged, so the same memory wall returns. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to add devices and replicate the full training state on each one receives the same test as the rule to partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them. Their different outcomes reveal what zero contributes without asking the reader to trust historical convention.

#### Stop Replicating the Same Training State

Four workers each keep roughly one quarter of a large moment vector rather than four complete copies, then cooperate for the update.

Hold the setting, evidence, and desired outcome fixed while testing zero. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

#### The calculation hidden inside zero

Do not read the coming ZeRO line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Adam's moment state has twelve equal chunks and four devices are cooperating. Replication gives every device all twelve; sharding gives each device three. Asking for state per device therefore means sharing the total across P owners: total divided by P. The approximation sign remains because temporary gathers and uneven tensor sizes prevent the physical memory from being exactly that ideal share.

M_total is shardable model state and P is the number of cooperating devices under an ideal balanced partition.

##### Why no cheaper operation does the same job

[Division](../MATHEMATICAL_MOVES.md#division) expresses an equal share per device. Multiplication describes the failed replicated system's total cluster memory, not the amount one device must hold. [Approximation](../MATHEMATICAL_MOVES.md#approximation) admits temporary gathers, buffers, and uneven tensors.

Every symbol in ZeRO can now be read back into an action already performed. The whole procedure fits in one line:

$$
M_{\text{state per device}}\approx\frac{M_{\text{total state}}}{P}
$$

#### Where zero runs out

Because a worker no longer owns a complete state by itself, sharding trades redundant memory for communication and makes recovery and state ownership more complex.

This is where zero runs out for a causal reason. We gave it enough structure to partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take zero to the workbench

A mathematical story about zero earns trust only when the failed and repaired paths can both be reproduced. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running zero, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the zero result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/172-zero-sharding/README.md).*

---

### Excavation 173 — Tensor Parallelism — Split One Matrix That No Device Can Hold

<!-- book-prose-v2 -->

Sharded parameters can be gathered for computation, but the largest matrix itself becomes too large to materialize or multiply on one worker.

A careful builder would first avoid adding machinery and assign whole layers to different devices and pass every activation through them sequentially.

The shortcut appears to retain everything tensor parallelism needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

Reality now asks a question the retained information cannot answer: one oversized layer still cannot fit, and devices responsible for later layers wait while earlier ones work.

The counterexample teaches tensor parallelism. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output.

Now—and not earlier—we may introduce **Tensor Parallelism**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to assign whole layers to different devices and pass every activation through them sequentially, and the case answers that one oversized layer still cannot fit, and devices responsible for later layers wait while earlier ones work. With the narrow repair—to split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Tensor Parallelism returns to the same counterexample, replaces the attempt to assign whole layers to different devices and pass every activation through them sequentially with the responsibility to split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output, and must succeed where the shortcut failed.

#### Split One Matrix That No Device Can Hold

Divide one vocabulary projection into four column blocks. Each device scores one quarter of the vocabulary from the same hidden state; concatenation restores the full logits.

A formula for tensor parallelism is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

#### The calculation hidden inside tensor parallelism

Before Tensor Parallelism receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Split the vocabulary-scoring matrix into four column blocks. Every device receives the same hidden state X but multiplies it by only its own block W_p, producing scores Y_p for its quarter of the vocabulary. Those scores must remain distinct, so place the four blocks beside one another in vocabulary order. Adding them would collapse different tokens into the same slots. Y names the restored full score row after concatenation.

W is partitioned into P column blocks; every worker receives X and produces the corresponding block of output columns.

##### Why no cheaper operation does the same job

[Concatenation](../MATHEMATICAL_MOVES.md#concatenation) preserves distinct output columns side by side; addition would collapse vocabulary scores that must remain separate. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) applies the same input X to each learned block, and equality states that partitioned execution matches the unsplit matrix operation.

Every symbol in Tensor Parallelism can now be read back into an action already performed. The whole procedure fits in one line:

$$
Y_p=XW_p,\quad Y=[Y_1,Y_2,\ldots,Y_P]
$$

#### Where tensor parallelism runs out

Tensor parallelism introduces communication inside every layer, so a slow interconnect can erase its benefit.

The boundary can be predicted from the construction itself. Tensor Parallelism performs the repair to split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

#### Take tensor parallelism to the workbench

Move tensor parallelism from imagination to evidence by making the shortcut fail under controlled inputs. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running tensor parallelism, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the tensor parallelism result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/173-tensor-parallelism/README.md).*

---

### Excavation 174 — Speculative Decoding — Let a Small Model Propose, Never Decide

<!-- book-prose-v2 -->

Tensor parallelism makes one target-model step possible, but autoregressive dependence still serializes token generation.

The obvious economy is to let a cheap draft model emit several tokens and return them directly.

The proposal deserves a fair hearing. For speculative decoding, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The decisive test is this: speed improves by silently replacing the trusted target distribution with a weaker model's distribution.

The failure changes the question behind speculative decoding. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling.

Only at this point does the inherited name **Speculative Decoding** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of speculative decoding by mentally removing the repair. We fall back to the proposal to let a cheap draft model emit several tokens and return them directly; then speed improves by silently replacing the trusted target distribution with a weaker model's distribution. Restore only the ability to let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to let a cheap draft model emit several tokens and return them directly to requiring the system to let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to speculative decoding.

#### Let a Small Model Propose, Never Decide

The draft proposes “the tiger sleeps.” One target call verifies all three positions; an unsupported token is rejected and sampling resumes from the corrected target distribution.

Put the old procedure beside speculative decoding. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

#### The calculation hidden inside speculative decoding

Do not read the coming Speculative Decoding line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

If the draft assigns tiger probability 0.8 but the target assigns 0.4, only half of those proposals have target support: 0.4/0.8=0.5. If the draft assigns 0.4 and the target 0.8, the ratio is 2, but acceptance cannot be 200 percent, so it stops at 1. The function a(x) names this capped acceptance chance for proposed token x.

q(x) is draft probability, p(x) is target probability, and a(x) is the probability of accepting the draft token under the correction step.

##### Why no cheaper operation does the same job

[Division](../MATHEMATICAL_MOVES.md#division) compares target support per unit of draft support. [Minimum](../MATHEMATICAL_MOVES.md#minimum) caps acceptance at one because probabilities cannot exceed certainty. Simply taking max or always accepting would change the target distribution; the ratio corrects proposals that the draft overproduces.

Every symbol in Speculative Decoding can now be read back into an action already performed. The whole procedure fits in one line:

$$
a(x)=\min\left(1,\frac{p(x)}{q(x)}\right)
$$

#### Where speculative decoding runs out

Speed depends on draft agreement and hardware utilization; poor proposals add work instead of removing it.

The limit follows from the job assigned to speculative decoding. Its repair knows how to let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

#### Take speculative decoding to the workbench

A claim about speculative decoding now exists on the page; the laboratory must be able to contradict it. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running speculative decoding, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the speculative decoding result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/174-speculative-decoding/README.md).*

---

### Excavation 175 — A Modern Tiny Language Model — Assemble the Measured Engine

<!-- book-prose-v2 -->

Speculative decoding accelerates the final serial loop. We now have many locally useful repairs, but a pile of optimizations is not yet one reproducible model.

Before naming anything new, try to enable every technique at once and celebrate if the program runs.

Its appeal is not ignorance but economy. A Modern Tiny Language Model should not be added until an observation exposes the exact thing the older procedure cannot preserve.

One counterexample is enough to expose the missing job: when quality or speed changes, no one knows which mechanism caused it; masks, precision, sharding, and caches can disagree at their boundaries.

Notice what the counterexample has accomplished for a modern tiny language model. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: assemble the engine in dependency order, preserve a reference path, and test numerical or distributional equivalence at every boundary before accepting measured gains.

Humanity eventually gathered this problem and its repairs under the name **A Modern Tiny Language Model**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace a modern tiny language model with the old instruction to enable every technique at once and celebrate if the program runs. The result is again that when quality or speed changes, no one knows which mechanism caused it; masks, precision, sharding, and caches can disagree at their boundaries. Put back only the requirement to assemble the engine in dependency order, preserve a reference path, and test numerical or distributional equivalence at every boundary before accepting measured gains. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when a modern tiny language model is introduced. The same evidence that defeated the attempt to enable every technique at once and celebrate if the program runs is presented again. Only the ability to assemble the engine in dependency order, preserve a reference path, and test numerical or distributional equivalence at every boundary before accepting measured gains changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### Assemble the Measured Engine

Train one tiny model with packed examples, RoPE, GQA, exact tiled attention, pre-RMSNorm, SwiGLU, tied embeddings, AdamW, clipping, mixed precision, accumulation, and checkpointing; then serve it with a KV cache and verified draft proposals.

Run the a modern tiny language model scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

#### Where a modern tiny language model runs out

The engine is modern, not final. New hardware, data, and observations will create new bottlenecks, and every proposed repair must re-enter the bounded loop from Excavation 150.

Why does that boundary remain? A Modern Tiny Language Model was built for one responsibility: assemble the engine in dependency order, preserve a reference path, and test numerical or distributional equivalence at every boundary before accepting measured gains. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take a modern tiny language model to the workbench

The argument for a modern tiny language model is still provisional until a runnable case can make it fail. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running a modern tiny language model, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the a modern tiny language model result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/175-modern-tiny-llm/README.md).*
