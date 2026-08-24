# Excavation 184 — Data Mixtures — Decide Which Worlds Receive a Voice

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

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

## Decide Which Worlds Receive a Voice

The station assigns 0.50 to curated web text, 0.20 to science, 0.15 to code, 0.10 to books, and 0.05 to field reports. The five shares exhaust one draw without pretending the sources are equally large or equally important.

## The calculation hidden inside data mixtures

The archivist-engineer carries the data mixtures scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

D counts the named data domains and w_d is the chance that the next training draw chooses domain d. Nonnegative weights prevent negative sampling; a total of one exhausts all possible domain choices.

### Why the melody needs these exact notes

[Summation](../../MATHEMATICAL_MOVES.md#summation) combines mutually exclusive domain shares into the whole probability mass. Multiplication would make one zero-weight domain erase the mixture. [Equality](../../MATHEMATICAL_MOVES.md#equals) requires a complete distribution, while the [inequality](../../MATHEMATICAL_MOVES.md#inequalities) forbids impossible negative shares.

Listen beneath data mixtures: **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Cover the prose about data mixtures and each mark can still be recovered from the case. Only now is the compressed form safe to write:

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
