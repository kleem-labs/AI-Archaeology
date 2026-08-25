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

At the Archive Foundry, the archivist-engineer meets the next case beside the chain-of-custody ledger. The nearest idea is also the most reasonable one: copy every available text file into one large folder and begin tokenizing.

The attraction of this attempt is easy to see. To copy every available text file into one large folder and begin tokenizing reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: a file is replaced upstream, another is silently skipped, and a third appears twice under different paths. The same training command now describes a different body of evidence.

The contradiction matters because it identifies a structural loss in the instruction to copy every available text file into one large folder and begin tokenizing, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The chain-of-custody ledger will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must create an immutable manifest that records each source, version, content hash, license or usage basis, processing stage, and document count before any training shard exists. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **A Corpus Manifest**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

#### Know What Entered the Run

The ranger station records `field-reports/v3`, its retrieval date, 8,412 documents, and the hash of its manifest. A later run can prove whether it used the same evidence.

#### Where a corpus manifest runs out

A manifest makes the corpus accountable; it cannot prove that every recorded document is suitable, lawful, accurate, or harmless.

A final test reaches beyond the new instrument. It does not refute Corpus Manifest; it reveals the edge of what was constructed. The archivist-engineer carries that edge into the following room.

---

### Excavation 177 — Document Boundaries — Keep One Story from Leaking into Another

The manifest fixes which source documents belong to the run. Tokenization can still concatenate them into a stream where the ending of one document predicts the beginning of an unrelated one.

The previous discovery reaches the Archive Foundry carrying one unfinished problem. Beside the chain-of-custody ledger, the archivist-engineer first tries to join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width.

There is good reason to begin this way. If we join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: a ranger report ending with “tiger tracks near” is trained to predict the first word of an unrelated software license. The model receives a relationship that never existed in either document.

This failure cannot be repaired by performing the instruction to join every token sequence end to end and cut fixed-length training windows wherever the counter reaches the context width more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the chain-of-custody ledger; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to mark document ends, reset position where the design requires it, and block attention or loss across boundaries unless cross-document packing is explicitly intended. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Document Boundaries**. The name is simply a handle for the distinction already reconstructed.

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

---

### Excavation 178 — Language Identification — Do Not Confuse Familiar Script with Familiar Language

Document boundaries now preserve honest local context. The manifest still mixes languages, code, names, and corrupted text, so a declared English run cannot yet tell what language evidence it actually contains.

A new case arrives at the Archive Foundry. Nothing yet demands a new invention, so the archivist-engineer uses the chain-of-custody ledger to keep documents containing mostly familiar Latin characters and discard the rest.

This is precisely the kind of shortcut a careful builder should try first. The instruction to keep documents containing mostly familiar Latin characters and discard the rest preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: spanish and Vietnamese are mistaken for English, transliterated languages disappear, and English code or identifier lists pass despite containing little natural language.

The counterexample separates two questions that the attempt to keep documents containing mostly familiar Latin characters and discard the rest had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the chain-of-custody ledger fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now use a calibrated language classifier, retain its confidence and model version, and route uncertain documents to an explicit unknown bucket rather than forcing a label. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Language Identification**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

#### Do Not Confuse Familiar Script with Familiar Language

A field report receives English 0.93, Spanish 0.05, and unknown 0.02. The pipeline keeps English only because its score clears the recorded threshold; a 0.44/0.41 split is quarantined.

#### The calculation hidden inside language identification

The archivist-engineer carries the language identification scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

d is the document being inspected; the set L contains allowed language labels; p(l|d) is the classifier's support for one label; l-star is the label whose support is largest.

##### Why the melody needs these exact notes

[Conditional probability](../MATHEMATICAL_MOVES.md#conditional-bar) asks for language support given this document. [Arg max](../MATHEMATICAL_MOVES.md#arg-max) keeps the winning label rather than only its score. Summing the scores would erase which language produced them; a threshold is still checked afterward because the winner may be weak.

Every mark in the coming language identification equation now belongs to a visible part of the case. The compressed form is:

$$
\ell^*=\underset{\ell\in\mathcal L}{\mathrm{argmax}}\ p(\ell\mid d)
$$

#### Where language identification runs out

Because the classifier learned from finite examples and reduces a mixed document to one distribution, language identification remains probabilistic and domain-sensitive; short, multilingual, and code-heavy documents are especially difficult.

The language identification repair holds, but the world asks for something it was never given. At the Archive Foundry, that unmet need is preserved rather than hidden behind a stronger claim.

---

### Excavation 179 — Exact Deduplication — Stop Paying Twice for the Same Document

Language labels make the intended corpus measurable. Counting the accepted files now reveals identical reports mirrored across archives and repeated under new filenames.

Inside the Archive Foundry, the old method is given an honest chance. The archivist-engineer places the evidence on the chain-of-custody ledger and tries to leave duplicates in place because more training examples should always help.

Nothing about this first move is careless. To leave duplicates in place because more training examples should always help is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: one press release copied to a thousand sites receives a thousand votes, while a rare field observation receives one. Compute is spent memorizing repetition rather than encountering new evidence.

The important discovery is not merely that trying to leave duplicates in place because more training examples should always help failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the chain-of-custody ledger, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to normalize only irrelevant formatting, hash the resulting document, and keep one accountable representative for each identical hash while preserving duplicate counts in the ledger. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Exact Deduplication**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

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

---

### Excavation 180 — Near Deduplication — When a Copy Changes a Few Words

Exact deduplication removes byte-equivalent documents. The copied article with a new banner, reordered footer, or one edited sentence still survives as apparently new evidence.

At the Archive Foundry, the archivist-engineer meets the next case beside the chain-of-custody ledger. The nearest idea is also the most reasonable one: lowercase both documents and demand that every remaining word match.

The attraction of this attempt is easy to see. To lowercase both documents and demand that every remaining word match reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: one inserted advertisement defeats the rule, while independently written short notices can match by accident. Exact sequence equality is too brittle for disguised copies.

The contradiction matters because it identifies a structural loss in the instruction to lowercase both documents and demand that every remaining word match, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The chain-of-custody ledger will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must represent each document by overlapping shingles, compare the shared fraction with Jaccard similarity, and use MinHash-style candidate retrieval before exact verification at scale. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Near Deduplication**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

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

---

### Excavation 181 — Quality Filtering — Remove Noise Without Defining Humanity Away

Near-deduplication leaves a corpus with more distinct documents, not necessarily better ones. Some are navigation fragments, keyword piles, machine corruption, or adversarial spam.

The previous discovery reaches the Archive Foundry carrying one unfinished problem. Beside the chain-of-custody ledger, the archivist-engineer first tries to keep only documents that resemble one prestigious encyclopedia.

There is good reason to begin this way. If we keep only documents that resemble one prestigious encyclopedia, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: the filter removes spam, but it also suppresses informal dialect, local knowledge, code, dialogue, and communities whose writing differs from the chosen reference.

This failure cannot be repaired by performing the instruction to keep only documents that resemble one prestigious encyclopedia more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the chain-of-custody ledger; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to combine transparent structural signals with small controlled model-based tests, inspect what each threshold removes, and publish source-by-source retention counts before accepting a filter. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Quality Filtering**. The name is simply a handle for the distinction already reconstructed.

#### Remove Noise Without Defining Humanity Away

The station rejects a page with 70 percent repeated navigation and no sentences, but manually audits samples near the threshold and notices that short emergency bulletins need a different rule from essays.

#### Where quality filtering runs out

Every quality filter encodes values and domain assumptions; measured downstream gains do not prove that excluded voices were unimportant.

The chain-of-custody ledger answers today's question and falls silent at the next. That silence is precise: Quality Filtering was built to repair one failure, not to pretend every later boundary is already solved.

---

### Excavation 182 — Data Provenance — Keep the Path Back to Every Source

Quality filtering produces an accepted set and a rejected set. Without a trace through each transformation, neither set can explain how a source document reached its decision.

A new case arrives at the Archive Foundry. Nothing yet demands a new invention, so the archivist-engineer uses the chain-of-custody ledger to save only the final cleaned text because intermediate metadata costs storage.

This is precisely the kind of shortcut a careful builder should try first. The instruction to save only the final cleaned text because intermediate metadata costs storage preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: a rights request, filtering bug, or benchmark contamination report arrives, but the final shard cannot be mapped back to the source record or processing rule that produced it.

The counterexample separates two questions that the attempt to save only the final cleaned text because intermediate metadata costs storage had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the chain-of-custody ledger fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Data Provenance**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

#### Keep the Path Back to Every Source

Document `river-0042` points to its source URL, retrieval time, raw hash, language decision, duplicate cluster, quality audit, redaction record, and final shard offset.

#### Where data provenance runs out

Provenance makes decisions inspectable; it cannot repair a source that was collected without sufficient rights, consent, or context.

A final test reaches beyond the new instrument. It does not refute Data Provenance; it reveals the edge of what was constructed. The archivist-engineer carries that edge into the following room.

---

### Excavation 183 — PII Redaction — Do Not Turn Accidental Secrets into Lessons

Provenance can locate every retained document. Inspection now finds phone numbers, email addresses, account identifiers, and private-looking text embedded in otherwise useful pages.

Inside the Archive Foundry, the old method is given an honest chance. The archivist-engineer places the evidence on the chain-of-custody ledger and tries to remove any entire document containing a sequence that resembles personal information.

Nothing about this first move is careless. To remove any entire document containing a sequence that resembles personal information is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: one phone number erases a long public safety guide, while obfuscated addresses and context-dependent identifiers still pass. The rule destroys useful evidence without reliably removing the risky span.

The important discovery is not merely that trying to remove any entire document containing a sequence that resembles personal information failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the chain-of-custody ledger, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to detect candidate spans with several methods, classify them in context, replace confirmed sensitive spans with typed placeholders, and preserve only a restricted audit record of the decision. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **PII Redaction**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

#### Do Not Turn Accidental Secrets into Lessons

The sentence “Call Maya at 555-0142 about the injured tiger” becomes “Call [PERSON] at [PHONE] about the injured tiger”; the grammatical lesson survives while the direct identifier does not.

#### Where pii redaction runs out

Redaction has false positives and false negatives, and public availability does not by itself settle privacy, consent, or appropriate use.

One unsolved mark remains on the chain-of-custody ledger. None of the responsibilities inside PII Redaction can move it, and so it becomes the observation from which the next excavation must begin.

---

### Excavation 184 — Data Mixtures — Decide Which Worlds Receive a Voice

Redaction reduces one preventable privacy risk. The clean sources still differ enormously in size: web pages could drown out books, code, science, and the station's rare field reports.

At the Archive Foundry, the archivist-engineer meets the next case beside the chain-of-custody ledger. The nearest idea is also the most reasonable one: concatenate every accepted source and let its raw token count determine how often it appears.

The attraction of this attempt is easy to see. To concatenate every accepted source and let its raw token count determine how often it appears reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: the largest crawl silently becomes the curriculum. A source ten thousand times smaller may almost never reach a batch even when it carries relationships absent from the web.

The contradiction matters because it identifies a structural loss in the instruction to concatenate every accepted source and let its raw token count determine how often it appears, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The chain-of-custody ledger will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must choose and publish a probability weight for each domain, treating the mixture as an explicit modeling decision that must be tested on per-domain validation streams. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Data Mixtures**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

#### Decide Which Worlds Receive a Voice

The station assigns 0.50 to curated web text, 0.20 to science, 0.15 to code, 0.10 to books, and 0.05 to field reports. The five shares exhaust one draw without pretending the sources are equally large or equally important.

#### The calculation hidden inside data mixtures

The archivist-engineer carries the data mixtures scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

D counts the named data domains and w_d is the chance that the next training draw chooses domain d. Nonnegative weights prevent negative sampling; a total of one exhausts all possible domain choices.

##### Why the melody needs these exact notes

[Summation](../MATHEMATICAL_MOVES.md#summation) combines mutually exclusive domain shares into the whole probability mass. Multiplication would make one zero-weight domain erase the mixture. [Equality](../MATHEMATICAL_MOVES.md#equals) requires a complete distribution, while the [inequality](../MATHEMATICAL_MOVES.md#inequalities) forbids impossible negative shares.

Listen beneath data mixtures: **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Every mark in the coming data mixtures equation now belongs to a visible part of the case. The compressed form is:

$$
\sum_{d=1}^{D}w_d=1,\quad w_d\ge 0
$$

#### Where data mixtures runs out

Mixture weights redistribute attention but cannot make a poor or missing domain representative, accurate, or safe.

The data mixtures repair holds, but the world asks for something it was never given. At the Archive Foundry, that unmet need is preserved rather than hidden behind a stronger claim.

---

### Excavation 185 — Mixture Sampling — Turn Planned Shares into a Reproducible Stream

The mixture weights state which domains should be heard. They do not yet produce a finite ordered token stream that every resumed worker can reconstruct.

The previous discovery reaches the Archive Foundry carrying one unfinished problem. Beside the chain-of-custody ledger, the archivist-engineer first tries to round each domain's desired share independently and concatenate the resulting blocks.

There is good reason to begin this way. If we round each domain's desired share independently and concatenate the resulting blocks, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero.

This failure cannot be repaired by performing the instruction to round each domain's desired share independently and concatenate the resulting blocks more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the chain-of-custody ledger; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Mixture Sampling**. The name is simply a handle for the distinction already reconstructed.

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

---

### Excavation 186 — The Token Budget — Convert a Training Plan into a Count of Lessons

Seeded mixture sampling can produce an ordered stream. The run still says “train for a while,” so neither cost nor source exposure is bounded.

A new case arrives at the Archive Foundry. Nothing yet demands a new invention, so the archivist-engineer uses the chain-of-custody ledger to stop when the wall clock reaches an affordable date.

This is precisely the kind of shortcut a careful builder should try first. The instruction to stop when the wall clock reaches an affordable date preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: faster hardware sees more tokens, interruptions see fewer, and two runs with the same calendar budget teach different amounts of evidence.

The counterexample separates two questions that the attempt to stop when the wall clock reaches an affordable date had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the chain-of-custody ledger fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **The Token Budget**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

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

---

### Excavation 187 — Compute-Optimal Allocation — Buy a Larger Memory or More Experience?

The token budget fixes how much evidence the model will see. A fixed compute allowance still permits a wider model trained on fewer tokens or a smaller model trained on more.

Inside the Archive Foundry, the old method is given an honest chance. The archivist-engineer places the evidence on the chain-of-custody ledger and tries to spend nearly the entire budget on parameter count because a larger model can store more patterns.

Nothing about this first move is careless. To spend nearly the entire budget on parameter count because a larger model can store more patterns is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: the large model is stopped after too little experience and remains undertrained, while much of its expensive capacity never receives enough varied evidence.

The important discovery is not merely that trying to spend nearly the entire budget on parameter count because a larger model can store more patterns failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the chain-of-custody ledger, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to estimate candidate parameter-and-token pairs under the same compute budget, run smaller scaling experiments, and choose the pair predicted to minimize held-out loss rather than maximizing either axis alone. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Compute-Optimal Allocation**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

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

---

### Excavation 188 — Learning-Rate Warmup — Let Adam Learn the Terrain Before Running

Compute allocation chooses the model and token horizon. At the first update, Adam's moment memories contain almost no history, while randomly initialized activations and gradients are changing fastest.

At the Archive Foundry, the archivist-engineer meets the next case beside the chain-of-custody ledger. The nearest idea is also the most reasonable one: begin immediately at the peak learning rate chosen for the stable middle of training.

The attraction of this attempt is easy to see. To begin immediately at the peak learning rate chosen for the stable middle of training reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: the first noisy batches can make large updates before the optimizer's scale estimates become trustworthy, producing a loss spike that the later stable rate would not have caused.

The contradiction matters because it identifies a structural loss in the instruction to begin immediately at the peak learning rate chosen for the stable middle of training, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The chain-of-custody ledger will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Learning-Rate Warmup**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

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

---

### Excavation 189 — Cosine Decay — Make Late Corrections Smaller Without a Cliff

Warmup protects the optimizer's first steps. Keeping the peak rate for the entire token budget makes late updates as aggressive as early ones even when the model is refining rather than discovering broad structure.

The previous discovery reaches the Archive Foundry carrying one unfinished problem. Beside the chain-of-custody ledger, the archivist-engineer first tries to drop the rate abruptly near the end of training.

There is good reason to begin this way. If we drop the rate abruptly near the end of training, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: a sudden cliff changes update scale in one step and makes the chosen drop date an arbitrary discontinuity; dropping too early freezes useful learning.

This failure cannot be repaired by performing the instruction to drop the rate abruptly near the end of training more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the chain-of-custody ledger; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to decay smoothly from the peak toward a chosen minimum over the remaining horizon, while recording the schedule as part of the resumable state. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Cosine Decay**. The name is simply a handle for the distinction already reconstructed.

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

---

### Excavation 190 — Gradient Noise Scale — When More Examples Stop Buying More Direction

The schedule controls how far one global update moves. We still do not know how many examples should vote in that update before extra devices mostly repeat the same directional evidence.

A new case arrives at the Archive Foundry. Nothing yet demands a new invention, so the archivist-engineer uses the chain-of-custody ledger to make the global batch as large as the cluster permits.

This is precisely the kind of shortcut a careful builder should try first. The instruction to make the global batch as large as the cluster permits preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: early doubling reduces disagreement and improves the direction, but beyond a workload-dependent point the averaged gradient barely changes while each update consumes twice as many tokens.

The counterexample separates two questions that the attempt to make the global batch as large as the cluster permits had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the chain-of-custody ledger fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now measure disagreement among micro-batch gradients relative to the strength of their shared direction, and use that noise scale as evidence for the largest useful batch rather than a hardware target. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Gradient Noise Scale**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

#### When More Examples Stop Buying More Direction

Three named micro-batches question the same two weights: the field reports propose [2.0,1.0], science proposes [2.1,0.9], and books propose [1.9,1.1]. The first number is advice to the tiger-before-river weight; the second is advice to a punctuation weight. Their mean [2.0,1.0] is strong and their disagreement around it is small. If the witnesses instead propose [4,−2], [0,4], and [2,1], disagreement is large relative to the same broad direction, so a larger batch can still buy useful certainty.

#### The calculation hidden inside gradient noise scale

The archivist-engineer carries the gradient noise scale scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Each g_i is one model micro-batch's gradient advice. The covariance measures how those witnesses disagree; its trace totals disagreement across coordinates. The squared norm of their mean measures the strength of the shared direction; G compares noise with signal.

##### Why the melody needs these exact notes

[Covariance](../MATHEMATICAL_MOVES.md#covariance) keeps variation around the common advice rather than raw gradient size. [Trace](../MATHEMATICAL_MOVES.md#trace) gathers coordinate variances without inventing cross-coordinate units. [Division](../MATHEMATICAL_MOVES.md#division) asks disagreement per unit of squared shared direction; subtraction would not remove dependence on signal scale.

The mandala has curved back upon itself. In this chamber we meet **the paired dance**—two quantities reveal whether their departures move together; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. What seemed like a new formula is older mathematical instinct arranged around a new need.

Every mark in the coming gradient noise scale equation now belongs to a visible part of the case. The compressed form is:

$$
G=\frac{\mathrm{tr}(\mathrm{Cov}[g_i])}{\lVert E[g_i]\rVert^2}
$$

#### Where gradient noise scale runs out

Gradient noise scale is an empirical guide, not a universal batch-size law; it changes during training and with the task and optimizer.

The gradient noise scale repair holds, but the world asks for something it was never given. At the Archive Foundry, that unmet need is preserved rather than hidden behind a stronger claim.

---

### Excavation 191 — Data Parallelism — Let Several Workers Observe Different Evidence

Gradient noise measurements choose a useful global batch. One device cannot process that batch quickly enough, even though the modern model and optimizer state now fit through sharding.

Inside the Archive Foundry, the old method is given an honest chance. The archivist-engineer places the evidence on the chain-of-custody ledger and tries to send the same mini-batch to every worker and average their gradients.

Nothing about this first move is careless. To send the same mini-batch to every worker and average their gradients is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: all workers repeat the same computation and return the same evidence, so hardware cost rises without increasing batch diversity or reducing step time meaningfully.

The important discovery is not merely that trying to send the same mini-batch to every worker and average their gradients failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the chain-of-custody ledger, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Data Parallelism**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

#### Let Several Workers Observe Different Evidence

Four workers each read eight different sequences. Their four average gradients become one average over thirty-two sequences before any worker advances the parameters.

#### The calculation hidden inside data parallelism

The archivist-engineer carries the data parallelism scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

P is the number of data-parallel workers, g_p is worker p's average gradient from different examples, and g is the single gradient used by the shared optimizer step.

##### Why the melody needs these exact notes

[Summation](../MATHEMATICAL_MOVES.md#summation) lets every worker's independent evidence contribute. [Division](../MATHEMATICAL_MOVES.md#division) returns advice per worker so adding hardware does not enlarge the update by itself. Multiplication would let a zero coordinate from one worker erase all others.

The calculation reuses familiar motions: **the chorus**—many witnesses contribute to one answer without one silence erasing the rest; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. Together they keep the path from the concrete case to notation intact.

The chain-of-custody ledger already contains the complete data parallelism mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
g=\frac1P\sum_{p=1}^{P}g_p
$$

#### Where data parallelism runs out

Because one shared update cannot proceed until every worker's evidence has joined the average, synchronous data parallelism waits for the slowest worker and communicates a full update's worth of gradient information.

Here the new path ends honestly. Data Parallelism can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

---

### Excavation 192 — Pipeline Parallelism — Stop Waiting for the Whole Model to Cross One Device at a Time

Data parallel workers process different examples, but each replica still needs the model's sequential layers. Splitting those layers across devices makes only one device active if a whole batch traverses the stages at once.

At the Archive Foundry, the archivist-engineer meets the next case beside the chain-of-custody ledger. The nearest idea is also the most reasonable one: send one complete batch through stage one, then stage two, then stage three.

The attraction of this attempt is easy to see. To send one complete batch through stage one, then stage two, then stage three reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: while stage two works, stage one and stage three wait. The model fits, but most devices are idle for most of the step.

The contradiction matters because it identifies a structural loss in the instruction to send one complete batch through stage one, then stage two, then stage three, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The chain-of-custody ledger will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Pipeline Parallelism**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

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

---

### Excavation 193 — Three-Dimensional Parallelism — Give Each Memory Wall Its Own Axis

Pipeline micro-batches keep layer stages busy. A large run may still exceed memory inside one layer, require more independent data witnesses, and contain too many layers for one device group.

The previous discovery reaches the Archive Foundry carrying one unfinished problem. Beside the chain-of-custody ledger, the archivist-engineer first tries to increase whichever parallel technique was introduced most recently until the model fits.

There is good reason to begin this way. If we increase whichever parallel technique was introduced most recently until the model fits, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: more pipeline stages increase bubbles, more tensor splits increase frequent communication, and more data replicas preserve full model memory. One axis cannot solve three different limits efficiently.

This failure cannot be repaired by performing the instruction to increase whichever parallel technique was introduced most recently until the model fits more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the chain-of-custody ledger; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Three-Dimensional Parallelism**. The name is simply a handle for the distinction already reconstructed.

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

---

### Excavation 194 — Sharded Checkpoints — Save One Recoverable State Without Gathering It

Three-dimensional parallelism spreads parameters, moments, gradients, and progress across many owners. Asking one coordinator to gather everything before saving can exceed its memory and stall the cluster.

A new case arrives at the Archive Foundry. Nothing yet demands a new invention, so the archivist-engineer uses the chain-of-custody ledger to let every worker write its local tensors and call the directory a checkpoint.

This is precisely the kind of shortcut a careful builder should try first. The instruction to let every worker write its local tensors and call the directory a checkpoint preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: a worker fails before writing, two shards belong to different steps, or a filename is reused. The directory exists but cannot reconstruct one globally consistent training state.

The counterexample separates two questions that the attempt to let every worker write its local tensors and call the directory a checkpoint had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the chain-of-custody ledger fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now write versioned shards to temporary locations, record hashes and ownership in a checkpoint manifest, and publish one atomic completion marker only after every required shard is durable. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Sharded Checkpoints**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

#### Save One Recoverable State Without Gathering It

Twenty-four workers save step 8,000. The manifest expects twenty-four parameter shards, optimizer shards, scheduler state, RNG state, and data cursors; the checkpoint becomes eligible for recovery only when every recorded hash verifies.

#### Where sharded checkpoints runs out

A complete checkpoint limits lost work but consumes storage and I/O bandwidth; frequent synchronous saves can dominate training time.

A final test reaches beyond the new instrument. It does not refute Sharded Checkpoints; it reveals the edge of what was constructed. The archivist-engineer carries that edge into the following room.

---

### Excavation 195 — Deterministic Resume — Continue the Same Experiment, Not a Similar One

The sharded checkpoint can reconstruct every distributed tensor. If it omits the sampler cursor, random-number generators, scheduler phase, or overflow state, restart follows a different future.

Inside the Archive Foundry, the old method is given an honest chance. The archivist-engineer places the evidence on the chain-of-custody ledger and tries to restore model weights and let every other component start fresh.

Nothing about this first move is careless. To restore model weights and let every other component start fresh is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: adam forgets its moments, warmup may begin again, dropout chooses different masks, and data workers repeat or skip documents. The loss curve after restart cannot be attributed to the original run.

The important discovery is not merely that trying to restore model weights and let every other component start fresh failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the chain-of-custody ledger, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Deterministic Resume**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

#### Continue the Same Experiment, Not a Similar One

The station stops after update 200, restores weights, Adam moments, schedule position, scaler, RNG streams, and each data cursor, then reproduces updates 201 through 205 byte for byte on the reference implementation.

#### Where deterministic resume runs out

Exact replay can still fail across nondeterministic kernels, changed hardware, libraries, or distributed timing; the required reproducibility level must be stated.

One unsolved mark remains on the chain-of-custody ledger. None of the responsibilities inside Deterministic Resume can move it, and so it becomes the observation from which the next excavation must begin.

---

### Excavation 196 — Loss Spikes — Distinguish One Hard Batch from a Run Leaving the Road

Deterministic resume makes failures reproducible. During a long run, the observed loss sometimes jumps; automatically rewinding every jump wastes compute, while ignoring a sustained instability can destroy the model.

At the Archive Foundry, the archivist-engineer meets the next case beside the chain-of-custody ledger. The nearest idea is also the most reasonable one: declare any loss larger than the previous loss a failure and restore immediately.

The attraction of this attempt is easy to see. To declare any loss larger than the previous loss a failure and restore immediately reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: ordinary batches vary, so healthy learning triggers constant rollbacks. A slow divergence can rise without one dramatic step and escape the rule.

The contradiction matters because it identifies a structural loss in the instruction to declare any loss larger than the previous loss a failure and restore immediately, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The chain-of-custody ledger will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Loss Spikes**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

#### Distinguish One Hard Batch from a Run Leaving the Road

Recent clean validation losses center near 2.0 with spread 0.1. One batch reaches 2.35 and then returns; another run stays above 2.5 while gradient norm grows. Only the persistent, corroborated event triggers recovery.

#### The calculation hidden inside loss spikes

The archivist-engineer carries the loss spikes scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

L_t is the current monitored model loss, mu_t is its robust recent center, sigma_t is ordinary recent spread, and z_t says how many usual spreads the current value lies above or below that center.

##### Why the melody needs these exact notes

[Subtraction](../MATHEMATICAL_MOVES.md#subtraction) removes the local baseline. [Division](../MATHEMATICAL_MOVES.md#division) expresses the remainder in units of ordinary variation, making different loss scales comparable. A raw threshold would behave differently as normal loss falls during training.

Inside loss spikes, familiar operations return with stricter duties: **the chisel**—what is shared is removed so the remaining change can be seen; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Every mark in the coming loss spikes equation now belongs to a visible part of the case. The compressed form is:

$$
z_t=\frac{L_t-\mu_t}{\sigma_t}
$$

#### Where loss spikes runs out

Thresholds detect symptoms, not causes; corrupt data, overflow, optimizer settings, hardware faults, and architectural instability require different repairs.

The loss spikes repair holds, but the world asks for something it was never given. At the Archive Foundry, that unmet need is preserved rather than hidden behind a stronger claim.

---

### Excavation 197 — A Validation Stream — Ask Whether Learning Survives Outside the Current Batch

Loss-spike monitoring protects the training process from obvious instability. A smooth training curve can still improve mainly on repeated or overrepresented training domains.

The previous discovery reaches the Archive Foundry carrying one unfinished problem. Beside the chain-of-custody ledger, the archivist-engineer first tries to evaluate only the next training batch because it is already available.

There is good reason to begin this way. If we evaluate only the next training batch because it is already available, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: the same data mixture and duplicates that shaped the update also judge it. Training loss can fall while held-out language or a rare domain becomes worse.

This failure cannot be repaired by performing the instruction to evaluate only the next training batch because it is already available more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the chain-of-custody ledger; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to maintain versioned, deduplicated, contamination-checked validation streams by domain and evaluate them at recorded token intervals without using them to update weights. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **A Validation Stream**. The name is simply a handle for the distinction already reconstructed.

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

---

### Excavation 198 — A Memorization Audit — Did the Model Learn a Pattern or Store a Passage?

Held-out validation shows whether prediction improves outside current batches. It does not reveal whether rare or repeated training sequences can be extracted verbatim from the model.

A new case arrives at the Archive Foundry. Nothing yet demands a new invention, so the archivist-engineer uses the chain-of-custody ledger to ask the model whether it remembers private text and trust its answer.

This is precisely the kind of shortcut a careful builder should try first. The instruction to ask the model whether it remembers private text and trust its answer preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: a model has no reliable introspective inventory of its training examples, and ordinary prompts may miss strings that an adversarial sampling strategy can recover.

The counterexample separates two questions that the attempt to ask the model whether it remembers private text and trust its answer had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the chain-of-custody ledger fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now plant consented synthetic canaries, measure their rank among alternatives, test extraction procedures on authorized data, and connect failures back through provenance and duplicate counts. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **A Memorization Audit**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

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

---

### Excavation 199 — The Training Report — Preserve the Decisions, Not Only the Weights

Memorization auditing adds one essential limitation to the evaluation record. A released checkpoint still cannot explain its corpus, mixture, compute, interruptions, exclusions, intended uses, or known failures by inspecting weight tensors.

Inside the Archive Foundry, the old method is given an honest chance. The archivist-engineer places the evidence on the chain-of-custody ledger and tries to publish the final benchmark table and assume the configuration files explain the rest.

Nothing about this first move is careless. To publish the final benchmark table and assume the configuration files explain the rest is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: a score has no visible data lineage, uncertainty, subgroup behavior, energy or hardware context, incident history, or warning about uses the evaluation never tested.

The important discovery is not merely that trying to publish the final benchmark table and assume the configuration files explain the rest failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the chain-of-custody ledger, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to generate a training report from manifests and logs, then add human-reviewed explanations of intended use, out-of-scope use, limitations, incidents, provenance, evaluation conditions, and responsible release decisions. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **The Training Report**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

#### Preserve the Decisions, Not Only the Weights

The station's report names corpus and code versions, tokens seen, mixture shares, compute, checkpoint recoveries, per-domain validation, memorization probes, excluded sources, and the exact model artifact hash.

#### Where the training report runs out

Documentation improves accountability but can be incomplete, outdated, misleading, or ignored; claims still require inspectable evidence.

The chain-of-custody ledger answers today's question and falls silent at the next. That silence is precise: Training Report was built to repair one failure, not to pretend every later boundary is already solved.

---

### Excavation 200 — A Tiny Pretraining Factory — Close the Accountable Training Loop

The training report can explain one finished run. We have now earned all the mechanisms needed to make the next run reconstructable from source documents to final artifact rather than relying on memory and scattered scripts.

At the Archive Foundry, the archivist-engineer meets the next case beside the chain-of-custody ledger. The nearest idea is also the most reasonable one: connect every tool into one automatic pipeline and trust any run that reaches the final stage.

The attraction of this attempt is easy to see. To connect every tool into one automatic pipeline and trust any run that reaches the final stage reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: automation can faithfully repeat a wrong manifest, destructive filter, contaminated validation set, incomplete checkpoint, or unauthorized release. Completion is not evidence of correctness.

The contradiction matters because it identifies a structural loss in the instruction to connect every tool into one automatic pipeline and trust any run that reaches the final stage, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The chain-of-custody ledger will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must assemble signed stage manifests, boundary-aware curation, audited mixtures, fixed budgets, measured schedules, distributed equivalence tests, atomic checkpoints, live validation, memorization probes, and human release gates into one reversible factory. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **A Tiny Pretraining Factory**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

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
