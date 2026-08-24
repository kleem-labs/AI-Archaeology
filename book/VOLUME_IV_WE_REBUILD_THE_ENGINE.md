# Volume IV — We Rebuild the Engine

The research loop has earned the right to propose changes. We return to the tiny language model, freeze one honest baseline, and rebuild its engine one measured bottleneck at a time without surrendering a reference path.

One discovery will create the need for the next; the object under construction never resets.

## Overture

The brass reference machine hums in the Engine Cavern. Every optimization will be offered speed, memory, or scale, but the old machine remains beside it as a tuning fork. A faster path is accepted only when the mathematical responsibility sounds the same note.

```text
reference path ══ measured equivalence ══ optimized path
```

In this volume:

- [Part XII — Rebuilding the Engine Without Breaking the System](#part-xii--rebuilding-the-engine-without-breaking-the-system)

---

## Part XII — Rebuilding the Engine Without Breaking the System

The bounded loop gives us permission to improve—not permission to guess. We freeze the tiny language model, measure where its time and memory go, and replace one bottleneck at a time while the original path remains available to challenge every faster one.

---

### Excavation 151 — A Reproducible Baseline — Improve Something That Actually Exists

> **Mathematical roots:** [Causality & Experimental Design](../MATHEMATICS_ATLAS.md#causality) · [Mathematical Foundations & Measurement](../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Model systems and engine optimization

The bounded loop can approve a candidate, but approval is meaningless if nobody can reconstruct the system it is supposed to improve.

Nothing in the Engine Cavern yet bears today's mathematical name. There is only the enginewright, the brass reference machine, and one plausible action: keep the final score and the model file; those should be enough to compare the next idea.

The rule survives the easy cases. The next case leaves a crack through the middle of it: a rerun changes the data order, random seed, tokenizer revision, and library behavior. Its score moves even though the proposed improvement was never applied. More confidence cannot repair information that never entered the rule.

*The enginewright sketches the break before changing it:*

```text
observation
    │
    ▼
[keep the final score and the model…]
    │
    ╳  a rerun changes the data order,…
    │
    ▼
[freeze the model specification, data…]
```

Two trails now cross the brass reference machine. The pale trail bears the instruction “keep the final score and the model file; those should be enough to compare the next idea.” It disappears into the observed failure: a rerun changes the data order, random seed, tokenizer revision, and library behavior. Its score moves even though the proposed improvement was never applied. The darker trail carries one additional capacity—to freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed reproducible baseline mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the brass reference machine is altered in exactly one way: freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline. Much later, people will call this territory **A Reproducible Baseline**. Here the name is only a memory of the failure it can survive.

The brass reference machine has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and reproducible baseline looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made. The Engine Cavern lets reproducible baseline change speed, memory, or scale while the brass reference machine guards meaning. Equality here is not decoration; it is a promise that the optimized path performs the same mathematical responsibility by another physical route.

#### Improve Something That Actually Exists

Run the same tiny tiger-language model twice from the recorded seed. Only after its loss curve and held-out score agree do we permit one component to change.

#### The calculation hidden inside a reproducible baseline

The enginewright carries the reproducible baseline scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The frozen run scores 2.4 and the candidate scores 2.1 on the same loss test. Looking at 2.1 alone cannot tell you whether anything improved. Remove the old 2.4 from the new 2.1: the remaining −0.3 is the candidate's change. We call the old measurement m_baseline, the new one m_candidate, and the remainder delta m only after doing that comparison.

m_baseline is the frozen model's measurement; m_candidate is measured by the same procedure; delta m names only the change between them.

##### Why the melody needs these exact notes

[Subtraction](../MATHEMATICAL_MOVES.md#subtraction) removes the common baseline and isolates the candidate's change. Addition would make two large scores look impressive even when they are identical. The order fixes the sign: positive means the candidate raised this metric.

Before the line is compressed, notice its recurring motions: **the chisel**—what is shared is removed so the remaining change can be seen. They are the handholds by which the reader can later climb back from notation to meaning.

The enginewright reads the journey of reproducible baseline once more across the brass reference machine, then lets the words contract without losing their order:

$$
\Delta m=m_{\text{candidate}}-m_{\text{baseline}}
$$

#### Where a reproducible baseline runs out

Reproducibility makes differences attributable; it does not tell us which component is worth changing.

The brass reference machine answers today's question and falls silent at the next. That silence is precise: Reproducible Baseline was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the brass reference machine

Rebuild the reproducible baseline scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/151-reproducible-baseline/README.md).*

---

### Excavation 152 — Profiling — Measure Where the Time Went

> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Model systems and engine optimization

A reproducible baseline gives us a trustworthy before-state. Its first run is too slow for the ranger station, but a total runtime does not identify the guilty stage.

At the Engine Cavern, the enginewright returns to the brass reference machine. Yesterday's instrument still lies open, so the first move asks for no new magic: optimize the largest-looking matrix because attention is famous for being expensive.

Reality answers without terminology: the device spends much of the run waiting for data and moving tensors. Making one matrix faster barely changes the wall clock. The brass reference machine now holds two situations the old rule cannot keep apart.

*The enginewright sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   optimize the largest-looking matrix… the device spends much of the run…
            \        /
             \      /
              measure data loading, computation,…
```

The brass reference machine is divided down the middle. Left side: “optimize the largest-looking matrix because attention is famous for being expensive.” Its final mark records the device spends much of the run waiting for data and moving tensors. Making one matrix faster barely changes the wall clock. Right side: the same starting evidence, now allowed to measure data loading, computation, communication, and idle time separately before choosing a repair. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given profiling a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: measure data loading, computation, communication, and idle time separately before choosing a repair. The name **Profiling** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to optimize the largest-looking matrix because attention is famous for being expensive; on the other lies the observed fact that the device spends much of the run waiting for data and moving tensors. Making one matrix faster barely changes the wall clock. The bridge called profiling has exactly the planks needed to measure data loading, computation, communication, and idle time separately before choosing a repair.

#### Measure Where the Time Went

A 100 ms step contains 35 ms of loading, 45 ms of compute, 10 ms of communication, and 10 ms idle. The first engineering question is now visible in numbers.

#### The calculation hidden inside profiling

The enginewright carries the profiling scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Start a stopwatch with one training step. Loading ends at 35 ms; computation then carries the clock to 80; communication to 90; idle synchronization to 100. These are consecutive pieces of one elapsed interval, so you join them end to end. The name T_step is simply the final reading after T_data, T_compute, T_communication, and T_idle have all contributed.

Each T names elapsed time assigned to one non-overlapping stage of the same training step.

##### Why the melody needs these exact notes

[Addition](../MATHEMATICAL_MOVES.md#addition) is forced because these non-overlapping durations occur along one wall-clock path and accumulate into total time. Multiplication would claim that doubling one stage scales every other stage. The equality is valid only when the measured categories cover the step without overlap.

Listen beneath profiling: **the joining river**—separate contributions meet without losing where they came from. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Nothing remains unnamed in the profiling case on the brass reference machine. We can finally trade the long route for its compact map:

$$
T_{\text{step}}=T_{\text{data}}+T_{\text{compute}}+T_{\text{communication}}+T_{\text{idle}}
$$

#### Where profiling runs out

A profile describes this workload on this hardware; changing sequence length or batch size can move the bottleneck.

A final test reaches beyond the new instrument. It does not refute Profiling; it reveals the edge of what was constructed. The enginewright carries that edge into the following room.

#### Return to the brass reference machine

Rebuild the profiling scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/152-profiling/README.md).*

---

### Excavation 153 — The Input Pipeline — Stop Making the Accelerator Wait

> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Model systems and engine optimization

Profiling reveals that the accelerator repeatedly waits for the next token batch. The model is ready, but its evidence is still being read and prepared.

Morning reaches the Engine Cavern before anyone has a name for today's difficulty. Beside the brass reference machine, the enginewright tries the smallest continuation of what already works: load a batch, wait until loading finishes, compute it, and only then begin loading the next one.

Then the quiet test arrives: data time and compute time are paid sequentially on every step, leaving expensive compute hardware idle. What looked like simplicity is revealed as a missing distinction.

*The enginewright sketches the break before changing it:*

```text
OLD PATH:  request ──▶ load a batch, wait until loading… ──▶ data time and compute time are paid…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ prepare the next batch while the… ──▶ accountable result
```

The enginewright turns the brass reference machine toward the light. Through the old engraving, load a batch, wait until loading finishes, compute it, and only then begin loading the next one, the evidence ends in the same contradiction: data time and compute time are paid sequentially on every step, leaving expensive compute hardware idle. A second engraving adds only the power to prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The enginewright circles the place where the two input pipeline cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering. The enginewright writes **The Input Pipeline** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The enginewright does not memorize input pipeline. Instead, the enginewright memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering. The formal name merely lets that motion be shared.

#### Stop Making the Accelerator Wait

If loading takes 35 ms and compute 45 ms, serial work costs 80 ms. Once overlapped, a steady-state step is governed mainly by the slower 45 ms stage.

#### The calculation hidden inside the input pipeline

The enginewright carries the input pipeline scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Now give the ranger station's data loader and accelerator separate workers and start both together. Loading finishes after 35 ms, but the next step is still waiting for computation at 45 ms. The pair is ready when the slower worker finishes—not after 35+45 ms. That finishing time is what T_overlapped records; the approximation sign leaves room for pipeline startup and coordination.

The two times describe stages allowed to run concurrently after the pipeline is filled.

##### Why the melody needs these exact notes

[Maximum](../MATHEMATICAL_MOVES.md#maximum) appears because concurrent stages finish when the slower one finishes. Adding would describe serial execution—the failed design. [Approximation](../MATHEMATICAL_MOVES.md#approximation) admits startup, synchronization, and overhead that prevent perfect overlap.

The calculation borrows several gestures already encountered elsewhere: **the highest lantern**—the strongest surviving possibility sets the visible ceiling. the input pipeline feels new because the objects are new; the gestures remain recognizably human.

The story of input pipeline has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
T_{\text{overlapped}}\approx\max(T_{\text{data}},T_{\text{compute}})
$$

#### Where the input pipeline runs out

Prefetching can hide latency, not unlimited data cost; workers, memory, or storage bandwidth can become the next limit.

One unsolved mark remains on the brass reference machine. None of the responsibilities inside Input Pipeline can move it, and so it becomes the observation from which the next excavation must begin.

#### Return to the brass reference machine

Rebuild the input pipeline scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/153-input-pipeline/README.md).*

---

### Excavation 154 — Sequence Packing — Stop Training on Empty Space

> **Mathematical roots:** [Optimization](../MATHEMATICS_ATLAS.md#optimization) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

The input pipeline now keeps the device busy. Inspection shows that many of the tokens occupying each fixed rectangle are padding rather than language.

The brass reference machine at the Engine Cavern still carries the marks of the previous discovery. The enginewright follows them as far as they seem willing to go: pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste.

The enginewright repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: the loss ignores padding, but attention and matrix multiplication still spend time and memory carrying those empty positions. The failure is stable enough to become evidence.

*The enginewright sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ pad every sentence to the longest… ──▶ blurred: the loss ignores padding, but…
      │
      └── new lens ──▶ pack several short examples into each… ──▶ distinction survives
```

Across the brass reference machine, the old path and the repaired path run side by side. One carries “pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste”; the other knows how to pack several short examples into each fixed-length row and mask their boundaries so examples cannot read one another. When the failure—the loss ignores padding, but attention and matrix multiplication still spend time and memory carrying those empty positions—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to sequence packing. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: pack several short examples into each fixed-length row and mask their boundaries so examples cannot read one another. This problem and its repair will travel under the name **Sequence Packing**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste? The answer remains the loss ignores padding, but attention and matrix multiplication still spend time and memory carrying those empty positions. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

#### Stop Training on Empty Space

Lengths 6, 5, 3, and 2 fill two rows of length 8 exactly. Padding falls from 16 allocated positions with 6 empty to 16 positions with none empty.

#### The calculation hidden inside sequence packing

The enginewright carries the sequence packing scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Draw two rows with eight boxes each: sixteen paid positions. Place sequences of lengths 6 and 2 in the first row, then 5 and 3 in the second. All sixteen boxes now contain real tokens. To ask what share of the paid space teaches the model, put useful boxes over paid boxes: 16/16. Eta_pack is only a short name for that useful fraction.

The numerator counts language tokens that create lessons; the denominator counts every position for which hardware reserves work.

##### Why the melody needs these exact notes

[Division](../MATHEMATICAL_MOVES.md#division) forms the useful share per allocated position, making batches of different sizes comparable. A raw token count would reward larger batches even if their wasted fraction were worse. The ratio stays between zero and one because real tokens cannot exceed allocated positions.

Three old motions cast new shadows here: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Cover the prose about sequence packing and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
\eta_{\text{pack}}=\frac{N_{\text{real tokens}}}{N_{\text{allocated positions}}}
$$

#### Where sequence packing runs out

Packing improves utilization only if masks and position resets prevent cross-example contamination.

The sequence packing repair holds, but the world asks for something it was never given. At the Engine Cavern, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the brass reference machine

Rebuild the sequence packing scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/154-sequence-packing/README.md).*

---

### Excavation 155 — Rotary Position Embeddings — Let Distance Enter the Match

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

Packed training supplies dense sequences, but the learned absolute position cards from our first GPT bind each slot to a private identity rather than making relative displacement part of the query-key match.

Night gathers around the Engine Cavern. Under the light of the brass reference machine, the enginewright refuses to invent prematurely and begins with the plain rule: learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples.

At the edge of the brass reference machine, the shortcut produces its consequence: moving the same phrase from positions 10–12 to 110–112 changes every position vector although the internal distances are unchanged. That consequence, not a textbook, earns the next move.

*The enginewright sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: learn an unrelated vector for every…
possible road B ─┘              └── loses: moving the same phrase from positions…

same roads ──▶ repaired map ──▶ rotate pairs of query and key…
```

The enginewright covers the new mark and the old contradiction returns: moving the same phrase from positions 10–12 to 110–112 changes every position vector although the internal distances are unchanged. The cover is lifted, restoring the ability to rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason rotary position embeddings exists.

What must change for rotary position embeddings is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference. That threshold is where **Rotary Position Embeddings** enters the story.

The marks on the brass reference machine form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. rotary position embeddings is not any single point. It is the path connecting them in the only order that makes the last point necessary.

#### Let Distance Enter the Match

Rotate the two coordinates of tiger by angle mθ and river by nθ. Their match depends on (m−n)θ, so shifting both tokens together preserves their separation signal.

#### The calculation hidden inside rotary position embeddings

The enginewright carries the rotary position embeddings scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Imagine the pair of coordinates as a clock hand beginning at [1,0]. At position one, a quarter-turn sends it to [0,1]; at position two, another quarter-turn sends it to [−1,0]. The hand's length never changes—only its angle does. Multiplying position p by the chosen turn theta tells us the total angle; the four cosine-and-sine entries record how any starting pair must contribute to its two rotated coordinates.

p is token position, theta is one rotation frequency, and R rotates one coordinate pair without changing its length.

##### Why the melody needs these exact notes

[Function application](../MATHEMATICAL_MOVES.md#function-application) applies the same rotation rule at each position. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) mixes the two coordinates according to cosine and sine; [addition](../MATHEMATICAL_MOVES.md#addition) combines their signed contributions. Squaring or adding p would change magnitude instead of encoding position as an angle whose differences survive a shared shift.

The symbols are about to change costume, but their work has appeared before: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the joining river**—separate contributions meet without losing where they came from. This is how distant excavations begin to sound like variations of one melody.

The brass reference machine already contains the complete rotary position embeddings mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
R(p\theta)=\begin{bmatrix}\cos(p\theta)&-\sin(p\theta)\\\sin(p\theta)&\cos(p\theta)\end{bmatrix}
$$

#### Where rotary position embeddings runs out

RoPE supplies structured relative position, but distances far beyond training still produce unfamiliar phases.

Here the new path ends honestly. Rotary Position Embeddings can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the brass reference machine

Rebuild the rotary position embeddings scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/155-rotary-position/README.md).*

---

### Excavation 156 — Relative Position Bias — What Should Happen Beyond the Seen Window?

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

Rotary position makes displacement visible inside the attention match. When the station tests much longer sequences, the model must rank relationships at separations absent from training.

Inside the Engine Cavern, every old tool is given one honest chance. The enginewright sets the brass reference machine between the evidence and the desired answer, then tries to trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there.

For a moment the mark looks complete. Then the evidence refuses to fit: a mathematically defined position is not necessarily a learned behavior; attention can become erratic at unfamiliar separations. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The enginewright sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: trust every unseen distance to behave…
                         │
                         └── mismatch: a mathematically defined position is…

reference evidence ──▶ measured repair: add an explicit distance-dependent…
```

The enginewright lays two translucent sheets over the brass reference machine. The first is inscribed, “trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there.” Its path ends where a mathematically defined position is not necessarily a learned behavior; attention can become erratic at unfamiliar separations. The second receives the same evidence but is allowed to add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation. Held to the light, the sheets separate at exactly one decision.

No one reaches for a relative position bias formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The enginewright changes only that one responsibility: add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation. When the ink dries, the name **Relative Position Bias** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The brass reference machine keeps both histories. Its older mark still says, ‘trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there’; beside it, the newer mark says, ‘add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation.’ The distance between those sentences is the exact shape of relative position bias: no larger than the failure required, and no smaller than reality permits.

#### What Should Happen Beyond the Seen Window

For one head with slope 0.1, a key 2 places back receives −0.2 while a key 20 places back receives −2.0 before softmax. Content can overcome the penalty, but distance has a predictable cost.

#### The calculation hidden inside relative position bias

The enginewright carries the relative position bias scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Suppose tiger matches one key with content score 3.0. The key is two places away, and we decide that each place should cost 0.1, so distance contributes 2×0.1=0.2. Removing that cost leaves 2.8. A key twenty places away pays 20×0.1=2.0 and keeps 1.0. We now name the original content score s_ij, the price per place m, and the adjusted result s-prime.

s_ij is the content match, |i−j| is token separation, m is this head's nonnegative distance slope, and s-prime is the adjusted score.

##### Why the melody needs these exact notes

[Subtraction](../MATHEMATICAL_MOVES.md#subtraction) lowers rather than raises distant matches. [Absolute value](../MATHEMATICAL_MOVES.md#absolute-value) keeps separation size while discarding left-versus-right direction in this bias. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) lets slope m control the price per position; adding a fixed m would not make farther tokens cost more.

Inside relative position bias, familiar operations return with stricter duties: **the chisel**—what is shared is removed so the remaining change can be seen; and **the lock and key**—one influence matters through another, and either missing factor can close the path. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Every mark needed for relative position bias is now visible on the brass reference machine. The symbols do not add an idea; they bind the discovered moves into one line:

$$
s_{ij}^{\prime}=s_{ij}-m\lvert i-j\rvert
$$

#### Where relative position bias runs out

A fixed distance preference can suppress a decisive remote clue and is an architectural bias, not universal truth.

At the Engine Cavern, the enginewright leaves a blank beneath the new mark. Relative Position Bias has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the brass reference machine

Rebuild the relative position bias scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/156-relative-position-bias/README.md).*

---

### Excavation 157 — The KV Cache — Stop Re-reading the Entire Past

> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Model systems and engine optimization

Relative position now behaves predictably, but autoregressive generation still reruns the Transformer over the full prefix after appending each token.

A new case arrives at the Engine Cavern, but the enginewright first reaches for the familiar brass reference machine. Its promise is simple: at step t, recompute keys and values for positions 1 through t because the prefix is presented again.

The rule survives the easy cases. The next case leaves a crack through the middle of it: past token representations are unchanged in causal decoding, so the same projections are calculated repeatedly while one new token is added. More confidence cannot repair information that never entered the rule.

*The enginewright sketches the break before changing it:*

```text
observation
    │
    ▼
[at step t, recompute keys and values…]
    │
    ╳  past token representations are…
    │
    ▼
[store each layer's past keys and…]
```

Two trails now cross the brass reference machine. The pale trail bears the instruction “at step t, recompute keys and values for positions 1 through t because the prefix is presented again.” It disappears into the observed failure: past token representations are unchanged in causal decoding, so the same projections are calculated repeatedly while one new token is added. The darker trail carries one additional capacity—to store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed kv cache mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the brass reference machine is altered in exactly one way: store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache. Much later, people will call this territory **The KV Cache**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the brass reference machine. The failed path remains visible beneath the repair, because kv cache is easier to remember when its scar remains attached to it. The scar reads, ‘past token representations are unchanged in causal decoding, so the same projections are calculated repeatedly while one new token is added’; the new line exists only to keep that loss from happening again.

#### Stop Re-reading the Entire Past

Generating token 101 computes one new key and value, then reads the 100 cached pairs. It does not rebuild pairs 1 through 100.

#### The calculation hidden inside the kv cache

The enginewright carries the kv cache scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

At token 101, write the hundred old keys on cards and compute one new card. Nothing on the old cards has changed, so combining must mean placing card 101 after cards 1 through 100—not adding their numbers together. K_1:t−1 names the ordered stack already present, k_t the one new card, and K_1:t the longer stack after appending.

K_1:t−1 is the unchanged past cache, k_t is the newly computed key, and K_1:t is the cache available to the current query.

##### Why the melody needs these exact notes

[Function application](../MATHEMATICAL_MOVES.md#function-application) names one append operation. Appending preserves order and old values; [addition](../MATHEMATICAL_MOVES.md#addition) would numerically blend keys and destroy which token produced each one. The indices show that only position t is new.

Trace each operation by touch rather than by name: **the joining river**—separate contributions meet without losing where they came from. Together they form the smallest mechanism that survives the counterexample.

The enginewright reads the journey of kv cache once more across the brass reference machine, then lets the words contract without losing their order:

$$
K_{1:t}=\mathrm{append}(K_{1:t-1},k_t)
$$

#### Where the kv cache runs out

Because every past key and value must remain available, saved computation becomes growing memory and memory-bandwidth cost, especially for long contexts and many users.

The brass reference machine answers today's question and falls silent at the next. That silence is precise: KV Cache was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the brass reference machine

Rebuild the kv cache scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/157-kv-cache/README.md).*

---

### Excavation 158 — Multi-Query Attention — Why Cache Separate Copies for Every Head?

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

Caching turns repeated arithmetic into memory reads. Profiling now shows decoding limited by loading separate key and value histories for every attention head.

The doors of the Engine Cavern close against the wind. On the brass reference machine, the enginewright writes the cheapest rule that might still be true: preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections.

Reality answers without terminology: the caches grow with both sequence length and head count, and loading them dominates the arithmetic for one new token. The brass reference machine now holds two situations the old rule cannot keep apart.

*The enginewright sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   preserve one complete KV cache for… the caches grow with both sequence…
            \        /
             \      /
              keep many query heads but share one…
```

The brass reference machine is divided down the middle. Left side: “preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections.” Its final mark records the caches grow with both sequence length and head count, and loading them dominates the arithmetic for one new token. Right side: the same starting evidence, now allowed to keep many query heads but share one key head and one value head across them. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given multi-query attention a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: keep many query heads but share one key head and one value head across them. The name **Multi-Query Attention** arrives afterward, like a title given to a path whose stones are already underfoot.

A thread now runs backward from multi-query attention through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and the caches grow with both sequence length and head count, and loading them dominates the arithmetic for one new token. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction.

#### Why Cache Separate Copies for Every Head

Eight query experts ask eight different questions of the same cached catalog. Cache entries fall from eight key-value pairs per token to one pair per token.

#### The calculation hidden inside multi-query attention

The enginewright carries the multi-query attention scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Take one layer with 100 remembered tokens. If each KV head stores 64 coordinates, one head needs 100×64 coordinate slots for keys and the same again for values. Eight heads need eight copies of those slots. The three counts—tokens L, KV heads H_KV, and width d_h—multiply because every choice from one count is paired with every choice from the others.

L is cached sequence length, H_KV is the number of key-value heads, and d_h is the width stored per head.

##### Why the melody needs these exact notes

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) appears because every token stores every KV head's coordinates: doubling any factor doubles memory. [Proportionality](../MATHEMATICAL_MOVES.md#proportionality) omits fixed factors such as both K and V, bytes per number, layers, and batch size while preserving the scaling argument.

The mandala has curved back upon itself. In this chamber we meet **the lock and key**—one influence matters through another, and either missing factor can close the path. What seemed like a new formula is older mathematical instinct arranged around a new need.

Nothing remains unnamed in the multi-query attention case on the brass reference machine. We can finally trade the long route for its compact map:

$$
M_{\text{KV}}\propto L H_{\text{KV}} d_h
$$

#### Where multi-query attention runs out

A single shared catalog can remove distinctions that genuinely need different key-value spaces.

A final test reaches beyond the new instrument. It does not refute Multi-Query Attention; it reveals the edge of what was constructed. The enginewright carries that edge into the following room.

#### Return to the brass reference machine

Rebuild the multi-query attention scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/158-multi-query-attention/README.md).*

---

### Excavation 159 — Grouped-Query Attention — Recover Some Specialist Memory

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Model systems and engine optimization

One shared KV head makes decoding light enough for the station, but evaluation finds a quality loss on relationships that benefited from distinct catalogs.

Nothing in the Engine Cavern yet bears today's mathematical name. There is only the enginewright, the brass reference machine, and one plausible action: return immediately to one KV head per query head.

Then the quiet test arrives: quality recovers, but so does the full cache and bandwidth cost that forced sharing. What looked like simplicity is revealed as a missing distinction.

*The enginewright sketches the break before changing it:*

```text
OLD PATH:  request ──▶ return immediately to one KV head per… ──▶ quality recovers, but so does the…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ partition query heads into groups;… ──▶ accountable result
```

The enginewright turns the brass reference machine toward the light. Through the old engraving, return immediately to one KV head per query head, the evidence ends in the same contradiction: quality recovers, but so does the full cache and bandwidth cost that forced sharing. A second engraving adds only the power to partition query heads into groups; queries remain distinct while each group shares one key-value head. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The enginewright circles the place where the two grouped-query attention cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: partition query heads into groups; queries remain distinct while each group shares one key-value head. The enginewright writes **Grouped-Query Attention** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The enginewright places a finger over the new distinction. At once the two cases collapse and quality recovers, but so does the full cache and bandwidth cost that forced sharing. Lifting the finger restores only this capacity: partition query heads into groups; queries remain distinct while each group shares one key-value head. That tiny reversible motion is the chapter's proof of necessity.

#### Recover Some Specialist Memory

Eight query heads arranged into two KV groups preserve two catalogs. The cache is twice MQA's size but one quarter of ordinary eight-head KV storage.

#### The calculation hidden inside grouped-query attention

The enginewright carries the grouped-query attention scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Line up the model's eight query heads and two KV catalogs. Four consecutive query heads must point to catalog 0 and the next four to catalog 1. Scaling head number h from the eight-head range into the two-catalog range gives h×2/8; rounding down turns positions 0 through 3 into address 0 and positions 4 through 7 into address 1. The name g(h) records that address-making rule.

h is a query-head index, H_Q counts query heads, H_KV counts shared KV groups, and g(h) selects the group serving head h.

##### Why the melody needs these exact notes

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) spreads the KV group range across query-head indices; [division](../MATHEMATICAL_MOVES.md#division) converts one query index into its proportional group location. The floor deliberately [rounds](../MATHEMATICAL_MOVES.md#rounding) down so every head receives one valid discrete group rather than a fractional address.

Before the line is compressed, notice its recurring motions: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. They are the handholds by which the reader can later climb back from notation to meaning.

The story of grouped-query attention has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
g(h)=\left\lfloor\frac{hH_{\text{KV}}}{H_Q}\right\rfloor
$$

#### Where grouped-query attention runs out

Because sharing deliberately removes independent KV views, the number and assignment of groups remain empirical design choices whose quality must be measured.

One unsolved mark remains on the brass reference machine. None of the responsibilities inside Grouped-Query Attention can move it, and so it becomes the observation from which the next excavation must begin.

#### Return to the brass reference machine

Rebuild the grouped-query attention scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/159-grouped-query-attention/README.md).*

---

### Excavation 160 — FlashAttention — The Arithmetic Was Not the Bottleneck

> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Discrete Mathematics, Logic & Algorithms](../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Model systems and engine optimization

Grouped-query attention makes generation economical, yet training long packed sequences still materializes a large attention-score matrix in slow device memory.

At the Engine Cavern, the enginewright returns to the brass reference machine. Yesterday's instrument still lies open, so the first move asks for no new magic: reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost.

The enginewright repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: approximation changes the model, while profiling shows much of the time is spent writing and rereading exact intermediate scores rather than multiplying them. The failure is stable enough to become evidence.

*The enginewright sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ reduce arithmetic by approximating… ──▶ blurred: approximation changes the model,…
      │
      └── new lens ──▶ tile queries, keys, and values into… ──▶ distinction survives
```

Across the brass reference machine, the old path and the repaired path run side by side. One carries “reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost”; the other knows how to tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once. When the failure—approximation changes the model, while profiling shows much of the time is spent writing and rereading exact intermediate scores rather than multiplying them—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to flashattention. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once. This problem and its repair will travel under the name **FlashAttention**, but the name carries no knowledge the scene has not earned.

What changed on the brass reference machine can be said without symbols. Before, the method could only reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost; now it can also tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

#### The Arithmetic Was Not the Bottleneck

Process two score tiles. Carry only the running maximum, normalized denominator, and weighted value total into the next tile; the final answer matches ordinary softmax attention.

#### The calculation hidden inside flashattention

The enginewright carries the flashattention scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The model's first attention tile contains scores 1 and 4, so 4 becomes the remembered safety ceiling. The next tile contains 3 and 2; neither exceeds 4, so the ceiling remains 4. If a later tile contained 7, the ceiling would become 7 and the earlier exponential totals would be rescaled. Thus m is the largest score already processed, the s_j values are the arriving tile, and m-prime is the one maximum covering both histories.

m is the largest score already seen, s_j are scores in the new tile, and m-prime is the safe maximum for the combined tiles.

##### Why the melody needs these exact notes

[Maximum](../MATHEMATICAL_MOVES.md#maximum) preserves the one value needed to stabilize exponentials across both old and new tiles. Addition would invent a score that never occurred; averaging could be lower than the true maximum and allow overflow. The prime marks the updated running version; see [symbol decorations](../MATHEMATICAL_MOVES.md#symbol-decorations).

Listen beneath flashattention: **the highest lantern**—the strongest surviving possibility sets the visible ceiling. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Cover the prose about flashattention and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
m^{\prime}=\max(m,\max_j s_j)
$$

#### Where flashattention runs out

FlashAttention removes avoidable memory traffic, not quadratic pairwise arithmetic itself.

The flashattention repair holds, but the world asks for something it was never given. At the Engine Cavern, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the brass reference machine

Rebuild the flashattention scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/160-flash-attention/README.md).*

---

### Excavation 161 — RMSNorm — Do We Need to Subtract the Centre?

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

FlashAttention removes one systems bottleneck, making smaller repeated operations visible. Layer normalization calculates both a mean and a spread at every token and layer.

Morning reaches the Engine Cavern before anyone has a name for today's difficulty. Beside the brass reference machine, the enginewright tries the smallest continuation of what already works: delete normalization because each individual operation appears cheap.

At the edge of the brass reference machine, the shortcut produces its consequence: deep residual streams drift in scale and training destabilizes; the repeated control was doing essential work. That consequence, not a textbook, earns the next move.

*The enginewright sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: delete normalization because each…
possible road B ─┘              └── loses: deep residual streams drift in scale…

same roads ──▶ repaired map ──▶ keep rescaling invariance by dividing…
```

The enginewright covers the new mark and the old contradiction returns: deep residual streams drift in scale and training destabilizes; the repeated control was doing essential work. The cover is lifted, restoring the ability to keep rescaling invariance by dividing by root-mean-square magnitude, while testing whether explicit recentering is dispensable, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason rmsnorm exists.

What must change for rmsnorm is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: keep rescaling invariance by dividing by root-mean-square magnitude, while testing whether explicit recentering is dispensable. That threshold is where **RMSNorm** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In rmsnorm, that memory takes a precise form: whenever deep residual streams drift in scale and training destabilizes; the repeated control was doing essential work, preserve enough structure to keep rescaling invariance by dividing by root-mean-square magnitude, while testing whether explicit recentering is dispensable.

#### Do We Need to Subtract the Centre

Vectors [3,4] and [30,40] become the same relative pattern after division by their RMS, although neither has its mean subtracted.

#### The calculation hidden inside rmsnorm

The enginewright carries the rmsnorm scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Take the model feature pair [3,4]. Adding the raw values would let a negative feature cancel a positive one, so first turn their sizes into 9 and 16. Together they contribute 25; shared across two features that is 12.5 per feature. Its square root, about 3.54, returns to the features' ordinary units. Only now do we call this typical magnitude RMS(x) and the feature count d.

d is feature width; each x_i is one feature; RMS(x) is the vector's typical magnitude before a learned scale is applied.

##### Why the melody needs these exact notes

[Squaring](../MATHEMATICAL_MOVES.md#powers) keeps negative and positive feature magnitudes from cancelling. [Summation](../MATHEMATICAL_MOVES.md#summation) gathers every feature's contribution, [division](../MATHEMATICAL_MOVES.md#division) makes the magnitude per feature, and the [square root](../MATHEMATICAL_MOVES.md#square-root) returns to the original scale. Omitting division would make wider vectors appear larger merely for having more coordinates.

The calculation borrows several gestures already encountered elsewhere: **the echoing chamber**—large departures return with greater force while opposite signs stop cancelling; **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. rmsnorm feels new because the objects are new; the gestures remain recognizably human.

The brass reference machine already contains the complete rmsnorm mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
\mathrm{RMS}(x)=\sqrt{\frac1d\sum_{i=1}^{d}x_i^2}
$$

#### Where rmsnorm runs out

RMSNorm does not guarantee that recentering is unimportant for every architecture or task.

Here the new path ends honestly. RMSNorm can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the brass reference machine

Rebuild the rmsnorm scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/161-rmsnorm/README.md).*

---

### Excavation 162 — Pre-Normalization — Protect the Residual Highway

> **Mathematical roots:** [Optimization](../MATHEMATICS_ATLAS.md#optimization) · [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Model systems and engine optimization

The block is cheaper, but making it deeper reveals unstable early gradients when normalization follows each residual addition.

The brass reference machine at the Engine Cavern still carries the marks of the previous discovery. The enginewright follows them as far as they seem willing to go: keep post-normalization because each block's output then looks standardized before the next block.

For a moment the mark looks complete. Then the evidence refuses to fit: the supposedly clean output places normalization directly on the identity route every gradient must cross, making the long residual path harder to preserve. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The enginewright sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: keep post-normalization because each…
                         │
                         └── mismatch: the supposedly clean output places…

reference evidence ──▶ measured repair: normalize only the input to the…
```

The enginewright lays two translucent sheets over the brass reference machine. The first is inscribed, “keep post-normalization because each block's output then looks standardized before the next block.” Its path ends where the supposedly clean output places normalization directly on the identity route every gradient must cross, making the long residual path harder to preserve. The second receives the same evidence but is allowed to normalize only the input to the changing branch and let the identity stream pass around it unchanged. Held to the light, the sheets separate at exactly one decision.

No one reaches for a pre-normalization formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The enginewright changes only that one responsibility: normalize only the input to the changing branch and let the identity stream pass around it unchanged. When the ink dries, the name **Pre-Normalization** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because the supposedly clean output places normalization directly on the identity route every gradient must cross, making the long residual path harder to preserve, while the other can normalize only the input to the changing branch and let the identity stream pass around it unchanged. That fork—not the vocabulary—is where pre-normalization lives.

#### Protect the Residual Highway

A block computes a normalized proposal F, then adds that proposal to the untouched x. If F initially contributes little, the block can behave almost like identity.

#### The calculation hidden inside pre-normalization

The enginewright carries the pre-normalization scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Let the residual stream carry a useful tiger signal x. The new branch examines a normalized copy and proposes a correction F(...). At initialization that proposal may be almost zero. Adding it to the untouched x lets the block say 'change nothing yet'; replacing x with the proposal would destroy the signal. The layer indices merely distinguish the stream before and after this addition.

x_l is the residual stream entering layer l; RMSNorm prepares only the branch; F proposes a change; x_l+1 is the next stream.

##### Why the melody needs these exact notes

[Function application](../MATHEMATICAL_MOVES.md#function-application) fixes the order: normalize, then transform. [Addition](../MATHEMATICAL_MOVES.md#addition) preserves an untouched identity contribution beside the proposal. Replacing x with F would erase the gradient highway; normalizing the sum would place another transformation on that highway.

Three old motions cast new shadows here: **the joining river**—separate contributions meet without losing where they came from. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Every mark needed for pre-normalization is now visible on the brass reference machine. The symbols do not add an idea; they bind the discovered moves into one line:

$$
x_{\ell+1}=x_\ell+F(\mathrm{RMSNorm}(x_\ell))
$$

#### Where pre-normalization runs out

Pre-normalization improves gradient behavior but changes representation scale and does not eliminate every deep-training instability.

At the Engine Cavern, the enginewright leaves a blank beneath the new mark. Pre-Normalization has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the brass reference machine

Rebuild the pre-normalization scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/162-pre-normalization/README.md).*

---

### Excavation 163 — SwiGLU — Let One Learned Path Gate Another

> **Mathematical roots:** [Optimization](../MATHEMATICS_ATLAS.md#optimization) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

Pre-normalization lets gradients reach deep blocks, but the ordinary feed-forward network applies one fixed activation independently to one projection.

Night gathers around the Engine Cavern. Under the light of the brass reference machine, the enginewright refuses to invent prematurely and begins with the plain rule: make the hidden layer merely wider and trust more coordinates to express every conditional interaction.

The rule survives the easy cases. The next case leaves a crack through the middle of it: width adds capacity but still asks one projection both to create content and decide when that content matters. More confidence cannot repair information that never entered the rule.

*The enginewright sketches the break before changing it:*

```text
observation
    │
    ▼
[make the hidden layer merely wider…]
    │
    ╳  width adds capacity but still asks…
    │
    ▼
[create one content projection and one…]
```

Two trails now cross the brass reference machine. The pale trail bears the instruction “make the hidden layer merely wider and trust more coordinates to express every conditional interaction.” It disappears into the observed failure: width adds capacity but still asks one projection both to create content and decide when that content matters. The darker trail carries one additional capacity—to create one content projection and one gate projection; use the smooth gate to scale content feature by feature. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed swiglu mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the brass reference machine is altered in exactly one way: create one content projection and one gate projection; use the smooth gate to scale content feature by feature. Much later, people will call this territory **SwiGLU**. Here the name is only a memory of the failure it can survive.

The brass reference machine has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and swiglu looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

#### Let One Learned Path Gate Another

For a token describing a river bank, one path proposes financial features while the gate suppresses them; in a money context the same content path can be opened.

#### The calculation hidden inside swiglu

The enginewright carries the swiglu scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Picture one candidate feature saying 'river-bank meaning: 5.' A separate learned gate examines this occurrence of bank. Near the river it may open close to 1, allowing almost all 5 through; near money it may close near 0, silencing that feature. This demands multiplication: zero times content must become zero. W_v creates the candidate, W_g creates gate evidence, SiLU shapes that evidence, and the circled product pairs each gate with its own feature.

W_g creates gate evidence, SiLU bends it smoothly, W_v creates candidate content, and the circled product combines matching hidden coordinates.

##### Why the melody needs these exact notes

[Function application](../MATHEMATICAL_MOVES.md#function-application) makes the gate depend on this token. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) is forced because a zero gate must silence its matching content and a partial gate must scale it. Addition would let closed content leak through. The elementwise mark means aligned coordinates interact rather than forming every pair.

The symbols are about to change costume, but their work has appeared before: **the lock and key**—one influence matters through another, and either missing factor can close the path. This is how distant excavations begin to sound like variations of one melody.

The enginewright reads the journey of swiglu once more across the brass reference machine, then lets the words contract without losing their order:

$$
\mathrm{SwiGLU}(x)=\mathrm{SiLU}(xW_g)\odot(xW_v)
$$

#### Where swiglu runs out

Gating improves useful capacity but increases projection parameters and does not explain what every hidden feature means.

The brass reference machine answers today's question and falls silent at the next. That silence is precise: SwiGLU was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the brass reference machine

Rebuild the swiglu scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/163-swiglu/README.md).*

---

### Excavation 164 — Weight Tying — Use One Word Geometry Twice

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

SwiGLU improves the block, but the model stores one large table for input embeddings and another large matrix for scoring the same vocabulary at output.

Inside the Engine Cavern, every old tool is given one honest chance. The enginewright sets the brass reference machine between the evidence and the desired answer, then tries to let both matrices learn independently because reading a token and predicting it are different jobs.

Reality answers without terminology: the model spends parameters learning two unrelated geometries for the same set of word identities, and rare tokens receive weak evidence in both places. The brass reference machine now holds two situations the old rule cannot keep apart.

*The enginewright sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   let both matrices learn independently… the model spends parameters learning…
            \        /
             \      /
              reuse the embedding table transposed…
```

The brass reference machine is divided down the middle. Left side: “let both matrices learn independently because reading a token and predicting it are different jobs.” Its final mark records the model spends parameters learning two unrelated geometries for the same set of word identities, and rare tokens receive weak evidence in both places. Right side: the same starting evidence, now allowed to reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given weight tying a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias. The name **Weight Tying** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to let both matrices learn independently because reading a token and predicting it are different jobs; on the other lies the observed fact that the model spends parameters learning two unrelated geometries for the same set of word identities, and rare tokens receive weak evidence in both places. The bridge called weight tying has exactly the planks needed to reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias.

#### Use One Word Geometry Twice

The tiger vector used to enter the model also becomes the direction a final hidden state must align with to predict tiger.

#### The calculation hidden inside weight tying

The enginewright carries the weight tying scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The input table already contains a row pointing in the learned direction of tiger. At the output, predicting tiger means asking how strongly the final hidden state points along that same direction. Turning table rows into scoring columns changes only their orientation. E names the existing table, T marks that turn, and equality says W_out is the very same learned values—not a second copy trained to resemble them.

E stores one embedding row per token; transpose turns those rows into output-scoring columns without changing their values.

##### Why the melody needs these exact notes

[Equality](../MATHEMATICAL_MOVES.md#equals) imposes shared parameters rather than merely similar initialization. Transposition changes orientation so matrix shapes fit; it does not relearn or numerically transform the coordinates. Using addition would combine two matrices instead of making one geometry perform both roles.

Nothing remains unnamed in the weight tying case on the brass reference machine. We can finally trade the long route for its compact map:

$$
W_{\text{out}}=E^{\mathsf T}
$$

#### Where weight tying runs out

Tying reduces parameters and imposes a useful constraint, but separate input and output roles may sometimes benefit from extra freedom.

A final test reaches beyond the new instrument. It does not refute Weight Tying; it reveals the edge of what was constructed. The enginewright carries that edge into the following room.

#### Return to the brass reference machine

Rebuild the weight tying scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/164-weight-tying/README.md).*

---

### Excavation 165 — Adam — Give Each Parameter Its Own Step Scale

> **Mathematical roots:** [Optimization](../MATHEMATICS_ATLAS.md#optimization) · [Probability & Statistics](../MATHEMATICS_ATLAS.md#probability) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

Weight tying concentrates more roles in shared parameters. During training, some coordinates receive frequent large gradients while rare-token coordinates receive sparse small ones.

A new case arrives at the Engine Cavern, but the enginewright first reaches for the familiar brass reference machine. Its promise is simple: use the same raw gradient step scale for every parameter.

Then the quiet test arrives: a rate safe for frequent large gradients barely moves sparse coordinates; a rate large enough for sparse coordinates makes noisy ones unstable. What looked like simplicity is revealed as a missing distinction.

*The enginewright sketches the break before changing it:*

```text
OLD PATH:  request ──▶ use the same raw gradient step scale… ──▶ a rate safe for frequent large…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ keep fading memories of gradient… ──▶ accountable result
```

The enginewright turns the brass reference machine toward the light. Through the old engraving, use the same raw gradient step scale for every parameter, the evidence ends in the same contradiction: a rate safe for frequent large gradients barely moves sparse coordinates; a rate large enough for sparse coordinates makes noisy ones unstable. A second engraving adds only the power to keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The enginewright circles the place where the two adam cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude. The enginewright writes **Adam** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The enginewright does not memorize adam. Instead, the enginewright memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude. The formal name merely lets that motion be shared.

#### Give Each Parameter Its Own Step Scale

A frequently noisy weight builds a large second-moment estimate and receives a smaller normalized step; a consistently directed sparse weight can still move.

#### The calculation hidden inside adam

The enginewright carries the adam scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Follow one weight that repeatedly receives gradients near 2 and another that usually receives gradients near 0.2. A single raw step scale makes their movement differ tenfold even if each signal is ordinary for its own weight. Remember each weight's recent direction in m and its recent squared size in v; compare direction with the square root of size, then let eta choose the common overall pace. Epsilon is the tiny floor that keeps a never-touched weight from asking us to divide by zero.

m-hat is bias-corrected directional memory, v-hat is bias-corrected squared-gradient memory, eta is global scale, and epsilon prevents division by zero.

##### Why the melody needs these exact notes

[Division](../MATHEMATICAL_MOVES.md#division) measures direction relative to recent gradient magnitude, giving each coordinate an adaptive scale. The [square root](../MATHEMATICAL_MOVES.md#square-root) returns squared-gradient memory to gradient units. [Subtraction](../MATHEMATICAL_MOVES.md#subtraction) moves opposite estimated uphill direction; adding would increase loss locally.

Trace each operation by touch rather than by name: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; **the road home**—a squared construction returns to the scale of the world that created it; and **the chisel**—what is shared is removed so the remaining change can be seen. Together they form the smallest mechanism that survives the counterexample.

The story of adam has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
\theta_{t+1}=\theta_t-\eta\frac{\widehat m_t}{\sqrt{\widehat v_t}+\epsilon}
$$

#### Where adam runs out

Adaptive scaling can generalize differently from SGD and introduces extra state for every parameter.

One unsolved mark remains on the brass reference machine. None of the responsibilities inside Adam can move it, and so it becomes the observation from which the next excavation must begin.

#### Return to the brass reference machine

Rebuild the adam scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/165-adam/README.md).*

---

### Excavation 166 — AdamW — Keep Shrinkage Separate from Adaptation

> **Mathematical roots:** [Optimization](../MATHEMATICS_ATLAS.md#optimization) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

Adam trains the block, but adding an L2 penalty to the loss sends shrinkage through the optimizer's coordinate-wise rescaling.

The doors of the Engine Cavern close against the wind. On the brass reference machine, the enginewright writes the cheapest rule that might still be true: treat penalty gradients and data gradients identically because both appear in one total loss.

The enginewright repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: coordinates with different gradient histories receive different effective shrinkage even when the intended rule was to decay all selected weights at one rate. The failure is stable enough to become evidence.

*The enginewright sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ treat penalty gradients and data… ──▶ blurred: coordinates with different gradient…
      │
      └── new lens ──▶ apply Adam's adaptive data update and… ──▶ distinction survives
```

Across the brass reference machine, the old path and the repaired path run side by side. One carries “treat penalty gradients and data gradients identically because both appear in one total loss”; the other knows how to apply Adam's adaptive data update and parameter decay as separate operations. When the failure—coordinates with different gradient histories receive different effective shrinkage even when the intended rule was to decay all selected weights at one rate—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to adamw. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: apply Adam's adaptive data update and parameter decay as separate operations. This problem and its repair will travel under the name **AdamW**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—treat penalty gradients and data gradients identically because both appear in one total loss? The answer remains coordinates with different gradient histories receive different effective shrinkage even when the intended rule was to decay all selected weights at one rate. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

#### Keep Shrinkage Separate from Adaptation

Two equal weights with different gradient histories receive different Adam steps but the same proportional decay.

#### The calculation hidden inside adamw

The enginewright carries the adamw scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Suppose two weights both equal 2, although their gradient histories differ. If decay means 'remove one tenth of one percent of the present weight this step,' both should lose the same proportion before their evidence-driven Adam movements differ. Multiplying theta by 1−eta lambda performs that direct shrink. The separate subtraction then applies Adam's learned direction, preventing gradient history from secretly changing the intended decay rule.

lambda is decay strength; the first term shrinks the old parameter directly; the second is Adam's data-driven update.

##### Why the melody needs these exact notes

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) by 1−eta lambda makes decay proportional to current parameter size: a zero weight stays zero and doubling a weight doubles shrinkage. [Subtraction](../MATHEMATICAL_MOVES.md#subtraction) then applies the independently adapted loss step. Hiding decay inside m and v would mix two jobs the formula deliberately separates.

The mandala has curved back upon itself. In this chamber we meet **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the chisel**—what is shared is removed so the remaining change can be seen. What seemed like a new formula is older mathematical instinct arranged around a new need.

Cover the prose about adamw and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
\theta_{t+1}=(1-\eta\lambda)\theta_t-\eta\frac{\widehat m_t}{\sqrt{\widehat v_t}+\epsilon}
$$

#### Where adamw runs out

Decoupled decay still requires choosing which parameters to decay and how strongly.

The adamw repair holds, but the world asks for something it was never given. At the Engine Cavern, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the brass reference machine

Rebuild the adamw scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/166-adamw/README.md).*

---

### Excavation 167 — Gradient Clipping — Stop One Shock from Becoming a Catastrophe

> **Mathematical roots:** [Optimization](../MATHEMATICS_ATLAS.md#optimization) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical) · [Calculus & Differential Change](../MATHEMATICS_ATLAS.md#calculus)
>
> **Applied territory:** Model systems and engine optimization

Most steps are stable, but a rare batch produces an enormous global gradient norm and overwhelms Adam's still-developing moment estimates.

Nothing in the Engine Cavern yet bears today's mathematical name. There is only the enginewright, the brass reference machine, and one plausible action: discard the entire batch whenever any gradient coordinate looks large.

At the edge of the brass reference machine, the shortcut produces its consequence: useful directional evidence is lost, and one arbitrary coordinate threshold ignores the size of the full update vector. That consequence, not a textbook, earns the next move.

*The enginewright sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: discard the entire batch whenever any…
possible road B ─┘              └── loses: useful directional evidence is lost,…

same roads ──▶ repaired map ──▶ preserve the gradient's direction but…
```

The enginewright covers the new mark and the old contradiction returns: useful directional evidence is lost, and one arbitrary coordinate threshold ignores the size of the full update vector. The cover is lifted, restoring the ability to preserve the gradient's direction but scale its whole norm down only when it exceeds a chosen ceiling, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason gradient clipping exists.

What must change for gradient clipping is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: preserve the gradient's direction but scale its whole norm down only when it exceeds a chosen ceiling. That threshold is where **Gradient Clipping** enters the story.

The marks on the brass reference machine form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. gradient clipping is not any single point. It is the path connecting them in the only order that makes the last point necessary.

#### Stop One Shock from Becoming a Catastrophe

A gradient of length 20 with ceiling 5 is multiplied by one quarter. A gradient of length 3 passes unchanged.

#### The calculation hidden inside gradient clipping

The enginewright carries the gradient clipping scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The model's current gradient points in a useful direction but has length 20, while this run permits length 5. The required scale is 5/20, or one quarter, so every component shrinks by one quarter and direction survives. If the next gradient has length 3, the fraction 5/3 would enlarge it—exactly what we do not want—so we cap the multiplier at 1. We call the ceiling c, the original advice g, and the safe advice g-prime.

g is the original gradient vector, c is the allowed norm ceiling, and g-prime is the gradient actually given to the optimizer.

##### Why the melody needs these exact notes

[Division](../MATHEMATICAL_MOVES.md#division) computes the fraction needed to bring the current norm down to c. [Minimum](../MATHEMATICAL_MOVES.md#minimum) chooses at most one, so small gradients are never enlarged. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) scales every coordinate equally, preserving direction; clipping coordinates separately would rotate the update.

Before the line is compressed, notice its recurring motions: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; **the narrow gate**—the smaller allowance prevents a promise from exceeding its boundary; and **the lock and key**—one influence matters through another, and either missing factor can close the path. They are the handholds by which the reader can later climb back from notation to meaning.

The brass reference machine already contains the complete gradient clipping mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
g^{\prime}=g\min\left(1,\frac{c}{\lVert g\rVert}\right)
$$

#### Where gradient clipping runs out

Clipping limits damage; it can hide a broken loss, corrupt data, or an unsuitable learning rate if used without diagnosis.

Here the new path ends honestly. Gradient Clipping can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the brass reference machine

Rebuild the gradient clipping scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/167-gradient-clipping/README.md).*

---

### Excavation 168 — Mixed Precision — Stop Storing Every Number with Unneeded Detail

> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Model systems and engine optimization

Stable gradients now expose the physical bill: weights, activations, and gradients are stored and moved as wide numbers even when many operations tolerate fewer bits.

At the Engine Cavern, the enginewright returns to the brass reference machine. Yesterday's instrument still lies open, so the first move asks for no new magic: convert every value and every update permanently to half precision.

For a moment the mark looks complete. Then the evidence refuses to fit: small updates disappear when rounded into large weights, and some intermediate values overflow or underflow the smaller numeric range. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The enginewright sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: convert every value and every update…
                         │
                         └── mismatch: small updates disappear when rounded…

reference evidence ──▶ measured repair: use reduced precision for bulk…
```

The enginewright lays two translucent sheets over the brass reference machine. The first is inscribed, “convert every value and every update permanently to half precision.” Its path ends where small updates disappear when rounded into large weights, and some intermediate values overflow or underflow the smaller numeric range. The second receives the same evidence but is allowed to use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision. Held to the light, the sheets separate at exactly one decision.

No one reaches for a mixed precision formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The enginewright changes only that one responsibility: use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision. When the ink dries, the name **Mixed Precision** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The brass reference machine keeps both histories. Its older mark still says, ‘convert every value and every update permanently to half precision’; beside it, the newer mark says, ‘use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision.’ The distance between those sentences is the exact shape of mixed precision: no larger than the failure required, and no smaller than reality permits.

#### Stop Storing Every Number with Unneeded Detail

A million activation values require roughly two megabytes at 16 bits instead of four at 32 bits, while a 32-bit master weight accumulates tiny updates safely.

#### The calculation hidden inside mixed precision

The enginewright carries the mixed precision scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Place one million model activation numbers in memory. At 32 bits each they occupy 32 million bits; at 16 bits each, 16 million bits. Hardware reports bytes, with eight bits in each byte, so divide either total by eight: four megabytes versus two. N counts the values, b is the chosen bits per value, and M is the resulting payload in bytes.

N is the number of stored scalar values, b is bits per value, and division by eight converts bits into bytes.

##### Why the melody needs these exact notes

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) is forced because every one of N values consumes b bits. [Division](../MATHEMATICAL_MOVES.md#division) converts units using eight bits per byte; adding eight would not perform a unit conversion. The equality describes payload memory and intentionally omits allocator overhead.

Listen beneath mixed precision: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Every mark needed for mixed precision is now visible on the brass reference machine. The symbols do not add an idea; they bind the discovered moves into one line:

$$
M=\frac{N b}{8}\ \text{bytes}
$$

#### Where mixed precision runs out

Mixed precision reduces representation cost, but numeric range—not only bit count—still threatens small gradients.

At the Engine Cavern, the enginewright leaves a blank beneath the new mark. Mixed Precision has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the brass reference machine

Rebuild the mixed precision scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/168-mixed-precision/README.md).*

---

### Excavation 169 — Loss Scaling — Rescue Gradients Too Small to Represent

> **Mathematical roots:** [Calculus & Differential Change](../MATHEMATICS_ATLAS.md#calculus) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

The forward pass looks correct, but some half-precision gradients round to zero before the optimizer can use them.

Morning reaches the Engine Cavern before anyone has a name for today's difficulty. Beside the brass reference machine, the enginewright tries the smallest continuation of what already works: increase the learning rate so small updates become visible.

The rule survives the easy cases. The next case leaves a crack through the middle of it: the learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update. More confidence cannot repair information that never entered the rule.

*The enginewright sketches the break before changing it:*

```text
observation
    │
    ▼
[increase the learning rate so small…]
    │
    ╳  the learning rate acts after…
    │
    ▼
[multiply the loss before…]
```

Two trails now cross the brass reference machine. The pale trail bears the instruction “increase the learning rate so small updates become visible.” It disappears into the observed failure: the learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update. The darker trail carries one additional capacity—to multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed loss scaling mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the brass reference machine is altered in exactly one way: multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating. Much later, people will call this territory **Loss Scaling**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the brass reference machine. The failed path remains visible beneath the repair, because loss scaling is easier to remember when its scar remains attached to it. The scar reads, ‘the learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update’; the new line exists only to keep that loss from happening again.

#### Rescue Gradients Too Small to Represent

A gradient 0.000001 becomes 0.001 when loss scale is 1000, survives backpropagation, and returns to 0.000001 after unscaling.

#### The calculation hidden inside loss scaling

The enginewright carries the loss scaling scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A true gradient of 0.000001 may vanish in half precision. Before differentiation, make the loss one thousand times larger; every loss-derived gradient becomes 0.001 and survives. Before updating the weight, divide by the same thousand and recover 0.000001. S names this temporary magnifier, L the original loss, and g the restored gradient—the model has not been told to learn a thousand times faster.

L is original loss, S is a temporary positive scale, and g is the recovered gradient in the loss's original units.

##### Why the melody needs these exact notes

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) by S enlarges every loss-derived gradient before narrow arithmetic can erase it. [Division](../MATHEMATICAL_MOVES.md#division) by the same S reverses that temporary unit change before the optimizer. Adding S would not proportionally enlarge tiny sensitivities and could not be undone uniformly.

The calculation borrows several gestures already encountered elsewhere: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. loss scaling feels new because the objects are new; the gestures remain recognizably human.

The enginewright reads the journey of loss scaling once more across the brass reference machine, then lets the words contract without losing their order:

$$
g=\frac{1}{S}\nabla_\theta(SL)
$$

#### Where loss scaling runs out

A scale large enough to prevent underflow can cause overflow, so practical systems adjust it dynamically.

The brass reference machine answers today's question and falls silent at the next. That silence is precise: Loss Scaling was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the brass reference machine

Rebuild the loss scaling scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/169-loss-scaling/README.md).*

---

### Excavation 170 — Gradient Accumulation — Build a Large Batch That Does Not Fit

> **Mathematical roots:** [Calculus & Differential Change](../MATHEMATICS_ATLAS.md#calculus) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

The optimizer needs a less noisy effective batch, but all its examples and activations cannot coexist on one device.

The brass reference machine at the Engine Cavern still carries the marks of the previous discovery. The enginewright follows them as far as they seem willing to go: reduce the batch until it fits and change nothing else.

Reality answers without terminology: the gradient becomes noisier and the training regime changes; increasing the learning rate cannot recreate evidence never averaged together. The brass reference machine now holds two situations the old rule cannot keep apart.

*The enginewright sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   reduce the batch until it fits and… the gradient becomes noisier and the…
            \        /
             \      /
              run several micro-batches, sum their…
```

The brass reference machine is divided down the middle. Left side: “reduce the batch until it fits and change nothing else.” Its final mark records the gradient becomes noisier and the training regime changes; increasing the learning rate cannot recreate evidence never averaged together. Right side: the same starting evidence, now allowed to run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given gradient accumulation a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step. The name **Gradient Accumulation** arrives afterward, like a title given to a path whose stones are already underfoot.

A thread now runs backward from gradient accumulation through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and the gradient becomes noisier and the training regime changes; increasing the learning rate cannot recreate evidence never averaged together. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction.

#### Build a Large Batch That Does Not Fit

Four micro-batches of eight examples create one effective batch of thirty-two while only eight examples' activations are resident at a time.

#### The calculation hidden inside gradient accumulation

The enginewright carries the gradient accumulation scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Imagine four small tables of eight examples arriving one after another. Each table gives its own average advice about the weights, but none is allowed to update yet. Add the four pieces of advice into one pending total, then share that total across the four witnesses. K counts those witnesses, g_k names one witness's advice, and g_effective is what the single optimizer step hears.

K is the number of micro-batches and g_k is the gradient average produced by micro-batch k of equal size.

##### Why the melody needs these exact notes

[Summation](../MATHEMATICAL_MOVES.md#summation) lets every micro-batch contribute to the same pending update. [Division](../MATHEMATICAL_MOVES.md#division) returns advice per micro-batch so increasing K does not enlarge the step by itself. Multiplication would let a zero coordinate in one micro-batch erase all others.

Three old motions cast new shadows here: **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Nothing remains unnamed in the gradient accumulation case on the brass reference machine. We can finally trade the long route for its compact map:

$$
g_{\text{effective}}=\frac1K\sum_{k=1}^{K}g_k
$$

#### Where gradient accumulation runs out

Accumulation lowers activation memory but adds serial work and does not reduce parameter or optimizer-state memory.

A final test reaches beyond the new instrument. It does not refute Gradient Accumulation; it reveals the edge of what was constructed. The enginewright carries that edge into the following room.

#### Return to the brass reference machine

Rebuild the gradient accumulation scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/170-gradient-accumulation/README.md).*

---

### Excavation 171 — Activation Checkpointing — Remember Less, Recompute Exactly

> **Mathematical roots:** [Calculus & Differential Change](../MATHEMATICS_ATLAS.md#calculus) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

Only one micro-batch is resident, yet backpropagation retains every layer's intermediate values until their gradients are computed.

Night gathers around the Engine Cavern. Under the light of the brass reference machine, the enginewright refuses to invent prematurely and begins with the plain rule: delete all activations after the forward pass.

Then the quiet test arrives: backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly. What looked like simplicity is revealed as a missing distinction.

*The enginewright sketches the break before changing it:*

```text
OLD PATH:  request ──▶ delete all activations after the… ──▶ backward computation then lacks the…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ keep selected checkpoint activations… ──▶ accountable result
```

The enginewright turns the brass reference machine toward the light. Through the old engraving, delete all activations after the forward pass, the evidence ends in the same contradiction: backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly. A second engraving adds only the power to keep selected checkpoint activations and recompute the missing segments once when backward reaches them. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The enginewright circles the place where the two activation checkpointing cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: keep selected checkpoint activations and recompute the missing segments once when backward reaches them. The enginewright writes **Activation Checkpointing** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The enginewright places a finger over the new distinction. At once the two cases collapse and backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly. Lifting the finger restores only this capacity: keep selected checkpoint activations and recompute the missing segments once when backward reaches them. That tiny reversible motion is the chapter's proof of necessity.

#### Remember Less, Recompute Exactly

In a nine-layer chain, retain boundaries around three-layer segments. Backward rebuilds one segment at a time instead of storing all nine layers.

#### The calculation hidden inside activation checkpointing

The enginewright carries the activation checkpointing scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

In a model chain of nine layers, keeping every activation costs nine stored boundaries. Keep only layers 0, 3, and 6; during backward work, rebuild the three missing operations inside the needed segment. For a much longer chain, choosing about the square root of L boundaries creates segments of about the same length, balancing stored checkpoints against recomputation. Big-O records this growth pattern, not an exact byte count.

L is the number of sequential layers and the expression records the memory-growth order under a balanced basic checkpoint scheme.

##### Why the melody needs these exact notes

[Square root](../MATHEMATICAL_MOVES.md#square-root) appears because balancing roughly sqrt(L) stored boundaries with sqrt(L)-sized recomputed segments minimizes the larger side of the trade. [Proportionality](../MATHEMATICAL_MOVES.md#proportionality) is implicit in big-O: exact bytes depend on activation shapes and implementation.

The symbols are about to change costume, but their work has appeared before: **the road home**—a squared construction returns to the scale of the world that created it. This is how distant excavations begin to sound like variations of one melody.

The story of activation checkpointing has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
M_{\text{activations}}=O(\sqrt{L})
$$

#### Where activation checkpointing runs out

Checkpointing buys memory with extra computation; a poor partition can save little or recompute too much.

One unsolved mark remains on the brass reference machine. None of the responsibilities inside Activation Checkpointing can move it, and so it becomes the observation from which the next excavation must begin.

#### Return to the brass reference machine

Rebuild the activation checkpointing scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/171-activation-checkpointing/README.md).*

---

### Excavation 172 — ZeRO — Stop Replicating the Same Training State

> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../MATHEMATICS_ATLAS.md#dynamics) · [Optimization](../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Model systems and engine optimization

Recomputation makes the forward graph fit, but AdamW stores parameters, gradients, first moments, and second moments. Ordinary data parallelism copies all of them onto every device.

Inside the Engine Cavern, every old tool is given one honest chance. The enginewright sets the brass reference machine between the evidence and the desired answer, then tries to add devices and replicate the full training state on each one.

The enginewright repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: compute capacity grows while per-device model-state memory remains almost unchanged, so the same memory wall returns. The failure is stable enough to become evidence.

*The enginewright sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ add devices and replicate the full… ──▶ blurred: compute capacity grows while…
      │
      └── new lens ──▶ partition optimizer states,… ──▶ distinction survives
```

Across the brass reference machine, the old path and the repaired path run side by side. One carries “add devices and replicate the full training state on each one”; the other knows how to partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them. When the failure—compute capacity grows while per-device model-state memory remains almost unchanged, so the same memory wall returns—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to zero. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them. This problem and its repair will travel under the name **ZeRO**, but the name carries no knowledge the scene has not earned.

What changed on the brass reference machine can be said without symbols. Before, the method could only add devices and replicate the full training state on each one; now it can also partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

#### Stop Replicating the Same Training State

Four workers each keep roughly one quarter of a large moment vector rather than four complete copies, then cooperate for the update.

#### The calculation hidden inside zero

The enginewright carries the zero scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Adam's moment state has twelve equal chunks and four devices are cooperating. Replication gives every device all twelve; sharding gives each device three. Asking for state per device therefore means sharing the total across P owners: total divided by P. The approximation sign remains because temporary gathers and uneven tensor sizes prevent the physical memory from being exactly that ideal share.

M_total is shardable model state and P is the number of cooperating devices under an ideal balanced partition.

##### Why the melody needs these exact notes

[Division](../MATHEMATICAL_MOVES.md#division) expresses an equal share per device. Multiplication describes the failed replicated system's total cluster memory, not the amount one device must hold. [Approximation](../MATHEMATICAL_MOVES.md#approximation) admits temporary gathers, buffers, and uneven tensors.

Inside zero, familiar operations return with stricter duties: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Cover the prose about zero and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
M_{\text{state per device}}\approx\frac{M_{\text{total state}}}{P}
$$

#### Where zero runs out

Because a worker no longer owns a complete state by itself, sharding trades redundant memory for communication and makes recovery and state ownership more complex.

The zero repair holds, but the world asks for something it was never given. At the Engine Cavern, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the brass reference machine

Rebuild the zero scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/172-zero-sharding/README.md).*

---

### Excavation 173 — Tensor Parallelism — Split One Matrix That No Device Can Hold

> **Mathematical roots:** [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra) · [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

Sharded parameters can be gathered for computation, but the largest matrix itself becomes too large to materialize or multiply on one worker.

A new case arrives at the Engine Cavern, but the enginewright first reaches for the familiar brass reference machine. Its promise is simple: assign whole layers to different devices and pass every activation through them sequentially.

At the edge of the brass reference machine, the shortcut produces its consequence: one oversized layer still cannot fit, and devices responsible for later layers wait while earlier ones work. That consequence, not a textbook, earns the next move.

*The enginewright sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: assign whole layers to different…
possible road B ─┘              └── loses: one oversized layer still cannot fit,…

same roads ──▶ repaired map ──▶ split a matrix across its columns or…
```

The enginewright covers the new mark and the old contradiction returns: one oversized layer still cannot fit, and devices responsible for later layers wait while earlier ones work. The cover is lifted, restoring the ability to split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason tensor parallelism exists.

What must change for tensor parallelism is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output. That threshold is where **Tensor Parallelism** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In tensor parallelism, that memory takes a precise form: whenever one oversized layer still cannot fit, and devices responsible for later layers wait while earlier ones work, preserve enough structure to split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output.

#### Split One Matrix That No Device Can Hold

Divide one vocabulary projection into four column blocks. Each device scores one quarter of the vocabulary from the same hidden state; concatenation restores the full logits.

#### The calculation hidden inside tensor parallelism

The enginewright carries the tensor parallelism scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Split the vocabulary-scoring matrix into four column blocks. Every device receives the same hidden state X but multiplies it by only its own block W_p, producing scores Y_p for its quarter of the vocabulary. Those scores must remain distinct, so place the four blocks beside one another in vocabulary order. Adding them would collapse different tokens into the same slots. Y names the restored full score row after concatenation.

W is partitioned into P column blocks; every worker receives X and produces the corresponding block of output columns.

##### Why the melody needs these exact notes

[Concatenation](../MATHEMATICAL_MOVES.md#concatenation) preserves distinct output columns side by side; addition would collapse vocabulary scores that must remain separate. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) applies the same input X to each learned block, and equality states that partitioned execution matches the unsplit matrix operation.

Trace each operation by touch rather than by name: **the binding loom**—distinct pieces remain side by side instead of being blended away; and **the lock and key**—one influence matters through another, and either missing factor can close the path. Together they form the smallest mechanism that survives the counterexample.

The brass reference machine already contains the complete tensor parallelism mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
Y_p=XW_p,\quad Y=[Y_1,Y_2,\ldots,Y_P]
$$

#### Where tensor parallelism runs out

Tensor parallelism introduces communication inside every layer, so a slow interconnect can erase its benefit.

Here the new path ends honestly. Tensor Parallelism can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the brass reference machine

Rebuild the tensor parallelism scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/173-tensor-parallelism/README.md).*

---

### Excavation 174 — Speculative Decoding — Let a Small Model Propose, Never Decide

> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Model systems and engine optimization

Tensor parallelism makes one target-model step possible, but autoregressive dependence still serializes token generation.

The doors of the Engine Cavern close against the wind. On the brass reference machine, the enginewright writes the cheapest rule that might still be true: let a cheap draft model emit several tokens and return them directly.

For a moment the mark looks complete. Then the evidence refuses to fit: speed improves by silently replacing the trusted target distribution with a weaker model's distribution. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The enginewright sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: let a cheap draft model emit several…
                         │
                         └── mismatch: speed improves by silently replacing…

reference evidence ──▶ measured repair: let the draft propose a short…
```

The enginewright lays two translucent sheets over the brass reference machine. The first is inscribed, “let a cheap draft model emit several tokens and return them directly.” Its path ends where speed improves by silently replacing the trusted target distribution with a weaker model's distribution. The second receives the same evidence but is allowed to let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling. Held to the light, the sheets separate at exactly one decision.

No one reaches for a speculative decoding formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The enginewright changes only that one responsibility: let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling. When the ink dries, the name **Speculative Decoding** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because speed improves by silently replacing the trusted target distribution with a weaker model's distribution, while the other can let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling. That fork—not the vocabulary—is where speculative decoding lives.

#### Let a Small Model Propose, Never Decide

The draft proposes “the tiger sleeps.” One target call verifies all three positions; an unsupported token is rejected and sampling resumes from the corrected target distribution.

#### The calculation hidden inside speculative decoding

The enginewright carries the speculative decoding scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

If the draft assigns tiger probability 0.8 but the target assigns 0.4, only half of those proposals have target support: 0.4/0.8=0.5. If the draft assigns 0.4 and the target 0.8, the ratio is 2, but acceptance cannot be 200 percent, so it stops at 1. The function a(x) names this capped acceptance chance for proposed token x.

q(x) is draft probability, p(x) is target probability, and a(x) is the probability of accepting the draft token under the correction step.

##### Why the melody needs these exact notes

[Division](../MATHEMATICAL_MOVES.md#division) compares target support per unit of draft support. [Minimum](../MATHEMATICAL_MOVES.md#minimum) caps acceptance at one because probabilities cannot exceed certainty. Simply taking max or always accepting would change the target distribution; the ratio corrects proposals that the draft overproduces.

The mandala has curved back upon itself. In this chamber we meet **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; and **the narrow gate**—the smaller allowance prevents a promise from exceeding its boundary. What seemed like a new formula is older mathematical instinct arranged around a new need.

Every mark needed for speculative decoding is now visible on the brass reference machine. The symbols do not add an idea; they bind the discovered moves into one line:

$$
a(x)=\min\left(1,\frac{p(x)}{q(x)}\right)
$$

#### Where speculative decoding runs out

Speed depends on draft agreement and hardware utilization; poor proposals add work instead of removing it.

At the Engine Cavern, the enginewright leaves a blank beneath the new mark. Speculative Decoding has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the brass reference machine

Rebuild the speculative decoding scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/174-speculative-decoding/README.md).*

---

### Excavation 175 — A Modern Tiny Language Model — Assemble the Measured Engine

> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Model systems and engine optimization

Speculative decoding accelerates the final serial loop. We now have many locally useful repairs, but a pile of optimizations is not yet one reproducible model.

Nothing in the Engine Cavern yet bears today's mathematical name. There is only the enginewright, the brass reference machine, and one plausible action: enable every technique at once and celebrate if the program runs.

The rule survives the easy cases. The next case leaves a crack through the middle of it: when quality or speed changes, no one knows which mechanism caused it; masks, precision, sharding, and caches can disagree at their boundaries. More confidence cannot repair information that never entered the rule.

*The enginewright sketches the break before changing it:*

```text
observation
    │
    ▼
[enable every technique at once and…]
    │
    ╳  when quality or speed changes, no one…
    │
    ▼
[assemble the engine in dependency…]
```

Two trails now cross the brass reference machine. The pale trail bears the instruction “enable every technique at once and celebrate if the program runs.” It disappears into the observed failure: when quality or speed changes, no one knows which mechanism caused it; masks, precision, sharding, and caches can disagree at their boundaries. The darker trail carries one additional capacity—to assemble the engine in dependency order, preserve a reference path, and test numerical or distributional equivalence at every boundary before accepting measured gains. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed modern tiny language model mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the brass reference machine is altered in exactly one way: assemble the engine in dependency order, preserve a reference path, and test numerical or distributional equivalence at every boundary before accepting measured gains. Much later, people will call this territory **A Modern Tiny Language Model**. Here the name is only a memory of the failure it can survive.

The brass reference machine has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and modern tiny language model looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

#### Assemble the Measured Engine

Train one tiny model with packed examples, RoPE, GQA, exact tiled attention, pre-RMSNorm, SwiGLU, tied embeddings, AdamW, clipping, mixed precision, accumulation, and checkpointing; then serve it with a KV cache and verified draft proposals.

#### Where a modern tiny language model runs out

The engine is modern, not final. New hardware, data, and observations will create new bottlenecks, and every proposed repair must re-enter the bounded loop from Excavation 150.

The brass reference machine answers today's question and falls silent at the next. That silence is precise: Modern Tiny Language Model was built to repair one failure, not to pretend every later boundary is already solved.

#### The old mind inside the new engine

The engine has changed its position system, cache, attention kernel, normalization, gate, optimizer, precision, memory plan, and distribution across machines. Yet the reference path remains beside it like a tuning fork: every faster mechanism must still produce the mathematical responsibility first derived in the valley.

```text
reference ──preserved meaning──▶ optimized engine
```

The trail called *the old mind inside the new engine* is what remains when one necessity becomes another.

#### Return to the brass reference machine

Rebuild the modern tiny language model scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/175-modern-tiny-llm/README.md).*
