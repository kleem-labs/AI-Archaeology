# Excavation 178 — Language Identification — Do Not Confuse Familiar Script with Familiar Language

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

## Do Not Confuse Familiar Script with Familiar Language

A field report receives English 0.93, Spanish 0.05, and unknown 0.02. The pipeline keeps English only because its score clears the recorded threshold; a 0.44/0.41 split is quarantined.

Hold the setting, evidence, and desired outcome fixed while testing language identification. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

## The calculation hidden inside language identification

Do not read the coming Language Identification line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

d is the document being inspected; the set L contains allowed language labels; p(l|d) is the classifier's support for one label; l-star is the label whose support is largest.

### Why no cheaper operation does the same job

[Conditional probability](../../MATHEMATICAL_MOVES.md#conditional-bar) asks for language support given this document. [Arg max](../../MATHEMATICAL_MOVES.md#arg-max) keeps the winning label rather than only its score. Summing the scores would erase which language produced them; a threshold is still checked afterward because the winner may be weak.

Every symbol in Language Identification can now be read back into an action already performed. The whole procedure fits in one line:

$$
\ell^*=\underset{\ell\in\mathcal L}{\mathrm{argmax}}\ p(\ell\mid d)
$$

## Where language identification runs out

Because the classifier learned from finite examples and reduces a mixed document to one distribution, language identification remains probabilistic and domain-sensitive; short, multilingual, and code-heavy documents are especially difficult.

This is where language identification runs out for a causal reason. We gave it enough structure to use a calibrated language classifier, retain its confidence and model version, and route uncertain documents to an explicit unknown bucket rather than forcing a label, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

## Take language identification to the workbench

A mathematical story about language identification earns trust only when the failed and repaired paths can both be reproduced. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running language identification, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the language identification result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Exact Deduplication — Stop Paying Twice for the Same Document](../179-exact-deduplication/README.md)
