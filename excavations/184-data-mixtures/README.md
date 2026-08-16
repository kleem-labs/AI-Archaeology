# Excavation 184 — Data Mixtures — Decide Which Worlds Receive a Voice

Redaction reduces one preventable privacy risk. The clean sources still differ enormously in size: web pages could drown out books, code, science, and the station's rare field reports.

One tempting answer is to concatenate every accepted source and let its raw token count determine how often it appears.

The shortcut reaches its first real document and breaks. The largest crawl silently becomes the curriculum. A source ten thousand times smaller may almost never reach a batch even when it carries relationships absent from the web.

Now the missing job can be stated plainly. Choose and publish a probability weight for each domain, treating the mixture as an explicit modeling decision that must be tested on per-domain validation streams.

## Let one run decide

The station assigns 0.50 to curated web text, 0.20 to science, 0.15 to code, 0.10 to books, and 0.05 to field reports. The five shares exhaust one draw without pretending the sources are equally large or equally important.

## The arithmetic we have earned

D counts the named data domains and w_d is the chance that the next training draw chooses domain d. Nonnegative weights prevent negative sampling; a total of one exhausts all possible domain choices.

### Why these operations are forced

[Summation](../../MATHEMATICAL_MOVES.md#summation) combines mutually exclusive domain shares into the whole probability mass. Multiplication would make one zero-weight domain erase the mixture. [Equality](../../MATHEMATICAL_MOVES.md#equals) requires a complete distribution, while the [inequality](../../MATHEMATICAL_MOVES.md#inequalities) forbids impossible negative shares.

Only now can we compress the procedure:

$$
\sum_{d=1}^{D}w_d=1,\quad w_d\ge 0
$$

## What this repair cannot do

Mixture weights redistribute attention but cannot make a poor or missing domain representative, accurate, or safe.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Mixture Sampling — Turn Planned Shares into a Reproducible Stream](../185-mixture-sampling/README.md)
