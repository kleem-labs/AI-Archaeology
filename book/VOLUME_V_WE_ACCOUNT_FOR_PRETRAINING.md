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

<!-- book-prose-v2 -->

The modern tiny language-model engine preserves a reference path through training and serving. It still cannot explain which documents will shape its weights, because no corpus has been frozen as part of the experiment.

The first defensible move is to copy every available text file into one large folder and begin tokenizing.

There is a real principle behind this restraint: the complexity of a corpus manifest must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Now keep that rule fixed and let the difficult case enter: a file is replaced upstream, another is silently skipped, and a third appears twice under different paths. The same training command now describes a different body of evidence.

That distinction is the hinge on which a corpus manifest turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: create an immutable manifest that records each source, version, content hash, license or usage basis, processing stage, and document count before any training shard exists.

We have earned the chapter's shorter name: **A Corpus Manifest**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that a corpus manifest is necessary rather than decorative. Delete its new responsibility and use the earlier plan to copy every available text file into one large folder and begin tokenizing. Immediately, a file is replaced upstream, another is silently skipped, and a third appears twice under different paths. The same training command now describes a different body of evidence. Reintroduce the single job to create an immutable manifest that records each source, version, content hash, license or usage basis, processing stage, and document count before any training shard exists. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can create an immutable manifest that records each source, version, content hash, license or usage basis, processing stage, and document count before any training shard exists. Because the old plan to copy every available text file into one large folder and begin tokenizing is the only displaced piece, the reader can locate exactly where a corpus manifest changes the outcome.

#### Know What Entered the Run

The ranger station records `field-reports/v3`, its retrieval date, 8,412 documents, and the hash of its manifest. A later run can prove whether it used the same evidence.

The name a corpus manifest is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### Where a corpus manifest runs out

A manifest makes the corpus accountable; it cannot prove that every recorded document is suitable, lawful, accurate, or harmless.

The weakness is not an accidental footnote. Every operation in a corpus manifest serves the narrower purpose to create an immutable manifest that records each source, version, content hash, license or usage basis, processing stage, and document count before any training shard exists; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take a corpus manifest to the workbench

Understanding a corpus manifest now means predicting its intermediate results before asking software for an answer. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running a corpus manifest, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the a corpus manifest result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/176-corpus-manifest/README.md).*

---

### Excavation 177 — Document Boundaries — Keep One Story from Leaking into Another

<!-- book-prose-v2 -->

The manifest fixes which source documents belong to the run. Tokenization can still concatenate them into a stream where the ending of one document predicts the beginning of an unrelated one.

At this point the shortest path seems to be to join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width.

This is how document boundaries ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

The world supplies the one comparison the shortcut hoped never to face: a ranger report ending with “tiger tracks near” is trained to predict the first word of an unrelated software license. The model receives a relationship that never existed in either document.

The wrong answer makes the need for document boundaries inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended.

The usual name, **Document Boundaries**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width produces the observed failure: a ranger report ending with “tiger tracks near” is trained to predict the first word of an unrelated software license. The model receives a relationship that never existed in either document. Starting with the repaired demand to mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended preserves the information the shortcut lost. The subject of document boundaries lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended instead of merely trying to join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width. That controlled contrast is what turns a plausible explanation of document boundaries into an understandable derivation.

#### Keep One Story from Leaking into Another

Two short documents share one packed row, but a boundary mask lets each token read only tokens from its own document. The empty hardware space is saved without inventing a false continuation.

There are now two histories of this document boundaries case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

#### The calculation hidden inside document boundaries

Before Document Boundaries receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

A_ij answers one concrete yes-or-no question for token positions i and j: may information cross between them? One means the pair shares a document; zero means the boundary forbids the connection.

##### Why no cheaper operation does the same job

[Cases](../MATHEMATICAL_MOVES.md#cases) are forced because same-document and cross-document pairs obey different rules. [Equality](../MATHEMATICAL_MOVES.md#equals) assigns an exact permission bit. A distance score would blur a categorical boundary, while addition would invent partial permission.

Every symbol in Document Boundaries can now be read back into an action already performed. The whole procedure fits in one line:

$$
A_{ij}=\begin{cases}1&\text{tokens }i,j\text{ share a document}\\0&\text{otherwise}\end{cases}
$$

#### Where document boundaries runs out

Boundary isolation prevents accidental cross-document lessons; it cannot decide whether two paragraphs really belong to the same source document.

Look back at what document boundaries actually preserves: it can mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

#### Take document boundaries to the workbench

The reader has reconstructed document boundaries in words; the workbench tests whether those words specify a real procedure. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running document boundaries, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the document boundaries result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/177-document-boundaries/README.md).*

---

### Excavation 178 — Language Identification — Do Not Confuse Familiar Script with Familiar Language

<!-- book-prose-v2 -->

Document boundaries now preserve honest local context. The manifest still mixes languages, code, names, and corrupted text, so a declared English run cannot yet tell what language evidence it actually contains.

We can postpone invention if we simply keep documents containing mostly familiar Latin characters and discard the rest.

If the proposal works on every relevant case, language identification is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

Its hidden assumption becomes visible as soon as we observe that spanish and Vietnamese are mistaken for English, transliterated languages disappear, and English code or identifier lists pass despite containing little natural language.

Nothing magical creates language identification. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: use a calibrated language classifier, retain its confidence and model version, and route uncertain documents to an explicit unknown bucket rather than forcing a label.

This boundary between the failed rule and its repair is the subject later work calls **Language Identification**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize language identification; try to break it by subtraction. Remove the part that knows how to use a calibrated language classifier, retain its confidence and model version, and route uncertain documents to an explicit unknown bucket rather than forcing a label, leaving only the attempt to keep documents containing mostly familiar Latin characters and discard the rest. What returns is not a vague weakness but the original contradiction: spanish and Vietnamese are mistaken for English, transliterated languages disappear, and English code or identifier lists pass despite containing little natural language. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to keep documents containing mostly familiar Latin characters and discard the rest receives the same test as the rule to use a calibrated language classifier, retain its confidence and model version, and route uncertain documents to an explicit unknown bucket rather than forcing a label. Their different outcomes reveal what language identification contributes without asking the reader to trust historical convention.

#### Do Not Confuse Familiar Script with Familiar Language

A field report receives English 0.93, Spanish 0.05, and unknown 0.02. The pipeline keeps English only because its score clears the recorded threshold; a 0.44/0.41 split is quarantined.

Hold the setting, evidence, and desired outcome fixed while testing language identification. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

#### The calculation hidden inside language identification

Do not read the coming Language Identification line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

d is the document being inspected; the set L contains allowed language labels; p(l|d) is the classifier's support for one label; l-star is the label whose support is largest.

##### Why no cheaper operation does the same job

[Conditional probability](../MATHEMATICAL_MOVES.md#conditional-bar) asks for language support given this document. [Arg max](../MATHEMATICAL_MOVES.md#arg-max) keeps the winning label rather than only its score. Summing the scores would erase which language produced them; a threshold is still checked afterward because the winner may be weak.

Every symbol in Language Identification can now be read back into an action already performed. The whole procedure fits in one line:

$$
\ell^*=\underset{\ell\in\mathcal L}{\mathrm{argmax}}\ p(\ell\mid d)
$$

#### Where language identification runs out

Because the classifier learned from finite examples and reduces a mixed document to one distribution, language identification remains probabilistic and domain-sensitive; short, multilingual, and code-heavy documents are especially difficult.

This is where language identification runs out for a causal reason. We gave it enough structure to use a calibrated language classifier, retain its confidence and model version, and route uncertain documents to an explicit unknown bucket rather than forcing a label, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take language identification to the workbench

A mathematical story about language identification earns trust only when the failed and repaired paths can both be reproduced. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running language identification, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the language identification result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/178-language-identification/README.md).*

---

### Excavation 179 — Exact Deduplication — Stop Paying Twice for the Same Document

<!-- book-prose-v2 -->

Language labels make the intended corpus measurable. Counting the accepted files now reveals identical reports mirrored across archives and repeated under new filenames.

The previous discovery seems almost sufficient: we could leave duplicates in place because more training examples should always help.

The shortcut appears to retain everything exact deduplication needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

Then a case arrives in which convenience and truth separate: one press release copied to a thousand sites receives a thousand votes, while a rare field observation receives one. Compute is spent memorizing repetition rather than encountering new evidence.

The counterexample teaches exact deduplication. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: normalize only irrelevant formatting, hash the resulting document, and keep one accountable representative for each identical hash while preserving duplicate counts in the ledger.

Now—and not earlier—we may introduce **Exact Deduplication**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to leave duplicates in place because more training examples should always help, and the case answers that one press release copied to a thousand sites receives a thousand votes, while a rare field observation receives one. Compute is spent memorizing repetition rather than encountering new evidence. With the narrow repair—to normalize only irrelevant formatting, hash the resulting document, and keep one accountable representative for each identical hash while preserving duplicate counts in the ledger—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Exact Deduplication returns to the same counterexample, replaces the attempt to leave duplicates in place because more training examples should always help with the responsibility to normalize only irrelevant formatting, hash the resulting document, and keep one accountable representative for each identical hash while preserving duplicate counts in the ledger, and must succeed where the shortcut failed.

#### Stop Paying Twice for the Same Document

Three files differ only in line endings and trailing spaces. After recorded normalization they produce the same fingerprint, so one enters training and the manifest records three original locations.

A formula for exact deduplication is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

#### The calculation hidden inside exact deduplication

Before Exact Deduplication receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

d is the original tiger field-report document, N performs the recorded normalization, H is a deterministic content-hash function, and h(d) is the fingerprint used to group exact copies.

##### Why no cheaper operation does the same job

[Function composition](../MATHEMATICAL_MOVES.md#function-composition) fixes the order: normalize first, hash second. Reversing the order leaves irrelevant byte differences visible. [Equality](../MATHEMATICAL_MOVES.md#equals) groups only matching fingerprints; adding hashes has no interpretation and would not identify copies.

Every symbol in Exact Deduplication can now be read back into an action already performed. The whole procedure fits in one line:

$$
h(d)=H(N(d))
$$

#### Where exact deduplication runs out

Because a cryptographic hash reacts to any retained content change, exact hashes catch identical normalized text but give a copied article with one inserted advertisement a different fingerprint.

The boundary can be predicted from the construction itself. Exact Deduplication performs the repair to normalize only irrelevant formatting, hash the resulting document, and keep one accountable representative for each identical hash while preserving duplicate counts in the ledger; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

#### Take exact deduplication to the workbench

Move exact deduplication from imagination to evidence by making the shortcut fail under controlled inputs. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running exact deduplication, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the exact deduplication result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/179-exact-deduplication/README.md).*

---

### Excavation 180 — Near Deduplication — When a Copy Changes a Few Words

<!-- book-prose-v2 -->

Exact deduplication removes byte-equivalent documents. The copied article with a new banner, reordered footer, or one edited sentence still survives as apparently new evidence.

The least expensive next move is to lowercase both documents and demand that every remaining word match.

The proposal deserves a fair hearing. For near deduplication, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The proposal breaks for a specific reason, not by authority: one inserted advertisement defeats the rule, while independently written short notices can match by accident. Exact sequence equality is too brittle for disguised copies.

The failure changes the question behind near deduplication. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale.

Only at this point does the inherited name **Near Deduplication** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of near deduplication by mentally removing the repair. We fall back to the proposal to lowercase both documents and demand that every remaining word match; then one inserted advertisement defeats the rule, while independently written short notices can match by accident. Exact sequence equality is too brittle for disguised copies. Restore only the ability to represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to lowercase both documents and demand that every remaining word match to requiring the system to represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to near deduplication.

#### When a Copy Changes a Few Words

The original report has ten shingles; its mirrored copy shares eight and introduces two. Their intersection has eight shingles and their union has twelve, giving similarity 8/12 rather than pretending the documents are either perfectly equal or wholly unrelated.

Put the old procedure beside near deduplication. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

#### The calculation hidden inside near deduplication

Do not read the coming Near Deduplication line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

A and B are the shingle sets from the original tiger report and its edited mirror. Their intersection counts phrases both contain; their union counts every distinct phrase appearing in either; J is the shared fraction.

##### Why no cheaper operation does the same job

[Intersection](../MATHEMATICAL_MOVES.md#intersection) keeps shared evidence and [union](../MATHEMATICAL_MOVES.md#union) defines the total distinct evidence available. [Cardinality](../MATHEMATICAL_MOVES.md#cardinality) turns each set into a count. [Division](../MATHEMATICAL_MOVES.md#division) makes the overlap comparable across document lengths; a raw shared count would favor long documents.

Every symbol in Near Deduplication can now be read back into an action already performed. The whole procedure fits in one line:

$$
J(A,B)=\frac{\lvert A\cap B\rvert}{\lvert A\cup B\rvert}
$$

#### Where near deduplication runs out

Near-deduplication depends on shingle size and threshold; aggressive settings can erase legitimate quotations, templates, or independent accounts.

The limit follows from the job assigned to near deduplication. Its repair knows how to represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

#### Take near deduplication to the workbench

A claim about near deduplication now exists on the page; the laboratory must be able to contradict it. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running near deduplication, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the near deduplication result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/180-near-deduplication/README.md).*

---

### Excavation 181 — Quality Filtering — Remove Noise Without Defining Humanity Away

<!-- book-prose-v2 -->

Near-deduplication leaves a corpus with more distinct documents, not necessarily better ones. Some are navigation fragments, keyword piles, machine corruption, or adversarial spam.

For a moment, remain loyal to the simplest proposal: keep only documents that resemble one prestigious encyclopedia.

Its appeal is not ignorance but economy. Quality Filtering should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Reality now asks a question the retained information cannot answer: the filter removes spam, but it also suppresses informal dialect, local knowledge, code, dialogue, and communities whose writing differs from the chosen reference.

Notice what the counterexample has accomplished for quality filtering. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: combine transparent structural signals with small controlled model-based tests, inspect what each threshold removes, and publish source-by-source retention counts before accepting a filter.

Humanity eventually gathered this problem and its repairs under the name **Quality Filtering**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace quality filtering with the old instruction to keep only documents that resemble one prestigious encyclopedia. The result is again that the filter removes spam, but it also suppresses informal dialect, local knowledge, code, dialogue, and communities whose writing differs from the chosen reference. Put back only the requirement to combine transparent structural signals with small controlled model-based tests, inspect what each threshold removes, and publish source-by-source retention counts before accepting a filter. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when quality filtering is introduced. The same evidence that defeated the attempt to keep only documents that resemble one prestigious encyclopedia is presented again. Only the ability to combine transparent structural signals with small controlled model-based tests, inspect what each threshold removes, and publish source-by-source retention counts before accepting a filter changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### Remove Noise Without Defining Humanity Away

The station rejects a page with 70 percent repeated navigation and no sentences, but manually audits samples near the threshold and notices that short emergency bulletins need a different rule from essays.

Run the quality filtering scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

#### Where quality filtering runs out

Every quality filter encodes values and domain assumptions; measured downstream gains do not prove that excluded voices were unimportant.

Why does that boundary remain? Quality Filtering was built for one responsibility: combine transparent structural signals with small controlled model-based tests, inspect what each threshold removes, and publish source-by-source retention counts before accepting a filter. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take quality filtering to the workbench

The argument for quality filtering is still provisional until a runnable case can make it fail. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running quality filtering, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the quality filtering result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/181-quality-filtering/README.md).*

---

### Excavation 182 — Data Provenance — Keep the Path Back to Every Source

<!-- book-prose-v2 -->

Quality filtering produces an accepted set and a rejected set. Without a trace through each transformation, neither set can explain how a source document reached its decision.

Nothing yet appears to demand a new invention. We can save only the final cleaned text because intermediate metadata costs storage.

There is a real principle behind this restraint: the complexity of data provenance must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The decisive test is this: a rights request, filtering bug, or benchmark contamination report arrives, but the final shard cannot be mapped back to the source record or processing rule that produced it.

That distinction is the hinge on which data provenance turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard.

We have earned the chapter's shorter name: **Data Provenance**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that data provenance is necessary rather than decorative. Delete its new responsibility and use the earlier plan to save only the final cleaned text because intermediate metadata costs storage. Immediately, a rights request, filtering bug, or benchmark contamination report arrives, but the final shard cannot be mapped back to the source record or processing rule that produced it. Reintroduce the single job to assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard. Because the old plan to save only the final cleaned text because intermediate metadata costs storage is the only displaced piece, the reader can locate exactly where data provenance changes the outcome.

#### Keep the Path Back to Every Source

Document `river-0042` points to its source URL, retrieval time, raw hash, language decision, duplicate cluster, quality audit, redaction record, and final shard offset.

The name data provenance is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### Where data provenance runs out

Provenance makes decisions inspectable; it cannot repair a source that was collected without sufficient rights, consent, or context.

The weakness is not an accidental footnote. Every operation in data provenance serves the narrower purpose to assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take data provenance to the workbench

Understanding data provenance now means predicting its intermediate results before asking software for an answer. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running data provenance, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the data provenance result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/182-data-provenance/README.md).*

---

### Excavation 183 — PII Redaction — Do Not Turn Accidental Secrets into Lessons

<!-- book-prose-v2 -->

Provenance can locate every retained document. Inspection now finds phone numbers, email addresses, account identifiers, and private-looking text embedded in otherwise useful pages.

The machinery already in our hands suggests that we remove any entire document containing a sequence that resembles personal information.

This is how pii redaction ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

One counterexample is enough to expose the missing job: one phone number erases a long public safety guide, while obfuscated addresses and context-dependent identifiers still pass. The rule destroys useful evidence without reliably removing the risky span.

The wrong answer makes the need for pii redaction inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: detect candidate spans with several methods, classify them in context, replace confirmed sensitive spans with typed placeholders, and preserve only a restricted audit record of the decision.

The usual name, **PII Redaction**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to remove any entire document containing a sequence that resembles personal information produces the observed failure: one phone number erases a long public safety guide, while obfuscated addresses and context-dependent identifiers still pass. The rule destroys useful evidence without reliably removing the risky span. Starting with the repaired demand to detect candidate spans with several methods, classify them in context, replace confirmed sensitive spans with typed placeholders, and preserve only a restricted audit record of the decision preserves the information the shortcut lost. The subject of pii redaction lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to detect candidate spans with several methods, classify them in context, replace confirmed sensitive spans with typed placeholders, and preserve only a restricted audit record of the decision instead of merely trying to remove any entire document containing a sequence that resembles personal information. That controlled contrast is what turns a plausible explanation of pii redaction into an understandable derivation.

#### Do Not Turn Accidental Secrets into Lessons

The sentence “Call Maya at 555-0142 about the injured tiger” becomes “Call [PERSON] at [PHONE] about the injured tiger”; the grammatical lesson survives while the direct identifier does not.

There are now two histories of this pii redaction case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

#### Where pii redaction runs out

Redaction has false positives and false negatives, and public availability does not by itself settle privacy, consent, or appropriate use.

Look back at what pii redaction actually preserves: it can detect candidate spans with several methods, classify them in context, replace confirmed sensitive spans with typed placeholders, and preserve only a restricted audit record of the decision. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

#### Take pii redaction to the workbench

The reader has reconstructed pii redaction in words; the workbench tests whether those words specify a real procedure. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running pii redaction, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the pii redaction result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/183-pii-redaction/README.md).*

---

### Excavation 184 — Data Mixtures — Decide Which Worlds Receive a Voice

<!-- book-prose-v2 -->

Redaction reduces one preventable privacy risk. The clean sources still differ enormously in size: web pages could drown out books, code, science, and the station's rare field reports.

If the old idea can be stretched one step farther, we should concatenate every accepted source and let its raw token count determine how often it appears.

If the proposal works on every relevant case, data mixtures is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

Now keep that rule fixed and let the difficult case enter: the largest crawl silently becomes the curriculum. A source ten thousand times smaller may almost never reach a batch even when it carries relationships absent from the web.

Nothing magical creates data mixtures. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: choose and publish a probability weight for each domain, treating the mixture as an explicit modeling decision that must be tested on per-domain validation streams.

This boundary between the failed rule and its repair is the subject later work calls **Data Mixtures**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize data mixtures; try to break it by subtraction. Remove the part that knows how to choose and publish a probability weight for each domain, treating the mixture as an explicit modeling decision that must be tested on per-domain validation streams, leaving only the attempt to concatenate every accepted source and let its raw token count determine how often it appears. What returns is not a vague weakness but the original contradiction: the largest crawl silently becomes the curriculum. A source ten thousand times smaller may almost never reach a batch even when it carries relationships absent from the web. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to concatenate every accepted source and let its raw token count determine how often it appears receives the same test as the rule to choose and publish a probability weight for each domain, treating the mixture as an explicit modeling decision that must be tested on per-domain validation streams. Their different outcomes reveal what data mixtures contributes without asking the reader to trust historical convention.

#### Decide Which Worlds Receive a Voice

The station assigns 0.50 to curated web text, 0.20 to science, 0.15 to code, 0.10 to books, and 0.05 to field reports. The five shares exhaust one draw without pretending the sources are equally large or equally important.

Hold the setting, evidence, and desired outcome fixed while testing data mixtures. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

#### The calculation hidden inside data mixtures

Do not read the coming Data Mixtures line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

D counts the named data domains and w_d is the chance that the next training draw chooses domain d. Nonnegative weights prevent negative sampling; a total of one exhausts all possible domain choices.

##### Why no cheaper operation does the same job

[Summation](../MATHEMATICAL_MOVES.md#summation) combines mutually exclusive domain shares into the whole probability mass. Multiplication would make one zero-weight domain erase the mixture. [Equality](../MATHEMATICAL_MOVES.md#equals) requires a complete distribution, while the [inequality](../MATHEMATICAL_MOVES.md#inequalities) forbids impossible negative shares.

Every symbol in Data Mixtures can now be read back into an action already performed. The whole procedure fits in one line:

$$
\sum_{d=1}^{D}w_d=1,\quad w_d\ge 0
$$

#### Where data mixtures runs out

Mixture weights redistribute attention but cannot make a poor or missing domain representative, accurate, or safe.

This is where data mixtures runs out for a causal reason. We gave it enough structure to choose and publish a probability weight for each domain, treating the mixture as an explicit modeling decision that must be tested on per-domain validation streams, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take data mixtures to the workbench

A mathematical story about data mixtures earns trust only when the failed and repaired paths can both be reproduced. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running data mixtures, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the data mixtures result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/184-data-mixtures/README.md).*

---

### Excavation 185 — Mixture Sampling — Turn Planned Shares into a Reproducible Stream

<!-- book-prose-v2 -->

The mixture weights state which domains should be heard. They do not yet produce a finite ordered token stream that every resumed worker can reconstruct.

A careful builder would first avoid adding machinery and round each domain's desired share independently and concatenate the resulting blocks.

The shortcut appears to retain everything mixture sampling needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

The world supplies the one comparison the shortcut hoped never to face: independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero.

The counterexample teaches mixture sampling. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source.

Now—and not earlier—we may introduce **Mixture Sampling**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to round each domain's desired share independently and concatenate the resulting blocks, and the case answers that independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero. With the narrow repair—to use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Mixture Sampling returns to the same counterexample, replaces the attempt to round each domain's desired share independently and concatenate the resulting blocks with the responsibility to use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source, and must succeed where the shortcut failed.

#### Turn Planned Shares into a Reproducible Stream

For 1,000 document draws, a 0.05 field-report weight expects about 50 selections. The seeded schedule interleaves those reports with other domains and records the actual count rather than promising exact equality by chance.

A formula for mixture sampling is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

#### The calculation hidden inside mixture sampling

Before Mixture Sampling receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

N is the total number of scheduled training draws, w_d is domain d's share, n_d is its realized count, and E[n_d] is the average count expected across many schedules.

##### Why no cheaper operation does the same job

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) is forced because each of N draws independently offers domain d the same share w_d. Addition would grant a fixed number unrelated to run length. [Expectation](../MATHEMATICAL_MOVES.md#expectation) describes a long-run average, not a guarantee that one finite schedule equals Nw_d exactly.

Every symbol in Mixture Sampling can now be read back into an action already performed. The whole procedure fits in one line:

$$
E[n_d]=Nw_d
$$

#### Where mixture sampling runs out

Sampling realizes probabilities only approximately in a finite run, and replacement can repeat scarce documents enough to increase memorization.

The boundary can be predicted from the construction itself. Mixture Sampling performs the repair to use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

#### Take mixture sampling to the workbench

Move mixture sampling from imagination to evidence by making the shortcut fail under controlled inputs. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running mixture sampling, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the mixture sampling result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/185-mixture-sampling/README.md).*

---

### Excavation 186 — The Token Budget — Convert a Training Plan into a Count of Lessons

<!-- book-prose-v2 -->

Seeded mixture sampling can produce an ordered stream. The run still says “train for a while,” so neither cost nor source exposure is bounded.

The obvious economy is to stop when the wall clock reaches an affordable date.

The proposal deserves a fair hearing. For the token budget, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Its hidden assumption becomes visible as soon as we observe that faster hardware sees more tokens, interruptions see fewer, and two runs with the same calendar budget teach different amounts of evidence.

The failure changes the question behind the token budget. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute.

Only at this point does the inherited name **The Token Budget** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of the token budget by mentally removing the repair. We fall back to the proposal to stop when the wall clock reaches an affordable date; then faster hardware sees more tokens, interruptions see fewer, and two runs with the same calendar budget teach different amounts of evidence. Restore only the ability to define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to stop when the wall clock reaches an affordable date to requiring the system to define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to the token budget.

#### Convert a Training Plan into a Count of Lessons

A tiny run uses 2,000 updates with 32 sequences of 128 real tokens each. Every update carries 4,096 lessons, so the complete plan exposes 8,192,000 tokens.

Put the old procedure beside the token budget. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

#### The calculation hidden inside the token budget

Do not read the coming The Token Budget line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

T is the planned number of optimizer updates, B_tokens counts real loss-bearing tokens in one global batch, and N_tokens is the complete exposure budget.

##### Why no cheaper operation does the same job

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) appears because every one of T updates consumes B_tokens lessons. Addition would count only one update plus one batch. Padding is excluded because it occupies hardware but contributes no language target.

Every symbol in The Token Budget can now be read back into an action already performed. The whole procedure fits in one line:

$$
N_{\text{tokens}}=T B_{\text{tokens}}
$$

#### Where the token budget runs out

Equal token counts do not imply equal compute when model size, sequence length, sparsity, or hardware efficiency differs.

The limit follows from the job assigned to the token budget. Its repair knows how to define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

#### Take the token budget to the workbench

A claim about the token budget now exists on the page; the laboratory must be able to contradict it. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running the token budget, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the the token budget result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/186-token-budget/README.md).*

---

### Excavation 187 — Compute-Optimal Allocation — Buy a Larger Memory or More Experience?

<!-- book-prose-v2 -->

The token budget fixes how much evidence the model will see. A fixed compute allowance still permits a wider model trained on fewer tokens or a smaller model trained on more.

Before naming anything new, try to spend nearly the entire budget on parameter count because a larger model can store more patterns.

Its appeal is not ignorance but economy. Compute-Optimal Allocation should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Then a case arrives in which convenience and truth separate: the large model is stopped after too little experience and remains undertrained, while much of its expensive capacity never receives enough varied evidence.

Notice what the counterexample has accomplished for compute-optimal allocation. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: estimate candidate parameter-and-token pairs under the same compute budget, run smaller scaling experiments, and choose the pair predicted to minimize held-out loss rather than maximizing either axis alone.

Humanity eventually gathered this problem and its repairs under the name **Compute-Optimal Allocation**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace compute-optimal allocation with the old instruction to spend nearly the entire budget on parameter count because a larger model can store more patterns. The result is again that the large model is stopped after too little experience and remains undertrained, while much of its expensive capacity never receives enough varied evidence. Put back only the requirement to estimate candidate parameter-and-token pairs under the same compute budget, run smaller scaling experiments, and choose the pair predicted to minimize held-out loss rather than maximizing either axis alone. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when compute-optimal allocation is introduced. The same evidence that defeated the attempt to spend nearly the entire budget on parameter count because a larger model can store more patterns is presented again. Only the ability to estimate candidate parameter-and-token pairs under the same compute budget, run smaller scaling experiments, and choose the pair predicted to minimize held-out loss rather than maximizing either axis alone changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### Buy a Larger Memory or More Experience

The station compares doubling parameters while halving tokens with keeping the smaller model and doubling tokens. Because both alter the same compute bill, held-out scaling runs decide which balance learns more.

Run the compute-optimal allocation scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

#### The calculation hidden inside compute-optimal allocation

Before Compute-Optimal Allocation receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

P is the number of trainable model parameters, D is the number of training tokens, and C is a rough count of floating-point work for dense Transformer training; six summarizes forward and backward work per parameter-token interaction.

##### Why no cheaper operation does the same job

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) is forced because every token exercises the model's parameters: doubling either P or D roughly doubles work. [Approximation](../MATHEMATICAL_MOVES.md#approximation) preserves the scaling relation while admitting architecture and implementation details. Adding P and D would combine incompatible units.

Every symbol in Compute-Optimal Allocation can now be read back into an action already performed. The whole procedure fits in one line:

$$
C\approx 6PD
$$

#### Where compute-optimal allocation runs out

Compute-optimal estimates are empirical and depend on architecture, data quality, optimizer, and the inference cost the project can afford afterward.

Why does that boundary remain? Compute-Optimal Allocation was built for one responsibility: estimate candidate parameter-and-token pairs under the same compute budget, run smaller scaling experiments, and choose the pair predicted to minimize held-out loss rather than maximizing either axis alone. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take compute-optimal allocation to the workbench

The argument for compute-optimal allocation is still provisional until a runnable case can make it fail. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running compute-optimal allocation, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the compute-optimal allocation result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/187-compute-optimal-allocation/README.md).*

---

### Excavation 188 — Learning-Rate Warmup — Let Adam Learn the Terrain Before Running

<!-- book-prose-v2 -->

Compute allocation chooses the model and token horizon. At the first update, Adam's moment memories contain almost no history, while randomly initialized activations and gradients are changing fastest.

The first defensible move is to begin immediately at the peak learning rate chosen for the stable middle of training.

There is a real principle behind this restraint: the complexity of learning-rate warmup must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The proposal breaks for a specific reason, not by authority: the first noisy batches can make large updates before the optimizer's scale estimates become trustworthy, producing a loss spike that the later stable rate would not have caused.

That distinction is the hinge on which learning-rate warmup turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule.

We have earned the chapter's shorter name: **Learning-Rate Warmup**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that learning-rate warmup is necessary rather than decorative. Delete its new responsibility and use the earlier plan to begin immediately at the peak learning rate chosen for the stable middle of training. Immediately, the first noisy batches can make large updates before the optimizer's scale estimates become trustworthy, producing a loss spike that the later stable rate would not have caused. Reintroduce the single job to increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule. Because the old plan to begin immediately at the peak learning rate chosen for the stable middle of training is the only displaced piece, the reader can locate exactly where learning-rate warmup changes the outcome.

#### Let Adam Learn the Terrain Before Running

With peak rate 0.001 and 100 warmup updates, update 25 receives 0.00025, update 50 receives 0.0005, and update 100 finally reaches 0.001.

The name learning-rate warmup is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### The calculation hidden inside learning-rate warmup

Do not read the coming Learning-Rate Warmup line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

t is the current model warmup update, T_warm is the number of warmup updates, eta_peak is the intended stable rate, and eta_t is the smaller rate used now.

##### Why no cheaper operation does the same job

[Division](../MATHEMATICAL_MOVES.md#division) turns elapsed warmup steps into a progress fraction from zero to one. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) applies that fraction to the peak rate. Adding t would mix step counts with a rate; jumping directly to eta_peak recreates the failed attempt.

Every symbol in Learning-Rate Warmup can now be read back into an action already performed. The whole procedure fits in one line:

$$
\eta_t=\eta_{\text{peak}}\frac{t}{T_{\text{warm}}}\quad(0\le t\le T_{\text{warm}})
$$

#### Where learning-rate warmup runs out

Warmup reduces early shock but cannot rescue an unsuitable peak rate, broken initialization, corrupt batch, or incorrect optimizer state.

The weakness is not an accidental footnote. Every operation in learning-rate warmup serves the narrower purpose to increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take learning-rate warmup to the workbench

Understanding learning-rate warmup now means predicting its intermediate results before asking software for an answer. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running learning-rate warmup, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the learning-rate warmup result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/188-learning-rate-warmup/README.md).*

---

### Excavation 189 — Cosine Decay — Make Late Corrections Smaller Without a Cliff

<!-- book-prose-v2 -->

Warmup protects the optimizer's first steps. Keeping the peak rate for the entire token budget makes late updates as aggressive as early ones even when the model is refining rather than discovering broad structure.

At this point the shortest path seems to be to drop the rate abruptly near the end of training.

This is how cosine decay ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Reality now asks a question the retained information cannot answer: a sudden cliff changes update scale in one step and makes the chosen drop date an arbitrary discontinuity; dropping too early freezes useful learning.

The wrong answer makes the need for cosine decay inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state.

The usual name, **Cosine Decay**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to drop the rate abruptly near the end of training produces the observed failure: a sudden cliff changes update scale in one step and makes the chosen drop date an arbitrary discontinuity; dropping too early freezes useful learning. Starting with the repaired demand to decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state preserves the information the shortcut lost. The subject of cosine decay lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state instead of merely trying to drop the rate abruptly near the end of training. That controlled contrast is what turns a plausible explanation of cosine decay into an understandable derivation.

#### Make Late Corrections Smaller Without a Cliff

Halfway through decay, cosine is zero, so the rate sits halfway between its peak and minimum. At the final planned update, cosine reaches negative one and the rate reaches the minimum without a jump.

There are now two histories of this cosine decay case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

#### The calculation hidden inside cosine decay

Before Cosine Decay receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

t is model-training progress through the decay interval of length T; eta_max and eta_min are its endpoint rates; cosine supplies a smooth path between them.

##### Why no cheaper operation does the same job

[Subtraction](../MATHEMATICAL_MOVES.md#subtraction) isolates the adjustable rate range, [division](../MATHEMATICAL_MOVES.md#division) converts progress to a fraction, and [cosine](../MATHEMATICAL_MOVES.md#cosine) bends that fraction smoothly with flat endpoint slopes. Addition places the scaled range above eta_min. A raw linear drop is possible, but cosine avoids an abrupt endpoint slope.

Every symbol in Cosine Decay can now be read back into an action already performed. The whole procedure fits in one line:

$$
\eta_t=\eta_{\min}+\frac{\eta_{\max}-\eta_{\min}}{2}\left(1+\cos\frac{\pi t}{T}\right)
$$

#### Where cosine decay runs out

Cosine decay assumes a known horizon and is not automatically optimal when training is unexpectedly extended.

Look back at what cosine decay actually preserves: it can decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

#### Take cosine decay to the workbench

The reader has reconstructed cosine decay in words; the workbench tests whether those words specify a real procedure. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running cosine decay, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the cosine decay result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/189-cosine-decay/README.md).*

---

### Excavation 190 — Gradient Noise Scale — When More Examples Stop Buying More Direction

<!-- book-prose-v2 -->

The schedule controls how far one global update moves. We still do not know how many examples should vote in that update before extra devices mostly repeat the same directional evidence.

We can postpone invention if we simply make the global batch as large as the cluster permits.

If the proposal works on every relevant case, gradient noise scale is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The decisive test is this: early doubling reduces disagreement and improves the direction, but beyond a workload-dependent point the averaged gradient barely changes while each update consumes twice as many tokens.

Nothing magical creates gradient noise scale. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: measure disagreement among micro-batch gradients relative to the strength of their shared direction, and use that noise scale as evidence for the largest useful batch rather than a hardware target.

This boundary between the failed rule and its repair is the subject later work calls **Gradient Noise Scale**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize gradient noise scale; try to break it by subtraction. Remove the part that knows how to measure disagreement among micro-batch gradients relative to the strength of their shared direction, and use that noise scale as evidence for the largest useful batch rather than a hardware target, leaving only the attempt to make the global batch as large as the cluster permits. What returns is not a vague weakness but the original contradiction: early doubling reduces disagreement and improves the direction, but beyond a workload-dependent point the averaged gradient barely changes while each update consumes twice as many tokens. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to make the global batch as large as the cluster permits receives the same test as the rule to measure disagreement among micro-batch gradients relative to the strength of their shared direction, and use that noise scale as evidence for the largest useful batch rather than a hardware target. Their different outcomes reveal what gradient noise scale contributes without asking the reader to trust historical convention.

#### When More Examples Stop Buying More Direction

Three named micro-batches question the same two weights: the field reports propose [2.0,1.0], science proposes [2.1,0.9], and books propose [1.9,1.1]. The first number is advice to the tiger-before-river weight; the second is advice to a punctuation weight. Their mean [2.0,1.0] is strong and their disagreement around it is small. If the witnesses instead propose [4,−2], [0,4], and [2,1], disagreement is large relative to the same broad direction, so a larger batch can still buy useful certainty.

Hold the setting, evidence, and desired outcome fixed while testing gradient noise scale. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

#### The calculation hidden inside gradient noise scale

Do not read the coming Gradient Noise Scale line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Each g_i is one model micro-batch's gradient advice. The covariance measures how those witnesses disagree; its trace totals disagreement across coordinates. The squared norm of their mean measures the strength of the shared direction; G compares noise with signal.

##### Why no cheaper operation does the same job

[Covariance](../MATHEMATICAL_MOVES.md#covariance) keeps variation around the common advice rather than raw gradient size. [Trace](../MATHEMATICAL_MOVES.md#trace) gathers coordinate variances without inventing cross-coordinate units. [Division](../MATHEMATICAL_MOVES.md#division) asks disagreement per unit of squared shared direction; subtraction would not remove dependence on signal scale.

Every symbol in Gradient Noise Scale can now be read back into an action already performed. The whole procedure fits in one line:

$$
G=\frac{\mathrm{tr}(\mathrm{Cov}[g_i])}{\lVert E[g_i]\rVert^2}
$$

#### Where gradient noise scale runs out

Gradient noise scale is an empirical guide, not a universal batch-size law; it changes during training and with the task and optimizer.

This is where gradient noise scale runs out for a causal reason. We gave it enough structure to measure disagreement among micro-batch gradients relative to the strength of their shared direction, and use that noise scale as evidence for the largest useful batch rather than a hardware target, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take gradient noise scale to the workbench

A mathematical story about gradient noise scale earns trust only when the failed and repaired paths can both be reproduced. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running gradient noise scale, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the gradient noise scale result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/190-gradient-noise-scale/README.md).*

---

### Excavation 191 — Data Parallelism — Let Several Workers Observe Different Evidence

<!-- book-prose-v2 -->

Gradient noise measurements choose a useful global batch. One device cannot process that batch quickly enough, even though the modern model and optimizer state now fit through sharding.

The previous discovery seems almost sufficient: we could send the same mini-batch to every worker and average their gradients.

The shortcut appears to retain everything data parallelism needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

One counterexample is enough to expose the missing job: all workers repeat the same computation and return the same evidence, so hardware cost rises without increasing batch diversity or reducing step time meaningfully.

The counterexample teaches data parallelism. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update.

Now—and not earlier—we may introduce **Data Parallelism**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to send the same mini-batch to every worker and average their gradients, and the case answers that all workers repeat the same computation and return the same evidence, so hardware cost rises without increasing batch diversity or reducing step time meaningfully. With the narrow repair—to replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Data Parallelism returns to the same counterexample, replaces the attempt to send the same mini-batch to every worker and average their gradients with the responsibility to replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update, and must succeed where the shortcut failed.

#### Let Several Workers Observe Different Evidence

Four workers each read eight different sequences. Their four average gradients become one average over thirty-two sequences before any worker advances the parameters.

A formula for data parallelism is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

#### The calculation hidden inside data parallelism

Before Data Parallelism receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

P is the number of data-parallel workers, g_p is worker p's average gradient from different examples, and g is the single gradient used by the shared optimizer step.

##### Why no cheaper operation does the same job

[Summation](../MATHEMATICAL_MOVES.md#summation) lets every worker's independent evidence contribute. [Division](../MATHEMATICAL_MOVES.md#division) returns advice per worker so adding hardware does not enlarge the update by itself. Multiplication would let a zero coordinate from one worker erase all others.

Every symbol in Data Parallelism can now be read back into an action already performed. The whole procedure fits in one line:

$$
g=\frac1P\sum_{p=1}^{P}g_p
$$

#### Where data parallelism runs out

Because one shared update cannot proceed until every worker's evidence has joined the average, synchronous data parallelism waits for the slowest worker and communicates a full update's worth of gradient information.

The boundary can be predicted from the construction itself. Data Parallelism performs the repair to replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

#### Take data parallelism to the workbench

Move data parallelism from imagination to evidence by making the shortcut fail under controlled inputs. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running data parallelism, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the data parallelism result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/191-data-parallelism/README.md).*

---

### Excavation 192 — Pipeline Parallelism — Stop Waiting for the Whole Model to Cross One Device at a Time

<!-- book-prose-v2 -->

Data parallel workers process different examples, but each replica still needs the model's sequential layers. Splitting those layers across devices makes only one device active if a whole batch traverses the stages at once.

The least expensive next move is to send one complete batch through stage one, then stage two, then stage three.

The proposal deserves a fair hearing. For pipeline parallelism, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Now keep that rule fixed and let the difficult case enter: while stage two works, stage one and stage three wait. The model fits, but most devices are idle for most of the step.

The failure changes the question behind pipeline parallelism. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently.

Only at this point does the inherited name **Pipeline Parallelism** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of pipeline parallelism by mentally removing the repair. We fall back to the proposal to send one complete batch through stage one, then stage two, then stage three; then while stage two works, stage one and stage three wait. The model fits, but most devices are idle for most of the step. Restore only the ability to split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to send one complete batch through stage one, then stage two, then stage three to requiring the system to split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to pipeline parallelism.

#### Stop Waiting for the Whole Model to Cross One Device at a Time

With four pipeline stages and eight micro-batches, the first few clock slots fill the pipeline, eight slots carry useful work, and the last few drain it. More micro-batches shrink the idle fraction.

Put the old procedure beside pipeline parallelism. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

#### The calculation hidden inside pipeline parallelism

Do not read the coming Pipeline Parallelism line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

m is the number of model micro-batches and p the number of pipeline stages in a simple forward pipeline. Useful work occupies m slots; filling and draining add p−1 slots; U is the idealized occupied share.

##### Why no cheaper operation does the same job

[Addition](../MATHEMATICAL_MOVES.md#addition) joins useful slots with unavoidable fill-and-drain slots. [Division](../MATHEMATICAL_MOVES.md#division) turns useful slots into a share of total schedule time. Multiplying m and p would count stage-tasks, not the fraction of time one stage remains usefully occupied.

Every symbol in Pipeline Parallelism can now be read back into an action already performed. The whole procedure fits in one line:

$$
U=\frac{m}{m+p-1}
$$

#### Where pipeline parallelism runs out

Because sequential layer dependencies require the pipeline to fill and drain, pipeline parallelism introduces bubbles and activation transfers; making micro-batches too small can then reduce the efficiency of each matrix operation.

The limit follows from the job assigned to pipeline parallelism. Its repair knows how to split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

#### Take pipeline parallelism to the workbench

A claim about pipeline parallelism now exists on the page; the laboratory must be able to contradict it. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running pipeline parallelism, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the pipeline parallelism result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/192-pipeline-parallelism/README.md).*

---

### Excavation 193 — Three-Dimensional Parallelism — Give Each Memory Wall Its Own Axis

<!-- book-prose-v2 -->

Pipeline micro-batches keep layer stages busy. A large run may still exceed memory inside one layer, require more independent data witnesses, and contain too many layers for one device group.

For a moment, remain loyal to the simplest proposal: increase whichever parallel technique was introduced most recently until the model fits.

Its appeal is not ignorance but economy. Three-Dimensional Parallelism should not be added until an observation exposes the exact thing the older procedure cannot preserve.

The world supplies the one comparison the shortcut hoped never to face: more pipeline stages increase bubbles, more tensor splits increase frequent communication, and more data replicas preserve full model memory. One axis cannot solve three different limits efficiently.

Notice what the counterexample has accomplished for three-dimensional parallelism. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost.

Humanity eventually gathered this problem and its repairs under the name **Three-Dimensional Parallelism**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace three-dimensional parallelism with the old instruction to increase whichever parallel technique was introduced most recently until the model fits. The result is again that more pipeline stages increase bubbles, more tensor splits increase frequent communication, and more data replicas preserve full model memory. One axis cannot solve three different limits efficiently. Put back only the requirement to compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when three-dimensional parallelism is introduced. The same evidence that defeated the attempt to increase whichever parallel technique was introduced most recently until the model fits is presented again. Only the ability to compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### Give Each Memory Wall Its Own Axis

Two tensor workers form each layer, four pipeline stages hold the depth, and three data replicas see different examples. The run uses 2×4×3=24 workers with each axis performing one named job.

Run the three-dimensional parallelism scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

#### The calculation hidden inside three-dimensional parallelism

Before Three-Dimensional Parallelism receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Each factor counts independent choices along one model-parallel axis. Selecting one tensor rank, one pipeline rank, and one data rank identifies exactly one worker; P_total counts all such combinations.

##### Why no cheaper operation does the same job

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) is forced by the product rule: every choice on one axis pairs with every choice on the others. Addition would count axis labels rather than workers. [Equality](../MATHEMATICAL_MOVES.md#equals) assumes the grid is fully populated.

Every symbol in Three-Dimensional Parallelism can now be read back into an action already performed. The whole procedure fits in one line:

$$
P_{\text{total}}=P_{\text{tensor}}P_{\text{pipeline}}P_{\text{data}}
$$

#### Where three-dimensional parallelism runs out

Three-dimensional parallelism increases coordination and configuration complexity; a poor mapping to the physical network can spend more time communicating than computing.

Why does that boundary remain? Three-Dimensional Parallelism was built for one responsibility: compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take three-dimensional parallelism to the workbench

The argument for three-dimensional parallelism is still provisional until a runnable case can make it fail. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running three-dimensional parallelism, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the three-dimensional parallelism result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/193-three-dimensional-parallelism/README.md).*

---

### Excavation 194 — Sharded Checkpoints — Save One Recoverable State Without Gathering It

<!-- book-prose-v2 -->

Three-dimensional parallelism spreads parameters, moments, gradients, and progress across many owners. Asking one coordinator to gather everything before saving can exceed its memory and stall the cluster.

Nothing yet appears to demand a new invention. We can let every worker write its local tensors and call the directory a checkpoint.

There is a real principle behind this restraint: the complexity of sharded checkpoints must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Its hidden assumption becomes visible as soon as we observe that a worker fails before writing, two shards belong to different steps, or a filename is reused. The directory exists but cannot reconstruct one globally consistent training state.

That distinction is the hinge on which sharded checkpoints turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: write versioned shards to temporary locations, record hashes and ownership in a checkpoint manifest, and publish one atomic completion marker only after every required shard is durable.

We have earned the chapter's shorter name: **Sharded Checkpoints**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that sharded checkpoints is necessary rather than decorative. Delete its new responsibility and use the earlier plan to let every worker write its local tensors and call the directory a checkpoint. Immediately, a worker fails before writing, two shards belong to different steps, or a filename is reused. The directory exists but cannot reconstruct one globally consistent training state. Reintroduce the single job to write versioned shards to temporary locations, record hashes and ownership in a checkpoint manifest, and publish one atomic completion marker only after every required shard is durable. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can write versioned shards to temporary locations, record hashes and ownership in a checkpoint manifest, and publish one atomic completion marker only after every required shard is durable. Because the old plan to let every worker write its local tensors and call the directory a checkpoint is the only displaced piece, the reader can locate exactly where sharded checkpoints changes the outcome.

#### Save One Recoverable State Without Gathering It

Twenty-four workers save step 8,000. The manifest expects twenty-four parameter shards, optimizer shards, scheduler state, RNG state, and data cursors; the checkpoint becomes eligible for recovery only when every recorded hash verifies.

The name sharded checkpoints is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### Where sharded checkpoints runs out

A complete checkpoint limits lost work but consumes storage and I/O bandwidth; frequent synchronous saves can dominate training time.

The weakness is not an accidental footnote. Every operation in sharded checkpoints serves the narrower purpose to write versioned shards to temporary locations, record hashes and ownership in a checkpoint manifest, and publish one atomic completion marker only after every required shard is durable; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take sharded checkpoints to the workbench

Understanding sharded checkpoints now means predicting its intermediate results before asking software for an answer. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running sharded checkpoints, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the sharded checkpoints result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/194-sharded-checkpoints/README.md).*

---

### Excavation 195 — Deterministic Resume — Continue the Same Experiment, Not a Similar One

<!-- book-prose-v2 -->

The sharded checkpoint can reconstruct every distributed tensor. If it omits the sampler cursor, random-number generators, scheduler phase, or overflow state, restart follows a different future.

The machinery already in our hands suggests that we restore model weights and let every other component start fresh.

This is how deterministic resume ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Then a case arrives in which convenience and truth separate: adam forgets its moments, warmup may begin again, dropout chooses different masks, and data workers repeat or skip documents. The loss curve after restart cannot be attributed to the original run.

The wrong answer makes the need for deterministic resume inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps.

The usual name, **Deterministic Resume**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to restore model weights and let every other component start fresh produces the observed failure: adam forgets its moments, warmup may begin again, dropout chooses different masks, and data workers repeat or skip documents. The loss curve after restart cannot be attributed to the original run. Starting with the repaired demand to checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps preserves the information the shortcut lost. The subject of deterministic resume lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps instead of merely trying to restore model weights and let every other component start fresh. That controlled contrast is what turns a plausible explanation of deterministic resume into an understandable derivation.

#### Continue the Same Experiment, Not a Similar One

The station stops after update 200, restores weights, Adam moments, schedule position, scaler, RNG streams, and each data cursor, then reproduces updates 201 through 205 byte for byte on the reference implementation.

There are now two histories of this deterministic resume case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

#### Where deterministic resume runs out

Exact replay can still fail across nondeterministic kernels, changed hardware, libraries, or distributed timing; the required reproducibility level must be stated.

Look back at what deterministic resume actually preserves: it can checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

#### Take deterministic resume to the workbench

The reader has reconstructed deterministic resume in words; the workbench tests whether those words specify a real procedure. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running deterministic resume, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the deterministic resume result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/195-deterministic-resume/README.md).*

---

### Excavation 196 — Loss Spikes — Distinguish One Hard Batch from a Run Leaving the Road

<!-- book-prose-v2 -->

Deterministic resume makes failures reproducible. During a long run, the observed loss sometimes jumps; automatically rewinding every jump wastes compute, while ignoring a sustained instability can destroy the model.

If the old idea can be stretched one step farther, we should declare any loss larger than the previous loss a failure and restore immediately.

If the proposal works on every relevant case, loss spikes is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The proposal breaks for a specific reason, not by authority: ordinary batches vary, so healthy learning triggers constant rollbacks. A slow divergence can rise without one dramatic step and escape the rule.

Nothing magical creates loss spikes. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response.

This boundary between the failed rule and its repair is the subject later work calls **Loss Spikes**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize loss spikes; try to break it by subtraction. Remove the part that knows how to compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response, leaving only the attempt to declare any loss larger than the previous loss a failure and restore immediately. What returns is not a vague weakness but the original contradiction: ordinary batches vary, so healthy learning triggers constant rollbacks. A slow divergence can rise without one dramatic step and escape the rule. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to declare any loss larger than the previous loss a failure and restore immediately receives the same test as the rule to compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response. Their different outcomes reveal what loss spikes contributes without asking the reader to trust historical convention.

#### Distinguish One Hard Batch from a Run Leaving the Road

Recent clean validation losses center near 2.0 with spread 0.1. One batch reaches 2.35 and then returns; another run stays above 2.5 while gradient norm grows. Only the persistent, corroborated event triggers recovery.

Hold the setting, evidence, and desired outcome fixed while testing loss spikes. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

#### The calculation hidden inside loss spikes

Do not read the coming Loss Spikes line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

L_t is the current monitored model loss, mu_t is its robust recent center, sigma_t is ordinary recent spread, and z_t says how many usual spreads the current value lies above or below that center.

##### Why no cheaper operation does the same job

[Subtraction](../MATHEMATICAL_MOVES.md#subtraction) removes the local baseline. [Division](../MATHEMATICAL_MOVES.md#division) expresses the remainder in units of ordinary variation, making different loss scales comparable. A raw threshold would behave differently as normal loss falls during training.

Every symbol in Loss Spikes can now be read back into an action already performed. The whole procedure fits in one line:

$$
z_t=\frac{L_t-\mu_t}{\sigma_t}
$$

#### Where loss spikes runs out

Thresholds detect symptoms, not causes; corrupt data, overflow, optimizer settings, hardware faults, and architectural instability require different repairs.

This is where loss spikes runs out for a causal reason. We gave it enough structure to compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

#### Take loss spikes to the workbench

A mathematical story about loss spikes earns trust only when the failed and repaired paths can both be reproduced. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running loss spikes, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the loss spikes result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/196-loss-spike-recovery/README.md).*

---

### Excavation 197 — A Validation Stream — Ask Whether Learning Survives Outside the Current Batch

<!-- book-prose-v2 -->

Loss-spike monitoring protects the training process from obvious instability. A smooth training curve can still improve mainly on repeated or overrepresented training domains.

A careful builder would first avoid adding machinery and evaluate only the next training batch because it is already available.

The shortcut appears to retain everything a validation stream needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

Reality now asks a question the retained information cannot answer: the same data mixture and duplicates that shaped the update also judge it. Training loss can fall while held-out language or a rare domain becomes worse.

The counterexample teaches a validation stream. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: maintain versioned, deduplicated, contamination-checked validation streams by domain and evaluate them at recorded token intervals without using them to update weights.

Now—and not earlier—we may introduce **A Validation Stream**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to evaluate only the next training batch because it is already available, and the case answers that the same data mixture and duplicates that shaped the update also judge it. Training loss can fall while held-out language or a rare domain becomes worse. With the narrow repair—to maintain versioned, deduplicated, contamination-checked validation streams by domain and evaluate them at recorded token intervals without using them to update weights—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. A Validation Stream returns to the same counterexample, replaces the attempt to evaluate only the next training batch because it is already available with the responsibility to maintain versioned, deduplicated, contamination-checked validation streams by domain and evaluate them at recorded token intervals without using them to update weights, and must succeed where the shortcut failed.

#### Ask Whether Learning Survives Outside the Current Batch

After every million training tokens, the station measures held-out field reports, science, books, code, and web text separately. A lower global average cannot hide that field-report loss rose.

A formula for a validation stream is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

#### The calculation hidden inside a validation stream

Before A Validation Stream receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

The validation stream contains N honest next-token events. The model assigns the observed token x_i a conditional probability from its earlier context. Negative log turns confident neglect into positive cost, and L_val averages that cost across the stream.

##### Why no cheaper operation does the same job

[Logarithms](../MATHEMATICAL_MOVES.md#logarithm) turn multiplied sequence probabilities into additive token costs. [Negative signs](../MATHEMATICAL_MOVES.md#negative-sign) make lower assigned probability cost more. [Summation](../MATHEMATICAL_MOVES.md#summation) lets every event contribute, and [division](../MATHEMATICAL_MOVES.md#division) makes streams of different lengths comparable.

Every symbol in A Validation Stream can now be read back into an action already performed. The whole procedure fits in one line:

$$
L_{\text{val}}=-\frac1N\sum_{i=1}^{N}\log p_\theta(x_i\mid x_{<i})
$$

#### Where a validation stream runs out

Validation detects only the distributions and behaviors represented in its finite streams; repeatedly tuning against it can eventually overfit it.

The boundary can be predicted from the construction itself. A Validation Stream performs the repair to maintain versioned, deduplicated, contamination-checked validation streams by domain and evaluate them at recorded token intervals without using them to update weights; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

#### Take a validation stream to the workbench

Move a validation stream from imagination to evidence by making the shortcut fail under controlled inputs. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running a validation stream, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the a validation stream result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/197-validation-stream/README.md).*

---

### Excavation 198 — A Memorization Audit — Did the Model Learn a Pattern or Store a Passage?

<!-- book-prose-v2 -->

Held-out validation shows whether prediction improves outside current batches. It does not reveal whether rare or repeated training sequences can be extracted verbatim from the model.

The obvious economy is to ask the model whether it remembers private text and trust its answer.

The proposal deserves a fair hearing. For a memorization audit, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The decisive test is this: a model has no reliable introspective inventory of its training examples, and ordinary prompts may miss strings that an adversarial sampling strategy can recover.

The failure changes the question behind a memorization audit. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts.

Only at this point does the inherited name **A Memorization Audit** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of a memorization audit by mentally removing the repair. We fall back to the proposal to ask the model whether it remembers private text and trust its answer; then a model has no reliable introspective inventory of its training examples, and ordinary prompts may miss strings that an adversarial sampling strategy can recover. Restore only the ability to plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to ask the model whether it remembers private text and trust its answer to requiring the system to plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to a memorization audit.

#### Did the Model Learn a Pattern or Store a Passage

The station inserts one synthetic radio code once and another code one hundred times. If the repeated code becomes far easier to rank and complete, the audit exposes the relationship between repetition and extractable memory without using a real secret.

Put the old procedure beside a memorization audit. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

#### The calculation hidden inside a memorization audit

Do not read the coming A Memorization Audit line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

R is the known space of possible synthetic canaries and rank is the tested canary's position when alternatives are ordered from most to least likely. Exposure measures how many bits of the search space the model has effectively removed.

##### Why no cheaper operation does the same job

[Cardinality](../MATHEMATICAL_MOVES.md#cardinality) counts possible canaries. [Logarithms](../MATHEMATICAL_MOVES.md#logarithm) turn multiplicative changes in search space and rank into bits. [Subtraction](../MATHEMATICAL_MOVES.md#subtraction) removes the remaining search difficulty from the original difficulty; adding would reward a worse rank.

Every symbol in A Memorization Audit can now be read back into an action already performed. The whole procedure fits in one line:

$$
\mathrm{exposure}=\log_2\lvert\mathcal R\rvert-\log_2\mathrm{rank}
$$

#### Where a memorization audit runs out

A canary audit samples possible attacks and strings; passing it does not prove that no training data can be extracted.

The limit follows from the job assigned to a memorization audit. Its repair knows how to plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

#### Take a memorization audit to the workbench

A claim about a memorization audit now exists on the page; the laboratory must be able to contradict it. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running a memorization audit, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the a memorization audit result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/198-memorization-audit/README.md).*

---

### Excavation 199 — The Training Report — Preserve the Decisions, Not Only the Weights

<!-- book-prose-v2 -->

Memorization auditing adds one essential limitation to the evaluation record. A released checkpoint still cannot explain its corpus, mixture, compute, interruptions, exclusions, intended uses, or known failures by inspecting weight tensors.

Before naming anything new, try to publish the final benchmark table and assume the configuration files explain the rest.

Its appeal is not ignorance but economy. The Training Report should not be added until an observation exposes the exact thing the older procedure cannot preserve.

One counterexample is enough to expose the missing job: a score has no visible data lineage, uncertainty, subgroup behavior, energy or hardware context, incident history, or warning about uses the evaluation never tested.

Notice what the counterexample has accomplished for the training report. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: generate a training report from manifests and logs, then add human-reviewed explanations of intended use, out-of-scope use, limitations, incidents, provenance, evaluation conditions, and responsible release decisions.

Humanity eventually gathered this problem and its repairs under the name **The Training Report**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace the training report with the old instruction to publish the final benchmark table and assume the configuration files explain the rest. The result is again that a score has no visible data lineage, uncertainty, subgroup behavior, energy or hardware context, incident history, or warning about uses the evaluation never tested. Put back only the requirement to generate a training report from manifests and logs, then add human-reviewed explanations of intended use, out-of-scope use, limitations, incidents, provenance, evaluation conditions, and responsible release decisions. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when the training report is introduced. The same evidence that defeated the attempt to publish the final benchmark table and assume the configuration files explain the rest is presented again. Only the ability to generate a training report from manifests and logs, then add human-reviewed explanations of intended use, out-of-scope use, limitations, incidents, provenance, evaluation conditions, and responsible release decisions changes, so the repaired conclusion cannot be credited to a conveniently different example.

#### Preserve the Decisions, Not Only the Weights

The station's report names corpus and code versions, tokens seen, mixture shares, compute, checkpoint recoveries, per-domain validation, memorization probes, excluded sources, and the exact model artifact hash.

Run the the training report scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

#### Where the training report runs out

Documentation improves accountability but can be incomplete, outdated, misleading, or ignored; claims still require inspectable evidence.

Why does that boundary remain? The Training Report was built for one responsibility: generate a training report from manifests and logs, then add human-reviewed explanations of intended use, out-of-scope use, limitations, incidents, provenance, evaluation conditions, and responsible release decisions. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

#### Take the training report to the workbench

The argument for the training report is still provisional until a runnable case can make it fail. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running the training report, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the the training report result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/199-training-report/README.md).*

---

### Excavation 200 — A Tiny Pretraining Factory — Close the Accountable Training Loop

<!-- book-prose-v2 -->

The training report can explain one finished run. We have now earned all the mechanisms needed to make the next run reconstructable from source documents to final artifact rather than relying on memory and scattered scripts.

The first defensible move is to connect every tool into one automatic pipeline and trust any run that reaches the final stage.

There is a real principle behind this restraint: the complexity of a tiny pretraining factory must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Now keep that rule fixed and let the difficult case enter: automation can faithfully repeat a wrong manifest, destructive filter, contaminated validation set, incomplete checkpoint, or unauthorized release. Completion is not evidence of correctness.

That distinction is the hinge on which a tiny pretraining factory turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: assemble signed stage manifests, boundary-aware curation, audited mixtures, fixed budgets, measured schedules, distributed equivalence tests, atomic checkpoints, live validation, memorization probes, and human release gates into one reversible factory.

We have earned the chapter's shorter name: **A Tiny Pretraining Factory**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that a tiny pretraining factory is necessary rather than decorative. Delete its new responsibility and use the earlier plan to connect every tool into one automatic pipeline and trust any run that reaches the final stage. Immediately, automation can faithfully repeat a wrong manifest, destructive filter, contaminated validation set, incomplete checkpoint, or unauthorized release. Completion is not evidence of correctness. Reintroduce the single job to assemble signed stage manifests, boundary-aware curation, audited mixtures, fixed budgets, measured schedules, distributed equivalence tests, atomic checkpoints, live validation, memorization probes, and human release gates into one reversible factory. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can assemble signed stage manifests, boundary-aware curation, audited mixtures, fixed budgets, measured schedules, distributed equivalence tests, atomic checkpoints, live validation, memorization probes, and human release gates into one reversible factory. Because the old plan to connect every tool into one automatic pipeline and trust any run that reaches the final stage is the only displaced piece, the reader can locate exactly where a tiny pretraining factory changes the outcome.

#### Close the Accountable Training Loop

A tiny run begins from ten named documents, records every acceptance and removal, trains a reproducible model, survives an intentional interruption, reproduces its next updates, generates its report, and refuses release when the memorization gate fails.

The name a tiny pretraining factory is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

#### Where a tiny pretraining factory runs out

The factory is accountable, not omniscient. New sources, laws, hardware, attacks, and uses create new failures that must return to observation and the bounded research loop.

The weakness is not an accidental footnote. Every operation in a tiny pretraining factory serves the narrower purpose to assemble signed stage manifests, boundary-aware curation, audited mixtures, fixed budgets, measured schedules, distributed equivalence tests, atomic checkpoints, live validation, memorization probes, and human release gates into one reversible factory; none was designed to answer the new question. We have reached the honest edge of the invention.

#### Take a tiny pretraining factory to the workbench

Understanding a tiny pretraining factory now means predicting its intermediate results before asking software for an answer. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running a tiny pretraining factory, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the a tiny pretraining factory result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

The factory returns every proposed change to the bounded loop: observe, test, document, authorize, release reversibly, and remain able to reconstruct what happened.

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/200-tiny-pretraining-factory/README.md).*
