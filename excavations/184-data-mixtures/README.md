# Excavation 184 — Data Mixtures — Decide Which Worlds Receive a Voice

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

## Decide Which Worlds Receive a Voice

The station assigns 0.50 to curated web text, 0.20 to science, 0.15 to code, 0.10 to books, and 0.05 to field reports. The five shares exhaust one draw without pretending the sources are equally large or equally important.

Hold the setting, evidence, and desired outcome fixed while testing data mixtures. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

## The calculation hidden inside data mixtures

Do not read the coming Data Mixtures line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

D counts the named data domains and w_d is the chance that the next training draw chooses domain d. Nonnegative weights prevent negative sampling; a total of one exhausts all possible domain choices.

### Why no cheaper operation does the same job

[Summation](../../MATHEMATICAL_MOVES.md#summation) combines mutually exclusive domain shares into the whole probability mass. Multiplication would make one zero-weight domain erase the mixture. [Equality](../../MATHEMATICAL_MOVES.md#equals) requires a complete distribution, while the [inequality](../../MATHEMATICAL_MOVES.md#inequalities) forbids impossible negative shares.

Every symbol in Data Mixtures can now be read back into an action already performed. The whole procedure fits in one line:

$$
\sum_{d=1}^{D}w_d=1,\quad w_d\ge 0
$$

## Where data mixtures runs out

Mixture weights redistribute attention but cannot make a poor or missing domain representative, accurate, or safe.

This is where data mixtures runs out for a causal reason. We gave it enough structure to choose and publish a probability weight for each domain, treating the mixture as an explicit modeling decision that must be tested on per-domain validation streams, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

## Take data mixtures to the workbench

A mathematical story about data mixtures earns trust only when the failed and repaired paths can both be reproduced. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running data mixtures, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the data mixtures result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Mixture Sampling — Turn Planned Shares into a Reproducible Stream](../185-mixture-sampling/README.md)
