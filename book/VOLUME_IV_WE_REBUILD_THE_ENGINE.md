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

The bounded loop can approve a candidate, but approval is meaningless if nobody can reconstruct the system it is supposed to improve.

Inside the Engine Cavern, the old method is given an honest chance. The enginewright places the evidence on the brass reference machine and tries to keep the final score and the model file; those should be enough to compare the next idea.

Nothing about this first move is careless. To keep the final score and the model file; those should be enough to compare the next idea is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: a rerun changes the data order, random seed, tokenizer revision, and library behavior. Its score moves even though the proposed improvement was never applied.

The important discovery is not merely that trying to keep the final score and the model file; those should be enough to compare the next idea failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the brass reference machine, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **A Reproducible Baseline**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

#### Improve Something That Actually Exists

Run the same tiny tiger-language model twice from the recorded seed. Only after its loss curve and held-out score agree do we permit one component to change.

#### The calculation hidden inside a reproducible baseline

The enginewright carries the reproducible baseline scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The frozen run scores 2.4 and the candidate scores 2.1 on the same loss test. Looking at 2.1 alone cannot tell you whether anything improved. Remove the old 2.4 from the new 2.1: the remaining −0.3 is the candidate's change. We call the old measurement m_baseline, the new one m_candidate, and the remainder delta m only after doing that comparison.

m_baseline is the frozen model's measurement; m_candidate is measured by the same procedure; delta m names only the change between them.

##### Why the melody needs these exact notes

[Subtraction](../MATHEMATICAL_MOVES.md#subtraction) removes the common baseline and isolates the candidate's change. Addition would make two large scores look impressive even when they are identical. The order fixes the sign: positive means the candidate raised this metric.

The calculation reuses familiar motions: **the chisel**—what is shared is removed so the remaining change can be seen. Together they keep the path from the concrete case to notation intact.

The enginewright reads the journey of reproducible baseline once more across the brass reference machine, then lets the words contract without losing their order:

$$
\Delta m=m_{\text{candidate}}-m_{\text{baseline}}
$$

#### Where a reproducible baseline runs out

Reproducibility makes differences attributable; it does not tell us which component is worth changing.

The brass reference machine answers today's question and falls silent at the next. That silence is precise: Reproducible Baseline was built to repair one failure, not to pretend every later boundary is already solved.

---

### Excavation 152 — Profiling — Measure Where the Time Went

A reproducible baseline gives us a trustworthy before-state. Its first run is too slow for the ranger station, but a total runtime does not identify the guilty stage.

At the Engine Cavern, the enginewright meets the next case beside the brass reference machine. The nearest idea is also the most reasonable one: optimize the largest-looking matrix because attention is famous for being expensive.

The attraction of this attempt is easy to see. To optimize the largest-looking matrix because attention is famous for being expensive reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: the device spends much of the run waiting for data and moving tensors. Making one matrix faster barely changes the wall clock.

The contradiction matters because it identifies a structural loss in the instruction to optimize the largest-looking matrix because attention is famous for being expensive, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The brass reference machine will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must measure data loading, computation, communication, and idle time separately before choosing a repair. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Profiling**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

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

---

### Excavation 153 — The Input Pipeline — Stop Making the Accelerator Wait

Profiling reveals that the accelerator repeatedly waits for the next token batch. The model is ready, but its evidence is still being read and prepared.

The previous discovery reaches the Engine Cavern carrying one unfinished problem. Beside the brass reference machine, the enginewright first tries to load a batch, wait until loading finishes, compute it, and only then begin loading the next one.

There is good reason to begin this way. If we load a batch, wait until loading finishes, compute it, and only then begin loading the next one, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: data time and compute time are paid sequentially on every step, leaving expensive compute hardware idle.

This failure cannot be repaired by performing the instruction to load a batch, wait until loading finishes, compute it, and only then begin loading the next one more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the brass reference machine; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **The Input Pipeline**. The name is simply a handle for the distinction already reconstructed.

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

---

### Excavation 154 — Sequence Packing — Stop Training on Empty Space

The input pipeline now keeps the device busy. Inspection shows that many of the tokens occupying each fixed rectangle are padding rather than language.

A new case arrives at the Engine Cavern. Nothing yet demands a new invention, so the enginewright uses the brass reference machine to pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste.

This is precisely the kind of shortcut a careful builder should try first. The instruction to pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: the loss ignores padding, but attention and matrix multiplication still spend time and memory carrying those empty positions.

The counterexample separates two questions that the attempt to pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the brass reference machine fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now pack several short examples into each fixed-length row and mask their boundaries so examples cannot read one another. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Sequence Packing**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

#### Stop Training on Empty Space

Lengths 6, 5, 3, and 2 fill two rows of length 8 exactly. Padding falls from 16 allocated positions with 6 empty to 16 positions with none empty.

#### The calculation hidden inside sequence packing

The enginewright carries the sequence packing scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Draw two rows with eight boxes each: sixteen paid positions. Place sequences of lengths 6 and 2 in the first row, then 5 and 3 in the second. All sixteen boxes now contain real tokens. To ask what share of the paid space teaches the model, put useful boxes over paid boxes: 16/16. Eta_pack is only a short name for that useful fraction.

The numerator counts language tokens that create lessons; the denominator counts every position for which hardware reserves work.

##### Why the melody needs these exact notes

[Division](../MATHEMATICAL_MOVES.md#division) forms the useful share per allocated position, making batches of different sizes comparable. A raw token count would reward larger batches even if their wasted fraction were worse. The ratio stays between zero and one because real tokens cannot exceed allocated positions.

Three old motions cast new shadows here: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Every mark in the coming sequence packing equation now belongs to a visible part of the case. The compressed form is:

$$
\eta_{\text{pack}}=\frac{N_{\text{real tokens}}}{N_{\text{allocated positions}}}
$$

#### Where sequence packing runs out

Packing improves utilization only if masks and position resets prevent cross-example contamination.

The sequence packing repair holds, but the world asks for something it was never given. At the Engine Cavern, that unmet need is preserved rather than hidden behind a stronger claim.

---

### Excavation 155 — Rotary Position Embeddings — Let Distance Enter the Match

Packed training supplies dense sequences, but the learned absolute position cards from our first GPT bind each slot to a private identity rather than making relative displacement part of the query-key match.

Inside the Engine Cavern, the old method is given an honest chance. The enginewright places the evidence on the brass reference machine and tries to learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples.

Nothing about this first move is careless. To learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: moving the same phrase from positions 10–12 to 110–112 changes every position vector although the internal distances are unchanged.

The important discovery is not merely that trying to learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the brass reference machine, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Rotary Position Embeddings**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

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

---

### Excavation 156 — Relative Position Bias — What Should Happen Beyond the Seen Window?

Rotary position makes displacement visible inside the attention match. When the station tests much longer sequences, the model must rank relationships at separations absent from training.

At the Engine Cavern, the enginewright meets the next case beside the brass reference machine. The nearest idea is also the most reasonable one: trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there.

The attraction of this attempt is easy to see. To trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: a mathematically defined position is not necessarily a learned behavior; attention can become erratic at unfamiliar separations.

The contradiction matters because it identifies a structural loss in the instruction to trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The brass reference machine will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Relative Position Bias**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

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

---

### Excavation 157 — The KV Cache — Stop Re-reading the Entire Past

Relative position now behaves predictably, but autoregressive generation still reruns the Transformer over the full prefix after appending each token.

The previous discovery reaches the Engine Cavern carrying one unfinished problem. Beside the brass reference machine, the enginewright first tries to at step t, recompute keys and values for positions 1 through t because the prefix is presented again.

There is good reason to begin this way. If we at step t, recompute keys and values for positions 1 through t because the prefix is presented again, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: past token representations are unchanged in causal decoding, so the same projections are calculated repeatedly while one new token is added.

This failure cannot be repaired by performing the instruction to at step t, recompute keys and values for positions 1 through t because the prefix is presented again more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the brass reference machine; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **The KV Cache**. The name is simply a handle for the distinction already reconstructed.

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

---

### Excavation 158 — Multi-Query Attention — Why Cache Separate Copies for Every Head?

Caching turns repeated arithmetic into memory reads. Profiling now shows decoding limited by loading separate key and value histories for every attention head.

A new case arrives at the Engine Cavern. Nothing yet demands a new invention, so the enginewright uses the brass reference machine to preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections.

This is precisely the kind of shortcut a careful builder should try first. The instruction to preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: the caches grow with both sequence length and head count, and loading them dominates the arithmetic for one new token.

The counterexample separates two questions that the attempt to preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the brass reference machine fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now keep many query heads but share one key head and one value head across them. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Multi-Query Attention**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

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

---

### Excavation 159 — Grouped-Query Attention — Recover Some Specialist Memory

One shared KV head makes decoding light enough for the station, but evaluation finds a quality loss on relationships that benefited from distinct catalogs.

Inside the Engine Cavern, the old method is given an honest chance. The enginewright places the evidence on the brass reference machine and tries to return immediately to one KV head per query head.

Nothing about this first move is careless. To return immediately to one KV head per query head is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: quality recovers, but so does the full cache and bandwidth cost that forced sharing.

The important discovery is not merely that trying to return immediately to one KV head per query head failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the brass reference machine, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to partition query heads into groups; queries remain distinct while each group shares one key-value head. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Grouped-Query Attention**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

#### Recover Some Specialist Memory

Eight query heads arranged into two KV groups preserve two catalogs. The cache is twice MQA's size but one quarter of ordinary eight-head KV storage.

#### The calculation hidden inside grouped-query attention

The enginewright carries the grouped-query attention scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Line up the model's eight query heads and two KV catalogs. Four consecutive query heads must point to catalog 0 and the next four to catalog 1. Scaling head number h from the eight-head range into the two-catalog range gives h×2/8; rounding down turns positions 0 through 3 into address 0 and positions 4 through 7 into address 1. The name g(h) records that address-making rule.

h is a query-head index, H_Q counts query heads, H_KV counts shared KV groups, and g(h) selects the group serving head h.

##### Why the melody needs these exact notes

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) spreads the KV group range across query-head indices; [division](../MATHEMATICAL_MOVES.md#division) converts one query index into its proportional group location. The floor deliberately [rounds](../MATHEMATICAL_MOVES.md#rounding) down so every head receives one valid discrete group rather than a fractional address.

The calculation reuses familiar motions: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. Together they keep the path from the concrete case to notation intact.

The story of grouped-query attention has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
g(h)=\left\lfloor\frac{hH_{\text{KV}}}{H_Q}\right\rfloor
$$

#### Where grouped-query attention runs out

Because sharing deliberately removes independent KV views, the number and assignment of groups remain empirical design choices whose quality must be measured.

One unsolved mark remains on the brass reference machine. None of the responsibilities inside Grouped-Query Attention can move it, and so it becomes the observation from which the next excavation must begin.

---

### Excavation 160 — FlashAttention — The Arithmetic Was Not the Bottleneck

Grouped-query attention makes generation economical, yet training long packed sequences still materializes a large attention-score matrix in slow device memory.

At the Engine Cavern, the enginewright meets the next case beside the brass reference machine. The nearest idea is also the most reasonable one: reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost.

The attraction of this attempt is easy to see. To reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: approximation changes the model, while profiling shows much of the time is spent writing and rereading exact intermediate scores rather than multiplying them.

The contradiction matters because it identifies a structural loss in the instruction to reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The brass reference machine will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **FlashAttention**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

#### The Arithmetic Was Not the Bottleneck

Process two score tiles. Carry only the running maximum, normalized denominator, and weighted value total into the next tile; the final answer matches ordinary softmax attention.

#### The calculation hidden inside flashattention

The enginewright carries the flashattention scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The model's first attention tile contains scores 1 and 4, so 4 becomes the remembered safety ceiling. The next tile contains 3 and 2; neither exceeds 4, so the ceiling remains 4. If a later tile contained 7, the ceiling would become 7 and the earlier exponential totals would be rescaled. Thus m is the largest score already processed, the s_j values are the arriving tile, and m-prime is the one maximum covering both histories.

m is the largest score already seen, s_j are scores in the new tile, and m-prime is the safe maximum for the combined tiles.

##### Why the melody needs these exact notes

[Maximum](../MATHEMATICAL_MOVES.md#maximum) preserves the one value needed to stabilize exponentials across both old and new tiles. Addition would invent a score that never occurred; averaging could be lower than the true maximum and allow overflow. The prime marks the updated running version; see [symbol decorations](../MATHEMATICAL_MOVES.md#symbol-decorations).

Listen beneath flashattention: **the highest lantern**—the strongest surviving possibility sets the visible ceiling. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Every mark in the coming flashattention equation now belongs to a visible part of the case. The compressed form is:

$$
m^{\prime}=\max(m,\max_j s_j)
$$

#### Where flashattention runs out

FlashAttention removes avoidable memory traffic, not quadratic pairwise arithmetic itself.

The flashattention repair holds, but the world asks for something it was never given. At the Engine Cavern, that unmet need is preserved rather than hidden behind a stronger claim.

---

### Excavation 161 — RMSNorm — Do We Need to Subtract the Centre?

FlashAttention removes one systems bottleneck, making smaller repeated operations visible. Layer normalization calculates both a mean and a spread at every token and layer.

The previous discovery reaches the Engine Cavern carrying one unfinished problem. Beside the brass reference machine, the enginewright first tries to delete normalization because each individual operation appears cheap.

There is good reason to begin this way. If we delete normalization because each individual operation appears cheap, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: deep residual streams drift in scale and training destabilizes; the repeated control was doing essential work.

This failure cannot be repaired by performing the instruction to delete normalization because each individual operation appears cheap more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the brass reference machine; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to keep rescaling invariance by dividing by root-mean-square magnitude, while testing whether explicit recentering is dispensable. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **RMSNorm**. The name is simply a handle for the distinction already reconstructed.

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

---

### Excavation 162 — Pre-Normalization — Protect the Residual Highway

The block is cheaper, but making it deeper reveals unstable early gradients when normalization follows each residual addition.

A new case arrives at the Engine Cavern. Nothing yet demands a new invention, so the enginewright uses the brass reference machine to keep post-normalization because each block's output then looks standardized before the next block.

This is precisely the kind of shortcut a careful builder should try first. The instruction to keep post-normalization because each block's output then looks standardized before the next block preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: the supposedly clean output places normalization directly on the identity route every gradient must cross, making the long residual path harder to preserve.

The counterexample separates two questions that the attempt to keep post-normalization because each block's output then looks standardized before the next block had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the brass reference machine fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now normalize only the input to the changing branch and let the identity stream pass around it unchanged. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Pre-Normalization**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

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

---

### Excavation 163 — SwiGLU — Let One Learned Path Gate Another

Pre-normalization lets gradients reach deep blocks, but the ordinary feed-forward network applies one fixed activation independently to one projection.

Inside the Engine Cavern, the old method is given an honest chance. The enginewright places the evidence on the brass reference machine and tries to make the hidden layer merely wider and trust more coordinates to express every conditional interaction.

Nothing about this first move is careless. To make the hidden layer merely wider and trust more coordinates to express every conditional interaction is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: width adds capacity but still asks one projection both to create content and decide when that content matters.

The important discovery is not merely that trying to make the hidden layer merely wider and trust more coordinates to express every conditional interaction failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the brass reference machine, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to create one content projection and one gate projection; use the smooth gate to scale content feature by feature. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **SwiGLU**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

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

---

### Excavation 164 — Weight Tying — Use One Word Geometry Twice

SwiGLU improves the block, but the model stores one large table for input embeddings and another large matrix for scoring the same vocabulary at output.

At the Engine Cavern, the enginewright meets the next case beside the brass reference machine. The nearest idea is also the most reasonable one: let both matrices learn independently because reading a token and predicting it are different jobs.

The attraction of this attempt is easy to see. To let both matrices learn independently because reading a token and predicting it are different jobs reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: the model spends parameters learning two unrelated geometries for the same set of word identities, and rare tokens receive weak evidence in both places.

The contradiction matters because it identifies a structural loss in the instruction to let both matrices learn independently because reading a token and predicting it are different jobs, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The brass reference machine will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Weight Tying**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

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

---

### Excavation 165 — Adam — Give Each Parameter Its Own Step Scale

Weight tying concentrates more roles in shared parameters. During training, some coordinates receive frequent large gradients while rare-token coordinates receive sparse small ones.

The previous discovery reaches the Engine Cavern carrying one unfinished problem. Beside the brass reference machine, the enginewright first tries to use the same raw gradient step scale for every parameter.

There is good reason to begin this way. If we use the same raw gradient step scale for every parameter, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: a rate safe for frequent large gradients barely moves sparse coordinates; a rate large enough for sparse coordinates makes noisy ones unstable.

This failure cannot be repaired by performing the instruction to use the same raw gradient step scale for every parameter more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the brass reference machine; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Adam**. The name is simply a handle for the distinction already reconstructed.

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

---

### Excavation 166 — AdamW — Keep Shrinkage Separate from Adaptation

Adam trains the block, but adding an L2 penalty to the loss sends shrinkage through the optimizer's coordinate-wise rescaling.

A new case arrives at the Engine Cavern. Nothing yet demands a new invention, so the enginewright uses the brass reference machine to treat penalty gradients and data gradients identically because both appear in one total loss.

This is precisely the kind of shortcut a careful builder should try first. The instruction to treat penalty gradients and data gradients identically because both appear in one total loss preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: coordinates with different gradient histories receive different effective shrinkage even when the intended rule was to decay all selected weights at one rate.

The counterexample separates two questions that the attempt to treat penalty gradients and data gradients identically because both appear in one total loss had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the brass reference machine fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now apply Adam's adaptive data update and parameter decay as separate operations. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **AdamW**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

#### Keep Shrinkage Separate from Adaptation

Two equal weights with different gradient histories receive different Adam steps but the same proportional decay.

#### The calculation hidden inside adamw

The enginewright carries the adamw scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Suppose two weights both equal 2, although their gradient histories differ. If decay means 'remove one tenth of one percent of the present weight this step,' both should lose the same proportion before their evidence-driven Adam movements differ. Multiplying theta by 1−eta lambda performs that direct shrink. The separate subtraction then applies Adam's learned direction, preventing gradient history from secretly changing the intended decay rule.

lambda is decay strength; the first term shrinks the old parameter directly; the second is Adam's data-driven update.

##### Why the melody needs these exact notes

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) by 1−eta lambda makes decay proportional to current parameter size: a zero weight stays zero and doubling a weight doubles shrinkage. [Subtraction](../MATHEMATICAL_MOVES.md#subtraction) then applies the independently adapted loss step. Hiding decay inside m and v would mix two jobs the formula deliberately separates.

The mandala has curved back upon itself. In this chamber we meet **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the chisel**—what is shared is removed so the remaining change can be seen. What seemed like a new formula is older mathematical instinct arranged around a new need.

Every mark in the coming adamw equation now belongs to a visible part of the case. The compressed form is:

$$
\theta_{t+1}=(1-\eta\lambda)\theta_t-\eta\frac{\widehat m_t}{\sqrt{\widehat v_t}+\epsilon}
$$

#### Where adamw runs out

Decoupled decay still requires choosing which parameters to decay and how strongly.

The adamw repair holds, but the world asks for something it was never given. At the Engine Cavern, that unmet need is preserved rather than hidden behind a stronger claim.

---

### Excavation 167 — Gradient Clipping — Stop One Shock from Becoming a Catastrophe

Most steps are stable, but a rare batch produces an enormous global gradient norm and overwhelms Adam's still-developing moment estimates.

Inside the Engine Cavern, the old method is given an honest chance. The enginewright places the evidence on the brass reference machine and tries to discard the entire batch whenever any gradient coordinate looks large.

Nothing about this first move is careless. To discard the entire batch whenever any gradient coordinate looks large is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: useful directional evidence is lost, and one arbitrary coordinate threshold ignores the size of the full update vector.

The important discovery is not merely that trying to discard the entire batch whenever any gradient coordinate looks large failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the brass reference machine, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to preserve the gradient's direction but scale its whole norm down only when it exceeds a chosen ceiling. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Gradient Clipping**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

#### Stop One Shock from Becoming a Catastrophe

A gradient of length 20 with ceiling 5 is multiplied by one quarter. A gradient of length 3 passes unchanged.

#### The calculation hidden inside gradient clipping

The enginewright carries the gradient clipping scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The model's current gradient points in a useful direction but has length 20, while this run permits length 5. The required scale is 5/20, or one quarter, so every component shrinks by one quarter and direction survives. If the next gradient has length 3, the fraction 5/3 would enlarge it—exactly what we do not want—so we cap the multiplier at 1. We call the ceiling c, the original advice g, and the safe advice g-prime.

g is the original gradient vector, c is the allowed norm ceiling, and g-prime is the gradient actually given to the optimizer.

##### Why the melody needs these exact notes

[Division](../MATHEMATICAL_MOVES.md#division) computes the fraction needed to bring the current norm down to c. [Minimum](../MATHEMATICAL_MOVES.md#minimum) chooses at most one, so small gradients are never enlarged. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) scales every coordinate equally, preserving direction; clipping coordinates separately would rotate the update.

The calculation reuses familiar motions: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; **the narrow gate**—the smaller allowance prevents a promise from exceeding its boundary; and **the lock and key**—one influence matters through another, and either missing factor can close the path. Together they keep the path from the concrete case to notation intact.

The brass reference machine already contains the complete gradient clipping mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
g^{\prime}=g\min\left(1,\frac{c}{\lVert g\rVert}\right)
$$

#### Where gradient clipping runs out

Clipping limits damage; it can hide a broken loss, corrupt data, or an unsuitable learning rate if used without diagnosis.

Here the new path ends honestly. Gradient Clipping can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

---

### Excavation 168 — Mixed Precision — Stop Storing Every Number with Unneeded Detail

Stable gradients now expose the physical bill: weights, activations, and gradients are stored and moved as wide numbers even when many operations tolerate fewer bits.

At the Engine Cavern, the enginewright meets the next case beside the brass reference machine. The nearest idea is also the most reasonable one: convert every value and every update permanently to half precision.

The attraction of this attempt is easy to see. To convert every value and every update permanently to half precision reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: small updates disappear when rounded into large weights, and some intermediate values overflow or underflow the smaller numeric range.

The contradiction matters because it identifies a structural loss in the instruction to convert every value and every update permanently to half precision, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The brass reference machine will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Mixed Precision**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

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

---

### Excavation 169 — Loss Scaling — Rescue Gradients Too Small to Represent

The forward pass looks correct, but some half-precision gradients round to zero before the optimizer can use them.

The previous discovery reaches the Engine Cavern carrying one unfinished problem. Beside the brass reference machine, the enginewright first tries to increase the learning rate so small updates become visible.

There is good reason to begin this way. If we increase the learning rate so small updates become visible, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: the learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update.

This failure cannot be repaired by performing the instruction to increase the learning rate so small updates become visible more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the brass reference machine; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Loss Scaling**. The name is simply a handle for the distinction already reconstructed.

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

---

### Excavation 170 — Gradient Accumulation — Build a Large Batch That Does Not Fit

The optimizer needs a less noisy effective batch, but all its examples and activations cannot coexist on one device.

A new case arrives at the Engine Cavern. Nothing yet demands a new invention, so the enginewright uses the brass reference machine to reduce the batch until it fits and change nothing else.

This is precisely the kind of shortcut a careful builder should try first. The instruction to reduce the batch until it fits and change nothing else preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: the gradient becomes noisier and the training regime changes; increasing the learning rate cannot recreate evidence never averaged together.

The counterexample separates two questions that the attempt to reduce the batch until it fits and change nothing else had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the brass reference machine fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Gradient Accumulation**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

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

---

### Excavation 171 — Activation Checkpointing — Remember Less, Recompute Exactly

Only one micro-batch is resident, yet backpropagation retains every layer's intermediate values until their gradients are computed.

Inside the Engine Cavern, the old method is given an honest chance. The enginewright places the evidence on the brass reference machine and tries to delete all activations after the forward pass.

Nothing about this first move is careless. To delete all activations after the forward pass is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly.

The important discovery is not merely that trying to delete all activations after the forward pass failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the brass reference machine, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to keep selected checkpoint activations and recompute the missing segments once when backward reaches them. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Activation Checkpointing**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

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

---

### Excavation 172 — ZeRO — Stop Replicating the Same Training State

Recomputation makes the forward graph fit, but AdamW stores parameters, gradients, first moments, and second moments. Ordinary data parallelism copies all of them onto every device.

At the Engine Cavern, the enginewright meets the next case beside the brass reference machine. The nearest idea is also the most reasonable one: add devices and replicate the full training state on each one.

The attraction of this attempt is easy to see. To add devices and replicate the full training state on each one reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: compute capacity grows while per-device model-state memory remains almost unchanged, so the same memory wall returns.

The contradiction matters because it identifies a structural loss in the instruction to add devices and replicate the full training state on each one, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The brass reference machine will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **ZeRO**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

#### Stop Replicating the Same Training State

Four workers each keep roughly one quarter of a large moment vector rather than four complete copies, then cooperate for the update.

#### The calculation hidden inside zero

The enginewright carries the zero scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Adam's moment state has twelve equal chunks and four devices are cooperating. Replication gives every device all twelve; sharding gives each device three. Asking for state per device therefore means sharing the total across P owners: total divided by P. The approximation sign remains because temporary gathers and uneven tensor sizes prevent the physical memory from being exactly that ideal share.

M_total is shardable model state and P is the number of cooperating devices under an ideal balanced partition.

##### Why the melody needs these exact notes

[Division](../MATHEMATICAL_MOVES.md#division) expresses an equal share per device. Multiplication describes the failed replicated system's total cluster memory, not the amount one device must hold. [Approximation](../MATHEMATICAL_MOVES.md#approximation) admits temporary gathers, buffers, and uneven tensors.

Inside zero, familiar operations return with stricter duties: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Every mark in the coming zero equation now belongs to a visible part of the case. The compressed form is:

$$
M_{\text{state per device}}\approx\frac{M_{\text{total state}}}{P}
$$

#### Where zero runs out

Because a worker no longer owns a complete state by itself, sharding trades redundant memory for communication and makes recovery and state ownership more complex.

The zero repair holds, but the world asks for something it was never given. At the Engine Cavern, that unmet need is preserved rather than hidden behind a stronger claim.

---

### Excavation 173 — Tensor Parallelism — Split One Matrix That No Device Can Hold

Sharded parameters can be gathered for computation, but the largest matrix itself becomes too large to materialize or multiply on one worker.

The previous discovery reaches the Engine Cavern carrying one unfinished problem. Beside the brass reference machine, the enginewright first tries to assign whole layers to different devices and pass every activation through them sequentially.

There is good reason to begin this way. If we assign whole layers to different devices and pass every activation through them sequentially, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: one oversized layer still cannot fit, and devices responsible for later layers wait while earlier ones work.

This failure cannot be repaired by performing the instruction to assign whole layers to different devices and pass every activation through them sequentially more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the brass reference machine; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Tensor Parallelism**. The name is simply a handle for the distinction already reconstructed.

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

---

### Excavation 174 — Speculative Decoding — Let a Small Model Propose, Never Decide

Tensor parallelism makes one target-model step possible, but autoregressive dependence still serializes token generation.

A new case arrives at the Engine Cavern. Nothing yet demands a new invention, so the enginewright uses the brass reference machine to let a cheap draft model emit several tokens and return them directly.

This is precisely the kind of shortcut a careful builder should try first. The instruction to let a cheap draft model emit several tokens and return them directly preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: speed improves by silently replacing the trusted target distribution with a weaker model's distribution.

The counterexample separates two questions that the attempt to let a cheap draft model emit several tokens and return them directly had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the brass reference machine fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Speculative Decoding**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

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

---

### Excavation 175 — A Modern Tiny Language Model — Assemble the Measured Engine

Speculative decoding accelerates the final serial loop. We now have many locally useful repairs, but a pile of optimizations is not yet one reproducible model.

Inside the Engine Cavern, the old method is given an honest chance. The enginewright places the evidence on the brass reference machine and tries to enable every technique at once and celebrate if the program runs.

Nothing about this first move is careless. To enable every technique at once and celebrate if the program runs is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: when quality or speed changes, no one knows which mechanism caused it; masks, precision, sharding, and caches can disagree at their boundaries.

The important discovery is not merely that trying to enable every technique at once and celebrate if the program runs failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the brass reference machine, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to assemble the engine in dependency order, preserve a reference path, and test numerical or distributional equivalence at every boundary before accepting measured gains. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **A Modern Tiny Language Model**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

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
