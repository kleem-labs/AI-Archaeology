# Excavation 178 — Language Identification — Do Not Confuse Familiar Script with Familiar Language

Document boundaries now preserve honest local context. The manifest still mixes languages, code, names, and corrupted text, so a declared English run cannot yet tell what language evidence it actually contains.

One tempting answer is to keep documents containing mostly familiar Latin characters and discard the rest.

The shortcut reaches its first real document and breaks. Spanish and Vietnamese are mistaken for English, transliterated languages disappear, and English code or identifier lists pass despite containing little natural language.

Now the missing job can be stated plainly. Use a calibrated language classifier, retain its confidence and model version, and route uncertain documents to an explicit unknown bucket rather than forcing a label.

## Let one run decide

A field report receives English 0.93, Spanish 0.05, and unknown 0.02. The pipeline keeps English only because its score clears the recorded threshold; a 0.44/0.41 split is quarantined.

## The arithmetic we have earned

d is the document being inspected; the set L contains allowed language labels; p(l|d) is the classifier's support for one label; l-star is the label whose support is largest.

### Why these operations are forced

[Conditional probability](../../MATHEMATICAL_MOVES.md#conditional-bar) asks for language support given this document. [Arg max](../../MATHEMATICAL_MOVES.md#arg-max) keeps the winning label rather than only its score. Summing the scores would erase which language produced them; a threshold is still checked afterward because the winner may be weak.

Only now can we compress the procedure:

$$
\ell^*=\underset{\ell\in\mathcal L}{\mathrm{argmax}}\ p(\ell\mid d)
$$

## What this repair cannot do

Because the classifier learned from finite examples and reduces a mixed document to one distribution, language identification remains probabilistic and domain-sensitive; short, multilingual, and code-heavy documents are especially difficult.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Exact Deduplication — Stop Paying Twice for the Same Document](../179-exact-deduplication/README.md)
