# Excavation 181 — Quality Filtering — Remove Noise Without Defining Humanity Away

Near-deduplication leaves a corpus with more distinct documents, not necessarily better ones. Some are navigation fragments, keyword piles, machine corruption, or adversarial spam.

An obvious shortcut is to keep only documents that resemble one prestigious encyclopedia.

Then the hidden cost becomes visible. The filter removes spam, but it also suppresses informal dialect, local knowledge, code, dialogue, and communities whose writing differs from the chosen reference.

Crossing that boundary requires one additional guarantee. Combine transparent structural signals with small controlled model-based tests, inspect what each threshold removes, and publish source-by-source retention counts before accepting a filter.

## Let one run decide

The station rejects a page with 70 percent repeated navigation and no sentences, but manually audits samples near the threshold and notices that short emergency bulletins need a different rule from essays.

## What this repair cannot do

Every quality filter encodes values and domain assumptions; measured downstream gains do not prove that excluded voices were unimportant.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Data Provenance — Keep the Path Back to Every Source](../182-data-provenance/README.md)
