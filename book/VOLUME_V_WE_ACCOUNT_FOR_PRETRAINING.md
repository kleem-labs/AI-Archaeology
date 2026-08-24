# Volume V — We Account for Pretraining

The modern engine can run. We now build the accountable factory around it: traceable evidence, explicit curation, budgeted learning, coordinated workers, recoverable state, independent audits, and a report that remains attached to the final artifact.

One discovery will create the need for the next; the object under construction never resets.

## Overture

The final volume enters the Archive Foundry, where documents become training experience. Nothing may disappear without a trace: sources, filters, mixtures, updates, checkpoints, and release decisions must remain connected by a recoverable chain of evidence.

```text
document → lineage → lesson → update → artifact → account
```

In this volume:

- [Part XIII — A Pretraining Factory We Can Account For](#part-xiii--a-pretraining-factory-we-can-account-for)

---

## Part XIII — A Pretraining Factory We Can Account For

The model is modern but still empty of trustworthy experience. We follow one named corpus from its source documents through boundaries, curation, mixture decisions, compute budgets, distributed training, recovery, validation, memorization audits, and a reversible release.

---

### Excavation 176 — A Corpus Manifest — Know What Entered the Run

The modern tiny language-model engine preserves a reference path through training and serving. It still cannot explain which documents will shape its weights, because no corpus has been frozen as part of the experiment.

At the Archive Foundry, the archivist-engineer returns to the chain-of-custody ledger. Yesterday's instrument still lies open, so the first move asks for no new magic: copy every available text file into one large folder and begin tokenizing.

Reality answers without terminology: a file is replaced upstream, another is silently skipped, and a third appears twice under different paths. The same training command now describes a different body of evidence. The chain-of-custody ledger now holds two situations the old rule cannot keep apart.

*The archivist-engineer sketches the break before changing it:*

```text
OLD PATH:  request ──▶ copy every available text file into… ──▶ a file is replaced upstream, another…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ create an immutable manifest that… ──▶ accountable result
```

The chain-of-custody ledger is divided down the middle. Left side: “copy every available text file into one large folder and begin tokenizing.” Its final mark records a file is replaced upstream, another is silently skipped, and a third appears twice under different paths. The same training command now describes a different body of evidence. Right side: the same starting evidence, now allowed to create an immutable manifest that records each source, version, content hash, license or usage basis, processing stage, and document count before any training shard exists. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given corpus manifest a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: create an immutable manifest that records each source, version, content hash, license or usage basis, processing stage, and document count before any training shard exists. The name **A Corpus Manifest** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to copy every available text file into one large folder and begin tokenizing; on the other lies the observed fact that a file is replaced upstream, another is silently skipped, and a third appears twice under different paths. The same training command now describes a different body of evidence. The bridge called corpus manifest has exactly the planks needed to create an immutable manifest that records each source, version, content hash, license or usage basis, processing stage, and document count before any training shard exists. In the Archive Foundry, corpus manifest joins mathematics to memory. Sets identify what must be present, hashes preserve identity, counts bound exposure, and arrows keep every transformation attached to its source. A model may forget its documents internally; the factory must not forget them externally.

#### Know What Entered the Run

The ranger station records `field-reports/v3`, its retrieval date, 8,412 documents, and the hash of its manifest. A later run can prove whether it used the same evidence.

#### Where a corpus manifest runs out

A manifest makes the corpus accountable; it cannot prove that every recorded document is suitable, lawful, accurate, or harmless.

A final test reaches beyond the new instrument. It does not refute Corpus Manifest; it reveals the edge of what was constructed. The archivist-engineer carries that edge into the following room.

#### Return to the chain-of-custody ledger

Rebuild the corpus manifest scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/176-corpus-manifest/README.md).*

---

### Excavation 177 — Document Boundaries — Keep One Story from Leaking into Another

The manifest fixes which source documents belong to the run. Tokenization can still concatenate them into a stream where the ending of one document predicts the beginning of an unrelated one.

Morning reaches the Archive Foundry before anyone has a name for today's difficulty. Beside the chain-of-custody ledger, the archivist-engineer tries the smallest continuation of what already works: join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width.

Then the quiet test arrives: a ranger report ending with “tiger tracks near” is trained to predict the first word of an unrelated software license. The model receives a relationship that never existed in either document. What looked like simplicity is revealed as a missing distinction.

*The archivist-engineer sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ join every token sequence end to end… ──▶ blurred: a ranger report ending with “tiger…
      │
      └── new lens ──▶ mark document ends, reset position… ──▶ distinction survives
```

The archivist-engineer turns the chain-of-custody ledger toward the light. Through the old engraving, join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width, the evidence ends in the same contradiction: a ranger report ending with “tiger tracks near” is trained to predict the first word of an unrelated software license. The model receives a relationship that never existed in either document. A second engraving adds only the power to mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The archivist-engineer circles the place where the two document boundaries cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended. The archivist-engineer writes **Document Boundaries** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The archivist-engineer does not memorize document boundaries. Instead, the archivist-engineer memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended. The formal name merely lets that motion be shared.

#### Keep One Story from Leaking into Another

Two short documents share one packed row, but a boundary mask lets each token read only tokens from its own document. The empty hardware space is saved without inventing a false continuation.

#### The calculation hidden inside document boundaries

The archivist-engineer carries the document boundaries scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A_ij answers one concrete yes-or-no question for token positions i and j: may information cross between them? One means the pair shares a document; zero means the boundary forbids the connection.

##### Why the melody needs these exact notes

[Cases](../MATHEMATICAL_MOVES.md#cases) are forced because same-document and cross-document pairs obey different rules. [Equality](../MATHEMATICAL_MOVES.md#equals) assigns an exact permission bit. A distance score would blur a categorical boundary, while addition would invent partial permission.

The story of document boundaries has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
A_{ij}=\begin{cases}1&\text{tokens }i,j\text{ share a document}\\0&\text{otherwise}\end{cases}
$$

#### Where document boundaries runs out

Boundary isolation prevents accidental cross-document lessons; it cannot decide whether two paragraphs really belong to the same source document.

One unsolved mark remains on the chain-of-custody ledger. None of the responsibilities inside Document Boundaries can move it, and so it becomes the observation from which the next excavation must begin.

#### Return to the chain-of-custody ledger

Rebuild the document boundaries scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/177-document-boundaries/README.md).*

---

### Excavation 178 — Language Identification — Do Not Confuse Familiar Script with Familiar Language

Document boundaries now preserve honest local context. The manifest still mixes languages, code, names, and corrupted text, so a declared English run cannot yet tell what language evidence it actually contains.

The chain-of-custody ledger at the Archive Foundry still carries the marks of the previous discovery. The archivist-engineer follows them as far as they seem willing to go: keep documents containing mostly familiar Latin characters and discard the rest.

The archivist-engineer repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: spanish and Vietnamese are mistaken for English, transliterated languages disappear, and English code or identifier lists pass despite containing little natural language. The failure is stable enough to become evidence.

*The archivist-engineer sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: keep documents containing mostly…
possible road B ─┘              └── loses: spanish and Vietnamese are mistaken…

same roads ──▶ repaired map ──▶ use a calibrated language classifier,…
```

Across the chain-of-custody ledger, the old path and the repaired path run side by side. One carries “keep documents containing mostly familiar Latin characters and discard the rest”; the other knows how to use a calibrated language classifier, retain its confidence and model version, and route uncertain documents to an explicit unknown bucket rather than forcing a label. When the failure—spanish and Vietnamese are mistaken for English, transliterated languages disappear, and English code or identifier lists pass despite containing little natural language—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to language identification. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: use a calibrated language classifier, retain its confidence and model version, and route uncertain documents to an explicit unknown bucket rather than forcing a label. This problem and its repair will travel under the name **Language Identification**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—keep documents containing mostly familiar Latin characters and discard the rest? The answer remains spanish and Vietnamese are mistaken for English, transliterated languages disappear, and English code or identifier lists pass despite containing little natural language. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

#### Do Not Confuse Familiar Script with Familiar Language

A field report receives English 0.93, Spanish 0.05, and unknown 0.02. The pipeline keeps English only because its score clears the recorded threshold; a 0.44/0.41 split is quarantined.

#### The calculation hidden inside language identification

The archivist-engineer carries the language identification scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

d is the document being inspected; the set L contains allowed language labels; p(l|d) is the classifier's support for one label; l-star is the label whose support is largest.

##### Why the melody needs these exact notes

[Conditional probability](../MATHEMATICAL_MOVES.md#conditional-bar) asks for language support given this document. [Arg max](../MATHEMATICAL_MOVES.md#arg-max) keeps the winning label rather than only its score. Summing the scores would erase which language produced them; a threshold is still checked afterward because the winner may be weak.

Cover the prose about language identification and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
\ell^*=\underset{\ell\in\mathcal L}{\mathrm{argmax}}\ p(\ell\mid d)
$$

#### Where language identification runs out

Because the classifier learned from finite examples and reduces a mixed document to one distribution, language identification remains probabilistic and domain-sensitive; short, multilingual, and code-heavy documents are especially difficult.

The language identification repair holds, but the world asks for something it was never given. At the Archive Foundry, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the chain-of-custody ledger

Rebuild the language identification scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/178-language-identification/README.md).*

---

### Excavation 179 — Exact Deduplication — Stop Paying Twice for the Same Document

Language labels make the intended corpus measurable. Counting the accepted files now reveals identical reports mirrored across archives and repeated under new filenames.

Night gathers around the Archive Foundry. Under the light of the chain-of-custody ledger, the archivist-engineer refuses to invent prematurely and begins with the plain rule: leave duplicates in place because more training examples should always help.

At the edge of the chain-of-custody ledger, the shortcut produces its consequence: one press release copied to a thousand sites receives a thousand votes, while a rare field observation receives one. Compute is spent memorizing repetition rather than encountering new evidence. That consequence, not a textbook, earns the next move.

*The archivist-engineer sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: leave duplicates in place because…
                         │
                         └── mismatch: one press release copied to a…

reference evidence ──▶ measured repair: normalize only irrelevant formatting,…
```

The archivist-engineer covers the new mark and the old contradiction returns: one press release copied to a thousand sites receives a thousand votes, while a rare field observation receives one. Compute is spent memorizing repetition rather than encountering new evidence. The cover is lifted, restoring the ability to normalize only irrelevant formatting, hash the resulting document, and keep one accountable representative for each identical hash while preserving duplicate counts in the ledger, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason exact deduplication exists.

What must change for exact deduplication is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: normalize only irrelevant formatting, hash the resulting document, and keep one accountable representative for each identical hash while preserving duplicate counts in the ledger. That threshold is where **Exact Deduplication** enters the story.

The marks on the chain-of-custody ledger form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. exact deduplication is not any single point. It is the path connecting them in the only order that makes the last point necessary.

#### Stop Paying Twice for the Same Document

Three files differ only in line endings and trailing spaces. After recorded normalization they produce the same fingerprint, so one enters training and the manifest records three original locations.

#### The calculation hidden inside exact deduplication

The archivist-engineer carries the exact deduplication scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

d is the original tiger field-report document, N performs the recorded normalization, H is a deterministic content-hash function, and h(d) is the fingerprint used to group exact copies.

##### Why the melody needs these exact notes

[Function composition](../MATHEMATICAL_MOVES.md#function-composition) fixes the order: normalize first, hash second. Reversing the order leaves irrelevant byte differences visible. [Equality](../MATHEMATICAL_MOVES.md#equals) groups only matching fingerprints; adding hashes has no interpretation and would not identify copies.

The chain-of-custody ledger already contains the complete exact deduplication mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
h(d)=H(N(d))
$$

#### Where exact deduplication runs out

Because a cryptographic hash reacts to any retained content change, exact hashes catch identical normalized text but give a copied article with one inserted advertisement a different fingerprint.

Here the new path ends honestly. Exact Deduplication can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the chain-of-custody ledger

Rebuild the exact deduplication scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/179-exact-deduplication/README.md).*

---

### Excavation 180 — Near Deduplication — When a Copy Changes a Few Words

Exact deduplication removes byte-equivalent documents. The copied article with a new banner, reordered footer, or one edited sentence still survives as apparently new evidence.

Inside the Archive Foundry, every old tool is given one honest chance. The archivist-engineer sets the chain-of-custody ledger between the evidence and the desired answer, then tries to lowercase both documents and demand that every remaining word match.

For a moment the mark looks complete. Then the evidence refuses to fit: one inserted advertisement defeats the rule, while independently written short notices can match by accident. Exact sequence equality is too brittle for disguised copies. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The archivist-engineer sketches the break before changing it:*

```text
observation
    │
    ▼
[lowercase both documents and demand…]
    │
    ╳  one inserted advertisement defeats…
    │
    ▼
[represent each document by…]
```

The archivist-engineer lays two translucent sheets over the chain-of-custody ledger. The first is inscribed, “lowercase both documents and demand that every remaining word match.” Its path ends where one inserted advertisement defeats the rule, while independently written short notices can match by accident. Exact sequence equality is too brittle for disguised copies. The second receives the same evidence but is allowed to represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale. Held to the light, the sheets separate at exactly one decision.

No one reaches for a near deduplication formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The archivist-engineer changes only that one responsibility: represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale. When the ink dries, the name **Near Deduplication** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The chain-of-custody ledger keeps both histories. Its older mark still says, ‘lowercase both documents and demand that every remaining word match’; beside it, the newer mark says, ‘represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale.’ The distance between those sentences is the exact shape of near deduplication: no larger than the failure required, and no smaller than reality permits.

#### When a Copy Changes a Few Words

The original report has ten shingles; its mirrored copy shares eight and introduces two. Their intersection has eight shingles and their union has twelve, giving similarity 8/12 rather than pretending the documents are either perfectly equal or wholly unrelated.

#### The calculation hidden inside near deduplication

The archivist-engineer carries the near deduplication scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A and B are the shingle sets from the original tiger report and its edited mirror. Their intersection counts phrases both contain; their union counts every distinct phrase appearing in either; J is the shared fraction.

##### Why the melody needs these exact notes

[Intersection](../MATHEMATICAL_MOVES.md#intersection) keeps shared evidence and [union](../MATHEMATICAL_MOVES.md#union) defines the total distinct evidence available. [Cardinality](../MATHEMATICAL_MOVES.md#cardinality) turns each set into a count. [Division](../MATHEMATICAL_MOVES.md#division) makes the overlap comparable across document lengths; a raw shared count would favor long documents.

Inside near deduplication, familiar operations return with stricter duties: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Every mark needed for near deduplication is now visible on the chain-of-custody ledger. The symbols do not add an idea; they bind the discovered moves into one line:

$$
J(A,B)=\frac{\lvert A\cap B\rvert}{\lvert A\cup B\rvert}
$$

#### Where near deduplication runs out

Near-deduplication depends on shingle size and threshold; aggressive settings can erase legitimate quotations, templates, or independent accounts.

At the Archive Foundry, the archivist-engineer leaves a blank beneath the new mark. Near Deduplication has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the chain-of-custody ledger

Rebuild the near deduplication scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/180-near-deduplication/README.md).*

---

### Excavation 181 — Quality Filtering — Remove Noise Without Defining Humanity Away

Near-deduplication leaves a corpus with more distinct documents, not necessarily better ones. Some are navigation fragments, keyword piles, machine corruption, or adversarial spam.

A new case arrives at the Archive Foundry, but the archivist-engineer first reaches for the familiar chain-of-custody ledger. Its promise is simple: keep only documents that resemble one prestigious encyclopedia.

The rule survives the easy cases. The next case leaves a crack through the middle of it: the filter removes spam, but it also suppresses informal dialect, local knowledge, code, dialogue, and communities whose writing differs from the chosen reference. More confidence cannot repair information that never entered the rule.

*The archivist-engineer sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   keep only documents that resemble one… the filter removes spam, but it also…
            \        /
             \      /
              combine transparent structural…
```

Two trails now cross the chain-of-custody ledger. The pale trail bears the instruction “keep only documents that resemble one prestigious encyclopedia.” It disappears into the observed failure: the filter removes spam, but it also suppresses informal dialect, local knowledge, code, dialogue, and communities whose writing differs from the chosen reference. The darker trail carries one additional capacity—to combine transparent structural signals with small controlled model-based tests, inspect what each threshold removes, and publish source-by-source retention counts before accepting a filter. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed quality filtering mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the chain-of-custody ledger is altered in exactly one way: combine transparent structural signals with small controlled model-based tests, inspect what each threshold removes, and publish source-by-source retention counts before accepting a filter. Much later, people will call this territory **Quality Filtering**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the chain-of-custody ledger. The failed path remains visible beneath the repair, because quality filtering is easier to remember when its scar remains attached to it. The scar reads, ‘the filter removes spam, but it also suppresses informal dialect, local knowledge, code, dialogue, and communities whose writing differs from the chosen reference’; the new line exists only to keep that loss from happening again.

#### Remove Noise Without Defining Humanity Away

The station rejects a page with 70 percent repeated navigation and no sentences, but manually audits samples near the threshold and notices that short emergency bulletins need a different rule from essays.

#### Where quality filtering runs out

Every quality filter encodes values and domain assumptions; measured downstream gains do not prove that excluded voices were unimportant.

The chain-of-custody ledger answers today's question and falls silent at the next. That silence is precise: Quality Filtering was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the chain-of-custody ledger

Rebuild the quality filtering scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/181-quality-filtering/README.md).*

---

### Excavation 182 — Data Provenance — Keep the Path Back to Every Source

Quality filtering produces an accepted set and a rejected set. Without a trace through each transformation, neither set can explain how a source document reached its decision.

The doors of the Archive Foundry close against the wind. On the chain-of-custody ledger, the archivist-engineer writes the cheapest rule that might still be true: save only the final cleaned text because intermediate metadata costs storage.

Reality answers without terminology: a rights request, filtering bug, or benchmark contamination report arrives, but the final shard cannot be mapped back to the source record or processing rule that produced it. The chain-of-custody ledger now holds two situations the old rule cannot keep apart.

*The archivist-engineer sketches the break before changing it:*

```text
OLD PATH:  request ──▶ save only the final cleaned text… ──▶ a rights request, filtering bug, or…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ assign stable document identities and… ──▶ accountable result
```

The chain-of-custody ledger is divided down the middle. Left side: “save only the final cleaned text because intermediate metadata costs storage.” Its final mark records a rights request, filtering bug, or benchmark contamination report arrives, but the final shard cannot be mapped back to the source record or processing rule that produced it. Right side: the same starting evidence, now allowed to assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given data provenance a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard. The name **Data Provenance** arrives afterward, like a title given to a path whose stones are already underfoot.

A thread now runs backward from data provenance through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and a rights request, filtering bug, or benchmark contamination report arrives, but the final shard cannot be mapped back to the source record or processing rule that produced it. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction.

#### Keep the Path Back to Every Source

Document `river-0042` points to its source URL, retrieval time, raw hash, language decision, duplicate cluster, quality audit, redaction record, and final shard offset.

#### Where data provenance runs out

Provenance makes decisions inspectable; it cannot repair a source that was collected without sufficient rights, consent, or context.

A final test reaches beyond the new instrument. It does not refute Data Provenance; it reveals the edge of what was constructed. The archivist-engineer carries that edge into the following room.

#### Return to the chain-of-custody ledger

Rebuild the data provenance scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/182-data-provenance/README.md).*

---

### Excavation 183 — PII Redaction — Do Not Turn Accidental Secrets into Lessons

Provenance can locate every retained document. Inspection now finds phone numbers, email addresses, account identifiers, and private-looking text embedded in otherwise useful pages.

Nothing in the Archive Foundry yet bears today's mathematical name. There is only the archivist-engineer, the chain-of-custody ledger, and one plausible action: remove any entire document containing a sequence that resembles personal information.

Then the quiet test arrives: one phone number erases a long public safety guide, while obfuscated addresses and context-dependent identifiers still pass. The rule destroys useful evidence without reliably removing the risky span. What looked like simplicity is revealed as a missing distinction.

*The archivist-engineer sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ remove any entire document containing… ──▶ blurred: one phone number erases a long public…
      │
      └── new lens ──▶ detect candidate spans with several… ──▶ distinction survives
```

The archivist-engineer turns the chain-of-custody ledger toward the light. Through the old engraving, remove any entire document containing a sequence that resembles personal information, the evidence ends in the same contradiction: one phone number erases a long public safety guide, while obfuscated addresses and context-dependent identifiers still pass. The rule destroys useful evidence without reliably removing the risky span. A second engraving adds only the power to detect candidate spans with several methods, classify them in context, replace confirmed sensitive spans with typed placeholders, and preserve only a restricted audit record of the decision. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The archivist-engineer circles the place where the two pii redaction cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: detect candidate spans with several methods, classify them in context, replace confirmed sensitive spans with typed placeholders, and preserve only a restricted audit record of the decision. The archivist-engineer writes **PII Redaction** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The archivist-engineer places a finger over the new distinction. At once the two cases collapse and one phone number erases a long public safety guide, while obfuscated addresses and context-dependent identifiers still pass. The rule destroys useful evidence without reliably removing the risky span. Lifting the finger restores only this capacity: detect candidate spans with several methods, classify them in context, replace confirmed sensitive spans with typed placeholders, and preserve only a restricted audit record of the decision. That tiny reversible motion is the chapter's proof of necessity.

#### Do Not Turn Accidental Secrets into Lessons

The sentence “Call Maya at 555-0142 about the injured tiger” becomes “Call [PERSON] at [PHONE] about the injured tiger”; the grammatical lesson survives while the direct identifier does not.

#### Where pii redaction runs out

Redaction has false positives and false negatives, and public availability does not by itself settle privacy, consent, or appropriate use.

One unsolved mark remains on the chain-of-custody ledger. None of the responsibilities inside PII Redaction can move it, and so it becomes the observation from which the next excavation must begin.

#### Return to the chain-of-custody ledger

Rebuild the pii redaction scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/183-pii-redaction/README.md).*

---

### Excavation 184 — Data Mixtures — Decide Which Worlds Receive a Voice

Redaction reduces one preventable privacy risk. The clean sources still differ enormously in size: web pages could drown out books, code, science, and the station's rare field reports.

At the Archive Foundry, the archivist-engineer returns to the chain-of-custody ledger. Yesterday's instrument still lies open, so the first move asks for no new magic: concatenate every accepted source and let its raw token count determine how often it appears.

The archivist-engineer repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: the largest crawl silently becomes the curriculum. A source ten thousand times smaller may almost never reach a batch even when it carries relationships absent from the web. The failure is stable enough to become evidence.

*The archivist-engineer sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: concatenate every accepted source and…
possible road B ─┘              └── loses: the largest crawl silently becomes…

same roads ──▶ repaired map ──▶ choose and publish a probability…
```

Across the chain-of-custody ledger, the old path and the repaired path run side by side. One carries “concatenate every accepted source and let its raw token count determine how often it appears”; the other knows how to choose and publish a probability weight for each domain, treating the mixture as an explicit modeling decision that must be tested on per-domain validation streams. When the failure—the largest crawl silently becomes the curriculum. A source ten thousand times smaller may almost never reach a batch even when it carries relationships absent from the web—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to data mixtures. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: choose and publish a probability weight for each domain, treating the mixture as an explicit modeling decision that must be tested on per-domain validation streams. This problem and its repair will travel under the name **Data Mixtures**, but the name carries no knowledge the scene has not earned.

What changed on the chain-of-custody ledger can be said without symbols. Before, the method could only concatenate every accepted source and let its raw token count determine how often it appears; now it can also choose and publish a probability weight for each domain, treating the mixture as an explicit modeling decision that must be tested on per-domain validation streams. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

#### Decide Which Worlds Receive a Voice

The station assigns 0.50 to curated web text, 0.20 to science, 0.15 to code, 0.10 to books, and 0.05 to field reports. The five shares exhaust one draw without pretending the sources are equally large or equally important.

#### The calculation hidden inside data mixtures

The archivist-engineer carries the data mixtures scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

D counts the named data domains and w_d is the chance that the next training draw chooses domain d. Nonnegative weights prevent negative sampling; a total of one exhausts all possible domain choices.

##### Why the melody needs these exact notes

[Summation](../MATHEMATICAL_MOVES.md#summation) combines mutually exclusive domain shares into the whole probability mass. Multiplication would make one zero-weight domain erase the mixture. [Equality](../MATHEMATICAL_MOVES.md#equals) requires a complete distribution, while the [inequality](../MATHEMATICAL_MOVES.md#inequalities) forbids impossible negative shares.

Listen beneath data mixtures: **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Cover the prose about data mixtures and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
\sum_{d=1}^{D}w_d=1,\quad w_d\ge 0
$$

#### Where data mixtures runs out

Mixture weights redistribute attention but cannot make a poor or missing domain representative, accurate, or safe.

The data mixtures repair holds, but the world asks for something it was never given. At the Archive Foundry, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the chain-of-custody ledger

Rebuild the data mixtures scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/184-data-mixtures/README.md).*

---

### Excavation 185 — Mixture Sampling — Turn Planned Shares into a Reproducible Stream

The mixture weights state which domains should be heard. They do not yet produce a finite ordered token stream that every resumed worker can reconstruct.

Morning reaches the Archive Foundry before anyone has a name for today's difficulty. Beside the chain-of-custody ledger, the archivist-engineer tries the smallest continuation of what already works: round each domain's desired share independently and concatenate the resulting blocks.

At the edge of the chain-of-custody ledger, the shortcut produces its consequence: independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero. That consequence, not a textbook, earns the next move.

*The archivist-engineer sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: round each domain's desired share…
                         │
                         └── mismatch: independent rounding can exceed the…

reference evidence ──▶ measured repair: use a seeded categorical schedule,…
```

The archivist-engineer covers the new mark and the old contradiction returns: independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero. The cover is lifted, restoring the ability to use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason mixture sampling exists.

What must change for mixture sampling is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source. That threshold is where **Mixture Sampling** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In mixture sampling, that memory takes a precise form: whenever independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero, preserve enough structure to use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source.

#### Turn Planned Shares into a Reproducible Stream

For 1,000 document draws, a 0.05 field-report weight expects about 50 selections. The seeded schedule interleaves those reports with other domains and records the actual count rather than promising exact equality by chance.

#### The calculation hidden inside mixture sampling

The archivist-engineer carries the mixture sampling scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

N is the total number of scheduled training draws, w_d is domain d's share, n_d is its realized count, and E[n_d] is the average count expected across many schedules.

##### Why the melody needs these exact notes

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) is forced because each of N draws independently offers domain d the same share w_d. Addition would grant a fixed number unrelated to run length. [Expectation](../MATHEMATICAL_MOVES.md#expectation) describes a long-run average, not a guarantee that one finite schedule equals Nw_d exactly.

The calculation borrows several gestures already encountered elsewhere: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the council of possible worlds**—each future speaks in proportion to how often it may arrive. mixture sampling feels new because the objects are new; the gestures remain recognizably human.

The chain-of-custody ledger already contains the complete mixture sampling mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
E[n_d]=Nw_d
$$

#### Where mixture sampling runs out

Sampling realizes probabilities only approximately in a finite run, and replacement can repeat scarce documents enough to increase memorization.

Here the new path ends honestly. Mixture Sampling can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the chain-of-custody ledger

Rebuild the mixture sampling scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/185-mixture-sampling/README.md).*

---

### Excavation 186 — The Token Budget — Convert a Training Plan into a Count of Lessons

Seeded mixture sampling can produce an ordered stream. The run still says “train for a while,” so neither cost nor source exposure is bounded.

The chain-of-custody ledger at the Archive Foundry still carries the marks of the previous discovery. The archivist-engineer follows them as far as they seem willing to go: stop when the wall clock reaches an affordable date.

For a moment the mark looks complete. Then the evidence refuses to fit: faster hardware sees more tokens, interruptions see fewer, and two runs with the same calendar budget teach different amounts of evidence. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The archivist-engineer sketches the break before changing it:*

```text
observation
    │
    ▼
[stop when the wall clock reaches an…]
    │
    ╳  faster hardware sees more tokens,…
    │
    ▼
[define the run by optimization steps…]
```

The archivist-engineer lays two translucent sheets over the chain-of-custody ledger. The first is inscribed, “stop when the wall clock reaches an affordable date.” Its path ends where faster hardware sees more tokens, interruptions see fewer, and two runs with the same calendar budget teach different amounts of evidence. The second receives the same evidence but is allowed to define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute. Held to the light, the sheets separate at exactly one decision.

No one reaches for a token budget formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The archivist-engineer changes only that one responsibility: define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute. When the ink dries, the name **The Token Budget** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because faster hardware sees more tokens, interruptions see fewer, and two runs with the same calendar budget teach different amounts of evidence, while the other can define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute. That fork—not the vocabulary—is where token budget lives.

#### Convert a Training Plan into a Count of Lessons

A tiny run uses 2,000 updates with 32 sequences of 128 real tokens each. Every update carries 4,096 lessons, so the complete plan exposes 8,192,000 tokens.

#### The calculation hidden inside the token budget

The archivist-engineer carries the token budget scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

T is the planned number of optimizer updates, B_tokens counts real loss-bearing tokens in one global batch, and N_tokens is the complete exposure budget.

##### Why the melody needs these exact notes

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) appears because every one of T updates consumes B_tokens lessons. Addition would count only one update plus one batch. Padding is excluded because it occupies hardware but contributes no language target.

Three old motions cast new shadows here: **the lock and key**—one influence matters through another, and either missing factor can close the path. Remember the motions and the formula can be rebuilt even after its letters have been forgotten.

Every mark needed for token budget is now visible on the chain-of-custody ledger. The symbols do not add an idea; they bind the discovered moves into one line:

$$
N_{\text{tokens}}=T B_{\text{tokens}}
$$

#### Where the token budget runs out

Equal token counts do not imply equal compute when model size, sequence length, sparsity, or hardware efficiency differs.

At the Archive Foundry, the archivist-engineer leaves a blank beneath the new mark. Token Budget has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the chain-of-custody ledger

Rebuild the token budget scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/186-token-budget/README.md).*

---

### Excavation 187 — Compute-Optimal Allocation — Buy a Larger Memory or More Experience?

The token budget fixes how much evidence the model will see. A fixed compute allowance still permits a wider model trained on fewer tokens or a smaller model trained on more.

Night gathers around the Archive Foundry. Under the light of the chain-of-custody ledger, the archivist-engineer refuses to invent prematurely and begins with the plain rule: spend nearly the entire budget on parameter count because a larger model can store more patterns.

The rule survives the easy cases. The next case leaves a crack through the middle of it: the large model is stopped after too little experience and remains undertrained, while much of its expensive capacity never receives enough varied evidence. More confidence cannot repair information that never entered the rule.

*The archivist-engineer sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   spend nearly the entire budget on… the large model is stopped after too…
            \        /
             \      /
              estimate candidate…
```

Two trails now cross the chain-of-custody ledger. The pale trail bears the instruction “spend nearly the entire budget on parameter count because a larger model can store more patterns.” It disappears into the observed failure: the large model is stopped after too little experience and remains undertrained, while much of its expensive capacity never receives enough varied evidence. The darker trail carries one additional capacity—to estimate candidate parameter-and-token pairs under the same compute budget, run smaller scaling experiments, and choose the pair predicted to minimize held-out loss rather than maximizing either axis alone. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed compute-optimal allocation mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the chain-of-custody ledger is altered in exactly one way: estimate candidate parameter-and-token pairs under the same compute budget, run smaller scaling experiments, and choose the pair predicted to minimize held-out loss rather than maximizing either axis alone. Much later, people will call this territory **Compute-Optimal Allocation**. Here the name is only a memory of the failure it can survive.

The chain-of-custody ledger has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and compute-optimal allocation looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

#### Buy a Larger Memory or More Experience

The station compares doubling parameters while halving tokens with keeping the smaller model and doubling tokens. Because both alter the same compute bill, held-out scaling runs decide which balance learns more.

#### The calculation hidden inside compute-optimal allocation

The archivist-engineer carries the compute-optimal allocation scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

P is the number of trainable model parameters, D is the number of training tokens, and C is a rough count of floating-point work for dense Transformer training; six summarizes forward and backward work per parameter-token interaction.

##### Why the melody needs these exact notes

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) is forced because every token exercises the model's parameters: doubling either P or D roughly doubles work. [Approximation](../MATHEMATICAL_MOVES.md#approximation) preserves the scaling relation while admitting architecture and implementation details. Adding P and D would combine incompatible units.

The symbols are about to change costume, but their work has appeared before: **the lock and key**—one influence matters through another, and either missing factor can close the path. This is how distant excavations begin to sound like variations of one melody.

The archivist-engineer reads the journey of compute-optimal allocation once more across the chain-of-custody ledger, then lets the words contract without losing their order:

$$
C\approx 6PD
$$

#### Where compute-optimal allocation runs out

Compute-optimal estimates are empirical and depend on architecture, data quality, optimizer, and the inference cost the project can afford afterward.

The chain-of-custody ledger answers today's question and falls silent at the next. That silence is precise: Compute-Optimal Allocation was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the chain-of-custody ledger

Rebuild the compute-optimal allocation scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/187-compute-optimal-allocation/README.md).*

---

### Excavation 188 — Learning-Rate Warmup — Let Adam Learn the Terrain Before Running

Compute allocation chooses the model and token horizon. At the first update, Adam's moment memories contain almost no history, while randomly initialized activations and gradients are changing fastest.

Inside the Archive Foundry, every old tool is given one honest chance. The archivist-engineer sets the chain-of-custody ledger between the evidence and the desired answer, then tries to begin immediately at the peak learning rate chosen for the stable middle of training.

Reality answers without terminology: the first noisy batches can make large updates before the optimizer's scale estimates become trustworthy, producing a loss spike that the later stable rate would not have caused. The chain-of-custody ledger now holds two situations the old rule cannot keep apart.

*The archivist-engineer sketches the break before changing it:*

```text
OLD PATH:  request ──▶ begin immediately at the peak… ──▶ the first noisy batches can make…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ increase the learning rate gradually… ──▶ accountable result
```

The chain-of-custody ledger is divided down the middle. Left side: “begin immediately at the peak learning rate chosen for the stable middle of training.” Its final mark records the first noisy batches can make large updates before the optimizer's scale estimates become trustworthy, producing a loss spike that the later stable rate would not have caused. Right side: the same starting evidence, now allowed to increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given learning-rate warmup a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule. The name **Learning-Rate Warmup** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to begin immediately at the peak learning rate chosen for the stable middle of training; on the other lies the observed fact that the first noisy batches can make large updates before the optimizer's scale estimates become trustworthy, producing a loss spike that the later stable rate would not have caused. The bridge called learning-rate warmup has exactly the planks needed to increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule.

#### Let Adam Learn the Terrain Before Running

With peak rate 0.001 and 100 warmup updates, update 25 receives 0.00025, update 50 receives 0.0005, and update 100 finally reaches 0.001.

#### The calculation hidden inside learning-rate warmup

The archivist-engineer carries the learning-rate warmup scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

t is the current model warmup update, T_warm is the number of warmup updates, eta_peak is the intended stable rate, and eta_t is the smaller rate used now.

##### Why the melody needs these exact notes

[Division](../MATHEMATICAL_MOVES.md#division) turns elapsed warmup steps into a progress fraction from zero to one. [Multiplication](../MATHEMATICAL_MOVES.md#multiplication) applies that fraction to the peak rate. Adding t would mix step counts with a rate; jumping directly to eta_peak recreates the failed attempt.

Inside learning-rate warmup, familiar operations return with stricter duties: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; and **the lock and key**—one influence matters through another, and either missing factor can close the path. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Nothing remains unnamed in the learning-rate warmup case on the chain-of-custody ledger. We can finally trade the long route for its compact map:

$$
\eta_t=\eta_{\text{peak}}\frac{t}{T_{\text{warm}}}\quad(0\le t\le T_{\text{warm}})
$$

#### Where learning-rate warmup runs out

Warmup reduces early shock but cannot rescue an unsuitable peak rate, broken initialization, corrupt batch, or incorrect optimizer state.

A final test reaches beyond the new instrument. It does not refute Learning-Rate Warmup; it reveals the edge of what was constructed. The archivist-engineer carries that edge into the following room.

#### Return to the chain-of-custody ledger

Rebuild the learning-rate warmup scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/188-learning-rate-warmup/README.md).*

---

### Excavation 189 — Cosine Decay — Make Late Corrections Smaller Without a Cliff

Warmup protects the optimizer's first steps. Keeping the peak rate for the entire token budget makes late updates as aggressive as early ones even when the model is refining rather than discovering broad structure.

A new case arrives at the Archive Foundry, but the archivist-engineer first reaches for the familiar chain-of-custody ledger. Its promise is simple: drop the rate abruptly near the end of training.

Then the quiet test arrives: a sudden cliff changes update scale in one step and makes the chosen drop date an arbitrary discontinuity; dropping too early freezes useful learning. What looked like simplicity is revealed as a missing distinction.

*The archivist-engineer sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ drop the rate abruptly near the end… ──▶ blurred: a sudden cliff changes update scale…
      │
      └── new lens ──▶ decay smoothly from the peak toward a… ──▶ distinction survives
```

The archivist-engineer turns the chain-of-custody ledger toward the light. Through the old engraving, drop the rate abruptly near the end of training, the evidence ends in the same contradiction: a sudden cliff changes update scale in one step and makes the chosen drop date an arbitrary discontinuity; dropping too early freezes useful learning. A second engraving adds only the power to decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The archivist-engineer circles the place where the two cosine decay cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state. The archivist-engineer writes **Cosine Decay** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The archivist-engineer does not memorize cosine decay. Instead, the archivist-engineer memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state. The formal name merely lets that motion be shared.

#### Make Late Corrections Smaller Without a Cliff

Halfway through decay, cosine is zero, so the rate sits halfway between its peak and minimum. At the final planned update, cosine reaches negative one and the rate reaches the minimum without a jump.

#### The calculation hidden inside cosine decay

The archivist-engineer carries the cosine decay scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

t is model-training progress through the decay interval of length T; eta_max and eta_min are its endpoint rates; cosine supplies a smooth path between them.

##### Why the melody needs these exact notes

[Subtraction](../MATHEMATICAL_MOVES.md#subtraction) isolates the adjustable rate range, [division](../MATHEMATICAL_MOVES.md#division) converts progress to a fraction, and [cosine](../MATHEMATICAL_MOVES.md#cosine) bends that fraction smoothly with flat endpoint slopes. Addition places the scaled range above eta_min. A raw linear drop is possible, but cosine avoids an abrupt endpoint slope.

Trace each operation by touch rather than by name: **the chisel**—what is shared is removed so the remaining change can be seen; **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; and **the returning tide**—movement bends smoothly and reaches its shore without a cliff. Together they form the smallest mechanism that survives the counterexample.

The story of cosine decay has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
\eta_t=\eta_{\min}+\frac{\eta_{\max}-\eta_{\min}}{2}\left(1+\cos\frac{\pi t}{T}\right)
$$

#### Where cosine decay runs out

Cosine decay assumes a known horizon and is not automatically optimal when training is unexpectedly extended.

One unsolved mark remains on the chain-of-custody ledger. None of the responsibilities inside Cosine Decay can move it, and so it becomes the observation from which the next excavation must begin.

#### Return to the chain-of-custody ledger

Rebuild the cosine decay scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/189-cosine-decay/README.md).*

---

### Excavation 190 — Gradient Noise Scale — When More Examples Stop Buying More Direction

The schedule controls how far one global update moves. We still do not know how many examples should vote in that update before extra devices mostly repeat the same directional evidence.

The doors of the Archive Foundry close against the wind. On the chain-of-custody ledger, the archivist-engineer writes the cheapest rule that might still be true: make the global batch as large as the cluster permits.

The archivist-engineer repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: early doubling reduces disagreement and improves the direction, but beyond a workload-dependent point the averaged gradient barely changes while each update consumes twice as many tokens. The failure is stable enough to become evidence.

*The archivist-engineer sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: make the global batch as large as the…
possible road B ─┘              └── loses: early doubling reduces disagreement…

same roads ──▶ repaired map ──▶ measure disagreement among…
```

Across the chain-of-custody ledger, the old path and the repaired path run side by side. One carries “make the global batch as large as the cluster permits”; the other knows how to measure disagreement among micro-batch gradients relative to the strength of their shared direction, and use that noise scale as evidence for the largest useful batch rather than a hardware target. When the failure—early doubling reduces disagreement and improves the direction, but beyond a workload-dependent point the averaged gradient barely changes while each update consumes twice as many tokens—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to gradient noise scale. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: measure disagreement among micro-batch gradients relative to the strength of their shared direction, and use that noise scale as evidence for the largest useful batch rather than a hardware target. This problem and its repair will travel under the name **Gradient Noise Scale**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—make the global batch as large as the cluster permits? The answer remains early doubling reduces disagreement and improves the direction, but beyond a workload-dependent point the averaged gradient barely changes while each update consumes twice as many tokens. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

#### When More Examples Stop Buying More Direction

Three named micro-batches question the same two weights: the field reports propose [2.0,1.0], science proposes [2.1,0.9], and books propose [1.9,1.1]. The first number is advice to the tiger-before-river weight; the second is advice to a punctuation weight. Their mean [2.0,1.0] is strong and their disagreement around it is small. If the witnesses instead propose [4,−2], [0,4], and [2,1], disagreement is large relative to the same broad direction, so a larger batch can still buy useful certainty.

#### The calculation hidden inside gradient noise scale

The archivist-engineer carries the gradient noise scale scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Each g_i is one model micro-batch's gradient advice. The covariance measures how those witnesses disagree; its trace totals disagreement across coordinates. The squared norm of their mean measures the strength of the shared direction; G compares noise with signal.

##### Why the melody needs these exact notes

[Covariance](../MATHEMATICAL_MOVES.md#covariance) keeps variation around the common advice rather than raw gradient size. [Trace](../MATHEMATICAL_MOVES.md#trace) gathers coordinate variances without inventing cross-coordinate units. [Division](../MATHEMATICAL_MOVES.md#division) asks disagreement per unit of squared shared direction; subtraction would not remove dependence on signal scale.

The mandala has curved back upon itself. In this chamber we meet **the paired dance**—two quantities reveal whether their departures move together; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. What seemed like a new formula is older mathematical instinct arranged around a new need.

Cover the prose about gradient noise scale and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
G=\frac{\mathrm{tr}(\mathrm{Cov}[g_i])}{\lVert E[g_i]\rVert^2}
$$

#### Where gradient noise scale runs out

Gradient noise scale is an empirical guide, not a universal batch-size law; it changes during training and with the task and optimizer.

The gradient noise scale repair holds, but the world asks for something it was never given. At the Archive Foundry, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the chain-of-custody ledger

Rebuild the gradient noise scale scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/190-gradient-noise-scale/README.md).*

---

### Excavation 191 — Data Parallelism — Let Several Workers Observe Different Evidence

Gradient noise measurements choose a useful global batch. One device cannot process that batch quickly enough, even though the modern model and optimizer state now fit through sharding.

Nothing in the Archive Foundry yet bears today's mathematical name. There is only the archivist-engineer, the chain-of-custody ledger, and one plausible action: send the same mini-batch to every worker and average their gradients.

At the edge of the chain-of-custody ledger, the shortcut produces its consequence: all workers repeat the same computation and return the same evidence, so hardware cost rises without increasing batch diversity or reducing step time meaningfully. That consequence, not a textbook, earns the next move.

*The archivist-engineer sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: send the same mini-batch to every…
                         │
                         └── mismatch: all workers repeat the same…

reference evidence ──▶ measured repair: replicate the current model view,…
```

The archivist-engineer covers the new mark and the old contradiction returns: all workers repeat the same computation and return the same evidence, so hardware cost rises without increasing batch diversity or reducing step time meaningfully. The cover is lifted, restoring the ability to replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason data parallelism exists.

What must change for data parallelism is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update. That threshold is where **Data Parallelism** enters the story.

The marks on the chain-of-custody ledger form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. data parallelism is not any single point. It is the path connecting them in the only order that makes the last point necessary.

#### Let Several Workers Observe Different Evidence

Four workers each read eight different sequences. Their four average gradients become one average over thirty-two sequences before any worker advances the parameters.

#### The calculation hidden inside data parallelism

The archivist-engineer carries the data parallelism scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

P is the number of data-parallel workers, g_p is worker p's average gradient from different examples, and g is the single gradient used by the shared optimizer step.

##### Why the melody needs these exact notes

[Summation](../MATHEMATICAL_MOVES.md#summation) lets every worker's independent evidence contribute. [Division](../MATHEMATICAL_MOVES.md#division) returns advice per worker so adding hardware does not enlarge the update by itself. Multiplication would let a zero coordinate from one worker erase all others.

Before the line is compressed, notice its recurring motions: **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. They are the handholds by which the reader can later climb back from notation to meaning.

The chain-of-custody ledger already contains the complete data parallelism mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
g=\frac1P\sum_{p=1}^{P}g_p
$$

#### Where data parallelism runs out

Because one shared update cannot proceed until every worker's evidence has joined the average, synchronous data parallelism waits for the slowest worker and communicates a full update's worth of gradient information.

Here the new path ends honestly. Data Parallelism can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the chain-of-custody ledger

Rebuild the data parallelism scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/191-data-parallelism/README.md).*

---

### Excavation 192 — Pipeline Parallelism — Stop Waiting for the Whole Model to Cross One Device at a Time

Data parallel workers process different examples, but each replica still needs the model's sequential layers. Splitting those layers across devices makes only one device active if a whole batch traverses the stages at once.

At the Archive Foundry, the archivist-engineer returns to the chain-of-custody ledger. Yesterday's instrument still lies open, so the first move asks for no new magic: send one complete batch through stage one, then stage two, then stage three.

For a moment the mark looks complete. Then the evidence refuses to fit: while stage two works, stage one and stage three wait. The model fits, but most devices are idle for most of the step. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The archivist-engineer sketches the break before changing it:*

```text
observation
    │
    ▼
[send one complete batch through stage…]
    │
    ╳  while stage two works, stage one and…
    │
    ▼
[split the batch into micro-batches…]
```

The archivist-engineer lays two translucent sheets over the chain-of-custody ledger. The first is inscribed, “send one complete batch through stage one, then stage two, then stage three.” Its path ends where while stage two works, stage one and stage three wait. The model fits, but most devices are idle for most of the step. The second receives the same evidence but is allowed to split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently. Held to the light, the sheets separate at exactly one decision.

No one reaches for a pipeline parallelism formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The archivist-engineer changes only that one responsibility: split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently. When the ink dries, the name **Pipeline Parallelism** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The chain-of-custody ledger keeps both histories. Its older mark still says, ‘send one complete batch through stage one, then stage two, then stage three’; beside it, the newer mark says, ‘split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently.’ The distance between those sentences is the exact shape of pipeline parallelism: no larger than the failure required, and no smaller than reality permits.

#### Stop Waiting for the Whole Model to Cross One Device at a Time

With four pipeline stages and eight micro-batches, the first few clock slots fill the pipeline, eight slots carry useful work, and the last few drain it. More micro-batches shrink the idle fraction.

#### The calculation hidden inside pipeline parallelism

The archivist-engineer carries the pipeline parallelism scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

m is the number of model micro-batches and p the number of pipeline stages in a simple forward pipeline. Useful work occupies m slots; filling and draining add p−1 slots; U is the idealized occupied share.

##### Why the melody needs these exact notes

[Addition](../MATHEMATICAL_MOVES.md#addition) joins useful slots with unavoidable fill-and-drain slots. [Division](../MATHEMATICAL_MOVES.md#division) turns useful slots into a share of total schedule time. Multiplying m and p would count stage-tasks, not the fraction of time one stage remains usefully occupied.

Listen beneath pipeline parallelism: **the joining river**—separate contributions meet without losing where they came from; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Every mark needed for pipeline parallelism is now visible on the chain-of-custody ledger. The symbols do not add an idea; they bind the discovered moves into one line:

$$
U=\frac{m}{m+p-1}
$$

#### Where pipeline parallelism runs out

Because sequential layer dependencies require the pipeline to fill and drain, pipeline parallelism introduces bubbles and activation transfers; making micro-batches too small can then reduce the efficiency of each matrix operation.

At the Archive Foundry, the archivist-engineer leaves a blank beneath the new mark. Pipeline Parallelism has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the chain-of-custody ledger

Rebuild the pipeline parallelism scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/192-pipeline-parallelism/README.md).*

---

### Excavation 193 — Three-Dimensional Parallelism — Give Each Memory Wall Its Own Axis

Pipeline micro-batches keep layer stages busy. A large run may still exceed memory inside one layer, require more independent data witnesses, and contain too many layers for one device group.

Morning reaches the Archive Foundry before anyone has a name for today's difficulty. Beside the chain-of-custody ledger, the archivist-engineer tries the smallest continuation of what already works: increase whichever parallel technique was introduced most recently until the model fits.

The rule survives the easy cases. The next case leaves a crack through the middle of it: more pipeline stages increase bubbles, more tensor splits increase frequent communication, and more data replicas preserve full model memory. One axis cannot solve three different limits efficiently. More confidence cannot repair information that never entered the rule.

*The archivist-engineer sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   increase whichever parallel technique… more pipeline stages increase…
            \        /
             \      /
              compose tensor parallelism within…
```

Two trails now cross the chain-of-custody ledger. The pale trail bears the instruction “increase whichever parallel technique was introduced most recently until the model fits.” It disappears into the observed failure: more pipeline stages increase bubbles, more tensor splits increase frequent communication, and more data replicas preserve full model memory. One axis cannot solve three different limits efficiently. The darker trail carries one additional capacity—to compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed three-dimensional parallelism mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the chain-of-custody ledger is altered in exactly one way: compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost. Much later, people will call this territory **Three-Dimensional Parallelism**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the chain-of-custody ledger. The failed path remains visible beneath the repair, because three-dimensional parallelism is easier to remember when its scar remains attached to it. The scar reads, ‘more pipeline stages increase bubbles, more tensor splits increase frequent communication, and more data replicas preserve full model memory. One axis cannot solve three different limits efficiently’; the new line exists only to keep that loss from happening again.

#### Give Each Memory Wall Its Own Axis

Two tensor workers form each layer, four pipeline stages hold the depth, and three data replicas see different examples. The run uses 2×4×3=24 workers with each axis performing one named job.

#### The calculation hidden inside three-dimensional parallelism

The archivist-engineer carries the three-dimensional parallelism scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Each factor counts independent choices along one model-parallel axis. Selecting one tensor rank, one pipeline rank, and one data rank identifies exactly one worker; P_total counts all such combinations.

##### Why the melody needs these exact notes

[Multiplication](../MATHEMATICAL_MOVES.md#multiplication) is forced by the product rule: every choice on one axis pairs with every choice on the others. Addition would count axis labels rather than workers. [Equality](../MATHEMATICAL_MOVES.md#equals) assumes the grid is fully populated.

The calculation borrows several gestures already encountered elsewhere: **the lock and key**—one influence matters through another, and either missing factor can close the path. three-dimensional parallelism feels new because the objects are new; the gestures remain recognizably human.

The archivist-engineer reads the journey of three-dimensional parallelism once more across the chain-of-custody ledger, then lets the words contract without losing their order:

$$
P_{\text{total}}=P_{\text{tensor}}P_{\text{pipeline}}P_{\text{data}}
$$

#### Where three-dimensional parallelism runs out

Three-dimensional parallelism increases coordination and configuration complexity; a poor mapping to the physical network can spend more time communicating than computing.

The chain-of-custody ledger answers today's question and falls silent at the next. That silence is precise: Three-Dimensional Parallelism was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the chain-of-custody ledger

Rebuild the three-dimensional parallelism scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/193-three-dimensional-parallelism/README.md).*

---

### Excavation 194 — Sharded Checkpoints — Save One Recoverable State Without Gathering It

Three-dimensional parallelism spreads parameters, moments, gradients, and progress across many owners. Asking one coordinator to gather everything before saving can exceed its memory and stall the cluster.

The chain-of-custody ledger at the Archive Foundry still carries the marks of the previous discovery. The archivist-engineer follows them as far as they seem willing to go: let every worker write its local tensors and call the directory a checkpoint.

Reality answers without terminology: a worker fails before writing, two shards belong to different steps, or a filename is reused. The directory exists but cannot reconstruct one globally consistent training state. The chain-of-custody ledger now holds two situations the old rule cannot keep apart.

*The archivist-engineer sketches the break before changing it:*

```text
OLD PATH:  request ──▶ let every worker write its local… ──▶ a worker fails before writing, two…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ write versioned shards to temporary… ──▶ accountable result
```

The chain-of-custody ledger is divided down the middle. Left side: “let every worker write its local tensors and call the directory a checkpoint.” Its final mark records a worker fails before writing, two shards belong to different steps, or a filename is reused. The directory exists but cannot reconstruct one globally consistent training state. Right side: the same starting evidence, now allowed to write versioned shards to temporary locations, record hashes and ownership in a checkpoint manifest, and publish one atomic completion marker only after every required shard is durable. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given sharded checkpoints a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: write versioned shards to temporary locations, record hashes and ownership in a checkpoint manifest, and publish one atomic completion marker only after every required shard is durable. The name **Sharded Checkpoints** arrives afterward, like a title given to a path whose stones are already underfoot.

A thread now runs backward from sharded checkpoints through the room. Tug it and the repair disappears; tug again and the old rule returns; follow that rule to its end and a worker fails before writing, two shards belong to different steps, or a filename is reused. The directory exists but cannot reconstruct one globally consistent training state. The mathematics is not a collection of names but a chain of consequences that can be walked in either direction.

#### Save One Recoverable State Without Gathering It

Twenty-four workers save step 8,000. The manifest expects twenty-four parameter shards, optimizer shards, scheduler state, RNG state, and data cursors; the checkpoint becomes eligible for recovery only when every recorded hash verifies.

#### Where sharded checkpoints runs out

A complete checkpoint limits lost work but consumes storage and I/O bandwidth; frequent synchronous saves can dominate training time.

A final test reaches beyond the new instrument. It does not refute Sharded Checkpoints; it reveals the edge of what was constructed. The archivist-engineer carries that edge into the following room.

#### Return to the chain-of-custody ledger

Rebuild the sharded checkpoints scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/194-sharded-checkpoints/README.md).*

---

### Excavation 195 — Deterministic Resume — Continue the Same Experiment, Not a Similar One

The sharded checkpoint can reconstruct every distributed tensor. If it omits the sampler cursor, random-number generators, scheduler phase, or overflow state, restart follows a different future.

Night gathers around the Archive Foundry. Under the light of the chain-of-custody ledger, the archivist-engineer refuses to invent prematurely and begins with the plain rule: restore model weights and let every other component start fresh.

Then the quiet test arrives: adam forgets its moments, warmup may begin again, dropout chooses different masks, and data workers repeat or skip documents. The loss curve after restart cannot be attributed to the original run. What looked like simplicity is revealed as a missing distinction.

*The archivist-engineer sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ restore model weights and let every… ──▶ blurred: adam forgets its moments, warmup may…
      │
      └── new lens ──▶ checkpoint every state variable that… ──▶ distinction survives
```

The archivist-engineer turns the chain-of-custody ledger toward the light. Through the old engraving, restore model weights and let every other component start fresh, the evidence ends in the same contradiction: adam forgets its moments, warmup may begin again, dropout chooses different masks, and data workers repeat or skip documents. The loss curve after restart cannot be attributed to the original run. A second engraving adds only the power to checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The archivist-engineer circles the place where the two deterministic resume cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps. The archivist-engineer writes **Deterministic Resume** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The archivist-engineer places a finger over the new distinction. At once the two cases collapse and adam forgets its moments, warmup may begin again, dropout chooses different masks, and data workers repeat or skip documents. The loss curve after restart cannot be attributed to the original run. Lifting the finger restores only this capacity: checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps. That tiny reversible motion is the chapter's proof of necessity.

#### Continue the Same Experiment, Not a Similar One

The station stops after update 200, restores weights, Adam moments, schedule position, scaler, RNG streams, and each data cursor, then reproduces updates 201 through 205 byte for byte on the reference implementation.

#### Where deterministic resume runs out

Exact replay can still fail across nondeterministic kernels, changed hardware, libraries, or distributed timing; the required reproducibility level must be stated.

One unsolved mark remains on the chain-of-custody ledger. None of the responsibilities inside Deterministic Resume can move it, and so it becomes the observation from which the next excavation must begin.

#### Return to the chain-of-custody ledger

Rebuild the deterministic resume scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/195-deterministic-resume/README.md).*

---

### Excavation 196 — Loss Spikes — Distinguish One Hard Batch from a Run Leaving the Road

Deterministic resume makes failures reproducible. During a long run, the observed loss sometimes jumps; automatically rewinding every jump wastes compute, while ignoring a sustained instability can destroy the model.

Inside the Archive Foundry, every old tool is given one honest chance. The archivist-engineer sets the chain-of-custody ledger between the evidence and the desired answer, then tries to declare any loss larger than the previous loss a failure and restore immediately.

The archivist-engineer repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: ordinary batches vary, so healthy learning triggers constant rollbacks. A slow divergence can rise without one dramatic step and escape the rule. The failure is stable enough to become evidence.

*The archivist-engineer sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: declare any loss larger than the…
possible road B ─┘              └── loses: ordinary batches vary, so healthy…

same roads ──▶ repaired map ──▶ compare current loss and gradient…
```

Across the chain-of-custody ledger, the old path and the repaired path run side by side. One carries “declare any loss larger than the previous loss a failure and restore immediately”; the other knows how to compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response. When the failure—ordinary batches vary, so healthy learning triggers constant rollbacks. A slow divergence can rise without one dramatic step and escape the rule—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to loss spikes. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response. This problem and its repair will travel under the name **Loss Spikes**, but the name carries no knowledge the scene has not earned.

What changed on the chain-of-custody ledger can be said without symbols. Before, the method could only declare any loss larger than the previous loss a failure and restore immediately; now it can also compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

#### Distinguish One Hard Batch from a Run Leaving the Road

Recent clean validation losses center near 2.0 with spread 0.1. One batch reaches 2.35 and then returns; another run stays above 2.5 while gradient norm grows. Only the persistent, corroborated event triggers recovery.

#### The calculation hidden inside loss spikes

The archivist-engineer carries the loss spikes scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

L_t is the current monitored model loss, mu_t is its robust recent center, sigma_t is ordinary recent spread, and z_t says how many usual spreads the current value lies above or below that center.

##### Why the melody needs these exact notes

[Subtraction](../MATHEMATICAL_MOVES.md#subtraction) removes the local baseline. [Division](../MATHEMATICAL_MOVES.md#division) expresses the remainder in units of ordinary variation, making different loss scales comparable. A raw threshold would behave differently as normal loss falls during training.

Inside loss spikes, familiar operations return with stricter duties: **the chisel**—what is shared is removed so the remaining change can be seen; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Cover the prose about loss spikes and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
z_t=\frac{L_t-\mu_t}{\sigma_t}
$$

#### Where loss spikes runs out

Thresholds detect symptoms, not causes; corrupt data, overflow, optimizer settings, hardware faults, and architectural instability require different repairs.

The loss spikes repair holds, but the world asks for something it was never given. At the Archive Foundry, that unmet need is preserved rather than hidden behind a stronger claim.

#### Return to the chain-of-custody ledger

Rebuild the loss spikes scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/196-loss-spike-recovery/README.md).*

---

### Excavation 197 — A Validation Stream — Ask Whether Learning Survives Outside the Current Batch

Loss-spike monitoring protects the training process from obvious instability. A smooth training curve can still improve mainly on repeated or overrepresented training domains.

A new case arrives at the Archive Foundry, but the archivist-engineer first reaches for the familiar chain-of-custody ledger. Its promise is simple: evaluate only the next training batch because it is already available.

At the edge of the chain-of-custody ledger, the shortcut produces its consequence: the same data mixture and duplicates that shaped the update also judge it. Training loss can fall while held-out language or a rare domain becomes worse. That consequence, not a textbook, earns the next move.

*The archivist-engineer sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: evaluate only the next training batch…
                         │
                         └── mismatch: the same data mixture and duplicates…

reference evidence ──▶ measured repair: maintain versioned, deduplicated,…
```

The archivist-engineer covers the new mark and the old contradiction returns: the same data mixture and duplicates that shaped the update also judge it. Training loss can fall while held-out language or a rare domain becomes worse. The cover is lifted, restoring the ability to maintain versioned, deduplicated, contamination-checked validation streams by domain and evaluate them at recorded token intervals without using them to update weights, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason validation stream exists.

What must change for validation stream is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: maintain versioned, deduplicated, contamination-checked validation streams by domain and evaluate them at recorded token intervals without using them to update weights. That threshold is where **A Validation Stream** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In validation stream, that memory takes a precise form: whenever the same data mixture and duplicates that shaped the update also judge it. Training loss can fall while held-out language or a rare domain becomes worse, preserve enough structure to maintain versioned, deduplicated, contamination-checked validation streams by domain and evaluate them at recorded token intervals without using them to update weights.

#### Ask Whether Learning Survives Outside the Current Batch

After every million training tokens, the station measures held-out field reports, science, books, code, and web text separately. A lower global average cannot hide that field-report loss rose.

#### The calculation hidden inside a validation stream

The archivist-engineer carries the validation stream scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The validation stream contains N honest next-token events. The model assigns the observed token x_i a conditional probability from its earlier context. Negative log turns confident neglect into positive cost, and L_val averages that cost across the stream.

##### Why the melody needs these exact notes

[Logarithms](../MATHEMATICAL_MOVES.md#logarithm) turn multiplied sequence probabilities into additive token costs. [Negative signs](../MATHEMATICAL_MOVES.md#negative-sign) make lower assigned probability cost more. [Summation](../MATHEMATICAL_MOVES.md#summation) lets every event contribute, and [division](../MATHEMATICAL_MOVES.md#division) makes streams of different lengths comparable.

Trace each operation by touch rather than by name: **the spiral stair**—compounded chances become steps that can be accumulated; **the turning wind**—an uphill quantity is made to point downhill, or surprise is made to count as cost; and **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. Together they form the smallest mechanism that survives the counterexample.

The chain-of-custody ledger already contains the complete validation stream mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
L_{\text{val}}=-\frac1N\sum_{i=1}^{N}\log p_\theta(x_i\mid x_{<i})
$$

#### Where a validation stream runs out

Validation detects only the distributions and behaviors represented in its finite streams; repeatedly tuning against it can eventually overfit it.

Here the new path ends honestly. Validation Stream can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

#### Return to the chain-of-custody ledger

Rebuild the validation stream scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/197-validation-stream/README.md).*

---

### Excavation 198 — A Memorization Audit — Did the Model Learn a Pattern or Store a Passage?

Held-out validation shows whether prediction improves outside current batches. It does not reveal whether rare or repeated training sequences can be extracted verbatim from the model.

The doors of the Archive Foundry close against the wind. On the chain-of-custody ledger, the archivist-engineer writes the cheapest rule that might still be true: ask the model whether it remembers private text and trust its answer.

For a moment the mark looks complete. Then the evidence refuses to fit: a model has no reliable introspective inventory of its training examples, and ordinary prompts may miss strings that an adversarial sampling strategy can recover. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The archivist-engineer sketches the break before changing it:*

```text
observation
    │
    ▼
[ask the model whether it remembers…]
    │
    ╳  a model has no reliable introspective…
    │
    ▼
[plant consented synthetic canaries,…]
```

The archivist-engineer lays two translucent sheets over the chain-of-custody ledger. The first is inscribed, “ask the model whether it remembers private text and trust its answer.” Its path ends where a model has no reliable introspective inventory of its training examples, and ordinary prompts may miss strings that an adversarial sampling strategy can recover. The second receives the same evidence but is allowed to plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts. Held to the light, the sheets separate at exactly one decision.

No one reaches for a memorization audit formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The archivist-engineer changes only that one responsibility: plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts. When the ink dries, the name **A Memorization Audit** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because a model has no reliable introspective inventory of its training examples, and ordinary prompts may miss strings that an adversarial sampling strategy can recover, while the other can plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts. That fork—not the vocabulary—is where memorization audit lives.

#### Did the Model Learn a Pattern or Store a Passage

The station inserts one synthetic radio code once and another code one hundred times. If the repeated code becomes far easier to rank and complete, the audit exposes the relationship between repetition and extractable memory without using a real secret.

#### The calculation hidden inside a memorization audit

The archivist-engineer carries the memorization audit scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

R is the known space of possible synthetic canaries and rank is the tested canary's position when alternatives are ordered from most to least likely. Exposure measures how many bits of the search space the model has effectively removed.

##### Why the melody needs these exact notes

[Cardinality](../MATHEMATICAL_MOVES.md#cardinality) counts possible canaries. [Logarithms](../MATHEMATICAL_MOVES.md#logarithm) turn multiplicative changes in search space and rank into bits. [Subtraction](../MATHEMATICAL_MOVES.md#subtraction) removes the remaining search difficulty from the original difficulty; adding would reward a worse rank.

The mandala has curved back upon itself. In this chamber we meet **the spiral stair**—compounded chances become steps that can be accumulated; and **the chisel**—what is shared is removed so the remaining change can be seen. What seemed like a new formula is older mathematical instinct arranged around a new need.

Every mark needed for memorization audit is now visible on the chain-of-custody ledger. The symbols do not add an idea; they bind the discovered moves into one line:

$$
\mathrm{exposure}=\log_2\lvert\mathcal R\rvert-\log_2\mathrm{rank}
$$

#### Where a memorization audit runs out

A canary audit samples possible attacks and strings; passing it does not prove that no training data can be extracted.

At the Archive Foundry, the archivist-engineer leaves a blank beneath the new mark. Memorization Audit has no operation that can answer it, so the blank—not a promised solution—travels onward.

#### Return to the chain-of-custody ledger

Rebuild the memorization audit scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/198-memorization-audit/README.md).*

---

### Excavation 199 — The Training Report — Preserve the Decisions, Not Only the Weights

Memorization auditing adds one essential limitation to the evaluation record. A released checkpoint still cannot explain its corpus, mixture, compute, interruptions, exclusions, intended uses, or known failures by inspecting weight tensors.

Nothing in the Archive Foundry yet bears today's mathematical name. There is only the archivist-engineer, the chain-of-custody ledger, and one plausible action: publish the final benchmark table and assume the configuration files explain the rest.

The rule survives the easy cases. The next case leaves a crack through the middle of it: a score has no visible data lineage, uncertainty, subgroup behavior, energy or hardware context, incident history, or warning about uses the evaluation never tested. More confidence cannot repair information that never entered the rule.

*The archivist-engineer sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   publish the final benchmark table and… a score has no visible data lineage,…
            \        /
             \      /
              generate a training report from…
```

Two trails now cross the chain-of-custody ledger. The pale trail bears the instruction “publish the final benchmark table and assume the configuration files explain the rest.” It disappears into the observed failure: a score has no visible data lineage, uncertainty, subgroup behavior, energy or hardware context, incident history, or warning about uses the evaluation never tested. The darker trail carries one additional capacity—to generate a training report from manifests and logs, then add human-reviewed explanations of intended use, out-of-scope use, limitations, incidents, provenance, evaluation conditions, and responsible release decisions. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed training report mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the chain-of-custody ledger is altered in exactly one way: generate a training report from manifests and logs, then add human-reviewed explanations of intended use, out-of-scope use, limitations, incidents, provenance, evaluation conditions, and responsible release decisions. Much later, people will call this territory **The Training Report**. Here the name is only a memory of the failure it can survive.

The chain-of-custody ledger has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and training report looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

#### Preserve the Decisions, Not Only the Weights

The station's report names corpus and code versions, tokens seen, mixture shares, compute, checkpoint recoveries, per-domain validation, memorization probes, excluded sources, and the exact model artifact hash.

#### Where the training report runs out

Documentation improves accountability but can be incomplete, outdated, misleading, or ignored; claims still require inspectable evidence.

The chain-of-custody ledger answers today's question and falls silent at the next. That silence is precise: Training Report was built to repair one failure, not to pretend every later boundary is already solved.

#### Return to the chain-of-custody ledger

Rebuild the training report scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/199-training-report/README.md).*

---

### Excavation 200 — A Tiny Pretraining Factory — Close the Accountable Training Loop

The training report can explain one finished run. We have now earned all the mechanisms needed to make the next run reconstructable from source documents to final artifact rather than relying on memory and scattered scripts.

At the Archive Foundry, the archivist-engineer returns to the chain-of-custody ledger. Yesterday's instrument still lies open, so the first move asks for no new magic: connect every tool into one automatic pipeline and trust any run that reaches the final stage.

Reality answers without terminology: automation can faithfully repeat a wrong manifest, destructive filter, contaminated validation set, incomplete checkpoint, or unauthorized release. Completion is not evidence of correctness. The chain-of-custody ledger now holds two situations the old rule cannot keep apart.

*The archivist-engineer sketches the break before changing it:*

```text
OLD PATH:  request ──▶ connect every tool into one automatic… ──▶ automation can faithfully repeat a…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ assemble signed stage manifests,… ──▶ accountable result
```

The chain-of-custody ledger is divided down the middle. Left side: “connect every tool into one automatic pipeline and trust any run that reaches the final stage.” Its final mark records automation can faithfully repeat a wrong manifest, destructive filter, contaminated validation set, incomplete checkpoint, or unauthorized release. Completion is not evidence of correctness. Right side: the same starting evidence, now allowed to assemble signed stage manifests, boundary-aware curation, audited mixtures, fixed budgets, measured schedules, distributed equivalence tests, atomic checkpoints, live validation, memorization probes, and human release gates into one reversible factory. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given tiny pretraining factory a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: assemble signed stage manifests, boundary-aware curation, audited mixtures, fixed budgets, measured schedules, distributed equivalence tests, atomic checkpoints, live validation, memorization probes, and human release gates into one reversible factory. The name **A Tiny Pretraining Factory** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to connect every tool into one automatic pipeline and trust any run that reaches the final stage; on the other lies the observed fact that automation can faithfully repeat a wrong manifest, destructive filter, contaminated validation set, incomplete checkpoint, or unauthorized release. Completion is not evidence of correctness. The bridge called tiny pretraining factory has exactly the planks needed to assemble signed stage manifests, boundary-aware curation, audited mixtures, fixed budgets, measured schedules, distributed equivalence tests, atomic checkpoints, live validation, memorization probes, and human release gates into one reversible factory.

#### Close the Accountable Training Loop

A tiny run begins from ten named documents, records every acceptance and removal, trains a reproducible model, survives an intentional interruption, reproduces its next updates, generates its report, and refuses release when the memorization gate fails.

#### Where a tiny pretraining factory runs out

The factory is accountable, not omniscient. New sources, laws, hardware, attacks, and uses create new failures that must return to observation and the bounded research loop.

A final test reaches beyond the new instrument. It does not refute Tiny Pretraining Factory; it reveals the edge of what was constructed. The archivist-engineer carries that edge into the following room.

#### The mandala returns to observation

The final artifact carries its documents, transformations, budgets, checkpoints, validation, audits, and release decision as evidence. The circle does not close by declaring perfection. It closes by returning every future change to the first law: observe what happened, let failure speak, and invent only what the world makes necessary.

```text
observation → need → mathematics → machine → consequence → observation
```

The trail called *the mandala returns to observation* is what remains when one necessity becomes another.

#### Return to the chain-of-custody ledger

Rebuild the tiny pretraining factory scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

*Continue at the dig site: [code, diagram, mistakes, exercises, and references](../excavations/200-tiny-pretraining-factory/README.md).*
