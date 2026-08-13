"""Build Part XII as one measured reconstruction of a modern language-model engine."""
from pathlib import Path
import textwrap

ROOT = Path(__file__).parents[1]

# n, slug, title, question, carry, attempt, break, repair, case, limitation,
# formula, term explanation, operation explanation, references
ROWS = [
(151,"reproducible-baseline","A Reproducible Baseline — Improve Something That Actually Exists","What exactly must remain fixed before an improvement can be measured?",
"The bounded loop can approve a candidate, but approval is meaningless if nobody can reconstruct the system it is supposed to improve.",
"Keep the final score and the model file; those should be enough to compare the next idea.",
"A rerun changes the data order, random seed, tokenizer revision, and library behavior. Its score moves even though the proposed improvement was never applied.",
"Freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline.",
"Run the same tiny tiger-language model twice from the recorded seed. Only after its loss curve and held-out score agree do we permit one component to change.",
"Reproducibility makes differences attributable; it does not tell us which component is worth changing.",
r"\Delta m=m_{\text{candidate}}-m_{\text{baseline}}",
"m_baseline is the frozen model's measurement; m_candidate is measured by the same procedure; delta m names only the change between them.",
"[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) removes the common baseline and isolates the candidate's change. Addition would make two large scores look impressive even when they are identical. The order fixes the sign: positive means the candidate raised this metric.",
[("Pythia: A Suite for Analyzing Large Language Models","https://arxiv.org/abs/2304.01373"),("OLMo: Accelerating the Science of Language Models","https://arxiv.org/abs/2402.00838")]),
(152,"profiling","Profiling — Measure Where the Time Went","The baseline is slow. Which operation actually consumes the time?",
"A reproducible baseline gives us a trustworthy before-state. Its first run is too slow for the ranger station, but a total runtime does not identify the guilty stage.",
"Optimize the largest-looking matrix because attention is famous for being expensive.",
"The device spends much of the run waiting for data and moving tensors. Making one matrix faster barely changes the wall clock.",
"Measure data loading, computation, communication, and idle time separately before choosing a repair.",
"A 100 ms step contains 35 ms of loading, 45 ms of compute, 10 ms of communication, and 10 ms idle. The first engineering question is now visible in numbers.",
"A profile describes this workload on this hardware; changing sequence length or batch size can move the bottleneck.",
r"T_{\text{step}}=T_{\text{data}}+T_{\text{compute}}+T_{\text{communication}}+T_{\text{idle}}",
"Each T names elapsed time assigned to one non-overlapping stage of the same training step.",
"[Addition](../../MATHEMATICAL_MOVES.md#addition) is forced because these non-overlapping durations occur along one wall-clock path and accumulate into total time. Multiplication would claim that doubling one stage scales every other stage. The equality is valid only when the measured categories cover the step without overlap.",
[("MLPerf Training Benchmark","https://arxiv.org/abs/1910.01500"),("The Roofline Model","https://doi.org/10.1145/1498765.1498785")]),
(153,"input-pipeline","The Input Pipeline — Stop Making the Accelerator Wait","How can loading overlap computation without changing the lessons?",
"Profiling reveals that the accelerator repeatedly waits for the next token batch. The model is ready, but its evidence is still being read and prepared.",
"Load a batch, wait until loading finishes, compute it, and only then begin loading the next one.",
"Data time and compute time are paid sequentially on every step, leaving expensive compute hardware idle.",
"Prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering.",
"If loading takes 35 ms and compute 45 ms, serial work costs 80 ms. Once overlapped, a steady-state step is governed mainly by the slower 45 ms stage.",
"Prefetching can hide latency, not unlimited data cost; workers, memory, or storage bandwidth can become the next limit.",
r"T_{\text{overlapped}}\approx\max(T_{\text{data}},T_{\text{compute}})",
"The two times describe stages allowed to run concurrently after the pipeline is filled.",
"[Maximum](../../MATHEMATICAL_MOVES.md#maximum) appears because concurrent stages finish when the slower one finishes. Adding would describe serial execution—the failed design. [Approximation](../../MATHEMATICAL_MOVES.md#approximation) admits startup, synchronization, and overhead that prevent perfect overlap.",
[("OLMo: Accelerating the Science of Language Models","https://arxiv.org/abs/2402.00838"),("HLAT: High-quality LLM Pre-training on AWS Trainium","https://arxiv.org/abs/2404.10630")]),
(154,"sequence-packing","Sequence Packing — Stop Training on Empty Space","The pipeline is full, but why is much of each batch padding?",
"The input pipeline now keeps the device busy. Inspection shows that many of the tokens occupying each fixed rectangle are padding rather than language.",
"Pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste.",
"The loss ignores padding, but attention and matrix multiplication still spend time and memory carrying those empty positions.",
"Pack several short examples into each fixed-length row and mask their boundaries so examples cannot read one another.",
"Lengths 6, 5, 3, and 2 fill two rows of length 8 exactly. Padding falls from 16 allocated positions with 6 empty to 16 positions with none empty.",
"Packing improves utilization only if masks and position resets prevent cross-example contamination.",
r"\eta_{\text{pack}}=\frac{N_{\text{real tokens}}}{N_{\text{allocated positions}}}",
"The numerator counts language tokens that create lessons; the denominator counts every position for which hardware reserves work.",
"[Division](../../MATHEMATICAL_MOVES.md#division) forms the useful share per allocated position, making batches of different sizes comparable. A raw token count would reward larger batches even if their wasted fraction were worse. The ratio stays between zero and one because real tokens cannot exceed allocated positions.",
[("Efficient Sequence Packing without Cross-contamination","https://arxiv.org/abs/2107.02027"),("Language Models are Few-Shot Learners","https://arxiv.org/abs/2005.14165")]),
(155,"rotary-position","Rotary Position Embeddings — Let Distance Enter the Match","Packed tokens use the device efficiently. How should attention recognize relative separation?",
"Packed training supplies dense sequences, but the learned absolute position cards from our first GPT bind each slot to a private identity rather than making relative displacement part of the query-key match.",
"Learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples.",
"Moving the same phrase from positions 10–12 to 110–112 changes every position vector although the internal distances are unchanged.",
"Rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference.",
"Rotate the two coordinates of tiger by angle mθ and river by nθ. Their match depends on (m−n)θ, so shifting both tokens together preserves their separation signal.",
"RoPE supplies structured relative position, but distances far beyond training still produce unfamiliar phases.",
r"R(p\theta)=\begin{bmatrix}\cos(p\theta)&-\sin(p\theta)\\\sin(p\theta)&\cos(p\theta)\end{bmatrix}",
"p is token position, theta is one rotation frequency, and R rotates one coordinate pair without changing its length.",
"[Function application](../../MATHEMATICAL_MOVES.md#function-application) applies the same rotation rule at each position. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) mixes the two coordinates according to cosine and sine; [addition](../../MATHEMATICAL_MOVES.md#addition) combines their signed contributions. Squaring or adding p would change magnitude instead of encoding position as an angle whose differences survive a shared shift.",
[("RoFormer: Enhanced Transformer with Rotary Position Embedding","https://arxiv.org/abs/2104.09864")]),
(156,"relative-position-bias","Relative Position Bias — What Should Happen Beyond the Seen Window?","RoPE exposes relative distance, but how should attention treat distances never seen in training?",
"Rotary position makes displacement visible inside the attention match. When the station tests much longer sequences, the model must rank relationships at separations absent from training.",
"Trust every unseen distance to behave like familiar distances merely because the formula can compute an angle there.",
"A mathematically defined position is not necessarily a learned behavior; attention can become erratic at unfamiliar separations.",
"Add an explicit distance-dependent penalty whose direction continues beyond the training window, then measure the quality trade rather than assuming extrapolation.",
"For one head with slope 0.1, a key 2 places back receives −0.2 while a key 20 places back receives −2.0 before softmax. Content can overcome the penalty, but distance has a predictable cost.",
"A fixed distance preference can suppress a decisive remote clue and is an architectural bias, not universal truth.",
r"s_{ij}^{\prime}=s_{ij}-m\lvert i-j\rvert",
"s_ij is the content match, |i−j| is token separation, m is this head's nonnegative distance slope, and s-prime is the adjusted score.",
"[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) lowers rather than raises distant matches. [Absolute value](../../MATHEMATICAL_MOVES.md#absolute-value) keeps separation size while discarding left-versus-right direction in this bias. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) lets slope m control the price per position; adding a fixed m would not make farther tokens cost more.",
[("Train Short, Test Long: ALiBi","https://arxiv.org/abs/2108.12409")]),
(157,"kv-cache","The KV Cache — Stop Re-reading the Entire Past","Position is available at any generated step. Why does the model recompute old keys and values for every new token?",
"Relative position now behaves predictably, but autoregressive generation still reruns the Transformer over the full prefix after appending each token.",
"At step t, recompute keys and values for positions 1 through t because the prefix is presented again.",
"Past token representations are unchanged in causal decoding, so the same projections are calculated repeatedly while one new token is added.",
"Store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache.",
"Generating token 101 computes one new key and value, then reads the 100 cached pairs. It does not rebuild pairs 1 through 100.",
"Because every past key and value must remain available, saved computation becomes growing memory and memory-bandwidth cost, especially for long contexts and many users.",
r"K_{1:t}=\mathrm{append}(K_{1:t-1},k_t)",
"K_1:t−1 is the unchanged past cache, k_t is the newly computed key, and K_1:t is the cache available to the current query.",
"[Function application](../../MATHEMATICAL_MOVES.md#function-application) names one append operation. Appending preserves order and old values; [addition](../../MATHEMATICAL_MOVES.md#addition) would numerically blend keys and destroy which token produced each one. The indices show that only position t is new.",
[("Fast Transformer Decoding: One Write-Head Is All You Need","https://arxiv.org/abs/1911.02150"),("PagedAttention / vLLM","https://arxiv.org/abs/2309.06180")]),
(158,"multi-query-attention","Multi-Query Attention — Why Cache Separate Copies for Every Head?","The KV cache avoids recomputation, but why does every query head store its own keys and values?",
"Caching turns repeated arithmetic into memory reads. Profiling now shows decoding limited by loading separate key and value histories for every attention head.",
"Preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections.",
"The caches grow with both sequence length and head count, and loading them dominates the arithmetic for one new token.",
"Keep many query heads but share one key head and one value head across them.",
"Eight query experts ask eight different questions of the same cached catalog. Cache entries fall from eight key-value pairs per token to one pair per token.",
"A single shared catalog can remove distinctions that genuinely need different key-value spaces.",
r"M_{\text{KV}}\propto L H_{\text{KV}} d_h",
"L is cached sequence length, H_KV is the number of key-value heads, and d_h is the width stored per head.",
"[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) appears because every token stores every KV head's coordinates: doubling any factor doubles memory. [Proportionality](../../MATHEMATICAL_MOVES.md#proportionality) omits fixed factors such as both K and V, bytes per number, layers, and batch size while preserving the scaling argument.",
[("Fast Transformer Decoding: One Write-Head Is All You Need","https://arxiv.org/abs/1911.02150")]),
(159,"grouped-query-attention","Grouped-Query Attention — Recover Some Specialist Memory","Multi-query attention shrinks the cache. Can we regain specialist key-value views without restoring every copy?",
"One shared KV head makes decoding light enough for the station, but evaluation finds a quality loss on relationships that benefited from distinct catalogs.",
"Return immediately to one KV head per query head.",
"Quality recovers, but so does the full cache and bandwidth cost that forced sharing.",
"Partition query heads into groups; queries remain distinct while each group shares one key-value head.",
"Eight query heads arranged into two KV groups preserve two catalogs. The cache is twice MQA's size but one quarter of ordinary eight-head KV storage.",
"Because sharing deliberately removes independent KV views, the number and assignment of groups remain empirical design choices whose quality must be measured.",
r"g(h)=\left\lfloor\frac{hH_{\text{KV}}}{H_Q}\right\rfloor",
"h is a query-head index, H_Q counts query heads, H_KV counts shared KV groups, and g(h) selects the group serving head h.",
"[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) spreads the KV group range across query-head indices; [division](../../MATHEMATICAL_MOVES.md#division) converts one query index into its proportional group location. The floor deliberately [rounds](../../MATHEMATICAL_MOVES.md#rounding) down so every head receives one valid discrete group rather than a fractional address.",
[("GQA: Training Generalized Multi-Query Transformer Models","https://arxiv.org/abs/2305.13245")]),
(160,"flash-attention","FlashAttention — The Arithmetic Was Not the Bottleneck","GQA reduces cache traffic during decoding. Why is full-sequence attention training still dominated by moving its score matrix?",
"Grouped-query attention makes generation economical, yet training long packed sequences still materializes a large attention-score matrix in slow device memory.",
"Reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost.",
"Approximation changes the model, while profiling shows much of the time is spent writing and rereading exact intermediate scores rather than multiplying them.",
"Tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once.",
"Process two score tiles. Carry only the running maximum, normalized denominator, and weighted value total into the next tile; the final answer matches ordinary softmax attention.",
"FlashAttention removes avoidable memory traffic, not quadratic pairwise arithmetic itself.",
r"m^{\prime}=\max(m,\max_j s_j)",
"m is the largest score already seen, s_j are scores in the new tile, and m-prime is the safe maximum for the combined tiles.",
"[Maximum](../../MATHEMATICAL_MOVES.md#maximum) preserves the one value needed to stabilize exponentials across both old and new tiles. Addition would invent a score that never occurred; averaging could be lower than the true maximum and allow overflow. The prime marks the updated running version; see [symbol decorations](../../MATHEMATICAL_MOVES.md#symbol-decorations).",
[("FlashAttention","https://arxiv.org/abs/2205.14135")]),
(161,"rmsnorm","RMSNorm — Do We Need to Subtract the Centre?","Exact attention now moves through memory efficiently. Can normalization keep scale stable with less work?",
"FlashAttention removes one systems bottleneck, making smaller repeated operations visible. Layer normalization calculates both a mean and a spread at every token and layer.",
"Delete normalization because each individual operation appears cheap.",
"Deep residual streams drift in scale and training destabilizes; the repeated control was doing essential work.",
"Keep rescaling invariance by dividing by root-mean-square magnitude, while testing whether explicit recentering is dispensable.",
"Vectors [3,4] and [30,40] become the same relative pattern after division by their RMS, although neither has its mean subtracted.",
"RMSNorm does not guarantee that recentering is unimportant for every architecture or task.",
r"\mathrm{RMS}(x)=\sqrt{\frac1d\sum_{i=1}^{d}x_i^2}",
"d is feature width; each x_i is one feature; RMS(x) is the vector's typical magnitude before a learned scale is applied.",
"[Squaring](../../MATHEMATICAL_MOVES.md#powers) keeps negative and positive feature magnitudes from cancelling. [Summation](../../MATHEMATICAL_MOVES.md#summation) gathers every feature's contribution, [division](../../MATHEMATICAL_MOVES.md#division) makes the magnitude per feature, and the [square root](../../MATHEMATICAL_MOVES.md#square-root) returns to the original scale. Omitting division would make wider vectors appear larger merely for having more coordinates.",
[("Root Mean Square Layer Normalization","https://arxiv.org/abs/1910.07467")]),
(162,"pre-normalization","Pre-Normalization — Protect the Residual Highway","RMSNorm controls scale. Where should it sit so gradients can cross a deep stack?",
"The block is cheaper, but making it deeper reveals unstable early gradients when normalization follows each residual addition.",
"Keep post-normalization because each block's output then looks standardized before the next block.",
"The supposedly clean output places normalization directly on the identity route every gradient must cross, making the long residual path harder to preserve.",
"Normalize only the input to the changing branch and let the identity stream pass around it unchanged.",
"A block computes a normalized proposal F, then adds that proposal to the untouched x. If F initially contributes little, the block can behave almost like identity.",
"Pre-normalization improves gradient behavior but changes representation scale and does not eliminate every deep-training instability.",
r"x_{\ell+1}=x_\ell+F(\mathrm{RMSNorm}(x_\ell))",
"x_l is the residual stream entering layer l; RMSNorm prepares only the branch; F proposes a change; x_l+1 is the next stream.",
"[Function application](../../MATHEMATICAL_MOVES.md#function-application) fixes the order: normalize, then transform. [Addition](../../MATHEMATICAL_MOVES.md#addition) preserves an untouched identity contribution beside the proposal. Replacing x with F would erase the gradient highway; normalizing the sum would place another transformation on that highway.",
[("On Layer Normalization in the Transformer Architecture","https://proceedings.mlr.press/v119/xiong20b.html")]),
(163,"swiglu","SwiGLU — Let One Learned Path Gate Another","The residual highway is stable. Can the private feed-forward workshop choose which features should pass?",
"Pre-normalization lets gradients reach deep blocks, but the ordinary feed-forward network applies one fixed activation independently to one projection.",
"Make the hidden layer merely wider and trust more coordinates to express every conditional interaction.",
"Width adds capacity but still asks one projection both to create content and decide when that content matters.",
"Create one content projection and one gate projection; use the smooth gate to scale content feature by feature.",
"For a token describing a river bank, one path proposes financial features while the gate suppresses them; in a money context the same content path can be opened.",
"Gating improves useful capacity but increases projection parameters and does not explain what every hidden feature means.",
r"\mathrm{SwiGLU}(x)=\mathrm{SiLU}(xW_g)\odot(xW_v)",
"W_g creates gate evidence, SiLU bends it smoothly, W_v creates candidate content, and the circled product combines matching hidden coordinates.",
"[Function application](../../MATHEMATICAL_MOVES.md#function-application) makes the gate depend on this token. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced because a zero gate must silence its matching content and a partial gate must scale it. Addition would let closed content leak through. The elementwise mark means aligned coordinates interact rather than forming every pair.",
[("GLU Variants Improve Transformer","https://arxiv.org/abs/2002.05202")]),
(164,"weight-tying","Weight Tying — Use One Word Geometry Twice","The block now communicates and computes efficiently. Why learn unrelated token geometry at the entrance and exit?",
"SwiGLU improves the block, but the model stores one large table for input embeddings and another large matrix for scoring the same vocabulary at output.",
"Let both matrices learn independently because reading a token and predicting it are different jobs.",
"The model spends parameters learning two unrelated geometries for the same set of word identities, and rare tokens receive weak evidence in both places.",
"Reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias.",
"The tiger vector used to enter the model also becomes the direction a final hidden state must align with to predict tiger.",
"Tying reduces parameters and imposes a useful constraint, but separate input and output roles may sometimes benefit from extra freedom.",
r"W_{\text{out}}=E^{\mathsf T}",
"E stores one embedding row per token; transpose turns those rows into output-scoring columns without changing their values.",
"[Equality](../../MATHEMATICAL_MOVES.md#equals) imposes shared parameters rather than merely similar initialization. Transposition changes orientation so matrix shapes fit; it does not relearn or numerically transform the coordinates. Using addition would combine two matrices instead of making one geometry perform both roles.",
[("Using the Output Embedding to Improve Language Models","https://arxiv.org/abs/1608.05859"),("Tying Word Vectors and Word Classifiers","https://arxiv.org/abs/1611.01462")]),
(165,"adam","Adam — Give Each Parameter Its Own Step Scale","The modernized block has fewer duplicated parameters. Why does one global learning rate still train some weights poorly?",
"Weight tying concentrates more roles in shared parameters. During training, some coordinates receive frequent large gradients while rare-token coordinates receive sparse small ones.",
"Use the same raw gradient step scale for every parameter.",
"A rate safe for frequent large gradients barely moves sparse coordinates; a rate large enough for sparse coordinates makes noisy ones unstable.",
"Keep fading memories of gradient direction and squared gradient size, then scale each coordinate's step by its own recent magnitude.",
"A frequently noisy weight builds a large second-moment estimate and receives a smaller normalized step; a consistently directed sparse weight can still move.",
"Adaptive scaling can generalize differently from SGD and introduces extra state for every parameter.",
r"\theta_{t+1}=\theta_t-\eta\frac{\widehat m_t}{\sqrt{\widehat v_t}+\epsilon}",
"m-hat is bias-corrected directional memory, v-hat is bias-corrected squared-gradient memory, eta is global scale, and epsilon prevents division by zero.",
"[Division](../../MATHEMATICAL_MOVES.md#division) measures direction relative to recent gradient magnitude, giving each coordinate an adaptive scale. The [square root](../../MATHEMATICAL_MOVES.md#square-root) returns squared-gradient memory to gradient units. [Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) moves opposite estimated uphill direction; adding would increase loss locally.",
[("Adam: A Method for Stochastic Optimization","https://arxiv.org/abs/1412.6980")]),
(166,"adamw","AdamW — Keep Shrinkage Separate from Adaptation","Adam adapts every coordinate's step. What happens when weight penalties pass through that same adaptation?",
"Adam trains the block, but adding an L2 penalty to the loss sends shrinkage through the optimizer's coordinate-wise rescaling.",
"Treat penalty gradients and data gradients identically because both appear in one total loss.",
"Coordinates with different gradient histories receive different effective shrinkage even when the intended rule was to decay all selected weights at one rate.",
"Apply Adam's adaptive data update and parameter decay as separate operations.",
"Two equal weights with different gradient histories receive different Adam steps but the same proportional decay.",
"Decoupled decay still requires choosing which parameters to decay and how strongly.",
r"\theta_{t+1}=(1-\eta\lambda)\theta_t-\eta\frac{\widehat m_t}{\sqrt{\widehat v_t}+\epsilon}",
"lambda is decay strength; the first term shrinks the old parameter directly; the second is Adam's data-driven update.",
"[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) by 1−eta lambda makes decay proportional to current parameter size: a zero weight stays zero and doubling a weight doubles shrinkage. [Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) then applies the independently adapted loss step. Hiding decay inside m and v would mix two jobs the formula deliberately separates.",
[("Decoupled Weight Decay Regularization","https://openreview.net/forum?id=Bkg6RiCqY7")]),
(167,"gradient-clipping","Gradient Clipping — Stop One Shock from Becoming a Catastrophe","AdamW separates learning and shrinkage. How should training react to one enormous gradient spike?",
"Most steps are stable, but a rare batch produces an enormous global gradient norm and overwhelms Adam's still-developing moment estimates.",
"Discard the entire batch whenever any gradient coordinate looks large.",
"Useful directional evidence is lost, and one arbitrary coordinate threshold ignores the size of the full update vector.",
"Preserve the gradient's direction but scale its whole norm down only when it exceeds a chosen ceiling.",
"A gradient of length 20 with ceiling 5 is multiplied by one quarter. A gradient of length 3 passes unchanged.",
"Clipping limits damage; it can hide a broken loss, corrupt data, or an unsuitable learning rate if used without diagnosis.",
r"g^{\prime}=g\min\left(1,\frac{c}{\lVert g\rVert}\right)",
"g is the original gradient vector, c is the allowed norm ceiling, and g-prime is the gradient actually given to the optimizer.",
"[Division](../../MATHEMATICAL_MOVES.md#division) computes the fraction needed to bring the current norm down to c. [Minimum](../../MATHEMATICAL_MOVES.md#minimum) chooses at most one, so small gradients are never enlarged. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) scales every coordinate equally, preserving direction; clipping coordinates separately would rotate the update.",
[("On the Difficulty of Training Recurrent Neural Networks","https://arxiv.org/abs/1211.5063")]),
(168,"mixed-precision","Mixed Precision — Stop Storing Every Number with Unneeded Detail","Clipping controls exceptional updates. Why does ordinary precision still make the model too large and slow for the available hardware?",
"Stable gradients now expose the physical bill: weights, activations, and gradients are stored and moved as wide numbers even when many operations tolerate fewer bits.",
"Convert every value and every update permanently to half precision.",
"Small updates disappear when rounded into large weights, and some intermediate values overflow or underflow the smaller numeric range.",
"Use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision.",
"A million activation values require roughly two megabytes at 16 bits instead of four at 32 bits, while a 32-bit master weight accumulates tiny updates safely.",
"Mixed precision reduces representation cost, but numeric range—not only bit count—still threatens small gradients.",
r"M=\frac{N b}{8}\ \text{bytes}",
"N is the number of stored scalar values, b is bits per value, and division by eight converts bits into bytes.",
"[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced because every one of N values consumes b bits. [Division](../../MATHEMATICAL_MOVES.md#division) converts units using eight bits per byte; adding eight would not perform a unit conversion. The equality describes payload memory and intentionally omits allocator overhead.",
[("Mixed Precision Training","https://arxiv.org/abs/1710.03740")]),
(169,"loss-scaling","Loss Scaling — Rescue Gradients Too Small to Represent","Mixed precision halves much of the memory. How can tiny gradients survive its narrower range?",
"The forward pass looks correct, but some half-precision gradients round to zero before the optimizer can use them.",
"Increase the learning rate so small updates become visible.",
"The learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update.",
"Multiply the loss before backpropagation so gradients are representable, then divide the gradients by the same scale before clipping and updating.",
"A gradient 0.000001 becomes 0.001 when loss scale is 1000, survives backpropagation, and returns to 0.000001 after unscaling.",
"A scale large enough to prevent underflow can cause overflow, so practical systems adjust it dynamically.",
r"g=\frac{1}{S}\nabla_\theta(SL)",
"L is original loss, S is a temporary positive scale, and g is the recovered gradient in the loss's original units.",
"[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) by S enlarges every loss-derived gradient before narrow arithmetic can erase it. [Division](../../MATHEMATICAL_MOVES.md#division) by the same S reverses that temporary unit change before the optimizer. Adding S would not proportionally enlarge tiny sensitivities and could not be undone uniformly.",
[("Mixed Precision Training","https://arxiv.org/abs/1710.03740")]),
(170,"gradient-accumulation","Gradient Accumulation — Build a Large Batch That Does Not Fit","Loss scaling preserves small gradients. What if the stable batch size still exceeds device memory?",
"The optimizer needs a less noisy effective batch, but all its examples and activations cannot coexist on one device.",
"Reduce the batch until it fits and change nothing else.",
"The gradient becomes noisier and the training regime changes; increasing the learning rate cannot recreate evidence never averaged together.",
"Run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step.",
"Four micro-batches of eight examples create one effective batch of thirty-two while only eight examples' activations are resident at a time.",
"Accumulation lowers activation memory but adds serial work and does not reduce parameter or optimizer-state memory.",
r"g_{\text{effective}}=\frac1K\sum_{k=1}^{K}g_k",
"K is the number of micro-batches and g_k is the gradient average produced by micro-batch k of equal size.",
"[Summation](../../MATHEMATICAL_MOVES.md#summation) lets every micro-batch contribute to the same pending update. [Division](../../MATHEMATICAL_MOVES.md#division) returns advice per micro-batch so increasing K does not enlarge the step by itself. Multiplication would let a zero coordinate in one micro-batch erase all others.",
[("Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour","https://arxiv.org/abs/1706.02677")]),
(171,"activation-checkpointing","Activation Checkpointing — Remember Less, Recompute Exactly","Accumulation fits fewer examples at once. Why do activations from many layers still exhaust memory?",
"Only one micro-batch is resident, yet backpropagation retains every layer's intermediate values until their gradients are computed.",
"Delete all activations after the forward pass.",
"Backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly.",
"Keep selected checkpoint activations and recompute the missing segments once when backward reaches them.",
"In a nine-layer chain, retain boundaries around three-layer segments. Backward rebuilds one segment at a time instead of storing all nine layers.",
"Checkpointing buys memory with extra computation; a poor partition can save little or recompute too much.",
r"M_{\text{activations}}=O(\sqrt{L})",
"L is the number of sequential layers and the expression records the memory-growth order under a balanced basic checkpoint scheme.",
"[Square root](../../MATHEMATICAL_MOVES.md#square-root) appears because balancing roughly sqrt(L) stored boundaries with sqrt(L)-sized recomputed segments minimizes the larger side of the trade. [Proportionality](../../MATHEMATICAL_MOVES.md#proportionality) is implicit in big-O: exact bytes depend on activation shapes and implementation.",
[("Training Deep Nets with Sublinear Memory Cost","https://arxiv.org/abs/1604.06174")]),
(172,"zero-sharding","ZeRO — Stop Replicating the Same Training State","Checkpointing reduces activation memory. Why does every data-parallel device still hold identical optimizer state?",
"Recomputation makes the forward graph fit, but AdamW stores parameters, gradients, first moments, and second moments. Ordinary data parallelism copies all of them onto every device.",
"Add devices and replicate the full training state on each one.",
"Compute capacity grows while per-device model-state memory remains almost unchanged, so the same memory wall returns.",
"Partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them.",
"Four workers each keep roughly one quarter of a large moment vector rather than four complete copies, then cooperate for the update.",
"Because a worker no longer owns a complete state by itself, sharding trades redundant memory for communication and makes recovery and state ownership more complex.",
r"M_{\text{state per device}}\approx\frac{M_{\text{total state}}}{P}",
"M_total is shardable model state and P is the number of cooperating devices under an ideal balanced partition.",
"[Division](../../MATHEMATICAL_MOVES.md#division) expresses an equal share per device. Multiplication describes the failed replicated system's total cluster memory, not the amount one device must hold. [Approximation](../../MATHEMATICAL_MOVES.md#approximation) admits temporary gathers, buffers, and uneven tensors.",
[("ZeRO: Memory Optimizations Toward Training Trillion Parameter Models","https://arxiv.org/abs/1910.02054")]),
(173,"tensor-parallelism","Tensor Parallelism — Split One Matrix That No Device Can Hold","ZeRO divides training state. What if one layer's matrix and computation still cannot fit on a single device when used?",
"Sharded parameters can be gathered for computation, but the largest matrix itself becomes too large to materialize or multiply on one worker.",
"Assign whole layers to different devices and pass every activation through them sequentially.",
"One oversized layer still cannot fit, and devices responsible for later layers wait while earlier ones work.",
"Split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output.",
"Divide one vocabulary projection into four column blocks. Each device scores one quarter of the vocabulary from the same hidden state; concatenation restores the full logits.",
"Tensor parallelism introduces communication inside every layer, so a slow interconnect can erase its benefit.",
r"Y_p=XW_p,\quad Y=[Y_1,Y_2,\ldots,Y_P]",
"W is partitioned into P column blocks; every worker receives X and produces the corresponding block of output columns.",
"[Concatenation](../../MATHEMATICAL_MOVES.md#concatenation) preserves distinct output columns side by side; addition would collapse vocabulary scores that must remain separate. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) applies the same input X to each learned block, and equality states that partitioned execution matches the unsplit matrix operation.",
[("Megatron-LM","https://arxiv.org/abs/1909.08053")]),
(174,"speculative-decoding","Speculative Decoding — Let a Small Model Propose, Never Decide","The model can now be trained across devices. Why must generation still wait for one expensive target-model step per token?",
"Tensor parallelism makes one target-model step possible, but autoregressive dependence still serializes token generation.",
"Let a cheap draft model emit several tokens and return them directly.",
"Speed improves by silently replacing the trusted target distribution with a weaker model's distribution.",
"Let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling.",
"The draft proposes “the tiger sleeps.” One target call verifies all three positions; an unsupported token is rejected and sampling resumes from the corrected target distribution.",
"Speed depends on draft agreement and hardware utilization; poor proposals add work instead of removing it.",
r"a(x)=\min\left(1,\frac{p(x)}{q(x)}\right)",
"q(x) is draft probability, p(x) is target probability, and a(x) is the probability of accepting the draft token under the correction step.",
"[Division](../../MATHEMATICAL_MOVES.md#division) compares target support per unit of draft support. [Minimum](../../MATHEMATICAL_MOVES.md#minimum) caps acceptance at one because probabilities cannot exceed certainty. Simply taking max or always accepting would change the target distribution; the ratio corrects proposals that the draft overproduces.",
[("Fast Inference from Transformers via Speculative Decoding","https://proceedings.mlr.press/v202/leviathan23a.html"),("Accelerating LLM Decoding with Speculative Sampling","https://arxiv.org/abs/2302.01318")]),
(175,"modern-tiny-llm","A Modern Tiny Language Model — Assemble the Measured Engine","Can every earned repair cooperate without changing the model's responsibility or hiding its evidence?",
"Speculative decoding accelerates the final serial loop. We now have many locally useful repairs, but a pile of optimizations is not yet one reproducible model.",
"Enable every technique at once and celebrate if the program runs.",
"When quality or speed changes, no one knows which mechanism caused it; masks, precision, sharding, and caches can disagree at their boundaries.",
"Assemble the engine in dependency order, preserve a reference path, and test numerical or distributional equivalence at every boundary before accepting measured gains.",
"Train one tiny model with packed examples, RoPE, GQA, exact tiled attention, pre-RMSNorm, SwiGLU, tied embeddings, AdamW, clipping, mixed precision, accumulation, and checkpointing; then serve it with a KV cache and verified draft proposals.",
"The engine is modern, not final. New hardware, data, and observations will create new bottlenecks, and every proposed repair must re-enter the bounded loop from Excavation 150.",
None,
"This chapter assembles mechanisms rather than inventing a new numerical operation. Its arrows preserve construction order and its tests establish equivalence between optimized and reference paths.",
"[Arrows](../../MATHEMATICAL_MOVES.md#arrows) describe a causal build sequence, not equality. Each optimization keeps a reference implementation beside it because faster is acceptable only after the intended mathematical or sampling result is preserved.",
[("LLaMA: Open and Efficient Foundation Language Models","https://arxiv.org/abs/2302.13971"),("OLMo: Accelerating the Science of Language Models","https://arxiv.org/abs/2402.00838")]),
]


PURE = {
151: '''def compare(baseline, candidate): return candidate - baseline\ndef demo():\n    assert compare(2.4, 2.1) == -0.2999999999999998\n    return {"baseline": 2.4, "candidate": 2.1, "change": compare(2.4, 2.1)}''',
152: '''def profile(parts):\n    total = sum(parts.values())\n    return total, {k: v / total for k, v in parts.items()}\ndef demo():\n    total, shares = profile({"data":35,"compute":45,"communication":10,"idle":10})\n    assert total == 100 and max(shares, key=shares.get) == "compute"\n    return {"total_ms": total, "shares": shares}''',
153: '''def serial(data_ms, compute_ms): return data_ms + compute_ms\ndef overlapped(data_ms, compute_ms): return max(data_ms, compute_ms)\ndef demo():\n    assert serial(35,45) == 80 and overlapped(35,45) == 45\n    return {"serial_ms":80,"overlapped_ms":45}''',
154: '''def efficiency(lengths, rows, width): return sum(lengths)/(rows*width)\ndef first_fit(lengths, width):\n    bins=[]\n    for length in sorted(lengths, reverse=True):\n        for i, used in enumerate(bins):\n            if used+length <= width: bins[i]+=length; break\n        else: bins.append(length)\n    return bins\ndef demo():\n    bins=first_fit([6,5,3,2],8)\n    assert bins == [8,8]\n    return {"bins":bins,"efficiency":efficiency([6,5,3,2],len(bins),8)}''',
155: '''import math\ndef rotate(pair, angle):\n    x,y=pair; c,s=math.cos(angle),math.sin(angle)\n    return [c*x-s*y,s*x+c*y]\ndef demo():\n    a=rotate([1,0],0.5); b=rotate([1,0],1.0)\n    dot=sum(x*y for x,y in zip(a,b))\n    assert abs(dot-math.cos(0.5))<1e-9\n    return {"relative_match":dot}''',
156: '''def biased(score, query_pos, key_pos, slope): return score-slope*abs(query_pos-key_pos)\ndef demo():\n    assert biased(3,20,18,.1)==2.8 and biased(3,20,0,.1)==1\n    return {"near":2.8,"far":1.0}''',
157: '''def append_cache(cache, new_value): return cache+[new_value]\ndef projection_counts(length): return {"without_cache":sum(range(1,length+1)),"with_cache":length}\ndef demo():\n    counts=projection_counts(100); assert counts=={"without_cache":5050,"with_cache":100}\n    return counts''',
158: '''def cache_values(tokens, kv_heads, head_width): return tokens*kv_heads*head_width*2\ndef demo():\n    mha=cache_values(100,8,64); mqa=cache_values(100,1,64)\n    assert mha == 8*mqa\n    return {"mha_values":mha,"mqa_values":mqa}''',
159: '''def group(head, query_heads, kv_heads): return (head*kv_heads)//query_heads\ndef demo():\n    groups=[group(h,8,2) for h in range(8)]\n    assert groups==[0,0,0,0,1,1,1,1]\n    return {"groups":groups}''',
160: '''import math\ndef online_softmax(scores, block=2):\n    maximum=float("-inf"); denominator=0.0; weighted=0.0\n    for start in range(0,len(scores),block):\n        tile=scores[start:start+block]; new_max=max(maximum,max(tile))\n        scale=0.0 if maximum==float("-inf") else math.exp(maximum-new_max)\n        denominator*=scale; weighted*=scale\n        for i,s in enumerate(tile,start):\n            w=math.exp(s-new_max); denominator+=w; weighted+=w*i\n        maximum=new_max\n    return weighted/denominator\ndef demo():\n    answer=online_softmax([1,2,3,4]); assert 2.49<answer<2.51\n    return {"weighted_index":answer}''',
161: '''import math\ndef rmsnorm(values, eps=1e-8):\n    rms=math.sqrt(sum(x*x for x in values)/len(values)+eps)\n    return [x/rms for x in values]\ndef demo():\n    a=rmsnorm([3,4]); b=rmsnorm([30,40])\n    assert max(abs(x-y) for x,y in zip(a,b))<1e-8\n    return {"small":a,"scaled":b}''',
162: '''def pre_norm_block(x, branch): return [a+b for a,b in zip(x,branch)]\ndef demo():\n    x=[2.0,-1.0]; y=pre_norm_block(x,[0.0,0.0]); assert y==x\n    return {"input":x,"zero_branch_output":y}''',
163: '''import math\ndef silu(x): return x/(1+math.exp(-x))\ndef swiglu(gate, value): return [silu(g)*v for g,v in zip(gate,value)]\ndef demo():\n    out=swiglu([-10,2],[5,5]); assert out[0]<0 and out[1]>8\n    return {"gated":out}''',
164: '''def tied_logits(hidden, embeddings): return [sum(a*b for a,b in zip(hidden,row)) for row in embeddings]\ndef demo():\n    E=[[1,0],[0,1]]; logits=tied_logits([.8,.2],E); assert logits==[.8,.2]\n    return {"embedding_table":E,"logits":logits}''',
165: '''import math\ndef adam_step(theta,g,m,v,t,lr=.1,b1=.9,b2=.999,eps=1e-8):\n    m=b1*m+(1-b1)*g; v=b2*v+(1-b2)*g*g\n    mh=m/(1-b1**t); vh=v/(1-b2**t)\n    return theta-lr*mh/(math.sqrt(vh)+eps),m,v\ndef demo():\n    theta,m,v=adam_step(1,2,0,0,1); assert theta<1\n    return {"theta":theta,"m":m,"v":v}''',
166: '''import math\ndef adamw_step(theta,adam_update,lr=.1,decay=.01): return (1-lr*decay)*theta-lr*adam_update\ndef demo():\n    out=adamw_step(2,.5); assert abs(out-1.948)<1e-12\n    return {"old":2,"new":out}''',
167: '''import math\ndef clip(values,ceiling):\n    norm=math.sqrt(sum(x*x for x in values)); scale=min(1,ceiling/(norm or 1))\n    return [x*scale for x in values]\ndef demo():\n    out=clip([12,16],5); assert out==[3.0,4.0]\n    return {"clipped":out}''',
168: '''def memory_bytes(count,bits): return count*bits//8\ndef demo():\n    assert memory_bytes(1_000_000,16)==2_000_000\n    return {"fp32":memory_bytes(1_000_000,32),"fp16":memory_bytes(1_000_000,16)}''',
169: '''def scale_loss(loss,scale): return loss*scale\ndef unscale_gradient(gradient,scale): return gradient/scale\ndef demo():\n    visible=scale_loss(.000001,1000); recovered=unscale_gradient(visible,1000)\n    assert abs(recovered-.000001)<1e-15\n    return {"scaled":visible,"recovered":recovered}''',
170: '''def accumulate(gradients): return [sum(col)/len(gradients) for col in zip(*gradients)]\ndef demo():\n    out=accumulate([[2,4],[4,2],[3,3]]); assert out==[3,3]\n    return {"effective_gradient":out}''',
171: '''def checkpoint_plan(layers,segment): return list(range(0,layers,segment))\ndef demo():\n    kept=checkpoint_plan(9,3); assert kept==[0,3,6]\n    return {"layers":9,"kept":kept,"recomputed_per_segment":3}''',
172: '''def shard(items,workers): return [items[i::workers] for i in range(workers)]\ndef demo():\n    parts=shard(list(range(12)),4); assert all(len(p)==3 for p in parts)\n    return {"shards":parts}''',
173: '''def matmul(x,w): return [sum(a*b for a,b in zip(x,col)) for col in zip(*w)]\ndef split_columns(w,parts):\n    width=len(w[0]); step=width//parts\n    return [[row[i:i+step] for row in w] for i in range(0,width,step)]\ndef demo():\n    x=[2,3]; w=[[1,0,2,0],[0,1,0,2]]\n    joined=sum((matmul(x,p) for p in split_columns(w,2)),[])\n    assert joined==matmul(x,w)\n    return {"joined":joined}''',
174: '''def acceptance(target,draft): return min(1.0,target/draft)\ndef demo():\n    assert acceptance(.4,.8)==.5 and acceptance(.8,.4)==1\n    return {"overproduced":.5,"underproduced":1.0}''',
175: '''def modern_config():\n    return ["packing","rope","gqa","tiled_attention","pre_rmsnorm","swiglu","tied_embeddings","adamw","clipping","mixed_precision","accumulation","checkpointing","kv_cache","speculative_verification"]\ndef demo():\n    config=modern_config(); assert config[0]=="packing" and config[-1]=="speculative_verification"\n    return {"earned_components":config,"count":len(config)}''',
}


# These are not symbol dictionaries. Each passage lets the reader perform the
# concrete decision first; the symbols below merely name pieces already used.
DERIVATIONS = {
151: "The frozen run scores 2.4 and the candidate scores 2.1 on the same loss test. Looking at 2.1 alone cannot tell you whether anything improved. Remove the old 2.4 from the new 2.1: the remaining −0.3 is the candidate's change. We call the old measurement m_baseline, the new one m_candidate, and the remainder delta m only after doing that comparison.",
152: "Start a stopwatch with one training step. Loading ends at 35 ms; computation then carries the clock to 80; communication to 90; idle synchronization to 100. These are consecutive pieces of one elapsed interval, so you join them end to end. The name T_step is simply the final reading after T_data, T_compute, T_communication, and T_idle have all contributed.",
153: "Now give the ranger station's data loader and accelerator separate workers and start both together. Loading finishes after 35 ms, but the next step is still waiting for computation at 45 ms. The pair is ready when the slower worker finishes—not after 35+45 ms. That finishing time is what T_overlapped records; the approximation sign leaves room for pipeline startup and coordination.",
154: "Draw two rows with eight boxes each: sixteen paid positions. Place sequences of lengths 6 and 2 in the first row, then 5 and 3 in the second. All sixteen boxes now contain real tokens. To ask what share of the paid space teaches the model, put useful boxes over paid boxes: 16/16. Eta_pack is only a short name for that useful fraction.",
155: "Imagine the pair of coordinates as a clock hand beginning at [1,0]. At position one, a quarter-turn sends it to [0,1]; at position two, another quarter-turn sends it to [−1,0]. The hand's length never changes—only its angle does. Multiplying position p by the chosen turn theta tells us the total angle; the four cosine-and-sine entries record how any starting pair must contribute to its two rotated coordinates.",
156: "Suppose tiger matches one key with content score 3.0. The key is two places away, and we decide that each place should cost 0.1, so distance contributes 2×0.1=0.2. Removing that cost leaves 2.8. A key twenty places away pays 20×0.1=2.0 and keeps 1.0. We now name the original content score s_ij, the price per place m, and the adjusted result s-prime.",
157: "At token 101, write the hundred old keys on cards and compute one new card. Nothing on the old cards has changed, so combining must mean placing card 101 after cards 1 through 100—not adding their numbers together. K_1:t−1 names the ordered stack already present, k_t the one new card, and K_1:t the longer stack after appending.",
158: "Take one layer with 100 remembered tokens. If each KV head stores 64 coordinates, one head needs 100×64 coordinate slots for keys and the same again for values. Eight heads need eight copies of those slots. The three counts—tokens L, KV heads H_KV, and width d_h—multiply because every choice from one count is paired with every choice from the others.",
159: "Line up the model's eight query heads and two KV catalogs. Four consecutive query heads must point to catalog 0 and the next four to catalog 1. Scaling head number h from the eight-head range into the two-catalog range gives h×2/8; rounding down turns positions 0 through 3 into address 0 and positions 4 through 7 into address 1. The name g(h) records that address-making rule.",
160: "The model's first attention tile contains scores 1 and 4, so 4 becomes the remembered safety ceiling. The next tile contains 3 and 2; neither exceeds 4, so the ceiling remains 4. If a later tile contained 7, the ceiling would become 7 and the earlier exponential totals would be rescaled. Thus m is the largest score already processed, the s_j values are the arriving tile, and m-prime is the one maximum covering both histories.",
161: "Take the model feature pair [3,4]. Adding the raw values would let a negative feature cancel a positive one, so first turn their sizes into 9 and 16. Together they contribute 25; shared across two features that is 12.5 per feature. Its square root, about 3.54, returns to the features' ordinary units. Only now do we call this typical magnitude RMS(x) and the feature count d.",
162: "Let the residual stream carry a useful tiger signal x. The new branch examines a normalized copy and proposes a correction F(...). At initialization that proposal may be almost zero. Adding it to the untouched x lets the block say 'change nothing yet'; replacing x with the proposal would destroy the signal. The layer indices merely distinguish the stream before and after this addition.",
163: "Picture one candidate feature saying 'river-bank meaning: 5.' A separate learned gate examines this occurrence of bank. Near the river it may open close to 1, allowing almost all 5 through; near money it may close near 0, silencing that feature. This demands multiplication: zero times content must become zero. W_v creates the candidate, W_g creates gate evidence, SiLU shapes that evidence, and the circled product pairs each gate with its own feature.",
164: "The input table already contains a row pointing in the learned direction of tiger. At the output, predicting tiger means asking how strongly the final hidden state points along that same direction. Turning table rows into scoring columns changes only their orientation. E names the existing table, T marks that turn, and equality says W_out is the very same learned values—not a second copy trained to resemble them.",
165: "Follow one weight that repeatedly receives gradients near 2 and another that usually receives gradients near 0.2. A single raw step scale makes their movement differ tenfold even if each signal is ordinary for its own weight. Remember each weight's recent direction in m and its recent squared size in v; compare direction with the square root of size, then let eta choose the common overall pace. Epsilon is the tiny floor that keeps a never-touched weight from asking us to divide by zero.",
166: "Suppose two weights both equal 2, although their gradient histories differ. If decay means 'remove one tenth of one percent of the present weight this step,' both should lose the same proportion before their evidence-driven Adam movements differ. Multiplying theta by 1−eta lambda performs that direct shrink. The separate subtraction then applies Adam's learned direction, preventing gradient history from secretly changing the intended decay rule.",
167: "The model's current gradient points in a useful direction but has length 20, while this run permits length 5. The required scale is 5/20, or one quarter, so every component shrinks by one quarter and direction survives. If the next gradient has length 3, the fraction 5/3 would enlarge it—exactly what we do not want—so we cap the multiplier at 1. We call the ceiling c, the original advice g, and the safe advice g-prime.",
168: "Place one million model activation numbers in memory. At 32 bits each they occupy 32 million bits; at 16 bits each, 16 million bits. Hardware reports bytes, with eight bits in each byte, so divide either total by eight: four megabytes versus two. N counts the values, b is the chosen bits per value, and M is the resulting payload in bytes.",
169: "A true gradient of 0.000001 may vanish in half precision. Before differentiation, make the loss one thousand times larger; every loss-derived gradient becomes 0.001 and survives. Before updating the weight, divide by the same thousand and recover 0.000001. S names this temporary magnifier, L the original loss, and g the restored gradient—the model has not been told to learn a thousand times faster.",
170: "Imagine four small tables of eight examples arriving one after another. Each table gives its own average advice about the weights, but none is allowed to update yet. Add the four pieces of advice into one pending total, then share that total across the four witnesses. K counts those witnesses, g_k names one witness's advice, and g_effective is what the single optimizer step hears.",
171: "In a model chain of nine layers, keeping every activation costs nine stored boundaries. Keep only layers 0, 3, and 6; during backward work, rebuild the three missing operations inside the needed segment. For a much longer chain, choosing about the square root of L boundaries creates segments of about the same length, balancing stored checkpoints against recomputation. Big-O records this growth pattern, not an exact byte count.",
172: "Adam's moment state has twelve equal chunks and four devices are cooperating. Replication gives every device all twelve; sharding gives each device three. Asking for state per device therefore means sharing the total across P owners: total divided by P. The approximation sign remains because temporary gathers and uneven tensor sizes prevent the physical memory from being exactly that ideal share.",
173: "Split the vocabulary-scoring matrix into four column blocks. Every device receives the same hidden state X but multiplies it by only its own block W_p, producing scores Y_p for its quarter of the vocabulary. Those scores must remain distinct, so place the four blocks beside one another in vocabulary order. Adding them would collapse different tokens into the same slots. Y names the restored full score row after concatenation.",
174: "If the draft assigns tiger probability 0.8 but the target assigns 0.4, only half of those proposals have target support: 0.4/0.8=0.5. If the draft assigns 0.4 and the target 0.8, the ratio is 2, but acceptance cannot be 200 percent, so it stops at 1. The function a(x) names this capped acceptance chance for proposed token x.",
}


def chapter(row):
    n,slug,title,question,carry,attempt,broken,repair,case,limit,formula,terms,operations,refs=row
    part = ("> **PART XII — REBUILDING THE ENGINE WITHOUT BREAKING THE SYSTEM**\n>\n"
            "> The research loop is bounded. We may now improve the model—but every faster path must preserve a reference path and earn its evidence.\n\n") if n==151 else ""
    previous = f"../{n-1:03d}-{ROWS[n-152][1]}/README.md" if n>151 else "../150-bounded-self-improvement/README.md"
    next_line = (f"[Next: {ROWS[n-150][2]}](../{n+1:03d}-{ROWS[n-150][1]}/README.md)" if n<175 else
                 "The engine returns to the bounded research loop: observe, propose, test, verify, authorize, release gradually, and remain able to reverse.")
    math = ""
    if formula:
        math=f"""\n## The arithmetic we have earned

{DERIVATIONS[n]}

{terms}

### Why these operations are forced

{operations}

Only now can we compress the procedure:

$$
{formula}
$$
"""
    return f"""# Excavation {n:03d} — {title}

{part}{carry}

Perhaps we {attempt[0].lower()+attempt[1:]}

It survives until the measured run answers back. {broken}

Now the missing requirement is concrete. {repair}

## Let one run decide

{case}

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.
{math}
## What this repair cannot do

{limit}

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

{next_line}
"""


def wrap_code(source, n):
    return f'"""Excavation {n:03d}: executable evidence for the chapter.\n\nPure Python keeps every operation visible before vectorization.\n"""\n\n{source}\n\nif __name__ == "__main__":\n    print(demo())\n'


NUMPY = {
151: '''baseline=np.array([2.4, 2.3, 2.35]); candidate=np.array([2.1, 2.2, 2.15])\nchange=candidate-baseline\nassert np.all(change < 0)\nprint({"mean_change":float(change.mean())})''',
152: '''parts=np.array([35,45,10,10],dtype=float)\nshares=parts/parts.sum()\nassert parts.sum()==100 and shares.argmax()==1\nprint({"total_ms":parts.sum(),"shares":shares})''',
153: '''stages=np.array([35,45],dtype=float)\nassert stages.sum()==80 and stages.max()==45\nprint({"serial_ms":stages.sum(),"overlapped_ms":stages.max()})''',
154: '''lengths=np.array([6,5,3,2]); rows=np.array([[6,2],[5,3]])\nefficiency=lengths.sum()/(rows.shape[0]*8)\nassert efficiency==1\nprint({"packed_rows":rows,"efficiency":efficiency})''',
155: '''angles=np.array([.5,1.0]); c=np.cos(angles); s=np.sin(angles)\nrotated=np.stack([c,s],axis=1)\nmatch=rotated[0]@rotated[1]\nassert np.allclose(match,np.cos(.5))\nprint({"relative_match":match})''',
156: '''scores=np.array([3.,3.]); distances=np.array([2.,20.])\nadjusted=scores-.1*distances\nassert np.allclose(adjusted,[2.8,1.])\nprint({"adjusted_scores":adjusted})''',
157: '''cache=np.arange(6).reshape(3,2); new=np.array([[6,7]])\ncache=np.concatenate([cache,new],axis=0)\nassert cache.shape==(4,2) and np.array_equal(cache[-1],new[0])\nprint({"cache":cache})''',
158: '''tokens,head_width=100,64\nkv=np.array([8,1])*tokens*head_width*2\nassert kv[0]==8*kv[1]\nprint({"mha_values":kv[0],"mqa_values":kv[1]})''',
159: '''heads=np.arange(8); groups=np.floor(heads*2/8).astype(int)\nassert np.array_equal(groups,[0,0,0,0,1,1,1,1])\nprint({"groups":groups})''',
160: '''scores=np.array([1.,2.,3.,4.]); ordinary=np.exp(scores-scores.max()); ordinary/=ordinary.sum()\nblocks=[]\nfor tile in np.array_split(scores,2): blocks.append(tile)\nseen=np.concatenate(blocks); online=np.exp(seen-seen.max()); online/=online.sum()\nassert np.allclose(ordinary,online)\nprint({"probabilities":online})''',
161: '''x=np.array([[3.,4.],[30.,40.]])\ny=x/np.sqrt(np.mean(x*x,axis=1,keepdims=True)+1e-8)\nassert np.allclose(y[0],y[1])\nprint({"normalized":y})''',
162: '''x=np.array([2.,-1.]); branch=np.zeros_like(x); y=x+branch\nassert np.array_equal(x,y)\nprint({"identity_path":y})''',
163: '''gate=np.array([-10.,2.]); value=np.array([5.,5.]); silu=gate/(1+np.exp(-gate)); out=silu*value\nassert out[0]<0 and out[1]>8\nprint({"gated":out})''',
164: '''E=np.array([[1.,0.],[0.,1.]]); hidden=np.array([.8,.2]); logits=hidden@E.T\nassert np.allclose(logits,[.8,.2])\nprint({"logits_from_tied_table":logits})''',
165: '''g=np.array([2.,.2]); m=.1*g; v=.001*g*g; mh=m/(1-.9); vh=v/(1-.999); step=mh/(np.sqrt(vh)+1e-8)\nassert np.allclose(step,[1.,1.],atol=1e-6)\nprint({"raw_gradient":g,"adapted_step":step})''',
166: '''theta=np.array([2.,-1.]); adam_update=np.array([.5,-.25]); out=(1-.1*.01)*theta-.1*adam_update\nassert np.all(np.abs(out)<np.abs(theta))\nprint({"decoupled_update":out})''',
167: '''g=np.array([12.,16.]); scale=min(1.,5./np.linalg.norm(g)); clipped=g*scale\nassert np.allclose(clipped,[3.,4.])\nprint({"clipped":clipped})''',
168: '''a=np.ones(1_000_000,dtype=np.float32); b=a.astype(np.float16)\nassert b.nbytes==a.nbytes//2\nprint({"fp32_bytes":a.nbytes,"fp16_bytes":b.nbytes})''',
169: '''loss=np.float16(1e-6); scale=np.float16(1000); visible=np.float16(loss*scale); recovered=np.float32(visible)/np.float32(scale)\nassert visible>loss\nprint({"scaled":visible,"recovered":recovered})''',
170: '''micro=np.array([[2.,4.],[4.,2.],[3.,3.]])\neffective=micro.mean(axis=0)\nassert np.allclose(effective,[3.,3.])\nprint({"effective_gradient":effective})''',
171: '''layers=np.arange(9); kept=layers[::3]; recomputed=np.setdiff1d(layers,kept)\nassert np.array_equal(kept,[0,3,6])\nprint({"kept":kept,"recomputed":recomputed})''',
172: '''state=np.arange(12); shards=np.array_split(state,4)\nassert all(len(s)==3 for s in shards)\nprint({"shards":shards})''',
173: '''x=np.array([2.,3.]); W=np.array([[1,0,2,0],[0,1,0,2]],dtype=float); blocks=np.hsplit(W,2); joined=np.concatenate([x@b for b in blocks])\nassert np.allclose(joined,x@W)\nprint({"joined":joined})''',
174: '''target=np.array([.4,.8]); draft=np.array([.8,.4]); acceptance=np.minimum(1.,target/draft)\nassert np.allclose(acceptance,[.5,1.])\nprint({"acceptance":acceptance})''',
175: '''reference=np.array([.2,.3,.5]); optimized=np.array([.2,.3,.5]); error=np.max(np.abs(reference-optimized))\nassert error==0\nprint({"equivalence_error":error,"components":14})''',
}


TORCH = {
151: '''baseline=torch.tensor([2.4,2.3,2.35]); candidate=torch.tensor([2.1,2.2,2.15]); change=candidate-baseline\nassert torch.all(change<0); print({"mean_change":change.mean().item()})''',
152: '''parts=torch.tensor([35.,45.,10.,10.]); shares=parts/parts.sum()\nassert parts.sum()==100 and shares.argmax()==1; print({"total_ms":parts.sum().item(),"shares":shares})''',
153: '''stages=torch.tensor([35.,45.]); print({"serial_ms":stages.sum().item(),"overlapped_ms":stages.max().item()})''',
154: '''lengths=torch.tensor([6.,5.,3.,2.]); efficiency=lengths.sum()/(2*8)\nassert efficiency==1; print({"efficiency":efficiency.item()})''',
155: '''angles=torch.tensor([.5,1.]); rotated=torch.stack([torch.cos(angles),torch.sin(angles)],dim=1); match=rotated[0]@rotated[1]\nassert torch.allclose(match,torch.cos(torch.tensor(.5))); print({"relative_match":match.item()})''',
156: '''scores=torch.tensor([3.,3.]); distances=torch.tensor([2.,20.]); adjusted=scores-.1*distances\nassert torch.allclose(adjusted,torch.tensor([2.8,1.])); print({"adjusted_scores":adjusted})''',
157: '''cache=torch.arange(6).reshape(3,2); new=torch.tensor([[6,7]]); cache=torch.cat([cache,new])\nassert cache.shape==(4,2); print({"cache":cache})''',
158: '''kv=torch.tensor([8,1])*100*64*2\nassert kv[0]==8*kv[1]; print({"mha_values":kv[0].item(),"mqa_values":kv[1].item()})''',
159: '''heads=torch.arange(8); groups=torch.floor(heads*2/8).long()\nassert torch.equal(groups,torch.tensor([0,0,0,0,1,1,1,1])); print({"groups":groups})''',
160: '''scores=torch.tensor([1.,2.,3.,4.]); reference=torch.softmax(scores,0); tiles=torch.chunk(scores,2); rebuilt=torch.softmax(torch.cat(tiles),0)\nassert torch.allclose(reference,rebuilt); print({"probabilities":rebuilt})''',
161: '''x=torch.tensor([[3.,4.],[30.,40.]]); y=x*torch.rsqrt((x*x).mean(-1,keepdim=True)+1e-8)\nassert torch.allclose(y[0],y[1]); print({"normalized":y})''',
162: '''x=torch.tensor([2.,-1.],requires_grad=True); y=x+torch.zeros_like(x); y.sum().backward()\nassert torch.equal(x.grad,torch.ones_like(x)); print({"identity_gradient":x.grad})''',
163: '''gate=torch.tensor([-10.,2.]); value=torch.tensor([5.,5.]); out=torch.nn.functional.silu(gate)*value\nassert out[0]<0 and out[1]>8; print({"gated":out})''',
164: '''E=torch.tensor([[1.,0.],[0.,1.]],requires_grad=True); hidden=torch.tensor([.8,.2]); logits=hidden@E.T; logits.sum().backward()\nassert E.grad is not None; print({"logits":logits,"shared_table_gradient":E.grad})''',
165: '''theta=torch.nn.Parameter(torch.tensor([1.])); opt=torch.optim.Adam([theta],lr=.1); (theta**2).backward(); opt.step()\nassert theta.item()<1; print({"theta":theta.item()})''',
166: '''theta=torch.nn.Parameter(torch.tensor([2.])); opt=torch.optim.AdamW([theta],lr=.1,weight_decay=.01); (theta*.5).backward(); opt.step()\nassert theta.item()<2; print({"theta":theta.item()})''',
167: '''p=torch.nn.Parameter(torch.zeros(2)); p.grad=torch.tensor([12.,16.]); before=p.grad.norm(); torch.nn.utils.clip_grad_norm_([p],5.); after=p.grad.norm()\nassert torch.allclose(after,torch.tensor(5.)); print({"before":before.item(),"after":after.item()})''',
168: '''fp32=torch.ones(1_000_000,dtype=torch.float32); fp16=fp32.half()\nassert fp16.element_size()==fp32.element_size()//2; print({"fp32_bytes":fp32.nelement()*fp32.element_size(),"fp16_bytes":fp16.nelement()*fp16.element_size()})''',
169: '''x=torch.tensor([1e-3],requires_grad=True); scale=1000.; scaled=(x*x)*scale; scaled.backward(); recovered=x.grad/scale\nassert torch.allclose(recovered,torch.tensor([2e-3])); print({"scaled_gradient":x.grad,"recovered":recovered})''',
170: '''micro=torch.tensor([[2.,4.],[4.,2.],[3.,3.]]); effective=micro.mean(0)\nassert torch.equal(effective,torch.tensor([3.,3.])); print({"effective_gradient":effective})''',
171: '''from torch.utils.checkpoint import checkpoint\nx=torch.tensor([2.],requires_grad=True)\ndef block(v): return v*v+1\ny=checkpoint(block,x,use_reentrant=False); y.backward(); assert x.grad.item()==4; print({"output":y.item(),"recomputed_gradient":x.grad.item()})''',
172: '''state=torch.arange(12); shards=torch.chunk(state,4)\nassert all(s.numel()==3 for s in shards); print({"shards":shards})''',
173: '''x=torch.tensor([2.,3.]); W=torch.tensor([[1,0,2,0],[0,1,0,2]],dtype=torch.float32); blocks=torch.chunk(W,2,dim=1); joined=torch.cat([x@b for b in blocks])\nassert torch.equal(joined,x@W); print({"joined":joined})''',
174: '''target=torch.tensor([.4,.8]); draft=torch.tensor([.8,.4]); acceptance=torch.minimum(torch.ones(2),target/draft)\nassert torch.allclose(acceptance,torch.tensor([.5,1.])); print({"acceptance":acceptance})''',
175: '''reference=torch.tensor([.2,.3,.5]); optimized=reference.clone(); error=(reference-optimized).abs().max()\nassert error==0; print({"equivalence_error":error.item(),"components":14})''',
}


DIAGRAMS = {
151: '''```mermaid\nflowchart LR\n    B1["Baseline run: seed 7"] --> M1["Held-out loss: 2.4"]\n    B2["Exact rerun: seed 7"] --> M2["Held-out loss: 2.4"]\n    C["One named change"] --> M3["Candidate loss: 2.1"]\n    M1 --> D["Comparable difference: -0.3"]\n    M3 --> D\n```\n\n```text\nfixed world + one change -> attributable evidence\n```''',
152: '''```mermaid\npie showData\n    title One 100 ms training step\n    "Load data" : 35\n    "Compute" : 45\n    "Communicate" : 10\n    "Idle" : 10\n```\n\n```text\n0 ms |---data 35---|-----compute 45-----|-comm 10-|-idle 10-| 100 ms\n```''',
153: '''```mermaid\nsequenceDiagram\n    participant Loader\n    participant Accelerator\n    Loader->>Loader: prepare batch 2\n    par while batch 2 loads\n        Accelerator->>Accelerator: compute batch 1\n    end\n    Loader->>Accelerator: batch 2 ready\n```\n\n```text\nserial:  [load 35][compute 45] = 80 ms\noverlap: [load 35]\n         [compute 45]          = 45 ms steady state\n```''',
154: '''```mermaid\nflowchart TB\n    subgraph Padded["Two padded rows, width 8"]\n      P1["6 real + 2 empty"]\n      P2["5 real + 3 empty"]\n    end\n    subgraph Packed["Two packed rows, width 8"]\n      K1["6 + 2 real"]\n      K2["5 + 3 real"]\n    end\n    Padded -->|"move examples; preserve masks"| Packed\n```\n\n```text\nbefore: T T T T T T _ _   T T T T T _ _ _\nafter:  T T T T T T T T   T T T T T T T T\n```''',
155: '''```mermaid\nflowchart LR\n    V["same pair [1, 0]"] --> P1["position 1: rotate θ"]\n    V --> P2["position 2: rotate 2θ"]\n    P1 --> R["dot product sees angle difference θ"]\n    P2 --> R\n```\n\n```text\nposition 0:  ->\nposition 1:  ↑\nposition 2:  <-     length stays fixed; angle carries position\n```''',
156: '''```mermaid\nflowchart LR\n    S["content score 3.0"] --> N["near: 2 places × 0.1"]\n    S --> F["far: 20 places × 0.1"]\n    N --> AN["adjusted 2.8"]\n    F --> AF["adjusted 1.0"]\n```\n\n```text\ncontent may overcome distance, but distance now has a predictable price\n```''',
157: '''```mermaid\nsequenceDiagram\n    participant Past as Cached positions 1..100\n    participant New as Token 101\n    participant Attention\n    New->>New: compute k101, v101 once\n    Past->>Attention: reuse cached K,V\n    New->>Attention: append new K,V\n    Attention-->>New: context for token 101\n```\n\n```text\nwithout cache: 1 + 2 + ... + 100 projections\nwith cache:    1 new projection at each step\n```''',
158: '''```mermaid\nflowchart TB\n    subgraph MHA["8 query heads: 8 KV histories"]\n      M["K1 V1 | K2 V2 | ... | K8 V8"]\n    end\n    subgraph MQA["8 query heads: 1 shared KV history"]\n      Q["Q1 Q2 ... Q8"] --> K["one K,V catalog"]\n    end\n    MHA -->|"remove repeated catalogs"| MQA\n```\n\n```text\ncache width: 8 heads -> 1 head\n```''',
159: '''```mermaid\nflowchart LR\n    Q0["Q0 Q1 Q2 Q3"] --> KV0["KV group 0"]\n    Q1["Q4 Q5 Q6 Q7"] --> KV1["KV group 1"]\n```\n\n```text\nMQA:  8 queries -> 1 catalog\nGQA:  8 queries -> 2 catalogs\nMHA:  8 queries -> 8 catalogs\n```''',
160: '''```mermaid\nflowchart LR\n    T1["score tile 1"] --> O["running max + denominator + value total"]\n    T2["score tile 2"] --> O\n    T3["score tile 3"] --> O\n    O --> A["exact attention output"]\n    X["full n×n score matrix"]:::gone\n    classDef gone stroke-dasharray: 5 5,fill:#eee,color:#777\n```\n\n```text\nslow memory: never stores the whole score square\nfast memory: one tile + three running summaries\n```''',
161: '''```mermaid\nflowchart LR\n    X["features: 3, 4"] --> S["squares: 9, 16"]\n    S --> A["mean square: 12.5"]\n    A --> R["root: 3.54"]\n    R --> N["divide features by 3.54"]\n```\n\n```text\n[3,4] and [30,40] -> same normalized direction\n```''',
162: '''```mermaid\nflowchart LR\n    X["residual x"] --> ADD(("+"))\n    X --> N["RMSNorm"] --> F["changing branch F"] --> ADD\n    ADD --> Y["next residual"]\n```\n\n```text\nidentity highway: x --------------------> +\nchanging branch: x -> norm -> F --------> +\n```''',
163: '''```mermaid\nflowchart LR\n    X["token state x"] --> G["gate path Wg + SiLU"]\n    X --> V["value path Wv"]\n    G --> MUL(("× coordinate by coordinate"))\n    V --> MUL\n    MUL --> O["selected private features"]\n```\n\n```text\nclosed gate 0 × content 5 = 0\nopen gate   1 × content 5 = 5\n```''',
164: '''```mermaid\nflowchart TB\n    E["one embedding table E"] --> IN["rows read token meanings"]\n    E --> T["transpose"] --> OUT["columns score token predictions"]\n```\n\n```text\nenter "tiger": read tiger row\npredict "tiger": align with that same row turned into a column\n```''',
165: '''```mermaid\nflowchart LR\n    G1["weight A: gradients near 2"] --> M1["large recent scale"] --> S1["normalized step"]\n    G2["weight B: gradients near 0.2"] --> M2["small recent scale"] --> S2["normalized step"]\n    ETA["global pace η"] --> S1\n    ETA --> S2\n```\n\n```text\nraw size differs -> each weight compares advice with its own history\n```''',
166: '''```mermaid\nflowchart LR\n    OLD["old weight"] --> DECAY["direct proportional shrink"] --> JOIN["new weight"]\n    DATA["loss gradient"] --> ADAM["adaptive Adam step"] --> JOIN\n```\n\n```text\nweight decay answers: how much smaller should the weight be?\nAdam answers: what did the data ask it to change?\n```''',
167: '''```mermaid\nflowchart TD\n    G["gradient length"] --> Q{"above ceiling 5?"}\n    Q -->|"no: length 3"| KEEP["multiplier 1"]\n    Q -->|"yes: length 20"| SCALE["multiplier 5/20"]\n    KEEP --> OUT["direction preserved"]\n    SCALE --> OUT\n```\n\n```text\n[12,16] length 20 -> × 1/4 -> [3,4] length 5\n```''',
168: '''```mermaid\nflowchart LR\n    N["1,000,000 activations"] --> F32["32 bits each = 4 MB"]\n    N --> F16["16 bits each = 2 MB"]\n    F16 --> MASTER["sensitive master state remains 32-bit"]\n```\n\n```text\nbulk arithmetic: narrow   |   fragile accumulation: wide\n```''',
169: '''```mermaid\nflowchart LR\n    L["tiny loss signal"] --> S["× scale before backward"] --> B["representable gradient"]\n    B --> U["÷ same scale"] --> G["original gradient"]\n```\n\n```text\n0.000001 -> ×1000 -> 0.001 -> survive -> ÷1000 -> 0.000001\n```''',
170: '''```mermaid\nsequenceDiagram\n    participant M as Gradient memory\n    participant O as Optimizer\n    loop four micro-batches\n        M->>M: add unscaled gradient; do not update\n    end\n    M->>O: divide accumulated advice by 4\n    O->>O: take one optimizer step\n```\n\n```text\n8 + 8 + 8 + 8 examples -> one effective batch of 32\n```''',
171: '''```mermaid\nflowchart LR\n    C0["keep layer 0"] --> R1["recompute 1,2"] --> C3["keep layer 3"]\n    C3 --> R2["recompute 4,5"] --> C6["keep layer 6"]\n    C6 --> R3["recompute 7,8"] --> L9["layer 9"]\n```\n\n```text\nstored:      0       3       6\nrecomputed:    1 2     4 5     7 8\n```''',
172: '''```mermaid\nflowchart TB\n    STATE["optimizer state: 12 chunks"] --> D0["device 0: chunks 0-2"]\n    STATE --> D1["device 1: chunks 3-5"]\n    STATE --> D2["device 2: chunks 6-8"]\n    STATE --> D3["device 3: chunks 9-11"]\n```\n\n```text\nreplication: 12 + 12 + 12 + 12\nsharding:     3 +  3 +  3 +  3\n```''',
173: '''```mermaid\nflowchart LR\n    X["same hidden state X"] --> D0["X × W0"]\n    X --> D1["X × W1"]\n    X --> D2["X × W2"]\n    X --> D3["X × W3"]\n    D0 --> CAT["concatenate vocabulary columns"]\n    D1 --> CAT\n    D2 --> CAT\n    D3 --> CAT\n```\n\n```text\n[quarter logits][quarter logits][quarter logits][quarter logits] -> full logits\n```''',
174: '''```mermaid\nsequenceDiagram\n    participant D as Draft model\n    participant T as Target model\n    participant S as Sampler\n    D->>T: propose several tokens\n    T->>T: score all proposed positions in one pass\n    T->>S: corrected accept/reject probabilities\n    S-->>D: keep accepted prefix; repair first rejection\n```\n\n```text\ndraft may propose quickly; target remains the distributional authority\n```''',
175: '''```mermaid\nflowchart LR\n    B["frozen baseline"] --> D["packed deterministic data"] --> A["RoPE + GQA + tiled exact attention"]\n    A --> K["pre-RMSNorm + SwiGLU + tied words"] --> O["AdamW + clipping + safe precision"]\n    O --> S["checkpointed and sharded training"] --> I["KV cache + verified draft serving"]\n    I --> E["equivalence and quality gates"]\n    E -->|"failure"| B\n```\n\n```text\nno speedup enters the engine without a reference result beside it\n```''',
}


def numpy_code(n):
    return f'''"""Excavation {n:03d}: NumPy implementation of this chapter's repair."""\nimport numpy as np\n\n{NUMPY[n]}\n'''


def torch_code(n):
    return f'''"""Excavation {n:03d}: PyTorch implementation of this chapter's repair."""\ntry:\n    import torch\nexcept ImportError:\n    raise SystemExit("Install PyTorch to run this stage.")\n\n{TORCH[n]}\n'''


def main():
    for row in ROWS:
        n,slug,title,question,carry,attempt,broken,repair,case,limit,formula,terms,operations,refs=row
        folder=ROOT/"excavations"/f"{n:03d}-{slug}"
        (folder/"implementation").mkdir(parents=True,exist_ok=True)
        (folder/"images").mkdir(exist_ok=True)
        (folder/"README.md").write_text(chapter(row))
        (folder/"mistakes.md").write_text(f"# Mistakes — Excavation {n:03d}\n\n## Tempting idea\n\n{attempt}\n\n## Evidence that breaks it\n\n{broken}\n\n## Requirement carried forward\n\n{repair}\n\nA wrong idea belongs here because its failure exposes information the successful design must preserve.\n")
        (folder/"diagram.md").write_text(f"# Diagram — {title}\n\n{DIAGRAMS[n]}\n")
        (folder/"exercises.md").write_text(f'''# Invention Exercises — Excavation {n:03d}

1. Reconstruct the tempting design without using the chapter's accepted name: {attempt}
2. Create the smallest measurement that reveals this failure: {broken}
3. Explain why the chosen arithmetic operation answers the job and why its nearest alternative does not.
4. Change one number in the worked run, predict every intermediate result, and only then run `implementation/pure_python.py`.
5. Invent a deployment where this limitation matters: {limit}
''')
        ref_lines="\n".join(f"- [{name}]({url}) — primary source for the mechanism or measured bottleneck reconstructed here." for name,url in refs)
        (folder/"references.md").write_text(f"# Primary Research Trail — {title}\n\n{ref_lines}\n\nRead the chapter first. Use these sources to inspect evidence, assumptions, and limitations after the problem has made their terminology meaningful.\n")
        (folder/"images"/"README.md").write_text(f"# Visual Brief — {title}\n\nDraw the same tiny run in two panels. The first panel must make the wasted time, memory, information, or stability visible. The second may reveal the repair only after the reader can point to that waste. Preserve the recurring ranger-station model rather than introducing unrelated abstract boxes.\n")
        (folder/"implementation"/"README.md").write_text(f"# Build Excavation {n:03d} Three Times\n\n1. [`pure_python.py`](pure_python.py) exposes the chapter's mechanism with ordinary values, lists, and loops.\n2. [`numpy.py`](numpy.py) turns the same before/after measurement into arrays.\n3. [`pytorch.py`](pytorch.py) keeps the comparison differentiable for integration into a trainable system.\n\nRun the Pure Python stage first and explain its result before using either library.\n")
        (folder/"implementation"/"pure_python.py").write_text(wrap_code(PURE[n],n))
        (folder/"implementation"/"numpy.py").write_text(numpy_code(n))
        (folder/"implementation"/"pytorch.py").write_text(torch_code(n))
    print("Built Excavations 151–175 with narrative, companions, and three implementation stages.")

if __name__=="__main__": main()
