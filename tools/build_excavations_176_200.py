"""Build Part XIII as one accountable language-model pretraining run."""
from pathlib import Path

ROOT = Path(__file__).parents[1]

# number, slug, title, carry, attempt, failure, repair, case, limit,
# formula, term explanation, operation explanation, primary references
ROWS = [
(176,"corpus-manifest","A Corpus Manifest — Know What Entered the Run",
"The modern tiny language-model engine preserves a reference path through training and serving. It still cannot explain which documents will shape its weights, because no corpus has been frozen as part of the experiment.",
"copy every available text file into one large folder and begin tokenizing",
"A file is replaced upstream, another is silently skipped, and a third appears twice under different paths. The same training command now describes a different body of evidence.",
"Create an immutable manifest that records each source, version, content hash, license or usage basis, processing stage, and document count before any training shard exists.",
"The ranger station records `field-reports/v3`, its retrieval date, 8,412 documents, and the hash of its manifest. A later run can prove whether it used the same evidence.",
"A manifest makes the corpus accountable; it cannot prove that every recorded document is suitable, lawful, accurate, or harmless.",
None,
"This chapter earns a ledger rather than a new numerical compression.",
"[Sets and membership](../../MATHEMATICAL_MOVES.md#membership) help describe what belongs to a corpus, but the discovery is the provenance procedure itself.",
[("Datasheets for Datasets","https://arxiv.org/abs/1803.09010"),("Dolma","https://arxiv.org/abs/2402.00159")]),
(177,"document-boundaries","Document Boundaries — Keep One Story from Leaking into Another",
"The manifest fixes which source documents belong to the run. Tokenization can still concatenate them into a stream where the ending of one document predicts the beginning of an unrelated one.",
"join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width",
"A ranger report ending with “tiger tracks near” is trained to predict the first word of an unrelated software license. The model receives a relationship that never existed in either document.",
"Mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended.",
"Two short documents share one packed row, but a boundary mask lets each token read only tokens from its own document. The empty hardware space is saved without inventing a false continuation.",
"Boundary isolation prevents accidental cross-document lessons; it cannot decide whether two paragraphs really belong to the same source document.",
r"A_{ij}=\begin{cases}1&\text{tokens }i,j\text{ share a document}\\0&\text{otherwise}\end{cases}",
"A_ij answers one concrete yes-or-no question for token positions i and j: may information cross between them? One means the pair shares a document; zero means the boundary forbids the connection.",
"[Cases](../../MATHEMATICAL_MOVES.md#cases) are forced because same-document and cross-document pairs obey different rules. [Equality](../../MATHEMATICAL_MOVES.md#equals) assigns an exact permission bit. A distance score would blur a categorical boundary, while addition would invent partial permission.",
[("Efficient Sequence Packing without Cross-contamination","https://arxiv.org/abs/2107.02027"),("Dolma","https://arxiv.org/abs/2402.00159")]),
(178,"language-identification","Language Identification — Do Not Confuse Familiar Script with Familiar Language",
"Document boundaries now preserve honest local context. The manifest still mixes languages, code, names, and corrupted text, so a declared English run cannot yet tell what language evidence it actually contains.",
"keep documents containing mostly familiar Latin characters and discard the rest",
"Spanish and Vietnamese are mistaken for English, transliterated languages disappear, and English code or identifier lists pass despite containing little natural language.",
"Use a calibrated language classifier, retain its confidence and model version, and route uncertain documents to an explicit unknown bucket rather than forcing a label.",
"A field report receives English 0.93, Spanish 0.05, and unknown 0.02. The pipeline keeps English only because its score clears the recorded threshold; a 0.44/0.41 split is quarantined.",
"Because the classifier learned from finite examples and reduces a mixed document to one distribution, language identification remains probabilistic and domain-sensitive; short, multilingual, and code-heavy documents are especially difficult.",
r"\ell^*=\underset{\ell\in\mathcal L}{\mathrm{argmax}}\ p(\ell\mid d)",
"d is the document being inspected; the set L contains allowed language labels; p(l|d) is the classifier's support for one label; l-star is the label whose support is largest.",
"[Conditional probability](../../MATHEMATICAL_MOVES.md#conditional-bar) asks for language support given this document. [Arg max](../../MATHEMATICAL_MOVES.md#arg-max) keeps the winning label rather than only its score. Summing the scores would erase which language produced them; a threshold is still checked afterward because the winner may be weak.",
[("CCNet","https://arxiv.org/abs/1911.00359"),("Language Identification and Beyond with FastText","https://arxiv.org/abs/1607.01759")]),
(179,"exact-deduplication","Exact Deduplication — Stop Paying Twice for the Same Document",
"Language labels make the intended corpus measurable. Counting the accepted files now reveals identical reports mirrored across archives and repeated under new filenames.",
"leave duplicates in place because more training examples should always help",
"One press release copied to a thousand sites receives a thousand votes, while a rare field observation receives one. Compute is spent memorizing repetition rather than encountering new evidence.",
"Normalize only irrelevant formatting, hash the resulting document, and keep one accountable representative for each identical hash while preserving duplicate counts in the ledger.",
"Three files differ only in line endings and trailing spaces. After recorded normalization they produce the same fingerprint, so one enters training and the manifest records three original locations.",
"Because a cryptographic hash reacts to any retained content change, exact hashes catch identical normalized text but give a copied article with one inserted advertisement a different fingerprint.",
r"h(d)=H(N(d))",
"d is the original tiger field-report document, N performs the recorded normalization, H is a deterministic content-hash function, and h(d) is the fingerprint used to group exact copies.",
"[Function composition](../../MATHEMATICAL_MOVES.md#function-composition) fixes the order: normalize first, hash second. Reversing the order leaves irrelevant byte differences visible. [Equality](../../MATHEMATICAL_MOVES.md#equals) groups only matching fingerprints; adding hashes has no interpretation and would not identify copies.",
[("Deduplicating Training Data Makes Language Models Better","https://arxiv.org/abs/2107.06499"),("CCNet","https://arxiv.org/abs/1911.00359")]),
(180,"near-deduplication","Near Deduplication — When a Copy Changes a Few Words",
"Exact deduplication removes byte-equivalent documents. The copied article with a new banner, reordered footer, or one edited sentence still survives as apparently new evidence.",
"lowercase both documents and demand that every remaining word match",
"One inserted advertisement defeats the rule, while independently written short notices can match by accident. Exact sequence equality is too brittle for disguised copies.",
"Represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale.",
"The original report has ten shingles; its mirrored copy shares eight and introduces two. Their intersection has eight shingles and their union has twelve, giving similarity 8/12 rather than pretending the documents are either perfectly equal or wholly unrelated.",
"Near-deduplication depends on shingle size and threshold; aggressive settings can erase legitimate quotations, templates, or independent accounts.",
r"J(A,B)=\frac{\lvert A\cap B\rvert}{\lvert A\cup B\rvert}",
"A and B are the shingle sets from the original tiger report and its edited mirror. Their intersection counts phrases both contain; their union counts every distinct phrase appearing in either; J is the shared fraction.",
"[Intersection](../../MATHEMATICAL_MOVES.md#intersection) keeps shared evidence and [union](../../MATHEMATICAL_MOVES.md#union) defines the total distinct evidence available. [Cardinality](../../MATHEMATICAL_MOVES.md#cardinality) turns each set into a count. [Division](../../MATHEMATICAL_MOVES.md#division) makes the overlap comparable across document lengths; a raw shared count would favor long documents.",
[("Deduplicating Training Data Makes Language Models Better","https://arxiv.org/abs/2107.06499"),("On the Resemblance and Containment of Documents","https://doi.org/10.1109/SEQUEN.1997.666900")]),
(181,"quality-filtering","Quality Filtering — Remove Noise Without Defining Humanity Away",
"Near-deduplication leaves a corpus with more distinct documents, not necessarily better ones. Some are navigation fragments, keyword piles, machine corruption, or adversarial spam.",
"keep only documents that resemble one prestigious encyclopedia",
"The filter removes spam, but it also suppresses informal dialect, local knowledge, code, dialogue, and communities whose writing differs from the chosen reference.",
"Combine transparent structural signals with small controlled model-based tests, inspect what each threshold removes, and publish source-by-source retention counts before accepting a filter.",
"The station rejects a page with 70 percent repeated navigation and no sentences, but manually audits samples near the threshold and notices that short emergency bulletins need a different rule from essays.",
"Every quality filter encodes values and domain assumptions; measured downstream gains do not prove that excluded voices were unimportant.",
None,
"The chapter uses a decision record because collapsing several value judgments into one unexplained score would hide rather than clarify them.",
"[Weighted sums](../../MATHEMATICAL_MOVES.md#weighted-sum) can combine inspected signals, but no weight becomes morally neutral merely because it appears in arithmetic.",
[("DataComp-LM","https://arxiv.org/abs/2406.11794"),("CCNet","https://arxiv.org/abs/1911.00359")]),
(182,"data-provenance","Data Provenance — Keep the Path Back to Every Source",
"Quality filtering produces an accepted set and a rejected set. Without a trace through each transformation, neither set can explain how a source document reached its decision.",
"save only the final cleaned text because intermediate metadata costs storage",
"A rights request, filtering bug, or benchmark contamination report arrives, but the final shard cannot be mapped back to the source record or processing rule that produced it.",
"Assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard.",
"Document `river-0042` points to its source URL, retrieval time, raw hash, language decision, duplicate cluster, quality audit, redaction record, and final shard offset.",
"Provenance makes decisions inspectable; it cannot repair a source that was collected without sufficient rights, consent, or context.",
None,
"The discovery is a lineage graph whose edges carry named transformations and versions.",
"[Arrows](../../MATHEMATICAL_MOVES.md#arrows) represent transformation history, not equality. Replacing the graph with a flat list would lose which output came from which input.",
[("Datasheets for Datasets","https://arxiv.org/abs/1803.09010"),("Dolma","https://arxiv.org/abs/2402.00159")]),
(183,"pii-redaction","PII Redaction — Do Not Turn Accidental Secrets into Lessons",
"Provenance can locate every retained document. Inspection now finds phone numbers, email addresses, account identifiers, and private-looking text embedded in otherwise useful pages.",
"remove any entire document containing a sequence that resembles personal information",
"One phone number erases a long public safety guide, while obfuscated addresses and context-dependent identifiers still pass. The rule destroys useful evidence without reliably removing the risky span.",
"Detect candidate spans with several methods, classify them in context, replace confirmed sensitive spans with typed placeholders, and preserve only a restricted audit record of the decision.",
"The sentence “Call Maya at 555-0142 about the injured tiger” becomes “Call [PERSON] at [PHONE] about the injured tiger”; the grammatical lesson survives while the direct identifier does not.",
"Redaction has false positives and false negatives, and public availability does not by itself settle privacy, consent, or appropriate use.",
None,
"This chapter earns a risk-reduction workflow rather than a promise that one regular expression can define privacy.",
"[Replacement](../../MATHEMATICAL_MOVES.md#replacement) preserves surrounding structure while removing a risky span; deletion of the whole document would discard unrelated evidence.",
[("Extracting Training Data from Large Language Models","https://arxiv.org/abs/2012.07805"),("Dolma","https://arxiv.org/abs/2402.00159")]),
(184,"data-mixtures","Data Mixtures — Decide Which Worlds Receive a Voice",
"Redaction reduces one preventable privacy risk. The clean sources still differ enormously in size: web pages could drown out books, code, science, and the station's rare field reports.",
"concatenate every accepted source and let its raw token count determine how often it appears",
"The largest crawl silently becomes the curriculum. A source ten thousand times smaller may almost never reach a batch even when it carries relationships absent from the web.",
"Choose and publish a probability weight for each domain, treating the mixture as an explicit modeling decision that must be tested on per-domain validation streams.",
"The station assigns 0.50 to curated web text, 0.20 to science, 0.15 to code, 0.10 to books, and 0.05 to field reports. The five shares exhaust one draw without pretending the sources are equally large or equally important.",
"Mixture weights redistribute attention but cannot make a poor or missing domain representative, accurate, or safe.",
r"\sum_{d=1}^{D}w_d=1,\quad w_d\ge 0",
"D counts the named data domains and w_d is the chance that the next training draw chooses domain d. Nonnegative weights prevent negative sampling; a total of one exhausts all possible domain choices.",
"[Summation](../../MATHEMATICAL_MOVES.md#summation) combines mutually exclusive domain shares into the whole probability mass. Multiplication would make one zero-weight domain erase the mixture. [Equality](../../MATHEMATICAL_MOVES.md#equals) requires a complete distribution, while the [inequality](../../MATHEMATICAL_MOVES.md#inequalities) forbids impossible negative shares.",
[("DoReMi","https://arxiv.org/abs/2305.10429"),("The Pile","https://arxiv.org/abs/2101.00027")]),
(185,"mixture-sampling","Mixture Sampling — Turn Planned Shares into a Reproducible Stream",
"The mixture weights state which domains should be heard. They do not yet produce a finite ordered token stream that every resumed worker can reconstruct.",
"round each domain's desired share independently and concatenate the resulting blocks",
"Independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero.",
"Use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source.",
"For 1,000 document draws, a 0.05 field-report weight expects about 50 selections. The seeded schedule interleaves those reports with other domains and records the actual count rather than promising exact equality by chance.",
"Sampling realizes probabilities only approximately in a finite run, and replacement can repeat scarce documents enough to increase memorization.",
r"E[n_d]=Nw_d",
"N is the total number of scheduled training draws, w_d is domain d's share, n_d is its realized count, and E[n_d] is the average count expected across many schedules.",
"[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced because each of N draws independently offers domain d the same share w_d. Addition would grant a fixed number unrelated to run length. [Expectation](../../MATHEMATICAL_MOVES.md#expectation) describes a long-run average, not a guarantee that one finite schedule equals Nw_d exactly.",
[("DoReMi","https://arxiv.org/abs/2305.10429"),("Dolma","https://arxiv.org/abs/2402.00159")]),
(186,"token-budget","The Token Budget — Convert a Training Plan into a Count of Lessons",
"Seeded mixture sampling can produce an ordered stream. The run still says “train for a while,” so neither cost nor source exposure is bounded.",
"stop when the wall clock reaches an affordable date",
"Faster hardware sees more tokens, interruptions see fewer, and two runs with the same calendar budget teach different amounts of evidence.",
"Define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute.",
"A tiny run uses 2,000 updates with 32 sequences of 128 real tokens each. Every update carries 4,096 lessons, so the complete plan exposes 8,192,000 tokens.",
"Equal token counts do not imply equal compute when model size, sequence length, sparsity, or hardware efficiency differs.",
r"N_{\text{tokens}}=T B_{\text{tokens}}",
"T is the planned number of optimizer updates, B_tokens counts real loss-bearing tokens in one global batch, and N_tokens is the complete exposure budget.",
"[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) appears because every one of T updates consumes B_tokens lessons. Addition would count only one update plus one batch. Padding is excluded because it occupies hardware but contributes no language target.",
[("OLMo","https://arxiv.org/abs/2402.00838"),("Training Compute-Optimal Large Language Models","https://arxiv.org/abs/2203.15556")]),
(187,"compute-optimal-allocation","Compute-Optimal Allocation — Buy a Larger Memory or More Experience?",
"The token budget fixes how much evidence the model will see. A fixed compute allowance still permits a wider model trained on fewer tokens or a smaller model trained on more.",
"spend nearly the entire budget on parameter count because a larger model can store more patterns",
"The large model is stopped after too little experience and remains undertrained, while much of its expensive capacity never receives enough varied evidence.",
"Estimate candidate parameter-and-token pairs under the same compute budget, run smaller scaling experiments, and choose the pair predicted to minimize held-out loss rather than maximizing either axis alone.",
"The station compares doubling parameters while halving tokens with keeping the smaller model and doubling tokens. Because both alter the same compute bill, held-out scaling runs decide which balance learns more.",
"Compute-optimal estimates are empirical and depend on architecture, data quality, optimizer, and the inference cost the project can afford afterward.",
r"C\approx 6PD",
"P is the number of trainable model parameters, D is the number of training tokens, and C is a rough count of floating-point work for dense Transformer training; six summarizes forward and backward work per parameter-token interaction.",
"[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced because every token exercises the model's parameters: doubling either P or D roughly doubles work. [Approximation](../../MATHEMATICAL_MOVES.md#approximation) preserves the scaling relation while admitting architecture and implementation details. Adding P and D would combine incompatible units.",
[("Training Compute-Optimal Large Language Models","https://arxiv.org/abs/2203.15556"),("Scaling Laws for Neural Language Models","https://arxiv.org/abs/2001.08361")]),
(188,"learning-rate-warmup","Learning-Rate Warmup — Let Adam Learn the Terrain Before Running",
"Compute allocation chooses the model and token horizon. At the first update, Adam's moment memories contain almost no history, while randomly initialized activations and gradients are changing fastest.",
"begin immediately at the peak learning rate chosen for the stable middle of training",
"The first noisy batches can make large updates before the optimizer's scale estimates become trustworthy, producing a loss spike that the later stable rate would not have caused.",
"Increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule.",
"With peak rate 0.001 and 100 warmup updates, update 25 receives 0.00025, update 50 receives 0.0005, and update 100 finally reaches 0.001.",
"Warmup reduces early shock but cannot rescue an unsuitable peak rate, broken initialization, corrupt batch, or incorrect optimizer state.",
r"\eta_t=\eta_{\text{peak}}\frac{t}{T_{\text{warm}}}\quad(0\le t\le T_{\text{warm}})",
"t is the current model warmup update, T_warm is the number of warmup updates, eta_peak is the intended stable rate, and eta_t is the smaller rate used now.",
"[Division](../../MATHEMATICAL_MOVES.md#division) turns elapsed warmup steps into a progress fraction from zero to one. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) applies that fraction to the peak rate. Adding t would mix step counts with a rate; jumping directly to eta_peak recreates the failed attempt.",
[("Attention Is All You Need","https://arxiv.org/abs/1706.03762"),("Accurate, Large Minibatch SGD","https://arxiv.org/abs/1706.02677")]),
(189,"cosine-decay","Cosine Decay — Make Late Corrections Smaller Without a Cliff",
"Warmup protects the optimizer's first steps. Keeping the peak rate for the entire token budget makes late updates as aggressive as early ones even when the model is refining rather than discovering broad structure.",
"drop the rate abruptly near the end of training",
"A sudden cliff changes update scale in one step and makes the chosen drop date an arbitrary discontinuity; dropping too early freezes useful learning.",
"Decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state.",
"Halfway through decay, cosine is zero, so the rate sits halfway between its peak and minimum. At the final planned update, cosine reaches negative one and the rate reaches the minimum without a jump.",
"Cosine decay assumes a known horizon and is not automatically optimal when training is unexpectedly extended.",
r"\eta_t=\eta_{\min}+\frac{\eta_{\max}-\eta_{\min}}{2}\left(1+\cos\frac{\pi t}{T}\right)",
"t is model-training progress through the decay interval of length T; eta_max and eta_min are its endpoint rates; cosine supplies a smooth path between them.",
"[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) isolates the adjustable rate range, [division](../../MATHEMATICAL_MOVES.md#division) converts progress to a fraction, and [cosine](../../MATHEMATICAL_MOVES.md#cosine) bends that fraction smoothly with flat endpoint slopes. Addition places the scaled range above eta_min. A raw linear drop is possible, but cosine avoids an abrupt endpoint slope.",
[("SGDR: Stochastic Gradient Descent with Warm Restarts","https://arxiv.org/abs/1608.03983"),("OLMo","https://arxiv.org/abs/2402.00838")]),
(190,"gradient-noise-scale","Gradient Noise Scale — When More Examples Stop Buying More Direction",
"The schedule controls how far one global update moves. We still do not know how many examples should vote in that update before extra devices mostly repeat the same directional evidence.",
"make the global batch as large as the cluster permits",
"Early doubling reduces disagreement and improves the direction, but beyond a workload-dependent point the averaged gradient barely changes while each update consumes twice as many tokens.",
"Measure disagreement among micro-batch gradients relative to the strength of their shared direction, and use that noise scale as evidence for the largest useful batch rather than a hardware target.",
"Three named micro-batches question the same two weights: the field reports propose [2.0,1.0], science proposes [2.1,0.9], and books propose [1.9,1.1]. The first number is advice to the tiger-before-river weight; the second is advice to a punctuation weight. Their mean [2.0,1.0] is strong and their disagreement around it is small. If the witnesses instead propose [4,−2], [0,4], and [2,1], disagreement is large relative to the same broad direction, so a larger batch can still buy useful certainty.",
"Gradient noise scale is an empirical guide, not a universal batch-size law; it changes during training and with the task and optimizer.",
r"G=\frac{\mathrm{tr}(\mathrm{Cov}[g_i])}{\lVert E[g_i]\rVert^2}",
"Each g_i is one model micro-batch's gradient advice. The covariance measures how those witnesses disagree; its trace totals disagreement across coordinates. The squared norm of their mean measures the strength of the shared direction; G compares noise with signal.",
"[Covariance](../../MATHEMATICAL_MOVES.md#covariance) keeps variation around the common advice rather than raw gradient size. [Trace](../../MATHEMATICAL_MOVES.md#trace) gathers coordinate variances without inventing cross-coordinate units. [Division](../../MATHEMATICAL_MOVES.md#division) asks disagreement per unit of squared shared direction; subtraction would not remove dependence on signal scale.",
[("An Empirical Model of Large-Batch Training","https://arxiv.org/abs/1812.06162")]),
(191,"data-parallelism","Data Parallelism — Let Several Workers Observe Different Evidence",
"Gradient noise measurements choose a useful global batch. One device cannot process that batch quickly enough, even though the modern model and optimizer state now fit through sharding.",
"send the same mini-batch to every worker and average their gradients",
"All workers repeat the same computation and return the same evidence, so hardware cost rises without increasing batch diversity or reducing step time meaningfully.",
"Replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update.",
"Four workers each read eight different sequences. Their four average gradients become one average over thirty-two sequences before any worker advances the parameters.",
"Because one shared update cannot proceed until every worker's evidence has joined the average, synchronous data parallelism waits for the slowest worker and communicates a full update's worth of gradient information.",
r"g=\frac1P\sum_{p=1}^{P}g_p",
"P is the number of data-parallel workers, g_p is worker p's average gradient from different examples, and g is the single gradient used by the shared optimizer step.",
"[Summation](../../MATHEMATICAL_MOVES.md#summation) lets every worker's independent evidence contribute. [Division](../../MATHEMATICAL_MOVES.md#division) returns advice per worker so adding hardware does not enlarge the update by itself. Multiplication would let a zero coordinate from one worker erase all others.",
[("PyTorch Distributed: Experiences on Accelerating Data Parallel Training","https://arxiv.org/abs/2006.15704"),("Accurate, Large Minibatch SGD","https://arxiv.org/abs/1706.02677")]),
(192,"pipeline-parallelism","Pipeline Parallelism — Stop Waiting for the Whole Model to Cross One Device at a Time",
"Data parallel workers process different examples, but each replica still needs the model's sequential layers. Splitting those layers across devices makes only one device active if a whole batch traverses the stages at once.",
"send one complete batch through stage one, then stage two, then stage three",
"While stage two works, stage one and stage three wait. The model fits, but most devices are idle for most of the step.",
"Split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently.",
"With four pipeline stages and eight micro-batches, the first few clock slots fill the pipeline, eight slots carry useful work, and the last few drain it. More micro-batches shrink the idle fraction.",
"Because sequential layer dependencies require the pipeline to fill and drain, pipeline parallelism introduces bubbles and activation transfers; making micro-batches too small can then reduce the efficiency of each matrix operation.",
r"U=\frac{m}{m+p-1}",
"m is the number of model micro-batches and p the number of pipeline stages in a simple forward pipeline. Useful work occupies m slots; filling and draining add p−1 slots; U is the idealized occupied share.",
"[Addition](../../MATHEMATICAL_MOVES.md#addition) joins useful slots with unavoidable fill-and-drain slots. [Division](../../MATHEMATICAL_MOVES.md#division) turns useful slots into a share of total schedule time. Multiplying m and p would count stage-tasks, not the fraction of time one stage remains usefully occupied.",
[("GPipe","https://arxiv.org/abs/1811.06965"),("Efficient Large-Scale Language Model Training with Megatron-LM","https://arxiv.org/abs/2104.04473")]),
(193,"three-dimensional-parallelism","Three-Dimensional Parallelism — Give Each Memory Wall Its Own Axis",
"Pipeline micro-batches keep layer stages busy. A large run may still exceed memory inside one layer, require more independent data witnesses, and contain too many layers for one device group.",
"increase whichever parallel technique was introduced most recently until the model fits",
"More pipeline stages increase bubbles, more tensor splits increase frequent communication, and more data replicas preserve full model memory. One axis cannot solve three different limits efficiently.",
"Compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost.",
"Two tensor workers form each layer, four pipeline stages hold the depth, and three data replicas see different examples. The run uses 2×4×3=24 workers with each axis performing one named job.",
"Three-dimensional parallelism increases coordination and configuration complexity; a poor mapping to the physical network can spend more time communicating than computing.",
r"P_{\text{total}}=P_{\text{tensor}}P_{\text{pipeline}}P_{\text{data}}",
"Each factor counts independent choices along one model-parallel axis. Selecting one tensor rank, one pipeline rank, and one data rank identifies exactly one worker; P_total counts all such combinations.",
"[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced by the product rule: every choice on one axis pairs with every choice on the others. Addition would count axis labels rather than workers. [Equality](../../MATHEMATICAL_MOVES.md#equals) assumes the grid is fully populated.",
[("Efficient Large-Scale Language Model Training with Megatron-LM","https://arxiv.org/abs/2104.04473"),("Megatron-Turing NLG 530B","https://arxiv.org/abs/2201.11990")]),
(194,"sharded-checkpoints","Sharded Checkpoints — Save One Recoverable State Without Gathering It",
"Three-dimensional parallelism spreads parameters, moments, gradients, and progress across many owners. Asking one coordinator to gather everything before saving can exceed its memory and stall the cluster.",
"let every worker write its local tensors and call the directory a checkpoint",
"A worker fails before writing, two shards belong to different steps, or a filename is reused. The directory exists but cannot reconstruct one globally consistent training state.",
"Write versioned shards to temporary locations, record hashes and ownership in a checkpoint manifest, and publish one atomic completion marker only after every required shard is durable.",
"Twenty-four workers save step 8,000. The manifest expects twenty-four parameter shards, optimizer shards, scheduler state, RNG state, and data cursors; the checkpoint becomes eligible for recovery only when every recorded hash verifies.",
"A complete checkpoint limits lost work but consumes storage and I/O bandwidth; frequent synchronous saves can dominate training time.",
None,
"The chapter earns an atomic distributed commit procedure rather than a new scalar formula.",
"[Sets](../../MATHEMATICAL_MOVES.md#sets) express the required shard inventory, and [equality](../../MATHEMATICAL_MOVES.md#equals) can verify that present shards exactly match the manifest. A mere shard count would miss duplicates or wrong identities.",
[("DataStates-LLM","https://arxiv.org/abs/2406.10707"),("OLMo","https://arxiv.org/abs/2402.00838")]),
(195,"deterministic-resume","Deterministic Resume — Continue the Same Experiment, Not a Similar One",
"The sharded checkpoint can reconstruct every distributed tensor. If it omits the sampler cursor, random-number generators, scheduler phase, or overflow state, restart follows a different future.",
"restore model weights and let every other component start fresh",
"Adam forgets its moments, warmup may begin again, dropout chooses different masks, and data workers repeat or skip documents. The loss curve after restart cannot be attributed to the original run.",
"Checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps.",
"The station stops after update 200, restores weights, Adam moments, schedule position, scaler, RNG streams, and each data cursor, then reproduces updates 201 through 205 byte for byte on the reference implementation.",
"Exact replay can still fail across nondeterministic kernels, changed hardware, libraries, or distributed timing; the required reproducibility level must be stated.",
None,
"The relevant object is a complete state tuple whose members already have concrete jobs in the next update.",
"[Tuples](../../MATHEMATICAL_MOVES.md#tuples) preserve differently typed state components without adding them. [Indices](../../MATHEMATICAL_MOVES.md#indices) keep the update and data positions explicit.",
[("OLMo","https://arxiv.org/abs/2402.00838"),("Pythia","https://arxiv.org/abs/2304.01373")]),
(196,"loss-spike-recovery","Loss Spikes — Distinguish One Hard Batch from a Run Leaving the Road",
"Deterministic resume makes failures reproducible. During a long run, the observed loss sometimes jumps; automatically rewinding every jump wastes compute, while ignoring a sustained instability can destroy the model.",
"declare any loss larger than the previous loss a failure and restore immediately",
"Ordinary batches vary, so healthy learning triggers constant rollbacks. A slow divergence can rise without one dramatic step and escape the rule.",
"Compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response.",
"Recent clean validation losses center near 2.0 with spread 0.1. One batch reaches 2.35 and then returns; another run stays above 2.5 while gradient norm grows. Only the persistent, corroborated event triggers recovery.",
"Thresholds detect symptoms, not causes; corrupt data, overflow, optimizer settings, hardware faults, and architectural instability require different repairs.",
r"z_t=\frac{L_t-\mu_t}{\sigma_t}",
"L_t is the current monitored model loss, mu_t is its robust recent center, sigma_t is ordinary recent spread, and z_t says how many usual spreads the current value lies above or below that center.",
"[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) removes the local baseline. [Division](../../MATHEMATICAL_MOVES.md#division) expresses the remainder in units of ordinary variation, making different loss scales comparable. A raw threshold would behave differently as normal loss falls during training.",
[("Spike No More","https://arxiv.org/abs/2312.16903"),("HLAT","https://arxiv.org/abs/2404.10630")]),
(197,"validation-stream","A Validation Stream — Ask Whether Learning Survives Outside the Current Batch",
"Loss-spike monitoring protects the training process from obvious instability. A smooth training curve can still improve mainly on repeated or overrepresented training domains.",
"evaluate only the next training batch because it is already available",
"The same data mixture and duplicates that shaped the update also judge it. Training loss can fall while held-out language or a rare domain becomes worse.",
"Maintain versioned, deduplicated, contamination-checked validation streams by domain and evaluate them at recorded token intervals without using them to update weights.",
"After every million training tokens, the station measures held-out field reports, science, books, code, and web text separately. A lower global average cannot hide that field-report loss rose.",
"Validation detects only the distributions and behaviors represented in its finite streams; repeatedly tuning against it can eventually overfit it.",
r"L_{\text{val}}=-\frac1N\sum_{i=1}^{N}\log p_\theta(x_i\mid x_{<i})",
"The validation stream contains N honest next-token events. The model assigns the observed token x_i a conditional probability from its earlier context. Negative log turns confident neglect into positive cost, and L_val averages that cost across the stream.",
"[Logarithms](../../MATHEMATICAL_MOVES.md#logarithm) turn multiplied sequence probabilities into additive token costs. [Negative signs](../../MATHEMATICAL_MOVES.md#negative-sign) make lower assigned probability cost more. [Summation](../../MATHEMATICAL_MOVES.md#summation) lets every event contribute, and [division](../../MATHEMATICAL_MOVES.md#division) makes streams of different lengths comparable.",
[("Paloma","https://arxiv.org/abs/2312.10523"),("Dolma","https://arxiv.org/abs/2402.00159")]),
(198,"memorization-audit","A Memorization Audit — Did the Model Learn a Pattern or Store a Passage?",
"Held-out validation shows whether prediction improves outside current batches. It does not reveal whether rare or repeated training sequences can be extracted verbatim from the model.",
"ask the model whether it remembers private text and trust its answer",
"A model has no reliable introspective inventory of its training examples, and ordinary prompts may miss strings that an adversarial sampling strategy can recover.",
"Plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts.",
"The station inserts one synthetic radio code once and another code one hundred times. If the repeated code becomes far easier to rank and complete, the audit exposes the relationship between repetition and extractable memory without using a real secret.",
"A canary audit samples possible attacks and strings; passing it does not prove that no training data can be extracted.",
r"\mathrm{exposure}=\log_2\lvert\mathcal R\rvert-\log_2\mathrm{rank}",
"R is the known space of possible synthetic canaries and rank is the tested canary's position when alternatives are ordered from most to least likely. Exposure measures how many bits of the search space the model has effectively removed.",
"[Cardinality](../../MATHEMATICAL_MOVES.md#cardinality) counts possible canaries. [Logarithms](../../MATHEMATICAL_MOVES.md#logarithm) turn multiplicative changes in search space and rank into bits. [Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) removes the remaining search difficulty from the original difficulty; adding would reward a worse rank.",
[("The Secret Sharer","https://arxiv.org/abs/1802.08232"),("Extracting Training Data from Large Language Models","https://arxiv.org/abs/2012.07805"),("Deduplicating Training Data Makes Language Models Better","https://arxiv.org/abs/2107.06499")]),
(199,"training-report","The Training Report — Preserve the Decisions, Not Only the Weights",
"Memorization auditing adds one essential limitation to the evaluation record. A released checkpoint still cannot explain its corpus, mixture, compute, interruptions, exclusions, intended uses, or known failures by inspecting weight tensors.",
"publish the final benchmark table and assume the configuration files explain the rest",
"A score has no visible data lineage, uncertainty, subgroup behavior, energy or hardware context, incident history, or warning about uses the evaluation never tested.",
"Generate a training report from manifests and logs, then add human-reviewed explanations of intended use, out-of-scope use, limitations, incidents, provenance, evaluation conditions, and responsible release decisions.",
"The station's report names corpus and code versions, tokens seen, mixture shares, compute, checkpoint recoveries, per-domain validation, memorization probes, excluded sources, and the exact model artifact hash.",
"Documentation improves accountability but can be incomplete, outdated, misleading, or ignored; claims still require inspectable evidence.",
None,
"This chapter earns a structured account connecting evidence and decisions rather than another model transformation.",
"[Tables](../../MATHEMATICAL_MOVES.md#tables) preserve exact mappings among claims, evidence, conditions, and limitations; a single aggregate score would erase those relationships.",
[("Model Cards for Model Reporting","https://arxiv.org/abs/1810.03993"),("Datasheets for Datasets","https://arxiv.org/abs/1803.09010"),("OLMo","https://arxiv.org/abs/2402.00838")]),
(200,"tiny-pretraining-factory","A Tiny Pretraining Factory — Close the Accountable Training Loop",
"The training report can explain one finished run. We have now earned all the mechanisms needed to make the next run reconstructable from source documents to final artifact rather than relying on memory and scattered scripts.",
"connect every tool into one automatic pipeline and trust any run that reaches the final stage",
"Automation can faithfully repeat a wrong manifest, destructive filter, contaminated validation set, incomplete checkpoint, or unauthorized release. Completion is not evidence of correctness.",
"Assemble signed stage manifests, boundary-aware curation, audited mixtures, fixed budgets, measured schedules, distributed equivalence tests, atomic checkpoints, live validation, memorization probes, and human release gates into one reversible factory.",
"A tiny run begins from ten named documents, records every acceptance and removal, trains a reproducible model, survives an intentional interruption, reproduces its next updates, generates its report, and refuses release when the memorization gate fails.",
"The factory is accountable, not omniscient. New sources, laws, hardware, attacks, and uses create new failures that must return to observation and the bounded research loop.",
None,
"No final equation is introduced because the discovery is the tested composition of procedures already derived.",
"[Arrows](../../MATHEMATICAL_MOVES.md#arrows) preserve causal stage order, while [logical conjunction](../../MATHEMATICAL_MOVES.md#logical-and) requires every independent release gate rather than averaging a failure away.",
[("OLMo","https://arxiv.org/abs/2402.00838"),("Dolma","https://arxiv.org/abs/2402.00159"),("DataComp-LM","https://arxiv.org/abs/2406.11794")]),
]


def chapter(row):
    n,slug,title,carry,attempt,failure,repair,case,limit,formula,terms,operations,refs=row
    index=(n-176)%6
    attempt_leads=("Perhaps we ","We first try to ","One tempting answer is to ","At first we ","Using what we have, we ","An obvious shortcut is to ")
    failure_leads=("But the run answers back. ","That confidence lasts only until the first measurement. ","The shortcut reaches its first real document and breaks. ","Reality objects. ","The plan survives only until the evidence is counted. ","Then the hidden cost becomes visible. ")
    repair_leads=("The failure leaves one precise requirement. ","What broke tells us what the next design must preserve. ","Now the missing job can be stated plainly. ","That evidence forces a repair. ","The lost information tells us what must come next. ","Crossing that boundary requires one additional guarantee. ")
    part = ("> **PART XIII — A PRETRAINING FACTORY WE CAN ACCOUNT FOR**\n>\n"
            "> The engine can run. Now every document, update, shard, interruption, and release claim must leave enough evidence to reconstruct the same experiment.\n\n") if n == 176 else ""
    math = ""
    if formula:
        math = f"""\n## The arithmetic we have earned

{terms}

### Why these operations are forced

{operations}

Only now can we compress the procedure:

$$
{formula}
$$
"""
    nxt = (f"[Next: {ROWS[n-175][2]}](../{n+1:03d}-{ROWS[n-175][1]}/README.md)" if n < 200 else
           "The factory returns every proposed change to the bounded loop: observe, test, document, authorize, release reversibly, and remain able to reconstruct what happened.")
    return f"""# Excavation {n:03d} — {title}

{part}{carry}

{attempt_leads[index]}{attempt}.

{failure_leads[index]}{failure}

{repair_leads[index]}{repair}

## Let one run decide

{case}
{math}
## What this repair cannot do

{limit}

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

{nxt}
"""


PURE = {
176: '''import hashlib\ndef manifest(sources):\n    rows=[]\n    for name,documents in sorted(sources.items()):\n        joined="\\n".join(documents).encode(); rows.append({"source":name,"documents":len(documents),"sha256":hashlib.sha256(joined).hexdigest()})\n    return rows\ndef demo():\n    out=manifest({"field-v3":["tiger","river"]}); assert out[0]["documents"]==2\n    return {"manifest":out}''',
177: '''def boundary_mask(document_ids): return [[int(a==b) for b in document_ids] for a in document_ids]\ndef demo():\n    mask=boundary_mask(["report-a","report-a","license-b"]); assert mask[0]==[1,1,0]\n    return {"mask":mask}''',
178: '''def identify(scores,threshold=.8):\n    label=max(scores,key=scores.get); return label if scores[label]>=threshold else "unknown"\ndef demo():\n    assert identify({"en":.93,"es":.05})=="en" and identify({"en":.44,"es":.41})=="unknown"\n    return {"confident":"en","uncertain":"unknown"}''',
179: '''import hashlib\ndef normalize(text): return " ".join(text.split()).lower()\ndef fingerprint(text): return hashlib.sha256(normalize(text).encode()).hexdigest()\ndef demo():\n    a=fingerprint("Tiger  near river\\n"); b=fingerprint(" tiger near   river "); assert a==b\n    return {"same_fingerprint":a==b,"fingerprint":a}''',
180: '''def shingles(text,width=2):\n    words=text.lower().split(); return {tuple(words[i:i+width]) for i in range(len(words)-width+1)}\ndef jaccard(a,b): return len(a&b)/len(a|b) if a|b else 1.0\ndef demo():\n    a=shingles("tiger tracks beside the river bank"); b=shingles("tiger tracks beside a river bank"); score=jaccard(a,b); assert 0<score<1\n    return {"near_duplicate_score":score}''',
181: '''def structural_signals(text):\n    lines=[x.strip() for x in text.splitlines() if x.strip()]; repeated=1-len(set(lines))/max(1,len(lines)); sentences=sum(x.endswith((".","?","!")) for x in lines)\n    return {"repeated_line_share":repeated,"sentence_count":sentences}\ndef demo():\n    spam=structural_signals("MENU\\nMENU\\nMENU"); report=structural_signals("Tiger seen.\\nTrack direction recorded."); assert spam["repeated_line_share"]>report["repeated_line_share"]\n    return {"spam":spam,"report":report,"decision":"audit thresholds by source"}''',
182: '''def lineage(document_id,source,steps,shard): return {"id":document_id,"source":source,"steps":list(steps),"shard":shard}\ndef demo():\n    row=lineage("river-0042","field-v3",["lang:en","dedup:cluster-7","redact:v2"],"shard-01@128"); assert row["steps"][1]=="dedup:cluster-7"\n    return row''',
183: '''import re\ndef redact(text):\n    text=re.sub(r"\\b[\\w.+-]+@[\\w.-]+\\.[A-Za-z]{2,}\\b","[EMAIL]",text)\n    return re.sub(r"\\b\\d{3}-\\d{4}\\b","[PHONE]",text)\ndef demo():\n    out=redact("Call Maya at 555-0142 or maya@example.org about the tiger"); assert "555" not in out and "example.org" not in out\n    return {"redacted":out}''',
184: '''def validate(weights,tolerance=1e-12): return all(x>=0 for x in weights.values()) and abs(sum(weights.values())-1)<tolerance\ndef demo():\n    mix={"web":.5,"science":.2,"code":.15,"books":.1,"field":.05}; assert validate(mix)\n    return {"mixture":mix,"total":sum(mix.values())}''',
185: '''import random\ndef schedule(weights,draws,seed):\n    names=list(weights); rng=random.Random(seed); return rng.choices(names,weights=[weights[n] for n in names],k=draws)\ndef demo():\n    weights={"web":.8,"field":.2}; a=schedule(weights,1000,7); b=schedule(weights,1000,7); assert a==b\n    return {"field_draws":a.count("field"),"reproducible":True}''',
186: '''def token_budget(steps,sequences,width): return steps*sequences*width\ndef demo():\n    total=token_budget(2000,32,128); assert total==8_192_000\n    return {"tokens":total}''',
187: '''def training_flops(parameters,tokens,factor=6): return factor*parameters*tokens\ndef demo():\n    small=training_flops(100_000_000,2_000_000_000); large=training_flops(200_000_000,1_000_000_000); assert small==large\n    return {"equal_compute":small,"candidates":["more_tokens","more_parameters"]}''',
188: '''def warmup(step,warm_steps,peak): return peak*min(1,step/warm_steps)\ndef demo():\n    rates=[warmup(t,100,.001) for t in (0,25,50,100)]; assert rates==[0,.00025,.0005,.001]\n    return {"rates":rates}''',
189: '''import math\ndef cosine_rate(step,horizon,maximum,minimum=0): return minimum+(maximum-minimum)/2*(1+math.cos(math.pi*step/horizon))\ndef demo():\n    rates=[cosine_rate(t,100,.001,.0001) for t in (0,50,100)]; assert abs(rates[1]-.00055)<1e-12\n    return {"start_middle_end":rates}''',
190: '''def noise_scale(gradients):\n    width=len(gradients[0]); mean=[sum(g[j] for g in gradients)/len(gradients) for j in range(width)]; variance=sum(sum((g[j]-mean[j])**2 for g in gradients)/len(gradients) for j in range(width)); signal=sum(x*x for x in mean)\n    return variance/signal if signal else float("inf")\ndef demo():\n    agree=noise_scale([[2,1],[2.1,.9],[1.9,1.1]]); disagree=noise_scale([[4,-2],[0,4],[2,1]]); assert disagree>agree\n    return {"agreeing_scale":agree,"disagreeing_scale":disagree}''',
191: '''def average_worker_gradients(workers): return [sum(values)/len(workers) for values in zip(*workers)]\ndef demo():\n    g=average_worker_gradients([[2,4],[4,2],[3,3],[3,3]]); assert g==[3,3]\n    return {"shared_gradient":g,"workers":4}''',
192: '''def utilization(microbatches,stages): return microbatches/(microbatches+stages-1)\ndef timeline(microbatches,stages): return [[m+s for m in range(microbatches)] for s in range(stages)]\ndef demo():\n    assert utilization(8,4)==8/11\n    return {"utilization":utilization(8,4),"clock_slots":timeline(8,4)}''',
193: '''def worker_count(tensor,pipeline,data): return tensor*pipeline*data\ndef coordinates(tensor,pipeline,data): return [(t,p,d) for d in range(data) for p in range(pipeline) for t in range(tensor)]\ndef demo():\n    ranks=coordinates(2,4,3); assert len(ranks)==worker_count(2,4,3)==24 and len(set(ranks))==24\n    return {"workers":len(ranks),"first":ranks[0],"last":ranks[-1]}''',
194: '''import hashlib\ndef complete(expected,shards):\n    present={name for name,data in shards.items() if hashlib.sha256(data).hexdigest()==expected.get(name)}\n    return present==set(expected)\ndef demo():\n    data={"rank0":b"weights-a","rank1":b"weights-b"}; expected={k:hashlib.sha256(v).hexdigest() for k,v in data.items()}; assert complete(expected,data) and not complete(expected,{"rank0":data["rank0"]})\n    return {"complete":True,"required_shards":sorted(expected)}''',
195: '''def next_step(state):\n    value=(state["rng"]*1103515245+12345)%2**31; state=dict(state,rng=value,step=state["step"]+1,cursor=state["cursor"]+1); return state,value%100\ndef demo():\n    saved={"weights":[1.0],"moments":[.2],"step":200,"cursor":800,"rng":7}; a,out1=next_step(saved); b,out2=next_step(saved); assert a==b and out1==out2\n    return {"next_state":a,"next_draw":out1}''',
196: '''def z_score(current,history):\n    center=sum(history)/len(history); spread=(sum((x-center)**2 for x in history)/len(history))**.5; return (current-center)/(spread or 1)\ndef persistent_alarm(losses,window=4,threshold=3):\n    baseline=losses[:window]\n    return len(losses)>=window+2 and all(z_score(x,baseline)>threshold for x in losses[-2:])\ndef demo():\n    transient=[2.0,2.1,1.9,2.0,2.35,2.0]; sustained=[2.0,2.1,1.9,2.0,2.6,2.7]; assert not persistent_alarm(transient) and persistent_alarm(sustained)\n    return {"transient_alarm":False,"sustained_alarm":True}''',
197: '''import math\ndef mean_nll(probabilities): return -sum(math.log(p) for p in probabilities)/len(probabilities)\ndef demo():\n    domains={"field":[.7,.6],"web":[.8,.9]}; losses={name:mean_nll(p) for name,p in domains.items()}; assert losses["field"]>losses["web"]\n    return {"per_domain_loss":losses}''',
198: '''import math\ndef exposure(search_space,rank): return math.log2(search_space)-math.log2(rank)\ndef demo():\n    once=exposure(1_000_000,100_000); repeated=exposure(1_000_000,10); assert repeated>once\n    return {"single_exposure":once,"repeated_exposure":repeated}''',
199: '''def build_report(manifest,run,evaluations,incidents):\n    required=("corpus_hash","tokens","compute","artifact_hash"); assert all(key in {**manifest,**run} for key in required)\n    return {"manifest":manifest,"run":run,"evaluations":evaluations,"incidents":incidents,"limitations":["finite audits","documented scope only"]}\ndef demo():\n    report=build_report({"corpus_hash":"abc"},{"tokens":8192,"compute":49152,"artifact_hash":"xyz"},{"field_loss":2.1},["restored step 200"]); assert report["limitations"]\n    return report''',
200: '''def release(factory):\n    gates=(factory["manifest_signed"],factory["resume_verified"],factory["validation_passed"],factory["memorization_passed"],factory["approved"],factory["rollback_ready"]); return all(gates)\ndef demo():\n    clean={"manifest_signed":True,"resume_verified":True,"validation_passed":True,"memorization_passed":True,"approved":True,"rollback_ready":True}; risky=dict(clean,memorization_passed=False); assert release(clean) and not release(risky)\n    return {"clean_release":True,"memorization_failure_release":False}''',
}


NUMPY = {
176: '''sources=np.array(["field-v3","science-v2"]); counts=np.array([8412,12000]); assert counts.sum()==20412; print({"sources":sources,"documents":counts})''',
177: '''ids=np.array([0,0,1]); mask=(ids[:,None]==ids[None,:]).astype(int); assert np.array_equal(mask[0],[1,1,0]); print({"mask":mask})''',
178: '''scores=np.array([.93,.05,.02]); labels=np.array(["en","es","unknown"]); winner=labels[scores.argmax()] if scores.max()>=.8 else "unknown"; assert winner=="en"; print({"winner":winner,"confidence":scores.max()})''',
179: '''fingerprints=np.array([12,12,91,37,91]); unique,counts=np.unique(fingerprints,return_counts=True); assert counts.max()==2; print({"unique":unique,"duplicate_counts":counts})''',
180: '''a=np.array([1,1,1,1,0,0],dtype=bool); b=np.array([1,1,1,0,1,0],dtype=bool); score=np.logical_and(a,b).sum()/np.logical_or(a,b).sum(); assert 0<score<1; print({"jaccard":score})''',
181: '''signals=np.array([[.8,0],[.0,2]],dtype=float); retained=signals[:,0]<.5; assert np.array_equal(retained,[False,True]); print({"signals":signals,"retained":retained})''',
182: '''edges=np.array([["raw","normalized"],["normalized","redacted"],["redacted","shard-01"]]); assert edges[-1,1]=="shard-01"; print({"lineage_edges":edges})''',
183: '''tokens=np.array(["Call","[PERSON]","at","[PHONE]","about","tiger"]); assert not any("555" in x for x in tokens); print({"redacted_tokens":tokens})''',
184: '''weights=np.array([.5,.2,.15,.1,.05]); assert np.all(weights>=0) and np.isclose(weights.sum(),1); print({"weights":weights})''',
185: '''rng=np.random.default_rng(7); draws=rng.choice(2,size=1000,p=[.8,.2]); counts=np.bincount(draws,minlength=2); assert counts.sum()==1000; print({"realized_counts":counts,"expected":np.array([800,200])})''',
186: '''steps=np.int64(2000); batch=np.int64(32*128); tokens=steps*batch; assert tokens==8_192_000; print({"tokens":tokens})''',
187: '''parameters=np.array([100e6,200e6]); tokens=np.array([2e9,1e9]); compute=6*parameters*tokens; assert compute[0]==compute[1]; print({"compute":compute})''',
188: '''steps=np.array([0,25,50,100]); rates=.001*np.minimum(1,steps/100); assert np.allclose(rates,[0,.00025,.0005,.001]); print({"rates":rates})''',
189: '''steps=np.array([0,50,100]); rates=.0001+(.001-.0001)/2*(1+np.cos(np.pi*steps/100)); assert np.isclose(rates[1],.00055); print({"rates":rates})''',
190: '''g=np.array([[2.,1.],[2.1,.9],[1.9,1.1]]); mean=g.mean(0); covariance=np.cov(g,rowvar=False,bias=True); scale=np.trace(covariance)/(mean@mean); assert scale<.01; print({"noise_scale":scale,"covariance":covariance})''',
191: '''workers=np.array([[2.,4.],[4.,2.],[3.,3.],[3.,3.]]); shared=workers.mean(0); assert np.array_equal(shared,[3,3]); print({"shared_gradient":shared})''',
192: '''m,p=8,4; utilization=m/(m+p-1); clocks=np.add.outer(np.arange(p),np.arange(m)); assert np.isclose(utilization,8/11); print({"utilization":utilization,"clock_slots":clocks})''',
193: '''shape=np.array([2,4,3]); workers=shape.prod(); coords=np.stack(np.unravel_index(np.arange(workers),shape),axis=1); assert len(coords)==24; print({"worker_grid":shape,"workers":workers})''',
194: '''expected=np.array([11,22,33,44]); present=np.array([11,22,33,44]); assert np.array_equal(np.sort(expected),np.sort(present)); print({"complete":True,"shards":len(present)})''',
195: '''state=np.array([1.0,.2,200,800,7]); restored=state.copy(); assert np.array_equal(state,restored); print({"restored_state":restored})''',
196: '''history=np.array([2.0,2.1,1.9,2.0]); current=2.6; z=(current-history.mean())/(history.std() or 1); assert z>3; print({"z_score":z})''',
197: '''p=np.array([[.7,.6],[.8,.9]]); losses=-np.log(p).mean(1); assert losses[0]>losses[1]; print({"field_loss":losses[0],"web_loss":losses[1]})''',
198: '''ranks=np.array([100000,10]); exposure=np.log2(1_000_000)-np.log2(ranks); assert exposure[1]>exposure[0]; print({"exposure":exposure})''',
199: '''fields=np.array(["corpus","tokens","compute","validation","memorization","incidents","limitations"]); assert "limitations" in fields; print({"report_fields":fields})''',
200: '''gates=np.array([True,True,True,False,True,True]); assert not gates.all(); print({"release":gates.all(),"failed_gate":np.where(~gates)[0]})''',
}


TORCH = {
176: '''counts=torch.tensor([8412,12000]); assert counts.sum()==20412; print({"documents":counts})''',
177: '''ids=torch.tensor([0,0,1]); mask=(ids[:,None]==ids[None,:]).int(); assert torch.equal(mask[0],torch.tensor([1,1,0])); print({"mask":mask})''',
178: '''scores=torch.tensor([.93,.05,.02]); winner=scores.argmax(); assert winner.item()==0 and scores.max()>=.8; print({"winner_index":winner.item(),"confidence":scores.max().item()})''',
179: '''fingerprints=torch.tensor([12,12,91,37,91]); unique,counts=torch.unique(fingerprints,return_counts=True); assert counts.max()==2; print({"unique":unique,"counts":counts})''',
180: '''a=torch.tensor([1,1,1,1,0,0],dtype=torch.bool); b=torch.tensor([1,1,1,0,1,0],dtype=torch.bool); score=(a&b).sum().float()/(a|b).sum(); assert 0<score<1; print({"jaccard":score})''',
181: '''signals=torch.tensor([[.8,0.],[0.,2.]]); retained=signals[:,0]<.5; assert torch.equal(retained,torch.tensor([False,True])); print({"retained":retained})''',
182: '''stage_ids=torch.tensor([0,1,2,3]); assert torch.equal(stage_ids[1:],stage_ids[:-1]+1); print({"lineage_stage_ids":stage_ids})''',
183: '''risk=torch.tensor([0.,1.,0.,1.,0.,0.]); redacted=risk.bool(); assert redacted.sum()==2; print({"redacted_positions":torch.where(redacted)[0]})''',
184: '''weights=torch.tensor([.5,.2,.15,.1,.05]); assert torch.all(weights>=0) and torch.isclose(weights.sum(),torch.tensor(1.)); print({"weights":weights})''',
185: '''generator=torch.Generator().manual_seed(7); weights=torch.tensor([.8,.2]); draws=torch.multinomial(weights,1000,replacement=True,generator=generator); counts=torch.bincount(draws,minlength=2); assert counts.sum()==1000; print({"counts":counts})''',
186: '''tokens=torch.tensor(2000,dtype=torch.int64)*32*128; assert tokens==8_192_000; print({"tokens":tokens.item()})''',
187: '''parameters=torch.tensor([100e6,200e6]); tokens=torch.tensor([2e9,1e9]); compute=6*parameters*tokens; assert compute[0]==compute[1]; print({"compute":compute})''',
188: '''steps=torch.tensor([0.,25.,50.,100.]); rates=.001*torch.minimum(torch.ones_like(steps),steps/100); assert torch.allclose(rates,torch.tensor([0.,.00025,.0005,.001])); print({"rates":rates})''',
189: '''steps=torch.tensor([0.,50.,100.]); rates=.0001+(.001-.0001)/2*(1+torch.cos(torch.pi*steps/100)); assert torch.isclose(rates[1],torch.tensor(.00055)); print({"rates":rates})''',
190: '''g=torch.tensor([[2.,1.],[2.1,.9],[1.9,1.1]]); mean=g.mean(0); centered=g-mean; covariance=centered.T@centered/len(g); scale=torch.trace(covariance)/(mean@mean); assert scale<.01; print({"noise_scale":scale})''',
191: '''workers=torch.tensor([[2.,4.],[4.,2.],[3.,3.],[3.,3.]]); shared=workers.mean(0); assert torch.equal(shared,torch.tensor([3.,3.])); print({"shared_gradient":shared})''',
192: '''m,p=8,4; clocks=torch.arange(p)[:,None]+torch.arange(m)[None,:]; utilization=m/(m+p-1); assert clocks.shape==(4,8); print({"utilization":utilization,"clock_slots":clocks})''',
193: '''shape=torch.tensor([2,4,3]); workers=shape.prod(); assert workers==24; print({"parallel_shape":shape,"workers":workers.item()})''',
194: '''expected=torch.tensor([11,22,33,44]); present=torch.tensor([11,22,33,44]); assert torch.equal(torch.sort(expected).values,torch.sort(present).values); print({"complete":True})''',
195: '''state={"weights":torch.tensor([1.]),"moments":torch.tensor([.2]),"step":torch.tensor(200),"cursor":torch.tensor(800),"rng":torch.tensor(7)}; restored={k:v.clone() for k,v in state.items()}; assert all(torch.equal(state[k],restored[k]) for k in state); print(restored)''',
196: '''history=torch.tensor([2.,2.1,1.9,2.]); current=torch.tensor(2.6); z=(current-history.mean())/history.std(correction=0); assert z>3; print({"z_score":z})''',
197: '''p=torch.tensor([[.7,.6],[.8,.9]]); losses=-torch.log(p).mean(1); assert losses[0]>losses[1]; print({"domain_losses":losses})''',
198: '''ranks=torch.tensor([100000.,10.]); exposure=torch.log2(torch.tensor(1_000_000.))-torch.log2(ranks); assert exposure[1]>exposure[0]; print({"exposure":exposure})''',
199: '''metrics=torch.tensor([8_192_000.,49_152_000.,2.1,.3]); assert torch.isfinite(metrics).all(); print({"tokens_compute_loss_exposure":metrics})''',
200: '''gates=torch.tensor([True,True,True,False,True,True]); release=torch.all(gates); assert not release; print({"release":release.item(),"failed_gate":torch.where(~gates)[0]})''',
}


DIAGRAMS = {
176: '''```mermaid\nflowchart LR\n  S1["field-reports/v3"] --> M["signed corpus manifest"]\n  S2["science/v2"] --> M\n  S3["code/v5"] --> M\n  M --> H["manifest hash"] --> R["reconstructable run"]\n```\n\n```text\nsource + version + count + hash + usage basis -> one frozen evidence ledger\n```''',
177: '''```mermaid\nflowchart TB\n  subgraph Row["one packed row"]\n    A["report A tokens"] --- B["document boundary"] --- C["license B tokens"]\n  end\n  A -->|"attention allowed"| A\n  C -->|"attention allowed"| C\n  A -. "blocked" .-> C\n```\n\n```text\nA A A | B B\n1 1 1 | 0 0   <- what an A token may read\n```''',
178: '''```mermaid\nflowchart LR\n  D["one field report"] --> C["language classifier v3"]\n  C --> E["English 0.93"]\n  C --> S["Spanish 0.05"]\n  C --> U["unknown 0.02"]\n  E -->|"above 0.80"| KEEP["English stream"]\n```\n\n```text\nwinner without confidence -> forced label\nwinner plus threshold      -> label or unknown\n```''',
179: '''```mermaid\nflowchart LR\n  A["Tiger near river\\n"] --> N["recorded normalization"] --> H1["hash 7fa..."]\n  B[" tiger  near river "] --> N --> H2["hash 7fa..."]\n  H1 --> ONE["one training representative"]\n  H2 --> ONE\n```\n\n```text\nthree locations -> one fingerprint -> one vote, three provenance records\n```''',
180: '''```mermaid\nflowchart LR\n  A["original: 10 shingles"] --> I["shared intersection: 8"]\n  B["edited copy: 10 shingles"] --> I\n  A --> U["distinct union: 12"]\n  B --> U\n  I --> J["Jaccard: 8 / 12 = 0.67"]\n  U --> J\n```\n\n```text\nshared 8 / distinct total 12 = 0.67 near-duplicate similarity\n```''',
181: '''```mermaid\nflowchart TD\n  D["document"] --> S1["repeated-line share"]\n  D --> S2["sentence structure"]\n  D --> S3["source-aware model signal"]\n  S1 --> A["retention audit by source"]\n  S2 --> A\n  S3 --> A\n  A --> H["human review near thresholds"]\n```\n\n```text\nfilter quality must be measured twice: what it removes and whom it removes\n```''',
182: '''```mermaid\nflowchart LR\n  RAW["river-0042 raw"] --> N["normalize v2"] --> L["language en 0.93"] --> D["dedup cluster 7"] --> P["redact v2"] --> S["shard-01 offset 128"]\n```\n\n```text\nfinal token -> shard offset -> decision trail -> original source\n```''',
183: '''```mermaid\nflowchart LR\n  O["Call Maya at 555-0142 about tiger"] --> DET["candidate span detectors"]\n  DET --> CTX["context review"] --> R["Call [PERSON] at [PHONE] about tiger"]\n```\n\n```text\nkeep the grammatical lesson; remove the direct identifier; log the rule\n```''',
184: '''```mermaid\npie showData\n  title Explicit pretraining mixture\n  "curated web" : 50\n  "science" : 20\n  "code" : 15\n  "books" : 10\n  "field reports" : 5\n```\n\n```text\nraw corpus size does not get to choose the curriculum silently\n```''',
185: '''```mermaid\nsequenceDiagram\n  participant RNG as Seeded scheduler\n  participant W as Web source\n  participant F as Field source\n  participant T as Training stream\n  RNG->>W: draw web\n  W->>T: document\n  RNG->>F: draw field\n  F->>T: document\n  RNG->>W: next seeded draw\n```\n\n```text\nplanned share -> seeded choices -> realized counts -> resumable cursor\n```''',
186: '''```mermaid\nflowchart LR\n  S["2,000 optimizer steps"] --> X(("×"))\n  B["32 sequences × 128 real tokens"] --> X\n  X --> T["8,192,000 training tokens"]\n```\n\n```text\ncalendar time varies; the promised number of lessons does not\n```''',
187: '''```mermaid\nflowchart TB\n  C["fixed compute budget"] --> A["more parameters × fewer tokens"]\n  C --> B["fewer parameters × more tokens"]\n  A --> V["small scaling experiments"]\n  B --> V\n  V --> CHOICE["lowest predicted held-out loss"]\n```\n\n```text\ncompute buys parameter-token interactions, not size alone\n```''',
188: '''```mermaid\nxychart-beta\n  x-axis "warmup step" [0,25,50,75,100]\n  y-axis "learning rate" 0 --> 0.001\n  line [0,0.00025,0.0005,0.00075,0.001]\n```\n\n```text\nempty Adam memory + peak rate -> early shock\ngradual rate                  -> time to learn scale\n```''',
189: '''```mermaid\nxychart-beta\n  x-axis "decay progress" [0,25,50,75,100]\n  y-axis "learning rate" 0.0001 --> 0.001\n  line [0.001,0.000868,0.00055,0.000232,0.0001]\n```\n\n```text\nbroad early movement -> careful late correction, without a sudden cliff\n```''',
190: '''```mermaid\nflowchart LR\n  G1["micro-batch gradient 1"] --> M["shared direction"]\n  G2["micro-batch gradient 2"] --> M\n  G3["micro-batch gradient 3"] --> M\n  G1 --> N["disagreement around mean"]\n  G2 --> N\n  G3 --> N\n  M --> R["noise / signal"]\n  N --> R\n```\n\n```text\nmore witnesses help while disagreement is large relative to shared advice\n```''',
191: '''```mermaid\nflowchart TB\n  M["same model state"] --> W1["worker 1: examples 1-8"]\n  M --> W2["worker 2: examples 9-16"]\n  M --> W3["worker 3: examples 17-24"]\n  M --> W4["worker 4: examples 25-32"]\n  W1 --> AVG["average gradients"]\n  W2 --> AVG\n  W3 --> AVG\n  W4 --> AVG\n  AVG --> U["one shared update"]\n```\n\n```text\nsame model, different evidence, one logically shared next state\n```''',
192: '''```mermaid\nsequenceDiagram\n  participant S1 as layers 1-3\n  participant S2 as layers 4-6\n  participant S3 as layers 7-9\n  S1->>S2: micro-batch A\n  S1->>S2: micro-batch B while A advances\n  S2->>S3: micro-batch A\n  S1->>S2: micro-batch C while B advances\n```\n\n```text\nclock: 1 2 3 4 5\nstage1 A B C . .\nstage2 . A B C .\nstage3 . . A B C\n```''',
193: '''```mermaid\nflowchart TB\n  subgraph Data["3 data replicas"]\n    subgraph Pipe["4 pipeline stages each"]\n      T["2 tensor ranks inside every stage"]\n    end\n  end\n  T --> TOTAL["2 × 4 × 3 = 24 workers"]\n```\n\n```text\nworker identity = (tensor rank, pipeline rank, data rank)\n```''',
194: '''```mermaid\nflowchart TB\n  R0["rank 0 temporary shard"] --> M["checkpoint manifest + hashes"]\n  R1["rank 1 temporary shard"] --> M\n  RN["rank N temporary shard"] --> M\n  M --> Q{"every required shard durable?"}\n  Q -->|"yes"| C["atomic COMPLETE marker"]\n  Q -->|"no"| X["not recoverable"]\n```\n\n```text\ndirectory exists != checkpoint complete\n```''',
195: '''```mermaid\nflowchart LR\n  C["checkpoint at step 200"] --> W["weights"]\n  C --> O["optimizer moments"]\n  C --> S["schedule + scaler"]\n  C --> R["RNG streams"]\n  C --> D["data cursors"]\n  W --> N["exact update 201"]\n  O --> N\n  S --> N\n  R --> N\n  D --> N\n```\n\n```text\nweights alone restore a model; complete state restores an experiment\n```''',
196: '''```mermaid\nflowchart TD\n  L["current loss and gradient norm"] --> Z["compare with robust recent baseline"]\n  Z --> P{"persistent and corroborated?"}\n  P -->|"no"| KEEP["preserve event; continue monitoring"]\n  P -->|"yes"| SAVE["quarantine batch + diagnose"] --> R["restore verified checkpoint"]\n```\n\n```text\none hard batch:  spike -> normal\ndivergence:      spike -> high -> higher + gradient growth\n```''',
197: '''```mermaid\nflowchart LR\n  C["checkpoint"] --> F["held-out field reports"]\n  C --> S["held-out science"]\n  C --> B["held-out books"]\n  C --> W["held-out web"]\n  F --> DASH["per-domain validation history"]\n  S --> DASH\n  B --> DASH\n  W --> DASH\n```\n\n```text\nglobal average down can still hide field-report loss up\n```''',
198: '''```mermaid\nflowchart LR\n  C1["synthetic canary seen once"] --> R1["rank 100,000"] --> E1["low exposure"]\n  C2["synthetic canary repeated 100×"] --> R2["rank 10"] --> E2["high exposure"]\n  E2 --> P["trace repetition through provenance"]\n```\n\n```text\nknown synthetic secret -> measured rank -> authorized extraction audit\n```''',
199: '''```mermaid\nflowchart TB\n  DATA["corpus + provenance"] --> REPORT["training report"]\n  RUN["tokens + compute + interruptions"] --> REPORT\n  EVAL["domain validation + memorization"] --> REPORT\n  GOV["intended use + limits + approval"] --> REPORT\n  REPORT --> ART["artifact hash"]\n```\n\n```text\nweights answer prompts; the report answers what produced and bounded them\n```''',
200: '''```mermaid\nflowchart LR\n  M["signed manifest"] --> C["boundary-aware curation"] --> MIX["audited mixture"] --> B["token + compute budget"]\n  B --> TRAIN["measured distributed training"] --> CKPT["atomic resumable checkpoints"] --> V["validation + memorization audits"] --> G{"all release gates"}\n  G -->|"pass"| R["versioned reversible release"]\n  G -->|"fail"| LOOP["return to bounded research loop"]\n```\n\n```text\nno stage can average away a failed provenance, privacy, recovery, or release gate\n```''',
}


def wrap_python(source,n):
    return f'"""Excavation {n:03d}: dependency-free evidence for this chapter.\n"""\n\n{source}\n\nif __name__ == "__main__":\n    print(demo())\n'


def numpy_code(n):
    return f'"""Excavation {n:03d}: NumPy form of the chapter experiment.\n"""\nimport numpy as np\n\n{NUMPY[n]}\n'


def torch_code(n):
    return f'''"""Excavation {n:03d}: PyTorch form of the chapter experiment."""
try:
    import torch
except ImportError:
    raise SystemExit("Install PyTorch to run this stage.")

{TORCH[n]}
'''


def main():
    for row in ROWS:
        n,slug,title,carry,attempt,failure,repair,case,limit,formula,terms,operations,refs=row
        folder=ROOT/"excavations"/f"{n:03d}-{slug}"
        (folder/"implementation").mkdir(parents=True,exist_ok=True)
        (folder/"images").mkdir(exist_ok=True)
        (folder/"README.md").write_text(chapter(row))
        (folder/"mistakes.md").write_text(f"# Mistakes — Excavation {n:03d}\n\n## Tempting idea\n\n{attempt.capitalize()}.\n\n## Evidence that breaks it\n\n{failure}\n\n## Requirement carried forward\n\n{repair}\n\nThe wrong idea remains because its failure exposes information the successful design must preserve.\n")
        (folder/"diagram.md").write_text(f"# Diagram — {title}\n\n{DIAGRAMS[n]}\n")
        (folder/"exercises.md").write_text(f"# Invention Exercises — Excavation {n:03d}\n\n1. Reconstruct the tempting design without using the accepted method's name: {attempt}.\n2. Create the smallest named corpus or training run that makes this failure visible: {failure}\n3. Explain why the chosen operation answers the job and why its nearest alternative does not.\n4. Change one concrete value from the chapter, predict the new intermediate result, and then run `implementation/pure_python.py`.\n5. Design an audit for this remaining limitation: {limit}\n")
        references="\n".join(f"- [{name}]({url}) — primary source for the mechanism, evidence, or limitation reconstructed here." for name,url in refs)
        (folder/"references.md").write_text(f"# Primary Research Trail — {title}\n\n{references}\n\nRead the excavation first. Use these sources afterward to inspect assumptions, empirical evidence, and limitations behind the standard name.\n")
        (folder/"images"/"README.md").write_text(f"# Visual Brief — {title}\n\nIllustrate the same ranger-station corpus and training run in two states. The first must make the lost provenance, false boundary, duplicated evidence, wasted compute, disagreement, or unrecoverable state visible. Reveal the repair only in the second state. Do not substitute generic neural-network boxes for the concrete documents, workers, shards, or measurements in this excavation.\n")
        (folder/"implementation"/"README.md").write_text(f"# Build Excavation {n:03d} Three Times\n\n1. [`pure_python.py`](pure_python.py) makes every decision visible with ordinary values, dictionaries, sets, and loops.\n2. [`numpy.py`](numpy.py) performs this chapter's same measurement over arrays.\n3. [`pytorch.py`](pytorch.py) expresses the same mechanism with tensors suitable for a training system.\n\nRun Pure Python first. State what should fail and what should remain invariant before using a library.\n")
        (folder/"implementation"/"pure_python.py").write_text(wrap_python(PURE[n],n))
        (folder/"implementation"/"numpy.py").write_text(numpy_code(n))
        (folder/"implementation"/"pytorch.py").write_text(torch_code(n))
    print("Built Excavations 176–200 with chapters, specific diagrams, companions, and three implementation stages.")


if __name__=="__main__":
    main()
