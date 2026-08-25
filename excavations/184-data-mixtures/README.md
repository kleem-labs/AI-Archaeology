# Excavation 184 — Data Mixtures — Decide Which Worlds Receive a Voice

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Data and pretraining operations

Redaction reduces one preventable privacy risk. The clean sources still differ enormously in size: web pages could drown out books, code, science, and the station's rare field reports.

At the Archive Foundry, the archivist-engineer meets the next case beside the chain-of-custody ledger. The nearest idea is also the most reasonable one: concatenate every accepted source and let its raw token count determine how often it appears.

The attraction of this attempt is easy to see. To concatenate every accepted source and let its raw token count determine how often it appears reuses a rule that already handles the ordinary cases, asks for no machinery whose purpose is still unclear, and produces an answer quickly enough to act on. Economy is a virtue while the rule preserves every distinction the decision needs. The danger is that a short rule can look complete simply because the cases that expose its blindness have not appeared yet.

The easy case appears to confirm the rule. Then a harder observation exposes its limit: the largest crawl silently becomes the curriculum. A source ten thousand times smaller may almost never reach a batch even when it carries relationships absent from the web.

The contradiction matters because it identifies a structural loss in the instruction to concatenate every accepted source and let its raw token count determine how often it appears, not a rare arithmetic accident. Repeating the same procedure more carefully would reproduce the same blindness. More data would help only if the rule had somewhere to keep the distinction that the new evidence reveals. Any genuine repair must therefore change what the method can represent while leaving its successful behavior on the easy cases intact. The chain-of-custody ledger will remain beside both versions so that the added capacity can be traced to the observation that demanded it.

The repair can now be kept narrow. The new method must choose and publish a probability weight for each domain, treating the mixture as an explicit modeling decision that must be tested on per-domain validation streams. This addition answers the counterexample directly; it does not claim to solve every later problem. Everything the earlier rule did honestly can remain, but this missing capacity can no longer be omitted.

A construction that performs this newly earned job is **Data Mixtures**. The name arrives after its responsibility is already visible, and it remains attached to the failure that gave it meaning.

## Decide Which Worlds Receive a Voice

The station assigns 0.50 to curated web text, 0.20 to science, 0.15 to code, 0.10 to books, and 0.05 to field reports. The five shares exhaust one draw without pretending the sources are equally large or equally important.

## The calculation hidden inside data mixtures

The archivist-engineer carries the data mixtures scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

D counts the named data domains and w_d is the chance that the next training draw chooses domain d. Nonnegative weights prevent negative sampling; a total of one exhausts all possible domain choices.

### Why the melody needs these exact notes

[Summation](../../MATHEMATICAL_MOVES.md#summation) combines mutually exclusive domain shares into the whole probability mass. Multiplication would make one zero-weight domain erase the mixture. [Equality](../../MATHEMATICAL_MOVES.md#equals) requires a complete distribution, while the [inequality](../../MATHEMATICAL_MOVES.md#inequalities) forbids impossible negative shares.

Listen beneath data mixtures: **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Every mark in the coming data mixtures equation now belongs to a visible part of the case. The compressed form is:

$$
\sum_{d=1}^{D}w_d=1,\quad w_d\ge 0
$$

## Where data mixtures runs out

Mixture weights redistribute attention but cannot make a poor or missing domain representative, accurate, or safe.

The data mixtures repair holds, but the world asks for something it was never given. At the Archive Foundry, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the chain-of-custody ledger

Rebuild the data mixtures scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Mixture Sampling — Turn Planned Shares into a Reproducible Stream](../185-mixture-sampling/README.md)
