# Excavation 125 — An Open-Ended Research System

[Previous: Excavation 124](../124-adversarial-robustness/README.md)

How can a system keep discovering without silently rewriting its goals or safety boundaries?

The first solution that suggests itself is this: Let it generate experiments, change itself, and deploy improvements automatically.

The idea survives only until we test it against reality: A flawed metric or experiment compounds through self-modification before external review.

The failure gives us a precise requirement: Separate hypothesis generation, sandboxed experiment, independent evaluation, authority, reproducibility, and approved deployment.

## Now work a case you can see

The system proposes a tokenizer change, tests it in isolation, reproduces gains, checks regressions, and submits evidence for human approval.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Open-ended discovery remains bounded by chosen objectives, measurements, and human institutions.

The boundary follows from the mechanism itself. We designed it to separate hypothesis generation, sandboxed experiment, independent evaluation, authority, reproducibility, and approved deployment. That operation solves the failure we had reached, but it contains no step that answers the additional problem above.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

## Next Need

The system can conduct bounded research, but it still needs to turn curiosity into a claim that evidence could defeat.

[Next: Hypotheses](../126-hypothesis-generation/README.md)
