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

The bounded loop can approve a candidate, but approval is meaningless if nobody can reconstruct the system it is supposed to improve.

Perhaps we keep the final score and the model file; those should be enough to compare the next idea.

It survives until the measured run answers back. A rerun changes the data order, random seed, tokenizer revision, and library behavior. Its score moves even though the proposed improvement was never applied.

Now the missing requirement is concrete. Freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline.

Run the same tiny tiger-language model twice from the recorded seed. Only after its loss curve and held-out score agree do we permit one component to change.

The frozen run scores 2.4 and the candidate scores 2.1 on the same loss test. Looking at 2.1 alone cannot tell you whether anything improved. Remove the old 2.4 from the new 2.1: the remaining −0.3 is the candidate's change. We call the old measurement m_baseline, the new one m_candidate, and the remainder delta m only after doing that comparison.

m_baseline is the frozen model's measurement; m_candidate is measured by the same procedure; delta m names only the change between them.

##### Why these operations are forced

[Subtraction](../MATHEMATICAL_MOVES.md#subtraction) removes the common baseline and isolates the candidate's change. Addition would make two large scores look impressive even when they are identical. The order fixes the sign: positive means the candidate raised this metric.

Only now can we compress the procedure:

$$
\Delta m=m_{\text{candidate}}-m_{\text{baseline}}
$$

Reproducibility makes differences attributable; it does not tell us which component is worth changing.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/151-reproducible-baseline/README.md).*

---

### Excavation 152 — Profiling — Measure Where the Time Went

A reproducible baseline gives us a trustworthy before-state. Its first run is too slow for the ranger station, but a total runtime does not identify the guilty stage.

Perhaps we optimize the largest-looking matrix because attention is famous for being expensive.

It survives until the measured run answers back. The device spends much of the run waiting for data and moving tensors. Making one matrix faster barely changes the wall clock.

Now the missing requirement is concrete. Measure data loading, computation, communication, and idle time separately before choosing a repair.

A 100 ms step contains 35 ms of loading, 45 ms of compute, 10 ms of communication, and 10 ms idle. The first engineering question is now visible in numbers.

Start a stopwatch with one training step. Loading ends at 35 ms; computation then carries the clock to 80; communication to 90; idle synchronization to 100. These are consecutive pieces of one elapsed interval, so you join them end to end. The name T_step is simply the final reading after T_data, T_compute, T_communication, and T_idle have all contributed.

Each T names elapsed time assigned to one non-overlapping stage of the same training step.

##### Why these operations are forced

[Addition](../MATHEMATICAL_MOVES.md#addition) is forced because these non-overlapping durations occur along one wall-clock path and accumulate into total time. Multiplication would claim that doubling one stage scales every other stage. The equality is valid only when the measured categories cover the step without overlap.

Only now can we compress the procedure:

$$
T_{\text{step}}=T_{\text{data}}+T_{\text{compute}}+T_{\text{communication}}+T_{\text{idle}}
$$

A profile describes this workload on this hardware; changing sequence length or batch size can move the bottleneck.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/152-profiling/README.md).*

---

### Excavation 153 — The Input Pipeline — Stop Making the Accelerator Wait

Profiling reveals that the accelerator repeatedly waits for the next token batch. The model is ready, but its evidence is still being read and prepared.

Perhaps we load a batch, wait until loading finishes, compute it, and only then begin loading the next one.

It survives until the measured run answers back. Data time and compute time are paid sequentially on every step, leaving expensive compute hardware idle.

Now the missing requirement is concrete. Prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering.

If loading takes 35 ms and compute 45 ms, serial work costs 80 ms. Once overlapped, a steady-state step is governed mainly by the slower 45 ms stage.

Now give the ranger station's data loader and accelerator separate workers and start both together. Loading finishes after 35 ms, but the next step is still waiting for computation at 45 ms. The pair is ready when the slower worker finishes—not after 35+45 ms. That finishing time is what T_overlapped records; the approximation sign leaves room for pipeline startup and coordination.

The two times describe stages allowed to run concurrently after the pipeline is filled.

##### Why these operations are forced

[Maximum](../MATHEMATICAL_MOVES.md#maximum) appears because concurrent stages finish when the slower one finishes. Adding would describe serial execution—the failed design. [Approximation](../MATHEMATICAL_MOVES.md#approximation) admits startup, synchronization, and overhead that prevent perfect overlap.

Only now can we compress the procedure:

$$
T_{\text{overlapped}}\approx\max(T_{\text{data}},T_{\text{compute}})
$$

Prefetching can hide latency, not unlimited data cost; workers, memory, or storage bandwidth can become the next limit.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/153-input-pipeline/README.md).*

---

### Excavation 154 — Sequence Packing — Stop Training on Empty Space

The input pipeline now keeps the device busy. Inspection shows that many of the tokens occupying each fixed rectangle are padding rather than language.

Perhaps we pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste.

It survives until the measured run answers back. The loss ignores padding, but attention and matrix multiplication still spend time and memory carrying those empty positions.

Now the missing requirement is concrete. Pack several short examples into each fixed-length row and mask their boundaries so examples cannot read one another.

Lengths 6, 5, 3, and 2 fill two rows of length 8 exactly. Padding falls from 16 allocated positions with 6 empty to 16 positions with none empty.

Draw two rows with eight boxes each: sixteen paid positions. Place sequences of lengths 6 and 2 in the first row, then 5 and 3 in the second. All sixteen boxes now contain real tokens. To ask what share of the paid space teaches the model, put useful boxes over paid boxes: 16/16. Eta_pack is only a short name for that useful fraction.

The numerator counts language tokens that create lessons; the denominator counts every position for which hardware reserves work.

##### Why these operations are forced

[Division](../MATHEMATICAL_MOVES.md#division) forms the useful share per allocated position, making batches of different sizes comparable. A raw token count would reward larger batches even if their wasted fraction were worse. The ratio stays between zero and one because real tokens cannot exceed allocated positions.

Only now can we compress the procedure:

$$
\eta_{\text{pack}}=\frac{N_{\text{real tokens}}}{N_{\text{allocated positions}}}
$$

Packing improves utilization only if masks and position resets prevent cross-example contamination.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/154-sequence-packing/README.md).*

---

### Excavation 155 — Rotary Position Embeddings — Let Distance Enter the Match

Packed training supplies dense sequences, but the learned absolute position cards from our first GPT bind each slot to a private identity rather than making relative displacement part of the query-key match.

Perhaps we learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples.

It survives until the measured run answers back. Moving the same phrase from positions 10–12 to 110–112 changes every position vector although the internal distances are unchanged.

Now the missing requirement is concrete. Rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference.

Rotate the two coordinates of tiger by angle mθ and river by nθ. Their match depends on (m−n)θ, so shifting both tokens together preserves their separation signal.

Imagine the pair of coordinates as a clock hand beginning at [1,0]. At position one, a quarter-turn sends it to [0,1]; at position two, another quarter-turn sends it to [−1,0]. The hand's length never changes—only its angle does. Multiplying position p by the chosen turn theta tells us the total angle; the four cosine-and-sine entries record how any starting pair must contribute to its two rotated coordinates.

p is token position, theta is one rotation frequency, and R rotates one coordinate pair without changing its length.

##### Why these operations are forced

[Function application](../MATHEMATICAL_MOVES.md#function-application) applies the same rotation rule at each position. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) mixes the two coordinates according to cosine and sine; [addition](../MATHEMATICAL_MOVES.md#addition) combines their signed contributions. Squaring or adding p would change magnitude instead of encoding position as an angle whose differences survive a shared shift.

Only now can we compress the procedure:

$$
R(p\theta)=\begin{bmatrix}\cos(p\theta)&-\sin(p\theta)\\\sin(p\theta)&\cos(p\theta)\end{bmatrix}
$$

RoPE supplies structured relative position, but distances far beyond training still produce unfamiliar phases.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/155-rotary-position/README.md).*

---

### Excavation 156 — Relative Position Bias — What Should Happen Beyond the Seen Window?

Rotary position makes displacement visible inside the attention match. When the station tests much longer sequences, the model must rank relationships at separations absent from training.

Perhaps we trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there.

It survives until the measured run answers back. A mathematically defined position is not necessarily a learned behavior; attention can become erratic at unfamiliar separations.

Now the missing requirement is concrete. Add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation.

For one head with slope 0.1, a key 2 places back receives −0.2 while a key 20 places back receives −2.0 before softmax. Content can overcome the penalty, but distance has a predictable cost.

Suppose tiger matches one key with content score 3.0. The key is two places away, and we decide that each place should cost 0.1, so distance contributes 2×0.1=0.2. Removing that cost leaves 2.8. A key twenty places away pays 20×0.1=2.0 and keeps 1.0. We now name the original content score s_ij, the price per place m, and the adjusted result s-prime.

s_ij is the content match, |i−j| is token separation, m is this head's nonnegative distance slope, and s-prime is the adjusted score.

##### Why these operations are forced

[Subtraction](../MATHEMATICAL_MOVES.md#subtraction) lowers rather than raises distant matches. [Absolute value](../MATHEMATICAL_MOVES.md#absolute-value) keeps separation size while discarding left-versus-right direction in this bias. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) lets slope m control the price per position; adding a fixed m would not make farther tokens cost more.

Only now can we compress the procedure:

$$
s_{ij}^{\prime}=s_{ij}-m\lvert i-j\rvert
$$

A fixed distance preference can suppress a decisive remote clue and is an architectural bias, not universal truth.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/156-relative-position-bias/README.md).*

---

### Excavation 157 — The KV Cache — Stop Re-reading the Entire Past

Relative position now behaves predictably, but autoregressive generation still reruns the Transformer over the full prefix after appending each token.

Perhaps we at step t, recompute keys and values for positions 1 through t because the prefix is presented again.

It survives until the measured run answers back. Past token representations are unchanged in causal decoding, so the same projections are calculated repeatedly while one new token is added.

Now the missing requirement is concrete. Store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache.

Generating token 101 computes one new key and value, then reads the 100 cached pairs. It does not rebuild pairs 1 through 100.

At token 101, write the hundred old keys on cards and compute one new card. Nothing on the old cards has changed, so combining must mean placing card 101 after cards 1 through 100—not adding their numbers together. K_1:t−1 names the ordered stack already present, k_t the one new card, and K_1:t the longer stack after appending.

K_1:t−1 is the unchanged past cache, k_t is the newly computed key, and K_1:t is the cache available to the current query.

##### Why these operations are forced

[Function application](../MATHEMATICAL_MOVES.md#function-application) names one append operation. Appending preserves order and old values; [addition](../MATHEMATICAL_MOVES.md#addition) would numerically blend keys and destroy which token produced each one. The indices show that only position t is new.

Only now can we compress the procedure:

$$
K_{1:t}=\mathrm{append}(K_{1:t-1},k_t)
$$

Because every past key and value must remain available, saved computation becomes growing memory and memory-bandwidth cost, especially for long contexts and many users.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/157-kv-cache/README.md).*

---

### Excavation 158 — Multi-Query Attention — Why Cache Separate Copies for Every Head?

Caching turns repeated arithmetic into memory reads. Profiling now shows decoding limited by loading separate key and value histories for every attention head.

Perhaps we preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections.

It survives until the measured run answers back. The caches grow with both sequence length and head count, and loading them dominates the arithmetic for one new token.

Now the missing requirement is concrete. Keep many query heads but share one key head and one value head across them.

Eight query experts ask eight different questions of the same cached catalog. Cache entries fall from eight key-value pairs per token to one pair per token.

Take one layer with 100 remembered tokens. If each KV head stores 64 coordinates, one head needs 100×64 coordinate slots for keys and the same again for values. Eight heads need eight copies of those slots. The three counts—tokens L, KV heads H_KV, and width d_h—multiply because every choice from one count is paired with every choice from the others.

L is cached sequence length, H_KV is the number of key-value heads, and d_h is the width stored per head.

##### Why these operations are forced

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) appears because every token stores every KV head's coordinates: doubling any factor doubles memory. [Proportionality](../MATHEMATICAL_MOVES.md#proportionality) omits fixed factors such as both K and V, bytes per number, layers, and batch size while preserving the scaling argument.

Only now can we compress the procedure:

$$
M_{\text{KV}}\propto L H_{\text{KV}} d_h
$$

A single shared catalog can remove distinctions that genuinely need different key-value spaces.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/158-multi-query-attention/README.md).*

---

### Excavation 159 — Grouped-Query Attention — Recover Some Specialist Memory

One shared KV head makes decoding light enough for the station, but evaluation finds a quality loss on relationships that benefited from distinct catalogs.

Perhaps we return immediately to one KV head per query head.

It survives until the measured run answers back. Quality recovers, but so does the full cache and bandwidth cost that forced sharing.

Now the missing requirement is concrete. Partition query heads into groups; queries remain distinct while each group shares one key-value head.

Eight query heads arranged into two KV groups preserve two catalogs. The cache is twice MQA's size but one quarter of ordinary eight-head KV storage.

Line up the model's eight query heads and two KV catalogs. Four consecutive query heads must point to catalog 0 and the next four to catalog 1. Scaling head number h from the eight-head range into the two-catalog range gives h×2/8; rounding down turns positions 0 through 3 into address 0 and positions 4 through 7 into address 1. The name g(h) records that address-making rule.

h is a query-head index, H_Q counts query heads, H_KV counts shared KV groups, and g(h) selects the group serving head h.

##### Why these operations are forced

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) spreads the KV group range across query-head indices; [division](../MATHEMATICAL_MOVES.md#division) converts one query index into its proportional group location. The floor deliberately [rounds](../MATHEMATICAL_MOVES.md#rounding) down so every head receives one valid discrete group rather than a fractional address.

Only now can we compress the procedure:

$$
g(h)=\left\lfloor\frac{hH_{\text{KV}}}{H_Q}\right\rfloor
$$

Because sharing deliberately removes independent KV views, the number and assignment of groups remain empirical design choices whose quality must be measured.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/159-grouped-query-attention/README.md).*

---

### Excavation 160 — FlashAttention — The Arithmetic Was Not the Bottleneck

Grouped-query attention makes generation economical, yet training long packed sequences still materializes a large attention-score matrix in slow device memory.

Perhaps we reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost.

It survives until the measured run answers back. Approximation changes the model, while profiling shows much of the time is spent writing and rereading exact intermediate scores rather than multiplying them.

Now the missing requirement is concrete. Tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once.

Process two score tiles. Carry only the running maximum, normalized denominator, and weighted value total into the next tile; the final answer matches ordinary softmax attention.

The model's first attention tile contains scores 1 and 4, so 4 becomes the remembered safety ceiling. The next tile contains 3 and 2; neither exceeds 4, so the ceiling remains 4. If a later tile contained 7, the ceiling would become 7 and the earlier exponential totals would be rescaled. Thus m is the largest score already processed, the s_j values are the arriving tile, and m-prime is the one maximum covering both histories.

m is the largest score already seen, s_j are scores in the new tile, and m-prime is the safe maximum for the combined tiles.

##### Why these operations are forced

[Maximum](../MATHEMATICAL_MOVES.md#maximum) preserves the one value needed to stabilize exponentials across both old and new tiles. Addition would invent a score that never occurred; averaging could be lower than the true maximum and allow overflow. The prime marks the updated running version; see [symbol decorations](../MATHEMATICAL_MOVES.md#symbol-decorations).

Only now can we compress the procedure:

$$
m^{\prime}=\max(m,\max_j s_j)
$$

FlashAttention removes avoidable memory traffic, not quadratic pairwise arithmetic itself.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/160-flash-attention/README.md).*

---

### Excavation 161 — RMSNorm — Do We Need to Subtract the Centre?

FlashAttention removes one systems bottleneck, making smaller repeated operations visible. Layer normalization calculates both a mean and a spread at every token and layer.

Perhaps we delete normalization because each individual operation appears cheap.

It survives until the measured run answers back. Deep residual streams drift in scale and training destabilizes; the repeated control was doing essential work.

Now the missing requirement is concrete. Keep rescaling invariance by dividing by root-mean-square magnitude, while testing whether explicit recentering is dispensable.

Vectors [3,4] and [30,40] become the same relative pattern after division by their RMS, although neither has its mean subtracted.

Take the model feature pair [3,4]. Adding the raw values would let a negative feature cancel a positive one, so first turn their sizes into 9 and 16. Together they contribute 25; shared across two features that is 12.5 per feature. Its square root, about 3.54, returns to the features' ordinary units. Only now do we call this typical magnitude RMS(x) and the feature count d.

d is feature width; each x_i is one feature; RMS(x) is the vector's typical magnitude before a learned scale is applied.

##### Why these operations are forced

[Squaring](../MATHEMATICAL_MOVES.md#powers) keeps negative and positive feature magnitudes from cancelling. [Summation](../MATHEMATICAL_MOVES.md#summation) gathers every feature's contribution, [division](../MATHEMATICAL_MOVES.md#division) makes the magnitude per feature, and the [square root](../MATHEMATICAL_MOVES.md#square-root) returns to the original scale. Omitting division would make wider vectors appear larger merely for having more coordinates.

Only now can we compress the procedure:

$$
\mathrm{RMS}(x)=\sqrt{\frac1d\sum_{i=1}^{d}x_i^2}
$$

RMSNorm does not guarantee that recentering is unimportant for every architecture or task.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/161-rmsnorm/README.md).*

---

### Excavation 162 — Pre-Normalization — Protect the Residual Highway

The block is cheaper, but making it deeper reveals unstable early gradients when normalization follows each residual addition.

Perhaps we keep post-normalization because each block's output then looks standardized before the next block.

It survives until the measured run answers back. The supposedly clean output places normalization directly on the identity route every gradient must cross, making the long residual path harder to preserve.

Now the missing requirement is concrete. Normalize only the input to the changing branch and let the identity stream pass around it unchanged.

A block computes a normalized proposal F, then adds that proposal to the untouched x. If F initially contributes little, the block can behave almost like identity.

Let the residual stream carry a useful tiger signal x. The new branch examines a normalized copy and proposes a correction F(...). At initialization that proposal may be almost zero. Adding it to the untouched x lets the block say 'change nothing yet'; replacing x with the proposal would destroy the signal. The layer indices merely distinguish the stream before and after this addition.

x_l is the residual stream entering layer l; RMSNorm prepares only the branch; F proposes a change; x_l+1 is the next stream.

##### Why these operations are forced

[Function application](../MATHEMATICAL_MOVES.md#function-application) fixes the order: normalize, then transform. [Addition](../MATHEMATICAL_MOVES.md#addition) preserves an untouched identity contribution beside the proposal. Replacing x with F would erase the gradient highway; normalizing the sum would place another transformation on that highway.

Only now can we compress the procedure:

$$
x_{\ell+1}=x_\ell+F(\mathrm{RMSNorm}(x_\ell))
$$

Pre-normalization improves gradient behavior but changes representation scale and does not eliminate every deep-training instability.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/162-pre-normalization/README.md).*

---

### Excavation 163 — SwiGLU — Let One Learned Path Gate Another

Pre-normalization lets gradients reach deep blocks, but the ordinary feed-forward network applies one fixed activation independently to one projection.

Perhaps we make the hidden layer merely wider and trust more coordinates to express every conditional interaction.

It survives until the measured run answers back. Width adds capacity but still asks one projection both to create content and decide when that content matters.

Now the missing requirement is concrete. Create one content projection and one gate projection; use the smooth gate to scale content feature by feature.

For a token describing a river bank, one path proposes financial features while the gate suppresses them; in a money context the same content path can be opened.

Picture one candidate feature saying 'river-bank meaning: 5.' A separate learned gate examines this occurrence of bank. Near the river it may open close to 1, allowing almost all 5 through; near money it may close near 0, silencing that feature. This demands multiplication: zero times content must become zero. W_v creates the candidate, W_g creates gate evidence, SiLU shapes that evidence, and the circled product pairs each gate with its own feature.

W_g creates gate evidence, SiLU bends it smoothly, W_v creates candidate content, and the circled product combines matching hidden coordinates.

##### Why these operations are forced

[Function application](../MATHEMATICAL_MOVES.md#function-application) makes the gate depend on this token. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) is forced because a zero gate must silence its matching content and a partial gate must scale it. Addition would let closed content leak through. The elementwise mark means aligned coordinates interact rather than forming every pair.

Only now can we compress the procedure:

$$
\mathrm{SwiGLU}(x)=\mathrm{SiLU}(xW_g)\odot(xW_v)
$$

Gating improves useful capacity but increases projection parameters and does not explain what every hidden feature means.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/163-swiglu/README.md).*

---

### Excavation 164 — Weight Tying — Use One Word Geometry Twice

SwiGLU improves the block, but the model stores one large table for input embeddings and another large matrix for scoring the same vocabulary at output.

Perhaps we let both matrices learn independently because reading a token and predicting it are different jobs.

It survives until the measured run answers back. The model spends parameters learning two unrelated geometries for the same set of word identities, and rare tokens receive weak evidence in both places.

Now the missing requirement is concrete. Reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias.

The tiger vector used to enter the model also becomes the direction a final hidden state must align with to predict tiger.

The input table already contains a row pointing in the learned direction of tiger. At the output, predicting tiger means asking how strongly the final hidden state points along that same direction. Turning table rows into scoring columns changes only their orientation. E names the existing table, T marks that turn, and equality says W_out is the very same learned values—not a second copy trained to resemble them.

E stores one embedding row per token; transpose turns those rows into output-scoring columns without changing their values.

##### Why these operations are forced

[Equality](../MATHEMATICAL_MOVES.md#equals) imposes shared parameters rather than merely similar initialization. Transposition changes orientation so matrix shapes fit; it does not relearn or numerically transform the coordinates. Using addition would combine two matrices instead of making one geometry perform both roles.

Only now can we compress the procedure:

$$
W_{\text{out}}=E^{\mathsf T}
$$

Tying reduces parameters and imposes a useful constraint, but separate input and output roles may sometimes benefit from extra freedom.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/164-weight-tying/README.md).*

---

### Excavation 165 — Adam — Give Each Parameter Its Own Step Scale

Weight tying concentrates more roles in shared parameters. During training, some coordinates receive frequent large gradients while rare-token coordinates receive sparse small ones.

Perhaps we use the same raw gradient step scale for every parameter.

It survives until the measured run answers back. A rate safe for frequent large gradients barely moves sparse coordinates; a rate large enough for sparse coordinates makes noisy ones unstable.

Now the missing requirement is concrete. Keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude.

A frequently noisy weight builds a large second-moment estimate and receives a smaller normalized step; a consistently directed sparse weight can still move.

Follow one weight that repeatedly receives gradients near 2 and another that usually receives gradients near 0.2. A single raw step scale makes their movement differ tenfold even if each signal is ordinary for its own weight. Remember each weight's recent direction in m and its recent squared size in v; compare direction with the square root of size, then let eta choose the common overall pace. Epsilon is the tiny floor that keeps a never-touched weight from asking us to divide by zero.

m-hat is bias-corrected directional memory, v-hat is bias-corrected squared-gradient memory, eta is global scale, and epsilon prevents division by zero.

##### Why these operations are forced

[Division](../MATHEMATICAL_MOVES.md#division) measures direction relative to recent gradient magnitude, giving each coordinate an adaptive scale. The [square root](../MATHEMATICAL_MOVES.md#square-root) returns squared-gradient memory to gradient units. [Subtraction](../MATHEMATICAL_MOVES.md#subtraction) moves opposite estimated uphill direction; adding would increase loss locally.

Only now can we compress the procedure:

$$
\theta_{t+1}=\theta_t-\eta\frac{\widehat m_t}{\sqrt{\widehat v_t}+\epsilon}
$$

Adaptive scaling can generalize differently from SGD and introduces extra state for every parameter.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/165-adam/README.md).*

---

### Excavation 166 — AdamW — Keep Shrinkage Separate from Adaptation

Adam trains the block, but adding an L2 penalty to the loss sends shrinkage through the optimizer's coordinate-wise rescaling.

Perhaps we treat penalty gradients and data gradients identically because both appear in one total loss.

It survives until the measured run answers back. Coordinates with different gradient histories receive different effective shrinkage even when the intended rule was to decay all selected weights at one rate.

Now the missing requirement is concrete. Apply Adam's adaptive data update and parameter decay as separate operations.

Two equal weights with different gradient histories receive different Adam steps but the same proportional decay.

Suppose two weights both equal 2, although their gradient histories differ. If decay means 'remove one tenth of one percent of the present weight this step,' both should lose the same proportion before their evidence-driven Adam movements differ. Multiplying theta by 1−eta lambda performs that direct shrink. The separate subtraction then applies Adam's learned direction, preventing gradient history from secretly changing the intended decay rule.

lambda is decay strength; the first term shrinks the old parameter directly; the second is Adam's data-driven update.

##### Why these operations are forced

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) by 1−eta lambda makes decay proportional to current parameter size: a zero weight stays zero and doubling a weight doubles shrinkage. [Subtraction](../MATHEMATICAL_MOVES.md#subtraction) then applies the independently adapted loss step. Hiding decay inside m and v would mix two jobs the formula deliberately separates.

Only now can we compress the procedure:

$$
\theta_{t+1}=(1-\eta\lambda)\theta_t-\eta\frac{\widehat m_t}{\sqrt{\widehat v_t}+\epsilon}
$$

Decoupled decay still requires choosing which parameters to decay and how strongly.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/166-adamw/README.md).*

---

### Excavation 167 — Gradient Clipping — Stop One Shock from Becoming a Catastrophe

Most steps are stable, but a rare batch produces an enormous global gradient norm and overwhelms Adam's still-developing moment estimates.

Perhaps we discard the entire batch whenever any gradient coordinate looks large.

It survives until the measured run answers back. Useful directional evidence is lost, and one arbitrary coordinate threshold ignores the size of the full update vector.

Now the missing requirement is concrete. Preserve the gradient's direction but scale its whole norm down only when it exceeds a chosen ceiling.

A gradient of length 20 with ceiling 5 is multiplied by one quarter. A gradient of length 3 passes unchanged.

The model's current gradient points in a useful direction but has length 20, while this run permits length 5. The required scale is 5/20, or one quarter, so every component shrinks by one quarter and direction survives. If the next gradient has length 3, the fraction 5/3 would enlarge it—exactly what we do not want—so we cap the multiplier at 1. We call the ceiling c, the original advice g, and the safe advice g-prime.

g is the original gradient vector, c is the allowed norm ceiling, and g-prime is the gradient actually given to the optimizer.

##### Why these operations are forced

[Division](../MATHEMATICAL_MOVES.md#division) computes the fraction needed to bring the current norm down to c. [Minimum](../MATHEMATICAL_MOVES.md#minimum) chooses at most one, so small gradients are never enlarged. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) scales every coordinate equally, preserving direction; clipping coordinates separately would rotate the update.

Only now can we compress the procedure:

$$
g^{\prime}=g\min\left(1,\frac{c}{\lVert g\rVert}\right)
$$

Clipping limits damage; it can hide a broken loss, corrupt data, or an unsuitable learning rate if used without diagnosis.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/167-gradient-clipping/README.md).*

---

### Excavation 168 — Mixed Precision — Stop Storing Every Number with Unneeded Detail

Stable gradients now expose the physical bill: weights, activations, and gradients are stored and moved as wide numbers even when many operations tolerate fewer bits.

Perhaps we convert every value and every update permanently to half precision.

It survives until the measured run answers back. Small updates disappear when rounded into large weights, and some intermediate values overflow or underflow the smaller numeric range.

Now the missing requirement is concrete. Use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision.

A million activation values require roughly two megabytes at 16 bits instead of four at 32 bits, while a 32-bit master weight accumulates tiny updates safely.

Place one million model activation numbers in memory. At 32 bits each they occupy 32 million bits; at 16 bits each, 16 million bits. Hardware reports bytes, with eight bits in each byte, so divide either total by eight: four megabytes versus two. N counts the values, b is the chosen bits per value, and M is the resulting payload in bytes.

N is the number of stored scalar values, b is bits per value, and division by eight converts bits into bytes.

##### Why these operations are forced

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) is forced because every one of N values consumes b bits. [Division](../MATHEMATICAL_MOVES.md#division) converts units using eight bits per byte; adding eight would not perform a unit conversion. The equality describes payload memory and intentionally omits allocator overhead.

Only now can we compress the procedure:

$$
M=\frac{N b}{8}\ \text{bytes}
$$

Mixed precision reduces representation cost, but numeric range—not only bit count—still threatens small gradients.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/168-mixed-precision/README.md).*

---

### Excavation 169 — Loss Scaling — Rescue Gradients Too Small to Represent

The forward pass looks correct, but some half-precision gradients round to zero before the optimizer can use them.

Perhaps we increase the learning rate so small updates become visible.

It survives until the measured run answers back. The learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update.

Now the missing requirement is concrete. Multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating.

A gradient 0.000001 becomes 0.001 when loss scale is 1000, survives backpropagation, and returns to 0.000001 after unscaling.

A true gradient of 0.000001 may vanish in half precision. Before differentiation, make the loss one thousand times larger; every loss-derived gradient becomes 0.001 and survives. Before updating the weight, divide by the same thousand and recover 0.000001. S names this temporary magnifier, L the original loss, and g the restored gradient—the model has not been told to learn a thousand times faster.

L is original loss, S is a temporary positive scale, and g is the recovered gradient in the loss's original units.

##### Why these operations are forced

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) by S enlarges every loss-derived gradient before narrow arithmetic can erase it. [Division](../MATHEMATICAL_MOVES.md#division) by the same S reverses that temporary unit change before the optimizer. Adding S would not proportionally enlarge tiny sensitivities and could not be undone uniformly.

Only now can we compress the procedure:

$$
g=\frac{1}{S}\nabla_\theta(SL)
$$

A scale large enough to prevent underflow can cause overflow, so practical systems adjust it dynamically.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/169-loss-scaling/README.md).*

---

### Excavation 170 — Gradient Accumulation — Build a Large Batch That Does Not Fit

The optimizer needs a less noisy effective batch, but all its examples and activations cannot coexist on one device.

Perhaps we reduce the batch until it fits and change nothing else.

It survives until the measured run answers back. The gradient becomes noisier and the training regime changes; increasing the learning rate cannot recreate evidence never averaged together.

Now the missing requirement is concrete. Run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step.

Four micro-batches of eight examples create one effective batch of thirty-two while only eight examples' activations are resident at a time.

Imagine four small tables of eight examples arriving one after another. Each table gives its own average advice about the weights, but none is allowed to update yet. Add the four pieces of advice into one pending total, then share that total across the four witnesses. K counts those witnesses, g_k names one witness's advice, and g_effective is what the single optimizer step hears.

K is the number of micro-batches and g_k is the gradient average produced by micro-batch k of equal size.

##### Why these operations are forced

[Summation](../MATHEMATICAL_MOVES.md#summation) lets every micro-batch contribute to the same pending update. [Division](../MATHEMATICAL_MOVES.md#division) returns advice per micro-batch so increasing K does not enlarge the step by itself. Multiplication would let a zero coordinate in one micro-batch erase all others.

Only now can we compress the procedure:

$$
g_{\text{effective}}=\frac1K\sum_{k=1}^{K}g_k
$$

Accumulation lowers activation memory but adds serial work and does not reduce parameter or optimizer-state memory.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/170-gradient-accumulation/README.md).*

---

### Excavation 171 — Activation Checkpointing — Remember Less, Recompute Exactly

Only one micro-batch is resident, yet backpropagation retains every layer's intermediate values until their gradients are computed.

Perhaps we delete all activations after the forward pass.

It survives until the measured run answers back. Backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly.

Now the missing requirement is concrete. Keep selected checkpoint activations and recompute the missing segments once when backward reaches them.

In a nine-layer chain, retain boundaries around three-layer segments. Backward rebuilds one segment at a time instead of storing all nine layers.

In a model chain of nine layers, keeping every activation costs nine stored boundaries. Keep only layers 0, 3, and 6; during backward work, rebuild the three missing operations inside the needed segment. For a much longer chain, choosing about the square root of L boundaries creates segments of about the same length, balancing stored checkpoints against recomputation. Big-O records this growth pattern, not an exact byte count.

L is the number of sequential layers and the expression records the memory-growth order under a balanced basic checkpoint scheme.

##### Why these operations are forced

[Square root](../MATHEMATICAL_MOVES.md#square-root) appears because balancing roughly sqrt(L) stored boundaries with sqrt(L)-sized recomputed segments minimizes the larger side of the trade. [Proportionality](../MATHEMATICAL_MOVES.md#proportionality) is implicit in big-O: exact bytes depend on activation shapes and implementation.

Only now can we compress the procedure:

$$
M_{\text{activations}}=O(\sqrt{L})
$$

Checkpointing buys memory with extra computation; a poor partition can save little or recompute too much.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/171-activation-checkpointing/README.md).*

---

### Excavation 172 — ZeRO — Stop Replicating the Same Training State

Recomputation makes the forward graph fit, but AdamW stores parameters, gradients, first moments, and second moments. Ordinary data parallelism copies all of them onto every device.

Perhaps we add devices and replicate the full training state on each one.

It survives until the measured run answers back. Compute capacity grows while per-device model-state memory remains almost unchanged, so the same memory wall returns.

Now the missing requirement is concrete. Partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them.

Four workers each keep roughly one quarter of a large moment vector rather than four complete copies, then cooperate for the update.

Adam's moment state has twelve equal chunks and four devices are cooperating. Replication gives every device all twelve; sharding gives each device three. Asking for state per device therefore means sharing the total across P owners: total divided by P. The approximation sign remains because temporary gathers and uneven tensor sizes prevent the physical memory from being exactly that ideal share.

M_total is shardable model state and P is the number of cooperating devices under an ideal balanced partition.

##### Why these operations are forced

[Division](../MATHEMATICAL_MOVES.md#division) expresses an equal share per device. Multiplication describes the failed replicated system's total cluster memory, not the amount one device must hold. [Approximation](../MATHEMATICAL_MOVES.md#approximation) admits temporary gathers, buffers, and uneven tensors.

Only now can we compress the procedure:

$$
M_{\text{state per device}}\approx\frac{M_{\text{total state}}}{P}
$$

Because a worker no longer owns a complete state by itself, sharding trades redundant memory for communication and makes recovery and state ownership more complex.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/172-zero-sharding/README.md).*

---

### Excavation 173 — Tensor Parallelism — Split One Matrix That No Device Can Hold

Sharded parameters can be gathered for computation, but the largest matrix itself becomes too large to materialize or multiply on one worker.

Perhaps we assign whole layers to different devices and pass every activation through them sequentially.

It survives until the measured run answers back. One oversized layer still cannot fit, and devices responsible for later layers wait while earlier ones work.

Now the missing requirement is concrete. Split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output.

Divide one vocabulary projection into four column blocks. Each device scores one quarter of the vocabulary from the same hidden state; concatenation restores the full logits.

Split the vocabulary-scoring matrix into four column blocks. Every device receives the same hidden state X but multiplies it by only its own block W_p, producing scores Y_p for its quarter of the vocabulary. Those scores must remain distinct, so place the four blocks beside one another in vocabulary order. Adding them would collapse different tokens into the same slots. Y names the restored full score row after concatenation.

W is partitioned into P column blocks; every worker receives X and produces the corresponding block of output columns.

##### Why these operations are forced

[Concatenation](../MATHEMATICAL_MOVES.md#concatenation) preserves distinct output columns side by side; addition would collapse vocabulary scores that must remain separate. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) applies the same input X to each learned block, and equality states that partitioned execution matches the unsplit matrix operation.

Only now can we compress the procedure:

$$
Y_p=XW_p,\quad Y=[Y_1,Y_2,\ldots,Y_P]
$$

Tensor parallelism introduces communication inside every layer, so a slow interconnect can erase its benefit.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/173-tensor-parallelism/README.md).*

---

### Excavation 174 — Speculative Decoding — Let a Small Model Propose, Never Decide

Tensor parallelism makes one target-model step possible, but autoregressive dependence still serializes token generation.

Perhaps we let a cheap draft model emit several tokens and return them directly.

It survives until the measured run answers back. Speed improves by silently replacing the trusted target distribution with a weaker model's distribution.

Now the missing requirement is concrete. Let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling.

The draft proposes “the tiger sleeps.” One target call verifies all three positions; an unsupported token is rejected and sampling resumes from the corrected target distribution.

If the draft assigns tiger probability 0.8 but the target assigns 0.4, only half of those proposals have target support: 0.4/0.8=0.5. If the draft assigns 0.4 and the target 0.8, the ratio is 2, but acceptance cannot be 200 percent, so it stops at 1. The function a(x) names this capped acceptance chance for proposed token x.

q(x) is draft probability, p(x) is target probability, and a(x) is the probability of accepting the draft token under the correction step.

##### Why these operations are forced

[Division](../MATHEMATICAL_MOVES.md#division) compares target support per unit of draft support. [Minimum](../MATHEMATICAL_MOVES.md#minimum) caps acceptance at one because probabilities cannot exceed certainty. Simply taking max or always accepting would change the target distribution; the ratio corrects proposals that the draft overproduces.

Only now can we compress the procedure:

$$
a(x)=\min\left(1,\frac{p(x)}{q(x)}\right)
$$

Speed depends on draft agreement and hardware utilization; poor proposals add work instead of removing it.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/174-speculative-decoding/README.md).*

---

### Excavation 175 — A Modern Tiny Language Model — Assemble the Measured Engine

Speculative decoding accelerates the final serial loop. We now have many locally useful repairs, but a pile of optimizations is not yet one reproducible model.

Perhaps we enable every technique at once and celebrate if the program runs.

It survives until the measured run answers back. When quality or speed changes, no one knows which mechanism caused it; masks, precision, sharding, and caches can disagree at their boundaries.

Now the missing requirement is concrete. Assemble the engine in dependency order, preserve a reference path, and test numerical or distributional equivalence at every boundary before accepting measured gains.

Train one tiny model with packed examples, RoPE, GQA, exact tiled attention, pre-RMSNorm, SwiGLU, tied embeddings, AdamW, clipping, mixed precision, accumulation, and checkpointing; then serve it with a KV cache and verified draft proposals.

The engine is modern, not final. New hardware, data, and observations will create new bottlenecks, and every proposed repair must re-enter the bounded loop from Excavation 150.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/175-modern-tiny-llm/README.md).*
