# Volume V — We Account for Pretraining

The modern engine can run. We now build the accountable factory around it: traceable evidence, explicit curation, budgeted learning, coordinated workers, recoverable state, independent audits, and a report that remains attached to the final artifact.

One discovery will create the need for the next; the object under construction never resets.

In this volume:

- [Part XIII — A Pretraining Factory We Can Account For](#part-xiii--a-pretraining-factory-we-can-account-for)

---

## Part XIII — A Pretraining Factory We Can Account For

The model is modern but still empty of trustworthy experience. We follow one named corpus from its source documents through boundaries, curation, mixture decisions, compute budgets, distributed training, recovery, validation, memorization audits, and a reversible release.

---

### Excavation 176 — A Corpus Manifest — Know What Entered the Run

The modern tiny language-model engine preserves a reference path through training and serving. It still cannot explain which documents will shape its weights, because no corpus has been frozen as part of the experiment.

Perhaps we copy every available text file into one large folder and begin tokenizing.

But the run answers back. A file is replaced upstream, another is silently skipped, and a third appears twice under different paths. The same training command now describes a different body of evidence.

The failure leaves one precise requirement. Create an immutable manifest that records each source, version, content hash, license or usage basis, processing stage, and document count before any training shard exists.

The ranger station records `field-reports/v3`, its retrieval date, 8,412 documents, and the hash of its manifest. A later run can prove whether it used the same evidence.

A manifest makes the corpus accountable; it cannot prove that every recorded document is suitable, lawful, accurate, or harmless.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/176-corpus-manifest/README.md).*

---

### Excavation 177 — Document Boundaries — Keep One Story from Leaking into Another

The manifest fixes which source documents belong to the run. Tokenization can still concatenate them into a stream where the ending of one document predicts the beginning of an unrelated one.

We first try to join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width.

That confidence lasts only until the first measurement. A ranger report ending with “tiger tracks near” is trained to predict the first word of an unrelated software license. The model receives a relationship that never existed in either document.

What broke tells us what the next design must preserve. Mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended.

Two short documents share one packed row, but a boundary mask lets each token read only tokens from its own document. The empty hardware space is saved without inventing a false continuation.

A_ij answers one concrete yes-or-no question for token positions i and j: may information cross between them? One means the pair shares a document; zero means the boundary forbids the connection.

##### Why these operations are forced

[Cases](../MATHEMATICAL_MOVES.md#cases) are forced because same-document and cross-document pairs obey different rules. [Equality](../MATHEMATICAL_MOVES.md#equals) assigns an exact permission bit. A distance score would blur a categorical boundary, while addition would invent partial permission.

Only now can we compress the procedure:

$$
A_{ij}=\begin{cases}1&\text{tokens }i,j\text{ share a document}\\0&\text{otherwise}\end{cases}
$$

Boundary isolation prevents accidental cross-document lessons; it cannot decide whether two paragraphs really belong to the same source document.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/177-document-boundaries/README.md).*

---

### Excavation 178 — Language Identification — Do Not Confuse Familiar Script with Familiar Language

Document boundaries now preserve honest local context. The manifest still mixes languages, code, names, and corrupted text, so a declared English run cannot yet tell what language evidence it actually contains.

One tempting answer is to keep documents containing mostly familiar Latin characters and discard the rest.

The shortcut reaches its first real document and breaks. Spanish and Vietnamese are mistaken for English, transliterated languages disappear, and English code or identifier lists pass despite containing little natural language.

Now the missing job can be stated plainly. Use a calibrated language classifier, retain its confidence and model version, and route uncertain documents to an explicit unknown bucket rather than forcing a label.

A field report receives English 0.93, Spanish 0.05, and unknown 0.02. The pipeline keeps English only because its score clears the recorded threshold; a 0.44/0.41 split is quarantined.

d is the document being inspected; the set L contains allowed language labels; p(l|d) is the classifier's support for one label; l-star is the label whose support is largest.

##### Why these operations are forced

[Conditional probability](../MATHEMATICAL_MOVES.md#conditional-bar) asks for language support given this document. [Arg max](../MATHEMATICAL_MOVES.md#arg-max) keeps the winning label rather than only its score. Summing the scores would erase which language produced them; a threshold is still checked afterward because the winner may be weak.

Only now can we compress the procedure:

$$
\ell^*=\underset{\ell\in\mathcal L}{\mathrm{argmax}}\ p(\ell\mid d)
$$

Because the classifier learned from finite examples and reduces a mixed document to one distribution, language identification remains probabilistic and domain-sensitive; short, multilingual, and code-heavy documents are especially difficult.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/178-language-identification/README.md).*

---

### Excavation 179 — Exact Deduplication — Stop Paying Twice for the Same Document

Language labels make the intended corpus measurable. Counting the accepted files now reveals identical reports mirrored across archives and repeated under new filenames.

At first we leave duplicates in place because more training examples should always help.

Reality objects. One press release copied to a thousand sites receives a thousand votes, while a rare field observation receives one. Compute is spent memorizing repetition rather than encountering new evidence.

That evidence forces a repair. Normalize only irrelevant formatting, hash the resulting document, and keep one accountable representative for each identical hash while preserving duplicate counts in the ledger.

Three files differ only in line endings and trailing spaces. After recorded normalization they produce the same fingerprint, so one enters training and the manifest records three original locations.

d is the original tiger field-report document, N performs the recorded normalization, H is a deterministic content-hash function, and h(d) is the fingerprint used to group exact copies.

##### Why these operations are forced

[Function composition](../MATHEMATICAL_MOVES.md#function-composition) fixes the order: normalize first, hash second. Reversing the order leaves irrelevant byte differences visible. [Equality](../MATHEMATICAL_MOVES.md#equals) groups only matching fingerprints; adding hashes has no interpretation and would not identify copies.

Only now can we compress the procedure:

$$
h(d)=H(N(d))
$$

Because a cryptographic hash reacts to any retained content change, exact hashes catch identical normalized text but give a copied article with one inserted advertisement a different fingerprint.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/179-exact-deduplication/README.md).*

---

### Excavation 180 — Near Deduplication — When a Copy Changes a Few Words

Exact deduplication removes byte-equivalent documents. The copied article with a new banner, reordered footer, or one edited sentence still survives as apparently new evidence.

Using what we have, we lowercase both documents and demand that every remaining word match.

The plan survives only until the evidence is counted. One inserted advertisement defeats the rule, while independently written short notices can match by accident. Exact sequence equality is too brittle for disguised copies.

The lost information tells us what must come next. Represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale.

The original report has ten shingles; its mirrored copy shares eight and introduces two. Their intersection has eight shingles and their union has twelve, giving similarity 8/12 rather than pretending the documents are either perfectly equal or wholly unrelated.

A and B are the shingle sets from the original tiger report and its edited mirror. Their intersection counts phrases both contain; their union counts every distinct phrase appearing in either; J is the shared fraction.

##### Why these operations are forced

[Intersection](../MATHEMATICAL_MOVES.md#intersection) keeps shared evidence and [union](../MATHEMATICAL_MOVES.md#union) defines the total distinct evidence available. [Cardinality](../MATHEMATICAL_MOVES.md#cardinality) turns each set into a count. [Division](../MATHEMATICAL_MOVES.md#division) makes the overlap comparable across document lengths; a raw shared count would favor long documents.

Only now can we compress the procedure:

$$
J(A,B)=\frac{\lvert A\cap B\rvert}{\lvert A\cup B\rvert}
$$

Near-deduplication depends on shingle size and threshold; aggressive settings can erase legitimate quotations, templates, or independent accounts.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/180-near-deduplication/README.md).*

---

### Excavation 181 — Quality Filtering — Remove Noise Without Defining Humanity Away

Near-deduplication leaves a corpus with more distinct documents, not necessarily better ones. Some are navigation fragments, keyword piles, machine corruption, or adversarial spam.

An obvious shortcut is to keep only documents that resemble one prestigious encyclopedia.

Then the hidden cost becomes visible. The filter removes spam, but it also suppresses informal dialect, local knowledge, code, dialogue, and communities whose writing differs from the chosen reference.

Crossing that boundary requires one additional guarantee. Combine transparent structural signals with small controlled model-based tests, inspect what each threshold removes, and publish source-by-source retention counts before accepting a filter.

The station rejects a page with 70 percent repeated navigation and no sentences, but manually audits samples near the threshold and notices that short emergency bulletins need a different rule from essays.

Every quality filter encodes values and domain assumptions; measured downstream gains do not prove that excluded voices were unimportant.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/181-quality-filtering/README.md).*

---

### Excavation 182 — Data Provenance — Keep the Path Back to Every Source

Quality filtering produces an accepted set and a rejected set. Without a trace through each transformation, neither set can explain how a source document reached its decision.

Perhaps we save only the final cleaned text because intermediate metadata costs storage.

But the run answers back. A rights request, filtering bug, or benchmark contamination report arrives, but the final shard cannot be mapped back to the source record or processing rule that produced it.

The failure leaves one precise requirement. Assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard.

Document `river-0042` points to its source URL, retrieval time, raw hash, language decision, duplicate cluster, quality audit, redaction record, and final shard offset.

Provenance makes decisions inspectable; it cannot repair a source that was collected without sufficient rights, consent, or context.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/182-data-provenance/README.md).*

---

### Excavation 183 — PII Redaction — Do Not Turn Accidental Secrets into Lessons

Provenance can locate every retained document. Inspection now finds phone numbers, email addresses, account identifiers, and private-looking text embedded in otherwise useful pages.

We first try to remove any entire document containing a sequence that resembles personal information.

That confidence lasts only until the first measurement. One phone number erases a long public safety guide, while obfuscated addresses and context-dependent identifiers still pass. The rule destroys useful evidence without reliably removing the risky span.

What broke tells us what the next design must preserve. Detect candidate spans with several methods, classify them in context, replace confirmed sensitive spans with typed placeholders, and preserve only a restricted audit record of the decision.

The sentence “Call Maya at 555-0142 about the injured tiger” becomes “Call [PERSON] at [PHONE] about the injured tiger”; the grammatical lesson survives while the direct identifier does not.

Redaction has false positives and false negatives, and public availability does not by itself settle privacy, consent, or appropriate use.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/183-pii-redaction/README.md).*

---

### Excavation 184 — Data Mixtures — Decide Which Worlds Receive a Voice

Redaction reduces one preventable privacy risk. The clean sources still differ enormously in size: web pages could drown out books, code, science, and the station's rare field reports.

One tempting answer is to concatenate every accepted source and let its raw token count determine how often it appears.

The shortcut reaches its first real document and breaks. The largest crawl silently becomes the curriculum. A source ten thousand times smaller may almost never reach a batch even when it carries relationships absent from the web.

Now the missing job can be stated plainly. Choose and publish a probability weight for each domain, treating the mixture as an explicit modeling decision that must be tested on per-domain validation streams.

The station assigns 0.50 to curated web text, 0.20 to science, 0.15 to code, 0.10 to books, and 0.05 to field reports. The five shares exhaust one draw without pretending the sources are equally large or equally important.

D counts the named data domains and w_d is the chance that the next training draw chooses domain d. Nonnegative weights prevent negative sampling; a total of one exhausts all possible domain choices.

##### Why these operations are forced

[Summation](../MATHEMATICAL_MOVES.md#summation) combines mutually exclusive domain shares into the whole probability mass. Multiplication would make one zero-weight domain erase the mixture. [Equality](../MATHEMATICAL_MOVES.md#equals) requires a complete distribution, while the [inequality](../MATHEMATICAL_MOVES.md#inequalities) forbids impossible negative shares.

Only now can we compress the procedure:

$$
\sum_{d=1}^{D}w_d=1,\quad w_d\ge 0
$$

Mixture weights redistribute attention but cannot make a poor or missing domain representative, accurate, or safe.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/184-data-mixtures/README.md).*

---

### Excavation 185 — Mixture Sampling — Turn Planned Shares into a Reproducible Stream

The mixture weights state which domains should be heard. They do not yet produce a finite ordered token stream that every resumed worker can reconstruct.

At first we round each domain's desired share independently and concatenate the resulting blocks.

Reality objects. Independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero.

That evidence forces a repair. Use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source.

For 1,000 document draws, a 0.05 field-report weight expects about 50 selections. The seeded schedule interleaves those reports with other domains and records the actual count rather than promising exact equality by chance.

N is the total number of scheduled training draws, w_d is domain d's share, n_d is its realized count, and E[n_d] is the average count expected across many schedules.

##### Why these operations are forced

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) is forced because each of N draws independently offers domain d the same share w_d. Addition would grant a fixed number unrelated to run length. [Expectation](../MATHEMATICAL_MOVES.md#expectation) describes a long-run average, not a guarantee that one finite schedule equals Nw_d exactly.

Only now can we compress the procedure:

$$
E[n_d]=Nw_d
$$

Sampling realizes probabilities only approximately in a finite run, and replacement can repeat scarce documents enough to increase memorization.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/185-mixture-sampling/README.md).*

---

### Excavation 186 — The Token Budget — Convert a Training Plan into a Count of Lessons

Seeded mixture sampling can produce an ordered stream. The run still says “train for a while,” so neither cost nor source exposure is bounded.

Using what we have, we stop when the wall clock reaches an affordable date.

The plan survives only until the evidence is counted. Faster hardware sees more tokens, interruptions see fewer, and two runs with the same calendar budget teach different amounts of evidence.

The lost information tells us what must come next. Define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute.

A tiny run uses 2,000 updates with 32 sequences of 128 real tokens each. Every update carries 4,096 lessons, so the complete plan exposes 8,192,000 tokens.

T is the planned number of optimizer updates, B_tokens counts real loss-bearing tokens in one global batch, and N_tokens is the complete exposure budget.

##### Why these operations are forced

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) appears because every one of T updates consumes B_tokens lessons. Addition would count only one update plus one batch. Padding is excluded because it occupies hardware but contributes no language target.

Only now can we compress the procedure:

$$
N_{\text{tokens}}=T B_{\text{tokens}}
$$

Equal token counts do not imply equal compute when model size, sequence length, sparsity, or hardware efficiency differs.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/186-token-budget/README.md).*

---

### Excavation 187 — Compute-Optimal Allocation — Buy a Larger Memory or More Experience?

The token budget fixes how much evidence the model will see. A fixed compute allowance still permits a wider model trained on fewer tokens or a smaller model trained on more.

An obvious shortcut is to spend nearly the entire budget on parameter count because a larger model can store more patterns.

Then the hidden cost becomes visible. The large model is stopped after too little experience and remains undertrained, while much of its expensive capacity never receives enough varied evidence.

Crossing that boundary requires one additional guarantee. Estimate candidate parameter-and-token pairs under the same compute budget, run smaller scaling experiments, and choose the pair predicted to minimize held-out loss rather than maximizing either axis alone.

The station compares doubling parameters while halving tokens with keeping the smaller model and doubling tokens. Because both alter the same compute bill, held-out scaling runs decide which balance learns more.

P is the number of trainable model parameters, D is the number of training tokens, and C is a rough count of floating-point work for dense Transformer training; six summarizes forward and backward work per parameter-token interaction.

##### Why these operations are forced

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) is forced because every token exercises the model's parameters: doubling either P or D roughly doubles work. [Approximation](../MATHEMATICAL_MOVES.md#approximation) preserves the scaling relation while admitting architecture and implementation details. Adding P and D would combine incompatible units.

Only now can we compress the procedure:

$$
C\approx 6PD
$$

Compute-optimal estimates are empirical and depend on architecture, data quality, optimizer, and the inference cost the project can afford afterward.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/187-compute-optimal-allocation/README.md).*

---

### Excavation 188 — Learning-Rate Warmup — Let Adam Learn the Terrain Before Running

Compute allocation chooses the model and token horizon. At the first update, Adam's moment memories contain almost no history, while randomly initialized activations and gradients are changing fastest.

Perhaps we begin immediately at the peak learning rate chosen for the stable middle of training.

But the run answers back. The first noisy batches can make large updates before the optimizer's scale estimates become trustworthy, producing a loss spike that the later stable rate would not have caused.

The failure leaves one precise requirement. Increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule.

With peak rate 0.001 and 100 warmup updates, update 25 receives 0.00025, update 50 receives 0.0005, and update 100 finally reaches 0.001.

t is the current model warmup update, T_warm is the number of warmup updates, eta_peak is the intended stable rate, and eta_t is the smaller rate used now.

##### Why these operations are forced

[Division](../MATHEMATICAL_MOVES.md#division) turns elapsed warmup steps into a progress fraction from zero to one. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) applies that fraction to the peak rate. Adding t would mix step counts with a rate; jumping directly to eta_peak recreates the failed attempt.

Only now can we compress the procedure:

$$
\eta_t=\eta_{\text{peak}}\frac{t}{T_{\text{warm}}}\quad(0\le t\le T_{\text{warm}})
$$

Warmup reduces early shock but cannot rescue an unsuitable peak rate, broken initialization, corrupt batch, or incorrect optimizer state.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/188-learning-rate-warmup/README.md).*

---

### Excavation 189 — Cosine Decay — Make Late Corrections Smaller Without a Cliff

Warmup protects the optimizer's first steps. Keeping the peak rate for the entire token budget makes late updates as aggressive as early ones even when the model is refining rather than discovering broad structure.

We first try to drop the rate abruptly near the end of training.

That confidence lasts only until the first measurement. A sudden cliff changes update scale in one step and makes the chosen drop date an arbitrary discontinuity; dropping too early freezes useful learning.

What broke tells us what the next design must preserve. Decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state.

Halfway through decay, cosine is zero, so the rate sits halfway between its peak and minimum. At the final planned update, cosine reaches negative one and the rate reaches the minimum without a jump.

t is model-training progress through the decay interval of length T; eta_max and eta_min are its endpoint rates; cosine supplies a smooth path between them.

##### Why these operations are forced

[Subtraction](../MATHEMATICAL_MOVES.md#subtraction) isolates the adjustable rate range, [division](../MATHEMATICAL_MOVES.md#division) converts progress to a fraction, and [cosine](../MATHEMATICAL_MOVES.md#cosine) bends that fraction smoothly with flat endpoint slopes. Addition places the scaled range above eta_min. A raw linear drop is possible, but cosine avoids an abrupt endpoint slope.

Only now can we compress the procedure:

$$
\eta_t=\eta_{\min}+\frac{\eta_{\max}-\eta_{\min}}{2}\left(1+\cos\frac{\pi t}{T}\right)
$$

Cosine decay assumes a known horizon and is not automatically optimal when training is unexpectedly extended.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/189-cosine-decay/README.md).*

---

### Excavation 190 — Gradient Noise Scale — When More Examples Stop Buying More Direction

The schedule controls how far one global update moves. We still do not know how many examples should vote in that update before extra devices mostly repeat the same directional evidence.

One tempting answer is to make the global batch as large as the cluster permits.

The shortcut reaches its first real document and breaks. Early doubling reduces disagreement and improves the direction, but beyond a workload-dependent point the averaged gradient barely changes while each update consumes twice as many tokens.

Now the missing job can be stated plainly. Measure disagreement among micro-batch gradients relative to the strength of their shared direction, and use that noise scale as evidence for the largest useful batch rather than a hardware target.

Three named micro-batches question the same two weights: the field reports propose [2.0,1.0], science proposes [2.1,0.9], and books propose [1.9,1.1]. The first number is advice to the tiger-before-river weight; the second is advice to a punctuation weight. Their mean [2.0,1.0] is strong and their disagreement around it is small. If the witnesses instead propose [4,−2], [0,4], and [2,1], disagreement is large relative to the same broad direction, so a larger batch can still buy useful certainty.

Each g_i is one model micro-batch's gradient advice. The covariance measures how those witnesses disagree; its trace totals disagreement across coordinates. The squared norm of their mean measures the strength of the shared direction; G compares noise with signal.

##### Why these operations are forced

[Covariance](../MATHEMATICAL_MOVES.md#covariance) keeps variation around the common advice rather than raw gradient size. [Trace](../MATHEMATICAL_MOVES.md#trace) gathers coordinate variances without inventing cross-coordinate units. [Division](../MATHEMATICAL_MOVES.md#division) asks disagreement per unit of squared shared direction; subtraction would not remove dependence on signal scale.

Only now can we compress the procedure:

$$
G=\frac{\mathrm{tr}(\mathrm{Cov}[g_i])}{\lVert E[g_i]\rVert^2}
$$

Gradient noise scale is an empirical guide, not a universal batch-size law; it changes during training and with the task and optimizer.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/190-gradient-noise-scale/README.md).*

---

### Excavation 191 — Data Parallelism — Let Several Workers Observe Different Evidence

Gradient noise measurements choose a useful global batch. One device cannot process that batch quickly enough, even though the modern model and optimizer state now fit through sharding.

At first we send the same mini-batch to every worker and average their gradients.

Reality objects. All workers repeat the same computation and return the same evidence, so hardware cost rises without increasing batch diversity or reducing step time meaningfully.

That evidence forces a repair. Replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update.

Four workers each read eight different sequences. Their four average gradients become one average over thirty-two sequences before any worker advances the parameters.

P is the number of data-parallel workers, g_p is worker p's average gradient from different examples, and g is the single gradient used by the shared optimizer step.

##### Why these operations are forced

[Summation](../MATHEMATICAL_MOVES.md#summation) lets every worker's independent evidence contribute. [Division](../MATHEMATICAL_MOVES.md#division) returns advice per worker so adding hardware does not enlarge the update by itself. Multiplication would let a zero coordinate from one worker erase all others.

Only now can we compress the procedure:

$$
g=\frac1P\sum_{p=1}^{P}g_p
$$

Because one shared update cannot proceed until every worker's evidence has joined the average, synchronous data parallelism waits for the slowest worker and communicates a full update's worth of gradient information.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/191-data-parallelism/README.md).*

---

### Excavation 192 — Pipeline Parallelism — Stop Waiting for the Whole Model to Cross One Device at a Time

Data parallel workers process different examples, but each replica still needs the model's sequential layers. Splitting those layers across devices makes only one device active if a whole batch traverses the stages at once.

Using what we have, we send one complete batch through stage one, then stage two, then stage three.

The plan survives only until the evidence is counted. While stage two works, stage one and stage three wait. The model fits, but most devices are idle for most of the step.

The lost information tells us what must come next. Split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently.

With four pipeline stages and eight micro-batches, the first few clock slots fill the pipeline, eight slots carry useful work, and the last few drain it. More micro-batches shrink the idle fraction.

m is the number of model micro-batches and p the number of pipeline stages in a simple forward pipeline. Useful work occupies m slots; filling and draining add p−1 slots; U is the idealized occupied share.

##### Why these operations are forced

[Addition](../MATHEMATICAL_MOVES.md#addition) joins useful slots with unavoidable fill-and-drain slots. [Division](../MATHEMATICAL_MOVES.md#division) turns useful slots into a share of total schedule time. Multiplying m and p would count stage-tasks, not the fraction of time one stage remains usefully occupied.

Only now can we compress the procedure:

$$
U=\frac{m}{m+p-1}
$$

Because sequential layer dependencies require the pipeline to fill and drain, pipeline parallelism introduces bubbles and activation transfers; making micro-batches too small can then reduce the efficiency of each matrix operation.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/192-pipeline-parallelism/README.md).*

---

### Excavation 193 — Three-Dimensional Parallelism — Give Each Memory Wall Its Own Axis

Pipeline micro-batches keep layer stages busy. A large run may still exceed memory inside one layer, require more independent data witnesses, and contain too many layers for one device group.

An obvious shortcut is to increase whichever parallel technique was introduced most recently until the model fits.

Then the hidden cost becomes visible. More pipeline stages increase bubbles, more tensor splits increase frequent communication, and more data replicas preserve full model memory. One axis cannot solve three different limits efficiently.

Crossing that boundary requires one additional guarantee. Compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost.

Two tensor workers form each layer, four pipeline stages hold the depth, and three data replicas see different examples. The run uses 2×4×3=24 workers with each axis performing one named job.

Each factor counts independent choices along one model-parallel axis. Selecting one tensor rank, one pipeline rank, and one data rank identifies exactly one worker; P_total counts all such combinations.

##### Why these operations are forced

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) is forced by the product rule: every choice on one axis pairs with every choice on the others. Addition would count axis labels rather than workers. [Equality](../MATHEMATICAL_MOVES.md#equals) assumes the grid is fully populated.

Only now can we compress the procedure:

$$
P_{\text{total}}=P_{\text{tensor}}P_{\text{pipeline}}P_{\text{data}}
$$

Three-dimensional parallelism increases coordination and configuration complexity; a poor mapping to the physical network can spend more time communicating than computing.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/193-three-dimensional-parallelism/README.md).*

---

### Excavation 194 — Sharded Checkpoints — Save One Recoverable State Without Gathering It

Three-dimensional parallelism spreads parameters, moments, gradients, and progress across many owners. Asking one coordinator to gather everything before saving can exceed its memory and stall the cluster.

Perhaps we let every worker write its local tensors and call the directory a checkpoint.

But the run answers back. A worker fails before writing, two shards belong to different steps, or a filename is reused. The directory exists but cannot reconstruct one globally consistent training state.

The failure leaves one precise requirement. Write versioned shards to temporary locations, record hashes and ownership in a checkpoint manifest, and publish one atomic completion marker only after every required shard is durable.

Twenty-four workers save step 8,000. The manifest expects twenty-four parameter shards, optimizer shards, scheduler state, RNG state, and data cursors; the checkpoint becomes eligible for recovery only when every recorded hash verifies.

A complete checkpoint limits lost work but consumes storage and I/O bandwidth; frequent synchronous saves can dominate training time.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/194-sharded-checkpoints/README.md).*

---

### Excavation 195 — Deterministic Resume — Continue the Same Experiment, Not a Similar One

The sharded checkpoint can reconstruct every distributed tensor. If it omits the sampler cursor, random-number generators, scheduler phase, or overflow state, restart follows a different future.

We first try to restore model weights and let every other component start fresh.

That confidence lasts only until the first measurement. Adam forgets its moments, warmup may begin again, dropout chooses different masks, and data workers repeat or skip documents. The loss curve after restart cannot be attributed to the original run.

What broke tells us what the next design must preserve. Checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps.

The station stops after update 200, restores weights, Adam moments, schedule position, scaler, RNG streams, and each data cursor, then reproduces updates 201 through 205 byte for byte on the reference implementation.

Exact replay can still fail across nondeterministic kernels, changed hardware, libraries, or distributed timing; the required reproducibility level must be stated.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/195-deterministic-resume/README.md).*

---

### Excavation 196 — Loss Spikes — Distinguish One Hard Batch from a Run Leaving the Road

Deterministic resume makes failures reproducible. During a long run, the observed loss sometimes jumps; automatically rewinding every jump wastes compute, while ignoring a sustained instability can destroy the model.

One tempting answer is to declare any loss larger than the previous loss a failure and restore immediately.

The shortcut reaches its first real document and breaks. Ordinary batches vary, so healthy learning triggers constant rollbacks. A slow divergence can rise without one dramatic step and escape the rule.

Now the missing job can be stated plainly. Compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response.

Recent clean validation losses center near 2.0 with spread 0.1. One batch reaches 2.35 and then returns; another run stays above 2.5 while gradient norm grows. Only the persistent, corroborated event triggers recovery.

L_t is the current monitored model loss, mu_t is its robust recent center, sigma_t is ordinary recent spread, and z_t says how many usual spreads the current value lies above or below that center.

##### Why these operations are forced

[Subtraction](../MATHEMATICAL_MOVES.md#subtraction) removes the local baseline. [Division](../MATHEMATICAL_MOVES.md#division) expresses the remainder in units of ordinary variation, making different loss scales comparable. A raw threshold would behave differently as normal loss falls during training.

Only now can we compress the procedure:

$$
z_t=\frac{L_t-\mu_t}{\sigma_t}
$$

Thresholds detect symptoms, not causes; corrupt data, overflow, optimizer settings, hardware faults, and architectural instability require different repairs.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/196-loss-spike-recovery/README.md).*

---

### Excavation 197 — A Validation Stream — Ask Whether Learning Survives Outside the Current Batch

Loss-spike monitoring protects the training process from obvious instability. A smooth training curve can still improve mainly on repeated or overrepresented training domains.

At first we evaluate only the next training batch because it is already available.

Reality objects. The same data mixture and duplicates that shaped the update also judge it. Training loss can fall while held-out language or a rare domain becomes worse.

That evidence forces a repair. Maintain versioned, deduplicated, contamination-checked validation streams by domain and evaluate them at recorded token intervals without using them to update weights.

After every million training tokens, the station measures held-out field reports, science, books, code, and web text separately. A lower global average cannot hide that field-report loss rose.

The validation stream contains N honest next-token events. The model assigns the observed token x_i a conditional probability from its earlier context. Negative log turns confident neglect into positive cost, and L_val averages that cost across the stream.

##### Why these operations are forced

[Logarithms](../MATHEMATICAL_MOVES.md#logarithm) turn multiplied sequence probabilities into additive token costs. [Negative signs](../MATHEMATICAL_MOVES.md#negative-sign) make lower assigned probability cost more. [Summation](../MATHEMATICAL_MOVES.md#summation) lets every event contribute, and [division](../MATHEMATICAL_MOVES.md#division) makes streams of different lengths comparable.

Only now can we compress the procedure:

$$
L_{\text{val}}=-\frac1N\sum_{i=1}^{N}\log p_\theta(x_i\mid x_{<i})
$$

Validation detects only the distributions and behaviors represented in its finite streams; repeatedly tuning against it can eventually overfit it.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/197-validation-stream/README.md).*

---

### Excavation 198 — A Memorization Audit — Did the Model Learn a Pattern or Store a Passage?

Held-out validation shows whether prediction improves outside current batches. It does not reveal whether rare or repeated training sequences can be extracted verbatim from the model.

Using what we have, we ask the model whether it remembers private text and trust its answer.

The plan survives only until the evidence is counted. A model has no reliable introspective inventory of its training examples, and ordinary prompts may miss strings that an adversarial sampling strategy can recover.

The lost information tells us what must come next. Plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts.

The station inserts one synthetic radio code once and another code one hundred times. If the repeated code becomes far easier to rank and complete, the audit exposes the relationship between repetition and extractable memory without using a real secret.

R is the known space of possible synthetic canaries and rank is the tested canary's position when alternatives are ordered from most to least likely. Exposure measures how many bits of the search space the model has effectively removed.

##### Why these operations are forced

[Cardinality](../MATHEMATICAL_MOVES.md#cardinality) counts possible canaries. [Logarithms](../MATHEMATICAL_MOVES.md#logarithm) turn multiplicative changes in search space and rank into bits. [Subtraction](../MATHEMATICAL_MOVES.md#subtraction) removes the remaining search difficulty from the original difficulty; adding would reward a worse rank.

Only now can we compress the procedure:

$$
\mathrm{exposure}=\log_2\lvert\mathcal R\rvert-\log_2\mathrm{rank}
$$

A canary audit samples possible attacks and strings; passing it does not prove that no training data can be extracted.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/198-memorization-audit/README.md).*

---

### Excavation 199 — The Training Report — Preserve the Decisions, Not Only the Weights

Memorization auditing adds one essential limitation to the evaluation record. A released checkpoint still cannot explain its corpus, mixture, compute, interruptions, exclusions, intended uses, or known failures by inspecting weight tensors.

An obvious shortcut is to publish the final benchmark table and assume the configuration files explain the rest.

Then the hidden cost becomes visible. A score has no visible data lineage, uncertainty, subgroup behavior, energy or hardware context, incident history, or warning about uses the evaluation never tested.

Crossing that boundary requires one additional guarantee. Generate a training report from manifests and logs, then add human-reviewed explanations of intended use, out-of-scope use, limitations, incidents, provenance, evaluation conditions, and responsible release decisions.

The station's report names corpus and code versions, tokens seen, mixture shares, compute, checkpoint recoveries, per-domain validation, memorization probes, excluded sources, and the exact model artifact hash.

Documentation improves accountability but can be incomplete, outdated, misleading, or ignored; claims still require inspectable evidence.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/199-training-report/README.md).*

---

### Excavation 200 — A Tiny Pretraining Factory — Close the Accountable Training Loop

The training report can explain one finished run. We have now earned all the mechanisms needed to make the next run reconstructable from source documents to final artifact rather than relying on memory and scattered scripts.

Perhaps we connect every tool into one automatic pipeline and trust any run that reaches the final stage.

But the run answers back. Automation can faithfully repeat a wrong manifest, destructive filter, contaminated validation set, incomplete checkpoint, or unauthorized release. Completion is not evidence of correctness.

The failure leaves one precise requirement. Assemble signed stage manifests, boundary-aware curation, audited mixtures, fixed budgets, measured schedules, distributed equivalence tests, atomic checkpoints, live validation, memorization probes, and human release gates into one reversible factory.

A tiny run begins from ten named documents, records every acceptance and removal, trains a reproducible model, survives an intentional interruption, reproduces its next updates, generates its report, and refuses release when the memorization gate fails.

The factory is accountable, not omniscient. New sources, laws, hardware, attacks, and uses create new failures that must return to observation and the bounded research loop.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/200-tiny-pretraining-factory/README.md).*
